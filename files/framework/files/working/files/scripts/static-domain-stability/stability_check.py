#!/usr/bin/env python3
"""Checks for the static domain's stability: the linear perturbations of the static closed universe with a cosmological
constant and a perfect fluid, sector by sector, from the Einstein tensor of each perturbed metric.

  A  H-ISO: the Raychaudhuri equation, linearized about the static solution with continuity and delta p = c_s^2 delta rho,
     gives e'' = (1 + 3 c_s^2) e / R^2
  B  I-S: in longitudinal gauge with the zonal harmonics Q_n = sin((n+1) chi)/sin(chi), the 00 and theta-theta Einstein
     equations give Psi'' = [1 - c_s^2 (k^2 - 3)] Psi / R^2 with k^2 = n(n+2), at n = 0, 2, 3, 4
  C  H-ANISO: the diagonal Bianchi IX metric -dt^2 + sum a_i^2 sigma_i^2 (d sigma_1 = sigma_2 ^ sigma_3, cyclic), whose
     round case a_i = A is the S^3 of radius R = 2A, linearized about the static solution: the traceless modes obey
     q'' = -8 q / R^2 and the trace obeys the H-ISO equation
  D  the left-invariant traceless symmetric tensors on the round S^3 are transverse-traceless with rough Laplacian -6/R^2
  E  holding the radius fixed: with e = 0, the first-order Friedmann constraint and Raychaudhuri equation force
     delta rho = delta p = 0
Mutation arms, each of which must turn its claim red: delta p = 0 in place of c_s^2 delta rho (A), Phi = 2 Psi in place
of Phi = Psi (B), the coefficient 6/R^2 in place of 8/R^2 (C), sigma_1^2 + sigma_2^2 in place of a traceless tensor (D),
a homogeneous delta rho kept while e = 0 (E).
Units: G and the radius R kept symbolic; the Einstein tensors are evaluated at one point, since each geometry is homogeneous
or the harmonic is fixed.
"""
import sympy as sp

t, chi, th, ph, ps = sp.symbols('t chi theta phi psi', real=True)
R, G, A = sp.symbols('R G A', positive=True)
rho0, p0, cs2 = sp.symbols('rho0 p0 c_s2', real=True)
eps = sp.symbols('epsilon')
RHO_OF_R = sp.solve(sp.Eq(1 / R**2, 4 * sp.pi * G * (rho0 + p0)), rho0)[0]


def chop(ex):
    return sp.expand(ex).replace(lambda x: x.is_Float and abs(x) < 1e-30, lambda x: sp.Integer(0))


def christoffel(g, ginv, X):
    n = len(X)
    dg = [[[sp.diff(g[i, j], X[k]) for k in range(n)] for j in range(n)] for i in range(n)]
    return [[[sum(ginv[a, d] * (dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(n)) / 2
              for c in range(n)] for b in range(n)] for a in range(n)]


def ricci_at(Gam, X, pt):
    n = len(X)
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(b, n):
            val = sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c]) for a in range(n))
            val += sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n))
            Ric[b, c] = Ric[c, b] = val.subs(pt)
    return Ric


def claim_a(dp_factor=cs2):
    e = sp.Function('e')(t)
    drho = -3 * (rho0 + p0) * e
    edd = -sp.Rational(4, 3) * sp.pi * G * (drho + 3 * dp_factor * drho)
    coef = sp.simplify((edd / e).subs(rho0, RHO_OF_R)) * R**2
    return sp.simplify(coef - (1 + 3 * cs2)) == 0, sp.simplify(coef)


def claim_b(phi_factor=1):
    Psi = sp.Function('Psi')(t); dl = sp.Function('dl')(t)
    X = [t, chi, th, ph]
    out = []
    for n in (0, 2, 3, 4):
        Q = sp.sin((n + 1) * chi) / sp.sin(chi)
        f = 1 - 2 * eps * Psi * Q
        g = sp.diag(-(1 + 2 * eps * phi_factor * Psi * Q), R**2 * f, R**2 * f * sp.sin(chi)**2,
                    R**2 * f * sp.sin(chi)**2 * sp.sin(th)**2)
        ginv = sp.diag(*[1 / g[i, i] for i in range(4)])
        pt = {chi: sp.Rational(9, 10), th: sp.Rational(11, 10)}
        Ric = ricci_at(christoffel(g, ginv, X), X, pt)
        gP, giP = g.subs(pt), ginv.subs(pt)
        Rs = sum(giP[i, i] * Ric[i, i] for i in range(4))
        Gm = [giP[i, i] * (Ric[i, i] - Rs / 2 * gP[i, i]) for i in range(4)]
        Qv = sp.N(Q.subs(pt), 40)
        fo = lambda ex: chop(sp.N(sp.diff(ex, eps).subs(eps, 0), 40))
        e00 = fo(Gm[0]) + 8 * sp.pi * G * dl * Qv
        ett = fo(Gm[2]) - 8 * sp.pi * G * cs2 * dl * Qv
        psidd = sp.solve(ett.subs(dl, sp.solve(e00, dl)[0]), sp.diff(Psi, t, 2))[0]
        coef = chop(sp.expand(psidd / Psi * R**2))
        k2 = n * (n + 2)
        err = max(abs(sp.N((coef - (1 - cs2 * (k2 - 3))).subs(cs2, c))) for c in (sp.Rational(-2, 3), 0, sp.Rational(1, 5), 1, 3))
        out.append((n, k2, err))
    return all(e < 1e-12 for _, _, e in out), out


def bianchi_ix():
    a = [sp.Function(f'a{i}')(t) for i in (1, 2, 3)]
    X = [t, th, ph, ps]
    s = [sp.Matrix([0, -sp.sin(ps), sp.cos(ps) * sp.sin(th), 0]), sp.Matrix([0, sp.cos(ps), sp.sin(ps) * sp.sin(th), 0]),
         sp.Matrix([0, 0, sp.cos(th), 1])]
    g = sp.diag(-1, 0, 0, 0) + sum((a[i]**2 * s[i] * s[i].T for i in range(3)), sp.zeros(4))
    S = sp.Matrix([[s[i][j] for j in (1, 2, 3)] for i in range(3)])
    Xd = sp.simplify(S.inv())
    Xv = [sp.Matrix([0] + list(Xd[:, i])) for i in range(3)]
    ginv = sp.diag(-1, 0, 0, 0) + sum((Xv[i] * Xv[i].T / a[i]**2 for i in range(3)), sp.zeros(4))
    pt = {th: sp.Rational(6, 5), ps: sp.Rational(7, 10), ph: sp.Rational(1, 3)}
    Ric = ricci_at(christoffel(g, ginv, X), X, pt)
    gP, giP = g.subs(pt), ginv.subs(pt)
    Rs = sum(giP[i, j] * Ric[i, j] for i in range(4) for j in range(4))
    Gm = giP * (Ric - Rs / 2 * gP)
    def comp(v):
        v = v.subs(pt); w = gP * v
        return ((w.T * Gm * v)[0] / (w.T * v)[0]).evalf(40)
    b = [sp.Function(f'b{i}')(t) for i in (1, 2, 3)]; dr = sp.Function('dr')(t)
    lin = {a[i]: A * (1 + eps * b[i]) for i in range(3)}
    def first(ex):
        ex = ex.subs(lin).doit()
        return chop(sp.diff(ex, eps).subs(eps, 0)), chop(ex.subs(eps, 0))
    g00 = first(Gm[0, 0].evalf(40))
    gii = [first(comp(Xv[i])) for i in range(3)]
    cond = {rho0: sp.solve(sp.Eq(1 / (2 * A)**2, 4 * sp.pi * G * (rho0 + p0)), rho0)[0]}
    cont = {dr: -(rho0 + p0) * (b[0] + b[1] + b[2])}
    spat = [chop(sp.nsimplify(chop((gii[i][0] - 8 * sp.pi * G * cs2 * dr).subs(cont).subs(cond)), tolerance=1e-25, rational=True))
            for i in range(3)]
    background_ok = abs(sp.N(g00[1] * A**2 + sp.Rational(3, 4))) < 1e-25 and all(abs(sp.N(z[1] * A**2 + sp.Rational(1, 4))) < 1e-25 for z in gii)
    q = sp.Function('q')(t); e = sp.Function('e')(t)
    tl = sp.simplify((spat[0] - spat[1]).subs(b[0], b[1] + q).doit())
    qcoef = sp.simplify(sp.solve(tl, sp.diff(q, t, 2))[0].subs(A, R / 2) / q * R**2)
    tr = sp.simplify(spat[0].subs({b[0]: e, b[1]: e, b[2]: e}).doit())
    ecoef = sp.simplify(sp.solve(tr, sp.diff(e, t, 2))[0].subs(A, R / 2) / e * R**2)
    c00 = chop((g00[0] + 8 * sp.pi * G * dr).subs(cont).subs(cond).subs({b[0]: e, b[1]: e, b[2]: e}).doit())
    return background_ok, qcoef, ecoef, c00


def claim_c(bix, expected=-8):
    background_ok, qcoef, ecoef, c00 = bix
    ok = (background_ok and abs(sp.N(qcoef - expected)) < 1e-12 and sp.simplify(ecoef - (1 + 3 * cs2)) == 0
          and abs(sp.N(c00.subs(sp.Function('e')(t), 1))) < 1e-25)
    return ok


def claim_d(traceless=True):
    X = [th, ph, ps]
    s1 = sp.Matrix([-sp.sin(ps), sp.cos(ps) * sp.sin(th), 0]); s2 = sp.Matrix([sp.cos(ps), sp.sin(ps) * sp.sin(th), 0])
    s3 = sp.Matrix([0, sp.cos(th), 1])
    g = s1 * s1.T + s2 * s2.T + s3 * s3.T          # round S^3 of radius 2
    gi = sp.simplify(g.inv())
    Gam = christoffel(g, gi, X)
    pt = {th: sp.Rational(6, 5), ps: sp.Rational(7, 10), ph: sp.Rational(1, 3)}
    results = []
    tensors = (s1 * s1.T - s2 * s2.T, s1 * s2.T + s2 * s1.T) if traceless else (s1 * s1.T + s2 * s2.T,)
    for h in tensors:
        T = [[[sp.diff(h[a, b], X[c]) - sum(Gam[d][c][a] * h[d, b] + Gam[d][c][b] * h[a, d] for d in range(3))
               for b in range(3)] for a in range(3)] for c in range(3)]
        U = [[[[sp.diff(T[c][a][b], X[e]) - sum(Gam[d][e][c] * T[d][a][b] + Gam[d][e][a] * T[c][d][b] + Gam[d][e][b] * T[c][a][d]
                                                   for d in range(3)) for b in range(3)] for a in range(3)] for c in range(3)] for e in range(3)]
        tr = abs(sp.N(sum(gi[a, b] * h[a, b] for a in range(3) for b in range(3)).subs(pt), 30))
        div = max(abs(sp.N(sum(gi[c, a] * T[c][a][b] for c in range(3) for a in range(3)).subs(pt), 30)) for b in range(3))
        lap = sp.Matrix(3, 3, lambda a, b: sum(gi[e, c] * U[e][c][a][b] for e in range(3) for c in range(3))).subs(pt).evalf(30)
        hP = h.subs(pt).evalf(30)
        ratios = [lap[i, j] / hP[i, j] for i in range(3) for j in range(3) if abs(hP[i, j]) > 1e-6]
        eig_ok = all(abs(r - sp.Rational(-3, 2)) < 1e-20 for r in ratios)      # -6/R^2 at R = 2
        results.append(tr < 1e-25 and div < 1e-25 and eig_ok)
    return all(results)


def claim_e(mutant=None):
    """With e = 0, the first-order homogeneous Friedmann constraint, 0 = (8 pi G/3) drho + 2 e / R^2, and Raychaudhuri
    equation, e'' = -(4 pi G/3)(drho + 3 dp), admit only drho = dp = 0. A mutant pair is tested against both equations
    and against that unique solution."""
    drho, dp = sp.symbols('drho dp')
    e, edd = sp.Integer(0), sp.Integer(0)
    fried = sp.Rational(8, 3) * sp.pi * G * drho + 2 * e / R**2
    rayc = edd + sp.Rational(4, 3) * sp.pi * G * (drho + 3 * dp)
    sol = sp.solve([fried, rayc], [drho, dp], dict=True)
    unique_zero = sol == [{drho: 0, dp: 0}]
    pair = {drho: 0, dp: 0} if mutant is None else mutant(drho, dp)
    solves = sp.simplify(fried.subs(pair)) == 0 and sp.simplify(rayc.subs(pair)) == 0
    return unique_zero and solves and pair == {drho: 0, dp: 0}


def main():
    claims = 0
    ok_a, coef_a = claim_a()
    print("A  H-ISO: the Raychaudhuri equation about the static solution")
    print("   e''/e * R^2 = %s: %s" % (coef_a, "PASS" if ok_a else "FAIL")); claims += not ok_a
    ok_b, rows = claim_b()
    print("B  I-S: longitudinal gauge, zonal harmonics, Einstein tensor at a point")
    for n, k2, err in rows:
        print("   n = %d, k^2 = %2d: Psi''/Psi * R^2 = 1 - c_s^2 (k^2 - 3) to %s" % (n, k2, "1e-12" if err < 1e-12 else "%.1e" % float(err)))
    print("   %s" % ("PASS" if ok_b else "FAIL")); claims += not ok_b
    bix = bianchi_ix()
    ok_c = claim_c(bix)
    print("C  H-ANISO: diagonal Bianchi IX, Einstein tensor in Euler angles, projected on the dual frame")
    print("   background -3/R^2 and -1/R^2: %s; traceless q''/q * R^2 = %s; trace e''/e * R^2 = %s; 00 constraint zero: %s"
          % ("yes" if bix[0] else "no", sp.N(bix[1], 12), sp.simplify(bix[2]), "yes" if abs(sp.N(bix[3].subs(sp.Function('e')(t), 1))) < 1e-25 else "no"))
    print("   %s" % ("PASS" if ok_c else "FAIL")); claims += not ok_c
    ok_d = claim_d()
    print("D  left-invariant traceless symmetric tensors on the round S^3")
    print("   trace and divergence zero, rough Laplacian -6/R^2: %s" % ("PASS" if ok_d else "FAIL")); claims += not ok_d
    ok_e = claim_e()
    print("E  the radius held fixed")
    print("   e = 0 forces delta rho = delta p = 0 in the homogeneous sector: %s" % ("PASS" if ok_e else "FAIL")); claims += not ok_e
    arms = (("delta p = 0 in place of c_s^2 delta rho (A)", not claim_a(dp_factor=0)[0]),
            ("Phi = 2 Psi in place of Phi = Psi (B)", not claim_b(phi_factor=2)[0]),
            ("the coefficient 6/R^2 in place of 8/R^2 (C)", not claim_c(bix, expected=-6)),
            ("sigma_1^2 + sigma_2^2 in place of a traceless tensor (D)", not claim_d(traceless=False)),
            ("a homogeneous delta rho kept while e = 0 (E)", not claim_e(mutant=lambda drho, dp: {drho: sp.Symbol("d0", positive=True), dp: -sp.Symbol("d0", positive=True) / 3})))
    print("arms")
    for name, hit in arms:
        print("   arm: %-58s %s" % (name, "RED" if hit else "STAYED GREEN"))
    n_red = sum(hit for _, hit in arms)
    print("%d claims failed; %d/%d arms red" % (claims, n_red, len(arms)))
    return 0 if claims == 0 and n_red == len(arms) else 1


if __name__ == "__main__":
    raise SystemExit(main())
