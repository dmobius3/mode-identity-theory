"""fixed_radius_check.py -- the instrument of The Fixed Radius at Second Order (fixed-radius-second-order.md).

Two modes, kept apart as the page's §5 requires:
  qualify (the default): the instrument's algebraic identities, the cells decided before the run (H-ANISO
      exactly), the I-T and I-V reductions, the controls, each with a mutation arm that must turn its check red
      once the parents pass, and the terms-to-instrument map. It computes no grade for the open sector, I-S.
  run: refuses unless the frozen registration is on origin/main at the given commit, hashes to the given
      SHA-256, and pins this file's SHA-256, and this file equals the one at that commit. Only then does it
      grade the open sector, once, and report the I-T and I-V reductions again.

Build stage 4: the qualification core; the I-S machinery with the eigenvalue symbolic and its domain layer; the I-V
reduction; the time-averaged diagnostic; the integrability conditions; and the run with its record, run.json. All of
it is qualified on controls only: no density-sector grade, diagnostic or second-order charge is computed outside the
run, whose code path a dry run exercises on a non-physical configuration (mock_mode).

Conventions (Buchert 2001, Gen. Relativ. Gravit. 33, 1381): sigma^2 = (1/2) sigma^i_j sigma^j_i; the averaged
Raychaudhuri equation (13a) and constraint (13b) for the scaled densities N^2 eps and N^2 p, with Lambda carried
as a component of the source (eps_L = Lambda/(8 pi G), p_L = -eps_L); the kinematical backreaction (13c),
Q = (2/3) <(N theta - <N theta>)^2> - 2 <N^2 sigma^2>; the dynamical backreaction (13d), P = <N^2 A> + <N-dot theta~>,
with A = a^i_||i + a^i a_i = (D^2 N)/N the acceleration's divergence. Needs sympy.
"""
import argparse, hashlib, os, subprocess, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = "files/framework/files/working/files/fixed-radius-second-order.md"

# ---- the static background (the page's §1), parametrized by R and p0 ----
G, R = sp.symbols('G R', positive=True)
p0, cs2, p2 = sp.symbols('p_0 c_s2 p_2', real=True)        # p(eps0), p'(eps0), p''(eps0)
t, e = sp.symbols('t epsilon', real=True)                   # time, amplitude
EPS0 = 1/(4*sp.pi*G*R**2) - p0                              # 1/R^2 = 4 pi G (eps0 + p0)
LAM = 1/R**2 + 8*sp.pi*G*p0                                 # Lambda = 4 pi G (eps0 + 3 p0)
W0 = EPS0 + p0                                              # eps0 + p0 = 1/(4 pi G R^2) > 0

def pressure(deps, dvar=0, cs2_=cs2, p2_=p2):
    """the response law to second order (T2): <p> = p0 + cs2 <d eps> + (1/2) p2 <d eps_1^2>"""
    return p0 + cs2_*deps + sp.Rational(1, 2)*p2_*dvar

def eps_of_charge(x, xvar=0):
    """C1's density from the charge, by Buchert's (11a), d rho_rm / rho_rm = d eps / (eps + p). With
    x = d rho_rm / rho_rm0: eps = eps0 + W0 x + (1/2) cs2 W0 x^2 + O(x^3); averaged, x^2 carries <x^2>."""
    return EPS0 + W0*x + sp.Rational(1, 2)*cs2*W0*xvar

# ---- Buchert's averaged equations (13a), (13b), with Lambda as a source component ----
def buchert_residuals(aD, Q, P, avgN2eps, avgN2p, avgN2, avgN2R):
    """residuals of 3 aD''/aD + 4 pi G <N^2 (eps + 3p)> - Lambda <N^2> - (Q + P)        (13a)
    and of 6 (aD'/aD)^2 - 16 pi G <N^2 eps> - 2 Lambda <N^2> + (Q + <N^2 R>)           (13b)"""
    r13a = 3*sp.diff(aD, t, 2)/aD + 4*sp.pi*G*(avgN2eps + 3*avgN2p) - LAM*avgN2 - Q - P
    r13b = 6*(sp.diff(aD, t)/aD)**2 - 16*sp.pi*G*avgN2eps - 2*LAM*avgN2 + Q + avgN2R
    return r13a, r13b

def orders(expr, n=3):
    """the coefficients of epsilon^0 .. epsilon^(n-1)"""
    s = sp.series(sp.expand(expr), e, 0, n).removeO()
    return [sp.simplify(s.coeff(e, k)) for k in range(n)]

def vanishes_identically(expr, var=t):
    """an expression in t vanishes at every t: symbolically, or at several rational times"""
    expr = sp.simplify(sp.expand_trig(expr))
    if expr == 0:
        return True
    return all(sp.simplify(expr.subs(var, sp.Rational(k, 7))) == 0 for k in (1, 2, 3, 5, 11))

# ---- H-ANISO: the exact Bianchi IX model near the round S^3 (the page's §3) ----
BETA = sp.symbols('b1:4', real=True)
def bianchi_ix_ricci(beta, Ahalf=R/2):
    """a_k = A exp(beta_k), d sigma_1 = sigma_2 ^ sigma_3, so the round metric has radius R = 2A"""
    a = [Ahalf*sp.exp(bk) for bk in beta]
    den = 2*a[0]**2*a[1]**2*a[2]**2
    ric = [(a[k]**4 - (a[(k+1) % 3]**2 - a[(k+2) % 3]**2)**2)/den for k in range(3)]   # orthonormal R_(kk)
    return ric, sum(ric)

def hanio_frequency(Ahalf=R/2):
    """omega^2 from the trace-free Ricci at linear order (sigma-dot = -(trace-free Ricci) at theta = 0)"""
    x = sp.symbols('x')
    ric, R3 = bianchi_ix_ricci(BETA, Ahalf)
    lin = sp.series((ric[0] - R3/3).subs({BETA[0]: 2*x, BETA[1]: -x, BETA[2]: -x}), x, 0, 2).removeO()
    return sp.simplify(lin.coeff(x)/2)

E1 = sp.Matrix([2, -1, -1])/sp.sqrt(6)
E2 = sp.Matrix([0, 1, -1])/sp.sqrt(2)
def hanio_config(kind, w):
    if kind == 'standing':
        b = e*sp.cos(w*t)*E1
    elif kind == 'quadrature':                              # equal amplitudes 90 degrees apart: a null complex amplitude
        b = e*(sp.cos(w*t)*E1 + sp.sin(w*t)*E2)
    elif kind == 'general':                                 # unequal amplitudes: a non-null complex amplitude
        b = e*(sp.cos(w*t)*E1 + sp.Rational(1, 2)*sp.sin(w*t)*E2)
    return list(b)

def hanio_quadratics(beta, Ahalf=R/2):
    """sigma^2 = (1/2) Tr beta-dot^2, and the curvature change at fixed volume, by orders in epsilon (Ahalf = R is a
    mutation arm: the round radius taken as A instead of 2A)"""
    _, R3 = bianchi_ix_ricci(BETA, Ahalf)
    sig2 = sp.Rational(1, 2)*sum(sp.diff(bk, t)**2 for bk in beta)
    return sp.expand(sig2), orders(R3.subs({BETA[k]: beta[k] for k in range(3)}) - 6/R**2)

def hanio_cell(kind, charge, w2, drop_quadratics=False, residuals=False):
    """grade one H-ANISO configuration with R_V fixed at every instant, through Buchert's (13a), (13b).
    Homogeneous and synchronous: N = 1, Q = -2 sigma^2, P = 0. Returns (grade, detail), or with residuals=True
    the second-order residuals of (13a), (13b) and the homogeneous density shift they carry, before any reading."""
    beta = hanio_config(kind, sp.sqrt(w2))
    sig2, dR = hanio_quadratics(beta)
    assert dR[0] == 0 and dR[1] == 0
    if drop_quadratics:                                     # a mutation arm: no second-order source at all
        sig2, dR = 0, [0, 0, 0]
    deps = sp.symbols('delta_eps', real=True)               # the homogeneous second-order density shift
    r13a, r13b = buchert_residuals(sp.Integer(1), -2*sig2, 0, EPS0 + e**2*deps, pressure(e**2*deps), 1,
                                   6/R**2 + e**2*dR[2])
    ra, rb = [orders(r)[2] for r in (r13a, r13b)]
    if residuals:
        return ra, rb, deps
    w = sp.sqrt(w2)
    return read(fourier_parts(ra, w), fourier_parts(rb, w), deps, charge)

# ---- the time-averaged diagnostic (T6, the page's §4 and §5): reported beside each grade, never a grade ----
def period_average(expr, w, window=None):
    """the average over the window [0, window], by default one period 2 pi/w of the first-order mode, which spans
    whole periods of every second-order residual (frequencies 0 and 2w)"""
    P = 2*sp.pi/w if window is None else window
    return sp.simplify(sp.integrate(sp.expand(sp.expand_trig(expr)), (t, 0, P))/P)

def time_averaged_reading(ra, rb, w, charge, var, window=None, at_zero=False):
    """T6's diagnostic: the grade's own solve-and-test (read) on the period averages of the second-order residuals
    of (13a) and (13b), with the same admissible homogeneous variables and no others: none under C1, where the
    charge fixes the density; under C2, the one constant density shift var, solved from the averaged (13b) as the
    grade solves it from the constant part of the instantaneous one. No integration constant enters. window and
    at_zero are mutation arms (another window; the value at t = 0 in place of the average). The readings:
    'holds on average', 'holds on average only at ...', 'fails on average'. A time-independent configuration has
    no average to take and is marked inapplicable by the caller."""
    pa = fourier_parts(ra, w, window, at_zero, mean_only=True)
    pb = fourier_parts(rb, w, window, at_zero, mean_only=True)
    g, d = read(pa, pb, var, charge)
    if g == 'ABSORBED':
        return 'holds on average', d
    if g == 'CONDITIONAL':
        return 'holds on average only at c_s^2 = %s' % d.get('condition c_s^2', d.get('response')), d
    return 'fails on average', d

# ---- the reading shared by every grade and by the diagnostic (the page's §4) ----
RESPONSE = (cs2, p2)

def fourier_parts(r, w, window=None, at_zero=False, mean_only=False):
    """a second-order residual of a mode of frequency w is r(t) = a0 + ac cos 2wt + as sin 2wt. Returns
    [a0, ac, as/w]: the sine part divided by w, which T2's class keeps positive. window and at_zero serve the
    diagnostic's arms (a0 over another window; r(0) in place of a0)."""
    a0 = sp.simplify(r.subs(t, 0)) if at_zero else period_average(r, w, window)
    if mean_only:
        return [a0]
    return [a0, sp.simplify(2*period_average(r*sp.cos(2*w*t), w)), sp.simplify(2*period_average(r*sp.sin(2*w*t), w)/w)]

LEVEL_MIN = {'S3': 2, 'RP3': 2, 'S3/2I': 12}             # the first admitted density level on each domain

def cs2_floor(domain):
    """T2, read per domain (ruled 2026-10-11): every admitted first-order mode stays bounded, (lambda_min - 3) c_s^2 > 1,
    so c_s^2 > 1/5 on S^3 and RP^3 (n = 2) and c_s^2 > 1/165 on S^3/2I (n = 12)"""
    n = LEVEL_MIN[domain]
    return sp.Rational(1, n*(n + 2) - 3)

def admissible(sol, domain='S3', floor=None, ceiling=1):
    """T2's class on the domain: c_s^2 real, above the domain's floor, and at most 1 (ruled 2026-10-11: a condition
    above 1 is recorded, never counted). True or False where the solution fixes c_s^2 as a number; True where it
    leaves c_s^2 free; None where it ties c_s^2 to other symbols, to be judged where they are known. floor overrides
    the domain's floor and ceiling the upper end (mutation arms: one global floor; no ceiling)."""
    v = sol.get(cs2)
    if v is None:
        return True
    if v.free_symbols:
        return None
    lo = cs2_floor(domain) if floor is None else floor
    return bool(v.is_real) and bool(v > lo) and (ceiling is None or bool(v <= ceiling))

def project_shift(conds, var, constant=False):
    """the conditions on the response law alone, with C2's charge shift var a single constant that is solved, never
    set: it is solved from a condition in which it enters linearly with a nonzero coefficient free of the response
    law, and substituted into the rest. If no condition carries it, it is irrelevant. If it enters only otherwise,
    None: the caller withdraws the reading. constant=True also requires the coefficient free of lambda, so that no
    level is exceptional (the reading over levels)."""
    conds = [c for c in (sp.expand(sp.simplify(x)) for x in conds) if c != 0]
    if not any(c.has(var) for c in conds):
        return conds
    for i, c in enumerate(conds):
        if not c.has(var) or sp.diff(c, var, 2) != 0:
            continue
        a = sp.expand(sp.diff(c, var))
        if a != 0 and not (a.free_symbols & (set(RESPONSE) | ({LAMS} if constant else set()))):
            v = -sp.expand(c.subs(var, 0))/a
            return [sp.expand(sp.fraction(sp.together(x.subs(var, v)))[0]) for j, x in enumerate(conds) if j != i]
    return None

def contained(A, B):
    """every law of A lies in B (laws as solve_laws gives them)"""
    if B == 'all':
        return True
    if A == 'all':
        return False
    return all(any(all(sp.simplify(sp.sympify(k).subs(a) - sp.sympify(v).subs(a)) == 0 for k, v in b.items()) for b in B) for a in A)

def read(parts_a, parts_b, var, charge, domain='S3', floor=None, ceiling=1, old_filter=False, shift_zero=False):
    """the solve-and-test shared by every grade and the diagnostic, on the parts of the (13a) and (13b) residuals
    (all three parts for a grade at every instant; the averages alone for the diagnostic).
    The homogeneous variable var: under C1 it is zero. Under C2 it is one constant, solved, never set: from (13b)'s
    constant part when that part carries it; otherwise from another residual (project_shift). Where its coefficient
    in (13b) depends on the response law, the laws where that coefficient vanishes are read on their own: when they
    hold, they join the law set; when the generic set would wrongly keep them, the reading is withdrawn.
    Then the law set: every response law, ABSORBED; some, each within T2's class on the domain (admissible_part,
    shared with the reading over levels), CONDITIONAL with them as its condition; none, NOT ABSORBED.
    old_filter keeps every law not proved inadmissible, and shift_zero sets the shift to zero where (13b) does not
    fix it (mutation arms: the superseded behaviour)."""
    pa, pb = list(parts_a), list(parts_b)
    detail = {'parts': {'13a': pa, '13b': pb}}
    withdrawn = lambda why: ('withdrawn', dict(detail, **{'withdrawn': why, 'conditions': pa + pb, 'raw laws': None}))
    extra = []
    if charge == 'C1':
        conds = [sp.expand(x.subs(var, 0)) for x in pa + pb]
    else:
        b0 = sp.expand(sp.simplify(pb[0]))
        if b0.has(var):
            if sp.diff(b0, var, 2) != 0:
                return withdrawn('the shift enters the constraint nonlinearly')
            k, rest = sp.expand(sp.diff(b0, var)), sp.expand(b0.subs(var, 0))
            detail[str(var)] = -rest/k
            conds = [sp.expand(sp.fraction(sp.together(x.subs(var, -rest/k)))[0]) for x in pa + pb[1:]]
            if k.free_symbols & set(RESPONSE):           # the laws where the shift's coefficient vanishes
                K = solve_laws([k])
                generic = solve_laws(conds)
                for kl in ([] if K == 'all' else K):
                    sub = project_shift([x.subs(kl) for x in pa + pb], var)
                    if sub is None:
                        return withdrawn("the shift's coefficient vanishes at a law where nothing fixes the shift")
                    D = intersect_laws([kl], solve_laws(sub))
                    GK = intersect_laws(generic, [kl])
                    if contained(D, GK) and contained(GK, D):
                        continue
                    if contained(GK, D):
                        extra += D                              # held by the degenerate branch alone
                    else:
                        return withdrawn("the generic law set keeps laws where the shift's coefficient vanishes and the reading fails")
        elif shift_zero:
            conds = [sp.expand(x.subs(var, 0)) for x in pa + pb]
        else:
            conds = project_shift(pa + pb, var)
            if conds is None:
                return withdrawn('no residual fixes the shift free of the response law')
    conds = [c for c in (sp.expand(sp.simplify(x)) for x in conds) if c != 0]
    detail['conditions'] = conds
    laws = solve_laws(conds)
    if extra and laws != 'all':
        laws = laws + extra
    detail['raw laws'] = laws
    if laws == 'all':
        return 'ABSORBED', detail
    if old_filter:
        final = [(s, 'kept') for s in laws if admissible(s, domain, floor, ceiling) is not False]
    else:
        final = admissible_part(laws, domain, floor, ceiling)
    kept = [s for s, _ in final]
    detail['inadmissible'] = [s for s in laws if s not in kept]
    if final:
        detail['response'] = kept
        detail['admissibility'] = [why for _, why in final]
        cs = [s[cs2] for s in kept if cs2 in s]
        if cs:
            detail['condition c_s^2'] = cs
        return 'CONDITIONAL', detail
    return 'NOT ABSORBED', detail

def hanio_diagnostic(kind, charge, w2, **kw):
    ra, rb, deps = hanio_cell(kind, charge, w2, residuals=True)
    return time_averaged_reading(ra, rb, sp.sqrt(w2), charge, deps, **kw)

# ---- the positive control: an exact closed FLRW solution near the static one, radius free (the page's §5) ----
def flrw_separatrix(cs2_val, p2_val):
    """x1, x2 of the exact FLRW separatrix at fixed matter content (see flrw_second_order), and the static check"""
    xs = sp.symbols('x')
    c1, c2_, c3 = sp.symbols('c1 c2 c3')
    eps_x = EPS0 + c1*xs + c2_*xs**2 + c3*xs**3
    lnfac = sp.series(sp.log(1 + xs), xs, 0, 4).removeO()
    peps = p0 + cs2_val*(eps_x - EPS0) + sp.Rational(1, 2)*p2_val*(eps_x - EPS0)**2
    eq = sp.expand(sp.diff(eps_x, xs) + 3*(eps_x + peps)*sp.diff(lnfac, xs))
    sol = sp.solve([sp.series(eq, xs, 0, 3).removeO().coeff(xs, k) for k in range(3)], [c1, c2_, c3], dict=True)[0]
    eps_x = eps_x.subs(sol)
    Phi = sp.expand(sp.simplify(sp.series((1 + xs)**2*(8*sp.pi*G/3*eps_x + LAM/3 - 1/(R**2*(1 + xs)**2)), xs, 0, 4).removeO()))
    static = sp.simplify(Phi.coeff(xs, 0)) == 0 and sp.simplify(Phi.coeff(xs, 1)) == 0
    lam2, phi3 = sp.simplify(Phi.coeff(xs, 2)), sp.simplify(Phi.coeff(xs, 3))
    x1 = sp.exp(sp.sqrt(lam2)*t)
    x2f = sp.Function('x2')
    x2 = sp.dsolve(sp.Eq(x2f(t).diff(t, 2) - lam2*x2f(t), sp.Rational(3, 2)*phi3*x1**2),
                   ics={x2f(0): 0, x2f(t).diff(t).subs(t, 0): 0}).rhs
    return x1, x2, eps_x, xs, lam2, static

def flrw_second_order(cs2_val, p2_val, corrupt=False):
    """a(t) = R(1 + x(t)) to second order, built from the exact first integral
    H^2 = (8 pi G/3) eps(a) + Lambda/3 - 1/a^2, with eps(a) from continuity at fixed matter content, and not from
    Buchert's form. At fixed matter content the first integral admits, near the static point, only the separatrix
    x1 = exp(lambda t) (Eddington's mode); x2 solves x2'' - lambda^2 x2 = (3/2) phi3 x1^2. Then Buchert's residuals
    are evaluated on it, with Q = P = 0 and <N^2 R> = 6/a^2."""
    xs = sp.symbols('x')
    c1, c2_, c3 = sp.symbols('c1 c2 c3')
    eps_x = EPS0 + c1*xs + c2_*xs**2 + c3*xs**3
    lnfac = sp.series(sp.log(1 + xs), xs, 0, 4).removeO()
    peps = p0 + cs2_val*(eps_x - EPS0) + sp.Rational(1, 2)*p2_val*(eps_x - EPS0)**2
    eq = sp.expand(sp.diff(eps_x, xs) + 3*(eps_x + peps)*sp.diff(lnfac, xs))     # d eps/dx = -3 (eps + p) d ln(1+x)/dx
    sol = sp.solve([sp.series(eq, xs, 0, 3).removeO().coeff(xs, k) for k in range(3)], [c1, c2_, c3], dict=True)[0]
    eps_x = eps_x.subs(sol)
    Phi = sp.expand(sp.simplify(sp.series((1 + xs)**2*(8*sp.pi*G/3*eps_x + LAM/3 - 1/(R**2*(1 + xs)**2)), xs, 0, 4).removeO()))
    static = sp.simplify(Phi.coeff(xs, 0)) == 0 and sp.simplify(Phi.coeff(xs, 1)) == 0
    lam2, phi3 = sp.simplify(Phi.coeff(xs, 2)), sp.simplify(Phi.coeff(xs, 3))
    x1 = sp.exp(sp.sqrt(lam2)*t)
    x2f = sp.Function('x2')
    x2 = sp.dsolve(sp.Eq(x2f(t).diff(t, 2) - lam2*x2f(t), sp.Rational(3, 2)*phi3*x1**2),
                   ics={x2f(0): 0, x2f(t).diff(t).subs(t, 0): 0}).rhs
    if corrupt:
        x2 = 2*x2                                           # a mutation arm: the second-order response doubled
    x = e*x1 + e**2*x2
    aD = R*(1 + x)
    eps_av = eps_x.subs(xs, x)
    p_av = p0 + cs2_val*(eps_av - EPS0) + sp.Rational(1, 2)*p2_val*(eps_av - EPS0)**2
    r13a, r13b = buchert_residuals(aD, 0, 0, eps_av, p_av, 1, 6/aD**2)
    return static, [orders(r) for r in (r13a, r13b)], lam2

# ---- the I-T reduction, structurally (the page's §3 and §5) ----
def it_reduction(tt=True):
    """A transverse-traceless first-order perturbation h1 of the round S^3, with the fluid at rest. Its trace, the
    trace's rate and gradient, and its divergence vanish (tt=True; the mutation arm keeps a trace). Then:
      the first-order curvature, D.D.h1 - D^2 tr h1 - (2/R^2) tr h1, vanishes, so the Hamiltonian constraint gives
        no density at a static background (where K = 0);
      the expansion, theta1 = (1/2) d(tr h1)/dt, vanishes, and so does the momentum constraint's source,
        (1/2) d/dt (D.h1 - D tr h1), so there is no momentum;
      with no pressure gradient there is no acceleration, a_i = -D_i p/(eps + p), and the first-order lapse is a
        constant, zero by gauge.
    At second order (13c) gives Q = (2/3) <theta1^2> - 2 <sigma^2> = -2 <sigma^2>, and (13d) gives P = 0: with
    N = 1 + O(eps^2), <N^2 A> = <D^2 N2> + O(eps^3) averages to zero over a closed slice, and N-dot theta~ = O(eps^4)."""
    trh, divh, divdivh, laptr, trh_dot, divh_dot, gtrh_dot, sig2 = sp.symbols(
        'trh divh divdivh laptr trh_dot divh_dot gtrh_dot sigma2_avg')
    conds = dict.fromkeys([trh, divh, divdivh, laptr, trh_dot, divh_dot, gtrh_dot], 0) if tt else {}
    dR1 = (divdivh - laptr - 2/R**2*trh).subs(conds)
    deps1 = sp.simplify(dR1/(16*sp.pi*G))
    theta1 = (sp.Rational(1, 2)*trh_dot).subs(conds)
    mom1 = (sp.Rational(1, 2)*(divh_dot - gtrh_dot)).subs(conds)
    lapse1 = 0 if deps1 == 0 else sp.Symbol('nu1')
    Q2 = sp.Rational(2, 3)*theta1**2 - 2*sig2
    P2 = 0 if lapse1 == 0 else sp.Symbol('P_lapse')
    ok = deps1 == 0 and theta1 == 0 and mom1 == 0 and lapse1 == 0 and sp.simplify(Q2 + 2*sig2) == 0 and P2 == 0
    return ok, {'d eps1': deps1, 'theta1': theta1, 'momentum1': mom1, 'lapse1': lapse1, 'Q2': Q2, 'P2': P2}

# ---- I-S, the density sector (the page's §2 and §5): machinery, controls, and a grader the run alone calls ----
chi = sp.Symbol('chi', real=True)
uu = sp.Symbol('u', real=True)

def zonal_Q(n):
    """the zonal scalar harmonic sin((n+1) chi)/sin chi = U_n(cos chi): eigenvalue -n(n+2), unit mean square on S^3"""
    return sp.chebyshevu(n, sp.cos(chi))

def to_u(expr):
    """a zonal scalar, even in sin chi, as a polynomial in u = cos chi (asserted)"""
    ex = sp.expand(sp.expand_trig(expr)).subs(sp.sin(chi), sp.sqrt(1 - uu**2)).subs(sp.cos(chi), uu)
    num, den = sp.fraction(sp.cancel(sp.together(sp.expand(ex))))
    assert not den.has(uu), f'not a polynomial in cos chi: {den}'
    return sp.expand(num/den)

def S3avg(f):
    """the background average over S^3 of a zonal function, exactly:
    (2/pi) int_{-1}^{1} f(u) sqrt(1 - u^2) du, with int u^(2m) sqrt(1 - u^2) du = Gamma(m + 1/2) Gamma(3/2)/Gamma(m + 2)"""
    tot = 0
    for (k,), c in sp.Poly(to_u(f), uu).terms():
        if k % 2 == 0:
            m = k//2
            tot += c*sp.gamma(m + sp.Rational(1, 2))*sp.gamma(sp.Rational(3, 2))/sp.gamma(m + 2)
    return sp.simplify(2/sp.pi*tot)

def tc(expr, n=3):
    """Taylor coefficients in epsilon, by differentiation"""
    out, d = [], expr
    for k in range(n):
        out.append(sp.expand(d.subs(e, 0)/sp.factorial(k)))
        d = sp.diff(d, e)
    return out

def avg_ser(fs, js):
    """the J-weighted average to second order, from coefficient lists of f and of J/J0"""
    num = [S3avg(sum(fs[i]*js[k - i] for i in range(k + 1))) for k in range(3)]
    den = [S3avg(js[k]) for k in range(3)]
    q0 = num[0]/den[0]; q1 = (num[1] - q0*den[1])/den[0]; q2 = (num[2] - q0*den[2] - q1*den[1])/den[0]
    return [sp.expand(q0), sp.expand(q1), sp.expand(q2)]

def mul(a, b):
    return [sp.expand(sum(a[i]*b[k - i] for i in range(k + 1))) for k in range(3)]

def ricci_scalar_warped(Gchi, F):
    """R^2 (Gchi dchi^2 + F sin^2 chi dOmega^2) = a^2 dchi^2 + r^2 dOmega^2: -4 (r'/a)'/(a r) + 2 (1 - (r'/a)^2)/r^2"""
    a, r = R*sp.sqrt(Gchi), R*sp.sin(chi)*sp.sqrt(F)
    rs = sp.diff(r, chi)/a
    return -4*sp.diff(rs, chi)/(a*r) + 2*(1 - rs**2)/r**2

def is_metric(psi1, E1, c2):
    """g_ij = R^2 [(1 - 2 e psi1 - 2 e^2 c2) gamma + 2 e grad grad E1], zonal and diagonal: (Gchi, F = Gtheta/sin^2 chi)"""
    Gchi = 1 - 2*e*psi1 - 2*e**2*c2 + 2*e*sp.diff(E1, chi, 2)
    F = 1 - 2*e*psi1 - 2*e**2*c2 + 2*e*sp.cos(chi)/sp.sin(chi)*sp.diff(E1, chi)
    return Gchi, F

def averaged_curvature(psi1, E1, fix_volume=True):
    """<R>_J by orders, with the homogeneous second-order trace c2 fixing R_V (or c2 = 0, a mutation arm)"""
    c2s = sp.Symbol('c2')
    Gchi, F = is_metric(psi1, E1, c2s)
    js = tc(sp.sqrt(Gchi)*F)
    c2v = sp.solve(S3avg(js[2]), c2s)[0] if fix_volume else 0
    Gchi, F, js = Gchi.subs(c2s, c2v), F.subs(c2s, c2v), [x.subs(c2s, c2v) for x in js]
    return avg_ser(tc(ricci_scalar_warped(Gchi, F)), js)

def is_residuals(nu1, psi1, E1, x1, c2=None, nu2h=sp.Symbol('nu2h'), aD=None, charge='C1', kappa=0):
    """Buchert's (13a), (13b) by orders, for comoving-orthogonal zonal fields:
      N = 1 + e nu1 + e^2 nu2h, nu2h the homogeneous lapse (gauge);
      g_ij = R^2 [(1 - 2 e psi1 - 2 e^2 c2) gamma + 2 e grad grad E1], c2 = None solving R_V fixed (then aD = R);
      the rest-mass x = d rho_rm / rho_rm0 = e x1 + e^2 x2h, x2h homogeneous and fixed by the charge,
      N = int rho_rm J held at its background value (C1) or N0 (1 + e^2 kappa) (C2);
      eps(x) by Buchert's (11a), p(eps) by the response law of T2.
    The second-order fields' inhomogeneous parts do not enter these averages at second order."""
    c2s = sp.Symbol('c2')
    Gchi, F = is_metric(psi1, E1, c2s if c2 is None else c2)
    js = tc(sp.sqrt(Gchi)*F)
    vol = [S3avg(x) for x in js]
    if c2 is None:
        c2v = sp.solve(vol[2], c2s)[0]
        Gchi, F, js = Gchi.subs(c2s, c2v), F.subs(c2s, c2v), [x.subs(c2s, c2v) for x in js]
        vol = [S3avg(x) for x in js]
        aD = R
    N = 1 + e*nu1 + e**2*nu2h
    x2h = sp.Symbol('x2h')
    xloc = e*x1 + e**2*x2h
    target = tc((1 + (e**2*kappa if charge == 'C2' else 0))/(vol[0] + e*vol[1] + e**2*vol[2]) - 1)
    xav = avg_ser(tc(xloc), js)
    assert sp.simplify(xav[1] - target[1]) == 0
    xloc = xloc.subs(x2h, sp.solve(sp.expand(xav[2] - target[2]), x2h)[0])
    epsloc = EPS0 + W0*xloc + sp.Rational(1, 2)*cs2*W0*xloc**2
    ploc = pressure(epsloc - EPS0, (epsloc - EPS0)**2)
    Tchi = sp.diff(sp.log(Gchi), t)/(2*N); Tth = sp.diff(sp.log(F), t)/(2*N)
    theta = Tchi + 2*Tth
    sig2 = sp.Rational(1, 2)*((Tchi - theta/3)**2 + 2*(Tth - theta/3)**2)
    A = lambda f: avg_ser(tc(f), js)
    Nth = A(N*theta)
    Q = [sp.Rational(2, 3)*(a - b) - 2*c for a, b, c in zip(A(N**2*theta**2), mul(Nth, Nth), A(N**2*sig2))]
    P = [-a + b for a, b in zip(A(sp.diff(N, chi)**2/(R**2*Gchi)), A(sp.diff(N, t)*theta))]   # <N D^2 N> = -<|DN|^2>
    aDs, hD = tc(3*sp.diff(aD, t, 2)/aD), tc(6*(sp.diff(aD, t)/aD)**2)
    Ne, Np, N2, NR = A(N**2*epsloc), A(N**2*ploc), A(N**2), A(N**2*ricci_scalar_warped(Gchi, F))
    r13a = [aDs[k] + 4*sp.pi*G*(Ne[k] + 3*Np[k]) - LAM*N2[k] - Q[k] - P[k] for k in range(3)]
    r13b = [hD[k] - 16*sp.pi*G*Ne[k] - 2*LAM*N2[k] + Q[k] + NR[k] for k in range(3)]
    return r13a, r13b

def is_mode(n, T):
    """the first-order density mode in the comoving-orthogonal gauge, with lambda = n(n+2):
    psi = Q T, E = -Q T, nu = cs2 (lambda - 3) Q T, x = d rho_rm/rho_rm0 = -(lambda - 3) Q T,
    omega^2 = (cs2 (lambda - 3) - 1)/R^2; checked against the direct Einstein-tensor solve (is_mode_direct)"""
    Q, lam = zonal_Q(n), n*(n + 2)
    return {'nu1': cs2*(lam - 3)*Q*T, 'psi1': Q*T, 'E1': -Q*T, 'x1': -(lam - 3)*Q*T,
            'omega2': (cs2*(lam - 3) - 1)/R**2}

def _ricci_diag(gd, X):
    n = len(X)
    ginv = [1/x for x in gd]
    Gam = [[[sp.Rational(1, 2)*ginv[a]*((sp.diff(gd[a], X[c]) if a == b else 0) + (sp.diff(gd[a], X[b]) if a == c else 0)
              - (sp.diff(gd[b], X[a]) if b == c else 0)) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            r = 0
            for a in range(n):
                r += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    r += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
            Ric[b, c] = r
    return Ric

def is_mode_direct(n):
    """the control: the first-order Einstein equations solved directly for psi, E, nu, d eps ~ Q e^{i w t}"""
    w = sp.Symbol('omega', positive=True); thc, phc = sp.symbols('theta_c phi_c', real=True)
    Q = zonal_Q(n); S, Qa, Na, D = sp.symbols('S Q_a N_a D'); ph = sp.exp(sp.I*w*t)
    nu, psi, E = Na*Q*ph, S*Q*ph, Qa*Q*ph
    Gchi = 1 - 2*e*psi + 2*e*sp.diff(E, chi, 2)
    Gth = sp.sin(chi)**2*(1 - 2*e*psi) + 2*e*sp.sin(chi)*sp.cos(chi)*sp.diff(E, chi)
    gd = [-(1 + e*nu)**2, R**2*Gchi, R**2*Gth, R**2*Gth*sp.sin(thc)**2]
    Ric = _ricci_diag(gd, [t, chi, thc, phc]); ginv = [1/x for x in gd]
    Rs = sum(ginv[a]*Ric[a, a] for a in range(4))
    eps_, p_ = EPS0 + e*D*Q*ph, p0 + e*cs2*D*Q*ph
    eqs = {'tt': ginv[0]*Ric[0, 0] - Rs/2 + LAM + 8*sp.pi*G*eps_, 'tchi': ginv[0]*Ric[0, 1],
           'chichi': ginv[1]*Ric[1, 1] - Rs/2 + LAM - 8*sp.pi*G*p_, 'thth': ginv[2]*Ric[2, 2] - Rs/2 + LAM - 8*sp.pi*G*p_}
    first = {}
    for k, v in eqs.items():
        cf = tc(v, 2)
        assert sp.simplify(cf[0]) == 0
        first[k] = sp.simplify(cf[1]/ph)
    profs = {'tt': Q, 'tchi': sp.diff(Q, chi), 'trace': Q, 'tracefree': sp.diff(Q, chi, 2) - sp.cos(chi)/sp.sin(chi)*sp.diff(Q, chi)}
    eq = {'tt': first['tt'], 'tchi': first['tchi'], 'trace': first['chichi'] + 2*first['thth'], 'tracefree': first['chichi'] - first['thth']}
    red = {}
    for k in eq:
        vals = [sp.simplify(sp.expand_trig(sp.expand_trig(eq[k].subs(chi, sp.acos(c)))/sp.expand_trig(profs[k].subs(chi, sp.acos(c)))))
                for c in (sp.Rational(1, 7), sp.Rational(2, 7), sp.Rational(3, 7))]
        assert all(sp.simplify(v - vals[0]) == 0 for v in vals[1:]), f'{k} does not separate'
        red[k] = vals[0]
    M = sp.Matrix([[sp.diff(red[k], a) for a in (S, Qa, Na, D)] for k in ('tt', 'tchi', 'trace', 'tracefree')])
    w2 = sp.Symbol('w2', positive=True)
    roots = [r for r in sp.solve(sp.factor(sp.simplify(M.det().subs(w, sp.sqrt(w2)))), w2) if r != 0]
    assert len(roots) == 1
    ns = M.subs(w, sp.sqrt(roots[0])).applyfunc(sp.simplify).nullspace()
    assert len(ns) == 1
    v = ns[0]/ns[0][0]                                      # normalize psi = 1
    return sp.simplify(roots[0]), [sp.simplify(x) for x in v]   # (psi, E, nu, d eps) amplitudes

KAP, NU2H = sp.Symbol('kappa'), sp.Symbol('nu2h')        # C2's charge shift; the homogeneous second-order lapse (gauge)

def grade_IS(n, kind, charge, mode=None):
    """THE RUN ONLY: grade one density-sector configuration at level n with R_V fixed at every instant, through
    the shared reading. Standing: T = cos(w t). Quadrature: by Schur, the averaged second-order quantities of two
    orthogonal harmonics of one eigenspace add, so the residual is that of cos(w t) plus that of sin(w t), the
    charge shift counted once. General: amplitudes 1 and 1/2. The per-level check on the symbolic form. The parts
    are taken with a positive frequency W, then W^2 = omega^2, as the symbolic path takes them: integrating with
    omega itself would leave a case for omega = 0, which T2 excludes."""
    Tf = sp.Function('T')(t)
    m = (mode or is_mode)(n, Tf)
    ra, rb = is_residuals(m['nu1'], m['psi1'], m['E1'], m['x1'], charge=charge, kappa=KAP)
    W = sp.Symbol('W', positive=True)
    at = lambda r, T, k=True: sp.simplify((r if k else r.subs(KAP, 0)).subs(Tf, T).doit())
    weight = {'standing': 0, 'quadrature': 1, 'general': sp.Rational(1, 4)}[kind]
    combo = lambda r: at(r, sp.cos(W*t)) + (weight*at(r, sp.sin(W*t), False) if weight else 0)
    a2, b2 = [sp.simplify(combo(r[2]).subs(NU2H, 0)) for r in (ra, rb)]
    parts = lambda r: [sp.expand(sp.simplify(sp.expand(x.subs(W, sp.sqrt(m['omega2']))))) for x in fourier_parts(r, W)]
    return read(parts(a2), parts(b2), KAP, charge)

# ---- I-S with the eigenvalue symbolic (the page's §1 and §4): every level at once ----
LAMS = sp.Symbol('lambda', positive=True)
IS_NODES = (2, 3, 4, 5, 6, 7, 8)       # seven levels fix exactly a polynomial in lambda of degree at most six
IS_CHECKS = (9, 10, 12)                 # three more check it; n = 12 is the first scalar level of S^3/2I
IS_DEGREE_BOUND = 5                     # the derivation's bound; the ten levels certify up to 9
T0s, T1s, T2s = sp.symbols('T0 T1 T2')  # T(t), T'(t), T''(t)
GENS = (T0s, T1s, T2s, KAP, NU2H)

def omega2_of(lam):
    return (cs2*(lam - 3) - 1)/R**2

def lagrange(pts):
    """the polynomial in lambda through the points (lambda_k, y_k), exactly"""
    tot = 0
    for k, (xk, yk) in enumerate(pts):
        basis = sp.Integer(1)
        for j, (xj, _) in enumerate(pts):
            if j != k:
                basis *= (LAMS - xj)/sp.Integer(xk - xj)
        tot += yk*basis
    return sp.expand(tot)

def interpolate_levels(values, nodes=IS_NODES, checks=IS_CHECKS):
    """values: level n -> an expression. Returns the polynomial in lambda = n(n+2) through the node levels, the
    exact agreement at each check level, and its degree in lambda, which must be within IS_DEGREE_BOUND.
    Why each coefficient is a polynomial in lambda, of degree at most 5:
      every second-order average is a quadratic integral of first-order fields, and for an eigenmode integration
      by parts and the constant curvature reduce it to a polynomial in lambda: at most 3 from its derivatives (at
      most 6 spatial derivatives in all, two to each power of lambda) and at most 2 from its amplitudes (psi and E
      carry none, nu and x each carry lambda - 3);
      the two homogeneous variables solved on the way, the volume's trace c2 and the charge's density x2h, come
      from linear equations with constant coefficients (-3 and 1), and the averages divide only by <J0> = 1, so no
      denominator in lambda enters;
      T and its derivatives stay separate monomials, so the frequency enters only when the time dependence is
      substituted, through omega^2, a polynomial in lambda.
    The seven nodes fix a polynomial of degree at most 6, and agreement at all ten computed levels certifies the
    interpolant exactly for any polynomial of degree up to 9: a difference of degree at most 9 with ten roots is zero."""
    poly = lagrange([(n*(n + 2), values[n]) for n in nodes])
    agree = {n: sp.simplify(poly.subs(LAMS, n*(n + 2)) - values[n]) == 0 for n in checks if n in values}
    deg = sp.Poly(poly, LAMS).degree() if poly != 0 else -1
    return poly, agree, deg

def interpolation_record(coeffs, nodes=IS_NODES, checks=IS_CHECKS, bound=None):
    """the symbolic form from each level's own coefficients: each monomial's polynomial in lambda with its checks and
    degree, and whether the form is established, every check level agreeing and every degree within the bound"""
    bound = IS_DEGREE_BOUND if bound is None else bound
    levels = tuple(nodes) + tuple(checks)
    polys, interp = [], {}
    for side, name in ((0, '13a'), (1, '13b')):
        keys = set().union(*[set(coeffs[n][side]) for n in levels])
        pd = {}
        for mon in keys:
            poly, agree, deg = interpolate_levels({n: coeffs[n][side].get(mon, sp.Integer(0)) for n in levels}, nodes, checks)
            pd[mon] = poly
            interp[f'{name} {mon}'] = {'polynomial': poly, 'checks agree': agree, 'degree': deg}
        polys.append(pd)
    established = all(all(v['checks agree'].values()) and v['degree'] <= bound for v in interp.values())
    return polys, interp, established

def is_coefficients(n, charge='C2', mode=None):
    """THE RUN ONLY: the second-order residuals of (13a) and (13b) for the level-n density mode with its time
    dependence T(t) left general, with the charge left free (C2; C1 is kappa = 0), as coefficients of the monomials
    in T, T', T'', kappa and the homogeneous lapse nu2h"""
    Tf = sp.Function('T')(t)
    m = (mode or is_mode)(n, Tf)
    ra, rb = is_residuals(m['nu1'], m['psi1'], m['E1'], m['x1'], charge=charge, kappa=KAP)
    out = []
    for r in (ra[2], rb[2]):
        r = r.subs(sp.Derivative(Tf, (t, 2)), T2s).subs(sp.Derivative(Tf, t), T1s).subs(Tf, T0s)
        out.append({mon: sp.simplify(c) for mon, c in sp.Poly(sp.expand(r), *GENS).terms()})
    return out

def residual_from(coeffs, T, keep_kappa=True):
    sub = {T0s: T, T1s: sp.diff(T, t), T2s: sp.diff(T, t, 2), NU2H: 0}
    if not keep_kappa:
        sub[KAP] = 0
    return sp.expand(sum(c*sp.Mul(*[g**k for g, k in zip(GENS, mon)]) for mon, c in coeffs.items()).subs(sub))

def symbolic_parts(polys, kind, mean_only=False, lam=LAMS):
    """one configuration's residual parts from the coefficient polynomials, the eigenvalue symbolic (or a level's
    lambda): standing T = cos(W t); quadrature and general by Schur's sum as in grade_IS, the charge shift once; the
    parts [a0, ac, as/W] of (13a) and (13b), with W^2 = omega^2(lambda) once they are taken. They are polynomials in
    lambda, c_s^2, p'' and kappa. The diagnostic takes a0 alone."""
    W = sp.Symbol('W', positive=True)
    weight = {'standing': 0, 'quadrature': 1, 'general': sp.Rational(1, 4)}[kind]
    rs = []
    for coeffs in polys:
        cf = {mon: sp.expand(c.subs(LAMS, lam)) for mon, c in coeffs.items()}
        r = residual_from(cf, sp.cos(W*t)) + (weight*residual_from(cf, sp.sin(W*t), False) if weight else 0)
        rs.append([sp.expand(sp.simplify(sp.expand(x.subs(W, sp.sqrt(omega2_of(lam)))))) for x in fourier_parts(r, W, mean_only=mean_only)])
    return rs[0], rs[1]

def read_symbolic(polys, kind, charge, mean_only=False, lam=LAMS, domain='S3', **read_kw):
    """one configuration's reading at a level (or with lambda symbolic), through the shared reading"""
    pa, pb = symbolic_parts(polys, kind, mean_only, lam)
    return read(pa, pb, KAP, charge, domain, **read_kw)

def computed_levels(level_coeffs, kind, charge, domain, mean_only=False, rule='intersection', **read_kw):
    """the verdict from the computed levels alone, where the every-level reading is withdrawn (the symbolic form not
    established, or the reading over levels withdrawn on this domain): the intersection of the law sets of the
    computed levels the domain admits, then T2's admissibility, as over every level. A withdrawn level withdraws it.
    rule = 'weakest' is the superseded rule, the weakest per-level grade (a mutation arm)."""
    levels = [n for n in sorted(level_coeffs) if admits(domain, n, kind)]
    rec = {'domain': domain, 'computed levels': levels}
    if not levels:
        rec['verdict'] = 'no admitted level computed'
        return rec
    readings = {n: read_symbolic(level_coeffs[n], kind, charge, mean_only=mean_only, lam=sp.Integer(n*(n + 2)), domain=domain, **read_kw)
                for n in levels}
    rec['per level'] = {n: g for n, (g, _) in readings.items()}
    if any(g == 'withdrawn' for g, _ in readings.values()):
        rec['verdict'] = 'withdrawn'
        return rec
    if rule == 'weakest':
        rank = {'NOT ABSORBED': 0, 'CONDITIONAL': 1, 'ABSORBED': 2}
        rec['verdict'] = min((g for g, _ in readings.values()), key=lambda g: rank[g])
        return rec
    laws = 'all'
    for n in levels:
        laws = intersect_laws(laws, readings[n][1]['raw laws'])
    final = admissible_part(laws, domain)
    rec['laws'] = final
    rec['verdict'] = 'ABSORBED' if final == 'all' else ('CONDITIONAL' if final else 'NOT ABSORBED')
    return rec

def multiplicity(domain, n):
    """the number of invariant scalar harmonics at level n: (n+1)^2 on S^3; the same for even n on RP^3 and none for
    odd n; on S^3/2I, m_n (n+1), with m_n the coefficient of s^n in Molien's series (1 + s^30)/((1 - s^12)(1 - s^20))
    (molien-shells.test.py: 13 surviving modes at n = 12)"""
    if domain == 'S3':
        return (n + 1)**2
    if domain == 'RP3':
        return (n + 1)**2 if n % 2 == 0 else 0
    return (n + 1)*sum(1 for a in range(n//12 + 1) for b in range(n//20 + 1) for c in (0, 1) if 12*a + 20*b + 30*c == n)

def admits(domain, n, kind):
    """a configuration exists at level n on the domain: one invariant harmonic for a standing mode, two for a pair"""
    return n >= 2 and multiplicity(domain, n) >= (1 if kind == 'standing' else 2)

IS_DOMAINS = ('S3', 'RP3', 'S3/2I')

def level_of(lam):
    """the level n >= 2 with lambda = n(n+2), or None"""
    lam = sp.nsimplify(lam)
    if not (lam.is_number and lam.is_integer):
        return None
    r = sp.sqrt(1 + lam)
    return int(r - 1) if r.is_integer and r - 1 >= 2 else None

def solve_laws(conds):
    """the response laws (c_s^2, p'') under which every condition vanishes, each checked by substitution: 'all' when
    no condition remains, otherwise a list of solutions, possibly empty. A solution that gives p'' in terms of c_s^2
    is turned round where it can be, so that admissibility is judged on c_s^2."""
    conds = [c for c in (sp.expand(sp.simplify(c)) for c in conds) if c != 0]
    if not conds:
        return 'all'
    out = []
    for s in sp.solve(conds, list(RESPONSE), dict=True):
        if not all(sp.simplify(c.subs(s)) == 0 for c in conds):
            continue
        if cs2 not in s and p2 in s and s[p2].has(cs2):
            inv = sp.solve(sp.Eq(p2, s[p2]), cs2, dict=True)
            if inv:
                out += inv
                continue
        out.append(s)
    return out

def intersect_laws(A, B):
    """the laws in both sets"""
    if A == 'all':
        return B
    if B == 'all':
        return A
    out = []
    for a in A:
        for b in B:
            eqs = [k - v for k, v in a.items()] + [k - v for k, v in b.items()]
            out += sp.solve(eqs, list(RESPONSE), dict=True) if eqs else [{}]
    return out

def admissible_part(laws, domain, floor=None, ceiling=1):
    """the laws within T2's class on the domain, each with the range it leaves: a law fixing c_s^2 is kept when that
    value is admissible; one tying c_s^2 to p'' is kept when some p'' makes it admissible; one tying it to the
    background is kept and marked so"""
    if laws == 'all':
        return 'all'
    lo = cs2_floor(domain) if floor is None else floor
    out = []
    for s in laws:
        a = admissible(s, domain, floor, ceiling)
        if a is True:
            out.append((s, 'admissible'))
        elif a is None:
            v = s[cs2]
            if v.free_symbols <= {p2}:
                rng = sp.solve_univariate_inequality(v > lo, p2, relational=False)
                if ceiling is not None:
                    rng = sp.Intersection(rng, sp.solve_univariate_inequality(v <= ceiling, p2, relational=False))
                if rng != sp.S.EmptySet:
                    out.append((s, f"admissible for p'' in {rng}"))
            else:
                out.append((s, 'admissibility depends on the background'))
    return out

def common_laws(polys, kind, charge, domain, mean_only=False, rule='intersection', floor=None, ceiling=1, use_exceptions=True, **read_kw):
    """THE RUN: the response laws that hold one configuration at every admitted level of a domain, C_D, the
    intersection over the admitted levels n of the admissible laws C_n that satisfy level n (the page's §4).
    Every domain admits infinitely many levels, and once the charge shift is solved the conditions are polynomials in
    lambda; so a law satisfies every generic level exactly when each coefficient of each condition's polynomial in
    lambda vanishes there, a system in c_s^2 and p'' alone. Under C2 the shift kappa is solved from (13b)'s constant
    part: where its coefficient is a constant there is no exceptional level; where it depends on lambda alone, its
    admitted roots are exceptional levels, each read on its own and intersected in; where it depends on the response
    law, the every-level reading is withdrawn. Admissibility is T2's on the domain. Verdict: ABSORBED when every law
    holds every level; CONDITIONAL when an admissible law does, the set recorded; NOT ABSORBED when none does.
    rule = 'per-level' is the superseded rule (a condition that changes with the level gives NOT ABSORBED), floor a
    single global floor, ceiling=None no upper end, use_exceptions=False ignores exceptional levels: mutation arms;
    read_kw passes the reading's own arms to the exceptional levels."""
    pa, pb = symbolic_parts(polys, kind, mean_only)
    rec = {'domain': domain, 'parts, the eigenvalue symbolic': {'13a': pa, '13b': pb}}
    exc = []
    if charge == 'C1':
        conds = [sp.expand(x.subs(KAP, 0)) for x in pa + pb]
    else:
        k, rest = sp.expand(sp.diff(pb[0], KAP)), sp.expand(pb[0].subs(KAP, 0))
        rec['kappa coefficient'] = k
        if k.free_symbols & set(RESPONSE):
            rec.update({'verdict': 'withdrawn', 'every level': "withdrawn: the charge shift's coefficient depends on the response law"})
            return rec
        if k == 0:                                      # (13b) does not carry the shift: project it out, never set it
            if read_kw.get('shift_zero'):
                conds = [sp.expand(x.subs(KAP, 0)) for x in pa + pb]
            else:
                conds = project_shift(pa + pb, KAP, constant=True)
                if conds is None:
                    rec.update({'verdict': 'withdrawn', 'every level': "withdrawn: (13b) does not carry the charge shift, and no "
                                "residual fixes it with a constant coefficient"})
                    return rec
        else:
            conds = [sp.expand(sp.fraction(sp.together(x.subs(KAP, -rest/k)))[0]) for x in pa + pb[1:]]
            if k.has(LAMS) and use_exceptions:
                roots = sp.solve(sp.fraction(sp.together(k))[0], LAMS)
                exc = sorted({n for n in (level_of(r) for r in roots if r.is_number and r.is_real) if n is not None and admits(domain, n, kind)})
    if rule == 'per-level':
        sols = solve_laws(conds)
        free = sols != 'all' and sols and all(not any(sp.sympify(x).has(LAMS) for x in s.values()) for s in sols)
        rec['verdict'] = 'ABSORBED' if sols == 'all' else ('CONDITIONAL' if free and admissible_part(sols, domain, floor, ceiling) else 'NOT ABSORBED')
        return rec
    gen = []
    for c in conds:
        if c != 0:
            gen += [x for x in sp.Poly(c, LAMS).all_coeffs() if sp.simplify(x) != 0]
    laws = solve_laws(gen)
    rec['generic laws'] = laws
    rec['exceptional levels'] = exc
    at = {}
    for n in exc:
        g_n, d_n = read_symbolic(polys, kind, charge, mean_only=mean_only, lam=sp.Integer(n*(n + 2)), domain=domain, **read_kw)
        if g_n == 'withdrawn':
            rec.update({'verdict': 'withdrawn', 'every level': f'withdrawn: the reading at the exceptional level n = {n} is withdrawn',
                        'at exceptional levels': {n: {'reading': g_n, 'why': d_n.get('withdrawn')}}})
            return rec
        C_n = d_n['raw laws']
        at[n] = {'reading': g_n, 'laws': C_n}
        laws = intersect_laws(laws, C_n)
    rec['at exceptional levels'] = at
    final = admissible_part(laws, domain, floor, ceiling)
    rec['laws'] = final
    rec['verdict'] = 'ABSORBED' if final == 'all' else ('CONDITIONAL' if final else 'NOT ABSORBED')
    return rec

# ---- I-V, the vorticity sector: the reduction, derived (the page's §3 and §5) ----
th3, ph3 = sp.symbols('theta_v phi_v', real=True)
X3 = [chi, th3, ph3]
GAM3 = sp.diag(1, sp.sin(chi)**2, sp.sin(chi)**2*sp.sin(th3)**2)          # the unit S^3, hyperspherical

def lie_metric3(F):
    """(L_F gamma)_ij for a vector field with components F^k"""
    return sp.Matrix(3, 3, lambda i, j: sum(F[k]*sp.diff(GAM3[i, j], X3[k]) + GAM3[k, j]*sp.diff(F[k], X3[i])
                                            + GAM3[i, k]*sp.diff(F[k], X3[j]) for k in range(3)))

def divergence3(F):
    sq = sp.sqrt(GAM3.det())
    return sp.simplify(sum(sp.diff(sq*F[k], X3[k]) for k in range(3))/sq)

def S3avg3(f):
    """the average over the unit S^3 of a function of chi and theta (axisymmetric about phi)"""
    return sp.simplify(sp.integrate(sp.integrate(sp.expand(f*sp.sin(chi)**2*sp.sin(th3)), (th3, 0, sp.pi)), (chi, 0, sp.pi))/sp.pi)

def averaged_curvature_vector(F, h2=None, fix_volume=True):
    """<R>_J by orders for gamma + e L_F gamma + e^2 (h2 + c gamma): a first-order relabeling F, any smooth
    second-order h2, and c holding the volume fixed (or zero: a mutation arm). Exact and deterministic: the curvature
    in series arithmetic, the volume element from sqrt det(1 + e A + e^2 B) = 1 + e tr A/2 + e^2 (tr B/2 - tr A^2/4
    + (tr A)^2/8), and the exact average over S^3."""
    c = sp.Symbol('c')
    h1 = lie_metric3(F)
    h2full = c*GAM3 + (h2 if h2 is not None else sp.zeros(3, 3))
    Rs = ricci_scalar_coeffs(X3, GAM3, h1, h2full)
    Gi = GAM3.inv()
    A, B = (Gi*h1).applyfunc(sp.expand), (Gi*h2full).applyfunc(sp.expand)
    js = [sp.Integer(1), sp.expand(A.trace()/2), sp.expand(B.trace()/2 + A.trace()**2/8 - (A*A).trace()/4)]
    cv = sp.solve(avg_hyper_fast(js[2]), c)[0] if fix_volume else 0
    Rs, js = [sp.expand(x.subs(c, cv)) for x in Rs], [sp.expand(x.subs(c, cv)) for x in js]
    num = [avg_hyper_fast(sum(Rs[i]*js[k - i] for i in range(k + 1))) for k in range(3)]
    den = [avg_hyper_fast(js[k]) for k in range(3)]
    q0 = num[0]/den[0]; q1 = (num[1] - q0*den[1])/den[0]; q2 = (num[2] - q0*den[2] - q1*den[1])/den[0]
    return [sp.simplify(q0), sp.simplify(q1), sp.simplify(q2)]

def first_variation_avg(h):
    """<R> to first order at the round metric in the direction h, and <tr h>: the page's -(2/R^2) <tr h>"""
    return avg_hyper_fast(ricci_scalar_coeffs(X3, GAM3, h)[1]), avg_hyper_fast(sp.expand((GAM3.inv()*h).trace()))

def ambient_tensor(A):
    """the smooth symmetric tensor A_ab dX^a dX^b on the unit S^3 from a constant 4x4 matrix, X its embedding"""
    Xe = [sp.cos(chi), sp.sin(chi)*sp.cos(th3), sp.sin(chi)*sp.sin(th3)*sp.cos(ph3), sp.sin(chi)*sp.sin(th3)*sp.sin(ph3)]
    J = sp.Matrix(4, 3, lambda a, i: sp.diff(Xe[a], X3[i]))
    return (J.T*sp.Matrix(A)*J).applyfunc(sp.simplify)

def christoffel3():
    gi = GAM3.inv()
    return [[[sp.simplify(sp.Rational(1, 2)*sum(gi[k, l]*(sp.diff(GAM3[j, l], X3[i]) + sp.diff(GAM3[i, l], X3[j])
             - sp.diff(GAM3[i, j], X3[l])) for l in range(3))) for j in range(3)] for i in range(3)] for k in range(3)]

def iv_first_order(F, B):
    """the linearized vector sector on explicit fields of the form f d_phi: the relabeling F of the slice and the
    shift B. With the slice round and N = 1 at first order, K_ij = (1/2)(D_i B_j + D_j B_i), and the momentum
    constraint D_j K^j_i = 8 pi G (rho0 + p0) v_i gives the tilt. Returns div F, tr h1, the first-order curvature
    change, the mean curvature tr K1, <K_ij K^ij>, and <|D.K|^2>, proportional to <v^2>."""
    h1 = lie_metric3(F)
    K1 = lie_metric3(B)/2
    gi = GAM3.inv()
    Kmix = (gi*K1).applyfunc(sp.simplify)                    # K^j_i, row j, column i
    Gm = christoffel3(); sq = sp.sqrt(GAM3.det())
    divK = [sp.simplify(sum(sp.diff(sq*Kmix[j, i], X3[j]) for j in range(3))/sq
                        - sum(Gm[k][i][j]*Kmix[j, k] for j in range(3) for k in range(3))) for i in range(3)]
    Kup = gi*K1*gi
    R1 = ricci_scalar_coeffs(X3, GAM3, h1)[1]
    return {'divF': divergence3(F), 'trh1': sp.simplify((gi*h1).trace()), 'R1': sp.Integer(0) if trig_zero(R1) else R1,
            'trK1': sp.simplify((gi*K1).trace()),
            'K2': avg_hyper_fast(sum(K1[i, j]*Kup[i, j] for i in range(3) for j in range(3))),
            'divK2': avg_hyper_fast(sum(gi[i, j]*divK[i]*divK[j] for i in range(3) for j in range(3)))}

def iv_constraint(tilt_sign=1, keep_gamma=True, raych_tilt=True, lam_shift=0):
    """the averaged equations at second order with V_h fixed, for the I-V configuration, two ways.
    Buchert, Mourier and Roy's (3.33) and (3.32), transcribed: 3 H^2 = 8 pi G <N^2 eps> + <N^2> Lambda - (1/2)<N^2 R>
    - (1/2) Q - (1/2) T and 3 a''/a = -4 pi G <N^2 (eps + 3p)> + <N^2> Lambda + Q + P + (1/2) T, with (3.34)
    Q = -<K_ij K^ij> (the mean curvature vanishes at first order), P fourth order, and (3.36)
    T = -16 pi G <N^2 (gamma^2 - 1)(eps + p)> = -16 pi G (rho0 + p0) <v^2>.
    The plain ADM forms, derived apart: the averaged Hamiltonian constraint <R + K^2 - K_ij K^ij - 16 pi G E - 2 Lambda>
    and, at fixed volume, the averaged d K/dt, -<K_ij K^ij> - 4 pi G <E + S> + Lambda, with E = rho + (rho + p) v^2
    and S = 3p + (rho + p) v^2 the normal observers' energy density and stress trace.
    The volume is fixed, so H = a'' = 0, and <R> is unchanged (iv checks). The second-order lapse, the only thing
    the two slicings of the page's §2 differ by here, multiplies the background's constraint and Raychaudhuri
    combinations; the second of these is also the coefficient of the slices' second-order displacement in the mean
    curvature, beside a Laplacian whose average vanishes. Under C1 (kappa = 0), then with the charge left free.
    Mutation arms: tilt_sign = -1 flips T in the transcription of BMR; keep_gamma = False drops the tilt factor
    from the charge; raych_tilt = False drops T from (3.32); lam_shift moves Lambda off its static value."""
    V2, K2, kap, N2 = sp.symbols('V2 K2 kappa N2avg', real=True)            # <v^2>, <K_ij K^ij>, the charge's shift, <N^2> - 1
    n0 = sp.Symbol('n_0', positive=True)
    lam = LAM + lam_shift
    dn = n0*(kap - (V2/2 if keep_gamma else 0))                             # <n Gamma> = n0 (1 + kappa), Gamma = 1 + v^2/2
    drho = W0*dn/n0                                                         # T7(b): dn/n = d rho/(rho + p); no first-order density
    Q, T = -K2, -tilt_sign*16*sp.pi*G*W0*V2
    bg33, bg32 = 8*sp.pi*G*EPS0 + lam - 3/R**2, -4*sp.pi*G*(EPS0 + 3*p0) + lam
    r33 = 8*sp.pi*G*((1 + N2)*EPS0 + drho) + (1 + N2)*lam - (1 + N2)*3/R**2 - Q/2 - T/2 - bg33
    r32 = -4*sp.pi*G*((1 + N2)*(EPS0 + 3*p0) + (1 + 3*cs2)*drho) + (1 + N2)*lam + Q + (T/2 if raych_tilt else 0) - bg32
    adm_h = -K2 - 16*sp.pi*G*(drho + W0*V2)
    adm_r = -K2 - 4*sp.pi*G*((1 + 3*cs2)*drho + 2*W0*V2)
    lapse_free = all(sp.simplify(sp.diff(sp.expand(r), N2)) == 0 for r in (r33, r32))
    same = sp.simplify(r33.subs(N2, 0) + adm_h/2) == 0 and sp.simplify(r32.subs(N2, 0) - adm_r) == 0
    c1 = sp.simplify(r33.subs({kap: 0, N2: 0}))
    form = sp.simplify(c1 - (4*sp.pi*G*W0*V2 + K2/2)) == 0
    a, b = sp.symbols('a b', positive=True)
    ks = sp.solve(r33.subs(N2, 0), kap)
    cs = sp.solve(sp.simplify(r32.subs(N2, 0).subs(kap, ks[0])), cs2) if len(ks) == 1 else []
    val = sp.simplify(cs[0].subs({V2: a/(4*sp.pi*G*W0), K2: 4*b})) if len(cs) == 1 else None
    comp = val is not None and sp.simplify(val - (a + 3*b)/(3*(a + b))) == 0
    rng = comp and sp.simplify(val - sp.Rational(1, 3) - 2*b/(3*(a + b))) == 0 and sp.simplify(1 - val - 2*a/(3*(a + b))) == 0
    return {'lapse_free': lapse_free, 'ADM_equals_BMR': same, 'C1_form': form, 'C1_value': c1,
            'comparison': comp, 'range': rng, 'cs2': val}

# ---- the remaining integrability conditions (the page's §4 and §5): reported beside the grades, never graded ----
def s_add(*xs):
    return [sp.expand(sum(x[k] for x in xs)) for k in range(3)]

def s_mul(a, b):
    return [sp.expand(a[0]*b[0]), sp.expand(a[0]*b[1] + a[1]*b[0]), sp.expand(a[0]*b[2] + a[1]*b[1] + a[2]*b[0])]

def s_scale(c, a):
    return [sp.expand(c*x) for x in a]

def s_diff(a, v):
    return [sp.diff(x, v) for x in a]

def momentum_constraint(X, g0, g1, nu, b, v, W8=2, connection_sign=-1, g2=None):
    """the momentum constraint through second order on a slice of unit radius with coordinates X, its two sides
    apart, each as [order 0, 1, 2] per component i: grav_i = D_j (K^j_i - delta^j_i K), with
    K_ij = -(1/2N)(d_t g_ij - D_i beta_j - D_j beta_i), and mat_i = 8 pi G J_i = 8 pi G (rho0 + p0) g_ij v^j for a fluid
    with first-order tilt e v^i and no first-order density or pressure, so that its second-order part is the
    first-order metric times the first-order tilt (Gamma^2 - 1 is second order, so its term is third). The slice
    metric is g0 + e g1, the lapse 1 + e nu, the shift e b^i; 8 pi G (rho0 + p0) = 2/R^2 = W8. The second-order
    fields are left out: their part integrates to zero against a Killing field (it is the linearized constraint,
    whose adjoint the Killing fields annihilate), except the fluid's own second-order tilt, named apart.
    connection_sign = +1 flips the sign of the term -Gamma^k_ji K^j_k (a mutation arm). g2, a second-order metric,
    serves the check that a homogeneous trace leaves the constraint unchanged."""
    n = 3
    g = [[[g0[i, j], g1[i, j], g2[i, j] if g2 is not None else 0] for j in range(n)] for i in range(n)]
    g0i = g0.inv().applyfunc(sp.simplify)
    A = (g0i*g1*g0i).applyfunc(sp.expand)
    Bm = (A*g1*g0i).applyfunc(sp.expand)
    if g2 is not None:
        Bm = (Bm - g0i*g2*g0i).applyfunc(sp.expand)
    ginv = [[[g0i[i, j], -A[i, j], Bm[i, j]] for j in range(n)] for i in range(n)]
    dg = [[[s_diff(g[i][j], X[l]) for l in range(n)] for j in range(n)] for i in range(n)]      # dg[i][j][l] = d_l g_ij
    Gam = [[[s_scale(sp.Rational(1, 2), s_add(*[s_mul(ginv[k][l], s_add(dg[j][l][i], dg[i][l][j], s_scale(-1, dg[i][j][l])))
                                                for l in range(n)])) for j in range(n)] for i in range(n)] for k in range(n)]
    b_lo = [s_add(*[s_mul(g[j][k], [0, b[k], 0]) for k in range(n)]) for j in range(n)]
    Db = [[s_add(s_diff(b_lo[j], X[i]), s_scale(-1, s_add(*[s_mul(Gam[k][i][j], b_lo[k]) for k in range(n)])))
           for j in range(n)] for i in range(n)]
    half_Ninv = [sp.Rational(1, 2), -nu/2, nu**2/2]
    K = [[s_scale(-1, s_mul(half_Ninv, s_add(s_diff(g[i][j], t), s_scale(-1, Db[i][j]), s_scale(-1, Db[j][i]))))
          for j in range(n)] for i in range(n)]
    Km = [[s_add(*[s_mul(ginv[j][k], K[k][i]) for k in range(n)]) for i in range(n)] for j in range(n)]   # Km[j][i] = K^j_i
    trK = s_add(*[Km[j][j] for j in range(n)])
    grav = []
    for i in range(n):
        term = s_add(*[s_diff(Km[j][i], X[j]) for j in range(n)])
        term = s_add(term, *[s_mul(Gam[j][j][k], Km[k][i]) for j in range(n) for k in range(n)])
        term = s_add(term, s_scale(connection_sign, s_add(*[s_mul(Gam[k][j][i], Km[j][k]) for j in range(n) for k in range(n)])))
        grav.append(s_add(term, s_scale(-1, s_diff(trK, X[i]))))
    mat = [s_scale(W8, s_add(*[s_mul(g[i][j], [0, v[j], 0]) for j in range(n)])) for i in range(n)]
    return grav, mat

def avg_hyper(f):
    """the average over the unit S^3 in hyperspherical coordinates (chi, theta_v, phi_v), any phi dependence"""
    return S3avg3(sp.integrate(sp.expand(f), (ph3, 0, 2*sp.pi))/(2*sp.pi))

_cX, _sX, _cT, _sT, _cP, _sP = sp.symbols('cX sX cT sT cP sP')

def _beta_int(a, b, shift=0):
    """int_0^pi cos^a x sin^b x dx for a in {0, 1} and an integer b >= 0 (shift moves b: a mutation arm)"""
    if a == 1:
        return sp.Integer(0)
    b = b + shift
    return sp.sqrt(sp.pi)*sp.gamma(sp.Rational(b + 1, 2))/sp.gamma(sp.Rational(b, 2) + 1)

def _phi_int(a, b):
    """int_0^{2 pi} cos^a x sin^b x dx for a in {0, 1} and an integer b >= 0"""
    if a == 1 or b % 2 == 1:
        return sp.Integer(0)
    return 2*sp.sqrt(sp.pi)*sp.gamma(sp.Rational(b + 1, 2))/sp.gamma(sp.Rational(b, 2) + 1)

def avg_hyper_fast(f, shift=0):
    """the same average as avg_hyper, exactly and faster: with the measure sin^2 chi sin theta multiplied in and
    cos^2 = 1 - sin^2 used in each angle, a trigonometric polynomial integrates monomial by monomial through Beta
    functions. Where a negative power of a sine survives the reduction, it falls back to avg_hyper."""
    g = sp.expand(f*sp.sin(chi)**2*sp.sin(th3))
    g = g.subs({sp.cos(chi): _cX, sp.sin(chi): _sX, sp.cos(th3): _cT, sp.sin(th3): _sT, sp.cos(ph3): _cP, sp.sin(ph3): _sP})
    if g.has(chi) or g.has(th3) or g.has(ph3):
        return avg_hyper(f)
    num, den = sp.fraction(sp.together(g))
    num = sp.expand(num)
    for c_, s_ in ((_cX, _sX), (_cT, _sT), (_cP, _sP)):          # cos^2 -> 1 - sin^2, so each cosine appears at most once
        P = sp.Poly(num, c_)
        num = sp.expand(sum(coef*(c_**(k % 2))*(1 - s_**2)**(k//2) for (k,), coef in P.terms()))
    q = sp.expand(num/den)
    tot = 0
    for term in sp.Add.make_args(q):
        coef, ex = sp.Integer(1), {}
        for fac in sp.Mul.make_args(term):
            base, e_ = fac.as_base_exp()
            if base in (_cX, _sX, _cT, _sT, _cP, _sP):
                ex[base] = ex.get(base, 0) + e_
            else:
                coef *= fac
        if any(not sp.Integer(v).is_integer or v < 0 for v in ex.values()):
            return avg_hyper(f)
        tot += coef*_beta_int(ex.get(_cX, 0), ex.get(_sX, 0), shift)*_beta_int(ex.get(_cT, 0), ex.get(_sT, 0))*_phi_int(ex.get(_cP, 0), ex.get(_sP, 0))
    return sp.simplify(tot/(2*sp.pi**2))

def trig_zero(expr):
    """an exact zero test for a trigonometric expression in the hyperspherical angles: with cos^2 = 1 - sin^2 used in
    each angle, the numerator reduces to a canonical form, which vanishes exactly when the expression does"""
    g = sp.expand(expr).subs({sp.cos(chi): _cX, sp.sin(chi): _sX, sp.cos(th3): _cT, sp.sin(th3): _sT, sp.cos(ph3): _cP, sp.sin(ph3): _sP})
    num = sp.expand(sp.fraction(sp.together(g))[0])
    for c_, s_ in ((_cX, _sX), (_cT, _sT), (_cP, _sP)):
        P = sp.Poly(num, c_)
        num = sp.expand(sum(coef*(c_**(k % 2))*(1 - s_**2)**(k//2) for (k,), coef in P.terms()))
    return num == 0

def ricci_scalar_coeffs(X, g0, g1, g2=None):
    """the scalar curvature of g0 + e g1 + e^2 g2 as [order 0, 1, 2], in the series arithmetic the momentum constraint
    uses: deterministic in cost, with no series expansion and no simplification"""
    n = 3
    g = [[[g0[i, j], g1[i, j], g2[i, j] if g2 is not None else 0] for j in range(n)] for i in range(n)]
    g0i = g0.inv().applyfunc(sp.simplify)
    A = (g0i*g1*g0i).applyfunc(sp.expand)
    Bm = (A*g1*g0i).applyfunc(sp.expand)
    if g2 is not None:
        Bm = (Bm - g0i*g2*g0i).applyfunc(sp.expand)
    ginv = [[[g0i[i, j], -A[i, j], Bm[i, j]] for j in range(n)] for i in range(n)]
    dg = [[[s_diff(g[i][j], X[l]) for l in range(n)] for j in range(n)] for i in range(n)]
    Gam = [[[s_scale(sp.Rational(1, 2), s_add(*[s_mul(ginv[k][l], s_add(dg[j][l][i], dg[i][l][j], s_scale(-1, dg[i][j][l])))
                                                for l in range(n)])) for j in range(n)] for i in range(n)] for k in range(n)]
    Ric = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            term = s_add(*[s_diff(Gam[k][i][j], X[k]) for k in range(n)])
            term = s_add(term, s_scale(-1, s_add(*[s_diff(Gam[k][i][k], X[j]) for k in range(n)])))
            term = s_add(term, *[s_mul(Gam[k][k][l], Gam[l][i][j]) for k in range(n) for l in range(n)])
            Ric[i][j] = s_add(term, s_scale(-1, s_add(*[s_mul(Gam[k][j][l], Gam[l][i][k]) for k in range(n) for l in range(n)])))
    return s_add(*[s_mul(ginv[i][j], Ric[i][j]) for i in range(n) for j in range(n)])

def killing_hyper():
    """the six rotation generators of the unit S^3 in hyperspherical coordinates, X_a d_b - X_b d_a, and the two
    chiral triples q -> q u and q -> u q (u = i, j, k, with q = X1 + X2 i + X3 j + X4 k): the first commutes with
    left multiplication, so it alone survives on S^3/2I when 2I acts on the left"""
    Xe = sp.Matrix([sp.cos(chi), sp.sin(chi)*sp.cos(th3), sp.sin(chi)*sp.sin(th3)*sp.cos(ph3), sp.sin(chi)*sp.sin(th3)*sp.sin(ph3)])
    J = Xe.jacobian(sp.Matrix(X3))
    gi = GAM3.inv()
    def tangent(V):
        return [sp.simplify(x) for x in gi*J.T*V]
    gens = {}
    for a in range(4):
        for c in range(a + 1, 4):
            V = sp.zeros(4, 1); V[c] = Xe[a]; V[a] = -Xe[c]
            gens[f'X{a+1}d{c+1}-X{c+1}d{a+1}'] = tangent(V)
    q = sp.Quaternion(*Xe)
    for name, u in (('i', sp.Quaternion(0, 1, 0, 0)), ('j', sp.Quaternion(0, 0, 1, 0)), ('k', sp.Quaternion(0, 0, 0, 1))):
        for side, prod in (('qu', q*u), ('uq', u*q)):
            gens[f'{side}:{name}'] = tangent(sp.Matrix([prod.a, prod.b, prod.c, prod.d]))
    return gens

def charges(grav, mat, gens, average):
    """each generator's complete quadratic charge <xi^i (grav_i - mat_i)>, at second order, with its two parts"""
    out = {}
    for name, xi in gens.items():
        G2 = average(sum(xi[i]*grav[i][2] for i in range(3)))
        M2 = average(sum(xi[i]*mat[i][2] for i in range(3)))
        out[name] = {'gravitational': sp.simplify(G2), 'matter': sp.simplify(-M2), 'total': sp.simplify(G2 - M2)}
    return out

def iv_integrability(F, gauge):
    """I-V's Killing charges at second order on one transverse field F of the form f d_phi (shift e F in the
    relabeled gauge): gauge 'shift' has the slice round at first order and the shift carrying the mode; gauge
    'static-shift-free' has no shift and the first-order slice metric -t L_F gamma, the same first-order solution
    relabeled in time. The tilt is the first-order momentum constraint's: 8 pi G (rho0 + p0) v_i = D_j K^j_i."""
    zero = sp.zeros(3, 3)
    grav1, _ = momentum_constraint(X3, GAM3, zero, 0, F, [0, 0, 0])
    v_lo = [grav1[i][1]/2 for i in range(3)]
    v = [sp.simplify(sum(GAM3.inv()[i, j]*v_lo[j] for j in range(3))) for i in range(3)]
    if gauge == 'shift':
        grav, mat = momentum_constraint(X3, GAM3, zero, 0, F, v)
    else:
        grav, mat = momentum_constraint(X3, GAM3, -t*lie_metric3(F), 0, [0, 0, 0], v)
    first = [sp.simplify(grav[i][1] - mat[i][1]) for i in range(3)]
    return first, charges(grav, mat, killing_hyper(), avg_hyper_fast)

EUL = sp.symbols('psi_e theta_e phi_e', real=True)

def sigma_matrix():
    """the left-invariant forms of SU(2) in Euler angles, rows sigma^a, columns (d psi, d theta, d phi):
    sigma1 = sin psi d theta - cos psi sin theta d phi, sigma2 = cos psi d theta + sin psi sin theta d phi,
    sigma3 = d psi + cos theta d phi; (1/4) sum sigma^a sigma^a is the unit S^3"""
    ps, th, _ = EUL
    return sp.Matrix([[0, sp.sin(ps), -sp.cos(ps)*sp.sin(th)], [0, sp.cos(ps), sp.sin(ps)*sp.sin(th)], [1, 0, sp.cos(th)]])

def hanio_integrability(beta1):
    """H-ANISO's Killing charges at second order on the unit S^3: the slice metric (1/4) sigma^T (1 + 2 e beta1(t)) sigma,
    unit lapse and no shift, with the fluid at rest at first order (no first-order tilt, density or pressure, so the
    matter part has no quadratic term). Against the three left-invariant generators, of unit length, which survive
    on S^3/2I. The configuration is left-invariant, so the charge density is constant; it is evaluated at two
    points, which must agree. A left-invariant configuration's charges against the right-invariant generators
    average to zero over the group."""
    S = sigma_matrix()
    g0 = (S.T*S/4).applyfunc(sp.simplify)
    g1 = (S.T*(2*beta1)*S/4).applyfunc(sp.expand)
    grav, mat = momentum_constraint(list(EUL), g0, g1, 0, [0, 0, 0], [0, 0, 0])
    first = [sp.simplify(grav[i][1] - mat[i][1]) for i in range(3)]
    E = S.inv().applyfunc(sp.simplify)
    pts = [{EUL[0]: 0, EUL[1]: sp.pi/2, EUL[2]: 0}, {EUL[0]: sp.pi/3, EUL[1]: sp.pi/3, EUL[2]: 0}]
    out = {}
    for a in range(3):
        xi = [2*E[i, a] for i in range(3)]
        Gd = [sp.simplify(sp.expand_trig(sum(xi[i]*grav[i][2] for i in range(3)).subs(pt))) for pt in pts]
        Md = [sp.simplify(sp.expand_trig(sum(xi[i]*mat[i][2] for i in range(3)).subs(pt))) for pt in pts]
        out[f'e{a+1}'] = {'gravitational': Gd[0], 'matter': -Md[0], 'total': sp.simplify(Gd[0] - Md[0]),
                          'constant': sp.simplify(Gd[0] - Gd[1]) == 0 and sp.simplify(Md[0] - Md[1]) == 0}
    return first, out

def hanio_trace_check(nonconstant=False):
    """UB's check that the spatial conditions do not see the radius: a homogeneous change of the radius at second
    order, the slice metric's homogeneous trace f(t) g0, enters K as a multiple of the identity, whose contribution
    D_b K^b_a - D_a K = -2 D_a kappa vanishes. On the H-ANISO rotating member, the second-order constraint is then
    unchanged at every point. nonconstant=True puts a trace f(t) cos(theta) g0 that is not homogeneous (a mutation
    arm), which changes it pointwise, though not its integral against a Killing field."""
    S = sigma_matrix()
    g0 = (S.T*S/4).applyfunc(sp.simplify)
    g1 = (S.T*(2*hanio_beta_matrix('rotating', sp.sqrt(8)))*S/4).applyfunc(sp.expand)
    f = sp.Function('f')(t)*(sp.cos(EUL[1]) if nonconstant else 1)
    base, _ = momentum_constraint(list(EUL), g0, g1, 0, [0, 0, 0], [0, 0, 0])
    trace, _ = momentum_constraint(list(EUL), g0, g1, 0, [0, 0, 0], [0, 0, 0], g2=(f*g0).applyfunc(sp.expand))
    return all(sp.simplify(trace[i][2] - base[i][2]) == 0 for i in range(3))

def hanio_beta_matrix(kind, w):
    """the page's three H-ANISO configurations as traceless diagonal matrices, and a rotating non-diagonal member
    of the general superposition: cos(w t) A + sin(w t) B with A = diag(1, -1, 0)/sqrt 2, B = (E_12 + E_21)/sqrt 2"""
    if kind == 'rotating':
        A = sp.diag(1, -1, 0)/sp.sqrt(2)
        B = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])/sp.sqrt(2)
        return sp.cos(w*t)*A + sp.sin(w*t)*B
    return sp.diag(*[x/e for x in hanio_config(kind, w)])

def hanio_frame_charge(beta1):
    """the independent path for H-ANISO: Bianchi class A in its left-invariant frame, where for constant frame
    components D_b K^b_a = -K^{bc} g_cd C^d_ba with C^d_ba = epsilon_dba; g = (1/4)(1 + 2 e beta1), K = -(1/2) g-dot.
    Returns the frame components at second order, C_a = C(e_a); a unit generator is 2 e_a."""
    g = (sp.eye(3) + 2*e*beta1)/4
    gi = 4*(sp.eye(3) - 2*e*beta1 + 4*e**2*beta1*beta1)
    K = -sp.diff(g, t)/2
    M = (gi*K).applyfunc(sp.expand)                       # (g^-1 K)^b_d
    C = [-sum(M[b, d]*sp.LeviCivita(d, b, a) for b in range(3) for d in range(3)) for a in range(3)]
    return [sp.simplify(sp.expand(c).coeff(e, 2)) for c in C]

def hess3(f):
    """the background Hessian D_i D_j f on the unit S^3, hyperspherical"""
    Gm = christoffel3()
    return sp.Matrix(3, 3, lambda i, j: sp.diff(f, X3[i], X3[j]) - sum(Gm[k][i][j]*sp.diff(f, X3[k]) for k in range(3)))

def is_fields(kind, n=2, sign=-1):
    """the I-S first-order mode in the comoving-orthogonal gauge on the unit S^3: psi, E = sign psi (the mode has
    sign -1; +1 is a mutation arm), nu = c_s^2 (lambda - 3) psi. 'zonal': psi = Q_n cos(w t); 'rotating': the
    quadrature pair Y1 cos(w t) + Y2 sin(w t), Y1, Y2 = sqrt 24 X1 X3, sqrt 24 X1 X4 at n = 2, unit mean square"""
    lam = n*(n + 2)
    w = sp.sqrt(cs2*(lam - 3) - 1)
    if kind == 'zonal':
        psi = zonal_Q(n).subs(chi, chi)*sp.cos(w*t)
    else:
        assert n == 2
        psi = sp.sqrt(24)*sp.cos(chi)*sp.sin(chi)*sp.sin(th3)*(sp.cos(ph3)*sp.cos(w*t) + sp.sin(ph3)*sp.sin(w*t))
    E = sign*psi
    g1 = -2*psi*GAM3 + 2*hess3(E)
    return g1.applyfunc(sp.expand), cs2*(lam - 3)*psi

def is_first_order_constraint(kind, sign=-1):
    """qualification may check the first-order momentum constraint of the I-S mode (a property of the stability
    page's first-order solution): in the comoving-orthogonal gauge J = 0, so D_j(K^j_i - delta^j_i K) must vanish"""
    g1, nu = is_fields(kind, sign=sign)
    grav, _ = momentum_constraint(X3, GAM3, g1, nu, [0, 0, 0], [0, 0, 0])
    return [sp.simplify(grav[i][1]) for i in range(3)]

def is_integrability(kind, sign=-1):
    """THE RUN ONLY: the I-S Killing charges at second order, in the comoving-orthogonal gauge, where the fluid
    moves with the normal, so J = 0 at every order and the whole charge sits in the gravitational side; on the
    unit S^3, against the six rotation generators and the two chiral triples"""
    g1, nu = is_fields(kind, sign=sign)
    grav, mat = momentum_constraint(X3, GAM3, g1, nu, [0, 0, 0], [0, 0, 0])
    return charges(grav, mat, killing_hyper(), avg_hyper_fast)

# ---- the run gate (the page's §5): the frozen registration and this file's identity ----
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def git(*args):
    return subprocess.run(['git', '-C', HERE, *args], capture_output=True)

def run_gate(commit, page_sha, main_ref='origin/main'):
    """refuse unless: commit is on main (origin/main; another ref only for the gate's probe, in a throwaway clone);
    the page at commit hashes to page_sha; the page pins this file's SHA-256; and this file on disk is
    byte-identical to the file at commit. The record keeps the values computed here, not the arguments."""
    with open(os.path.abspath(__file__), 'rb') as f:
        me = sha256_bytes(f.read())
    if main_ref.startswith('origin/'):
        git('fetch', '-q', 'origin')
    on_main = git('merge-base', '--is-ancestor', commit, main_ref).returncode == 0
    page = git('show', f'{commit}:{PAGE}')
    page_ok = page.returncode == 0 and sha256_bytes(page.stdout) == page_sha
    pins_me = page.returncode == 0 and me.encode() in page.stdout
    top = git('rev-parse', '--show-toplevel').stdout.decode().strip()
    rel = os.path.relpath(os.path.abspath(__file__), top)
    at_commit = git('show', f'{commit}:{rel}')
    same = at_commit.returncode == 0 and sha256_bytes(at_commit.stdout) == me
    return {'commit': commit, 'main_ref': main_ref, 'on_main': on_main,
            'page': PAGE, 'page_sha256_computed': sha256_bytes(page.stdout) if page.returncode == 0 else None,
            'page_sha256_matches_argument': page_ok, 'page_pins_instrument': pins_me,
            'instrument': rel, 'instrument_sha256_computed': me, 'instrument_equals_file_at_commit': same,
            'pass': on_main and page_ok and pins_me and same}

# ---- controls for the symbolic form and the domain layer (synthetic forms; no density mode enters) ----
def synthetic_forms():
    """fourteen synthetic coefficient forms with known readings: (name, configuration, form, the verdict expected on
    each domain under C2, and under C1). 'withdrawn' marks a reading over levels that must withdraw."""
    L, one, k1 = LAMS, sp.Integer(1), (0, 0, 0, 1, 0)
    S, N, C, A, W = 'S3 RP3 S3/2I'.split(), 'NOT ABSORBED', 'CONDITIONAL', 'ABSORBED', 'withdrawn'
    every = lambda v: dict.fromkeys(S, v)
    return [
        ('identically zero', 'quadrature', [{(2, 0, 0, 0, 0): sp.Integer(0)}, {k1: one}], every(A), every(A)),
        ('one admissible condition, free of lambda', 'quadrature', [{(2, 0, 0, 0, 0): cs2 - sp.Rational(1, 3)}, {k1: one}], every(C), every(C)),
        ('a condition depending on lambda', 'quadrature', [{(2, 0, 0, 0, 0): cs2 - L/40}, {k1: one}], every(N), every(N)),
        ('an inadmissible condition', 'quadrature', [{(0, 2, 0, 0, 0): one, (2, 0, 0, 0, 0): omega2_of(L)}, {k1: one}], every(N), every(N)),
        ('absorbed except at n = 2', 'quadrature', [{(2, 0, 0, 0, 0): sp.Integer(0)}, {k1: L - 8, (2, 0, 0, 0, 0): one}],
         {'S3': N, 'RP3': N, 'S3/2I': A}, every(N)),
        ("radiation at every level, (3 c_s^2 - 1)(lambda - 3) + p'' lambda", 'quadrature',
         [{(2, 0, 0, 0, 0): (3*cs2 - 1)*(L - 3) + p2*L}, {k1: one}], every(C), every(C)),
        ('c_s^2 = 1/10, inside the floor on S^3/2I only', 'quadrature', [{(2, 0, 0, 0, 0): cs2 - sp.Rational(1, 10)}, {k1: one}],
         {'S3': N, 'RP3': N, 'S3/2I': C}, {'S3': N, 'RP3': N, 'S3/2I': C}),
        ('c_s^2 = 2, above the ceiling', 'quadrature', [{(2, 0, 0, 0, 0): cs2 - 2}, {k1: one}], every(N), every(N)),
        ("an impossible law, c_s^2 = p''^2 + 2", 'quadrature', [{(2, 0, 0, 0, 0): cs2 - p2**2 - 2}, {k1: one}], every(N), every(N)),
        ("UA's shift: (13a) = kappa - c_s^2 + p'', (13b) = (lambda - 8)(kappa - p'')", 'standing',
         [{k1: one, (0, 0, 0, 0, 0): p2 - cs2}, {k1: L - 8, (0, 0, 0, 0, 0): -(L - 8)*p2}], every(C), every(N)),
        ('c_s^2 = 1/4 + lambda/400', 'quadrature', [{(2, 0, 0, 0, 0): cs2 - sp.Rational(1, 4) - L/400}, {k1: one}], every(N), every(N)),
        ("a shift coefficient that depends on the law, 3 c_s^2 - 1", 'quadrature', [{(2, 0, 0, 0, 0): p2}, {k1: 3*cs2 - 1}], every(W), every(C)),
        ("UA's free shift: (13a) = kappa - c_s^2 + p'', (13b) = 0", 'standing', [{k1: one, (0, 0, 0, 0, 0): p2 - cs2}, {(0, 0, 0, 0, 0): sp.Integer(0)}],
         every(A), every(C)),
        ("UB's free shift: (13a) = kappa - c_s^2, (13b) = p''", 'quadrature', [{k1: one, (0, 0, 0, 0, 0): -cs2}, {(0, 0, 0, 0, 0): p2}],
         every(C), every(N)),
    ]

def synthetic_levels(form, levels=IS_NODES + IS_CHECKS):
    """a synthetic form's own coefficients at each computed level, as the run would have them"""
    return {n: [{mon: sp.expand(c.subs(LAMS, n*(n + 2))) for mon, c in side.items()} for side in form] for n in levels}

def fallback_forms():
    """the computed-levels fallback's controls: (name, configuration, form, the verdict expected on each domain, C2)"""
    forms = {name: (kind, f) for name, kind, f, _, _ in synthetic_forms()}
    S, N, C = 'S3 RP3 S3/2I'.split(), 'NOT ABSORBED', 'CONDITIONAL'
    return [('c_s^2 = 1/4 + lambda/400', *forms['c_s^2 = 1/4 + lambda/400'], {'S3': N, 'RP3': N, 'S3/2I': C}),
            ("a shift coefficient that depends on the law, 3 c_s^2 - 1", *forms["a shift coefficient that depends on the law, 3 c_s^2 - 1"],
             dict.fromkeys(S, C))]

# ---- the run (the page's §5 and §6): once, after the gate; its record is run.json beside this file ----
def jsonable(x):
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set)):
        return [jsonable(v) for v in x]
    if isinstance(x, (bool, int, float, str)) or x is None:
        return x
    return str(x)

def certify(entry, ignore=False):
    """the explicit checks fail closed: when the explicit grade at n = 2 or 12 disagrees with the per-level reading
    there, every verdict the configuration's per-level path produced, over every level or over the computed levels, is
    moved to a key saying it is not certified, beside both disagreeing values, and none stands as the configuration's
    grade. ignore=True certifies regardless (a mutation arm: the superseded behaviour)."""
    bad = sorted(n for n, v in entry.get('explicit checks', {}).items() if not v['agrees'])
    entry['certified'] = ignore or not bad
    if bad and not ignore:
        for key in [k for k in entry if k.startswith('every level') or k.startswith('computed levels only')]:
            entry[key + ', not certified'] = entry.pop(key)
        entry['not certified, because'] = f'the explicit grade at n = {bad} disagrees with the per-level reading; both values are kept'
    return entry

def mock_mode(n, T):
    """FOR THE DRY RUN ONLY: a non-physical first-order configuration (psi = Q T, E = 2 Q T, x = 3 Q T, nu = 0) that
    exercises the density-sector code path without evaluating the density mode"""
    Q = zonal_Q(n)
    return {'nu1': 0*Q, 'psi1': Q*T, 'E1': 2*Q*T, 'x1': 3*Q*T, 'omega2': (cs2*(n*(n + 2) - 3) - 1)/R**2}

def run_IS(mode=None, sign=-1):
    """the density sector: coefficients at the node and check levels, the symbolic form, every configuration under
    both charge readings on every domain, the time-averaged diagnostic, the explicit per-level checks at n = 2 and
    n = 12, and the integrability conditions"""
    rec = {}
    levels = IS_NODES + IS_CHECKS
    coeffs = {n: is_coefficients(n, mode=mode) for n in levels}
    c1 = is_coefficients(2, charge='C1', mode=mode)
    rec['C1 is C2 at kappa = 0, n = 2'] = all(
        sp.simplify(sum(c*sp.Mul(*[g**k for g, k in zip(GENS, mon)]) for mon, c in a.items()) -
                    sum(c*sp.Mul(*[g**k for g, k in zip(GENS, mon)]) for mon, c in b.items()).subs(KAP, 0)) == 0
        for a, b in zip(c1, coeffs[2]))
    rec['homogeneous lapse drops out'] = all(mon[4] == 0 or sp.simplify(c) == 0 for n in levels for side in coeffs[n] for mon, c in side.items())
    polys, interp, established = interpolation_record(coeffs)
    rec['symbolic form'] = {'established': established, 'nodes': IS_NODES, 'checks': IS_CHECKS,
                            'degree bound': IS_DEGREE_BOUND, 'coefficients': interp}
    rec['per-level coefficients'] = {n: {'13a': coeffs[n][0], '13b': coeffs[n][1]} for n in levels}
    configs = {}
    for kind in ('standing', 'quadrature', 'general'):
        for charge in ('C1', 'C2'):
            per_level, per_level_avg = {}, {}
            for n in levels:                                # each level's own coefficients, on each domain admitting it
                lam_n, doms = sp.Integer(n*(n + 2)), [d for d in IS_DOMAINS if admits(d, n, kind)]
                per_level[n] = {d: read_symbolic(coeffs[n], kind, charge, lam=lam_n, domain=d) for d in doms}
                per_level_avg[n] = {d: read_symbolic(coeffs[n], kind, charge, mean_only=True, lam=lam_n, domain=d) for d in doms}
            entry = {'per level': per_level, 'per level, time-averaged': per_level_avg}
            for label, mean in (('', False), (', time-averaged', True)):
                if established:
                    every = {d: common_laws(polys, kind, charge, d, mean_only=mean) for d in IS_DOMAINS}
                    entry['every level' + label] = every
                    withdrawn = [d for d in IS_DOMAINS if every[d]['verdict'] == 'withdrawn']
                else:
                    entry['every level' + label] = ('withdrawn: the symbolic form is not established (a check level disagreed, or a '
                                                    'degree exceeded the bound); the grades cover the computed levels only')
                    withdrawn = list(IS_DOMAINS)
                if withdrawn:                               # the computed levels carry the grade, by the same intersection
                    entry['computed levels only' + label] = {d: computed_levels(coeffs, kind, charge, d, mean_only=mean) for d in withdrawn}
            entry['explicit checks'] = {n: (lambda g: {'grade_IS': g, 'per-level reading': per_level[n]['S3'], 'agrees': g[0] == per_level[n]['S3'][0]})(
                grade_IS(n, kind, charge, mode=mode)) for n in (2, 12)}
            configs[f'{kind}, {charge}'] = certify(entry)
    rec['configurations'] = configs
    rec['integrability'] = {'zonal standing, n = 2': is_integrability('zonal', sign=sign),
                            'rotating pair, n = 2 (X1 X3, X1 X4)': is_integrability('rotating', sign=sign),
                            'timelike': 'the averaged constraint (13b), graded above'}
    return rec

def run_decided():
    """the decided sectors, reported again under the frozen instrument"""
    rec = {}
    w2 = hanio_frequency()
    rec['H-ANISO'] = {
        'omega^2 R^2': sp.simplify(w2*R**2),
        'cells': {f'{k}, {c}': hanio_cell(k, c, w2) for k in ('standing', 'quadrature', 'general') for c in ('C1', 'C2')},
        'time-averaged': {f'{k}, {c}': hanio_diagnostic(k, c, w2) for k in ('standing', 'quadrature', 'general') for c in ('C1', 'C2')},
        'integrability (unit radius, unit left-invariant generators)': {
            k: {'routine': hanio_integrability(hanio_beta_matrix(k, sp.sqrt(8))),
                'frame path, 2 C_a': [2*x for x in hanio_frame_charge(hanio_beta_matrix(k, sp.sqrt(8)))]}
            for k in ('standing', 'quadrature', 'general', 'rotating')},
        'domains': 'the five modes are left-invariant: S^3, RP^3, S^3/2I'}
    rec['I-T'] = {'reduction': it_reduction(), 'lowest level integrability': 'by orientation reversal from H-ANISO; higher levels not computed'}
    fields = {'cos chi d_phi': [0, 0, sp.cos(chi)], 'sin chi cos theta d_phi': [0, 0, sp.sin(chi)*sp.cos(th3)]}
    rec['I-V'] = {
        'first order': {k: iv_first_order(F, F) for k, F in fields.items()},
        'averaged curvature, relabeling at fixed V_h': {k: averaged_curvature_vector(F) for k, F in fields.items()},
        'first variation, <R1> and <tr h>': {'dX1 dX1': first_variation_avg(ambient_tensor([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])),
                                             'gamma': first_variation_avg(GAM3)},
        'constraint': iv_constraint(),
        'integrability': {f'{k}, {g}': iv_integrability(F, g) for k, F in fields.items() for g in ('shift', 'static-shift-free')},
        'time-averaged': 'inapplicable: the configuration is time-independent (T6)'}
    return rec

def run(gate, mode=None, sign=-1, out_path=None):
    """THE RUN, once, after the gate passed (or, with mode=mock_mode and sign=+1, the dry run, whose record is
    discarded): the decided sectors reported again, the density sector graded, the record written"""
    import json, platform, time
    t0 = time.time()
    rec = {'gate': gate, 'environment': {'python': platform.python_version(), 'sympy': sp.__version__, 'platform': platform.platform(),
                                         'hash seed': os.environ.get('PYTHONHASHSEED')},
           'dry run': mode is not None}
    rec['decided'] = run_decided()
    rec['I-S'] = run_IS(mode=mode, sign=sign)
    rec['seconds'] = round(time.time() - t0, 1)
    with open(out_path or os.path.join(HERE, 'run.json'), 'w') as f:
        json.dump(jsonable(rec), f, indent=1, sort_keys=True)
    return rec

# ---- the terms-to-instrument map (the page's §5) ----
TERMS = [
    ('§0 T4, the volume radius fixed', 'buchert_residuals with aD constant (hanio_cell)'),
    ('§0 T6, every instant', 'vanishes_identically: each residual required at every t'),
    ('§0 T7(a), the induced homogeneous source', 'hanio_cell: delta_eps solved from (13b), never chosen'),
    ('§0 T7(b), C1, the charge held', 'eps_of_charge; hanio_cell(charge="C1"): delta_eps = 0 at fixed volume'),
    ('§1 T2, the response law to second order', 'pressure'),
    ('§1 T3, standing, quadrature and general configurations', 'hanio_config'),
    ('§2 Buchert 2001, (13a) to (13d)', 'buchert_residuals; it_reduction for (13c), (13d)'),
    ('§2 BMR 2020, fluid-extrinsic, for I-V', 'iv_constraint: (3.32) and (3.33) with (3.34) and (3.36), transcribed, on the whole slice as (3.54) and (3.56) give them; (3.35) and (3.55) beyond second order'),
    ('§2 the I-V slicings, both', 'iv_constraint: the second-order lapse drops out; the mean curvature shifts by the same background combination and a Laplacian'),
    ('§3 H-ANISO, exactly', 'bianchi_ix_ricci, hanio_frequency, hanio_quadratics, hanio_cell'),
    ('§3 I-T, the reduction P = 0, Q = -2 <sigma^2>', 'it_reduction (structural)'),
    ('§3 I-V, the reduction', 'iv_first_order on two n = 2 fields; averaged_curvature_vector and first_variation_avg; iv_constraint under C1, BMR against ADM'),
    ('§3 I-V, the charge left free, for comparison', 'iv_constraint: c_s^2 = (a + 3b)/(3(a + b)) and its range'),
    ('§3 the charge left free, for comparison', 'hanio_cell(charge="C2")'),
    ('§5 the positive control', 'flrw_second_order'),
    ('§5 the negative control', 'hanio_cell("standing", ...)'),
    ('§5 the quadrature control', 'hanio_cell("quadrature", ...), both charge readings'),
    ('§5 the run gate', 'run_gate; probed before the freeze in a throwaway clone: its parent passes and four arms fail'),
    ('§0 T6 and §5 step 6, the time-averaged diagnostic', 'period_average over one period of the first-order mode; time_averaged_reading with the grade\'s own variables; hanio_diagnostic'),
    ('§1 T1, harmonics mode by mode; quotients by restriction', 'zonal_Q; S3avg; Schur: grade_IS sums orthogonal modes'),
    ('§2 Buchert 2001, the I-S averages', 'is_residuals: tc, avg_ser, ricci_scalar_warped, the charge, the response law'),
    ('§2 R_V fixed for I-S', 'is_residuals: c2 solved from <J> = 1 at second order'),
    ('§3 the I-S first-order mode', 'is_mode, checked by is_mode_direct'),
    ('§4 the I-S grades, every instant, both charge readings', 'the run: read_symbolic per level and domain, common_laws per domain; grade_IS at n = 2 and 12 as the explicit check'),
    ('§1 T1 and §4, I-S at every level, the eigenvalue symbolic', 'is_coefficients (the run) at n = 2 to 10 and 12; interpolate_levels through n = 2 to 8, checked at 9, 10 and 12, within IS_DEGREE_BOUND'),
    ('§1 the quotients and their levels', 'multiplicity and admits: (n+1)^2; even n on RP^3; the Molien count times (n+1) on S^3/2I'),
    ('§4 the verdict over levels, per domain', 'common_laws: C_D, the intersection over admitted levels; the polynomial-in-lambda coefficients, the shift coefficient, exceptional levels, admissible_part'),
    ('§4 and §5, the computed levels where the every-level reading is withdrawn', 'computed_levels: the intersection of the computed levels\' law sets, then admissible_part'),
    ('§5 the degree bound and its certificate', 'interpolation_record with IS_DEGREE_BOUND = 5; ten levels certify up to degree 9'),
    ('§5 the explicit checks at n = 2 and 12, failing closed', 'certify: a disagreement withholds every per-level-path verdict'),
    ('§1 T2, read per domain (ruled 2026-10-11)', 'cs2_floor, admissible: 1/(lambda_min - 3) below, 1 above'),
    ('§4 the shared reading, for every grade and the diagnostic', 'read, fourier_parts, project_shift, solve_laws, admissible_part (T2 per domain: 1/(lambda_min - 3) < c_s^2 <= 1)'),
    ('§5 the I-S controls', 'is_mode_direct, S3avg identities, the conformal check, averaged_curvature (pure gauge), the FLRW control via is_residuals'),
    ('§5 and §6, Losic and Unruh, the comparison', 'not computed by the instrument: a record written after the run from run.json and their paper, and reviewed before the result closes'),
    ('§4 and §5, the remaining integrability conditions', 'momentum_constraint, gravitational and matter parts apart; charges against killing_hyper or the left-invariant frame; hanio_integrability, checked by hanio_frame_charge; iv_integrability in two gauges; is_integrability (the run); the timelike condition is the graded (13b)'),
    ('§5 the run and its record', 'run: run_decided, run_IS; run.json, with the identities the gate computes'),
    ('§5 the dry run', 'mock_mode: a non-physical configuration through the same code path, its record discarded'),
]

def qualify():
    out = []
    def line(ok, text):
        out.append(f"[{'PASS' if ok else 'FAIL'}] {text}")
        return ok
    w2 = hanio_frequency()
    p_w = line(sp.simplify(w2 - 8/R**2) == 0, f'H-ANISO frequency, from the trace-free Ricci: omega^2 = {sp.simplify(w2*R**2)}/R^2')
    bq = hanio_config('quadrature', sp.sqrt(w2))
    _, dRq = hanio_quadratics(bq)
    p_c = line(sp.simplify(e**2*dRq[2] + 8/R**2*sum(bk**2 for bk in bq)) == 0,
               'the curvature at fixed volume, to second order: delta 3R = -(8/R^2) Tr beta^2')
    expect = {('standing', 'C1'): 'NOT ABSORBED', ('quadrature', 'C1'): 'NOT ABSORBED', ('general', 'C1'): 'NOT ABSORBED',
              ('standing', 'C2'): 'NOT ABSORBED', ('quadrature', 'C2'): 'CONDITIONAL', ('general', 'C2'): 'NOT ABSORBED'}
    grades, p_h = {}, True
    for (kind, charge), want in expect.items():
        g, d = grades[(kind, charge)] = hanio_cell(kind, charge, w2)
        extra = f', at c_s^2 = {d["condition c_s^2"]}' if g == 'CONDITIONAL' else ''
        p_h &= line(g == want, f'H-ANISO {kind}, {"charge held" if charge == "C1" else "charge left free"}: {g}{extra}')
    p_q = line(grades[('quadrature', 'C2')][1].get('condition c_s^2') == [sp.Rational(1, 3)],
               'the quadrature control: with the charge left free it holds only at c_s^2 = 1/3')
    want_avg = {'C1': 'fails on average', 'C2': 'holds on average only at c_s^2 = [1/3]'}
    pred_d = lambda kind, **kw: all(hanio_diagnostic(kind, ch, w2, **kw)[0] == want_avg[ch] for ch in ('C1', 'C2'))
    p_d1 = line(pred_d('quadrature'), 'the time-averaged diagnostic, constant control: the H-ANISO quadrature cell reads on average '
                'as its grade (charge held: fails; charge left free: only at c_s^2 = 1/3)')
    p_d2 = line(pred_d('standing') and pred_d('general'), 'the time-averaged diagnostic, time-dependent control: the H-ANISO '
                'standing and general configurations, averaged over one period, read as the quadrature cell')
    p_f = True
    for c, q in ((sp.Rational(1, 3), 0), (sp.Rational(1, 5), sp.Rational(1, 7))):
        static, res, lam2 = flrw_second_order(c, q)
        p_f &= line(static and all(cf == 0 for r in res for cf in r),
                    f'positive control: an exact FLRW solution (c_s^2 = {c}, p\'\' = {q}), radius free, satisfies (13a) and (13b) '
                    f'through second order; lambda^2 = {sp.simplify(lam2*R**2)}/R^2')
    ok_t, it = it_reduction()
    p_t = line(ok_t, 'the I-T reduction, structurally: no first-order density, expansion, momentum or lapse; Q = -2 <sigma^2>, P = 0')
    # ---- the I-S machinery, on controls only ----
    p_s = True
    direct = {}
    for n in (2, 3, 4):                                     # the comoving mode against the direct Einstein-tensor solve
        w2d, amps = direct[n] = is_mode_direct(n)
        lam = n*(n + 2)
        want = [1, -1, cs2*(lam - 3), -(lam - 3)/(4*sp.pi*G*R**2)]
        p_s &= line(sp.simplify(w2d - is_mode(n, 1)['omega2']) == 0 and all(sp.simplify(a - b) == 0 for a, b in zip(amps, want)),
                    f'I-S mode, n = {n}: the direct solve gives omega^2 = ({sp.simplify(w2d*R**2)})/R^2 and psi : E : nu : d eps as is_mode states')
    ns = (2, 3, 4)
    orth = all(S3avg(zonal_Q(a)*zonal_Q(b)) == (1 if a == b else 0) for a in ns for b in ns) and all(S3avg(zonal_Q(a)) == 0 for a in ns)
    grad = all(sp.simplify(S3avg(sp.diff(zonal_Q(a), chi)**2) - a*(a + 2)) == 0 for a in ns)
    cross = all(S3avg(sp.diff(zonal_Q(a), chi)*sp.diff(zonal_Q(b), chi)) == 0 for a in ns for b in ns if a != b)
    hess = lambda q: sp.diff(q, chi, 2)**2 + 2*(sp.cos(chi)/sp.sin(chi)*sp.diff(q, chi))**2
    boch = all(sp.simplify(S3avg(hess(zonal_Q(a))) - (a*(a + 2))**2 + 2*a*(a + 2)) == 0 for a in ns)
    p_o = line(orth and grad and cross and boch, 'harmonics: <Q_n Q_m> = delta_nm, <Q_n> = 0, <|dQ|^2> = lambda, cross-gradients vanish, Bochner <|DDQ|^2> = lambda^2 - 2 lambda')
    aa = sp.Symbol('a'); phiQ = aa*zonal_Q(2)
    Gchi, F = is_metric(phiQ, 0, 0)
    om = sp.log(1 - 2*e*phiQ)/2
    lap = (sp.diff(sp.sin(chi)**2*sp.diff(om, chi), chi)/sp.sin(chi)**2)/R**2
    conf = tc(sp.exp(-2*om)*(6/R**2 - 4*lap - 2*sp.diff(om, chi)**2/R**2))
    p_k = line(all(to_u(x - y) == 0 for x, y in zip(tc(ricci_scalar_warped(Gchi, F)), conf)),
               'the curvature routine against the exact conformal formula, through second order')
    L = sp.Symbol('L')
    p_g = True
    for n in (2, 3):
        p_g &= line(averaged_curvature(0, L*zonal_Q(n)) == [6/R**2, 0, 0],
                    f'pure gauge, n = {n}: a spatial relabeling leaves <R> unchanged through second order, with R_V fixed')
    X1, X2 = sp.Function('X1')(t), sp.Function('X2')(t)
    def flrw_is(double=False):
        x1, x2, *_ = flrw_separatrix(cs2, p2)
        ra, rb = is_residuals(0, -X1, 0, -3*X1, c2=-X2 - X1**2/2, nu2h=0, aD=R*(1 + e*X1 + e**2*X2), charge='C1')
        sub = {X1: x1, X2: (2 if double else 1)*x2}
        return [sp.simplify(c.subs(sub).doit()) for c in ra + rb]
    p_fi = line(all(c == 0 for c in flrw_is()), "the positive control through the I-S code path: the exact FLRW solution, c_s^2 and p'' symbolic, the charge held, radius free")
    # ---- the I-V reduction (the page's §3), on two transverse n = 2 fields, then through the averaged equations ----
    fields = {'cos chi d_phi': [0, 0, sp.cos(chi)], 'sin chi cos theta d_phi': [0, 0, sp.sin(chi)*sp.cos(th3)]}
    fo = {k: iv_first_order(F, F) for k, F in fields.items()}
    pred_v1 = lambda rs: all(r['divF'] == 0 and r['trh1'] == 0 and r['R1'] == 0 and r['trK1'] == 0 for r in rs)
    pred_v2 = lambda rs: all(bool(r['K2'] > 0) and bool(r['divK2'] > 0) for r in rs)
    p_v1 = line(pred_v1(fo.values()), 'I-V first order, on two transverse n = 2 fields: div F = 0, so tr h = 0 and tr K = 0, '
                'and a relabeling leaves the curvature unchanged')
    p_v2 = line(pred_v2(fo.values()), 'I-V first order: a non-Killing transverse shift has <K_ij K^ij> = '
                f'{fo["cos chi d_phi"]["K2"]} > 0 and tilt through the momentum constraint, <|D.K|^2> = {fo["cos chi d_phi"]["divK2"]} (unit S^3)')
    acv = {k: averaged_curvature_vector(F) for k, F in fields.items()}
    p_v3 = line(all(v == [6, 0, 0] for v in acv.values()),
                'I-V averaged curvature: a first-order relabeling leaves <R> unchanged through second order, with V_h fixed (unit S^3)')
    X1sq = ambient_tensor([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    fv = [first_variation_avg(h) for h in (X1sq, GAM3)]
    pred_v3b = lambda coef: all(sp.simplify(r1 - coef*tr) == 0 for r1, tr in fv)
    p_v3b = line(pred_v3b(-2) and all(tr != 0 for _, tr in fv),
                 'I-V first variation at the round metric: <R> changes by -(2/R^2) <tr h>, on dX1 dX1 and on the metric itself, '
                 'so a second-order term at fixed V_h adds nothing')
    ivc = iv_constraint()
    p_v4 = line(ivc['lapse_free'], "I-V slicings: the second-order lapse multiplies only the static background's constraint and "
                'Raychaudhuri combinations, so the reduction is the same on both slicings')
    p_v5 = line(ivc['ADM_equals_BMR'] and ivc['C1_form'],
                f"I-V under C1: BMR's (3.33) and (3.32) agree with the plain ADM forms, and (3.33) reads {ivc['C1_value']} = 0 "
                '(V2 = <v^2>, K2 = <K_ij K^ij>): a sum of non-negative terms')
    p_v6 = line(ivc['comparison'] and ivc['range'], 'I-V with the charge left free (comparison): (3.32) then holds only at '
                'c_s^2 = (a + 3b)/(3(a + b)), strictly between 1/3 and 1')
    # ---- the symbolic form, its domain layer, the multiplicities ----
    hv = {}
    for n in IS_NODES + IS_CHECKS:
        Q = zonal_Q(n)
        hv[n] = (S3avg(Q**2), S3avg(sp.diff(Q, chi)**2), S3avg(sp.diff(Q, chi, 2)**2 + 2*(sp.cos(chi)/sp.sin(chi)*sp.diff(Q, chi))**2))
    want_h = (sp.Integer(1), LAMS, LAMS**2 - 2*LAMS)
    pred_i1 = lambda nodes: all((lambda r: sp.expand(r[0] - want_h[k]) == 0 and all(r[1].values()))(
        interpolate_levels({n: hv[n][k] for n in hv}, nodes=nodes)) for k in range(3))
    p_i1 = line(pred_i1(IS_NODES), 'the symbolic form: interpolation through n = 2 to 8 reproduces <Q^2> = 1, <|dQ|^2> = lambda and '
                "Bochner's lambda^2 - 2 lambda exactly, and agrees at n = 9, 10 and 12")
    syn = synthetic_forms()
    syn_read = lambda f, kind, ch, **kw: {dom: common_laws(f, kind, ch, dom, **kw)['verdict'] for dom in IS_DOMAINS}
    pred_i2 = lambda **kw: all(syn_read(f, kind, 'C2', **kw) == w2_ and syn_read(f, kind, 'C1', **kw) == w1_ for _, kind, f, w2_, w1_ in syn)
    p_i2 = line(pred_i2(), f'the reading over levels on {len(syn)} synthetic forms, under both charge readings: ' + '; '.join(name for name, *_ in syn) +
                ': each reads as expected on each domain')
    fb = fallback_forms()
    pred_fb = lambda **kw: all({d: computed_levels(synthetic_levels(f), kind, 'C2', d, **kw)['verdict'] for d in IS_DOMAINS} == want
                               for _, kind, f, want in fb)
    p_fb = line(pred_fb(), 'the computed-levels fallback intersects the law sets of the computed levels: c_s^2 = 1/4 + lambda/400 reads NOT ABSORBED '
                'on S^3 and RP^3 and CONDITIONAL on S^3/2I, whose only computed level is 12; the law-dependent shift, withdrawn over '
                'levels, reads CONDITIONAL there')
    form = {name: f for name, _, f, _, _ in syn}
    pred_rd = lambda **kw: read_symbolic(form["an impossible law, c_s^2 = p''^2 + 2"], 'quadrature', 'C2', lam=sp.Integer(8), **kw)[0] == 'NOT ABSORBED' and \
        read_symbolic(form["UA's shift: (13a) = kappa - c_s^2 + p'', (13b) = (lambda - 8)(kappa - p'')"], 'standing', 'C2', lam=sp.Integer(8), **kw)[0] == 'ABSORBED'
    p_rd = line(pred_rd(), "the per-level reading: c_s^2 = p''^2 + 2 has no admissible law (NOT ABSORBED); where (13b) does not fix the shift, "
                "another residual does, and UA's form holds at n = 2 (ABSORBED)")
    deg = lambda k: {n: [{(2, 0, 0, 0, 0): sp.Integer(n*(n + 2))**k + 1}, {(0, 0, 0, 1, 0): sp.Integer(1)}] for n in IS_NODES + IS_CHECKS}
    pred_deg = lambda bound=None: interpolation_record(deg(5), bound=bound)[2] and not interpolation_record(deg(6), bound=bound)[2]
    p_deg = line(pred_deg(), f'the degree bound, {IS_DEGREE_BOUND}: a coefficient of degree 5 establishes the symbolic form, one of degree 6 does not')
    def pred_cert(**kw):
        agree = certify({'explicit checks': {2: {'agrees': True}, 12: {'agrees': True}}, 'every level': {'S3': 'ABSORBED'}}, **kw)
        split = certify({'explicit checks': {2: {'agrees': True}, 12: {'agrees': False}}, 'every level': {'S3': 'ABSORBED'},
                         'computed levels only': {'S3': 'ABSORBED'}}, **kw)
        return agree['certified'] and 'every level' in agree and not split['certified'] and 'every level' not in split and \
            'computed levels only' not in split and 'every level, not certified' in split and 'not certified, because' in split
    p_cert = line(pred_cert(), 'the explicit checks fail closed: a disagreement at n = 2 or 12 withholds every verdict of the per-level path, '
                  'keeping it under a key that says it is not certified')
    p_i3 = line([multiplicity('S3/2I', n) for n in (12, 20, 24, 30)] == [13, 21, 25, 31] and multiplicity('RP3', 3) == 0
                and admits('S3/2I', 12, 'quadrature') and not admits('S3/2I', 2, 'standing'),
                'the multiplicities: 13, 21, 25 and 31 invariant harmonics at n = 12, 20, 24 and 30 on S^3/2I (molien-shells.test.py), '
                'none at odd n on RP^3; pairs exist at n = 12 on S^3/2I')
    # ---- the integrability routine: H-ANISO against the frame formula, I-V, the I-S first-order constraint ----
    hint = {k: hanio_integrability(hanio_beta_matrix(k, sp.sqrt(8))) for k in ('standing', 'quadrature', 'general', 'rotating')}
    frame_rot = [2*x for x in hanio_frame_charge(hanio_beta_matrix('rotating', sp.sqrt(8)))]
    pred_n1 = lambda h: all(all(v == 0 for v in h[k][0]) for k in h) and \
        all(h[k][1][a]['total'] == 0 and h[k][1][a]['constant'] for k in ('standing', 'quadrature', 'general') for a in ('e1', 'e2', 'e3')) and \
        [h['rotating'][1][a]['total'] for a in ('e1', 'e2', 'e3')] == frame_rot and frame_rot[2] != 0 and h['rotating'][1]['e3']['matter'] == 0
    p_n1 = line(pred_n1(hint), 'integrability, H-ANISO: the standing and quadrature configurations and the general superposition\'s diagonal '
                f'members carry no charge; a rotating non-diagonal member carries {frame_rot[2]} (eps^2/R^2, unit left-invariant axis), '
                'all of it gravitational, as the class-A frame formula gives')
    avg_tests = [sp.cos(chi)**2, (sp.sin(chi)*sp.sin(th3)*sp.cos(ph3))**4, sp.cos(chi)*sp.sin(th3), zonal_Q(5)**2, sp.diff(zonal_Q(4), chi)**2,
                 sp.sin(chi)**2*sp.cos(th3)**2*sp.cos(chi)**2]
    pred_avg = lambda **kw: all(sp.simplify(avg_hyper(f) - avg_hyper_fast(f, **kw)) == 0 for f in avg_tests)
    p_avg = line(pred_avg(), 'the exact fast average over S^3 (Beta functions, monomial by monomial) agrees with direct integration on '
                 f'{len(avg_tests)} integrands')
    p_tr = line(hanio_trace_check(), 'the spatial conditions do not see the radius: a homogeneous second-order trace, a change of radius, '
                'leaves the H-ANISO rotating member\'s second-order momentum constraint unchanged at every point')
    ivi = {(k, g): iv_integrability(F, g) for k, F in fields.items() for g in ('shift', 'static-shift-free')}
    pred_n2 = lambda r: all(all(x == 0 for x in r[key][0]) and all(c['total'] == 0 and c['gravitational'] == 0 and c['matter'] == 0
                                                               for c in r[key][1].values()) for key in r)
    p_n2 = line(pred_n2(ivi), 'integrability, I-V: no charge against the six rotation generators and both chiral triples, on both n = 2 fields, '
                'in the relabeled gauge and the shift-free gauge; the first-order constraint holds in both')
    p_n3 = line(all(x == 0 for k in ('zonal', 'rotating') for x in is_first_order_constraint(k)),
                'integrability, I-S: the density mode satisfies the first-order momentum constraint in the comoving-orthogonal gauge '
                '(zonal and rotating pair); its second-order charges are computed in the run')
    parents = p_w and p_c and p_h and p_q and p_d1 and p_d2 and p_f and p_t and p_s and p_o and p_k and p_g and p_fi and \
        p_i1 and p_i2 and p_fb and p_rd and p_deg and p_cert and p_i3 and p_n1 and p_avg and p_tr and p_n2 and p_n3 and \
        p_v1 and p_v2 and p_v3 and p_v3b and p_v4 and p_v5 and p_v6
    arms = {
        'the frequency with the round radius taken as A instead of 2A': sp.simplify(hanio_frequency(Ahalf=R) - 8/R**2) != 0,
        'the curvature at fixed volume with the round radius taken as A instead of 2A':
            sp.simplify(e**2*hanio_quadratics(bq, Ahalf=R)[1][2] + 8/R**2*sum(bk**2 for bk in bq)) != 0,
        'each H-ANISO cell with its quadratic source removed, all six read otherwise':
            all(hanio_cell(k, c, w2, drop_quadratics=True)[0] != want for (k, c), want in expect.items()),
        "the second positive control (c_s^2 = 1/5, p'' = 1/7) with its second-order response doubled":
            not all(cf == 0 for r in flrw_second_order(sp.Rational(1, 5), sp.Rational(1, 7), corrupt=True)[1] for cf in r),
        'each I-S mode against a frequency without its -1, c_s^2 (lambda - 3)/R^2':
            all(sp.simplify(direct[n][0] - cs2*(n*(n + 2) - 3)/R**2) != 0 for n in (2, 3, 4)),
        "Bochner's identity without its -2 lambda": not all(sp.simplify(S3avg(hess(zonal_Q(a))) - (a*(a + 2))**2) == 0 for a in ns),
        'a second-order trace that is not homogeneous': not hanio_trace_check(nonconstant=True),
        "the fast average with its Beta exponent shifted by two": not pred_avg(shift=2),
        'the quadrature cell at omega^2 = 6/R^2': hanio_cell('quadrature', 'C2', 6/R**2)[1].get('condition c_s^2') != [sp.Rational(1, 3)],
        'the C1 standing cell with its quadratic source removed': hanio_cell('standing', 'C1', w2, drop_quadratics=True)[0] != 'NOT ABSORBED',
        'the positive control with its second-order response doubled': not all(cf == 0 for r in flrw_second_order(sp.Rational(1, 3), 0, corrupt=True)[1] for cf in r),
        'the I-T reduction with a trace kept': not it_reduction(tt=False)[0],
        'the I-S mode with the lapse taken as zero': sp.simplify(direct[2][1][2]) != 0,
        'pure gauge without the volume condition, n = 2 and 3': all(averaged_curvature(0, L*zonal_Q(n), fix_volume=False)[2] != 0 for n in (2, 3)),
        'the I-S-path positive control with its second-order response doubled': not all(c == 0 for c in flrw_is(double=True)),
        'the conformal check with the second-order term dropped': to_u(tc(ricci_scalar_warped(Gchi, F))[2]) != 0,
        'the time-averaged standing control with the average replaced by its value at t = 0': not pred_d('standing', at_zero=True),
        'the time-averaged standing control over a third of a period': not pred_d('standing', window=2*sp.pi/sp.sqrt(w2)/3),
        'the time-averaged quadrature control with the free density held at zero':
            (lambda r: time_averaged_reading(r[0], r[1], sp.sqrt(w2), 'C1', r[2])[0] != want_avg['C2'])(hanio_cell('quadrature', 'C2', w2, residuals=True)),
        'interpolation through the first two nodes only': not pred_i1((2, 3)),
        'the domain layer without its exceptional levels': not pred_i2(use_exceptions=False),
        'the superseded rule over levels, a condition that changes with the level read as NOT ABSORBED': not pred_i2(rule='per-level'),
        'one global floor, c_s^2 > 1/5 on every domain': not pred_i2(floor=sp.Rational(1, 5)),
        'no upper end on c_s^2': not pred_i2(ceiling=None),
        'the reading over levels with the shift set to zero where (13b) does not fix it': not pred_i2(shift_zero=True),
        'the superseded weakest-grade rule for the computed levels': not pred_fb(rule='weakest'),
        'the per-level reading keeping every law not proved inadmissible': not pred_rd(old_filter=True),
        'the per-level reading with the shift set to zero where (13b) does not fix it': not pred_rd(shift_zero=True),
        'the degree bound at 6': not pred_deg(bound=6),
        'certification that ignores a disagreement': not pred_cert(ignore=True),
        "the Molien count without its factor n + 1": [multiplicity('S3/2I', n)//(n + 1) for n in (12, 20, 24, 30)] != [13, 21, 25, 31],
        'the H-ANISO charge with the sign of the second connection term flipped':
            (lambda S_: (lambda gr: sp.simplify(sp.expand_trig(sum(2*S_.inv()[i, 2]*gr[i][2] for i in range(3)).subs({EUL[0]: 0, EUL[1]: sp.pi/2, EUL[2]: 0}))) != frame_rot[2])(
                momentum_constraint(list(EUL), (S_.T*S_/4).applyfunc(sp.simplify), (S_.T*(2*hanio_beta_matrix('rotating', sp.sqrt(8)))*S_/4).applyfunc(sp.expand),
                                    0, [0, 0, 0], [0, 0, 0], connection_sign=1)[0]))(sigma_matrix()),
        'the I-V shift-free charge against a field that is not Killing, sin chi cos chi d_chi':
            (lambda gm: charges(gm[0], gm[1], {'x': [sp.sin(chi)*sp.cos(chi), 0, 0]}, avg_hyper)['x']['total'] != 0)(
                momentum_constraint(X3, GAM3, -t*lie_metric3(fields['cos chi d_phi']), 0, [0, 0, 0],
                                    [sp.simplify(sum(GAM3.inv()[i, j]*momentum_constraint(X3, GAM3, sp.zeros(3, 3), 0, fields['cos chi d_phi'], [0, 0, 0])[0][j][1]/2 for j in range(3))) for i in range(3)])),
        'the I-S first-order constraint with E = +psi': not all(x == 0 for x in is_first_order_constraint('zonal', sign=1)),
        'I-V first order with a non-transverse field, sin chi d_chi': not pred_v1([iv_first_order([sp.sin(chi), 0, 0], [sp.sin(chi), 0, 0])]),
        'I-V first order with a Killing shift, d_phi': not pred_v2([iv_first_order(fields['cos chi d_phi'], [0, 0, 1])]),
        'I-V averaged curvature without the volume condition': averaged_curvature_vector(fields['cos chi d_phi'], fix_volume=False) != [6, 0, 0],
        'I-V first variation with its trace term dropped': not pred_v3b(0),
        'I-V slicings with Lambda off its static value': not iv_constraint(lam_shift=sp.Symbol('delta'))['lapse_free'],
        "I-V under C1 with T's sign flipped in the transcription of BMR": not (lambda d: d['ADM_equals_BMR'] and d['C1_form'])(iv_constraint(tilt_sign=-1)),
        'I-V under C1 with the tilt factor dropped from the charge': not (lambda d: d['ADM_equals_BMR'] and d['C1_form'])(iv_constraint(keep_gamma=False)),
        'I-V comparison with T dropped from (3.32)': not (lambda d: d['comparison'] and d['range'])(iv_constraint(raych_tilt=False)),
    }
    for name, fired in arms.items():
        line(fired and parents, f'arm turns its check red: {name}')
    cover = [
        ('the H-ANISO frequency', ['the frequency with the round radius taken as A instead of 2A']),
        ('the curvature at fixed volume', ['the curvature at fixed volume with the round radius taken as A instead of 2A']),
        ('the six H-ANISO cells', ['each H-ANISO cell with its quadratic source removed, all six read otherwise',
                                  'the C1 standing cell with its quadratic source removed', 'the quadrature cell at omega^2 = 6/R^2']),
        ('the quadrature control', ['the quadrature cell at omega^2 = 6/R^2']),
        ('the diagnostic, constant control', ['the time-averaged quadrature control with the free density held at zero']),
        ('the diagnostic, time-dependent control', ['the time-averaged standing control with the average replaced by its value at t = 0',
                                                    'the time-averaged standing control over a third of a period']),
        ('the positive control at c_s^2 = 1/3', ['the positive control with its second-order response doubled']),
        ('the positive control at c_s^2 = 1/5', ["the second positive control (c_s^2 = 1/5, p'' = 1/7) with its second-order response doubled"]),
        ('the I-T reduction', ['the I-T reduction with a trace kept']),
        ('the I-S modes, n = 2, 3, 4', ['each I-S mode against a frequency without its -1, c_s^2 (lambda - 3)/R^2', 'the I-S mode with the lapse taken as zero']),
        ('the harmonic identities', ["Bochner's identity without its -2 lambda"]),
        ('the conformal check', ['the conformal check with the second-order term dropped']),
        ('pure gauge, n = 2 and 3', ['pure gauge without the volume condition, n = 2 and 3']),
        ('the positive control through the I-S path', ['the I-S-path positive control with its second-order response doubled']),
        ('I-V first order, transverse', ['I-V first order with a non-transverse field, sin chi d_chi']),
        ('I-V first order, the shift', ['I-V first order with a Killing shift, d_phi']),
        ('I-V averaged curvature', ['I-V averaged curvature without the volume condition']),
        ('I-V first variation', ['I-V first variation with its trace term dropped']),
        ('I-V slicings', ['I-V slicings with Lambda off its static value']),
        ('I-V under C1', ["I-V under C1 with T's sign flipped in the transcription of BMR", 'I-V under C1 with the tilt factor dropped from the charge']),
        ('I-V comparison', ['I-V comparison with T dropped from (3.32)']),
        ('the symbolic form', ['interpolation through the first two nodes only']),
        ('the reading over levels', ['the domain layer without its exceptional levels', 'the superseded rule over levels, a condition that changes with the level read as NOT ABSORBED',
                                     'one global floor, c_s^2 > 1/5 on every domain', 'no upper end on c_s^2',
                                     'the reading over levels with the shift set to zero where (13b) does not fix it']),
        ('the computed-levels fallback', ['the superseded weakest-grade rule for the computed levels']),
        ('the per-level reading', ['the per-level reading keeping every law not proved inadmissible',
                                   'the per-level reading with the shift set to zero where (13b) does not fix it']),
        ('the degree bound', ['the degree bound at 6']),
        ('the fail-closed certification', ['certification that ignores a disagreement']),
        ('the multiplicities', ['the Molien count without its factor n + 1']),
        ('integrability, H-ANISO', ['the H-ANISO charge with the sign of the second connection term flipped']),
        ('the homogeneous trace', ['a second-order trace that is not homogeneous']),
        ('the fast average', ['the fast average with its Beta exponent shifted by two']),
        ('integrability, I-V', ['the I-V shift-free charge against a field that is not Killing, sin chi cos chi d_chi']),
        ('integrability, I-S first order', ['the I-S first-order constraint with E = +psi']),
    ]
    assert all(a in arms for _, names in cover for a in names) and {a for _, names in cover for a in names} == set(arms), 'every arm maps to a check'
    out.append('every check and the arms that cover it:')
    out += [f'       {check}: ' + '; '.join(names) for check, names in cover]
    out.append('terms-to-instrument map:')
    out += [f'       {term}: {path}' for term, path in TERMS]
    out.append('ALL PASS' if parents and all(arms.values()) else 'SOME FAIL')
    out.append(f"qualification only: no I-S grade is computed (python {sys.version.split()[0]}, sympy {sp.__version__}, hash seed {os.environ.get('PYTHONHASHSEED')})")
    return '\n'.join(out)

if __name__ == '__main__':
    if os.environ.get('PYTHONHASHSEED') != '0':           # pin the hash seed: sympy's internal orderings, and with them its
        os.environ['PYTHONHASHSEED'] = '0'                 # paths and their cost, then repeat exactly from run to run
        os.execv(sys.executable, [sys.executable, os.path.abspath(__file__)] + sys.argv[1:])
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='mode')
    r = sub.add_parser('run')
    r.add_argument('--registration-commit', required=True)
    r.add_argument('--page-sha256', required=True)
    a = ap.parse_args()
    if a.mode == 'run':
        gate = run_gate(a.registration_commit, a.page_sha256)
        print(gate)
        if not gate['pass']:
            sys.exit('the run gate failed: nothing is graded')
        rec = run(gate)
        print('recorded: run.json,', rec['seconds'], 's')
        sys.exit(0)
    print(qualify())
