"""Pre-freeze tests for step_two_run.py, on synthetic inputs only.

Tripwires make the contract's boundary mechanical: any call that would run CAMB, and any Commander evaluation on a
vector other than the file's own test vector, raises and fails the suite. The shell machinery is checked against the
Sachs-Wolfe estimate declared before the freeze (sw_estimate.out), not against anything new.
"""
import json, math, os, re, shutil, subprocess, sys, tempfile
os.environ["CLIPY_NOJAX"] = "1"
import numpy as np
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import step_two_run as R

FAILS, PASSES = [], []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    (PASSES if ok else FAILS).append(label)


import camb


def _tripwire(*a, **k):
    raise RuntimeError("tripwire: a CAMB computation was called before the freeze")


for _name in ("get_results", "get_transfer_functions", "get_background"):
    setattr(camb, _name, _tripwire)
_orig_eval = R.Commander.evaluate


def _guarded(self, cl, A):
    vec = np.concatenate([np.asarray(cl, dtype=np.float64)[: self.lmax + 1], [float(A)]])
    if not np.array_equal(vec, self.default_par):
        raise RuntimeError("tripwire: the likelihood was called on a vector other than the file's test vector")
    return _orig_eval(self, cl, A)


R.Commander.evaluate = _guarded

print("== Tripwires")
try:
    camb.get_results(None)
    check("CAMB tripwire fires", False)
except RuntimeError as e:
    check("CAMB tripwire fires", "tripwire" in str(e))

print("\n== Shells and weights")
m = R.molien_counts(4000)
base = [0] * 4001
for a in range(4000 // 12 + 1):
    for b in range((4000 - 12 * a) // 20 + 1):
        base[12 * a + 20 * b] += 1
direct = [base[n] + (base[n - 30] if n >= 30 else 0) for n in range(4001)]
check("vectorized Molien counts equal the direct count to N = 4000", list(m) == direct)
check("step one's rows: m_N = 1 at 0, 12, 20, 24, 30; 2 at 60; zero at odd N", [int(m[n]) for n in (0, 12, 20, 24, 30, 60)] == [1, 1, 1, 1, 1, 2] and not m[1::2].any())
N, W = R.shell_table(60, "molien")
got = {n: round(float(W[n - 1]), 4) for n in (12, 20, 24, 30)}
check(f"W_12, W_20, W_24, W_30 = {got} match shell_weights_check.out", got == {12: 9.0027, 20: 3.4311, 24: 2.4185, 30: 1.5716})

print("\n== Shell sum on a synthetic Sachs-Wolfe transfer (reproducing the declared pre-freeze estimate)")
chi = 14000.0
period = 2 * np.pi / chi
q = np.concatenate([np.geomspace(1e-7, 1e-4, 400, endpoint=False), np.arange(1e-4, 0.45, period / 10)])
L = np.arange(0, 61)
D = np.array([spherical_jn(l, q * chi) for l in L])
tr = R.GridTransfer(L, q, D)
kk = np.linspace(7e-4, 0.4, 5000)
interp_err = max(float(np.max(np.abs(tr([l], kk)[0] - spherical_jn(l, kk * chi)))) for l in (2, 10, 29))
check(f"cubic interpolation of Delta_l on a 10-points-per-period grid: max error {interp_err:.1e} (< 1e-4)", interp_err < 1e-4)
check("grid spacing reported against the rule", tr.max_spacing_above(math.sqrt(168) / R.R_B_MPC) <= period / 8)
one = lambda k: np.ones_like(k)
cont = {l: 2 * np.pi / (l * (l + 1)) for l in range(R.LMIN, R.LMAX + 1)}
SW_OUT = next(p for p in (os.path.join(HERE, "sw_estimate.out"), os.path.join(os.path.dirname(HERE), "sw_estimate.out")) if os.path.exists(p))
sw = open(SW_OUT, encoding="utf-8").read()
rows = {int(r[0]): [float(x) for x in r[1:]] for r in re.findall(r"^ +(\d+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+) +([\d.]+)$", sw, re.M)}
for name, Rm, col in (("A", R.R_A_MPC, 0), ("B", R.R_B_MPC, 1)):
    cl, rec = R.shell_sum(Rm, tr, one, "molien")
    ratio = {l: float(cl[l - R.LMIN] / cont[l]) for l in range(R.LMIN, R.LMAX + 1)}
    worst = max(abs(ratio[l] - rows[l][col]) for l in range(R.LMIN, R.LMAX + 1))
    check(f"route {name}: the runner's shell sum reproduces sw_estimate.out at all 28 multipoles (worst {worst:.4f} <= 0.0015); "
          f"cutoff converged at N_max = {rec['N_max']}", worst <= 0.0015 and rec["converged"])

print("\n== G2 logic on the synthetic transfer")
pass_s3 = pass_mol = fail_no120 = None
g2 = R.gate_g2(tr, one, chi, np.array([cont[l] for l in range(R.LMIN, R.LMAX + 1)]))
print(f"   R = {g2['R_mpc']:.3e} Mpc; max deviation: s3 {g2['s3']['max_fractional_deviation']:.2e}, molien {g2['molien']['max_fractional_deviation']:.2e}, "
      f"molien_no120 {g2['molien_no120']['max_fractional_deviation']:.2e}")
check("G2 passes on correct machinery (both spectra within 1e-3, the mutation outside it)", g2["passed"])
cl_bad, rec_bad = R.shell_sum(R.R_A_MPC, tr, one, "molien", cap=2048, tol=1e-14)
check("the cutoff rule reports non-convergence when the cap is reached first", rec_bad["converged"] is False)

print("\n== Inputs (metadata and arithmetic only)")
P = os.environ.get("STEP_TWO_DATA", os.path.join(HERE, "planck"))   # the Planck inputs are not committed; point here
pb, tb = R.read_minimum(os.path.join(P, R.BASELINE_FIT + ".minimum"))
pc, tc = R.read_minimum(os.path.join(P, R.COMPARISON_FIT + ".minimum"))
check("baseline fit parsed: omegabh2, theta, calPlanck, chi2_lowl = 23.25721, table lowl 23.257",
      pb["omegabh2"] == 0.02237737 and pb["theta"] == 1.04092 and pb["calPlanck"] == 1.00061 and abs(pb["chi2_lowl"] - R.G1A_REF_CHI2) < 5e-6 and tb["lowl"]["chi2"] == 23.257)
check("comparison fit parsed: calPlanck 1.00076, logA, ns, no lowl term", pc["calPlanck"] == 1.00076 and "logA" in pc and "ns" in pc and "chi2_lowl" not in pc and "lowl" not in tc)
th = R.read_theory_cl_tt(os.path.join(P, R.BASELINE_FIT + ".minimum.theory_cl"))
check("theory_cl read as C_l = 2 pi D_l / (l(l+1)): C_2 from D_2 = 1017.48", abs(th[2] - 2 * np.pi * 1017.48 / 6) < 1e-9 and th[0] == th[1] == 0 and np.all(th[2:] > 0))
with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
    f.write("# l Dl\n2 600.0\n3 900.0\n4 800.0\n")
check("C_2/C_3 from a synthetic spectrum: 2 D_2 / D_3", abs(R.published_c2_over_c3(f.name) - 2 * 600.0 / 900.0) < 1e-12)
os.unlink(f.name)

print("\n== Likelihood wrapper, on the file's own test vector only")
C = R.Commander(os.path.join(P, R.CLIK_REL))
lnl, sup = C.evaluate(C.default_par[:30], C.default_par[30])
st = open(os.path.join(HERE, "self_test.out"), encoding="utf-8").read()
check(f"the runner's wrapper returns the self-test value: {lnl:.10f}", f"obtained {lnl:.10f}" in st)
check("the test vector sits in the interior at all 28 multipoles, largest |x| 1.932", sup["n_outside"] == 0 and all(r["class"] == "interior" for r in sup["rows"])
      and abs(max(abs(r["x"]) for r in sup["rows"]) - 1.932) < 5e-4)
try:
    C.evaluate(C.default_par[:30] * 1.01, C.default_par[30])
    check("likelihood tripwire fires on any other vector", False)
except RuntimeError as e:
    check("likelihood tripwire fires on any other vector", "tripwire" in str(e))

print("\n== Support classification (a pure function, no likelihood call)")
supj = json.load(open(os.path.join(HERE, "commander_support.json"), encoding="utf-8"))["support"]
lo = np.array([s["D_l_lower"] for s in supj]); hi = np.array([s["D_l_upper"] for s in supj])
dl = np.sqrt(lo * hi); x = np.zeros(28)
dl[1], dl[3] = 0.5 * lo[1], 0.8 * lo[3]
x[10] = 4.5
c = R.classify_support(dl, lo, hi, x)
check("two multipoles outside (l = 3 and 5), largest fractional distance 0.5, one edge flagged",
      c["n_outside"] == 2 and c["outside_l"] == [3, 5] and abs(c["max_fractional_distance_outside"] - 0.5) < 1e-12
      and c["rows"][10]["class"] == "edge" and c["rows"][10]["flag"] == "unqualified interpolation")
calls = []
def stub_splint(d):
    calls.append(np.array(d, dtype=np.float64))
    return np.zeros(len(d))
rec = R.support_record(dl, lo, hi, stub_splint)
check("support_record: the spline sees only values inside the table, and outside multipoles carry no x",
      len(calls) == 1 and bool(np.all((calls[0] >= lo) & (calls[0] <= hi))) and rec["outside_l"] == [3, 5]
      and all(r["x"] is None for r in rec["rows"] if r["class"] == "outside") and all(r["x"] is not None for r in rec["rows"] if r["class"] != "outside"))

print("\n== score(), both branches, with a stub likelihood (no likelihood call)")
class StubPars:
    TCMB = 1e-6
    @staticmethod
    def scalar_power(k):
        return np.ones_like(k)
class StubCommander:
    def __init__(self, lnl, lower, upper):
        self.lnl, self.lower, self.upper = lnl, lower, upper
    def evaluate(self, cl_uK2, A):
        l = np.arange(len(cl_uK2), dtype=np.float64)
        d = (np.asarray(cl_uK2) / A ** 2 * l * (l + 1) / (2 * np.pi))[R.LMIN:R.LMAX + 1]
        return self.lnl, R.support_record(d, self.lower, self.upper, lambda v: np.zeros(len(v)))
trf = {"transfer": tr, "pars": StubPars, "tcmb2": 1.0, "cl_lcdm_uK2": np.concatenate([[0.0, 0.0], [cont[l] for l in range(R.LMIN, R.LMAX + 1)]])}
cl_p1, _ = R.shell_sum(R.R_A_MPC, tr, one, "molien")
d_p1 = cl_p1 * np.arange(R.LMIN, R.LMAX + 1) * np.arange(R.LMIN + 1, R.LMAX + 2) / (2 * np.pi)
wide_lo, wide_hi = d_p1 * 1e-3, d_p1 * 1e3
tight_lo = wide_lo.copy(); tight_lo[1] = d_p1[1] * 2.0; tight_lo[3] = d_p1[3] * 1.5
sA = R.score("A", R.R_A_MPC, trf, StubCommander(-1e30, tight_lo, wide_hi), 1.0, -10.0, 0.3)
check(f"out-of-support branch: label Negative, delta_lnL recorded as out of support, outside l = {sA['outside_l']}",
      sA["label"] == "Negative" and sA["delta_lnL"] == "out of support" and sA["outside_l"] == [3, 5] and sA["n_outside"] == 2
      and abs(sA["max_fractional_distance_outside"] - 0.5) < 1e-12)
labels = [R.score("A", R.R_A_MPC, trf, StubCommander(v, wide_lo, wide_hi), 1.0, -10.0, 0.3)["label"] for v in (-13.0, -8.5, -7.0)]
check(f"in-support branch: Delta lnL -3, +1.5, +3 give {labels}", labels == ["Negative", "Inconclusive", "Positive"])
check("band labels: +2 Positive, -2 Negative, 1.99 Inconclusive, None Unevaluated",
      [R.band_label(v) for v in (2.0, -2.0, 1.99, None)] == ["Positive", "Negative", "Inconclusive", "Unevaluated"])

print("\n== Runtime check and the refusal to run early")
tmp = tempfile.mkdtemp()   # the packet copied without its manifest, so these checks read the same before and after the freeze
for f in R.PACKET_FILES:
    shutil.copy(os.path.join(HERE, f), tmp)
bad = R.runtime_check(tmp, P, require_manifest=False)
check(f"the runtime check passes on this environment, on the packet without its manifest ({len(bad)} mismatches)", bad == [])
check("with the manifest required (as --run requires it), a missing manifest fails closed",
      "freeze manifest missing" in R.runtime_check(tmp, P))
R.write_manifest(tmp)
check("with a matching freeze manifest the runtime check passes", R.runtime_check(tmp, P) == [])
open(os.path.join(tmp, "self_test.out"), "a").write("tamper\n")
check("a packet file changed after the manifest fails the runtime check",
      any("differs from the freeze manifest: self_test.out" in b for b in R.runtime_check(tmp, P)))
shutil.rmtree(tmp)
saved = R.RUNTIME["numpy"]; R.RUNTIME["numpy"] = "0.0"
bad2 = R.runtime_check(HERE, P); R.RUNTIME["numpy"] = saved
check("the runtime check fails closed on a changed version", any("numpy" in b for b in bad2))
out = os.path.join(tempfile.gettempdir(), "step_two_should_not_exist.json")
r = subprocess.run([sys.executable, os.path.join(HERE, "step_two_run.py"), "--out", out], capture_output=True, text=True)
check("without --run the runner exits 2 and evaluates nothing", r.returncode == 2 and "Nothing was evaluated" in r.stdout and not os.path.exists(out))

print("\n== CAMB settings (object setup only, no computation)")
from camb import nonlinear
names = {v: k for k, v in nonlinear.halofit_version_names.items()}
pars = camb.CAMBparams()
pars.set_classes(recombination_model="Recfast")
pars.Recomb.set_params(recfast_approx_model="planck")
check(f"halofit_version 5 maps to '{names.get(5)}'; Recfast 'planck' set has fudge_He 0.86 and no He rate correction",
      5 in names and abs(pars.Recomb.RECFAST_fudge_He - 0.86) < 1e-12 and pars.Recomb.RECFAST_He_rate_correction is False)
check("the BBN table named in the settings ships with CAMB", os.path.isfile(os.path.join(os.path.dirname(camb.__file__), R.CAMB_SETTINGS["bbn_table"])))
e1 = R.camb_params(pb, for_g1b=True)
check("erratum E1 reaches CAMB: one massive eigenstate carrying 3.046/3 of N_eff with 2.030667 massless, the fit's omega_nu h^2 "
      "and Y_P, helium reionization width 0.5 from z = 5, PPF dark energy, curved-sky lensing, l_max 2850, k eta_max 14000",
      e1.nu_mass_eigenstates == 1 and abs(e1.nu_mass_degeneracies[0] - 3.046 / 3) < 1e-12
      and abs(e1.num_nu_massless - (3.046 - 3.046 / 3)) < 1e-12 and abs(e1.omnuh2 / pb["omeganuh2"] - 1) < 1e-12
      and abs(e1.YHe / pb["yheused"] - 1) < 1e-5 and e1.Reion.helium_delta_redshift == 0.5 and e1.Reion.helium_redshiftstart == 5.0
      and type(e1.DarkEnergy).__name__ == "DarkEnergyPPF" and camb.config.lensing_method == 1
      and e1.max_l == 2850 and e1.max_eta_k == 14000.0)

print(f"\n{len(PASSES)} checks passed, {len(FAILS)} failed")
print("ALL PASS" if not FAILS else f"FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
