#!/usr/bin/env python3
"""UB's finding on D6's claim 1 (2026-10-16), checked on this machine before functional.py changes. Case: theoremD:R3.
It scores nothing.

UB found that most of the cubic's round-off on the rigid branch is einsum's accumulation over large chunks, and that
claim 1 as registered passes when the cubic is accumulated by GEMM. Here, in D6's own chunk grouping (the default
Functional), on D6's unit seed v and its members c = sqrt(eps) v, lam = 8 + eps, at N = 16, 24, 32 and 40:
  - the level-2 identity of the cubic, ||P0 cubic(v) - v|| (|psi_v|^2 = 1, so cubic(v) = v exactly), and the part off
    level 2, with functional.py's einsum and with a GEMM over the same chunks, P.reshape(-1, m)^H (s psi).reshape(-1);
  - D6's claim 1 quantity, ||F'(c)|| against the size of the terms before they cancel, both ways.
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import basis, functional as fn, branches as br, devtools  # noqa: E402

CASE = 'theoremD:R3'
devtools.require(CASE)
out = []


def say(s):
    print(s, flush=True)
    out.append(s)


def gemm_cubic(Fn, c):
    m = Fn.B.m
    g = np.zeros(m, dtype=complex)
    for P, w in Fn.chunks():
        psi = P @ c
        s = np.sum(np.abs(psi) ** 2, axis=-1)
        g = g + w * (P.reshape(-1, m).conj().T @ (s[:, None] * psi).reshape(-1))
    return g


def main():
    for N in (16, 24, 32, 40):
        B = basis.Basis('R3', N)
        Fn = fn.Functional(B)
        v = br.seed_state('C1', B)
        low = np.array([n == 2 for n, _, _ in B.index])
        ce, cg = Fn.cubic(v), gemm_cubic(Fn, v)
        ide = lambda cb: (float(np.linalg.norm(np.where(low, cb, 0) - v)), float(np.linalg.norm(np.where(low, 0, cb))))
        say(f"N = {N}, m = {B.m}, {Fn.rows} rows per chunk of {Fn.rule.M}, cached {Fn.cached}: the level-2 identity einsum"
            f" {ide(ce)[0]:.1e} (off level 2 {ide(ce)[1]:.1e}), GEMM {ide(cg)[0]:.1e} (off level 2 {ide(cg)[1]:.1e})")
        for eps in (0.5, 1.0, 2.0):
            c, lam = np.sqrt(eps) * v, 8.0 + eps
            r = []
            for cub in (Fn.cubic(c), gemm_cubic(Fn, c)):
                res = np.linalg.norm((Fn.e - lam) * c + cub)
                size = np.linalg.norm(Fn.e * c) + lam * np.linalg.norm(c) + np.linalg.norm(cub)
                r.append(res / size)
            say(f"   eps {eps}: claim 1's residual against the size: einsum {r[0]:.1e}, GEMM {r[1]:.1e}  (the bound: 1e-15)")
    path = os.path.join(HERE, 'd6_gemm_check.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), CASE, ["UB's einsum finding on D6's claim 1, checked before any change to"
                                                        " functional.py; it scores nothing."], outputs=(path,))


if __name__ == '__main__':
    main()
