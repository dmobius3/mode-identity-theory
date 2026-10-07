"""Exact analysis at a critical point u of the reduced quartic: criticality, M, its inertia,
the orbit tangent K, the radical r of omega on K, and the characteristic polynomial of the
slow matrix S = J0 G^{-1} M (similar to the orthonormal-basis J0 M)."""
import sympy as sp
from sympy import Rational as R
from sympy.polys.matrices import DomainMatrix
from core import h_poly, metric, J0, gen_real, Theta_real, grad_hess

_cache = {}

def setup(j2, q):
    key = (j2, tuple(sorted(q.items())))
    if key not in _cache:
        hp = h_poly(j2, q)
        grad, hess = grad_hess(hp)
        _cache[key] = (hp, grad, hess)
    return _cache[key]


def field_of(entries):
    algs = set()
    for e in entries:
        for a in sp.preorder_traversal(sp.sympify(e)):
            if isinstance(a, sp.Pow) and a.exp == R(1, 2):
                algs.add(a)
    return sorted(algs, key=str)


def charpoly(Mat, var):
    ents = list(Mat)
    algs = field_of(ents)
    if algs:
        K = sp.QQ.algebraic_field(*algs)
    else:
        K = sp.QQ
    dM = DomainMatrix.from_list_sympy(*Mat.shape, Mat.tolist()).convert_to(K)
    coeffs = dM.charpoly()
    poly = sp.Poly([K.to_sympy(c) for c in coeffs], var)
    return sp.Poly(sp.expand(poly.as_expr()), var)


def count_with_mult(P, lo, hi):
    """Real roots of P in (lo, hi), counted with multiplicity (Sturm on each square-free factor)."""
    tot = 0
    for f, mult in sp.sqf_list(P)[1]:
        tot += mult * sp.Poly(f, P.gen).count_roots(lo, hi)
    return tot


def inertia_from_charpoly(cp, var):
    """All roots real (symmetric matrix): exact sign counts with multiplicity."""
    P = sp.Poly(cp, var)
    z = 0
    while P.eval(0) == 0:
        P = sp.Poly(sp.cancel(P.as_expr() / var), var); z += 1
    pos = count_with_mult(P, 0, None)
    neg = count_with_mult(P, None, 0)
    assert pos + neg == P.degree(), 'non-real roots in a symmetric char poly'
    return neg, z, pos


def analyse(j2, q, u, quaternionic, label=''):
    hp, grad, hess = setup(j2, q)
    n2 = 2 * (j2 + 1)
    G = metric(j2)
    sub = dict(zip(hp.gens, u))
    hv = sp.radsimp(sp.expand(hp.as_expr().subs(sub)))
    gv = sp.Matrix([sp.expand(g.as_expr().subs(sub)) for g in grad])
    Hm = sp.Matrix(n2, n2, lambda i, k: sp.expand(hess[i][k].as_expr().subs(sub)))
    uvec = sp.Matrix(u)
    nrm = sp.expand((uvec.T * G * uvec)[0])
    lam = sp.radsimp(4 * hv / nrm)
    crit = sp.simplify(gv - lam * G * uvec)
    is_crit = all(sp.simplify(c) == 0 for c in crit)
    Qval = sp.radsimp(hv / nrm**2)
    Mp = (Hm - lam * G).applyfunc(sp.expand)
    # orbit tangent
    gens = [J0(j2)] + gen_real(j2)
    if quaternionic:
        T = Theta_real(j2)
        gens += [T, T * J0(j2)]
    Kcols = [ (g * uvec).applyfunc(sp.expand) for g in gens ]
    Kmat = sp.Matrix.hstack(*Kcols)
    k = Kmat.rank(simplify=True)
    # omega in p-coordinates: omega(x, y) = x^T J0 G y
    W = (Kmat.T * J0(j2) * G * Kmat).applyfunc(sp.simplify)
    r = k - W.rank(simplify=True)
    mu = sp.Symbol('mu')
    cpM = charpoly(Mp, mu)
    nneg, nzero, npos = inertia_from_charpoly(cpM, mu)
    sig = (nneg, nzero - k, npos - 1)          # on N_u: drop the orbit kernel and the radial direction
    S = J0(j2) * G.inv() * Mp
    cpS = charpoly(S, mu)
    P = sp.Poly(cpS, mu); mS = 0
    while P.eval(0) == 0:
        P = sp.Poly(sp.cancel(P.as_expr() / mu), mu); mS += 1
    # even part in nu = mu^2
    nu = sp.Symbol('nu')
    Pe = P.as_expr()
    assert sp.expand(Pe - Pe.subs(mu, -mu)) == 0, 'not even'
    Pnu = sp.Poly(sp.expand(Pe).subs(mu, sp.sqrt(nu)), nu)
    deg = Pnu.degree()
    neg_real = count_with_mult(Pnu, None, 0)     # real roots < 0 (0 excluded already)
    pos_real = count_with_mult(Pnu, 0, None)
    sqf = sp.gcd(Pnu, Pnu.diff(nu)).degree() == 0
    if neg_real == deg:
        typ = 'elliptic' + (', simple' if sqf else ', repeated frequencies')
    else:
        typ = f'hyperbolic ({pos_real} positive real nu, {deg - neg_real - pos_real} complex nu)'
    # normalize: S scales with |u|^2_G; report P for the unit vector
    Pnu_unit = sp.factor(sp.expand(Pnu.as_expr().subs(nu, nu * nrm**2)))
    # Krein signature per frequency cluster (rational nu_c only; irrational simple roots are definite)
    krein = []
    if neg_real == deg:
        for f, mult in sp.factor_list(Pnu)[1]:
            fp = sp.Poly(f, nu)
            if fp.degree() == 1:
                nuc = sp.solve(fp.as_expr(), nu)[0]
                Ec = (S * S - nuc * sp.eye(S.shape[0])).applyfunc(sp.expand)
                basis = Ec.nullspace(simplify=True)
                B = sp.Matrix.hstack(*basis)
                Mc = (B.T * Mp * B).applyfunc(sp.simplify)
                cpc = charpoly(Mc, mu)
                ng, zr, ps = inertia_from_charpoly(cpc, mu)
                krein.append((f'nu*|u|^4={sp.radsimp(nuc / nrm**2)}', mult, (ng, zr, ps)))
            else:
                krein.append((str(fp.as_expr()), mult, 'irrational roots' + ('' if mult == 1 else ', REPEATED: not checked')))
    return dict(label=label, Q=Qval, crit=is_crit, sig=sig, k=k, r=r, mS=mS, typ=typ, Pnu_unit=Pnu_unit, krein=krein,
                Pnu=sp.factor(Pnu.as_expr()), cpM=cpM, M=Mp, G=G, Kmat=Kmat, S=S, lam=lam, nrm=nrm, W=W)
