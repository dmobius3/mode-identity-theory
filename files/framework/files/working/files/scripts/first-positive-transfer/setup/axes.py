#!/usr/bin/env python3
"""The 2I convention and the pinned placements for G4, checked exactly (sympy).
2I: the 120 unit icosians, the 24 Hurwitz units and the 96 elements (0, ±1, ±φ⁻¹, ±φ)/2 under even permutations of the
coordinates (1, i, j, k). The icosahedral group I acts on Im ℍ by conjugation. Checks: the group has 120 elements and is
closed; conjugation gives 60 rotations; the pinned 2-, 3- and 5-fold poles are fixed axes of rotations of those orders;
each pinned azimuth is orthogonal to its pole; the generic pole's least angle to any symmetry axis."""
import itertools, sympy as sp

phi = (1 + sp.sqrt(5)) / 2
ip = 1 / phi


def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)


def even_perms(n):
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        if inv % 2 == 0:
            yield p


els = set()
for i in range(4):
    for s in (1, -1):
        v = [0, 0, 0, 0]; v[i] = s; els.add(tuple(sp.nsimplify(x) for x in v))
for signs in itertools.product((1, -1), repeat=4):
    els.add(tuple(sp.Rational(s, 2) for s in signs))
base = (0, 1, ip, phi)
for p in even_perms(4):
    for signs in itertools.product((1, -1), repeat=3):
        vals = [base[p[k]] for k in range(4)]
        nz = [k for k in range(4) if vals[k] != 0]
        v = [0, 0, 0, 0]
        for k, s in zip(nz, signs):
            v[k] = sp.nsimplify(s * vals[k] / 2)
        els.add(tuple(sp.simplify(x) for x in v))
els = {tuple(sp.nsimplify(sp.simplify(x)) for x in e) for e in els}
print("elements:", len(els))
key = lambda q: tuple(float(x) for x in q)
fl = {tuple(round(x, 9) for x in key(e)) for e in els}
closed = all(tuple(round(x, 9) for x in key(qmul(a, b))) in fl for a in list(els)[:40] for b in list(els)[:40])
print("closed (sampled 40x40):", closed, "| all unit:", all(abs(sum(float(x)**2 for x in e) - 1) < 1e-12 for e in els))


def rot(q):
    """The rotation of Im H by conjugation x -> q x q̄."""
    qc = (q[0], -q[1], -q[2], -q[3])
    cols = []
    for e in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)):
        r = qmul(qmul(q, e), qc)
        cols.append([sp.simplify(r[1]), sp.simplify(r[2]), sp.simplify(r[3])])
    return sp.Matrix(cols).T


rots = {}
for e in els:
    M = rot(e)
    rots[tuple(round(float(x), 9) for x in M)] = M
print("distinct rotations:", len(rots))


def order(M):
    P = sp.eye(3)
    for k in range(1, 11):
        P = sp.simplify(P * M)
        if P == sp.eye(3):
            return k
    return None


def is_axis_of_order(u, n):
    u = sp.Matrix(u)
    for M in rots.values():
        if order(M) == n and sp.simplify(M * u - u) == sp.zeros(3, 1):
            return True
    return False


u2 = (1, 0, 0)
u3 = (1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3))
n5 = sp.sqrt(1 + ip**2)
u5 = (ip / n5, 1 / n5, 0)
c2, c3, c5 = (0, 1, 0), (1 / sp.sqrt(2), -1 / sp.sqrt(2), 0), (0, 0, 1)
pg, cg = (1 / sp.sqrt(14), 2 / sp.sqrt(14), 3 / sp.sqrt(14)), (2 / sp.sqrt(5), -1 / sp.sqrt(5), 0)
dot = lambda a, b: sp.simplify(sum(x * y for x, y in zip(a, b)))
print("2-fold pole i:", is_axis_of_order(u2, 2), "| 3-fold pole (i+j+k)/sqrt3:", is_axis_of_order(u3, 3), "| 5-fold pole (phi^-1 i + j)/n:", is_axis_of_order(u5, 5))
print("azimuths orthogonal:", [dot(u2, c2), dot(u3, c3), dot(u5, c5), dot(pg, cg)], "| unit:", [sp.simplify(dot(v, v)) for v in (u2, u3, u5, c2, c3, c5, pg, cg)])
axes = []
for M in rots.values():
    if M == sp.eye(3):
        continue
    ev = (M - sp.eye(3)).nullspace()
    if ev:
        a = [float(x) for x in ev[0]]
        n = sum(x * x for x in a) ** 0.5
        axes.append([x / n for x in a])
import math
pgf = [float(x) for x in pg]
least = min(math.degrees(math.acos(min(1.0, abs(sum(x * y for x, y in zip(pgf, a)))))) for a in axes)
print("generic pole: least angle to any symmetry axis = %.2f degrees (over %d axis directions)" % (least, len(axes)))
