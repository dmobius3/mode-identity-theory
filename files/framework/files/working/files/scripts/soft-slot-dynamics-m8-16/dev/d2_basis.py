#!/usr/bin/env python3
"""D2: the complete-level twisted harmonic basis (DESIGN.md section 8). Case: synthetic.

Claims, each with a mutation arm that must turn it red:
  1. The generators are exact: d pi_n is a Lie algebra map ([dX, dY] = d[X, Y]), four times the Casimir is
     n(n + 2) (sum of d pi_n(G_a)^2 = -n(n + 2) I), and pi_n(exp(theta X)) = exp(theta d pi_n(X)), for n <= 48.
  2. pi_n is a unitary representation at random points of SU(2), for n <= 48.
  3. Each slot's basis at N = 16 is left-equivariant, f(gamma x) = rho(gamma) f(x) on all 120 elements, and
     right-covariant, f_{n,i,k}(x h) = sum_k' pi_n(h)_{k'k} f_{n,i,k'}(x), at random x and h.
  4. Through the rule, the basis is orthonormal at N = 16 for every slot and at N = 24 for the soft slots.
  5. The fibre symmetry preserves each level: for the spinorial slots a quaternionic structure C (C conj(rho) =
     rho C, C conj(C) = -I), for the others a real structure (C conj(C) = +I); C conj(f) lies in the level's span.
Arms: no sqrt(n + 1) normalization (orthonormality fails); intertwiners perturbed by 1e-3 (equivariance fails);
pi_n transposed in the right covariance (right covariance fails).
"""
import os
import sys
import numpy as np
from scipy.linalg import expm
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import su2, group2i, basis, quadrature, devtools  # noqa: E402

devtools.require('synthetic')
rng = np.random.default_rng(20261015)
out = []


def say(s):
    print(s)
    out.append(s)


def random_su2(k):
    q = rng.normal(size=(k, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    return su2.quat_to_su2(q)


def claim1(nmax=48):
    worst = [0.0, 0.0, 0.0]
    G = su2.GENS
    for n in range(nmax + 1):
        d = [su2.gen_matrix(n, X) for X in G]
        for a in range(3):
            for b in range(3):
                C = G[a] @ G[b] - G[b] @ G[a]
                worst[0] = max(worst[0], np.abs(d[a] @ d[b] - d[b] @ d[a] - su2.gen_matrix(n, C)).max())
        cas = sum(x @ x for x in d)
        worst[1] = max(worst[1], np.abs(cas + n * (n + 2) * np.eye(n + 1)).max() / max(1, n * (n + 2)))
        for _ in range(3):
            c = rng.normal(size=3)
            X = sum(ci * Gi for ci, Gi in zip(c, G))
            th = rng.uniform(-2, 2)
            lhs = su2.pi(n, expm(th * X))
            rhs = expm(th * su2.gen_matrix(n, X))
            worst[2] = max(worst[2], np.abs(lhs - rhs).max())
    return worst[0] < 1e-9 and worst[1] < 1e-13 and worst[2] < 1e-10, worst


def claim2(nmax=48, k=20):
    U, V = random_su2(k), random_su2(k)
    worst = [0.0, 0.0]
    for n in range(nmax + 1):
        PU, PV, PUV = su2.pi(n, U), su2.pi(n, V), su2.pi(n, U @ V)
        worst[0] = max(worst[0], np.abs(PUV - PU @ PV).max())
        worst[1] = max(worst[1], np.abs(np.einsum('pij,pkj->pik', PU, PU.conj()) - np.eye(n + 1)).max())
    return worst[0] < 1e-10 and worst[1] < 1e-11, worst


def claim3(B, perturb=False, transpose=False, k=6):
    if perturb:
        for n in B.levels:
            B.A[n] = [A + 1e-3 * rng.normal(size=A.shape) for A in B.A[n]]
    E = B.E
    X = random_su2(k)
    Fx = B.evaluate(X)                                          # (k, r, m)
    gX = su2.quat_to_su2(E)[:, None] @ X[None]                 # (120, k, 2, 2)
    Fg = B.evaluate(gX.reshape(-1, 2, 2)).reshape(120, k, B.r, B.m)
    R = group2i.rep(B.slot, E)
    left = np.abs(Fg - np.einsum('gij,pjm->gpim', R, Fx)).max()
    H = random_su2(k)
    Fxh = B.evaluate(X @ H)
    pred = np.zeros_like(Fxh)
    col = 0
    for n in B.levels:
        Pn = su2.pi(n, H)
        if transpose:
            Pn = np.swapaxes(Pn, -1, -2)
        for _ in B.A[n]:
            blk = Fx[:, :, col:col + n + 1]
            pred[:, :, col:col + n + 1] = np.einsum('prj,pjk->prk', blk, Pn)
            col += n + 1
    right = np.abs(Fxh - pred).max()
    return left < 1e-11 and right < 1e-11, (left, right)


def gram_through_rule(B, rule, normalize=True):
    G = np.zeros((B.m, B.m), dtype=complex)
    scale = np.ones(B.m)
    if not normalize:
        scale = np.array([1 / np.sqrt(n + 1) for n, _, _ in B.index])
    for g in range(rule.n_t):
        F = B.evaluate_at_t_node(rule, g).reshape(-1, B.m) * scale
        G += rule.node_weight(g) * (F.conj().T @ F)
    return np.abs(G - np.eye(B.m)).max()


def fibre_structure(slot, E, gens):
    """C with C conj(rho(g)) = rho(g) C at the generators, C unitary, sign = C conj(C)."""
    r = group2i.dim(slot)
    rows = []
    for g in gens:
        R = group2i.rep(slot, E[g])
        rows.append(np.kron(np.eye(r), R) - np.kron(R.conj().T, np.eye(r)))
    _, s, Vh = np.linalg.svd(np.vstack(rows))
    C = Vh[-1].conj().reshape((r, r)).T
    C = C / np.sqrt(np.abs(np.trace(C @ C.conj().T)) / r)
    return C, (C @ C.conj())[0, 0].real, s[-1]


def claim5(B, rule):
    C, sign, res = fibre_structure(B.slot, B.E, B.gens)
    want = -1 if B.slot in group2i.SPINORIAL else 1
    ok = abs(sign - want) < 1e-12 and res < 1e-12
    # project C conj(f) onto the basis, level by level, through the rule; the residual must vanish
    Gproj = np.zeros((B.m, B.m), dtype=complex)
    norm2 = np.zeros(B.m)
    for g in range(rule.n_t):
        F = B.evaluate_at_t_node(rule, g)                       # (M, M, r, m)
        CF = np.einsum('ij,uvjm->uvim', C, F.conj()).reshape(-1, B.m)
        Ff = F.reshape(-1, B.m)
        w = rule.node_weight(g)
        Gproj += w * (Ff.conj().T @ CF)
        norm2 += w * np.sum(np.abs(CF) ** 2, axis=0)
    captured = np.sum(np.abs(Gproj) ** 2, axis=0)
    leak = np.abs(norm2 - captured).max()
    lv = np.array([n for n, _, _ in B.index])
    cross = max(np.abs(Gproj[lv[:, None] != lv[None, :]]).max(initial=0.0), 0.0)
    ok &= leak < 1e-11 and cross < 1e-11
    return ok, (sign, res, leak, cross)


def main():
    failed, arms = 0, []
    ok, w = claim1()
    say(f"1. generators, n <= 48: {'PASS' if ok else 'FAIL'}  bracket {w[0]:.1e}, Casimir (relative) {w[1]:.1e}, exp {w[2]:.1e}")
    failed += not ok
    ok, w = claim2()
    say(f"2. pi_n a unitary representation, n <= 48: {'PASS' if ok else 'FAIL'}  homomorphism {w[0]:.1e}, unitarity {w[1]:.1e}")
    failed += not ok
    E = group2i.elements()
    gens = group2i.generators(E)
    rule16 = quadrature.HopfRule(16)
    for s in group2i.SLOTS:
        B = basis.Basis(s, 16, E, gens)
        ok3, w3 = claim3(B)
        e16 = gram_through_rule(B, rule16)
        ok5, w5 = claim5(B, rule16)
        ok = ok3 and e16 < 1e-12 and ok5
        say(f"3-5. {s}, N = 16, m = {B.m}: {'PASS' if ok else 'FAIL'}  left {w3[0]:.1e}, right {w3[1]:.1e},"
            f" orthonormality {e16:.1e}; fibre C conj(C) = {w5[0]:+.0f} (residual {w5[1]:.1e}), level leak {w5[2]:.1e}, cross-level {w5[3]:.1e}")
        failed += not ok
    rule24 = quadrature.HopfRule(24)
    for s in ('R2', 'R4', 'R5'):
        B = basis.Basis(s, 24, E, gens)
        e24 = gram_through_rule(B, rule24)
        ok = e24 < 1e-12
        say(f"4. {s}, N = 24, m = {B.m}: {'PASS' if ok else 'FAIL'}  orthonormality through the rule {e24:.1e}")
        failed += not ok
    # arms
    B = basis.Basis('R4', 16, E, gens)
    arms.append(('no sqrt(n + 1) normalization (R4, N = 16)', not (gram_through_rule(B, rule16, normalize=False) < 1e-12)))
    B = basis.Basis('R5', 16, E, gens)
    arms.append(('intertwiners perturbed by 1e-3 (R5, N = 16)', not claim3(B, perturb=True)[0]))
    B = basis.Basis('R2', 16, E, gens)
    arms.append(('pi_n transposed in the right covariance (R2, N = 16)', not claim3(B, transpose=True)[0]))
    say('arms')
    for label, red in arms:
        say(f"   arm: {label:55s} {'RED' if red else 'green (FAIL)'}")
    failed += sum(not r for _, r in arms)
    say(f"{failed} failed (claims and arms)")
    path = os.path.join(HERE, 'd2_basis.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f'D2, the basis: {"PASS" if not failed else "FAIL"}, 5 claims over all eight slots, 3 arms red.'
                      if not failed else f'D2: {failed} failures; see the output.',
                      'Tolerances: fixed before the run (1e-9 for the Lie bracket; 1e-13 relative for the Casimir; 1e-10'
                      ' and 1e-11 for exp and the representation; 1e-11 for equivariance, the fibre leak and the cross-level'
                      ' terms; 1e-12 for orthonormality through the rule and for the fibre structure). The run informed none.'],
                     outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
