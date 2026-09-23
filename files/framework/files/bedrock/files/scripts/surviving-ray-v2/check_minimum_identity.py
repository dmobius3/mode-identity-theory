# Exact checks for the minimum of r6 (Surviving Ray v2, Section 7.3 prerequisite).
#
# Claim (DERIVED, proved in the text by Schur's lemma): identify V_3 with binary sextics by
#   u  ->  P_u(x, y) = sum_m u_m sqrt(C(6, 3+m)) x^(3+m) y^(3-m),
# an isometry for the Bombieri norm [sum_a c_a x^a y^(n-a)]^2 = sum_a |c_a|^2 / C(n, a).
# Then [u (x) w]_6 corresponds to the product P_u P_w, so that
#   r6(u) = |rho_6(u)|^2 = |[u (x) Theta u]_6|^2 = [P_u P_{Theta u}]^2   (unit u).
# The bound r6 >= 6!6!/12! = 1/924 and its equality set are then cited results
# (Beauzamy-Bombieri-Enflo-Montgomery 1990; Reznick 1993), not checked here.
#
# Conventions are v1's: Theta(sum u_m v_m) = sum (-1)^m conj(u_m) v_{-m} (Section 2.2),
# rho_K(u) = [u (x) Theta u]_K with Condon-Shortley Clebsch-Gordan coefficients (Section 2.3),
# and the Majorana sextic F_u(z) = sum (-1)^(3-m) sqrt(C(6, 3+m)) u_m z^(3-m) (Section 2.1).
import sympy as sp
from sympy.physics.quantum.cg import CG
from math import comb

ms = list(range(-3, 4))
results = []


def check(name, cond):
    results.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)


def cg(j1, m1, j2, m2, J, M):
    return sp.nsimplify(CG(sp.S(j1), sp.S(m1), sp.S(j2), sp.S(m2), sp.S(J), sp.S(M)).doit())


# 1. The top Clebsch-Gordan coefficients are the Bombieri product coefficients, exactly.
def stretched(m1, m2):
    return sp.sqrt(sp.Rational(comb(6, 3 + m1) * comb(6, 3 + m2), comb(12, 6 + m1 + m2)))


bad = [(a, b) for a in ms for b in ms if sp.simplify(cg(3, a, 3, b, 6, a + b) - stretched(a, b)) != 0]
check(f'all 49 coefficients <3 m1; 3 m2 | 6 m1+m2> = sqrt(C(6,3+m1) C(6,3+m2) / C(12,6+m1+m2)) ({len(bad)} mismatches)', not bad)

# arm: the spin-4 coefficients are not of that form (so check 1 can fail)
bad4 = [(a, b) for a in ms for b in ms if abs(a + b) <= 4 and sp.simplify(cg(3, a, 3, b, 4, a + b) - stretched(a, b)) != 0]
check(f'arm: spin-4 coefficients fail the same test ({len(bad4)} mismatches)', len(bad4) > 0)

# 2. The polynomial identity r6 = [P_u P_{Theta u}]^2 in 14 real variables, exactly.
x, y = sp.symbols('x y')
a = sp.symbols('a0:7', real=True)
b = sp.symbols('b0:7', real=True)
u = {m: a[m + 3] + sp.I * b[m + 3] for m in ms}
theta_u = {-m: (-1) ** (m % 2) * sp.conjugate(u[m]) for m in ms}   # Theta v_m = (-1)^m v_{-m}


def sq_abs(e):
    e = sp.expand(e)
    return sp.expand(e * sp.conjugate(e))


def rho6_sq(p, q):
    total = 0
    for M in range(-6, 7):
        c = sum(cg(3, m1, 3, M - m1, 6, M) * p[m1] * q[M - m1] for m1 in ms if abs(M - m1) <= 3)
        total += sq_abs(c)
    return sp.expand(total)


def poly(p):
    return sum(p[m] * sp.sqrt(comb(6, 3 + m)) * x ** (3 + m) * y ** (3 - m) for m in ms)


def bombieri_sq(f, n):
    P = sp.Poly(sp.expand(f), x, y)
    return sp.expand(sum(sq_abs(P.coeff_monomial(x ** k * y ** (n - k))) / comb(n, k) for k in range(n + 1)))


lhs = rho6_sq(u, theta_u)
rhs = bombieri_sq(poly(u) * poly(theta_u), 12)
check('|[u (x) Theta u]_6|^2 = [P_u P_(Theta u)]^2 identically (14 real variables)', sp.expand(lhs - rhs) == 0)

# arm: Theta dropped (u (x) u against P_u^2 with Theta u's norm) breaks the r6 identity
check('arm: [P_u P_u]^2 is not |rho_6(u)|^2', sp.expand(lhs - bombieri_sq(poly(u) ** 2, 12)) != 0)
# arm: an unweighted coefficient norm on degree 12 breaks it
unweighted = sp.expand(sum(sq_abs(sp.Poly(sp.expand(poly(u) * poly(theta_u)), x, y).coeff_monomial(x ** k * y ** (12 - k)))
                           for k in range(13)))
check('arm: dropping the 1/C(12,k) weights breaks it', sp.expand(lhs - unweighted) != 0)

# 3. Isometry: [P_u]^2 = |u|^2 and [P_(Theta u)]^2 = |u|^2.
norm_u = sp.expand(sum(sq_abs(u[m]) for m in ms))
check('[P_u]^2 = |u|^2 and [P_(Theta u)]^2 = |u|^2',
      sp.expand(bombieri_sq(poly(u), 6) - norm_u) == 0 and sp.expand(bombieri_sq(poly(theta_u), 6) - norm_u) == 0)

# 4. v1's Majorana sextic, homogenised, is P_u(x, -y): a unitary substitution, so the identity
#    holds verbatim with v1's F_u, and the Bombieri norms are unchanged.
z = sp.symbols('z')
F = sum((-1) ** ((3 - m) % 2) * sp.sqrt(comb(6, 3 + m)) * u[m] * z ** (3 - m) for m in ms)
F_hom = sp.expand(x ** 6 * F.subs(z, y / x))
check("v1's F_u homogenised equals P_u(x, -y)", sp.expand(F_hom - poly(u).subs(y, -y)) == 0)

# 5. Values: v_3 gives 1/924, the hexagon (v_3 + v_-3)/sqrt 2 gives 463/924 (Section 5.5 values).
def val(coeffs):
    sub = {}
    for m in ms:
        c = sp.nsimplify(coeffs.get(m, 0))
        sub[a[m + 3]] = sp.re(c)
        sub[b[m + 3]] = sp.im(c)
    return sp.nsimplify(rhs.subs(sub))


v3 = val({3: 1})
hexa = val({3: 1 / sp.sqrt(2), -3: 1 / sp.sqrt(2)})
check(f'coherent v_3: {v3} = 1/924; hexagon: {hexa} = 463/924', v3 == sp.Rational(1, 924) and hexa == sp.Rational(463, 924))

# 6. Theta maps the constellation to its antipodal image z -> -1/conj(z), numerically at a
#    generic state (so the twelve roots of F_u F_(Theta u) are the constellation and its antipode).
import numpy as np
rng = np.random.default_rng(7)
uu = rng.normal(size=7) + 1j * rng.normal(size=7)
tu = {-m: (-1) ** (m % 2) * np.conj(uu[m + 3]) for m in ms}


def roots(coef):  # coef[m] multiplies z^(3-m) with the v1 sign and binomial factor
    c = [(-1) ** ((3 - m) % 2) * np.sqrt(comb(6, 3 + m)) * coef[m] for m in ms]   # z^6 ... z^0 as m = -3 .. 3
    return np.roots(c)


r_u = roots({m: uu[m + 3] for m in ms})
r_t = roots(tu)
anti = -1 / np.conj(r_u)
dist = max(min(abs(p - q) for q in r_t) for p in anti)
check(f'roots of F_(Theta u) are the antipodes of the roots of F_u (max distance {dist:.1e})', dist < 1e-9)

# 7. P_(Theta u)(x, y) = -conj(P_u)(y, -x), where conj conjugates the coefficients (exact), which
#    is the antipodal statement of check 6 as an identity of forms.
Pbar_swapped = sum(sp.conjugate(u[m]) * sp.sqrt(comb(6, 3 + m)) * y ** (3 + m) * (-x) ** (3 - m) for m in ms)
check('P_(Theta u)(x, y) = -conj(P_u)(y, -x) identically', sp.expand(poly(theta_u) + Pbar_swapped) == 0)
check('arm: +conj(P_u)(y, -x) fails', sp.expand(poly(theta_u) - Pbar_swapped) != 0)

# 8. The general upper bound [PQ]^2 <= [P]^2 [Q]^2 for binary forms (the product is the projection
#    of p (x) q onto the symmetric tensors), numerically on random pairs of sextics, and equality at
#    equal powers x^6 x^6. Reconnaissance for the remark in Section 7.3, not a proof.
def bsq(c):
    nn = len(c) - 1
    return float(sum(abs(c[k]) ** 2 / comb(nn, k) for k in range(nn + 1)))


ratios = []
for _ in range(20000):
    p = rng.normal(size=7) + 1j * rng.normal(size=7)
    q = rng.normal(size=7) + 1j * rng.normal(size=7)
    ratios.append(bsq(np.convolve(p, q)) / (bsq(p) * bsq(q)))
e6 = np.zeros(7)
e6[6] = 1.0
check(f'upper bound: max ratio over 20000 random pairs {max(ratios):.4f} <= 1, and x^6 x^6 gives exactly 1',
      max(ratios) <= 1 and abs(bsq(np.convolve(e6, e6)) - 1) < 1e-12)

n_fail = sum(1 for _, ok in results if not ok)
print('ALL PASS' if n_fail == 0 else f'{n_fail} FAILED')
