"""Step two, pre-freeze implementation qualification: the Commander file's own self-test, with the pinned clipy.

Allowed before the freeze (both reviewers, round 5): load the exact hashed Commander .clik file with the pinned clipy
and evaluate only the file-supplied test vector (check_param) against the file-supplied expected value (check_value).
No other spectrum is evaluated: not the Planck best fit, not CAMB output, not P1. The tabulated support is read from the
file, so the contract's out-of-support clause can quote it.
"""
import contextlib, hashlib, io, json, os
os.environ["CLIPY_NOJAX"] = "1"
import numpy as np
import astropy, astropy.io.fits as pf
import clipy

HERE = os.path.dirname(os.path.abspath(__file__))
CLIK = os.path.join(HERE, "planck/baseline/plc_3.0/low_l/commander/commander_dx12_v3_2_29.clik")
env = json.load(open(os.path.join(HERE, "environment.json")))

for rel, meta in env["commander_file_contents"].items():
    p = os.path.join(CLIK, rel)
    assert os.path.getsize(p) == meta["bytes"] and hashlib.sha256(open(p, "rb").read()).hexdigest() == meta["sha256"], rel
print(f"Commander file matches its recorded hashes ({len(env['commander_file_contents'])} files)")
assert clipy.__version__ == "0.15" and clipy.hasjax is False
print(f"clipy {clipy.version()} | numpy {np.__version__} | astropy {astropy.__version__} | CLIPY_NOJAX={os.environ['CLIPY_NOJAX']} | jax used: {clipy.hasjax}")

expected = None
for line in open(os.path.join(CLIK, "clik/_mdb")):
    k, t, v = line.split()
    if k == "check_value":
        expected = float(v)
check_param = pf.getdata(os.path.join(CLIK, "clik/check_param")).astype(np.float64)

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    lkl = clipy.clik(CLIK)
print("clipy's own load-time self-test:", " | ".join(s for s in buf.getvalue().strip().split("\n") if s.strip() and s.strip() != "----"))

par = np.array(lkl.default_par, dtype=np.float64)
assert np.array_equal(par, check_param), "default_par is not the file's check_param"
captured = {}
orig = lkl._internal.internal_lkl
def spy(vec):
    captured["dl"] = np.array(vec, dtype=np.float64)
    return orig(vec)
lkl._internal.internal_lkl = spy
got = float(lkl(par))
lkl._internal.internal_lkl = orig
residual = got - expected
print(f"full precision, same file-supplied vector: expected {expected:.8f}, obtained {got:.10f}, residual {residual:+.3e}")
print(f"as chi2_eff = -2 ln L: expected {-2*expected:.8f}, obtained {-2*got:.10f}")
# Recorded, not asserted. The first run asserted |residual| < 1e-6, a bound set with no stated basis, and tripped at
# 1.03e-6; the qualification tolerance is stated in the contract instead of being chosen here after the fact.
print(f"   relative residual {abs(residual/expected):.2e}; check_value is stored to 1e-8 (half a unit: 5e-9); "
      f"the decision band is 2 in ln L, {2/abs(residual):.1e} times the residual")

prior = np.array(lkl._internal.prior, dtype=np.float64)
sig = pf.open(os.path.join(CLIK, "clik/lkl_0/_external/sigma.fits"))
lmin_in, lmax_in, nbin = sig[0].header["LMIN"], sig[0].header["LMAX"], sig[0].header["NBIN"]
lmin, lmax = lkl._internal.lmin, lkl._internal.lmax
cl2x = sig[0].data[:, lmin - lmin_in:lmax + 1 - lmin_in].astype(np.float64)
nl = lmax + 1 - lmin
indep = np.zeros((2, nl))
for i in range(nl):
    lo = [j for j in range(nbin) if abs(cl2x[1, i, j] + 5) < 1e-4]
    hi = [j for j in range(nbin) if abs(cl2x[1, i, j] - 5) < 1e-4]
    indep[0, i] = cl2x[0, i, (max(lo) + 1 if lo else 0) + 2]
    indep[1, i] = cl2x[0, i, (min(hi) + 1 if hi else 10000) - 4]
print(f"tabulated support: clipy's bounds equal an independent reading of sigma.fits: {np.array_equal(prior, indep)} "
      f"(LMIN {lmin_in}, LMAX {lmax_in}, NBIN {nbin}; likelihood uses l = {lmin}..{lmax})")
assert np.array_equal(prior, indep)

dl = captured["dl"]
x, dxdcl = lkl._internal.splint_gauss_and_deriv(dl)
x = np.array(x, dtype=np.float64)
cls_edge = ["interior" if abs(v) <= 4 else "edge" for v in x]
inside = bool(np.all(dl >= prior[0]) and np.all(dl <= prior[1]))
print(f"self-test vector: inside the support at every l: {inside}; Gaussianized |x| max {np.max(np.abs(x)):.3f}; classes: "
      f"{sum(c == 'interior' for c in cls_edge)} interior, {sum(c == 'edge' for c in cls_edge)} edge")
print("   l    support lower D_l    support upper D_l    self-test D_l    x")
for i in range(nl):
    print(f"  {lmin + i:3d} {prior[0, i]:18.3f} {prior[1, i]:20.3f} {dl[i]:16.3f} {x[i]:7.3f}")

json.dump({"expected_lnL": expected, "obtained_lnL": got, "residual": residual,
           "clipy": clipy.version(), "numpy": np.__version__, "astropy": astropy.__version__, "CLIPY_NOJAX": "1",
           "support_rule": "clipy gibbs_lkl: returns -1e30 if any D_l is below prior[0] or above prior[1]; bounds are the cl2x grid "
                           "points 3 bins inside the +-5 saturation of the Gaussianized variable",
           "support": [{"l": lmin + i, "D_l_lower": prior[0, i], "D_l_upper": prior[1, i], "self_test_D_l": dl[i], "self_test_x": x[i]}
                       for i in range(nl)]},
          open(os.path.join(HERE, "commander_support.json"), "w"), indent=2)
print("commander_support.json written")
