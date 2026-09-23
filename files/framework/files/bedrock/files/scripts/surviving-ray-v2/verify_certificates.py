#!/usr/bin/env python3
"""Surviving Ray v2, Section 7.2: re-check the three outside-orbit certificates from their published data, and test
the same machinery on M8.12's exact census points. Requires NumPy, SymPy and mpmath; reads sr_v2_certificates.json
beside it and nothing else. Nothing here depends on how the certified points were found.

Model. A state u in V_3 is the binary sextic P_u(x, y) = sum_k w_k x^k y^(6-k), with w_k = sqrt(C(6, k)) u_(k-3) in
the weight basis, and the Bombieri inner product <P, Q> = sum_k conj(p_k) q_k / C(6, k). Time reversal is
P_(Theta u)(x, y) = -conj(P_u)(y, -x). By Lemma 7.3, r6 = ||rho_6||^2 = [P_u P_(Theta u)]^2, the Bombieri norm of the
degree-12 product: a real quartic in the 14 real coordinates (Re w_0..Re w_6, Im w_0..Im w_6), with rational
coefficients, so 60-digit interval arithmetic evaluates it exactly up to outward rounding. The rotation generators
x d/dy, y d/dx and (x d/dx - y d/dy)/2 have rational matrices.

For each orbit, at its published box:
1. Critical orbit. On the published fixed set (x = B y, B rational), the system
   B^T (grad r - 2 mu G x - sum_k nu_k G T_k x) = 0, x^T G x = 1, <B^T G T_k x_c, y - y_c> = 0
   (one slice for each continuous symmetry, through the published centre) passes the Krawczyk test at the published
   radius: exactly one zero lies in the box, and by symmetric criticality it is critical on the whole sphere.
2. Isotropy. From below: the published fixed set is fixed, exactly, by the stated group. From above: the six
   Majorana points of the box, enclosed in disjoint boxes after a fixed rational rotation, admit only
   distance-preserving permutations, counted and split into proper and improper by a determinant's sign.
3. Signatures. The bordered second variation over the box is made congruent by the eigenvectors of its centre, and
   when every Gershgorin disc misses zero its inertia is certified (Sylvester): on the whole sphere, on the fixed set,
   and, for the two orbits with a unitary C2, on its complex fixed set.
4. Values: 924 r6 over the box.
Controls: M8.12's exact representatives, certified here from exact points. Arms: planted failures, each on a green
parent, must be caught.
"""
import hashlib
import itertools
import json
import sys
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import mpmath
import numpy as np
import sympy as sp
from mpmath import iv, mp

mp.dps = 60
iv.dps = 60
HERE = Path(__file__).resolve().parent
DATA = HERE / 'sr_v2_certificates.json'
print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
print(f'data {DATA.name}: SHA-256 {hashlib.sha256(DATA.read_bytes()).hexdigest()}')
print(f'python {sys.version.split()[0]}, sympy {sp.__version__}, numpy {np.__version__}, mpmath {mpmath.__version__}')
RES = []


def gate(name, ok):
    RES.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    return bool(ok)


# ---------------------------------------------------------------- 1. the model
A = sp.symbols('a0:7', real=True)
Bv = sp.symbols('b0:7', real=True)
V = list(A) + list(Bv)
W = [A[k] + sp.I * Bv[k] for k in range(7)]
Wt = [(-1) ** (j + 1) * sp.conjugate(W[6 - j]) for j in range(7)]          # P_(Theta u)
Cc = [sp.expand(sum(W[k] * Wt[j - k] for k in range(7) if 0 <= j - k <= 6)) for j in range(13)]
r_expr = sp.expand(sum(sp.expand(Cc[j] * sp.conjugate(Cc[j])) / sp.binomial(12, j) for j in range(13)))
N_expr = sum((A[k] ** 2 + Bv[k] ** 2) / sp.binomial(6, k) for k in range(7))
grad_expr = [sp.diff(r_expr, v) for v in V]
hess_pairs = [(i, j) for i in range(14) for j in range(i, 14)]
hess_expr = [sp.diff(grad_expr[i], V[j]) for i, j in hess_pairs]


def to_terms(expr):
    P = sp.Poly(sp.expand(expr), *V)
    return [(m, Fr(int(c.p), int(c.q))) for m, c in P.terms()]


class Bank:
    """Polynomials sharing one monomial table, evaluated in mp or iv."""

    def __init__(self, exprs):
        tls = [to_terms(e) for e in exprs]
        index = {}
        for tl in tls:
            for m, _ in tl:
                index.setdefault(m, len(index))
        self.monos = list(index)
        self.polys = [[(index[m], c) for m, c in tl] for tl in tls]
        self.cache = {}

    def __call__(self, x, ctx):
        if id(ctx) not in self.cache:
            self.cache[id(ctx)] = [[ctx.mpf(c.numerator) / c.denominator for _, c in tl] for tl in self.polys]
        pw = [[ctx.mpf(1)] + [xi ** e for e in range(1, 5)] for xi in x]
        mv = []
        for m in self.monos:
            v = ctx.mpf(1)
            for i, e in enumerate(m):
                if e:
                    v = v * pw[i][e]
            mv.append(v)
        out = []
        for tl, cl in zip(self.polys, self.cache[id(ctx)]):
            s = ctx.mpf(0)
            for (idx, _), c in zip(tl, cl):
                s += mv[idx] * c
            out.append(s)
        return out


GRAD, HESS, RN = Bank(grad_expr), Bank(hess_expr), Bank([r_expr, N_expr])
gate('r = [P_u P_(Theta u)]^2 is a real polynomial with rational coefficients', not r_expr.has(sp.I))

# generators: J+ = x d/dy, J- = y d/dx, Jz = (x d/dx - y d/dy)/2 on the coefficients
Jp = [[Fr(0)] * 7 for _ in range(7)]
Jm = [[Fr(0)] * 7 for _ in range(7)]
for k in range(7):
    if k < 6:
        Jp[k + 1][k] = Fr(6 - k)
    if k > 0:
        Jm[k - 1][k] = Fr(k)
Jz = [[Fr(k - 3) if i == k else Fr(0) for k in range(7)] for i in range(7)]
Z7 = [[Fr(0)] * 7 for _ in range(7)]
I7 = [[Fr(int(i == j)) for j in range(7)] for i in range(7)]


def madd(X, Y, s=1):
    return [[X[i][j] + s * Y[i][j] for j in range(7)] for i in range(7)]


def mscale(X, s):
    return [[s * X[i][j] for j in range(7)] for i in range(7)]


def realrep(Are, Aim):
    """The real 14 x 14 matrix of Are + i Aim acting on (Re w, Im w)."""
    return [Are[i] + [-x for x in Aim[i]] for i in range(7)] + [Aim[i] + Are[i] for i in range(7)]


FxH = mscale(madd(Jp, Jm), Fr(1, 2))                      # Fx = (J+ + J-)/2
FyA = mscale(madd(Jp, Jm, -1), Fr(1, 2))                  # Fy = -i (J+ - J-)/2
GEN = {'T0': realrep(Z7, I7), 'Tx': realrep(Z7, FxH), 'Ty': realrep(FyA, Z7), 'Tz': realrep(Z7, Jz)}
Gd = [Fr(1, comb(6, k)) for k in range(7)] * 2            # the Bombieri metric


def cmat(M, ctx):
    return [[ctx.mpf(q.numerator) / q.denominator for q in row] for row in M]


def matvec(M, x, ctx):
    return [sum((M[i][j] * x[j] for j in range(len(x)) if M[i][j] != 0), ctx.mpf(0)) for i in range(len(M))]


def value924(x, ctx):
    r, N = RN(x, ctx)
    return 924 * r / (N * N)


def exact(t):
    """The exact rational value of an mpf."""
    m, e = mp.mpf(t).man_exp
    return Fr(int(m)) * (Fr(2) ** int(e))


def contains(v, q):
    """Whether the interval v contains the rational q, exactly."""
    return exact(v.a) <= q <= exact(v.b)


# ---------------------------------------------------------------- 2. the critical system and the Krawczyk test
class CritSystem:
    def __init__(self, B, slices, yc):
        self.B = B
        self.d = 14 if B is None else len(B[0])
        self.T = [GEN[s] for s in slices]
        self.n = self.d + 1 + len(slices)
        xc = self.xof([mp.mpf(v) for v in yc], mp)
        G = [mp.mpf(q.numerator) / q.denominator for q in Gd]
        self.yc = [mp.mpf(v) for v in yc]
        self.cov = []
        for T in self.T:
            s = matvec(cmat(T, mp), xc, mp)
            self.cov.append(self.BT([G[i] * s[i] for i in range(14)], mp))

    def xof(self, y, ctx):
        if self.B is None:
            return list(y)
        return [sum((ctx.mpf(self.B[i][j].numerator) / self.B[i][j].denominator * y[j]
                     for j in range(self.d) if self.B[i][j] != 0), ctx.mpf(0)) for i in range(14)]

    def BT(self, v, ctx):
        if self.B is None:
            return list(v)
        return [sum((ctx.mpf(self.B[i][j].numerator) / self.B[i][j].denominator * v[i]
                     for i in range(14) if self.B[i][j] != 0), ctx.mpf(0)) for j in range(self.d)]

    def F(self, z, ctx):
        d = self.d
        y, mu, nu = z[:d], z[d], z[d + 1:]
        x = self.xof(y, ctx)
        G = [ctx.mpf(q.numerator) / q.denominator for q in Gd]
        g = GRAD(x, ctx)
        vec = [g[i] - 2 * mu * G[i] * x[i] for i in range(14)]
        for k, T in enumerate(self.T):
            tx = matvec(cmat(T, ctx), x, ctx)
            vec = [vec[i] - nu[k] * G[i] * tx[i] for i in range(14)]
        out = self.BT(vec, ctx)
        out.append(sum((G[i] * x[i] * x[i] for i in range(14)), ctx.mpf(0)) - 1)
        for k in range(len(self.T)):
            out.append(sum((ctx.mpf(self.cov[k][j]) * (y[j] - ctx.mpf(self.yc[j])) for j in range(d)), ctx.mpf(0)))
        return out

    def hess_L(self, x, mu, ctx, drop_mu=False):
        G = [ctx.mpf(q.numerator) / q.denominator for q in Gd]
        H = [[ctx.mpf(0)] * 14 for _ in range(14)]
        for (i, j), v in zip(hess_pairs, HESS(x, ctx)):
            H[i][j] = v
            H[j][i] = v
        if not drop_mu:
            for i in range(14):
                H[i][i] = H[i][i] - 2 * mu * G[i]
        return H, G

    def restrict(self, H, ctx):
        if self.B is None:
            return H
        d = self.d
        HB = [[sum((H[i][l] * (ctx.mpf(self.B[l][j].numerator) / self.B[l][j].denominator)
                    for l in range(14) if self.B[l][j] != 0), ctx.mpf(0)) for j in range(d)] for i in range(14)]
        cols = [self.BT([HB[i][j] for i in range(14)], ctx) for j in range(d)]
        return [[cols[j][i] for j in range(d)] for i in range(d)]

    def J(self, z, ctx):
        d, n = self.d, self.n
        y, mu, nu = z[:d], z[d], z[d + 1:]
        x = self.xof(y, ctx)
        H, G = self.hess_L(x, mu, ctx)
        Tcs = [cmat(T, ctx) for T in self.T]
        for k, Tc in enumerate(Tcs):
            for i in range(14):
                for j in range(14):
                    if Tc[i][j] != 0:
                        H[i][j] = H[i][j] - nu[k] * G[i] * Tc[i][j]
        A_ = self.restrict(H, ctx)
        Jac = [[ctx.mpf(0)] * n for _ in range(n)]
        for i in range(d):
            for j in range(d):
                Jac[i][j] = A_[i][j]
        BGx = self.BT([G[i] * x[i] for i in range(14)], ctx)
        for i in range(d):
            Jac[i][d] = -2 * BGx[i]
            Jac[d][i] = 2 * BGx[i]
        for k, Tc in enumerate(Tcs):
            tx = matvec(Tc, x, ctx)
            col = self.BT([G[i] * tx[i] for i in range(14)], ctx)
            for i in range(d):
                Jac[i][d + 1 + k] = -col[i]
                Jac[d + 1 + k][i] = ctx.mpf(self.cov[k][i])
        return Jac


def krawczyk(S, zc, rho):
    """True, box when K(X) lies in the interior of X = zc + [-rho, rho]^n."""
    n = S.n
    zc = [mp.mpf(v) for v in zc]
    try:
        Y = mp.inverse(mp.matrix(S.J(zc, mp)))
    except ZeroDivisionError:
        return False, None
    zi = [iv.mpf(v) for v in zc]
    Fc = S.F(zi, iv)
    box = [iv.mpf([v - rho, v + rho]) for v in zc]
    JX = S.J(box, iv)
    Yi = [[iv.mpf(Y[i, j]) for j in range(n)] for i in range(n)]
    YF = [sum((Yi[i][j] * Fc[j] for j in range(n)), iv.mpf(0)) for i in range(n)]
    YJ = [[sum((Yi[i][l] * JX[l][j] for l in range(n)), iv.mpf(0)) for j in range(n)] for i in range(n)]
    D = [box[i] - zi[i] for i in range(n)]
    K = [zi[i] - YF[i] + sum((((1 if i == j else 0) - YJ[i][j]) * D[j] for j in range(n)), iv.mpf(0))
         for i in range(n)]
    return all(K[i].a > box[i].a and K[i].b < box[i].b for i in range(n)), box


# ---------------------------------------------------------------- 3. inertia
def inertia(S, zc, box, drop_mu=False, with_slices=True):
    """Certified (n-, 0, n+) of the second variation on the tangent space of S's sphere modulo its slices, from the
    bordered matrix [[B^T H_L B, C], [C^T, 0]] over the box; None when a Gershgorin disc meets zero."""
    d = S.d

    def bordered(y, mu, ctx):
        x = S.xof(y, ctx)
        H, G = S.hess_L(x, mu, ctx, drop_mu)
        A_ = S.restrict(H, ctx)
        cols = [S.BT([G[i] * x[i] for i in range(14)], ctx)]
        if with_slices:
            cols += [[ctx.mpf(v) for v in c] for c in S.cov]
        m = len(cols)
        M = [[ctx.mpf(0)] * (d + m) for _ in range(d + m)]
        for i in range(d):
            for j in range(d):
                M[i][j] = A_[i][j]
        for k, c in enumerate(cols):
            for i in range(d):
                M[i][d + k] = c[i]
                M[d + k][i] = c[i]
        return M, m

    Mi, m = bordered(box[:d], box[d], iv)
    Mc, _ = bordered([mp.mpf(v) for v in zc[:d]], mp.mpf(zc[d]), mp)
    n = len(Mi)
    _, Q = mp.eigsy(mp.matrix(Mc))
    Qi = [[iv.mpf(Q[i, j]) for j in range(n)] for i in range(n)]
    MQ = [[sum((Mi[i][l] * Qi[l][j] for l in range(n)), iv.mpf(0)) for j in range(n)] for i in range(n)]
    K = [[sum((Qi[l][i] * MQ[l][j] for l in range(n)), iv.mpf(0)) for j in range(n)] for i in range(n)]
    neg = pos = 0
    for i in range(n):
        rad = sum((abs(K[i][j]) for j in range(n) if j != i), iv.mpf(0))
        lo, hi = (K[i][i] - rad).a, (K[i][i] + rad).b
        if lo > 0:
            pos += 1
        elif hi < 0:
            neg += 1
        else:
            return None
    return (neg - m, 0, pos - m)


FULL_SLICES = ['T0', 'Tx', 'Ty', 'Tz']


def full_at(S, zc, box, **kw):
    """The full transverse signature over the box of a fixed-set certificate (same point, same multiplier)."""
    d = S.d
    xc = S.xof([mp.mpf(v) for v in zc[:d]], mp)
    Sf = CritSystem(None, FULL_SLICES, xc)
    return inertia(Sf, xc + [mp.mpf(zc[d])], S.xof(box[:d], iv) + [box[d]], **kw)


def char_subspace(k_main, m0, chi_x=None):
    """Rational basis (14 x d) of {w : R_z(2 pi/k) w = e^(-2 pi i m0/k) w [, R_x(pi) w = chi_x w]}, as complex
    columns (a real and an imaginary column for each)."""
    S1 = [j for j in range(7) if (j - 3 - m0) % k_main == 0]
    vecs = []
    if chi_x is None:
        vecs = [{j: Fr(1)} for j in S1]
    else:
        for j in S1:
            if j < 3 and (6 - j) in S1:
                vecs.append({j: Fr(1), 6 - j: Fr(-chi_x)})
            elif j == 3 and chi_x == -1:
                vecs.append({3: Fr(1)})
    cols = []
    for v in vecs:
        cols.append([v.get(i, Fr(0)) for i in range(7)] + [Fr(0)] * 7)
        cols.append([Fr(0)] * 7 + [v.get(i, Fr(0)) for i in range(7)])
    return [[cols[c][i] for c in range(len(cols))] for i in range(14)]


def real_columns(Bc):
    return [[row[c] for c in range(0, len(row), 2)] for row in Bc]


def c2_signature(S, zc, box, m0):
    """The signature on the complex C2 fixed set of character m0, over the box of a certificate whose fixed set is
    the real part of it; None, False if the fixed set is not inside that subspace."""
    d = S.d
    Bc = char_subspace(2, m0)
    if len(Bc[0]) != 2 * d or any(S.B[i][c] != Bc[i][2 * c] for i in range(14) for c in range(d)):
        return None, False
    yc, yb = [], []
    for c in range(d):
        yc += [mp.mpf(zc[c]), mp.mpf(0)]
        yb += [box[c], iv.mpf(0)]
    Sc = CritSystem(Bc, ['T0', 'Tz'], yc)
    return inertia(Sc, yc + [mp.mpf(zc[d])], yb + [box[d]]), True


# ---------------------------------------------------------------- 4. the Majorana points and their permutations
class CI:
    def __init__(self, re_, im_):
        self.re, self.im = re_, im_

    def __add__(self, o):
        return CI(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CI(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return CI(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)


def poly_eval(coefs, zc):
    acc = CI(iv.mpf(0), iv.mpf(0))
    for c in reversed(coefs):
        acc = acc * zc + c
    return acc


def overlap(p, q):
    return not (p.b < q.a or q.b < p.a)


def _gen_rotation():
    """The exact substitution matrix of the SU(2) element of the rational unit quaternion (2, 4, 5, 6)/9, applied
    before the points are isolated so that none sits at a pole of a chart; it moves the constellation rigidly."""
    a, b, c, d = (sp.Rational(n, 9) for n in (2, 4, 5, 6))
    U11, U12, U21, U22 = a + sp.I * b, -c + sp.I * d, c + sp.I * d, a - sp.I * b
    X_, Y_ = sp.symbols('X_ Y_')
    M = [[None] * 7 for _ in range(7)]
    for k in range(7):
        P = sp.Poly(sp.expand((U11 * X_ + U12 * Y_) ** k * (U21 * X_ + U22 * Y_) ** (6 - k)), X_, Y_)
        for j in range(7):
            cf = sp.nsimplify(P.coeff_monomial(X_ ** j * Y_ ** (6 - j)))
            M[j][k] = (Fr(int(sp.re(cf).p), int(sp.re(cf).q)), Fr(int(sp.im(cf).p), int(sp.im(cf).q)))
    return M


M_GEN = _gen_rotation()


def star_boxes(wre, wim):
    """Six certified root boxes of F_u(z) = P_u(1, -z) on the sphere, from interval coefficients, after M_GEN."""
    rre, rim = [], []
    for j in range(7):
        sr, si = iv.mpf(0), iv.mpf(0)
        for k in range(7):
            mr, mi = M_GEN[j][k]
            if mr == 0 and mi == 0:
                continue
            mrI, miI = iv.mpf(mr.numerator) / mr.denominator, iv.mpf(mi.numerator) / mi.denominator
            sr += mrI * wre[k] - miI * wim[k]
            si += mrI * wim[k] + miI * wre[k]
        rre.append(sr)
        rim.append(si)
    wc = [complex(float(mp.mpf(rre[k].mid)), float(mp.mpf(rim[k].mid))) for k in range(7)]
    wI = [CI(rre[k], rim[k]) for k in range(7)]
    zpoly = [CI((-1) ** j * wI[6 - j].re, (-1) ** j * wI[6 - j].im) for j in range(7)]
    ypoly = [CI((-1) ** k * wI[k].re, (-1) ** k * wI[k].im) for k in range(7)]
    if abs(wc[0]) >= abs(wc[6]):
        roots = np.roots([(-1) ** j * wc[6 - j] for j in range(6, -1, -1)])
    else:
        roots = 1 / np.roots([(-1) ** k * wc[k] for k in range(6, -1, -1)])
    if len(roots) != 6:
        return None
    pts = []
    for z0 in roots:
        chart, c0, coefs = ('z', z0, zpoly) if abs(z0) <= 1 else ('y', 1 / z0, ypoly)
        dco = [CI(iv.mpf(j) * coefs[j].re, iv.mpf(j) * coefs[j].im) for j in range(1, 7)]
        cm = mp.mpc(c0.real, c0.imag)
        pm = [mp.mpc(mp.mpf(coefs[j].re.mid), mp.mpf(coefs[j].im.mid)) for j in range(7)]
        for _ in range(60):
            step = sum(pm[j] * cm ** j for j in range(7)) / sum(j * pm[j] * cm ** (j - 1) for j in range(1, 7))
            cm -= step
            if abs(step) < mp.mpf(10) ** -55:
                break
        yinv = 1 / sum(j * pm[j] * cm ** (j - 1) for j in range(1, 7))
        ok = False
        for rs in ('1e-40', '1e-30', '1e-20', '1e-12'):
            rho = mp.mpf(rs)
            Zb = CI(iv.mpf([cm.real - rho, cm.real + rho]), iv.mpf([cm.imag - rho, cm.imag + rho]))
            cc = CI(iv.mpf(cm.real), iv.mpf(cm.imag))
            yI = CI(iv.mpf(yinv.real), iv.mpf(yinv.imag))
            K = cc - yI * poly_eval(coefs, cc) + (CI(iv.mpf(1), iv.mpf(0)) - yI * poly_eval(dco, Zb)) * (Zb - cc)
            if K.re.a > Zb.re.a and K.re.b < Zb.re.b and K.im.a > Zb.im.a and K.im.b < Zb.im.b:
                ok = True
                break
        if not ok:
            return None
        s, t = Zb.re, Zb.im
        den = 1 + s * s + t * t
        pts.append((2 * s / den, 2 * t / den, (1 - s * s - t * t) / den) if chart == 'z' else
                   (2 * s / den, -2 * t / den, (s * s + t * t - 1) / den))
    for i in range(6):
        for j in range(i + 1, 6):
            if all(overlap(pts[i][c], pts[j][c]) for c in range(3)):
                return None
    return pts


def permutation_count(pts):
    """(proper, improper, undecided): the permutations of the six points compatible with all 15 distance
    enclosures, split by the sign of a determinant."""
    def dist2(P, Q):
        return sum(((P[c] - Q[c]) * (P[c] - Q[c]) for c in range(3)), iv.mpf(0))

    def det3(P, Q, R):
        return (P[0] * (Q[1] * R[2] - Q[2] * R[1]) - P[1] * (Q[0] * R[2] - Q[2] * R[0])
                + P[2] * (Q[0] * R[1] - Q[1] * R[0]))
    D = [[dist2(pts[i], pts[j]) if i != j else iv.mpf(0) for j in range(6)] for i in range(6)]
    surv = [sg for sg in itertools.permutations(range(6))
            if all(overlap(D[i][j], D[sg[i]][sg[j]]) for i in range(6) for j in range(i + 1, 6))]
    cent = [[float(mp.mpf(P[c].mid)) for c in range(3)] for P in pts]
    tri = max(itertools.combinations(range(6), 3), key=lambda t: abs(np.linalg.det(np.array([cent[i] for i in t]))))
    d0 = det3(*[pts[i] for i in tri])
    rot = refl = und = 0
    for sg in surv:
        d1 = det3(*[pts[sg[i]] for i in tri])
        if (d0.a > 0 and d1.a > 0) or (d0.b < 0 and d1.b < 0):
            rot += 1
        elif (d0.a > 0 and d1.b < 0) or (d0.b < 0 and d1.a > 0):
            refl += 1
        else:
            und += 1
    return rot, refl, und


def stars_of(S, box):
    xb = S.xof(box[:S.d], iv)
    pts = star_boxes(xb[:7], xb[7:14])
    return None if pts is None else permutation_count(pts)


# ---------------------------------------------------------------- 5. the group, from below, exactly
def fixed_by_group(B, m0):
    """True when every column of B is real (so fixed, up to the phase -1, by Theta R_y(pi), which acts as
    w -> -conj(w)) and, if m0 is not None, supported on the weights k - 3 = m0 mod 2 (so multiplied by
    e^(-i pi m0) = (-1)^m0 by R_z(pi))."""
    for c in range(len(B[0])):
        if any(B[7 + i][c] != 0 for i in range(7)):
            return False
        if m0 is not None and any(B[i][c] != 0 and (i - 3 - m0) % 2 != 0 for i in range(7)):
            return False
    return True


# convention gate: Theta R_y(pi) acts as w -> -conj(w), and R_z(pi) as w_k -> (-1)^(k-3) w_k
mp.dps = 50
Fy_c = mp.matrix([[mp.mpc(0, -1) * (mp.mpf(FyA[i][j].numerator) / FyA[i][j].denominator) for j in range(7)]
                  for i in range(7)])
Dy = mp.expm(Fy_c * mp.mpc(0, -mp.pi))
Dz = mp.expm(mp.matrix([[mp.mpc(0, -mp.pi) * (k - 3) if i == k else 0 for k in range(7)] for i in range(7)]))
rng = np.random.default_rng(3)
dev_y = dev_z = mp.mpf(0)
for _ in range(5):
    w = mp.matrix([mp.mpc(float(rng.normal()), float(rng.normal())) for _ in range(7)])
    Dw = Dy * w
    theta = [(-1) ** (j + 1) * mp.conj(Dw[6 - j]) for j in range(7)]
    dev_y = max(dev_y, max(abs(theta[j] + mp.conj(w[j])) for j in range(7)))
    Dzw = Dz * w
    dev_z = max(dev_z, max(abs(Dzw[k] - (-1) ** (k - 3) * w[k]) for k in range(7)))
mp.dps = 60
gate(f'convention: Theta R_y(pi) acts as w -> -conj(w) (deviation {mp.nstr(dev_y, 3)}) and R_z(pi) as '
     f'w_k -> (-1)^(k-3) w_k (deviation {mp.nstr(dev_z, 3)})', dev_y < mp.mpf('1e-40') and dev_z < mp.mpf('1e-40'))


# ---------------------------------------------------------------- 6. controls: M8.12's exact representatives
def exact_point(rep):
    """A unit vector (14 mp reals) from M8.12's representative {m: c_m} in the weight basis."""
    w = [sp.sqrt(comb(6, k)) * sp.sympify(rep.get(k - 3, 0)) for k in range(7)]
    N = sp.nsimplify(sum(sp.Abs(v) ** 2 / comb(6, k) for k, v in enumerate(w)))
    w = [sp.nsimplify(v / sp.sqrt(N)) for v in w]
    return [mp.mpf(sp.re(v).evalf(80)) for v in w] + [mp.mpf(sp.im(v).evalf(80)) for v in w], w


def coords_in(B, x):
    """The coordinates y with x = B y, for a basis whose columns have disjoint supports, read at each column's first
    nonzero entry (x must lie in the span; the Krawczyk test would fail otherwise)."""
    y = []
    for c in range(len(B[0])):
        i = next(i for i in range(14) if B[i][c] != 0)
        y.append(x[i] / (mp.mpf(B[i][c].numerator) / B[i][c].denominator))
    return y


def certify_exact(x, B=None, slices=(), radii=('1e-50', '1e-45', '1e-40')):
    """Krawczyk at an exact critical point: centre (y, mu = 2 r, nu = 0)."""
    y = x if B is None else coords_in(B, x)
    S = CritSystem(B, list(slices), y)
    zc = list(y) + [2 * RN(x, mp)[0]] + [mp.mpf(0)] * len(slices)
    for rs in radii:
        ok, box = krawczyk(S, zc, mp.mpf(rs))
        if ok:
            return S, zc, box, rs
    return S, zc, None, None


REPS = {'octahedron': {2: 1, -2: 1}, 'hexagon': {3: 1, -3: 1}, 'pyramid': {3: sp.sqrt(12), -2: sp.sqrt(13)},
        'prism': {3: 1, 0: sp.sqrt(sp.Rational(23, 10)), -3: 1}, 'C3ray': {2: 1, -1: 2},
        'D2ray': {2: 1, 0: sp.I * sp.sqrt(sp.Rational(6, 5)), -2: 1}}
M812_FULL = {'octahedron': (6, 0, 3), 'hexagon': (9, 0, 0), 'pyramid': (5, 0, 4), 'prism': (3, 0, 6),
             'C3ray': (5, 0, 4), 'D2ray': (5, 0, 4)}
M812_VALUE = {'octahedron': Fr(288), 'hexagon': Fr(463), 'pyramid': Fr(1188, 5), 'prism': Fr(8800, 43),
              'C3ray': Fr(1188, 5), 'D2ray': Fr(225)}
WEIGHT = {3: Fr(1), 2: Fr(36), 1: Fr(225), 0: Fr(400)}
vals = {m: value924(exact_point({m: 1})[0], iv) for m in WEIGHT}
gate('the model gives M8.12\'s values 924 r6 = 1, 36, 225, 400 at the weight states v3, v2, v1, v0',
     all(contains(vals[m], q) for m, q in WEIGHT.items()))
print('\ncontrols: the six finite-stabiliser census orbits of M8.12, from its exact representatives')
CTRL = {}
for name, rep in REPS.items():
    x, _ = exact_point(rep)
    S, zc, box, rs = certify_exact(x, None, FULL_SLICES)
    ok = box is not None
    sig = inertia(S, zc, box) if ok else None
    v = value924(S.xof(box[:14], iv), iv) if ok else None
    q = M812_VALUE[name]
    inside = ok and contains(v, q)
    CTRL[name] = dict(S=S, zc=zc, box=box, sig=sig)
    print(f'  {name}: certified on the whole sphere at radius {rs}; signature {sig}; M8.12 {M812_FULL[name]}',
          flush=True)
    gate(f'control {name}: certified from its exact point; signature equals M8.12\'s {M812_FULL[name]}; 924 r6 '
         f'encloses {q}', ok and sig == M812_FULL[name] and inside)

print('\ncontrols in their own fixed sets: the pyramid (C5, real) and the prism (D3, real), from exact points')
FIXED_CTRL = {'pyramid': (real_columns(char_subspace(5, 3)), (5, 5), (1, 0, 0)),
              'prism': (real_columns(char_subspace(3, 0, -1)), (6, 6), (0, 0, 1))}
FC = {}
for name, (B, stars_exp, line_sig) in FIXED_CTRL.items():
    x, _ = exact_point(REPS[name])
    S, zc, box, rs = certify_exact(x, B)
    ok = box is not None
    st = stars_of(S, box) if ok else None
    sf = full_at(S, zc, box) if ok else None
    sj = inertia(S, zc, box) if ok else None
    FC[name] = dict(S=S, zc=zc, box=box)
    print(f'  {name}: fixed set of real dimension {S.d}, certified at radius {rs}; stars (proper, improper, '
          f'undecided) {st}; full {sf}; on the fixed set {sj}', flush=True)
    gate(f'control {name}: isotropy order {sum(stars_exp)} ({stars_exp[0]} proper, {stars_exp[1]} improper) from the '
         f'stars of its box; full signature {M812_FULL[name]}; on its fixed set {line_sig}, its line extremum',
         ok and st == stars_exp + (0,) and sf == M812_FULL[name] and sj == line_sig)

d2 = CTRL['D2ray']
st_d2 = stars_of(d2['S'], d2['box']) if d2['box'] is not None else None
gate(f'control D2 ray: isotropy order 8 (4 proper, 4 improper) from the stars of its whole-sphere box ({st_d2})',
     st_d2 == (4, 4, 0))

# ---------------------------------------------------------------- 7. the three outside orbits, from the data
data = json.loads(DATA.read_text(encoding='utf-8'))
EXPECT = {'O1': ('T1', 4, (2, 2), (4, 0, 5), (1, 0, 2), (2, 0, 3), '215.7757925'),
          'O2': ('T2', 2, (1, 1), (6, 0, 3), (4, 0, 1), None, '238.0165289'),
          'O3': ('T3', 4, (2, 2), (7, 0, 2), (2, 0, 1), (3, 0, 2), '238.3568547')}
print('\nthe three outside orbits, each re-checked at its published box')
ORB = {}
for label, (key, order, split, e_full, e_fix, e_c2, head) in EXPECT.items():
    o = data['orbits'][key]
    B = [[Fr(q) for q in row] for row in o['basis_14xd']]
    m0 = o['fixed_set'].get('character_m0')
    rebuilt = real_columns(char_subspace(2, m0) if m0 is not None else char_subspace(1, 0))
    gate(f'{label}: the published fixed set is the real part of the {"C2 character subspace m0 = " + str(m0) if m0 is not None else "whole space"}, '
         f'and the stated group fixes it exactly', B == rebuilt and fixed_by_group(B, m0))
    zc = [mp.mpf(s) for s in o['centre']]
    S = CritSystem(B, o['slices'], zc[:len(B[0])])
    ok, box = krawczyk(S, zc, mp.mpf(o['radius']))
    ORB[label] = dict(S=S, zc=zc, box=box, m0=m0, o=o)
    gate(f'{label}: the Krawczyk test passes at the published centre and radius {o["radius"]}: one critical orbit '
         f'in the box (fixed-set dimension {S.d}, slices {o["slices"]})', ok)
    if not ok:
        continue
    st = stars_of(S, box)
    gate(f'{label}: isotropy of order {order} from the stars of this box ({st})', st == split + (0,) and
         sum(split) == order == o['isotropy_order'])
    v = value924(S.xof(box[:S.d], iv), iv)
    width = mp.mpf(v.b) - mp.mpf(v.a)
    lo_s, hi_s = mp.nstr(mp.mpf(v.a), 55), mp.nstr(mp.mpf(v.b), 55)
    print(f'  {label}: 924 r6 in [{lo_s}, {hi_s}], width {mp.nstr(width, 3)}', flush=True)
    ORB[label].update(v=v, width=width)
    gate(f'{label}: the value enclosure has width below 1e-50 and begins {head}…, as Section 7.2 prints',
         width < mp.mpf('1e-50') and lo_s.startswith(head) and hi_s.startswith(head))
    sf, sj = full_at(S, zc, box), inertia(S, zc, box)
    sc = c2_signature(S, zc, box, m0)[0] if m0 is not None else None
    print(f'  {label}: signatures: full {sf}, on the isotropy fixed set {sj}' +
          (f', on the complex C2 fixed set {sc}' if m0 is not None else ''), flush=True)
    ORB[label].update(sf=sf, sj=sj, sc=sc)
    gate(f'{label}: signatures certified as Section 7.2 prints them: full {e_full}, on the isotropy fixed set {e_fix}'
         + (f', on the C2 fixed set {e_c2}' if e_c2 else ''), (sf, sj, sc) == (e_full, e_fix, e_c2))

q = Fr(28800, 121)
if ORB['O2'].get('v') is not None:
    v = ORB['O2']['v']
    gate('O2: 28800/121 lies in its value enclosure', contains(v, q))

# ---------------------------------------------------------------- 8. arms, each on a green parent
print('\narms')
o1 = ORB['O1']
parent = o1.get('box') is not None
zc_moved = list(o1['zc'])
zc_moved[0] += mp.mpf('1e-50')
ok_moved, _ = krawczyk(o1['S'], zc_moved, mp.mpf(o1['o']['radius'])) if parent else (True, None)
gate('arm: with its centre moved by 1e-50, O1\'s box of radius 1e-55 no longer certifies', parent and not ok_moved)
pyr = FC['pyramid']
parent = pyr['box'] is not None and full_at(pyr['S'], pyr['zc'], pyr['box']) == M812_FULL['pyramid']
arm = full_at(pyr['S'], pyr['zc'], pyr['box'], drop_mu=True) if parent else None
gate(f'arm: without -2 mu G the pyramid\'s full signature changes (to {arm})', parent and arm is not None
     and arm != M812_FULL['pyramid'])
parent = o1.get('sf') == EXPECT['O1'][3]
arm = full_at(o1['S'], o1['zc'], o1['box'], with_slices=False) if parent else 'parent red'
gate('arm: without its slice columns the full bordered matrix at O1\'s box is not certified', parent and arm is None)
parent = o1.get('sc') == EXPECT['O1'][5]
gate('arm: O1\'s fixed set is not inside the complex C2 subspace of the other character',
     parent and not c2_signature(o1['S'], o1['zc'], o1['box'], 1 - o1['m0'])[1])
gate('arm: the stated group check fails for the other character', parent and not fixed_by_group(o1['S'].B, 1 - o1['m0']))
if ORB['O2'].get('v') is not None:
    v = ORB['O2']['v']
    for lab, p in (('28801/121', Fr(28801, 121)), ('28800/121 + 1e-40', q + Fr(1, 10 ** 40)),
                   ('28800/121 - 1e-40', q - Fr(1, 10 ** 40))):
        gate(f'arm: {lab} lies outside O2\'s value enclosure', not contains(v, p))
if pyr['box'] is not None:
    rng = np.random.default_rng(20260922)
    xs = pyr['S'].xof(pyr['zc'][:pyr['S'].d], mp)
    delta = rng.normal(size=14)
    delta /= np.linalg.norm(delta)
    xp = [xs[i] + mp.mpf(float(1e-6 * delta[i])) for i in range(14)]
    Np = RN(xp, mp)[1]
    xp = [t / mp.sqrt(Np) for t in xp]
    pts = star_boxes([iv.mpf(t) for t in xp[:7]], [iv.mpf(t) for t in xp[7:]])
    st = permutation_count(pts) if pts is not None else None
    gate(f'arm: a pyramid displaced by 1e-6 keeps only the identity among its star permutations ({st})',
         st is not None and st[0] == 1 and st[1] == 0)
rng = np.random.default_rng(7)
wr = rng.normal(size=14)
x = [mp.mpf(float(t)) for t in wr]
Nr = RN(x, mp)[1]
x = [t / mp.sqrt(Nr) for t in x]
S = CritSystem(None, FULL_SLICES, x)
ok_r, _ = krawczyk(S, x + [2 * RN(x, mp)[0], 0, 0, 0, 0], mp.mpf('1e-30'))
gate('arm: a random unit state does not certify as critical', not ok_r)
lo_o1 = mp.nstr(mp.mpf(ORB['O1']['v'].a), 55) if ORB['O1'].get('v') is not None else ''
gate('arm: a misprinted value, 215.7757926…, would not match O1\'s enclosure',
     lo_o1.startswith('215.7757925') and not lo_o1.startswith('215.7757926'))
xv0, _ = exact_point({0: 1})
S = CritSystem(None, FULL_SLICES, xv0)
ok_v0, _ = krawczyk(S, xv0 + [2 * RN(xv0, mp)[0], 0, 0, 0, 0], mp.mpf('1e-30'))
gate('arm: v0, whose stabiliser is continuous, does not certify with four slices', not ok_v0)

print('\nsummary')
for label in ('O1', 'O2', 'O3'):
    r = ORB[label]
    if r.get('v') is not None:
        print(f'  {label}: 924 r6 width {mp.nstr(r["width"], 3)}; full {r["sf"]}; isotropy fixed set {r["sj"]}; '
              f'C2 fixed set {r["sc"]}')
print('ALL PASS' if all(RES) else f'{sum(1 for x in RES if not x)} FAILED')
sys.exit(0 if all(RES) else 1)
