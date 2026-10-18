#!/usr/bin/env python3
"""D7: C2a, C2b and C3 (DESIGN.md section 8; EXPECTED_V0.md). Cases: C2a, C2b, C3.

Usage: d7_controls.py CONTROL [N ...] [--eps E ...] (default N = 16 24 32 and eps = 0.5 1 2). On each N the branch starts
from the theorem's germ at the first eps, scaled to the leading-order norm, ||c||^2 = eps/Q(u), and continues to each
next eps from the previous accepted point, by Newton in ||c||^2 with a secant to the target eps (within 1e-6) and the
orbit tangents as borders (DESIGN.md section 6; instrument/branches.py).

The expectations, fixed before the run, with their sources:
  - C2a, R4's coherent v_3 (lam0 = 48): Q = 1288/1287; (k, r_u) = (3, 1); the slow pairs +-i eps kappa tau, Krein
    positive, tau = 28/143, 56/429, 140/99, 112/39, 896/1287; signature (0, 0, 10), so Theorem R(c) and B >= 0:
    (n(L), n(D), K) = (0, 0, 0), Elliptic.
  - C2b, R2's v_{7/2} (lam0 = 63): Q = 144/143; (5, 1); tau = 112/143, 168/143, 336/143, 504/143, 560/143, Krein
    positive; (0, 0, 10): (0, 0, 0), Elliptic.
  - C3, R4's octahedron v_2 + v_{-2} (lam0 = 48): Q = 175/143; (4, 4); three real pairs +-eps kappa nu^(1/2),
    nu = 250880/552123; signature (6, 0, 3): n(L) = 6 at small amplitude (B on the slow space has M_u's negative index,
    and the fast part is coercive), K = k_r = 3 (the slow spectrum is the three real pairs, the fast part Krein
    positive), so n(D) = 3 by Theorem K; Hyperbolic.
  Sources: the Soft-Slot Branches §IV (the rows, signatures and slow frequencies) and Theorem R (a) to (c); M8.15's
  m815_common.py (QEXACT, and kappa = 1/(8 lam0^(1/2) Q)); the Hamiltonian-Krein Identification, Theorem K.

Claims:
  1. The seed: Q(u) equals its exact value to 1e-12 relative; u is critical on the lowest level to 1e-12; the tangents'
     rank and sigma-radical are (k, r_u).
  2. Each point: the secant reaches the target eps within 1e-6, with every Newton solve accepted (the enforced bound);
     the record matches EXPECTED_V0.md's row, with the leak of the actual tangents (T_a c, i c, and J c, i J c in R2)
     within the record's bound (RECAL_PLAN.md), and k chains; the type and (n(L), n(D), K) as above; the balance holds; nothing is unresolved.
  3. Theorem R's leading order: the slow nonzero eigenvalues (the record's own typed eigenvalues below 1, outside its
     gray zone; RECAL_PLAN.md) are the expected count and
     class, each slow imaginary group definite and Krein positive (C2a, C2b), or three positive reals (C3); matched in
     order to eps kappa tau (or eps kappa nu^(1/2)), their largest relative deviation is smaller at eps = 0.5 than at
     eps = 2 (the o(1) of Theorem R(a)). The deviations are reported.
  4. Convergence in N: the type, n(L), K and the slow groups' Krein signs are unchanged between the two highest N and
     the same along the ladder. The slow eigenvalues' relative changes between the two highest N are reported,
     unscored: DESIGN.md section 10.2 fixes the fraction from D6 and D7, disclosed.
Reported: the time per Newton evaluation and per point, for the cost of N = 40 (UA, UB).
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import basis, functional as fn, linear as ln, branches as br, devtools  # noqa: E402

U = np.finfo(float).eps
EXPECT = {
    'C2a': dict(lam0=48.0, Q=Fr(1288, 1287), k=3, r=1, kind='i', t=[Fr(28, 143), Fr(56, 429), Fr(140, 99), Fr(112, 39), Fr(896, 1287)],
                idx=(0, 0, 0), type='Elliptic'),
    'C2b': dict(lam0=63.0, Q=Fr(144, 143), k=5, r=1, kind='i', t=[Fr(112, 143), Fr(168, 143), Fr(336, 143), Fr(504, 143), Fr(560, 143)],
                idx=(0, 0, 0), type='Elliptic'),
    'C3': dict(lam0=48.0, Q=Fr(175, 143), k=4, r=4, kind='r', t=[Fr(250880, 552123)] * 3, idx=(6, 3, 3), type='Hyperbolic'),
}
out, rec_json = [], {}


def say(s):
    print(s, flush=True)
    out.append(s)


def summary(r):
    return dict(type=r['type'], nL=r['nL'], nD=r['nD'], K=r['K'], kr=r['kr'], kc=r['kc'], ki=r['ki'], sdim=r['sdim'],
                ranks=r['jordan_ranks'], blocks=r['blocks'], leak=r['symmetry_leak'], v0_matches=r['v0_matches'],
                margin=r['margin'], cluster_max=r['cluster_max'], outside_min=r['outside_min'], balance=r['balance'],
                unresolved=r['unresolved'], normA=r['normA'])


def slow_spectrum(r, kind):
    """The slow eigenvalues as the record itself classifies them (UA): typed, outside the gray zone, below 1."""
    lam, lab = r['lam'], r['labels']
    typed = np.isin(lab, ('real', 'imag', 'complex')) & (np.abs(lam) < 1.0)
    slow = lam[typed]
    if kind == 'i':
        vals = np.sort(lam.imag[typed & (lab == 'imag') & (lam.imag > 0)])
    else:
        vals = np.sort(lam.real[typed & (lab == 'real') & (lam.real > 0)])
    groups = [g for g in r['imag_groups'] if abs(g[0]) < 1.0]
    return vals, groups, len(slow)


def main():
    args = sys.argv[1:]
    name = args[0]
    assert name in EXPECT
    case = br.CASES[name][0]
    devtools.require(case)
    rest = args[1:]
    eps_list = [float(x) for x in rest[rest.index('--eps') + 1:]] if '--eps' in rest else [0.5, 1.0, 2.0]
    Ns = [int(x) for x in (rest[:rest.index('--eps')] if '--eps' in rest else rest)] or [16, 24, 32]
    E = EXPECT[name]
    rows, sha = br.expected_v0(ROOT)
    expected = rows[name]
    _, slot, n0 = br.CASES[name]
    say(f"D7, {name} ({slot}, level {n0}); N = {Ns}, eps = {eps_list}; EXPECTED_V0.md SHA-256 {sha}, row {expected}")
    failed = 0
    ladder = {}
    devs = {}
    for N in Ns:
        t0 = time.perf_counter()
        B = basis.Basis(slot, N)
        Fn = fn.Functional(B)
        K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
        u = br.seed_state(name, B)
        chk = br.orbit_checks(Fn, u, K)
        Qx = float(E['Q'])
        ok1 = abs(chk['Q'] - Qx) / Qx < 1e-12 and chk['crit'] < 1e-12 and (chk['k'], chk['r']) == (E['k'], E['r'])
        failed += not ok1
        setup = time.perf_counter() - t0
        say(f"N = {N}, m = {B.m}: 1. the seed {'PASS' if ok1 else 'FAIL'}  Q(u) {chk['Q']:.15f} against {Qx:.15f},"
            f" criticality {chk['crit']:.1e}, (k, r_u) = ({chk['k']}, {chk['r']}); setup {setup:.1f} s, cached {Fn.cached}")
        kappa = 1 / (8 * np.sqrt(E['lam0']) * Qx)
        c_prev, lam_prev, slope, acc_prev = np.sqrt(eps_list[0] / chk['Q']) * u, E['lam0'] + eps_list[0], 1 / chk['Q'], False
        for eps in eps_list:
            t1 = time.perf_counter()
            res = br.continue_to(Fn, E['lam0'], eps, c_prev, lam_prev, slope, K=K, prev_accepted=acc_prev)
            t_solve = time.perf_counter() - t1
            n_eval = sum(s['evaluations'] for s in res['steps'])
            if not res['ok']:
                failed += 1
                say(f"   eps {eps}: FAIL  {res['reason']}; steps {res['steps']}")
                rec_json[f'N{N}_eps{eps}'] = dict(ok=False, reason=res['reason'], steps=res['steps'])
                break
            c, lam = res['c'], res['lam']
            t2 = time.perf_counter()
            L = Fn.hess_dense(c, lam)
            t_hess = time.perf_counter() - t2
            A, Bm, W = ln.first_order(L, np.sqrt(lam))
            margin = ln.margin(np.linalg.norm(A, 2), float(np.vdot(c, c).real))
            sym = [np.concatenate([t, np.zeros(2 * B.m)]) for t in br.tangent_vectors(Fn, c, K)]
            t3 = time.perf_counter()
            r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=expected)
            t_rec = time.perf_counter() - t3
            ok2 = (abs(res['eps'] - eps) <= 1e-6 and all(s['accepted'] for s in res['steps']) and r['v0_matches']
                   and r['blocks'] == E['k'] and r['type'] == E['type'] and (r['nL'], r['nD'], r['K']) == E['idx']
                   and r['balance'] and not r['unresolved'])
            vals, groups, nslow = slow_spectrum(r, E['kind'])
            pred = np.sort([eps * kappa * (float(t) if E['kind'] == 'i' else np.sqrt(float(t))) for t in E['t']])
            count_ok = len(vals) == len(pred) and nslow == 2 * len(pred)
            krein_ok = (all(g[4] == 'definite' and g[2] == 0 for g in groups) and len(groups) == len(set(np.round(vals, 9))))\
                if E['kind'] == 'i' else (r['kr'] == 3 and not groups)
            dev = (np.abs(vals - pred) / pred).tolist() if count_ok else []
            devs[(N, eps)] = max(dev) if dev else np.inf
            ok3pt = count_ok and krein_ok
            ok = ok2 and ok3pt
            failed += not ok
            ladder[(N, eps)] = dict(type=r['type'], nL=r['nL'], K=r['K'], krein=[g[2] for g in groups], vals=vals.tolist())
            per_eval = t_solve / max(n_eval, 1)
            rec_json[f'N{N}_eps{eps}'] = dict(ok=True, eps=res['eps'], lam=lam, m=res['m'], steps=res['steps'],
                                              evaluations=n_eval, seconds_solve=t_solve, seconds_per_evaluation=per_eval,
                                              seconds_hessian=t_hess, seconds_record=t_rec, slow=vals.tolist(),
                                              predicted=pred.tolist(), deviations=dev,
                                              slow_groups=[(complex(g[0]).imag, g[1], g[2], g[4]) for g in groups], **summary(r))
            say(f"   eps {eps}: 2. {'PASS' if ok2 else 'FAIL'}, 3. slow {'PASS' if ok3pt else 'FAIL'}  reached {res['eps']:.9f} in"
                f" {len(res['steps'])} solves, {n_eval} evaluations, floor {res['info']['floor_rel']:.1e} relative;"
                f" V0 dim {r['sdim']}, ranks {r['jordan_ranks']}, {r['blocks']} chains, leak {r['symmetry_leak']:.1e};"
                f" (n(L), n(D), K) = ({r['nL']}, {r['nD']}, {r['K']}), k_r {r['kr']}; {r['type']}, unresolved {r['unresolved']};"
                f" margin {margin:.1e}, cluster max {r['cluster_max']:.1e}; slow {len(vals)} of {len(pred)} expected,"
                f" Krein {'definite +' if E['kind'] == 'i' and krein_ok else ('three real' if krein_ok else 'MISMATCH')},"
                f" largest deviation from Theorem R {devs[(N, eps)]:.2e}; {per_eval:.1f} s per evaluation, Hessian {t_hess:.1f} s,"
                f" record {t_rec:.1f} s, point {time.perf_counter() - t1:.1f} s")
            c_prev, lam_prev, slope, acc_prev = c, lam, res['slope'], True
    # claim 3: the o(1), at each N
    if 0.5 in eps_list and 2.0 in eps_list:
        for N in Ns:
            if (N, 0.5) in devs and (N, 2.0) in devs:
                ok3 = devs[(N, 0.5)] < devs[(N, 2.0)]
                failed += not ok3
                say(f"3. N = {N}: the largest deviation at eps 0.5, {devs[(N, 0.5)]:.2e}, against eps 2, {devs[(N, 2.0)]:.2e}:"
                    f" {'PASS' if ok3 else 'FAIL'}")
    # claim 4: convergence in N
    if len(Ns) >= 2:
        for eps in eps_list:
            pts = [(N, ladder[(N, eps)]) for N in Ns if (N, eps) in ladder]
            if len(pts) < 2:
                continue
            same = all((p['type'], p['nL'], p['K'], p['krein']) == (pts[0][1]['type'], pts[0][1]['nL'], pts[0][1]['K'],
                                                                     pts[0][1]['krein']) for _, p in pts)
            (Na, a), (Nb, b) = pts[-2], pts[-1]
            change = max((abs(x - y) / abs(y) for x, y in zip(a['vals'], b['vals'])), default=np.nan)
            failed += not same
            say(f"4. eps {eps}: type, n(L), K and the slow Krein signs the same along N = {[N for N, _ in pts]}: {same};"
                f" the slow eigenvalues' largest relative change from N = {Na} to {Nb}: {change:.2e} (unscored)")
    say(f"{failed} failed")
    tag = f"{name}_N{'_'.join(str(n) for n in Ns)}" + ('' if eps_list == [0.5, 1.0, 2.0] else '_eps' + '_'.join(str(e) for e in eps_list))
    path = os.path.join(HERE, f'd7_{tag}.out')
    jpath = os.path.join(HERE, f'd7_{tag}.json')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(rec_json, f, indent=1, default=float)
    devtools.log_run(os.path.abspath(__file__), case,
                     [f'D7, {name}, N = {Ns}, eps = {eps_list}: {"PASS" if not failed else "FAIL"}.' if not failed else
                      f'D7, {name}, N = {Ns}, eps = {eps_list}: {failed} failures; see the output.',
                      f'EXPECTED_V0.md SHA-256 {sha} (as logged before the run), row {expected}.',
                      'Tolerances: fixed before the run (Q to 1e-12, criticality 1e-12; the secant within 1e-6 of the target;'
                      ' acceptance 1e-15 relative, enforced; the record as calibrated in RECAL_PLAN.md; slow eigenvalues as the'
                      ' record types them, below 1). The run informed none, except that the fraction of DESIGN.md section 10.2 is to be fixed from'
                      ' these changes, disclosed.'], outputs=(path, jpath))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
