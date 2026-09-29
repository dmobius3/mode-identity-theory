"""Review of the first-positive transfer run: the same cone-trace matching's spectrum (2026-09-28), by direct ODE integration, independent of the
Legendre-function secular formula. Constant transverse sector, one half, R = 1: -(1/sin d)(sin d f')' = lam f on
(0, pi/2), d the distance to the cone, d = pi/2 the seam. Near the cone f = uN ln(d/2) + uD + o(1) (the pillar's
section 3.5) and the bridging datum is uDt = uD + uN ln(delta0/2). seam "D" (f = 0 at the seam) is the untwisted
same-trace odd sector; seam "N" (f' = 0) is the pillar's twisted antisymmetric subsector."""
import numpy as np, math, sys
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
EPS = 1e-7
def traces(lam, seam, fac=1.0):
    y0 = [0.0, 1.0] if seam == "D" else [1.0, 0.0]
    s = solve_ivp(lambda d, v: [v[1], -math.cos(d) / math.sin(d) * v[1] - lam * v[0]], [math.pi / 2, EPS], y0,
                  method="DOP853", rtol=1e-12, atol=1e-14)
    f, fp = s.y[0, -1], s.y[1, -1]; uN = fac * EPS * fp
    return uN, f - uN * math.log(EPS / 2)
def uDt(lam, seam, d0, fac=1.0):
    uN, uD = traces(lam, seam, fac); return uD + uN * math.log(d0 / 2)
def roots(fn, lo=-8, hi=14, N=700):
    xs = np.linspace(lo, hi, N); vs = [fn(x) for x in xs]
    return [brentq(fn, xs[i], xs[i + 1], xtol=1e-13) for i in range(N - 1) if vs[i] * vs[i + 1] < 0]
ok = True
def report(name, passed, detail):
    global ok; ok &= passed; print(("PASS " if passed else "FAIL ") + name + ": " + detail); sys.stdout.flush()
close = lambda a, b, t=1e-7: len(a) == len(b) and all(abs(x - y) < t for x, y in zip(a, b))
# S1: the Friedrichs towers (uN = 0): even across the seam 0, 6; odd 2, 12.
fN = roots(lambda l: traces(l, "N")[0], -1, 14); fD = roots(lambda l: traces(l, "D")[0], -1, 14)
report("S1 Friedrichs towers", close(fN, [0, 6]) and close(fD, [2, 12]), f"seam N {[round(x, 8) for x in fN]}, seam D {[round(x, 8) for x in fD]}")
fx = roots(lambda l: traces(l, "D")[0], -1, 14)
print(f"   arm S1 (seams swapped): {[round(x, 8) for x in fx]} -> {'trips' if not close(fx, [0, 6]) else 'MISSED'}"); ok &= not close(fx, [0, 6])
# S2: the pillar's Proposition 4.4, seam N: one negative root for each delta0, and the deformed root at 2 when delta0 = 2/e.
r = roots(lambda l: uDt(l, "N", 2 / math.e))
report("S2 pillar threshold", sum(x < 0 for x in r) == 1 and any(abs(x - 2) < 1e-7 for x in r), f"delta0 = 2/e roots {[round(x, 8) for x in r]}")
rm = roots(lambda l: uDt(l, "N", 2 / math.e, fac=2.0))
print(f"   arm S2 (log coefficient read as for ln d^2): {[round(x, 8) for x in rm]} -> {'trips' if not any(abs(x - 2) < 1e-7 for x in rm) else 'MISSED'}")
ok &= not any(abs(x - 2) < 1e-7 for x in rm)
# S3: the same-trace odd sector at delta0 = 1 reproduces the run's positive root 7.823147140.
r1 = roots(lambda l: uDt(l, "D", 1.0)); pos = [x for x in r1 if x > 0]
report("S3 run's positive root", bool(pos) and abs(pos[0] - 7.823147140) < 1e-7, f"delta0 = 1 roots {[round(x, 8) for x in r1]}")
rn = [x for x in roots(lambda l: uDt(l, "N", 1.0)) if x > 0]
print(f"   arm S3 (seam N): first positive {rn[0]:.8f} -> {'trips' if abs(rn[0] - 7.823147140) >= 1e-7 else 'MISSED'}"); ok &= abs(rn[0] - 7.823147140) >= 1e-7
# Findings, not checks.
neg = [x for x in r1 if x < 0]
print(f"FINDING 1: at delta0 = R the same-trace odd sector has the negative root {neg[0]:.8f}/R^2 (lambda < -1/4, where nu = -1/2 + i kappa)." if neg else "FINDING 1: no negative root")
u2 = traces(2.0, "D")
print(f"FINDING 2: lambda = 2 is not a same-trace eigenvalue for any delta0: the seam-D solution there is a multiple of cos d, regular (uN = {u2[0]:.1e}), so uDt = uD = {u2[1]:.9f}, nonzero for every delta0.")
print("delta0 scan, same-trace odd sector roots in [-8, 14]:")
for d0 in (0.25, 0.5, 1.0, 1.5, 3.0, 4.0, 8.0):
    print(f"   delta0 = {d0:<5}", [round(x, 6) for x in roots(lambda l: uDt(l, "D", d0))])
print("ALL PASS, every arm trips" if ok else "NOT ALL PASS")
