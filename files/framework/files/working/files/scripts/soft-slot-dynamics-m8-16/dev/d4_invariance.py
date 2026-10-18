#!/usr/bin/env python3
"""D4: the discrete functional's derivatives, invariance and Hessian identities on synthetic states (DESIGN.md
section 8). Case: synthetic. Every slot R1..R8, at N = 12, on random coefficient states (canonical basis).

Claims, each with a mutation arm that must turn it red:
  1. F' and F'' are F's derivatives: central differences agree (relative 1e-8 and 1e-7), the dense real Hessian
     equals the Hessian-vector product (1e-12) and is symmetric (1e-13).
  2. F is invariant: under random right translations, under the phase, and, on the spinorial slots, under
     exp(theta J) with J^2 = -1 (Sp(1)); on the real-type slots under the real structure, an involution.
  3. At non-critical states the identity F''(c)(T c) = T F'(c) holds for every generator T: the three right
     generators, i, and on the spinorial slots J and iJ (relative 1e-12).
  4. The chunked path, which evaluates the basis one alpha row at a time and keeps none of it, agrees with the
     cached whole-node path (UB's b), to round-off of the changed summation order.
Arms: part of the top level dropped (invariance under right translation fails); the factor 2 of the Hessian's
rank-one term flipped in sign (the identity fails).
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import su2, group2i, basis, functional as fn, devtools  # noqa: E402

devtools.require('synthetic')
rng = np.random.default_rng(20261016)
out = []
N = 12


def say(s):
    print(s)
    out.append(s)


def rand_c(m, scale=2.0):
    c = rng.normal(size=m) + 1j * rng.normal(size=m)
    return scale * c / np.linalg.norm(c)


def random_su2():
    q = rng.normal(size=4)
    return su2.quat_to_su2(q / np.linalg.norm(q))


def rel(a, b):
    return np.abs(a - b) / max(np.abs(b), 1e-300)


def claim1(Fn, c, lam):
    m = Fn.B.m
    d = rand_c(m, 1.0)
    eps = 1e-5
    fd = (Fn.energy(c + eps * d, lam) - Fn.energy(c - eps * d, lam)) / (2 * eps)
    g = np.real(np.vdot(Fn.grad(c, lam), d))
    e1 = rel(fd, g)
    fdg = (Fn.grad(c + eps * d, lam) - Fn.grad(c - eps * d, lam)) / (2 * eps)
    hd = Fn.hess_apply(c, lam, d)
    e2 = np.linalg.norm(fdg - hd) / np.linalg.norm(hd)
    H = Fn.hess_dense(c, lam)
    e3 = np.linalg.norm(H @ fn.to_real(d) - fn.to_real(hd)) / np.linalg.norm(hd)
    e4 = np.abs(H - H.T).max() / np.abs(H).max()
    return e1 < 1e-8 and e2 < 1e-7 and e3 < 1e-12 and e4 < 1e-13, (e1, e2, e3, e4)


def claim2(Fn, c, lam, K):
    F0 = Fn.energy(c, lam)
    worst = 0.0
    for _ in range(3):
        worst = max(worst, rel(Fn.energy(fn.right_rotation(Fn.B, random_su2()) @ c, lam), F0))
    worst = max(worst, rel(Fn.energy(np.exp(0.7j) * c, lam), F0))
    Jc = K @ c.conj()
    if Fn.B.slot in group2i.SPINORIAL:
        sq = np.linalg.norm(K @ Jc.conj() + c) / np.linalg.norm(c)          # J^2 = -1
        th = 0.9
        worst = max(worst, rel(Fn.energy(np.cos(th) * c + np.sin(th) * Jc, lam), F0))
    else:
        sq = np.linalg.norm(K @ Jc.conj() - c) / np.linalg.norm(c)          # an involution
        worst = max(worst, rel(Fn.energy(Jc, lam), F0))
    return worst < 1e-13 and sq < 1e-12, (worst, sq)


def claim3(Fn, c, lam, K, hess_apply=None):
    hess_apply = Fn.hess_apply if hess_apply is None else hess_apply
    g = Fn.grad(c, lam)
    gens = [(T @ c, T @ g) for T in fn.right_generators(Fn.B)]
    gens.append((1j * c, 1j * g))
    if Fn.B.slot in group2i.SPINORIAL:
        gens.append((K @ c.conj(), K @ g.conj()))
        gens.append((1j * (K @ c.conj()), 1j * (K @ g.conj())))
    worst = 0.0
    for Tc, Tg in gens:
        worst = max(worst, np.linalg.norm(hess_apply(c, lam, Tc) - Tg) / np.linalg.norm(Tg))
    return worst < 1e-12, (worst, len(gens))


def arm_dropped_level(slot):
    """Drop half of the top level's k indices from one block, and test invariance on that space."""
    B = basis.Basis(slot, N)
    Fn = fn.Functional(B)
    top = B.levels[-1]
    keep = np.ones(B.m, dtype=bool)
    idx = [j for j, (n, i, k) in enumerate(B.index) if n == top and i == 0 and k < (top + 1) // 2]
    keep[idx] = False
    c = rand_c(B.m) * keep
    lam = B.eig.min() + 1.0
    F0 = Fn.energy(c, lam)
    worst = 0.0
    for _ in range(3):
        c2 = (fn.right_rotation(B, random_su2()) @ c) * keep
        worst = max(worst, rel(Fn.energy(c2, lam), F0))
    return worst < 1e-13


def flipped_hess(Fn):
    def h(c, lam, d):
        out = (Fn.e - lam) * d
        for P, w in Fn.chunks():
            psi, dpsi = P @ c, P @ d
            s = np.sum(np.abs(psi) ** 2, axis=-1)
            re = np.real(np.sum(psi.conj() * dpsi, axis=-1))
            v = s[:, None] * dpsi - 2 * re[:, None] * psi
            out = out + w * np.einsum('prj,pr->j', P.conj(), v)
        return out
    return h


def main():
    failed, arms = 0, []
    E = group2i.elements()
    gens = group2i.generators(E)
    for s in group2i.SLOTS:
        B = basis.Basis(s, N, E, gens)
        Fn = fn.Functional(B)
        _, K = fn.fibre_structure_matrix(Fn)
        c = rand_c(B.m)
        lam = B.eig.min() + 1.0
        ok1, w1 = claim1(Fn, c, lam)
        ok2, w2 = claim2(Fn, c, lam, K)
        ok3, w3 = claim3(Fn, c, lam, K)
        ok = ok1 and ok2 and ok3
        failed += not ok
        say(f"{s}, N = {N}, m = {B.m}: {'PASS' if ok else 'FAIL'}  derivatives {w1[0]:.1e} {w1[1]:.1e}, dense vs product"
            f" {w1[2]:.1e}, symmetry {w1[3]:.1e}; invariance {w2[0]:.1e}, J^2 {'= -1' if s in group2i.SPINORIAL else 'involution'}"
            f" {w2[1]:.1e}; identity over {w3[1]} generators {w3[0]:.1e}")
    # claim 4 (UB's b): the chunked path, with the basis evaluated per t node, agrees with the cached one
    worst4 = 0.0
    for s in ('R2', 'R4', 'R5'):
        B = basis.Basis(s, N, E, gens)
        Fc, Fu = fn.Functional(B), fn.Functional(B, cache_bytes=0, chunk_bytes=1)
        assert Fc.cached and Fc.rows == Fc.rule.M and not Fu.cached and Fu.rows == 1
        c = rand_c(B.m)
        lam = B.eig.min() + 1.0
        d = rand_c(B.m, 1.0)
        worst4 = max(worst4, rel(Fu.energy(c, lam), Fc.energy(c, lam)),
                     np.linalg.norm(Fu.grad(c, lam) - Fc.grad(c, lam)) / np.linalg.norm(Fc.grad(c, lam)),
                     np.linalg.norm(Fu.hess_apply(c, lam, d) - Fc.hess_apply(c, lam, d)) / np.linalg.norm(Fc.hess_apply(c, lam, d)),
                     np.abs(Fu.hess_dense(c, lam) - Fc.hess_dense(c, lam)).max() / np.abs(Fc.hess_dense(c, lam)).max())
    ok4 = worst4 < 1e-14
    failed += not ok4
    say(f"4. the chunked path, one alpha row at a time, against the cached whole nodes (R2, R4, R5): {'PASS' if ok4 else 'FAIL'}"
        f"  worst relative difference {worst4:.1e}")
    arms.append(('part of the top level dropped (R5)', not arm_dropped_level('R5')))
    B = basis.Basis('R2', N, E, gens)
    Fn = fn.Functional(B)
    _, K = fn.fibre_structure_matrix(Fn)
    c = rand_c(B.m)
    arms.append(("the Hessian's rank-one term with its sign flipped (R2)",
                 not claim3(Fn, c, B.eig.min() + 1.0, K, hess_apply=flipped_hess(Fn))[0]))
    say('arms')
    for label, red in arms:
        say(f"   arm: {label:55s} {'RED' if red else 'green (FAIL)'}")
    failed += sum(not r for _, r in arms)
    say(f"{failed} failed (claims and arms)")
    path = os.path.join(HERE, 'd4_invariance.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f'D4, invariance and the Hessian identities: {"PASS" if not failed else "FAIL"}, 3 claims on all eight slots and the chunked path,'
                      ' 2 arms red.' if not failed else f'D4: {failed} failures; see the output.',
                      'Tolerances: fixed before the run (1e-8 and 1e-7 relative for the central differences at step 1e-5; 1e-12'
                      ' for the dense Hessian against the product and for the identity; 1e-13 for its symmetry and for'
                      ' invariance; 1e-12 for J^2 and the involution; 1e-14 for chunked against cached). The run informed none.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
