#!/usr/bin/env python3
"""Terms for the revised G4 work order, checked numerically (tolerance 1e-9) on the 120 unit icosians.
T1  the 9 irreducible characters of 2I, built from the defining 2 and its Galois conjugate 2', are orthonormal, and
    tau(-I) = -1 exactly for 2, 2', 4', 6.
T2  the first two occurring levels n >= 1 of each tau in the degree-n harmonics' left 2I-module V_n (tau = 1: 12, 20).
T3  which sector each block's output lands in: under the value sampler it is odd under -I (twisted) iff tau(-I) = -1;
    under the transverse sampler iff tau(-I) = +1.
T4  the pinned placements: the non-central elements of 2I that preserve the core's plane under left multiplication
    (2-fold: +-k; the others: none), and those on each pole's axis (2, 4 and 8 at the 2-, 3- and 5-fold poles).
T5  the frozen band map, with d flipped beyond the pinch, is continuous there, and -I pairs (0, w) with (piR, -w), the
    pillar's seam, at every placement.
--arms: each check must fail on a planted defect, parent green first."""
import itertools, math, sys

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-9

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)

def icosians():
    els = set()
    def add(v):
        els.add(tuple(round(x, 12) + 0.0 for x in v))
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4; v[i] = s; add(v)
    for signs in itertools.product((1, -1), repeat=4):
        add([s / 2 for s in signs])
    base = (0.0, 1.0, 1 / PHI, PHI)
    for p in itertools.permutations(range(4)):
        if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2:
            continue
        vals = [base[p[k]] for k in range(4)]
        nz = [k for k in range(4) if vals[k] != 0]
        for signs in itertools.product((1, -1), repeat=3):
            v = [0.0] * 4
            for k, s in zip(nz, signs):
                v[k] = s * vals[k] / 2
            add(v)
    return sorted(els)

G = icosians()

def sigma(x):
    """The Galois conjugation on the real parts that occur: phi/2 -> -1/(2 phi), 1/(2 phi) -> -phi/2."""
    table = {0.5 * PHI: -0.5 / PHI, -0.5 * PHI: 0.5 / PHI, 0.5 / PHI: -0.5 * PHI, -0.5 / PHI: 0.5 * PHI}
    for k, v in table.items():
        if abs(x - k) < TOL:
            return v
    return x

def characters(swap_galois=False):
    chi = {}
    for g in G:
        c2 = 2 * g[0]
        c2p = 2 * sigma(g[0])
        if swap_galois:
            c2, c2p = c2p, c2
        chi[g] = {"1": 1.0, "2": c2, "2'": c2p, "3": c2 ** 2 - 1, "3'": c2p ** 2 - 1, "4": c2 * c2p,
                  "4'": c2 ** 3 - 2 * c2, "5": c2 ** 4 - 3 * c2 ** 2 + 1, "6": c2 ** 5 - 4 * c2 ** 3 + 3 * c2}
    return chi

NAMES = ["1", "2", "2'", "3", "3'", "4", "4'", "5", "6"]
SPINORIAL = {"2", "2'", "4'", "6"}

def chi_n(n, g):
    c = max(-1.0, min(1.0, g[0]))
    th = math.acos(c)
    if abs(math.sin(th)) < 1e-12:
        return (n + 1) * (1 if c > 0 else (-1) ** n)
    return math.sin((n + 1) * th) / math.sin(th)

def mult(n, tau, chi):
    return sum(chi_n(n, g) * chi[g][tau] for g in G) / len(G)

def levels(tau, chi, count=2, nmax=80):
    out = []
    for n in range(1, nmax):
        m = mult(n, tau, chi)
        assert abs(m - round(m)) < 1e-6, (tau, n, m)
        if round(m) > 0:
            out.append(n)
            if len(out) == count:
                return out
    return out

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def norm(v):
    s = math.sqrt(sum(x * x for x in v)); return tuple(x / s for x in v)

S5 = math.sqrt(5)
PLACEMENTS = {"generic": ((1, 2, 3), (2, -1, 0)), "2-fold": ((1, 0, 0), (0, 1, 0)),
              "3-fold": ((1, 1, 1), (1, -1, 0)), "5-fold": ((1 / PHI, 1, 0), (0, 0, 1))}

def placement_counts(pole, azim):
    p, c = norm(pole), norm(azim)
    assert abs(sum(x * y for x, y in zip(p, c))) < TOL
    P, C = (0.0,) + p, (0.0,) + c
    d = cross(p, c)
    core_keep, pole_axis = 0, 0
    for g in G:
        if abs(abs(g[0]) - 1) < TOL:
            continue                                   # the central elements +-1
        ok = True
        for x in (P, C):
            y = qmul(g, x)
            if abs(y[0]) > 1e-9 or abs(sum(a * b for a, b in zip(y[1:], d))) > 1e-9:
                ok = False
        core_keep += ok
        im = g[1:]
        if math.sqrt(sum(x * x for x in cross(im, p))) < 1e-9:
            pole_axis += 1
    return core_keep, pole_axis

def band_point(pole, azim, y, w, flip=True):
    p, c = norm(pole), norm(azim)
    d = cross(p, c)
    if flip and y > math.pi / 2:
        d = tuple(-x for x in d)
    return tuple(math.cos(y) * (math.cos(w) * ci + math.sin(w) * di) + math.sin(y) * pi for ci, di, pi in zip(c, d, p))

def seam_ok(placements, flip=True):
    worst = 0.0
    for pole, azim in placements.values():
        for w in (-0.9, -0.3, 0.2, 0.7):
            a, b = band_point(pole, azim, 0.0, w, flip), band_point(pole, azim, math.pi, -w, flip)
            worst = max(worst, max(abs(x + y) for x, y in zip(a, b)))
            l, r = band_point(pole, azim, math.pi / 2 - 1e-9, w, flip), band_point(pole, azim, math.pi / 2 + 1e-9, w, flip)
            worst = max(worst, max(abs(x - y) for x, y in zip(l, r)) * 1e-3)
    return worst < 1e-9

def checks(chi, placements, expected_levels, core_expect, shift=1, flip=True):
    r = {}
    ok = True
    for a in NAMES:
        for b in NAMES:
            ip = sum(chi[g][a] * chi[g][b] for g in G) / len(G)
            ok &= abs(ip - (1.0 if a == b else 0.0)) < 1e-6
    minus = next(g for g in G if abs(g[0] + 1) < TOL)
    spin = {t for t in NAMES if chi[minus][t] < 0}
    r["T1 nine orthonormal characters; tau(-I) = -1 exactly for 2, 2', 4', 6"] = ok and len(G) == 120 and spin == SPINORIAL
    got = {t: levels(t, chi) for t in NAMES}
    r["T2 first two occurring levels n >= 1 of each irreducible, as frozen"] = got == expected_levels
    t3 = True
    for t, ns in got.items():
        for n in ns:
            value_twisted = n % 2 == 1                     # restriction keeps degree n; -I acts as (-1)^n
            trans_twisted = (n - shift) % 2 == 1           # the normal derivative lowers the degree by one
            t3 &= value_twisted == (t in SPINORIAL) and trans_twisted == (t not in SPINORIAL)
    r["T3 value sampler twists exactly the spinorial blocks; transverse exactly the integer-spin ones"] = t3
    counts = {name: placement_counts(*pc) for name, pc in placements.items()}
    r["T4 core-preserving non-central elements: 2 at the 2-fold placement, 0 elsewhere; pole axes carry 0, 2, 4, 8"] = counts == core_expect
    r["T5 the band map with d flipped beyond the pinch is continuous and -I pairs (0, w) with (piR, -w)"] = seam_ok(placements, flip)
    return r, got, counts

FROZEN_LEVELS = {"1": [12, 20], "2": [1, 11], "2'": [7, 13], "3": [2, 10], "3'": [6, 10], "4": [6, 8], "4'": [3, 9], "5": [4, 8], "6": [5, 7]}
CORE = {"generic": (0, 0), "2-fold": (2, 2), "3-fold": (0, 4), "5-fold": (0, 8)}

if __name__ == "__main__":
    chi = characters()
    res, got, counts = checks(chi, PLACEMENTS, FROZEN_LEVELS, CORE)
    for k, v in res.items():
        print(("PASS " if v else "FAIL ") + k)
    print("levels", got)
    print("placements (core-preserving, pole-axis)", counts)
    if "--arms" in sys.argv:
        assert all(res.values()), "arms need a green parent"
        broken = characters()
        for g in G:
            broken[g] = dict(broken[g]); broken[g]["4"] = broken[g]["4'"]
        planted = [
            ("T1", (broken, PLACEMENTS, FROZEN_LEVELS, CORE)),
            ("T2", (chi, PLACEMENTS, dict(FROZEN_LEVELS, **{"1": [12, 24]}), CORE)),
            ("T3", (chi, PLACEMENTS, FROZEN_LEVELS, CORE, 0)),
            ("T4", (chi, dict(PLACEMENTS, **{"2-fold": ((1, 0, 0), (0, 1, 1))}), FROZEN_LEVELS, CORE)),
            ("T5", (chi, PLACEMENTS, FROZEN_LEVELS, CORE, 1, False)),
        ]
        for key, args in planted:
            r2, _, _ = checks(*args)
            name = next(k for k in r2 if k.startswith(key + " "))
            print(("ARM FIRED " if not r2[name] else "ARM SILENT ") + name)
