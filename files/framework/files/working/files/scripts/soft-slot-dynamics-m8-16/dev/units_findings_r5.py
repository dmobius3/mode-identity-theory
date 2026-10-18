#!/usr/bin/env python3
"""The units' second-round findings on section 7 and Newton's acceptance (UA, UB, 2026-10-15, night), reproduced on
the package as it stood at DEVLOG 48, before any fix. It records what the package returned against what the units
reported, and logs two entries, one per case.

  UA (case synthetic): L = diag(0, -100000) on one complex dof, omega^2 = 25001, so det(s^2 + s G + L) =
      s^2 (s^2 + 4); one phase chain, whose partner energy is 1 + 4 omega^2/k = -4e-5 exactly. The true indices are
      n(L) = 1, n(D) = 1, K = 0. UA reports n(D) = 0, D's nullity 2, the balance false, and Elliptic, unflagged.
  UB (case manufactured): forced states on the lowest level of R2 and R4 at N = 12, at eps in {0.5, 2, 6, 72}, with h
      shifted by a generic 1e-9 relative, so the exact solution is off the float grid. UB reports that the floor,
      against the size of the terms after they cancel, ||(e - lam) c|| + ||cubic|| + ||h||, exceeds 1e-15 at R2's low
      eps (2.0e-15 at 0.5, 1.0e-15 at 2), and against the size before they cancel, ||e c|| + |lam| ||c|| +
      ||cubic|| + ||h||, lies at 2.3e-18 to 9.5e-17 in all eight.
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import basis, functional as fn, linear as ln, newton, devtools  # noqa: E402

devtools.require('synthetic')
devtools.require('manufactured')
U = np.finfo(float).eps


def part_ua():
    lines = []
    L = np.diag([0.0, -100000.0])
    omega = np.sqrt(25001.0)
    A, B, W = ln.first_order(L, omega)
    margin = 30.0 * np.sqrt(U * np.linalg.norm(A, 2))
    r = ln.record(A, B, W, L, margin)
    ev = np.sort_complex(np.linalg.eigvals(A))
    D = r['V0'].T @ B @ r['V0']
    dev = np.linalg.eigvalsh((D + D.T) / 2)
    ok = (r['nL'] == 1 and r['nD'] == 0 and r['dimkerD'] == 2 and r['blocks'] == 1 and r['K'] == 0
          and not r['balance'] and r['type'] == 'Elliptic' and not r['unresolved'])
    lines.append(f"UA's model: eigenvalues {np.round(ev, 9)}; margin {margin:.1e}; V0 dim {r['sdim']}, ranks {r['jordan_ranks']},"
                 f" blocks {r['blocks']}; D's eigenvalues {[f'{x:+.3e}' for x in dev]} against ||B|| = {np.linalg.norm(B, 2):.3e};"
                 f" n(L) {r['nL']}, n(D) {r['nD']} with {r['dimkerD']} zeros, K {r['K']}, balance {r['balance']}; {r['type']},"
                 f" unresolved {r['unresolved']}: {'reproduced' if ok else 'NOT reproduced'}")
    return ok, lines


def part_ub():
    lines, refused_low, worst_new = [], [], 0.0
    rng = np.random.default_rng(20261021)
    for slot in ('R2', 'R4'):
        B = basis.Basis(slot, 12)
        Fn = fn.Functional(B)
        n0 = B.levels[0]
        lam0 = float(n0 * (n0 + 2))
        low = np.array([n == n0 for n, _, _ in B.index])
        for eps in (0.5, 2.0, 6.0, 72.0):
            u = np.where(low, rng.normal(size=B.m) + 1j * rng.normal(size=B.m), 0)
            u = u / np.linalg.norm(u)
            s = np.sqrt(eps / np.linalg.norm(Fn.cubic(u)))
            cs, lam_s = s * u, lam0 + eps
            h = Fn.grad(cs, lam_s)
            g = rng.normal(size=B.m) + 1j * rng.normal(size=B.m)
            h = h + 1e-9 * np.linalg.norm(h) * g / np.linalg.norm(g)
            d = rng.normal(size=B.m) + 1j * rng.normal(size=B.m)
            seed = cs + 1e-4 * np.linalg.norm(cs) * d / np.linalg.norm(d)
            c, lam, _, hist, acc, info = newton.solve(Fn, h, float(np.real(np.vdot(cs, cs))), seed, lam_s + 1e-4 * eps)
            cub = Fn.cubic(c)
            old = np.linalg.norm((Fn.e - lam) * c) + np.linalg.norm(cub) + np.linalg.norm(h)
            new = np.linalg.norm(Fn.e * c) + abs(lam) * np.linalg.norm(c) + np.linalg.norm(cub) + np.linalg.norm(h)
            r_old, r_new = info['floor'] / old, info['floor'] / new
            worst_new = max(worst_new, r_new)
            if r_old > 1e-15 and eps <= 2.0:
                refused_low.append(f'{slot} at {eps}')
            lines.append(f"UB's float grid: {slot}, level {n0}, eps {eps}: {len(hist)} evaluations, floor {info['floor']:.2e};"
                         f" against the cancelled size {r_old:.1e} (accepted by the package as it stands: {acc});"
                         f" against the size before cancelling {r_new:.1e}")
    ok = bool(refused_low) and worst_new < 1e-15
    lines.append(f"UB's float grid: refused at low eps against the cancelled size: {refused_low or 'none'}; the largest floor"
                 f" against the size before cancelling {worst_new:.1e}: {'reproduced' if ok else 'NOT reproduced'}")
    return ok, lines


def log(case, name, ok, lines, summary):
    for s in lines:
        print(s)
    path = os.path.join(HERE, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    devtools.log_run(os.path.abspath(__file__), case, [summary + (' Reproduced.' if ok else ' NOT reproduced.')
                                                       + ' Nothing is scored; the run records the finding before the fix.'],
                     outputs=(path,))


def main():
    ok, lines = part_ua()
    log('synthetic', 'units_findings_r5_ua.out', ok, lines,
        "UA's index finding, on the package before any fix: L = diag(0, -100000), omega^2 = 25001.")
    ok, lines = part_ub()
    log('manufactured', 'units_findings_r5_ub.out', ok, lines,
        "UB's float-grid finding, on the package before any fix: lowest-level forced states, R2 and R4 at N = 12.")


if __name__ == '__main__':
    main()
