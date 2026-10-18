#!/usr/bin/env python3
"""D3: the product rule's exactness to degree 4N, against the derived requirement (DESIGN.md section 4).
Case: synthetic.

Claims, each with a mutation arm that must turn it red:
  1. Its two factors, exhaustively, for N in {4, 8, 16, 24, 32, 40, 48}: the uniform angular rule with M = 4N + 1
     gives (1/M) sum e^{ik angle} = delta_{k0} for every |k| <= 4N, and N + 1 Gauss nodes give the moments 1/(j + 1)
     of t^j on [0, 1] for every j <= 2N.
  2. End to end, against the exact integral p! r! / (p + r + 1)! (zero unless p = q and r = s): every monomial
     a^p conj(a)^q b^r conj(b)^s of degree <= 4N for N in {2, 3, 4}; for N in {8, 16, 24, 32, 40}, 2000 random
     monomials of degree <= 4N and the extreme ones of degree exactly 4N.
  3. The bound is sharp: at degree 4N + 1 the angular factor fails on a^(4N+1); the t factor, exact to t-degree
     2N + 1, gives 0 for the squared nodal polynomial of t-degree 2N + 2, whose integral is positive.
  4. On the integrals the instrument will form: for random psi in the soft slots R2, R4 and R5 at N = 8 and 12,
     the integral of |psi|^4 agrees, to round-off, between the rule at N, at N + 3 and at 2N.
Arms: M = 4N angular nodes (aliasing at k = 4N); N Gauss nodes in t (one short).
"""
import itertools
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import group2i, basis, quadrature, devtools  # noqa: E402

devtools.require('synthetic')
rng = np.random.default_rng(20261015)
out = []


def say(s):
    print(s)
    out.append(s)


def claim1(Ns=(4, 8, 16, 24, 32, 40, 48), M_of=lambda N: 4 * N + 1, nt_of=lambda N: N + 1):
    worst_ang, worst_t = 0.0, 0.0
    for N in Ns:
        R = quadrature.HopfRule(N, M=M_of(N), n_t=nt_of(N))
        k = np.arange(-4 * N, 4 * N + 1)
        worst_ang = max(worst_ang, np.abs(R.angular_mean(k) - (k == 0)).max())
        for j in range(2 * N + 1):
            worst_t = max(worst_t, abs(R.t_moment(j) * (j + 1) - 1))
    return worst_ang < 1e-13 and worst_t < 1e-12, (worst_ang, worst_t)


def rel_err(R, p, q, r, s):
    ex = quadrature.exact_monomial(p, q, r, s)
    got = R.monomial(p, q, r, s)
    return abs(got - ex) / (ex if ex else 1.0)


def claim2(M_of=lambda N: 4 * N + 1, nt_of=lambda N: N + 1):
    worst, count = 0.0, 0
    for N in (2, 3, 4):
        R = quadrature.HopfRule(N, M=M_of(N), n_t=nt_of(N))
        for p, q, r, s in itertools.product(range(4 * N + 1), repeat=4):
            if p + q + r + s <= 4 * N:
                worst = max(worst, rel_err(R, p, q, r, s))
                count += 1
    for N in (8, 16, 24, 32, 40):
        R = quadrature.HopfRule(N, M=M_of(N), n_t=nt_of(N))
        D = 4 * N
        extremes = [(D, 0, 0, 0), (0, D, 0, 0), (0, 0, D, 0), (0, 0, 0, D), (2 * N, 2 * N, 0, 0), (0, 0, 2 * N, 2 * N),
                    (N, N, N, N), (2 * N, 0, 0, 2 * N), (D - 1, 1, 0, 0), (D // 2, D // 2 - 1, 0, 1)]
        for _ in range(2000):
            deg = rng.integers(0, D + 1)
            cuts = np.sort(rng.integers(0, deg + 1, size=3))
            extremes.append((cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], deg - cuts[2]))
        for m in extremes:
            worst = max(worst, rel_err(R, *map(int, m)))
            count += 1
    return worst < 1e-12, (worst, count)


def claim3():
    ok = True
    errs = []
    for N in (4, 8, 16, 24):
        R = quadrature.HopfRule(N)
        e1 = rel_err(R, 4 * N + 1, 0, 0, 0)          # exact value 0; the rule aliases at k = M
        # the t factor's witness: the squared nodal polynomial, t-degree 2N + 2, zero at every rule node
        nodal2 = lambda t: np.prod((np.subtract.outer(t, R.t)) ** 2, axis=-1)
        Rx = quadrature.HopfRule(N + 1)              # N + 2 Gauss nodes: exact to t-degree 2N + 3
        true = np.sum(Rx.wt * nodal2(Rx.t))
        got = np.sum(R.wt * nodal2(R.t))
        e2 = abs(got - true) / true
        errs.append((N, e1, e2))
        ok &= e1 > 1e-3 and e2 > 0.5
    return ok, errs


def random_psi(B):
    c = rng.normal(size=B.m) + 1j * rng.normal(size=B.m)
    return c / np.linalg.norm(c)


def quartic(B, c, R):
    total = 0.0
    for g in range(R.n_t):
        F = B.evaluate_at_t_node(R, g)                 # (M, M, r, m)
        psi = F @ c                                    # (M, M, r)
        total += R.node_weight(g) * np.sum(np.sum(np.abs(psi) ** 2, axis=-1) ** 2)
    return total


def claim4():
    E = group2i.elements()
    gens = group2i.generators(E)
    worst, rows = 0.0, []
    for s in ('R2', 'R4', 'R5'):
        for N in (8, 12):
            B = basis.Basis(s, N, E, gens)
            c = random_psi(B)
            vals = [quartic(B, c, quadrature.HopfRule(K)) for K in (N, N + 3, 2 * N)]
            spread = (max(vals) - min(vals)) / abs(vals[0])
            worst = max(worst, spread)
            rows.append((s, N, B.m, vals[0], spread))
    return worst < 1e-13, rows


def main():
    failed, arms = 0, []
    ok, w = claim1()
    say(f"1. the factors, N in 4..48: {'PASS' if ok else 'FAIL'}  angular {w[0]:.1e}, t moments (relative) {w[1]:.1e}")
    failed += not ok
    ok, w = claim2()
    say(f"2. monomials end to end: {'PASS' if ok else 'FAIL'}  worst relative error {w[0]:.1e} over {w[1]} monomials")
    failed += not ok
    ok, w = claim3()
    say(f"3. sharpness at degree 4N + 1: {'PASS' if ok else 'FAIL'}  " +
        '; '.join(f'N={N}: a^(4N+1) {e1:.1e}, nodal^2 {e2:.2f}' for N, e1, e2 in w))
    failed += not ok
    ok, rows = claim4()
    say(f"4. the quartic of random sections, rule at N, N + 3, 2N: {'PASS' if ok else 'FAIL'}")
    for s, N, m, v, spread in rows:
        say(f"   {s}, N = {N}, m = {m}: integral of |psi|^4 = {v:.15f}, relative spread {spread:.1e}")
    failed += not ok
    arms.append(('M = 4N angular nodes', not claim2(M_of=lambda N: 4 * N)[0]))
    arms.append(('N Gauss nodes in t', not claim2(nt_of=lambda N: N)[0]))
    say('arms')
    for label, red in arms:
        say(f"   arm: {label:55s} {'RED' if red else 'green (FAIL)'}")
    failed += sum(not r for _, r in arms)
    say(f"{failed} failed (claims and arms)")
    path = os.path.join(HERE, 'd3_rule.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f'D3, the rule: {"PASS" if not failed else "FAIL"}, 4 claims, 2 arms red. Exactness is shown against the'
                      ' derived degree-4N requirement (the factors exhaustively, monomials end to end, the sharp bound, and the'
                      ' quartic of random soft-slot sections), not by comparison with any other rule.'
                      if not failed else f'D3: {failed} failures; see the output.',
                      'Tolerances: fixed before the run (1e-13 angular, 1e-12 relative for moments and monomials, 1e-13 relative'
                      ' for the quartic spread; sharpness needs errors above 1e-3 (angular) and 0.5 (nodal)). The run informed none.'],
                     outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
