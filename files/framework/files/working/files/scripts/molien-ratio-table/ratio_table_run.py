#!/usr/bin/env python3
"""The Molien shells, the full-transfer ratio table: a registered, theory-only computation.

It computes the low-l temperature spectrum that the P1 spectral-transfer prescription gives at MIT's two radii, as the
per-multipole ratio R_l = C_l(P1)/C_l(LambdaCDM) for 2 <= l <= 29, with numerator and denominator from one CAMB transfer
run. No data enter: no likelihood code or file, no support table, no published spectrum.

Order of work, as frozen in the contract (sections 2 to 4):
  0. Runtime check: exact versions, arm64, every package fingerprint, the parameter file's hash, the freeze manifest and,
     in a git working tree, a clean packet. Any mismatch ends the run as Uninformative before anything is computed.
  1. The transfer run at the comparison fit. The accuracy boost starts at 2 and rises by one until CAMB's q grid has at
     least eight points per 2 pi/chi* period from k12(R_B) up to k chi* = 1000 (by 6, or the gate fails); then the reach
     gate (the grid reaches k chi* >= 1000), the transfer settings, and every multipole from 2 to 29 computed.
  2. G2: the shell sum at R = 200 chi* reproduces CAMB's continuous spectrum to 1e-3 in each C_l for the full S^3 and the
     Molien spectra, and the same code with the 1/120 dropped fails.
  3. The table at A (R = 6130 Mpc) and B (R = 19700 Mpc): C_l(P1) by the shell sum, whose cutoff must converge.
  4. The repeat, a control and not a gate: the transfer run, the continuum and both routes' sums at the chosen boost plus
     one. Its four declared failures (an error of CAMB's own, a transfer not as registered, a route's cutoff not
     converging, a route's ratios not 28 positive finite numbers) leave the frozen table standing and make the affected
     route's two labels Unresolved; none of its numbers there enters a label. Any other failure is an infrastructure
     defect and ends the run as Uninformative.
  5. The labels, per route: shape (d_inf = max |R_l - 1| against 0.1) and separation (K_min = min(K_P1, K_Lambda) against 2),
     each Unresolved when the frozen computation and the repeat fall on opposite sides of its threshold.
A stop never discards what was computed: the record built before it is kept as a partial record, with no labels.
Erratum E1 (2026-09-14), after Run 1 stopped at G2: Delta_l is interpolated by one cubic spline on each side of CAMB's
native block boundary at k eta0 = 3000, where its grid step grows 300-fold, rather than by one spline across it, and the
script checks that the boundary is where CAMB's grid construction puts it.

This script must not run before the freeze. Before the freeze it is exercised only by ratio_table_tests.py, on synthetic
inputs, behind tripwires. After the freeze:
  .venv/bin/python ratio_table_run.py --run --data <folder holding the parameter file> --out <result file outside the packet>
"""
import argparse, hashlib, importlib.metadata as md, json, math, os, platform, re, subprocess, sys, time, traceback

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- Frozen constants (contract sections 2 to 4). Changing any after the freeze is a move that does not count (6). ----
R_A_MPC, R_B_MPC = 6130.0, 19700.0
ROUTES = (("A", R_A_MPC), ("B", R_B_MPC))
LMIN, LMAX = 2, 29
G2_TOL, G2_R_OVER_CHI = 1e-3, 200.0
CUT_START, CUT_CAP, CUT_TOL = 1024, 2 ** 21, 1e-4
SHAPE_THRESHOLD, SEPARATION_THRESHOLD = 0.1, 2.0
REACH_KCHI = 1000.0
# Erratum E1: CAMB's native block boundary, max_k_dk = max(3000, 2 maximum_l)/tau0 in SetkValuesForInt (cmbmain.f90,
# line 1324), k eta0 = 3000 for these settings at every boost; above it the grid steps about 0.04/boost Mpc^-1 (line 1330).
SPLIT_KETA0 = 3000.0
K12_B = math.sqrt(168.0) / R_B_MPC   # the smallest wavenumber either route sums: N = 12 at R_B
RUNTIME = {"python": "3.13.13", "camb": "2.0.4", "numpy": "2.5.0", "scipy": "1.18.0"}
MANIFEST = "freeze_manifest.json"
PACKET_FILES = ("ratio_table_run.py", "ratio_table_tests.py", "ratio_table_tests.out", "ratio_table_figures.py",
                "environment.json", "provenance.json", "sw_estimate.out", "isw_estimate.out")
COMPARISON_FIT = "base_plikHM_TTTEEE_lowE"
# CAMB's physics settings: v1's, as erratum E1 left them, the Planck 2018 baseline configuration (contract section 2).
CAMB_SETTINGS = {"recfast_approx_model": "planck", "deltazrei": 0.5, "bbn_table": "PArthENoPE_880.2_standard.dat",
                 "neutrino_hierarchy": "normal", "mnu": 0.06, "nnu": 3.046, "standard_neutrino_neff": 3.046,
                 "pivot_scalar": 0.05, "helium_delta_redshift": 0.5, "helium_redshiftstart": 5.0, "dark_energy_model": "ppf"}
# The transfer settings, written out (section 2): max_l 260, every multipole computed, lensing off in both of CAMB's
# flags, no nonlinear correction, max_eta_k and lAccuracyBoost at v1's values, the accuracy boost set by the grid rule.
TRANSFER = {"max_l": 260, "max_eta_k": 12000.0, "lSampleBoost": 50.0, "lAccuracyBoost": 2.0,
            "boost_start": 2, "boost_cap": 6, "points_per_period": 8}


class RunStop(Exception):
    """A gate or the runtime check failed: the run ends as Uninformative, with no labels. The record computed before the
    stop is kept as its partial record (contract section 3)."""

    def __init__(self, message, partial=None):
        super().__init__(message)
        self.partial = partial


def camb_errors():
    """CAMB's own exception classes: an error of CAMB's own is the repeat's first declared failure (section 3)."""
    try:
        from camb.baseconfig import CAMBError, CAMBValueError, CAMBUnknownArgumentError, CAMBParamRangeError, CAMBFortranError
        return (CAMBError, CAMBValueError, CAMBUnknownArgumentError, CAMBParamRangeError, CAMBFortranError)
    except ImportError:
        return ()


# ------------------------------- shells and weights: v1's code, unchanged (section 2) -------------------------------
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
    """Delta_l(k) sampled on a q grid, interpolated per l by a cubic spline in q, and zero off the grid. Given split, the index
    of CAMB's native block boundary (erratum E1), one cubic spline runs through the knots up to and including the boundary and
    serves below it, and another runs through the knots from the boundary on and serves at and above it: each passes through
    every native knot, the boundary takes its knot value, and no slope is carried across the jump in CAMB's step there."""

    def __init__(self, L, q, delta, split=None):
        from scipy.interpolate import CubicSpline
        self.q = np.asarray(q, dtype=np.float64)
        if np.any(np.diff(self.q) <= 0):
            raise RunStop("transfer q grid is not strictly increasing")
        idx = {int(l): i for i, l in enumerate(L)}
        missing = [l for l in range(LMIN, LMAX + 1) if l not in idx]
        if missing:
            raise RunStop(f"transfer data lacks l = {missing}")
        self.split = split
        if split is None:
            self.splines = {l: CubicSpline(self.q, np.asarray(delta[idx[l]], dtype=np.float64)) for l in range(LMIN, LMAX + 1)}
        else:
            if not 0 < split < len(self.q) - 1:
                raise RunStop(f"the interpolation's split, knot {split}, is not an interior knot")
            rows = {l: np.asarray(delta[idx[l]], dtype=np.float64) for l in range(LMIN, LMAX + 1)}
            self.lower = {l: CubicSpline(self.q[:split + 1], rows[l][:split + 1]) for l in rows}
            self.upper = {l: CubicSpline(self.q[split:], rows[l][split:]) for l in rows}

    def max_spacing_above(self, kmin):
        sel = self.q >= kmin
        return float(np.max(np.diff(self.q[sel]))) if sel.sum() > 1 else float("inf")

    def __call__(self, lvals, k):
        out = np.zeros((len(lvals), len(k)))
        inside = (k >= self.q[0]) & (k <= self.q[-1])
        if self.split is None:
            if np.any(inside):
                for i, l in enumerate(lvals):
                    out[i, inside] = self.splines[int(l)](k[inside])
            return out
        qb = self.q[self.split]
        below, above = inside & (k < qb), inside & (k >= qb)
        for i, l in enumerate(lvals):
            if np.any(below):
                out[i, below] = self.lower[int(l)](k[below])
            if np.any(above):
                out[i, above] = self.upper[int(l)](k[above])
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


# ------------------------------------------- the grid rule and the reach -------------------------------------------
def max_spacing_between(q, k_lo, k_hi):
    """The largest step of the q grid over the intervals that meet [k_lo, k_hi]: the grid rule's range, bounded above."""
    q = np.asarray(q, dtype=np.float64)
    meets = (q[1:] > k_lo) & (q[:-1] < k_hi)
    return float(np.max(np.diff(q)[meets])) if np.any(meets) else float("inf")


def grid_record(t):
    q, chi = np.asarray(t["q"], dtype=np.float64), float(t["chi_star"])
    required = 2 * math.pi / chi / TRANSFER["points_per_period"]
    spacing = max_spacing_between(q, K12_B, REACH_KCHI / chi)
    return {"AccuracyBoost": int(t["boost"]), "max_spacing": spacing, "required": required, "meets_rule": bool(spacing <= required),
            "reach_kchi": float(q[-1] * chi), "chi_star_mpc": chi, "n_q": int(len(q)), "boundary": native_boundary(t)[1]}


def native_boundary(t):
    """Erratum E1: CAMB's native block boundary on this grid, as (split index or None, record, fault or None). A grid that ends
    at or below k eta0 = SPLIT_KETA0 has no coarse block, and one spline serves. A grid that runs past it must have exactly one
    knot there, an interior one, at which the grid's largest step ratio sits; otherwise the fault says what differs, and the
    transfer is not as registered."""
    q = np.asarray(t["q"], dtype=np.float64)
    x = q * float(t["tau0"])
    if x[-1] <= SPLIT_KETA0:
        return None, {"k_eta0": None, "step_ratio": None}, None
    hit = np.nonzero(np.abs(x - SPLIT_KETA0) <= 1e-9 * SPLIT_KETA0)[0]
    if len(hit) != 1 or not 0 < hit[0] < len(q) - 1:
        return None, {"k_eta0": None, "step_ratio": None}, (f"CAMB's grid runs past k eta0 = {SPLIT_KETA0:g} without a single "
                                                             f"interior knot there")
    s = np.diff(q)
    ratio = s[1:] / s[:-1]
    j, top = int(hit[0]), int(np.argmax(ratio)) + 1
    rec = {"k_eta0": float(x[j]), "step_ratio": float(ratio[j - 1])}
    if top != j:
        return None, rec, f"the grid's largest step ratio is at k eta0 = {x[top]:.6g}, not at CAMB's block boundary"
    return j, rec, None


def check_transfer(t):
    """The settings that must have reached CAMB, and every multipole from 2 to 29 computed (contract section 3); from erratum
    E1, CAMB's native block boundary where its construction puts it, with the interpolation split there."""
    if t["max_l"] != TRANSFER["max_l"] or t["do_lensing"] or t["want_cmb_lensing"]:
        raise RunStop(f"the transfer settings did not reach CAMB: max_l {t['max_l']}, DoLensing {t['do_lensing']}, "
                      f"Want_CMB_lensing {t['want_cmb_lensing']}")
    split, _, fault = native_boundary(t)
    if fault:
        raise RunStop(fault)
    return GridTransfer(t["L"], t["q"], t["delta"], split=split)


# ------------------------------------------- the table and its two labels -------------------------------------------
def first_shell_share(R_mpc, transfer, pk, cl):
    """The share of each C_l(P1) carried by the first shell, N = 12."""
    N, W = shell_table(12, "molien")
    k = np.array([math.sqrt(12.0 * 14.0) / R_mpc])
    c12 = W[11] * float(np.asarray(pk(k))[0]) * transfer(np.arange(LMIN, LMAX + 1), k)[:, 0] ** 2
    return c12 / cl


def separations(ratio):
    """K_P1 and K_Lambda, the expected log-likelihood separations on an ideal, full, noiseless sky if P1 or LambdaCDM
    generated it, with their per-multipole terms and K_min, from the ratio table alone (contract section 4)."""
    r = np.asarray(ratio, dtype=np.float64)
    if r.shape != (LMAX - LMIN + 1,) or not np.all(np.isfinite(r)) or np.any(r <= 0):
        raise RunStop("the ratio table is not 28 positive, finite numbers")
    l = np.arange(LMIN, LMAX + 1, dtype=np.float64)
    tp = (2 * l + 1) / 2 * (r - 1 - np.log(r))
    tl = (2 * l + 1) / 2 * (1 / r - 1 + np.log(r))
    kp, kl = float(tp.sum()), float(tl.sum())
    return {"K_P1": kp, "K_Lambda": kl, "K_min": min(kp, kl), "terms_P1": [float(x) for x in tp], "terms_Lambda": [float(x) for x in tl]}


def shape_label(d_frozen, d_repeat):
    near = [d <= SHAPE_THRESHOLD for d in (d_frozen, d_repeat)]
    return "Near unity" if all(near) else ("Departing" if not any(near) else "Unresolved")


def separation_label(k_frozen, k_repeat):
    sep = [k >= SEPARATION_THRESHOLD for k in (k_frozen, k_repeat)]
    return "Separated" if all(sep) else ("Not separated" if not any(sep) else "Unresolved")


def continuum(t):
    return np.asarray(t["cl_lcdm_uK2"], dtype=np.float64)[LMIN:LMAX + 1] / t["tcmb2"]


def route_table(R_mpc, transfer, t):
    cl, rec = shell_sum(R_mpc, transfer, t["power"], "molien")
    ratio = cl / continuum(t)
    l = np.arange(LMIN, LMAX + 1)
    return {"R_mpc": R_mpc, "cutoff": rec, "ratio": [float(x) for x in ratio],
            "D_l_P1_uK2": [float(x) for x in cl * t["tcmb2"] * l * (l + 1) / (2 * np.pi)],
            "first_shell_share": [float(x) for x in first_shell_share(R_mpc, transfer, t["power"], cl)],
            "d_inf": float(np.max(np.abs(ratio - 1))), **separations(ratio)}


def lcdm_dl(t):
    l = np.arange(LMIN, LMAX + 1)
    return [float(x) for x in np.asarray(t["cl_lcdm_uK2"], dtype=np.float64)[LMIN:LMAX + 1] * l * (l + 1) / (2 * np.pi)]


def frozen_computation(p, compute, out):
    """The grid rule, the reach gate, G2 and both routes' tables; each gate stops the run (section 3). Everything is
    written into out as it is computed, so a stop leaves it behind as the partial record."""
    out["grid"] = []
    for boost in range(TRANSFER["boost_start"], TRANSFER["boost_cap"] + 1):
        t = compute(p, boost)
        rec = grid_record(t)
        out["grid"].append(rec)
        tr = check_transfer(t)
        if rec["meets_rule"]:
            break
    else:
        raise RunStop(f"the grid rule was not met by AccuracyBoost {TRANSFER['boost_cap']}")
    if rec["reach_kchi"] < REACH_KCHI:
        raise RunStop(f"reach gate: the grid ends at k chi* = {rec['reach_kchi']:.1f}, below {REACH_KCHI:.0f}")
    out.update({"chosen_boost": int(t["boost"]), "chi_star_mpc": float(t["chi_star"]), "derived": t.get("derived", {}),
                "q_range": [float(t["q"][0]), float(t["q"][-1])],
                "settings": {"transfer": dict(TRANSFER), "camb": dict(CAMB_SETTINGS), "G2_tolerance": G2_TOL,
                             "shape_threshold": SHAPE_THRESHOLD, "separation_threshold": SEPARATION_THRESHOLD,
                             "reach_kchi": REACH_KCHI, "radii_mpc": {"A": R_A_MPC, "B": R_B_MPC}}})
    out["LCDM_D_l_uK2"] = {"frozen": lcdm_dl(t)}
    out["G2"] = gate_g2(tr, t["power"], t["chi_star"], continuum(t))
    if not out["G2"]["passed"]:
        raise RunStop("G2 failed")
    for name, R in ROUTES:
        rt = route_table(R, tr, t)
        out[name] = {"frozen": rt}
        if not rt["cutoff"]["converged"]:
            raise RunStop(f"route {name}: the shell cutoff did not converge by N_max = {CUT_CAP}")


def repeat_control(p, compute, out, estimates):
    """The repeat, a control and not a gate (section 3). Its four declared failures leave the frozen table standing and make
    the affected route's two labels Unresolved, and none of its numbers at that route enters d_inf or K_min. Any other
    exception propagates: an infrastructure defect, which ends the run as Uninformative."""
    rep = out["repeat"] = {"AccuracyBoost": out["chosen_boost"] + 1}
    t2 = tr2 = None
    try:
        t2 = compute(p, rep["AccuracyBoost"])
        rep["grid"] = grid_record(t2)
        tr2 = check_transfer(t2)
    except camb_errors() as e:
        rep["failure"] = f"the repeat's CAMB computation failed: {type(e).__name__}: {e}"
    except RunStop as e:
        rep["failure"] = f"the repeat's transfer is not as registered: {e}"
    if tr2 is not None:
        out["LCDM_D_l_uK2"]["repeat"] = lcdm_dl(t2)
    for name, R in ROUTES:
        f = out[name]["frozen"]
        why, r = rep.get("failure"), None
        if tr2 is not None:
            try:
                r = route_table(R, tr2, t2)
                if not r["cutoff"]["converged"]:
                    why = f"the repeat's shell cutoff did not converge by N_max = {CUT_CAP}"
            except RunStop as e:
                why = f"the repeat's ratios are not 28 positive, finite numbers: {e}"
        if why is None:
            out[name]["repeat"] = {**r, "valid": True}
            out[name]["repeat_max_relative_change"] = float(np.max(np.abs(np.asarray(f["ratio"]) / np.asarray(r["ratio"]) - 1)))
            out[name]["labels"] = {"shape": shape_label(f["d_inf"], r["d_inf"]), "separation": separation_label(f["K_min"], r["K_min"])}
        else:
            failed = {"valid": False, "failure": why}
            if r is not None:
                failed.update({"cutoff": r["cutoff"], "unconverged_ratio": r["ratio"]})
            out[name]["repeat"] = failed
            out[name]["labels"] = {"shape": "Unresolved", "separation": "Unresolved", "reason": "the repeat failed at this route"}
        if estimates is not None:
            e = estimates[name]
            out[name]["estimates"] = {"sachs_wolfe": list(e["sw"]), "with_isw_to_l10": list(e["isw"])}
            out[name]["versus_estimates"] = {"sachs_wolfe": [f["ratio"][i] / e["sw"][i] for i in range(LMAX - LMIN + 1)],
                                             "with_isw_to_l10": [f["ratio"][i] / e["isw"][i] for i in range(10 - LMIN + 1)]}


def compute_all(p, compute, estimates=None):
    """Sections 3 to 5 for a transfer provider compute(p, boost). A failing gate raises RunStop. Whatever the exception, the
    record computed so far is attached to it as `partial`, so a stop never discards what was computed (section 3)."""
    out = {}
    try:
        frozen_computation(p, compute, out)
        repeat_control(p, compute, out, estimates)
    except Exception as e:
        e.partial = out
        raise
    return out


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


def estimate_ratios(packet):
    """The two pre-freeze estimates' ratios at A and B, from the packet's byte-identical copies of v1's records."""
    sw_text = open(os.path.join(packet, "sw_estimate.out"), encoding="utf-8").read()
    sw = {int(m.group(1)): (float(m.group(2)), float(m.group(3))) for m in
          re.finditer(r"^ +(\d+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+)$", sw_text, re.M)}
    isw_text = open(os.path.join(packet, "isw_estimate.out"), encoding="utf-8").read()
    head = "== C_l(P1)/C_l(LCDM) with and without the ISW term"
    if head not in isw_text:
        raise RunStop("isw_estimate.out lacks its ratio table")
    isw = {int(m.group(1)): (float(m.group(3)), float(m.group(5))) for m in
           re.finditer(r"^ +(\d+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+)$", isw_text.split(head, 1)[1], re.M)}
    if sorted(sw) != list(range(LMIN, LMAX + 1)) or sorted(isw) != list(range(LMIN, 11)):
        raise RunStop("the estimate records do not parse into l = 2..29 and l = 2..10")
    return {name: {"sw": [sw[l][i] for l in range(LMIN, LMAX + 1)], "isw": [isw[l][i] for l in range(LMIN, 11)]}
            for i, name in enumerate(("A", "B"))}


# ------------------------------------------------------- CAMB -------------------------------------------------------
def camb_params(p, accuracy_boost):
    """CAMBparams for the comparison fit, every setting written out (contract section 2)."""
    import camb
    from camb import model
    if p["mnu"] != CAMB_SETTINGS["mnu"]:
        raise RunStop(f"the fit's mnu {p['mnu']} is not the frozen {CAMB_SETTINGS['mnu']}")
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
    pars.DoLensing = False          # both lensing flags off before set_for_lmax, so max_l is exactly 260 (section 8)
    pars.Want_CMB_lensing = False
    pars.NonLinear = model.NonLinear_none
    pars.set_for_lmax(TRANSFER["max_l"], max_eta_k=TRANSFER["max_eta_k"], lens_potential_accuracy=0)
    pars.set_accuracy(AccuracyBoost=float(accuracy_boost), lSampleBoost=TRANSFER["lSampleBoost"], lAccuracyBoost=TRANSFER["lAccuracyBoost"])
    if pars.max_l != TRANSFER["max_l"] or pars.DoLensing or pars.Want_CMB_lensing or pars.max_eta_k != TRANSFER["max_eta_k"]:
        raise RunStop("the transfer settings did not reach CAMB's parameter object")
    return pars


def compute_transfer(p, boost):
    """One CAMB transfer run at the comparison fit: the temperature transfer functions on CAMB's q grid and, from the same
    run and without recomputing it, the continuous unlensed spectrum. Never called before the freeze."""
    import camb
    pars = camb_params(p, boost)
    data = camb.get_transfer_functions(pars)
    ct = data.get_cmb_transfer_data("scalar")
    der = data.get_derived_params()
    chi_star = float(data.comoving_radial_distance(der["zstar"]))
    data.power_spectra_from_transfer()
    cl = data.get_cmb_power_spectra(CMB_unit="muK", raw_cl=True, spectra=("unlensed_scalar",), lmax=LMAX)["unlensed_scalar"][:, 0]
    return {"boost": int(boost), "q": np.array(ct.q, dtype=np.float64), "L": np.array(ct.L), "delta": np.array(ct.delta_p_l_k[0], dtype=np.float64),
            "chi_star": chi_star, "tau0": float(data.tau0), "cl_lcdm_uK2": np.array(cl[: LMAX + 1], dtype=np.float64),
            "tcmb2": (pars.TCMB * 1e6) ** 2,
            "power": pars.scalar_power, "max_l": int(pars.max_l), "do_lensing": bool(pars.DoLensing),
            "want_cmb_lensing": bool(pars.Want_CMB_lensing), "derived": {k: float(v) for k, v in der.items()}}


# ------------------------------------------------------ report ------------------------------------------------------
def printed_digits(r):
    """Significant digits the report prints for R_l: as many as G2's deviations and the valid repeats support (section 4)."""
    devs = [r["G2"][s]["max_fractional_deviation"] for s in ("s3", "molien")] if "G2" in r else []
    devs += [r[n]["repeat_max_relative_change"] for n, _ in ROUTES if "repeat_max_relative_change" in r.get(n, {})]
    return int(min(6, max(2, math.floor(-math.log10(max(max(devs), 1e-12)))))) if devs else 4


def report_sections(r):
    """The tables, labels, gates and controls present in a result or a partial record."""
    lines, dg = [], printed_digits(r)
    f = lambda x: f"{x:.{dg}g}"
    rep = r.get("repeat", {})
    if "chosen_boost" in r:
        lines.append(f"Chosen AccuracyBoost {r['chosen_boost']}" + (f"; repeat at {rep['AccuracyBoost']}" if rep else "")
                     + f"; chi* = {r['chi_star_mpc']:.2f} Mpc.")
        lines.append(f"R_l printed to {dg} significant digits, the precision G2's deviations and the valid repeats support.")
    if rep.get("failure"):
        lines.append(f"The repeat failed for both routes: {rep['failure']}.")
    lines.append("")
    for name, _ in ROUTES:
        if name not in r:
            continue
        x, fr = r[name], r[name]["frozen"]
        rp = x["repeat"] if x.get("repeat", {}).get("valid") else None
        head = f"Route {name}, R = {fr['R_mpc']:.0f} Mpc."
        if "labels" in x:
            head += f"  Shape: {x['labels']['shape']}.  Separation: {x['labels']['separation']}."
        if not fr["cutoff"]["converged"]:
            head += "  Its frozen shell cutoff did not converge: the gate failed here, and this table is recorded, not labelled."
        lines.append(head)
        tot = f"  d_inf {fr['d_inf']:.4g}; K_P1 {fr['K_P1']:.4g}; K_Lambda {fr['K_Lambda']:.4g}; K_min {fr['K_min']:.4g}"
        if rp:
            tot += (f"; repeat: d_inf {rp['d_inf']:.4g}, K_P1 {rp['K_P1']:.4g}, K_Lambda {rp['K_Lambda']:.4g}, K_min {rp['K_min']:.4g}; "
                    f"largest change of R_l in the repeat {x['repeat_max_relative_change']:.2e}")
        elif "repeat" in x:
            tot += f"; the repeat failed at this route ({x['repeat']['failure']}), and its numbers enter no label"
        lines.append(tot)
        lines.append("   l   D_l LCDM   D_l P1      R_l   R_l repeat  first shell  K_P1 term  K_Lambda term  R/SW est  R/ISW est")
        lc, ve = r.get("LCDM_D_l_uK2", {}).get("frozen"), x.get("versus_estimates", {})
        for i, l in enumerate(range(LMIN, LMAX + 1)):
            sw = f"{ve['sachs_wolfe'][i]:9.3f}" if ve else "        -"
            iw = f"{ve['with_isw_to_l10'][i]:9.3f}" if ve and l <= 10 else "        -"
            lines.append(f"  {l:2d}  {(f'{lc[i]:9.2f}' if lc else '        -')}  {fr['D_l_P1_uK2'][i]:9.2f}  {f(fr['ratio'][i]):>9}  "
                         f"{(f(rp['ratio'][i]) if rp else '-'):>9}  {fr['first_shell_share'][i]:11.4f}  {fr['terms_P1'][i]:9.4f}  "
                         f"{fr['terms_Lambda'][i]:13.4f}  {sw}  {iw}")
        lines.append("")
    if "G2" in r:
        g2 = r["G2"]
        lines.append(f"G2 at R = {g2['R_mpc']:.4g} Mpc: S^3 {g2['s3']['max_fractional_deviation']:.2e}, Molien {g2['molien']['max_fractional_deviation']:.2e}, "
                     f"1/120 dropped {g2['molien_no120']['max_fractional_deviation']:.2e} (tolerance {G2_TOL:g}); passed {g2['passed']}.")
    for g in r.get("grid", []) + ([rep["grid"]] if "grid" in rep else []):
        b = g.get("boundary") or {}
        split = f"; CAMB's block boundary at k eta0 = {b['k_eta0']:.1f}, step x{b['step_ratio']:.1f}" if b.get("k_eta0") else ""
        lines.append(f"Grid at AccuracyBoost {g['AccuracyBoost']}: largest step {g['max_spacing']:.3e} against {g['required']:.3e} required, "
                     f"reach k chi* = {g['reach_kchi']:.0f}, {g['n_q']} points, {'meets' if g['meets_rule'] else 'misses'} the rule{split}.")
    for name, _ in ROUTES:
        for which in ("frozen", "repeat"):
            c = r.get(name, {}).get(which, {}).get("cutoff")
            if c:
                lines.append(f"Cutoff, route {name}, {which}: N_max {c['N_max']}, converged {c['converged']}.")
    return lines


def format_report(result):
    """The human-readable record: both routes' 28-row tables, the labels, the gates and the controls, or the partial record
    of a run that stopped."""
    lines = [f"Molien shells, the full-transfer ratio table. Status: {result['status']}."]
    if result["status"] == "Complete":
        return "\n".join(lines + report_sections(result)) + "\n"
    lines.append(f"Reason: {result.get('reason')}")
    if result.get("partial"):
        lines += ["", "Partial record: the run stopped, so no labels are assigned; what was computed before the stop is recorded as computed."]
        lines += report_sections(result["partial"])
    return "\n".join(lines) + "\n"


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
    """Every item of the contract's runtime check; returns a list of mismatches (empty when the runtime is the frozen one)."""
    bad = []
    if sys.version.split()[0] != RUNTIME["python"]:
        bad.append(f"python {sys.version.split()[0]} != {RUNTIME['python']}")
    if platform.machine() != "arm64":
        bad.append(f"machine {platform.machine()} != arm64")
    for pkg in ("camb", "numpy", "scipy"):
        try:
            v = md.version(pkg)
        except md.PackageNotFoundError:
            v = None
        if v != RUNTIME[pkg]:
            bad.append(f"{pkg} {v} != {RUNTIME[pkg]}")
    env = json.load(open(os.path.join(packet, "environment.json"), encoding="utf-8"))
    for pkg, rec in env["installed_tree_fingerprints"]["packages"].items():
        try:
            fp, n = tree_fingerprint(pkg)
            if fp != rec["tree_sha256"] or n != rec["files"]:
                bad.append(f"package fingerprint differs: {pkg}")
        except md.PackageNotFoundError:
            bad.append(f"package missing: {pkg}")
    prov = json.load(open(os.path.join(packet, "provenance.json"), encoding="utf-8"))
    entry = [f for f in prov["files"] if f["file"] == COMPARISON_FIT + ".minimum"]
    if len(entry) != 1:
        bad.append("provenance.json does not record the parameter file once")
    else:
        pth = os.path.join(data, entry[0]["file"])
        if not os.path.isfile(pth) or os.path.getsize(pth) != entry[0]["bytes"] or sha256_file(pth) != entry[0]["sha256"]:
            bad.append(f"parameter file differs or is missing: {entry[0]['file']}")
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
        if files.get("ratio_table_run.py") != sha256_file(os.path.abspath(__file__)):
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
    ap.add_argument("--run", action="store_true", help="run the frozen computation (only after the freeze)")
    ap.add_argument("--packet", default=HERE, help="the packet folder: environment.json, provenance.json, the estimates")
    ap.add_argument("--data", default=os.path.join(HERE, "planck"), help="the folder holding the parameter file")
    ap.add_argument("--out", default=None, help="the result file, outside the packet; its report is written beside it")
    ap.add_argument("--write-manifest", action="store_true", help="write the freeze manifest for the packet and exit")
    a = ap.parse_args(argv)
    if a.write_manifest:
        files = write_manifest(a.packet)
        print(f"freeze manifest written: {len(files)} files")
        return 0
    if not a.run:
        print("ratio_table_run.py runs only after the freeze; pass --run. Nothing was computed.")
        return 2
    if not a.out:
        print("--out is required, and must lie outside the packet. Nothing was computed.")
        return 2
    out = os.path.abspath(a.out)
    if os.path.commonpath([out, os.path.abspath(a.packet)]) == os.path.abspath(a.packet):
        print("--out lies inside the packet, which would break the freeze. Nothing was computed.")
        return 2
    t0 = time.time()
    result = {"script_sha256": sha256_file(os.path.abspath(__file__)), "git": git_state(a.packet),
              "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    def finish(status, reason=None):
        result.update({"status": status, "reason": reason, "seconds": round(time.time() - t0, 1)})
        json.dump(result, open(out, "w", encoding="utf-8"), indent=2, default=lambda o: o.item() if hasattr(o, "item") else str(o))
        open(os.path.splitext(out)[0] + "_report.txt", "w", encoding="utf-8").write(format_report(result))
        print(json.dumps({k: result[k] for k in ("status", "reason")}, indent=1))
        return 0 if status == "Complete" else 1

    bad = runtime_check(a.packet, a.data)
    result["runtime_check"] = {"mismatches": bad}
    if bad:
        return finish("Uninformative", "environment mismatch: " + "; ".join(bad))
    try:
        p, _ = read_minimum(os.path.join(a.data, COMPARISON_FIT + ".minimum"))
        result.update(compute_all(p, compute_transfer, estimate_ratios(a.packet)))
    except RunStop as e:
        result["partial"] = e.partial or None
        return finish("Uninformative", str(e))
    except Exception as e:
        result["traceback"] = traceback.format_exc()
        result["partial"] = getattr(e, "partial", None) or None
        return finish("Uninformative", "infrastructure failure (see traceback)")
    return finish("Complete")


if __name__ == "__main__":
    sys.exit(main())
