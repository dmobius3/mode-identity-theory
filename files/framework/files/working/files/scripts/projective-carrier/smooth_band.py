#!/usr/bin/env python3
"""The tube of half-width W around a projective line in RP²(R), first-eigenvalue.md §7; R = 1.

Fermi metric dt² + cos²t dσ², core length π, Neumann edges at t = ±W. A section of the orientation line bundle
separates as u(t)e^{ikσ} with u(−t)e^{ikπ} = −u(t): u even with k odd, or u odd with k even. The lowest level of each
branch solves −(1/f)(f u')' + (k²/f²)u = λu, f = cos t, u'(W) = 0, found by shooting from t = 0 with the parity's data.

Checks (exit 1 on any failure):
  S1  the RP² eigenfunctions: u = cos t with k = 1 and u = sin t with k = 0 solve the equation at λ = 2 exactly
  S2  at each sampled width the first twisted level is below 2 (projective-carrier.md's Theorem 2 gives every width)
  S3  the level increases across the sampled widths and is within 2e-3 of 2 at W = 1.55
  S4  at each sampled width the k = 1 even branch lies below the k = 0 odd branch; k = ±1 are degenerate at every
      width, since the equation depends only on k²
--arms plants a defect for each numerical check and requires it to fire."""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

WIDTHS = (0.25, 0.5, 1.0, 1.4, 1.5, 1.55)


def shoot(lam, W, k, even):
    def rhs(t, y):
        u, v = y
        return [v, np.tan(t) * v + (k * k / np.cos(t) ** 2 - lam) * u]
    y0 = [1.0, 0.0] if even else [0.0, 1.0]
    return solve_ivp(rhs, [0, W], y0, rtol=1e-12, atol=1e-13).y[1, -1]


def lowest(W, k, even, hi, n):
    grid = np.linspace(1e-9, hi, n)
    vals = [shoot(l, W, k, even) for l in grid]
    for a, b, fa, fb in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if fa * fb < 0:
            return brentq(shoot, a, b, args=(W, k, even), xtol=1e-12)
    raise RuntimeError(f"no root below {hi} at W = {W}")


def symbolic(k_cos=1, k_sin=0):
    t = sp.symbols("t")
    f = sp.cos(t)
    op = lambda u, k: sp.simplify(-sp.diff(f * sp.diff(u, t), t) / f + k**2 * u / f**2 - 2 * u)
    return op(sp.cos(t), k_cos) == 0 and op(sp.sin(t), k_sin) == 0 and sp.diff(sp.sin(t), t).subs(t, sp.pi / 2) == 0


def table():
    rows = []
    for W in WIDTHS:
        a, b = lowest(W, 1, True, hi=6.0, n=300), lowest(W, 0, False, hi=80.0, n=800)
        rows.append((W, a, b, min(a, b), 2 * np.pi * np.cos(W)))
    return rows


def checks(rows, sym):
    first = [r[3] for r in rows]
    return {
        "S1 RP² eigenfunctions at λ = 2 exactly": sym,
        "S2 first twisted level below 2 at each sampled width": all(x < 2 for x in first),
        "S3 increasing across the sampled widths, within 2e-3 of 2 at W = 1.55": all(p < q for p, q in zip(first, first[1:])) and 2 - first[-1] < 2e-3,
        "S4 at each sampled width the k = ±1 branch lies below the k = 0 branch": all(r[1] < r[2] for r in rows),
    }


def main():
    rows, sym = table(), symbolic()
    print("W/R    even u, k=1    odd u, k=0    first twisted level    edge length 2*pi*cos(W)")
    for W, a, b, m, e in rows:
        print(f"{W:4.2f}   {a:12.4f}   {b:11.4f}   {m:12.4f}          {e:8.4f}")
    res = checks(rows, sym)
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    if "--arms" in sys.argv:
        assert all(res.values()), "arms need a green parent"
        planted = {
            "S2 first twisted level below 2 at each sampled width": [(W, a, b, 2.0 + 1e-9 if W == 1.0 else m, e) for W, a, b, m, e in rows],
            "S3 increasing across the sampled widths, within 2e-3 of 2 at W = 1.55": list(reversed(rows)),
            "S4 at each sampled width the k = ±1 branch lies below the k = 0 branch": [(W, b, a, m, e) for W, a, b, m, e in rows],
        }
        fired = {name: not checks(bad, sym)[name] for name, bad in planted.items()}
        fired["S1 RP² eigenfunctions at λ = 2 exactly"] = not symbolic(k_cos=0)   # cos t paired with the wrong wavenumber
        for name, ok in fired.items():
            print(("ARM FIRED " if ok else "ARM SILENT ") + name)
        return 0 if all(fired.values()) else 1
    return 0 if all(res.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
