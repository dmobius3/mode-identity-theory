"""Tier 2, run 1, review: the reflection check (2026-09-23). Not part of the frozen method.

Claim. The antipodal copy of B is B rotated by pi about gamma: -p(s, -t) = R12(pi) p(s, t). That rotation fixes gamma
pointwise and swaps the two halves of Lawson's closed Klein bottle tau_{2,1} = B u (-B). So the closed bottle's Jacobi
spectrum is B's Dirichlet spectrum plus B's Neumann spectrum, and Morozov-Penskoi's index 7 and nullity 5 check the run.

Checked here:
(a) the rotation identity, symbolically, and V_m(pi - t) = V_m(t), so in each sector the reflection is t -> pi - t;
(b) the exact Neumann facts: sin t/sqrt f solves R^2 J_2 phi = -2 phi with phi'(pi/2) = 0 (the pair <e1,nu>, <e2,nu>), and
    the rotation profiles of m = 1, 3 have phi'(pi/2) = 0, so they are Neumann zero modes (four real fields);
(c) by symmetric finite differences (three resolutions, Richardson): the closed-bottle sector problems on [0, pi], B's
    Dirichlet and Neumann problems on [0, pi/2], the eigenvalue-by-eigenvalue splitting, and the totals with multiplicity;
(d) an exact lower bound, Neumann index >= 5. The Neumann form imposes no boundary condition, sectors are orthogonal
    for it, and five test functions each have negative form: <e1,nu>, <e2,nu> in m = +-2 (eigenfunctions at -2); the
    constant profile in m = +-1, since V_1 = u/4 - u^2/2 - 2 <= -9/4 for u = 1/f in [1, 4]; and sin t in m = 0, whose
    form is at most int (cos^2 t - 2 sin^2 t) sqrt f dt <= pi/4 - pi/4 = 0 minus a positive term, using 1/2 <= sqrt f <= 1.
    (<e3,nu>, <e4,nu> would also serve in m = +-1: they vanish on gamma, so their form is -2 times their norm.)
    With Dirichlet index >= 2 exact, closed index 7 then forces Dirichlet index = 2;
(e) a mutation arm on a green parent: dropping |A|^2 must break the 7/5 totals.
Tolerance 1e-6 on finite-difference values, above the method's floor of about 5e-8 (as in independent_check.py).
"""
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import eigh_tridiagonal

TOL = 1e-6
fails = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)
    return ok

# (a) the rotation identity and the symmetry of V_m
s, t = sp.symbols('s t', real=True)
p = sp.Matrix([sp.cos(t) * sp.cos(s), sp.cos(t) * sp.sin(s), sp.sin(t) * sp.cos(s / 2), sp.sin(t) * sp.sin(s / 2)])
R12pi = sp.diag(-1, -1, 1, 1)
check("(a1) -p(s, -t) = R12(pi) p(s, t)", sp.simplify(-p.subs(t, -t) - R12pi * p) == sp.zeros(4, 1))
f = 1 - sp.Rational(3, 4) * sp.sin(t) ** 2
m_ = sp.symbols('m', integer=True)
V = m_ ** 2 / (4 * f) - 1 / (2 * f ** 2) - 2
check("(a2) V_m(pi - t) = V_m(t)", sp.simplify(V.subs(t, sp.pi - t) - V) == 0)

# (b) exact Neumann facts
def RJ(phi, m):
    Vm = sp.Rational(m * m, 4) / f - 1 / (2 * f ** 2) - 2
    return -sp.diff(phi, t, 2) - sp.diff(f, t) / (2 * f) * sp.diff(phi, t) + Vm * phi

u = sp.symbols('u', positive=True)
def zero_in_u(expr):
    return sp.simplify(expr.subs({sp.sin(t): u, sp.cos(t): sp.sqrt(1 - u ** 2)}, simultaneous=True)) == 0

phi2 = sp.sin(t) / sp.sqrt(f)
check("(b1) R^2 J_2 (sin t/sqrt f) = -2 sin t/sqrt f", zero_in_u(RJ(phi2, 2) + 2 * phi2))
check("(b2) (sin t/sqrt f)' = 0 at pi/2, odd", sp.simplify(sp.diff(phi2, t).subs(t, sp.pi / 2)) == 0 and sp.simplify(phi2.subs(t, -t) + phi2) == 0)
phiK1 = (3 * sp.sin(t) ** 2 - 2) / (4 * sp.sqrt(f))
phiK3 = (1 + sp.cos(t) ** 2) / (4 * sp.sqrt(f))
check("(b3) rotation profiles solve J_1, J_3 = 0 and have zero slope at pi/2",
      zero_in_u(RJ(phiK1, 1)) and zero_in_u(RJ(phiK3, 3))
      and sp.simplify(sp.diff(phiK1, t).subs(t, sp.pi / 2)) == 0 and sp.simplify(sp.diff(phiK3, t).subs(t, sp.pi / 2)) == 0)

# (c) finite differences: bc 'D' removes the end node, 'N' keeps it with a reflected half cell
def fd_eigs(m, L, bc0, bcL, N, k=10, dropA=False):
    h = L / N
    tt = np.arange(N + 1) * h
    fv = lambda x: 1 - 0.75 * np.sin(x) ** 2
    pv = np.sqrt(fv(tt))
    ph = np.sqrt(fv(tt[:-1] + h / 2))
    V = m * m / (4 * fv(tt)) - (0 if dropA else 1 / (2 * fv(tt) ** 2)) - 2
    idx = np.arange(0 if bc0 == 'N' else 1, N + 1 if bcL == 'N' else N)
    n = len(idx)
    diag = np.empty(n); off = np.empty(n - 1); w = np.empty(n)
    for r, i in enumerate(idx):
        left = ph[i - 1] if i > 0 else None
        right = ph[i] if i < N else None
        if i == 0:
            diag[r] = right / h ** 2 + pv[i] * V[i] / 2; w[r] = pv[i] / 2
        elif i == N:
            diag[r] = left / h ** 2 + pv[i] * V[i] / 2; w[r] = pv[i] / 2
        else:
            diag[r] = (left + right) / h ** 2 + pv[i] * V[i]; w[r] = pv[i]
        if r < n - 1:
            off[r] = -ph[i] / h ** 2
    sc = 1 / np.sqrt(w)
    return eigh_tridiagonal(diag * sc * sc, off * sc[:-1] * sc[1:], select='i', select_range=(0, k - 1), eigvals_only=True)

def extrap(m, L, bc0, bcL, base, dropA=False, k=10):
    e = [fd_eigs(m, L, bc0, bcL, base * 2 ** j, k, dropA) for j in range(3)]
    return (4 * e[2] - e[1]) / 3, np.abs((4 * e[2] - e[1]) / 3 - (4 * e[1] - e[0]) / 3)

def counts(vals):
    return int(np.sum(vals < -TOL)), int(np.sum(np.abs(vals) <= TOL))

def spectra(dropA=False, show=True):
    tot = {'D': [0, 0], 'N': [0, 0], 'K': [0, 0]}
    split_ok = True
    for m in range(4):
        b0 = 'D' if m % 2 == 0 else 'N'
        D, sD = extrap(m, np.pi / 2, b0, 'D', 4000, dropA)
        Nn, sN = extrap(m, np.pi / 2, b0, 'N', 4000, dropA)
        K, sK = extrap(m, np.pi, b0, b0, 8000, dropA, k=20)
        mult = 1 if m == 0 else 2
        for key, vals in (('D', D), ('N', Nn), ('K', K)):
            ni, nn = counts(vals)
            tot[key][0] += mult * ni; tot[key][1] += mult * nn
        merged = np.sort(np.concatenate([D, Nn]))
        below = K[K < 12]
        ok = len(below) <= len(merged) and np.max(np.abs(below - merged[:len(below)])) < TOL
        split_ok &= ok
        if show:
            print("  m=%d  B Dirichlet: %s" % (m, " ".join("% .7f" % v for v in D[D < 12])))
            print("       B Neumann:   %s" % " ".join("% .7f" % v for v in Nn[Nn < 12]))
            print("       closed [0,pi]: %s   (max spread %.1e)" % (" ".join("% .7f" % v for v in below), max(sD.max(), sN.max(), sK.max())))
            print("       counts (index, nullity): Dirichlet %s, Neumann %s, closed %s; closed = Dirichlet u Neumann below 12: %s"
                  % (counts(D), counts(Nn), counts(K), ok))
    return tot, split_ok

print("\n(c) finite differences, h = pi/16000 at the finest level; |m| >= 4 contributes nothing (V_m > 0)")
tot, split_ok = spectra()
print("  totals with multiplicity (index, nullity): Dirichlet %s, Neumann %s, closed %s" % (tot['D'], tot['N'], tot['K']))
check("(c1) the splitting holds sector by sector", split_ok)
check("(c2) B Dirichlet totals = (2, 1), the run's", tot['D'] == [2, 1])
check("(c3) B Neumann totals = (5, 4)", tot['N'] == [5, 4])
check("(c4) closed totals = (7, 5), Morozov-Penskoi's Theorem 2", tot['K'] == [7, 5])

# (d) exact lower bound on the Neumann index: five test functions in orthogonal sectors, no boundary condition imposed
uu = sp.symbols('uu', positive=True)
V1u = uu / 4 - uu ** 2 / 2 - 2          # V_1 with u = 1/f
check("(d1) V_1 = u/4 - u^2/2 - 2 in u = 1/f: exactly V_1", sp.simplify(V.subs(m_, 1) - V1u.subs(uu, 1 / f)) == 0)
crit = sp.solve(sp.diff(V1u, uu), uu)
vmax = max([V1u.subs(uu, 1), V1u.subs(uu, 4)] + [V1u.subs(uu, c) for c in crit if 1 <= c <= 4])
check("(d2) V_1 <= -9/4 on u in [1, 4] (its critical point u = 1/4 lies outside), so the constant profile has Q_1 < 0",
      vmax == sp.Rational(-9, 4) and all(not (1 <= c <= 4) for c in crit))
mp.mp.dps = 50
fm = lambda x: 1 - mp.mpf(3) / 4 * mp.sin(x) ** 2
q = lambda g: mp.quad(g, [0, mp.pi / 4, mp.pi / 2])
A1 = q(lambda x: mp.cos(x) ** 2 * mp.sqrt(fm(x)))                    # <= pi/4, since sqrt f <= 1
A2 = q(lambda x: 2 * mp.sin(x) ** 2 * mp.sqrt(fm(x)))                # >= pi/4, since sqrt f >= 1/2
A3 = q(lambda x: mp.sin(x) ** 2 / (2 * fm(x) ** mp.mpf(1.5)))        # > 0
Q0 = A1 - A2 - A3
print("\n(d) Q_0(sin t) = %s = %s - %s - %s (per unit s-length, R = 1)" % tuple(mp.nstr(v, 12) for v in (Q0, A1, A2, A3)))
check("(d3) sin t in m = 0: the bound's pieces hold (first <= pi/4 <= second, third > 0), so Q_0 < 0 without decimals",
      A1 <= mp.pi / 4 and A2 >= mp.pi / 4 and A3 > 0 and Q0 < 0)
Q1 = q(lambda x: (1 / (4 * fm(x)) - 1 / (2 * fm(x) ** 2) - 2) * mp.sqrt(fm(x)))
print("  Q_1(1) = %s; m = +-2: <e1,nu>, <e2,nu> are Neumann eigenfunctions at -2 (b1, b2)" % mp.nstr(Q1, 12))
check("(d4) the constant profile's form in m = 1 is negative", Q1 < 0)
print("  so the Neumann index is >= 5 exactly; the Dirichlet index is >= 2 exactly; closed index 7 (Morozov-Penskoi)")
print("  forces Dirichlet index = 2 and Neumann index = 5. Closed nullity 5, with Neumann nullity >= 4 (b3) and")
print("  Dirichlet nullity >= 1 (psi_X), forces Dirichlet nullity = 1 and Neumann nullity = 4.")

# (e) mutation arm
print("\n(e) mutation arm: |A|^2 dropped")
check("(e0) parent green: (c2)-(c4) passed", not any(x.startswith(("(c2)", "(c3)", "(c4)")) for x in fails))
totm, _ = spectra(dropA=True, show=False)
print("  mutated totals: Dirichlet %s, Neumann %s, closed %s" % (totm['D'], totm['N'], totm['K']))
check("(e1) the mutation breaks the closed totals (7, 5)", totm['K'] != [7, 5])

print("\n%s: %d failed" % ("ALL PASS" if not fails else "FAILURES", len(fails)))
