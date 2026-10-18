#!/usr/bin/env python3
"""D6: Theorem D at a rigid slot, R3, M8.15's C1 (DESIGN.md section 8; EXPECTED_V0.md). Case: theoremD:R3.

Usage: d6_theoremD.py [N ...] (default 16 24 32). At each N, and eps in {0.5, 1, 2}, on c = sqrt(eps) v, for a fixed
generic unit v on R3's lowest level (level 2, lam0 = 8), with lam = 8 + eps. On that level |psi|^2 = ||c||^2 at every
point, so this is Theorem B's member with lam = lam0 + |v|^2, and it needs no solve.

Claims, fixed before the run:
  1. Exact at every N: the residual ||F'(c)||, against the size of the terms before they cancel (DESIGN.md section 6), is
     below the acceptance bound 1e-15, and the cubic's part off level 2 is below 1e-14 of the cubic.
  2. The lowest level's spectrum (the Slot Ground States, Theorem D, item 2): among A's eigenvalues with positive
     imaginary part, 2 i omega twice and i (4 omega^2 + 2 eps)^(1/2) once, each to 1e-10 relative, omega = lam^(1/2).
  3. The record: V0 matches EXPECTED_V0.md's C1 row (dimension 6, ranks [1, 0]), with the symmetry leak of the tangents
     T_a c and i c at most 1e-8, and 5 chains, Theorem D's geometric multiplicity; (n(L), n(D), K) = (0, 0, 0): L is
     2 Re(phi^dagger .) phi on the lowest level and positive definite off it, and the phase partner's energy
     Omega(theta, xi) is positive; typed Elliptic; nothing unresolved.
  4. Convergence in N: the type, n(L), K and the three lowest-level eigenvalues are unchanged along the ladder (the
     eigenvalues to 1e-12 relative).
Reported, unscored: the seed checks, Q(v) = 1, criticality, and the symmetry orbit's rank and sigma-radical (4 and 2
at a generic v: the kernel's fifth direction is the rigid family's, Theorem D); and the time per point. Also UA's
bounded criterion for claim 1 (2026-10-16), which UA approved in place of the claim and which is reported here beside
the claim as registered: g_N = ||G_00 - I||_2, the rule's Gram matrix on level 2, and delta_N, the largest
| |psi_v|^2 - 1 | over the nodes, each at most 1e-12; and the on-level residual, ||P0 F'(c)|| / ||P0 cubic(c)||, at
most min(10 (g_N + delta_N + u), 1e-12).
Claim 1 failed at N = 24 and 32 in its first run (DEVLOG 68) through einsum's accumulation in functional.py; UB found
it, d6_gemm_check.py confirmed it on this machine, and the accumulation is now a GEMM. The claim is unchanged.
"""
import json
import os
import sys
import time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import basis, functional as fn, linear as ln, branches as br, devtools  # noqa: E402

CASE = 'theoremD:R3'
devtools.require(CASE)
U = np.finfo(float).eps
EPS = (0.5, 1.0, 2.0)
out, rec_json = [], {}


def say(s):
    print(s, flush=True)
    out.append(s)


def summary(r):
    return dict(type=r['type'], nL=r['nL'], nD=r['nD'], K=r['K'], kr=r['kr'], kc=r['kc'], ki=r['ki'], sdim=r['sdim'],
                ranks=r['jordan_ranks'], blocks=r['blocks'], leak=r['symmetry_leak'], v0_matches=r['v0_matches'],
                margin=r['margin'], cluster_max=r['cluster_max'], outside_min=r['outside_min'], balance=r['balance'],
                unresolved=r['unresolved'], normA=r['normA'])


def main():
    Ns = [int(a) for a in sys.argv[1:]] or [16, 24, 32]
    rows, sha = br.expected_v0(ROOT)
    expected = rows['C1']
    say(f"D6, Theorem D at R3; N = {Ns}; EXPECTED_V0.md SHA-256 {sha}, row C1 {expected}")
    failed = 0
    ladder = {}
    for N in Ns:
        t0 = time.perf_counter()
        B = basis.Basis('R3', N)
        Fn = fn.Functional(B)
        v = br.seed_state('C1', B)
        chk = br.orbit_checks(Fn, v)
        say(f"N = {N}, m = {B.m}: seed Q(v) {chk['Q']:.15f}, criticality {chk['crit']:.1e}, symmetry rank {chk['k']},"
            f" sigma-radical {chk['r']} (setup {time.perf_counter() - t0:.1f} s)")
        low = np.array([n == 2 for n, _, _ in B.index])
        # UA's quantities, unscored: the level-2 Gram matrix and the pointwise |psi_v|^2, over every node
        G0 = np.zeros((int(low.sum()), int(low.sum())), dtype=complex)
        dN = 0.0
        for P, w in Fn.chunks():
            Pl = P[:, :, low].reshape(-1, int(low.sum()))
            G0 = G0 + w * (Pl.conj().T @ Pl)
            dN = max(dN, float(np.abs(np.sum(np.abs(P @ v) ** 2, axis=-1) - 1).max()))
        gN = float(np.linalg.norm(G0 - np.eye(int(low.sum())), 2))
        ua_bound = min(10 * (gN + dN + U), 1e-12)
        say(f"   UA's quantities (unscored): g_N {gN:.1e}, delta_N {dN:.1e}; the on-level bound min(10(g + delta + u), 1e-12)"
            f" = {ua_bound:.1e}")
        for eps in EPS:
            t1 = time.perf_counter()
            c, lam = np.sqrt(eps) * v, 8.0 + eps
            cub = Fn.cubic(c)
            res = np.linalg.norm((Fn.e - lam) * c + cub)
            size = np.linalg.norm(Fn.e * c) + lam * np.linalg.norm(c) + np.linalg.norm(cub)
            off = np.linalg.norm(np.where(low, 0, cub)) / np.linalg.norm(cub)
            ok1 = res / size < 1e-15 and off < 1e-14
            on_level = np.linalg.norm(np.where(low, (Fn.e - lam) * c + cub, 0)) / np.linalg.norm(np.where(low, cub, 0))
            ua_ok = gN <= 1e-12 and dN <= 1e-12 and on_level <= ua_bound
            L = Fn.hess_dense(c, lam)
            A, Bm, W = ln.first_order(L, np.sqrt(lam))
            margin = ln.margin(np.linalg.norm(A, 2), float(np.vdot(c, c).real))
            sym = [np.concatenate([t, np.zeros(2 * B.m)]) for t in br.tangent_vectors(Fn, c)]
            r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=expected)
            omega = np.sqrt(lam)
            lamA = r['lam']
            up = lamA[(r['labels'] == 'imag') & (lamA.imag > 0)]       # as the record types them (UA)
            pred = [2 * omega, 2 * omega, np.sqrt(4 * omega ** 2 + 2 * eps)]
            used, errs = set(), []
            for p in pred:
                d = np.abs(up.imag - p) / p
                for j in np.argsort(d):
                    if j not in used:
                        used.add(j)
                        errs.append(float(d[j]))
                        break
            ok2 = len(errs) == 3 and max(errs) < 1e-10
            ok3 = (r['v0_matches'] and r['blocks'] == 5 and (r['nL'], r['nD'], r['K']) == (0, 0, 0)
                   and r['type'] == 'Elliptic' and not r['unresolved'])
            ok = ok1 and ok2 and ok3
            failed += not ok
            ladder[(N, eps)] = (r['type'], r['nL'], r['K'], sorted(up.imag[list(used)]))
            rec_json[f'N{N}_eps{eps}'] = dict(residual_rel=res / size, off_level=off, lowest_errors=errs, **summary(r),
                                              seconds=time.perf_counter() - t1, ua_gN=gN, ua_deltaN=dN, ua_on_level=on_level,
                                              ua_bound=ua_bound, ua_pass=bool(ua_ok))
            say(f"   eps {eps}: {'PASS' if ok else 'FAIL'}  residual {res / size:.1e} of the size, off level 2 {off:.1e};"
                f" lowest level against Theorem D {max(errs):.1e}; V0 dim {r['sdim']}, ranks {r['jordan_ranks']},"
                f" {r['blocks']} chains, leak {r['symmetry_leak']:.1e}; (n(L), n(D), K) = ({r['nL']}, {r['nD']}, {r['K']});"
                f" {r['type']}, unresolved {r['unresolved']}; margin {margin:.1e}, cluster max {r['cluster_max']:.1e},"
                f" nearest outside {r['outside_min']:.1e}; {time.perf_counter() - t1:.1f} s; UA's criterion (unscored): on-level"
                f" {on_level:.1e} against {ua_bound:.1e}, {'pass' if ua_ok else 'FAIL'}")
    # claim 4: along the ladder
    ok4 = True
    for eps in EPS:
        pts = [ladder[(N, eps)] for N in Ns if (N, eps) in ladder]
        same = all(p[:3] == pts[0][:3] for p in pts)
        spread = max((max(abs(a - b) / b for a, b in zip(p[3], pts[0][3])) for p in pts), default=0.0)
        ok4 &= same and spread < 1e-12
        say(f"4. eps {eps}, along N = {Ns}: type, n(L), K unchanged: {same}; the lowest level's eigenvalues move by at most"
            f" {spread:.1e}")
    failed += not ok4
    say(f"{failed} failed")
    tag = '_'.join(str(n) for n in Ns)
    path = os.path.join(HERE, f'd6_theoremD_N{tag}.out')
    jpath = os.path.join(HERE, f'd6_theoremD_N{tag}.json')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(rec_json, f, indent=1, default=float)
    devtools.log_run(os.path.abspath(__file__), CASE,
                     [f'D6, Theorem D at R3, N = {Ns}: {"PASS" if not failed else "FAIL"}, 4 claims at eps 0.5, 1 and 2.'
                      if not failed else f'D6, N = {Ns}: {failed} failures; see the output.',
                      f'EXPECTED_V0.md SHA-256 {sha} (as logged before the run), row C1 {expected}.',
                      'Tolerances: fixed before the run (the acceptance bound 1e-15 for the residual; 1e-14 off level 2; 1e-10'
                      ' for the lowest level against Theorem D; the record as in DL; 1e-12 along the ladder). The run'
                      ' informed none.'], outputs=(path, jpath))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
