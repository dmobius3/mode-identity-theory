"""Diagnosis of the failed G1b in run 1 (2026-09-13, commit d56fe94): the gate's own computation at the frozen settings,
per multipole, and the configuration CAMB actually used. Nothing is changed and no variant is run.
Usage: CLIPY_NOJAX=1 PYTHONDONTWRITEBYTECODE=1 .venv/bin/python g1b_diagnosis.py <packet dir> <planck dir>
"""
import os, sys
pk, data = sys.argv[1], sys.argv[2]
sys.path.insert(0, pk)
import numpy as np, camb
import step_two_run as R
p, _ = R.read_minimum(os.path.join(data, R.BASELINE_FIT + ".minimum"))
theory = R.read_theory_cl_tt(os.path.join(data, R.BASELINE_FIT + ".minimum.theory_cl"))
pars = R.camb_params(p, for_g1b=True)
res = camb.get_results(pars)
tot = res.get_cmb_power_spectra(pars, CMB_unit="muK", raw_cl=True, spectra=("total",), lmax=R.LMAX)["total"][:, 0]
unl = res.get_cmb_power_spectra(pars, CMB_unit="muK", raw_cl=True, spectra=("unlensed_scalar",), lmax=R.LMAX)["unlensed_scalar"][:, 0]
print(" l   CAMB/Planck - 1   (lensed; unlensed/lensed - 1)")
dev = []
for l in range(R.LMIN, R.LMAX + 1):
    d = tot[l] / theory[l] - 1
    dev.append(abs(d))
    print(f"{l:2d}   {d:+.5f}{'  > 2e-3' if abs(d) > 2e-3 else ''}   ({unl[l] / tot[l] - 1:+.1e})")
print(f"max |dev| {max(dev):.5f} at l = {R.LMIN + int(np.argmax(dev))}; multipoles above 2e-3: "
      f"{[R.LMIN + i for i, d in enumerate(dev) if d > 2e-3]}")
print("\nconfiguration CAMB actually used:")
print(f"  H0 {pars.H0:.4f}  ombh2 {pars.ombh2}  omch2 {pars.omch2}  omnuh2 {pars.omnuh2:.6f}  YHe {pars.YHe:.5f}  TCMB {pars.TCMB}")
ne = pars.nu_mass_eigenstates
print(f"  num_nu_massive {pars.num_nu_massive}  num_nu_massless {pars.num_nu_massless:.4f}  nu_mass_eigenstates {ne}  "
      f"degeneracies {list(pars.nu_mass_degeneracies[:ne])}  fractions {list(pars.nu_mass_fractions[:ne])}  "
      f"numbers {list(pars.nu_mass_numbers[:ne])}  share_delta_neff {pars.share_delta_neff}")
print(f"  Reion: {pars.Reion}")
der = res.get_derived_params()
print("  derived: " + ", ".join(f"{k} {der[k]:.5g}" for k in ("zstar", "zdrag", "thetastar", "zre") if k in der))
print(f"  z_re {pars.Reion.redshift:.4f}; optical depth {res.get_tau():.6f} (input tau {p['tau']})" if hasattr(res, "get_tau") else f"  z_re {pars.Reion.redshift:.4f}")
print(f"  lSampleBoost {pars.Accuracy.lSampleBoost}  AccuracyBoost {pars.Accuracy.AccuracyBoost}  lAccuracyBoost {pars.Accuracy.lAccuracyBoost}")
