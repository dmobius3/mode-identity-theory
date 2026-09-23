# Exact checks for the proof of the maximum in Surviving Ray v2, Section 7.3, in v2's notation.
#
# v2 writes the note's Step 1 with the paper's B_0 = [u (x) u]_0 in place of Kawaguchi and Ueda's
# a_00, and v1's time reversal Theta(sum u_m v_m) = sum (-1)^m conj(u_m) v_{-m}. Every number the
# draft states is recomputed here in those conventions, not copied from the audit. Planted
# failures sit beside the checks they target.
import sympy as sp
from sympy.physics.quantum.cg import CG

ms = list(range(-3, 4))          # index i = m + 3
results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)


def cg(j1, m1, j2, m2, J, M):
    return sp.nsimplify(CG(sp.S(j1), sp.S(m1), sp.S(j2), sp.S(m2), sp.S(J), sp.S(M)).doit())


# spin-3 matrices, Condon-Shortley
Fz = sp.diag(*ms)
Fp = sp.zeros(7, 7)
for m in ms[:-1]:
    Fp[m + 4, m + 3] = sp.sqrt(12 - m * (m + 1))
Fm = Fp.T
Fx = (Fp + Fm) / 2
Fy = (Fp - Fm) / (2 * sp.I)
F = [Fx, Fy, Fz]
I7 = sp.eye(7)

a_ = sp.symbols('a0:7', real=True)
b_ = sp.symbols('b0:7', real=True)
u = sp.Matrix([a_[i] + sp.I * b_[i] for i in range(7)])


def inner(x, y):                  # antilinear in the first slot
    return sp.expand((x.H * y)[0, 0])


def theta(x):                     # (Theta x)_m = (-1)^m conj(x_{-m})
    return sp.Matrix([(-1) ** (m % 2) * sp.conjugate(x[-m + 3]) for m in ms])


def sq(e):
    e = sp.expand(e)
    return sp.expand(e * sp.conjugate(e))


def top_norm_sq(x, y, K=6):
    tot = 0
    for M in range(-K, K + 1):
        c = sum(cg(3, m1, 3, M - m1, K, M) * x[m1 + 3] * y[M - m1 + 3] for m1 in ms if abs(M - m1) <= 3)
        tot += sq(c)
    return sp.expand(tot)


def B0(x):
    return sp.expand(sum(cg(3, m, 3, -m, 0, 0) * x[m + 3] * x[-m + 3] for m in ms))


def f_vec(x):
    return [sp.expand(inner(x, Fk * x)) for Fk in F]


def nematic(x):
    return sp.Matrix(3, 3, lambda i, j: sp.expand(inner(x, (F[i] * F[j] + F[j] * F[i]) / 2 * x)))


norm2 = inner(u, u)
fu = f_vec(u)
Nu = nematic(u)
b0 = B0(u)

# C1. B_0 = -<Theta u, u>/sqrt 7, and |B_0|^2 <= |u|^4/7 is Cauchy-Schwarz with |Theta u| = |u|.
check('B_0 = -<Theta u, u>/sqrt(7) identically', sp.expand(b0 + inner(theta(u), u) / sp.sqrt(7)) == 0)
check('|Theta u|^2 = |u|^2 identically', sp.expand(inner(theta(u), theta(u)) - norm2) == 0)

# C2. Tr N = 12 |u|^2 (the Casimir); arm: 13 fails.
check('Tr N = 12 |u|^2 identically', sp.expand(Nu.trace() - 12 * norm2) == 0)
check('arm: Tr N = 13 |u|^2 fails', sp.expand(Nu.trace() - 13 * norm2) != 0)

# C3. Step 1: |rho_6|^2 = -5/231 |u|^4 - |f|^2/22 + (7/11)|B_0|^2 + Tr N^2/198, as polynomials.
rho6 = top_norm_sq(u, theta(u))
f2 = sp.expand(sum(c ** 2 for c in fu))
trN2 = sp.expand(sum(Nu[i, j] ** 2 for i in range(3) for j in range(3)))
b02 = sq(b0)
rhs = sp.expand(sp.Rational(-5, 231) * norm2 ** 2 - f2 / 22 + sp.Rational(7, 11) * b02 + trN2 / 198)
check('Step 1 identity holds as a polynomial in 14 real variables', sp.expand(rho6 - rhs) == 0)
check('arm: 1/199 in place of 1/198 fails', sp.expand(rho6 - rhs + trN2 / 198 - trN2 / 199) != 0)

# C4. Weight-state rows, determinant 180/7, and the solved coefficients.
def at(expr, vec):
    sub = {}
    for i in range(7):
        sub[a_[i]] = sp.re(vec[i])
        sub[b_[i]] = sp.im(vec[i])
    return sp.nsimplify(expr.subs(sub))


rows, vals = [], []
for m in (3, 2, 1, 0):
    e = [0] * 7
    e[m + 3] = 1
    rows.append([at(norm2 ** 2, e), at(f2, e), at(b02, e), at(trN2, e)])
    vals.append(at(rho6, e))
R = sp.Matrix(rows)
check(f'weight rows {rows}', rows == [[1, 9, 0, sp.Rational(171, 2)], [1, 4, 0, 48], [1, 1, 0, sp.Rational(123, 2)],
                                      [1, 0, sp.Rational(1, 7), 72]])
check(f'determinant {R.det()} = 180/7', R.det() == sp.Rational(180, 7))
coef = list(R.solve(sp.Matrix(vals)))
check(f'924 r6 at the weight states = {[924 * v for v in vals]}; coefficients {coef}',
      [924 * v for v in vals] == [1, 36, 225, 400] and coef == [sp.Rational(-5, 231), sp.Rational(-1, 22), sp.Rational(7, 11), sp.Rational(1, 198)])

# C5. Step 3a: Tr(QE) = <u, A_E u> for traceless symmetric E, and the operator identity.
E = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'E{min(i, j)}{max(i, j)}', real=True))
E = E.subs(E[2, 2], -E[0, 0] - E[1, 1])
A_E = sum((((F[i] * F[j] + F[j] * F[i]) / 2) * E[i, j] for i in range(3) for j in range(3)), sp.zeros(7, 7))
Q = Nu - 4 * norm2 * sp.eye(3)
check('Tr(QE) = <u, A_E u> for every traceless symmetric E', sp.expand((Q * E).trace() - inner(u, A_E * u)) == 0)

a, b = sp.symbols('a b', real=True)
e1, e2, e3 = -a / 3 + 2 * b, -a / 3 - 2 * b, 2 * a / 3
op = e1 * Fx ** 2 + e2 * Fy ** 2 + e3 * Fz ** 2
check('e1 Fx^2 + e2 Fy^2 + e3 Fz^2 = a(Fz^2 - 4) + b(F+^2 + F-^2), with e3 = 2a/3, e1 - e2 = 4b',
      sp.simplify(op - (a * (Fz ** 2 - 4 * I7) + b * (Fp ** 2 + Fm ** 2))) == sp.zeros(7, 7))
check('e is traceless and |e|^2 = (2/3)a^2 + 8b^2',
      sp.expand(e1 + e2 + e3) == 0 and sp.expand(e1 ** 2 + e2 ** 2 + e3 ** 2 - (sp.Rational(2, 3) * a ** 2 + 8 * b ** 2)) == 0)

# C6. The split, in the adapted basis s3, s1 | t3, -t1 | s2, v0 | t2.
def v(m):
    e = sp.zeros(7, 1)
    e[m + 3] = 1
    return e


r2 = sp.sqrt(2)
basis = [(v(3) + v(-3)) / r2, (v(1) + v(-1)) / r2,
         (v(3) - v(-3)) / r2, -(v(1) - v(-1)) / r2,
         (v(2) + v(-2)) / r2, v(0),
         (v(2) - v(-2)) / r2]
U = sp.Matrix.hstack(*basis)
Op = a * (Fz ** 2 - 4 * I7) + b * (Fp ** 2 + Fm ** 2)
blk = sp.simplify(U.H * Op * U)
M1 = sp.Matrix([[5 * a, sp.sqrt(60) * b], [sp.sqrt(60) * b, -3 * a + 12 * b]])
M2 = M1.subs(b, -b)
M3 = sp.Matrix([[0, sp.sqrt(240) * b], [sp.sqrt(240) * b, -4 * a]])
target = sp.diag(M1, M2, M3, sp.zeros(1, 1))
check('A_E = M1 (+) M1(a,-b) (+) M3 (+) 0 exactly in that basis', sp.simplify(blk - target) == sp.zeros(7, 7))
U_arm = sp.Matrix.hstack(*(basis[:3] + [(v(1) - v(-1)) / r2] + basis[4:]))
blk_arm = sp.simplify(U_arm.H * Op * U_arm)
check('arm: with t1 unflipped the middle block is not literally M1(a,-b)', sp.simplify(blk_arm - target) != sp.zeros(7, 7))
check('arm: M1 and M2 differ as matrices (so the b -> -b step is needed)', sp.simplify(M1 - M2) != sp.zeros(2, 2))

# C7. Top eigenvalues of the blocks, and M3's on-ellipse form.
def top_eig_parts(M):
    t = sp.expand(M.trace() / 2)
    d = sp.expand(t ** 2 - M.det())
    return t, d


t1, d1 = top_eig_parts(M1)
t3, d3 = top_eig_parts(M3)
check(f'lambda_max(M1) = {t1} + sqrt({d1})', sp.expand(t1 - (a + 6 * b)) == 0 and sp.expand(d1 - (16 * a ** 2 - 48 * a * b + 96 * b ** 2)) == 0)
check(f'lambda_max(M3) = {t3} + sqrt({d3})', sp.expand(t3 + 2 * a) == 0 and sp.expand(d3 - (4 * a ** 2 + 240 * b ** 2)) == 0)
ell = sp.Rational(2, 3) * a ** 2 + 8 * b ** 2 - 1
check('on the ellipse 4a^2 + 240b^2 = 30 - 16a^2', sp.expand((4 * a ** 2 + 240 * b ** 2) - (30 - 16 * a ** 2) - 30 * ell) == 0)
check('arm: 2 * (the 8b^2 of the ellipse) breaks that', sp.expand((4 * a ** 2 + 240 * b ** 2) - (30 - 16 * a ** 2) - 30 * (sp.Rational(2, 3) * a ** 2 + 16 * b ** 2 - 1)) != 0)

# C8. The M1 chain.
K = 15 / sp.sqrt(6)
N2 = sp.Rational(2, 3) * a ** 2 + 8 * b ** 2
check('K^2 = 75/2 and K^2 N^2 = 25a^2 + 300b^2', sp.simplify(K ** 2 - sp.Rational(75, 2)) == 0 and sp.expand(K ** 2 * N2 - (25 * a ** 2 + 300 * b ** 2)) == 0)
check('(K - a - 6b)^2 - (16a^2 - 48ab + 96b^2) = K^2 - 2K(a + 6b) - 15a^2 + 60ab - 60b^2',
      sp.simplify((K - a - 6 * b) ** 2 - (16 * a ** 2 - 48 * a * b + 96 * b ** 2) - (K ** 2 - 2 * K * (a + 6 * b) - 15 * a ** 2 + 60 * a * b - 60 * b ** 2)) == 0)
Nn = sp.Symbol('N', positive=True)
check('homogenised: 25a^2 + 300b^2 - 2KN(a + 6b) - 15a^2 + 60ab - 60b^2 = 10[(a^2 + 6ab + 24b^2) - (3/sqrt 6) N (a + 6b)]',
      sp.simplify(25 * a ** 2 + 300 * b ** 2 - 2 * K * Nn * (a + 6 * b) - 15 * a ** 2 + 60 * a * b - 60 * b ** 2
                  - 10 * ((a ** 2 + 6 * a * b + 24 * b ** 2) - 3 / sp.sqrt(6) * Nn * (a + 6 * b))) == 0)
sos = sp.expand((a ** 2 + 6 * a * b + 24 * b ** 2) ** 2 - sp.Rational(3, 2) * (a + 6 * b) ** 2 * N2)
check('(a^2 + 6ab + 24b^2)^2 - (3/2)(a + 6b)^2 N^2 = 36 b^2 (a + 2b)^2', sp.expand(sos - 36 * b ** 2 * (a + 2 * b) ** 2) == 0)
check('arm: 23b^2 in place of 24b^2 breaks it',
      sp.expand((a ** 2 + 6 * a * b + 23 * b ** 2) ** 2 - sp.Rational(3, 2) * (a + 6 * b) ** 2 * N2 - 36 * b ** 2 * (a + 2 * b) ** 2) != 0)
check('a^2 + 6ab + 24b^2 = (a + 3b)^2 + 15b^2', sp.expand(a ** 2 + 6 * a * b + 24 * b ** 2 - (a + 3 * b) ** 2 - 15 * b ** 2) == 0)

# C9. Side conditions on the ellipse. The inequalities are tested as exact sums of squares, not
#     only as the arithmetic of their constants.
check('6 N^2 - (a + 6b)^2 = 3(a - 2b)^2, so a + 6b <= sqrt 6 on the ellipse; K - sqrt 6 = 9/sqrt 6 > 0',
      sp.expand(6 * N2 - (a + 6 * b) ** 2 - 3 * (a - 2 * b) ** 2) == 0 and sp.simplify(K - sp.sqrt(6) - 9 / sp.sqrt(6)) == 0)
check('(3/2) N^2 - a^2 = 12 b^2, so |a| <= sqrt(3/2); K + 2a >= K - 2 sqrt(3/2) = 9/sqrt 6 > 0; 30 - 16a^2 >= 6',
      sp.expand(sp.Rational(3, 2) * N2 - a ** 2 - 12 * b ** 2) == 0
      and sp.simplify(K - 2 * sp.sqrt(sp.Rational(3, 2)) - 9 / sp.sqrt(6)) == 0 and 30 - 16 * sp.Rational(3, 2) == 6)
check('arm: 5 N^2 in place of 6 N^2 is not a sum of squares (a = 2b makes it negative)',
      sp.expand(5 * N2 - (a + 6 * b) ** 2).subs({a: 2, b: 1}) < 0)

# C10. M3's square completion.
check('(K + 2a)^2 - (30 - 16a^2) = 20 (a + sqrt 6/4)^2', sp.simplify((K + 2 * a) ** 2 - (30 - 16 * a ** 2) - 20 * (a + sp.sqrt(6) / 4) ** 2) == 0)

# C11. Equality points, block by block, by an exact decision procedure: lambda_max(M) = K iff
#      det(M - K I) = 0 and tr M <= 2K. On the ellipse, with a = sqrt6 x, b = sqrt6 y.
x, y = sp.symbols('x y', real=True)
ell_xy = sp.expand(ell.subs({a: sp.sqrt(6) * x, b: sp.sqrt(6) * y}))
pts = set()
for name, M in (('M1', M1), ('M2', M2), ('M3', M3)):
    Mx = M.subs({a: sp.sqrt(6) * x, b: sp.sqrt(6) * y})
    sols = sp.solve([sp.expand((Mx - K * sp.eye(2)).det()), ell_xy], [x, y], dict=True)
    good = [s for s in sols if all(sp.im(sp.nsimplify(val)) == 0 for val in s.values())
            and sp.simplify(Mx.subs(s).trace() - 2 * K) <= 0]
    for s in good:
        pts.add((sp.nsimplify(s[x]), sp.nsimplify(s[y])))
    print(f'     {name}: equality points (x, y) = {sorted((sp.nsimplify(s[x]), sp.nsimplify(s[y])) for s in good)}')
check(f'three equality points in all: {sorted(pts)}', sorted(pts) == sorted({(sp.Rational(1, 2), 0), (sp.Rational(-1, 4), sp.Rational(1, 8)), (sp.Rational(-1, 4), sp.Rational(-1, 8))}))
eset = set()
for (px, py) in pts:
    av, bv = sp.sqrt(6) * px, sp.sqrt(6) * py
    ev = tuple(sp.nsimplify(sp.sqrt(6) * t.subs({a: av, b: bv})) for t in (e1, e2, e3))
    eset.add(ev)
check(f'they are the three permutations of (2, -1, -1)/sqrt 6: sqrt6 * e in {sorted(eset)}',
      eset == {(-1, -1, 2), (2, -1, -1), (-1, 2, -1)})

# C12. For E = (3 n n^T - I)/sqrt 6, A_E = (3 (n.F)^2 - 12)/sqrt 6, and E is unit when |n| = 1.
n = sp.symbols('n1:4', real=True)
En = (3 * sp.Matrix(n) * sp.Matrix(n).T - sp.eye(3)) / sp.sqrt(6)
A_En = sum((((F[i] * F[j] + F[j] * F[i]) / 2) * En[i, j] for i in range(3) for j in range(3)), sp.zeros(7, 7))
nF = n[0] * Fx + n[1] * Fy + n[2] * Fz
check('A_E = (3 (n.F)^2 - (F.F))/sqrt 6, and F.F = 12', sp.simplify(A_En - (3 * nF ** 2 - (Fx ** 2 + Fy ** 2 + Fz ** 2)) / sp.sqrt(6)) == sp.zeros(7, 7)
      and sp.simplify(Fx ** 2 + Fy ** 2 + Fz ** 2 - 12 * I7) == sp.zeros(7, 7))
nn = sum(t ** 2 for t in n)
check('|E|^2 = 1 when |n| = 1, and Tr E = 0', sp.expand((En * En).trace() - (9 * nn ** 2 - 6 * nn + 3) / 6) == 0 and sp.expand(En.trace() - (3 * nn - 3) / sp.sqrt(6)) == 0)

# C13. The spectrum of (3 Fz^2 - 12)/sqrt 6.
diagv = [(3 * m ** 2 - 12) / sp.sqrt(6) for m in ms]
top = max(diagv, key=lambda t: float(t))
check(f'(3Fz^2 - 12)/sqrt6 is diagonal; top value {sp.nsimplify(top)} = 15/sqrt 6, only at m = +-3',
      sp.simplify(top - K) == 0 and [m for m in ms if sp.simplify(diagv[m + 3] - K) == 0] == [-3, 3])

# C14. On span{v3, v-3}: f, B_0, N, and r6 = 463/924 - D^2/2 on the unit sphere.
al, be = sp.symbols('alpha beta')
w = al * v(3) + be * v(-3)
W = sp.Symbol('W', positive=True)
fw = f_vec(w)
check('f = (0, 0, 3(|alpha|^2 - |beta|^2)) on the span',
      sp.expand(fw[0]) == 0 and sp.expand(fw[1]) == 0 and sp.expand(fw[2] - 3 * (al * sp.conjugate(al) - be * sp.conjugate(be))) == 0)
check('<Theta w, w> = -2 alpha beta, so |B_0|^2 = 4|alpha|^2|beta|^2/7', sp.expand(inner(theta(w), w) + 2 * al * be) == 0)
Nw = nematic(w)
s2 = al * sp.conjugate(al) + be * sp.conjugate(be)
check('N = diag(3/2, 3/2, 9) |w|^2 on the span, so Tr N^2 = 171/2 on its unit sphere',
      sp.simplify(Nw - sp.diag(sp.Rational(3, 2) * s2, sp.Rational(3, 2) * s2, 9 * s2)) == sp.zeros(3, 3))
rw = top_norm_sq(w, theta(w))
D = al * sp.conjugate(al) - be * sp.conjugate(be)
check('|rho_6|^2 = (463/924)|w|^4 - D^2/2 on the span, D = |alpha|^2 - |beta|^2',
      sp.expand(rw - (sp.Rational(463, 924) * s2 ** 2 - D ** 2 / 2)) == 0)
check('arm: -D^2/3 fails', sp.expand(rw - (sp.Rational(463, 924) * s2 ** 2 - D ** 2 / 3)) != 0)

# C15. The arithmetic the text quotes.
check('-5/231 + 1/11 + 171/396 = 463/924, 48 + 75/2 = 171/2, 6!6!/12! = 1/924',
      sp.Rational(-5, 231) + sp.Rational(1, 11) + sp.Rational(171, 396) == sp.Rational(463, 924)
      and 48 + sp.Rational(75, 2) == sp.Rational(171, 2)
      and sp.factorial(6) ** 2 / sp.factorial(12) == sp.Rational(1, 924))

n_fail = sum(1 for _, ok in results if not ok)
print('ALL PASS' if n_fail == 0 else f'{n_fail} FAILED')
