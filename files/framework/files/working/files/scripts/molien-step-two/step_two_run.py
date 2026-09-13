#!/usr/bin/env python3
"""Step two of the Molien shells program: the preregistered low-l test of the P1 spectral-transfer prescription.

Order of work, as frozen in step_two_contract.md:
  0. Runtime check: exact versions, JAX absent, arm64, package fingerprints and every input hash. Any mismatch ends
     the run as Uninformative before anything is evaluated.
  1. G1a, Planck interface: the packaged best-fit spectrum through clipy reproduces Commander chi2_eff 23.25721 to 0.005.
  2. G1b, CAMB: CAMB 2.0.4 at the baseline best fit reproduces that spectrum (l = 2..29) to 2e-3 and its chi2_eff to 0.2.
  3. G2, shell replacement: the shell sum at R = 200 chi* reproduces the continuous CAMB spectrum to 1e-3 for the full
     S^3 and the Molien spectra; the same code with the 1/120 dropped must fail.
  4. Scoring at A (R = 6130 Mpc, sets the Verdict) and B (R = 19700 Mpc, its own label): Delta lnL against LambdaCDM,
     the C_2/C_3 secondary, and the per-l diagnostic (ratio, Gaussianized x, support class, out-of-support detail).

This script must not run before the freeze. Before the freeze it is exercised only by step_two_tests.py, on synthetic
inputs, behind tripwires. After the freeze:  CLIPY_NOJAX=1 .venv/bin/python step_two_run.py --run
"""
import argparse, base64, contextlib, hashlib, importlib.metadata as md, importlib.util, io, json, math, os, platform, re
import subprocess, sys, time, traceback

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Frozen constants (contract sections 2 to 4). Changing any after the freeze is a move that does not count (6). ----
R_A_MPC, R_B_MPC = 6130.0, 19700.0
LMIN, LMAX = 2, 29
BAND = 2.0
G1A_REF_CHI2, G1A_TOL = 23.25721, 0.005
G1B_CL_TOL, G1B_CHI2_TOL = 2e-3, 0.2
G2_TOL, G2_R_OVER_CHI = 1e-3, 200.0
CUT_START, CUT_CAP, CUT_TOL = 1024, 2 ** 21, 1e-4
EDGE_X = 4.0
RUNTIME = {"python": "3.13.13", "camb": "2.0.4", "clipy-like": "0.15", "numpy": "2.5.0", "scipy": "1.18.0", "astropy": "8.0.1"}
MANIFEST = "freeze_manifest.json"
PACKET_FILES = ("step_two_run.py", "step_two_tests.py", "step_two_tests.out", "fetch_inputs.py", "self_test.py", "self_test.out",
                "environment.json", "provenance.json", "commander_support.json")
BASELINE_FIT = "base_plikHM_TTTEEE_lowl_lowE"   # G1a and G1b
COMPARISON_FIT = "base_plikHM_TTTEEE_lowE"      # the parameters of the comparison (section 2)
CLIK_REL = "baseline/plc_3.0/low_l/commander/commander_dx12_v3_2_29.clik"
# CAMB settings matched to the fits' .minimum.inputparams (CosmoMC Sept2017, CAMB Aug17, Recfast 1.5.2, tanh reionization,
# BBN consistency, normal hierarchy with mnu = 0.06, halofit_version 5, lensed spectra with nonlinear lensing).
# Erratum E1 (2026-09-13): the settings those files leave to the code, set as the code behind the fits set them (CosmoMC's
# 2017 CAMB calculator over CAMB Aug2017) where CAMB 2.0.4's defaults differ: the standard N_eff that fixes the neutrino
# split and the BBN input, the helium reionization width and start, PPF dark energy, curved-sky lensing, and G1b's CAMB
# l_max (2650 plus CAMB's 200 margin = 2850, CosmoMC's lmax_computed_cl + 150) and k eta_max (14000).
CAMB_SETTINGS = {"recfast_approx_model": "planck", "deltazrei": 0.5, "bbn_table": "PArthENoPE_880.2_standard.dat",
                 "neutrino_hierarchy": "normal", "mnu": 0.06, "nnu": 3.046, "pivot_scalar": 0.05, "halofit_version_int": 5,
                 "g1b_lmax": 2650, "g1b_max_eta_k": 14000.0, "lens_potential_accuracy": 1,
                 "standard_neutrino_neff": 3.046, "helium_delta_redshift": 0.5, "helium_redshiftstart": 5.0,
                 "dark_energy_model": "ppf", "lensing_method": 1}
# The transfer run for G2 and scoring: every l to 60, k eta_0 to 12000, and a grid rule fixed before the freeze. The accuracy
# boost starts at 2 and rises by 1 until the q grid has at least 8 points per acoustic period 2 pi / chi* above the smallest
# scored wavenumber (N = 12 at R_B); if that has not happened by 6, the run fails closed.
TRANSFER = {"lmax": 60, "max_eta_k": 12000.0, "lSampleBoost": 50.0, "lAccuracyBoost": 2.0,
            "boost_start": 2.0, "boost_cap": 6.0, "points_per_period": 8}


class RunStop(Exception):
    """A gate or the runtime check failed: the run ends as Uninformative (contract sections 3 and 7)."""


# ---------------------------------------- shells and weights (contract section 2) ----------------------------------------
def molien_counts(nmax):
    """m_N for N = 0..nmax from (1 + t^30) / ((1 - t^12)(1 - t^20)), by cumulative sums along residue classes."""
    c = np.zeros(nmax + 1, dtype=np.int64)
    c[0] = 1
    for s in (12, 20):
        for r in range(s):
            c[r::s] = np.cumsum(c[r::s])
    m = c.copy()
    m[30:] += c[:-30]
    return m


_TABLES = {}


def shell_table(nmax, spectrum):
    """N = 1..nmax and W_N = 4 pi (2 pi^2 / V) g_N / k_N^3, which is R-free. spectrum: 'molien' (the model),
    's3' (G2's full S^3 check, g = (N+1)^2, V = 2 pi^2 R^3) or 'molien_no120' (G2's mutation: the 1/120 dropped)."""
    key = (nmax, spectrum)
    if key not in _TABLES:
        N = np.arange(1, nmax + 1, dtype=np.float64)
        if spectrum == "s3":
            g, vol = (N + 1) ** 2, 1.0
        elif spectrum in ("molien", "molien_no120"):
            g, vol = molien_counts(nmax)[1:].astype(np.float64) * (N + 1), (120.0 if spectrum == "molien" else 1.0)
        else:
            raise ValueError(spectrum)
        _TABLES[key] = (N, 4 * np.pi * vol * g / (N * (N + 2)) ** 1.5)
    return _TABLES[key]


class GridTransfer:
    """Delta_l(k) sampled on a q grid, interpolated per l by a cubic spline in q, and zero off the grid."""

    def __init__(self, L, q, delta):
        from scipy.interpolate import CubicSpline
        self.q = np.asarray(q, dtype=np.float64)
        if np.any(np.diff(self.q) <= 0):
            raise RunStop("transfer q grid is not strictly increasing")
        idx = {int(l): i for i, l in enumerate(L)}
        missing = [l for l in range(LMIN, LMAX + 1) if l not in idx]
        if missing:
            raise RunStop(f"transfer data lacks l = {missing}")
        self.splines = {l: CubicSpline(self.q, np.asarray(delta[idx[l]], dtype=np.float64)) for l in range(LMIN, LMAX + 1)}

    def max_spacing_above(self, kmin):
        sel = self.q >= kmin
        return float(np.max(np.diff(self.q[sel]))) if sel.sum() > 1 else float("inf")

    def __call__(self, lvals, k):
        out = np.zeros((len(lvals), len(k)))
        inside = (k >= self.q[0]) & (k <= self.q[-1])
        if np.any(inside):
            for i, l in enumerate(lvals):
                out[i, inside] = self.splines[int(l)](k[inside])
        return out


def shell_sum(R_mpc, transfer, pk, spectrum, start=CUT_START, cap=CUT_CAP, tol=CUT_TOL, chunk=250_000):
    """Dimensionless C_l = sum_N W_N P(k_N) Delta_l(k_N)^2 for l = LMIN..LMAX. The upper cutoff starts at N_max = start and
    doubles until every C_l changes by less than tol on two successive doublings; every shell from N = 1 is summed."""
    lvals = np.arange(LMIN, LMAX + 1)
    Nall, Wall = shell_table(cap, spectrum)
    acc = np.zeros(len(lvals))
    done, n, changes, prev = 0, start, [], None
    while True:
        for a in range(done, n, chunk):
            b = min(n, a + chunk)
            w = Wall[a:b]
            keep = w > 0
            if np.any(keep):
                N = Nall[a:b][keep]
                k = np.sqrt(N * (N + 2)) / R_mpc
                acc = acc + (transfer(lvals, k) ** 2) @ (w[keep] * pk(k))
        done = n
        if prev is not None:
            changes.append((n, float(np.max(np.abs(acc - prev) / np.maximum(np.abs(acc), 1e-300)))))
            if len(changes) >= 2 and changes[-1][1] < tol and changes[-2][1] < tol:
                return acc, {"N_max": n, "converged": True, "changes": changes}
        prev = acc.copy()
        if n >= cap:
            return acc, {"N_max": n, "converged": False, "changes": changes}
        n = min(2 * n, cap)


# --------------------------------------------- likelihood and its support ---------------------------------------------
def classify_support(dl, lower, upper, x, lmin=LMIN):
    """Per-l position of D_l in the Commander table: interior (|x| <= 4), edge (|x| > 4, inside), or outside, with the
    bound crossed and the fractional distance beyond it for multipoles outside (contract sections 3 and 4)."""
    rows, outside = [], []
    for i in range(len(dl)):
        l, d, lo, hi = lmin + i, float(dl[i]), float(lower[i]), float(upper[i])
        if d < lo or d > hi:
            bound = lo if d < lo else hi
            row = {"l": l, "D_l": d, "x": None, "class": "outside", "bound": bound, "fractional_distance": abs(d - bound) / bound}
            outside.append(row)
        else:
            xv = None if x is None else float(x[i])
            row = {"l": l, "D_l": d, "x": xv, "class": "interior" if xv is not None and abs(xv) <= EDGE_X else "edge"}
            if row["class"] == "edge":
                row["flag"] = "unqualified interpolation"
        rows.append(row)
    return {"rows": rows, "out_of_support": bool(outside), "n_outside": len(outside),
            "outside_l": [o["l"] for o in outside],
            "max_fractional_distance_outside": max((o["fractional_distance"] for o in outside), default=0.0)}


def support_record(dl, lower, upper, splint, lmin=LMIN):
    """Classify every D_l against the table bounds first, then evaluate the Gaussianizing spline only where it is defined:
    the spline receives a copy in which each multipole outside the table sits at the bound it crossed, and x is reported
    only for multipoles inside. So the out-of-support path never asks the interpolation to leave the frozen support."""
    dl = np.asarray(dl, dtype=np.float64)
    lower, upper = np.asarray(lower, dtype=np.float64), np.asarray(upper, dtype=np.float64)
    inside = (dl >= lower) & (dl <= upper)
    x = np.full(len(dl), np.nan)
    if np.any(inside):
        x_all = np.asarray(splint(np.clip(dl, lower, upper)), dtype=np.float64)
        x[inside] = x_all[inside]
    return classify_support(dl, lower, upper, x, lmin)


class Commander:
    """The Commander low-l TT likelihood through the pinned clipy, recording what the likelihood saw at each multipole."""

    def __init__(self, clik_dir):
        os.environ["CLIPY_NOJAX"] = "1"
        import clipy
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.lkl = clipy.clik(clik_dir)
        self.load_output = buf.getvalue().strip()
        g = self.lkl._internal
        self.lmin, self.lmax = int(g.lmin), int(g.lmax)
        self.lower = np.array(g.prior[0], dtype=np.float64)
        self.upper = np.array(g.prior[1], dtype=np.float64)
        self.default_par = np.array(self.lkl.default_par, dtype=np.float64)

    def evaluate(self, cl_uK2, A_planck):
        """ln L for a TT spectrum C_l in muK^2 indexed by l = 0..lmax, and calibration A_planck, plus the support record.
        clipy returns the sentinel -1e30 when any D_l is outside the table; the record says which."""
        vec = np.concatenate([np.asarray(cl_uK2, dtype=np.float64)[: self.lmax + 1], [float(A_planck)]])
        g, captured = self.lkl._internal, {}
        orig = g.internal_lkl

        def spy(v):
            captured["dl"] = np.array(v, dtype=np.float64)
            return orig(v)

        g.internal_lkl = spy
        try:
            lnl = float(self.lkl(vec))
        finally:
            g.internal_lkl = orig
        return lnl, support_record(captured["dl"], self.lower, self.upper,
                                   lambda d: np.array(g.splint_gauss_and_deriv(d)[0], dtype=np.float64), self.lmin)


def band_label(dlnl):
    if dlnl is None:
        return "Unevaluated"
    return "Positive" if dlnl >= BAND else ("Negative" if dlnl <= -BAND else "Inconclusive")


# ------------------------------------------------------ inputs ------------------------------------------------------
def read_minimum(path):
    """Parameters (name -> value) and the per-likelihood table of a CosmoMC .minimum file."""
    params, table = {}, {}
    text = open(path, encoding="utf-8").read()
    for line in text.split("\n"):
        s = line.split()
        if len(s) >= 3 and s[0].isdigit():
            params[s[2]] = float(s[1])
    for m in re.finditer(r"^\s*([\d.]+)\s+([\d.]+)\s+CMB: (\w+) = (\S+)", text, re.M):
        table[m.group(3)] = {"minus_lnL": float(m.group(1)), "chi2": float(m.group(2)), "file": m.group(4)}
    return params, table


def read_theory_cl_tt(path):
    """C_l^TT in muK^2 for l = 0..LMAX from a .minimum.theory_cl file (columns l, D_l^TT, ...; D_l = l(l+1)C_l/2pi)."""
    cl = np.zeros(LMAX + 1)
    for line in open(path, encoding="utf-8"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        s = line.split()
        l = int(float(s[0]))
        if LMIN <= l <= LMAX:
            cl[l] = 2 * np.pi * float(s[1]) / (l * (l + 1))
    return cl


def published_c2_over_c3(path):
    """C_2/C_3 of a published spectrum file with columns l, D_l, ... (contract section 4, the secondary)."""
    d = {}
    for line in open(path, encoding="utf-8"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        s = line.split()
        l = int(float(s[0]))
        if l in (2, 3):
            d[l] = float(s[1])
    return (d[2] / 6.0) / (d[3] / 12.0)


# -------------------------------------------------------- CAMB --------------------------------------------------------
def camb_params(p, for_g1b=False, accuracy_boost=None):
    """CAMBparams for a fit's parameters, with every setting written out (contract section 2, Codes; erratum E1)."""
    import camb
    from camb import model, nonlinear
    if p["mnu"] != CAMB_SETTINGS["mnu"]:
        raise RunStop(f"the fit's mnu {p['mnu']} is not the frozen {CAMB_SETTINGS['mnu']}")
    camb.config.lensing_method = CAMB_SETTINGS["lensing_method"]
    pars = camb.CAMBparams()
    pars.set_classes(recombination_model="Recfast")
    pars.Recomb.set_params(recfast_approx_model=CAMB_SETTINGS["recfast_approx_model"])
    pars.set_dark_energy(w=-1.0, cs2=1.0, wa=0, dark_energy_model=CAMB_SETTINGS["dark_energy_model"])
    # E1: CosmoMC handed CAMB the fit's omega_nu h^2 (recorded in the .minimum for mnu = 0.06), not the mass
    pars.set_cosmology(cosmomc_theta=p["theta"] / 100.0, ombh2=p["omegabh2"], omch2=p["omegach2"], omk=0.0,
                       mnu=None, omnuh2_active=p["omeganuh2"], nnu=CAMB_SETTINGS["nnu"],
                       neutrino_hierarchy=CAMB_SETTINGS["neutrino_hierarchy"],
                       standard_neutrino_neff=CAMB_SETTINGS["standard_neutrino_neff"],
                       tau=p["tau"], YHe=None, bbn_predictor=CAMB_SETTINGS["bbn_table"])
    pars.Reion.set_extra_params(deltazrei=CAMB_SETTINGS["deltazrei"])
    pars.Reion.helium_delta_redshift = CAMB_SETTINGS["helium_delta_redshift"]
    pars.Reion.helium_redshiftstart = CAMB_SETTINGS["helium_redshiftstart"]
    pars.InitPower.set_params(As=math.exp(p["logA"]) * 1e-10, ns=p["ns"], pivot_scalar=CAMB_SETTINGS["pivot_scalar"])
    pars.WantTensors = False
    if for_g1b:
        names = {v: k for k, v in nonlinear.halofit_version_names.items()}
        pars.NonLinearModel.set_params(halofit_version=names[CAMB_SETTINGS["halofit_version_int"]])
        pars.set_for_lmax(CAMB_SETTINGS["g1b_lmax"], max_eta_k=CAMB_SETTINGS["g1b_max_eta_k"],
                          lens_potential_accuracy=CAMB_SETTINGS["lens_potential_accuracy"])
        pars.max_eta_k = CAMB_SETTINGS["g1b_max_eta_k"]   # set_for_lmax raises it to 18000 for lens_potential_accuracy = 1
        pars.NonLinear = model.NonLinear_lens
        pars.DoLensing = True
    else:
        pars.set_for_lmax(TRANSFER["lmax"], max_eta_k=TRANSFER["max_eta_k"], lens_potential_accuracy=0)
        pars.NonLinear = model.NonLinear_none
        pars.DoLensing = False
        pars.set_accuracy(AccuracyBoost=accuracy_boost, lSampleBoost=TRANSFER["lSampleBoost"], lAccuracyBoost=TRANSFER["lAccuracyBoost"])
    return pars


def transfer_run(p):
    """Transfer functions at the comparison fit under the grid rule, with the continuous (unlensed) CAMB spectrum."""
    import camb
    boost, tried = TRANSFER["boost_start"], []
    while True:
        pars = camb_params(p, accuracy_boost=boost)
        data = camb.get_transfer_functions(pars)
        ct = data.get_cmb_transfer_data("scalar")
        der = data.get_derived_params()
        chi_star = float(data.comoving_radial_distance(der["zstar"]))
        transfer = GridTransfer(ct.L, ct.q, ct.delta_p_l_k[0])
        period = 2 * np.pi / chi_star
        spacing = transfer.max_spacing_above(math.sqrt(168.0) / R_B_MPC)
        tried.append({"AccuracyBoost": boost, "max_q_spacing": spacing, "required": period / TRANSFER["points_per_period"]})
        if spacing <= period / TRANSFER["points_per_period"]:
            break
        if boost >= TRANSFER["boost_cap"]:
            raise RunStop(f"transfer grid still too coarse at AccuracyBoost {boost}: {tried}")
        boost += 1.0
    data.power_spectra_from_transfer()
    cl = data.get_cmb_power_spectra(pars, CMB_unit="muK", raw_cl=True, spectra=("unlensed_scalar",), lmax=LMAX)["unlensed_scalar"][:, 0]
    return {"transfer": transfer, "pars": pars, "chi_star": chi_star, "cl_lcdm_uK2": np.array(cl[: LMAX + 1], dtype=np.float64),
            "tcmb2": (pars.TCMB * 1e6) ** 2, "grid": tried, "q_range": [float(transfer.q[0]), float(transfer.q[-1])], "derived": der}


# ------------------------------------------------------- gates -------------------------------------------------------
def gate_g1a(commander, theory_cl, A):
    lnl, sup = commander.evaluate(theory_cl, A)
    chi2 = -2.0 * lnl
    return {"chi2_eff": chi2, "reference": G1A_REF_CHI2, "difference": chi2 - G1A_REF_CHI2, "tolerance": G1A_TOL,
            "passed": (not sup["out_of_support"]) and abs(chi2 - G1A_REF_CHI2) <= G1A_TOL, "support": sup}


def gate_g1b(p_base, theory_cl, commander, A):
    import camb
    pars = camb_params(p_base, for_g1b=True)
    res = camb.get_results(pars)
    tot = res.get_cmb_power_spectra(pars, CMB_unit="muK", raw_cl=True, spectra=("total",), lmax=LMAX)["total"][:, 0]
    tot = np.array(tot[: LMAX + 1], dtype=np.float64)
    dev = np.abs(tot[LMIN:] / theory_cl[LMIN:] - 1.0)
    lnl, sup = commander.evaluate(tot, A)
    chi2 = -2.0 * lnl
    return {"max_fractional_Cl_deviation": float(np.max(dev)), "worst_l": int(LMIN + np.argmax(dev)), "chi2_eff": chi2,
            "passed": bool(np.max(dev) <= G1B_CL_TOL and abs(chi2 - G1A_REF_CHI2) <= G1B_CHI2_TOL and not sup["out_of_support"])}


def gate_g2(transfer, pk, chi_star, cl_cont):
    R = G2_R_OVER_CHI * chi_star
    out = {"R_mpc": R}
    for spectrum in ("s3", "molien", "molien_no120"):
        cl, rec = shell_sum(R, transfer, pk, spectrum)
        out[spectrum] = {"max_fractional_deviation": float(np.max(np.abs(cl / cl_cont - 1.0))), "cutoff": rec}
    out["passed"] = bool(out["s3"]["cutoff"]["converged"] and out["molien"]["cutoff"]["converged"]
                         and out["s3"]["max_fractional_deviation"] <= G2_TOL and out["molien"]["max_fractional_deviation"] <= G2_TOL
                         and out["molien_no120"]["max_fractional_deviation"] > G2_TOL)
    return out


def score(name, R, tr, commander, A, lnl_lcdm, c2c3_published):
    cl, rec = shell_sum(R, tr["transfer"], tr["pars"].scalar_power, "molien")
    if not rec["converged"]:
        raise RunStop(f"route {name}: shell cutoff did not converge by N_max = {CUT_CAP}")
    cl_uK2 = np.zeros(LMAX + 1)
    cl_uK2[LMIN:] = cl * tr["tcmb2"]
    lnl, sup = commander.evaluate(cl_uK2, A)
    if sup["out_of_support"]:
        dlnl, label = None, "Negative"
    else:
        dlnl = lnl - lnl_lcdm
        label = band_label(dlnl)
    return {"route": name, "R_mpc": R, "label": label, "delta_lnL": dlnl if dlnl is not None else "out of support",
            "lnL": lnl, "out_of_support": sup["out_of_support"], "n_outside": sup["n_outside"], "outside_l": sup["outside_l"],
            "max_fractional_distance_outside": sup["max_fractional_distance_outside"],
            "C2_over_C3": float(cl_uK2[2] / cl_uK2[3]), "C2_over_C3_published": c2c3_published,
            "ratio_to_LCDM": {int(l): float(cl_uK2[l] / tr["cl_lcdm_uK2"][l]) for l in range(LMIN, LMAX + 1)},
            "support": sup["rows"], "cutoff": rec}


# --------------------------------------------------- runtime check ---------------------------------------------------
def tree_fingerprint(name):
    dist = md.distribution(name)
    files = [f for f in (dist.files or []) if "__pycache__" not in f.parts and not str(f).endswith(".pyc")]
    h, n = hashlib.sha256(), 0
    for f in sorted(files, key=lambda x: str(x)):
        p = f.locate()
        if os.path.isfile(p):
            h.update(str(f).encode() + b"\0" + hashlib.sha256(open(p, "rb").read()).digest())
            n += 1
    return h.hexdigest(), n


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def runtime_check(packet, data, require_manifest=True):
    """Every item of the contract's runtime check; returns a list of mismatches (empty when the runtime is the frozen one).
    After the freeze the manifest is required, so a modified script or record fails closed."""
    bad = []
    if sys.version.split()[0] != RUNTIME["python"]:
        bad.append(f"python {sys.version.split()[0]} != {RUNTIME['python']}")
    if platform.machine() != "arm64":
        bad.append(f"machine {platform.machine()} != arm64")
    if os.environ.get("CLIPY_NOJAX") != "1":
        bad.append("CLIPY_NOJAX is not 1")
    if importlib.util.find_spec("jax") is not None:
        bad.append("jax is importable")
    for pkg in ("camb", "clipy-like", "numpy", "scipy", "astropy"):
        try:
            v = md.version(pkg)
        except md.PackageNotFoundError:
            v = None
        if v != RUNTIME[pkg]:
            bad.append(f"{pkg} {v} != {RUNTIME[pkg]}")
    try:
        import clipy
        if clipy.hasjax is not False:
            bad.append("clipy.hasjax is not False")
    except Exception as e:
        bad.append(f"clipy import failed: {e}")
    env = json.load(open(os.path.join(packet, "environment.json"), encoding="utf-8"))
    for pkg, rec in env["installed_tree_fingerprints"]["packages"].items():
        try:
            fp, n = tree_fingerprint(pkg)
            if fp != rec["tree_sha256"] or n != rec["files"]:
                bad.append(f"package fingerprint differs: {pkg}")
        except md.PackageNotFoundError:
            bad.append(f"package missing: {pkg}")
    prov = json.load(open(os.path.join(packet, "provenance.json"), encoding="utf-8"))
    for f in prov["files"]:
        p = os.path.join(data, f["file"])
        if not os.path.isfile(p) or sha256_file(p) != f["sha256"]:
            bad.append(f"input differs or is missing: {f['file']}")
    for rel, rec in env["commander_file_contents"].items():
        p = os.path.join(data, CLIK_REL, rel)
        if not os.path.isfile(p) or sha256_file(p) != rec["sha256"]:
            bad.append(f"Commander file differs: {rel}")
    man = os.path.join(packet, MANIFEST)
    if os.path.isfile(man):
        files = json.load(open(man, encoding="utf-8"))["files"]
        missing = [f for f in PACKET_FILES if f not in files]
        if missing:
            bad.append(f"freeze manifest omits {missing}")
        for name, h in files.items():
            p = os.path.join(packet, name)
            if not os.path.isfile(p) or sha256_file(p) != h:
                bad.append(f"packet file differs from the freeze manifest: {name}")
        if files.get("step_two_run.py") != sha256_file(os.path.abspath(__file__)):
            bad.append("the running script is not the frozen one")
    elif require_manifest:
        bad.append("freeze manifest missing")
    gs = git_state(packet)
    if gs.get("head") and gs.get("uncommitted_changes"):
        bad.append("uncommitted changes in the packet directory")
    return bad


def write_manifest(packet):
    """The freeze manifest: the SHA-256 of every packet file, written once the packet is final (evaluates nothing)."""
    files = {f: sha256_file(os.path.join(packet, f)) for f in PACKET_FILES}
    json.dump({"written_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "files": files},
              open(os.path.join(packet, MANIFEST), "w", encoding="utf-8"), indent=2)
    return files


def git_state(path):
    try:
        head = subprocess.run(["git", "-C", path, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", path, "status", "--porcelain", "--", "."], capture_output=True, text=True, check=True).stdout
        return {"head": head, "uncommitted_changes": bool(dirty.strip())}
    except Exception:
        return {"head": None, "note": "not a git working tree"}


# -------------------------------------------------------- main --------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--run", action="store_true", help="run the frozen test (only after the freeze)")
    ap.add_argument("--packet", default=HERE, help="directory holding environment.json and provenance.json")
    ap.add_argument("--data", default=os.path.join(HERE, "planck"), help="directory holding the Planck inputs")
    ap.add_argument("--out", default=os.path.join(HERE, "step_two_result.json"))
    ap.add_argument("--write-manifest", action="store_true", help="write the freeze manifest for the packet and exit")
    a = ap.parse_args(argv)
    if a.write_manifest:
        files = write_manifest(a.packet)
        print(f"freeze manifest written: {len(files)} files")
        return 0
    if not a.run:
        print("step_two_run.py runs only after the freeze; pass --run. Nothing was evaluated.")
        return 2
    t0 = time.time()
    result = {"script_sha256": sha256_file(os.path.abspath(__file__)), "git": git_state(a.packet), "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    def finish(verdict, reason=None):
        result.update({"Verdict": verdict, "reason": reason, "seconds": round(time.time() - t0, 1)})
        json.dump(result, open(a.out, "w", encoding="utf-8"), indent=2, default=float)
        print(json.dumps({k: result[k] for k in ("Verdict", "reason")}, indent=1))
        return 0 if verdict in ("Positive", "Negative", "Inconclusive") else 1

    bad = runtime_check(a.packet, a.data)
    result["runtime_check"] = {"mismatches": bad}
    if bad:
        return finish("Uninformative", "environment mismatch: " + "; ".join(bad))
    try:
        commander = Commander(os.path.join(a.data, CLIK_REL))
        result["self_test_on_load"] = commander.load_output
        p_base, t_base = read_minimum(os.path.join(a.data, BASELINE_FIT + ".minimum"))
        p_comp, _ = read_minimum(os.path.join(a.data, COMPARISON_FIT + ".minimum"))
        if abs(p_base["chi2_lowl"] - G1A_REF_CHI2) > 5e-6:
            raise RunStop("the baseline .minimum does not carry the frozen G1a reference")
        theory = read_theory_cl_tt(os.path.join(a.data, BASELINE_FIT + ".minimum.theory_cl"))
        g1a = gate_g1a(commander, theory, p_base["calPlanck"])
        result["G1a"] = g1a
        if not g1a["passed"]:
            raise RunStop("G1a failed")
        g1b = gate_g1b(p_base, theory, commander, p_base["calPlanck"])
        result["G1b"] = g1b
        if not g1b["passed"]:
            raise RunStop("G1b failed")
        tr = transfer_run(p_comp)
        result["transfer_run"] = {"chi_star_mpc": tr["chi_star"], "grid": tr["grid"], "q_range": tr["q_range"]}
        g2 = gate_g2(tr["transfer"], tr["pars"].scalar_power, tr["chi_star"], tr["cl_lcdm_uK2"][LMIN:] / tr["tcmb2"])
        result["G2"] = g2
        if not g2["passed"]:
            raise RunStop("G2 failed")
        A = p_comp["calPlanck"]
        lnl_lcdm, sup_lcdm = commander.evaluate(tr["cl_lcdm_uK2"], A)
        result["LCDM"] = {"lnL": lnl_lcdm, "support": sup_lcdm["rows"]}
        if sup_lcdm["out_of_support"]:
            raise RunStop("the LambdaCDM comparison spectrum is outside the Commander table")
        c2c3 = published_c2_over_c3(os.path.join(a.data, "COM_PowerSpect_CMB-TT-full_R3.01.txt"))
        result["A"] = score("A", R_A_MPC, tr, commander, A, lnl_lcdm, c2c3)
        result["B"] = score("B", R_B_MPC, tr, commander, A, lnl_lcdm, c2c3)
    except RunStop as e:
        return finish("Uninformative", str(e))
    except Exception:
        result["traceback"] = traceback.format_exc()
        return finish("Uninformative", "infrastructure failure (see traceback)")
    return finish(result["A"]["label"], None)


if __name__ == "__main__":
    sys.exit(main())
