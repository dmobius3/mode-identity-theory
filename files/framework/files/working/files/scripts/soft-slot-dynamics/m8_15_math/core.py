"""Exact machinery for the soft slots' reduced quartic (bench, M8.15 target math).

Block E0 = V_j (spin j = j2/2), weighted coordinates p_m with w_m = sqrt((j+m)!(j-m)!) p_m,
where w_m are the orthonormal Condon-Shortley components. In p-coordinates the quartic
h(w) = sum_J q_J ||[w (x) w]_J||^2, the metric, the spin generators and the quaternionic
or real structure Theta are all rational. Real coordinates x = (Re p, Im p).
"""
from functools import lru_cache
import sympy as sp
from sympy import Rational as R
from sympy.physics.wigner import clebsch_gordan


def ms(j2):
    """m values j, j-1, ..., -j as Rationals."""
    return [R(j2 - 2 * k, 2) for k in range(j2 + 1)]


def weight(j2, m):
    j = R(j2, 2)
    return sp.factorial(j + m) * sp.factorial(j - m)


@lru_cache(None)
def quartic_coeffs(j2, qkey):
    """Coefficients T[(a,b,c,d)] of h = sum T * conj(p_a) conj(p_b) p_c p_d over index tuples
    (indices into ms(j2)), with h = sum_J q_J sum_M |sum CG(m1 m2|J M) w_m1 w_m2|^2."""
    q = dict(qkey)
    j = R(j2, 2)
    M_ = ms(j2)
    n = len(M_)
    T = {}
    for J, qJ in q.items():
        for Mt in range(-J, J + 1):
            pairs = []
            for a in range(n):
                for b in range(n):
                    if M_[a] + M_[b] == Mt:
                        c = clebsch_gordan(j, j, J, M_[a], M_[b], Mt)
                        if c != 0:
                            # w_m = sqrt(weight) p_m
                            pairs.append((a, b, c * sp.sqrt(weight(j2, M_[a]) * weight(j2, M_[b]))))
            for (a, b, ca) in pairs:
                for (c_, d, cb) in pairs:
                    key = (a, b, c_, d)
                    T[key] = T.get(key, 0) + qJ * ca * cb
    return {k: sp.nsimplify(sp.simplify(v)) for k, v in T.items() if sp.simplify(v) != 0}


def real_vars(j2):
    n = j2 + 1
    xs = sp.symbols(f'x0:{n}', real=True)
    ys = sp.symbols(f'y0:{n}', real=True)
    return xs, ys


def h_poly(j2, q):
    """h as a polynomial in the real coordinates (x = Re p, y = Im p)."""
    T = quartic_coeffs(j2, tuple(sorted(q.items())))
    xs, ys = real_vars(j2)
    p = [xs[k] + sp.I * ys[k] for k in range(j2 + 1)]
    pc = [xs[k] - sp.I * ys[k] for k in range(j2 + 1)]
    expr = sum(v * pc[a] * pc[b] * p[c] * p[d] for (a, b, c, d), v in T.items())
    expr = sp.expand(expr)
    assert sp.simplify(sp.im(expr)) == 0 or sp.expand(expr - sp.conjugate(expr)) == 0
    return sp.Poly(sp.re(expr) if expr.has(sp.I) else expr, *xs, *ys)


def metric(j2):
    """G with |w|^2 = x^T G x."""
    g = [weight(j2, m) for m in ms(j2)]
    return sp.diag(*(g + g))


def J0(j2):
    n = j2 + 1
    Z, I = sp.zeros(n), sp.eye(n)
    return sp.Matrix(sp.BlockMatrix([[Z, -I], [I, Z]]))


def complex_to_real(C):
    """Real 2n x 2n matrix of the complex-linear map p -> C p (C complex n x n)."""
    A, B = C.applyfunc(sp.re), C.applyfunc(sp.im)
    return sp.Matrix(sp.BlockMatrix([[A, -B], [B, A]]))


def spin_ops(j2):
    """Complex matrices of J+, J-, Jz in p-coordinates (rational)."""
    M_ = ms(j2)
    n = len(M_)
    j = R(j2, 2)
    Jp, Jm, Jz = sp.zeros(n), sp.zeros(n), sp.zeros(n)
    for a, m in enumerate(M_):
        Jz[a, a] = m
        if a > 0:          # J+ : m -> m+1, index a-1; p'_{m+1} = (j-m) p_m
            Jp[a - 1, a] = j - m
        if a < n - 1:      # J- : m -> m-1, index a+1; p'_{m-1} = (j+m) p_m
            Jm[a + 1, a] = j + m
    return Jp, Jm, Jz


def gen_real(j2):
    """Real matrices of the right-translation generators X_a = -i J_a."""
    Jp, Jm, Jz = spin_ops(j2)
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2 * sp.I)
    return [complex_to_real(-sp.I * Ja) for Ja in (Jx, Jy, Jz)]


def Theta_real(j2):
    """Real matrix of Theta: (Theta w)_{-m} = (-1)^{j-m} conj(w_m); in p-coordinates the same law."""
    M_ = ms(j2)
    n = len(M_)
    j = R(j2, 2)
    T = sp.zeros(2 * n)
    for a, m in enumerate(M_):
        b = M_.index(-m)
        s = (-1) ** int(j - m)
        T[b, a] = s          # Re part
        T[n + b, n + a] = -s  # Im part, conjugated
    return T


def grad_hess(hp):
    gens = hp.gens
    grad = [hp.diff(v) for v in gens]
    hess = [[g.diff(v) for v in gens] for g in grad]
    return grad, hess


def evaluate(hp, grad, hess, u):
    sub = dict(zip(hp.gens, u))
    hv = sp.nsimplify(hp.as_expr().subs(sub))
    gv = sp.Matrix([sp.expand(g.as_expr().subs(sub)) for g in grad])
    Hv = sp.Matrix([[sp.expand(e.as_expr().subs(sub)) for e in row] for row in hess])
    return hv, gv, Hv
