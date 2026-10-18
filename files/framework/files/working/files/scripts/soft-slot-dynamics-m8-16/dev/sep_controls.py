#!/usr/bin/env python3
"""The separation rule on the controls (SEPARATION_PLAN.md, Step 2; Blake's decision, 2026-10-17). Cases: C2a, C2b, C3.

Usage: sep_controls.py CONTROL --sample | --ladders
  --sample:  D7's sample, eps in {0.5, 1, 2}, at N = 16, 24 and 32, each N continued from the germ at eps = 0.5 as in
             d7_controls.py; the rule read from three cutoffs (UA).
  --ladders: M8.15's ladder from the germ at eps = 0.25 to the window's top, at N = 16 and at N = 24, as in d7_ladders.py's
             base at lower N; the rule read from two cutoffs at every eps, and at the tops, where the next level's mode
             near zero sits (UB).
At each point the solve and the record are D7's (instrument/branches.py, instrument/linear.py at section 7's calibration
and L's cut), and convergence.summarize keeps what the rule needs. Then convergence.separation reads each eps, with the
band edge from the highest basis's levels above the lowest cutoff used. No ladder at N = 32 or 40 runs, and no new control.

Each point's summary, and the basis's level energies, are saved in the JSON, so the rule can be read again without a
solve (UB, 2026-10-17).

Claims, derived before the run:
  --sample: 1. every point accepted, its record as D7 read it (the type, (n(L), n(D), K) and V0 as expected, nothing
    unresolved); 2. the rule reads every eps converged, with the control's type: C2a and C2b Elliptic, C3 Hyperbolic.
    D7's records at these points (DEVLOG 69 to 71) put the slow band's ratio of distance to uncertainty, from the same
    three cutoffs, at 1.7e3 or more (C2a, eps = 0.5, where the floor binds), and the numerical estimate is expected
    far below the floor. Under the set rule (UA, UB, 2026-10-17), C2a's two Krein-positive groups near 4.039 at
    eps = 2, which had no unique match in entry 159, form one set; C2a carries no Krein-negative group, so the set's
    only event is the gray zone, about 4.04 away, and the point converges if the set's uncertainty is under 0.40.
  --ladders: 1. every point accepted; 2. no eps reads converged with a type other than the control's along its window
    (D7's ladders agree with M8.15 at all 121 points). The verdicts, the binding groups, and at the top three points the
    tested group nearest zero, are reported, unscored. Rerun under the set rule (C2a and C2b), the readings that failed
    only on unique matching in entries 162 and 163 may converge; the safety claim is the check on the looser matching.
"""
import json
import os
import sys
import time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import basis, functional as fn, linear as ln, branches as br, convergence as cv, devtools  # noqa: E402
import d7_ladders as d7l  # noqa: E402

TYPE = {'C2a': 'Elliptic', 'C2b': 'Elliptic', 'C3': 'Hyperbolic'}
IDX = {'C2a': (0, 0, 0), 'C2b': (0, 0, 0), 'C3': (6, 3, 3)}
out, rec_json = [], {}


def say(s=''):
    print(s, flush=True)
    out.append(s)


def run_N(name, E, N, targets, expected):
    """The branch at cutoff N through the targets, from the germ; the records and summaries at each."""
    _, slot, _ = br.CASES[name]
    t0 = time.perf_counter()
    B = basis.Basis(slot, N)
    Fn = fn.Functional(B)
    K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
    u = br.seed_state(name, B)
    chk = br.orbit_checks(Fn, u, K)
    Qx = float(E['Q'])
    seed_ok = abs(chk['Q'] - Qx) / Qx < 1e-12 and chk['crit'] < 1e-12 and (chk['k'], chk['r']) == (E['k'], E['r'])
    say(f"{name} N = {N}, m = {B.m}: the seed {'PASS' if seed_ok else 'FAIL'}; setup {time.perf_counter() - t0:.1f} s")
    fails = 0 if seed_ok else 1
    pts = {}
    c_prev, lam_prev, slope, acc = np.sqrt(targets[0] / chk['Q']) * u, E['lam0'] + targets[0], 1 / chk['Q'], False
    for eps in targets:
        t1 = time.perf_counter()
        res = br.continue_to(Fn, E['lam0'], eps, c_prev, lam_prev, slope, K=K, prev_accepted=acc)
        if not res['ok']:
            fails += 1
            say(f"   eps {eps:.4f}: FAIL  {res['reason']}; the ladder at N = {N} ends here")
            break
        c, lam = res['c'], res['lam']
        L = Fn.hess_dense(c, lam)
        A, Bm, W = ln.first_order(L, np.sqrt(lam))
        margin = ln.margin(np.linalg.norm(A, 2), float(np.vdot(c, c).real))
        sym = [np.concatenate([t, np.zeros(2 * B.m)]) for t in br.tangent_vectors(Fn, c, K)]
        r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=expected)
        s = cv.summarize(r, A, W)
        accepted = abs(res['eps'] - eps) <= 1e-6 and all(st['accepted'] for st in res['steps'])
        as_d7 = (r['type'] == TYPE[name] and (r['nL'], r['nD'], r['K']) == IDX[name] and bool(r['v0_matches'])
                 and r['balance'] and not r['unresolved'])
        fails += not accepted
        pts[eps] = dict(sum=s, lam=lam, accepted=accepted, as_d7=as_d7, eig=B.eig)
        rec_json[f'N{N}_eps{eps}'] = dict(eps=res['eps'], lam=lam, m=res['m'], accepted=accepted, record=d7l.summary(r),
                                          seconds=time.perf_counter() - t1, summary=s, eig=sorted(set(B.eig)))
        say(f"   eps {eps:8.4f}: {'accepted' if accepted else 'NOT ACCEPTED'}; {r['type']} ({r['nL']}, {r['nD']}, {r['K']}),"
            f" V0 {'as expected' if r['v0_matches'] else 'MISMATCH'}, unresolved {r['unresolved']}; {len(s['groups'])} typed"
            f" groups; {time.perf_counter() - t1:.0f} s")
        c_prev, lam_prev, slope, acc = c, lam, res['slope'], True
    return pts, fails


def read(name, Ns, runs, eps):
    sums = [runs[N][eps]['sum'] for N in Ns]
    band = cv.band_edge(runs[Ns[-1]][eps]['eig'], Ns[0], runs[Ns[-1]][eps]['lam'])
    return cv.separation(sums, band=band), band


def main():
    name, mode = sys.argv[1], sys.argv[2]
    assert name in TYPE and mode in ('--sample', '--ladders')
    case = br.CASES[name][0]
    devtools.require(case)
    E = d7l.EXPECT[name]
    rows, sha = br.expected_v0(ROOT)
    expected = rows[name]
    if mode == '--sample':
        Ns, targets = [16, 24, 32], [0.5, 1.0, 2.0]
    else:
        Ns, targets = [16, 24], d7l.ladder(0.25, E['eps_max'])
    say(f"The separation rule on {name} ({mode[2:]}): N = {Ns}, eps from {targets[0]:g} to {targets[-1]:g} ({len(targets)}"
        f" points); EXPECTED_V0.md SHA-256 {sha}, row {expected}; factor {cv.FACTOR:g}")
    t0 = time.perf_counter()
    runs, failed = {}, 0
    for N in Ns:
        runs[N], f = run_N(name, E, N, targets, expected)
        failed += f
    common = [e for e in targets if all(e in runs[N] for N in Ns)]
    wrong, verdicts, tops = 0, [], common[-3:]
    for eps in common:
        res, band = read(name, Ns, runs, eps)
        verdicts.append(res['verdict'])
        if res['verdict'] == 'converged' and res['type'] != TYPE[name]:
            wrong += 1
        tested = [r_ for r_ in res['rows'] if 'U' in r_]
        worst = min(tested, key=lambda r_: r_['ratio']) if tested else None
        nums = [r_['num'] for r_ in tested if np.isfinite(r_['num'])]
        line = (f"   eps {eps:8.4f}: {res['verdict']}" + (f" {res['type']}" if res['type'] else '') + f"; band edge {band:.3g};"
                f" {len(res['rows'])} groups read")
        if worst:
            line += (f"; the smallest ratio {worst['ratio']:.3g} at {cv.row_centre(worst):.6g} ({worst['role']} {worst.get('kind', 'group')}, {worst['event']}):"
                     f" U {worst['U']:.2e} (remaining {worst['rem']:.1e}, floor {worst['floor']:.1e}, numerical {worst['num']:.1e}),"
                     f" d {worst['d']:.2e}")
        if nums:
            line += f"; numerical estimates {min(nums):.1e} to {max(nums):.1e}"
        if res['reasons']:
            line += f"; {res['reasons'][:2]}"
        say(line)
        if eps in tops and mode == '--ladders' and tested:
            near = min(tested, key=lambda r_: abs(cv.row_centre(r_)))
            say(f"      the tested group nearest zero: {cv.row_centre(near):.6g} ({near['cls']}, Krein {near['neg']}): U {near['U']:.2e},"
                f" d {near['d']:.2e} ({near['event']}), ratio {near['ratio']:.3g}")
        rec_json[f'rule_eps{eps}'] = dict(verdict=res['verdict'], type=res['type'], band=band, reasons=res['reasons'],
                                          rows=res['rows'])
    if mode == '--sample':
        ok1 = failed == 0 and all(runs[N][e]['as_d7'] for N in Ns for e in common) and len(common) == len(targets)
        ok2 = all(v == 'converged' for v in verdicts) and wrong == 0
        say(f"1. every point accepted, its record as D7 read it: {'PASS' if ok1 else 'FAIL'}")
        say(f"2. the rule converged at every eps, with the type {TYPE[name]}: {'PASS' if ok2 else 'FAIL'}"
            f" ({verdicts.count('converged')} of {len(verdicts)})")
        failed_claims = (not ok1) + (not ok2)
    else:
        ok1 = failed == 0 and len(common) == len(targets)
        ok2 = wrong == 0
        say(f"1. every point accepted: {'PASS' if ok1 else 'FAIL'}")
        say(f"2. no eps converged with a type other than {TYPE[name]}: {'PASS' if ok2 else 'FAIL'}  ({wrong} wrong;"
            f" reported: {verdicts.count('converged')} converged and {verdicts.count('Unresolved')} Unresolved of {len(verdicts)})")
        failed_claims = (not ok1) + (not ok2)
    say(f"{failed_claims} failed; {time.perf_counter() - t0:.0f} s")
    tag = f"{name}_{mode[2:]}"
    path, jpath = os.path.join(HERE, f'sep_controls_{tag}.out'), os.path.join(HERE, f'sep_controls_{tag}.json')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(rec_json, f, indent=1, default=lambda o: float(o) if np.isscalar(o) else str(o))
    devtools.log_run(os.path.abspath(__file__), case,
                     [f"The separation rule on {name} ({mode[2:]}): {'PASS' if not failed_claims else 'FAIL'} ({failed_claims}"
                      f" failed); {verdicts.count('converged')} of {len(verdicts)} eps converged.",
                      f'EXPECTED_V0.md SHA-256 {sha}, row {expected}. Each outcome derived before the run (the script\'s'
                      ' docstring; SEPARATION_PLAN.md).'], outputs=(path, jpath))
    if failed_claims:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
