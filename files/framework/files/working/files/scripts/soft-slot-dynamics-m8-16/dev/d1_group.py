#!/usr/bin/env python3
"""D1: the group 2I and the eight slot representations (DESIGN.md section 8). Case: synthetic.

Claims, each with a mutation arm that must turn it red:
  1. 2I is 120 distinct unit quaternions closed under products, with inverses; the Galois map is a bijection of
     2I onto another copy of the group (120 distinct unit quaternions, closed) and multiplicative; the
     deterministic generating pair generates all 120.
  2. Each slot's rho is unitary and a homomorphism on all 120 x 120 pairs; its character equals soft_quartic.py's
     formula; the eight characters are orthonormal; rho(-1) = -I exactly for the spinorial slots R1, R2, R6, R8.
  3. For n = 0..48 the canonical intertwiners (the group average on elementary matrices in a fixed order, with
     Gram-Schmidt) number the character multiplicity, as does the independent nullspace count at the generators,
     each with a clear gap; they satisfy rho(g) A = A pi_n(g) on all 120 elements, are Frobenius-orthonormal, and do
     not move when the group sum runs in the other order; each slot's lowest level is its McKay distance.
Arms: the identity in place of the Galois map (R2 = R1, so orthogonality fails); a non-generating pair (the
nullspace dimension exceeds the multiplicity); pi_2 transposed for R3 (no longer a homomorphism); the elementary
matrices in reversed order (a different valid basis, which the canonical comparison must see).
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import su2, group2i, devtools  # noqa: E402

devtools.require('synthetic')
TOL = 1e-12
NMAX = 48
out = []


def say(s):
    print(s)
    out.append(s)


def claim1(galois=group2i.galois):
    E = group2i.elements()
    norms = np.abs(np.linalg.norm(E, axis=1) - 1).max()
    prods = group2i.qmul(E[:, None, :], E[None, :, :]).reshape(-1, 4)
    idx = group2i.index_of(E, prods)                       # asserts each product is an element
    ok_closure = len(idx) == 14400
    inv_ok = all(np.isclose(group2i.qmul(E[i], E[i] * np.array([1, -1, -1, -1]))[0], 1) for i in range(120))
    G = galois(E)                                        # the image, another copy of the group
    distinct = np.unique(np.round(G, 12), axis=0).shape[0] == 120 and np.abs(np.linalg.norm(G, axis=1) - 1).max() < TOL
    GG = group2i.qmul(G[:, None, :], G[None, :, :]).reshape(-1, 4)
    group2i.index_of(G, GG)                              # asserts the image is closed under products
    bij = distinct
    mult = np.abs(galois(prods) - GG).max()
    g1, g2 = group2i.generators(E)
    gen_ok = len(group2i.closure(E, (g1, g2))) == 120
    ok = norms < TOL and ok_closure and inv_ok and bij and mult < TOL and gen_ok
    return ok, dict(norms=norms, galois_mult=mult, generators=(int(g1), int(g2)), image_is_a_group=bij)


def claim2(rep=group2i.rep):
    E = group2i.elements()
    chars, worst = {}, {}
    ok = True
    minus = group2i.index_of(E, np.array([-1.0, 0, 0, 0]))[0]
    for s in group2i.SLOTS:
        R = rep(s, E)                                      # (120, r, r)
        r = R.shape[-1]
        unit = np.abs(np.einsum('gij,gkj->gik', R, R.conj()) - np.eye(r)).max()
        prods = group2i.qmul(E[:, None, :], E[None, :, :])
        k = group2i.index_of(E, prods.reshape(-1, 4)).reshape(120, 120)
        hom = np.abs(R[k] - np.einsum('aij,bjk->abik', R, R)).max()
        ch = np.trace(R, axis1=1, axis2=2)
        fmatch = np.abs(ch - group2i.chi_formula(s, E)).max()
        spin = np.abs(R[minus] - (-1 if s in group2i.SPINORIAL else 1) * np.eye(r)).max()
        chars[s] = ch
        worst[s] = (unit, hom, fmatch, spin)
        ok &= unit < TOL and hom < 1e-11 and fmatch < 1e-11 and spin < TOL and r == group2i.dim(s)
    gram = np.array([[np.mean(chars[a] * chars[b].conj()).real for b in group2i.SLOTS] for a in group2i.SLOTS])
    orth = np.abs(gram - np.eye(8)).max()
    ok &= orth < 1e-12
    return ok, dict(worst=worst, orth=orth)


def claim3(gens=None, nmax=NMAX, elementary_order_arm=False):
    E = group2i.elements()
    gens = group2i.generators(E) if gens is None else gens
    ok = True
    lowest, gaps, worst_res, worst_orth, worst_order = {}, [], 0.0, 0.0, 0.0
    gs_kept, gs_dropped, arm_diff = [], [], 0.0
    rev = np.arange(len(E))[::-1]
    for s in group2i.SLOTS:
        for n in range(nmax + 1):
            m = group2i.multiplicity(n, s, E)
            Anull, sv = group2i.intertwiner_nullspace(n, s, E, gens)       # the independent count
            A, (kmin, dmax) = group2i.intertwiners(n, s, E)                 # the canonical basis
            if not (len(Anull) == m == len(A)):
                ok = False
            if m and s not in lowest:
                lowest[s] = n
            nz = np.sort(sv)
            if 0 < m < len(nz):
                gaps.append((nz[m - 1], nz[m]))
            if A:
                gs_kept.append(kmin)
                gs_dropped.append(dmax)
                R = group2i.rep(s, E)
                P = su2.pi(n, su2.quat_to_su2(E))
                for a in A:
                    worst_res = max(worst_res, np.abs(np.einsum('gij,jk->gik', R, a) - np.einsum('ij,gjk->gik', a, P)).max())
                Gm = np.array([[np.vdot(a, b) for b in A] for a in A])
                worst_orth = max(worst_orth, np.abs(Gm - np.eye(len(A))).max())
                Arev, _ = group2i.intertwiners(n, s, E, group_order=rev)        # the sum in the other order
                worst_order = max(worst_order, max(np.abs(x - y).max() for x, y in zip(A, Arev)))
                if elementary_order_arm and n <= 20:
                    k = group2i.dim(s) * (n + 1)
                    Aalt, _ = group2i.intertwiners(n, s, E, elementary_order=list(range(k))[::-1])
                    arm_diff = max(arm_diff, max(np.abs(x - y).max() for x, y in zip(A, Aalt)))
    ok &= [lowest.get(s) for s in group2i.SLOTS] == [1, 7, 2, 6, 6, 3, 4, 5]
    ok &= worst_res < 1e-10 and worst_orth < 1e-12 and worst_order < 1e-12
    gap_null = max(g[0] for g in gaps) if gaps else 0.0
    gap_live = min(g[1] for g in gaps) if gaps else 0.0
    ok &= gap_null < 1e-12 and gap_live > 1e-3
    ok &= min(gs_kept) > 1e-6 and max(gs_dropped) < 1e-10          # no first-pass residual within two orders of the 1e-8 cut
    if elementary_order_arm:
        ok &= arm_diff < 1e-6
    return ok, dict(lowest=lowest, worst_res=worst_res, worst_orth=worst_orth, gap_null=gap_null, gap_live=gap_live,
                    gs_kept=min(gs_kept), gs_dropped=max(gs_dropped), worst_order=worst_order, arm_diff=arm_diff)


def main():
    failed, arms = 0, []
    ok, info = claim1()
    say(f"1. 2I and the Galois map: {'PASS' if ok else 'FAIL'}  {info}")
    failed += not ok
    ok, info = claim2()
    say(f"2. the eight representations: {'PASS' if ok else 'FAIL'}  character Gram error {info['orth']:.1e}")
    for s, (u, h, f, sp) in info['worst'].items():
        say(f"   {s}: unitarity {u:.1e}, homomorphism {h:.1e}, character vs soft_quartic {f:.1e}, rho(-1) {sp:.1e}")
    failed += not ok
    ok, info = claim3()
    say(f"3. intertwiners, n = 0..{NMAX}: {'PASS' if ok else 'FAIL'}  lowest levels {info['lowest']}")
    say(f"   canonical basis: residual over all 120 elements {info['worst_res']:.1e}; Frobenius orthonormality"
        f" {info['worst_orth']:.1e}; Gram-Schmidt kept >= {info['gs_kept']:.2e}, dropped <= {info['gs_dropped']:.1e};"
        f" the group sum reversed changes it by {info['worst_order']:.1e}")
    say(f"   the nullspace count at the generators: null <= {info['gap_null']:.1e}, live >= {info['gap_live']:.3f}")
    failed += not ok
    # arms
    E = group2i.elements()
    ok_a, _ = claim2(rep=lambda s, q: group2i.rep('R1', q) if s == 'R2' else group2i.rep(s, q))
    arms.append(('the identity in place of the Galois map (R2 = R1)', not ok_a))
    g1, _ = group2i.generators(E)
    ok_b, _ = claim3(gens=(g1, g1), nmax=12)
    arms.append(('a non-generating pair (one generator twice)', not ok_b))
    ok_c, _ = claim2(rep=lambda s, q: np.swapaxes(group2i.rep('R3', q), -1, -2) if s == 'R3' else group2i.rep(s, q))
    arms.append(('pi_2 transposed for R3', not ok_c))
    ok_d, info_d = claim3(nmax=20, elementary_order_arm=True)
    arms.append(('elementary matrices in reversed order (a different basis)', not ok_d))
    say('arms')
    for label, red in arms:
        say(f"   arm: {label:55s} {'RED' if red else 'green (FAIL)'}")
    failed += sum(not r for _, r in arms)
    say(f"{failed} failed (claims and arms)")
    path = os.path.join(HERE, 'd1_group.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f'D1, the group and its representations: {"PASS" if not failed else "FAIL"}, 3 claims, 4 arms red.'
                      if not failed else f'D1: {failed} failures; see the output.',
                      'Tolerances: fixed before the run (1e-12 for unitarity, Galois and orthonormality; 1e-11 for the'
                      ' homomorphism and the character match; 1e-10 for the intertwining residual; a null singular value'
                      ' below 1e-12 against a live one above 1e-3). The run informed none of them.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
