#!/usr/bin/env python3
"""Rederives the isotropy group of S^3/2I and what it forces on an isometry-invariant covariance. Group theory only: no field,
no spectrum, no CMB quantity.

S^3 = SU(2) as unit quaternions; 2I acts on the left, and a point of the quotient is the coset [x] = 2I x.
  1. 2I is 120 unit quaternions closed under multiplication.
  2. Right multiplication [x] -> [x b] is well defined on cosets, and transitive.
  3. The stabilizer of [1] under it is 2I; b in 2I acts on the tangent space at [1] by Ad(b^-1): the representative of
     [exp(v) b] nearest 1 is exactly b^-1 exp(v) b = exp(Ad(b^-1) v).
  4. The 120 maps Ad(b) are 60 distinct rotations preserving the icosahedron, in classes of rotation angle 0, 2pi/5, 4pi/5,
     2pi/3, pi of sizes 1, 12, 12, 20, 15: the group A5. By homogeneity every point carries a copy.
  5. The A5 content of each spin-l representation, from characters evaluated on those 60 rotations, and which pairs (l, l')
     share an irreducible constituent: by Schur the only pairs an A5-invariant covariance may couple.
  6. Cross-check with step one: the number of A5 invariants at spin l equals the Molien count m_(2l), l = 0 to 40.
"""
import itertools

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
rng = np.random.default_rng(12)


def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def qinv(a):
    return np.array([a[0], -a[1], -a[2], -a[3]])


def key(q):
    return tuple(np.round(q, 9) + 0.0)


def even_perms(v):
    for p in itertools.permutations(range(4)):
        if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0:
            yield tuple(v[i] for i in p)


G = {}
for i in range(4):
    for s in (1.0, -1.0):
        e = np.zeros(4)
        e[i] = s
        G[key(e)] = e
for sg in itertools.product((0.5, -0.5), repeat=4):
    G[key(np.array(sg))] = np.array(sg)
for sg in itertools.product((1, -1), repeat=3):
    for p in even_perms((0.0, 0.5 * sg[0], 0.5 * sg[1] / PHI, 0.5 * sg[2] * PHI)):
        G[key(np.array(p))] = np.array(p)
E = list(G.values())
closed = all(key(qmul(a, b)) in G for a in E for b in E)
print(f"1. 2I: {len(E)} unit quaternions (norms 1 to {max(abs(np.linalg.norm(q) - 1) for q in E):.0e}); closed under multiplication: {closed}")


def coset(x):
    return frozenset(key(qmul(g, x)) for g in E)


def rand_unit():
    q = rng.normal(size=4)
    return q / np.linalg.norm(q)


ok_desc = all(coset(qmul(qmul(g, x), b)) == coset(qmul(x, b)) for x, b in ((rand_unit(), rand_unit()) for _ in range(20)) for g in E[:40])
x = rand_unit()
print(f"2. right multiplication is well defined on cosets: [(g x) b] = [x b] for 20 random (x, b) and 40 g each: {ok_desc}; "
      f"transitive: [x x^-1] = [1] for random x: {coset(qmul(x, qinv(x))) == coset(np.array([1.0, 0, 0, 0]))}")
one = coset(np.array([1.0, 0, 0, 0]))
stab_in = all(coset(b) == one for b in E)
stab_out = not any(coset(rand_unit()) == one for _ in range(200))


def qexp(v):
    t = np.linalg.norm(v)
    return np.concatenate([[np.cos(t)], np.sin(t) * v / t])


def ad(b):
    return np.array([qmul(qmul(b, np.concatenate([[0.0], e])), qinv(b))[1:] for e in np.eye(3)]).T


worst = 0.0
for b in E:
    v = 1e-3 * rand_unit()[1:]
    y = qmul(qexp(v), b)
    reps = [qmul(g, y) for g in E]
    near = min(reps, key=lambda r: np.linalg.norm(r - np.array([1.0, 0, 0, 0])))
    worst = max(worst, np.linalg.norm(near - qexp(ad(qinv(b)) @ v)))
print(f"3. stabilizer of [1]: every b in 2I fixes it ({stab_in}), no random b does ({stab_out}); b in 2I moves the tangent "
      f"space at [1] by Ad(b^-1): the representative of [exp(v) b] nearest 1 equals exp(Ad(b^-1) v) to {worst:.0e}")
R = {}
for b in E:
    R[key(ad(b).flatten())] = ad(b)
rots = list(R.values())
ico = [np.array(v, float) for c in ((0, 1, PHI), (1, PHI, 0), (PHI, 0, 1)) for v in itertools.product(*[(s, -s) if s else (0,) for s in c])]
icoset = {key(np.append(v, 0.0)) for v in ico}
keeps = all({key(np.append(Rm @ v, 0.0)) for v in ico} == icoset for Rm in rots)
ang = [float(np.arccos(np.clip((np.trace(Rm) - 1) / 2, -1, 1))) for Rm in rots]
classes = {}
for a in ang:
    k = round(a / np.pi, 6)
    classes[k] = classes.get(k, 0) + 1
names = {0.0: "0", 0.4: "2pi/5", 0.8: "4pi/5", round(2 / 3, 6): "2pi/3", 1.0: "pi"}
print(f"4. Ad(2I): {len(rots)} distinct rotations; the {len(ico)} vertices of the icosahedron are permuted by all of them: {keeps}; "
      f"rotation-angle classes {[(names.get(k, k), n) for k, n in sorted(classes.items())]}")
TABLE = {"1": {0.0: 1, 0.4: 1, 0.8: 1, round(2 / 3, 6): 1, 1.0: 1},
         "3": {0.0: 3, 0.4: PHI, 0.8: 1 - PHI, round(2 / 3, 6): 0, 1.0: -1},
         "3'": {0.0: 3, 0.4: 1 - PHI, 0.8: PHI, round(2 / 3, 6): 0, 1.0: -1},
         "4": {0.0: 4, 0.4: -1, 0.8: -1, round(2 / 3, 6): 1, 1.0: 0},
         "5": {0.0: 5, 0.4: 0, 0.8: 0, round(2 / 3, 6): -1, 1.0: 1}}
DIM = {"1": 1, "3": 3, "3'": 3, "4": 4, "5": 5}


def chi_spin(l, a):
    return 2 * l + 1 if a < 1e-12 else np.sin((l + 0.5) * a) / np.sin(a / 2)


def content(l):
    out = {}
    for rho, tab in TABLE.items():
        m = sum(chi_spin(l, a) * tab[round(a / np.pi, 6)] for a in ang) / 60
        assert abs(m - round(m)) < 1e-9
        if round(m):
            out[rho] = int(round(m))
    assert sum(n * DIM[r] for r, n in out.items()) == 2 * l + 1
    return out


def fmt(c):
    return " + ".join((f"{n}x" if n > 1 else "") + r for r, n in c.items())


print("5. A5 content of spin l. An A5-invariant covariance is a scalar on each constituent that appears once and a positive matrix on\n"
      "   the multiplicity of one that repeats (first at l = 8); a spin whose content is a single irreducible is forced isotropic:")
C = {l: content(l) for l in range(0, 41)}
for l in range(0, 11):
    print(f"   l = {l:2d}: {fmt(C[l]):22s} {'forced isotropic' if sum(C[l].values()) == 1 else 'anisotropy allowed'}")
print("   pairs (l, l') that may be coupled (share a constituent) and that are forced to zero, for 1 <= l < l' <= 6:")
for l in range(1, 7):
    row = []
    for lp in range(l + 1, 7):
        sh = sorted(set(C[l]) & set(C[lp]))
        row.append(f"({l},{lp}) {'shares ' + '+'.join(sh) if sh else 'zero'}")
    if row:
        print("   " + "; ".join(row))
c = np.zeros(81, dtype=int)
c[0] = 1
for s in (12, 20):
    for r in range(s):
        c[r::s] = np.cumsum(c[r::s])
m = c.copy()
m[30:] += c[:-30]
agree = all(C[l].get("1", 0) == m[2 * l] for l in range(0, 41))
print(f"6. A5 invariants at spin l equal the Molien count m_(2l) for l = 0 to 40: {agree} "
      f"(l = 6, 10, 15: {[C[l].get('1', 0) for l in (6, 10, 15)]}; l = 30: {C[30].get('1', 0)}); first m_N > 1 at N = "
      f"{next(n for n in range(81) if m[n] > 1)}")
