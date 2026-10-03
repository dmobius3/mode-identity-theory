#!/usr/bin/env python3
"""The cross-check of smoothed-cone-limit.md §III, run after Steps 0 and 1 landed; R = 1.

The class: metric dy² + a_ε(y)² dw² with a_ε² = cos²y + ε² on the band's rectangle, seam (0, w) ~ (π, −w), Neumann
edges. Only the transverse-constant sector n = 0 carries the declared curves, and it does not depend on W. With
δ = y − π/2 and s = ∫₀^δ dδ'/a_ε, that sector is −Y'' = λ a_ε² Y on s ∈ [−F, F], F = K(m)/(1+ε²)^{1/2}, m = 1/(1+ε²),
a_ε² even in s. With u, v the even and odd solutions at s = 0 (u(0) = 1, u'(0) = 0; v(0) = 0, v'(0) = 1), the seam
gives the levels: twisted (antiperiodic) at u(F) = 0 or v'(F) = 0, untwisted (periodic) at u'(F) = 0 or v(F) = 0.

Method A integrates in s (DOP853); method B integrates the same solutions in δ, as (Y, P = a_ε Y_δ), at ε ≥ 1e−3.
Proposition 1's bounds on the twisted bottom: lower 1/(E(m)K(m)), upper F/∫₀^F s² a_ε² ds, both exact at every ε.
The declared curve: the root ν(ν+1) in (0, 2) of the paper's −γ − ψ(ν+1) − (π/2)cot(πν/2) = ln(ε/4).

Thresholds were fixed before the first run and not changed after it.
Checks (exit 1 on any failure):
  V1  methods A and B agree on the four lowest twisted and three lowest positive untwisted levels to relative
      1e−8, at ε = 1e−1, 1e−2, 1e−3
  V2  the s-integration lands on the seam: |δ(F) − π/2| < 1e−9 at every ε
  C1  the twisted bottom lies between Proposition 1's lower and upper bounds at every ε (relative slack 1e−9)
  C2  the twisted bottom is within relative 1e−3 of the declared curve at every ε ≤ 1e−3
  C3  the next twisted level is within 1e−3 of 2 at every ε ≤ 1e−3
  C4  the twisted and untwisted levels merge: |t_k − u_k|, k = 0..3, strictly decreases as ε decreases
--arms plants a defect for each check and requires it to fire."""
import sys
import numpy as np
import mpmath as mp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

EPS = [1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12]
B_EPS = [1e-1, 1e-2, 1e-3]
TOP = 22.0
RTOL, ATOL = 1e-12, 1e-14
mp.mp.dps = 60


def ellipk_exact(eps):
    """K(m) for m = 1/(1+eps^2), by the AGM with 1 - m = eps^2/(1+eps^2) formed exactly: forming 1 - m from m loses
    digits to cancellation at small eps."""
    e = mp.mpf(eps)
    return mp.pi / (2 * mp.agm(1, e / mp.sqrt(1 + e ** 2)))


def half_length(eps):
    return float(ellipk_exact(eps) / mp.sqrt(1 + mp.mpf(eps) ** 2))


def lower_bound(eps):
    m = 1 / (1 + mp.mpf(eps) ** 2)
    return float(1 / (mp.ellipe(m) * ellipk_exact(eps)))


def declared_curve(eps):
    g = lambda nu: -mp.euler - mp.digamma(nu + 1) - mp.pi / 2 * mp.cot(mp.pi * nu / 2) - mp.log(mp.mpf(eps) / 4)
    nu = mp.findroot(g, (mp.mpf("1e-30"), mp.mpf(1) - mp.mpf("1e-30")), solver="anderson")
    return float(nu * (nu + 1))


def shoot_s(lam, eps, F, plant=None):
    end = F * (1 + 1e-6) if plant == "overshoot" else F
    def rhs(s, z):
        d, u, up, v, vp, acc = z
        w = np.sin(d) ** 2 + eps ** 2
        return [np.sqrt(w), up, -lam * w * u, vp, -lam * w * v, s * s * w]
    sol = solve_ivp(rhs, (0.0, end), [0.0, 1.0, 0.0, 0.0, 1.0, 0.0], method="DOP853", rtol=RTOL,
                    atol=[ATOL * eps, ATOL, ATOL, ATOL, ATOL, ATOL])      # delta's tolerance on the neck's scale
    return sol.y[:, -1]


def shoot_delta(lam, eps, plant=None):
    e = eps * 1.001 if plant == "bad-eps" else eps   # a constant factor on a_ε would cancel from −(aY')'/a
    def rhs(d, z):
        a = np.sqrt(np.sin(d) ** 2 + e ** 2)
        yu, pu, yv, pv = z
        return [pu / a, -lam * a * yu, pv / a, -lam * a * yv]
    sol = solve_ivp(rhs, (0.0, np.pi / 2), [1.0, 0.0, 0.0, 1.0], method="DOP853", rtol=RTOL, atol=ATOL)
    return sol.y[:, -1]


# branch functions: index into (d, u, up, v, vp) for method A and (yu, pu, yv, pv) for method B
A_IDX = {"tw-even": 1, "tw-odd": 4, "un-even": 2, "un-odd": 3}
B_IDX = {"tw-even": 0, "tw-odd": 3, "un-even": 1, "un-odd": 2}


def roots_A(eps, F, branch):
    f = lambda lam: shoot_s(lam, eps, F)[A_IDX[branch]]
    grid = np.concatenate([np.geomspace(1e-4, 0.5, 60), np.linspace(0.5, TOP, 220)[1:]])
    vals = [f(x) for x in grid]
    out = []
    for x0, x1, f0, f1 in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if f0 == 0.0:
            out.append(x0)
        elif f0 * f1 < 0:
            out.append(brentq(f, x0, x1, xtol=1e-15, rtol=1e-15, maxiter=200))
    return out


def refine_B(eps, branch, guess, plant=None):
    f = lambda lam: shoot_delta(lam, eps, plant)[B_IDX[branch]]
    lo, hi = guess * (1 - 1e-4), guess * (1 + 1e-4)
    if f(lo) * f(hi) > 0:
        return float("nan")
    return brentq(f, lo, hi, xtol=1e-15, rtol=1e-15, maxiter=200)


def levels(eps, plant=None):
    F = half_length(eps)
    z0 = shoot_s(0.0, eps, F, plant)
    rts = {b: roots_A(eps, F, b) for b in A_IDX}
    tw = sorted(rts["tw-even"] + rts["tw-odd"])
    un = sorted([0.0] + rts["un-even"] + rts["un-odd"])
    branches = {r: b for b in A_IDX for r in rts[b]}
    return {"F": F, "seam": z0[0], "acc": z0[5], "tw": tw[:4], "un": un[:4], "branch": branches}


def run(plant=None, rows=None):
    if rows is None or plant == "overshoot":
        rows = {e: levels(e, plant if plant == "overshoot" else None) for e in EPS}
    r = {}
    bad = []
    for e in B_EPS:
        row = rows[e]
        for lam in row["tw"] + [x for x in row["un"] if x > 0]:
            b = refine_B(e, row["branch"][lam], lam, plant if plant == "bad-eps" else None)
            if not (abs(b - lam) <= 1e-8 * abs(lam)):
                bad.append((e, lam, b))
    r["V1 methods A and B agree on the levels to relative 1e-8"] = not bad
    r["V2 the s-integration lands on the seam to 1e-9"] = all(abs(rows[e]["seam"] - np.pi / 2) < 1e-9 for e in EPS)
    ok1 = True
    for e in EPS:
        t0 = rows[e]["tw"][0] * (1.1 if plant == "shift-bottom" else 1.0)
        lo, up = lower_bound(e), rows[e]["F"] / rows[e]["acc"]
        ok1 &= lo * (1 - 1e-9) <= t0 <= up * (1 + 1e-9)
    r["C1 the twisted bottom lies between Proposition 1's bounds"] = bool(ok1)
    ok2 = True
    for e in EPS:
        if e <= 1e-3:
            cur = (1 / np.log(4 / e)) if plant == "first-order-curve" else declared_curve(e)
            ok2 &= abs(rows[e]["tw"][0] - cur) <= 1e-3 * cur
    r["C2 the twisted bottom is within relative 1e-3 of the declared curve"] = bool(ok2)
    target = 6.0 if plant == "wrong-level" else 2.0
    r["C3 the next twisted level is within 1e-3 of 2"] = all(abs(rows[e]["tw"][1] - target) < 1e-3 for e in EPS if e <= 1e-3)
    ok4 = True
    for k in range(4):
        diffs = [abs(rows[e]["tw"][k] - (rows[e]["tw"][k] + 0.01 if plant == "no-merge" else rows[e]["un"][k])) for e in EPS]
        ok4 &= all(d1 < d0 for d0, d1 in zip(diffs[:-1], diffs[1:]))
    r["C4 the twisted and untwisted levels merge as eps decreases"] = bool(ok4)
    return r, rows


def table(rows):
    print("eps      F        t0 (twisted bottom)   declared curve       rel gap     lower bound          upper bound          t1 - 2")
    for e in EPS:
        row = rows[e]
        t0, cur = row["tw"][0], declared_curve(e)
        print(f"{e:7.0e}  {row['F']:7.4f}  {t0:.15f}  {cur:.15f}  {abs(t0 - cur) / cur:9.2e}  {lower_bound(e):.15f}  "
              f"{row['F'] / row['acc']:.15f}  {row['tw'][1] - 2:+.2e}")
    print("eps      |t_k - u_k| for k = 0, 1, 2, 3                          twisted t0..t3")
    for e in EPS:
        row = rows[e]
        d = "  ".join(f"{abs(a - b):.6e}" for a, b in zip(row["tw"], row["un"]))
        print(f"{e:7.0e}  {d}    " + "  ".join(f"{x:.9f}" for x in row["tw"]))


def main():
    res, rows = run()
    table(rows)
    names = list(res)
    for name in names:
        print(("PASS " if res[name] else "FAIL ") + name)
    green = all(res.values())
    if "--arms" in sys.argv:
        assert green, "arms need a green parent"
        rc = 0
        V1, V2, C1, C2, C3, C4 = names
        plants = {"bad-eps": [V1],             # method B run at ε·1.001
                  "overshoot": [V2],           # the s-integration run 1e-6 past F
                  "shift-bottom": [C1],        # the computed bottom raised by 10%
                  "first-order-curve": [C2],   # compared with 1/ln(4/ε) instead of the declared root
                  "wrong-level": [C3],         # the next level compared with 6
                  "no-merge": [C4]}            # untwisted levels replaced by twisted ones + 0.01
        for plant, targets in plants.items():
            r_p, _ = run(plant, rows)
            for t in targets:
                fired = not r_p[t]
                print(("ARM FIRED " if fired else "ARM SILENT ") + f"{t} [{plant}]")
                rc |= 0 if fired else 1
        return rc
    return 0 if green else 1


if __name__ == "__main__":
    sys.exit(main())
