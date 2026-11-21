#!/usr/bin/env python3
"""The Mirror (2026-11-20, section V added 2026-11-21): reproducible verification artifact
for sections III and V.

Rebuilds, from the McKay graph of 2I and Bar's Dirac spectrum on S^3/2I, the spectral
results that the-mirror.md section III reports, and certifies them gate by gate:

  G01  the class table: nine classes of 2I by SU(2) angle, with sizes that sum to 120 and
       agree with the character table's column orthogonality;
  G02  the character table, rebuilt from the McKay graph as torsion-correction.test.py does:
       orthonormal rows, the dimensions at C1, the spin parity at C2;
  G03  the signed Dirac table eta_n(sigma) = m+ - m-: dimension cancellation for n < 120,
       one chirality per level (the spin selection rule), and the McKay wavefront: each
       irrep enters the SU(2) tower at j = dist(sigma), so the table at n = dist(sigma) - 1;
  G04  formula (3), the class coefficient [(n+2) sin((n+1)a) - (n+1) sin((n+2)a)] / sin a,
       against the character-weighted table, with C1 identically zero;
  G05  the closed forms of C2, C7, C8 and C9 against an independent Hurwitz evaluation of the
       same series at real and complex s; the C8 form printed before 2026-11-20 fails it;
  G06  eta(sigma, 0) for all nine irreps by two paths, Bernoulli (exact rationals) and
       Donnelly (a finite group sum), equal to the printed values, with denominators dividing
       720, zero dimension-weighted sum, and the sign change between distance 3 and 4;
  G07  the per-irrep survivors in the L-function basis: 12, 10, 10, 10, 6, 8, 10, 8, 8 of 32,
       the surviving conductors, two universal survivors, twenty universal kills, and the
       stabilizer pattern of section III.C;
  G08  the Dirac zeta keeps the eta's survivors irrep by irrep, the set twisted by chi_-4,
       because each level carries one chirality; fitting in the period index instead gives
       30, 29, 30, 29, 29, 29, 29, 29, 28 for both, which is why that basis is not used;
  G09  the class-level survivors: C2 one, C7 to C9 one per layer, C3 to C6 two per layer;
       Lemma 3's S1, with f_r = sin(r a/2) / sin(a/2), keeps the characters of layer s;
  G10  the torsion L-basis of section III.A equals the logs of the closed forms
       (4/5) phi^-2, 9/4, 25/9 and (4/5) phi^2 to 45 digits, with the Galois ratio phi^-4;
  G11  the vacuum twist: eta_std - eta_gal at s = 0 is (2/5) x integer for every irrep, zero
       at R7; twisting multiplies each class eta by the twist's character, which is 0 on C9
       and 1 on C7 for both nontrivial twists (Lemma 4);
  G12  Lemma B of section V, exactly over Q: the 18 Dirac etas and zetas of the irreps have
       shift-0 layers of rank 16, shift-1 layers of rank 14 with a 4-dimensional kernel, and on
       that kernel shift-2 layers of rank 2, so every nonzero combination carries two shifts;
  G13  Lemma D of section V: the odd signature operator's eta of each irrep, from the curl
       blocks V_{l-1} x V_{l+1} (+) and V_{l+1} x V_{l-1} (-); its class values at s = 0 are
       cot^2(a/2), its R0 value 361/180 meets Ruberman-Saveliev with eta_Dir(R0) = 1079/720,
       1/2 eta_Dir + 1/8 eta_Sign = 1, the C9 eta equals 2^(2-s)(1 - 2^(2-s)) zeta(s-1) at real
       and complex s with no shift-0 layer, and among the signature etas only C9 drops a layer.

The torsions themselves are recomputed from the spectrum by
files/framework/files/working/files/scripts/torsion-correction.test.py; G10 checks that the
page's L-basis column and its closed forms agree.

Conventions. Dirac eigenvalues +-(n + 3/2) on the unit S^3. For the bundle of an irrep
sigma, m+_n = (n+2) N(sigma, n) and m-_n = (n+1) N(sigma, n+1), with N(sigma, j) the
multiplicity of sigma in the (j+1)-dimensional SU(2) irrep; this is the orientation that
gives formulas (2) and (3). Dirichlet series run over the odd numerators m = 2n + 3. A
character chi mod 120 survives when L(s - p, chi) appears for some p in {0, 1, 2}: the m^p
layer of the coefficient, restricted to the 32 residues prime to 120, has a nonzero
chi-projection. Donnelly's kernel (1 + cos a) / sin^2 a is written 1 / (1 - cos a).

Meta-guard (as in torsion-correction.test.py): every gate has a stable id, every mutation
names the gate it attacks, and --mutation-tests fails unless the mutation targets equal the
gate ids and every mutation turns its gate red.

  python3 the-mirror.test.py                   # verify (13 gates)
  python3 the-mirror.test.py --mutation-tests  # 13 defects, each must turn its gate red

Needs mpmath.
"""
import argparse
import sys
import time
from fractions import Fraction as F
from math import gcd

import mpmath as mp

mp.mp.dps = 50
TINY = mp.mpf(10) ** -30

LABELS = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]
DIMS = [1, 2, 2, 3, 3, 4, 4, 5, 6]
IX = {l: i for i, l in enumerate(LABELS)}
EDGES = [("R0", "R1"), ("R1", "R3"), ("R3", "R6"), ("R6", "R7"),
         ("R7", "R8"), ("R8", "R5"), ("R5", "R2"), ("R8", "R4")]
MCKAY_ORDER = ["R0", "R1", "R3", "R6", "R7", "R8", "R5", "R4", "R2"]
DIST = {"R0": 0, "R1": 1, "R3": 2, "R6": 3, "R7": 4, "R8": 5, "R5": 6, "R4": 6, "R2": 7}
INTEGER_SPIN = {"R0", "R3", "R4", "R5", "R7"}
# the page's class table: label, angle a / pi (SU(2) eigenvalues e^{+-i a}), order, size
CLASSES = [("C1", F(0), 1, 1), ("C2", F(1), 2, 1), ("C3", F(1, 5), 10, 12), ("C4", F(2, 5), 5, 12),
           ("C5", F(3, 5), 10, 12), ("C6", F(4, 5), 5, 12), ("C7", F(1, 3), 6, 20),
           ("C8", F(2, 3), 3, 20), ("C9", F(1, 2), 4, 30)]


def ang(frac):
    return mp.pi * mp.mpf(frac.numerator) / frac.denominator


def su2_char(j, a):
    """Character of the (j+1)-dimensional SU(2) irrep at the SU(2) angle a."""
    s = mp.sin(a)
    if abs(s) < TINY:
        return mp.mpf(j + 1) * (1 if abs(a) < 1 else (-1) ** j)
    return mp.sin((j + 1) * a) / s


def mckay(edges=EDGES, jmax=520):
    """N(sigma, j) for j < jmax, from the McKay recursion m_{j+1} = A m_j - m_{j-1}."""
    A = [[0] * 9 for _ in range(9)]
    for a, b in edges:
        A[IX[a]][IX[b]] = A[IX[b]][IX[a]] = 1
    m = [[0] * 9, [0] * 9]
    m[0][IX["R0"]] = 1
    m[1][IX["R1"]] = 1
    for j in range(1, jmax):
        m.append([sum(A[i][k] * m[j][k] for k in range(9)) - m[j - 1][i] for i in range(9)])
    return m


def char_table(mult, classes=CLASSES):
    M = mp.matrix([[mult[j][i] for i in range(9)] for j in range(9)])
    chi = [[mp.mpf(0)] * len(classes) for _ in range(9)]
    for c, cl in enumerate(classes):
        sol = mp.lu_solve(M, mp.matrix([su2_char(j, ang(cl[1])) for j in range(9)]))
        for i in range(9):
            chi[i][c] = sol[i]
    return chi


MULT = mckay()
CHI = char_table(MULT)


# ---------- Dirichlet characters mod 120, exact values in Q(i) ----------

UNITS = [r for r in range(1, 120) if gcd(r, 120) == 1]
ODD = list(range(1, 120, 2))
IND5 = {1: 0, 2: 1, 4: 2, 3: 3}          # 2 generates (Z/5)^x
IPOW = [(1, 0), (0, 1), (-1, 0), (0, -1)]
CHARS = [(a, b, c) for a in range(4) for b in range(2) for c in range(4)]   # mod 8 x mod 3 x mod 5
NAMES = {(0, 0, 0): "principal", (1, 0, 0): "chi_-4", (2, 0, 0): "chi_8", (3, 0, 0): "chi_-8",
         (0, 1, 0): "chi_-3", (1, 1, 0): "chi_12", (0, 0, 2): "chi_5", (0, 0, 1): "psi",
         (0, 0, 3): "psibar", (1, 0, 2): "chi_-20", (1, 0, 1): "chi_-4 psi", (1, 0, 3): "chi_-4 psibar"}


def chi_val(ch, m):
    """Exact value (re, im) of the character ch at a unit m: mod-8 index a in
    (principal, chi_-4, chi_8, chi_-8), mod-3 index b, mod-5 power c of psi, psi(2) = i."""
    a, b, c = ch
    s4 = 1 if m % 4 == 1 else -1
    s8 = 1 if m % 8 in (1, 7) else -1
    v = [1, s4, s8, s4 * s8][a] * (1 if b == 0 or m % 3 == 1 else -1)
    re, im = IPOW[(c * IND5[m % 5]) % 4]
    return v * re, v * im


def cond(ch):
    return [1, 4, 8, 8][ch[0]] * (3 if ch[1] else 1) * [1, 5, 5, 5][ch[2]]


def name(ch):
    return NAMES.get(ch, str(ch))


def times(ch, other):
    return (ch[0] ^ other[0], ch[1] ^ other[1], (ch[2] + other[2]) % 4)


def fit_m(cfun, r):
    """Exact a2 m^2 + a1 m + a0 through m = r, r+120, r+240; checked at r+360 and r+480."""
    xs = [r, r + 120, r + 240]
    ys = [F(cfun(x)) for x in xs]
    a = [F(0)] * 3
    for i in range(3):
        o = [xs[k] for k in range(3) if k != i]
        d = F((xs[i] - o[0]) * (xs[i] - o[1]))
        a[2] += ys[i] / d
        a[1] -= ys[i] * (o[0] + o[1]) / d
        a[0] += ys[i] * o[0] * o[1] / d
    for x in (r + 360, r + 480):
        if a[2] * x * x + a[1] * x + a[0] != cfun(x):
            raise AssertionError(f"residue {r} is not a quadratic quasi-polynomial in m")
    return a


def fit_k(cfun, r):
    """The same data fitted in the period index k, m = 120 k + r."""
    ys = [F(cfun(120 * k + r)) for k in range(3)]
    a2 = (ys[2] - 2 * ys[1] + ys[0]) / 2
    a1 = ys[1] - ys[0] - a2
    for k in (3, 4):
        if a2 * k * k + a1 * k + ys[0] != cfun(120 * k + r):
            raise AssertionError(f"residue {r} is not quadratic in k")
    return [ys[0], a1, a2]


def coeff(mult, i, kind="eta", shift=1):
    """Coefficient of m^-s (times 2^-s) at the odd numerator m = 2n + 3."""
    def c(m):
        n = (m - 3) // 2
        if n < 0:
            return 0
        if kind == "eta":
            return (n + 2) * mult[n][i] - (n + 1) * mult[n + shift][i]
        return (n + 2) * mult[n][i] + (n + 1) * mult[n + 1][i]
    return c


def projections(cfun, fitter=fit_m):
    lay = {r: fitter(cfun, r) for r in UNITS}
    out = {}
    for ch in CHARS:
        vals = [chi_val(ch, r) for r in UNITS]
        for p in range(3):
            out[(ch, p)] = (sum(lay[r][p] * v[0] for r, v in zip(UNITS, vals)),
                            -sum(lay[r][p] * v[1] for r, v in zip(UNITS, vals)))
    return out


def survivors(P):
    return {ch for ch in CHARS if any(P[(ch, p)] != (0, 0) for p in range(3))}


_PROJ = {}


def irrep_projections(fitter=fit_m, kind="eta"):
    key = (fitter.__name__, kind)
    if key not in _PROJ:
        _PROJ[key] = {l: projections(coeff(MULT, IX[l], kind), fitter) for l in LABELS}
    return _PROJ[key]


# ---------- gates ----------

GATES, MUTATIONS = {}, {}


def gate(gid, mutation):
    def deco(fn):
        GATES[gid] = fn
        MUTATIONS[gid] = mutation
        return fn
    return deco


@gate("G01", "C9 given 20 elements instead of 30")
def g01(defect):
    classes = [c if (c[0] != "C9" or not defect) else (c[0], c[1], c[2], 20) for c in CLASSES]
    ok = len(classes) == 9 and sum(c[3] for c in classes) == 120
    for c, (lab, a, order, size) in enumerate(classes):
        k = next(k for k in range(1, 121) if (a * k).denominator == 1 and (a * k).numerator % 2 == 0)
        col = sum(CHI[i][c] ** 2 for i in range(9))          # = 120 / size (centralizer order)
        ok &= k == order and abs(col - mp.mpf(120) / size) < TINY
    return ok, "sizes " + " ".join(f"{c[0]}:{c[3]}" for c in classes) + f", total {sum(c[3] for c in classes)}"


@gate("G02", "McKay edge R8-R4 moved to R7-R4")
def g02(defect):
    mult = mckay([e if e != ("R8", "R4") else ("R7", "R4") for e in EDGES]) if defect else MULT
    if any(v < 0 for row in mult[:200] for v in row):
        return False, "negative multiplicity from the recursion"
    chi = char_table(mult)
    sizes = [c[3] for c in CLASSES]
    ok = all(abs(sum(sizes[c] * chi[i][c] * chi[k][c] for c in range(9)) / 120 - (i == k)) < TINY
             for i in range(9) for k in range(9))
    ok &= all(abs(chi[i][0] - DIMS[i]) < TINY for i in range(9))
    ok &= all(abs(chi[i][1] - (DIMS[i] if LABELS[i] in INTEGER_SPIN else -DIMS[i])) < TINY for i in range(9))
    ok &= all(abs(sum(sizes[c] * chi[i][c] * su2_char(j, ang(CLASSES[c][1])) for c in range(9)) / 120
                  - mult[j][i]) < TINY for j in range(0, 130, 7) for i in range(9))
    return ok, "chi at C2: " + " ".join(f"{LABELS[i]}:{int(mp.nint(chi[i][1]))}" for i in range(9))


@gate("G03", "m- read from N(sigma, n+2) instead of N(sigma, n+1)")
def g03(defect):
    sh = 2 if defect else 1
    eta = lambda i, n: (n + 2) * MULT[n][i] - (n + 1) * MULT[n + sh][i]
    ok = all(sum(DIMS[i] * eta(i, n) for i in range(9)) == 0 for n in range(120))
    ok &= all((n + 2) * MULT[n][i] * (n + 1) * MULT[n + 1][i] == 0 for n in range(300) for i in range(9))
    tower = {l: next(j for j in range(60) if MULT[j][IX[l]] != 0) for l in LABELS}
    first = {l: next(n for n in range(60) if eta(IX[l], n) != 0) for l in LABELS}
    ok &= tower == DIST and all(first[l] == max(DIST[l] - 1, 0) for l in LABELS)
    rows = " | ".join(" ".join(f"{eta(IX[l], n):3d}" for l in MCKAY_ORDER) for n in (0, 5, 6))
    return ok, (f"sigma enters the SU(2) tower at j = dist(sigma) {[tower[l] for l in MCKAY_ORDER]}, "
                f"the signed table one level earlier through m-; rows n=0,5,6 (McKay order): {rows}")


@gate("G04", "formula (3) with (n+1) and (n+2) swapped")
def g04(defect):
    worst = mp.mpf(0)
    for c, (lab, a, _, _) in enumerate(CLASSES):
        al = ang(a)
        for n in range(300):
            table = sum(CHI[i][c] * ((n + 2) * MULT[n][i] - (n + 1) * MULT[n + 1][i]) for i in range(9))
            if lab in ("C1", "C2"):
                formula = (n + 2) * su2_char(n, al) - (n + 1) * su2_char(n + 1, al)
            else:
                p, q = ((n + 1), (n + 2)) if defect else ((n + 2), (n + 1))
                formula = (p * mp.sin((n + 1) * al) - q * mp.sin((n + 2) * al)) / mp.sin(al)
            worst = max(worst, abs(table - formula))
            if lab == "C1" and abs(table) > TINY:
                return False, "C1 coefficient nonzero"
    return worst < TINY, f"largest difference over 9 classes, n < 300: {mp.nstr(worst, 3)}"


CHI_M4 = [0, 1, 0, -1]
CHI_M3 = [0, 1, -1]
CHI_M8 = [0, 1, 0, 1, 0, -1, 0, -1]
CHI_8 = [0, 1, 0, -1, 0, -1, 0, 1]
CHI_12 = [0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1]


def Ld(s, table):
    return mp.dirichlet(s, table)


CLOSED = {
    "C2": lambda s: 2 ** (s - 1) * (Ld(s, CHI_M4) - Ld(s - 2, CHI_M4)),
    "C7": lambda s: 2 ** (s - 1) * ((1 + 3 ** (1 - s)) * Ld(s, CHI_M4) - Ld(s - 1, CHI_12)),
    "C8": lambda s: 2 ** (s - 1) * ((1 + 2 ** (-s)) * Ld(s, CHI_M3)
                                    - (1 - 2 ** (1 - s)) * (1 - 3 ** (2 - s)) * mp.zeta(s - 1)),
    "C9": lambda s: 2 ** (s - 1) * (Ld(s, CHI_M8) - Ld(s - 1, CHI_8)),
}
EARLIER_C8 = lambda s: 2 ** (s - 1) * (Ld(s, CHI_M3) - mp.zeta(s - 1))
S_POINTS = [mp.mpf("3.7"), mp.mpf("0.3"), mp.mpf("-0.6"), mp.mpc("1.5", "2"), mp.mpc("0.5", "14.134725")]


def hurwitz_class_eta(lab, s):
    """eta_g(s) = 2^s sum over odd residues r of sum_p a_{r,p} 120^(p-s) zeta(s - p, r/120),
    with a_{r,p} fitted from formula (3); no Euler factors are used."""
    al = ang(next(c[1] for c in CLASSES if c[0] == lab))

    def c(m):
        n = (m - 3) // 2
        return mp.mpf(0) if n < 0 else (n + 2) * su2_char(n, al) - (n + 1) * su2_char(n + 1, al)
    tot = 0
    for r in ODD:
        xs = [mp.mpf(r + 120 * k) for k in range(3)]
        ys = [c(r + 120 * k) for k in range(3)]
        a = mp.lu_solve(mp.matrix([[x ** p for p in range(3)] for x in xs]), mp.matrix(ys))
        if abs(sum(a[p] * mp.mpf(r + 360) ** p for p in range(3)) - c(r + 360)) > TINY:
            raise AssertionError(f"{lab}: residue {r} not quasi-polynomial")
        for p in range(3):
            if abs(a[p]) > TINY:
                tot += a[p] * mp.mpf(120) ** (p - s) * mp.zeta(s - p, mp.mpf(r) / 120)
    return 2 ** s * tot


@gate("G05", "the C8 closed form printed before 2026-11-20")
def g05(defect):
    worst, notes = mp.mpf(0), []
    for lab, form in CLOSED.items():
        if defect and lab == "C8":
            form = EARLIER_C8
        for s in S_POINTS:
            h = hurwitz_class_eta(lab, s)
            worst = max(worst, abs(h - form(s)) / max(1, abs(h)))
        notes.append(f"{lab}(3.7) = {mp.nstr(mp.re(hurwitz_class_eta(lab, S_POINTS[0])), 12)}")
    return worst < mp.mpf(10) ** -25, f"largest relative difference {mp.nstr(worst, 3)} over 4 classes x 5 points; " + ", ".join(notes)


ETA0 = {"R0": F(1079, 720), "R1": F(73, 72), "R3": F(9, 16), "R6": F(29, 180), "R7": F(-25, 144),
        "R8": F(-17, 40), "R5": F(-61, 180), "R4": F(-19, 80), "R2": F(-67, 360)}


def bern(p, x):
    return [None, x - F(1, 2), x * x - x + F(1, 6), x ** 3 - F(3, 2) * x * x + F(1, 2) * x][p]


def eta0_bernoulli(cfun):
    """sum over odd residues and layers of a_{r,p} 120^p zeta(-p, r/120), zeta(-p, x) = -B_{p+1}(x)/(p+1)."""
    tot = F(0)
    for r in ODD:
        a = fit_m(cfun, r)
        for p in range(3):
            tot += a[p] * F(120) ** p * (-bern(p + 1, F(r, 120)) / (p + 1))
    return tot


_ETA0 = {}


def eta0_all():
    if not _ETA0:
        _ETA0.update({l: eta0_bernoulli(coeff(MULT, IX[l])) for l in LABELS})
    return _ETA0


@gate("G06", "Donnelly kernel squared, 1/(1 - cos a)^2")
def g06(defect):
    path1 = eta0_all()
    path2 = {}
    for l in LABELS:
        i = IX[l]
        k = (lambda a: 1 / (1 - mp.cos(a)) ** 2) if defect else (lambda a: 1 / (1 - mp.cos(a)))
        path2[l] = sum(CLASSES[c][3] * CHI[i][c] * k(ang(CLASSES[c][1])) for c in range(1, 9)) / 120
    ok = all(path1[l] == ETA0[l] for l in LABELS)
    ok &= all(abs(path2[l] - mp.mpf(ETA0[l].numerator) / ETA0[l].denominator) < TINY for l in LABELS)
    ok &= all(720 % ETA0[l].denominator == 0 for l in LABELS)
    ok &= sum(DIMS[IX[l]] * ETA0[l] for l in LABELS) == 0
    ok &= all((ETA0[l] > 0) == (DIST[l] <= 3) for l in LABELS)
    return ok, "eta(sigma,0): " + ", ".join(f"{l} {path1[l]}" for l in MCKAY_ORDER)


SURVIVE = {"R0": (12, {1, 3, 4, 5, 8, 12, 20}), "R1": (10, {1, 3, 4, 5, 12, 20}), "R3": (10, {1, 4, 5, 8, 20}),
           "R6": (10, {1, 3, 4, 5, 12, 20}), "R7": (6, {1, 3, 4, 8, 12}), "R8": (8, {1, 4, 5, 20}),
           "R5": (10, {1, 3, 4, 5, 12, 20}), "R4": (8, {1, 4, 5, 8, 20}), "R2": (8, {1, 3, 4, 5, 12, 20})}
KILLS_MOD3 = {"R3", "R4", "R8"}
KILLS_MOD5 = {"R7"}
KILLS_MOD8 = {"R1", "R2", "R6", "R8", "R5"}


@gate("G07", "layers fitted in the period index k instead of in m")
def g07(defect):
    P = irrep_projections(fit_k if defect else fit_m)
    surv = {l: survivors(P[l]) for l in LABELS}
    ok = all((len(surv[l]), {cond(c) for c in surv[l]}) == SURVIVE[l] for l in LABELS)
    common, union = set.intersection(*surv.values()), set.union(*surv.values())
    ok &= common == {(0, 0, 0), (1, 0, 0)}
    ok &= len(CHARS) - len(union) == 20 and {cond(c) for c in CHARS if c not in union} == {15, 24, 40, 60, 120}
    ok &= {l for l in LABELS if not any(c[1] for c in surv[l])} == KILLS_MOD3
    ok &= {l for l in LABELS if not any(c[2] for c in surv[l])} == KILLS_MOD5
    ok &= {l for l in LABELS if not any(c[0] >= 2 for c in surv[l])} == KILLS_MOD8
    return ok, "survivors " + " ".join(f"{l}:{len(surv[l])}" for l in MCKAY_ORDER) + \
        f"; universal {sorted(name(c) for c in common)}; killed everywhere {len(CHARS) - len(union)}"


@gate("G08", "zeta support compared with the eta support twisted by chi_8")
def g08(defect):
    tw = (2, 0, 0) if defect else (1, 0, 0)
    eta_m, zeta_m = irrep_projections(fit_m, "eta"), irrep_projections(fit_m, "zeta")
    ok = all(survivors(zeta_m[l]) == {times(c, tw) for c in survivors(eta_m[l])} for l in LABELS)
    zeta_k, eta_k = irrep_projections(fit_k, "zeta"), irrep_projections(fit_k, "eta")
    kz = [len(survivors(zeta_k[l])) for l in MCKAY_ORDER]
    ke = [len(survivors(eta_k[l])) for l in MCKAY_ORDER]
    ok &= kz == ke == [30, 29, 30, 29, 29, 29, 29, 29, 28]
    return ok, f"zeta in the L-basis {[len(survivors(zeta_m[l])) for l in MCKAY_ORDER]}; period-index fits: zeta {kz}, eta {ke}"


A = (1, 0, 0)
CLASS_LAYERS = {
    "C2": ({A}, set(), {A}),
    "C3": ({A, (1, 0, 2)}, {(1, 0, 1), (1, 0, 3)}, set()),
    "C4": ({(0, 0, 1), (0, 0, 3)}, {(0, 0, 0), (0, 0, 2)}, set()),
    "C5": ({A, (1, 0, 2)}, {(1, 0, 1), (1, 0, 3)}, set()),
    "C6": ({(0, 0, 1), (0, 0, 3)}, {(0, 0, 0), (0, 0, 2)}, set()),
    "C7": ({A}, {(1, 1, 0)}, set()),
    "C8": ({(0, 1, 0)}, {(0, 0, 0)}, set()),
    "C9": ({(3, 0, 0)}, {(2, 0, 0)}, set()),
}


@gate("G09", "C9 placed at angle pi/4, which is not a class of 2I")
def g09(defect):
    classes = [c if (c[0] != "C9" or not defect) else ("C9", F(1, 4), 8, 30) for c in CLASSES]
    chi = char_table(MULT, classes)
    P = irrep_projections(fit_m)
    ok, out, smallest = True, [], mp.inf
    for c in range(1, 9):
        lab = classes[c][0]
        layers = []
        for p in range(3):
            vals = {ch: abs(sum(chi[i][c] * mp.mpc(*map(lambda x: mp.mpf(x.numerator) / x.denominator,
                                                        P[LABELS[i]][(ch, p)])) for i in range(9)))
                    for ch in CHARS}
            layers.append({ch for ch, v in vals.items() if v > TINY})
            smallest = min([smallest] + [v for v in vals.values() if v > TINY])
        ok &= tuple(layers) == CLASS_LAYERS[lab]
        if lab != "C2":            # Lemma 3's S1 over the units, f_r = sin(r a/2) / sin(a/2)
            half = ang(classes[c][1]) / 2
            s1 = {ch for ch in CHARS if abs(sum((mp.sin(r * half) / mp.sin(half)) * mp.mpc(chi_val(ch, r)[0], -chi_val(ch, r)[1])
                                                for r in UNITS)) > TINY}
            ok &= s1 == layers[0]
        out.append(f"{lab}:{len(set.union(*layers))}")
        if lab in ("C3", "C4"):
            out[-1] += " (" + "; ".join(f"s-{p}: " + ", ".join(sorted(name(x) for x in layers[p]))
                                        for p in range(2)) + ")"
    return ok, " ".join(out) + f" survivors; smallest nonzero projection {mp.nstr(smallest, 3)}"


@gate("G10", "R5 given the closed form 9/4")
def g10(defect):
    phi = (1 + mp.sqrt(5)) / 2
    lp = {p: mp.dirichlet(0, [0] + [1] * (p - 1), derivative=1) for p in (2, 3, 5)}   # L'(0, principal mod p)
    L1 = mp.dirichlet(1, [0, 1, -1, -1, 1])                                         # L(1, Legendre mod 5)
    basis = {"R3": -4 * lp[2] + 2 * lp[5] - mp.sqrt(5) * L1, "R7": 4 * lp[2] - 4 * lp[3],
             "R5": 4 * lp[3] - 4 * lp[5], "R4": -4 * lp[2] + 2 * lp[5] + mp.sqrt(5) * L1}
    closed = {"R3": mp.mpf(4) / 5 / phi ** 2, "R7": mp.mpf(9) / 4, "R5": mp.mpf(9) / 4 if defect else mp.mpf(25) / 9,
              "R4": mp.mpf(4) / 5 * phi ** 2}
    printed = {"R3": "-1.186", "R7": "0.811", "R5": "1.022", "R4": "0.739"}
    ok = all(abs(basis[l] - mp.log(closed[l])) < mp.mpf(10) ** -45 for l in basis)
    ok &= all(f"{float(basis[l]):.3f}" == printed[l] for l in basis)
    ok &= abs(closed["R3"] / closed["R4"] - phi ** -4) < TINY
    return ok, "log T^2: " + ", ".join(f"{l} {mp.nstr(basis[l], 8)}" for l in ("R3", "R7", "R5", "R4"))


@gate("G11", "R3 used as the Galois twist instead of R2")
def g11(defect):
    sizes = [c[3] for c in CLASSES]
    N = [[[int(mp.nint(sum(sizes[k] * CHI[a][k] * CHI[b][k] * CHI[c][k] for k in range(9)) / 120))
           for c in range(9)] for b in range(9)] for a in range(9)]
    eta0 = eta0_all()
    gal = "R3" if defect else "R2"
    tw = lambda rho: {l: sum(N[IX[l]][IX[rho]][t] * eta0[LABELS[t]] for t in range(9)) for l in LABELS}
    std, gl = tw("R1"), tw(gal)
    k = {l: (std[l] - gl[l]) / F(2, 5) for l in LABELS}
    ok = all(v.denominator == 1 for v in k.values()) and k["R7"] == 0
    c7, c9 = 6, 8                  # Lemma 4: both twists vanish on C9 and are 1 on C7
    ok &= all(abs(CHI[IX[rho]][c9]) < TINY and abs(CHI[IX[rho]][c7] - 1) < TINY for rho in ("R1", gal))
    for rho in ("R1", gal):        # class level: twisting multiplies each class eta by chi_rho(g)
        for c in range(9):
            for n in range(0, 120, 11):
                lhs = sum(CHI[i][c] * sum(N[i][IX[rho]][t] * ((n + 2) * MULT[n][t] - (n + 1) * MULT[n + 1][t])
                                          for t in range(9)) for i in range(9))
                rhs = CHI[IX[rho]][c] * sum(CHI[i][c] * ((n + 2) * MULT[n][i] - (n + 1) * MULT[n + 1][i]) for i in range(9))
                ok &= abs(lhs - rhs) < TINY
    return ok, "(eta_std - eta_gal)/(2/5): " + " ".join(f"{l}:{k[l]}" for l in MCKAY_ORDER)


# ---------- section V: Lemma B (Dirac, two shifts) and Lemma D (odd signature operator) ----------


def frac_rank(rows):
    """Rank over Q of a list of rows of Fractions."""
    M = [list(r) for r in rows]
    rank, ncols = 0, (len(M[0]) if M else 0)
    for col in range(ncols):
        piv = next((i for i in range(rank, len(M)) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for i in range(len(M)):
            if i != rank and M[i][col] != 0:
                f = M[i][col] / M[rank][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rank])]
        rank += 1
    return rank


def frac_kernel(rows, ncols):
    """A basis over Q of the vectors x with rows . x = 0."""
    M = [list(r) for r in rows]
    pivots, r = [], 0
    for col in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        M[r] = [a / M[r][col] for a in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivots.append(col)
        r += 1
    basis = []
    for fc in (c for c in range(ncols) if c not in pivots):
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(pivots):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis


@gate("G12", "the Dirac zeta taken as the eta")
def g12(defect):
    funcs = [coeff(MULT, i, "eta") for i in range(9)] + [coeff(MULT, i, "eta" if defect else "zeta") for i in range(9)]
    lay = [{r: fit_m(f, r) for r in ODD} for f in funcs]
    layer = lambda p: [[lay[k][r][p] for k in range(18)] for r in ODD]
    A, B, C = layer(0), layer(1), layer(2)
    r_all, rA, rB = frac_rank(A + B + C), frac_rank(A), frac_rank(B)
    ker = frac_kernel(B, 18)
    rC = frac_rank([[sum(row[k] * v[k] for k in range(18)) for v in ker] for row in C])
    ok = r_all == 16 and rA == 16 and rB == 14 and len(ker) == 4 and rC == 2
    return ok, (f"18 Dirac functions span {r_all}; shift-0 rank {rA}, shift-1 rank {rB} "
                f"(kernel {len(ker)}), shift-2 rank {rC} on that kernel")


MULT_SIG = mckay(jmax=640)
INT_RES = list(range(2, 122))           # one residue mod 120 for each class of m >= 2


def sig_coeff(i, flip=False):
    """Signature eta of the bundle of irrep i at the curl eigenvalue m = l + 1 >= 2: the + block
    V_{l-1} x V_{l+1} gives (m+1) N(sigma, m-2), the - block V_{l+1} x V_{l-1} gives (m-1) N(sigma, m).
    flip swaps the blocks, the opposite orientation."""
    def c(m):
        if m < 2:
            return 0
        v = (m + 1) * MULT_SIG[m - 2][i] - (m - 1) * MULT_SIG[m][i]
        return -v if flip else v
    return c


def fit_int(cfun, r):
    """Exact a2 m^2 + a1 m + a0 on the integers m = r mod 120, through r, r+120, r+240;
    checked at r+360 and r+480."""
    xs = [r, r + 120, r + 240]
    ys = [F(cfun(x)) for x in xs]
    a = [F(0)] * 3
    for i in range(3):
        o = [xs[k] for k in range(3) if k != i]
        d = F((xs[i] - o[0]) * (xs[i] - o[1]))
        a[2] += ys[i] / d
        a[1] -= ys[i] * (o[0] + o[1]) / d
        a[0] += ys[i] * o[0] * o[1] / d
    for x in (r + 360, r + 480):
        if a[2] * x * x + a[1] * x + a[0] != cfun(x):
            raise AssertionError(f"residue {r} is not a quadratic quasi-polynomial in m")
    return a


def sig_layers(flip=False):
    return [{r: fit_int(sig_coeff(i, flip), r) for r in INT_RES} for i in range(9)]


def sig_eta0(lay):
    """eta at s = 0 from the layers: sum of a_{r,p} 120^p zeta(-p, r/120), zeta(-p, x) = -B_{p+1}(x)/(p+1)."""
    return sum(lay[r][p] * F(120) ** p * (-bern(p + 1, F(r, 120)) / (p + 1)) for r in INT_RES for p in range(3))


@gate("G13", "curl's + block taken as V_{l+1} x V_{l-1}, the opposite orientation")
def g13(defect):
    lay = sig_layers(flip=defect)
    e0 = [sig_eta0(lay[i]) for i in range(9)]
    ok = all(lay[i][r][2] == 0 for i in range(9) for r in INT_RES)          # the eta is linear in m
    for c, (lab, a, order, size) in enumerate(CLASSES):                      # class values at s = 0
        val = sum(CHI[i][c] * e0[i] for i in range(9))
        want = 0 if lab in ("C1", "C2") else mp.cot(ang(a) / 2) ** 2
        ok &= abs(val - want) < TINY
    rs = F(1, 2) * eta0_all()["R0"] + F(1, 8) * e0[IX["R0"]]
    ok &= e0[IX["R0"]] == F(361, 180) and rs == 1
    c9 = [int(mp.nint(CHI[i][8])) for i in range(9)]
    l9 = {r: [sum(c9[i] * lay[i][r][p] for i in range(9)) for p in range(3)] for r in INT_RES}
    ok &= all(l9[r][0] == 0 for r in INT_RES)                                  # no shift-0 layer at C9
    worst = mp.mpf(0)
    for s in (mp.mpf(4), mp.mpc(2.5, 3), mp.mpc(-1, 7)):
        val = sum(l9[r][p] * mp.mpf(120) ** (p - s) * mp.zeta(s - p, mp.mpf(r) / 120) for r in INT_RES for p in range(2))
        worst = max(worst, abs(val - 2 ** (2 - s) * (1 - 2 ** (2 - s)) * mp.zeta(s - 1)))
    ok &= worst < TINY
    L0 = [[lay[i][r][0] for i in range(9)] for r in INT_RES]
    L1 = [[lay[i][r][1] for i in range(9)] for r in INT_RES]
    r0, r1, rall = frac_rank(L0), frac_rank(L1), frac_rank(L0 + L1)
    ok &= rall == 7 and r1 == 7 and r0 == 6                                  # only C9 drops a layer
    return ok, (f"eta_Sign(R0, 0) = {e0[IX['R0']]}, 1/2 eta_Dir + 1/8 eta_Sign = {rs}; C9 closed form to "
                f"{mp.nstr(worst, 3)}; signature etas span {rall}, shift-1 rank {r1}, shift-0 rank {r0}")


def run(gid, defect=False):
    try:
        ok, detail = GATES[gid](defect)
    except Exception as e:  # a defect may break the construction outright; that counts as red
        ok, detail = False, f"raised {type(e).__name__}: {e}"
    return bool(ok), detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutation-tests", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    if args.mutation_tests:
        good = set(MUTATIONS) == set(GATES)
        print(f"mutation targets equal gate ids: {good}")
        for gid in sorted(GATES):
            ok, detail = run(gid, defect=True)
            good &= not ok
            print(f"{'RED ' if not ok else 'MISS'}  {gid} under defect: {MUTATIONS[gid]}")
        print(f"{'all' if good else 'NOT all'} {len(GATES)} defects caught ({time.time() - t0:.0f} s)")
        return 0 if good else 1
    results = []
    for gid in sorted(GATES):
        ok, detail = run(gid)
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {gid}  {detail}", flush=True)
    print(f"{sum(results)}/{len(results)} gates pass ({time.time() - t0:.0f} s)")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
