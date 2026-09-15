#!/usr/bin/env python3
"""Checks the A5 statements of The Effective-Metric Floors (effective-metric-floors.md), §IV and §V, at N = 12.

  A1  2I, built as 120 unit quaternions, is closed under multiplication; rho_j (spin j = N/2) is a representation of it,
      and its pairing with the rotation R(q) on directions is the standard one
  A2  the invariant counts for N = 0..30 are the Molien ones; Sym^12 under 2I is 1 + 3 + 4 + 5, so the commutant has
      dimension 4, and the invariant state spans the one-dimensional summand
  A3  a constant transfer commuting with 2I is A5-covariant, and on the invariant state its power is its weight on the
      trivial summand: members with that weight fixed agree on the invariant state and differ on a generic state
  A4  across the classified family, E(n) = rho(g) diag(t) rho(g)^dag with sum t = 1, the invariant state's angle-averaged
      power is 1/(N+1) for every t; across the constant A5 family with trace 1 it is not fixed
  A5  E(n) = f(n)|psi><psi| + c(1 - |psi><psi|), with f the sum over the twelve five-fold directions v of (n.v)^20, is
      A5-covariant and predicts f on the invariant state; the classified family's patterns on that state span exactly four
      dimensions, which hold P1's and Q's patterns and not f; and g = 1 + 0.9 (f's part outside that span)/max, again
      nonnegative and A5-invariant, is the pattern of another A5-covariant transfer and departs from the span by order unity
Each check carries a control that must come out the other way.
"""
import itertools
import sys

import numpy as np
from scipy.linalg import expm

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-10
N = 12
rng = np.random.default_rng(20260915)


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def key(q):
    return tuple(np.round(q, 9) + 0.0)


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
    keys = {key(q) for q in G}
    return len(keys) == len(G) and all(key(qmul(p, q)) in keys for p in G for q in G)


def spin(j):
    d = int(round(2 * j)) + 1
    m = j - np.arange(d)
    jp = np.zeros((d, d))
    for k in range(1, d):
        jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return (jp + jp.T) / 2, (jp - jp.T) / 2j, np.diag(m).astype(float)


def rho(q, J, sign=1):
    a, v = q[0], np.asarray(q[1:])
    s = np.linalg.norm(v)
    d = J[0].shape[0]
    if s < 1e-14:
        return np.eye(d) * (1 if a > 0 else (-1) ** (d - 1))
    theta, n = 2 * np.arctan2(s, a), v / s
    return expm(-1j * sign * theta * (n[0] * J[0] + n[1] * J[1] + n[2] * J[2]))


def rot(q):
    a, b, c, d = q
    return np.array([[1 - 2 * (c * c + d * d), 2 * (b * c - a * d), 2 * (b * d + a * c)],
                     [2 * (b * c + a * d), 1 - 2 * (b * b + d * d), 2 * (c * d - a * b)],
                     [2 * (b * d - a * c), 2 * (c * d + a * b), 1 - 2 * (b * b + c * c)]])


def pairing_error(J, sign):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    U, R = rho(q, J, sign), rot(q)
    return max(np.abs(U.conj().T @ J[k] @ U - sum(R[k, l] * J[l] for l in range(3))).max() for k in range(3))


def isotypic(reps):
    d = reps[0].shape[0]
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    X = X + X.conj().T
    C = sum(U @ X @ U.conj().T for U in reps) / len(reps)
    w, V = np.linalg.eigh(C)
    blocks, start = [], 0
    for k in range(1, d + 1):
        if k == d or w[k] - w[k - 1] > 1e-8:
            blocks.append(V[:, start:k])
            start = k
    return blocks


def main():
    checks, controls = [], []
    parity = 0 if closed(build_2i(0)) else 1
    G = build_2i(parity)
    index = {key(q): i for i, q in enumerate(G)}
    J = spin(N / 2)
    reps = [rho(q, J) for q in G]
    hom = max(np.abs(reps[index[key(qmul(p, q))]] - reps[i] @ reps[k]).max()
              for i, p in enumerate(G) for k, q in enumerate(G))
    checks.append(("A1 2I closed, rho a representation, standard pairing",
                   len(G) == 120 and closed(G) and hom < TOL and pairing_error(J, 1) < TOL,
                   "parity %d, |G| %d, homomorphism %.1e, pairing %.1e" % (parity, len(G), hom, pairing_error(J, 1))))
    controls.append(("A1 reversed rotation sense breaks the pairing", pairing_error(J, -1) > 1e-3))

    counts = {}
    for n in range(0, 31, 2):
        Jn = spin(n / 2)
        P = sum(rho(q, Jn) for q in G) / 120
        counts[n] = int(round(np.trace(P).real))
    molien = {n: (1 if n in (0, 12, 20, 24, 30) else 0) for n in range(0, 31, 2)}
    commutant = sum(abs(np.trace(U)) ** 2 for U in reps).real / 120
    blocks = isotypic(reps)
    sizes = sorted(b.shape[1] for b in blocks)
    Pinv = sum(reps) / 120
    w, V = np.linalg.eigh((Pinv + Pinv.conj().T) / 2)
    psi = V[:, -1]
    triv = next(b for b in blocks if b.shape[1] == 1)
    fixed = max(np.abs(U @ psi - psi).max() for U in reps)
    checks.append(("A2 Molien counts, 1 + 3 + 4 + 5, invariant state in the trivial summand",
                   counts == molien and abs(commutant - 4) < 1e-9 and sizes == [1, 3, 4, 5]
                   and abs(abs(np.vdot(triv[:, 0], psi)) - 1) < TOL and fixed < TOL,
                   "counts %s, commutant %.6f, sizes %s, psi fixed to %.1e" % (
                       [n for n in counts if counts[n]], commutant, sizes, fixed)))
    hurwitz = [U for U, q in zip(reps, G) if np.all(np.isclose(np.abs(q) * 2 % 1, 0))]
    controls.append(("A2 the 24 Hurwitz units alone give a larger commutant",
                     len(hurwitz) == 24 and sum(abs(np.trace(U)) ** 2 for U in hurwitz).real / 24 > 4 + 1e-6))

    proj = {b.shape[1]: b @ b.conj().T for b in blocks}
    a = dict(zip((1, 3, 4, 5), rng.uniform(0.2, 1.0, size=4)))
    E1 = sum(a[k] * proj[k] for k in proj)
    b2 = dict(a)
    b2.update({3: a[3] * 1.7, 4: a[4] * 0.4, 5: a[5] * 1.3})
    E2 = sum(b2[k] * proj[k] for k in proj)
    cov = max(np.abs(U @ E1 @ U.conj().T - E1).max() for U in reps)
    chi = rng.normal(size=N + 1) + 1j * rng.normal(size=N + 1)
    chi /= np.linalg.norm(chi)
    on_psi = abs(np.vdot(psi, E1 @ psi) - np.vdot(psi, E2 @ psi))
    on_chi = abs(np.vdot(chi, E1 @ chi) - np.vdot(chi, E2 @ chi))
    checks.append(("A3 constant 2I-commuting transfers agree on the invariant state",
                   cov < TOL and abs(np.vdot(psi, E1 @ psi) - a[1]) < TOL and on_psi < TOL,
                   "covariance %.1e, power on psi - a_1 %.1e, two members differ on psi by %.1e and on a generic state by %.3f"
                   % (cov, abs(np.vdot(psi, E1 @ psi) - a[1]), on_psi, on_chi)))
    M = rng.normal(size=(N + 1, N + 1))
    M = M @ M.T
    controls.append(("A3 a generic positive constant is not covariant, and the members differ on a generic state",
                     max(np.abs(U @ M @ U.conj().T - M).max() for U in reps) > 1e-3 and on_chi > 1e-3))

    x, wx = np.polynomial.legendre.leggauss(40)
    phis = np.arange(80) * 2 * np.pi / 80
    nodes, weights, frames = [], [], []
    for xi, wi in zip(x, wx):
        th = np.arccos(xi)
        for ph in phis:
            g = qmul(np.array([np.cos(ph / 2), 0, 0, np.sin(ph / 2)]), np.array([np.cos(th / 2), 0, np.sin(th / 2), 0]))
            nodes.append(rot(g)[:, 2])
            weights.append(wi / 2 / 80)
            frames.append(rho(g, J))
    nodes, weights = np.array(nodes), np.array(weights)
    direction_ok = max(np.abs(n - np.array([np.sin(np.arccos(z)) * np.cos(p), np.sin(np.arccos(z)) * np.sin(p), z])).max()
                       for n, z, p in zip(nodes, np.repeat(x, 80), np.tile(phis, 40)))
    amp = np.array([np.abs(U.conj().T @ psi) ** 2 for U in frames])
    worst = 0.0
    for _ in range(5):
        t = rng.uniform(size=N + 1)
        t /= t.sum()
        worst = max(worst, abs(weights @ (amp @ t) - 1 / (N + 1)))
    dims = {1: 1, 3: 3, 4: 4, 5: 5}
    tr = sum(a[k] * dims[k] for k in a)
    a_norm = {k: a[k] / tr for k in a}
    checks.append(("A4 classified family: the invariant state's averaged power is 1/(N+1) for every t",
                   worst < 1e-12 and direction_ok < 1e-12, "worst deviation %.1e over five random t" % worst))
    controls.append(("A4 a trace-1 constant A5 member gives a different averaged power",
                     abs(a_norm[1] - 1 / (N + 1)) > 1e-3))

    five = []
    for q in G:
        if np.isclose(abs(q[0]), PHI / 2) or np.isclose(abs(q[0]), 0.5 / PHI):
            v = q[1:] / np.linalg.norm(q[1:])
            for u in (v, -v):
                if not any(np.allclose(u, w_) for w_ in five):
                    five.append(u)
    five = np.array(five)

    def f(n):
        return float(np.sum((five @ n) ** 20))

    Ppsi = np.outer(psi, psi.conj())

    def E(n, state=Ppsi):
        return f(n) * state + 0.3 * (np.eye(N + 1) - state)

    worst_inv, worst_cov, worst_bad = 0.0, 0.0, 0.0
    Pchi = np.outer(chi, chi.conj())
    for _ in range(4):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        for q, U in zip(G, reps):
            m = rot(q) @ n
            worst_inv = max(worst_inv, abs(f(m) - f(n)) / f(n))
            worst_cov = max(worst_cov, np.abs(E(m) - U @ E(n) @ U.conj().T).max())
            worst_bad = max(worst_bad, np.abs(E(m, Pchi) - U @ E(n, Pchi) @ U.conj().T).max())
    fvals = np.array([f(n) for n in nodes])
    pattern = np.array([np.vdot(psi, E(n) @ psi).real for n in nodes])
    s = np.linalg.svd(amp, compute_uv=False)
    rank = int(np.sum(s > 1e-10 * s[0]))

    def fit(target):
        c, *_ = np.linalg.lstsq(amp, target, rcond=None)
        return c, np.linalg.norm(amp @ c - target) / np.linalg.norm(target)

    c_f, r_f = fit(fvals)
    r_p1, r_q = fit(np.full(len(nodes), 1 / (N + 1)))[1], fit(amp[:, 0])[1]
    # Membership is judged against the roundoff floor of the in-span patterns, near 1e-15, and size separately, on g:
    # f is mostly of low degree, so a single residual threshold would conflate the two.
    scale = np.abs(fvals - amp @ c_f).max()

    def g_pat(n):
        th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
        U = rho(qmul(np.array([np.cos(ph / 2), 0, 0, np.sin(ph / 2)]), np.array([np.cos(th / 2), 0, np.sin(th / 2), 0])), J)
        return 1 + 0.9 * (f(n) - (np.abs(U.conj().T @ psi) ** 2) @ c_f) / scale

    def E_g(n):
        return g_pat(n) * Ppsi + 0.3 * (np.eye(N + 1) - Ppsi)

    gvals = np.array([g_pat(n) for n in nodes])
    r_g = fit(gvals)[1]
    worst_g, low_g = 0.0, gvals.min()
    for _ in range(4):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        En = E_g(n)
        low_g = min(low_g, g_pat(n))
        for q, U in zip(G, reps):
            worst_g = max(worst_g, np.abs(E_g(rot(q) @ n) - U @ En @ U.conj().T).max())
    checks.append(("A5 direction-dependent A5 transfers reach patterns outside the classified span",
                   len(five) == 12 and worst_inv < 1e-12 and worst_cov < TOL and np.abs(pattern - fvals).max() < TOL
                   and (fvals.max() - fvals.min()) / fvals.max() > 0.1 and rank == 4 and r_f > 1e-6
                   and r_p1 < 1e-10 and r_q < 1e-10 and worst_g < 1e-9 and low_g > 0 and r_g > 0.1,
                   "f: invariant to %.1e, covariance %.1e, residual %.1e; classified span rank %d, P1 residual %.1e, Q %.1e; "
                   "g: covariance %.1e, minimum %.2f, residual %.3f" % (worst_inv, worst_cov, r_f, rank, r_p1, r_q,
                                                                        worst_g, low_g, r_g)))
    controls.append(("A5 the same construction on a generic state is not covariant", worst_bad > 1e-3))

    for name, ok, info in checks:
        print("%s  %s\n      %s" % ("PASS" if ok else "FAIL", name, info))
    for name, came_out in controls:
        print("control  %-80s %s" % (name, "as required" if came_out else "DID NOT"))
    ok = all(c[1] for c in checks) and all(c[1] for c in controls)
    print("%d/%d checks pass; %d/%d controls as required" % (
        sum(c[1] for c in checks), len(checks), sum(c[1] for c in controls), len(controls)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
