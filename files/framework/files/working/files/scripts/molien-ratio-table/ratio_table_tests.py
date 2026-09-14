"""Pre-freeze tests for ratio_table_run.py and ratio_table_figures.py, on synthetic inputs only.

Tripwires make the contract's boundary mechanical: every CAMB entry point that computes a background, transfer functions or
spectra raises and fails the suite. CAMB's theta-to-H0 solver computes backgrounds, so it is replaced by a declared stub
that records theta and sets a placeholder H0 without solving anything; the parameter object is inspected with it in place.
The shell machinery is checked against v1's runner and against the Sachs-Wolfe estimate recorded before v1's freeze,
and the whole pipeline runs end to end on a synthetic transfer provider, never on CAMB. Erratum E1 restores the coarse
block the provider carried before the freeze: its grids are built as CAMB builds its own, fine up to the native block
boundary at k eta0 = 3000 and coarse above it, and on them the frozen single spline must fail G2 while the split passes.
"""
import contextlib, hashlib, importlib.util, io, json, math, os, re, shutil, subprocess, sys, tempfile
import xml.etree.ElementTree as ET
import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
V1 = os.environ.get("V1_PACKET", os.path.join(os.path.dirname(HERE), "molien-step-two"))   # v1's committed packet
DATA = os.environ.get("RATIO_TABLE_DATA", os.path.join(HERE, "planck"))                    # the parameter file, not committed
FIGDIR = os.environ.get("RATIO_TABLE_FIGDIR")                                              # optional: keep the synthetic figures

FAILS, PASSES = [], []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    (PASSES if ok else FAILS).append(label)


import camb
from camb import model as camb_model, results as camb_results
from camb.baseconfig import CAMBError


def _tripwire(*a, **k):
    raise RuntimeError("tripwire: a CAMB computation was called before the freeze")


for _name in ("get_results", "get_transfer_functions", "get_background", "get_age", "get_zre_from_tau", "get_bispectrum",
              "get_matter_power_interpolator"):
    setattr(camb, _name, _tripwire)
for _name in ("calc_background_no_thermo", "calc_background", "calc_transfers", "calc_power_spectra", "power_spectra_from_transfer"):
    setattr(camb_results.CAMBdata, _name, _tripwire)
THETA_CALLS = []


def _theta_stub(self, theta, *a, **k):
    THETA_CALLS.append(theta)
    self.H0 = 67.0                      # a placeholder: nothing is solved


camb_model.CAMBparams.set_H0_for_theta = _theta_stub

import ratio_table_run as R
import ratio_table_figures as FIG

print("== Tripwires and the theta stub")
tripped = []
for fn in (lambda: camb.get_results(None), lambda: camb.get_transfer_functions(None), lambda: camb.get_background(None),
           lambda: camb_results.CAMBdata().calc_background_no_thermo(None), lambda: camb_results.CAMBdata().calc_transfers(None),
           lambda: camb_results.CAMBdata().power_spectra_from_transfer()):
    try:
        fn()
        tripped.append(False)
    except RuntimeError as e:
        tripped.append("tripwire" in str(e))
check(f"CAMB tripwires fire on all {len(tripped)} compute entry points tried", all(tripped) and len(tripped) == 6)
p0 = camb.CAMBparams()
p0.set_H0_for_theta(0.0104109)
check("theta is never solved: CAMB's theta-to-H0 solver is a stub that records theta and sets a placeholder H0",
      THETA_CALLS == [0.0104109] and p0.H0 == 67.0)
THETA_CALLS.clear()

print("\n== The packet's copies of v1's records")
same = [hashlib.sha256(open(os.path.join(HERE, f), "rb").read()).digest() == hashlib.sha256(open(os.path.join(V1, f), "rb").read()).digest()
        for f in ("environment.json", "provenance.json", "sw_estimate.out", "isw_estimate.out")]
check("environment.json, provenance.json, sw_estimate.out and isw_estimate.out are byte-identical to v1's committed packet", all(same))

print("\n== v1's shell machinery, unchanged")
spec = importlib.util.spec_from_file_location("v1_step_two_run", os.path.join(V1, "step_two_run.py"))
V1R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V1R)
chi = 14000.0
period = 2 * np.pi / chi
q = np.concatenate([np.geomspace(1e-7, 1e-4, 400, endpoint=False), np.arange(1e-4, 0.45, period / 10)])
L = np.arange(0, 61)
D = np.array([spherical_jn(l, q * chi) for l in L])
tr, tr_v1 = R.GridTransfer(L, q, D), V1R.GridTransfer(L, q, D)
one = lambda k: np.ones_like(k)
cont = np.array([2 * np.pi / (l * (l + 1)) for l in range(R.LMIN, R.LMAX + 1)])
kk = np.linspace(7e-4, 0.4, 3001)
lv = np.arange(R.LMIN, R.LMAX + 1)
g2_new, g2_old = R.gate_g2(tr, one, chi, cont), V1R.gate_g2(tr_v1, one, chi, cont)
check("Molien counts, the three weight tables, the spline transfer, the shell sum and G2 give v1's results exactly on test inputs",
      np.array_equal(R.molien_counts(4000), V1R.molien_counts(4000))
      and all(np.array_equal(R.shell_table(5000, s)[1], V1R.shell_table(5000, s)[1]) for s in ("molien", "s3", "molien_no120"))
      and np.array_equal(tr(lv, kk), tr_v1(lv, kk))
      and np.array_equal(R.shell_sum(R.R_A_MPC, tr, one, "molien")[0], V1R.shell_sum(V1R.R_A_MPC, tr_v1, one, "molien")[0])
      and json.dumps(g2_new, sort_keys=True) == json.dumps(g2_old, sort_keys=True)
      and (R.G2_TOL, R.G2_R_OVER_CHI, R.CUT_START, R.CUT_CAP, R.CUT_TOL, R.R_A_MPC, R.R_B_MPC, R.LMIN, R.LMAX)
      == (V1R.G2_TOL, V1R.G2_R_OVER_CHI, V1R.CUT_START, V1R.CUT_CAP, V1R.CUT_TOL, V1R.R_A_MPC, V1R.R_B_MPC, V1R.LMIN, V1R.LMAX))
m = R.molien_counts(4000)
base = [0] * 4001
for a in range(4000 // 12 + 1):
    for b in range((4000 - 12 * a) // 20 + 1):
        base[12 * a + 20 * b] += 1
direct = [base[n] + (base[n - 30] if n >= 30 else 0) for n in range(4001)]
check("Molien counts equal the direct count to N = 4000, with step one's rows (1 at 0, 12, 20, 24, 30; 2 at 60; zero at odd N)",
      list(m) == direct and [int(m[n]) for n in (0, 12, 20, 24, 30, 60)] == [1, 1, 1, 1, 1, 2] and not m[1::2].any())
N, W = R.shell_table(60, "molien")
got = {n: round(float(W[n - 1]), 4) for n in (12, 20, 24, 30)}
check(f"W_12, W_20, W_24, W_30 = {got} equal 480 pi m_N (N+1)/[N(N+2)]^(3/2) and v1's recorded values",
      got == {12: 9.0027, 20: 3.4311, 24: 2.4185, 30: 1.5716} and abs(W[11] - 480 * math.pi * 13 / 168 ** 1.5) < 1e-12)

print("\n== Shell sum on a synthetic Sachs-Wolfe transfer (the estimate declared before v1's freeze)")
sw_rows = {int(r[0]): [float(x) for x in r[1:]] for r in
           re.findall(r"^ +(\d+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+)$", open(os.path.join(HERE, "sw_estimate.out"), encoding="utf-8").read(), re.M)}
for name, Rm, col in (("A", R.R_A_MPC, 0), ("B", R.R_B_MPC, 1)):
    cl, rec = R.shell_sum(Rm, tr, one, "molien")
    worst = max(abs(cl[l - R.LMIN] / cont[l - R.LMIN] - sw_rows[l][col]) for l in range(R.LMIN, R.LMAX + 1))
    check(f"route {name}: the shell sum reproduces sw_estimate.out at all 28 multipoles (worst {worst:.4f} <= 0.0015); cutoff converged at N_max = {rec['N_max']}",
          worst <= 0.0015 and rec["converged"])
cl_A, _ = R.shell_sum(R.R_A_MPC, tr, one, "molien")
share = R.first_shell_share(R.R_A_MPC, tr, one, cl_A)
k12 = np.array([math.sqrt(168.0) / R.R_A_MPC])
indep = (480 * math.pi * 13 / 168 ** 1.5) * tr(lv, k12)[:, 0] ** 2 / cl_A
check(f"the first shell's share at A, recomputed from W_12, P(k_12) and Delta_l(k_12)^2, matches the runner's (largest {share.max():.3f}, within (0, 1])",
      np.allclose(share, indep, rtol=1e-12, atol=0) and bool(np.all((share > 0) & (share <= 1))))

print("\n== G2 on the synthetic transfer")
print(f"   R = {g2_new['R_mpc']:.3e} Mpc; max deviation: s3 {g2_new['s3']['max_fractional_deviation']:.2e}, molien {g2_new['molien']['max_fractional_deviation']:.2e}, "
      f"molien_no120 {g2_new['molien_no120']['max_fractional_deviation']:.2e}")
check("G2 passes on correct machinery at 1e-3 (both spectra within it, the 1/120 mutation outside it)", g2_new["passed"] and R.G2_TOL == 1e-3)
check("G2 fails when the continuum is off by 1%", R.gate_g2(tr, one, chi, cont * 1.01)["passed"] is False)
check("the cutoff rule reports non-convergence when the cap is reached first", R.shell_sum(R.R_A_MPC, tr, one, "molien", cap=2048, tol=1e-14)[1]["converged"] is False)

print("\n== The grid rule, bounded above, and the reach")
need, k_hi = period / 8, R.REACH_KCHI / chi
fine = np.concatenate([np.geomspace(1e-7, 1e-4, 400, endpoint=False), np.arange(1e-4, 0.45, period / 10), np.arange(0.46, 0.62, 0.02)])
coarse = np.concatenate([np.geomspace(1e-7, 1e-4, 400, endpoint=False), np.arange(1e-4, 0.45, period / 6), np.arange(0.46, 0.62, 0.02)])
v1_rule = R.GridTransfer(L, fine, np.zeros((len(L), len(fine)))).max_spacing_above(R.K12_B)
check("a grid fine from k12(R_B) to k chi* = 1000, with a coarse block above, meets the bounded rule, where v1's unbounded rule fails",
      R.max_spacing_between(fine, R.K12_B, k_hi) <= need < v1_rule)
check("a grid coarse inside the range misses the rule", R.max_spacing_between(coarse, R.K12_B, k_hi) > need)
edge = np.array([0.5 * R.K12_B, 0.5 * k_hi, 0.9 * k_hi, 1.5 * k_hi, 3.0 * k_hi])
check("a step straddling the range's upper edge counts, and a step wholly above it does not",
      abs(R.max_spacing_between(edge, R.K12_B, k_hi) - 0.6 * k_hi) < 1e-15)

print("\n== The separation measure and the two labels")
r = np.ones(28)
r[0], r[1] = 0.5, 2.0
s = R.separations(r)
hand_p1, hand_l = 2.5 * (math.log(2) - 0.5) + 3.5 * (1 - math.log(2)), 2.5 * (1 - math.log(2)) + 3.5 * (math.log(2) - 0.5)
check(f"K_P1 and K_Lambda reproduce a hand computation (R_2 = 0.5, R_3 = 2, the rest 1): {s['K_P1']:.6f} and {s['K_Lambda']:.6f}",
      abs(s["K_P1"] - hand_p1) < 1e-12 and abs(s["K_Lambda"] - hand_l) < 1e-12 and abs(hand_p1 - 1.556853) < 5e-7 and s["K_min"] == s["K_Lambda"])
rng = np.random.default_rng(7)
rr = np.exp(rng.normal(0, 1, 28))
sr = R.separations(rr)
ell = np.arange(2, 30)
check("K_P1 + K_Lambda = sum (2l+1)/2 (R + 1/R - 2) on a random table (the logarithms cancel), and the terms sum to the totals",
      abs(sr["K_P1"] + sr["K_Lambda"] - float(np.sum((2 * ell + 1) / 2 * (rr + 1 / rr - 2)))) < 1e-9
      and abs(sum(sr["terms_P1"]) - sr["K_P1"]) < 1e-9 and abs(sum(sr["terms_Lambda"]) - sr["K_Lambda"]) < 1e-9)
uni = [R.separations(np.full(28, 1 + e))[k] for e in (0.1, -0.1) for k in ("K_P1", "K_Lambda")]
check(f"uniform departures of 10% give the contract's 1.97 to 2.58: {[round(u, 4) for u in uni]}",
      [round(u, 4) for u in uni] == [2.1010, 1.9717, 2.4015, 2.5763])
check("the shape label: Near unity, Departing and Unresolved branches, with 0.1 itself Near unity",
      [R.shape_label(*v) for v in ((0.05, 0.06), (0.5, 0.6), (0.09, 0.11), (0.1, 0.1))] == ["Near unity", "Departing", "Unresolved", "Near unity"])
check("the separation label on K_min: Separated, Not separated and Unresolved branches, with 2 itself Separated",
      [R.separation_label(*v) for v in ((10, 12), (1, 1.5), (1.9, 2.1), (2.0, 2.0))] == ["Separated", "Not separated", "Unresolved", "Separated"])
corner = R.separation_label(min(1.5, 3.0), min(3.0, 1.5))
check(f"F1's corner case (frozen K_P1 1.5, K_Lambda 3; repeat K_P1 3, K_Lambda 1.5) is {corner}", corner == "Not separated")
stops = 0
for bad_r in (np.where(ell == 5, 0.0, 1.0), np.where(ell == 5, -0.1, 1.0), np.where(ell == 5, np.nan, 1.0), np.ones(27)):
    try:
        R.separations(bad_r)
    except R.RunStop:
        stops += 1
check("a zero, negative or non-finite ratio, or a table without 28 entries, stops the run", stops == 4)

print("\n== End to end on a synthetic transfer provider (no CAMB)")
STEPS = lambda b: 6 if b == 2 else 2 * b + 4          # boost 2: period/6 (misses the rule); 3: period/10; 4: period/12
TAU0 = 14300.0         # a synthetic conformal time today: CAMB's block boundary, k eta0 = 3000, sits at q = 3000/TAU0


def camb_grid(boost, steps, boundary=R.SPLIT_KETA0):
    """A q grid built as CAMB 2.0.4 builds its own (erratum E1): a logarithmic block, a fine linear block ending on the block
    boundary (k eta0 = 3000 unless moved for a test), and the coarse block CAMB appends above it, steps of about 0.04/boost
    Mpc^-1 up to k eta0 = max_eta_k = 12000. The coarse block restores the one the provider carried before the freeze."""
    qb, qe = boundary / TAU0, R.TRANSFER["max_eta_k"] / TAU0
    fine = np.linspace(1e-4, qb, int(math.ceil((qb - 1e-4) / (period / steps))) + 1)
    coarse = np.linspace(qb, qe, int(round((qe - qb) / (0.04 / boost))) + 1)[1:]
    return np.concatenate([np.geomspace(1e-7, 1e-4, 400, endpoint=False), fine, coarse])


def provider(steps=STEPS, reach_kchi=None, max_l=260, want_lensing=False, drop_l=None, cont_scale=1.0,
             plateau_at=(), raise_at=None, max_l_at=None, boundary_at=None):
    calls = []

    def compute(p, boost):
        calls.append(boost)
        if raise_at and boost in raise_at:
            raise raise_at[boost]
        qq = camb_grid(boost, steps(boost), (boundary_at or {}).get(boost, R.SPLIT_KETA0))
        LL = np.array([l for l in range(0, 61) if l != drop_l])
        DD = np.array([spherical_jn(l, qq * chi) for l in LL])
        if boost in plateau_at:           # a block that never decays, from q = 0.25 through the coarse block and on to q = 400:
            DD[:, qq >= 0.25] = 1e-3      # the shell sums at A and B keep growing to the cap
            qp = np.geomspace(0.9, 400.0, 300)
            qq, DD = np.concatenate([qq, qp]), np.concatenate([DD, np.full((len(LL), len(qp)), 1e-3)], axis=1)
        if reach_kchi is not None:
            keep = qq <= reach_kchi / chi
            qq, DD = qq[keep], DD[:, keep]
        cl = np.zeros(R.LMAX + 1)
        cl[R.LMIN:] = cont * cont_scale
        return {"boost": boost, "q": qq, "L": LL, "delta": DD, "chi_star": chi, "tau0": TAU0, "cl_lcdm_uK2": cl, "tcmb2": 1.0,
                "power": one, "max_l": (max_l_at or {}).get(boost, max_l), "do_lensing": False, "want_cmb_lensing": want_lensing,
                "derived": {"zstar": 1090.0}}
    return compute, calls


est = R.estimate_ratios(HERE)
compute, calls = provider()
res = R.compute_all({}, compute, est)
res["status"] = "Complete"
check(f"the grid rule misses at boost 2 and is met at 3, and the repeat runs at 4: calls {calls}",
      calls == [2, 3, 4] and res["chosen_boost"] == 3 and [g["meets_rule"] for g in res["grid"]] == [False, True]
      and res["repeat"]["grid"]["AccuracyBoost"] == 4 and all(g["reach_kchi"] >= 1000 for g in res["grid"]))
worst = max(abs(res[n]["frozen"]["ratio"][l - 2] - sw_rows[l][c]) for n, c in (("A", 0), ("B", 1)) for l in range(2, 30))
check(f"G2 passes in the pipeline, and both routes' ratios reproduce sw_estimate.out (worst {worst:.4f} <= 0.0015)", res["G2"]["passed"] and worst <= 0.0015)
check(f"labels on the Sachs-Wolfe transfer: A {res['A']['labels']}, B {res['B']['labels']}",
      all(res[n]["labels"] == {"shape": "Departing", "separation": "Separated"} for n in ("A", "B")))
check(f"the repeat's table is reported beside the frozen one and moves no ratio by more than 1e-3 (A {res['A']['repeat_max_relative_change']:.1e}, "
      f"B {res['B']['repeat_max_relative_change']:.1e})",
      all(res[n]["repeat"]["valid"] and 0 < res[n]["repeat_max_relative_change"] < 1e-3 for n in ("A", "B")))
check("the estimates are carried as recorded, and R_l is divided by them at every l (Sachs-Wolfe) and to l = 10 (with the integrated term)",
      all(res[n]["estimates"]["sachs_wolfe"] == est[n]["sw"] and res[n]["estimates"]["with_isw_to_l10"] == est[n]["isw"]
          and len(res[n]["versus_estimates"]["sachs_wolfe"]) == 28 and len(res[n]["versus_estimates"]["with_isw_to_l10"]) == 9
          and all(abs(res[n]["versus_estimates"]["sachs_wolfe"][i] * est[n]["sw"][i] - res[n]["frozen"]["ratio"][i]) < 1e-12 for i in range(28))
          for n in ("A", "B")))
rep = R.format_report(res)
rows = [ln for ln in rep.split("\n") if re.match(r"^  +\d+  ", ln)]
check(f"the report prints 28 rows per route, both labels per route, G2, every grid and every cutoff ({len(rows)} rows)",
      len(rows) == 56 and rep.count("Shape: Departing.  Separation: Separated.") == 2 and "G2 at R" in rep and rep.count("Grid at AccuracyBoost") == 3
      and rep.count("Cutoff, route") == 4 and json.loads(json.dumps(res, default=float))["chosen_boost"] == 3)

print("\n== Erratum E1: CAMB's native block boundary and the split interpolation")
bnd = [R.native_boundary(provider()[0]({}, b)) for b in (2, 3, 4)]
ratios = ", ".join(f"x{b[1]['step_ratio']:.0f}" for b in bnd)
check(f"on grids built as CAMB builds its own, at boosts 2, 3 and 4, the boundary is found from tau0 at k eta0 = 3000, where the "
      f"largest step ratio sits ({ratios})",
      all(b[2] is None and b[0] is not None and abs(b[1]["k_eta0"] - 3000.0) < 1e-6 and b[1]["step_ratio"] > 100 for b in bnd))
t3 = provider()[0]({}, 3)
tr3 = R.check_transfer(t3)
Dq = np.array([t3["delta"][list(t3["L"]).index(l)] for l in lv])
scale, j3, qb3 = float(np.max(np.abs(Dq))), tr3.split, t3["q"][tr3.split]
resid = float(np.max(np.abs(tr3(lv, t3["q"]) - Dq)))
edge = max(abs(float(tr3.lower[int(l)](qb3)) - Dq[i, j3]) for i, l in enumerate(lv))
check(f"the split interpolation passes through every native knot (largest residual {resid:.1e} of a largest |Delta_l| of {scale:.2f}), "
      f"and at the boundary both splines give the knot's value (the lower within {edge:.1e}), so it is continuous and single-valued there",
      resid <= 1e-14 * scale and edge <= 1e-14 * scale and all(float(tr3.upper[int(l)](qb3)) == Dq[i, j3] for i, l in enumerate(lv)))
pairs = []
for b in (3, 4):
    tb = provider()[0]({}, b)
    pairs.append((b, R.gate_g2(R.GridTransfer(tb["L"], tb["q"], tb["delta"]), one, chi, cont), R.gate_g2(R.check_transfer(tb), one, chi, cont)))
desc = "; ".join(f"boost {b}: single {g1['s3']['max_fractional_deviation']:.1e} and converged {g1['s3']['cutoff']['converged']}, "
                 f"split {g2['s3']['max_fractional_deviation']:.1e} and converged {g2['s3']['cutoff']['converged']}" for b, g1, g2 in pairs)
check(f"with the coarse block restored, G2 fails with the frozen single spline and passes with the split, at the chosen boost and "
      f"at the repeat's ({desc})", all(g1["passed"] is False and g2["passed"] is True for _, g1, g2 in pairs))
saved_nb = R.native_boundary
R.native_boundary = lambda t: (None, {"k_eta0": None, "step_ratio": None}, None)     # E1 reverted: one spline across the jump
try:
    try:
        R.compute_all({}, provider()[0], est)
        check("with E1 reverted, the pipeline stops at G2 as Run 1 did, keeping its partial record, with no route table", False)
    except R.RunStop as e:
        pt = e.partial or {}
        check("with E1 reverted, the pipeline stops at G2 as Run 1 did, keeping its partial record, with no route table",
              str(e) == "G2 failed" and pt["G2"]["passed"] is False and "A" not in pt and "B" not in pt)
finally:
    R.native_boundary = saved_nb
x3 = t3["q"] * TAU0
hole = (x3 < 1500.0) | (x3 > 2990.0)
t_hole = {**t3, "q": t3["q"][hole], "delta": t3["delta"][:, hole]}
t_moved = provider(boundary_at={3: 3100.0})[0]({}, 3)
t_short = {**t3, "q": t3["q"][x3 <= 2500.0], "delta": t3["delta"][:, x3 <= 2500.0]}
f_hole, f_moved, n_short = R.native_boundary(t_hole)[2], R.native_boundary(t_moved)[2], R.native_boundary(t_short)
check("a grid whose largest step ratio sits away from k eta0 = 3000, or that runs past it without a knot there, is not as registered; "
      "a grid ending below the boundary has no coarse block and takes one spline",
      f_hole is not None and "largest step ratio" in f_hole and f_moved is not None and "without a single interior knot" in f_moved
      and n_short[0] is None and n_short[2] is None and R.check_transfer(t_short).split is None)

print("\n== Every stop keeps its partial record")
SCENARIOS = (
    ("the grid rule never met by boost 6", dict(steps=lambda b: 6), "not met by AccuracyBoost 6",
     lambda pt, cl: len(pt["grid"]) == 5 and not any(g["meets_rule"] for g in pt["grid"]) and cl == [2, 3, 4, 5, 6]),
    ("the grid ending below k chi* = 1000", dict(steps=lambda b: 10, reach_kchi=900.0), "reach gate",
     lambda pt, cl: len(pt["grid"]) == 1 and pt["grid"][0]["reach_kchi"] < 1000 and pt["grid"][0]["meets_rule"]),
    ("max_l not reaching CAMB", dict(steps=lambda b: 10, max_l=60), "did not reach CAMB", lambda pt, cl: len(pt["grid"]) == 1),
    ("the lensing potential left on", dict(steps=lambda b: 10, want_lensing=True), "did not reach CAMB", lambda pt, cl: len(pt["grid"]) == 1),
    ("multipole 17 missing", dict(steps=lambda b: 10, drop_l=17), "lacks l = [17]", lambda pt, cl: len(pt["grid"]) == 1),
    ("CAMB's block boundary not where its construction puts it (erratum E1)", dict(boundary_at={2: 3100.0}), "without a single interior knot",
     lambda pt, cl: len(pt["grid"]) == 1 and cl == [2]),
    ("G2 failing (the continuum 1% off)", dict(steps=lambda b: 10, cont_scale=1.01), "G2 failed",
     lambda pt, cl: pt["G2"]["passed"] is False and pt["G2"]["molien"]["max_fractional_deviation"] > 1e-3
     and len(pt["LCDM_D_l_uK2"]["frozen"]) == 28 and "A" not in pt and "B" not in pt),
)
partial_g2 = None
for label, kw, needle, kept in SCENARIOS:
    comp, cl_calls = provider(**kw)
    try:
        R.compute_all({}, comp, est)
        check(f"a failing gate stops the run and keeps its partial record: {label}", False)
    except R.RunStop as e:
        pt = e.partial or {}
        check(f"a failing gate stops the run and keeps its partial record: {label}",
              needle in str(e) and kept(pt, cl_calls) and not any("labels" in pt.get(n, {}) for n in ("A", "B")))
        if "G2" in label:
            partial_g2 = pt
orig_sum = R.shell_sum


def b_never_converges(R_mpc, transfer, pk, spectrum, **kw):
    acc, rec = orig_sum(R_mpc, transfer, pk, spectrum, **kw)
    return (acc, {**rec, "converged": False}) if (R_mpc == R.R_B_MPC and spectrum == "molien") else (acc, rec)


R.shell_sum = b_never_converges
try:
    comp, _ = provider()
    try:
        R.compute_all({}, comp, est)
        check("route B's frozen cutoff failing (forced in a wrapper) keeps route A's whole table, G2 and B's unconverged table, with no labels", False)
    except R.RunStop as e:
        pt = e.partial
        check("route B's frozen cutoff failing (forced in a wrapper) keeps route A's whole table, G2 and B's unconverged table, with no labels",
              "route B" in str(e) and pt["A"]["frozen"]["ratio"] == res["A"]["frozen"]["ratio"] and pt["A"]["frozen"]["cutoff"]["converged"]
              and pt["B"]["frozen"]["cutoff"]["converged"] is False and pt["G2"]["passed"] and "repeat" not in pt
              and not any("labels" in pt[n] for n in ("A", "B")))
finally:
    R.shell_sum = orig_sum
prep = R.format_report({"status": "Uninformative", "reason": "G2 failed", "partial": partial_g2})
check("the report of a stopped run prints its partial record: the grid, G2 and the continuum's reason, and no label",
      "Partial record" in prep and "G2 at R" in prep and "passed False" in prep and "Grid at AccuracyBoost" in prep and "Shape:" not in prep)

print("\n== The repeat's declared failures (a control, not a gate)")


def frozen_as_clean(x):
    return all(x[n]["frozen"]["ratio"] == res[n]["frozen"]["ratio"] and x[n]["frozen"]["K_min"] == res[n]["frozen"]["K_min"] for n in ("A", "B"))


def both_unresolved(x):
    return all(x[n]["labels"]["shape"] == x[n]["labels"]["separation"] == "Unresolved" and x[n]["repeat"]["valid"] is False
               and "repeat_max_relative_change" not in x[n] for n in ("A", "B"))


comp, cl_calls = provider(plateau_at=(4,))
res_cut = R.compute_all({}, comp, est)
check("the repeat's cutoff not converging (a block that never decays, at boost 4 only): the frozen table stands, identical to the clean run's, "
      "and both routes are Unresolved with the failure and its reason recorded",
      cl_calls == [2, 3, 4] and frozen_as_clean(res_cut) and both_unresolved(res_cut)
      and all("did not converge" in res_cut[n]["repeat"]["failure"] and res_cut[n]["repeat"]["cutoff"]["converged"] is False for n in ("A", "B")))
check("the unconverged repeat enters no label: the frozen table alone reads Departing and Separated, the labels stay Unresolved, "
      "and the failed repeat carries no d_inf or K_min, only its unconverged ratios, marked as such",
      all(R.shape_label(res_cut[n]["frozen"]["d_inf"], res_cut[n]["frozen"]["d_inf"]) == "Departing"
          and R.separation_label(res_cut[n]["frozen"]["K_min"], res_cut[n]["frozen"]["K_min"]) == "Separated"
          and not any(k in res_cut[n]["repeat"] for k in ("d_inf", "K_min", "K_P1", "K_Lambda", "ratio"))
          and len(res_cut[n]["repeat"]["unconverged_ratio"]) == 28 for n in ("A", "B")))
comp, _ = provider(raise_at={4: CAMBError("synthetic CAMB failure")})
res_camb = R.compute_all({}, comp, est)
check("an error of CAMB's own in the repeat: the frozen table stands, both routes are Unresolved, and the error is recorded",
      frozen_as_clean(res_camb) and both_unresolved(res_camb) and "CAMB computation failed: CAMBError" in res_camb["repeat"]["failure"])
comp, _ = provider(max_l_at={4: 60})
res_set = R.compute_all({}, comp, est)
check("the repeat's transfer not as registered (max_l 60 at boost 4): the frozen table stands and both routes are Unresolved",
      frozen_as_clean(res_set) and both_unresolved(res_set) and "not as registered" in res_set["repeat"]["failure"])
comp, _ = provider(boundary_at={4: 3100.0})
res_bnd = R.compute_all({}, comp, est)
check("the repeat's grid with CAMB's block boundary out of place (erratum E1) is its second declared failure: the frozen table stands "
      "and both routes are Unresolved", frozen_as_clean(res_bnd) and both_unresolved(res_bnd)
      and "not as registered" in res_bnd["repeat"]["failure"] and "without a single interior knot" in res_bnd["repeat"]["failure"])
comp, _ = provider(raise_at={4: ValueError("synthetic defect")})
try:
    R.compute_all({}, comp, est)
    check("any other failure in the repeat is an infrastructure defect: it propagates, and still keeps both frozen tables as its partial record", False)
except ValueError as e:
    pt = e.partial
    check("any other failure in the repeat is an infrastructure defect: it propagates, and still keeps both frozen tables as its partial record",
          pt["A"]["frozen"]["ratio"] == res["A"]["frozen"]["ratio"] and pt["B"]["frozen"]["ratio"] == res["B"]["frozen"]["ratio"]
          and not any("labels" in pt[n] for n in ("A", "B")))
crep = R.format_report({**res_cut, "status": "Complete"})
check("the report of a failed repeat shows both routes Unresolved, the reason, and no repeat column",
      crep.count("Shape: Unresolved.  Separation: Unresolved.") == 2 and crep.count("the repeat failed at this route") == 2
      and all(ln.split()[4] == "-" for ln in crep.split("\n") if re.match(r"^  +\d+  ", ln)))

print("\n== The runner's main, in process, on the synthetic provider (runtime check stubbed; no CAMB)")
saved_rc, saved_ct = R.runtime_check, R.compute_transfer
R.runtime_check = lambda packet, data, require_manifest=True: []
outdir = tempfile.mkdtemp()
try:
    R.compute_transfer = provider()[0]
    with contextlib.redirect_stdout(io.StringIO()):
        code_ok = R.main(["--run", "--packet", HERE, "--data", DATA, "--out", os.path.join(outdir, "ok.json")])
    ok = json.load(open(os.path.join(outdir, "ok.json"), encoding="utf-8"))
    R.compute_transfer = provider(steps=lambda b: 10, cont_scale=1.01)[0]
    with contextlib.redirect_stdout(io.StringIO()):
        code_g2 = R.main(["--run", "--packet", HERE, "--data", DATA, "--out", os.path.join(outdir, "g2.json")])
    g2j = json.load(open(os.path.join(outdir, "g2.json"), encoding="utf-8"))
    g2r = open(os.path.join(outdir, "g2_report.txt"), encoding="utf-8").read()
finally:
    R.runtime_check, R.compute_transfer = saved_rc, saved_ct
check("main records a complete run: exit 0, status Complete, both labels, and a report beside the result",
      code_ok == 0 and ok["status"] == "Complete" and all(ok[n]["labels"]["shape"] == "Departing" for n in ("A", "B"))
      and os.path.isfile(os.path.join(outdir, "ok_report.txt")))
check("main keeps a stopped run's partial record in the result file and its report: exit 1, Uninformative, G2's deviations kept",
      code_g2 == 1 and g2j["status"] == "Uninformative" and g2j["reason"] == "G2 failed" and g2j["partial"]["G2"]["passed"] is False
      and "Partial record" in g2r and "G2 at R" in g2r)
shutil.rmtree(outdir)

print("\n== The figures, from the synthetic end-to-end result")
svg1, svg2 = FIG.spectra_svg(res), FIG.ratios_svg(res)
r1, r2 = ET.fromstring(svg1), ET.fromstring(svg2)


def marks(root, cls):
    return [e for e in root.iter() if e.get("class") == cls and e.get("data-v") is not None]


vals = lambda root, cls: [float(e.get("data-v")) for e in marks(root, cls)]
check("the spectra figure is well-formed SVG with LambdaCDM, A and B at 28 points each, every point a value of the result file",
      vals(r1, "m-lcdm") == res["LCDM_D_l_uK2"]["frozen"] and vals(r1, "m-A") == res["A"]["frozen"]["D_l_P1_uK2"]
      and vals(r1, "m-B") == res["B"]["frozen"]["D_l_P1_uK2"] and len(vals(r1, "m-A")) == 28)
check("the ratios figure has each route's panel: 28 full-transfer points, 28 Sachs-Wolfe and 9 integrated-term estimate markers, "
      "the 10% band and the unity line, every point a value of the result file",
      all(vals(r2, f"m-{n}") == res[n]["frozen"]["ratio"] and vals(r2, f"o-{n}") == res[n]["estimates"]["sachs_wolfe"] + res[n]["estimates"]["with_isw_to_l10"]
          for n in ("A", "B")) and len([e for e in r2.iter() if e.get("class") == "band" and e.tag.endswith("rect") and e.get("height")]) == 3)
texts = [e for root in (r1, r2) for e in root.iter() if e.tag.endswith("text")]
check(f"no text in either figure wears a series colour: all {len(texts)} text elements use ink classes",
      len(texts) > 40 and all(e.get("class") in ("t1", "t2", "tm") for e in texts))
if FIGDIR:
    os.makedirs(FIGDIR, exist_ok=True)
    open(os.path.join(FIGDIR, "synthetic_spectra.svg"), "w", encoding="utf-8").write(svg1)
    open(os.path.join(FIGDIR, "synthetic_ratios.svg"), "w", encoding="utf-8").write(svg2)

print("\n== CAMB parameter object (theta by the declared stub; nothing computed)")
pc, _ = R.read_minimum(os.path.join(DATA, R.COMPARISON_FIT + ".minimum"))
pars = R.camb_params(pc, 3)
check("the transfer settings reach CAMB's parameter object: max_l 260, both lensing flags off, lSampleBoost 50, lAccuracyBoost 2, "
      "AccuracyBoost 3, max_eta_k 12000, no nonlinear correction, no tensors",
      pars.max_l == 260 and not pars.DoLensing and not pars.Want_CMB_lensing and pars.Accuracy.lSampleBoost == 50.0
      and pars.Accuracy.lAccuracyBoost == 2.0 and pars.Accuracy.AccuracyBoost == 3.0 and pars.max_eta_k == 12000.0
      and str(pars.NonLinear) == str(camb_model.NonLinear_none) and not pars.WantTensors)
check("erratum E1's physics settings reach it: one massive eigenstate carrying 3.046/3 of N_eff, the fit's omega_nu h^2 and Y_P, "
      "tanh width 0.5, helium reionization width 0.5 from z = 5, PPF dark energy, Recfast 'planck' (fudge_He 0.86)",
      pars.nu_mass_eigenstates == 1 and abs(pars.nu_mass_degeneracies[0] - 3.046 / 3) < 1e-12
      and abs(pars.num_nu_massless - (3.046 - 3.046 / 3)) < 1e-12 and abs(pars.omnuh2 / pc["omeganuh2"] - 1) < 1e-12
      and "yheused" in pc and abs(pars.YHe / pc["yheused"] - 1) < 1e-5 and pars.Reion.delta_redshift == 0.5
      and pars.Reion.helium_delta_redshift == 0.5 and pars.Reion.helium_redshiftstart == 5.0
      and type(pars.DarkEnergy).__name__ == "DarkEnergyPPF" and abs(pars.Recomb.RECFAST_fudge_He - 0.86) < 1e-12)
check("theta reached the stub once, as the fit's theta/100, and nothing was solved", THETA_CALLS == [pc["theta"] / 100.0])
try:
    R.camb_params({**pc, "mnu": 0.07}, 3)
    check("the fit's mnu is the frozen 0.06, and any other value stops the run", False)
except R.RunStop:
    check("the fit's mnu is the frozen 0.06, and any other value stops the run", pc["mnu"] == 0.06)

print("\n== Runtime check and the refusal to run early")
tmp = tempfile.mkdtemp()      # the packet copied without its manifest, so these checks read the same before and after the freeze
for f in R.PACKET_FILES:
    src = os.path.join(HERE, f)
    shutil.copy(src, tmp) if os.path.exists(src) else open(os.path.join(tmp, f), "w").close()
bad = R.runtime_check(tmp, DATA, require_manifest=False)
check(f"the runtime check passes on this environment, on the packet without its manifest ({len(bad)} mismatches)", bad == [])
check("with the manifest required (as --run requires it), a missing manifest fails closed", "freeze manifest missing" in R.runtime_check(tmp, DATA))
R.write_manifest(tmp)
check("with a matching freeze manifest the runtime check passes", R.runtime_check(tmp, DATA) == [])
man = json.load(open(os.path.join(tmp, R.MANIFEST), encoding="utf-8"))
man["files"]["ratio_table_run.py"] = "0" * 64
json.dump(man, open(os.path.join(tmp, R.MANIFEST), "w", encoding="utf-8"))
bad_run = R.runtime_check(tmp, DATA)
check("a manifest that pins a different script fails closed: the runner is not the frozen one",
      "the running script is not the frozen one" in bad_run and any("freeze manifest: ratio_table_run.py" in b for b in bad_run))
R.write_manifest(tmp)
open(os.path.join(tmp, "provenance.json"), "a").write(" ")
check("a packet file changed after the manifest fails the runtime check",
      any("differs from the freeze manifest: provenance.json" in b for b in R.runtime_check(tmp, DATA)))
shutil.rmtree(tmp)
saved = R.RUNTIME["numpy"]
R.RUNTIME["numpy"] = "0.0"
bad2 = R.runtime_check(HERE, DATA)
R.RUNTIME["numpy"] = saved
check("the runtime check fails closed on a changed version", any(b.startswith("numpy") for b in bad2))
dtmp = tempfile.mkdtemp()
shutil.copy(os.path.join(DATA, R.COMPARISON_FIT + ".minimum"), dtmp)
open(os.path.join(dtmp, R.COMPARISON_FIT + ".minimum"), "a").write("\n")
check("a changed parameter file fails the runtime check", any("parameter file differs" in b for b in R.runtime_check(HERE, dtmp, require_manifest=False)))
shutil.rmtree(dtmp)
out = os.path.join(tempfile.gettempdir(), "ratio_table_should_not_exist.json")
r0 = subprocess.run([sys.executable, os.path.join(HERE, "ratio_table_run.py"), "--out", out], capture_output=True, text=True)
check("without --run the runner exits 2 and computes nothing", r0.returncode == 2 and "Nothing was computed" in r0.stdout and not os.path.exists(out))
inside = os.path.join(HERE, "should_not_exist.json")
r1_ = subprocess.run([sys.executable, os.path.join(HERE, "ratio_table_run.py"), "--run", "--out", inside], capture_output=True, text=True)
check("--out inside the packet is refused before anything runs", r1_.returncode == 2 and "inside the packet" in r1_.stdout and not os.path.exists(inside))

print(f"\n{len(PASSES)} checks passed, {len(FAILS)} failed")
print("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
