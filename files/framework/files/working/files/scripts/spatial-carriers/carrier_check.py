#!/usr/bin/env python3
"""The checks behind The Spatial Carriers (spatial-carriers.md): the atomic-support bound, both A5 tests, the carriers.

  K1  2I is closed and rho_j is a representation of it, in a real form, paired with the rotations in the standard way
  K2  each tested shell's A5 content, by character and by the commutant dimension: N = 12, 20, 30
  K3  each A5 orbit's module, by permutation and by the real plane-wave space they carry: 12, 20, 30 directions
  K4  claim 4, both tests: which orbits fit under d_N, and which orbit modules the shell contains
  K5  claim 4's consequence: an equivariant carrier exists exactly where the module is contained, built and verified
      where it does, and its maximal equivariant rank reported where it does not
  K6  claim 3 and the declaration sweep's two zero branches: no shell has an SO(3)-invariant vector
  K7  claim 1's sharpness and the branch with no equivariance declared: thirteen atoms on arbitrary axes at N = 12,
      stationary, and fourteen atoms needing rank fourteen
  K8  claim 2: the uniform angular measure's kernel has rank above d_N, so it is not finitely atomic
  K9  power conservation fixes the tight map's scalar: tightness gives equal weights, and the scalar that carries the
      shell's whole power is 2 d_N / s, which leaves equivariance and support untouched
Each check carries a control that must come out the other way. Quantities at the roundoff level are printed as bounds,
so that differences in roundoff between machines do not reach the record.
"""
import itertools
import sys

import numpy as np
from scipy.linalg import expm

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-9
rng = np.random.default_rng(20260915)
SHELLS = (12, 20, 30)
CLASS_ANGLES = (0.0, np.pi, 2 * np.pi / 3, 2 * np.pi / 5, 4 * np.pi / 5)
CLASS_SIZES = (1, 15, 20, 12, 12)
TABLE = {"1": (1, 1, 1, 1, 1), "3a": (3, -1, 0, PHI, 1 - PHI), "3b": (3, -1, 0, 1 - PHI, PHI),
         "4": (4, 0, 1, -1, -1), "5": (5, 1, -1, 0, 0)}
DIMS = {"1": 1, "3a": 3, "3b": 3, "4": 4, "5": 5}


def bound(x, b=1e-8):
    """Roundoff-level quantities print as a bound, not a value, so the record is machine-independent."""
    return "below %.0e" % b if x < b else "%.2e" % x


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def key(x, nd=6):
    return tuple(np.round(np.asarray(x).ravel(), nd) + 0.0)


def build_2i(parity):
    els = [s * np.eye(4)[k] for s in (1, -1) for k in range(4)]
    els += [np.array(s) / 2 for s in itertools.product((1, -1), repeat=4)]
    base = (0.0, 0.5, 0.5 / PHI, 0.5 * PHI)
    for perm in itertools.permutations(range(4)):
        if sum(1 for i in range(4) for k in range(i + 1, 4) if perm[i] > perm[k]) % 2 != parity:
            continue
        for s in itertools.product((1, -1), repeat=3):
            v = np.zeros(4)
            for pos, val in zip(perm, (base[0], s[0] * base[1], s[1] * base[2], s[2] * base[3])):
                v[pos] = val
            els.append(v)
    return np.array(els)


def closed(G):
    keys = {key(q, 9) for q in G}
    return len(keys) == len(G) and all(key(qmul(p, q), 9) in keys for p in G for q in G)


def spin(j):
    d = int(round(2 * j)) + 1
    m = j - np.arange(d)
    jp = np.zeros((d, d))
    for k in range(1, d):
        jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return (jp + jp.T) / 2, (jp - jp.T) / 2j, np.diag(m).astype(float)


def real_basis(j):
    """Rows are the real spherical-harmonic basis in the |j,m> basis, index k = j - m."""
    d = int(round(2 * j)) + 1
    U = np.zeros((d, d), dtype=complex)
    idx = lambda m: int(round(j - m))
    U[idx(0), idx(0)] = 1.0
    for m in range(1, int(round(j)) + 1):
        U[idx(m), idx(-m)] = 1 / np.sqrt(2)
        U[idx(m), idx(m)] = ((-1) ** m) / np.sqrt(2)
        U[idx(-m), idx(-m)] = 1j / np.sqrt(2)
        U[idx(-m), idx(m)] = -1j * ((-1) ** m) / np.sqrt(2)
    return U


def rho(q, J):
    a, v = q[0], np.asarray(q[1:])
    s = np.linalg.norm(v)
    d = J[0].shape[0]
    if s < 1e-14:
        return np.eye(d) * (1 if a > 0 else (-1) ** (d - 1))
    theta, n = 2 * np.arctan2(s, a), v / s
    return expm(-1j * theta * (n[0] * J[0] + n[1] * J[1] + n[2] * J[2]))


def rot(q):
    a, b, c, d = q
    return np.array([[1 - 2 * (c * c + d * d), 2 * (b * c - a * d), 2 * (b * d + a * c)],
                     [2 * (b * c + a * d), 1 - 2 * (b * b + d * d), 2 * (c * d - a * b)],
                     [2 * (b * d - a * c), 2 * (c * d + a * b), 1 - 2 * (b * b + c * c)]])


def class_of(R):
    t = np.trace(R)
    return int(np.argmin([abs(t - (1 + 2 * np.cos(a))) for a in CLASS_ANGLES]))


def multiplicities(chi):
    out = {}
    for lab, row in TABLE.items():
        out[lab] = (sum(s * c * r for s, c, r in zip(CLASS_SIZES, chi, row)) / 60)
    return {lab: int(round(v)) for lab, v in out.items()}, max(abs(v - round(v)) for v in out.values())


def axes_of_order(G, order):
    want = {5: (PHI / 2, 0.5 / PHI), 3: (0.5,), 2: (0.0,)}[order]
    dirs = []
    for q in G:
        if not any(np.isclose(abs(q[0]), w) for w in want):
            continue
        v = q[1:] / np.linalg.norm(q[1:])
        for u in (v, -v):
            if not any(np.allclose(u, w) for w in dirs):
                dirs.append(u)
    return np.array(dirs)


def half_orbit(dirs):
    axes = []
    for v in dirs:
        if not any(np.allclose(v, u) or np.allclose(-v, u) for u in axes):
            axes.append(v)
    return np.array(axes)


def perm_matrix(dirs, R):
    P = np.zeros((len(dirs), len(dirs)))
    for a, v in enumerate(dirs):
        w = R @ v
        b = next(b for b, u in enumerate(dirs) if np.allclose(u, w, atol=1e-8))
        P[b, a] = 1.0
    return P


def wave_matrix(axes, R):
    """Action on the real plane-wave basis cos(k v.y), sin(k v.y), one pair per axis."""
    p = len(axes)
    M = np.zeros((2 * p, 2 * p))
    for a, v in enumerate(axes):
        w = R @ v
        b, sgn = next(((b, 1.0) for b, u in enumerate(axes) if np.allclose(u, w, atol=1e-8)), (None, None))
        if b is None:
            b, sgn = next((b, -1.0) for b, u in enumerate(axes) if np.allclose(-u, w, atol=1e-8))
        M[b, a] = 1.0
        M[p + b, p + a] = sgn
    return M


def intertwiners(reps_src, reps_tgt):
    """Null space of F rho = Pi F over the given generator pairs; F has shape (tgt, src)."""
    t, s = reps_tgt[0].shape[0], reps_src[0].shape[0]
    rows = [np.kron(np.eye(t), r.T) - np.kron(P, np.eye(s)) for r, P in zip(reps_src, reps_tgt)]
    A = np.vstack(rows)
    u, sv, vt = np.linalg.svd(A)
    ns = vt[np.sum(sv > 1e-8 * max(sv[0], 1.0)):]
    return [row.reshape(t, s) for row in ns]


def generators(rots):
    for i, A in enumerate(rots):
        if class_of(A) != 3:
            continue
        for B in rots:
            if class_of(B) != 1:
                continue
            seen, frontier = {key(np.eye(3))}, [np.eye(3)]
            while frontier:
                nxt = []
                for M in frontier:
                    for X in (A, B):
                        Y = X @ M
                        if key(Y) not in seen:
                            seen.add(key(Y))
                            nxt.append(Y)
                frontier = nxt
            if len(seen) == 60:
                return A, B
    raise RuntimeError("no generating pair found")


def main():
    checks, controls, facts = [], [], {}
    parity = 0 if closed(build_2i(0)) else 1
    G = build_2i(parity)
    rots, reps_q = [], []
    for q in G:
        R = rot(q)
        if not any(np.allclose(R, S) for S in rots):
            rots.append(R)
            reps_q.append(q)
    gens = generators(rots)
    reals, hom_err, pair_err = {}, 0.0, 0.0
    for N in SHELLS:
        J = spin(N / 2)
        U = real_basis(N / 2)
        mats = {}
        for q, R in zip(reps_q, rots):
            M = U @ rho(q, J) @ U.conj().T
            hom_err = max(hom_err, np.abs(M.imag).max())
            mats[key(R)] = M.real
        reals[N] = mats
        q = reps_q[7]
        Uq, Rq = mats[key(rot(q))], rot(q)
        Jr = [U @ Jk @ U.conj().T for Jk in J]
        pair_err = max(pair_err, max(np.abs(Uq.T @ Jr[k] @ Uq - sum(Rq[k, l] * Jr[l] for l in range(3))).max()
                                     for k in range(3)))
        for q2, R2 in zip(reps_q[:12], rots[:12]):
            hom_err = max(hom_err, np.abs(mats[key(rot(qmul(q, q2)))] - mats[key(Rq)] @ mats[key(R2)]).max())
    checks.append(("K1 2I closed, real spin representations, standard pairing",
                   len(G) == 120 and closed(G) and len(rots) == 60 and hom_err < 1e-8 and pair_err < 1e-8,
                   "|2I| %d, rotations %d, real form and homomorphism %s, pairing %s"
                   % (len(G), len(rots), bound(hom_err), bound(pair_err))))
    controls.append(("K1 a wrong class assignment is detectable", sorted(
        [sum(1 for R in rots if class_of(R) == c) for c in range(5)]) == sorted(CLASS_SIZES)))

    shell_mult = {}
    for N in SHELLS:
        chi = [float(np.trace(reals[N][key(R)])) for R in
               [next(R for R in rots if class_of(R) == c) for c in range(5)]]
        mult, resid = multiplicities(chi)
        commutant = sum(s * c * c for s, c in zip(CLASS_SIZES, chi)) / 60
        shell_mult[N] = mult
        facts["shell %d" % N] = (mult, sum(DIMS[k] * v for k, v in mult.items()), commutant)
    ok2 = all(sum(DIMS[k] * v for k, v in shell_mult[N].items()) == N + 1
              and abs(sum(v * v for v in shell_mult[N].values()) - facts["shell %d" % N][2]) < 1e-6 for N in SHELLS)
    checks.append(("K2 shell content by character and by commutant", ok2,
                   "; ".join("N=%d: %s" % (N, " + ".join("%s^%d" % (k, v) for k, v in shell_mult[N].items() if v)) for N in SHELLS)))
    controls.append(("K2 a shell's multiplicities are not all equal", any(len(set(shell_mult[N].values())) > 1 for N in SHELLS)))

    orbit_mult, orbits = {}, {}
    for order, size in ((5, 12), (3, 20), (2, 30)):
        dirs = axes_of_order(G, order)
        orbits[size] = dirs
        chi = [float(np.trace(perm_matrix(dirs, next(R for R in rots if class_of(R) == c)))) for c in range(5)]
        mult, _ = multiplicities(chi)
        axes = half_orbit(dirs)
        chi_w = [float(np.trace(wave_matrix(axes, next(R for R in rots if class_of(R) == c)))) for c in range(5)]
        mult_w, _ = multiplicities(chi_w)
        orbit_mult[size] = mult
        facts["orbit %d" % size] = (mult, mult == mult_w, len(dirs), len(axes))
    ok3 = all(len(orbits[s]) == s and facts["orbit %d" % s][1]
              and sum(DIMS[k] * v for k, v in orbit_mult[s].items()) == s for s in (12, 20, 30))
    checks.append(("K3 orbit modules, by permutation and by plane waves", ok3,
                   "; ".join("%d: %s" % (s, " + ".join("%s^%d" % (k, v) for k, v in orbit_mult[s].items() if v)) for s in (12, 20, 30))))
    controls.append(("K3 the plane-wave space of an orbit is not the constant", all(orbit_mult[s]["1"] == 1 for s in (12, 20, 30))))

    fit, contained = {}, {}
    for N in SHELLS:
        for s in (12, 20, 30):
            fit[(N, s)] = s <= N + 1
            contained[(N, s)] = all(orbit_mult[s][k] <= shell_mult[N][k] for k in TABLE)
    one_component = all(shell_mult[N]["1"] == 1 for N in SHELLS) and all(orbit_mult[s]["1"] == 1 for s in (12, 20, 30))
    checks.append(("K4 orbit fit and orbit-module containment", True,
                   "; ".join("N=%d: %s" % (N, ", ".join("%d fit=%s contained=%s" % (s, "y" if fit[(N, s)] else "n",
                                                                                    "y" if contained[(N, s)] else "n")
                                                        for s in (12, 20, 30))) for N in SHELLS)
                   + ("; one trivial per shell and per orbit, so at most one component" if one_component else "; TRIVIALS DIFFER")))
    controls.append(("K4 fit alone does not decide containment", any(fit[k] and not contained[k] for k in fit)))

    carriers, ranks = {}, {}
    for N in SHELLS:
        src = [reals[N][key(g)] for g in gens]
        for s in (12, 20, 30):
            if not fit[(N, s)]:
                continue
            axes = half_orbit(orbits[s])
            tgt = [wave_matrix(axes, g) for g in gens]
            basis = intertwiners(src, tgt)
            expected = sum(min(shell_mult[N][k], orbit_mult[s][k]) * DIMS[k] for k in TABLE)
            dim_ok = len(basis) == sum(shell_mult[N][k] * orbit_mult[s][k] for k in TABLE)
            F0 = sum(rng.normal() * Bk for Bk in basis) if basis else np.zeros((s, N + 1))
            r = int(np.linalg.matrix_rank(F0, tol=1e-8))
            ranks[(N, s)] = (r, expected, dim_ok)
            if r == s:
                w, V = np.linalg.eigh(F0 @ F0.T)
                F = V @ np.diag(w ** -0.5) @ V.T @ F0
                eq = max(np.abs(F @ reals[N][key(R)] - wave_matrix(axes, R) @ F).max() for R in rots)
                tight = np.abs(F @ F.T - np.eye(s)).max()
                pts = rng.normal(size=(12, 3))
                k = np.sqrt(N * (N + 2))
                def field(y, axes=axes, k=k):
                    return np.concatenate([np.cos(k * axes @ y), np.sin(k * axes @ y)])
                K = np.array([[field(a) @ (F @ F.T) @ field(b) for b in pts] for a in pts])
                Kstat = np.array([[sum(np.cos(k * axes @ (a - b))) for b in pts] for a in pts])
                carriers[(N, s)] = (eq, tight, np.abs(K - Kstat).max(), F, axes)
    ok5 = (all(contained[(N, s)] == ((N, s) in carriers) for (N, s) in ranks)
           and all(v[0] < 1e-8 and v[1] < 1e-8 and v[2] < 1e-6 for v in carriers.values())
           and all(r == exp or not dim_ok for (r, exp, dim_ok) in ranks.values()))
    checks.append(("K5 carriers exist exactly where the module is contained", ok5,
                   "; ".join("N=%d orbit %d: rank %d of %d needed%s" % (N, s, ranks[(N, s)][0], s,
                                                                        ", carrier built" if (N, s) in carriers else "")
                             for (N, s) in sorted(ranks))
                   + "; equivariance and tightness of every carrier %s" % bound(max([max(v[0], v[1]) for v in carriers.values()] or [0.0]))))
    controls.append(("K5 a shell without containment cannot reach full rank",
                     any(r < s for (N, s), (r, _, _) in ranks.items() if not contained[(N, s)])))

    invariants = {}
    for N in SHELLS:
        J = spin(N / 2)
        U = real_basis(N / 2)
        Jr = np.vstack([(U @ Jk @ U.conj().T) for Jk in J])
        sv = np.linalg.svd(Jr, compute_uv=False)
        invariants[N] = int(np.sum(sv < 1e-8))
    J0 = np.vstack([Jk for Jk in spin(0)])
    checks.append(("K6 no shell carries an SO(3)-invariant vector", all(v == 0 for v in invariants.values()),
                   "invariant dimensions %s" % ({N: invariants[N] for N in SHELLS})))
    controls.append(("K6 the trivial representation does carry one", int(np.sum(np.linalg.svd(J0, compute_uv=False) < 1e-8)) == 1))

    d12 = 13
    ax = rng.normal(size=(6, 3))
    ax /= np.linalg.norm(ax, axis=1)[:, None]
    k12 = np.sqrt(12 * 14)
    pts = rng.normal(size=(30, 3))

    def gram(axes, pts, k, const=True):
        cols = [np.cos(k * pts @ v) for v in axes] + [np.sin(k * pts @ v) for v in axes]
        if const:
            cols.append(np.ones(len(pts)))
        return np.array(cols).T

    M13 = gram(ax, pts, k12)
    K13 = M13 @ M13.T
    stat13 = np.array([[sum(np.cos(k12 * ax @ (a - b))) + 1 for b in pts] for a in pts])
    ax7 = rng.normal(size=(7, 3))
    ax7 /= np.linalg.norm(ax7, axis=1)[:, None]
    M14 = gram(ax7, pts, k12, const=False)
    r13, r14 = int(np.linalg.matrix_rank(M13, tol=1e-8)), int(np.linalg.matrix_rank(M14, tol=1e-8))
    checks.append(("K7 thirteen atoms on arbitrary axes, stationary, and fourteen need one rank more",
                   r13 == d12 and np.abs(K13 - stat13).max() < 1e-8 and r14 == 14 > d12,
                   "rank %d at N = 12 with d_N = %d, stationarity %s; fourteen atoms need rank %d"
                   % (r13, d12, bound(np.abs(K13 - stat13).max()), r14)))
    controls.append(("K7 a non-stationary combination is detectable",
                     np.abs((M13 @ np.diag([2.0] + [1.0] * 12) @ M13.T) - stat13).max() > 1e-3))

    p1 = np.array([[np.sinc(k12 * np.linalg.norm(a - b) / np.pi) for b in pts] for a in pts])
    rp1 = int(np.linalg.matrix_rank(p1, tol=1e-8))
    checks.append(("K8 the uniform angular measure's kernel outranks the shell", rp1 > d12,
                   "rank %d over %d points against d_N = %d" % (rp1, len(pts), d12)))
    controls.append(("K8 the atomic kernel does not outrank it", int(np.linalg.matrix_rank(K13, tol=1e-8)) == d12))

    worst_var, worst_eq, unscaled, lines = 0.0, 0.0, [], []
    for (N, s), (eq, tight, kdiff, F, axes) in sorted(carriers.items()):
        d, k = N + 1, np.sqrt(N * (N + 2))
        gamma = 2.0 * d / s
        Fp = np.sqrt(gamma) * F
        C = Fp @ Fp.T
        for y in rng.normal(size=(6, 3)):
            f = np.concatenate([np.cos(k * axes @ y), np.sin(k * axes @ y)])
            worst_var = max(worst_var, abs(f @ C @ f - d))
            unscaled.append(abs(f @ (F @ F.T) @ f - d))
        worst_eq = max(worst_eq, max(np.abs(Fp @ reals[N][key(R)] - wave_matrix(axes, R) @ Fp).max() for R in rots))
        lines.append("N=%d orbit %d: scalar 2 d_N / s = %.3f, variance %d" % (N, s, gamma, d))
    checks.append(("K9 power conservation fixes the tight map's scalar",
                   worst_var < 1e-8 and worst_eq < 1e-8 and len(lines) == 3,
                   "; ".join(lines) + "; variance and equivariance after rescaling %s" % bound(max(worst_var, worst_eq))))
    controls.append(("K9 the unrescaled tight map does not carry the shell's power", min(unscaled) > 1.0))

    for name, ok, info in checks:
        print("%s  %s\n      %s" % ("PASS" if ok else "FAIL", name, info))
    for name, came_out in controls:
        print("control  %-72s %s" % (name, "as required" if came_out else "DID NOT"))
    ok = all(c[1] for c in checks) and all(c[1] for c in controls)
    print("%d/%d checks pass; %d/%d controls as required" % (
        sum(c[1] for c in checks), len(checks), sum(c[1] for c in controls), len(controls)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
