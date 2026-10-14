#!/usr/bin/env python3
"""Theorem R at the outside orbits O1 and O2 of the level-6 quartic, in R4 and R5, by interval arithmetic at points
certified on the full slice system, with O3 rerun from its own certificate as the control. branches_check.py and its
output are not changed; this script imports its exact machinery (the quartic, the metric, the generators).

Inputs: the Surviving Ray's certified boxes (Section 7.2), sr_v2_certificates.json beside that paper's scripts. Its
coordinates are the binary-sextic coefficients w_k under the Bombieri metric; the weighted coordinates of
branches_check.py are p_m = w_m / sqrt((3+m)!(3-m)!) in the Condon-Shortley basis, and the two agree as
w_k = sqrt(720) p_{k-3}, since binomial(6, k) k! (6-k)! = 720. Any sign or ordering convention between them is a
symmetry of the quartic, which the value and the signature checks would expose if it were not.

  P   provenance: the certificate file's SHA-256 equals its line in that folder's SHA256SUMS
  O1  R4: from the certificate's box centre, two Newton steps at 90 digits on the slice system of branches_check.py's
      claim I (the gradient, the sphere, the four orbit generators), then Krawczyk's test on a box of radius 1e-60;
      then interval characteristic polynomials: 924 r6, whose enclosure must lie inside the certificate's, the
      signature (4, 0, 5) of M_u on N_u against the Surviving Ray's table, orbit dimension 4 from the Gram
      determinant of the tangent vectors, |J|^2 > 0 so r_u = 2, a zero of S_u of multiplicity exactly 6 = k + r_u,
      and every root of the slow polynomial in nu certified real and simple by a sign change: one positive (a real
      pair) and three negative. Theorem R(b) rests on these alone: n0 = 0, from the signature step's four zero
      eigenvalues of M_u together with k = 4 from the Gram determinant (M_u vanishes on the orbit tangent, so the
      four zeros are the tangent only when it has dimension 4), and a sign change of the full characteristic
      polynomial det(mu - S_u) at the real eigenvalue, which uses neither the zero multiplicity nor r_u; those,
      with four negative roots, are what (e) needs
  O2  R4: the same, with the signature (6, 0, 3): one positive root and three negative, Theorem R(b)
  O3  R4, the control: the same, with the signature (7, 0, 2): four negative roots, elliptic and simple, the row
      branches_check.py's claim I certifies from its own 80-digit point, Theorem R(e) with (Z)
  R5  the same three orbits with the R5 quartic, whose q_J - 1 are R4's scaled by 9/16, at the same points:
      the same signatures and types
Mutation arms, each of which must turn its claim red for its own reason: O1's refined centre moved 1e-40 with no
further Newton step (Krawczyk fails); the signature (5, 0, 4) expected at O2 (no match); the R4 quartic's q_6
raised by 1%, with Newton run to convergence (a point certifies, at a value outside O1's certificate); O3
required to be hyperbolic (its clause is (e)); a positive root of O1's slow polynomial claimed at 3/2 of its
place (no sign change). The exit status is 1 if any claim fails or any arm stays green.
Runs in under a minute.
"""
import hashlib
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import branches_check as bc  # noqa: E402

CERT_DIR = HERE.parents[3] / 'bedrock' / 'files' / 'scripts' / 'surviving-ray-v2'
CERT = CERT_DIR / 'sr_v2_certificates.json'
N = 14
ORBITS = [('O1', 'T1', (4, 0, 5)), ('O2', 'T2', (6, 0, 3)), ('O3', 'T3', (7, 0, 2))]
WEIGHTED = (3, 2, 1, 0, -1, -2, -3)


def provenance():
    digest = hashlib.sha256(CERT.read_bytes()).hexdigest()
    lines = [ln.split() for ln in (CERT_DIR / 'SHA256SUMS').read_text().splitlines()]
    listed = [ln[0] for ln in lines if len(ln) == 2 and ln[1] == CERT.name]
    return digest, len(listed) == 1 and listed[0] == digest


def start_point(cert, tag):
    o = cert['orbits'][tag]
    B = [[sp.Rational(q) for q in row] for row in o['basis_14xd']]
    d = len(B[0])
    z = [mp.mpf(c) for c in o['centre'][:d]]
    w = [sum(mp.mpf(B[a][b].p) / B[a][b].q * z[b] for b in range(d)) for a in range(N)]
    s = mp.sqrt(720)
    x = [w[m + 3] / s for m in WEIGHTED] + [w[7 + m + 3] / s for m in WEIGHTED]
    return x, list(o['value_924_r6_enclosure_as_run'])


def compile_poly(P):
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


_quartics = {}


def quartic(q):
    key = tuple(sorted(q.items()))
    if key not in _quartics:
        hp, grad, hess = bc.setup(6, q)
        _quartics[key] = (compile_poly(hp), [compile_poly(g) for g in grad],
                          [[compile_poly(e) for e in row] for row in hess])
    return _quartics[key]


def sgn(z):
    return 1 if z.a > 0 else (-1 if z.b < 0 else 0)


def berk(A, ctx):
    n = len(A)
    C = [ctx.mpf(1), -A[0][0]]
    for r in range(1, n):
        Rr, S_, Cc, arr = [A[r][j] for j in range(r)], [[A[i][j] for j in range(r)] for i in range(r)], \
            [A[i][r] for i in range(r)], A[r][r]
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


def det(A):
    if len(A) == 1:
        return A[0][0]
    return sum(((-1) ** j) * A[0][j] * det([row[:j] + row[j + 1:] for row in A[1:]]) for j in range(len(A)))


def certify(x0, q, beta, shift=0, newton=2):
    """Krawczyk on the slice system about x0, then the interval quantities Theorem R needs. None if the test fails."""
    iv = mp.iv
    iv.dps = 90
    mp.mp.dps = 90
    h_ev, g_ev, H_ev = quartic(q)
    Gd = [int(bc.metric(6)[i, i]) for i in range(N)]
    xt = list(x0)
    Gens = [bc.J0(6)] + bc.gens(6)
    Xm = [[[mp.mpf(sp.Rational(X[a, b]).p) / sp.Rational(X[a, b]).q for b in range(N)] for a in range(N)] for X in Gens]
    ks = [[sum(X[a][b] * xt[b] for b in range(N)) for a in range(N)] for X in Xm]

    def F(v, ctx):
        x, lam, c = v[:N], v[N], v[N + 1:]
        g = [ge(x, ctx) for ge in g_ev]
        out = [g[a] - lam * Gd[a] * x[a] - sum(c[i] * Gd[a] * ctx.mpf(ks[i][a]) for i in range(4)) for a in range(N)]
        out.append(sum(Gd[i] * x[i]**2 for i in range(N)) - 1)
        out += [sum(Gd[a] * ctx.mpf(ks[i][a]) * (x[a] - ctx.mpf(xt[a])) for a in range(N)) for i in range(4)]
        return out

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
    for _ in range(newton):
        step = mp.lu_solve(mp.matrix(Jm(vt, mp)), mp.matrix(F(vt, mp)))
        vt = list(mp.matrix(vt) - step)
        if max(abs(s) for s in step) < mp.mpf('1e-85'):
            break
    vt[0] += mp.mpf(shift)
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
    if not all(Kk[a].a > X[a].a and Kk[a].b < X[a].b for a in range(D)):
        return None
    U = Kk[:N]
    nrm = sum(Gd[i] * U[i]**2 for i in range(N))
    v924 = (h_ev(U, iv) / nrm**2 - 1) * 924 / iv.mpf(sp.Rational(beta).p) * iv.mpf(sp.Rational(beta).q)
    lamU = 4 * h_ev(U, iv) / nrm
    HU = [[He(U, iv) for He in row] for row in H_ev]
    MU_ = [[HU[a][b] - (lamU * Gd[a] if a == b else 0) for b in range(N)] for a in range(N)]
    cM = berk(MU_, iv)
    sig_ok = all(cM[i].a <= 0 <= cM[i].b for i in range(4)) and all(sgn(cM[i]) != 0 for i in range(4, N + 1))
    signs = [sgn(cM[i]) for i in range(4, N + 1)]
    changes = sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])
    sig = (N - 4 - changes, 0, changes - 1)
    J0m = bc.J0(6)
    SU = [[sum(iv.mpf(int(J0m[a, c])) * MU_[c][b] / Gd[c] for c in range(N) if J0m[a, c] != 0) for b in range(N)]
          for a in range(N)]
    cS = berk(SU, iv)
    mS = 0
    while cS[mS].a <= 0 <= cS[mS].b:
        mS += 1
    Pc = [cS[mS + 2 * i] for i in range((N - mS) // 2 + 1)]
    KU = [[sum(iv.mpf(Xm[g][a][b]) * U[b] for b in range(N)) for a in range(N)] for g in range(4)]
    gram = [[sum(Gd[a] * KU[g][a] * KU[h][a] for a in range(N)) for h in range(4)] for g in range(4)]
    rank4 = det(gram).a > 0
    Jv = [sum(U[a] * sum(iv.mpf(int(J0m[a, c])) * Gd[c] * KU[g][c] for c in range(N) if J0m[a, c] != 0)
              for a in range(N)) / nrm for g in (1, 2, 3)]
    J2 = sum(t**2 for t in Jv)
    return dict(v924=v924, sig=sig, sig_ok=sig_ok, mS=mS, Pc=Pc, cS=cS, rank4=rank4, J2=J2, Jv=Jv)


def slow_roots(Pc):
    """Every root of the slow polynomial in nu, each certified real and simple by a sign change of the interval
    polynomial on a bracket of relative width 2e-20; returns (negatives, positives, all certified)."""
    iv = mp.iv
    rts = mp.polyroots([mp.mpf(c.mid) for c in Pc][::-1], maxsteps=200, extraprec=200)
    real = sorted(mp.re(r) for r in rts if abs(mp.im(r)) < mp.mpf('1e-30'))

    def Pev(t):
        t = iv.mpf(t)
        return sum((c * t**i for i, c in enumerate(Pc)), iv.mpf(0))
    ok = [r for r in real if sgn(Pev(r * (1 + mp.mpf('1e-20')))) * sgn(Pev(r * (1 - mp.mpf('1e-20')))) == -1]
    deg = len(Pc) - 1
    return [r for r in ok if r < 0], [r for r in ok if r > 0], len(ok) == deg == len(real), Pev


def full_sign_change(cS, mu):
    """A sign change of the full characteristic polynomial det(mu - S_u), every coefficient as certified, across a
    bracket of relative width 2e-20 about mu: a real eigenvalue of S_u there, with no zero stripped."""
    iv = mp.iv

    def P(t):
        t = iv.mpf(t)
        return sum((c * t**j for j, c in enumerate(cS)), iv.mpf(0))
    return sgn(P(mu * (1 + mp.mpf('1e-20')))) * sgn(P(mu * (1 - mp.mpf('1e-20')))) == -1


def classify(x0, q, beta, value, sig_expected, shift=0, newton=2):
    c = certify(x0, q, beta, shift, newton)
    if c is None:
        return None
    neg, pos, allc, Pev = slow_roots(c['Pc'])
    deg = len(c['Pc']) - 1
    r_u = 2 if c['J2'].a > 0 else None
    zeros_exact = r_u is not None and c['rank4'] and c['mS'] == 4 + r_u
    sig_match = c['sig_ok'] and c['sig'] == sig_expected
    mu_real = [mp.sqrt(r) for r in pos]
    b_direct = bool(mu_real) and all(full_sign_change(c['cS'], m) for m in mu_real)
    if pos and b_direct and c['sig_ok'] and c['rank4']:
        typ, clause = f'hyperbolic: {len(pos)} real pair(s), {len(neg)} imaginary pair(s)', '(b): spectrally unstable'
    elif allc and len(neg) == deg and zeros_exact and c['sig_ok']:
        typ, clause = 'elliptic, simple', '(e): spectrally stable'
    else:
        typ, clause = 'undecided', 'does not decide it'
    lo, hi = mp.mpf(mp.iv.mpf(value[0]).a), mp.mpf(mp.iv.mpf(value[1]).b)
    value_ok = lo <= mp.mpf(c['v924'].a) and mp.mpf(c['v924'].b) <= hi
    c.update(neg=neg, pos=pos, allc=allc, typ=typ, clause=clause, r_u=r_u, zeros_exact=zeros_exact, mu_real=mu_real,
             b_direct=b_direct, value_ok=value_ok, sig_match=sig_match, Pev=Pev)
    return c


def row_ok(c, want_clause):
    if c is None or not (c['value_ok'] and c['sig_match']):
        return False
    if want_clause == '(b)':
        return c['rank4'] and c['b_direct'] and c['clause'].startswith('(b)')
    return c['rank4'] and c['zeros_exact'] and c['allc'] and c['clause'].startswith(want_clause)


def main():
    mp.mp.dps = 90
    failed = 0
    digest, prov = provenance()
    print('P  provenance: sr_v2_certificates.json, SHA-256 %s' % digest)
    print('   matches its line in SHA256SUMS: %s' % ('PASS' if prov else 'FAIL'))
    failed += not prov
    cert = json.loads(CERT.read_text())
    starts = {name: start_point(cert, tag) for name, tag, _ in ORBITS}
    want = {'O1': '(b)', 'O2': '(b)', 'O3': '(e)'}
    results = {}
    for slot, q, beta in (('R4', bc.Q4, bc.BETA['R4']), ('R5', bc.Q5, bc.BETA['R5'])):
        for name, tag, sig in ORBITS:
            x0, value = starts[name]
            c = classify(x0, q, beta, value, sig)
            results[(slot, name)] = c
            ok = row_ok(c, want[name])
            failed += not ok
            label = f'{name} {slot}' + (' (control)' if name == 'O3' else '')
            print(f'{label}: Krawczyk, radius 1e-60, on the slice system; then interval characteristic polynomials')
            if c is None:
                print('   the Krawczyk test FAILED')
                continue
            print('   924 r6 in %s' % mp.iv.nstr(c['v924'], 60))
            print('   inside the certificate\'s enclosure [%s, %s]: %s' % (value[0], value[1], c['value_ok']))
            print(f'   signature {c["sig"]} (expected {sig}); orbit dimension 4: {c["rank4"]}')
            print('   |J|^2 in %s, so r_u = %s' % (mp.iv.nstr(c['J2'], 22), c['r_u']))
            print(f'   zero multiplicity of S_u: {c["mS"]} (k + r_u = {4 + (c["r_u"] or 0)})')
            print('   slow polynomial in nu: %d roots, all certified real and simple: %s' % (len(c['Pc']) - 1, c['allc']))
            print('     positive: %s' % [mp.nstr(r, 20) for r in c['pos']])
            print('     negative: %s' % [mp.nstr(r, 20) for r in c['neg']])
            if c['pos']:
                print('   det(mu - S_u) changes sign at mu = %s: %s; with n0 = 0 (four zeros of M_u, k = 4), that is all (b) uses'
                      % (', '.join('+-' + mp.nstr(m, 15) for m in c['mu_real']), c['b_direct']))
            print(f'   {c["typ"]}; Theorem R {c["clause"]}: {"PASS" if ok else "FAIL"}')
    parents = (row_ok(results[('R4', 'O1')], '(b)') and row_ok(results[('R4', 'O2')], '(b)')
               and row_ok(results[('R4', 'O3')], '(e)'))
    print("   the arms' parents, O1, O2 and O3 in R4, pass: %s" % parents)
    failed += not parents
    arms = []
    x1, v1 = starts['O1']
    c = classify(x1, bc.Q4, bc.BETA['R4'], v1, (4, 0, 5), shift='1e-40')
    arms.append(("O1's refined centre moved 1e-40, no further Newton step: Krawczyk fails", c is None))
    x2, v2 = starts['O2']
    c = classify(x2, bc.Q4, bc.BETA['R4'], v2, (5, 0, 4))
    arms.append(('the signature (5, 0, 4) expected at O2: no match', c is not None and c['value_ok'] and not c['sig_match']))
    q_bad = dict(bc.Q4)
    q_bad[6] = q_bad[6] * sp.Rational(101, 100)
    c = classify(x1, q_bad, bc.BETA['R4'], v1, (4, 0, 5), newton=40)
    moved = mp.iv.nstr(c['v924'], 12) if c is not None else 'none'
    arms.append(("q_6 raised by 1%%, Newton converged (O1): certified at 924 r6 = %s, off O1's" % moved,
                 c is not None and not c['value_ok']))
    arms.append(('O3 required to be hyperbolic: its clause is (e)', not results[('R4', 'O3')]['clause'].startswith('(b)')))
    c1 = results[('R4', 'O1')]
    off = c1['pos'][0] * mp.mpf(3) / 2
    arms.append(("O1's positive root claimed at 3/2 of its place: no sign change",
                 sgn(c1['Pev'](off * (1 + mp.mpf('1e-20')))) * sgn(c1['Pev'](off * (1 - mp.mpf('1e-20')))) != -1))
    for label, red in arms:
        print('   arm: %-78s %s' % (label, 'RED' if red else 'green (FAIL)'))
    print('%d claims failed; %d/%d arms red' % (failed, sum(r for _, r in arms), len(arms)))
    failed += sum(not red for _, red in arms)
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
