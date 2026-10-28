#!/usr/bin/env python3
"""Companion to s3-2i-oph-dictionary.md, section III: a sweep for its proposition. Random polynomial maps P: R^3 -> R^3 of degree at most 7 with
P(R_g x) = R'_g P(x) for all sixty rotations g, where R_g is the convex frame's rotation of a
port permutation and R'_g the twin frame's rotation of the same permutation (built as in
frame_degree.py). Each map is restricted to the unit sphere and normalized, and its degree is
the signed area of its image over 4 pi, summed over a fine geodesic triangulation. Control: the
same with R'_g replaced by R_g. The maps are drawn without reference to the
proposition's congruences. numpy only.
"""
import itertools

import numpy as np

PHI = (1 + 5 ** 0.5) / 2


def frame(p):
    V = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            V += [(0, s1, s2 * p), (s1, s2 * p, 0), (s2 * p, 0, s1)]
    return np.array(V, float)


Vp, Vm = frame(PHI), frame(1 - PHI)
n = len(Vp)
D = np.linalg.norm(Vp[:, None] - Vp[None], axis=2)
A = np.isclose(D, np.unique(np.round(D, 9))[1])
FACES = []
for i, j, k in itertools.combinations(range(n), 3):
    if A[i, j] and A[j, k] and A[i, k]:
        FACES.append((i, j, k) if np.linalg.det(Vp[[i, j, k]]) > 0 else (i, k, j))


def basis(V, a, b):
    return np.array([V[a], V[b], np.cross(V[a], V[b])]).T


w0 = int(np.flatnonzero(A[0])[0])
Rp, Rm = [], []
for a in range(n):
    for b in np.flatnonzero(A[a]):
        R = basis(Vp, a, b) @ np.linalg.inv(basis(Vp, 0, w0))
        perm = [int(np.flatnonzero(np.all(np.isclose(Vp, x), axis=1))[0]) for x in (R @ Vp.T).T]
        X, Y = Vm.T, Vm[perm].T
        Rp.append(R)
        Rm.append(Y @ X.T @ np.linalg.inv(X @ X.T))

EXP = [(a, b, d - a - b) for d in range(8) for a in range(d + 1) for b in range(d + 1 - a)]
M = len(EXP)


def mono(X):
    return np.stack([X[:, 0] ** a * X[:, 1] ** b * X[:, 2] ** c for a, b, c in EXP], axis=1)


rng = np.random.default_rng(1)
pts = rng.normal(size=(30, 3))
pts *= (rng.uniform(0.6, 1.4, size=30) / np.linalg.norm(pts, axis=1))[:, None]


def equivariant_maps(targets):
    """Null space of C -> [x -> C m(R_g x) - T_g C m(x)] over the sample points, C a 3 x M matrix."""
    m0 = mono(pts)
    rows = []
    for R, T in zip(Rp, targets):
        mR = mono(pts @ R.T)
        for i in range(3):
            row = np.zeros((len(pts), 3 * M))
            row[:, i * M:(i + 1) * M] += mR
            for j in range(3):
                row[:, j * M:(j + 1) * M] -= T[i, j] * m0
            rows.append(row)
    _, s, Vh = np.linalg.svd(np.vstack(rows), full_matrices=False)
    k = int(np.sum(s < 1e-9 * s[0]))
    return Vh[len(s) - k:]


def icosphere(levels):
    verts = [v / np.linalg.norm(v) for v in Vp]
    faces = list(FACES)
    for _ in range(levels):
        mid, new = {}, []

        def m(i, j):
            key = (min(i, j), max(i, j))
            if key not in mid:
                x = verts[i] + verts[j]
                verts.append(x / np.linalg.norm(x))
                mid[key] = len(verts) - 1
            return mid[key]

        for a, b, c in faces:
            ab, bc, ca = m(a, b), m(b, c), m(c, a)
            new += [(a, ab, ca), (b, bc, ab), (c, ca, bc), (ab, bc, ca)]
        faces = new
    return np.array(verts), np.array(faces)


SV, ST = icosphere(6)


def degree(U):
    a, b, c = U[ST[:, 0]], U[ST[:, 1]], U[ST[:, 2]]
    num = np.einsum("ij,ij->i", a, np.cross(b, c))
    den = 1 + np.einsum("ij,ij->i", a, b) + np.einsum("ij,ij->i", b, c) + np.einsum("ij,ij->i", c, a)
    return 2 * np.arctan2(num, den).sum() / (4 * np.pi)


print(f"triangulation: {len(ST)} faces; identity map degree {degree(SV):+.6f}")
seen = {}
for label, targets, r5, count in (("twin (rho -> rho')", Rm, {2, 3}, 12),
                                  ("control (rho -> rho)", Rp, {1, 4}, 8)):
    B = equivariant_maps(targets)
    print(f"{label}: {len(B)}-dimensional space of equivariant maps of degree <= 7")
    found, tries = [], 0
    while len(found) < count and tries < 10 * count:
        tries += 1
        C = (rng.normal(size=len(B)) @ B).reshape(3, M)
        P = mono(SV) @ C.T
        norms = np.linalg.norm(P, axis=1)
        if norms.min() < 1e-3 * norms.max():
            continue
        d = degree(P / norms[:, None])
        assert abs(d - round(d)) < 1e-6, f"non-integral degree {d}"
        found.append((int(round(d)), norms.min() / norms.max()))
    for d, ratio in found:
        ok = d % 2 == 1 and d % 5 in r5 and d % 3 != 0
        print(f"  degree {d:+4d}  min|P|/max|P| {ratio:.3f}  odd, {'+-2' if r5 == {2, 3} else '+-1'} mod 5, prime to 3: {ok}")
    print(f"  drawn {tries}, kept {len(found)} (dropped maps nearly vanishing on the sphere)")
    seen[frozenset(r5)] = [d for d, _ in found]

# Mutation arm: each congruence must reject the other family's degrees.
twin, ctrl = seen[frozenset({2, 3})], seen[frozenset({1, 4})]
print("twin congruence rejects every control degree:", all(d % 5 not in {2, 3} for d in ctrl))
print("control congruence rejects every twin degree:", all(d % 5 not in {1, 4} for d in twin))
