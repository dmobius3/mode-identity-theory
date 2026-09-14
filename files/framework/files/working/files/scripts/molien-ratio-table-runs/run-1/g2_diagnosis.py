#!/usr/bin/env python3
"""Why the ratio table's run stopped at G2, read from the gate's own computation.

Post-run and diagnostic only. It imports the frozen runner from the committed packet, repeats the transfer run at the
chosen boost with the same code and settings (twice: once through the runner, once kept whole to read its parameters
back), and examines only G2's objects: CAMB's q grid, the frozen cubic spline on it, and the G2 fixture's full-S^3 shell
sum at R = 200 chi*. No other interpolation is tried and no shell sum is formed at either route's radius. Two background
calculations are made only to read CAMB's parameters back, one of them with v1's two lensing flags on; no transfer
function or spectrum is computed with any setting other than the frozen ones.

Usage: python g2_diagnosis.py <packet> <folder holding the parameter file> <result.json>
"""
import json, math, os, sys

import numpy as np

PKT, DATA, RES = sys.argv[1:4]
sys.path.insert(0, PKT)
import ratio_table_run as r  # noqa: E402  (the frozen runner, imported, not run)
import camb  # noqa: E402

res = json.load(open(RES, encoding="utf-8"))
part = res["partial"]
assert res["status"] == "Uninformative" and res["reason"] == "G2 failed", res["reason"]
assert r.runtime_check(PKT, DATA) == [], "the runtime is not the frozen one"
boost = part["chosen_boost"]
p, _ = r.read_minimum(os.path.join(DATA, r.COMPARISON_FIT + ".minimum"))
L = np.arange(r.LMIN, r.LMAX + 1)

print(f"== 1. The transfer run at AccuracyBoost {boost}, repeated by the frozen code")
t = r.compute_transfer(p, boost)
g, rec = r.grid_record(t), part["grid"][-1]
for key in ("max_spacing", "required", "reach_kchi", "chi_star_mpc", "n_q"):
    print(f"  {key:12s} {g[key]!r:>24}   run: {rec[key]!r}")
dl = np.array(r.lcdm_dl(t)) / np.array(part["LCDM_D_l_uK2"]["frozen"]) - 1
print(f"  D_l(LCDM) against the run's record: largest relative difference {np.max(np.abs(dl)):.1e}")

data = camb.get_transfer_functions(r.camb_params(p, boost))   # the same transfer run, kept whole to read its parameters back
tau0 = float(data.conformal_time(0.0))
q = np.asarray(t["q"], dtype=np.float64)
assert np.array_equal(q, np.asarray(data.get_cmb_transfer_data("scalar").q, dtype=np.float64))
x = q * tau0
P, Ls = data.Params, np.asarray(t["L"])
print(f"\n== 2. CAMB's q grid in k eta0 (eta0 = {tau0:.3f} Mpc, the conformal time today, from the same transfer run)")
print(f"  {len(q)} points, from k eta0 = {x[0]:.4g} to {x[-1]:.6g}; max_eta_k is {r.TRANSFER['max_eta_k']:.0f}")
print(f"  the contract's reading (sections 3 and 8) put the end at k eta0 = 2.5 x 260 x {boost} = {2.5 * 260 * boost:.0f}")
print(f"  the run's parameters, read back: Want_CMB {P.Want_CMB}, Want_CMB_lensing {P.Want_CMB_lensing}, limber_windows"
      f" {P.SourceTerms.limber_windows}, limber_phi_lmin {P.SourceTerms.limber_phi_lmin}, max_l {P.max_l}, max_eta_k"
      f" {P.max_eta_k}, AccuracyBoost {P.Accuracy.AccuracyBoost}, BessIntBoost {P.Accuracy.BessIntBoost}; the runner sets no"
      f" source windows; transfer multipoles {int(Ls.min())} to {int(Ls.max())} ({len(Ls)})")
lw = lambda prm: prm.SourceTerms.limber_windows
pre, v1 = r.camb_params(p, boost), r.camb_params(p, boost)
v1.DoLensing, v1.Want_CMB_lensing = True, True   # v1's two lensing flags, for a background calculation only
print(f"  limber_windows: in a fresh CAMBparams() {lw(camb.CAMBparams())}; in the runner's parameter object before any"
      f" run {lw(pre)}; after a background calculation {lw(camb.get_background(pre).Params)}; after the transfer run"
      f" {lw(P)}; with both lensing flags on (v1's), after a background calculation {lw(camb.get_background(v1).Params)}")
s = np.diff(x)
ratio = s[1:] / s[:-1]
for i in np.where((ratio > 1.5) | (ratio < 1 / 1.5))[0]:
    print(f"  the step changes at k eta0 = {x[i + 1]:9.3f}: {s[i]:.5g} -> {s[i + 1]:.5g} (x {ratio[i]:.4g})")
j = int(np.argmax(ratio)) + 1   # x[j] is the last knot before the largest jump in spacing
print(f"  the largest jump: at k eta0 = {x[j]:.3f}, from {s[j - 1]:.5g} to {s[j]:.5g} (x {s[j] / s[j - 1]:.1f}); the steps"
      f" the contract names are 1.875/boost = {1.875 / boost:.5g} and 0.04 tau0/boost = {0.04 * tau0 / boost:.5g};"
      f" {len(x) - 1 - j} coarse steps run from there to the end")

print("\n== 3. Where each Delta_l is nonzero on CAMB's grid (k eta0 of the knots)")
tr = r.check_transfer(t)
D = np.asarray(t["delta"], dtype=np.float64)
idx = {int(l): i for i, l in enumerate(t["L"])}
print("   l  first nonzero   last nonzero   next knot   zeros inside   nonzero above the jump   max |Delta_l|")
last_nz = {}
for l in L:
    raw = D[idx[int(l)]]
    nz = np.nonzero(raw)[0]
    a, b = int(nz[0]), int(nz[-1])
    last_nz[int(l)] = b
    nxt = f"{x[b + 1]:11.6g}" if b + 1 < len(x) else "        end"
    print(f"  {l:2d}  {x[a]:13.5g}  {x[b]:13.6g}  {nxt}  {int(np.sum(raw[a:b + 1] == 0)):12d}  {int(np.sum(raw[j + 1:] != 0)):22d}"
          f"   {np.max(np.abs(raw)):.3e}")

print("\n== 4. G2's shell cutoff: the doublings, and the failing one split by wavenumber (full S^3 spectrum, R = 200 chi*)")
R = r.G2_R_OVER_CHI * t["chi_star"]
assert abs(R / part["G2"]["R_mpc"] - 1) < 1e-9
pk = t["power"]
c1 = r.shell_sum(R, tr, pk, "s3", start=524288, cap=524288)[0]
c2 = r.shell_sum(R, tr, pk, "s3", start=1048576, cap=1048576)[0]
c3 = r.shell_sum(R, tr, pk, "s3", start=2097152, cap=2097152)[0]
rel12, rel23 = np.abs(c2 - c1) / np.abs(c2), np.abs(c3 - c2) / np.abs(c3)
run_ch = part["G2"]["s3"]["cutoff"]["changes"]
print(f"  change at N_max 1048576: {rel12.max():.6e} (run {run_ch[-2][1]:.6e}); at 2097152: {rel23.max():.6e} (run {run_ch[-1][1]:.6e})")
kn = lambda n: math.sqrt(n * (n + 2.0)) / R
print(f"  shells 524288 < N <= 1048576 lie at k eta0 = {kn(524288) * tau0:.1f} to {kn(1048576) * tau0:.1f};"
      f" N_max = 2^21 reaches k eta0 = {kn(2 ** 21) * tau0:.1f}")
dev = c3 / r.continuum(t) - 1
print(f"  G2's deviation of the sum to 2^21 from CAMB's continuum, largest over l: {np.max(np.abs(dev)):.6e}"
      f" (run {part['G2']['s3']['max_fractional_deviation']:.6e})")
print("   l   change at 1048576   change at 2097152   deviation at 2097152")
for i, l in enumerate(L):
    print(f"  {l:2d}  {rel12[i]:18.3e}  {rel23[i]:18.3e}  {dev[i]:+20.3e}")
li = int(np.argmax(rel12))
print(f"  the largest change is at l = {L[li]}; each part below is its share of C_l there, and the largest share over l")
N_all, W_all = r.shell_table(r.CUT_CAP, "s3")


def part_sum(n0, n1, klo, khi):
    acc = np.zeros(len(L))
    for a in range(n0, n1, 250_000):
        b = min(n1, a + 250_000)
        N, w = N_all[a:b], W_all[a:b]
        k = np.sqrt(N * (N + 2)) / R
        sel = (k >= klo) & (k < khi)
        if np.any(sel):
            acc = acc + (tr(L, k[sel]) ** 2) @ (w[sel] * pk(k[sel]))
    return acc


edges = [0.0, q[j], q[j + 1], q[j + 2], q[j + 3], np.inf]
names = ("below the jump", "coarse interval 1", "coarse interval 2", "coarse interval 3", "beyond interval 3")
total = np.zeros(len(L))
for nm, lo, hi in zip(names, edges[:-1], edges[1:]):
    ps = part_sum(524288, 1048576, lo, hi)
    total += ps
    lo_x, hi_x = max(lo * tau0, kn(524288) * tau0), min(hi * tau0, kn(1048576) * tau0)
    print(f"  {nm:18s} k eta0 {lo_x:7.1f} to {hi_x:7.1f}: {ps[li] / c2[li]:+.3e} at l = {L[li]}; largest over l {np.max(np.abs(ps / c2)):.3e}")
print(f"  the parts reproduce the change to {np.max(np.abs(total - (c2 - c1)) / np.abs(c2)):.1e}")

print("\n== 5. The frozen spline in the first coarse interval (k eta0 3000 to 3187.5), against Delta_l just below the jump")
period = 2 * math.pi / t["chi_star"]
below = (q >= q[j] - 3 * period) & (q <= q[j])
print("  A: the largest |Delta_l| at the knots over the last three 2 pi/chi* periods below the jump. Then, over A: the largest")
print("  |spline| in the interval, |Delta_l| at its two knots, and the spline's slope at the jump times one period.")
print("   l           A   spline/A   left knot/A   right knot/A   slope x period/A")
for l in L:
    raw = D[idx[int(l)]]
    A = float(np.max(np.abs(raw[below])))
    if A == 0:
        print(f"  {l:2d}  zero below the jump (its last nonzero knot is at k eta0 {x[last_nz[int(l)]]:.6g})")
        continue
    xs = np.linspace(q[j], q[j + 1], 4001)
    sp = float(np.max(np.abs(tr([int(l)], xs)[0])))
    slope = float(tr.splines[int(l)](q[j], 1))
    print(f"  {l:2d}  {A:10.3e}  {sp / A:9.4g}  {abs(raw[j]) / A:12.3g}  {abs(raw[j + 1]) / A:13.3g}  {abs(slope) * period / A:16.3g}")
