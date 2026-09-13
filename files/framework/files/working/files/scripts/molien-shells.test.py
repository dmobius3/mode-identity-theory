#!/usr/bin/env python3
"""molien-shells.test.py -- the surviving Molien shells of S^3/2I and their icosahedral patterns (2026-09-13).

Companion to molien-shells.md. Nothing here touches the sky: no radius R, no projection,
no data. Checks:

  1. Fixture, exact in Z[phi]. 2I classes are indexed by SU(2) half-angle theta (trace 2 cos theta),
     A5 classes by rotation angle alpha = 2 theta. On the known rows l = 2, 6, 10, 15, 30 the
     A5-invariant harmonics H_l and the 2I-invariants in Sym^{2l} C^2 agree (0, 1, 1, 1, 2); the
     agreement holds for every l <= 30, and no odd degree carries a 2I-invariant (the central
     -I acts on Sym^N C^2 as (-1)^N).
     Mutation arms: indexing the A5 classes by half-angle gives non-integers, and indexing the
     2I classes by rotation angle gives integers that look plausible and miss the known rows;
     both break the fixture.
  2. The Molien counts match (1 + t^30)/((1 - t^12)(1 - t^20)), equivalently
     (1 - t^60)/((1 - t^12)(1 - t^20)(1 - t^30)), to N = 60. The shells N <= 30 are
     N = 0, 12, 20, 24, 30, carrying m_N (N + 1) = 1, 13, 21, 25, 31 surviving modes.
  3. The Reynolds projector over the 120 unit quaternions of 2I, acting on binary forms of
     degree N, has rank m_N for every N <= 30. Mutation arm: over the binary tetrahedral
     subgroup it has rank 1 at N = 6, where 2I has none.
  4. The patterns. Each invariant binary form is read as its root set on S^2 (its Majorana
     constellation, by stereographic projection of z1/z2). N = 12 gives the 12 vertices of a
     regular icosahedron, N = 20 its 20 face centres, N = 30 its 30 edge midpoints, and the
     N = 24 invariant is the square of the N = 12 one. Each set is antipodal, so the patterns
     carry 6, 10 and 15 axes. Mutation arm: a generic binary tetrahedral invariant of degree 12
     is not a regular icosahedron.

Run from anywhere: python3 molien-shells.test.py   (needs numpy)
"""
from fractions import Fraction as Fr

import numpy as np


def fail(msg):
    raise SystemExit(f"CHECK FAILED: {msg}")


# ----------------------------- Z[phi], pairs (a, b) = a + b*phi ---------------------------
def zadd(x, y): return (x[0] + y[0], x[1] + y[1])
def zsub(x, y): return (x[0] - y[0], x[1] - y[1])
def zmul(x, y): return (x[0] * y[0] + x[1] * y[1], x[0] * y[1] + x[1] * y[0] + x[1] * y[1])


# 2I in SU(2): (class size, trace 2 cos theta), theta the half-angle.
CLASSES_2I = [(1, (2, 0)), (1, (-2, 0)), (30, (0, 0)), (20, (1, 0)), (20, (-1, 0)),
              (12, (0, 1)), (12, (0, -1)), (12, (-1, 1)), (12, (1, -1))]
# A5 acting on R^3: (class size, 2 cos alpha), alpha the rotation angle.
CLASSES_A5 = [(1, (2, 0)), (15, (-2, 0)), (20, (-1, 0)), (12, (-1, 1)), (12, (0, -1))]
# The trap: the same five A5 classes indexed by half-angle alpha/2 instead of alpha.
CLASSES_A5_BY_HALF_ANGLE = [(1, (2, 0)), (15, (0, 0)), (20, (1, 0)), (12, (0, 1)), (12, (-1, 1))]
# The mirror trap: the nine 2I classes indexed by rotation angle 2 theta instead of theta.
CLASSES_2I_BY_ROTATION_ANGLE = [(1, (2, 0)), (1, (2, 0)), (30, (-2, 0)), (20, (-1, 0)), (20, (-1, 0)),
                                (12, (-1, 1)), (12, (-1, 1)), (12, (0, -1)), (12, (0, -1))]


def sym_char(N, t):
    """Character of Sym^N C^2 at trace t = 2 cos theta: U_0 = 1, U_1 = t, U_{n+1} = t U_n - U_{n-1}."""
    u0, u1 = (1, 0), t
    if N == 0:
        return u0
    for _ in range(N - 1):
        u0, u1 = u1, zsub(zmul(t, u1), u0)
    return u1


def harmonic_char(l, c):
    """Character of the degree-l spherical harmonics at c = 2 cos alpha: 1 + sum_{k=1}^{l} 2 cos(k alpha)."""
    total, prev, cur = (1, 0), (2, 0), c
    for _ in range(l):
        total = zadd(total, cur)
        prev, cur = cur, zsub(zmul(c, cur), prev)
    return total


def class_average(classes, order, char):
    s = (0, 0)
    for n, t in classes:
        v = char(t)
        s = zadd(s, (n * v[0], n * v[1]))
    if s[1] != 0 or s[0] % order != 0:
        return None                      # not an integer: wrong class data or wrong indexing
    return s[0] // order


def m(N): return class_average(CLASSES_2I, 120, lambda t: sym_char(N, t))
def h(l, classes=CLASSES_A5): return class_average(classes, 60, lambda c: harmonic_char(l, c))


# ----------------------------- 1. fixture ---------------------------------------------------
KNOWN = {2: 0, 6: 1, 10: 1, 15: 1, 30: 2}
for l, want in KNOWN.items():
    if h(l) != want or m(2 * l) != want:
        fail(f"fixture row l = {l}: H_l {h(l)}, Sym^{2 * l} {m(2 * l)}, expected {want}")
if any(m(2 * l) != h(l) for l in range(31)):
    fail("dim Sym^{2l}(C^2)^{2I} and dim H_l^{A5} disagree for some l <= 30")
if any(m(N) != 0 for N in range(1, 61, 2)):
    fail("an odd degree carries a 2I-invariant")
print("[1] Fixture, exact in Z[phi] (2I by SU(2) half-angle, A5 by rotation angle)")
print("     l   H_l^A5   Sym^{2l}(C^2)^2I")
for l in KNOWN:
    print(f"    {l:2d}   {h(l):5d}   {m(2 * l):8d}")
print("    agreement for every l <= 30; no 2I-invariant in odd degree up to N = 60")
wrong = {l: h(l, CLASSES_A5_BY_HALF_ANGLE) for l in KNOWN}
if all(wrong[l] == KNOWN[l] for l in KNOWN):
    fail("mutation arm: indexing A5 by half-angle did not break the fixture")
print(f"    mutation arm: A5 indexed by half-angle gives {wrong} (None = not an integer), breaking the fixture, as required")
plausible = {l: class_average(CLASSES_2I_BY_ROTATION_ANGLE, 120, lambda t, N=2 * l: sym_char(N, t)) for l in KNOWN}
if any(v is None for v in plausible.values()) or all(plausible[l] == KNOWN[l] for l in KNOWN):
    fail("mutation arm: 2I indexed by rotation angle should give integers that miss the known rows")
print(f"    mutation arm: 2I indexed by rotation angle gives integers {plausible}, plausible-looking and wrong, breaking the fixture, as required")


# ----------------------------- 2. Molien series and shells ----------------------------------
def two_generator_form(nmax):             # (1 + t^30) / ((1 - t^12)(1 - t^20))
    c = [0] * (nmax + 1)
    for a in range(0, nmax + 1, 12):
        for b in range(0, nmax + 1 - a, 20):
            for e in (0, 30):
                if a + b + e <= nmax:
                    c[a + b + e] += 1
    return c


def three_generator_form(nmax):           # (1 - t^60) / ((1 - t^12)(1 - t^20)(1 - t^30))
    c3 = [0] * (nmax + 1)
    for a in range(0, nmax + 1, 12):
        for b in range(0, nmax + 1 - a, 20):
            for e in range(0, nmax + 1 - a - b, 30):
                c3[a + b + e] += 1
    return [c3[N] - (c3[N - 60] if N >= 60 else 0) for N in range(nmax + 1)]


MOLIEN = [m(N) for N in range(61)]
if MOLIEN != two_generator_form(60) or MOLIEN != three_generator_form(60):
    fail("Molien counts differ from the closed forms")
SHELLS = [(N, MOLIEN[N], MOLIEN[N] * (N + 1)) for N in range(31) if MOLIEN[N]]
if SHELLS != [(0, 1, 1), (12, 1, 13), (20, 1, 21), (24, 1, 25), (30, 1, 31)]:
    fail(f"shell list {SHELLS}")
print("\n[2] Molien counts match (1+t^30)/((1-t^12)(1-t^20)) = (1-t^60)/((1-t^12)(1-t^20)(1-t^30)) to N = 60")
print(f"    shells N <= 30 as (N, invariants m_N, surviving modes m_N (N+1)): {SHELLS}")


# ----------------------------- 3. 2I as 120 unit quaternions, Reynolds projectors -----------
def qa(x, y): return (x[0] + y[0], x[1] + y[1])
def qm(x, y): return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def qn(x): return (-x[0], -x[1])
Z0, H = (Fr(0), Fr(0)), (Fr(1, 2), Fr(0))


def hmul(x, y):
    a1, b1, c1, d1 = x
    a2, b2, c2, d2 = y
    s = lambda *t: (sum(u[0] for u in t), sum(u[1] for u in t))
    return (s(qm(a1, a2), qn(qm(b1, b2)), qn(qm(c1, c2)), qn(qm(d1, d2))),
            s(qm(a1, b2), qm(b1, a2), qm(c1, d2), qn(qm(d1, c2))),
            s(qm(a1, c2), qn(qm(b1, d2)), qm(c1, a2), qm(d1, b2)),
            s(qm(a1, d2), qm(b1, c2), qn(qm(c1, b2)), qm(d1, a2)))


def closure(gens):
    group, frontier = set(gens), list(gens)
    while frontier:
        new = []
        for x in frontier:
            for y in gens:
                z = hmul(x, y)
                if z not in group:
                    group.add(z)
                    new.append(z)
        frontier = new
    return group


g1 = (H, H, H, H)                                         # (1 + i + j + k)/2
g2 = ((Fr(1, 4), Fr(1, 4)), (Fr(-1, 4), Fr(1, 4)), H, Z0)  # (phi + i/phi + j)/2
TWO_I = sorted(closure([g1, g2]))
if len(TWO_I) != 120:
    fail(f"2I closure has {len(TWO_I)} elements")
TWO_T = [q for q in TWO_I if all(x[1] == 0 and x[0] in (0, Fr(1, 2), Fr(-1, 2), 1, -1) for x in q)]
TWO_T_SET = set(TWO_T)
if len(TWO_T) != 24 or any(hmul(x, y) not in TWO_T_SET for x in TWO_T for y in TWO_T):
    fail("the Hurwitz units do not form a 24-element subgroup of 2I")

SQ5 = 5 ** 0.5
def real(x): return float(x[0]) + float(x[1]) * SQ5


def su2(q):
    a, b, c, d = (real(x) for x in q)
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


G_2I = [su2(q) for q in TWO_I]
G_2T = [su2(q) for q in TWO_T]
if any(abs(np.linalg.det(g) - 1) > 1e-12 or np.abs(g @ g.conj().T - np.eye(2)).max() > 1e-12 for g in G_2I):
    fail("a quaternion did not map into SU(2)")
PP = np.polynomial.polynomial


def sym_matrix(g, N):
    """Matrix of p -> p(g (z1, z2)) on binary forms of degree N, in the basis z1^k z2^(N-k)."""
    (al, be), (ga, de) = g
    M = np.zeros((N + 1, N + 1), dtype=complex)
    for k in range(N + 1):
        col = PP.polymul(PP.polypow([be, al], k), PP.polypow([de, ga], N - k))
        M[:len(col), k] = col[:N + 1]
    return M


def reynolds(group, N):
    return sum(sym_matrix(g, N) for g in group) / len(group)


def rank(R):
    s = np.linalg.svd(R, compute_uv=False)
    return int((s > 1e-8 * max(1.0, s[0])).sum())


ranks = [rank(reynolds(G_2I, N)) for N in range(31)]
if ranks != MOLIEN[:31]:
    fail(f"Reynolds ranks {ranks} differ from the Molien counts")
print("\n[3] Reynolds projector over the 120 quaternions: rank = m_N for every N <= 30")
r2t6 = rank(reynolds(G_2T, 6))
if r2t6 == MOLIEN[6]:
    fail("mutation arm: the binary tetrahedral projector at N = 6 matched 2I")
print(f"    mutation arm: over the binary tetrahedral subgroup the rank at N = 6 is {r2t6}, where 2I has {MOLIEN[6]}, as required")


# ----------------------------- 4. the patterns ----------------------------------------------
def invariant(group, N, seed=None):
    R = reynolds(group, N)
    if seed is None:
        u = R[:, int(np.argmax(np.linalg.norm(R, axis=0)))]
    else:
        u = R @ np.random.default_rng(seed).standard_normal(N + 1)
    return u / np.linalg.norm(u)


def on_sphere(u):
    """Root set of the binary form sum_k u_k z1^k z2^(N-k) as points of S^2 (z = z1/z2; z = infinity is the pole)."""
    N = len(u) - 1
    scale = np.abs(u).max()
    deg = N
    while deg > 0 and abs(u[deg]) < 1e-10 * scale:
        deg -= 1
    roots = np.roots(u[:deg + 1][::-1]) if deg > 0 else np.array([])
    pts = [np.array([2 * z.real, 2 * z.imag, abs(z) ** 2 - 1]) / (abs(z) ** 2 + 1) for z in roots]
    pts += [np.array([0.0, 0.0, 1.0])] * (N - deg)
    return np.array(pts)


def same_set(A, B, tol=1e-6):
    return (len(A) == len(B) and all(np.min(np.linalg.norm(B - a, axis=1)) < tol for a in A)
            and all(np.min(np.linalg.norm(A - b, axis=1)) < tol for b in B))


def unit(v): return v / np.linalg.norm(v)


def icosahedron(points, tol=1e-6):
    """Regular icosahedron test: 12 points, pairwise dots in {1, 1/sqrt5, -1/sqrt5, -1}, five nearest each."""
    if len(points) != 12:
        return None
    D = points @ points.T
    allowed = np.array([1, 1 / SQ5, -1 / SQ5, -1])
    if np.abs(D[..., None] - allowed).min(axis=-1).max() > tol:
        return None
    nbrs = [[j for j in range(12) if abs(D[i, j] - 1 / SQ5) < tol] for i in range(12)]
    if any(len(n) != 5 for n in nbrs):
        return None
    return nbrs


u12 = invariant(G_2I, 12)
V = on_sphere(u12)
nbrs = icosahedron(V)
if nbrs is None:
    fail("the degree-12 invariant's roots are not a regular icosahedron")
faces = sorted({tuple(sorted((i, j, k))) for i in range(12) for j in nbrs[i] for k in nbrs[i] if k in nbrs[j]})
edges = sorted({tuple(sorted((i, j))) for i in range(12) for j in nbrs[i]})
if len(faces) != 20 or len(edges) != 30:
    fail("icosahedron faces or edges miscounted")
FACE_CENTRES = np.array([unit(V[list(f)].sum(axis=0)) for f in faces])
EDGE_MIDPOINTS = np.array([unit(V[i] + V[j]) for i, j in edges])
if not same_set(on_sphere(invariant(G_2I, 20)), FACE_CENTRES):
    fail("the degree-20 invariant's roots are not the face centres")
if not same_set(on_sphere(invariant(G_2I, 30)), EDGE_MIDPOINTS):
    fail("the degree-30 invariant's roots are not the edge midpoints")
u24 = invariant(G_2I, 24)
sq = PP.polymul(u12, u12)[:25]
if np.linalg.norm(u24 - (np.vdot(sq, u24) / np.vdot(sq, sq)) * sq) > 1e-8:
    fail("the degree-24 invariant is not the square of the degree-12 one")
if not all(same_set(X, -X) for X in (V, FACE_CENTRES, EDGE_MIDPOINTS)):
    fail("a pattern is not antipodal")
angles = sorted({round(float(np.degrees(np.arccos(np.clip(V[0] @ V[j], -1, 1)))), 2) for j in range(1, 12)})
print("\n[4] Patterns: root sets (Majorana constellations) of the invariant forms on S^2")
print(f"    N = 12: 12 points, a regular icosahedron (angles from one vertex {angles} deg): the vertices, 6 axes")
print("    N = 20: 20 points, the face centres of that icosahedron: 10 axes")
print("    N = 24: the invariant is the square of the N = 12 one: the vertices, doubled")
print("    N = 30: 30 points, the edge midpoints of that icosahedron: 15 axes")
T12 = reynolds(G_2T, 12)
if rank(T12) != 2:
    fail(f"binary tetrahedral invariants of degree 12 have rank {rank(T12)}, expected 2")
w = invariant(G_2T, 12, seed=0)
if np.linalg.norm(w - (np.vdot(u12, w) / np.vdot(u12, u12)) * u12) < 1e-3:
    fail("the generic binary tetrahedral invariant happened to be the icosahedral one")
if icosahedron(on_sphere(w)) is not None:
    fail("mutation arm: a generic binary tetrahedral invariant passed the icosahedron test")
print("    mutation arm: a generic binary tetrahedral invariant of degree 12 (a 2-dimensional space) fails the icosahedron test, as required")
print("\nALL PASS")
