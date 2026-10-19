#!/usr/bin/env python3
"""The slow spectrum one order past Theorem R's leading term, at a nondegenerate critical orbit of the soft slots:
the coefficient c_g in lambda_g(eps) = eps kappa s_g + eps^2 c_g + O(eps^3), at M8.16's pyramid control P5 in R4 and
at its four soft-slot controls C2a, C2b, C3 and C2a/R5, with Theorem R'(c) at v1 as a check: the Soft-Slot Branches,
section III, Proposition N, whose checks i to viii are fixed there.

  python3 -I -B next_order_check.py COMPARISON_JSON EXACT_JSON

second_order_check.py's exact primitives are imported, unchanged, from the folder above this one.
COMPARISON_JSON: comparison_data.json, written by extract_comparison.py from M8.16's record before the derivation and
                 checked here against its SHA-256 (check iii).
EXACT_JSON: a new file, written here: the exact first correction at each case, which quadrature_check.py reads; run
            from this folder, it equals exact_values.json.

Units R = c = V = 1, as in second_order_check.py: lambda0 = K(K + 2), omega0 = sqrt(lambda0), kappa = 1/(8 omega0 Q),
h = |y|^4 + beta |Y6(y)|^2 = 2H, and Mhat = Hess h(u) - 4 h(u) for unit u. With z the solution of Mhat z = grad R~0(u)
on the normal space, the Hessian at the germ is Mhat/(2Q) + eps D_u + O(eps^2), D_u = (Hess R~0(u) - D^3h(u)[z])/Q^2,
and for a simple eigenvalue mu0 = kappa s_g of T0 = kappa J Mhat, with right and left eigenvectors r, l (l^T r = 1),

  c_g = l^T J D_u r / (4 omega0) - mu0 / (2 omega0^2) + mu0^2 l^T J r / (2 omega0),

the parts from the Hessian at the germ, the frequency's shift and lambda^2. Exact unless marked floating point.

  A  the leading order: Q, k, Mhat u = 8 Q u, Mhat K_u = 0, the nonzero slow spectrum against the terms' frozen
     spectrum, and the Krein signs; the zero multiplicity of Shat_u = J Mhat is k + r_u by an exact factorization of
     its characteristic polynomial (branches_check.py's charpoly and strip_zero), with the cofactor nonzero at 0
  B  the first correction's gradient: Euler's identity at each level, grad R~0(u) orthogonal to K_u, radial at the
     controls, and at P5 in span{u, n} with the exact values of check viii
  C  the Hessian at the germ: z solves Mhat z = grad R~0(u) on the normal space; for every generator X,
     D_u X u = Mhat X z / Q^2, check i, D_u X y0 = -kappa_u^{-1} M_u X y1; and the split
     D_u = (Hess R~0(u) - 6 R~0(u))/Q^2 - (3 R~0(u)/(2 Q^3)) Mhat - D^3h(u)[z_off]/Q^2, z_off the part of z off the
     ray, which gives c_g its five parts: the spherical Hessian, the amplitude, the off-ray shift, the frequency
     and lambda^2
  D  Theorem R'(c) at v1 in R4 and R5, check ii: D_u on K' = C v_{-3} is gamma_u times the metric, with the
     page's gamma_u
  E  the eigenvalue step against a model (floating point, 50 digits): the reduced pencil on E0,
     (lambda^2 + 2 omega_eps lambda J) + (eps/2) Hess f~(y_eps, eps), with y_eps found by Newton on the slice for
     f~ = h/2 - |y|^2 + eps R~0, at eps = 1e-4, 2e-4, 4e-4; the quadratic extrapolation of (lambda/eps - mu0)/eps
     to eps = 0 equals c_g within 1e-8, group by group
  F  the record, checks iv to vi: for each group, h = (lambda/eps - kappa s_g)/eps at the reached eps,
     c2 and c3 its linear and quadratic extrapolations to 0, and |c_g - c3| <= |c3 - c2| at N = 24 and 32, and at
     N = 16 with c_g from the missing channels removed; for a multiple group, c_g is the cluster mean, as the record's
     group centre is the mean of its eigenvalues
Mutation arms, each of which must turn its claim red: R4 with s = 2/7 (A); the cubic recoupling dropped (B); the
germ's shift along n dropped at P5 (C); the shift dropped at v1 (D); for E, the frequency's shift dropped, the
lambda^2 part dropped, the Hermitian pairing in place of the bilinear one, and the model's germ held on the ray; and
the off-ray shift dropped from c_g at P5 (F). Then, reported: c_g with its five parts and conditioning. The exit
status is 1 if a claim fails or an arm stays green.
"""
import hashlib
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy import I, Rational as R, sqrt

CMP, OUTJ = sys.argv[1:3]
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import second_order_check as so  # noqa: E402

CMP_SHA = '08bf8a711aa029fd8c639b4cc8911e0a786338476b6ceb0cbbc707cb5e41a9b4'
canon = so.canon
mp.mp.dps = 50


# ---------------------------------------------------------------- exact primitives, in orthonormal coordinates
def rin(a, b):
    return canon(sp.re(sum(sp.conjugate(x) * y for x, y in zip(a, b))))


def ket(j, d):
    M = so.ms(j)
    y = [sp.Integer(0)] * len(M)
    for m, c in d.items():
        y[M.index(m)] = sp.sympify(c)
    return y


def basis(n):
    B = []
    for a in range(n):
        e = [sp.Integer(0)] * n
        e[a] = sp.Integer(1)
        B.append(e)
    for a in range(n):
        e = [sp.Integer(0)] * n
        e[a] = I
        B.append(e)
    return B


def rcol(y):
    return sp.Matrix([canon(sp.re(c)) for c in y] + [canon(sp.im(c)) for c in y])


def cvec(x, n):
    return [sp.expand(x[a] + I * x[n + a]) for a in range(n)]


def spin(j):
    M = so.ms(j)
    n = len(M)
    Jz, Jp = sp.diag(*M), sp.zeros(n)
    for a in range(1, n):
        Jp[a - 1, a] = sqrt(j * (j + 1) - M[a] * (M[a] + 1))
    return (Jp + Jp.T) / 2, (Jp - Jp.T) / (2 * I), Jz


def generators(j, quaternionic):
    """The infinitesimal stationary symmetries on E0, as maps of complex vectors: the phase, the three rotations
    -i J_a, and in R2 the fibre's Theta and i Theta, Theta|j, m> = (-1)^(j - m)|j, -m> extended antilinearly."""
    M = so.ms(j)
    out = [('phase', lambda y: [sp.expand(I * c) for c in y])]
    for name, Ja in zip(('x', 'y', 'z'), spin(j)):
        C = -I * Ja
        out.append(('rotation ' + name, (lambda C: lambda y: [sp.expand(sum(C[a, b] * y[b] for b in range(len(y))))
                                                               for a in range(len(y))])(C)))
    if quaternionic:
        def th(y):
            o = [sp.Integer(0)] * len(y)
            for a, m in enumerate(M):
                o[M.index(-m)] = (-1) ** int(j - m) * sp.conjugate(y[a])
            return [sp.expand(c) for c in o]
        out.append(('Theta', th))
        out.append(('i Theta', lambda y: [sp.expand(I * c) for c in th(y)]))
    return out


def ypair2(j, a, b):
    return [sp.expand(p + q) for p, q in zip(so.Ypair(j, a, b), so.Ypair(j, b, a))]


def exact_case(slot, u, fixed, drop=(), cubic=True, s_override=None, shift='full'):
    """Everything exact at the unit representative u: Mhat, the first correction's value, gradient and Hessian, level
    by level, the orbit tangent, z, D^3h(u)[z] and D_u. fixed: the directions besides u that the isotropy fixes, in
    which grad R~0(u) is to lie. drop: the levels left out (N = 16). shift: 'full', 'radial' (z's part along the
    fixed directions other than u dropped) or 'none' (z = 0)."""
    j, s, K = so.SLOTS[slot]
    if s_override is not None:
        s = s_override
    assert rin(u, u) == 1, 'the representative must be a unit vector'
    n = int(2 * j) + 1
    N = 2 * n
    beta = (2 * j + 1) * (1 - s) / (13 * s)
    B = basis(n)
    Yu = so.Ypair(j, u, u)
    Y1 = [ypair2(j, u, e) for e in B]
    Y2 = {(a, b): ypair2(j, B[a], B[b]) for a in range(N) for b in range(a, N)}
    ue = [rin(u, e) for e in B]
    Hh = sp.zeros(N)
    for a in range(N):
        for b in range(a, N):
            Hh[a, b] = Hh[b, a] = canon(4 * (1 if a == b else 0) + 8 * ue[a] * ue[b]
                                        + 2 * beta * (rin(Y1[a], Y1[b]) + rin(Yu, Y2[a, b])))
    Q = canon(rin(u, u) ** 2 + beta * rin(Yu, Yu))
    Mh = (Hh - 4 * Q * sp.eye(N)).applyfunc(canon)
    grad, HR, Ru, lev = [sp.Integer(0)] * N, sp.zeros(N), sp.Integer(0), {}
    for J in so.levels(j):
        t = so.tJ(j, s, J, cubic)
        L = int(2 * J)
        if L == K or t == 0 or L in drop:
            continue
        mu = L * (L + 2) - K * (K + 2)
        w = t / ((2 * J + 1) * s ** 3 * mu)
        G0 = so.couple(j, J, Yu, u)
        G1 = [[sp.expand(x + y) for x, y in zip(so.couple(j, J, Yu, e), so.couple(j, J, Y1[a], u))]
              for a, e in enumerate(B)]
        F0 = rin(G0, G0)
        gr = [canon(2 * rin(G0, G1[a])) for a in range(N)]
        HF = sp.zeros(N)
        for a in range(N):
            for b in range(a, N):
                G2 = [x + y + z for x, y, z in zip(so.couple(j, J, Y1[a], B[b]), so.couple(j, J, Y1[b], B[a]),
                                                     so.couple(j, J, Y2[a, b], u))]
                HF[a, b] = HF[b, a] = canon(2 * (rin(G1[a], G1[b]) + rin(G0, G2)))
        lev[L] = dict(J=J, t=t, mu=mu, w=w, F0=F0, grad=gr, H=HF)
        Ru += -w * F0
        grad = [canon(g - w * x) for g, x in zip(grad, gr)]
        HR = (HR - w * HF).applyfunc(canon)
    Ru = canon(Ru)
    gens = generators(j, slot == 'R2')
    Kmat = sp.Matrix.hstack(*[rcol(g(u)) for _, g in gens])
    k = Kmat.rank()
    g = sp.Matrix(grad)
    fr = [rcol(u)] + [rcol(f) for f in fixed]
    comps = [canon((f.T * g)[0]) for f in fr]
    in_fixed = (g - sum((c * f for c, f in zip(comps, fr)), sp.zeros(N, 1))).applyfunc(canon) == sp.zeros(N, 1)
    Mf = sp.Matrix(len(fr), len(fr), lambda a, b: canon((fr[a].T * Mh * fr[b])[0]))
    closed = all((Mh * fr[b] - sum((Mf[a, b] * fr[a] for a in range(len(fr))), sp.zeros(N, 1))).applyfunc(canon)
                 == sp.zeros(N, 1) for b in range(len(fr)))
    zc = Mf.LUsolve(sp.Matrix(comps)).applyfunc(canon)
    zparts = [(zc[a] * fr[a]).applyfunc(canon) for a in range(len(fr))]
    z = sum(zparts, sp.zeros(N, 1)).applyfunc(canon)
    solved = (Mh * z - g).applyfunc(canon) == sp.zeros(N, 1) and (Kmat.T * z).applyfunc(canon) == sp.zeros(len(gens), 1)
    if shift == 'radial':
        z = zparts[0]
    elif shift == 'none':
        z = sp.zeros(N, 1)

    def d3(zz):
        zy = cvec(zz, n)
        uz = rin(u, zy)
        ze = [rin(zy, e) for e in B]
        Y1z = ypair2(j, u, zy)
        Y2z = [ypair2(j, zy, e) for e in B]
        D = sp.zeros(N)
        for a in range(N):
            for b in range(a, N):
                D[a, b] = D[b, a] = canon(8 * uz * (1 if a == b else 0) + 8 * (ze[a] * ue[b] + ue[a] * ze[b])
                                          + 2 * beta * (rin(Y2z[a], Y1[b]) + rin(Y1[a], Y2z[b]) + rin(Y1z, Y2[a, b])))
        return D
    D3 = d3(z)
    Dq = (HR - D3).applyfunc(canon)
    zoff = sum(zparts[1:], sp.zeros(N, 1)).applyfunc(canon) if shift == 'full' else sp.zeros(N, 1)
    Gam = ((HR - 6 * Ru * sp.eye(N)) / Q ** 2).applyfunc(canon)
    Amp = (-3 * Ru / (2 * Q ** 3) * Mh).applyfunc(canon)
    Off = (-d3(zoff) / Q ** 2).applyfunc(canon)
    split = (Gam + Amp + Off - Dq / Q ** 2).applyfunc(canon) == sp.zeros(N) if shift == 'full' else None
    check_i = []
    zy = cvec(z, n)
    for name, gf in gens:
        check_i.append((name, (Dq * rcol(gf(u)) - Mh * rcol(gf(zy))).applyfunc(canon) == sp.zeros(N, 1)))
    return dict(slot=slot, j=j, s=s, K=K, n=n, N=N, beta=beta, u=u, Q=Q, Mh=Mh, Hh=Hh, Ru=Ru, grad=grad, HR=HR,
                lev=lev, k=k, Kmat=Kmat, gens=gens, comps=comps, in_fixed=in_fixed, Mf=Mf, closed=closed, z=z,
                zparts=zparts, solved=solved, D3=D3, d3=d3, Du=(Dq / Q ** 2).applyfunc(canon), check_i=check_i,
                Gam=Gam, Amp=Amp, Off=Off, split=split)


# ---------------------------------------------------------------- floating point, 50 digits
def tomp(M):
    return mp.matrix([[mp.mpf(sp.N(M[a, b], 60)) for b in range(M.cols)] for a in range(M.rows)])


def Jmat(n):
    J = mp.zeros(2 * n)
    for a in range(n):
        J[n + a, a], J[a, n + a] = 1, -1
    return J


def norm2(A):
    return max(mp.svd_c(A, compute_uv=False))


def null_space(A, tol):
    U, S, V = mp.svd_c(A)
    return [V[k, :].H for k in range(A.cols) if k >= len(S) or abs(S[k]) < tol]


def leading(ex):
    """T0 = kappa J Mhat at 50 digits: its eigenvalues, the zero count, and per cluster of nonzero eigenvalues in the
    closed first quadrant, one for each {mu, -mu, conj mu, -conj mu}, the right and left eigenvectors, biorthonormal,
    and the Krein form of Mhat on the cluster's real invariant subspace."""
    n, N = ex['n'], ex['N']
    lam0 = ex['K'] * (ex['K'] + 2)
    w0 = mp.sqrt(lam0)
    Q = mp.mpf(sp.N(ex['Q'], 60))
    kap = 1 / (8 * w0 * Q)
    Mh, J = tomp(ex['Mh']), Jmat(n)
    T0 = kap * J * Mh
    E = mp.eig(T0, left=False, right=False)
    zeros = sum(1 for e in E if abs(e) < mp.mpf('1e-20'))
    reps = [e for e in E if abs(e) >= mp.mpf('1e-20') and mp.re(e) > -mp.mpf('1e-30') * abs(e)
            and mp.im(e) > -mp.mpf('1e-30') * abs(e)]                   # one per {mu, -mu, conj mu, -conj mu}
    clusters = []
    for e in reps:
        for c in clusters:
            if abs(e - c[0]) < mp.mpf('1e-25') * abs(e):
                c.append(e)
                break
        else:
            clusters.append([e])
    groups = []
    for c in clusters:
        mu0 = sum(c) / len(c)
        A = T0 - mu0 * mp.eye(N)
        Rv, Lv = null_space(A, mp.mpf('1e-30')), null_space(A.T, mp.mpf('1e-30'))
        m = len(Rv)
        Rm, Lm = mp.matrix(N, m), mp.matrix(m, N)
        for b in range(m):
            for a in range(N):
                Rm[a, b], Lm[b, a] = Rv[b][a], Lv[b][a]
        Lm = (Lm * Rm) ** -1 * Lm
        Re_, Im_ = mp.matrix(N, m), mp.matrix(N, m)
        for a in range(N):
            for b in range(m):
                Re_[a, b], Im_[a, b] = mp.re(Rm[a, b]), mp.im(Rm[a, b])
        krein = [(Re_[:, b].T * Mh * Re_[:, b])[0] + (Im_[:, b].T * Mh * Im_[:, b])[0] for b in range(m)]
        groups.append(dict(mu0=mu0, s=mu0 / kap, mult=len(c), dimR=m, dimL=len(Lv), R=Rm, L=Lm, krein=krein))
    groups.sort(key=lambda g: (abs(g['mu0']), float(mp.re(g['mu0']))))
    return dict(T0=T0, E=E, zeros=zeros, groups=groups, kap=kap, w0=w0, lam0=lam0, J=J, Mh=Mh)


def first_order(ex, ld, Du=None, variant='full'):
    """c_g per group: the eigenvalues of L T1 R on the group's eigenspace, with the three parts for a simple group,
    and the conditioning, |L| |R| with L R = 1. variant: 'full', 'no_freq', 'no_lam2' or 'hermitian'."""
    Du = tomp(ex['Du']) if Du is None else Du
    J, T0, w0 = ld['J'], ld['T0'], ld['w0']
    out = []
    for g in ld['groups']:
        mu0, Rm, Lm = g['mu0'], g['R'], g['L']
        if variant == 'hermitian':
            Lm = (Rm.H * Rm) ** -1 * Rm.H
        parts = [Lm * ((1 / (4 * w0)) * J * Du) * Rm,
                 Lm * (-(1 / (2 * w0 ** 2)) * T0) * Rm,
                 Lm * ((mu0 ** 2 / (2 * w0)) * J) * Rm]
        if variant == 'no_freq':
            parts[1] = parts[1] * 0
        if variant == 'no_lam2':
            parts[2] = parts[2] * 0
        W = parts[0] + parts[1] + parts[2]
        m = W.rows
        ev = [W[0, 0]] if m == 1 else sorted(mp.eig(W, left=False, right=False), key=lambda x: (float(mp.re(x)), float(mp.im(x))))
        off = max((abs(W[a, b] - (W[a, a] if a == b else 0)) for a in range(m) for b in range(m) if a != b), default=0)
        spread = max(abs(W[a, a] - W[0, 0]) for a in range(m))
        cond = norm2(Lm) * norm2(Rm)
        out.append(dict(mu0=mu0, c=ev, parts=[p[0, 0] for p in parts] if m == 1 else None, cond=cond,
                        scalar=(off < mp.mpf('1e-40') and spread < mp.mpf('1e-40')) if m > 1 else True))
    return out


# ---------------------------------------------------------------- the model (floating point, 50 digits)
class Model:
    def __init__(self, ex):
        j, s, K = ex['j'], ex['s'], ex['K']
        self.ex = ex
        self.ctx = so.mp_setup(j)
        self.n = n = ex['n']
        self.N = N = ex['N']
        self.B = so.mp_basis(n)
        self.beta = mp.mpf(sp.N(ex['beta'], 60))
        self.Ys = {(a, b): [x + y for x, y in zip(so.mp_Y(self.ctx, self.B[a], self.B[b]),
                                                   so.mp_Y(self.ctx, self.B[b], self.B[a]))]
                   for a in range(N) for b in range(a, N)}
        self.levels = [(so.mp_table(j, d['J']), mp.mpf(sp.N(d['w'], 60))) for L, d in sorted(ex['lev'].items())]
        Kc = tomp(ex['Kmat'])
        U, S, V = mp.svd_r(Kc.T, full_matrices=True)
        self.Nb = mp.matrix(N, N - ex['k'])
        cols = [V[k, :].T for k in range(N) if k >= len(S) or abs(S[k]) < mp.mpf('1e-30')]
        for b, c in enumerate(cols):
            for a in range(N):
                self.Nb[a, b] = c[a]
        self.u = mp.matrix([mp.mpf(sp.N(x, 60)) for x in rcol(ex['u'])])
        self.Q = mp.mpf(sp.N(ex['Q'], 60))
        self.J = Jmat(n)
        self.w0 = mp.sqrt(ex['K'] * (ex['K'] + 2))

    def hessians(self, x):
        n, N, ctx, B = self.n, self.N, self.ctx, self.B
        y = [mp.mpc(x[a], x[n + a]) for a in range(n)]
        Yu = so.mp_Y(ctx, y, y)
        Y1 = [[p + q for p, q in zip(so.mp_Y(ctx, y, e), so.mp_Y(ctx, e, y))] for e in B]
        nu2 = so.mp_rin(y, y)
        yB = [so.mp_rin(y, e) for e in B]
        Hh = mp.zeros(N)
        for a in range(N):
            for b in range(a, N):
                Hh[a, b] = Hh[b, a] = (4 * nu2 * (1 if a == b else 0) + 8 * yB[a] * yB[b]
                                       + 2 * self.beta * (so.mp_rin(Y1[a], Y1[b]) + so.mp_rin(Yu, self.Ys[a, b])))
        HR = mp.zeros(N)
        for tab, w in self.levels:
            l0 = so.mp_couple(tab, Yu, y)
            l1 = [[p + q for p, q in zip(so.mp_couple(tab, Yu, e), so.mp_couple(tab, Y1[k], y))] for k, e in enumerate(B)]
            for a in range(N):
                for b in range(a, N):
                    G2 = [p + q + r for p, q, r in zip(so.mp_couple(tab, Y1[a], B[b]), so.mp_couple(tab, Y1[b], B[a]),
                                                       so.mp_couple(tab, self.Ys[a, b], y))]
                    v = 2 * (so.mp_rin(l1[a], l1[b]) + so.mp_rin(l0, G2))
                    HR[a, b] = HR[a, b] - w * v
                    if b != a:
                        HR[b, a] = HR[a, b]
        return Hh, HR

    def germ(self, eps, ray=False):
        """Newton for the critical point of f~ = h/2 - |y|^2 + eps R~0 on the slice y0 + (normal space), or with
        ray=True on the ray through u alone; returns the point, the Hessian of f~ there, and the full gradient's size."""
        x = self.u / mp.sqrt(self.Q)
        for it in range(12):
            Hh, HR = self.hessians(x)
            Hf = Hh / 2 - 2 * mp.eye(self.N) + eps * HR
            gr = Hh * x / 6 - 2 * x + eps * HR * x / 5
            if ray:
                step = (self.u.T * gr)[0] / (self.u.T * Hf * self.u)[0] * self.u
                done = abs((self.u.T * gr)[0])
            else:
                A = self.Nb.T * Hf * self.Nb
                step = self.Nb * (A ** -1 * (self.Nb.T * gr))
                done = mp.norm(self.Nb.T * gr)
            if done < mp.mpf('1e-46'):
                break
            x = x - step
        return x, Hf, mp.norm(gr)

    def coefficients(self, targets, e=mp.mpf('1e-4'), ray=False):
        """For each target mu0 (with multiplicity), the quadratic extrapolation to 0 of (lambda/eps - mu0)/eps through
        eps = e, 2e, 4e; and the largest full gradient at the germs."""
        epss = [e, 2 * e, 4 * e]
        hs = {i: [] for i in range(len(targets))}
        worst = 0
        N = self.N
        for eps in epss:
            x, Hf, gnorm = self.germ(eps, ray)
            worst = max(worst, gnorm)
            we = mp.sqrt(self.w0 ** 2 + eps)
            C = mp.zeros(2 * N)
            for a in range(N):
                C[a, N + a] = 1
            low = -(eps / 2) * Hf
            for a in range(N):
                for b in range(N):
                    C[N + a, b] = low[a, b]
                    C[N + a, N + b] = -2 * we * self.J[a, b]
            ev = mp.eig(C, left=False, right=False)
            for i, (mu0, mult) in enumerate(targets):
                near = sorted(ev, key=lambda lam: abs(lam - eps * mu0))[:mult]
                hs[i].append(sorted([(lam / eps - mu0) / eps for lam in near], key=lambda x: (float(mp.re(x)), float(mp.im(x)))))
        out = []
        for i in range(len(targets)):
            vals = []
            for k in range(targets[i][1]):
                h = [hs[i][q][k] for q in range(3)]
                e1, e2, e3 = epss
                vals.append(h[0] * e2 * e3 / ((e1 - e2) * (e1 - e3)) + h[1] * e1 * e3 / ((e2 - e1) * (e2 - e3))
                            + h[2] * e1 * e2 / ((e3 - e1) * (e3 - e2)))
            out.append(vals)
        return out, worst


# ---------------------------------------------------------------- the cases
P5U = {3: 2 * sqrt(3) / 5, -2: sqrt(13) / 5}
P5N = {3: sqrt(13) / 5, -2: -2 * sqrt(3) / 5}
NU_C3 = R(250880, 552123)      # the page, Section IV: the octahedron's real pair, three times
CASES = [  # name, slot, representative, other fixed directions, the terms' Q, k and zero multiplicity k + r_u
    ('C2a', 'R4', {3: 1}, [], R(1288, 1287), 3, 4),
    ('C2b', 'R2', {R(7, 2): 1}, [], R(144, 143), 5, 6),
    ('C3', 'R4', {2: 1 / sqrt(2), -2: 1 / sqrt(2)}, [], R(175, 143), 4, 8),
    ('C2a/R5', 'R5', {3: 1}, [], R(2289, 2288), 3, 4),
    ('P5', 'R4', P5U, [P5N], R(77, 65), 4, 6),
]
DROP16 = {'R4': (18,), 'R5': (18,), 'R2': (17, 19)}   # check vi
VIII_DF = {10: -12 * sqrt(39) / 2275, 14: -4863 * sqrt(39) / 386750, 16: 71 * sqrt(39) / 22750, 18: 2 * sqrt(39) / 425}
VIII_SUM = -146711 * sqrt(39) / 10507997500         # check viii, fixed before the computation


def frozen(rec):
    """The terms' frozen slow spectrum, as the expected s_g per group in the record's order, with their exact values
    where the terms give them, and the record's Krein signs."""
    out = []
    for g in rec['spectrum']:
        t = g['tau']
        slot = sp.nsimplify(rec['s'])
        if g['cls'] == 'complex':
            val, ex = mp.mpc(t['re'], t['im']) * mp.mpf(sp.N(slot, 60)), None
        elif 'frac' in t:
            ex = slot * sp.Rational(t['frac'])
            val = mp.mpf(sp.N(ex, 60)) * (1j if g['cls'] == 'imag' else 1)
        elif g['cls'] == 'real':
            ex = sqrt(NU_C3)
            val = mp.mpf(sp.N(ex, 60))
        else:
            val, ex = mp.mpc(0, t['value']) * mp.mpf(sp.N(slot, 60)), None
        out.append(dict(cls=g['cls'], sign=g['sign'], mult=g['mult'], val=val, exact=ex is not None))
    return out


def fmt(z, d=10):
    """z to d digits, with a real or imaginary part below 1e-30 of |z| written as 0."""
    z = mp.mpc(z)
    if abs(z) == 0:
        return '0'
    re, im = mp.re(z), mp.im(z)
    re = 0 if abs(re) < mp.mpf('1e-30') * abs(z) else re
    im = 0 if abs(im) < mp.mpf('1e-30') * abs(z) else im
    return mp.nstr(mp.mpc(re, im) if im else mp.mpf(re), d)


def record_coefficients(rec, N):
    """Checks iv and v's inputs at cutoff N: per group in the record's order, kappa s_g (the prediction over its
    nominal eps) and h at the reached eps = 0.25, 0.5 and 1, with c2 and c3, the linear and quadratic extrapolations."""
    pts = [rec['points'][f'N{N}_eps{e:g}'] for e in (0.25, 0.5, 1.0)]
    out = []
    for gi in range(len(pts[0]['groups'])):
        ks = mp.mpc(*pts[0]['groups'][gi]['predicted']) / mp.mpf('0.25')
        es, hs = [], []
        for p, en in zip(pts, (0.25, 0.5, 1.0)):
            g = p['groups'][gi]
            assert abs(mp.mpc(*g['predicted']) / mp.mpf(en) - ks) < mp.mpf('1e-15') * abs(ks)
            e = mp.mpf(p['eps_reached'])
            es.append(e)
            hs.append((mp.mpc(*g['computed']) / e - ks) / e)
        c2 = (es[1] * hs[0] - es[0] * hs[1]) / (es[1] - es[0])
        c3 = sum(hs[i] * mp.fprod([(0 - es[k]) / (es[i] - es[k]) for k in range(3) if k != i]) for i in range(3))
        out.append(dict(ks=ks, c2=c2, c3=c3, cls=pts[0]['groups'][gi]['cls'], sign=pts[0]['groups'][gi]['sign']))
    return out


def record_check(data, lds, fos, fo16s, show, cases=None):
    """Checks v and vi: each record group's c3 against its derived c_g (the cluster mean for a multiple group, as the
    record's group centre is the mean of its eigenvalues), within |c3 - c2|, at N = 24 and 32 with every channel and
    at N = 16 with the missing channels removed. Returns whether every group agrees, and the ones that do not."""
    ok, bad = True, []
    for name, slot, *_ in CASES:
        if cases is not None and name not in cases:
            continue
        rec = data['cases'][name]
        fz = [f for f in frozen(rec) for _ in range(f['mult'])]
        r24 = record_coefficients(rec, 24)
        for N in (24, 32, 16):
            rc = record_coefficients(rec, N)
            for gi, (f, r) in enumerate(zip(fz, rc)):
                best = min(range(len(lds[name]['groups'])), key=lambda i: abs(lds[name]['groups'][i]['s'] - f['val']))
                fo = (fo16s if N == 16 else fos)[name][best]
                cg = sum(fo['c']) / len(fo['c'])
                spread = abs(r['c3'] - r['c2'])
                d = abs(cg - r['c3'])
                agree = d <= spread
                ok &= agree
                if not agree:
                    bad.append('%s N = %d group %d' % (name, N, gi + 1))
                if show:
                    extra = ''
                    if N == 16:
                        c24 = sum(fos[name][best]['c']) / len(fos[name][best]['c'])
                        extra = '; the change from N = 24: derived %s, record %s' % (
                            fmt((cg - c24) / r['ks'], 4), fmt((r['c3'] - r24[gi]['c3']) / r['ks'], 4))
                    print('   %-7s N = %d, group %d (%s%s): c_g/(kappa s) = %s; record c3 %s, c2 %s; |c_g - c3| = %s, spread %s: %s%s'
                          % (name, N, gi + 1, f['cls'], '' if f['sign'] is None else ' %+d' % f['sign'], fmt(cg / r['ks'], 7),
                             fmt(r['c3'] / r['ks'], 7), fmt(r['c2'] / r['ks'], 7), mp.nstr(d / abs(r['ks']), 3),
                             mp.nstr(spread / abs(r['ks']), 3), 'agrees' if agree else 'DISAGREES', extra))
    return ok, bad


def main():
    failed, arms = 0, []

    def report(ok):
        nonlocal failed
        failed += not ok
        print('   %s' % ('PASS' if ok else 'FAIL'))
    raw = open(CMP, 'rb').read()
    if hashlib.sha256(raw).hexdigest() != CMP_SHA:
        raise SystemExit('comparison_data.json differs from its SHA-256, fixed before the derivation (check iii)')
    data = json.loads(raw)
    print('The pyramid quartet\'s next-order term: the exact first correction, the Hessian at the germ, and c_g')
    print('comparison data: SHA-256 %s (check iii)' % CMP_SHA)
    print('units R = c = V = 1; mp.dps = %d' % mp.mp.dps)
    exs, lds, fos = {}, {}, {}
    for name, slot, rep, fx, Qt, kt, zt in CASES:
        j = so.SLOTS[slot][0]
        exs[name] = exact_case(slot, ket(j, rep), [ket(j, f) for f in fx])
        lds[name] = leading(exs[name])
        fos[name] = first_order(exs[name], lds[name])

    # ------------------------------------------------ A
    print('A  the leading order at each case, from the exact quartic in orthonormal coordinates')
    okA = True
    for name, slot, rep, fx, Qt, kt, zt in CASES:
        ex, ld = exs[name], lds[name]
        fz = frozen(data['cases'][name])
        uc = rcol(ex['u'])
        okq = ex['Q'] == Qt and ex['k'] == kt and (ex['Mh'] * uc - 8 * ex['Q'] * uc).applyfunc(canon) == sp.zeros(ex['N'], 1) \
            and (ex['Mh'] * ex['Kmat']).applyfunc(canon) == sp.zeros(ex['N'], ex['Kmat'].shape[1])
        Sx = (so.bc.J0(int(2 * ex['j'])) * ex['Mh']).applyfunc(canon)
        cofactor, zex = so.bc.strip_zero(so.bc.charpoly(Sx, so.bc.MU))
        okz = ld['zeros'] == zt and zex == zt and cofactor.eval(0) != 0
        gs = ld['groups']
        okm = len(gs) == len(fz)
        rows = []
        for f in fz:
            best = min(gs, key=lambda g: abs(g['s'] - f['val']))
            tol = mp.mpf('1e-40') if f['exact'] else mp.mpf('1e-9')
            match = abs(best['s'] - f['val']) < tol * max(1, abs(f['val'])) and best['mult'] == f['mult'] == best['dimR']
            if f['cls'] == 'imag':
                match &= all((q > 0) == (f['sign'] > 0) for q in best['krein'])
            okm &= match
            rows.append((f, best, match))
        okA &= okq and okz and okm
        print('   %-7s Q = %s, k = %d, Mhat u = 8 Q u and Mhat K_u = 0: %s; zero multiplicity of Shat_u %d by its exact '
              'characteristic polynomial (cofactor nonzero at 0: %s), %d in floating point; k + r_u = %d'
              % (name, ex['Q'], ex['k'], okq, zex, cofactor.eval(0) != 0, ld['zeros'], zt))
        for f, best, match in rows:
            print('           s = %s (%s%s), frozen %s: %s' % (fmt(best['s'], 12), f['cls'], '' if f['sign'] is None else
                  ', Krein %s' % ('+' if all(q > 0 for q in best['krein']) else '-' if all(q < 0 for q in best['krein']) else '?'),
                  fmt(f['val'], 12), 'match' if match else 'MISMATCH'))
    report(okA)

    # ------------------------------------------------ B
    print('B  the first correction\'s gradient at u: Euler, invariance, the fixed directions, check viii')
    okB = True
    for name, slot, rep, fx, Qt, kt, zt in CASES:
        ex = exs[name]
        uc = rcol(ex['u'])
        euler = all(canon((sp.Matrix(d['grad']).T * uc)[0] - 6 * d['F0']) == 0 for d in ex['lev'].values())
        hom = all(((d['H'] * uc) - 5 * sp.Matrix(d['grad'])).applyfunc(canon) == sp.zeros(ex['N'], 1) for d in ex['lev'].values())
        perp = (ex['Kmat'].T * sp.Matrix(ex['grad'])).applyfunc(canon) == sp.zeros(ex['Kmat'].shape[1], 1)
        radial = canon(ex['comps'][0] - 6 * ex['Ru']) == 0
        okB &= euler and hom and perp and ex['in_fixed'] and radial
        print('   %-7s levels %s; R~0(u) = %s; Euler dF_J[u] = 6 F_J and Hess F_J u = 5 grad F_J: %s; grad perpendicular '
              'to K_u: %s; in the fixed directions: %s; its radial part 6 R~0(u): %s'
              % (name, sorted(ex['lev']), ex['Ru'], euler and hom, perp, ex['in_fixed'], radial))
    ex = exs['P5']
    nvec = rcol(ket(R(3), P5N))
    per = {L: canon((sp.Matrix(d['grad']).T * nvec)[0]) for L, d in ex['lev'].items()}
    viii_sum = canon(sum(d['t'] * per[L] / ((2 * d['J'] + 1) * d['mu']) for L, d in ex['lev'].items()))
    ratio = canon(ex['comps'][1] / ex['comps'][0])
    okviii = per == {L: canon(v) for L, v in VIII_DF.items()} and canon(viii_sum - VIII_SUM) == 0 and \
        canon(ex['comps'][1] + viii_sum / ex['s'] ** 3) == 0 and abs(sp.N(ratio, 30) + R(1211, 10000)) < R(5, 100000)
    okB &= okviii
    print('   P5, check viii: dF_J(u)[n] = %s' % ', '.join('%s at %d' % (per[L], L) for L in sorted(per)))
    print('        sum_J t_J dF_J(u)[n] / ((2J+1) mu_J) = %s; grad R~0(u) . n = %s, %s of its radial part; check viii\'s values: %s'
          % (viii_sum, ex['comps'][1], sp.N(ratio, 12), okviii))
    report(okB)

    # ------------------------------------------------ C
    print('C  the Hessian at the germ: z on the normal space, and check i for every generator')
    okC = True
    for name, slot, rep, fx, Qt, kt, zt in CASES:
        ex = exs[name]
        ci = all(ok for _, ok in ex['check_i'])
        okC &= ex['solved'] and ex['closed'] and ci and ex['split']
        zs = ', '.join(str(canon(c)) for c in ex['Mf'].LUsolve(sp.Matrix(ex['comps'])))
        print('   %-7s Mhat on the fixed directions %s; z = (%s) in (u%s); solves Mhat z = grad R~0(u) on the normal space: %s; '
              'check i: %s' % (name, list(ex['Mf'].diagonal()) if ex['Mf'].is_diagonal() else ex['Mf'], zs,
                               ', n' if name == 'P5' else '', ex['solved'], ', '.join('%s %s' % (g, 'ok' if ok else 'FAIL')
                                                                                      for g, ok in ex['check_i'])))
    exP = exs['P5']
    zn = exP['Mf'].LUsolve(sp.Matrix(exP['comps']))[1]
    print('   P5: the germ y_eps = y0 + eps y1 + O(eps^2) turns off the ray u: y1 . n / |y0| = -2 z_n / Q = %s = %s'
          % (canon(-2 * zn / exP['Q']), sp.N(-2 * zn / exP['Q'], 12)))
    print('   at every case, exactly: D_u = (Hess R~0(u) - 6 R~0(u))/Q^2 - (3 R~0(u)/(2 Q^3)) Mhat - D^3h(u)[z_off]/Q^2, '
          'z_off the part of z off the ray: %s' % all(exs[c[0]]['split'] for c in CASES))
    report(okC)

    # ------------------------------------------------ D
    print('D  Theorem R\'(c) at v1, check ii: D_u on K\' = C v_{-3}, against the page\'s gamma_u')
    okD = True
    v1 = {}
    for slot in ('R4', 'R5'):
        exv = exact_case(slot, ket(R(3), {1: 1}), [])
        v1[slot] = exv
        kp = [rcol(ket(R(3), {-3: 1})), rcol(ket(R(3), {-3: I}))]
        Dk = sp.Matrix(2, 2, lambda a, b: canon((kp[a].T * exv['Du'] * kp[b])[0]))
        gam = so.V1_GAMMA[slot]
        ok = exv['in_fixed'] and exv['solved'] and Dk == gam * sp.eye(2)
        okD &= ok
        print('   %s: grad R~0(v1) radial: %s; D_u on K\' = %s; gamma_u on the page %s = %s: %s'
              % (slot, exv['in_fixed'], Dk.tolist(), gam, sp.N(gam, 10), ok))
    report(okD)

    # ------------------------------------------------ E
    print('E  the eigenvalue step against the model, floating point, 50 digits')
    okE = True
    models, mres = {}, {}
    for name, slot, rep, fx, Qt, kt, zt in CASES:
        md = Model(exs[name])
        models[name] = md
        targets = [(g['mu0'], g['mult']) for g in lds[name]['groups']]
        res, worst = md.coefficients(targets)
        mres[name] = (res, worst)
        for g, fo, mc in zip(lds[name]['groups'], fos[name], res):
            dev = max(abs(a - b) for a, b in zip(sorted(fo['c'], key=lambda x: (float(mp.re(x)), float(mp.im(x)))), mc)) / abs(fo['c'][0])
            ok = dev < mp.mpf('1e-8') and worst < mp.mpf('1e-40')
            okE &= ok
            print('   %-7s s = %s: c_g = %s; model %s; relative difference %s; full gradient at the germs %s: %s'
                  % (name, fmt(g['s'], 8), fmt(fo['c'][0], 12), fmt(mc[0], 12),
                     'below 1e-12' if dev < mp.mpf('1e-12') else mp.nstr(dev, 2),
                     'below 1e-40' if worst < mp.mpf('1e-40') else mp.nstr(worst, 2), 'ok' if ok else 'FAIL'))
    report(okE)

    # ------------------------------------------------ F
    print('F  the record, checks iv to vi: c2 and c3 at the reached eps, and |c_g - c3| <= |c3 - c2|, group by group, at N = 24 '
          'and 32, and at N = 16 with its missing channels removed (R4 and R5 level 18; R2 levels 17 and 19)')
    fo16s, ex16s = {}, {}
    for name, slot, rep, fx, *_ in CASES:
        j = so.SLOTS[slot][0]
        ex16s[name] = exact_case(slot, ket(j, rep), [ket(j, f) for f in fx], drop=DROP16[slot])
        fo16s[name] = first_order(ex16s[name], lds[name])
    okF, _ = record_check(data, lds, fos, fo16s, show=True)
    report(okF)

    # ------------------------------------------------ the arms
    print('arms')
    exA = exact_case('R4', ket(R(3), {3: 1}), [], s_override=R(2, 7))
    arms.append(('R4 with s = 2/7 (A)', exA['Q'] != R(1288, 1287), 'C2a\'s Q becomes %s' % exA['Q']))
    exB = exact_case('R4', ket(R(3), P5U), [ket(R(3), P5N)], cubic=False)
    perB = {L: canon((sp.Matrix(d['grad']).T * nvec)[0]) for L, d in exB['lev'].items()}
    sumB = canon(sum(d['t'] * perB[L] / ((2 * d['J'] + 1) * d['mu']) for L, d in exB['lev'].items()))
    arms.append(('the cubic recoupling dropped (B)', canon(sumB - VIII_SUM) != 0, 'the weighted sum becomes %s' % sumB))
    exC = exact_case('R4', ket(R(3), P5U), [ket(R(3), P5N)], shift='radial')
    badC = [g for g, ok in exC['check_i'] if not ok]
    arms.append(('the germ\'s shift along n dropped at P5 (C)', bool(badC), 'check i fails for %s' % ', '.join(badC)))
    exD = exact_case('R4', ket(R(3), {1: 1}), [], shift='none')
    kp = [rcol(ket(R(3), {-3: 1})), rcol(ket(R(3), {-3: I}))]
    DkD = canon((kp[0].T * exD['Du'] * kp[0])[0])
    arms.append(('the shift dropped at v1 (D)', DkD != so.V1_GAMMA['R4'], 'D_u on K\' becomes %s in R4' % DkD))
    for variant, label in (('no_freq', 'the frequency\'s shift dropped (E)'), ('no_lam2', 'the lambda^2 part dropped (E)'),
                           ('hermitian', 'the Hermitian pairing for the bilinear one (E)')):
        worst = 0
        for name, *_ in CASES:
            fo = first_order(exs[name], lds[name], variant=variant)
            for f, mc in zip(fo, mres[name][0]):
                worst = max(worst, max(abs(a - b) for a, b in zip(sorted(f['c'], key=lambda x: (float(mp.re(x)), float(mp.im(x)))), mc)) / abs(f['c'][0]))
        arms.append((label, worst > mp.mpf('1e-8'), 'the largest relative difference from the model becomes %s' % mp.nstr(worst, 3)))
    targets = [(g['mu0'], g['mult']) for g in lds['P5']['groups']]
    resR, _ = models['P5'].coefficients(targets, ray=True)
    worst = max(abs(mc[0] - fo['c'][0]) / abs(fo['c'][0]) for mc, fo in zip(resR, fos['P5']))
    arms.append(('the model\'s germ held on the ray at P5 (E)', worst > mp.mpf('1e-8'),
                 'the largest relative difference becomes %s' % mp.nstr(worst, 3)))
    exP, exP16 = exs['P5'], ex16s['P5']
    foOff = first_order(exP, lds['P5'], Du=tomp((exP['Du'] - exP['Off']).applyfunc(canon)))
    foOff16 = first_order(exP16, lds['P5'], Du=tomp((exP16['Du'] - exP16['Off']).applyfunc(canon)))
    okOff, bad = record_check(data, {'P5': lds['P5']}, {'P5': foOff}, {'P5': foOff16}, show=False, cases=('P5',))
    arms.append(('the off-ray shift dropped from c_g at P5 (F)', not okOff,
                 'P5\'s groups out of their spread: %s' % ', '.join(bad)))
    for label, red, why in arms:
        print('   arm: %-58s %s' % (label, 'RED' if red else 'green (FAIL)'))
        print('        %s' % why)

    # ------------------------------------------------ the result, reported
    print('the result: c_g per group, relative to kappa s_g, with its five parts, and the conditioning |l| |r|')
    for name, *_ in CASES:
        for g, fo in zip(lds[name]['groups'], fos[name]):
            mu0 = g['mu0']
            line = '   %-7s s = %-30s mult %d  c_g = %-34s c_g/(kappa s_g) = %-34s cond %s' % (
                name, fmt(g['s'], 10), g['mult'], ', '.join(fmt(c, 10) for c in fo['c']),
                ', '.join(fmt(c / mu0, 8) for c in fo['c']), mp.nstr(fo['cond'], 4))
            print(line)
            ex, ld = exs[name], lds[name]
            five = [(g['L'] * ((1 / (4 * ld['w0'])) * ld['J'] * tomp(ex[key])) * g['R'])[0, 0] / mu0
                    for key in ('Gam', 'Amp', 'Off')]
            if fo['parts']:
                five += [fo['parts'][1] / mu0, fo['parts'][2] / mu0]
                print('             parts: the spherical Hessian %s; the amplitude %s; the off-ray shift %s; the frequency %s; '
                      'lambda^2 %s' % tuple(fmt(p, 8) for p in five))
            else:
                print('             the correction on the %d-dimensional eigenspace is a multiple of the identity: %s; on it, '
                      'the spherical Hessian %s, the amplitude %s, the off-ray shift %s'
                      % (g['mult'], fo['scalar'], *[fmt(p, 8) for p in five]))

    # ------------------------------------------------ the exact values, for quadrature_check.py
    def s40(x):
        return str(sp.N(x, 40))
    out = {}
    for name, slot, *_ in CASES:
        ex = exs[name]
        out[name] = dict(slot=slot, u=[[s40(sp.re(c)), s40(sp.im(c))] for c in ex['u']], Q=str(ex['Q']), R0=s40(ex['Ru']),
                         grad=[s40(x) for x in ex['grad']], hess=[[s40(ex['HR'][a, b]) for b in range(ex['N'])]
                                                                for a in range(ex['N'])],
                         levels={str(L): s40(d['t'] * d['F0'] / ((2 * d['J'] + 1) * ex['s'] ** 3)) for L, d in ex['lev'].items()})
    text = json.dumps(out, indent=1) + '\n'
    with open(OUTJ, 'x', encoding='utf-8') as f:
        f.write(text)
    print('exact values for quadrature_check.py: %s, SHA-256 %s' % (Path(OUTJ).name, hashlib.sha256(text.encode()).hexdigest()))
    print('%d claims failed; %d/%d arms red' % (failed, sum(r for _, r, _ in arms), len(arms)))
    failed += sum(not r for _, r, _ in arms)
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
