#!/usr/bin/env python3
"""Identities behind projective-carrier.md §II (the untwisted 2/R² mode), §§III-IV (Theorem 2, the tubes' Gauss-Bonnet
balance) and §§VI, VIII (Lemma 4 and its comparison with the arch, the 3/R² fence).

Checks (exit 1 on any failure):
  I1  on a generic surface in S³(R), sum_i x_i² = R² and sum_i |∇x_i|² = 2 (Theorem 2, step 3), at random points
  I2  in band coordinates ds² = dy² + cos²(y/R) dw², −Δ sin(y/R) = (2/R²) sin(y/R), so J sin(y/R) = 0
  I3  first eigenvalue Proposition 4.2's trivialization carries sin(y/R) to x_p/R on the lune: +sin on y < πR/2, −sin on y > πR/2
  I4  the rotation field in the (p, ν) plane is tangent to S³, antisymmetric (Killing), and equals x_p ν on the great S²
  I5  a great S² in Sⁿ(R), n = 3..8: the tilt's eigenvalue 2/R² equals the Jacobi curvature term (the sum over the two
      tangent directions, from the curvature tensor in a random frame) for every n; the ambient Ricci floor (n − 1)/R²
      meets it only at n = 3
  I6  the linear coordinate on S³(R) has eigenvalue 3/R²; a sphere's first level n/R² meets n(n−1)/(2R²) only at n = 3
  I7  the tube dt² + cos²(t/R) dσ², |t| ≤ W, core πR: edge geodesic curvature tan(W/R)/R, and its integral over the
      edge, of length 2πR cos(W/R), equals the area over R² (Gauss-Bonnet with χ = 0)
  I8  φ₀u₀ (sin(y/R) on y < πR/2, −sin(y/R) beyond) solves the untwisted problem at 2/R²: the eigen-equation on each
      side and the periodic seam, which discriminates through the derivative only, since both modes vanish at the
      seam; it is odd about the cone, while u₀ is anti-periodic and even; both have intensity sin²(y/R)
  I9  §IX's second variation: for the normal-geodesic variation of a great S² in S³(R) with speed φ, the area element is
      exactly cos(tφ/R)·√(cos²(tφ/R) + t²|∇φ|²) dA, with no first-order term and second-order term (|∇φ|² − 2φ²/R²)/2
--arms plants a defect for each check and requires it to fire."""
import sys
import numpy as np
import sympy as sp

R, y, w, th, lat = sp.symbols("R y w theta lat", positive=True)


def surface_sums(dims=4, seed=7, n=25):
    """Random polynomial surface pushed onto S³(R); returns max deviations of sum x² from R² and sum |∇x|² from 2."""
    rng = np.random.default_rng(seed)
    Rv = 1.7
    C = rng.normal(size=(4, 6))
    mono = lambda u, v: np.array([1, u, v, u * v, u * u, v * v])
    dmono_u = lambda u, v: np.array([0, 1, 0, v, 2 * u, 0])
    dmono_v = lambda u, v: np.array([0, 0, 1, u, 0, 2 * v])
    dev1 = dev2 = 0.0
    for u, v in rng.uniform(-1, 1, size=(n, 2)):
        P, Pu, Pv = C @ mono(u, v), C @ dmono_u(u, v), C @ dmono_v(u, v)
        r = np.linalg.norm(P)
        proj = lambda d: Rv * (d - P * (P @ d) / r**2) / r        # derivative of Rv * P/|P|
        X, Xu, Xv = Rv * P / r, proj(Pu), proj(Pv)
        g = np.array([[Xu @ Xu, Xu @ Xv], [Xv @ Xu, Xv @ Xv]])
        ginv = np.linalg.inv(g)
        grads = np.array([[Xu[i], Xv[i]] for i in range(4)])[:dims]
        dev1 = max(dev1, abs((X[:dims] ** 2).sum() - Rv**2))
        dev2 = max(dev2, abs(sum(gr @ ginv @ gr for gr in grads) - 2))
    return dev1, dev2


def lap_band(f):
    c = sp.cos(y / R)
    return sp.diff(c * sp.diff(f, y), y) / c + sp.diff(f, w, 2) / c**2


def zonal_eigen(m, f):
    """−Δ on S^m(R) acting on f(θ), divided by f."""
    lap = sp.diff(sp.sin(th) ** (m - 1) * sp.diff(f, th), th) / (R**2 * sp.sin(th) ** (m - 1))
    return sp.simplify(-lap / f)


def curvature_terms(n, surf_dim, seed=3):
    """Round Sⁿ(R), R(X,Y)Z = (<Y,Z>X − <X,Z>Y)/R². A random orthonormal frame of the tangent space: surf_dim tangent
    directions of a great S^surf_dim, then a unit normal ν. Returns R² times the Jacobi curvature term, the sum over the
    tangent directions e of <R(ν,e)e, ν>, and R² times the ambient Ricci(ν, ν)."""
    rng = np.random.default_rng(seed + n)
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    e, nu = Q[:, :surf_dim], Q[:, surf_dim]
    Rt = lambda X, Y, Z: (Y @ Z) * X - (X @ Z) * Y
    jac = sum(Rt(nu, e[:, i], e[:, i]) @ nu for i in range(surf_dim))
    ric = sum(Rt(nu, Q[:, j], Q[:, j]) @ nu for j in range(n) if j != surf_dim)
    return jac, ric


def results(lam=2, plant=None):
    plant = plant or {}
    out = {}
    d1, d2 = surface_sums(dims=3 if plant.get("I1") else 4)
    out["I1 sum x² = R², sum |∇x|² = 2 on a generic surface in S³"] = d1 < 1e-12 and d2 < 1e-12
    u0 = sp.sin(y / R) if not plant.get("I2") else sp.sin(y / R) + sp.Rational(1, 10) * sp.sin(3 * y / R)
    out["I2 −Δ sin(y/R) = (2/R²) sin(y/R)"] = sp.simplify(-lap_band(u0) - sp.Integer(lam) / R**2 * u0) == 0
    xp_north = R * sp.sin(y / R)                      # latitude y/R
    xp_south = R * sp.sin(-(sp.pi * R - y) / R)       # latitude −(πR − y)/R
    s = -1 if not plant.get("I3") else 1
    out["I3 the trivialization carries sin(y/R) to x_p/R"] = (sp.simplify(xp_north / R - sp.sin(y / R)) == 0
                                                              and sp.simplify(xp_south / R - s * sp.sin(y / R)) == 0)
    x = sp.Matrix(sp.symbols("x1:5"))
    A = sp.zeros(4)
    A[3, 2], A[2, 3] = 1, -1                          # K(x) = x3 e4 − x4 e3: pole e3, normal e4
    if plant.get("I4"):
        A[2, 3] = 1
    K = A * x
    out["I4 rotation field: Killing, tangent to S³, equals x_p ν on x4 = 0"] = (A.T == -A and sp.expand((K.T * x)[0]) == 0
                                                                               and list(K.subs(x[3], 0)) == [0, 0, 0, x[2]])
    ok5, meets = True, []
    for nd in range(3, 9):
        m = nd - 1 if plant.get("I5") else 2               # planted: the hypersphere family, surface dimension n − 1
        tilt = float(zonal_eigen(m, R * sp.cos(th)) * R**2)
        jac, ric = curvature_terms(nd, m)
        ok5 &= abs(jac - tilt) < 1e-12
        if abs(ric - tilt) < 1e-12:
            meets.append(nd)
    out["I5 great S² in Sⁿ, n = 3..8: tilt 2/R² = Jacobi term for every n; Ricci floor meets it only at n = 3"] = ok5 and meets == [3]
    n = sp.symbols("n", positive=True, integer=True)
    first_s3 = zonal_eigen(3, R * sp.cos(th))
    out["I6 3/R² on S³, and n/R² = n(n−1)/(2R²) only at n = 3"] = (first_s3 == 3 / R**2
                                                                   and sp.solve(sp.Eq(n, n * (n - 1) / 2 + (1 if plant.get("I6") else 0)), n) == [3])
    t, sig, W = sp.symbols("t sigma W", positive=True)
    f = sp.cos(t / R)
    kg = sp.simplify((sp.diff(f, t) / f).subs(t, W))             # the edge t = W curves away from the core
    area = sp.integrate(sp.integrate(f, (sig, 0, sp.pi * R)), (t, -W, W))
    edge = 2 * sp.pi * R * sp.cos(W / R)
    bal = sp.simplify(area / R**2 + (kg if not plant.get("I7") else -kg) * edge)
    out["I7 the tube's edge curvature tan(W/R)/R balances its area (Gauss-Bonnet, χ = 0)"] = (sp.simplify(kg + sp.tan(W / R) / R) == 0
                                                                                            and bal == 0)
    v0 = sp.sin(y / R)
    north, south = sp.sin(y / R), -sp.sin(y / R)            # φ₀u₀ on y < πR/2 and on y > πR/2
    dy = lambda g: sp.diff(g, y)
    at = lambda g, v: sp.simplify(g.subs(y, v))
    s8 = -1 if plant.get("I8") else 1                         # planted: ask φ₀u₀ for the twisted, anti-periodic seam
    eig = all(sp.simplify(-lap_band(g) - 2 / R**2 * g) == 0 for g in (north, south))
    periodic = at(south, sp.pi * R) == s8 * at(north, 0) and at(dy(south), sp.pi * R) == s8 * at(dy(north), 0)
    anti_v0 = at(v0, sp.pi * R) == -at(v0, 0) and at(dy(v0), sp.pi * R) == -at(dy(v0), 0)
    odd_cone = sp.simplify(south.subs(y, sp.pi * R - y) + north) == 0
    even_v0 = sp.simplify(v0.subs(y, sp.pi * R - y) - v0) == 0
    same = sp.simplify(north**2 - v0**2) == 0 and sp.simplify(south**2 - v0**2) == 0
    out["I8 φ₀u₀ is an untwisted 2/R² mode, odd about the cone, with u₀'s intensity"] = (eig and periodic and anti_v0 and odd_cone
                                                                                        and even_v0 and same)
    t9, lam9 = sp.symbols("t9", positive=True), sp.symbols("lambda9", real=True)
    ph = sp.Function("phi")(th, lam9)
    x9 = sp.Matrix([R * sp.cos(th) * sp.cos(lam9), R * sp.cos(th) * sp.sin(lam9), R * sp.sin(th), 0])
    e4 = sp.Matrix([0, 0, 0, 1])
    c9 = sp.cos(t9 * ph / R)
    X9 = (x9 + t9 * ph * e4) if plant.get("I9") else (c9 * x9 + R * sp.sin(t9 * ph / R) * e4)   # planted: a flat normal graph
    Xa, Xb = X9.diff(th), X9.diff(lam9)
    G = sp.Matrix([[Xa.dot(Xa), Xa.dot(Xb)], [Xb.dot(Xa), Xb.dot(Xb)]])
    ga, gb = x9.diff(th).dot(x9.diff(th)), x9.diff(lam9).dot(x9.diff(lam9))
    grad2 = ph.diff(th) ** 2 / ga + ph.diff(lam9) ** 2 / gb
    dens2 = sp.simplify(G.det() / (ga * gb))
    ser = sp.series(sp.sqrt(dens2), t9, 0, 3).removeO()
    out["I9 second variation: exact area density, no first-order term, t² term (|∇φ|² − 2φ²/R²)/2"] = (
        sp.simplify(dens2 - c9**2 * (c9**2 + t9**2 * grad2)) == 0 and sp.simplify(ser.coeff(t9, 1)) == 0
        and sp.simplify(ser.coeff(t9, 2) - (grad2 - 2 * ph**2 / R**2) / 2) == 0)
    return out


def main():
    res = results()
    for name, ok in res.items():
        print(("PASS " if ok else "FAIL ") + name)
    if "--arms" in sys.argv:
        assert all(res.values()), "arms need a green parent"
        rc = 0
        for key in ("I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9"):
            name = next(k for k in res if k.startswith(key))
            fired = not results(plant={key: True})[name]
            print(("ARM FIRED " if fired else "ARM SILENT ") + name)
            rc |= 0 if fired else 1
        return rc
    return 0 if all(res.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
