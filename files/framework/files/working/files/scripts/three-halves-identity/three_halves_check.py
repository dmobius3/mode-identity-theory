#!/usr/bin/env python3
"""The checks behind the Temporal Budget Identity's note on the two 3/2's (temporal-budget.md, § II): the clock ratio and
the vacuum conversion's ratio, compared in general relativity's own register.

n is the spatial dimension, m the dimension of the carrier's cover, R the radius; MIT's case is (n, m) = (3, 2).

  C1   on S^m(R), the tilt sin(y/R) has -Delta sin(y/R) = (m/R^2) sin(y/R), from the warped metric
       dy^2 + cos^2(y/R) g, for m = 1 to 7 and for symbolic m
  C1b  independently, from an embedding: the restriction of a linear function to S^m(R) has -Delta x = (m/R^2) x
       (m = 2, 3), and a rotation of S^3 that moves a great S^2 is, along it, x_p times the unit normal
  C2   the scalar curvature of S^m(R) is m(m - 1)/R^2, from the metric, m = 2 to 5
  C3   the Ricci tensor of S^n(R) is ((n - 1)/R^2) g, the same in every direction, from the metric, n = 2 to 5
  C4   G(u, u) = C(n, 2) [(a'/(N a))^2 + k/a^2] for -N^2 dt^2 + a^2 (conformally flat slice of curvature k), from the
       metric, n = 2 to 6
  C5   on the time-symmetric vacuum slice S^n(R), Lambda_ref = G(u, u) = n(n - 1)/(2 R^2), from C4 at a' = 0
  C6   c = -d ln H / d ln a = n/2 on flat matter-only (Lambda = 0) slices, with the count's dilution derived from the
       divergence of rho u on the metric, not assumed; there tr K = div u = n H
  C7   c = Lambda_ref / Ric(nu, nu) at every n computed, and in closed form
  C8   the three conversion ratios (seed = tilt, cover's scalar curvature, normal Ricci curvature), their differences
       from c in closed form, and their zero sets
  C9   where the three carries of the seed agree pairwise, and (3, 2) as the only member where all three do
  C10  the provenance of the factors, on the constraint with its coefficient b and its degree q in K left free,
       E(b, q) = b tr Ric + e_q(K): g'' = b n at every degree, and c = n/q at every coefficient and prefactor; general
       relativity's E is b = 1/2, q = 2, where E is the metric's G(u, u) of C4 and C5
  C11  at (3, 2), from the Riemann tensor of S^3(R): the three coordinate planes at a point each have sectional curvature
       1/R^2, Ric(nu, nu) = 2/R^2 and tr Ric = 6/R^2; and C(n, 2) = n only at n = 3

The constraint is the scalar Gauss relation of a slice, G(u, u) = (1/2)[tr Ric + (tr K)^2 - |K|^2] = Sigma_{i<j}
[Sec(e_i, e_j) + k_i k_j], with kappa rho + Lambda on its right. For a totally geodesic cover the normal bundle is flat,
spanned by parallel normal fields, so the normal Laplacian on a tilt f nu is (Delta f) nu, and C1 and C1b compute the tilt
eigenvalue of definition D3. Each check carries a control that must come out the other way, and prints the reason it
does. Every quantity is exact. Run: python3 -I -B three_halves_check.py
"""
import itertools
import sys
from math import comb

import sympy as sp

R = sp.symbols("R", positive=True)
y = sp.symbols("y", real=True)
n_, m_ = sp.symbols("n m", positive=True, integer=True)


def z(expr):
    """Exactly zero after simplification."""
    return sp.simplify(expr) == 0


# ------------------------------------------------------------------ curvature of a diagonal metric in coordinates
def christoffel(g, X):
    """Gamma^l_{mu nu} of a diagonal metric g in coordinates X."""
    assert g.is_diagonal()
    D = len(X)
    ginv = [1 / g[i, i] for i in range(D)]
    return [[[sp.Rational(1, 2) * ginv[l] * (sp.diff(g[l, nu], X[mu]) + sp.diff(g[l, mu], X[nu]) - sp.diff(g[mu, nu], X[l]))
              for nu in range(D)] for mu in range(D)] for l in range(D)]


def ricci(G, X, mu, nu):
    """R_{mu nu} = d_l Gamma^l_{mu nu} - d_nu Gamma^l_{mu l} + Gamma^l_{l s} Gamma^s_{mu nu} - Gamma^l_{nu s} Gamma^s_{mu l}."""
    D = len(X)
    out = 0
    for l in range(D):
        out += sp.diff(G[l][mu][nu], X[l]) - sp.diff(G[l][mu][l], X[nu])
        for s in range(D):
            out += G[l][l][s] * G[s][mu][nu] - G[l][nu][s] * G[s][mu][l]
    return out


def riemann_up(G, X, r, s, mu, nu):
    """R^r_{s mu nu}, so that (R(e_mu, e_nu) e_s)^r = R^r_{s mu nu} and its r = mu contraction is R_{s nu}."""
    D = len(X)
    out = sp.diff(G[r][nu][s], X[mu]) - sp.diff(G[r][mu][s], X[nu])
    for l in range(D):
        out += G[r][mu][l] * G[l][nu][s] - G[r][nu][l] * G[l][mu][s]
    return out


def round_slice(dim, radius, sign=1):
    """The round S^dim(radius) (sign = -1: hyperbolic space) in stereographic coordinates, conformal factor 1 at 0."""
    xs = sp.symbols(f"x1:{dim + 1}", real=True)
    conf = 1 / (1 + sign * sum(x ** 2 for x in xs) / (4 * radius ** 2)) ** 2
    return sp.diag(*[conf] * dim), xs


def ricci_at_origin(g, xs):
    G = christoffel(g, xs)
    origin = {x: 0 for x in xs}
    D = len(xs)
    return sp.Matrix(D, D, lambda i, j: sp.simplify(ricci(G, xs, i, j).subs(origin)))


# ------------------------------------------------------------------ C1: the tilt on the warped metric
def tilt_eigenvalue_explicit(m, radius):
    """-Delta f / f for f = sin(y/radius) on dy^2 + cos^2(y/radius) g_{S^(m-1)(radius)}, from the metric's Christoffels,
    at the origin of the stereographic chart on S^(m-1) (f depends on y alone)."""
    J = sp.cos(y / radius)
    f = sp.sin(y / radius)
    xs = sp.symbols(f"w1:{m}", real=True)
    conf = 1 / (1 + sum(x ** 2 for x in xs) / (4 * radius ** 2)) ** 2
    X = (y,) + tuple(xs)
    g = sp.diag(1, *[J ** 2 * conf] * (m - 1))
    G = christoffel(g, X)
    D = len(X)
    lap = 0
    for a in range(D):
        for b in range(D):
            if g[a, b] == 0:
                continue
            term = sp.diff(f, X[a], X[b]) - sum(G[c][a][b] * sp.diff(f, X[c]) for c in range(D))
            lap += (1 / g[a, b]) * term
    lap = lap.subs({x: 0 for x in xs})
    return sp.simplify(-lap / f)


def tilt_eigenvalue_symbolic(weight_power):
    """-Delta f / f with the warped metric's volume density J^weight_power: (1/J^p)(J^p f')'."""
    J = sp.cos(y / R)
    f = sp.sin(y / R)
    lap = sp.diff(J ** weight_power * sp.diff(f, y), y) / J ** weight_power
    return sp.simplify(-lap / f)


# ------------------------------------------------------------------ C1b: the Laplacian from an embedding
def embedded_laplacian(Xvec, coords, func):
    """Laplace-Beltrami of func (a function of the coordinates) on the induced metric of the embedding Xvec."""
    D = len(coords)
    Jm = sp.Matrix([[sp.diff(Xi, c) for c in coords] for Xi in Xvec])
    g = sp.simplify(Jm.T * Jm)
    G = christoffel(g, coords)
    lap = 0
    for a in range(D):
        term = sp.diff(func, coords[a], coords[a]) - sum(G[c][a][a] * sp.diff(func, coords[c]) for c in range(D))
        lap += term / g[a, a]
    return sp.simplify(lap)


def sphere_embedding(m):
    if m == 2:
        th, ph = sp.symbols("theta phi", real=True)
        return [R * sp.cos(th) * sp.cos(ph), R * sp.cos(th) * sp.sin(ph), R * sp.sin(th)], (th, ph)
    if m == 3:
        ch, th, ph = sp.symbols("chi theta phi", real=True)
        return ([R * sp.cos(ch) * sp.cos(th) * sp.cos(ph), R * sp.cos(ch) * sp.cos(th) * sp.sin(ph),
                 R * sp.cos(ch) * sp.sin(th), R * sp.sin(ch)], (ch, th, ph))
    raise ValueError(m)


# ------------------------------------------------------------------ C4: G(u, u) for the slicing
def G_uu(n):
    t, k = sp.symbols("t k", real=True)
    xs = sp.symbols(f"x1:{n + 1}", real=True)
    N = sp.Function("N", positive=True)(t)
    a = sp.Function("a", positive=True)(t)
    conf = 1 / (1 + k * sum(x ** 2 for x in xs) / 4) ** 2
    X = (t,) + tuple(xs)
    g = sp.diag(-N ** 2, *[a ** 2 * conf] * n)
    G = christoffel(g, X)
    origin = {x: 0 for x in xs}
    ric = [sp.simplify(ricci(G, X, i, i).subs(origin).doit()) for i in range(n + 1)]
    ginv0 = [(1 / g[i, i]).subs(origin) for i in range(n + 1)]
    scal = sp.simplify(sum(ginv0[i] * ric[i] for i in range(n + 1)))
    G00 = sp.simplify(ric[0] + sp.Rational(1, 2) * scal * N ** 2)       # g_00 = -N^2
    return sp.simplify(G00 / N ** 2), sp.simplify(ric[0] / N ** 2), (t, k, N, a)


# ------------------------------------------------------------------ C6: the count's dilution, from the metric
def expansion_of_u(n):
    """tr K = div u for u = (1/N) d_t on -N^2 dt^2 + a^2 delta (n flat dimensions), over H = a'/(N a)."""
    t = sp.symbols("t", real=True)
    N = sp.Function("N", positive=True)(t)
    a = sp.Function("a", positive=True)(t)
    sqrt_g = sp.sqrt(-sp.diag(-N ** 2, *[a ** 2] * n).det())
    div_u = sp.diff(sqrt_g * (1 / N), t) / sqrt_g
    return sp.simplify(div_u / (sp.diff(a, t) / (N * a)))


def dilution_from_count(n):
    """e in rho ~ a^(-e), from div(rho u) = 0 on -N^2 dt^2 + a^2 delta (n flat dimensions), u = (1/N) d_t."""
    t = sp.symbols("t", real=True)
    N = sp.Function("N", positive=True)(t)
    a = sp.Function("a", positive=True)(t)
    rho = sp.Function("rho", positive=True)(t)
    sqrt_g = sp.sqrt(-sp.diag(-N ** 2, *[a ** 2] * n).det()) if isinstance(n, int) else N * a ** n
    div = sp.diff(sqrt_g * rho * (1 / N), t) / sqrt_g
    rho_dot = sp.solve(sp.Eq(div, 0), sp.diff(rho, t))[0]
    return sp.simplify(-(a / sp.diff(a, t)) * rho_dot / rho)


def dilution_from_stress(n, w):
    """e in rho ~ a^(-e), from div T^{mu 0} = 0 for a perfect fluid with p = w rho on the same metric."""
    t = sp.symbols("t", real=True)
    xs = sp.symbols(f"x1:{n + 1}", real=True)
    N = sp.Function("N", positive=True)(t)
    a = sp.Function("a", positive=True)(t)
    rho = sp.Function("rho", positive=True)(t)
    p = w * rho
    X = (t,) + tuple(xs)
    g = sp.diag(-N ** 2, *[a ** 2] * n)
    ginv = sp.diag(*[1 / g[i, i] for i in range(n + 1)])
    u = [1 / N] + [0] * n
    T = sp.Matrix(n + 1, n + 1, lambda i, j: (rho + p) * u[i] * u[j] + p * ginv[i, j])
    G = christoffel(g, X)
    D = n + 1
    div0 = sum(sp.diff(T[mu, 0], X[mu]) for mu in range(D))
    div0 += sum(G[mu][mu][l] * T[l, 0] for mu in range(D) for l in range(D))
    div0 += sum(G[0][mu][l] * T[mu, l] for mu in range(D) for l in range(D))
    rho_dot = sp.solve(sp.Eq(sp.simplify(div0), 0), sp.diff(rho, t))[0]
    return sp.simplify(-(a / sp.diff(a, t)) * rho_dot / rho)


def clock_ratio(prefactor_H2, e, k_term=0):
    """c = -d ln H / d ln a for prefactor (H^2 + k/a^2) = kappa M a^(-e)."""
    A, M, kap = sp.symbols("A M kappa", positive=True)
    H = sp.sqrt(kap * M / A ** e / prefactor_H2 - k_term / A ** 2)
    return sp.simplify(-A * sp.diff(sp.log(H), A)), A


def main():
    checks, controls = [], []

    # C1
    explicit = {m: tilt_eigenvalue_explicit(m, R) for m in range(1, 8)}
    sym = tilt_eigenvalue_symbolic(m_ - 1)
    ok = all(z(explicit[m] - m / R ** 2) for m in explicit) and z(sym - m_ / R ** 2)
    checks.append(("C1 the tilt sin(y/R) on S^m(R) has eigenvalue m/R^2, m = 1 to 7 and symbolic m", ok,
                   "m = 1..7: %s; symbolic: %s" % (", ".join(str(explicit[m]) for m in explicit), sym)))
    wrong = tilt_eigenvalue_symbolic(m_)
    controls.append(("C1.i the wrong zonal weight J^m", not z(wrong - m_ / R ** 2), "gives %s" % wrong))
    r_s = sp.symbols("r", positive=True)
    small = tilt_eigenvalue_explicit(2, r_s)
    controls.append(("C1.ii a small sphere of radius r < R, at m = 2", not z(small - 2 / R ** 2),
                     "its eigenvalue is %s, set by its own radius" % small))

    # C1b
    rows = []
    ok = True
    for m in (2, 3):
        Xv, coords = sphere_embedding(m)
        for idx, xk in enumerate(Xv):
            lap = embedded_laplacian(Xv, coords, xk)
            good = z(-lap - (m / R ** 2) * xk)
            ok = ok and good
            rows.append("m=%d x%d %s" % (m, idx + 1, "ok" if good else "NO"))
    # the rotation in the (e3, e4) plane of R^4, along the great S^2 = S^3 n {x4 = 0}
    x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4", real=True)
    V = sp.Matrix([0, 0, -x4, x3])
    on_cover = V.subs(x4, 0)
    normal = sp.Matrix([0, 0, 0, 1])
    tangential = on_cover - (on_cover.dot(normal)) * normal
    rot_ok = z(on_cover.dot(normal) - x3) and all(z(e) for e in tangential)
    ok = ok and rot_ok
    checks.append(("C1b from an embedding: -Delta x = (m/R^2) x for linear x (m = 2, 3); the tilting rotation is x3 nu", ok,
                   "%s; rotation along the cover: normal part %s, tangential part %s" % (
                       ", ".join(rows), on_cover.dot(normal), list(tangential))))
    Xv, coords = sphere_embedding(2)
    sq = embedded_laplacian(Xv, coords, Xv[2] ** 2)
    controls.append(("C1b x3^2 on S^2(R)", not z(-sq - (2 / R ** 2) * Xv[2] ** 2),
                     "-Delta x3^2 - (2/R^2) x3^2 = %s, not zero" % sp.simplify(-sq - (2 / R ** 2) * Xv[2] ** 2)))

    # C2
    scal_cover = {}
    for m in range(2, 6):
        g, xs = round_slice(m, R)
        ric = ricci_at_origin(g, xs)
        scal_cover[m] = sp.simplify(ric.trace())                    # g = delta at the origin
    ok = all(z(scal_cover[m] - m * (m - 1) / R ** 2) for m in scal_cover)
    checks.append(("C2 the scalar curvature of S^m(R) is m(m - 1)/R^2, m = 2 to 5", ok,
                   ", ".join("m=%d: %s" % (m, scal_cover[m]) for m in scal_cover)))
    g, xs = round_slice(3, R, sign=-1)
    hyp = sp.simplify(ricci_at_origin(g, xs).trace())
    controls.append(("C2 the hyperbolic metric of the same radius", not z(hyp - 6 / R ** 2), "gives %s at m = 3" % hyp))

    # C3
    ric_n, tr_ric_n = {}, {}
    ok = True
    for n in range(2, 6):
        g, xs = round_slice(n, R)
        ric = ricci_at_origin(g, xs)
        r0 = ric[0, 0]
        tr_ric_n[n] = sp.simplify(ric.trace())                      # g = delta at the origin
        ok = ok and all(z(ric[i, j] - (r0 if i == j else 0)) for i in range(n) for j in range(n)) and z(r0 - (n - 1) / R ** 2)
        ric_n[n] = r0
    checks.append(("C3 the Ricci tensor of S^n(R) is ((n - 1)/R^2) g, n = 2 to 5", ok,
                   ", ".join("n=%d: %s" % (n, ric_n[n]) for n in ric_n)))
    xs = sp.symbols("x1:4", real=True)
    conf2 = 1 / (1 + (xs[0] ** 2 + xs[1] ** 2) / (4 * R ** 2)) ** 2
    prod = ricci_at_origin(sp.diag(conf2, conf2, 1), xs)
    controls.append(("C3 the product S^2(R) x line", not all(z(prod[i, i] - prod[0, 0]) for i in range(3)),
                     "Ricci eigenvalues %s, not the same in every direction" % [prod[i, i] for i in range(3)]))

    # C4, C5
    lam_ref, G_rows = {}, []
    ok4, ok5 = True, True
    ric_uu_bad = True
    G_cache = {n: G_uu(n) for n in range(2, 7)}
    for n in range(2, 7):
        val, ric_uu, (t, k, N, a) = G_cache[n]
        H = sp.diff(a, t) / (N * a)
        ok4 = ok4 and z(val - sp.Rational(comb(n, 2)) * (H ** 2 + k / a ** 2))
        lam_ref[n] = sp.simplify(val.subs(sp.Derivative(a, t), 0).subs({a: 1, N: 1, k: 1 / R ** 2}))
        ok5 = ok5 and z(lam_ref[n] - sp.Rational(n * (n - 1), 2) / R ** 2)
        ric_uu_bad = ric_uu_bad and not z(ric_uu - sp.Rational(comb(n, 2)) * (H ** 2 + k / a ** 2))
        G_rows.append("n=%d: C(n,2) = %d" % (n, comb(n, 2)))
    checks.append(("C4 G(u, u) = C(n, 2) [(a'/(N a))^2 + k/a^2], n = 2 to 6", ok4, "; ".join(G_rows)))
    val3, ric_uu3, (t, k, N, a) = G_cache[3]
    controls.append(("C4 Ric(u, u) in place of G(u, u)", ric_uu_bad,
                     "Ric(u, u) at n = 3 is %s, which carries a''" % sp.simplify(ric_uu3)))
    checks.append(("C5 Lambda_ref = n(n - 1)/(2 R^2) on the time-symmetric vacuum slice, n = 2 to 6", ok5,
                   ", ".join("n=%d: %s" % (n, lam_ref[n]) for n in lam_ref)))
    no_half = {n: sp.simplify(2 * lam_ref[n]) for n in (3, 4)}         # the scalar curvature, the 1/2 dropped
    controls.append(("C5 the 1/2 dropped (Lambda read as the slice's scalar curvature)",
                     all(not z(no_half[n] - sp.Rational(n * (n - 1), 2) / R ** 2) for n in no_half),
                     "gives %s at n = 3, 4: twice the reference" % list(no_half.values())))

    # C6
    c_n, rows = {}, []
    ok = True
    for n in range(2, 7):
        e_count = dilution_from_count(n)
        e_stress = dilution_from_stress(n, 0)
        trK = expansion_of_u(n)
        val, _, (t, k, N, a) = G_cache[n]
        H = sp.diff(a, t) / (N * a)
        pref = sp.simplify(val.subs(k, 0) / H ** 2)                    # G(u, u) on flat slices, over H^2
        c, A = clock_ratio(pref, e_count)
        c_n[n] = c
        ok = ok and z(e_count - n) and z(e_stress - n) and z(c - sp.Rational(n, 2)) and z(trK - n)
        rows.append("n=%d: tr K = %s H, rho ~ a^-%s, c = %s" % (n, trK, e_count, c))
    e_sym = dilution_from_count(n_)
    ok = ok and z(e_sym - n_)
    checks.append(("C6 c = n/2 on flat matter-only (Lambda = 0) slices, the count's dilution from div(rho u) = 0; tr K = n H", ok,
                   "; ".join(rows) + "; symbolic n: rho ~ a^-%s" % e_sym))
    val3, _, (t, k, N, a) = G_cache[3]
    H = sp.diff(a, t) / (N * a)
    pref3 = sp.simplify(val3.subs(k, 0) / H ** 2)
    k1 = sp.symbols("k1", positive=True)
    c_curved, A = clock_ratio(pref3, 3, k_term=k1)
    controls.append(("C6.i curved slices, k != 0, n = 3", not z(sp.diff(c_curved, A)),
                     "-d ln H/d ln a = %s, which varies with a" % sp.simplify(c_curved)))
    rad = {n: clock_ratio(sp.Rational(comb(n, 2)), dilution_from_stress(n, sp.Rational(1, n)))[0] for n in (3, 4)}
    controls.append(("C6.ii radiation, p = rho/n, in place of a pressureless count",
                     all(not z(rad[n] - sp.Rational(n, 2)) and z(rad[n] - sp.Rational(n + 1, 2)) for n in rad),
                     "gives %s at n = 3, 4, that is (n + 1)/2" % list(rad.values())))

    # C7
    ratio = {n: sp.simplify(lam_ref[n] / ric_n[n]) for n in ric_n}
    ok = all(z(ratio[n] - c_n[n]) for n in ratio)
    closed = sp.simplify((n_ * (n_ - 1) / (2 * R ** 2)) / ((n_ - 1) / R ** 2))
    ok = ok and z(closed - n_ / 2)
    checks.append(("C7 c = Lambda_ref / Ric(nu, nu) at every n computed, and in closed form", ok,
                   ", ".join("n=%d: %s = %s" % (n, ratio[n], c_n[n]) for n in ratio) + "; closed form %s" % closed))
    over_scal = {n: sp.simplify(lam_ref[n] / (n * ric_n[n])) for n in (3, 4, 5)}
    controls.append(("C7 over the slice's scalar curvature instead", all(not z(over_scal[n] - c_n[n]) for n in over_scal),
                     "the ratio is %s at n = 3, 4, 5" % list(over_scal.values())))

    # C8
    tilt = lambda m: m / R ** 2
    members = [(n, m) for n in range(3, 6) for m in range(2, n)]
    g_vals = {(n, m): (sp.simplify(lam_ref[n] / explicit[m]), sp.simplify(lam_ref[n] / scal_cover[m]),
                       sp.simplify(lam_ref[n] / ric_n[n])) for (n, m) in members}
    g_closed = n_ * (n_ - 1) / (2 * m_)
    gp_closed = n_ * (n_ - 1) / (2 * m_ * (m_ - 1))
    gpp_closed = (n_ * (n_ - 1) / 2) / (n_ - 1)
    c_closed = n_ / 2
    agree = all(z(g_vals[(n, m)][0] - g_closed.subs({n_: n, m_: m})) and z(g_vals[(n, m)][1] - gp_closed.subs({n_: n, m_: m}))
                and z(g_vals[(n, m)][2] - gpp_closed.subs({n_: n, m_: m})) for (n, m) in members)
    d_g = sp.factor(g_closed - c_closed)
    d_gp = sp.factor(gp_closed - c_closed)
    d_gpp = sp.simplify(gpp_closed - c_closed)
    zero_g = sp.solve(sp.Eq(g_closed, c_closed), m_)
    zero_gp = sp.solve(sp.Eq(gp_closed, c_closed), n_)
    bound = 200
    curve = [(mm * mm - mm + 1, mm) for mm in range(2, bound) if mm * mm - mm + 1 < bound]
    curve_check = all(z(gp_closed.subs({n_: nn, m_: mm}) - c_closed.subs(n_, nn)) for nn, mm in curve)
    on_surface = sp.factor((gp_closed - c_closed).subs(m_, 2))
    on_hyper = sp.factor((gp_closed - c_closed).subs(m_, n_ - 1))
    surf_zeros = [s for s in sp.solve(on_surface, n_) if s >= 3]
    hyper_zeros = [s for s in sp.solve(on_hyper, n_) if s >= 3]
    g_surface = sp.factor(g_closed.subs(m_, 2))                      # the tilt carry with the carrier kept 2-dimensional
    g_surface_zeros = [s for s in sp.solve(sp.Eq(g_surface, c_closed), n_) if s >= 3]
    g_hyper = sp.simplify(g_closed.subs(m_, n_ - 1))
    ok = (agree and d_g == sp.factor(-n_ * (m_ - n_ + 1) / (2 * m_)) and d_gpp == 0 and zero_g == [n_ - 1]
          and zero_gp == [m_ ** 2 - m_ + 1] and curve_check and surf_zeros == [3] and hyper_zeros == [3]
          and g_surface_zeros == [3] and z(g_hyper - c_closed))
    checks.append(("C8 the three ratios against c: g = c on m = n - 1, g'' = c everywhere, g' = c on n = m^2 - m + 1", ok,
                   "computed (n, m) in %s agree with the closed forms g = %s, g' = %s, g'' = %s; g - c = %s; "
                   "g' - c = %s; g'' - c = %s; g = c iff m = %s; on m = 2, g = %s, equal to c at n = %s; on m = n - 1, "
                   "g = %s; g' = c iff n = %s, members below %d: %s; g' - c on m = 2: %s, zero at n = %s; "
                   "on m = n - 1: %s, zero at n = %s" % (members, g_closed, gp_closed, sp.simplify(gpp_closed), d_g, d_gp,
                                                          d_gpp, zero_g, g_surface, g_surface_zeros, g_hyper, zero_gp,
                                                          bound, curve, on_surface, surf_zeros, on_hyper, hyper_zeros)))
    off = {n: sp.simplify(g_closed.subs({n_: n, m_: n - 2}) - c_closed.subs(n_, n)) for n in (4, 5, 6)}
    controls.append(("C8.i g at m = n - 2", all(not z(off[n]) for n in off), "g - c = %s at n = 4, 5, 6" % list(off.values())))
    gp_off = sp.simplify(gp_closed.subs({n_: 8, m_: 3}) - c_closed.subs(n_, 8))
    controls.append(("C8.ii g' at (8, 3), off the curve n - 1 = m(m - 1)", not z(gp_off), "g' - c = %s there" % gp_off))

    # C9
    carries = {"tilt": m_, "cover": m_ * (m_ - 1), "normal Ricci": n_ - 1}   # in units of 1/R^2
    tilt_ric = sp.solve(sp.Eq(carries["tilt"], carries["normal Ricci"]), m_)
    tilt_cov = [s for s in sp.solve(sp.Eq(carries["tilt"], carries["cover"]), m_) if s != 0]
    cov_ric = sp.solve(sp.Eq(carries["cover"], carries["normal Ricci"]), n_)
    common_alg = sp.solve([sp.Eq(m_, 2), sp.Eq(m_, n_ - 1)], [n_, m_], dict=True)
    common_enum = [(n, m) for n in range(3, bound) for m in range(2, n) if m == n - 1 and m == m * (m - 1) and m * (m - 1) == n - 1]
    ok = tilt_ric == [n_ - 1] and tilt_cov == [2] and cov_ric == [m_ ** 2 - m_ + 1] and common_alg == [{n_: 3, m_: 2}] \
        and common_enum == [(3, 2)] and z(carries["cover"].subs(m_, 2) - carries["normal Ricci"].subs(n_, 3))
    checks.append(("C9 the carries agree pairwise on m = n - 1, m = 2, n - 1 = m(m - 1); all three only at (3, 2)", ok,
                   "tilt = normal Ricci iff m = %s; tilt = cover iff m = %s; cover = normal Ricci iff n = %s; "
                   "all three, by algebra: %s; by enumeration below %d: %s" % (tilt_ric, tilt_cov, cov_ric, common_alg, bound,
                                                                            common_enum)))
    at54 = {k_: v.subs({n_: 5, m_: 4}) for k_, v in carries.items()}
    controls.append(("C9 (5, 4), on the hypersurface branch beyond (3, 2)", len(set(at54.values())) > 1,
                     "the carries are %s there" % at54))

    # C10: one constraint with its coefficient b and its degree q in K left free,
    #   E(b, q) = b tr Ric + e_q(K),   e_q the degree-q elementary symmetric function of K's eigenvalues;
    #   general relativity's E is b = 1/2, q = 2, since e_2(K) = (1/2)[(tr K)^2 - |K|^2].
    b, q, P = sp.symbols("b q P", positive=True)
    Hs = sp.symbols("H", positive=True)

    def e_sym(eigs, deg):
        return sum(sp.prod(sub) for sub in itertools.combinations(eigs, deg))

    def static_ratio(n, hh, deg):
        """g'' from E on the substrate: K = 0, vacuum, so Lambda_ref = E; tr Ric from C3's metric."""
        lam = hh * tr_ric_n[n] + e_sym([0] * n, deg)
        return sp.simplify(lam / ric_n[n]), lam

    def effective_ratio(n, hh, deg):
        """c from E on flat slices: their Ricci tensor is 0, K = H g has n equal eigenvalues, E = kappa rho with the
        count's dilution of C6."""
        lhs = hh * 0 + e_sym([Hs] * n, deg)
        prefactor = sp.simplify(lhs / Hs ** deg)
        return clock_ratio_degree(prefactor, deg, dilution_from_count(n))[0], prefactor

    rows = []
    ok = True
    for n in range(3, 6):
        degs = tuple(range(1, min(4, n) + 1))                                         # e_q of n eigenvalues vanishes for q > n
        stat = [static_ratio(n, b, deg)[0] for deg in degs]
        eff = [effective_ratio(n, b, deg) for deg in degs]
        ok = ok and all(z(s - b * n) for s in stat)                                   # g'' = b n at every degree
        ok = ok and all(z(c - sp.Rational(n, deg)) and not c.has(b) and z(pf - comb(n, deg))
                        for (c, pf), deg in zip(eff, degs))                             # c = n/q, no b
        val, _, (t, k, N, a) = G_cache[n]                                             # ties to the metric at b = 1/2, q = 2
        H = sp.diff(a, t) / (N * a)
        ok = ok and z(eff[1][1] - sp.simplify(val.subs(k, 0) / H ** 2))
        ok = ok and z(static_ratio(n, sp.Rational(1, 2), 2)[1] - lam_ref[n])
        rows.append("n=%d: g'' = %s at q = %s; c = %s" % (n, stat[0], list(degs), [c for c, _ in eff]))
    c_sym, A = clock_ratio_degree(P, q, n_)
    ok = ok and z(c_sym - n_ / q) and not c_sym.has(P) and not c_sym.has(b)
    checks.append(("C10 with E's coefficient b, g'' = b n at any degree; with E's degree q in K, c = n/q at any coefficient", ok,
                   "; ".join(rows) + "; symbolic q, any prefactor P: c = %s; at b = 1/2 and q = 2, E is the metric's "
                   "G(u, u) of C4 and C5, and both ratios are n/2" % c_sym))
    b1 = {n: (static_ratio(n, 1, 2)[0], effective_ratio(n, 1, 2)[0]) for n in (3, 4)}
    controls.append(("C10.i b = 1 in place of 1/2",
                     all(not z(b1[n][0] - sp.Rational(n, 2)) and z(b1[n][1] - sp.Rational(n, 2)) for n in b1),
                     "g'' = %s leaves c, while c stays %s, at n = 3, 4" % ([b1[n][0] for n in b1], [b1[n][1] for n in b1])))
    q3 = {n: (effective_ratio(n, sp.Rational(1, 2), 3)[0], static_ratio(n, sp.Rational(1, 2), 3)[0]) for n in (3, 4)}
    controls.append(("C10.ii q = 3 in place of 2",
                     all(not z(q3[n][0] - q3[n][1]) and z(q3[n][1] - sp.Rational(n, 2)) for n in q3),
                     "c = %s leaves g'', while g'' stays %s, at n = 3, 4" % ([q3[n][0] for n in q3], [q3[n][1] for n in q3])))

    # C11
    g, xs = round_slice(3, R)
    G = christoffel(g, xs)
    origin = {x: 0 for x in xs}
    sec = {}
    for i, j in ((0, 1), (0, 2), (1, 2)):
        Rijij = sum(g[i, l] * riemann_up(G, xs, l, j, i, j) for l in range(3))
        sec[(i + 1, j + 1)] = sp.simplify((Rijij / (g[i, i] * g[j, j] - g[i, j] ** 2)).subs(origin))
    ric3 = ricci_at_origin(g, xs)
    nu = 2                                                    # the normal e3 of the plane (e1, e2)
    ric_nu = sp.simplify(ric3[nu, nu])
    from_planes = sec[(1, 3)] + sec[(2, 3)]
    tr = sp.simplify(ric3.trace())
    cn_eq_n = [s for s in sp.solve(sp.Eq(n_ * (n_ - 1) / 2, n_), n_)]
    ok = all(z(v - 1 / R ** 2) for v in sec.values()) and z(ric_nu - 2 / R ** 2) and z(from_planes - ric_nu) \
        and z(tr - 6 / R ** 2) and cn_eq_n == [3]
    checks.append(("C11 at (3, 2): three planes of curvature 1/R^2, Ric(nu, nu) = 2/R^2, tr Ric = 6/R^2; C(n, 2) = n only at 3", ok,
                   "sectional curvatures %s; Ric(nu, nu) = %s = Sec(e1, nu) + Sec(e2, nu); tr Ric = %s; C(n, 2) = n at n = %s"
                   % (sec, ric_nu, tr, cn_eq_n)))
    controls.append(("C11 C(n, 2) against n at n = 4", comb(4, 2) != 4, "C(4, 2) = %d" % comb(4, 2)))

    for name, ok, info in checks:
        print("%s  %s\n      %s" % ("PASS" if ok else "FAIL", name, info))
    for name, came_out, why in controls:
        print("control  %-72s %s\n         %s" % (name, "as required" if came_out else "DID NOT", why))
    ok = all(ck[1] for ck in checks) and all(ct[1] for ct in controls)
    print("%d/%d checks pass; %d/%d controls as required" % (
        sum(ck[1] for ck in checks), len(checks), sum(ct[1] for ct in controls), len(controls)))
    return 0 if ok else 1


def clock_ratio_degree(prefactor, q, e):
    """c = -d ln H / d ln a for prefactor H^q = kappa M a^(-e): a constraint of degree q in K on flat slices."""
    A, M, kap = sp.symbols("A M kappa", positive=True)
    H = (kap * M / A ** e / prefactor) ** (1 / sp.sympify(q))
    return sp.simplify(-A * sp.diff(sp.log(H), A)), A


if __name__ == "__main__":
    sys.exit(main())
