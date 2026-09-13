"""Post-verdict diagnosis (v1 closed Uninformative before this ran): which of erratum E1's settings moved G1b's spectrum.

Each setting is added alone to run 1's configuration and removed alone from run 2's. The builder is checked first to
reproduce both runs' G1b deviations exactly; nothing here evaluates the likelihood or computes a P1 quantity, and nothing
here can change v1's verdict.
Usage: CLIPY_NOJAX=1 PYTHONDONTWRITEBYTECODE=1 .venv/bin/python g1b_decompose.py <packet dir> <planck dir> <run 1 result> <run 2 result>
"""
import json, math, os, sys
pk, data, res1, res2 = sys.argv[1:5]
sys.path.insert(0, pk)
import numpy as np
import camb
from camb import model, nonlinear
import step_two_run as R

p, _ = R.read_minimum(os.path.join(data, R.BASELINE_FIT + ".minimum"))
theory = R.read_theory_cl_tt(os.path.join(data, R.BASELINE_FIT + ".minimum.theory_cl"))
ITEMS = ["standard_neff", "omnuh2_handoff", "helium_width", "helium_start", "ppf", "lensing_method", "lmax", "keta_max"]
HALOFIT = {v: k for k, v in nonlinear.halofit_version_names.items()}[5]
L = np.arange(R.LMIN, R.LMAX + 1)


def build(on):
    """Run 1's configuration (on = empty) or run 2's (on = every item), with any subset of E1's items switched on."""
    camb.config.lensing_method = 1 if "lensing_method" in on else 5
    P = camb.CAMBparams()
    P.set_classes(recombination_model="Recfast")
    P.Recomb.set_params(recfast_approx_model="planck")
    if "ppf" in on:
        P.set_dark_energy(w=-1.0, cs2=1.0, wa=0, dark_energy_model="ppf")
    nu = dict(mnu=None, omnuh2_active=p["omeganuh2"]) if "omnuh2_handoff" in on else dict(mnu=0.06)
    if "standard_neff" in on:
        nu["standard_neutrino_neff"] = 3.046
    P.set_cosmology(cosmomc_theta=p["theta"] / 100.0, ombh2=p["omegabh2"], omch2=p["omegach2"], omk=0.0, nnu=3.046,
                    neutrino_hierarchy="normal", tau=p["tau"], YHe=None, bbn_predictor="PArthENoPE_880.2_standard.dat", **nu)
    P.Reion.set_extra_params(deltazrei=0.5)
    if "helium_width" in on:
        P.Reion.helium_delta_redshift = 0.5
    if "helium_start" in on:
        P.Reion.helium_redshiftstart = 5.0
    P.InitPower.set_params(As=math.exp(p["logA"]) * 1e-10, ns=p["ns"], pivot_scalar=0.05)
    P.WantTensors = False
    P.NonLinearModel.set_params(halofit_version=HALOFIT)
    P.set_for_lmax(2650 if "lmax" in on else 2500, lens_potential_accuracy=1)
    if "keta_max" in on:
        P.max_eta_k = 14000.0
    P.NonLinear = model.NonLinear_lens
    P.DoLensing = True
    return P


def dev(on):
    P = build(set(on))
    r = camb.get_results(P)
    tot = r.get_cmb_power_spectra(P, CMB_unit="muK", raw_cl=True, spectra=("total",), lmax=R.LMAX)["total"][:, 0]
    return np.array([tot[l] / theory[l] - 1 for l in L])


A, B = dev([]), dev(ITEMS)
for name, d, path in (("run 1", A, res1), ("run 2", B, res2)):
    g1b = json.load(open(path, encoding="utf-8"))["G1b"]
    ok = abs(np.max(np.abs(d)) - g1b["max_fractional_Cl_deviation"]) < 1e-12 and int(L[np.argmax(np.abs(d))]) == g1b["worst_l"]
    print(f"builder reproduces {name}'s G1b: max |dev| {np.max(np.abs(d)):.8f} at l = {int(L[np.argmax(np.abs(d))])} "
          f"(recorded {g1b['max_fractional_Cl_deviation']:.8f} at l = {g1b['worst_l']}): {ok}")
    assert ok, f"the builder does not reproduce {name}"
total = B - A
print(f"\nE1's total shift: l = 2 {total[0]:+.5f}, l = 8 {total[6]:+.5f}, l = 9 {total[7]:+.5f}, l = 29 {total[-1]:+.5f}; "
      f"largest |shift| {np.max(np.abs(total)):.5f}")
print("\nsetting            added alone to run 1: l=2      l=8      l=29     max|.|    removed alone from run 2: l=2      l=8      l=29     max|.|")
adds = {}
for it in ITEMS:
    add = dev([it]) - A
    rem = B - dev([x for x in ITEMS if x != it])
    adds[it] = add
    print(f"{it:18} {add[0]:+.5f}  {add[6]:+.5f}  {add[-1]:+.5f}  {np.max(np.abs(add)):.5f}      "
          f"{rem[0]:+.5f}  {rem[6]:+.5f}  {rem[-1]:+.5f}  {np.max(np.abs(rem)):.5f}")
s = sum(adds.values())
print(f"\nsum of the single additions against the total shift: largest difference {np.max(np.abs(s - total)):.1e}")
pair = dev(["helium_width", "helium_start"]) - A
print(f"helium width and start added together to run 1: l = 2 {pair[0]:+.5f}, l = 8 {pair[6]:+.5f}, l = 29 {pair[-1]:+.5f}; "
      f"max |.| {np.max(np.abs(pair)):.5f}")
rest = total - pair - adds["keta_max"]
print(f"what the helium pair and keta_max leave of the total shift: largest |.| {np.max(np.abs(rest)):.1e}")
