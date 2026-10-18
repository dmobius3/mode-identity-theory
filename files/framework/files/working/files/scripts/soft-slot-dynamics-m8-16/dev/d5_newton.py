#!/usr/bin/env python3
"""D5: Newton on manufactured solutions (DESIGN.md section 8, UB's c2 and c4, UA's caveat). Case: manufactured.

The forcing h = F'_{lam*}(c*) makes a chosen c* exact at lam*, at ||c||^2 = ||c*||^2. It breaks the symmetry, so
c* is isolated; this tests the solver's mechanics only, never the unforced equation's kernel. Slots R4 and R5
(real type, U(1)) and R2 (spinorial, Sp(1)), at N = 12.

Claims, each with a mutation arm that must turn it red:
  1. Unbordered, Newton returns to (c*, lam*) from a perturbed seed, to a residual below 1e-12, quadratically: every
     step from inside the basin (r <= 1e-2) has r(k+1) <= max(10 r(k)^2, 1e-12), at least one above the floor.
  2. Bordered, with the borders an orthonormal basis of the tangents' span at the seed (pivoted QR, full rank at a
     random state) and the perturbation orthogonal to the tangents at c*, Newton returns to (c*, lam*) with the
     multipliers converging to zero.
  3. The pivoted QR reads the isotropy: at a weight vector of the lowest level the tangents' span drops one
     dimension (T_z c is a multiple of i c), from 4 to 3 in U(1) slots and from 6 to 5 in Sp(1) slots.
  4. The acceptance bound is reachable (UB's (d)): R4 at N = 24, at ||c*|| = 2 and 20, unbordered and with no fixed
     stop, is accepted, its floor, unbordered residual and multipliers below 1e-15 relative. The time per evaluation
     is recorded for D7's costs (UB's (e)).
  5. Off the float grid (UB's (c)): forced states on the lowest level of R2 and R4 at N = 12, at eps in {0.01, 0.1,
     0.5, 2, 6, 72}, with h shifted by a generic 1e-9 relative so the exact solution is not a float, are accepted, with
     the floor read against the size of the terms before they cancel, ||e c|| + |lam| ||c|| + ||cubic|| + ||h||. The
     seeds are 1e-4 off in relative norm, and 1e-5 at eps = 0.01 (UB); lam's seed is 1e-4 eps off. The amendment of
     DEVLOG 61: eps = 0.01 (UB) and 0.1 (UA) added, on their own random stream, so the original four reproduce.
Arms: Newton with its step halved (linear convergence) fails the quadratic test; with no fixed stop, its false floor
is refused by the acceptance bound alone (UA, UB); the Jacobian's quartic part scaled by 1 + 1e-3 fails the
quadratic test (UB); under the bordered solve, a perturbation with a tangent component ends off c*, with nonzero
multipliers, and is refused (UA); claim 5's eps = 0.01 floors, read against the size after the terms cancel,
||(e - lam) c|| + ||cubic|| + ||h||, exceed the bound in both slots (UB). Reported beside it, unscored: the eps = 0.1
floors against that size (UA's proposal). Newton's stop is read from the iteration, and acceptance is enforced in
newton.solve (DESIGN.md section 6); every claim's "converged" is that acceptance, with the fixed 1e-12 besides.
"""
import os
import sys
import time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import group2i, basis, functional as fn, newton, devtools  # noqa: E402

devtools.require('manufactured')
rng = np.random.default_rng(20261017)
out = []
N = 12
STOP = 1e-12


def say(s):
    print(s)
    out.append(s)


def rand_c(m, scale=2.0):
    c = rng.normal(size=m) + 1j * rng.normal(size=m)
    return scale * c / np.linalg.norm(c)


def tangents(Fn, c, K):
    T = [fn.to_real(G @ c) for G in fn.right_generators(Fn.B)] + [fn.to_real(1j * c)]
    if Fn.B.slot in group2i.SPINORIAL:
        Jc = K @ c.conj()
        T += [fn.to_real(Jc), fn.to_real(1j * Jc)]
    return T


def quadratic(hist, basin=1e-2, C=10.0, floor=1e-12):
    """Quadratic convergence by its defining inequality: every step from inside the basin (r <= basin) satisfies
    r(k+1) <= max(C r(k)^2, floor), and at least one such step lands above the floor. Returns (ok, the largest
    r(k+1)/r(k)^2 over basin steps above the floor, the number of such steps)."""
    worst, counted = 0.0, 0
    for k in range(len(hist) - 1):
        if hist[k] <= basin:
            if hist[k + 1] > max(C * hist[k] ** 2, floor):
                return False, hist[k + 1] / hist[k] ** 2, counted
            if hist[k + 1] > floor:
                counted += 1
                worst = max(worst, hist[k + 1] / hist[k] ** 2)
    return counted >= 1, worst, counted


def run(slot, arm=False):
    B = basis.Basis(slot, N)
    Fn = fn.Functional(B)
    _, K = fn.fibre_structure_matrix(Fn)
    cs = rand_c(B.m)
    lam_s = B.eig.min() + 2.0
    h = Fn.grad(cs, lam_s)
    ms = float(np.real(np.vdot(cs, cs)))
    rows = {}
    if not arm:
        d = rand_c(B.m, 0.04)
        c, lam, mu, hist, conv, fl = newton.solve(Fn, h, ms, cs + d, lam_s + 0.05, stop=STOP)
        rows['unbordered'] = (conv, np.linalg.norm(c - cs) / np.linalg.norm(cs), abs(lam - lam_s), fl['floor'], quadratic(hist),
                              len(hist), fl['floor_rel'])
    # a perturbation orthogonal to the tangents at c* (arm: with a tangent component)
    Ts = np.column_stack(tangents(Fn, cs, K))
    Q, _, _ = newton.tangent_borders(list(Ts.T))
    draw = fn.to_real(rand_c(B.m, 0.04))
    dperp = draw - Q @ (Q.T @ draw)
    if arm:
        dperp = dperp + np.linalg.norm(dperp) * Q[:, 0]
    x0 = fn.to_real(cs) + dperp
    borders, rank, _ = newton.tangent_borders(tangents(Fn, fn.to_complex(x0), K))
    c, lam, mu, hist, conv, fl = newton.solve(Fn, h, ms, fn.to_complex(x0), lam_s + 0.05, borders=borders, x_slice=x0, stop=STOP)
    rows['bordered'] = (conv, np.linalg.norm(c - cs) / np.linalg.norm(cs), abs(lam - lam_s), fl['floor'], quadratic(hist), len(hist),
                        np.abs(mu).max() if len(mu) else 0.0, rank, fl['floor_rel'], fl['unbordered_rel'], fl['mu_rel'])
    # the isotropy at a weight vector of the lowest level
    n0 = B.levels[0]
    k = 0 if n0 > 0 else 0
    j = [i for i, (n, a, kk) in enumerate(B.index) if n == n0 and a == 0 and kk == k][0]
    cw = np.zeros(B.m, dtype=complex)
    cw[j] = 2.0
    _, rank_w, _ = newton.tangent_borders(tangents(Fn, cw, K))
    rows['weight'] = (rank, rank_w)
    return rows


def main():
    failed = 0
    full = {'R4': 4, 'R5': 4, 'R2': 6}
    for s in ('R4', 'R5', 'R2'):
        r = run(s)
        cu, du, lu, ru, pu, iu, fu = r['unbordered']
        cb, db, lb, rb, pb, ib, mub, rank, fb, ub_, mb_ = r['bordered']
        rank_full, rank_w = r['weight']
        ok1 = cu and du < 1e-12 and lu < 1e-11 and ru < STOP and pu[0]
        ok2 = cb and db < 1e-12 and lb < 1e-11 and rb < STOP and pb[0] and mub < 1e-11 and rank == full[s]
        ok3 = rank_full == full[s] and rank_w == full[s] - 1
        ok = ok1 and ok2 and ok3
        failed += not ok
        say(f"{s}, N = {N}: {'PASS' if ok else 'FAIL'}")
        say(f"   unbordered: converged {cu} in {iu} evaluations, |c - c*|/|c*| {du:.1e}, |lam - lam*| {lu:.1e},"
            f" floor {ru:.1e} ({fu:.1e} relative), quadratic {pu[0]} (largest r(k+1)/r(k)^2 {pu[1]:.2e} over {pu[2]} steps)")
        say(f"   bordered (rank {rank}): converged {cb} in {ib} evaluations, |c - c*|/|c*| {db:.1e}, |lam - lam*| {lb:.1e},"
            f" floor {rb:.1e} ({fb:.1e} relative; unbordered {ub_:.1e}, multipliers {mb_:.1e} relative), quadratic {pb[0]}"
            f" (largest {pb[1]:.2e} over {pb[2]} steps), multipliers {mub:.1e}")
        say(f"   the tangents' rank: {rank_full} at a random state, {rank_w} at a weight vector of level {basis.Basis(s, N).levels[0]}")
    # arm 1: Newton with its step halved converges only linearly, and must fail the quadratic test
    B = basis.Basis('R4', N)
    Fn = fn.Functional(B)
    cs = rand_c(B.m)
    lam_s = B.eig.min() + 2.0
    h = Fn.grad(cs, lam_s)
    _, _, _, hist_d, conv_d, _ = newton.solve(Fn, h, float(np.real(np.vdot(cs, cs))), cs + rand_c(B.m, 0.04), lam_s + 0.05,
                                          stop=STOP, damping=0.5)
    red_d = not quadratic(hist_d)[0]
    say('arms')
    say(f"   arm: Newton with its step halved (R4)                         {'RED' if red_d else 'green (FAIL)'}"
        f"  ({len(hist_d)} evaluations, last residual {hist_d[-1]:.1e})")
    failed += not red_d
    # the same halved step with no fixed stop: only the acceptance bound can refuse its false floor
    _, _, _, hist_f, acc_f, info_f = newton.solve(Fn, h, float(np.real(np.vdot(cs, cs))), cs + rand_c(B.m, 0.04), lam_s + 0.05,
                                                  stop=None, damping=0.5)
    red_f = not acc_f
    say(f"   arm: the halved step's false floor, no fixed stop (R4)        {'RED' if red_f else 'green (FAIL)'}"
        f"  (stopped at {len(hist_f)} of 40 evaluations, floor {info_f['floor']:.1e}, {info_f['floor_rel']:.1e} relative; accepted {acc_f})")
    failed += not red_f
    # arm 2 (UB): the Jacobian's quartic part scaled by 1 + 1e-3; the residual is untouched, so Newton converges
    # only linearly and must fail the quadratic test
    seed2 = cs + rand_c(B.m, 0.04)
    scaled = lambda c, lam: (lambda p: p[0] + (1 + 1e-3) * p[1])(Fn.hess_parts(c, lam))
    _, _, _, hist_j, _, _ = newton.solve(Fn, h, float(np.real(np.vdot(cs, cs))), seed2, lam_s + 0.05, stop=STOP, hess=scaled)
    red_j = not quadratic(hist_j)[0]
    say(f"   arm: the Jacobian's quartic part scaled by 1 + 1e-3 (R4)      {'RED' if red_j else 'green (FAIL)'}"
        f"  (residuals {', '.join(f'{x:.1e}' for x in hist_j[:6])})")
    failed += not red_j
    r = run('R4', arm=True)
    cb, db, lb, rb, pb, ib, mub, rank, fb, ub_, mb_ = r['bordered']
    red = (not (db < 1e-12 and mub < 1e-11)) and not cb
    say(f"   arm: a perturbation with a tangent component, bordered (R4)   {'RED' if red else 'green (FAIL)'}"
        f"  (accepted {cb}, |c - c*|/|c*| {db:.1e}, multipliers {mub:.1e}; relative: floor {fb:.1e}, unbordered {ub_:.1e},"
        f" multipliers {mb_:.1e})")
    failed += not red
    # claim 4 (UB's (d)): the bound is reachable at N = 24, at two amplitudes, on its own random stream
    rng4 = np.random.default_rng(20261020)
    B24 = basis.Basis('R4', 24)
    t0 = time.perf_counter()
    F24 = fn.Functional(B24)
    t_setup = time.perf_counter() - t0
    ok4 = True
    for amp in (2.0, 20.0):
        z = rng4.normal(size=B24.m) + 1j * rng4.normal(size=B24.m)
        cs4 = amp * z / np.linalg.norm(z)
        lam4 = B24.eig.min() + 2.0
        h4 = F24.grad(cs4, lam4)
        z = rng4.normal(size=B24.m) + 1j * rng4.normal(size=B24.m)
        d4 = 0.04 * z / np.linalg.norm(z)
        t0 = time.perf_counter()
        c4, l4, _, hist4, acc4, info4 = newton.solve(F24, h4, float(np.real(np.vdot(cs4, cs4))), cs4 + d4, lam4 + 0.05)
        per = (time.perf_counter() - t0) / len(hist4)
        e4 = np.linalg.norm(c4 - cs4) / np.linalg.norm(cs4)
        good = acc4 and e4 < 1e-12 and abs(l4 - lam4) < 1e-10
        ok4 &= good
        say(f"4. R4, N = 24, m = {B24.m}, ||c*|| = {amp:.0f}: {'PASS' if good else 'FAIL'}  accepted {acc4} in {len(hist4)} evaluations;"
            f" floor {info4['floor']:.1e} ({info4['floor_rel']:.1e} relative), unbordered {info4['unbordered_rel']:.1e};"
            f" |c - c*|/|c*| {e4:.1e}, |lam - lam*| {abs(l4 - lam4):.1e}; {per:.1f} s per evaluation (setup {t_setup:.1f} s)")
    failed += not ok4
    # claim 5 (UB's (c)): lowest-level states off the float grid; and the arm, the cancelled size at eps = 0.01.
    # The original four eps draw from rng5 in their original order; the added two, from rng5b
    rng5, rng5b = np.random.default_rng(20261022), np.random.default_rng(20261023)
    ok5, over_001, at_01 = True, [], []
    for slot in ('R2', 'R4'):
        B5 = basis.Basis(slot, 12)
        F5 = fn.Functional(B5)
        n0 = B5.levels[0]
        lam0 = float(n0 * (n0 + 2))
        low = np.array([n == n0 for n, _, _ in B5.index])
        for eps, rg in [(0.5, rng5), (2.0, rng5), (6.0, rng5), (72.0, rng5), (0.01, rng5b), (0.1, rng5b)]:
            u = np.where(low, rg.normal(size=B5.m) + 1j * rg.normal(size=B5.m), 0)
            u = u / np.linalg.norm(u)
            s5 = np.sqrt(eps / np.linalg.norm(F5.cubic(u)))
            cs5, lam5 = s5 * u, lam0 + eps
            h5 = F5.grad(cs5, lam5)
            g = rg.normal(size=B5.m) + 1j * rg.normal(size=B5.m)
            h5 = h5 + 1e-9 * np.linalg.norm(h5) * g / np.linalg.norm(g)
            d5 = rg.normal(size=B5.m) + 1j * rg.normal(size=B5.m)
            off = 1e-5 if eps == 0.01 else 1e-4
            seed5 = cs5 + off * np.linalg.norm(cs5) * d5 / np.linalg.norm(d5)
            c5, l5, _, hist5, acc5, info5 = newton.solve(F5, h5, float(np.real(np.vdot(cs5, cs5))), seed5, lam5 + 1e-4 * eps)
            old = np.linalg.norm((F5.e - l5) * c5) + np.linalg.norm(F5.cubic(c5)) + np.linalg.norm(h5)
            r_old = info5['floor'] / old
            if eps == 0.01 and r_old > 1e-15:
                over_001.append(slot)
            if eps == 0.1:
                at_01.append(f'{slot} {r_old:.1e}')
            ok5 &= acc5
            say(f"5. {slot}, level {n0}, eps {eps}, off the float grid (seed {off:.0e} off): {'PASS' if acc5 else 'FAIL'}"
                f"  accepted {acc5} in {len(hist5)} evaluations; floor {info5['floor']:.2e}, {info5['floor_rel']:.1e} against"
                f" the size before cancelling, {r_old:.1e} against the cancelled size")
    failed += not ok5
    red5 = over_001 == ['R2', 'R4']
    say(f"   arm: claim 5 at eps = 0.01 against the cancelled size        {'RED' if red5 else 'green (FAIL)'}"
        f"  (over the bound in {over_001 or 'neither slot'})")
    say(f"   unscored, eps = 0.1 against the cancelled size (UA's proposal): {at_01}")
    failed += not red5
    say(f"{failed} failed (claims and arms)")
    path = os.path.join(HERE, 'd5_newton.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'manufactured',
                     [f'D5, manufactured solutions: {"PASS" if not failed else "FAIL"}, 3 claims on R4, R5 and R2, claim 4 at'
                      ' N = 24 and claim 5 off the float grid, 5 arms red. The forced problem tests the solver only, never the'
                      ' unforced kernel (UA).' if not failed else
                      f'D5: {failed} failures; see the output.',
                      'Tolerances: fixed before the run (a residual below 1e-12; acceptance at 1e-15 relative, enforced in'
                      ' newton.solve, for the floor, the unbordered residual and the multipliers, against the size of the terms'
                      ' before they cancel; |c - c*|/|c*| below 1e-12 and'
                      ' |lam - lam*| below 1e-11, 1e-10 at N = 24; quadratic convergence by r(k+1) <= max(10 r(k)^2, 1e-12) from'
                      ' inside the basin r <= 1e-2 (set after two runs, DEVLOG); multipliers below 1e-11; the QR rank cut 1e-10'
                      ' relative). The run informed none.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
