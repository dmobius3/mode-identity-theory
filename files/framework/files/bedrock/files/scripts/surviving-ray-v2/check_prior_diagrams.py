#!/usr/bin/env python3
"""Where the point sits in the earlier spin-3 phase diagrams (Section 9's prior art), exactly, with planted failures.

1. Santos and Pfau [SP] write the spin-3 energy as c1|f|^2 + (4 c2/7)|s_-|^2 + c3 sum_ij O_ij^2, with
   O_ij = <S_i S_j>. Two identities map it onto [KU]'s second form c1~|f|^2 + c2~|A00|^2 + c3~ TrN^2, each with a
   one-line proof. (i) O_ij = N_ij + (i/2) eps_ijk f_k with N real symmetric and f real, so
   sum_ij O_ij O_ij = TrN^2 + i sum N_ij eps_ijk f_k - (1/4) sum eps_ijk eps_ijl f_k f_l = TrN^2 - |f|^2/2, the middle
   sum vanishing (symmetric against antisymmetric) and sum_ij eps_ijk eps_ijl = 2 delta_kl. (ii) <3 m; 3 -m | 0 0> =
   (-1)^(3-m)/sqrt7 = -(-1)^m/sqrt7, so A00 = -(2/sqrt7) s_- and |A00|^2 = (4/7)|s_-|^2. The script checks both
   exactly on random states, which tests the conventions, not the algebra. Which reading of [SP]'s "sum_ij O_ij^2" is
   theirs, O_ij O_ij or O_ij O_ji = TrN^2 + |f|^2/2, is fixed by their own text: their printed weight-state
   expression, transcribed below in their variables, matches O_ij O_ij up to a constant and fails for O_ij O_ji, and
   their line 256 writes the f_z^2 coefficient as c1 - c3/2. So
   c1~ = c1 - c3/2, c2~ = c2, c3~ = c3. At the point (c1~, c2~, c3~) = (6, -84, -2/3) (SOURCES_CHECK.md), so in
   [SP]'s couplings c1/c3 = -17/2, while [SP]'s chromium values (c1 = 0.059 g6, c3 = -0.002 g6) fix c1/c3 near
   -59/2 along their whole diagram, which varies only the singlet length and the field.
2. Diener and Ho [DH] write it as alpha|Theta|^2 + beta sum_M |B_M|^2 + gamma <S>^2 and, equivalently,
   alpha_bar|Theta|^2 + beta_bar TrN^2 + gamma_bar <S>^2 with alpha_bar = alpha - 5 beta/3, beta_bar = beta/18,
   gamma_bar = gamma - 5 beta/12. Since |Theta|^2 = 7|A00|^2, [KU]'s second form gives gamma_bar = c1~,
   alpha_bar = c2~/7, beta_bar = c3~, and the point is (alpha, beta, gamma) = (-32, -12, 1) at g = -1 and its
   negative at g = 1. [DH]'s chromium line is beta/gamma = -0.892 (at the point it is -12).
3. [DH]'s drawn windows, from the tick labels of its two EPS figures (read in memory, SOURCES_CHECK.md), taken with a
   margin of one tick spacing on every side, and with either assignment of the two axes: the point lies outside
   both, at g = -1 in the gamma > 0 figure and at g = 1 in the gamma < 0 figure."""
import hashlib
import random
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
RES = []


def gate(name, ok):
    RES.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name)


ms = [3, 2, 1, 0, -1, -2, -3]
Sz = sp.diag(*ms)
Sp = sp.zeros(7)
for i, m in enumerate(ms):
    if i > 0:
        Sp[i - 1, i] = sp.sqrt(12 - m * (m + 1))
Sx, Sy = (Sp + Sp.T) / 2, (Sp - Sp.T) / (2 * sp.I)
S = [Sx, Sy, Sz]


def quartics(z):
    zc = sp.Matrix([sp.conjugate(x) for x in z])
    ev = lambda A: sp.expand((zc.T * A * sp.Matrix(z))[0])
    f = [ev(Si) for Si in S]
    f2 = sp.expand(sum(fi * sp.conjugate(fi) for fi in f))
    O = [[ev(S[i] * S[j]) for j in range(3)] for i in range(3)]
    sumO2 = sp.expand(sum(O[i][j] * O[i][j] for i in range(3) for j in range(3)))
    N = [[sp.expand((O[i][j] + O[j][i]) / 2) for j in range(3)] for i in range(3)]
    trN2 = sp.expand(sum(N[i][j] * N[j][i] for i in range(3) for j in range(3)))
    sm = sp.Rational(1, 2) * sum(sp.Integer(-1) ** ms[i] * z[i] * z[6 - i] for i in range(7))
    A00 = sum(sp.Integer(-1) ** (3 - ms[i]) * z[i] * z[6 - i] for i in range(7)) / sp.sqrt(7)
    return dict(f2=f2, sumO2=sumO2, trN2=trN2, s2=sp.expand(sm * sp.conjugate(sm)),
                A2=sp.expand(A00 * sp.conjugate(A00)))


random.seed(20260922)
ok1 = ok2 = True
for _ in range(5):
    z = [sp.Rational(random.randint(-9, 9), random.randint(1, 4)) + sp.I * sp.Rational(random.randint(-9, 9),
                                                                                       random.randint(1, 4)) for _ in range(7)]
    q = quartics(z)
    ok1 = ok1 and sp.simplify(q['sumO2'] - (q['trN2'] - q['f2'] / 2)) == 0
    ok2 = ok2 and sp.simplify(q['A2'] - sp.Rational(4, 7) * q['s2']) == 0
gate('[SP]: sum_ij O_ij O_ij = TrN^2 - |f|^2/2 on five random states, exactly (a convention check; proof above)', ok1)
gate('[SP]: |A00|^2 = (4/7)|s_-|^2 on five random states, exactly (a convention check; proof above)', ok2)
# arm: a wrong sign in the first identity must fail on the same states
random.seed(20260922)
z = [sp.Rational(random.randint(-9, 9), random.randint(1, 4)) + sp.I * sp.Rational(random.randint(-9, 9),
                                                                                   random.randint(1, 4)) for _ in range(7)]
q = quartics(z)
gate('arm: sum O^2 = TrN^2 + |f|^2/2 fails', sp.simplify(q['sumO2'] - (q['trN2'] + q['f2'] / 2)) != 0 and ok1)
# [SP]'s printed expression (sp4.tex line 246), transcribed in their variables:
#   sum_ij O_ij^2 = 77 - 12 gamma_z + 3 gamma_z^2/2 - f_z^2/2 + |eta|^2/2 + 2|sigma|^2,
# at the weight states gamma_z = m^2, f_z = m, eta = sigma = 0; both readings computed from the spin matrices
def sp_printed(m):
    gz, fz, eta2, sig2 = m * m, m, 0, 0
    return 77 - 12 * gz + Fr(3, 2) * gz * gz - Fr(fz * fz, 2) + Fr(eta2, 2) + 2 * sig2


def mean_field_sums(m):
    z = [sp.Integer(1) if mm == m else sp.Integer(0) for mm in ms]
    zc = sp.Matrix(z).T
    O = [[sp.expand((zc * S[i] * S[j] * sp.Matrix(z))[0]) for j in range(3)] for i in range(3)]
    same = sp.nsimplify(sp.expand(sum(O[i][j] * O[i][j] for i in range(3) for j in range(3))))
    swapped = sp.nsimplify(sp.expand(sum(O[i][j] * O[j][i] for i in range(3) for j in range(3))))
    return Fr(str(same)), Fr(str(swapped))


offs_same = {m: sp_printed(m) - mean_field_sums(m)[0] for m in (3, 2, 1, 0)}
offs_swap = {m: sp_printed(m) - mean_field_sums(m)[1] for m in (3, 2, 1, 0)}
print(f'  [SP] printed minus sum O_ij O_ij at m = 3, 2, 1, 0: {[str(offs_same[m]) for m in (3, 2, 1, 0)]}; '
      f'minus sum O_ij O_ji: {[str(offs_swap[m]) for m in (3, 2, 1, 0)]}')
gate('[SP]\'s printed expression is sum_ij O_ij O_ij plus a constant (5), the reading the conversion uses',
     len(set(offs_same.values())) == 1)
gate('arm: the other reading, sum_ij O_ij O_ji, does not differ from it by a constant', len(set(offs_swap.values())) > 1)

ct1, ct2, ct3 = Fr(6), Fr(-84), Fr(-2, 3)            # [KU]'s second form at (1, -32, -12), from SOURCES_CHECK.md
c3 = ct3
c1 = ct1 + c3 / 2
ratio_point = c1 / c3
ratio_cr = Fr(59, 1000) / Fr(-2, 1000)
print(f'  the point in [SP]\'s couplings: c1 = {c1}, c2 = {ct2}, c3 = {c3}; c1/c3 = {ratio_point}; chromium: {ratio_cr}')
gate('the point is not on [SP]\'s chromium slice (c1/c3 = -17/2 against about -59/2)',
     ratio_point == Fr(-17, 2) and abs(ratio_cr - ratio_point) > 10)
# [DH]: invert the nematic form
gamma_bar, alpha_bar, beta_bar = ct1, ct2 / 7, ct3
beta = 18 * beta_bar
gamma = gamma_bar + Fr(5, 12) * beta
alpha = alpha_bar + Fr(5, 3) * beta
print(f'  the point in [DH]\'s coordinates: (alpha, beta, gamma) = ({alpha}, {beta}, {gamma}) at g = -1')
gate('the point is (alpha, beta, gamma) = (-32, -12, 1) in [DH]\'s form, [KU]\'s (c_alpha, c_beta, c_gamma)',
     (alpha, beta, gamma) == (-32, -12, 1))
gate('the point is not on [DH]\'s chromium line (beta/gamma = -12 against -0.892)', beta / gamma == -12)
# arm: a wrong conversion (beta_bar = beta/126, KU's own c3 normalisation) must break the match
beta_w = 126 * beta_bar
gate('arm: beta_bar = beta/126 would give a different point', (alpha_bar + Fr(5, 3) * beta_w, beta_w,
                                                               gamma_bar + Fr(5, 12) * beta_w) != (-32, -12, 1))
# [DH]'s windows: tick labels (min, max, spacing) per axis; the window is widened by one spacing on each side
TICKS = {'gamma>0': {'alpha/gamma': (-2, 6, 2), 'beta/gamma': (-5, 5, 5)},
         'gamma<0': {'alpha/|gamma|': (-15, 5, 5), 'beta/|gamma|': (-8, 0, 4)}}


def inside(pt, fig):
    (a0, a1, da), (b0, b1, db) = TICKS[fig].values()
    boxes = [((a0 - da, a1 + da), (b0 - db, b1 + db)), ((b0 - db, b1 + db), (a0 - da, a1 + da))]   # either axis assignment
    return any(lo1 <= pt[0] <= hi1 and lo2 <= pt[1] <= hi2 for (lo1, hi1), (lo2, hi2) in boxes)


pt_neg = (alpha / gamma, beta / gamma)                 # g = -1: gamma = 1 > 0
pt_pos = (-alpha / abs(-gamma), -beta / abs(-gamma))   # g = 1: (alpha, beta, gamma) = (32, 12, -1)
print(f'  the point in [DH]\'s figures: {tuple(map(str, pt_neg))} in the gamma > 0 one, {tuple(map(str, pt_pos))} in the '
      f'gamma < 0 one')
gate('the point lies outside both of [DH]\'s drawn windows, with a tick-spacing margin and either axis assignment',
     not inside(pt_neg, 'gamma>0') and not inside(pt_pos, 'gamma<0') and gamma == 1)
gate('arm: a point inside a window is found inside', inside((Fr(1), Fr(-3)), 'gamma>0') and inside((Fr(-10), Fr(-2)),
                                                                                                    'gamma<0'))
print('ALL PASS' if all(RES) else 'SOME FAILED')
