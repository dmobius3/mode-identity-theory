#!/usr/bin/env python3
"""Tier 2 freeze, setup checks (2026-09-23, v2).

Verifies the computational identities S1-S14 listed below, and runs three mutation controls, each of which must
fail. It computes no eigenvalue of the Jacobi operator.

Not executed here, and stated in the draft as hand derivations: section 1.1 (the area lower bound, its equality
case, the immersed infimum, and the obstruction for embedded bands) and the embedding proof of section 1.2. S8 is
a numerical spot check of that proof, not the proof.

The one spectral fact this record touches, the rotation-invariant sector m = 0, is disclosed in the draft (section
1.4) because it follows from symmetry alone. The Jacobi fields of the four plane-mixing rotations, which would settle
the sectors |m| = 1 and 3, are deliberately NOT evaluated here: they belong to the run.

The band B: p(s,t) = R[cos t (cos s e1 + sin s e2) + sin t (cos(s/2) e3 + sin(s/2) e4)],
(s,t) in [0,2pi] x [-pi/2,pi/2], (2pi, t) ~ (0, -t). Double cover: s in R/4piZ, deck map tau(s,t) = (s+2pi, -t).
gamma = S^3(R) cut by the (e3,e4)-plane.

  S1  metric g = R^2 [f ds^2 + dt^2], f = 1 - (3/4) sin^2 t, with f in [1/4, 1]: an immersion up to the boundary
  S2  p lies on S^3(R)
  S3  unit normal nu orthogonal to p, p_s, p_t; |n|^2 = R^6 f
  S4  mean curvature H = trace(g^-1 A) = 0: B is minimal
  S5  |A|^2 = 1/(2 R^2 f^2) > 0, between 1/(2R^2) on the core and 8/R^2 on gamma
  S6  deck map: (a) p(tau x) = p(x); (b) nu(tau x) = -nu(x)
  S7  boundary: t = pi/2 lands on gamma, running once round it over the double cover, and t = -pi/2 is its tau-image
  S8  numerical spot check of the embedding proved in the draft's section 1.2: min |p(x)-p(y)| / d(x,y) over random pairs
  S9  area(B) = 4 pi R^2 E(3/4), E the complete elliptic integral of the second kind at parameter 3/4
  S10 the computational part of the projection lemma: Pi(z,w) = (|z|, w) maps S^3 into the closed hemisphere D bounded
      by gamma, fixes gamma pointwise, and |x-y|^2 - |Pi x - Pi y|^2 = 2(|z1||z2| - Re(z1 conj z2)) >= 0
  S11 sector operator: for psi = e^{i m s/2} phi(t), R^2 J psi = e^{i m s/2} [-(1/sqrt f)(sqrt f phi')' + V_m phi],
      V_m = m^2/(4f) - 1/(2 f^2) - 2, from J = -Delta_g - |A|^2 - Ric(nu,nu), Ric(nu,nu) = 2/R^2
  S12 parity: tau-oddness gives phi odd for m even and phi even for m odd; V_m is even in t
  S13 completeness: V_m > 0 on the whole band for m^2 >= 16, so sectors |m| >= 4 carry no index or nullity
  S14 the rotation about gamma (disclosed, settles m = 0): X12 + X34/2 = p_s is tangent; psi_X = <X12, nu> is
      s-independent, odd, zero exactly at t = 0, +-pi/2, and solves the m = 0 sector equation

Mutation controls, each of which must fail its target check:
  M1  the Ricci term 3/R^2 in place of 2/R^2: S11 fails
  M2  the claimed metric coefficient 2/3 in place of 3/4: S1 fails
  M3  a full turn in place of the half turn (e3,e4 frequency 1): S6a fails
"""
import sys

import numpy as np
import sympy as sp
from scipy import integrate, special

s, t = sp.symbols("s t", real=True)
R = sp.symbols("R", positive=True)
m = sp.symbols("m", integer=True)
E = sp.eye(4)
e1, e2, e3, e4 = [E[:, i] for i in range(4)]
F_TRUE = 1 - sp.Rational(3, 4) * sp.sin(t) ** 2
ok_all = True


def z(expr):
    return sp.simplify(sp.expand_trig(sp.simplify(expr))) == 0


def band(turn):
    return R * (sp.cos(t) * (sp.cos(s) * e1 + sp.sin(s) * e2) + sp.sin(t) * (sp.cos(turn * s) * e3 + sp.sin(turn * s) * e4))


def geometry(p):
    ps, pt = p.diff(s), p.diff(t)
    g = sp.Matrix([[ps.dot(ps), ps.dot(pt)], [pt.dot(ps), pt.dot(pt)]]).applyfunc(sp.simplify)
    M = sp.Matrix.hstack(p, ps, pt)
    n = sp.Matrix([(-1) ** i * sp.Matrix.vstack(*[M.row(j) for j in range(4) if j != i]).det() for i in range(4)]).applyfunc(sp.simplify)
    return ps, pt, g, n


def s1_ok(g, f_claim):
    return all(z(x) for x in (g - R ** 2 * sp.diag(f_claim, 1)))


def s6a_ok(p):
    return all(z(x) for x in (p.subs({s: s + 2 * sp.pi, t: -t}, simultaneous=True) - p))


def s11_ok(g, A2, ric, f_claim):
    phi = sp.Function("phi")
    sq = R ** 2 * sp.sqrt(f_claim)
    ginv = g.inv()
    psi = sp.exp(sp.I * m * s / 2) * phi(t)
    lap = (sp.diff(sq * ginv[0, 0] * sp.diff(psi, s), s) + sp.diff(sq * ginv[1, 1] * sp.diff(psi, t), t)) / sq
    Jpsi = -lap - (A2 + ric / R ** 2) * psi
    Vm = m ** 2 / (4 * f_claim) - 1 / (2 * f_claim ** 2) - 2
    target = sp.exp(sp.I * m * s / 2) * (-(sp.diff(sp.sqrt(f_claim) * sp.diff(phi(t), t), t)) / sp.sqrt(f_claim) + Vm * phi(t)) / R ** 2
    return z(sp.expand(Jpsi - target))


def report(ok, label):
    global ok_all
    ok_all = ok_all and bool(ok)
    print("%s  %s" % ("PASS" if ok else "FAIL", label))


p = band(sp.Rational(1, 2))
ps, pt, g, n = geometry(p)
f = F_TRUE
report(s1_ok(g, f), "S1 metric g = R^2 [f ds^2 + dt^2], f = 1 - (3/4) sin^2 t, f in [1/4, 1]")
report(z(p.dot(p) - R ** 2), "S2 p lies on S^3(R)")
report(z(n.dot(p)) and z(n.dot(ps)) and z(n.dot(pt)) and z(n.dot(n) - R ** 6 * f), "S3 unit normal nu = n/|n| with n orthogonal to p, p_s, p_t and |n|^2 = R^6 f")
nu = n / (R ** 3 * sp.sqrt(f))
A = sp.Matrix([[p.diff(a).diff(b).dot(nu) for b in (s, t)] for a in (s, t)]).applyfunc(sp.simplify)
report(sp.simplify((g.inv() * A).trace()) == 0, "S4 mean curvature trace(g^-1 A) = 0: B is minimal")
A2 = sp.simplify((g.inv() * A * g.inv() * A).trace())
report(z(A2 - 1 / (2 * R ** 2 * f ** 2)), "S5 |A|^2 = 1/(2 R^2 f^2): 1/(2R^2) on the core t = 0, 8/R^2 on gamma")
report(s6a_ok(p), "S6a deck map tau(s,t) = (s + 2pi, -t) fixes p: B is the quotient of the annulus by tau")
report(all(z(x) for x in (nu.subs({s: s + 2 * sp.pi, t: -t}, simultaneous=True) + nu)), "S6b nu(tau x) = -nu(x): the normal bundle is the orientation bundle; normal fields are tau-odd functions")
pb = p.subs(t, sp.pi / 2)
report(z(pb[0]) and z(pb[1]) and all(z(x) for x in (pb - R * (sp.cos(s / 2) * e3 + sp.sin(s / 2) * e4))),
       "S7 boundary t = pi/2 is R(cos(s/2) e3 + sin(s/2) e4): on the double cover s in [0, 4pi) it runs once round gamma, and t = -pi/2 is its tau-image")

rng = np.random.default_rng(20260923)


def pnum(S, T):
    return np.stack([np.cos(T) * np.cos(S), np.cos(T) * np.sin(S), np.sin(T) * np.cos(S / 2), np.sin(T) * np.sin(S / 2)], axis=-1)


def dq(S1, T1, S2, T2):
    """Parameter distance on the band: the nearest of the lifts (S2, T2) and (S2 +- 2pi, -T2)."""
    d1 = np.hypot(S1 - S2, T1 - T2)
    d2 = np.hypot(S1 - S2 - 2 * np.pi, T1 + T2)
    d3 = np.hypot(S1 - S2 + 2 * np.pi, T1 + T2)
    return np.minimum(np.minimum(d1, d2), d3)


S1_, S2_ = rng.uniform(0, 2 * np.pi, 400000), rng.uniform(0, 2 * np.pi, 400000)
T1_, T2_ = rng.uniform(-np.pi / 2, np.pi / 2, 400000), rng.uniform(-np.pi / 2, np.pi / 2, 400000)
ratio = np.linalg.norm(pnum(S1_, T1_) - pnum(S2_, T2_), axis=-1) / dq(S1_, T1_, S2_, T2_)
report(ratio.min() > 0.05, "S8 numerical spot check of the embedding proved in section 1.2: over 400000 random pairs, min |p(x)-p(y)|/d(x,y) = %.3f (R = 1)" % ratio.min())

area_num = integrate.dblquad(lambda T, S: np.sqrt(1 - 0.75 * np.sin(T) ** 2), 0, 2 * np.pi, -np.pi / 2, np.pi / 2, epsabs=1e-12, epsrel=1e-12)[0]
area_E = 4 * np.pi * special.ellipe(0.75)
report(abs(area_num - area_E) < 1e-9, "S9 area(B) = 4 pi R^2 E(3/4) = %.6f R^2 = %.4f x 2 pi R^2 (the hemisphere's area)" % (area_E, area_E / (2 * np.pi)))

a, b, c, d = sp.symbols("a b c d", real=True)   # z1 = a + ib, z2 = c + id
r1, r2 = sp.sqrt(a ** 2 + b ** 2), sp.sqrt(c ** 2 + d ** 2)
lip_gap = sp.simplify(((a - c) ** 2 + (b - d) ** 2) - (r1 - r2) ** 2 - 2 * (r1 * r2 - (a * c + b * d)))
X, Y = rng.normal(size=(200000, 4)), rng.normal(size=(200000, 4))
X /= np.linalg.norm(X, axis=1)[:, None]; Y /= np.linalg.norm(Y, axis=1)[:, None]
Pi = lambda V: np.stack([np.hypot(V[:, 0], V[:, 1]), np.zeros(len(V)), V[:, 2], V[:, 3]], axis=1)
lip = (np.linalg.norm(Pi(X) - Pi(Y), axis=1) <= np.linalg.norm(X - Y, axis=1) + 1e-14).all()
onto_S3 = np.allclose(np.linalg.norm(Pi(X), axis=1), 1.0)
circ = np.array([[0, 0, np.cos(q), np.sin(q)] for q in np.linspace(0, 2 * np.pi, 50)])
report(lip_gap == 0 and lip and onto_S3 and np.allclose(Pi(circ), circ),
       "S10 projection lemma, computational part: Pi(z,w) = (|z|,w) maps S^3 into the closed hemisphere D (area 2 pi R^2), fixes gamma, and |x-y|^2 - |Pi x - Pi y|^2 = 2(|z1||z2| - Re z1 conj(z2)) >= 0")

report(s11_ok(g, A2, 2, f), "S11 sector operator: R^2 J_m phi = -(1/sqrt f)(sqrt f phi')' + V_m phi, V_m = m^2/(4f) - 1/(2f^2) - 2 (Ric(nu,nu) = 2/R^2 included)")
Vm = m ** 2 / (4 * f) - 1 / (2 * f ** 2) - 2
report(z(Vm.subs(t, -t) - Vm), "S12 V_m is even in t; tau-oddness of e^{ims/2} phi(t) reads (-1)^m phi(-t) = -phi(t): phi odd for m even, phi even for m odd")

u = sp.symbols("u", positive=True)
Vu = sp.Rational(16, 4) * u - u ** 2 / 2 - 2
ends = [Vu.subs(u, 1), Vu.subs(u, 4)]
tt = np.linspace(-np.pi / 2, np.pi / 2, 20001)
ff = 1 - 0.75 * np.sin(tt) ** 2
V4min = (16 / (4 * ff) - 1 / (2 * ff ** 2) - 2).min()
report(all(e > 0 for e in ends) and V4min > 0,
       "S13 completeness: with u = 1/f in [1,4], V_m = (m^2/4)u - u^2/2 - 2 is concave in u; at m^2 = 16 its end values are %s, %s (grid min %.4f), and V_m grows with m^2: sectors |m| >= 4 are positive" % (ends[0], ends[1], V4min))

X12 = sp.Matrix([-p[1], p[0], 0, 0])
X34 = sp.Matrix([0, 0, -p[3], p[2]])
tangent = all(z(x) for x in (X12 + X34 / 2 - ps))
psiX = sp.simplify(X12.dot(nu))
psiX_s_free = sp.simplify(sp.diff(psiX, s)) == 0
psiX_odd = z(psiX.subs(t, -t) + psiX)
vanish_gamma = z(psiX.subs(t, sp.pi / 2))
tt2 = np.linspace(1e-6, np.pi / 2 - 1e-6, 200001)
psiX_num = sp.lambdify(t, psiX.subs(R, 1), "numpy")(tt2)
no_interior_zero = (np.abs(psiX_num) > 0).all() and (np.sign(psiX_num) == np.sign(psiX_num[0])).all()
JX = -(sp.diff(sp.sqrt(f) * sp.diff(psiX, t), t)) / sp.sqrt(f) + Vm.subs(m, 0) * psiX
report(tangent and psiX_s_free and psiX_odd and vanish_gamma and no_interior_zero and z(JX),
       "S14 rotation about gamma: X12 + X34/2 = p_s; psi_X = <X12, nu> = %s is s-free, odd, zero at t = 0 and +-pi/2 only, and solves the m = 0 sector equation" % psiX)

controls_ok = True


def control(fails, label):
    global controls_ok
    controls_ok = controls_ok and fails
    print("control  %s  %s" % (label, "fails as required" if fails else "DID NOT FAIL"))


control(not s11_ok(g, A2, 3, f), "M1 the Ricci term 3/R^2 in place of 2/R^2: S11")
control(not s1_ok(g, 1 - sp.Rational(2, 3) * sp.sin(t) ** 2), "M2 the claimed metric coefficient 2/3 in place of 3/4: S1")
control(not s6a_ok(band(1)), "M3 a full turn in place of the half turn: S6a")

print("all setup checks pass; all three controls fail as required" if (ok_all and controls_ok) else "SETUP CHECK FAILED")
sys.exit(0 if (ok_all and controls_ok) else 1)
