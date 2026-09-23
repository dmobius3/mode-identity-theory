#!/usr/bin/env python3
"""The ceiling Euclid Row IV is scored against (euclid-dr1.md, re-registration of 2026-09-23).

Boylan-Kolchin (2023, Nature Astronomy 7, 731; arXiv:2208.01611) bounds the abundance of galaxies above a stellar
mass M* by the halo mass function at full conversion efficiency (epsilon = 1):

  n_ceil(>M*, z)   = n_halo(>M*/f_b, z)          cumulative comoving number density    [Mpc^-3]
  rho_ceil(>M*, z) = f_b * rho_m(>M*/f_b, z)     cumulative comoving stellar-mass density [M_sun Mpc^-3]

A measured abundance averages over its redshift window, so the row compares it with the ceiling averaged over the
same window, weighted by the comoving volume element (window_ceiling below).

Method as the paper states it: Planck 2018 base LCDM with H0 = 67.32, Omega_m = 0.3158, n_s = 0.96605,
sigma_8 = 0.8120, f_b = 0.156; the Sheth & Tormen (1999) halo mass function. The linear power spectrum comes from
CAMB (the paper used the hmf package, which does the same), normalised to sigma_8 at z = 0, with one massive
neutrino of 0.06 eV as in the Planck base model. Masses in M_sun, volumes in comoving Mpc^3, no h.

  C1  number-density arm: for the paper's z ~ 9.1 candidate (Labbe et al., arXiv:2207.12446, sample_revision3 at
      commit 59fbbfa: id 35300, z = 9.077, log M* = 10.397), peak heights at epsilon = 1, 0.32, 0.1 within 0.15 of
      the paper's stated 4.5, 5.4, 6.4, and halo number densities within 0.30 dex of its stated 10^-5.2, 10^-7,
      10^-9.3
  C2  stellar-mass-density arm: the conversion efficiencies the paper finds for the stellar-mass densities of its
      two most massive candidates, 0.99 at z ~ 9.1 and 0.84 at z ~ 7.5, and 0.57 for the z ~ 9.1 density at its
      lower 1-sigma edge, each within 0.05. The densities are the paper's own (github.com/mrbk/JWST_MstarDensity at
      commit a5794dd, mass_cumul_z9.dat and mass_cumul_z8.dat): one galaxy of 2.49e10 M_sun, lower edge 4.24e9, over
      8.5 < z < 10 (id 35300), and one of 5.46e10 over 7 < z < 8.5 (id 38094, z = 7.477), each in 38 arcmin^2, with
      the volumes of the paper's own cosmology (radiation included, neutrinos massless). The efficiency is the one at
      which eps * f_b * rho_m(>M*/(eps * f_b)) equals the observed density, as the paper's code solves it.
  C3  the registered ceilings for M* >= 10^10 M_sun at z = 10, 11, 12, and averaged over 10 < z < 11, 12 and 14
  C4  context, not a score: JWST measurements above z ~ 10 against the ceiling averaged over their windows.
      Shuntov et al. 2025 (A&A 695, A20) publish a 10 < z < 12 mass function over 1520 arcmin^2 with no occupied
      bin above 10^10 M_sun (SMF_data_points.ecsv in their dataset, doi:10.5281/zenodo.14712538; their masses, in
      H0 = 70, Omega_m = 0.3, sit 0.02 dex higher in the registered cosmology, which leaves the top bin below 10^10),
      and Harvey et al. 2025 (ApJ 978, 89) tabulate none above 10^10 M_sun at 9.5 < z < 11.5 over 187 arcmin^2: for
      each, the one-sided 2-sigma Poisson limit on a zero count, and the completeness below which that limit would
      reach the ceiling. Casey et al. 2024 (ApJ 965, 98) state volume densities of about 10^-6 Mpc^-3 for
      M* ~ 10^10 at 10 < z < 14.
The control reruns C1 and C2 with sigma_8 = 0.70 and must fail both.
Needs camb 2.0.4, numpy and scipy.
"""
import sys

import camb
import numpy as np
from scipy import integrate, optimize, stats

H0, OM, NS, S8, FB, MNU = 67.32, 0.3158, 0.96605, 0.8120, 0.156, 0.06
h = H0 / 100.0
DELTA_C = 1.686
A_ST, a_ST, p_ST = 0.3222, 0.707, 0.3
RHO_M = OM * 2.775e11 * h ** 2                      # comoving matter density, M_sun / Mpc^3
C_KMS = 299792.458
CANDIDATE = (9.077, 10.397)                         # id 35300: z, log10 M*
PAPER = {1.0: (4.5, -5.2), 0.32: (5.4, -7.0), 0.1: (6.4, -9.3)}
Z9, Z8 = 9.077045913839543, 7.477300222506212       # ids 35300 and 38094 in the paper's data
RHO_PAPER = ((Z9, 2.49e10, 2.49e10, 8.5, 10.0, 0.99, "z ~ 9.1"),
             (Z9, 2.49e10, 4.24e9, 8.5, 10.0, 0.57, "z ~ 9.1, lower 1-sigma edge"),
             (Z8, 5.46e10, 5.46e10, 7.0, 8.5, 0.84, "z ~ 7.5"))
OR_PAPER = 2.4728e-5 * (1 + 3.04 * 7 / 8 * (4 / 11) ** (4 / 3)) / h ** 2   # photons and massless neutrinos
NULL_COUNTS = (("Shuntov et al. 2025", 10.0, 12.0, 1520.0), ("Harvey et al. 2025", 9.5, 11.5, 187.0))


def power(zs, s8):
    ob = FB * OM
    omnu_h2 = MNU / 93.14
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ob * h ** 2, omch2=(OM - ob) * h ** 2 - omnu_h2, mnu=MNU,
                       num_massive_neutrinos=1, omk=0.0)
    pars.InitPower.set_params(As=2.1e-9, ns=NS)
    pars.set_matter_power(redshifts=sorted(set([0.0] + list(zs)), reverse=True), kmax=200.0)
    pars.NonLinear = camb.model.NonLinear_none
    res = camb.get_results(pars)
    pk = res.get_matter_power_interpolator(nonlinear=False, hubble_units=False, k_hunit=False,
                                           var1="delta_tot", var2="delta_tot")
    return pk, (s8 / res.get_sigma8_0()) ** 2, res


def sigma(pk, scale, z, M):
    lnk = np.linspace(np.log(1e-4), np.log(150.0), 6000)
    k = np.exp(lnk)
    P = pk.P(z, k) * scale
    out = []
    for m in np.atleast_1d(M):
        x = k * (3 * m / (4 * np.pi * RHO_M)) ** (1 / 3)
        W = 3.0 * (np.sin(x) - x * np.cos(x)) / x ** 3
        out.append(np.sqrt(integrate.simpson(k ** 3 * P * W ** 2 / (2 * np.pi ** 2), x=lnk)))
    return np.array(out)


def cumulative(pk, scale, z, Mh):
    """n(>Mh), rho_m(>Mh) and the peak height at Mh, by the Sheth-Tormen mass function."""
    lnM = np.linspace(np.log(Mh), np.log(1e15), 900)
    M = np.exp(lnM)
    sig = sigma(pk, scale, z, M)
    nu2 = (DELTA_C / sig) ** 2
    f = A_ST * np.sqrt(2 * a_ST / np.pi) * (1 + (1 / (a_ST * nu2)) ** p_ST) * np.sqrt(nu2) * np.exp(-a_ST * nu2 / 2)
    dndlnM = RHO_M / M * f * np.abs(np.gradient(np.log(sig), lnM))
    return integrate.simpson(dndlnM, x=lnM), integrate.simpson(M * dndlnM, x=lnM), DELTA_C / sig[0]


def window_ceiling(pk, scale, res, z1, z2):
    """n_ceil and rho_ceil for M* >= 10^10 M_sun averaged over z1 < z < z2, weighted by the comoving volume element."""
    zs = np.linspace(z1, z2, int(round((z2 - z1) / 0.05)) + 1)
    w = res.comoving_radial_distance(zs) ** 2 * C_KMS / res.hubble_parameter(zs)
    nr = np.array([cumulative(pk, scale, z, 1e10 / FB)[:2] for z in zs])
    norm = integrate.simpson(w, x=zs)
    return integrate.simpson(nr[:, 0] * w, x=zs) / norm, FB * integrate.simpson(nr[:, 1] * w, x=zs) / norm


def comoving_volume(res, z1, z2, arcmin2):
    frac = arcmin2 / (4 * np.pi * (180 / np.pi) ** 2 * 3600)
    return 4 / 3 * np.pi * (res.comoving_radial_distance(z2) ** 3 - res.comoving_radial_distance(z1) ** 3) * frac


def paper_volume(z1, z2, arcmin2=38.0):
    """Comoving volume in the paper's own cosmology (flat, radiation included, neutrinos massless)."""
    E = lambda x: np.sqrt(OM * (1 + x) ** 3 + OR_PAPER * (1 + x) ** 4 + (1 - OM - OR_PAPER))
    dc = lambda z: C_KMS / H0 * integrate.quad(lambda x: 1 / E(x), 0, z, epsabs=0, epsrel=1e-11)[0]
    return 4 / 3 * np.pi * (dc(z2) ** 3 - dc(z1) ** 3) * arcmin2 / (4 * np.pi * (180 / np.pi) ** 2 * 3600)


def validate(s8):
    pk, scale, _ = power([CANDIDATE[0]], s8)
    rows, ok = [], True
    for eps, (nu_p, logn_p) in PAPER.items():
        n, _, nu = cumulative(pk, scale, CANDIDATE[0], 10 ** CANDIDATE[1] / (FB * eps))
        good = abs(nu - nu_p) <= 0.15 and abs(np.log10(n) - logn_p) <= 0.30
        ok = ok and good
        rows.append("eps = %.2f: nu = %.2f (paper %.1f), log10 n = %.2f (paper %.1f)" % (eps, nu, nu_p, np.log10(n), logn_p))
    return ok, rows


def validate_rho(s8):
    pk, scale, _ = power([Z9, Z8], s8)
    rows, ok = [], True
    for z, mstar, mass, z1, z2, eps_p, label in RHO_PAPER:
        rho_obs = mass / paper_volume(z1, z2)
        f = lambda eps: eps - rho_obs / (FB * cumulative(pk, scale, z, mstar / (eps * FB))[1])
        eps = optimize.brentq(f, 0.05, 5.0, xtol=1e-8)
        ok = ok and abs(eps - eps_p) <= 0.05
        rows.append("%s: log10 rho_obs = %.2f, eps = %.2f (paper %.2f)" % (label, np.log10(rho_obs), eps, eps_p))
    return ok, rows


def main():
    print("camb %s" % camb.__version__)
    ok1, rows = validate(S8)
    print("%s  C1 number-density arm, the paper's z ~ 9.1 candidate" % ("PASS" if ok1 else "FAIL"))
    for r in rows:
        print("      " + r)
    ok2, rows = validate_rho(S8)
    print("%s  C2 stellar-mass-density arm, the efficiencies the paper finds for its two most massive candidates" % ("PASS" if ok2 else "FAIL"))
    for r in rows:
        print("      " + r)
    zs = np.round(np.arange(9.5, 14.0 + 1e-9, 0.05), 2)
    pk, scale, res = power(list(zs), S8)
    print("C3  the registered ceilings, M* >= 10^10 M_sun (M_halo >= %.3e M_sun), epsilon = 1" % (1e10 / FB))
    for z in (10.0, 11.0, 12.0):
        n, rho, nu = cumulative(pk, scale, z, 1e10 / FB)
        print("      z = %4.1f: log10 n_ceil = %.2f, log10 rho_ceil = %.2f, nu = %.2f" % (z, np.log10(n), np.log10(FB * rho), nu))
    n10, rho10, _ = cumulative(pk, scale, 10.0, 1e10 / FB)
    for z2 in (11.0, 12.0, 14.0):
        n, rho = window_ceiling(pk, scale, res, 10.0, z2)
        print("      averaged over 10 < z < %2.0f: log10 n_ceil = %.2f, log10 rho_ceil = %.2f, %.2f and %.2f dex below their values at z = 10"
              % (z2, np.log10(n), np.log10(rho), np.log10(n10 / n), np.log10(FB * rho10 / rho)))
    print("C4  context, not a score: JWST measurements against the ceiling averaged over their windows")
    lam = -np.log(stats.norm.sf(2.0))
    for name, z1, z2, area in NULL_COUNTS:
        n_up = lam / comoving_volume(res, z1, z2, area)
        n_c, _ = window_ceiling(pk, scale, res, z1, z2)
        print("      %s, %.1f < z < %.1f over %.0f arcmin^2, no occupied bin above 10^10: log10 n < %.2f at 2 sigma, "
              "%.2f dex inside the ceiling (log10 %.2f); the limit reaches the ceiling only below %.1f%% completeness"
              % (name, z1, z2, area, np.log10(n_up), np.log10(n_c / n_up), np.log10(n_c), 100 * n_up / n_c))
    n_c, _ = window_ceiling(pk, scale, res, 10.0, 14.0)
    print("      Casey et al. 2024, 10 < z < 14, about 10^-6 Mpc^-3 for M* ~ 10^10: %.2f dex inside the ceiling (log10 %.2f)"
          % (np.log10(n_c) + 6.0, np.log10(n_c)))
    okc1, _ = validate(0.70)
    okc2, _ = validate_rho(0.70)
    print("control  C1 with sigma_8 = 0.70 fails the validation  %s" % ("as required" if not okc1 else "DID NOT"))
    print("control  C2 with sigma_8 = 0.70 fails the validation  %s" % ("as required" if not okc2 else "DID NOT"))
    ok = ok1 and ok2 and not okc1 and not okc2
    print("%s" % ("all checks pass; control as required" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
