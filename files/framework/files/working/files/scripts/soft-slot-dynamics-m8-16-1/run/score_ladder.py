#!/usr/bin/env python3
"""Amendment 5's ladder, scored (BOUNDARY.md, amendment 5; LADDER_PLAN.md v2, The claims). Case: dryrun.

Usage: score_ladder.py MIT_REPO

Read after `driver.py --dry` on the ladder's list (`build_dry.py ladder`). Two inputs, each against the SHA-256 its
run's log records: the ladder's outputs, run/dry/C2a_R5_ladder.json under run/dry/RUNLOG.json; and the registered
run's C2a/R5, run/out/C2a_R5.json under its RUNLOG.json, from MIT_REPO's history at the record's commit, 87fc643. The
case is the one the outputs carry, which must equal build_dry.py's. Every claim is read by checks.py's own functions.
Nothing is solved, and nothing here is scored for qualification.

Claims, derived before the run (LADDER_PLAN.md v2):
  1. Acceptance. At N = 16, 24 and 32 the seed passes, and all 15 points are accepted.
  2. The row. K1 at every point and cutoff; checks.k2 at every point to eps = 2, the sample's range, and reported
     beyond it, unscored; the record Elliptic, (0, 0, 0), with nothing unresolved, at every point and cutoff; and the
     convergence rule converged, Elliptic, at every eps.
  3. The calibration's conditions, as they stand, at every point and cutoff: the cluster coefficient at most
     (kappa/G)/10; L's kernel lift at most 100 u ||L||; L's smallest genuine eigenvalue at least 10 G_L 1000 u ||L||.
  4. K4's bar and trend, as the R5 control reads them: at eps = 0.25 every slow mode within the bar, and the largest
     deviation there below that at eps = 2, at each N. The full K4 along the ladder, which also needs every point
     converged, is reported beside them (UA).
  5. The sample. At eps = 0.25, each N's point equals the registered run's, field for field apart from its two
     timings, and so do the reading and the identity record there. At eps = 0.5, 1 and 2, the record's type, indices,
     V0's dimension and ranks, chains and Krein counts equal the registered run's.
Reported, unscored: the largest deviation from eps kappa s tau; each point's convergence reading, with its smallest
ratio and the band edge; the coefficient, the lift and the smallest genuine eigenvalue; the leak against its bound;
the identity from N = 24 to 32; at 0.5, 1 and 2, the slow eigenvalues' relative differences from the registered run;
the seconds per point and per Newton evaluation; the gate record and the verdict.
Arms, on copies of the outputs. Each must add a failure of its own to its claim, naming the point it mutates, beyond
the claim's failures on the outputs as they are (UA):
  A1. one point's acceptance set false, at N = 32, eps = 32: claim 1.
  A2. one record's type set Hyperbolic, at N = 32, eps = 32: claim 2.
  A3. one point's cluster coefficient set above its bound, at N = 32, eps = 32: claim 3.
  A4. one value of N = 16's point at eps = 0.25 moved by one unit in the last place: claim 5.
"""
import copy
import hashlib
import json
import math
import os
import subprocess
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools, linear as ln  # noqa: E402
import checks as ck  # noqa: E402
import build_dry  # noqa: E402

REPO = sys.argv[1] if len(sys.argv) > 1 else None
RECORD = '87fc643'
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
OUT = os.path.join(HERE, 'dry')
U = np.finfo(float).eps
NS = ('16', '24', '32')
TIMINGS = ('seconds', 'seconds_record')
COEF_MAX, LIFT_MAX, GENUINE_MIN = (ln.KAPPA / ln.GRAY) / 10, 100.0, 10 * ln.G_L * 1000.0
STRUCTURE = ('type', 'nL', 'nD', 'K', 'sdim', 'ranks', 'blocks', 'krein')
lines = []


def say(s=''):
    print(s, flush=True)
    lines.append(s)


def show(path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{RECORD}:{M816}/{path}'], check=True, capture_output=True).stdout


def logged(log, raw, name):
    files = log['completed'][name]['files']
    return len(files) == 1 and hashlib.sha256(raw).hexdigest() == next(iter(files.values()))


def differences(a, b, path=''):
    """Every place where a and b differ, a point's two timings aside; exact, floats included."""
    if isinstance(a, dict) and isinstance(b, dict):
        keys = (set(a) | set(b)) - (set(TIMINGS) if not path else set())
        return [d for k in sorted(keys) for d in (differences(a[k], b[k], f'{path}/{k}') if k in a and k in b
                                                  else [f'{path}/{k}: on one side only'])]
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f'{path}: lengths {len(a)} and {len(b)}']
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, f'{path}[{i}]')]
    return [] if a == b and type(a) is type(b) else [f'{path}: {a!r} against {b!r}']


def point(out, N, eps):
    return out['cutoffs'].get(N, {}).get('points', {}).get(ck.key(eps))


def claim1(out, case):
    bad = []
    for N in NS:
        c = out['cutoffs'].get(N)
        if not (c and c['seed']['ok']):
            bad.append(f'N = {N}: the seed')
            continue
        for p in case['points']:
            q = point(out, N, p['eps'])
            if not (q and q.get('accepted')):
                bad.append(f"N = {N}, eps {p['eps']:g}: {q.get('reason', 'not accepted') if q else 'not reached'}")
    return bad


def claim2(out, case):
    bad, beyond = [], {}
    for N in NS:
        for p in case['points']:
            e, q = p['eps'], point(out, N, p['eps'])
            if not (q and 'record' in q):
                bad.append(f'N = {N}, eps {e:g}: no record')
                continue
            if not ck.k1(q, case):
                bad.append(f'N = {N}, eps {e:g}: K1')
            if e <= 2.0:
                if not ck.k2(q, case, e):
                    bad.append(f'N = {N}, eps {e:g}: K2')
            else:
                beyond[(N, e)] = ck.k2(q, case, e)
            r = q['record']
            if not (r['type'] == 'Elliptic' and [r['nL'], r['nD'], r['K']] == [0, 0, 0] and not r['unresolved']):
                bad.append(f"N = {N}, eps {e:g}: {r['type']}, ({r['nL']}, {r['nD']}, {r['K']}), {r['unresolved']}")
    for p in case['points']:
        if not ck.converged(out, p['eps'], case):
            rd = out['readings'].get(ck.key(p['eps']), {})
            bad.append(f"eps {p['eps']:g}: the rule reads {rd.get('verdict')}, {rd.get('type')}")
    return bad, beyond


def claim3(out, case):
    bad, rows = [], []
    for N in NS:
        for p in case['points']:
            q = point(out, N, p['eps'])
            if not (q and 'lkernel' in q):
                bad.append(f"N = {N}, eps {p['eps']:g}: no reading")
                continue
            coef, lift, gen = q['coefficient'], q['lkernel']['lift'] / U, q['lkernel']['genuine'] / U
            rows.append((N, p['eps'], coef, lift, gen))
            if not (coef <= COEF_MAX and lift <= LIFT_MAX and gen >= GENUINE_MIN):
                bad.append(f"N = {N}, eps {p['eps']:g}: coefficient {coef:.4f}, lift {lift:.1f} u, genuine {gen:.2e} u")
    return bad, rows


def claim5(out, reg):
    bad = []
    for N in NS:
        a, b = point(out, N, 0.25), point(reg, N, 0.25)
        d = differences(a, b) if a and b else ['a point is missing']
        bad += [f'N = {N}, eps 0.25: {x}' for x in d[:3]] + ([f'N = {N}, eps 0.25: {len(d)} differences'] if len(d) > 3 else [])
    for part in ('readings', 'identity'):
        a, b = out[part].get(ck.key(0.25)), reg[part].get(ck.key(0.25))
        d = differences(a, b) if a and b else ['missing']
        bad += [f'eps 0.25, the {part[:-1] if part == "readings" else part}: {x}' for x in d[:3]]
    for e in (0.5, 1.0, 2.0):
        for N in NS:
            a, b = point(out, N, e), point(reg, N, e)
            if not (a and b and 'record' in a and 'record' in b):
                bad.append(f'N = {N}, eps {e:g}: a record is missing')
                continue
            bad += [f"N = {N}, eps {e:g}: {f} {a['record'][f]} against {b['record'][f]}" for f in STRUCTURE
                    if a['record'][f] != b['record'][f]]
    return bad


def slow(q, case, e):
    return sorted(c[2].imag for c in ck.computed(q, ck.slow_band(case, e)) if c[0] == 'imag')


def nudge(o, path):
    keys = [k for k in path.split('/') if k]
    for k in keys[:-1]:
        o = o[int(k) if isinstance(o, list) else k]
    last = int(keys[-1]) if isinstance(o, list) else keys[-1]
    o[last] = math.nextafter(o[last], math.inf)


def first_float(o, path=''):
    if isinstance(o, float):
        return path
    items = o.items() if isinstance(o, dict) else enumerate(o) if isinstance(o, list) else ()
    for k, v in items:
        if not path and k in TIMINGS:
            continue
        p = first_float(v, f'{path}/{k}')
        if p:
            return p
    return None


def main():
    devtools.require('dryrun')
    if not REPO:
        raise SystemExit(__doc__)
    say("Amendment 5's ladder, scored (LADDER_PLAN.md v2), from run/dry/ and MIT 87fc643; nothing solved.")
    log = json.load(open(os.path.join(OUT, 'RUNLOG.json'), encoding='utf-8'))
    raw = open(os.path.join(OUT, 'C2a_R5_ladder.json'), 'rb').read()
    reg_raw = show('run/out/C2a_R5.json')
    ok_in = logged(log, raw, build_dry.LADDER) and logged(json.loads(show('run/out/RUNLOG.json')), reg_raw, 'C2a/R5')
    out, reg = json.loads(raw), json.loads(reg_raw)
    case = out['case']
    want = json.loads(build_dry.build('ladder'))['cases'][build_dry.LADDER]
    same_case = case == want and [p['eps'] for p in case['points']] == [p['eps'] for p in want['points']]
    say(f"   the inputs equal their logs' SHA-256: {ok_in}; the case equals build_dry.py's ladder case: {same_case};"
        f" cutoffs {case['cutoffs']}, {len(case['points'])} points")
    if not (ok_in and same_case and [str(n) for n in case['cutoffs']] == list(NS)):
        say('the inputs do not match their records: nothing is scored')
        raise SystemExit(1)

    b1 = claim1(out, case)
    say(f"1. {'PASS' if not b1 else 'FAIL'}: acceptance, {3 * len(case['points'])} points"
        + ''.join(f'\n      {x}' for x in b1))
    b2, beyond = claim2(out, case)
    say(f"2. {'PASS' if not b2 else 'FAIL'}: the row, K1 and the record at every point, K2 to eps 2, the rule at every eps"
        + ''.join(f'\n      {x}' for x in b2))
    say(f"   K2 beyond eps 2, unscored: {sum(beyond.values())} of {len(beyond)} hold"
        + ''.join(f'; fails at N = {N}, eps {e:g}' for (N, e), v in sorted(beyond.items()) if not v))
    b3, rows3 = claim3(out, case)
    say(f"3. {'PASS' if not b3 else 'FAIL'}: the calibration's conditions" + ''.join(f'\n      {x}' for x in b3))
    if rows3:
        c_ = max(rows3, key=lambda r: r[2])
        l_ = max(rows3, key=lambda r: r[3])
        g_ = min(rows3, key=lambda r: r[4])
        say(f'   the largest coefficient {c_[2]:.4f} (N = {c_[0]}, eps {c_[1]:g}) against {COEF_MAX:.4f}; the largest lift'
            f' {l_[3]:.1f} u (N = {l_[0]}, eps {l_[1]:g}) against {LIFT_MAX:.0f} u; the smallest genuine eigenvalue'
            f' {g_[4]:.2e} u (N = {g_[0]}, eps {g_[1]:g}) against {GENUINE_MIN:.0e} u')
    chk = ck.check_control(out, case)
    ok4 = bool(chk['bar'] and chk['trend'])
    stored = json.loads(json.dumps(out['checks']))
    mine = json.loads(json.dumps({k: (v if not isinstance(v, dict) else {str(n): list(x) for n, x in v.items()})
                                  for k, v in chk.items()}))
    say(f"4. {'PASS' if ok4 else 'FAIL'}: K4's bar and trend, the bar at 0.25 {chk['bar']}, the trend {chk['trend']};"
        f" deviations at 0.25 and 2 by N {json.loads(json.dumps(mine['deviations']))}; the driver's stored checks"
        f" equal these: {stored == mine}")
    say(f"   the full K4 along the ladder, which also needs every point converged, unscored: {chk['K4']}"
        f" (converged {chk['converged']})")
    b5 = claim5(out, reg)
    say(f"5. {'PASS' if not b5 else 'FAIL'}: the sample against the registered run" + ''.join(f'\n      {x}' for x in b5))

    say('reported, unscored:')
    for N in NS:
        for p in case['points']:
            e, q = p['eps'], point(out, N, p['eps'])
            if not (q and 'record' in q):
                continue
            r, rd, ident = q['record'], out['readings'].get(ck.key(e), {}), out['identity'].get(ck.key(e), {})
            tested = [x for x in rd.get('rows', []) if 'ratio' in x]
            lb = ln.leak_bound(r['normA'], r['outside_min'])[0]
            per = (q['seconds'] - q['seconds_record']) / q['evaluations'] if q.get('evaluations') else float('nan')
            say(f"   N = {N}, eps {e:7.4g}: deviation {ck.leading(q, case, e)[1]:.3e}; {rd.get('verdict')} {rd.get('type')},"
                f" smallest ratio {min((x['ratio'] for x in tested), default=float('nan')):.3g}, band {rd.get('band', float('nan')):.3g};"
                f" coefficient {q['coefficient']:.4f}, lift {q['lkernel']['lift'] / U:.1f} u, genuine {q['lkernel']['genuine'] / U:.2e} u;"
                f" leak {r['leak']:.1e} against {lb:.1e}; identity {ident.get('aligned_distance', float('nan')):.2e}"
                f" {ident.get('same_record')}; {q['evaluations']} evaluations, {per:.1f} s each, point {q['seconds']:.1f} s")
    for e in (0.5, 1.0, 2.0):
        for N in NS:
            a, b = point(out, N, e), point(reg, N, e)
            if a and b:
                sa, sb = slow(a, case, e), slow(b, case, e)
                rel = max((abs(x - y) / abs(y) for x, y in zip(sa, sb)), default=float('nan')) if len(sa) == len(sb) else float('nan')
                say(f'   the slow eigenvalues against the registered run, N = {N}, eps {e:g}: largest relative difference {rel:.2e}')
    gate = json.load(open(os.path.join(OUT, 'GATE.json'), encoding='utf-8'))
    v = json.load(open(os.path.join(OUT, 'VERDICT.json'), encoding='utf-8'))
    same = lambda rec: rec and devtools.sha256(os.path.join(OUT, rec['file'])) == rec['sha256']  # noqa: E731
    say(f"   the gate record, as logged {bool(same(log.get('gate')))}: absent {gate['absent']}, complete {gate['complete']};"
        f" the verdict, as logged {bool(same(log.get('verdict')))}: {v['verdict']}")
    say(f"   the case's time {out['seconds']:.0f} s")

    say('arms, each of which must turn its claim red:')
    top = ck.key(case['points'][-1]['eps'])
    o1 = copy.deepcopy(out)
    o1['cutoffs']['32']['points'][top]['accepted'] = False
    o2 = copy.deepcopy(out)
    o2['cutoffs']['32']['points'][top]['record']['type'] = 'Hyperbolic'
    o3 = copy.deepcopy(out)
    o3['cutoffs']['32']['points'][top]['coefficient'] = 2 * COEF_MAX
    o4 = copy.deepcopy(out)
    where = first_float(o4['cutoffs']['16']['points'][ck.key(0.25)])
    nudge(o4['cutoffs']['16']['points'][ck.key(0.25)], where)
    def own(mutated, baseline, mark):
        """The mutation's own failure: one the mutated copy adds to the claim's failures as they are, naming the
        mutated point (UA)."""
        return any(x.startswith(mark) for x in set(mutated) - set(baseline))
    arms = [('A1. acceptance false at N = 32, eps 32', own(claim1(o1, case), b1, 'N = 32, eps 32:')),
            ('A2. a record Hyperbolic at N = 32, eps 32', own(claim2(o2, case)[0], b2, 'N = 32, eps 32: Hyperbolic')),
            ('A3. a coefficient above its bound at N = 32, eps 32',
             own(claim3(o3, case)[0], b3, 'N = 32, eps 32: coefficient')),
            (f'A4. N = 16, eps 0.25: {where} moved by one unit in the last place',
             own(claim5(o4, reg), b5, 'N = 16, eps 0.25:'))]
    for label, red in arms:
        say(f"   {label}: {'RED' if red else 'GREEN'}")
    failed = bool(b1) + bool(b2) + bool(b3) + (not ok4) + bool(b5) + sum(not red for _, red in arms)
    say(f'{failed} failed')
    with open(os.path.join(HERE, 'score_ladder.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
