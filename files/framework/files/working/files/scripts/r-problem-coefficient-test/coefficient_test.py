#!/usr/bin/env python3
"""What the cosmological-constant page's coefficient test can score on the coupling route (r-problem.md).

The test is Lambda_obs * R_ind^2 = 3, a departure beyond 5 sigma falsifying the coefficient relation. On the coupling
route R_ind comes from inverting the fine-structure formula alpha = C(Theta) * Omega_Lambda^(-1/60), with
C(Theta) = 2 sin^2(pi Theta) and Theta = 13/60 (fine-structure.md), against measured alpha. Everything below uses the
named anchor of the framework page: Lambda * l_P^2 = 2.845e-122, so Omega_Lambda = 3 / (Lambda * l_P^2).

A fractional error delta in the formula moves ln Omega_Lambda, and so ln Lambda_ref, by 60 * delta; the route's R
moves by half that. Measured alpha is known to about ten digits, so delta is the formula's accuracy alone, and no page
states it apart from the residual this comparison measures.

  K1  the printed values reproduce: the alpha residual (0.44%, r-problem), R near 6.1 Gpc, Lambda_ref about 23% low
      (cosmological-constant.md section V, r-problem), Lambda_ref * l_P^2 near 2.2e-122 (the Score row)
  K2  the two available readings of delta: 0 (the formula exact) and the residual itself (the residual as its own
      error bar), each for a fractional uncertainty on Lambda_obs of 1%, 2% and 3%. These are diagnostics under a
      named convention, not registered verdicts: the log-fractional figures propagate ln(Lambda_obs R^2 / 3). The
      exact reading is also shown in two linear forms, Q = Lambda_obs R^2 against 3 with Lambda_obs's fractional
      error scaled by the observed Q (ordinary propagation) or by the target 3 (a null-normalized score), since
      under the exact reading the sigma count depends on the propagation convention. The denominator is
      Lambda_obs's error, which also reaches alpha's prediction through the anchor (1/60 of it), so the alpha-space
      reading gives the same figure as the log-fractional one.
  K3  the formula accuracy at which the observed departure would sit exactly at 5 sigma, for the same three
      uncertainties; computed from the departure itself, so a diagnostic and not a criterion
  K4  the reference-scale choice: the fine-structure page's ~6% gap between alpha at q^2 = 0 and at the Z mass,
      read through the same 60-power lever, as a factor in Lambda_obs R_ind^2
The control reruns K1 at Theta = 17/60, the competitor seat on the fine-structure page, and must fail.
Standard library only.
"""
import math

LAMBDA_LP2 = 2.845e-122          # named anchor, Lambda * l_P^2
L_P_M = 1.616255e-35             # Planck length, m (CODATA 2018)
GPC_M = 3.0856775814913673e25    # 1 Gpc in m
ALPHA_OBS = 7.2973525693e-3      # CODATA 2018
GRID = 60
SIGMA_LAMBDA = (0.01, 0.02, 0.03)


def route(theta):
    omega = 3.0 / LAMBDA_LP2
    c = 2.0 * math.sin(math.pi * theta) ** 2
    alpha_pred = c * omega ** (-1.0 / GRID)
    r = math.log(alpha_pred / ALPHA_OBS)                  # ln of the formula's residual
    lever = GRID * r                                      # ln(Omega_alpha / Omega_anchor) = ln(Lambda_obs R^2 / 3)
    r_anchor = math.sqrt(3.0 / (LAMBDA_LP2 / L_P_M ** 2)) / GPC_M
    return {
        "C": c, "alpha_pred": alpha_pred, "r": r, "lever": lever,
        "R_anchor": r_anchor, "R_alpha": r_anchor * math.exp(lever / 2.0),
        "product": 3.0 * math.exp(lever), "deficit": 1.0 - math.exp(-lever),
        "lref_lp2": LAMBDA_LP2 * math.exp(-lever),
    }


def k1(v):
    return (0.0040 <= math.expm1(v["r"]) <= 0.0045 and 6.05 <= v["R_alpha"] <= 6.20
            and 0.21 <= v["deficit"] <= 0.25 and 2.15e-122 <= v["lref_lp2"] <= 2.25e-122)


def main():
    v = route(13 / 60)
    ok = k1(v)
    print(("PASS" if ok else "FAIL") + "  K1 the printed values reproduce, Theta = 13/60")
    print(f"      C(13/60) = {v['C']:.4f}, alpha predicted {v['alpha_pred']:.6f} against measured {ALPHA_OBS:.6f}: "
          f"residual {100 * math.expm1(v['r']):.3f}%")
    print(f"      60-fold lever: ln(Lambda_obs R^2 / 3) = {v['lever']:.4f}, so Lambda_obs R_ind^2 = {v['product']:.3f}")
    print(f"      R_ind = {v['R_alpha']:.3f} Gpc against the anchor's {v['R_anchor']:.4f} Gpc; Lambda_ref "
          f"{100 * v['deficit']:.1f}% below Lambda_obs, Lambda_ref l_P^2 = {v['lref_lp2']:.3e}")
    print("K2  the two readings of the formula's accuracy delta (diagnostics, not registered verdicts)")
    for s in SIGMA_LAMBDA:
        z_exact = v["lever"] / s
        z_lin_obs = (v["product"] - 3.0) / (s * v["product"])
        z_lin_null = (v["product"] - 3.0) / (s * 3.0)
        z_alpha = v["r"] / (s / GRID)
        z_resid = v["lever"] / math.hypot(GRID * v["r"], s)
        print(f"      sigma(Lambda_obs) = {100 * s:.0f}%: delta = 0 gives {z_exact:.1f} sigma log-fractional, "
              f"{z_alpha:.1f} sigma in alpha space, {z_lin_obs:.1f} sigma linear on the observed Q, "
              f"{z_lin_null:.1f} sigma null-normalized; delta = the residual gives {z_resid:.3f} sigma")
    print("K3  the formula accuracy that would put the observed departure at 5 sigma (a diagnostic, not a criterion)")
    for s in SIGMA_LAMBDA:
        delta = math.sqrt((v["lever"] / 5.0) ** 2 - s ** 2) / GRID
        print(f"      sigma(Lambda_obs) = {100 * s:.0f}%: delta = {100 * delta:.3f}%")
    scale_gap = 0.06
    print(f"K4  the reference scale: a {100 * scale_gap:.0f}% change in the alpha that is inverted moves "
          f"Lambda_obs R_ind^2 by a factor of {(1.0 + scale_gap) ** GRID:.1f}")
    c = route(17 / 60)
    fired = not k1(c)
    print(("PASS" if fired else "FAIL") + "  control: K1 fails at Theta = 17/60, as it must "
          f"(residual {100 * math.expm1(c['r']):.1f}%, Lambda_obs R^2 = {c['product']:.3g})")
    return 0 if ok and fired else 1


if __name__ == "__main__":
    raise SystemExit(main())
