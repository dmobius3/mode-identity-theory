#!/usr/bin/env python3
"""Checks behind carrier-edge-regimes.md (§§I-IV), with R kept symbolic where it can be and R = 1 elsewhere.

Checks (exit 1 on any failure):
  E1  each named energy is (κ/2)H² + κ̄K + γ for its stated (κ, κ̄, γ), with H = tr A and K = 1/R² + det A, and
      Γ = γ + κ̄/R² takes the stated value: 0 for ∫H², ∫|A|² and ½∫|Å|², 1/R² for ∫(H²/4 + 1/R²), γ for area
  E2  Lemma 1's first order: each named density has zero gradient in the principal curvatures at A = 0
  E3  Lemma 2's sign convention: on a geodesic disc of radius ρ in S²(R), d(Γ·Area + σL)/dρ = (Γ + σk_g)L with
      k_g = cot(ρ/R)/R, positive toward the disc
  E4  Lemma 3, geodesic legs: the chord saves 2ε(1 − sin(θ/2)) + O(ε³) and its triangle is ½ε² sin θ + O(ε⁴)
      (observed orders 3 and 4 at θ = 0.5, 1, 2, 3, in 50-digit arithmetic)
  E5  the pinch's passes, from the band's rectangle with the Möbius gluing (0, w) ~ (πR, −w), placed by the chart
      continued as X(y, −w) beyond the collapsed fibre: each pass turns by 2W/R around a sector of opening π − 2W/R
      that holds no point of the band
  E6  cutting one pass, as a cell complex on S² symmetric under −I: M(W)'s lift is not a manifold at ±N; the cut
      band's lift is a connected manifold with χ = 0 and two boundary cycles, so the cut band is a Möbius band (χ = 0,
      one boundary circle, one-sided), and the closure of its complement lifts to two discs, so it is a closed disc
  E7  a circle of S² that is not a great circle holds no antipodal pair
  E8  (κ/2)H² + κ̄ det A ≥ 0 for every A exactly when −2κ ≤ κ̄ ≤ 0, positive definite strictly inside
  E9  the support S± = span(N, u±, ν), u± = cos(W/R)c ± sin(W/R)d: turning the band's plane by t in the plane of c
      and ν cuts S± in projective lines through the pinch N at half-opening W_t from the turned core, with
      tan(W_t/R) = cos t tan(W/R); turning it in the plane of d and ν gives tan(W'_t/R) = tan(W/R)/cos t; and at
      t = 0, (4RW_t)'' = −2R² sin(2W/R) and (4RW'_t)'' = +2R² sin(2W/R)
  E10 a tube about a projective line of half-width R arctan(ΓR/σ) satisfies σk_g = −Γ, and a tube's edge has length
      2πR cos(W/R)
--arms plants a defect for each check and requires it to fire."""
import math
import sys
from collections import defaultdict

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 50
R = sp.symbols("R", positive=True)
k1, k2 = sp.symbols("k1 k2", real=True)
H, DET = k1 + k2, k1 * k2
K = 1 / R**2 + DET
WIDTHS = (0.3, 0.6, 1.0, 1.4)  # W/R


def named(plant=False):
    """name: (density, κ, κ̄, γ, stated Γ)."""
    return {
        "int H^2": (H**2, 2, 0, 0, 0),
        "int |A|^2": (k1**2 + k2**2, 2, (2 if plant else -2), 2 / R**2, 0),  # planted: κ̄ with the wrong sign
        "int (H^2/4 + 1/R^2)": (H**2 / 4 + 1 / R**2, sp.Rational(1, 2), 0, 1 / R**2, 1 / R**2),
        "(1/2) int |A°|^2": ((k1 - k2) ** 2 / 4, sp.Rational(1, 2), -1, 1 / R**2, 0),
        "area": (sp.Integer(1), 0, 0, 1, 1),
    }


def e1(plant=False):
    ok = True
    for dens, kap, kbar, gam, Gam in named(plant).values():
        ok &= sp.simplify(dens - (kap * H**2 / 2 + kbar * K + gam)) == 0
        ok &= sp.simplify(gam + kbar / R**2 - Gam) == 0 and sp.simplify(dens.subs({k1: 0, k2: 0}) - Gam) == 0
    return bool(ok)


def e2(plant=False):
    H0 = sp.symbols("H0", positive=True)
    dens = [d for d, *_ in named().values()] + ([(H - H0) ** 2] if plant else [])  # planted: spontaneous curvature
    return all(sp.simplify(sp.diff(d, k).subs({k1: 0, k2: 0})) == 0 for d in dens for k in (k1, k2))


def e3(plant=False):
    rho, Gam, sig = sp.symbols("rho Gamma sigma", positive=True)
    area = 2 * sp.pi * R**2 * (1 - sp.cos(rho / R))
    L = 2 * sp.pi * R * sp.sin(rho / R)
    kg = (-1 if plant else 1) * sp.cot(rho / R) / R  # planted: k_g measured away from the disc
    return sp.simplify(sp.diff(Gam * area + sig * L, rho) - (Gam + sig * kg) * L) == 0


def cut(theta, eps):
    theta, eps = mp.mpf(theta), mp.mpf(eps)
    c = mp.acos(mp.cos(eps) ** 2 + mp.sin(eps) ** 2 * mp.cos(theta))
    b = mp.acos((mp.cos(eps) - mp.cos(eps) * mp.cos(c)) / (mp.sin(eps) * mp.sin(c)))
    return 2 * eps - c, theta + 2 * b - mp.pi  # the saving, and the triangle's area (spherical excess)


def e4(plant=False):
    saving = (lambda th: 1 - mp.cos(th / 2)) if plant else (lambda th: 1 - mp.sin(th / 2))  # planted: cos for sin
    for theta in (mp.mpf("0.5"), mp.mpf(1), mp.mpf(2), mp.mpf(3)):
        rL, rA = [], []
        for eps in (mp.mpf("1e-2"), mp.mpf("5e-3"), mp.mpf("2.5e-3")):
            dL, dA = cut(theta, eps)
            rL.append(abs(dL - 2 * eps * saving(theta)))
            rA.append(abs(dA - eps**2 * mp.sin(theta) / 2))
        if min(mp.log(rL[i] / rL[i + 1], 2) for i in range(2)) < 2.9:
            return False
        if min(mp.log(rA[i] / rA[i + 1], 2) for i in range(2)) < 3.9:
            return False
    return True


def chart(y, w, plant=False):
    """The band's rectangle onto the bowtie at N in the unit S², continued as X(y, −w) beyond y = π/2."""
    if y > math.pi / 2 and not plant:  # planted: the annulus continuation X(y, w)
        w = -w
    return np.array([math.cos(y) * math.cos(w), math.cos(y) * math.sin(w), math.sin(y)])


def angdist(x, y):
    return abs((x - y + math.pi) % (2 * math.pi) - math.pi)


def e5(plant=False):
    h = 1e-6
    for a in WIDTHS:
        band = [math.atan2(*chart(math.pi / 2 + s * h, u, plant)[1::-1]) for s in (-1, 1) for u in np.linspace(-a, a, 41)]
        for edge in (a, -a):
            p_in, p_out = chart(math.pi / 2 - h, edge, plant), chart(math.pi / 2 + h, edge, plant)
            a_in, a_out = math.atan2(p_in[1], p_in[0]), math.atan2(p_out[1], p_out[0])
            gap = angdist(a_in, a_out)  # the opening between the arriving and leaving rays
            if abs(gap - (math.pi - 2 * a)) > 1e-5:  # the turn π − gap must be 2W/R
                return False
            fwd = (a_out - a_in) % (2 * math.pi)
            mid = a_in + fwd / 2 if fwd <= math.pi else a_out + (2 * math.pi - fwd) / 2
            if min(angdist(b, mid) for b in band) < gap / 2 - 1e-5:  # no band direction inside that sector
                return False
    return True


def cells(a, ns=12, sub=3):
    brk = sorted([(-a) % (2 * math.pi), a, math.pi - a, math.pi + a])
    phis = sorted(((brk[k] + ((brk[(k + 1) % 4] + (2 * math.pi if k == 3 else 0)) - brk[k]) * m / sub) % (2 * math.pi))
                  for k in range(4) for m in range(sub))
    n = len(phis)
    faces = {}
    for i in range(ns):
        for j in range(n):
            j2 = (j + 1) % n
            faces[(i, j)] = (("N", (1, j), (1, j2)) if i == 0 else ("S", (ns - 1, j2), (ns - 1, j)) if i == ns - 1
                             else ((i, j), (i, j2), (i + 1, j2), (i + 1, j)))
    centre = lambda j: ((phis[j] + phis[(j + 1) % n] + (2 * math.pi if j == n - 1 else 0)) / 2) % (2 * math.pi)
    anti = lambda f: (ns - 1 - f[0], (f[1] + n // 2) % n)
    return faces, centre, anti


def inside(x, lo, hi):
    x, lo, hi = x % (2 * math.pi), lo % (2 * math.pi), hi % (2 * math.pi)
    return lo < x < hi if lo < hi else (x > lo or x < hi)


def components(nodes, nbrs):
    seen, c = set(), 0
    for x in nodes:
        if x in seen:
            continue
        c += 1
        stack = [x]
        while stack:
            y = stack.pop()
            if y not in seen:
                seen.add(y)
                stack.extend(nbrs(y) - seen)
    return c


def complex_data(fs, faces):
    """χ, face components (through shared edges), manifoldness (one fan at each vertex), boundary cycles."""
    V, E = set(), defaultdict(list)
    for f in fs:
        vs = faces[f]
        V.update(vs)
        for k in range(len(vs)):
            E[frozenset((vs[k], vs[(k + 1) % len(vs)]))].append(f)
    adj = defaultdict(set)
    for fl in E.values():
        for f in fl:
            adj[f].update(g for g in fl if g != f)
    manifold = True
    for v in V:
        nb = defaultdict(set)
        for e, fl in E.items():
            if v in e:
                for f in fl:
                    nb[f].update(g for g in fl if g != f)
        manifold &= components([f for f in fs if v in faces[f]], lambda f: nb[f]) == 1
    badj = defaultdict(set)
    for e, fl in E.items():
        if len(fl) == 1:
            u, w = tuple(e)
            badj[u].add(w)
            badj[w].add(u)
    return len(V) - len(E) + len(fs), components(fs, lambda f: adj[f]), manifold, components(list(badj), lambda x: badj[x])


def e6(plant=False):
    for a in WIDTHS:
        faces, centre, anti = cells(a)
        D = {f for f in faces if inside(centre(f[1]), -a, a)}
        band = D | {anti(f) for f in D}
        if complex_data(band, faces)[2]:  # M(W)'s lift must fail to be a manifold at ±N
            return False
        if plant:  # planted: cut on the band's own side, removing its tip at N
            tip = {f for f in D if f[0] == 0}
            new = band - tip - {anti(f) for f in tip}
        else:  # cut the pass at N whose sector is (W/R, π − W/R): add the cell there, and its antipode
            T = {f for f in faces if f[0] == 0 and inside(centre(f[1]), a, math.pi - a)}
            new = band | T | {anti(f) for f in T}
        chi, comps, manifold, bcycles = complex_data(new, faces)
        if not (manifold and comps == 1 and chi == 0 and bcycles == 2):
            return False
        cchi, ccomps, cmanifold, cbcycles = complex_data(set(faces) - new, faces)
        if not (cmanifold and ccomps == 2 and cchi == 2 and cbcycles == 2):
            return False
    return True


def e7(plant=False):
    t = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
    for rho in ((math.pi / 2,) if plant else (0.4, 1.0, 1.3, 2.0, 2.9)):  # planted: a great circle
        P = np.stack([math.sin(rho) * np.cos(t), math.sin(rho) * np.sin(t), math.cos(rho) * np.ones_like(t)], 1)
        if (P @ P.T).min() < -1 + 1e-6:
            return False
    return True


def e8(plant=False):
    a, b, kap, kbar = sp.symbols("a b kappa kbar", real=True)
    form = sp.Matrix([[kap / 2, (kap + kbar) / 2], [(kap + kbar) / 2, kap / 2]])
    ok = sp.expand((sp.Matrix([[a, b]]) * form * sp.Matrix([a, b]))[0] - (kap / 2 * (a + b) ** 2 + kbar * a * b)) == 0
    ev = list(form.subs(kap, 1).eigenvals())
    low = lambda kb: min(e.subs(kbar, kb) for e in ev)
    ends = (-sp.Rational(11, 5), sp.Rational(1, 5)) if plant else (-2, 0)  # planted: a wider window
    ok &= all(low(kb) >= 0 for kb in ends)
    ok &= all(low(kb) > 0 for kb in (-sp.Rational(19, 10), -1, -sp.Rational(1, 10)))
    ok &= all(low(kb) < 0 for kb in (-sp.Rational(21, 10), sp.Rational(1, 10)))
    return bool(ok)


def null(rows):
    _, s, vt = np.linalg.svd(np.atleast_2d(rows))
    return vt[np.sum(s > 1e-12):]


def e9(plant=False):
    N, c, d, nu = np.eye(4)
    laws = {"c": lambda t, a: math.cos(t) * math.tan(a), "d": lambda t, a: math.tan(a) / math.cos(t)}
    if plant:  # planted: each turn checked against the other turn's law
        laws = {"c": laws["d"], "d": laws["c"]}
    for a in WIDTHS:
        for t in (0.1, 0.3, 0.6):
            for turn in ("c", "d"):
                if turn == "c":
                    core, side = math.cos(t) * c + math.sin(t) * nu, d
                else:
                    core, side = c, math.cos(t) * d + math.sin(t) * nu
                nS = null(np.stack([N, core, side]))[0]  # the turned plane's normal in R⁴
                for sgn in (1, -1):
                    nU = null(np.stack([N, math.cos(a) * c + sgn * math.sin(a) * d, nu]))[0]
                    line = null(np.stack([nS, nU]))  # the cut: a 2-plane of R⁴, a projective line
                    if line.shape[0] != 2 or np.linalg.norm(line @ N) < 1 - 1e-10:  # through the pinch N
                        return False
                    v = line[np.argmin(np.abs(line @ N))]
                    v = v - (v @ N) * N
                    v /= np.linalg.norm(v)
                    if abs(math.tan(math.atan2(abs(v @ side), abs(v @ core))) - laws[turn](t, a)) > 1e-9:
                        return False
    tt, aa = sp.symbols("t a", real=True)
    Wc, Wd = R * sp.atan(sp.tan(aa) * sp.cos(tt)), R * sp.atan(sp.tan(aa) / sp.cos(tt))
    return (sp.simplify(sp.diff(4 * R * Wc, tt, 2).subs(tt, 0) + 2 * R**2 * sp.sin(2 * aa)) == 0
            and sp.simplify(sp.diff(4 * R * Wd, tt, 2).subs(tt, 0) - 2 * R**2 * sp.sin(2 * aa)) == 0)


def kg_toward_disc(rho, n=200001):
    tt = np.linspace(0, 2 * np.pi, n)
    P = np.stack([np.sin(rho) * np.cos(tt), np.sin(rho) * np.sin(tt), np.cos(rho) * np.ones_like(tt)], 1)
    d1 = np.gradient(P, tt, axis=0)
    d2 = np.gradient(d1, tt, axis=0)
    i = n // 2
    return np.dot(np.cross(P[i], d1[i]), d2[i]) / np.linalg.norm(d1[i]) ** 3


def e10(plant=False):
    for g in (0.3, 1.0, 2.5):  # ΓR/σ at R = 1
        W = math.atan(1 / g) if plant else math.atan(g)  # planted: half-width R arctan(σ/(ΓR))
        if abs(g - kg_toward_disc(math.pi / 2 - W)) > 1e-6:  # σk_g = −Γ, k_g toward the band = −(toward the disc)
            return False
    for W in (0.3, 1.0, 1.4):
        rho = math.pi / 2 - W
        tt = np.linspace(0, 2 * np.pi, 20001)
        P = np.stack([np.sin(rho) * np.cos(tt), np.sin(rho) * np.sin(tt), np.cos(rho) * np.ones_like(tt)], 1)
        if abs(np.linalg.norm(np.diff(P, axis=0), axis=1).sum() - 2 * np.pi * math.cos(W)) > 1e-6:
            return False
    return True


CHECKS = [
    ("E1 the named energies are points of the family, with the stated Γ = γ + κ̄/R²", e1),
    ("E2 every named density is flat at A = 0: bending acts only at second order", e2),
    ("E3 the edge law's sign: d(Γ·Area + σL) = ∫(Γ + σk_g)V ds, k_g positive toward the band", e3),
    ("E4 a corner cut with geodesic legs saves 2ε(1 − sin(θ/2)) + O(ε³) and costs ½ε² sin θ + O(ε⁴)", e4),
    ("E5 each pass through the pinch turns by 2W/R around a band-free sector of opening π − 2W/R", e5),
    ("E6 cutting one pass leaves a Möbius band whose complement's closure is a closed disc", e6),
    ("E7 a circle that is not a great circle holds no antipodal pair", e7),
    ("E8 (κ/2)H² + κ̄ det A ≥ 0 exactly for −2κ ≤ κ̄ ≤ 0, positive definite strictly inside", e8),
    ("E9 on the two-sheet support, turning the plane toward ν narrows the band from c, tan(W_t/R) = cos t tan(W/R), and widens it from d, tan(W'_t/R) = tan(W/R)/cos t", e9),
    ("E10 the critical tube's half-width R arctan(ΓR/σ), and the tube edge 2πR cos(W/R)", e10),
]


def main():
    res = {name: fn() for name, fn in CHECKS}
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    if "--arms" in sys.argv:
        assert all(res.values()), "arms need a green parent"
        rc = 0
        for name, fn in CHECKS:
            fired = not fn(plant=True)
            print(("ARM FIRED " if fired else "ARM SILENT ") + name)
            rc |= 0 if fired else 1
        return rc
    return 0 if all(res.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
