#!/usr/bin/env python3
"""Proposition 4.2 of projective-carrier.md, numerically: the exact 2/R² survives suitably chosen moves of one lap of
M(W) off its line.

R = 1. The band M_V is the fundamental domain D_V = {0 < θ < π, −W < φ < W + V(θ)/sin θ} on the unit sphere (θ the
distance from the pinch's lift N, φ the longitude), whose Friedrichs realization is the Neumann Laplacian of D_V.
Profiles: β(x) = exp(1 − 1/(1 − x²)) on |x| < 1, b_mid(θ) = β((θ − π/2)/0.5), b_tip(θ) = β((θ − 0.6)/0.35), both
smooth and supported away from the pinch. Quadratic isoparametric finite elements in (θ, φ) with the round metric,
rows graded toward the poles, every node on its exact position, the poles merged into one node each, conical Gauss
quadrature at the poles; eigenvalues are element-wise Rayleigh quotients of the computed eigenvectors, extrapolated
over three refinements (order 4), with the error estimated from the last two extrapolants; on the moved bands the
observed order is between 3 and 4.5, and against a fourth refinement that estimate is conservative.

Checks (exit 1 on any failure), at W/R = 0.3, 0.6, 1.0:
  V1  on M(W): the bottom is 0, the first positive level is 2 within its error, the next is at least 1 above it, and
      its mode is the tilt x_p (distance from span{x, y, z} below 1e-6)
  V2  the first variation along b_mid and b_tip matches (3/(4W)) ∫ (sin²θ − 2cos²θ) b dθ to 2e-6 relative
      (central differences at ε = ±0.01, ±0.02 with Richardson in ε, whose remainder is below 1e-6)
  V3  turning the lap rigidly, V = t sin θ (t = 0.05, 0.1), leaves the level at 2 within its error
  V4  for t = 0.025, 0.05, 0.1 there is a bracket τ₋ < τ₊ with λ₁(t b_mid + τ b_tip) − 2 of opposite signs at its
      ends, each at least 10 times its error, so a root τ(t) lies inside
  V5  at each root the level 2 is the first positive one and simple: the bottom is 0 and the next level is at
      least 1 above it
  V6  at each root the moved lap is curved: max |k_g| ≥ 0.5 on it, against 0 on the fixed lap
  V7  at each root the 2-mode is not a rigid tilt: its L² distance from span{x, y, z}, relative to its norm, is at
      least 1e-4 and at least 100 times its error
  V8  every band computed is embedded in RP²: max φ_R < π − W
--arms plants a defect for each check and requires it to fire."""
import math
import sys
from functools import lru_cache

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

PI = math.pi
WIDTHS = (0.3, 0.6, 1.0)
TS = (0.025, 0.05, 0.1)
BUMPS = {"mid": (PI / 2, 0.5), "tip": (0.6, 0.35)}
LEVELS = (64, 128, 256)  # rows from pole to pole; columns scale with W


def beta(x, der=0):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = np.abs(x) < 1
    xm = x[m]
    q = 1 - xm * xm
    b = np.exp(1 - 1 / q)
    if der == 0:
        out[m] = b
    else:
        g1 = -2 * xm / q**2
        if der == 1:
            out[m] = b * g1
        else:
            g2 = -2 / q**2 - 8 * xm * xm / q**3
            out[m] = b * (g1 * g1 + g2)
    return out


def bump(name, th, der=0):
    th = np.asarray(th, dtype=float)
    if name == "rot":
        return [np.sin(th), np.cos(th), -np.sin(th)][der]
    c, a = BUMPS[name]
    return beta((th - c) / a, der) / a**der


def profile(coef, th, der=0):
    th = np.asarray(th, dtype=float)
    return sum((a * bump(n, th, der) for n, a in coef if a), np.zeros_like(th))


def phi_R(W, coef, th):
    """φ_R = W + V/sin θ and its first two θ-derivatives; V vanishes near the poles except for 'rot'."""
    s, c = np.sin(th), np.cos(th)
    V, V1, V2 = (profile(coef, th, k) for k in range(3))
    with np.errstate(divide="ignore", invalid="ignore"):
        f = np.where(s > 0, V / s, 0.0)
        f1 = np.where(s > 0, V1 / s - V * c / s**2, 0.0)
        f2 = np.where(s > 0, V2 / s - 2 * V1 * c / s**2 + V * (s**2 + 2 * c**2) / s**3, 0.0)
    if any(n == "rot" for n, a in coef if a):  # V = t sin θ: V/sin θ = t exactly, with zero derivatives
        t = dict(coef)["rot"]
        rest = tuple((n, a) for n, a in coef if n != "rot")
        g, g1, g2 = phi_R(0.0, rest, th) if rest else (0 * th, 0 * th, 0 * th)
        return W + t + g, g1, g2
    return W + f, f1, f2


def geodesic_curvature(th, ph, ph1, ph2):
    st, ct, sp_, cp_ = np.sin(th), np.cos(th), np.sin(ph), np.cos(ph)
    g = np.stack([st * cp_, st * sp_, ct])
    g1 = np.stack([ct * cp_ - st * sp_ * ph1, ct * sp_ + st * cp_ * ph1, -st])
    g2 = np.stack([-st * cp_ * (1 + ph1**2) - 2 * ct * sp_ * ph1 - st * sp_ * ph2,
                   -st * sp_ * (1 + ph1**2) + 2 * ct * cp_ * ph1 + st * cp_ * ph2, -ct])
    det = np.einsum("i...,i...->...", g, np.cross(g1, g2, axis=0))
    return det / np.einsum("i...,i...->...", g1, g1) ** 1.5


def conical_rule(n=7):
    g, w = leggauss(n)
    g, w = (g + 1) / 2, w / 2
    U, V = np.meshgrid(g, g, indexing="ij")
    WU, WV = np.meshgrid(w, w, indexing="ij")
    return np.stack([(U * (1 - V)).ravel(), (U * V).ravel()], 1), (WU * WV * U).ravel()


def p2(pts):
    x, y = pts[:, 0], pts[:, 1]
    l0, l1, l2 = 1 - x - y, x, y
    N = np.stack([l0 * (2 * l0 - 1), l1 * (2 * l1 - 1), l2 * (2 * l2 - 1), 4 * l0 * l1, 4 * l1 * l2, 4 * l2 * l0], 1)
    g0, g1, g2 = np.array([-1.0, -1.0]), np.array([1.0, 0.0]), np.array([0.0, 1.0])
    dN = np.zeros((len(x), 6, 2))
    dN[:, 0] = (4 * l0 - 1)[:, None] * g0
    dN[:, 1] = (4 * l1 - 1)[:, None] * g1
    dN[:, 2] = (4 * l2 - 1)[:, None] * g2
    dN[:, 3] = 4 * (l1[:, None] * g0 + l0[:, None] * g1)
    dN[:, 4] = 4 * (l2[:, None] * g1 + l1[:, None] * g2)
    dN[:, 5] = 4 * (l0[:, None] * g2 + l2[:, None] * g0)
    return N, dN


QPTS, QW = conical_rule()
NQ, DNQ = p2(QPTS)


def assemble(W, coef, Nt):
    Np = max(3, round(Nt * W / 2))
    thv = 0.5 * PI * (1 - np.cos(PI * np.linspace(0, 1, Nt + 1)))
    thv[0], thv[-1] = 0.0, PI
    thI = np.empty(2 * Nt + 1)
    thI[0::2], thI[1::2] = thv, 0.5 * (thv[:-1] + thv[1:])
    sJ = np.linspace(0, 1, 2 * Np + 1)
    wI = phi_R(W, coef, thI)[0] + W
    if np.any(wI <= 0):
        raise ValueError("the domain collapses")
    nI, nJ = 2 * Nt + 1, 2 * Np + 1
    dof = np.empty((nI, nJ), dtype=np.int64)
    dof[0], dof[1:-1], dof[-1] = 0, 1 + np.arange((nI - 2) * nJ).reshape(nI - 2, nJ), 1 + (nI - 2) * nJ
    ndof = 2 + (nI - 2) * nJ
    ii, jj = (a.ravel() for a in np.meshgrid(np.arange(Nt), np.arange(Np), indexing="ij"))
    VA = np.stack([np.stack([ii + 1, jj + 1], 1), np.stack([ii, jj], 1), np.stack([ii, jj + 1], 1)], 1)
    VB = np.stack([np.stack([ii, jj], 1), np.stack([ii + 1, jj + 1], 1), np.stack([ii + 1, jj], 1)], 1)
    G = 2 * np.concatenate([VA, VB], 0)
    G6 = np.concatenate([G, np.stack([(G[:, 0] + G[:, 1]) // 2, (G[:, 1] + G[:, 2]) // 2, (G[:, 2] + G[:, 0]) // 2], 1)], 1)
    I6, J6 = G6[:, :, 0], G6[:, :, 1]
    th6, ph6, dofs6 = thI[I6], -W + sJ[J6] * wI[I6], dof[I6, J6]
    thq, phq = th6 @ NQ.T, ph6 @ NQ.T
    dth, dph = np.einsum("ek,qkd->eqd", th6, DNQ), np.einsum("ek,qkd->eqd", ph6, DNQ)
    A, B, C, D = dth[..., 0], dth[..., 1], dph[..., 0], dph[..., 1]
    det = A * D - B * C
    Gx, Gy = DNQ[None, :, :, 0], DNQ[None, :, :, 1]
    Nth = (D[..., None] * Gx - C[..., None] * Gy) / det[..., None]
    Nph = (-B[..., None] * Gx + A[..., None] * Gy) / det[..., None]
    st = np.sin(thq)
    w1, w2 = QW[None] * np.abs(det) * st, QW[None] * np.abs(det) / st
    Ke = np.einsum("eq,eqk,eql->ekl", w1, Nth, Nth) + np.einsum("eq,eqk,eql->ekl", w2, Nph, Nph)
    Me = np.einsum("eq,qk,ql->ekl", w1, NQ, NQ)
    rows, cols = np.repeat(dofs6[:, :, None], 6, 2).ravel(), np.repeat(dofs6[:, None, :], 6, 1).ravel()
    Kg = sps.csr_matrix((Ke.ravel(), (rows, cols)), shape=(ndof, ndof))
    Mg = sps.csr_matrix((Me.ravel(), (rows, cols)), shape=(ndof, ndof))
    X = np.stack([st * np.cos(phq), st * np.sin(phq), np.cos(thq)], -1)
    laps = np.unique(np.concatenate([dof[:, 0], dof[:, -1]]))
    return dict(K=(0.5 * (Kg + Kg.T)).tocsc(), M=(0.5 * (Mg + Mg.T)).tocsc(), dofs6=dofs6, w1=w1, w2=w2, Nth=Nth,
                Nph=Nph, X=X, laps=laps, ndof=ndof)


def rayleigh(m, u):
    ue = u[m["dofs6"]]
    u0 = ue - ue.mean(1, keepdims=True)
    uth, uph = np.einsum("eqk,ek->eq", m["Nth"], u0), np.einsum("eqk,ek->eq", m["Nph"], u0)
    uq = np.einsum("qk,ek->eq", NQ, ue)
    return float((np.sum(m["w1"] * uth**2) + np.sum(m["w2"] * uph**2)) / np.sum(m["w1"] * uq**2))


def tilt_distance(m, u):
    uq = np.einsum("qk,ek->eq", NQ, u[m["dofs6"]])
    w, X = m["w1"], m["X"]
    a = np.linalg.solve(np.einsum("eq,eqc,eqd->cd", w, X, X), np.einsum("eq,eq,eqc->c", w, uq, X))
    r = uq - X @ a
    return float(np.sqrt(np.sum(w * r * r) / np.sum(w * uq * uq)))


@lru_cache(maxsize=None)
def solve(W, coef, Nt, dirichlet=False):
    m = assemble(W, coef, Nt)
    K, M = m["K"], m["M"]
    keep = np.setdiff1d(np.arange(m["ndof"]), m["laps"]) if dirichlet else np.arange(m["ndof"])
    Kk, Mk = K[keep][:, keep], M[keep][:, keep]
    lu = spla.splu((Kk + 0.5 * Mk).tocsc())
    op = spla.LinearOperator(Kk.shape, matvec=lu.solve, dtype=float)
    vals, vecs = spla.eigsh(Kk, k=3, M=Mk, sigma=-0.5, which="LM", OPinv=op, tol=0)
    order = np.argsort(vals)
    full = np.zeros((m["ndof"], 3))
    full[keep] = vecs[:, order]
    rq = [rayleigh(m, full[:, j]) for j in range(3)]
    return tuple(rq), tilt_distance(m, full[:, 1])


def extrapolate(vals):
    v = np.asarray(vals, float)
    Rx = v[1:] + (v[1:] - v[:-1]) / 15.0
    return float(Rx[-1]), float(abs(Rx[-1] - Rx[-2]))


def level(W, coef, dirichlet=False, which=1):
    """The `which`-th level (0 bottom), extrapolated over LEVELS, with its error."""
    return extrapolate([solve(W, coef, Nt, dirichlet)[0][which] for Nt in LEVELS])


def tilt(W, coef):
    """The mode's distance from the tilts at the finest level, with the last refinement's change as its error."""
    d = [solve(W, coef, Nt)[1] for Nt in LEVELS]
    return d[-1], abs(d[-1] - d[-2])


def P(W, name):
    return 3 / (4 * W) * quad(lambda t: (math.sin(t) ** 2 - 2 * math.cos(t) ** 2) * bump(name, np.array([t]))[0],
                              0, PI, points=[BUMPS[name][0]], limit=200, epsabs=1e-14, epsrel=1e-13)[0]


def coef_of(t=0.0, tau=0.0):
    return tuple((n, a) for n, a in (("mid", round(t, 15)), ("tip", round(tau, 15))) if a)


@lru_cache(maxsize=None)
def root(W, t):
    """τ(t) by the secant method on the extrapolated level, started from the first-order root."""
    kap = P(W, "mid") / P(W, "tip")
    f = lambda tau: level(W, coef_of(t, tau))[0] - 2
    x0, x1 = -kap * t, -kap * t * (1 + 1e-3)
    f0, f1 = f(x0), f(x1)
    for _ in range(30):
        if f1 == f0:
            break
        x0, x1, f0 = x1, x1 - f1 * (x1 - x0) / (f1 - f0), f1
        f1 = f(x1)
        if abs(x1 - x0) < 1e-13:
            break
    return x1


def v1(plant=False):
    for W in WIDTHS:
        (l0, _), (l1, e1), (l2, _) = (level(W, (), dirichlet=plant, which=k) for k in range(3))  # planted: Dirichlet laps
        d, _ = tilt(W, ())
        if not (abs(l0) < 1e-8 and abs(l1 - 2) <= max(e1, 1e-12) and e1 < 1e-7 and l2 - 2 >= 1 and d < 1e-6):
            return False
    return True


def slope(W, name):
    lam = {e: level(W, coef_of(**({"t": e} if name == "mid" else {"tau": e})))[0] for e in (-0.02, -0.01, 0.01, 0.02)}
    return (8 * (lam[0.01] - lam[-0.01]) - (lam[0.02] - lam[-0.02])) / (12 * 0.01)


def v2(plant=False):
    for W in WIDTHS:
        for name in ("mid", "tip"):
            p = (-1 if plant else 1) * P(W, name)  # planted: the formula with its sign flipped
            if abs(slope(W, name) - p) > 2e-6 * abs(p):
                return False
    return True


def v3(plant=False):
    for W in WIDTHS:
        for t in (0.05, 0.1):
            coef = (("mid", t),) if plant else (("rot", t),)  # planted: an uncompensated bump
            lam, err = level(W, coef)
            if abs(lam - 2) > max(err, 1e-12) or err > 1e-7:
                return False
    return True


def bracket(W, t, plant=False):
    tau = 0.0 if plant else root(W, t)  # planted: the bracket placed at τ = 0
    delta = 0.0 if plant else 1e-4
    return [(x,) + level(W, coef_of(t, x)) for x in (tau - delta, tau + delta)]


def v4(plant=False):
    for W in WIDTHS:
        for t in TS:
            (_, lo, elo), (_, hi, ehi) = bracket(W, t, plant)
            if not ((lo - 2) * (hi - 2) < 0 and abs(lo - 2) >= 10 * elo and abs(hi - 2) >= 10 * ehi):
                return False
    return True


def v5(plant=False):
    for W in ((PI / 2,) if plant else WIDTHS):  # planted: the critical width, where 2 is double
        for t in ((0.0,) if plant else TS):
            coef = coef_of(t, root(W, t)) if t else ()
            (l0, _), (l1, e1), (l2, _) = (level(W, coef, which=k) for k in range(3))
            if not (abs(l0) < 1e-8 and abs(l1 - 2) <= max(e1, 1e-9) and l2 - 2 >= 1):
                return False
    return True


def kg_max(W, coef):
    th = np.linspace(1e-3, PI - 1e-3, 20001)
    ph, ph1, ph2 = phi_R(W, coef, th)
    moved = np.max(np.abs(geodesic_curvature(th, ph, ph1, ph2)))
    fixed = np.max(np.abs(geodesic_curvature(th, -W + 0 * th, 0 * th, 0 * th)))
    return moved, fixed


def v6(plant=False):
    for W in WIDTHS:
        for t in TS:
            moved, fixed = kg_max(W, () if plant else coef_of(t, root(W, t)))  # planted: the unmoved lap
            if not (moved >= 0.5 and fixed < 1e-9):
                return False
    return True


def v7(plant=False):
    for W in WIDTHS:
        for t in TS:
            d, e = tilt(W, () if plant else coef_of(t, root(W, t)))  # planted: M(W) itself
            if not (d >= 1e-4 and d >= 100 * e):
                return False
    return True


def v8(plant=False):
    th = np.linspace(1e-3, PI - 1e-3, 20001)
    for W in WIDTHS:
        for t in TS:
            coef = coef_of(t, root(W, t))
            if plant:  # planted: the root profile scaled by 30
                coef = tuple((n, 30 * a) for n, a in coef)
            if not np.max(phi_R(W, coef, th)[0]) < PI - W:
                return False
    return True


CHECKS = [
    ("V1 on M(W) the bottom is 0 and 2/R² is the first positive level, simple, carried by the tilt x_p", v1),
    ("V2 the first variation along each profile matches (3/(4WR³)) ∫ (sin² − 2cos²)(s/R) V ds", v2),
    ("V3 turning the lap rigidly leaves the level at 2/R²", v3),
    ("V4 for each t a bracket in τ changes the sign of λ₁ − 2/R², each end at least 10 times its error", v4),
    ("V5 at each root 2/R² is the first positive level and simple", v5),
    ("V6 at each root the moved lap is curved, the fixed lap geodesic", v6),
    ("V7 at each root the 2/R² mode is not a rigid tilt", v7),
    ("V8 every band computed is embedded in RP²", v8),
]


def report():
    print("W/R  t      τ(t)       τ/t     bracket ends: λ₁ − 2 (error)          λ₂ − 2   max|k_g|R  sup|V|/R  tilt distance")
    for W in WIDTHS:
        for t in TS:
            tau = root(W, t)
            (_, lo, elo), (_, hi, ehi) = bracket(W, t)
            l2, _ = level(W, coef_of(t, tau), which=2)
            d, _ = tilt(W, coef_of(t, tau))
            print(f"{W:.1f}  {t:<5}  {tau:.6f}  {tau / t:.4f}  {lo - 2:+.1e} ({elo:.0e}), {hi - 2:+.1e} ({ehi:.0e})"
                  f"  {l2 - 2:.3f}    {kg_max(W, coef_of(t, tau))[0]:.2f}      {max(t, abs(tau)):.3f}     {d:.2e}")
    for W in WIDTHS:
        print(f"W/R = {W}: P[b_mid] = {P(W, 'mid'):.7f}, P[b_tip] = {P(W, 'tip'):.7f}; "
              f"computed slopes {slope(W, 'mid'):.7f}, {slope(W, 'tip'):.7f}")


def main():
    res = {name: fn() for name, fn in CHECKS}
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    report()
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
