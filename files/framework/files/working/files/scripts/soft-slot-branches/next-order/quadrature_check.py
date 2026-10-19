#!/usr/bin/env python3
"""A floating-point cross-check of the first correction from its definition, R~0(y) = -<L0^{-1} P_perp N(psi_y),
P_perp N(psi_y)> with N(psi) = |psi|^2 psi, by quadrature on S^3 = SU(2). Fresh: it uses neither M8.16's instrument,
nor second_order_check.py, nor Lemma F's closed form, only numpy and scipy: the floating-point cross-check of the
Soft-Slot Branches, section III, Proposition N.

  python3 -I -B quadrature_check.py EXACT_JSON

EXACT_JSON: exact_values.json, from next_order_check.py: Q(u), R~0(u), its gradient and Hessian in the real basis
(Re y_m, then Im y_m, m = j, ..., -j), and the level-2J norms |P_2J N(psi_u)|^2, from Lemma F's closed form.

The construction, in units R = V = 1:
- 2I is the 120 unit quaternions, and D^j(q) = expm(-i theta n.J) for q = cos(theta/2) + sin(theta/2) n, in the
  Condon-Shortley basis |j, m>; the closure of the 120 under multiplication is checked.
- The slot's part of V_j is the eigenspace of the class sum of the 12 elements with real part cos(pi/5) whose dimension
  is dim rho (3 in R4, 4 in R5, 2 in R2): the class sum is central, so it is a scalar on each isotypic part. P_rho
  is its projector and s = dim rho / (2j + 1). Any embedding of 2I gives the same functions of y, since right
  translations act on E0 and the integrals are left-invariant.
- psi_y(x) = s^{-1/2} P_rho D^j(x) y, so that |psi_y|^2 integrates to |y|^2 against the normalized Haar measure.
- The quadrature: x = e^{-i alpha J_z} e^{-i beta J_y} e^{-i gamma J_z}, alpha and gamma on uniform grids of 32
  points, cos beta at 20 Gauss-Legendre nodes. Every integrand here has frequencies at most 6j <= 21 in each angle
  and degree at most 6j in cos beta, so the rule is exact up to round-off. The level-2J part of a section f has
  |P_2J f|^2 = (2J + 1) sum |<D^J_{m m'}, f_a>|^2.
- R~0(y) = -sum over 2J != K of |P_2J N|^2 / mu_J, mu_J = 2J(2J + 2) - K(K + 2), over every level N reaches, and its
  gradient and Hessian from DN[phi] = 2 Re(psi^+ phi) psi + |psi|^2 phi and
  D^2N[phi, chi] = 2 Re(phi^+ chi) psi + 2 Re(psi^+ phi) chi + 2 Re(psi^+ chi) phi.
The claim: at each of the five cases, Q(u), R~0(u), its gradient and its Hessian equal the exact values within
1e-10 relative to their largest entry, and the levels where N(psi_u) has a nonzero part, besides K, are exactly those
where the exact values have one, with their norms within 1e-10 of the largest. At the octahedron (C3) the slot's
channels at levels 10 and 16 are zero at u, as in M8.10's frozen values. Mutation arm: the other isotypic part of V_j in place of the slot's, which must turn the claim red.
The exit status is 1 if the claim fails or the arm stays green.
"""
import hashlib
import itertools
import json
import sys
from fractions import Fraction

import numpy as np
from scipy.linalg import expm

EXACT = sys.argv[1]
NA, NB = 32, 20
SLOTS = {'R4': (3.0, 3, 6), 'R5': (3.0, 4, 6), 'R2': (3.5, 2, 7)}   # j, dim rho, K


def ms(j):
    return [j - k for k in range(int(round(2 * j)) + 1)]


def spin(j):
    M = ms(j)
    n = len(M)
    Jz = np.diag(M).astype(complex)
    Jp = np.zeros((n, n), complex)
    for a in range(1, n):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - M[a] * (M[a] + 1))
    return (Jp + Jp.T) / 2, (Jp - Jp.T) / (2j), Jz


def quaternions():
    phi = (1 + 5 ** 0.5) / 2
    qs = set()
    for i in range(4):
        for sg in (1, -1):
            v = [0.0] * 4
            v[i] = float(sg)
            qs.add(tuple(v))
    for sg in itertools.product((0.5, -0.5), repeat=4):
        qs.add(sg)
    vals = [0.0, 1.0, 1 / phi, phi]
    even = [p for p in itertools.permutations(range(4))
            if sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b]) % 2 == 0]
    for p in even:
        for sg in itertools.product((1, -1), repeat=3):
            sv = [1] + list(sg)
            qs.add(tuple(round(vals[p[k]] * sv[p[k]] / 2, 15) for k in range(4)))
    return [np.array(q) for q in sorted(qs)]


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def Dq(j, q, J3):
    a, v = q[0], q[1:]
    nv = np.linalg.norm(v)
    th = 2 * np.arctan2(nv, a)
    n = v / nv if nv > 1e-14 else np.array([0.0, 0.0, 1.0])
    return expm(-1j * th * (n[0] * J3[0] + n[1] * J3[1] + n[2] * J3[2]))


def slot_projector(j, dim, other=False):
    J3 = spin(j)
    qs = quaternions()
    closed = len(qs) == 120 and all(min(np.abs(np.array(qs) - qmul(p, q)).sum(1)) < 1e-12
                                    for p in qs[::7] for q in qs[::5])
    C = sum(Dq(j, q, J3) for q in qs if abs(q[0] - np.cos(np.pi / 5)) < 1e-12)
    ncls = sum(1 for q in qs if abs(q[0] - np.cos(np.pi / 5)) < 1e-12)
    E, V = np.linalg.eigh((C + C.conj().T) / 2)
    vals = []
    for e in E:
        if not any(abs(e - v) < 1e-9 for v in vals):
            vals.append(e)
    parts = {v: V[:, [k for k in range(len(E)) if abs(E[k] - v) < 1e-9]] for v in vals}
    pick = [B for B in parts.values() if (B.shape[1] == dim) != other]
    assert len(vals) == 2 and len(pick) == 1, (vals, [B.shape for B in parts.values()])
    B = pick[0]
    P = B @ B.conj().T
    comm = max(np.abs(P @ Dq(j, q, J3) - Dq(j, q, J3) @ P).max() for q in qs)
    return P, B.shape[1] / (2 * j + 1), dict(closed=closed, ncls=ncls, comm=comm)


class Grid:
    def __init__(self, j, Jmax):
        self.alpha = 2 * np.pi * np.arange(NA) / NA
        self.gamma = 2 * np.pi * np.arange(NA) / NA
        xb, wb = np.polynomial.legendre.leggauss(NB)
        self.beta, self.wb = np.arccos(xb), wb
        self.j = j
        self.dj = np.array([expm(-1j * b * spin(j)[1]).real for b in self.beta])          # (NB, n, n)
        self.mj = np.array(ms(j))
        Js, J = [], (0.5 if abs(j - int(j)) > 0.25 else 0.0)
        while J <= Jmax + 1e-9:
            Js.append(J)
            J += 1
        self.Js = Js
        self.dJ = {J: np.array([expm(-1j * b * spin(J)[1]).real for b in self.beta]) for J in Js}
        self.Jmax = Jmax
        self.mfull = np.array(ms(Jmax))
        self.Ea = np.exp(1j * np.outer(self.mfull, self.alpha))    # e^{i m alpha_k}, (M, NA)
        self.Eg = np.exp(1j * np.outer(self.mfull, self.gamma))

    def section(self, P, s, y):
        """psi_y on the grid: (NA, NB, NA, n), psi = s^-1/2 P D^j(x) y, D^j_{m m'} = e^{-i m alpha} d_{m m'}(beta) e^{-i m' gamma}."""
        ph_g = np.exp(-1j * np.outer(self.gamma, self.mj))                       # (NA, n): e^{-i m' gamma}
        inner = np.einsum('bmn,gn,n->bgm', self.dj, ph_g, y)                       # sum_m' d_{m m'} e^{-i m' gamma} y_m'
        ph_a = np.exp(-1j * np.outer(self.alpha, self.mj))                       # (NA, n)
        Dy = ph_a[:, None, None, :] * inner[None, :, :, :]                        # (NA, NB, NA, n)
        return np.einsum('ab,...b->...a', P, Dy) / np.sqrt(s)

    def levels(self, f):
        """The spin-J coefficients of a section f (NA, NB, NA, n): c[J] of shape (n, 2J+1, 2J+1), orthonormal, so
        |P_2J f|^2 = sum |c[J]|^2."""
        Fh = np.einsum('ma,abgc,pg->cbmp', self.Ea, f, self.Eg)                   # (n, NB, M, M)
        out = {}
        M = len(self.mfull)
        for J in self.Js:
            sel = [k for k in range(M) if abs(self.mfull[k]) <= J + 1e-9 and abs(self.mfull[k] - J) % 1 < 1e-9]
            sub = Fh[:, :, sel][:, :, :, sel]                                     # (n, NB, 2J+1, 2J+1)
            out[J] = np.sqrt(2 * J + 1) * np.einsum('b,bmp,cbmp->cmp', self.wb, self.dJ[J], sub) / (2 * NA * NA)
        return out


def rinner(c1, c2):
    return float(np.real(np.vdot(c1, c2)))


def case(name, rec, other=False, derivs=True):
    j, dim, K = SLOTS[rec['slot']]
    P, s, info = slot_projector(j, dim, other)
    n = int(round(2 * j)) + 1
    u = np.array([float(a) + 1j * float(b) for a, b in rec['u']])
    G = Grid(j, 3 * j)
    psi = G.section(P, s, u)
    m2 = np.real(np.einsum('...a,...a->...', psi.conj(), psi))
    nrm = float(np.sum(m2 * G.wb[None, :, None]) / (2 * NA * NA))
    Q = float(np.sum(m2 ** 2 * G.wb[None, :, None]) / (2 * NA * NA))
    Nf = m2[..., None] * psi
    cN = G.levels(Nf)
    lev = {J: float(np.sum(np.abs(c) ** 2)) for J, c in cN.items()}
    used = [J for J in G.Js if abs(2 * J - K) > 1e-9]
    mu = {J: 2 * J * (2 * J + 2) - K * (K + 2) for J in used}
    R0 = -sum(lev[J] / mu[J] for J in used)
    if not derivs:
        return dict(Q=Q, nrm=nrm, R0=R0, lev=lev, s=s, info=info, K=K)
    Bas = []
    for a in range(n):
        e = np.zeros(n, complex)
        e[a] = 1
        Bas.append(e)
    for a in range(n):
        e = np.zeros(n, complex)
        e[a] = 1j
        Bas.append(e)
    phis = [G.section(P, s, e) for e in Bas]
    rp = [np.real(np.einsum('...a,...a->...', psi.conj(), ph)) for ph in phis]
    DN = [2 * rp[k][..., None] * psi + m2[..., None] * phis[k] for k in range(2 * n)]
    cDN = [G.levels(f) for f in DN]
    grad = np.array([-sum(2 * rinner(cN[J], cDN[k][J]) / mu[J] for J in used) for k in range(2 * n)])
    H = np.zeros((2 * n, 2 * n))
    for k in range(2 * n):
        for l in range(k, 2 * n):
            pkl = np.real(np.einsum('...a,...a->...', phis[k].conj(), phis[l]))
            D2 = 2 * pkl[..., None] * psi + 2 * rp[k][..., None] * phis[l] + 2 * rp[l][..., None] * phis[k]
            c2 = G.levels(D2)
            H[k, l] = H[l, k] = -sum(2 * (rinner(cDN[k][J], cDN[l][J]) + rinner(cN[J], c2[J])) / mu[J] for J in used)
    return dict(Q=Q, nrm=nrm, R0=R0, grad=grad, H=H, lev=lev, s=s, info=info, K=K)


def compare(name, rec, q):
    Qe = float(Fraction(rec['Q']))
    ge = np.array([float(x) for x in rec['grad']])
    He = np.array([[float(x) for x in row] for row in rec['hess']])
    R0e = float(rec['R0'])
    le = {int(L): float(v) for L, v in rec['levels'].items()}
    top = max(q['lev'].values())
    nz = sorted(int(round(2 * J)) for J, v in q['lev'].items() if v > 1e-12 * top and abs(2 * J - q['K']) > 1e-9)
    enz = sorted(L for L, v in le.items() if v != 0)
    etop = max(le.values())
    d = dict(Q=abs(q['Q'] - Qe), R0=abs(q['R0'] - R0e) / abs(R0e), grad=np.abs(q['grad'] - ge).max() / np.abs(ge).max(),
             hess=np.abs(q['H'] - He).max() / np.abs(He).max(),
             levels=max(abs(q['lev'][L / 2] - le[L]) for L in le) / etop if nz == enz else float('inf'))
    return d, nz, enz


def main():
    raw = open(EXACT, 'rb').read()
    ex = json.loads(raw)
    print('The first correction by quadrature on SU(2), against %s (SHA-256 %s)' % (EXACT.split('/')[-1], hashlib.sha256(raw).hexdigest()))
    print('grid: alpha, gamma %d points each, cos beta %d Gauss-Legendre nodes' % (NA, NB))
    ok = True
    for name, rec in ex.items():
        q = case(name, rec)
        d, nz, le = compare(name, rec, q)
        good = d['Q'] < 1e-12 and q['nrm'] - 1 < 1e-12 and max(d['R0'], d['grad'], d['hess'], d['levels']) < 1e-10 and \
            q['info']['closed'] and q['info']['ncls'] == 12 and q['info']['comm'] < 1e-12
        ok &= good
        print('   %-7s 2I closed: %s; class of cos(pi/5): %d elements; P_rho commutes with 2I to %.1e; s = %.6f; |psi_u|^2 = %.15f'
              % (name, q['info']['closed'], q['info']['ncls'], q['info']['comm'], q['s'], q['nrm']))
        print('           levels with a nonzero part, besides K: %s (exact: %s); Q = %.15f; R~0(u) = %.15e' % (nz, le, q['Q'], q['R0']))
        print('           relative differences: Q %.1e, R~0 %.1e, gradient %.1e, Hessian %.1e, level norms %.1e: %s'
              % (d['Q'], d['R0'], d['grad'], d['hess'], d['levels'], 'ok' if good else 'FAIL'))
    print('   %s' % ('PASS' if ok else 'FAIL'))
    arm = []
    for name in ('C2a', 'P5'):
        q = case(name, ex[name], other=True, derivs=False)
        arm.append((name, dict(Q=abs(q['Q'] - float(Fraction(ex[name]['Q']))),
                               R0=abs(q['R0'] - float(ex[name]['R0'])) / abs(float(ex[name]['R0'])))))
    red = all(max(d['Q'], d['R0']) > 1e-6 for _, d in arm)
    print('arm: the other isotypic part of V_j in place of the slot\'s: %s' % ('RED' if red else 'green (FAIL)'))
    for name, d in arm:
        print('        %s: Q differs by %.3g, R~0 by %.3g relative' % (name, d['Q'], d['R0']))
    print('1 claim, %s; the arm %s' % ('passed' if ok else 'FAILED', 'red' if red else 'green (FAIL)'))
    if not (ok and red):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
