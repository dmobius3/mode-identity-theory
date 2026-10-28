#!/usr/bin/env python3
"""Companion to s3-2i-oph-dictionary.md, section III. Homogeneous polynomial maps F: C^2 -> C^2 of degree a with F(Q(g)z) = Q'(g)F(z) for
every g in 2I. Q is the defining doublet (2I as unit quaternions over Q(sqrt5), written as
SU(2) matrices) and Q' its Galois twin (sqrt5 -> -sqrt5, i fixed). Reports the dimension of
that space for a = 1..11 and, at a = 7, the equivariance residual over all 120 elements and
whether the two components share a zero on CP^1. numpy only.
"""
import numpy as np

R5 = 5 ** 0.5


def quat(a, b, c, d):
    return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


def gens(s5):
    p = (1 + s5) / 2  # phi, or its conjugate 1 - phi
    return [quat(.5, .5, .5, .5), quat(p / 2, (p - 1) / 2, .5, 0)]


# Close the pair (Q, Q') together, so element k of one list is the twin of element k of the other.
pairs = [(np.eye(2, dtype=complex), np.eye(2, dtype=complex))]
frontier = list(pairs)
while frontier:
    new = []
    for x, xt in frontier:
        for g, gt in zip(gens(R5), gens(-R5)):
            y, yt = g @ x, gt @ xt
            if not any(np.allclose(y, e) for e, _ in pairs):
                pairs.append((y, yt))
                new.append((y, yt))
    frontier = new
E = [p[0] for p in pairs]
Et = [p[1] for p in pairs]
print("group orders:", len(E), len({tuple(np.round(m, 9).ravel()) for m in Et}))
g10, g10t = gens(R5)[1], gens(-R5)[1]
print(f"trace of the order-10 generator: Q {np.trace(g10).real:.9f}, Q' {np.trace(g10t).real:.9f}")

rng = np.random.default_rng(0)
Z = rng.normal(size=(60, 2)) + 1j * rng.normal(size=(60, 2))


def mono(z, a):
    return np.array([z[0] ** (a - m) * z[1] ** m for m in range(a + 1)])


def system(a, gs, gts):
    rows = []
    for g, gt in zip(gs, gts):
        for z in Z:
            mz, m0 = mono(g @ z, a), mono(z, a)
            for comp in range(2):
                row = np.zeros(2 * (a + 1), dtype=complex)
                row[comp * (a + 1):(comp + 1) * (a + 1)] += mz
                row[:a + 1] -= gt[comp, 0] * m0
                row[a + 1:] -= gt[comp, 1] * m0
                rows.append(row)
    return np.array(rows)


for a in range(1, 12):
    sv = np.linalg.svd(system(a, gens(R5), gens(-R5)), compute_uv=False)
    print(f"a = {a:2d}: dimension of degree-a maps carrying Q to Q' = {int(np.sum(sv < 1e-9 * sv[0]))}")

a = 7
_, _, Vh = np.linalg.svd(system(a, gens(R5), gens(-R5)))
x = Vh[-1].conj()
c1, c2 = x[:a + 1], x[a + 1:]


def F(z):
    return np.array([c1 @ mono(z, a), c2 @ mono(z, a)])


W = rng.normal(size=(20, 2)) + 1j * rng.normal(size=(20, 2))
res = max(np.linalg.norm(F(g @ v) - gt @ F(v)) / np.linalg.norm(F(v))
          for g, gt in zip(E, Et) for v in W)
print(f"a = 7: equivariance residual over all 120 elements {res:.1e}")
# Components as binary forms in t = z1/z2, highest power first. A vanishing t^7 coefficient
# is a zero at t = infinity, the point [1:0].
scale = max(np.abs(x))
print(f"a = 7: t^7 coefficients |F1| {abs(c1[0]):.1e}, |F2| {abs(c2[0]):.1e} "
      f"(a zero at [1:0] for a component whose coefficient is ~0)")


def finite_roots(c):
    k = 0
    while abs(c[k]) < 1e-12 * scale:
        k += 1
    return np.roots(c[k:])


r1, r2 = finite_roots(c1), finite_roots(c2)
print(f"a = 7: finite roots per component {len(r1)}, {len(r2)}; "
      f"closest finite root of F1 to one of F2 {min(abs(p - q) for p in r1 for q in r2):.3f}")


def sylvester(p, q):
    m, k = len(p) - 1, len(q) - 1
    S = np.zeros((m + k, m + k), dtype=complex)
    for i in range(k):
        S[i, i:i + m + 1] = p
    for i in range(m):
        S[k + i, i:i + k + 1] = q
    return S


sv = np.linalg.svd(sylvester(c1 / np.linalg.norm(c1), c2 / np.linalg.norm(c2)), compute_uv=False)
print(f"a = 7: Sylvester matrix, smallest over largest singular value {sv[-1] / sv[0]:.3e}")
