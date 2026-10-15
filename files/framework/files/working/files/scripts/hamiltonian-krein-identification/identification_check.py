#!/usr/bin/env python3
"""Checks for the Hamiltonian-Krein identification: the count K = k_r + 2 k_c + 2 k_i^- = n(L) - n(D), with D the energy
on the generalized kernel of A taken modulo its kernel, and the three cases of a genuine crossing, on two-dimensional
models and on R2's degenerate point from The Soft-Slot Branches (its Hessian at the germ, its kernel K_u + K3 and
its family's complex structures). Floating point, 50 digits; second_order_check.py is imported and not changed.

For a Hamiltonian matrix A = -Omega^{-1} B, with B the energy and Omega the symplectic form: n(L) = n(B) is the
number of negative eigenvalues of B, D is B on the generalized kernel of A (it vanishes on the kernel), and K is
read from the spectrum, k_i^- from the sign of B on each imaginary eigenvector. A crossing is classified by Omega on
the whole kernel at the crossing: d3 = the rank of Omega between the family's radical R_T and the crossing
directions Z; d2 = the radical of Omega on T + Z, counted outside T; d1 = dim Z - d2 - d3.

  A  two-dimensional models: B = t I (case 1: imaginary at size |t| on both sides, the Krein sign that of t);
     B = diag(t, b), b = +-1 (case 2: |lambda|^2 = |t|, real where t b < 0, imaginary with the Krein sign of b where
     t b > 0); B = diag(0, t) with the first direction a family radical (case 3: no eigenvalue leaves zero, n(L) and
     n(D) are 1 together for t < 0, and D = 1/t on the partner); the count holds at every point
  B  R2's degenerate point, with the energy of K3 varied through zero, B_t = Hess f(y0) + t P_K3, at four members
     of its family, by their complex structures: (d1, d2, d3) = (2, 1, 0) at i, (2, 0, 1) at (i + 2j + 3k)/sqrt 14,
     and (0, 2, 1) at j and at (i + j + k)/sqrt 3; at t = +-1e-6 and +-1e-8, d1/2 pairs scale like |t| and flip
     their Krein sign, d2 pairs scale like |t|^(1/2) and are imaginary with Krein sign + for t > 0 and real for
     t < 0, n(L) goes 0 -> 3, n(D) goes 0 -> d3, and the count holds at every point
Mutation arms, each of which must turn its claim red for its own reason: the crossing classified by Omega on K3 alone,
without the family's directions (B, at the generic member: it predicts a real pair that is not there); the count
with n(D) subtracted twice, as the instrument's h with n(D) taken off again (B); Krein signs read from -B (A). The exit
status is 1 if any claim fails or any arm stays green. Runs in under a minute.
"""
import sys
from pathlib import Path

import mpmath as mp
from sympy import Rational as R

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'soft-slot-branches'))
import second_order_check as so  # noqa: E402

mp.mp.dps = 50
N = 16


# ---------------------------------------------------------------- the Hamiltonian tools
def null(A, tol=mp.mpf('1e-25')):
    U, S, V = mp.svd_r(A, full_matrices=True)
    return [V[k, :].T for k in range(A.cols) if (k >= len(S) or abs(S[k]) < tol)]


def orth(vs, tol=mp.mpf('1e-20')):
    out = []
    for v in vs:
        w = v.copy()
        for o in out:
            w -= (o.T * w)[0] * o
        n = mp.sqrt((w.T * w)[0])
        if n > tol:
            out.append(w / n)
    return out


def ham(Om, B):
    """A with Omega(A x, y) = B(x, y)."""
    return -(Om ** -1) * B


def gen_kernel(Om, E, V, r=mp.mpf('1e-15')):
    """The generalized kernel, as the Omega-annihilator of the eigenvectors of the nonzero eigenvalues: generalized
    eigenspaces for lambda and mu with lambda + mu != 0 are Omega-orthogonal (Lemma S), and Omega is nondegenerate.
    Eigenvalues below r are the numerical zeros; returns the basis and the count m0 of eigenvalues below r."""
    n = V.rows
    vs = [V[:, k] for k in range(n) if abs(E[k]) >= r]
    m0 = n - len(vs)
    if not vs:
        return [mp.matrix([1 if i == k else 0 for i in range(n)]) for k in range(n)], m0
    rows = []
    for v in vs:
        w = Om * v
        rows.append([mp.re(x) for x in w])
        rows.append([mp.im(x) for x in w])
    return orth(null(mp.matrix(rows), mp.mpf('1e-30'))), m0


def counts(Om, B, krein_sign=1, tol=mp.mpf('1e-15')):
    """n(L) = n(B); n(D) with D = B on the generalized kernel; the spectrum's K, and its small pairs."""
    A = ham(Om, B)
    nL = sum(1 for e in mp.eigsy(B)[0] if e < -mp.mpf('1e-30'))
    E, V = mp.eig(A)
    V0, m0 = gen_kernel(Om, E, V)
    nD = sum(1 for e in mp.eigsy(mp.matrix([[(a.T * B * b)[0] for b in V0] for a in V0]))[0]
             if e < -mp.mpf('1e-30')) if V0 else 0
    kr = kc = ki = 0
    pairs = []
    for k in range(A.rows):
        z = E[k]
        if abs(z) < tol:
            continue
        if abs(mp.im(z)) <= mp.mpf('1e-30') * abs(z) and mp.re(z) > 0:
            kr += 1
            pairs.append((abs(z), 'real', 0))
        elif mp.re(z) > mp.mpf('1e-30') * abs(z) and mp.im(z) > 0:
            kc += 1
            pairs.append((abs(z), 'complex', 0))
        elif mp.im(z) > 0 and abs(mp.re(z)) <= mp.mpf('1e-30') * abs(z):
            v = V[:, k]
            h = krein_sign * mp.re((v.H * B * v)[0])
            ki += h < 0
            pairs.append((abs(z), 'imag', 1 if h > 0 else -1))
    return dict(nL=nL, nD=nD, K=kr + 2 * kc + 2 * ki, kr=kr, kc=kc, ki=ki, pairs=sorted(pairs), V0=V0,
                V0_ok=len(V0) == m0)


def decomposition(Om, T, Z):
    """(d1, d2, d3) of a crossing: Omega on the whole kernel T + Z, against the family's radical R_T."""
    sig = lambda a, b: (a.T * Om * b)[0]
    RT = []
    if T:
        ST = mp.matrix([[sig(a, b) for b in T] for a in T])
        RT = [sum((c[i] * T[i] for i in range(len(T))), mp.zeros(N, 1)) for c in null(ST)]
    d3 = sum(1 for s in mp.svd_r(mp.matrix([[sig(r, z) for z in Z] for r in RT]), compute_uv=False)
             if abs(s) > mp.mpf('1e-20')) if RT else 0
    W = T + Z
    SW = mp.matrix([[sig(a, b) for b in W] for a in W])
    rad = [sum((c[i] * W[i] for i in range(len(W))), mp.zeros(N, 1)) for c in null(SW)]

    def off_T(v):
        w = v.copy()
        for o in T:
            w -= (o.T * w)[0] * o
        return w
    d2 = len(orth([off_T(v) for v in rad]))
    return len(Z) - d2 - d3, d2, d3


# ---------------------------------------------------------------- A: the two-dimensional models
OM2 = mp.matrix([[0, 1], [-1, 0]])
TS = ('1e-4', '1e-6', '-1e-6', '-1e-4')


def claim_a(krein_sign=1, out=None):
    ok, rows = True, []
    for t_ in TS:
        t = mp.mpf(t_)
        c1 = counts(OM2, mp.diag([t, t]), krein_sign)
        p = c1['pairs']
        good1 = c1['V0_ok'] and len(p) == 1 and p[0][1] == 'imag' and p[0][2] == mp.sign(t) and abs(p[0][0] - abs(t)) < 1e-40 and \
            c1['K'] == c1['nL'] - c1['nD'] and (c1['nL'], c1['nD']) == ((0, 0) if t > 0 else (2, 0))
        good2 = True
        for b in (1, -1):
            c2 = counts(OM2, mp.diag([t, b]), krein_sign)
            p = c2['pairs']
            side_real = t * b < 0
            good2 &= len(p) == 1 and abs(p[0][0] ** 2 - abs(t)) < 1e-40 and c2['K'] == c2['nL'] - c2['nD'] and \
                (p[0][1] == 'real' if side_real else (p[0][1] == 'imag' and p[0][2] == b))
        c3 = counts(OM2, mp.diag([0, t]), krein_sign)
        partner = mp.matrix([0, 1 / t])                       # A partner = the family radical (1, 0)
        Dval = (partner.T * mp.diag([0, t]) * partner)[0]
        good3 = c3['pairs'] == [] and len(c3['V0']) == 2 and abs(Dval - 1 / t) < 1e-30 * abs(1 / t) and \
            (c3['nL'], c3['nD']) == ((0, 0) if t > 0 else (1, 1)) and c3['K'] == c3['nL'] - c3['nD']
        ok &= good1 and good2 and good3
        rows.append((t_, c1, counts(OM2, mp.diag([t, 1]), krein_sign), counts(OM2, mp.diag([t, -1]), krein_sign), c3))
    if out is not None:
        out['rows'] = rows
    return ok


# ---------------------------------------------------------------- B: R2's degenerate point, at four members
def r2_setting():
    j = R(7, 2)
    M_ = so.ms(j)
    u = [mp.mpc(0)] * 8
    u[M_.index(R(5, 2))] = mp.sqrt(3) / 2
    u[M_.index(R(-3, 2))] = mp.mpf(1) / 2
    Hh, Q, HR, Ru, J0 = so.mp_hessians(j, R(1, 4), mp.mpf(24) / 13, 7, u)
    H0 = Hh / (2 * Q) - 2 * mp.eye(N)
    P = mp.zeros(8)
    for a, m in enumerate(M_):
        P[M_.index(-m), a] = (-1) ** int(j - m)
    Th = mp.zeros(N)
    for r in range(8):
        for c in range(8):
            Th[r, c], Th[8 + r, 8 + c] = P[r, c], -P[r, c]
    Jp, Jz = mp.zeros(8), mp.zeros(8)
    for a, m in enumerate(M_):
        Jz[a, a] = mp.mpf(m)
        if a > 0:
            Jp[a - 1, a] = mp.sqrt(mp.mpf(j * (j + 1) - m * (m + 1)))
    Jx, Jy = (Jp + Jp.T) / 2, (Jp - Jp.T) / (2j)
    um, uv = mp.matrix(u), so.mp_vec(u)
    Ku = orth([J0 * uv] + [so.mp_vec(list(-1j * (Jk * um))) for Jk in (Jx, Jy, Jz)] + [Th * uv, Th * J0 * uv])
    ker = orth(null(H0, mp.mpf('1e-30')))

    def off_K(v):
        w = v.copy()
        for o in Ku:
            w -= (o.T * w)[0] * o
        return w
    K3 = orth([off_K(k) for k in ker])
    PK3 = mp.zeros(N)
    for k in K3:
        PK3 += k * k.T
    return dict(H0=H0, J0=J0, Th=Th, Ku=Ku, K3=K3, PK3=PK3, ker=ker)


MEMBERS = [('i', (1, 0, 0), (2, 1, 0)), ('(i + 2j + 3k)/sqrt14', (1, 2, 3), (2, 0, 1)),
           ('j', (0, 1, 0), (0, 2, 1)), ('(i + j + k)/sqrt3', (1, 1, 1), (0, 2, 1))]
TB = ('1e-6', '1e-8', '-1e-8', '-1e-6')


def structure(s, abc):
    a, b, c = abc
    n = mp.sqrt(a * a + b * b + c * c)
    return (a * s['J0'] + b * s['Th'] + c * s['Th'] * s['J0']) / n


def claim_b(s, crossing_only=False, double_subtract=False, out=None):
    ok, rows = True, []
    for name, abc, expect in MEMBERS:
        Om = structure(s, abc)
        d = decomposition(Om, [] if crossing_only else s['Ku'], s['K3'])
        small = {}
        good = d == expect
        for t_ in TB:
            t = mp.mpf(t_)
            c = counts(Om, s['H0'] + t * s['PK3'])
            K_claim = c['nL'] - (2 * c['nD'] if double_subtract else c['nD'])
            small[t_] = [p for p in c['pairs'] if p[0] < mp.mpf('1e-2')]
            good &= c['V0_ok'] and c['K'] == K_claim and c['nL'] == (0 if t > 0 else 3) and c['nD'] == (0 if t > 0 else d[2])
            rows.append((name, t_, c, d))
        # scaling and sides: |t| pairs (ratio 100 between 1e-6 and 1e-8) and |t|^(1/2) pairs (ratio 10)
        for sgn in ('', '-'):
            big, sml = small[sgn + '1e-6'], small[sgn + '1e-8']
            lin = [(a_, b_) for a_, b_ in zip(big, sml) if abs(a_[0] / b_[0] - 100) < 1]
            sq = [(a_, b_) for a_, b_ in zip(big, sml) if abs(a_[0] / b_[0] - 10) < mp.mpf('0.1')]
            good &= len(big) == len(sml) == len(lin) + len(sq) and len(lin) == d[0] // 2 and len(sq) == d[1]
            tpos = sgn == ''
            good &= all(a_[1] == 'imag' and a_[2] == (1 if tpos else -1) for a_, _ in lin)
            good &= all((a_[1] == 'imag' and a_[2] == 1) if tpos else a_[1] == 'real' for a_, _ in sq)
        ok &= good
    if out is not None:
        out['rows'] = rows
    return ok


# ---------------------------------------------------------------- the record
def main():
    failed, arms = 0, []

    def report(ok):
        nonlocal failed
        failed += not ok
        print('   %s' % ('PASS' if ok else 'FAIL'))
    info = {}
    print('A  two-dimensional models of the three cases; the count K = n(L) - n(D) at every point')
    ok = claim_a(out=info)
    fmt = lambda c: 'n(L) %d n(D) %d K %d %s' % (c['nL'], c['nD'], c['K'], ['%s %s%s' % (
        mp.nstr(a_, 4), ty, {1: '+', -1: '-', 0: ''}[s_]) for a_, ty, s_ in c['pairs']])
    for t_, c1, c2p, c2m, c3 in info['rows']:
        print('   t = %-6s case 1: %s' % (t_, fmt(c1)))
        print('             case 2, b = +1: %s;  b = -1: %s' % (fmt(c2p), fmt(c2m)))
        print('             case 3: %s; dim of the generalized kernel %d' % (fmt(c3), len(c3['V0'])))
    report(ok)
    s = r2_setting()
    print('B  R2\'s degenerate point: K_u %d, ker %d, K3 %d; B_t = Hess f(y0) + t P_K3 at four members'
          % (len(s['Ku']), len(s['ker']), len(s['K3'])))
    info = {}
    ok = claim_b(s, out=info)
    last = None
    for name, t_, c, d in info['rows']:
        if name != last:
            print('   complex structure %s: (d1, d2, d3) = %s' % (name, d))
            last = name
        print('      t = %-6s n(L) %d n(D) %d K %d (k_r %d, k_i- %d); small pairs %s'
              % (t_, c['nL'], c['nD'], c['K'], c['kr'], c['ki'], ['%s %s%s' % (
                  mp.nstr(a_, 4), ty, {1: '+', -1: '-', 0: ''}[s_]) for a_, ty, s_ in c['pairs'] if a_ < mp.mpf('1e-2')]))
    report(ok)
    oc = {}
    claim_b(s, crossing_only=True, out=oc)
    gen = [d for n_, t_, c, d in oc['rows'] if n_.startswith('(i + 2j')][0]
    arms.append(('the crossing classified by Omega on K3 alone (B)', not claim_b(s, crossing_only=True),
                 'at the generic member it gives (d1, d2, d3) = %s, a real pair for t < 0 that the spectrum does not have'
                 % (gen,)))
    arms.append(('n(D) subtracted twice, as the instrument\'s h minus n(D) (B)', not claim_b(s, double_subtract=True),
                 'at members with d3 = 1 and t < 0, n(L) - 2 n(D) = 1 against K = 2'))
    oa = {}
    arms.append(('Krein signs read from -B (A)', not claim_a(krein_sign=-1, out=oa),
                 'case 1 at t = 1e-4 then counts its pair as Krein-negative, K = 2 against n(L) - n(D) = 0'))
    print('arms')
    for label, red, why in arms:
        print('   arm: %-60s %s' % (label, 'RED' if red else 'green (FAIL)'))
        print('        %s' % why)
    print('%d claims failed; %d/%d arms red' % (failed, sum(r for _, r, _ in arms), len(arms)))
    failed += sum(not r for _, r, _ in arms)
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
