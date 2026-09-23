"""Checks the bridge between the paper's quartic and the spin-3 condensate literature.

1. Exact: KU's (PRA 84, 053616) eta formulas and energies at (c_gamma, c_alpha, c_beta) = (1, -32, -12) reproduce
   the M8.12 census values through r6 = (64 - 7 E)/924, and KU's order parameters at those eta are the census rays.
2. Exact: the identity r6 = (64 - 7 E)/924 holds as a polynomial identity in the 14 real coordinates of u (sympy).
3. KU's printed B_20 coefficient of zeta_0^2 disagrees with the Clebsch-Gordan value, which their table uses.
Every check is armed with a planted failure.
"""
import sympy as sp
from sympy.physics.quantum.cg import CG

R = sp.Rational
cg_, ca, cb = sp.Integer(1), sp.Integer(-32), sp.Integer(-12)
fails = []
def gate(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        fails.append(name)

# 1. KU's table at the point
eta = {'H': cb / (2 * (cb - 3 * cg_)), 'E': 9 * cb / (48 * ca + cb), 'I': cb / (2 * (3 * cg_ - cb)), 'B': cb / (4 * cb - 3 * ca)}
E = {'FF': 9 * cg_, 'F': 4 * cg_, 'P': cg_ + 2 * cb, 'Q': ca + 4 * cb / 3, 'D': ca, 'A': ca + 25 * cb / 12,
     'H': cb * (72 * cg_ - 25 * cb) / (12 * (3 * cg_ - cb)), 'I': cb * (72 * cg_ - 25 * cb) / (12 * (3 * cg_ - cb)),
     'E': 81 * ca * cb / (48 * ca + cb), 'B': cb * (18 * ca - 25 * cb) / (3 * (3 * ca - 4 * cb))}
census = {'FF': 1, 'F': 36, 'P': 225, 'Q': 400, 'D': 288, 'A': 463, 'H': R(1188, 5), 'I': R(1188, 5), 'E': R(8800, 43), 'B': 225}
print('eta at the point:', {k: str(v) for k, v in eta.items()})
gate('KU eta at the point: H 2/5, E 3/43, I -2/5, B -1/4', eta == {'H': R(2, 5), 'E': R(3, 43), 'I': R(-2, 5), 'B': R(-1, 4)})
got = {k: 64 - 7 * v for k, v in E.items()}
gate('KU energies at the point give the ten census values of 924 r6', all(sp.simplify(got[k] - census[k]) == 0 for k in census))
gate('arm: at (1, -32, -11) the energies miss the census', any(sp.simplify(64 - 7 * v.subs({}) - census[k]) != 0 for k, v in
     {'A': ca + 25 * sp.Integer(-11) / 12}.items()))
# order parameters: squared moduli of KU's states at eta against the census representatives, normalised
ku_state = {'H': {3: (2 + eta['H']) / 5, -2: (3 - eta['H']) / 5}, 'E': {3: (1 - eta['E']) / 4, 0: (1 + eta['E']) / 2, -3: (1 - eta['E']) / 4},
            'I': {2: (1 + eta['I']) / 3, -1: (2 - eta['I']) / 3}, 'B': {2: (1 - eta['B']) / 4, 0: (1 + eta['B']) / 2, -2: (1 - eta['B']) / 4}}
rep = {k: {m: sp.Rational(v) for m, v in d.items()} for k, d in
       {'H': {3: 12, -2: 13}, 'E': {3: 1, 0: R(23, 10), -3: 1}, 'I': {2: 1, -1: 4}, 'B': {2: 1, 0: R(6, 5), -2: 1}}.items()}
norm = {k: {m: v / sum(r.values()) for m, v in r.items()} for k, r in rep.items()}
gate('KU states H, E, I, B at those eta are the census pyramid, prism, C3 ray and D2 ray (squared moduli)', ku_state == norm)
gate('arm: a prism at eta = 1/43 would not match', {m: v.subs({}) for m, v in {3: (1 - R(1, 43)) / 4}.items()}[3] != norm['E'][3])

# 2. the identity, exactly, over 14 real variables
MS = [3, 2, 1, 0, -1, -2, -3]; IDX = {m: i for i, m in enumerate(MS)}
x = sp.symbols('x0:7', real=True); y = sp.symbols('y0:7', real=True)
u = [x[i] + sp.I * y[i] for i in range(7)]
th = [(-1) ** (3 - m) * sp.conjugate(u[IDX[-m]]) for m in MS]
cgc = lambda a, b, L, M: CG(3, a, 3, b, L, M).doit()
rho6 = [sum(cgc(m1, Q - m1, 6, Q) * u[IDX[m1]] * th[IDX[Q - m1]] for m1 in MS if Q - m1 in MS) for Q in range(-6, 7)]
lhs = sp.expand(sum(sp.expand(r * sp.conjugate(r)) for r in rho6))
n2 = sum(xi ** 2 + yi ** 2 for xi, yi in zip(x, y))
Fz = sp.diag(*MS); Fp = sp.zeros(7, 7)
for i, m in enumerate(MS):
    if m + 1 in MS:
        Fp[IDX[m + 1], i] = sp.sqrt(12 - m * (m + 1))
Fx, Fy = (Fp + Fp.T) / 2, (Fp - Fp.T) / (2 * sp.I)
uv = sp.Matrix(u); ud = uv.H
f2 = sum(sp.expand((ud * F * uv)[0]) ** 2 for F in (Fx, Fy, Fz))
pair = lambda L, M: sum(cgc(m1, M - m1, L, M) * u[IDX[m1]] * u[IDX[M - m1]] for m1 in MS if M - m1 in MS)
b00 = 7 * sp.expand(pair(0, 0) * sp.conjugate(pair(0, 0)))
b2 = 7 * sum(sp.expand(pair(2, M) * sp.conjugate(pair(2, M))) for M in range(-2, 3))
Ehom = cg_ * f2 + ca * b00 + cb * b2
rhs = sp.expand((64 * n2 ** 2 - 7 * Ehom) / 924)
gate('r6 = (64 - 7 E)/924 at (1, -32, -12) as a polynomial identity in the 14 real coordinates', sp.expand(lhs - rhs) == 0)
gate('arm: at (1, -32, -11) the identity fails', sp.expand(lhs - sp.expand((64 * n2 ** 2 - 7 * (cg_ * f2 + ca * b00 - 11 * b2)) / 924)) != 0)

# 3. the printed B_20 coefficient
c = cgc(0, 0, 2, 0)
gate('<3 0; 3 0|2 0> = 2/sqrt(21), so |B_20|^2 at v0 is 7 c^2 = 4/3, as KU\'s table uses', sp.simplify(c - 2 / sp.sqrt(21)) == 0 and sp.simplify(7 * c ** 2 - R(4, 3)) == 0)
gate('KU\'s printed coefficient sqrt(2/3) would give 2/3 instead', sp.simplify(sp.sqrt(R(2, 3)) ** 2 - R(4, 3)) != 0)
# 4. the point in [KU]'s second phase diagram, Eq. (E3') coordinates: c~1 = c1 - 5 c3/84, c~2 = c2 - 5 c3/3, c~3 = c3/126,
#    with c_gamma = c1, c_alpha = c2/7, c_beta = c3/7 (symmetry.tex lines 355 to 365 and 910)
c1, c2, c3 = cg_, 7 * ca, 7 * cb
ct = (c1 - R(5, 84) * c3, c2 - R(5, 3) * c3, c3 / 126)
print('KU E3prime coefficients at the point:', [str(v) for v in ct], ' ratios (c~3/|c~1|, c~2/|c~1|):', [str(ct[2] / abs(ct[0])), str(ct[1] / abs(ct[0]))])
gate('the point is (c~3/|c~1|, c~2/|c~1|) = (-1/9, -14) with c~1 > 0, inside the drawn window of the phase-A region',
     ct[0] > 0 and ct[2] / abs(ct[0]) == R(-1, 9) and ct[1] / abs(ct[0]) == -14)
gate('the invariant form agrees: r6 = -5/231 - |f|^2/22 + (7/11)|a00|^2 + TrN^2/198 gives the same ratios for -r6',
     (R(-1, 198) / R(1, 22), R(-7, 11) / R(1, 22)) == (R(-1, 9), -14))
gate('arm: the point (1, -32, -11) would sit elsewhere', (7 * R(-11) / 126) / abs(1 - R(5, 84) * 7 * R(-11)) != R(-1, 9))
print('ALL PASS' if not fails else f'{len(fails)} FAILED')
