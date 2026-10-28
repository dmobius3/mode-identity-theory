#!/usr/bin/env python3
"""Degrees of the radial frame maps of the twelve-port carrier and its Galois twin, and the
rotation action each frame carries. Companion to s3-2i-oph-dictionary.md, section III.

Ports: the twelve directions given by the cyclic permutations of (0, +-1, +-p), with p = phi
for the convex frame and p = 1 - phi (the image of phi under sqrt5 -> -sqrt5, applied to every
coefficient) for the twin frame. Edges join nearest ports of the convex frame; faces are the
twenty mutually adjacent triples, oriented outward in the convex frame (the convex-positive
orientation). The radial map of a frame sends the face (i, j, k) onto the spherical triangle
spanned by its three port vectors; its degree is a signed preimage count at a regular
direction. numpy only.
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
assert (A.sum(1) == 5).all()
F = []
for i, j, k in itertools.combinations(range(n), 3):
    if A[i, j] and A[j, k] and A[i, k]:
        F.append((i, j, k) if np.linalg.det(Vp[[i, j, k]]) > 0 else (i, k, j))
assert len(F) == 20


def degree(V, y):
    total = 0
    for f in F:
        M = V[list(f)].T
        c = np.linalg.solve(M, y)
        assert np.all(np.abs(c) > 1e-9), "direction not regular"
        if np.all(c > 0):
            total += int(np.sign(np.linalg.det(M)))
    return total


print("degree of the radial map, faces oriented outward in the convex frame")
for y in ([1, 2, 4], [-3, 5, 2], [7, -2, 3]):
    y = np.array(y, float)
    print(f"  direction {y.astype(int).tolist()}: convex frame {degree(Vp, y):+d}, "
          f"twin frame {degree(Vm, y):+d}")

# The sixty rotations of the convex frame, as port permutations: one for each ordered edge
# (a, b), carrying a reference edge (u, w) onto it.
u = 0
w = int(np.flatnonzero(A[u])[0])


def basis(V, a, b):
    return np.array([V[a], V[b], np.cross(V[a], V[b])]).T


perms, Rp = [], []
for a in range(n):
    for b in np.flatnonzero(A[a]):
        R = basis(Vp, a, b) @ np.linalg.inv(basis(Vp, u, w))
        assert np.allclose(R @ R.T, np.eye(3)) and np.isclose(np.linalg.det(R), 1)
        img = (R @ Vp.T).T
        perm = [int(np.flatnonzero(np.all(np.isclose(Vp, x), axis=1))[0]) for x in img]
        perms.append(perm)
        Rp.append(R)
assert len({tuple(p) for p in perms}) == 60

# The same permutations on the twin frame: solve R' V_m[i] = V_m[perm(i)] and test it.
worst, Rm = 0.0, []
for perm in perms:
    X, Y = Vm.T, Vm[perm].T
    R = Y @ X.T @ np.linalg.inv(X @ X.T)
    worst = max(worst, np.abs(R @ X - Y).max(), np.abs(R @ R.T - np.eye(3)).max(),
                abs(np.linalg.det(R) - 1))
    Rm.append(R)
print(f"twin frame realizes the same 60 port permutations by rotations: max residual {worst:.1e}")


def power(perm, k):
    out = list(range(n))
    for _ in range(k):
        out = [perm[i] for i in out]
    return out


def kind(perm):
    """A rotation fixing a port is one-step if it carries a neighbour of that port to an
    adjacent neighbour, two-step otherwise."""
    fixed = [i for i in range(n) if perm[i] == i]
    if len(fixed) == n:
        return "identity"
    if not fixed:
        order = next(k for k in (2, 3) if power(perm, k) == list(range(n)))
        return f"order {order}"
    nb = int(np.flatnonzero(A[fixed[0]])[0])
    return "order 5, one-step" if A[nb, perm[nb]] else "order 5, two-step"


table = {}
for perm, R1, R2 in zip(perms, Rp, Rm):
    t = table.setdefault(kind(perm), [0, set(), set()])
    t[0] += 1
    t[1].add(round(float(np.trace(R1)), 9))
    t[2].add(round(float(np.trace(R2)), 9))
print(f"characters (phi = {PHI:.9f}, 1 - phi = {1 - PHI:.9f})")
for key in ("identity", "order 2", "order 3", "order 5, one-step", "order 5, two-step"):
    size, t1, t2 = table[key]
    print(f"  {key:18s} {size:2d} elements  convex frame {sorted(t1)}  twin frame {sorted(t2)}")
