#!/usr/bin/env python3
"""A diagnostic of D6's claim 1 (DEVLOG, the D6 run at N = 16, 24, 32). Case: theoremD:R3. It scores nothing.

At N = 24 and 32, the residual of Theorem B's exact member, against the size, read 1.4e-15 to 1.5e-14, and D6's own
seed check showed Q(v) off 1 by 9.3e-14 at N = 24 and criticality near 5e-14, where D7's seeds in R4 and R2 read about
1e-16 on the same grids. This run separates the candidates, on D6's unit seed v in R3's level 2, at N = 16, 24, 32:
  - the basis's evaluation: the largest | |psi(x)|^2 - 1 | over the nodes (|psi|^2 = ||v||^2 there exactly);
  - the weights: the sum of the rule's weights, less 1;
  - the summation: Q(v) as sum w |psi|^4 straight from the nodes, against Re<v, cubic(v)>, and the cubic's level-2
    error ||P0 cubic(v) - v|| (Q = 1 exactly) and its part off level 2, each with chunks of whole nodes and of one
    alpha row;
  - the other levels: the same with a basis of level 2 alone on the same rule;
  - the rule's own orthonormality on level 2, ||G - I||.
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import basis, functional as fn, quadrature, branches as br, devtools  # noqa: E402

CASE = 'theoremD:R3'
devtools.require(CASE)
out = []


def say(s):
    print(s, flush=True)
    out.append(s)


def measures(Fn, v, low):
    psi_dev, wsum, q_direct, gram = 0.0, 0.0, 0.0, np.zeros((low.sum(), low.sum()), dtype=complex)
    for P, w in Fn.chunks():
        psi = P @ v
        s = np.sum(np.abs(psi) ** 2, axis=-1)
        psi_dev = max(psi_dev, float(np.abs(s - 1).max()))
        wsum += w * P.shape[0]
        q_direct += w * np.sum(s ** 2)
        Pl = P[:, :, low]
        gram += w * np.einsum('pri,prj->ij', Pl.conj(), Pl)
    cub = Fn.cubic(v)
    return dict(psi=psi_dev, wsum=wsum - 1, q_direct=q_direct - 1, q_cubic=float(np.real(np.vdot(v, cub))) - 1,
                low=float(np.linalg.norm(np.where(low, cub, 0) - v)), off=float(np.linalg.norm(np.where(low, 0, cub))),
                gram=float(np.abs(gram - np.eye(low.sum())).max()))


def main():
    for N in (16, 24, 32):
        rule = quadrature.HopfRule(N)
        B = basis.Basis('R3', N)
        v = br.seed_state('C1', B)
        low = np.array([n == 2 for n, _, _ in B.index])
        B2 = basis.Basis('R3', 2)
        v2 = v[low]
        low2 = np.ones(B2.m, dtype=bool)
        rows = [('all levels, whole nodes', measures(fn.Functional(B, rule, cache_bytes=0, chunk_bytes=2 ** 40), v, low)),
                ('all levels, one-row chunks', measures(fn.Functional(B, rule, cache_bytes=0, chunk_bytes=1), v, low)),
                ('level 2 alone, whole nodes', measures(fn.Functional(B2, rule, cache_bytes=0, chunk_bytes=2 ** 40), v2, low2)),
                ('level 2 alone, one-row chunks', measures(fn.Functional(B2, rule, cache_bytes=0, chunk_bytes=1), v2, low2))]
        say(f"N = {N} (M = {rule.M}, {rule.n_t} t nodes, m = {B.m}):")
        for label, r in rows:
            say(f"   {label:30s} max||psi|^2 - 1| {r['psi']:.1e}; sum w - 1 {r['wsum']:+.1e}; Q - 1: direct {r['q_direct']:+.1e},"
                f" through the cubic {r['q_cubic']:+.1e}; cubic on level 2 {r['low']:.1e}, off it {r['off']:.1e};"
                f" level-2 Gram {r['gram']:.1e}")
    path = os.path.join(HERE, 'd6_diagnose.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), CASE, ["A diagnostic of D6's claim 1 at N = 16, 24, 32; it scores nothing."],
                     outputs=(path,))


if __name__ == '__main__':
    main()
