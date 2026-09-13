"""Pre-freeze check of the one term the Sachs-Wolfe-only estimate leaves out that helps route A:
the late integrated Sachs-Wolfe (ISW) effect.  Theory only: no data, no likelihood, no CAMB.

Crude line of sight: flat matter + Lambda background (Omega_m = 0.315, h = 0.674, no radiation),
potential Phi = -(3/5) R g(a) with g = D/a from linear growth, scale-invariant power, no matter
transfer function.  Per unit (-R/5) the temperature transfer is
    T_l(k) = g(a*) j_l(k chi*) + 6 int (dg/da) j_l(k r(a)) da,
with chi* = 14 Gpc for the Sachs-Wolfe term, as in sw_estimate.py.  The ratio is
    C_l(P1)/C_l(LCDM) = sum_N W_N T_l(k_N)^2 / (4 pi int dln k T_l(k)^2).
With the ISW coefficient set to zero it must reproduce sw_estimate.py.
"""
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import cumulative_trapezoid, trapezoid

OM, H = 0.315, 0.674
DH = 299792.458 / (100 * H)          # Mpc
CHI = 14000.0                        # Mpc, Sachs-Wolfe distance, as in sw_estimate.py
LS = list(range(2, 11))
FAILS = []

def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILS.append(label)

E = lambda a: np.sqrt(OM / a**3 + (1 - OM))
ag = np.linspace(1e-4, 1.0, 400001)
D = 2.5 * OM * E(ag) * cumulative_trapezoid(1 / (ag * E(ag))**3, ag, initial=0.0)
g_full = D / ag
check("growth: g -> 1 deep in matter domination", abs(g_full[4000] - 1) < 2e-3)
print(f"   g(a = 1) = {g_full[-1]:.4f} (linear growth suppression today)")
a = np.linspace(0.05, 1.0, 3001)
g = np.interp(a, ag, g_full)
dgda = np.gradient(g, a)
r = DH * (trapezoid(1 / (ag**2 * E(ag)), ag) - np.interp(a, ag, cumulative_trapezoid(1 / (ag**2 * E(ag)), ag, initial=0.0)))
print(f"   r(a = 0.05) = {r[0]:.0f} Mpc; the ISW source dg/da is negligible before that")

def transfer(k, l, isw=6.0):
    k = np.atleast_1d(k)
    out = np.empty(len(k))
    for s in range(0, len(k), 400):
        kk = k[s:s + 400]
        integ = trapezoid(dgda[None, :] * spherical_jn(l, kk[:, None] * r[None, :]), a, axis=1)
        out[s:s + 400] = spherical_jn(l, kk * CHI) + isw * integ
    return out

x = np.concatenate([np.geomspace(1e-3, 1.0, 400, endpoint=False), np.arange(1.0, 400.0, 0.02)])
k = x / CHI
lnk = np.log(k)

def molien_counts(nmax):
    c = np.zeros(nmax + 1, dtype=np.int64); c[0] = 1
    for step in (12, 20):
        for n in range(step, nmax + 1):
            c[n] += c[n - step]
    out = c.copy(); out[30:] += c[:-30]
    return out
m = molien_counts(3000)
N = np.arange(1, 3001)
W = 480 * np.pi * m[1:] * (N + 1) / (N * (N + 2))**1.5

def ratio(R, l, isw):
    kN = np.sqrt(N * (N + 2)) / R
    keep = (m[1:] > 0) & (kN * CHI <= 400.0)
    num = np.sum(W[keep] * transfer(kN[keep], l, isw)**2)
    den = 4 * np.pi * trapezoid(transfer(k, l, isw)**2, lnk)
    return num / den

print("\n== Fixture: continuum Sachs-Wolfe integral times 2l(l+1) (must be 1)")
sw_norm = {l: trapezoid(spherical_jn(l, x)**2, np.log(x)) * 2 * l * (l + 1) for l in (2, 5, 10)}
print("   " + ", ".join(f"l = {l}: {v:.5f}" for l, v in sw_norm.items()))
check("continuum normalization", all(abs(v - 1) < 1e-3 for v in sw_norm.values()))

print("\n== Fixture: ISW switched off reproduces sw_estimate.py (A 6.13, B 19.7 at l = 2..5)")
ref = {6130.0: [0.011, 0.004, 0.039, 0.011], 19700.0: [0.019, 0.226, 0.267, 0.152]}
got = {R: [ratio(R, l, 0.0) for l in (2, 3, 4, 5)] for R in ref}
for R in ref:
    print(f"   R = {R/1000:5.2f} Gpc: " + ", ".join(f"{g_:.3f}" for g_ in got[R]) + "   (sw_estimate: " + ", ".join(str(v) for v in ref[R]) + ")")
check("ISW-off ratios match sw_estimate.py to its printed precision",
      all(abs(round(gv, 3) - rv) <= 0.001 for R in ref for gv, rv in zip(got[R], ref[R])))

print("\n== LCDM in the same crude model: share of C_l from the ISW term alone, and the cross term")
for l in LS:
    tot = trapezoid(transfer(k, l)**2, lnk)
    sw = trapezoid(transfer(k, l, 0.0)**2, lnk)
    iswonly = trapezoid((transfer(k, l) - transfer(k, l, 0.0))**2, lnk)
    print(f"   l = {l:2d}: ISW auto {iswonly/tot:6.3f}   SW auto {sw/tot:6.3f}   cross {(tot - sw - iswonly)/tot:+6.3f}")

print("\n== C_l(P1)/C_l(LCDM) with and without the ISW term")
print("     l    A 6.13: SW only   with ISW      B 19.7: SW only   with ISW")
res = {}
for l in LS:
    row = [ratio(6130.0, l, 0.0), ratio(6130.0, l, 6.0), ratio(19700.0, l, 0.0), ratio(19700.0, l, 6.0)]
    res[l] = row
    print(f"   {l:3d}   {row[0]:14.3f} {row[1]:10.3f}   {row[2]:17.3f} {row[3]:10.3f}")
print(f"\n   A: quadrupole {res[2][1]/res[2][0]:.1f} times the Sachs-Wolfe-only figure; "
      f"median over l = 2..10 with ISW {np.median([res[l][1] for l in LS]):.3f} (SW only {np.median([res[l][0] for l in LS]):.3f})")
print("\nALL PASS" if not FAILS else f"\nFAILED: {FAILS}")
