"""The Slot Ground States, §IV: the soft blocks' reduced quartic in closed form.

Checks, each able to fail:
  1. the binary icosahedral group 2I (120 unit quaternions) closes, and its nine irreducible
     characters are orthonormal, with McKay distances (1, 7, 2, 6, 6, 3, 4, 5) for R1..R8;
  2. in each soft slot (R2 at level 7, R4 and R5 at level 6) the slot projector P has spin
     components only at 0 and 6 under conjugation;
  3. the group-sum quartic Q(w) = V int rho_w^2 / (int rho_w)^2 equals
     1 + d(d - r)/(13 r) ||(w w^dag)_6||^2 / |w|^4 on random states, and fails with the weight off by 1%;
  4. exactly (sympy), the pairing-channel coefficients are q_J = 1 + 13 beta {j j 6; j j J}, with
     beta = d(d - r)/(13 r) and j the block's spin, giving
     D7's weights 28/39 and 21/52 and R2's (144/143, 196/143, 28/11, 0); a spin-4 control does not fit;
  5. every symmetric-channel coefficient exceeds 1 in R4 and R5 (Proposition C1).
Floating point for 1 to 3 (double precision), exact rationals for 4 and 5. Runs in a few seconds.
"""
import itertools
from fractions import Fraction

import numpy as np
from scipy.linalg import expm
from sympy import Rational, S
from sympy.physics.wigner import wigner_6j

PHI = (1 + 5 ** 0.5) / 2


def binary_icosahedral():
    def parity(p):
        p, s = list(p), 0
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                s ^= 1
        return s

    els = set()
    for i in range(4):
        for sg in (1.0, -1.0):
            v = [0.0] * 4
            v[i] = sg
            els.add(tuple(v))
    for sg in itertools.product((0.5, -0.5), repeat=4):
        els.add(sg)
    base = (0.0, 0.5, 0.5 / PHI, 0.5 * PHI)  # even permutations of (0, 1, 1/phi, phi)/2
    for p in itertools.permutations(range(4)):
        if parity(p):
            continue
        for s1, s2, s3 in itertools.product((1, -1), repeat=3):
            vals = (0.0, s1 * base[1], s2 * base[2], s3 * base[3])
            v = [0.0] * 4
            for k in range(4):
                v[p[k]] = vals[k]
            els.add(tuple(round(x, 12) + 0.0 for x in v))
    els = sorted(els)
    assert len(els) == 120
    return [np.array(e) for e in els]


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def spin_matrices(j2):
    j = j2 / 2
    ms = [j - k for k in range(j2 + 1)]
    d = j2 + 1
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - ms[k] * (ms[k] + 1))
    Jm = Jp.conj().T
    return (Jp + Jm) / 2, (Jp - Jm) / 2j, np.diag(ms).astype(complex)


def rep(j2, q):
    a, v = q[0], np.array(q[1:])
    s = np.linalg.norm(v)
    if s < 1e-15:
        return np.eye(j2 + 1, dtype=complex) * (1.0 if a > 0 else (-1.0) ** j2)
    t, n = 2 * np.arctan2(s, a), v / s
    Jx, Jy, Jz = spin_matrices(j2)
    return expm(-1j * t * (n[0] * Jx + n[1] * Jy + n[2] * Jz))


def galois(t):  # sqrt5 -> -sqrt5 on the trace values of 2I
    for a, b in ((PHI, -1 / PHI), (-PHI, 1 / PHI), (1 / PHI, -PHI), (-1 / PHI, PHI)):
        if abs(t - a) < 1e-9:
            return b
    return float(round(t))


G = binary_icosahedral()
keys = {tuple(np.round(g, 9) + 0.0) for g in G}
assert all(tuple(np.round(qmul(g, h), 9) + 0.0) in keys for g in G for h in G)
tr = {j2: np.array([np.trace(rep(j2, g)).real for g in G]) for j2 in range(8)}
tg = np.array([galois(2 * g[0]) for g in G])
chi = {"R0": tr[0], "R1": tr[1], "R2": tr[7] - tr[5], "R3": tr[2], "R4": tg ** 2 - 1,
       "R5": tr[6] - (tg ** 2 - 1), "R6": tr[3], "R7": tr[4], "R8": tr[5]}
names = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
gram = np.array([[np.mean(chi[a] * chi[b]) for b in names] for a in names])
assert np.allclose(gram, np.eye(9), atol=1e-12)
dist = {}
for n in names[1:]:
    for j2 in range(40):
        t = np.array([np.trace(rep(j2, g)).real for g in G]) if j2 >= 8 else tr[j2]
        if round(np.mean(t * chi[n])) > 0:
            dist[n] = j2
            break
assert [dist[n] for n in names[1:]] == [1, 7, 2, 6, 6, 3, 4, 5]
print("1. 2I closes; nine characters orthonormal; McKay distances R1..R8 =", [dist[n] for n in names[1:]])

rng = np.random.default_rng(4)
for sec, j2, r in (("R2", 7, 2), ("R4", 6, 3), ("R5", 6, 4)):
    d = j2 + 1
    P = sum(c * rep(j2, g) for g, c in zip(G, chi[sec])) * r / 120
    assert np.allclose(P @ P, P, atol=1e-10) and abs(np.trace(P).real - r) < 1e-9
    Jx, Jy, Jz = spin_matrices(j2)
    # total spin on V (x) V for the group-sum quartic, and the adjoint spin on End(V) for the closed form
    I = np.eye(d)
    tot = [np.kron(A, I) + np.kron(I, A) for A in (Jx, Jy, Jz)]
    adj = [np.kron(A, I) - np.kron(I, A.T) for A in (Jx, Jy, Jz)]

    def projs(ops):
        C = sum(o @ o for o in ops)
        out = {}
        for L in range(j2 + 1):
            M = np.eye(d * d, dtype=complex)
            for K in range(j2 + 1):
                if K != L:
                    M = M @ (C - K * (K + 1) * np.eye(d * d)) / (L * (L + 1) - K * (K + 1))
            out[L] = M
        return out

    PJ, PL = projs(tot), projs(adj)
    PP = np.kron(P, P)
    q = {J: d ** 2 / r ** 2 * np.trace(PJ[J] @ PP).real / (2 * J + 1) for J in PJ}
    content = [L for L in PL if np.linalg.norm(PL[L] @ P.reshape(-1)) > 1e-9]
    assert content == [0, 6], content
    beta = d * (d - r) / (13 * r)
    dev = arm = 0.0
    for _ in range(20):
        w = rng.normal(size=d) + 1j * rng.normal(size=d)
        n4 = np.vdot(w, w).real ** 2
        ww = np.kron(w, w)
        Qw = sum(q[J] * np.linalg.norm(PJ[J] @ ww) ** 2 for J in q) / n4
        m6 = np.linalg.norm(PL[6] @ np.outer(w, w.conj()).reshape(-1)) ** 2 / n4
        dev = max(dev, abs(Qw - (1 + beta * m6)))
        arm = max(arm, abs(Qw - (1 + 1.01 * beta * m6)))
    assert dev < 1e-10 and arm > 1e-4
    print(f"2-3. {sec}: P has spin content {content}; closed form with beta = {Fraction(d * (d - r), 13 * r)} holds to "
          f"{dev:.1e} on 20 random states; with beta off by 1% the deviation is {arm:.1e}")

j = Rational(7, 2)
beta2 = Rational(8 * 6, 13 * 2)
q2 = {J: 1 + 13 * beta2 * S(wigner_6j(j, j, 6, j, j, J)) for J in (7, 5, 3, 1)}
assert q2 == {7: Rational(144, 143), 5: Rational(196, 143), 3: Rational(28, 11), 1: 0}
ctrl = {J: (q2[J] - 1) / (9 * S(wigner_6j(j, j, 4, j, j, J))) for J in q2}
assert len(set(ctrl.values())) > 1
assert beta2 == Rational(24, 13)
print(f"4. R2 exactly: beta = {beta2}, q_J =", {J: str(v) for J, v in q2.items()}, "; a spin-4 control does not fit")
for sec, beta, rr in (("R4", Rational(28, 39), 3), ("R5", Rational(21, 52), 4)):
    assert beta == Rational(7 * (7 - rr), 13 * rr)
    qF = {F: 1 + 13 * beta * S(wigner_6j(3, 3, 6, 3, 3, F)) for F in (6, 4, 2, 0)}
    assert all(v > 1 for v in qF.values())
    print(f"4-5. {sec} exactly: beta = {beta} (D7), q_F = {[str(qF[F]) for F in (6, 4, 2, 0)]}, all > 1")
print("ALL CHECKS PASS")
