#!/usr/bin/env python3
"""
w_star_proof.py: the checks behind the proof that W_* <= arctan(3 - sqrt 5)/2 at every pose,
with equality at 30 double lunes.  The argument is on the page self-intersection-width.md.

  E  exact arithmetic in Q(sqrt 5)(cos theta).  At the pose b = M, N = P every axis satisfies
     the entry inequality at T = tan(theta/2), ten of them with equality.  Also the exact values
     the proof quotes: tan(theta) = 3 - sqrt 5, and the triangle a, a', v with its right angle at v
     and its angles pi/3 and pi/5 at a and a'.
  I  interval arithmetic for the proof's numerical comparisons: (a), (b), (c) and (1) to (4).
  S  a float scan of the two-axis lemma itself over one Moebius triangle, with two mutation arms
     and one control.

Standard library, numpy, mpmath.  Run from the directory holding w_star.py:
    python3 -u w_star_proof.py          all three parts
    python3 -u w_star_proof.py quick    parts E and I only (seconds)
"""
import itertools
import math
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

import w_star as ws

iv = mp.iv
iv.dps = 50


# ------------------------------------------------------------------ exact field Q(sqrt 5)
class Q5:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q5) else Q5(x)

    def __add__(self, o):
        o = Q5.of(o)
        return Q5(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-Q5.of(o))

    def __rsub__(self, o):
        return Q5.of(o) - self

    def __mul__(self, o):
        o = Q5.of(o)
        return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 5 * self.b * self.b
        assert n != 0
        return Q5(self.a / n, -self.b / n)

    def __truediv__(self, o):
        return self * Q5.of(o).inv()

    def __rtruediv__(self, o):
        return Q5.of(o) * self.inv()

    def __eq__(self, o):
        o = Q5.of(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        d = a * a - 5 * b * b          # a and b of opposite sign
        if a > 0:
            return (d > 0) - (d < 0)
        return (d < 0) - (d > 0)

    def __abs__(self):
        return self if self.sign() >= 0 else -self

    def __float__(self):
        return float(self.a) + float(self.b) * 5 ** 0.5

    def to_iv(self):
        return iv.mpf(self.a.numerator) / self.a.denominator + iv.sqrt(5) * iv.mpf(self.b.numerator) / self.b.denominator

    def __repr__(self):
        return f"({self.a} + {self.b}*sqrt5)"


def rat_sqrt(q):
    q = Fr(q)
    if q < 0:
        return None
    n, d = math.isqrt(q.numerator), math.isqrt(q.denominator)
    return Fr(n, d) if n * n == q.numerator and d * d == q.denominator else None


def q5_sqrt(z):
    """the positive square root of z in Q(sqrt 5), or an error if z is not a square there."""
    assert z.sign() > 0
    s = rat_sqrt(z.a * z.a - 5 * z.b * z.b)
    assert s is not None, f"{z} is not a square in Q(sqrt 5)"
    for x2 in ((z.a + s) / 2, (z.a - s) / 2):
        x = rat_sqrt(x2)
        if x is None or x == 0:
            continue
        r = Q5(x, z.b / (2 * x))
        if r * r == z:
            return abs(r)
    if z.b == 0:
        y = rat_sqrt(z.a / 5)
        if y is not None:
            return Q5(0, y)
    raise AssertionError(f"{z} is not a square in Q(sqrt 5)")


PHI = Q5(Fr(1, 2), Fr(1, 2))
ZERO, ONE = Q5(0), Q5(1)


def qmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def exact_2I():
    els = []
    for i in range(4):
        for s in (1, -1):
            v = [ZERO] * 4
            v[i] = Q5(s)
            els.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=4):
        els.append(tuple(Q5(Fr(s, 2)) for s in signs))
    base = [ZERO, Q5(Fr(1, 2)), PHI / 2, ONE / (2 * PHI)]
    for perm in itertools.permutations(range(4)):
        if sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j]) % 2:
            continue
        for signs in itertools.product((1, -1), repeat=3):
            v, k = [ZERO] * 4, 0
            for pos, src in enumerate(perm):
                val = base[src]
                if not (val == ZERO):
                    val = val * signs[k]
                    k += 1
                v[pos] = val
            els.append(tuple(v))
    return els


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def exact_axes(G):
    half = Q5(Fr(1, 2))
    axes = []
    for g in G:
        r = g[1:]
        if all(c == ZERO for c in r):
            continue
        m = 2 if g[0] == ZERO else (3 if abs(g[0]) == half else 5)
        for ax in axes:
            if all(c == ZERO for c in cross(r, ax[0])):
                assert ax[1] == m
                break
        else:
            axes.append((r, m))
    return axes


def part_E():
    print("Part E: exact arithmetic")
    G = exact_2I()
    S = set(G)
    assert len(G) == 120 and len(S) == 120
    assert all(qmul(x, y) in S for x in G for y in G[::5]) and all(qmul(y, x) in S for x in G for y in G[::5])
    print("  2I: 120 exact elements, closed (products with every fifth element, both sides)")
    axes = exact_axes(G)
    cnt = {m: sum(1 for _, k in axes if k == m) for m in (2, 3, 5)}
    assert (len(axes), cnt[2], cnt[3], cnt[5]) == (31, 15, 10, 6)
    print(f"  axes: 31 = {cnt[2]} + {cnt[3]} + {cnt[5]}")

    # P a two-fold axis of unit raw length; a three-fold and a' five-fold orthogonal to it, adjacent
    rP = next(r for r, m in axes if m == 2 and dot(r, r) == ONE)
    in3 = [r for r, m in axes if m == 3 and dot(r, rP) == ZERO]
    in5 = [r for r, m in axes if m == 5 and dot(r, rP) == ZERO]
    assert len(in3) == 2 and len(in5) == 2
    best = None
    for r3 in in3:
        for r5 in in5:
            c2 = dot(r3, r5) * dot(r3, r5) / (dot(r3, r3) * dot(r5, r5))
            if best is None or (c2 - best[0]).sign() > 0:
                best = (c2, r3, r5)
    c2, ra, rb = best
    if dot(ra, rb).sign() < 0:
        rb = tuple(-c for c in rb)
    Na, Nb, ab = dot(ra, ra), dot(rb, rb), dot(ra, rb)
    assert c2 == (5 + 2 * Q5(0, 1)) / 15
    t = 3 - Q5(0, 1)                                    # tan(theta)
    assert (1 - c2) == c2 * t * t
    print("  cos^2(theta) = (5 + 2 sqrt 5)/15 and tan(theta) = 3 - sqrt 5 for the adjacent pair: exact")

    # the two-fold vertex v of a Moebius triangle on the edge a a': exact right angle at v
    rv = max((r for r, m in axes if m == 2),
             key=lambda r: float(dot(r, ra) * dot(r, ra) / (dot(r, r) * Na)) + float(dot(r, rb) * dot(r, rb) / (dot(r, r) * Nb)))
    cl3 = dot(rv, ra) * dot(rv, ra) / (dot(rv, rv) * Na)      # cos^2 of the side a v
    cl5 = dot(rv, rb) * dot(rv, rb) / (dot(rv, rv) * Nb)      # cos^2 of the side a' v
    assert cl3 * cl5 == c2, "cos(theta) = cos(lambda3) cos(lambda5) fails"
    tl3, tl5 = (1 - cl3) / cl3, (1 - cl5) / cl5
    assert tl3 == ONE / (PHI * PHI * PHI * PHI) and tl5 == ONE / (PHI * PHI)
    print("  the triangle a, a', v: cos(theta) = cos(lambda3) cos(lambda5) exactly (right angle at v);"
          " tan(lambda3) = phi^-2, tan(lambda5) = phi^-1")
    # In a right spherical triangle the cosine of an acute angle is tan(adjacent leg)/tan(hypotenuse).
    # So the angle at a is pi/3 exactly when tan^2(lambda3) = tan^2(theta)/4, and the angle at a' is
    # pi/5 exactly when tan^2(lambda5) = (phi/2)^2 tan^2(theta), cos(pi/5) being phi/2.
    assert tl3 == t * t / 4 and tl5 == PHI * PHI * t * t / 4
    print("  its angles at a and a' are pi/3 and pi/5 exactly: tan(lambda3) = tan(theta)/2,"
          " tan(lambda5) = (phi/2) tan(theta)")

    # the entry inequality at the pose b = M = (a + a')/|a + a'|, N = P, T = tan(theta/2):
    #   Xi(n) = cos^2 W0 - n_b^2 - sin^2 W0 n_N^2 - c_n sin(theta) |n_N| >= 0,
    # times 2(1 + C), C = cos(theta), written p + q C with p, q in Q(sqrt 5).
    cot2 = {2: ZERO, 3: Q5(Fr(1, 3)), 5: PHI * PHI / (4 - PHI * PHI)}     # cot^2(pi/m); cos(pi/5) = phi/2
    zero, pos, neg = [], [], []
    for r, m in axes:
        Nn = dot(r, r)
        nP = abs(dot(r, rP))                                   # |n_N| sqrt(Nn), P of unit length
        nu = nP * nP / Nn                                      # n_N^2
        kappa = ZERO if m == 2 else q5_sqrt(cot2[m] / Nn)      # c_n / sqrt(Nn), in Q(sqrt 5)
        alpha = dot(r, ra) * dot(r, ra) / (Nn * Na) + dot(r, rb) * dot(r, rb) / (Nn * Nb)
        beta = 2 * dot(r, ra) * dot(r, rb) / (Nn * ab)
        p = 1 + c2 - alpha - (1 - c2) * nu - 2 * t * kappa * nP * c2
        q = 2 - beta - 2 * t * kappa * nP
        sp, sq = p.sign(), q.sign()
        if sp == 0 and sq == 0:
            s = 0
        elif sp >= 0 and sq >= 0:
            s = 1
        elif sp <= 0 and sq <= 0:
            s = -1
        else:
            d = (p * p - q * q * c2).sign()                    # |p| against |q| C
            s = sp * d if d != 0 else 0
        (zero if s == 0 else pos if s > 0 else neg).append(m)
    print(f"  at b = M, N = P: entry inequality holds with equality for {len(zero)} axes"
          f" ({zero.count(2)} two-fold, {zero.count(3)} three-fold, {zero.count(5)} five-fold),"
          f" strictly for {len(pos)}, fails for {len(neg)}")
    assert (len(zero), len(pos), len(neg)) == (10, 21, 0)
    print("  so W_* = theta/2 exactly at that pose   PASS")
    rfar = next(r for r in in5 if not all(c == ZERO for c in cross(r, rb)))   # the other five-fold axis orthogonal to P
    return {"c2": c2, "cl3": cl3, "cl5": cl5, "ra": ra, "rb": rb, "rv": rv, "rP": rP, "rfar": rfar}


def part_I(ex):
    print("Part I: interval arithmetic, 50 digits")
    # mpmath's interval context has sin, cos, tan, sqrt and atan2; the inverse functions come from atan2.
    i_atan = lambda x: iv.atan2(x, iv.mpf(1))
    i_asin = lambda x: iv.atan2(x, iv.sqrt(1 - x * x))
    i_acos = lambda x: iv.atan2(iv.sqrt(1 - x * x), x)
    s5 = iv.sqrt(5)
    theta = i_atan(3 - s5)
    W0 = theta / 2
    c3 = 1 / iv.sqrt(3)
    c5 = iv.sqrt((PHI * PHI / (4 - PHI * PHI)).to_iv())            # cot(pi/5), from cos(pi/5) = phi/2
    cos36 = (PHI / 2).to_iv()
    pi = iv.pi

    def show(x):
        return mp.nstr(mp.mpf(x.mid), 12)

    def gt(x, y, label):
        ok = bool((x - y).a > 0)
        print(f"    {label}: {show(x)} > {show(y)}   {'PASS' if ok else 'FAIL'}")
        assert ok

    print(f"  W0 = {show(W0)} rad, theta = {show(theta)} rad")

    xi = lambda d, c: (iv.sin(d) ** 2 - iv.sin(W0) ** 2) / (c * iv.sin(theta) * iv.sin(d))
    h5 = lambda x: iv.cos(theta) * iv.cos(x) + cos36 * iv.sin(theta) * iv.sin(x)        # lower bound for cos d
    h3 = lambda x: iv.cos(theta) * iv.cos(x) + iv.sin(theta) * iv.sin(x) / 2            # lower bound for cos d'
    gt(h5(theta), h5(W0), "(a) h5(theta) against h5(W0)")
    dmax = i_acos(h5(W0))
    gt(h3(W0), h3(dmax), "(b) h3(W0) against h3(d_max)")
    dpmax = i_acos(h3(dmax))
    x3, x5 = xi(dmax, c3), xi(dpmax, c5)
    gt(iv.mpf(1), x3, "(c) 1 against xi_3(d_max)")
    gt(iv.mpf(1), x5, "(c) 1 against xi_5(d'_max)")
    bbar = i_asin(x3) + i_asin(x5)
    print(f"  d_max = {show(dmax * 180 / pi)} deg, d'_max = {show(dpmax * 180 / pi)} deg,"
          f" beta_bar = {show(bbar)} rad = {show(bbar * 180 / pi)} deg")
    gt(7 * pi / 15, bbar, "(1) 7pi/15 against beta_bar")
    sstar = 2 * bbar * iv.sin(W0) / (pi * iv.sqrt(3))
    g = 2 * i_acos(iv.sin(W0) / iv.sin(W0 + sstar / 2))
    print(f"  sigma* = {show(sstar)} rad")
    gt(g, bbar, "(2) g(sigma*) against beta_bar")
    gt(pi / 2, theta + (dmax + dpmax - theta) / 2, "(3) pi/2 against theta + sigma_max/2")
    gt(dmax + dpmax - theta, sstar, "(4) sigma_max against sigma*")
    print("  all comparisons certified   PASS")
    return float(mp.mpf(W0.mid))


def part_S(ex, W0):
    print("Part S: the two-axis lemma scanned over one Moebius triangle (floats)")
    f = lambda r: np.array([float(c) for c in r]) / math.sqrt(float(dot(r, r)))
    a, ap, v = f(ex["ra"]), f(ex["rb"]), f(ex["rv"])
    if v @ a < 0:
        v = -v
    assert v @ ap > 0
    t0 = math.tan(W0)
    psi = np.deg2rad(np.arange(0.0, 180.0, 0.1))
    nb = 300
    ctrue = np.array([1 / math.sqrt(3), 1 / math.tan(math.pi / 5)])
    # Two arms that must break the bound, each for its own reason:
    #   "three-fold read as two-fold": with c = 0 the window on N opens like a square root, as the
    #       deficit of the angle at b does, so the two constraints become compatible off the midpoint;
    #   "wrong five-fold axis": the lemma is about the adjacent pair; the other five-fold axis in
    #       the same plane is far from the triangle and constrains nothing near it.
    # One control that must leave the bound in place:
    #   "five-fold read as three-fold": lowering c_5 to c_3 widens the second window, but both windows
    #       still open linearly while the deficit of the angle at b opens like a square root.  The
    #       page's proof uses the value of c_5 in its comparisons; this records that the bound does not.
    CONTROL = "five-fold read as three-fold"
    AXS = {"true": np.array([a, ap]), "three-fold read as two-fold": np.array([a, ap]),
           "wrong five-fold axis": np.array([a, f(ex["rfar"])]), CONTROL: np.array([a, ap])}
    C = {"true": ctrue, "three-fold read as two-fold": np.array([0.0, ctrue[1]]), "wrong five-fold axis": ctrue,
         CONTROL: np.array([ctrue[0], ctrue[0]])}
    worst = {k: -1.0 for k in C}
    arg, count = None, 0
    for i in range(nb + 1):
        bs = np.array([(i / nb) * v + (j / nb) * a + (1 - i / nb - j / nb) * ap for j in range(nb + 1 - i)])
        bs /= np.linalg.norm(bs, axis=1, keepdims=True)
        tmp = np.where(np.abs(bs[:, :1]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
        u = np.cross(bs, tmp)
        u /= np.linalg.norm(u, axis=1, keepdims=True)
        w = np.cross(bs, u)
        Nn = np.cos(psi)[None, :, None] * u[:, None, :] + np.sin(psi)[None, :, None] * w[:, None, :]
        Bb = np.broadcast_to(bs[:, None, :], Nn.shape)
        Ee = np.cross(Bb, Nn)
        count += Nn.shape[0] * Nn.shape[1]
        for name, cc in C.items():
            F = np.min(ws.T_closed(Ee, Bb, Nn, AXS[name], cc), axis=-1)
            if F.max() > worst[name]:
                worst[name] = float(F.max())
                if name == "true":
                    k = np.unravel_index(int(np.argmax(F)), F.shape)
                    arg = bs[k[0]]
    M = (a + ap) / np.linalg.norm(a + ap)
    print(f"  poses: {count} (b on a {nb}-step barycentric grid of the triangle, N every 0.1 deg)")
    off = np.degrees(np.arccos(min(1.0, abs(arg @ M))))
    print(f"  tan(theta/2) = {t0:.9f};  the largest min(T(a), T(a')) does not exceed it by more than 1e-12"
          f"   {'PASS' if worst['true'] <= t0 + 1e-12 else 'FAIL'}")
    print(f"  it reaches tan(theta/2) to within 1e-12, within 0.001 deg of the edge midpoint M: "
          f"{worst['true'] >= t0 - 1e-12 and off < 1e-3}")
    arms = [k for k in C if k not in ("true", CONTROL)]
    for name in arms:
        print(f"  mutation ({name}): largest value {worst[name]:.6f}"
              f"   {'exceeds the bound, as it should' if worst[name] > t0 + 1e-6 else 'NOT DETECTED'}")
    print(f"  control ({CONTROL}): the largest value still does not exceed tan(theta/2) by more than 1e-12: "
          f"{worst[CONTROL] <= t0 + 1e-12}")
    assert abs(worst["true"] - t0) <= 1e-12 and off < 1e-3 and all(worst[k] > t0 + 1e-6 for k in arms)
    assert worst[CONTROL] <= t0 + 1e-12


if __name__ == "__main__":
    ex = part_E()
    W0 = part_I(ex)
    if "quick" in sys.argv[1:]:
        print("Part S: skipped (quick)")
    else:
        part_S(ex, W0)
