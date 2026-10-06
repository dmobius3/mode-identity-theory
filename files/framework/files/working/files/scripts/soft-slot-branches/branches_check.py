#!/usr/bin/env python3
"""Checks for the soft-slot branches: the reduced quartic's critical orbits in R4 and R5 (level 6, spin 3) and in R2
(level 7, spin 7/2). The computations are exact, in weighted coordinates p_m = w_m / sqrt((j+m)!(j-m)!), where the
quartic h = Q |w|^4 = sum_J q_J ||[w (x) w]_J||^2, the metric, the generators and Theta are rational; w_m are the
orthonormal Condon-Shortley components. At a critical point u, M_u = Hess h(u) - 4 h(u) G and S_u = J0 G^-1 M_u.

  A  the channel quartic equals (1 + beta ||(w w^dag)_6||^2 / |w|^4) |w|^4 at random rational points, in R2, R4 and R5
  B  R4: M8.12's ten census orbits: criticality, 924 r6, the signature of M_u on N_u, k, r_u, the zero multiplicity
     of S_u, and the slow type, against the expected rows
  C  R5: the same signatures and types, with the slow polynomial P5(nu) = P4(256 nu / 81) up to scale
  D  R2: the weight states and the four line points, against the expected rows
  E  R2: with the fibre Sp(1) directions in the orbit tangent, the weight-7/2 orbit is nondegenerate, (0, 0, 10)
  F  R2: the slow type at the family members with complex structures j, k, (i + j)/sqrt 2 and (i + k)/sqrt 2:
     elliptic throughout at the two definite orbits, hyperbolic at weight 5/2 and 3/2
  G  Krein: M_u restricted to ker(S_u^2 + tau^2), relative to the metric, is positive definite at both prism clusters
  H  the prism's isotropy: the 3-fold rotation about z fixes it, and the half-turn about x maps it to -u
  I  the third outside orbit: Krawczyk's test on the slice system about an 80-digit point, then interval
     characteristic polynomials: the value, the signature (7, 0, 2), orbit dimension 4, |J|^2 > 0, a zero of S_u of
     multiplicity 6, and four simple negative roots in nu
  J  the lines {5/2, -5/2}, {7/2, -7/2} and {3/2, -3/2} of R2 are Sp(1) orbits of weight states: Q is constant on them
  K  the Hermitian lifts of Q - 144/143 on R2 with multipliers |w|^2 and |w|^4 are not positive semidefinite
     (floating point: the smallest eigenvalue on the symmetric power)
Mutation arms, each of which must turn its claim red: beta off by 1% (A); the prism with sqrt 47 in place of sqrt 46
(B); the scaling 3/4 in place of 9/16 (C); the line point t = 6 in place of 7 (D); the Sp(1) directions dropped (E);
weight 5/2 tested only at the physical structure i (F); the definiteness test on the sum of a Krein-negative and a
Krein-positive cluster of v2 (G); the 6-fold rotation about z (H); the Krawczyk box centered 1e-40 away (I); the line
{7/2, -3/2} (J); the lift of Q - 144/143 + 1/2 (K).
Runs in a few minutes.
"""
import itertools
import random

import mpmath as mp
import numpy as np
import sympy as sp
from sympy import I, Rational as R, sqrt
from sympy.physics.wigner import clebsch_gordan
from sympy.polys.matrices import DomainMatrix

Q2 = {7: R(144, 143), 5: R(196, 143), 3: R(28, 11), 1: R(0)}
Q4 = {6: R(1288, 1287), 4: R(35, 33), 2: R(14, 9), 0: R(7, 3)}
Q5 = {6: R(2289, 2288), 4: R(91, 88), 2: R(21, 16), 0: R(7, 4)}
BETA = {7: R(24, 13), 'R4': R(28, 39), 'R5': R(21, 52)}
MU, NU = sp.symbols('mu nu')


# ---------------------------------------------------------------- the exact machinery
def ms(j2):
    return [R(j2 - 2 * k, 2) for k in range(j2 + 1)]


def weight(j2, m):
    j = R(j2, 2)
    return sp.factorial(j + m) * sp.factorial(j - m)


def h_poly(j2, q):
    j, M_, n = R(j2, 2), ms(j2), j2 + 1
    T = {}
    for J, qJ in q.items():
        for Mt in range(-J, J + 1):
            pairs = []
            for a in range(n):
                for b in range(n):
                    if M_[a] + M_[b] == Mt:
                        c = clebsch_gordan(j, j, J, M_[a], M_[b], Mt)
                        if c != 0:
                            pairs.append((a, b, c * sp.sqrt(weight(j2, M_[a]) * weight(j2, M_[b]))))
            for (a, b, ca) in pairs:
                for (c_, d, cb) in pairs:
                    T[(a, b, c_, d)] = T.get((a, b, c_, d), 0) + qJ * ca * cb
    T = {k: sp.nsimplify(sp.simplify(v)) for k, v in T.items()}
    xs = sp.symbols(f'x0:{n}', real=True)
    ys = sp.symbols(f'y0:{n}', real=True)
    p = [xs[k] + I * ys[k] for k in range(n)]
    pc = [xs[k] - I * ys[k] for k in range(n)]
    expr = sp.expand(sum(v * pc[a] * pc[b] * p[c] * p[d] for (a, b, c, d), v in T.items() if v != 0))
    return sp.Poly(sp.re(expr), *xs, *ys)


def metric(j2):
    g = [weight(j2, m) for m in ms(j2)]
    return sp.diag(*(g + g))


def J0(j2):
    n = j2 + 1
    return sp.Matrix(sp.BlockMatrix([[sp.zeros(n), -sp.eye(n)], [sp.eye(n), sp.zeros(n)]]))


def to_real(C):
    A, B = C.applyfunc(sp.re), C.applyfunc(sp.im)
    return sp.Matrix(sp.BlockMatrix([[A, -B], [B, A]]))


def spin_ops(j2):
    M_, n, j = ms(j2), j2 + 1, R(j2, 2)
    Jp, Jm, Jz = sp.zeros(n), sp.zeros(n), sp.zeros(n)
    for a, m in enumerate(M_):
        Jz[a, a] = m
        if a > 0:
            Jp[a - 1, a] = j - m
        if a < n - 1:
            Jm[a + 1, a] = j + m
    return (Jp + Jm) / 2, (Jp - Jm) / (2 * I), Jz


def gens(j2):
    return [to_real(-I * Ja) for Ja in spin_ops(j2)]


def theta(j2):
    M_, n, j = ms(j2), j2 + 1, R(j2, 2)
    T = sp.zeros(2 * n)
    for a, m in enumerate(M_):
        b, s = M_.index(-m), (-1) ** int(j - m)
        T[b, a], T[n + b, n + a] = s, -s
    return T


def charpoly(Mat, var):
    algs = sorted({a for e in Mat for a in sp.preorder_traversal(sp.sympify(e))
                   if isinstance(a, sp.Pow) and a.exp == R(1, 2)}, key=str)
    K = sp.QQ.algebraic_field(*algs) if algs else sp.QQ
    dM = DomainMatrix.from_list_sympy(*Mat.shape, Mat.tolist()).convert_to(K)
    return sp.Poly(sp.expand(sp.Poly([K.to_sympy(c) for c in dM.charpoly()], var).as_expr()), var)


def count(P, lo, hi):
    return sum(mult * sp.Poly(f, P.gen).count_roots(lo, hi) for f, mult in sp.sqf_list(P)[1])


def strip_zero(P):
    z = 0
    while P.eval(0) == 0:
        P = sp.Poly(sp.cancel(P.as_expr() / P.gen), P.gen)
        z += 1
    return P, z


def slow_type(S):
    P, mS = strip_zero(charpoly(S, MU))
    assert sp.expand(P.as_expr() - P.as_expr().subs(MU, -MU)) == 0
    Pn = sp.Poly(sp.expand(P.as_expr()).subs(MU, sp.sqrt(NU)), NU)
    neg, pos = count(Pn, None, 0), count(Pn, 0, None)
    deg = Pn.degree()
    if neg == deg:
        typ = 'elliptic, simple' if sp.gcd(Pn, Pn.diff(NU)).degree() == 0 else 'elliptic, repeated'
    else:
        typ = 'hyperbolic, ' + ('real pairs' if neg + pos == deg else 'complex quartets')
    return mS, typ, Pn


_cache = {}


def setup(j2, q):
    key = (j2, tuple(sorted(q.items())))
    if key not in _cache:
        hp = h_poly(j2, q)
        grad = [hp.diff(v) for v in hp.gens]
        _cache[key] = (hp, grad, [[g.diff(v) for v in hp.gens] for g in grad])
    return _cache[key]


def vec(j2, d):
    n = j2 + 1
    re, im = [0] * n, [0] * n
    for idx, z in d.items():
        z = sp.sympify(z)
        re[idx], im[idx] = sp.re(z), sp.im(z)
    return re + im


def analyse(j2, q, u, quaternionic, sp1=True, structure=None):
    hp, grad, hess = setup(j2, q)
    N2, G = 2 * (j2 + 1), metric(j2)
    sub = dict(zip(hp.gens, u))
    uv = sp.Matrix(u)
    hv = sp.radsimp(sp.expand(hp.as_expr().subs(sub)))
    nrm = sp.expand((uv.T * G * uv)[0])
    lam = sp.radsimp(4 * hv / nrm)
    gv = sp.Matrix([sp.expand(g.as_expr().subs(sub)) for g in grad])
    crit = all(sp.simplify(c) == 0 for c in gv - lam * G * uv)
    Mp = sp.Matrix(N2, N2, lambda i, k: sp.expand(hess[i][k].as_expr().subs(sub))) - lam * G
    gl = [J0(j2)] + gens(j2)
    if quaternionic and sp1:
        gl += [theta(j2), theta(j2) * J0(j2)]
    K = sp.Matrix.hstack(*[(g * uv).applyfunc(sp.expand) for g in gl])
    k = K.rank(simplify=True)
    r = k - (K.T * J0(j2) * G * K).applyfunc(sp.simplify).rank(simplify=True)
    P, z = strip_zero(charpoly(Mp, MU))
    neg, pos = count(P, None, 0), count(P, 0, None)
    sig = (neg, z - k, pos - 1)
    Jc = J0(j2) if structure is None else structure
    mS, typ, Pn = slow_type(Jc * G.inv() * Mp)
    Pu = sp.Poly(sp.expand(Pn.as_expr().subs(NU, NU * nrm**2)), NU).monic()
    return dict(Q=sp.radsimp(hv / nrm**2), crit=crit, sig=sig, k=k, r=r, mS=mS, typ=typ, Pu=Pu, M=Mp, G=G,
                S=Jc * G.inv() * Mp, nrm=nrm)


def fmt_P(Pu):
    return str(sp.factor(Pu.as_expr()))


# ---------------------------------------------------------------- the claims
def claim_a(beta_factor=1):
    rnd = random.Random(7)
    ok = True
    for j2, q, beta in ((7, Q2, BETA[7]), (6, Q4, BETA['R4']), (6, Q5, BETA['R5'])):
        hp = setup(j2, q)[0]
        n, M_, j = j2 + 1, ms(j2), R(j2, 2)
        for _ in range(2):
            pv = [R(rnd.randint(-5, 5), rnd.randint(1, 4)) + I * R(rnd.randint(-5, 5), rnd.randint(1, 4)) for _ in range(n)]
            x = [sp.re(z) for z in pv] + [sp.im(z) for z in pv]
            h = sp.expand(hp.as_expr().subs(dict(zip(hp.gens, x))))
            w = [sp.sqrt(weight(j2, m)) * pv[a] for a, m in enumerate(M_)]
            nw = sum(sp.expand(z * sp.conjugate(z)) for z in w)
            rho = 0
            for Mt in range(-6, 7):
                s = sum(w[a] * sp.conjugate(w[b]) * clebsch_gordan(j, j, 6, m, -mp_, Mt) * (-1) ** int(j - mp_)
                        for a, m in enumerate(M_) for b, mp_ in enumerate(M_) if m - mp_ == Mt)
                rho += sp.expand(s * sp.conjugate(s))
            ok &= sp.simplify(h - (1 + beta * beta_factor * rho / nw**2) * nw**2) == 0
    return ok


R4_ROWS = [  # name, representative (index: coefficient), 924 r6, signature, k, r, zero multiplicity, type
    ('coherent v3', {0: 1}, 1, (0, 0, 10), 3, 1, 4, 'elliptic, simple'),
    ('v2', {1: 1}, 36, (2, 0, 8), 3, 1, 4, 'elliptic, simple'),
    ('prism', {0: 1, 3: sqrt(46), 6: 1}, R(8800, 43), (3, 0, 6), 4, 4, 8, 'elliptic, repeated'),
    ('v1', {2: 1}, 225, (4, 2, 4), 3, 1, 6, 'elliptic, simple'),
    ('D2 ray', {1: 1, 3: 2 * I, 5: 1}, 225, (5, 0, 4), 4, 4, 8, 'hyperbolic, real pairs'),
    ('C3 ray', {1: 1, 4: sqrt(10)}, R(1188, 5), (5, 0, 4), 4, 2, 6, 'hyperbolic, complex quartets'),
    ('pyramid', {0: 1, 5: sqrt(26) / 2}, R(1188, 5), (5, 0, 4), 4, 2, 6, 'hyperbolic, complex quartets'),
    ('octahedron', {1: 1, 5: 1}, 288, (6, 0, 3), 4, 4, 8, 'hyperbolic, real pairs'),
    ('zonal v0', {3: 1}, 400, (8, 0, 2), 3, 3, 6, 'hyperbolic, real pairs'),
    ('hexagon', {0: 1, 6: 1}, 463, (9, 0, 0), 4, 4, 8, 'elliptic, repeated'),
]

R2_ROWS = [
    ('weight 7/2', {0: 1}, R(144, 143), (0, 0, 10), 5, 1, 6, 'elliptic, simple'),
    ('weight 5/2', {1: 1}, R(168, 143), (4, 0, 6), 5, 1, 6, 'elliptic, repeated'),
    ('weight 3/2', {2: 1}, R(224, 143), (8, 0, 2), 5, 1, 6, 'elliptic, simple'),
    ('weight 1/2', {3: 1}, R(168, 143), (4, 0, 6), 5, 1, 6, 'hyperbolic, complex quartets'),
    ('line {7/2, -5/2}', {0: 1, 6: 7 * sqrt(51) / 17}, R(369, 247), (6, 0, 3), 6, 2, 8, 'hyperbolic, complex quartets'),
    ('line {7/2, -3/2}', {0: 1, 5: 7}, R(22, 13), (9, 0, 0), 6, 4, 10, 'elliptic, simple'),
    ('line {7/2, -1/2}', {0: 1, 4: 7}, R(193, 143), (5, 0, 4), 6, 2, 8, 'hyperbolic, complex quartets'),
    ('line {5/2, -3/2}', {1: 1, 5: 1}, R(161, 143), (0, 3, 6), 6, 2, 12, 'elliptic, simple'),
]


def row_ok(a, value, sig, k, r, mS, typ, scale=None):
    v = a['Q'] if scale is None else sp.radsimp((a['Q'] - 1) * scale)
    return a['crit'] and v == value and a['sig'] == sig and (a['k'], a['r'], a['mS']) == (k, r, mS) and a['typ'] == typ


def claim_b(prism_root=46, out=None):
    ok = True
    for name, rep, val, sig, k, r, mS, typ in R4_ROWS:
        if name == 'prism':
            rep = {0: 1, 3: sqrt(prism_root), 6: 1}
        a = analyse(6, Q4, vec(6, rep), False)
        good = row_ok(a, val, sig, k, r, mS, typ, scale=924 * R(39, 28))
        ok &= good
        if out is not None:
            out.append((name, a, good))
    return ok


def claim_c(scale=R(9, 16)):
    ok = True
    for name, rep, *_ in R4_ROWS:
        a4, a5 = analyse(6, Q4, vec(6, rep), False), analyse(6, Q5, vec(6, rep), False)
        same = a4['sig'] == a5['sig'] and a4['typ'] == a5['typ'] and a4['mS'] == a5['mS']
        scaled = sp.Poly(sp.expand(a4['Pu'].as_expr().subs(NU, NU / scale**2)), NU).monic()
        ok &= same and scaled == a5['Pu']
    return ok


def claim_d(line_t=7, out=None):
    ok = True
    for name, rep, val, sig, k, r, mS, typ in R2_ROWS:
        if name == 'line {7/2, -3/2}':
            rep = {0: 1, 5: line_t}
        a = analyse(7, Q2, vec(7, rep), True)
        good = row_ok(a, val, sig, k, r, mS, typ)
        ok &= good
        if out is not None:
            out.append((name, a, good))
    return ok


def claim_e(sp1=True):
    a = analyse(7, Q2, vec(7, {0: 1}), True, sp1=sp1)
    return a['sig'] == (0, 0, 10)


def claim_f(only_i=False, out=None):
    J, T = J0(7), theta(7)
    structs = [('i', J)] if only_i else [('j', T), ('k', T * J), ('(i+j)/sqrt2', J + T), ('(i+k)/sqrt2', J + T * J)]
    expect = {'weight 7/2': 'elliptic', 'line {7/2, -3/2}': 'elliptic', 'weight 5/2': 'hyperbolic', 'weight 3/2': 'hyperbolic'}
    ok = True
    for name, rep in (('weight 7/2', {0: 1}), ('line {7/2, -3/2}', {0: 1, 5: 7}), ('weight 5/2', {1: 1}), ('weight 3/2', {2: 1})):
        types = []
        for sname, Ip in structs:
            a = analyse(7, Q2, vec(7, rep), True, structure=Ip)
            types.append(a['typ'].split(',')[0])
        if expect[name] == 'elliptic':
            good = all(t == 'elliptic' for t in types)
        else:
            good = all(t == 'hyperbolic' for t in types)
        ok &= good
        if out is not None:
            out.append((name, [s for s, _ in structs], types))
    return ok


def restricted_eigs(a, tau2_units):
    """Eigenvalues of M on the sum of the clusters ker(S^2 + tau^2), relative to the metric, for unit u."""
    S, M, G, nrm = a['S'], a['M'], a['G'], a['nrm']
    basis = []
    for t2 in tau2_units:
        basis += (S * S + t2 * nrm**2 * sp.eye(S.shape[0])).applyfunc(sp.expand).nullspace(simplify=True)
    B = sp.Matrix.hstack(*basis)
    lam = sp.Symbol('lam')
    det = sp.factor(sp.expand((B.T * M * B - lam * B.T * G * B).applyfunc(sp.radsimp).det(method='berkowitz')))
    return B.shape[1], [sp.radsimp(x / nrm) for x in sp.roots(sp.Poly(det, lam), multiple=True)]


def claim_g(mixed=False, out=None):
    if mixed:
        a = analyse(6, Q4, vec(6, {1: 1}), False)
        dim, ev = restricted_eigs(a, [R(3136, 1656369), R(12544, 20449)])
        return all(e > 0 for e in ev)
    a = analyse(6, Q4, vec(6, {0: 1, 3: sqrt(46), 6: 1}), False)
    ok = True
    for t2, mult in ((R(19066880, 278420571), 2), (R(5770240, 7913763), 1)):
        dim, ev = restricted_eigs(a, [t2])
        good = dim == 2 * mult and all(e > 0 for e in ev)
        ok &= good
        if out is not None:
            out.append((t2, dim, ev))
    return ok


def claim_h(sixfold=False):
    j2 = 6
    Jx, Jy, Jz = spin_ops(j2)
    u = sp.Matrix([1, 0, 0, sqrt(46), 0, 0, 1])
    lag = lambda A, f: sum((f(m) * sp.prod([(A - mm * sp.eye(7)) / (m - mm) for mm in range(-3, 4) if mm != m])
                            for m in range(-3, 4)), sp.zeros(7))
    if sixfold:
        Rz = lag(Jz, lambda m: sp.exp(-I * sp.pi * m / 3))
        v = (Rz * u).applyfunc(sp.simplify)
        return v == u or v == -u
    Rz3 = lag(Jz, lambda m: sp.exp(-2 * I * sp.pi * m / 3))
    Rx2 = lag(Jx, lambda m: sp.Integer(-1) ** m)
    return (Rz3 * u).applyfunc(sp.simplify) == u and (Rx2 * u).applyfunc(sp.simplify) == -u


OUTSIDE = [
    '-0.011502604124156085736702996783571084095112795563571941198347252115508733277951057',
    '0.031566304564559044105257664909173721694601688140964840386010671679052926377243907',
    '0.029304331516929078934748776843009435415579650072187257193228145283404181009007635',
    '0.048714478042089452955997319491567899808396680795668112539253038575916758612900312',
    '0.051790769733201908343648689840445597632753725571140190640968302907546975700182541',
    '0.000046577394627912540042894491840564707885640181337220126550491061522654765004610056',
    '0.0083099342608087602416816148311668618719028234800008057489838106253555359508436595',
    '-0.0025898621604632939568365754648730823707784287411883513770056672928101121770886286',
    '-0.034642334888249968703359134704006530808617184412560399503399337498576866538784742',
    '0.023557789326067116134611792281570921857564246080397627451003307596454240268598184',
    '0.016471344414356385998303446075025036645704745547597234591542753114736582044214355',
    '-0.06459469607724002481612768010916253545320032802698215710012266036600262523245379',
    '0.0040284531520430920619487787355855210494275420660972687144010125960398420625410618',
    '-0.011338985780714801955539283609730224360740763172997439955367039833619030179474287']


def claim_i(shift=0, out=None):
    iv = mp.iv
    iv.dps = 90
    mp.mp.dps = 90
    hp, grad, hess = setup(6, Q4)
    N = 14
    G = metric(6)
    Gd = [int(G[i, i]) for i in range(N)]

    def comp(P):
        terms = [(mon, sp.Rational(c)) for mon, c in P.terms()]

        def ev(xs, ctx):
            tot = ctx.mpf(0)
            for mon, c in terms:
                t = ctx.mpf(c.p) / ctx.mpf(c.q)
                for xi, e in zip(xs, mon):
                    if e:
                        t = t * xi**e
                tot += t
            return tot
        return ev
    h_ev, g_ev = comp(hp), [comp(g) for g in grad]
    H_ev = [[comp(e) for e in row] for row in hess]
    xt = [mp.mpf(s) for s in OUTSIDE]
    xt[0] += mp.mpf(shift)
    Gens = [J0(6)] + gens(6)
    Xm = [[[mp.mpf(sp.Rational(X[a, b]).p) / sp.Rational(X[a, b]).q for b in range(N)] for a in range(N)] for X in Gens]
    ks = [[sum(X[a][b] * xt[b] for b in range(N)) for a in range(N)] for X in Xm]

    def F(v, ctx):
        x, lam, c = v[:N], v[N], v[N + 1:]
        g = [ge(x, ctx) for ge in g_ev]
        out_ = [g[a] - lam * Gd[a] * x[a] - sum(c[i] * Gd[a] * ctx.mpf(ks[i][a]) for i in range(4)) for a in range(N)]
        out_.append(sum(Gd[i] * x[i]**2 for i in range(N)) - 1)
        out_ += [sum(Gd[a] * ctx.mpf(ks[i][a]) * (x[a] - ctx.mpf(xt[a])) for a in range(N)) for i in range(4)]
        return out_

    def Jm(v, ctx):
        x, lam = v[:N], v[N]
        Hm = [[He(x, ctx) for He in row] for row in H_ev]
        D = N + 5
        A = [[ctx.mpf(0)] * D for _ in range(D)]
        for a in range(N):
            for b in range(N):
                A[a][b] = Hm[a][b] - (lam * Gd[a] if a == b else 0)
            A[a][N] = -Gd[a] * x[a]
            for i in range(4):
                A[a][N + 1 + i] = -Gd[a] * ctx.mpf(ks[i][a])
        for b in range(N):
            A[N][b] = 2 * Gd[b] * x[b]
        for i in range(4):
            for b in range(N):
                A[N + 1 + i][b] = Gd[b] * ctx.mpf(ks[i][b])
        return A
    vt = xt + [4 * h_ev(xt, mp) / sum(Gd[i] * xt[i]**2 for i in range(N))] + [mp.mpf(0)] * 4
    if shift == 0:
        for _ in range(2):
            vt = list(mp.matrix(vt) - mp.lu_solve(mp.matrix(Jm(vt, mp)), mp.matrix(F(vt, mp))))
    Y = mp.inverse(mp.matrix(Jm(vt, mp)))
    rho = mp.mpf('1e-60')
    D = N + 5
    X = [iv.mpf([t - rho, t + rho]) for t in vt]
    Fm, JX = F([iv.mpf(t) for t in vt], iv), Jm(X, iv)
    Kk = []
    for a in range(D):
        s = iv.mpf(vt[a]) - sum(iv.mpf(Y[a, b]) * Fm[b] for b in range(D))
        for b in range(D):
            row = iv.mpf(1 if a == b else 0) - sum(iv.mpf(Y[a, c]) * JX[c][b] for c in range(D))
            s += row * (X[b] - iv.mpf(vt[b]))
        Kk.append(s)
    inside = all(Kk[a].a > X[a].a and Kk[a].b < X[a].b for a in range(D))
    if not inside:
        return False
    U = Kk[:N]
    nrm = sum(Gd[i] * U[i]**2 for i in range(N))
    v924 = (h_ev(U, iv) / nrm**2 - 1) * 924 * iv.mpf(39) / 28

    def sgn(z):
        return 1 if z.a > 0 else (-1 if z.b < 0 else 0)

    def berk(A, ctx):
        n = len(A)
        C = [ctx.mpf(1), -A[0][0]]
        for r in range(1, n):
            Rr, S_, Cc, arr = [A[r][j] for j in range(r)], [[A[i][j] for j in range(r)] for i in range(r)], [A[i][r] for i in range(r)], A[r][r]
            T, v = [ctx.mpf(1), -arr], Cc[:]
            for _ in range(r):
                T.append(-sum(Rr[i] * v[i] for i in range(r)))
                v = [sum(S_[i][j] * v[j] for j in range(r)) for i in range(r)]
            new = [ctx.mpf(0)] * (r + 2)
            for i in range(r + 2):
                for j in range(len(C)):
                    if 0 <= i - j < len(T):
                        new[i] += T[i - j] * C[j]
            C = new
        return C[::-1]
    lamU = 4 * h_ev(U, iv) / nrm
    HU = [[He(U, iv) for He in row] for row in H_ev]
    MU_ = [[HU[a][b] - (lamU * Gd[a] if a == b else 0) for b in range(N)] for a in range(N)]
    cM = berk(MU_, iv)
    sig_ok = all(cM[i].a <= 0 <= cM[i].b for i in range(4)) and all(sgn(cM[i]) != 0 for i in range(4, N + 1))
    signs = [sgn(cM[i]) for i in range(4, N + 1)]
    changes = sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])
    sig = (N - 4 - changes, 0, changes - 1)
    J0m = J0(6)
    SU = [[sum(iv.mpf(int(J0m[a, c])) * MU_[c][b] / Gd[c] for c in range(N) if J0m[a, c] != 0) for b in range(N)] for a in range(N)]
    cS = berk(SU, iv)
    mS = 0
    while cS[mS].a <= 0 <= cS[mS].b:
        mS += 1
    Pc = [cS[mS + 2 * i] for i in range((N - mS) // 2 + 1)]
    rts = mp.polyroots([mp.mpf((c.a + c.b) / 2) for c in Pc][::-1], maxsteps=200, extraprec=200)
    negs = sorted(mp.re(r) for r in rts if abs(mp.im(r)) < mp.mpf('1e-30') and mp.re(r) < 0)

    def Pev(t):
        t = iv.mpf(t)
        return sum((c * t**i for i, c in enumerate(Pc)), iv.mpf(0))
    simple_neg = len(negs) == len(Pc) - 1 and all(
        sgn(Pev(r * (1 + mp.mpf('1e-20')))) * sgn(Pev(r * (1 - mp.mpf('1e-20')))) == -1 for r in negs)
    KU = [[sum(iv.mpf(Xm[g][a][b]) * U[b] for b in range(N)) for a in range(N)] for g in range(4)]

    def det(A):
        if len(A) == 1:
            return A[0][0]
        return sum(((-1) ** j) * A[0][j] * det([row[:j] + row[j + 1:] for row in A[1:]]) for j in range(len(A)))
    rank4 = sgn(det([[KU[g][r] for g in range(4)] for r in range(4)])) != 0
    Jv = []
    for g in (1, 2, 3):
        Jv.append(sum(U[a] * sum(iv.mpf(int(J0m[a, c])) * Gd[c] * KU[g][c] for c in range(N) if J0m[a, c] != 0)
                      for a in range(N)) / nrm)
    J2 = sum(x**2 for x in Jv)
    if out is not None:
        out.update(v924=v924, sig=sig, mS=mS, nroots=len(negs), J2=J2, negs=negs)
    return inside and sig_ok and sig == (7, 0, 2) and rank4 and J2.a > 0 and mS == 6 and simple_neg


def claim_j(lines=((1, 6), (0, 7), (2, 5))):
    hp = setup(7, Q2)[0]
    G = metric(7)
    t = sp.symbols('t', positive=True)
    ok = True
    for a, b in lines:
        u = [0] * 16
        u[a], u[b] = 1, t
        Q = sp.simplify(sp.expand(hp.as_expr().subs(dict(zip(hp.gens, u)))) / sp.expand((sp.Matrix(u).T * G * sp.Matrix(u))[0])**2)
        ok &= sp.simplify(sp.diff(Q, t)) == 0
    return ok


def lift_min(level, shift=0.0):
    j2, n = 7, 8
    j = R(j2, 2)
    M_ = ms(j2)
    a = {7: 0.0 + shift, 5: 52 / 143 + shift, 3: 220 / 143 + shift, 1: -144 / 143 + shift}
    A = np.zeros((n * n, n * n))
    for J, aJ in a.items():
        for Mt in range(-J, J + 1):
            v = np.zeros(n * n)
            for x, m1 in enumerate(M_):
                for y, m2 in enumerate(M_):
                    if m1 + m2 == Mt:
                        v[x * n + y] = float(clebsch_gordan(j, j, J, m1, m2, Mt))
            A += aJ * np.outer(v, v)
    deg = level + 2
    combos = list(itertools.combinations_with_replacement(range(n), deg))
    B = np.zeros((n ** deg, len(combos)))
    for c, cmb in enumerate(combos):
        perms = set(itertools.permutations(cmb))
        for p in perms:
            idx = 0
            for e in p:
                idx = idx * n + e
            B[idx, c] = 1.0
        B[:, c] /= np.sqrt(len(perms))
    Bt = B.reshape(n * n, n ** (deg - 2), len(combos))
    AB = np.einsum('ab,bkc->akc', A, Bt).reshape(n ** deg, len(combos))
    M2 = B.T @ AB
    return float(np.linalg.eigvalsh((M2 + M2.T) / 2)[0])


def claim_k(shift=0.0):
    return lift_min(1, shift) < -1e-6 and lift_min(2, shift) < -1e-6


# ---------------------------------------------------------------- the record
def main():
    failed = 0

    def report(label, ok):
        nonlocal failed
        failed += not ok
        print('   %s' % ('PASS' if ok else 'FAIL'))
    print('A  the channel quartic against the closed form, R2, R4, R5, two random rational points each')
    report('A', claim_a())
    rows = []
    print('B  R4: M8.12\'s ten census orbits, exact')
    ok_b = claim_b(out=rows)
    for name, a, good in rows:
        v = sp.radsimp((a['Q'] - 1) * 924 * R(39, 28))
        print('   %-12s 924 r6 = %-8s (n-,n0,n+) = %-11s k, r = %d, %d  zero mult %2d  %s' % (name, v, a['sig'], a['k'], a['r'], a['mS'], a['typ']))
        print('                P(nu), unit u: %s' % fmt_P(a['Pu']))
    report('B', ok_b)
    print('C  R5: the same rows, every slow eigenvalue scaled by 9/16')
    report('C', claim_c())
    rows = []
    print('D  R2: the weight states and the line points, exact')
    ok_d = claim_d(out=rows)
    for name, a, good in rows:
        print('   %-17s Q = %-8s (n-,n0,n+) = %-11s k, r = %d, %d  zero mult %2d  %s' % (name, a['Q'], a['sig'], a['k'], a['r'], a['mS'], a['typ']))
        print('                     P(nu), unit u: %s' % fmt_P(a['Pu']))
    report('D', ok_d)
    print('E  R2: the weight-7/2 orbit with the Sp(1) directions in its tangent is (0, 0, 10)')
    report('E', claim_e())
    rows = []
    print('F  R2: the slow type at the family members')
    ok_f = claim_f(out=rows)
    for name, sn, types in rows:
        print('   %-17s %s' % (name, ', '.join('%s: %s' % (s, t) for s, t in zip(sn, types))))
    report('F', ok_f)
    rows = []
    print('G  Krein: M on the prism\'s clusters, relative to the metric, unit u')
    ok_g = claim_g(out=rows)
    for t2, dim, ev in rows:
        print('   tau^2 = %s: dim %d, eigenvalues %s' % (t2, dim, sorted(ev)))
    report('G', ok_g)
    print('H  the prism\'s isotropy: the 3-fold about z fixes it; the half-turn about x maps it to -u')
    report('H', claim_h())
    info = {}
    print('I  the third outside orbit: Krawczyk, radius 1e-60, then interval characteristic polynomials')
    ok_i = claim_i(out=info)
    print('   924 r6 in %s' % mp.iv.nstr(info['v924'], 40))
    print('   (n-,n0,n+) = %s; zero multiplicity of S_u %d; negative simple roots in nu: %d' % (info['sig'], info['mS'], info['nroots']))
    print('   nu roots, unit u: %s' % ', '.join(mp.nstr(r, 12) for r in info['negs']))
    print('   |J|^2 in %s' % mp.iv.nstr(info['J2'], 25))
    report('I', ok_i)
    print('J  R2\'s lines {5/2, -5/2}, {7/2, -7/2}, {3/2, -3/2}: Q constant')
    report('J', claim_j())
    print('K  R2: the lifts of Q - 144/143 with |w|^2 and |w|^4 are not positive semidefinite')
    print('   smallest eigenvalues: %.6f (|w|^2), %.6f (|w|^4)' % (lift_min(1), lift_min(2)))
    report('K', claim_k())
    arms = (('beta off by 1% (A)', not claim_a(beta_factor=R(101, 100))),
            ('the prism with sqrt 47 (B)', not claim_b(prism_root=47)),
            ('the scaling 3/4 in place of 9/16 (C)', not claim_c(scale=R(3, 4))),
            ('the line point t = 6 (D)', not claim_d(line_t=6)),
            ('the Sp(1) directions dropped (E)', not claim_e(sp1=False)),
            ('weight 5/2 at the physical structure only (F)', not claim_f(only_i=True)),
            ('a Krein-negative plus a Krein-positive cluster of v2 (G)', not claim_g(mixed=True)),
            ('the 6-fold rotation about z (H)', not claim_h(sixfold=True)),
            ('the Krawczyk box centered 1e-40 away (I)', not claim_i(shift='1e-40')),
            ('the line {7/2, -3/2} (J)', not claim_j(lines=((0, 5),))),
            ('the lift of Q - 144/143 + 1/2 (K)', not claim_k(shift=0.5)))
    print('arms')
    for label, red in arms:
        print('   arm: %-58s %s' % (label, 'RED' if red else 'GREEN'))
    print('%d claims failed; %d/%d arms red' % (failed, sum(r for _, r in arms), len(arms)))


if __name__ == '__main__':
    main()
