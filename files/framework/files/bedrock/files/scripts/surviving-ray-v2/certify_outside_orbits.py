#!/usr/bin/env python3
"""Work item 4, Surviving Ray v2: certify the three critical orbits outside M8.12's class.

The frozen packet is ../work_item_4_packet.md. Its SHA-256 is printed first, and the four inputs it pins
are re-hashed against its table before anything runs; a mismatch stops the run. Controls and arms run
before the targets.

Coordinates: w_0..w_6, the coefficients of the binary sextic P_u (w_k on x^k y^(6-k)), with the Bombieri
inner product. There r = ||rho_6||^2 = [P_u P_(Theta u)]^2 (Lemma 7.3), Theta is
P_(Theta u)(x, y) = -conj(P_u)(y, -x), and the rotation generators are x d/dy, y d/dx, (x d/dx - y d/dy)/2,
all with rational coefficients, so interval evaluation (mpmath.iv, 60 digits) is exact up to outward
rounding. Majorana stars follow v1's Section 2.1: roots of F_u(z) = P_u(1, -z), in two charts.

Standings (named in the packet): CERTIFIED, by the Krawczyk operator, never exact. A certificate that does
not close is reported as NOT CERTIFIED, with the smallest singular value of the Jacobian at the centre and
the radii tried. Morse signatures are printed as reconnaissance only.
"""
import hashlib
import itertools
import re
import sys
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import numpy as np
import scipy.linalg as sla
import sympy as sp
from mpmath import iv, mp
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation

mp.dps = 60
iv.dps = 60

SR = Path(__file__).resolve().parent.parent            # the Surviving Ray folder
MIT = SR.parent
PACKET = SR / 'work_item_4_packet.md'
RESULTS = []


def gate(name, ok):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    return bool(ok)


def stop(msg):
    print('STOP: ' + msg, flush=True)
    sys.exit(2)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# ---------------------------------------------------------------- 0. provenance
print(f'packet {PACKET.name}: SHA-256 {sha(PACKET)}')
print(f'script {Path(__file__).name}: SHA-256 {sha(__file__)}')
pins = re.findall(r'\| `(OpenWave/[^`]+)` \| `([0-9a-f]{64})` \|', PACKET.read_text(encoding='utf-8'))
ok_pins = len(pins) == 4 and all(sha(MIT / p) == h for p, h in pins)
for p, h in pins:
    print(f'  input {p}: {"matches" if sha(MIT / p) == h else "DIFFERS FROM"} the packet pin')
if not gate('the four inputs match the packet pins', ok_pins):
    stop('an input differs from its pin')

# ---------------------------------------------------------------- 1. the polynomial model
A = sp.symbols('a0:7', real=True)
Bv = sp.symbols('b0:7', real=True)
V = list(A) + list(Bv)
W = [A[k] + sp.I * Bv[k] for k in range(7)]
Wt = [(-1) ** (j + 1) * sp.conjugate(W[6 - j]) for j in range(7)]          # P_(Theta u)
Cc = [sp.expand(sum(W[k] * Wt[j - k] for k in range(7) if 0 <= j - k <= 6)) for j in range(13)]
r_expr = sp.expand(sum(sp.expand(Cc[j] * sp.conjugate(Cc[j])) / sp.binomial(12, j) for j in range(13)))
gate('r = [P_u P_(Theta u)]^2 is a real polynomial', not r_expr.has(sp.I))
N_expr = sum((A[k] ** 2 + Bv[k] ** 2) / sp.binomial(6, k) for k in range(7))


def to_terms(expr):
    P = sp.Poly(sp.expand(expr), *V)
    return [(m, Fr(int(c.p), int(c.q))) for m, c in P.terms()]


grad_expr = [sp.diff(r_expr, v) for v in V]
hess_pairs = [(i, j) for i in range(14) for j in range(i, 14)]
hess_expr = [sp.diff(grad_expr[i], V[j]) for i, j in hess_pairs]

# generators on the coefficients: J+ = x d/dy, J- = y d/dx, Jz = (x d/dx - y d/dy)/2
Jp = [[Fr(0)] * 7 for _ in range(7)]
Jm = [[Fr(0)] * 7 for _ in range(7)]
for k in range(7):
    if k < 6:
        Jp[k + 1][k] = Fr(6 - k)
    if k > 0:
        Jm[k - 1][k] = Fr(k)
Jz = [[Fr(k - 3) if i == k else Fr(0) for k in range(7)] for i in range(7)]


def madd(X, Y, s=1):
    return [[X[i][j] + s * Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]


def mscale(X, s):
    return [[s * X[i][j] for j in range(len(X[0]))] for i in range(len(X))]


Z7 = [[Fr(0)] * 7 for _ in range(7)]
I7 = [[Fr(int(i == j)) for j in range(7)] for i in range(7)]


def realrep(Are, Aim):
    """Real 14x14 representation of the complex matrix Are + i Aim acting on (a, b)."""
    top = [Are[i] + [-x for x in Aim[i]] for i in range(7)]
    bot = [Aim[i] + Are[i] for i in range(7)]
    return top + bot


FxH = mscale(madd(Jp, Jm), Fr(1, 2))                     # Fx = (J+ + J-)/2, real
FyA = mscale(madd(Jp, Jm, -1), Fr(1, 2))                 # Fy = -i (J+ - J-)/2: real part 0, imaginary -FyA
T0 = realrep(Z7, I7)                                     # i w
Tx = realrep(Z7, FxH)                                    # i Fx w
Ty = realrep(FyA, Z7)                                    # i Fy w = (J+ - J-)/2 w
Tz = realrep(Z7, Jz)                                     # i Fz w
RFx = realrep(FxH, Z7)
RFy = realrep(Z7, mscale(FyA, -1))
RFz = realrep(Jz, Z7)
Gd = [Fr(1, comb(6, k)) for k in range(7)] * 2           # the Bombieri metric, diagonal


def quad(M, X_):
    """x^T G M x as a sympy expression."""
    return sp.expand(sum(X_[i] * Gd[i] * sum(M[i][j] * X_[j] for j in range(14)) for i in range(14)))


def mmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


fvec = [quad(M, V) for M in (RFx, RFy, RFz)]
f2_expr = sp.expand(sum(f ** 2 for f in fvec))
RF = [RFx, RFy, RFz]
nem = [[quad(mscale(madd(mmul(RF[m], RF[n]), mmul(RF[n], RF[m])), Fr(1, 2)), V) for n in range(3)] for m in range(3)]
trN2_expr = sp.expand(sum(nem[m][n] ** 2 for m in range(3) for n in range(3)))
TW = sp.expand(sum((-1) ** (k + 1) * W[6 - k] * W[k] / sp.binomial(6, k) for k in range(7)))   # <Theta w, w>
b02_expr = sp.expand((sp.re(TW) ** 2 + sp.im(TW) ** 2) / 7)


class Bank:
    """Polynomials sharing one monomial table, evaluated in mp or iv."""

    def __init__(self, exprs):
        term_lists = [to_terms(e) for e in exprs]
        index = {}
        for tl in term_lists:
            for m, _ in tl:
                index.setdefault(m, len(index))
        self.monos = list(index)
        self.polys = [[(index[m], c) for m, c in tl] for tl in term_lists]
        self.cache = {}

    def consts(self, ctx):
        key = id(ctx)
        if key not in self.cache:
            self.cache[key] = [[ctx.mpf(c.numerator) / c.denominator for _, c in tl] for tl in self.polys]
        return self.cache[key]

    def __call__(self, x, ctx):
        pw = [[ctx.mpf(1)] + [xi ** e for e in range(1, 5)] for xi in x]
        mv = []
        for m in self.monos:
            v = ctx.mpf(1)
            for i, e in enumerate(m):
                if e:
                    v = v * pw[i][e]
            mv.append(v)
        cs = self.consts(ctx)
        out = []
        for tl, cl in zip(self.polys, cs):
            s = ctx.mpf(0)
            for (idx, _), c in zip(tl, cl):
                s += mv[idx] * c
            out.append(s)
        return out


GRAD = Bank(grad_expr)
HESS = Bank(hess_expr)
INV = Bank([r_expr, N_expr, f2_expr, b02_expr, trN2_expr])
print(f'model built: r has {len(to_terms(r_expr))} terms; gradient {len(GRAD.monos)} monomials; '
      f'Hessian {len(HESS.monos)} monomials', flush=True)


def cmat(M, ctx):
    return [[ctx.mpf(x.numerator) / x.denominator for x in row] for row in M]


def matvec(M, x, ctx):
    return [sum((M[i][j] * x[j] for j in range(len(x)) if M[i][j] != 0), ctx.mpf(0)) for i in range(len(M))]


# ---------------------------------------------------------------- 2. the critical system
class CritSystem:
    """grad r - 2 mu G x - sum nu_k G tau_k(x) = 0 (projected by B^T), x^T G x = 1, <s_k, x - x0> = 0.

    tau_k(x) = T_k x are the orbit tangents at the moving point; s_k = T_k x0 are fixed at the anchor (F1).
    x = B y parametrises a subspace (B = None for the whole space)."""

    def __init__(self, Bmat, slices, y0):
        self.B = Bmat
        self.d = 14 if Bmat is None else len(Bmat[0])
        self.T = slices
        self.n = self.d + 1 + len(slices)
        self.y0 = [mp.mpf(v) for v in y0]
        x0 = self.xof(self.y0, mp)
        G = [mp.mpf(g.numerator) / g.denominator for g in Gd]
        self.cov = []                                          # B^T G s_k, fixed numbers
        for T in slices:
            s = matvec(cmat(T, mp), x0, mp)
            Gs = [G[i] * s[i] for i in range(14)]
            self.cov.append(self.BT(Gs, mp))

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
        G = [ctx.mpf(g.numerator) / g.denominator for g in Gd]
        g = GRAD(x, ctx)
        Gx = [G[i] * x[i] for i in range(14)]
        vec = [g[i] - 2 * mu * Gx[i] for i in range(14)]
        for k, T in enumerate(self.T):
            tx = matvec(cmat(T, ctx), x, ctx)
            for i in range(14):
                vec[i] = vec[i] - nu[k] * G[i] * tx[i]
        out = self.BT(vec, ctx)
        out.append(sum((x[i] * Gx[i] for i in range(14)), ctx.mpf(0)) - 1)
        for k in range(len(self.T)):
            c = [ctx.mpf(v) for v in self.cov[k]]
            out.append(sum((c[j] * (y[j] - ctx.mpf(self.y0[j])) for j in range(d)), ctx.mpf(0)))
        return out

    def J(self, z, ctx):
        d, n = self.d, self.n
        y, mu, nu = z[:d], z[d], z[d + 1:]
        x = self.xof(y, ctx)
        G = [ctx.mpf(g.numerator) / g.denominator for g in Gd]
        hv = HESS(x, ctx)
        H = [[ctx.mpf(0)] * 14 for _ in range(14)]
        for (i, j), v in zip(hess_pairs, hv):
            H[i][j] = v
            H[j][i] = v
        for i in range(14):
            H[i][i] = H[i][i] - 2 * mu * G[i]
        Tcs = [cmat(T, ctx) for T in self.T]
        for k, Tc in enumerate(Tcs):
            for i in range(14):
                for j in range(14):
                    if Tc[i][j] != 0:
                        H[i][j] = H[i][j] - nu[k] * G[i] * Tc[i][j]
        # columns: J11 = B^T H B
        if self.B is None:
            HB = H
        else:
            HB = [[sum((H[i][l] * (ctx.mpf(self.B[l][j].numerator) / self.B[l][j].denominator)
                        for l in range(14) if self.B[l][j] != 0), ctx.mpf(0)) for j in range(d)] for i in range(14)]
        J11 = [self.BT([HB[i][j] for i in range(14)], ctx) for j in range(d)]      # list of columns
        Jac = [[ctx.mpf(0)] * n for _ in range(n)]
        for j in range(d):
            for i in range(d):
                Jac[i][j] = J11[j][i]
        Gx = [G[i] * x[i] for i in range(14)]
        BGx = self.BT(Gx, ctx)
        for i in range(d):
            Jac[i][d] = -2 * BGx[i]
            Jac[d][i] = 2 * BGx[i]
        for k, Tc in enumerate(Tcs):
            tx = matvec(Tc, x, ctx)
            col = self.BT([G[i] * tx[i] for i in range(14)], ctx)
            c = [ctx.mpf(v) for v in self.cov[k]]
            for i in range(d):
                Jac[i][d + 1 + k] = -col[i]
                Jac[d + 1 + k][i] = c[i]
        return Jac


def newton(S, z, maxit=60):
    for _ in range(maxit):
        Fz = mp.matrix(S.F(z, mp))
        Jz = mp.matrix(S.J(z, mp))
        dz = mp.lu_solve(Jz, Fz)
        z = [z[i] - dz[i] for i in range(S.n)]
        if mp.norm(dz) < mp.mpf(10) ** -56:
            break
    return z, mp.norm(mp.matrix(S.F(z, mp)))


def krawczyk(S, zc, rho):
    n = S.n
    Jc = mp.matrix(S.J(zc, mp))
    sv_ = mp.svd_r(Jc, compute_uv=False)
    smin = min(sv_[i] for i in range(sv_.rows))
    try:
        Y = mp.inverse(Jc)
    except ZeroDivisionError:
        return False, None, smin
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
    inside = all(K[i].a > box[i].a and K[i].b < box[i].b for i in range(n))
    return inside, box, smin


def certify(S, z, radii=('1e-30', '1e-20', '1e-40', '1e-12', '1e-8')):
    tried = []
    for rs in radii:
        ok, box, smin = krawczyk(S, z, mp.mpf(rs))
        tried.append(rs)
        if ok:
            return dict(ok=True, box=box, rho=rs, smin=smin, tried=tried)
    return dict(ok=False, box=None, rho=None, smin=smin, tried=tried)


# ---------------------------------------------------------------- 3. invariants, stars, permutations
def invariants(xbox):
    r, Nn, f2, b02, t2 = INV(xbox, iv)
    N2 = Nn * Nn
    return dict(v924=924 * r / N2, f2=f2 / N2, b02=b02 / N2, trN2=t2 / N2)


def overlap(p, q):
    return not (p.b < q.a or q.b < p.a)


def same_fingerprint(I1, I2):
    return all(overlap(I1[k], I2[k]) for k in ('v924', 'f2', 'b02', 'trN2'))


def fmt(I, digits=16):
    return f'[{mp.nstr(mp.mpf(I.a), digits)}, {mp.nstr(mp.mpf(I.b), digits)}]'


class CI:
    """A complex interval as a pair of real intervals."""

    def __init__(self, re_, im_):
        self.re, self.im = re_, im_

    def __add__(self, o):
        return CI(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return CI(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return CI(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)


def ci(z):
    return CI(iv.mpf(mp.mpf(z.real)), iv.mpf(mp.mpf(z.imag)))


def poly_eval(coefs, zc):
    """Horner, coefs[j] on z^j."""
    acc = CI(iv.mpf(0), iv.mpf(0))
    for c in reversed(coefs):
        acc = acc * zc + c
    return acc


def _gen_rotation():
    """Exact substitution matrix of U in SU(2) from the rational unit quaternion (2, 4, 5, 6)/9: a fixed,
    generic rotation applied before the stars are isolated, so that none sits at a pole of the charts (F2).
    It rotates the constellation rigidly, so the stabiliser's order is unchanged."""
    a, b, c, d = (sp.Rational(n, 9) for n in (2, 4, 5, 6))
    U11, U12, U21, U22 = a + sp.I * b, -c + sp.I * d, c + sp.I * d, a - sp.I * b
    X_, Y_ = sp.symbols('X_ Y_')
    M = [[None] * 7 for _ in range(7)]
    for k in range(7):
        P = sp.Poly(sp.expand((U11 * X_ + U12 * Y_) ** k * (U21 * X_ + U22 * Y_) ** (6 - k)), X_, Y_)
        for j in range(7):
            cf = sp.nsimplify(P.coeff_monomial(X_ ** j * Y_ ** (6 - j)))
            re_, im_ = sp.re(cf), sp.im(cf)
            M[j][k] = (Fr(int(re_.p), int(re_.q)), Fr(int(im_.p), int(im_.q)))
    return M


M_GEN = _gen_rotation()


def rotate_box(wre, wim):
    out_re, out_im = [], []
    for j in range(7):
        sr, si = iv.mpf(0), iv.mpf(0)
        for k in range(7):
            mr, mi = M_GEN[j][k]
            if mr == 0 and mi == 0:
                continue
            mrI = iv.mpf(mr.numerator) / mr.denominator
            miI = iv.mpf(mi.numerator) / mi.denominator
            sr += mrI * wre[k] - miI * wim[k]
            si += mrI * wim[k] + miI * wre[k]
        out_re.append(sr)
        out_im.append(si)
    return out_re, out_im


def star_boxes(wre, wim):
    """Six certified root boxes of F_u on the sphere, from interval coefficients w_k = wre[k] + i wim[k],
    after the fixed rational rotation M_GEN."""
    wre, wim = rotate_box(wre, wim)
    wc = [complex(float(mp.mpf(wre[k].mid)), float(mp.mpf(wim[k].mid))) for k in range(7)]
    wI = [CI(wre[k], wim[k]) for k in range(7)]
    zpoly = [CI((-1) ** j * wI[6 - j].re, (-1) ** j * wI[6 - j].im) for j in range(7)]     # F_u(z), z^j
    ypoly = [CI((-1) ** k * wI[k].re, (-1) ** k * wI[k].im) for k in range(7)]             # chart zeta = 1/z
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
        # refine the centre in mp
        cm = mp.mpc(c0.real, c0.imag)
        pm = [mp.mpc(mp.mpf(coefs[j].re.mid), mp.mpf(coefs[j].im.mid)) for j in range(7)]
        for _ in range(60):
            p = sum(pm[j] * cm ** j for j in range(7))
            dp = sum(j * pm[j] * cm ** (j - 1) for j in range(1, 7))
            step = p / dp
            cm -= step
            if abs(step) < mp.mpf(10) ** -55:
                break
        dpc = sum(j * pm[j] * cm ** (j - 1) for j in range(1, 7))
        yinv = 1 / dpc
        ok = False
        for rs in ('1e-40', '1e-30', '1e-20', '1e-12'):
            rho = mp.mpf(rs)
            Zb = CI(iv.mpf([cm.real - rho, cm.real + rho]), iv.mpf([cm.imag - rho, cm.imag + rho]))
            cc = CI(iv.mpf(cm.real), iv.mpf(cm.imag))
            pc = poly_eval(coefs, cc)
            dpZ = poly_eval(dco, Zb)
            yI = CI(iv.mpf(yinv.real), iv.mpf(yinv.imag))
            one = CI(iv.mpf(1), iv.mpf(0))
            K = cc - yI * pc + (one - yI * dpZ) * (Zb - cc)
            if K.re.a > Zb.re.a and K.re.b < Zb.re.b and K.im.a > Zb.im.a and K.im.b < Zb.im.b:
                ok = True
                break
        if not ok:
            return None
        s, t = Zb.re, Zb.im
        den = 1 + s * s + t * t
        if chart == 'z':
            P = (2 * s / den, 2 * t / den, (1 - s * s - t * t) / den)
        else:
            P = (2 * s / den, -2 * t / den, (s * s + t * t - 1) / den)
        pts.append(P)
    for i in range(6):
        for j in range(i + 1, 6):
            if all(overlap(pts[i][c], pts[j][c]) for c in range(3)):
                return None                                    # not separated: roots not certified distinct
    return pts


def dist2(P, Q):
    return sum(((P[c] - Q[c]) * (P[c] - Q[c]) for c in range(3)), iv.mpf(0))


def det3(P, Q, R):
    return (P[0] * (Q[1] * R[2] - Q[2] * R[1]) - P[1] * (Q[0] * R[2] - Q[2] * R[0])
            + P[2] * (Q[0] * R[1] - Q[1] * R[0]))


def rotation_survivors(pts):
    """Permutations of the stars compatible with all 15 distance enclosures, split into rotations and reflections."""
    D = [[dist2(pts[i], pts[j]) if i != j else iv.mpf(0) for j in range(6)] for i in range(6)]
    sums = [sum((D[i][j] for j in range(6) if j != i), iv.mpf(0)) for i in range(6)]
    pre = sum(1 for i in range(6) for j in range(i + 1, 6) if not overlap(sums[i], sums[j]))
    surv = []
    for sg in itertools.permutations(range(6)):
        if all(overlap(D[i][j], D[sg[i]][sg[j]]) for i in range(6) for j in range(i + 1, 6)):
            surv.append(sg)
    cent = [[float(mp.mpf(P[c].mid)) for c in range(3)] for P in pts]
    tri = max(itertools.combinations(range(6), 3), key=lambda t: abs(np.linalg.det(np.array([cent[i] for i in t]))))
    d0 = det3(*[pts[i] for i in tri])
    rot, refl, undecided = [], [], []
    for sg in surv:
        d1 = det3(*[pts[sg[i]] for i in tri])
        same = (d0.a > 0 and d1.a > 0) or (d0.b < 0 and d1.b < 0)
        opp = (d0.a > 0 and d1.b < 0) or (d0.b < 0 and d1.a > 0)
        (rot if same else refl if opp else undecided).append(sg)
    return dict(rot=rot, refl=refl, undecided=undecided, pre_separated_pairs=pre)


# ---------------------------------------------------------------- 4. numerics for frames and seeds
Fx_f = np.array([[float(x) for x in row] for row in FxH], dtype=complex)
Fy_f = -1j * np.array([[float(x) for x in row] for row in FyA], dtype=complex)
Fz_f = np.array([[float(x) for x in row] for row in Jz], dtype=complex)
gB = np.array([1 / comb(6, k) for k in range(7)])


def ipB(p, q):
    return np.sum(np.conj(p) * q * gB)


def Dmat(n, th):
    n = np.asarray(n, float) / np.linalg.norm(n)
    return sla.expm(-1j * th * (n[0] * Fx_f + n[1] * Fy_f + n[2] * Fz_f))


def defect(w, n, th):
    return 1 - abs(ipB(w, Dmat(n, th) @ w)) / ipB(w, w).real


def sph(t, p):
    return np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])


FIB = [(np.arccos(1 - 2 * (i + 0.5) / 1500), np.pi * (1 + 5 ** 0.5) * i) for i in range(1500)]


def find_axis(w, k, perp_to=None):
    th = 2 * np.pi / k
    if perp_to is None:
        cands = sorted((defect(w, sph(*g), th), g) for g in FIB)[:8]
        best = None
        for _, g in cands:
            res = minimize(lambda v: defect(w, sph(*v), th), np.array(g), method='Nelder-Mead',
                           options={'xatol': 1e-14, 'fatol': 1e-16, 'maxiter': 6000})
            if best is None or res.fun < best[0]:
                best = (res.fun, sph(*res.x))
        return best
    n1 = perp_to / np.linalg.norm(perp_to)
    e1 = np.cross(n1, [1.0, 0, 0] if abs(n1[0]) < 0.9 else [0, 1.0, 0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n1, e1)
    vec = lambda ph: np.cos(ph) * e1 + np.sin(ph) * e2
    grid = np.linspace(0, np.pi, 1200, endpoint=False)
    cands = sorted((defect(w, vec(p), th), p) for p in grid)[:6]
    best = None
    for _, p in cands:
        res = minimize(lambda v: defect(w, vec(v[0]), th), np.array([p]), method='Nelder-Mead',
                       options={'xatol': 1e-15, 'fatol': 1e-16, 'maxiter': 4000})
        if best is None or res.fun < best[0]:
            best = (res.fun, vec(res.x[0]))
    return best


def to_w(seed):
    """Census fibre vector (order v3..v-3) to Bombieri coefficients w_0..w_6, normalised."""
    w = np.array([np.sqrt(comb(6, k)) * seed[6 - k] for k in range(7)], dtype=complex)
    return w / np.sqrt(ipB(w, w).real)


def w_to_x(w):
    return [mp.mpf(float(v.real)) for v in w] + [mp.mpf(float(v.imag)) for v in w]


def mp_rotate(xw, A):
    """Apply D(A), A in SO(3), to the mp coefficient vector (as 14 reals); D(A) = exp(-i theta n.F)."""
    rv = Rotation.from_matrix(A).as_rotvec()
    th = float(np.linalg.norm(rv))
    n = rv / th if th > 0 else np.array([0, 0, 1.0])
    Fm = [[mp.mpc(float(n[0] * Fx_f[i, j].real + n[1] * Fy_f[i, j].real + n[2] * Fz_f[i, j].real),
                  float(n[0] * Fx_f[i, j].imag + n[1] * Fy_f[i, j].imag + n[2] * Fz_f[i, j].imag))
           for j in range(7)] for i in range(7)]
    M = mp.expm(mp.matrix(Fm) * mp.mpc(0, -th))
    wv = mp.matrix([mp.mpc(xw[k], xw[7 + k]) for k in range(7)])
    out = M * wv
    return [out[k].real for k in range(7)] + [out[k].imag for k in range(7)]


def frame(n1, n2=None):
    n1 = n1 / np.linalg.norm(n1)
    if n2 is None:
        n2 = np.cross(n1, [1.0, 0, 0] if abs(n1[0]) < 0.9 else [0, 1.0, 0])
    n2 = n2 - np.dot(n2, n1) * n1
    n2 /= np.linalg.norm(n2)
    return np.array([n2, np.cross(n1, n2), n1])            # rows: new x, y, z; A n1 = e_z, A n2 = e_x


def char_subspace(k_main, chi_main_m0, chi_x=None):
    """Rational basis (14 x d) of {w : R_z(2pi/k) w = e^(-2 pi i m0/k) w [, R_x(pi) w = chi_x w]}."""
    S1 = [j for j in range(7) if (j - 3 - chi_main_m0) % k_main == 0]
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


def Rx_pi_matrix():
    return Dmat([1, 0, 0], np.pi)


def signature(z):
    """Reconnaissance: transverse inertia of the second variation at a refined full-sphere point."""
    x = [z[i] for i in range(14)]
    mu = z[14]
    hv = HESS(x, mp)
    H = mp.matrix(14, 14)
    for (i, j), v in zip(hess_pairs, hv):
        H[i, j] = v
        H[j, i] = v
    G = [mp.mpf(g.numerator) / g.denominator for g in Gd]
    for i in range(14):
        H[i, i] -= 2 * mu * G[i]
    dirs = [x] + [matvec(cmat(T, mp), x, mp) for T in (T0, Tx, Ty, Tz)]
    # G-orthonormal basis of the complement of span(dirs)
    Hn = np.array([[float(H[i, j]) for j in range(14)] for i in range(14)])
    Gn = np.diag([float(g) for g in G])
    Dn = np.array([[float(v) for v in d] for d in dirs]).T
    Q, _ = np.linalg.qr(np.hstack([np.sqrt(Gn) @ Dn, np.eye(14)]))
    comp = Q[:, 5:14]
    L = np.linalg.inv(np.sqrt(Gn))
    Mred = comp.T @ L @ Hn @ L @ comp
    ev = np.linalg.eigvalsh((Mred + Mred.T) / 2)
    scale = np.max(np.abs(ev))
    return int(np.sum(ev < -1e-9 * scale)), int(np.sum(abs(ev) <= 1e-9 * scale)), int(np.sum(ev > 1e-9 * scale))


# ---------------------------------------------------------------- 5. model checks and the seeds
def r924_at(w):
    return 924 * float(INV(w_to_x(w), mp)[0]) / float(INV(w_to_x(w), mp)[1]) ** 2


checks = []
for m, target in ((3, 1), (2, 36), (1, 225), (0, 400)):
    w = np.zeros(7, dtype=complex)
    w[m + 3] = np.sqrt(comb(6, m + 3))
    checks.append(abs(r924_at(w) - target) < 1e-12)
gate('the model gives 924 r6 = 1, 36, 225, 400 at v3, v2, v1, v0', all(checks))
Rxf = Rx_pi_matrix()
gate('R_x(pi) acts as w_k -> -w_(6-k) in these coordinates',
     np.allclose(Rxf, -np.fliplr(np.eye(7)), atol=1e-12))

seeds = {}
LOG_VALUES = {'T1': 215.775792502, 'T2': 238.016528926, 'T3': 238.356854743}
for sector in ('r4', 'r5'):
    d = np.load(MIT / f'OpenWave/M8_DYNAMICS/out/pencil_census_{sector}.npz')
    for i in range(12):
        w = to_w(d[f'orb{i:02d}'])
        v = r924_at(w)
        x = w_to_x(w)
        f = [float(q) for q in INV(x, mp)]
        nem_n = np.array([[float(sp.N(nem[a][b].subs(dict(zip(V, [float(t) for t in x]))))) for b in range(3)]
                          for a in range(3)])
        top = float(np.max(np.linalg.eigvalsh(nem_n)))
        label = None
        for key, val in LOG_VALUES.items():
            if abs(v - val) < 1e-6:
                label = key
        if abs(v - 237.6) < 1e-6:
            label = 'pyramid' if abs(top - 6.4) < 1e-6 else 'C3ray' if abs(top - 5.2) < 1e-6 else None
        if abs(v - 8800 / 43) < 1e-6:
            label = 'prism'
        if abs(v - 225) < 1e-6:
            label = 'D2ray'
        if label:
            seeds[(sector, label)] = w
gate('both sectors hold the three targets and the three controls',
     all((s, l) in seeds for s in ('r4', 'r5') for l in ('T1', 'T2', 'T3', 'pyramid', 'prism', 'D2ray')))


def full_system(w):
    x0 = w_to_x(w)
    return CritSystem(None, [T0, Tx, Ty, Tz], x0), x0


def certify_full(w, label):
    S, x0 = full_system(w)
    r0, N0 = INV(x0, mp)[:2]
    z0 = x0 + [2 * r0 / N0 ** 2, 0, 0, 0, 0]
    z, res = newton(S, z0)
    out = certify(S, z)
    out['z'] = z
    out['res'] = res
    nu = [abs(v) for v in z[15:]]
    if out['ok']:
        out['inv'] = invariants(out['box'][:14])
        print(f'  {label}: CERTIFIED at radius {out["rho"]} (Newton residual {mp.nstr(res, 3)}; '
              f'|nu| <= {mp.nstr(max(nu), 3)}; smallest singular value {mp.nstr(out["smin"], 6)}); '
              f'924 r6 in {fmt(out["inv"]["v924"])}', flush=True)
    else:
        print(f'  {label}: NOT CERTIFIED (radii tried {out["tried"]}; smallest singular value at the centre '
              f'{mp.nstr(out["smin"], 6)})', flush=True)
    return out


def symmetry_bound(xbox, label):
    pts = star_boxes(xbox[:7], xbox[7:14])
    if pts is None:
        print(f'  {label}: stars NOT certified', flush=True)
        return None
    sv = rotation_survivors(pts)
    print(f'  {label}: six stars certified; permutations surviving the distance test: {len(sv["rot"])} rotations, '
          f'{len(sv["refl"])} reflections, {len(sv["undecided"])} undecided; per-star sums separate '
          f'{sv["pre_separated_pairs"]} of 15 pairs', flush=True)
    return sv


def certify_in_group(w, label, k_main, dihedral):
    """Rotate w into standard position for C_k (or D_k), then certify inside the character-fixed subspace."""
    fz, n1 = find_axis(w, k_main)
    n2 = None
    if dihedral:
        fx, n2 = find_axis(w, 2, perp_to=n1)
    A = frame(n1, n2)
    xw = w_to_x(w)
    chosen = None
    for Acand in (A, A.T):
        xr = mp_rotate(xw, Acand)
        wr = np.array([complex(float(xr[k]), float(xr[7 + k])) for k in range(7)])
        chi = ipB(wr, Dmat([0, 0, 1], 2 * np.pi / k_main) @ wr) / ipB(wr, wr)
        m0 = int(round(-k_main * np.angle(chi) / (2 * np.pi))) % k_main
        chix = None
        if dihedral:
            cx = ipB(wr, Rxf @ wr) / ipB(wr, wr)
            chix = 1 if cx.real > 0 else -1
        Bm = char_subspace(k_main, m0, chix)
        if len(Bm[0]) == 0:
            continue
        Bf = np.array([[float(v) for v in row] for row in Bm])
        xf = np.array([float(v) for v in xr])
        yls, *_ = np.linalg.lstsq(Bf, xf, rcond=None)
        resid = np.linalg.norm(Bf @ yls - xf)
        if resid < 1e-5 and (chosen is None or resid < chosen[0]):
            chosen = (resid, Bm, xr, m0, chix)
    if chosen is None:
        print(f'  {label}: no character-fixed subspace found near the rotated state', flush=True)
        return None
    resid, Bm, xr, m0, chix = chosen
    Bmp = mp.matrix([[mp.mpf(v.numerator) / v.denominator for v in row] for row in Bm])
    xv = mp.matrix(xr)
    y0 = mp.lu_solve(Bmp.T * Bmp, Bmp.T * xv)
    y0 = [y0[i] for i in range(len(Bm[0]))]
    slices = [T0] if dihedral else [T0, Tz]
    S = CritSystem(Bm, slices, y0)
    xx = S.xof(y0, mp)
    r0, N0 = INV(xx, mp)[:2]
    z, res = newton(S, y0 + [2 * r0 / N0 ** 2] + [0] * len(slices))
    out = certify(S, z)
    grp = f'{"D" if dihedral else "C"}{k_main}'
    if out['ok']:
        xbox = S.xof(out['box'][:S.d], iv)
        out['xbox'] = xbox
        out['inv'] = invariants(xbox)
        print(f'  {label}: certified inside the {grp}-fixed subspace (character m0 = {m0}'
              f'{"" if chix is None else f", R_x(pi) = {chix}"}; dimension {S.d // 2} complex) at radius '
              f'{out["rho"]}; 924 r6 in {fmt(out["inv"]["v924"])}', flush=True)
    else:
        print(f'  {label}: NOT CERTIFIED in the {grp}-fixed subspace (smallest singular value '
              f'{mp.nstr(out["smin"], 6)})', flush=True)
    return out


# ---------------------------------------------------------------- 6. controls
print('\ncontrols: known groups (pyramid C5, prism D3, D2 ray D2), from r4')
CONTROLS = {'pyramid': (5, False), 'prism': (3, True), 'D2ray': (2, True)}
control_ok = {}
cert = {}
for name, (k, dih) in CONTROLS.items():
    w = seeds[('r4', name)]
    full = certify_full(w, f'{name} (full sphere)')
    sub = certify_in_group(w, f'{name} (subspace)', k, dih)
    order = 2 * k if dih else k
    sv = symmetry_bound(sub['xbox'], f'{name} (stars)') if sub and sub['ok'] else None
    good = (full['ok'] and sub is not None and sub['ok'] and sv is not None and len(sv['rot']) == order
            and len(sv['undecided']) == 0 and same_fingerprint(full['inv'], sub['inv']))
    control_ok[name] = good
    cert[name] = full
    gate(f'control {name}: critical on the full sphere and in its subspace, stabiliser exactly '
         f'{"D" if dih else "C"}{k} (order {order}), fingerprints agree', good)

print('\narms')
if control_ok.get('pyramid'):
    rng = np.random.default_rng(20260922)
    zc = cert['pyramid']['z']
    xstar = zc[:14]
    delta = rng.normal(size=14)
    delta /= np.linalg.norm(delta)
    xp = [xstar[i] + mp.mpf(float(1e-6 * delta[i])) for i in range(14)]
    Np = INV(xp, mp)[1]
    xp = [v / mp.sqrt(Np) for v in xp]
    thin = [iv.mpf(v) for v in xp]
    svp = symmetry_bound(thin, 'displaced pyramid (stars)')
    gate('arm, perturbation: the displaced pyramid keeps only the identity among rotations',
         svp is not None and len(svp['rot']) == 1)
    wp = np.array([complex(float(xp[k]), float(xp[7 + k])) for k in range(7)])
    again = certify_full(wp, 'displaced pyramid, refined')
    gate('arm, perturbation: refined from the displaced start, the pyramid certifies again, same fingerprint',
         again['ok'] and same_fingerprint(again['inv'], cert['pyramid']['inv']))
else:
    gate('arm, perturbation: parent (pyramid control) green', False)

rng = np.random.default_rng(7)
wr = rng.normal(size=7) + 1j * rng.normal(size=7)
wr /= np.sqrt(ipB(wr, wr).real)
S, x0 = full_system(wr)
r0, N0 = INV(x0, mp)[:2]
res = certify(S, x0 + [2 * r0 / N0 ** 2, 0, 0, 0, 0])
print(f'  random state, not refined: {"CERTIFIED" if res["ok"] else "not certified"}; smallest singular value '
      f'{mp.nstr(res["smin"], 6)}')
gate('arm, non-critical: a random state does not certify', not res['ok'])

wv0 = np.zeros(7, dtype=complex)
wv0[3] = np.sqrt(20)
S, x0 = full_system(wv0)
r0, N0 = INV(x0, mp)[:2]
res = certify(S, x0 + [2 * r0 / N0 ** 2, 0, 0, 0, 0])
print(f'  v0 with three rotation slices: {"CERTIFIED" if res["ok"] else "not certified"}; smallest singular value '
      f'{mp.nstr(res["smin"], 6)}')
gate('arm, degenerate: v0 (continuous stabiliser) does not certify', not res['ok'])

if not all(ok for _, ok in RESULTS):
    stop('a control or arm failed; the targets are not run')

# ---------------------------------------------------------------- 7. targets
print('\ntargets, each from both sectors')
TARGETS = {'T1': '215.7758', 'T2': '238.0165', 'T3': '238.3569'}
summary = {}
for key, approx in TARGETS.items():
    print(f'{key} (924 r6 ~ {approx})')
    runs = {s: certify_full(seeds[(s, key)], f'{key} from {s}') for s in ('r4', 'r5')}
    both = runs['r4']['ok'] and runs['r5']['ok']
    if both and not same_fingerprint(runs['r4']['inv'], runs['r5']['inv']):
        stop(f'{key}: the two sectors certify different orbits')
    gate(f'{key}: certified from both sectors, same fingerprint', both)
    sv = symmetry_bound(runs['r4']['box'][:14], f'{key} (stars, from r4)') if runs['r4']['ok'] else None
    summary[key] = dict(runs=runs, sv=sv, sig=signature(runs['r4']['z']) if runs['r4']['ok'] else None)

# the C2 leads: lower bound inside the C2-fixed subspace
for key in ('T1', 'T3'):
    sub = certify_in_group(seeds[('r4', key)], f'{key} (C2 subspace)', 2, False)
    summary[key]['sub'] = sub
    sv = summary[key]['sv']
    exact_c2 = (sub is not None and sub['ok'] and sv is not None and len(sv['rot']) == 2 and not sv['undecided']
                and same_fingerprint(sub['inv'], summary[key]['runs']['r4']['inv']))
    gate(f'{key}: stabiliser exactly C2 (certified in its C2 subspace; two surviving rotations)', exact_c2)

sv = summary['T2']['sv']
gate('T2: stabiliser trivial (only the identity survives among rotations; none undecided)',
     sv is not None and len(sv['rot']) == 1 and not sv['undecided'])

# value separation from each other and from the census values
census = [Fr(1), Fr(36), Fr(8800, 43), Fr(225), Fr(1188, 5), Fr(288), Fr(400), Fr(463)]
census_I = [iv.mpf(c.numerator) / c.denominator for c in census]
ints = [summary[k]['runs']['r4']['inv']['v924'] for k in ('T1', 'T2', 'T3') if summary[k]['runs']['r4']['ok']]
sep = len(ints) == 3 and all(not overlap(ints[i], ints[j]) for i in range(3) for j in range(i + 1, 3))
sep = sep and all(not overlap(I, C) for I in ints for C in census_I)
gate('the three value enclosures are disjoint from each other and from the ten census values', sep)

print('\nsummary')
for key in ('T1', 'T2', 'T3'):
    s = summary[key]
    run = s['runs']['r4']
    if run['ok']:
        I = run['inv']
        print(f'  {key}: 924 r6 in {fmt(I["v924"], 20)}; |f|^2 in {fmt(I["f2"], 10)}; |B0|^2 in {fmt(I["b02"], 10)}; '
              f'TrN^2 in {fmt(I["trN2"], 10)}; box radius {run["rho"]}; rotations surviving {len(s["sv"]["rot"])}; '
              f'transverse signature (n-, n0, n+) = {s["sig"]} (reconnaissance)')
    else:
        print(f'  {key}: not certified')
n_fail = sum(1 for _, ok in RESULTS if not ok)
print('ALL PASS' if n_fail == 0 else f'{n_fail} FAILED')
