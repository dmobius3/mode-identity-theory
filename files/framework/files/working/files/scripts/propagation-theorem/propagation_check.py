#!/usr/bin/env python3
"""propagation_check.py -- checks for The Propagation Theorem (propagation-theorem.md).

Five claims, each with a mutation arm that must turn it red:

  1. Isotropy. On S^3/2I the right action's isotropy is 2I, acting on the tangent space
     through its image A5 in SO(3). A5 fixes no covector and leaves a one-dimensional
     space of quadratic forms invariant (irreducibility). The same holds for 2T and 2O.
     Arm: lens L(5,1), prism (binary dihedral of order 20) and trivial isotropy (S^3 or
     RP^3 under the right action alone) all leave more than one quadratic form.
  2. Invariants below degree six. A5's invariant polynomials on R^3 have Molien series
     (1 + t^15)/((1 - t^2)(1 - t^6)(1 - t^10)): below degree 6 only the powers of |xi|^2.
     Computed two ways (characters; a Reynolds rank at random points).
     Arm: 2T has a cubic invariant and 2O a second quartic one.
  3. The lifted action. On the two-dimensional slot bundle E_rho (rho the defining
     representation of 2I), phi(x) = x v is a section, phi(gamma x) = rho(gamma) phi(x),
     and the right action of -1 acts on it by -1. (The isotropy's action on the fibre over
     [1] is then rho, by the section property itself.)
     Arm: on the adjoint bundle -1 acts by +1, so the spinorial claim fails there.
  4. Distances. The round S^3 of radius R, its metric induced from the embedding in R^4,
     satisfies Ric = 2 g / R^2, so its curvature is 1/R^2; the transverse Jacobi field along
     a unit-speed geodesic, f'' + K f = 0 with f(0) = 0 and f'(0) = 1, is then R sin(chi/R),
     the metric's own transverse factor. Nothing in the chain assumes the answer.
     Arm: the flat R^3, embedded the same way, has K = 0 and Jacobi factor chi.
  5. Several images. 2I's shortest translation is pi/5 (largest real part below 1 is
     cos(pi/5)), so the injectivity radius of S^3/2I is pi R/10.
     Arm: 2O's shortest translation is pi/4.

Run: python3 propagation_check.py   (needs numpy and sympy; deterministic output)
"""
import itertools
import numpy as np
import sympy as sp

PHI = (1 + 5 ** 0.5) / 2

# ---------- quaternion groups ----------------------------------------------------------
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return (w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2)

def key(q):
    return tuple(round(c, 7) + 0.0 for c in q)

def group(elems):
    G = {}
    for q in elems:
        G.setdefault(key(q), tuple(float(c) for c in q))
    return [G[k] for k in sorted(G)]

def closed(G):
    S = {key(g) for g in G}
    return all(key(qmul(a, b)) in S for a in G for b in G)

def hurwitz():
    G = set()
    for i in range(4):
        for s in (1, -1):
            q = [0.0] * 4; q[i] = s; G.add(tuple(q))
    for signs in itertools.product((0.5, -0.5), repeat=4):
        G.add(signs)
    return [tuple(g) for g in G]

def even_perms(v):
    out = []
    for p in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
        if inv % 2 == 0:
            out.append(tuple(v[p[i]] for i in range(4)))
    return out

def binary_icosahedral():
    E = list(hurwitz())
    for s1, s2, s3 in itertools.product((1, -1), repeat=3):
        E += even_perms((0.0, s1 * 0.5, s2 / (2 * PHI), s3 * PHI / 2))
    return group(E)

def binary_octahedral():
    E = list(hurwitz())
    r = 1 / 2 ** 0.5
    for i, j in itertools.combinations(range(4), 2):
        for s, t in itertools.product((1, -1), repeat=2):
            q = [0.0] * 4; q[i] = s * r; q[j] = t * r; E.append(tuple(q))
    return group(E)

def binary_tetrahedral():
    return group(hurwitz())

def cyclic(n):          # order n in SU(2): the lens space L(n,1)
    return group((np.cos(2 * np.pi * k / n), np.sin(2 * np.pi * k / n), 0.0, 0.0) for k in range(n))

def binary_dihedral(n):  # order 4n: the prism space
    C = [(np.cos(np.pi * k / n), np.sin(np.pi * k / n), 0.0, 0.0) for k in range(2 * n)]
    return group(C + [qmul(c, (0.0, 0.0, 1.0, 0.0)) for c in C])

def rot(q):
    w, x, y, z = q
    return np.array([[1 - 2*(y*y + z*z), 2*(x*y - w*z), 2*(x*z + w*y)],
                     [2*(x*y + w*z), 1 - 2*(x*x + z*z), 2*(y*z - w*x)],
                     [2*(x*z - w*y), 2*(y*z + w*x), 1 - 2*(x*x + y*y)]])

def image(G):           # the isotropy's action on the tangent space, Gamma/{+-1} in SO(3)
    M = {}
    for q in G:
        R = rot(q); M[tuple(np.round(R, 9).ravel() + 0.0)] = R
    return list(M.values())

# ---------- claim 1: isotropy invariants -----------------------------------------------
def isotropy_invariants(K):
    n = len(K)
    vec = sum(np.trace(g) for g in K) / n
    sym2 = sum((np.trace(g) ** 2 + np.trace(g @ g)) / 2 for g in K) / n
    return int(round(vec)), int(round(sym2))

# ---------- claim 2: Molien series, two routes -----------------------------------------
def molien_characters(K, dmax):
    tot = np.zeros(dmax + 1, dtype=complex)
    for g in K:
        lam = np.linalg.eigvals(g)
        series = np.zeros(dmax + 1, dtype=complex); series[0] = 1
        for l in lam:               # multiply by 1/(1 - l t)
            geo = np.array([l ** d for d in range(dmax + 1)])
            series = np.convolve(series, geo)[:dmax + 1]
        tot += series
    c = tot.real / len(K)
    assert np.allclose(c, np.round(c), atol=1e-6) and np.allclose(tot.imag / len(K), 0, atol=1e-6)
    return [int(round(v)) for v in c]

def molien_reynolds(K, d, rng):
    monos = [m for m in itertools.product(range(d + 1), repeat=3) if sum(m) == d]
    pts = rng.normal(size=(3 * len(monos) + 5, 3))
    # Reynolds-average each monomial and evaluate at the points; the rank is the dimension
    A = np.zeros((len(pts), len(monos)))
    for g in K:
        Y = pts @ g.T
        A += np.stack([np.prod(Y ** np.array(m), axis=1) for m in monos], axis=1)
    A /= len(K)
    B = np.stack([np.prod(pts ** np.array(m), axis=1) for m in monos], axis=1)   # unaveraged scale
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > 1e-8 * np.linalg.norm(B, 2)))

# ---------- claim 3: the lifted action on the two-dimensional slot ---------------------
def su2(q):
    w, x, y, z = q
    return np.array([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]])

def lifted_minus_one(rep, G, rng):
    """For phi(x) = rep(x) v: the section property and the right action of -1."""
    v = rng.normal(size=rep(G[0]).shape[0]) + 1j * rng.normal(size=rep(G[0]).shape[0])
    xs = []
    for _ in range(5):
        q = rng.normal(size=4); q /= np.linalg.norm(q); xs.append(tuple(q))
    section = all(np.allclose(rep(qmul(g, x)) @ v, rep(g) @ (rep(x) @ v)) for g in G for x in xs)
    minus = rep((-1.0, 0.0, 0.0, 0.0))
    acts_by_minus_one = all(np.allclose(rep(qmul(x, (-1.0, 0.0, 0.0, 0.0))) @ v, -(rep(x) @ v)) for x in xs)
    return section, acts_by_minus_one, np.allclose(minus, -np.eye(minus.shape[0]))

def adjoint(q):
    return rot(q).astype(complex)

# ---------- claim 4: curvature from the embedding, then the Jacobi factor ---------------
def ricci(g, X):
    n = len(X); ginv = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                          - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    def riem(a, b, c, d):        # R^a_{bcd}
        return (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
    return sp.Matrix(n, n, lambda b, d: sp.simplify(sum(riem(a, b, a, d) for a in range(n))))

def distances(curved=True):
    R, psi, th, ph, chi = sp.symbols('R psi theta phi chi', positive=True)
    if curved:   # the round S^3 of radius R in R^4, geodesic polar coordinates about a point
        emb = sp.Matrix([R * sp.cos(psi), R * sp.sin(psi) * sp.cos(th),
                         R * sp.sin(psi) * sp.sin(th) * sp.cos(ph), R * sp.sin(psi) * sp.sin(th) * sp.sin(ph)])
        arclength = {psi: chi / R}
    else:        # the arm: flat R^3 in polar coordinates
        emb = sp.Matrix([psi * sp.cos(th), psi * sp.sin(th) * sp.cos(ph), psi * sp.sin(th) * sp.sin(ph)])
        arclength = {psi: chi}
    X = [psi, th, ph]
    J = emb.jacobian(X)
    g = sp.simplify(J.T * J)
    Ric = ricci(g, X)
    K = sp.simplify(Ric[1, 1] / (2 * g[1, 1]))           # in three dimensions Ric = 2K g
    einstein = all(sp.simplify(Ric[i, j] - 2 * K * g[i, j]) == 0 for i in range(3) for j in range(3))
    f = sp.Function('f')
    jac = sp.dsolve(sp.Eq(f(chi).diff(chi, 2) + K * f(chi), 0), f(chi),
                    ics={f(0): 0, f(chi).diff(chi).subs(chi, 0): 1}).rhs
    own = sp.simplify(g[1, 1].subs(arclength) - jac ** 2) == 0       # the metric's transverse factor
    target = sp.simplify(jac - R * sp.sin(chi / R)) == 0
    return einstein and sp.simplify(K - 1 / R ** 2) == 0 and own and target, K, sp.simplify(jac)

# ---------- claim 5: the shortest translation ------------------------------------------
def shortest_translation(G):
    best = max(q[0] for q in G if key(q) != key((1.0, 0.0, 0.0, 0.0)))
    return float(np.arccos(best))

def main():
    rng = np.random.default_rng(20261009)
    out, fails, arms = [], 0, 0
    def line(ok, text):
        nonlocal fails
        fails += (not ok)
        out.append(f"{'PASS' if ok else 'FAIL'} {text}")
    def arm(red, text):
        nonlocal fails, arms
        arms += 1
        fails += (not red)
        out.append(f"{'PASS' if red else 'FAIL'} arm: {text}")

    I2, O2, T2 = binary_icosahedral(), binary_octahedral(), binary_tetrahedral()
    line(len(I2) == 120 and closed(I2) and len(O2) == 48 and closed(O2) and len(T2) == 24 and closed(T2),
         f"groups: |2I| = {len(I2)}, |2O| = {len(O2)}, |2T| = {len(T2)}, each closed")
    A5, S4, A4 = image(I2), image(O2), image(T2)

    # claim 1
    inv = {n: isotropy_invariants(K) for n, K in (('2I', A5), ('2O', S4), ('2T', A4))}
    line(len(A5) == 60 and inv['2I'] == (0, 1),
         f"1 isotropy of S^3/2I: |A5| = {len(A5)}, invariant covectors {inv['2I'][0]}, invariant quadratic forms {inv['2I'][1]}")
    line(inv['2O'] == (0, 1) and inv['2T'] == (0, 1),
         f"1 the second-order statement holds on S^3/2O and S^3/2T too: {inv['2O']}, {inv['2T']}")
    lens, prism, triv = image(cyclic(5)), image(binary_dihedral(5)), [np.eye(3)]
    il, ip, it = isotropy_invariants(lens), isotropy_invariants(prism), isotropy_invariants(triv)
    arm(il[1] > 1 and ip[1] > 1 and it[1] > 1,
        f"lens L(5,1) {il}, prism (order 20) {ip}, trivial isotropy {it}: more than one invariant quadratic form, so non-round symbols exist")

    # claim 2
    ser = molien_characters(A5, 16)
    expect = [1, 0, 1, 0, 1, 0, 2, 0, 2, 0, 3, 0, 4, 0, 4, 1, 5]
    rey = [molien_reynolds(A5, d, rng) for d in range(0, 7)]
    line(ser == expect and rey == ser[:7],
         f"2 A5 invariants by degree 0-16 (characters): {ser}; degrees 0-6 by Reynolds rank: {rey}")
    line(ser[:6] == [1, 0, 1, 0, 1, 0],
         "2 below degree 6 the invariants are the powers of |xi|^2 alone, as for SO(3)")
    s4, a4 = molien_characters(S4, 6), molien_characters(A4, 6)
    arm(s4[4] == 2 and a4[3] == 1,
        f"2O invariants by degree {s4} (a second quartic), 2T {a4} (a cubic): the order-five extension is specific to 2I")

    # claim 3
    sec, m1, rho_m1 = lifted_minus_one(su2, I2, rng)
    line(sec and m1 and rho_m1,
         "3 on the two-dimensional slot, phi(x) = x v satisfies phi(gamma x) = rho(gamma) phi(x), and the right action of -1 acts on it by -1")
    sec_a, m1_a, rho_m1_a = lifted_minus_one(adjoint, I2, rng)
    arm(sec_a and not m1_a and not rho_m1_a,
        "on the adjoint bundle -1 acts by +1, so the spinorial statement fails there")

    # claim 4
    ok4, K4, jac4 = distances(True)
    line(ok4, f"4 the embedded round S^3 has Ric = 2K g with K = {K4}, and its transverse Jacobi factor is {jac4}, the metric's own")
    ok4f, K4f, jac4f = distances(False)
    arm(not ok4f, f"the embedded flat R^3 has K = {K4f} and Jacobi factor {jac4f}, not R sin(chi/R)")

    # claim 5
    d2i, d2o = shortest_translation(I2), shortest_translation(O2)
    line(abs(d2i - np.pi / 5) < 1e-12,
         f"5 2I's shortest translation {d2i:.12f} = pi/5, so the injectivity radius of S^3/2I is pi R/10")
    arm(abs(d2o - np.pi / 5) > 1e-6, f"2O's shortest translation {d2o:.12f} = pi/4, not pi/5")

    out.append(f"{sum(1 for o in out if o.startswith('PASS') and 'arm:' not in o)} checks and {arms} arms; {fails} FAIL")
    print('\n'.join(out))
    return fails

if __name__ == '__main__':
    raise SystemExit(main())
