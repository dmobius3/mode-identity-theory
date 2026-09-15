#!/usr/bin/env python3
"""Checks for R7's second calculation, the radial transfers: which conditions put a Molien shell at k_N, and what a
width would do to the ratio table's per-multipole structure.

On the round S^3 of radius R a shell-N function f satisfies Delta f = -lam f, lam = N(N+2)/R^2. Pull it back to flat R^3
by the exponential map at the observer, f~(u) = f(exp u). Pizzetti's formula gives its spherical means about the
observer, M(t) = f(0) + t^2 L1/3! + t^4 L2/5! + ..., with L1 and L2 the flat Laplacian and bi-Laplacian of f~ at 0. A
homogeneous flat field with positive spectral measure mu has means <j0(k t)>, so -L1/f(0) = <k^2> and L2/f(0) = <k^4>.
Units R = 1 unless a radius is named.

  C1  L1 = -lam f(0): a match through second order fixes <k^2> = N(N+2), at every N, for any function on the shell
  C2  L2 = (lam^2 - (4/3) lam) f(0): a match through fourth order would need <k^4> < <k^2>^2, which no positive measure
      allows; exact on the whole-shell kernel for symbolic N, and on anisotropic shell functions at N = 3, 4 and 12
  C3  with <k^2> = lam held, the fourth-order shortfall is Var(k^2) + (4/3) lam, least exactly at zero variance
  C4  the figures the draft quotes: the center under the conformally coupled operator, the landing multipoles, and the
      width at which a profile's own fourth-order mismatch equals the curvature's
  C5  a width sigma averages x = k chi* over sigma chi*, which multiplies cos 2x by exp(-2 (chi* sigma)^2): exact by
      quadrature, and on j_l(x)^2 itself at route A's first shell; the first shell's recorded share of C_l below its
      landing, read from the ratio table's run-2 record, whose SHA-256 is printed
Mutation arms, each of which must turn its claim red: a non-eigenfunction (C1), the coefficient 1 in place of 4/3 (C2),
the shortfall's sign flipped (C3), exp(-sigma^2/2) in place of exp(-2 sigma^2) (C5).

Usage: radial_check.py [run-2 result_report.txt]; the default is the record's place in the repo.
"""
import hashlib
import math
import pathlib
import re
import sys

import numpy as np
import sympy as sp
from scipy.special import spherical_jn

t, a = sp.symbols("t a", positive=True)
n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
COS = 1 - t**2 / 2 + t**4 / 24          # exact through t^5
SIN = t - t**3 / 6 + t**5 / 120         # exact through t^5
X = [COS, SIN * n1, SIN * n2, SIN * n3]  # the point at geodesic distance t from the observer (1, 0, 0, 0)

CHI_STAR = 13860.0                       # Mpc, the ratio table's recorded distance to last scattering
ROUTES = (("A", 6130.0), ("B", 19700.0))  # Mpc
REPORT = pathlib.Path(__file__).resolve().parent.parent / "molien-ratio-table-runs" / "run-2" / "result_report.txt"


def sphere_mean(expr):
    """Mean of a polynomial in n1, n2, n3 over the unit sphere, monomial by monomial."""
    total = 0
    for (p, q, r), coeff in sp.Poly(sp.expand(expr), n1, n2, n3).terms():
        if p % 2 or q % 2 or r % 2:
            continue
        total += coeff * sp.factorial2(p - 1) * sp.factorial2(q - 1) * sp.factorial2(r - 1) / sp.factorial2(p + q + r + 1)
    return sp.nsimplify(sp.expand(total))


def pizzetti(P):
    """(f(0), L1, L2) for the pullback of the polynomial P restricted to S^3."""
    ser = sp.Poly(sp.expand(P), t)
    coeff = lambda k: ser.coeff_monomial(t**k) if k else ser.coeff_monomial(1)
    return sp.nsimplify(sphere_mean(coeff(0))), sp.nsimplify(6 * sphere_mean(coeff(2))), sp.nsimplify(120 * sphere_mean(coeff(4)))


def shell_function(N, cs, ws):
    """A real harmonic homogeneous polynomial of degree N on R^4, restricted to S^3: a shell-N function."""
    out = 0
    for c, w in zip(cs, ws):
        assert sp.simplify(sum(ci * ci for ci in c)) == 0, "not a null vector"
        z = sum(ci * xi for ci, xi in zip(c, X))
        zb = sum(sp.conjugate(ci) * xi for ci, xi in zip(c, X))
        out += w * (z**N + zb**N) / 2
    return sp.expand(out)


def gauss_mean(fun, xbar, s, n=80):
    """Mean of fun(x) for x normal with mean xbar and standard deviation s, by Gauss-Hermite quadrature."""
    nodes, weights = np.polynomial.hermite.hermgauss(n)
    return float(np.sum(weights * fun(xbar + math.sqrt(2) * s * nodes)) / math.sqrt(math.pi))


def first_shell_shares(text):
    """{route: {l: share}} from the 'first shell' column of the run-2 report."""
    shares, cur = {}, None
    for line in text.split("\n"):
        m = re.match(r"Route ([AB]), R = \d+ Mpc\.", line)
        if m:
            cur = m.group(1)
            shares[cur] = {}
            continue
        m = re.match(r"\s+(\d+)\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+([\d.]+)\s", line)
        if m and cur:
            shares[cur][int(m.group(1))] = float(m.group(2))
    return shares


def damping_claims(damp):
    """C5's two claims under a proposed damping law damp(s): (identity holds, Bessel ratios agree)."""
    ident = all(abs(gauss_mean(lambda x: np.cos(2 * x), xb, s) - math.cos(2 * xb) * damp(s)) < 1e-12
                for xb in (29.306, 9.119) for s in (0.2295, 0.406, 1.305))
    xb = math.sqrt(168) * CHI_STAR / 6130.0
    ratios = []
    for s in (0.2295, 1.305):
        for l in (2, 5, 6):
            num = gauss_mean(lambda x: spherical_jn(l, x)**2, xb, s) - gauss_mean(lambda x: 1 / (2 * x**2), xb, s)
            den = spherical_jn(l, xb)**2 - 1 / (2 * xb**2)
            ratios.append((s, l, num / den, den * 2 * xb**2))
    return ident, all(abs(r - damp(s)) < 0.05 for s, _, r, _ in ratios), ratios


def main(argv):
    report = pathlib.Path(argv[1]) if len(argv) > 1 else REPORT
    red_claims = 0
    print("C1, C2: the whole-shell kernel sin(a t)/(a sin t), a = N + 1")
    K = sp.series(sp.sin(a * t) / (a * sp.sin(t)), t, 0, 6).removeO()
    k2 = sp.factor(sp.simplify(-6 * K.coeff(t, 2)))
    k4 = sp.simplify(120 * K.coeff(t, 4))
    lam = a**2 - 1
    ok1 = sp.simplify(k2 - lam) == 0
    ok2 = sp.simplify(k4 - (lam**2 - sp.Rational(4, 3) * lam)) == 0
    print("  <k^2> = %s = N(N+2): %s" % (k2, "PASS" if ok1 else "FAIL"))
    print("  <k^4> - <k^2>^2 = %s = -(4/3) N(N+2): %s" % (sp.factor(sp.simplify(k4 - k2**2)), "PASS" if ok2 else "FAIL"))
    red_claims += (not ok1) + (not ok2)

    s2 = sp.sqrt(2) / 2
    cs = [(1, sp.I, 0, 0), (0, 1, 0, sp.I), (s2, 0, s2, sp.I), (0, s2, sp.I, s2)]
    ws = [1, 2, 3, -1]
    print("C1, C2: anisotropic shell functions, a sum of Re (c . x)^N over four null vectors")
    for N in (3, 4, 12):
        P = shell_function(N, cs, ws)
        f0, L1, L2 = pizzetti(P)
        lamN = N * (N + 2)
        ok1 = sp.simplify(L1 + lamN * f0) == 0
        ok2 = sp.simplify(L2 - (lamN**2 - sp.Rational(4, 3) * lamN) * f0) == 0
        c2 = sp.Poly(P, t).coeff_monomial(t**2)
        along = [float(sp.N(c2.subs({n1: v[0], n2: v[1], n3: v[2]}))) for v in ((1, 0, 0), (0, 0, 1))]
        print("  N = %2d: f(0) = %.6f; second-order coefficient %.4f along x, %.4f along z; C1 %s, C2 %s" % (
            N, float(sp.N(f0)), along[0], along[1], "PASS" if ok1 else "FAIL", "PASS" if ok2 else "FAIL"))
        red_claims += (not ok1) + (not ok2)

    print("C3: fourth-order shortfall with <k^2> = lam held (two-point spectra at k^2 = lam +- d)")
    shortfall = lambda lamN, d, sign=1: d**2 + sign * sp.Rational(4, 3) * lamN
    values = [shortfall(168, d) for d in (0, 1, 4, 16)]
    ok3 = all(v > values[0] for v in values[1:]) and values[0] > 0
    print("  N = 12: shortfall %s at d = 0, 1, 4, 16; least at d = 0 and never zero: %s" % (
        ", ".join(str(v) for v in values), "PASS" if ok3 else "FAIL"))
    red_claims += not ok3

    print("C4: figures")
    for N in (12, 20, 30):
        kN = math.sqrt(N * (N + 2))
        print("  N = %2d: k_N R = %.4f; (N+1)/(k_N R) - 1 = %.5f; fourth-order curvature mismatch relative to lam^2 = %.5f;"
              " width 1/(sqrt3 R) relative to k_N = %.4f" % (N, kN, (N + 1) / kN - 1, 4 / (3 * N * (N + 2)), 1 / (math.sqrt(3) * kN)))
    k12 = math.sqrt(168)
    for name, R in ROUTES:
        x12 = k12 * CHI_STAR / R
        sx = CHI_STAR / (math.sqrt(3) * R)
        print("  route %s, R = %.0f Mpc: first shell lands at k_12 chi* = %.3f; the conformal center moves it by %.3f;"
              " the width 1/(sqrt3 R) is %.3f in k chi*" % (name, R, x12, x12 * (13 / k12 - 1), sx))

    print("C5: what a width does to the phase")
    ident, bessel, ratios = damping_claims(lambda s: math.exp(-2 * s**2))
    print("  mean of cos 2x over a normal width s is cos(2 xbar) exp(-2 s^2), below 1e-12: %s" % ("PASS" if ident else "FAIL"))
    for s, l, r, rel in ratios:
        print("  route A first shell, s = %.4f, l = %d: oscillating part of j_l^2 kept %.4f (exp(-2 s^2) = %.4f;"
              " unsmeared deviation from the mean %+.3f of it)" % (s, l, r, math.exp(-2 * s**2), rel))
    print("  j_l^2 ratios within 0.05 of exp(-2 s^2): %s" % ("PASS" if bessel else "FAIL"))
    red_claims += (not ident) + (not bessel)
    s90 = math.sqrt(math.log(10 / 9) / 2)
    text = report.read_text(encoding="utf-8")
    print("  the phase keeps 90%% for k chi* widths up to %.4f" % s90)
    print("  run-2 report sha256 %s" % hashlib.sha256(report.read_bytes()).hexdigest())
    shares = first_shell_shares(text)
    for name, R in ROUTES:
        x12 = k12 * CHI_STAR / R
        sx = CHI_STAR / (math.sqrt(3) * R)
        below = {l: v for l, v in shares[name].items() if l < x12}
        lo = min(below, key=below.get)
        hi = max(below, key=below.get)
        print("  route %s: below the landing (l <= %d) the first shell's share of C_l runs from %.4f at l = %d to %.4f at"
              " l = %d; 90%% phase width relative to k_12 = %.4f; at 1/(sqrt3 R) the phase keeps %.3f" % (
                  name, max(below), below[lo], lo, below[hi], hi, s90 / x12, math.exp(-2 * sx**2)))

    print("arms")
    P = shell_function(4, cs, ws)
    f0, L1, L2 = pizzetti(P)
    arm1 = sp.simplify(L2 - (24**2 - 1 * 24) * f0) != 0
    Q = sp.expand(P + X[0]**2 * X[1]**2)
    q0, qL1, _ = pizzetti(Q)
    arm2 = sp.simplify(qL1 + 24 * q0) != 0
    flipped = [shortfall(168, d, sign=-1) for d in (0, 1, 4, 16)]
    arm3 = not (all(v > flipped[0] for v in flipped[1:]) and flipped[0] > 0)
    m_ident, m_bessel, _ = damping_claims(lambda s: math.exp(-s**2 / 2))
    arm4 = not (m_ident and m_bessel)
    arms = (("coefficient 1 in place of 4/3 (C2)", arm1), ("non-eigenfunction (C1)", arm2),
            ("shortfall sign flipped (C3)", arm3), ("exp(-s^2/2) in place of exp(-2 s^2) (C5)", arm4))
    for name, hit in arms:
        print("  arm: %-42s %s" % (name, "RED" if hit else "STAYED GREEN"))
    n_red = sum(hit for _, hit in arms)
    print("%d claims failed; %d/%d arms red" % (red_claims, n_red, len(arms)))
    return 0 if red_claims == 0 and n_red == len(arms) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
