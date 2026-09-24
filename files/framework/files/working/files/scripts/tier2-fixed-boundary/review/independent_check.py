"""Tier 2, run 1: an independent check of the run (2026-09-23). Not part of the frozen method; it checks the run's result.

(a) Exact. For a minimal surface in S^3(R), the unit normal satisfies Delta nu = -|A|^2 nu, so <a, nu> for a constant vector a
    solves J<a,nu> = -(2/R^2)<a,nu>. On gamma, nu is orthogonal to p and to gamma', which span span(e3, e4), so <e3,nu> and
    <e4,nu> vanish on the boundary. For B they are cos t sin(s/2)/sqrt(f) and -cos t cos(s/2)/sqrt(f): sector |m| = 1,
    profile cos t/sqrt(f). Checked here: that profile solves R^2 J_1 phi = -2 phi (symbolically, and at 60 digits), it is
    even, vanishes at pi/2, and is positive on [0, pi/2). So mu = -2 is the m = 1 ground state, exactly.
(b) Independent discretization. The self-adjoint form -(p phi')' + p V phi = mu p phi, p = sqrt(f), by second-order symmetric
    finite differences on a vertex grid (reflection at t = 0 for odd m), reduced to a symmetric tridiagonal problem,
    three resolutions, Richardson-extrapolated. Every eigenvalue through the first with mu > 1, sectors 0-3.
(c) Independent Sturm count at mu = 0, with scipy's Radau (implicit) instead of DOP853.
(d) Mutation arm, on a green parent: Ric 2/R^2 -> 3/R^2 must move the m = 1 ground state to -3, and fail check (b1).
Tolerance 1e-6 on finite-difference values: the method's floor is about 5e-8 (the extrapolants' spread, printed with each
value; the exact zero of m = 0 comes out at -2.4e-8).
"""
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import eigh_tridiagonal
from scipy.integrate import solve_ivp

RUN = {0: [-1.403562511105e-12, 11.65988590217], 1: [-1.999999999952, 5.24544870788], 2: [1.849413336655],
        3: [0.6916191422377, 9.1229352395]}  # the run's N = 128 values, as printed in run-1/RETURN.md
fails = []
TOL = 1e-6  # finite-difference checks: above the method's floor of about 5e-8 (v2)

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)
    return ok

# (a) exact ground state of the m = 1 sector
t = sp.symbols('t', real=True)
f = 1 - sp.Rational(3, 4) * sp.sin(t) ** 2

def RJ(phi, m, ric=2):
    V = sp.Rational(m * m, 4) / f - 1 / (2 * f ** 2) - ric
    return -sp.diff(phi, t, 2) - sp.diff(f, t) / (2 * f) * sp.diff(phi, t) + V * phi

phi1 = sp.cos(t) / sp.sqrt(f)
resid = RJ(phi1, 1) + 2 * phi1
u = sp.symbols('u', positive=True)  # u = sin t on (0, pi/2), cos t = sqrt(1 - u^2)
resid_u = sp.simplify(resid.subs({sp.sin(t): u, sp.cos(t): sp.sqrt(1 - u ** 2)}, simultaneous=True))
check("(a1) R^2 J_1 (cos t/sqrt f) = -2 cos t/sqrt f, symbolic in u = sin t: residual %s" % resid_u, resid_u == 0)
g = sp.lambdify(t, resid, "mpmath")
mp.mp.dps = 60
worst = max(abs(g(mp.mpf(k) / 61 * mp.pi / 2)) for k in range(1, 61))
check("(a2) the same at 60 points, 60 digits: max |residual| = %s" % mp.nstr(worst, 3), worst < mp.mpf(10) ** -50)
check("(a3) profile even, zero at pi/2, positive on [0, pi/2)",
      sp.simplify(phi1.subs(t, -t) - phi1) == 0 and phi1.subs(t, sp.pi / 2) == 0
      and all(float(phi1.subs(t, k * sp.pi / 200)) > 0 for k in range(0, 100)))
X = sp.symbols('s', real=True)
p = [sp.cos(t) * sp.cos(X), sp.cos(t) * sp.sin(X), sp.sin(t) * sp.cos(X / 2), sp.sin(t) * sp.sin(X / 2)]
ps = [sp.diff(c, X) for c in p]
pt = [sp.diff(c, t) for c in p]
M = sp.Matrix([p, ps, pt])
n = [(-1) ** i * M[:, [j for j in range(4) if j != i]].det() for i in range(4)]
n = [sp.simplify(sp.expand_trig(c)) for c in n]
check("(a4) normal components: <e3,n> = %s, <e4,n> = %s, |n|^2 = f" % (n[2], n[3]),
      sp.simplify(n[2] - sp.sin(X / 2) * sp.cos(t)) == 0 and sp.simplify(n[3] + sp.cos(X / 2) * sp.cos(t)) == 0
      and sp.simplify(sum(c ** 2 for c in n) - f) == 0)

# (b) symmetric finite differences, Richardson-extrapolated
def fd_eigs(m, N, ric=2.0, k=4):
    h = (np.pi / 2) / N
    tt = np.arange(N + 1) * h
    fv = lambda x: 1 - 0.75 * np.sin(x) ** 2
    pv = np.sqrt(fv(tt))
    ph = np.sqrt(fv(tt[:-1] + h / 2))  # p at half nodes i + 1/2
    V = m * m / (4 * fv(tt)) - 1 / (2 * fv(tt) ** 2) - ric
    first = 1 if m % 2 == 0 else 0  # even m: phi(0) = 0; odd m: reflection phi(-h) = phi(h)
    idx = np.arange(first, N)       # phi(pi/2) = 0 always
    diag = np.empty(len(idx)); off = np.empty(len(idx) - 1); w = np.empty(len(idx))
    for r, i in enumerate(idx):
        if i == 0:
            diag[r] = ph[0] / h ** 2 + pv[0] * V[0] / 2; w[r] = pv[0] / 2
        else:
            diag[r] = (ph[i - 1] + ph[i]) / h ** 2 + pv[i] * V[i]; w[r] = pv[i]
        if r < len(idx) - 1:
            off[r] = -ph[i] / h ** 2
    s = 1 / np.sqrt(w)
    return eigh_tridiagonal(diag * s * s, off * s[:-1] * s[1:], select='i', select_range=(0, k - 1), eigvals_only=True)

def extrapolated(m, ric=2.0, Ns=(4000, 8000, 16000)):
    e = [fd_eigs(m, N, ric) for N in Ns]
    r1 = (4 * e[1] - e[0]) / 3; r2 = (4 * e[2] - e[1]) / 3
    return r2, np.abs(r2 - r1)

print("\n(b) symmetric finite differences, N = 4000, 8000, 16000, Richardson; spread = |two extrapolants' difference|")
for m in range(4):
    vals, spread = extrapolated(m)
    shown = []
    for j, v in enumerate(vals):
        shown.append(j)
        if v > 1:
            break
    for j in shown:
        un = RUN[m][j] if j < len(RUN[m]) else None
        print("  m=%d  mu_%d = % .10f  (spread %.1e)   run, Chebyshev N=128: %s" % (m, j, vals[j], spread[j],
              "% .10f" % un if un is not None else "not reported"))
        if un is not None:
            check("(b) m=%d mu_%d agrees with the run to 1e-6" % (m, j), abs(vals[j] - un) < 1e-6)
    neg = sum(1 for v in vals if v < -TOL)
    near = sum(1 for v in vals if abs(v) <= TOL)
    print("  m=%d  negative eigenvalues: %d, near-zero (|mu| <= %.0e): %d" % (m, neg, TOL, near))
v1, _ = extrapolated(1)
check("(b1) m=1 ground state = -2 to 1e-6 (the exact value of (a))", abs(v1[0] + 2) < TOL)
check("(b2) m=2 has no eigenvalue below 1 (index 0, no near-zero case)", extrapolated(2)[0][0] > 1)

# (c) Sturm count at mu = 0 with Radau
def radau_count(m, ric=2.0):
    fv = lambda x: 1 - 0.75 * np.sin(x) ** 2
    fp = lambda x: -1.5 * np.sin(x) * np.cos(x)
    rhs = lambda x, y: [y[1], -fp(x) / (2 * fv(x)) * y[1] + (m * m / (4 * fv(x)) - 1 / (2 * fv(x) ** 2) - ric) * y[0]]
    y0 = [0.0, 1.0] if m % 2 == 0 else [1.0, 0.0]
    sol = solve_ivp(rhs, [0, np.pi / 2], y0, method='Radau', rtol=1e-11, atol=1e-13, dense_output=True)
    g = np.linspace(0, np.pi / 2 - 1e-6, 20001)
    y = sol.sol(g)[0]
    zeros = int(np.sum(y[1:] * y[:-1] < 0))
    return zeros, abs(sol.sol(np.pi / 2)[0]) / np.max(np.abs(y))

print("\n(c) Sturm count at mu = 0, Radau")
for m, (z_run, rho_run) in {0: (0, 4.778534e-12), 1: (1, 1.0), 2: (0, 0.7380306), 3: (0, 1.0)}.items():
    z, rho = radau_count(m)
    print("  m=%d  zeros %d  rho %.3e   (run: %d, %.3e)" % (m, z, rho, z_run, rho_run))
    check("(c) m=%d zero count matches the run, and rho agrees on near-zero status" % m,
          z == z_run and ((rho <= 1e-6) == (rho_run <= 1e-8)))

# (d) mutation arm on a green parent
print("\n(d) mutation arm: Ric 2 -> 3")
check("(d0) parent green: (b1) passed on the unmutated operator", not any(x.startswith("(b1)") for x in fails))
vm, _ = extrapolated(1, ric=3.0)
print("  mutated m=1 ground state: %.10f" % vm[0])
check("(d1) mutated ground state is -3 (the identity shifts with the Ricci term)", abs(vm[0] + 3) < TOL)
check("(d2) the mutation fails check (b1)", not abs(vm[0] + 2) < TOL)

print("\n%s: %d failed" % ("ALL PASS" if not fails else "FAILURES", len(fails)))
