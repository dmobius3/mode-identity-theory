#!/usr/bin/env python3
"""The facts LADDER_PLAN.md v1 states, read again from source (development, off the instrument: nothing is solved,
and no sealed seed is constructed).

  python3 -I -B dev/ladder_plan_facts.py MIT_REPO

MIT_REPO: a clone of mode-identity-theory with deec830 and 87fc643 in its history. M8.16's files are read through git
at those commits, so the clone's working tree does not matter. M8.16.1's tree is this script's own.

Facts, each of which must hold, or the exit status is 1:
  1. The grid. cases.R5_LADDER is M8.15's grid to 32: 15 points, 0.25 2^(k/2) for k = 0 to 14, the last exactly 32.
     The sample's four points, cases.SAMPLE, are its k = 0, 2, 4 and 6, and C2a/R5 runs at them. T2/R5 and T3/R5
     run along it.
  2. M8.16's split. Its BOUNDARY.md at deec830 has the SHA-256 the terms cite, a54619de..., and holds the ruling,
     amendments 1 to 4, correction 1 and the note to amendments 2 and 3.
  3. The admission. devtools.GO admits C2a/R5 (amendments 3 and 4), so the ladder changes nothing in instrument/.
     No case list in run/ names M8.16's dry ladder, C2a:ladder: cases.ORDER, cases.CASES, build_dry.ORDER and
     DRY.json's order. Its special cases in cases.admission, cases.serialize and driver.run_case are unreachable.
  4. The driver's ladder path. driver.checks_of reads a 'dryladder' case with checks.check_row_k6, against M8.15's
     ladder record. reference/m815/ holds no R5 record, and M8.15's outputs at deec830
     (soft-slot-dynamics/m8_15_solver/out/) hold no branch of C2a in R5.
  5. The environment. record_environment.read() equals M8.16's run/ENVIRONMENT.json at 87fc643 on every field but
     the time it was recorded.
  6. The sample's first point, on record. The plumbing pass's C2a/R5 point at N = 16, eps = 0.25 (DEVLOG.md entry
     15, kept as dev/runs/008_plumbing/) equals the registered run's (87fc643's run/out/C2a_R5.json), field for field
     apart from its two timings. Each file is read against the SHA-256 its RUNLOG.json records.
  7. The rates. 87fc643's C2a/R5, at each N: the seconds per Newton evaluation (a point's time less its record's,
     over its evaluations) and per record, the least and largest over the four points.
  8. R4 on the same grid. M8.16's C2a ladder at deec830, dev/d7_ladders_C2a.json: the evaluations per point at
     N = 24 and 32 over eps = 0.25 to 32; and every one of its 39 points, to 72, Elliptic with (n(L), n(D), K) =
     (0, 0, 0), V0 as expected, 3 chains and nothing unresolved.
  9. K2's reading on the sample, on record. checks.k2, with M8.16.1's serialized C2a/R5, holds at every point of
     87fc643's C2a/R5 at every cutoff: the slow band holds exactly the five predicted pairs, matched by class and
     Krein sign, with nothing in the gray zone. M8.16 never scored K2 at C2a/R5.
Then, unscored: the plan's estimate (INFERRED), fact 7's rates on fact 8's counts.
Arm, which must turn its fact red:
  A1. Fact 6's comparison, with one value of a copy of the registered point moved by one unit in the last place.
"""
import copy
import hashlib
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402
import build_dry  # noqa: E402
import record_environment as env  # noqa: E402

REPO = sys.argv[1]
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
TIMINGS = ('seconds', 'seconds_record')
failed = []
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def fact(n, ok, line):
    say(f'{n}. {"PASS" if ok else "FAIL"}: {line}')
    if not ok:
        failed.append(n)


def show(rev, path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{rev}:{M816}/{path}'], check=True, capture_output=True).stdout


def logged(raw_log, raw, name):
    """raw, the bytes of the file the run log names for case name, against the SHA-256 that log records."""
    files = json.loads(raw_log)['completed'][name]['files']
    return len(files) == 1 and hashlib.sha256(raw).hexdigest() == next(iter(files.values()))


def differences(a, b, path=''):
    """Every place where a and b differ, the point's two timings aside; exact, floats included."""
    if isinstance(a, dict) and isinstance(b, dict):
        keys = (set(a) | set(b)) - (set(TIMINGS) if not path else set())
        return [d for k in sorted(keys) for d in (differences(a[k], b[k], f'{path}/{k}') if k in a and k in b
                                                  else [f'{path}/{k}: on one side only'])]
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f'{path}: lengths {len(a)} and {len(b)}']
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, f'{path}[{i}]')]
    return [] if a == b and type(a) is type(b) else [f'{path}: {a!r} against {b!r}']


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


def nudge(o, path):
    keys = [k for k in path.split('/') if k]
    for k in keys[:-1]:
        o = o[int(k) if isinstance(o, list) else k]
    last = int(keys[-1]) if isinstance(o, list) else keys[-1]
    o[last] = math.nextafter(o[last], math.inf)


def main():
    devtools.require('synthetic')
    say("The facts LADDER_PLAN.md v1 states, read from source; nothing solved.")

    k = list(range(15))
    grid = [0.25 * 2 ** (i / 2) for i in k]
    rows = {n: [p['eps'] for p in cs.CASES[n]['points']] for n in ('T2/R5', 'T3/R5')}
    r5 = [p['eps'] for p in cs.CASES['C2a/R5']['points']]
    fact(1, cs.R5_LADDER == grid and cs.R5_LADDER[-1] == 32.0 and cs.SAMPLE == [grid[i] for i in (0, 2, 4, 6)]
         and r5 == cs.SAMPLE and all(v == grid for v in rows.values()),
         f'{len(cs.R5_LADDER)} points, {cs.R5_LADDER[0]:g} to {cs.R5_LADDER[-1]:g}; the sample {cs.SAMPLE} at k = 0, 2, 4,'
         f' 6; C2a/R5 at {r5}; T2/R5 and T3/R5 along it: {all(v == grid for v in rows.values())}')

    raw = show('deec830', 'BOUNDARY.md')
    h = hashlib.sha256(raw).hexdigest()
    heads = re.findall(r'^## (.+?)(?:,|$)', raw.decode('utf-8'), re.M)
    want = ['The ruling', 'The lists', 'The admission it sits inside', "UA's technical priority", 'Amendment 1',
            'Correction 1 to amendment 1', 'Amendment 2', 'Amendment 3', 'Note to amendments 2 and 3', 'Amendment 4']
    fact(2, h.startswith('a54619de') and heads == want, f'BOUNDARY.md at deec830, SHA-256 {h}; its sections: {heads}')

    with open(os.path.join(ROOT, 'run', 'DRY.json'), encoding='utf-8') as f:
        dry_order = json.load(f)['order']
    lists = dict(ORDER=cs.ORDER, CASES=list(cs.CASES), build_dry=build_dry.ORDER, DRY=dry_order)
    named = {n: 'C2a:ladder' in v for n, v in lists.items()}
    src = {p: open(os.path.join(ROOT, 'run', p), encoding='utf-8').read() for p in ('cases.py', 'driver.py')}
    special = {p: s.count("'C2a:ladder'") for p, s in src.items()}
    fact(3, 'C2a/R5' in devtools.GO and not any(named.values()) and special == {'cases.py': 2, 'driver.py': 1},
         f"'C2a/R5' in devtools.GO: {'C2a/R5' in devtools.GO}; C2a:ladder named in {named}; its special cases"
         f' left in the code: {special}')

    m = re.search(r"    if role == 'dryladder':\n        return ck\.(\w+)\(", src['driver.py'])
    m815 = sorted(os.listdir(os.path.join(ROOT, 'reference', 'm815')))
    tree = subprocess.run(['git', '-C', REPO, 'ls-tree', '--name-only', 'deec830',
                           'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_solver/out/'],
                          check=True, capture_output=True, text=True).stdout.split()
    branches = sorted(os.path.basename(f) for f in tree if os.path.basename(f).startswith('branch_'))
    fact(4, m is not None and m[1] == 'check_row_k6' and not any('R5' in f for f in m815) and bool(branches)
         and not any(f.startswith('branch_C2a_R5') for f in branches),
         f"checks_of's dryladder branch calls {m[1] if m else None}; reference/m815/ holds {m815}; M8.15's branch"
         f" records: {branches}")

    then = json.loads(show('87fc643', 'run/ENVIRONMENT.json'))
    now = env.read()
    diff = sorted(f for f in set(then) | set(now) if then.get(f) != now.get(f))
    fact(5, diff == ['recorded'], f'the fields that differ from 87fc643\'s ENVIRONMENT.json: {diff}')

    reg_raw = show('87fc643', 'run/out/C2a_R5.json')
    reg_ok = logged(show('87fc643', 'run/out/RUNLOG.json'), reg_raw, 'C2a/R5')
    pl = os.path.join(ROOT, 'dev', 'runs', '008_plumbing')
    pl_raw = open(os.path.join(pl, 'C2a_R5.json'), 'rb').read()
    pl_ok = logged(open(os.path.join(pl, 'RUNLOG.json'), 'rb').read(), pl_raw, 'C2a/R5')
    reg, plb = json.loads(reg_raw), json.loads(pl_raw)
    a, b = reg['cutoffs']['16']['points']['0.25'], plb['cutoffs']['16']['points']['0.25']
    d = differences(a, b)
    fact(6, reg_ok and pl_ok and not d and set(a) - set(TIMINGS) == set(b) - set(TIMINGS),
         f'both files equal their logs\' SHA-256: {reg_ok and pl_ok}; {len(set(a) - set(TIMINGS))} fields compared,'
         f' {len(d)} differing' + ''.join(f'\n      {x}' for x in d[:5]))

    rates = {}
    for N, c in reg['cutoffs'].items():
        pts = c['points'].values()
        ev = [(p['seconds'] - p['seconds_record']) / p['evaluations'] for p in pts]
        rc = [p['seconds_record'] for p in pts]
        rates[N] = (min(ev), max(ev), min(rc), max(rc))
    fact(7, sorted(rates) == ['16', '24', '32'] and all(len(c['points']) == 4 for c in reg['cutoffs'].values()),
         'per evaluation and per record, seconds, least to largest: ' + '; '.join(
             f'N = {N}: {r[0]:.1f} to {r[1]:.1f}, {r[2]:.1f} to {r[3]:.1f}' for N, r in rates.items()))

    lad = json.loads(show('deec830', 'dev/d7_ladders_C2a.json'))
    pts = {key: v for key, v in lad.items() if key.startswith('N')}
    counts = {N: [lad[f'N{N}_eps{e!r}']['evaluations'] for e in grid] for N in (24, 32)}
    row_ok = [key for key, v in pts.items() if not (v['ok'] and v['record']['type'] == 'Elliptic'
              and [v['record'][x] for x in ('nL', 'nD', 'K')] == [0, 0, 0] and v['record']['v0_matches']
              and v['record']['blocks'] == 3 and not v['record']['unresolved'])]
    fact(8, len(pts) == 39 and not row_ok and all(len(c) == 15 for c in counts.values()),
         f'{len(pts)} points, {len(row_ok)} off the row; evaluations to 32: ' + '; '.join(
             f'N = {N}: {min(c)} to {max(c)} per point, {sum(c)} in all' for N, c in counts.items()))

    case = json.loads(json.dumps(dr.jsonable(cs.serialize('C2a/R5', cs.CASES['C2a/R5']))))
    k2 = {(N, e): ck.k2(p, case, float(e)) for N, c in reg['cutoffs'].items() for e, p in c['points'].items()}
    slow = {N: sorted({len(ck.computed(p, ck.slow_band(case, float(e)))) for e, p in c['points'].items()})
            for N, c in reg['cutoffs'].items()}
    fact(9, len(k2) == 12 and all(k2.values()),
         f'{sum(k2.values())} of {len(k2)} points; the modes in the slow band, by cutoff: {slow}')

    est = {}
    for N, src_N in (('16', 24), ('24', 24), ('32', 32)):
        lo, hi, rlo, rhi = rates[N]
        n = sum(counts[src_N])
        est[N] = (n * lo + 15 * rlo, n * hi + 15 * rhi)
    tot = (sum(v[0] for v in est.values()), sum(v[1] for v in est.values()))
    say('Estimate (INFERRED, unscored): ' + '; '.join(f'N = {N}: {v[0] / 60:.0f} to {v[1] / 60:.0f} min'
                                                      for N, v in est.items())
        + f'; in all {tot[0] / 3600:.2f} to {tot[1] / 3600:.2f} h, with N = 16 read on N = 24\'s counts')

    say('arm, which must turn its fact red:')
    a2 = copy.deepcopy(a)
    where = first_float(a2)
    nudge(a2, where)
    red = bool(differences(a2, b))
    say(f'   A1. {where} moved by one unit in the last place: {"RED" if red else "GREEN"}')
    n_failed = len(failed) + (not red)
    say(f'{n_failed} failed')
    with open(os.path.join(HERE, 'ladder_plan_facts.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if n_failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
