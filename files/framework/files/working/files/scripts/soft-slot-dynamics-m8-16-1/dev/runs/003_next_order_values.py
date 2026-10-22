#!/usr/bin/env python3
"""M8.16.1's pinned next-order values (development, off the instrument): Proposition N's coefficient c_g(N) for every
slow group of every case the next-order bar reads, at each cutoff N = 16, 24 and 32, with the C3 ray's c_g°(N), the
prediction with the off-ray part left out. The Soft-Slot Branches, section III, Proposition N; M8.16.1's terms,
THE NEXT-ORDER BAR and FROZEN VALUES: WHAT IS NEW.

  python3 -I -B next_order_values.py MIT_REPO OUT_JSON

MIT_REPO: a checkout whose scripts/soft-slot-branches/ holds the landed next_order_check.py and the files it imports,
used unchanged; the record lists every module loaded from it, and the data file read, with their SHA-256. Nothing here touches M8.16's instrument: no case is solved on it, and every
value, the sealed cases' included, comes from the reduced quartic alone.

The cases: the pyramid P5, the census rows T1 to T4 in R4 and R5 and T5 in R2, T5's second member T5J, and the C3 ray
C3R in R4. At each cutoff the formula keeps exactly the channels at or below it: at N = 16 that removes level 18 in R4
and R5 and levels 17 and 19 in R2 (check vi), and at N = 24 and 32 none; each cutoff is computed on its own.

The algebraic cases are exact up to the eigenvalue step, at 50 digits, as in the landed check: exact_case gives D_u, with
the germ's shift solved in the Krylov space of the gradient, and first_order gives c_g, reading each group at its member
in the closed first quadrant (+i tau for an imaginary pair). T4, whose representative is the interval-certified point,
comes from the landed check's model at 50 digits: the germ by Newton at eps = 1e-4, 2e-4 and 4e-4, then the quadratic
extrapolation of the reduced pencil's eigenvalues.

Checks, each of which must hold, or the exit status is 1:
  A  each case's leading order: Q, k and the zero multiplicity k + r_u (exact at the algebraic cases), and its slow
     spectrum against the frozen tau, with the multiplicities and the Krein signs of the imaginary groups; at the C3
     ray, whose tau this script freezes, the spectrum's structure against the terms' type: one quartet, one
     Krein-negative pair and one Krein-positive pair, by ascending |s|
  B  check i: exact at the algebraic cases, D_u X y0 = -kappa^-1 M_u X y1 for every generator X, with z solved and the
     split into five parts exact; at T4, the Hessian at the model's germ annihilates every orbit tangent at 50 digits,
     at each eps, the identity that check i states to first order
  C  every multiple group's correction is a multiple of the identity on its eigenspace
  D  the values at N = 24 and 32, computed apart, coincide
  E  the channels removed at N = 16 are exactly check vi's, and none is removed at 24 or 32
  F  the pyramid's c_g/(kappa s_g) reproduce claim F's printed values, at N = 24 and 32 and at N = 16
Mutation arms, each of which must turn its check red: N = 16 without its channels removed (F); R4 with s = 2/7 at T1/R4
(A); the C3 ray's structure read against its Krein signs swapped (A); the germ's shift dropped at P5 (B); and T4's germ
moved off the critical point along a normal direction (B).
"""
import hashlib
import json
import platform
import re
import sys
from pathlib import Path

REPO, OUT = Path(sys.argv[1]), Path(sys.argv[2])
SB = REPO / 'files/framework/files/working/files/scripts/soft-slot-branches'
NO = SB / 'next-order'
sys.argv = [str(NO / 'next_order_check.py'), str(NO / 'comparison_data.json'), '/dev/null']
sys.path.insert(0, str(NO))
import next_order_check as nc  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from sympy import I, Rational as R, sqrt  # noqa: E402

so, canon, bc = nc.so, nc.canon, nc.so.bc
mp.mp.dps = 50
CUTOFFS = (16, 24, 32)
SLOTFACTOR = {'R4': R(1), 'R5': R(9, 16), 'R2': R(1)}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# ---------------------------------------------------------------- the cases and their frozen leading order
def taus_sq(*fr):
    return [sqrt(f) for f in fr]


def quad_roots(a, b, c):
    """tau with tau^2 = -nu at the two roots of a nu^2 + b nu + c, both negative."""
    nu = sp.symbols('nu')
    rts = sp.solve(a * nu ** 2 + b * nu + c, nu)
    assert len(rts) == 2 and all(sp.N(r) < 0 for r in rts)
    return [sqrt(-r) for r in rts]


# frozen: a list of (tau or complex tau, multiplicity, Krein sign or None, exact?) in R4's normalization (M8.16's terms,
# FROZEN VALUES; T5J from its slow polynomial, t5_second_member.md); under: whether each group is under the bar
P5_FROZEN = [(mp.mpf('0.0622348691'), 1, -1, False), (mp.mpc('0.0417352860', '0.0609168609'), 1, None, False),
             (mp.mpf('1.0951854883'), 1, +1, False)]
T1_FROZEN = [(R(56, 1287), 1, -1, True)] + [(t, 1, +1, True) for t in (R(112, 143), R(112, 117), R(224, 143), R(560, 429))]
T2_FROZEN = [(taus_sq(R(5770240, 7913763))[0], 1, +1, True), (taus_sq(R(19066880, 278420571))[0], 2, +1, True)]
T3_FROZEN = [(taus_sq(R(90160, 61347))[0], 1, -1, True), (taus_sq(R(501760, 552123))[0], 2, -1, True)]
T5_FROZEN = [(t, 1, -1, True) for t in taus_sq(R(153664, 20449)) + quad_roots(418161601, 6989958976, 28677390336)]
T5J_FROZEN = [(t, 1, -1, True) for t in taus_sq(R(15680, 1859)) + quad_roots(418161601, 6605190592, 25491013632)]
T4_FROZEN = [(mp.mpf('1.01209160489'), 1, +1, False)] + [(mp.mpf(t), 1, -1, False) for t in ('0.310692742362', '0.139251832964', '0.00573685922309')]
T4_Q = {'R4': mp.mpf('1.185203461338846'), 'R5': mp.mpf('1.104176947003101')}

ALGEBRAIC = [  # name, slot, representative (orthonormal Condon-Shortley components, unnormalized), Q, k, k + r_u, frozen
    ('P5', 'R4', {3: 2 * sqrt(3) / 5, -2: sqrt(13) / 5}, R(77, 65), 4, 6, P5_FROZEN),
    ('T1/R4', 'R4', {2: 1}, R(147, 143), 3, 4, T1_FROZEN),
    ('T1/R5', 'R5', {2: 1}, R(581, 572), 3, 4, T1_FROZEN),
    ('T2/R4', 'R4', {3: 1, 0: sqrt(R(23, 10)), -3: 1}, R(5831, 5031), 4, 8, T2_FROZEN),
    ('T2/R5', 'R5', {3: 1, 0: sqrt(R(23, 10)), -3: 1}, R(609, 559), 4, 8, T2_FROZEN),
    ('T3/R4', 'R4', {3: 1, -3: 1}, R(1750, 1287), 4, 8, T3_FROZEN),
    ('T3/R5', 'R5', {3: 1, -3: 1}, R(2751, 2288), 4, 8, T3_FROZEN),
    ('T5/R2', 'R2', {R(7, 2): sqrt(R(3, 10)), R(-3, 2): sqrt(R(7, 10))}, R(22, 13), 6, 10, T5_FROZEN),
    ('T5J/R2', 'R2', {R(7, 2): sqrt(R(3, 20)), R(3, 2): I * sqrt(R(7, 20)), R(-3, 2): sqrt(R(7, 20)), R(-7, 2): -I * sqrt(R(3, 20))},
     R(22, 13), 6, 10, T5J_FROZEN),
    ('C3R/R4', 'R4', {2: 1, -1: 2}, R(77, 65), 4, 6, None),
]
UNDER = {'P5': lambda g: g['cls'] != 'imag' or g['krein'] == '+'}       # the pyramid: the quartet and the Krein+ pair
STRUCT = {'C3R/R4': [('complex', 1, None), ('imag', 1, '-'), ('imag', 1, '+')]}   # the terms' type, by ascending |s|


def structure_ok(groups, spec):
    return [(g['cls'], g['mult'], g['krein']) for g in sorted(groups, key=lambda g: abs(g['s']))] == spec


# ---------------------------------------------------------------- exact path
def unit(j, d):
    y = nc.ket(j, d)
    nrm = sqrt(sum(sp.expand(c * sp.conjugate(c)) for c in y))
    return [canon(c / nrm) for c in y]


def channels(slot):
    j, s, K = so.SLOTS[slot]
    return sorted(int(2 * J) for J in so.levels(j) if int(2 * J) != K and so.tJ(j, s, J, True) != 0)


def drop_for(slot, N):
    return tuple(L for L in channels(slot) if L > N)


def krylov_fixed(slot, u, drop, s_override=None):
    """The germ's shift directions: an exact orthonormal basis, beside u, of the Krylov space of the gradient's part off
    u under Mhat, which holds the solution of Mhat z = grad R~0(u) on the normal space (the bench's rows script)."""
    ex = nc.exact_case(slot, u, [], drop=drop, s_override=s_override)
    N, n = ex['N'], ex['n']
    g = sp.Matrix(ex['grad'])
    uc = nc.rcol(u)
    goff = (g - (uc.T * g)[0] * uc).applyfunc(canon)
    if goff == sp.zeros(N, 1):
        return []
    basis, v = [], goff
    for _ in range(N):
        for b in basis:
            v = (v - (b.T * v)[0] * b).applyfunc(canon)
        v = (v - (uc.T * v)[0] * uc).applyfunc(canon)
        nv2 = canon((v.T * v)[0])
        if nv2 == 0:
            break
        b = (v / sqrt(nv2)).applyfunc(canon)
        basis.append(b)
        v = (ex['Mh'] * b).applyfunc(canon)
    return [nc.cvec(b, n) for b in basis]


def classify(s):
    return 'imag' if abs(mp.re(s)) < mp.mpf('1e-30') * abs(s) else 'real' if abs(mp.im(s)) < mp.mpf('1e-30') * abs(s) else 'complex'


def leading_check(name, slot, groups, frozen):
    """A's spectrum part: each frozen group matched by s = slot factor x tau, with multiplicity and Krein sign."""
    if frozen is None:
        return True, []
    fac = mp.mpf(sp.N(SLOTFACTOR[slot], 60))
    ok, lines = len(groups) == len(frozen), []
    for tau, mult, sign, exact in frozen:
        tv = (mp.mpf(sp.N(tau, 60)) if not isinstance(tau, (mp.mpf, mp.mpc)) else tau) * fac
        target = tv * 1j if not isinstance(tv, mp.mpc) else tv
        best = min(groups, key=lambda g: abs(g['s'] - target))
        tol = mp.mpf('1e-40') if exact else mp.mpf('1e-9')
        m = abs(best['s'] - target) < tol * max(1, abs(target)) and best['mult'] == mult
        if sign is not None:
            m &= best['krein'] == ('+' if sign > 0 else '-')
        ok &= m
        lines.append('%s s = %s, frozen %s x %s, mult %d%s: %s' % (name, nc.fmt(best['s'], 12), sp.sstr(SLOTFACTOR[slot]),
                     nc.fmt(target / fac, 12), mult, '' if sign is None else ', Krein %+d' % sign, 'ok' if m else 'MISMATCH'))
    return ok, lines


def algebraic_case(name, slot, rep, Qt, kt, zt, frozen, N, drop=None, s_override=None, shift='full'):
    j = so.SLOTS[slot][0]
    u = unit(j, rep)
    drop = drop_for(slot, N) if drop is None else drop
    fixed = krylov_fixed(slot, u, drop, s_override)
    ex = nc.exact_case(slot, u, fixed, drop=drop, s_override=s_override, shift=shift)
    ld = nc.leading(ex)
    fo = nc.first_order(ex, ld)
    Sx = (bc.J0(int(2 * j)) * ex['Mh']).applyfunc(canon)
    cof, zex = bc.strip_zero(bc.charpoly(Sx, bc.MU))
    kap = ld['kap']
    groups = []
    for g, f in zip(ld['groups'], fo):
        cls = classify(g['s'])
        krein = None
        if cls == 'imag':
            krein = '+' if all(q > 0 for q in g['krein']) else '-' if all(q < 0 for q in g['krein']) else 'mixed'
        cg = f['c'][0]
        groups.append(dict(s=g['s'], mu0=g['mu0'], mult=g['mult'], cls=cls, krein=krein, c=cg, rel=cg / g['mu0'],
                           cond=f['cond'], scalar=f['scalar'], all_c=f['c']))
    okA_struct = ex['Q'] == Qt and ex['k'] == kt and zex == zt and cof.eval(0) != 0
    okA_spec, lines = leading_check(name, slot, groups, frozen)
    if name in STRUCT:
        st = structure_ok(groups, STRUCT[name])
        okA_spec &= st
        lines.append('%s structure, by ascending |s|: %s: %s' % (name, [(g['cls'], g['mult'], g['krein']) for g in sorted(groups, key=lambda g: abs(g['s']))],
                     'ok' if st else 'MISMATCH'))
    okB = ex['in_fixed'] and ex['closed'] and ex['solved'] and all(c for _, c in ex['check_i']) and bool(ex['split'])
    okC = all(g['scalar'] for g in groups if g['mult'] > 1)
    off = None
    if name.startswith('C3R'):
        Du0 = (ex['Du'] - ex['Off']).applyfunc(canon)
        off = [f['c'][0] for f in nc.first_order(ex, ld, Du=nc.tomp(Du0))]
    return dict(groups=groups, off=off, drop=list(drop), Q=ex['Q'], k=ex['k'], zeros=zex, fixed=len(fixed),
                okA=okA_struct and okA_spec, okA_lines=lines, okB=okB, okC=okC, kap=kap)


# ---------------------------------------------------------------- T4, by the model
def t4_point():
    xt = [mp.mpf(s_) for s_ in bc.OUTSIDE]
    n = 7
    M = so.ms(sp.Integer(3))
    w = [mp.sqrt(mp.mpf(int(bc.weight(6, m)))) for m in M]
    uc = [mp.mpc(xt[a], xt[n + a]) * w[a] for a in range(n)]
    nrm = mp.sqrt(sum(abs(c) ** 2 for c in uc))
    return [c / nrm for c in uc]


def t4_model(slot, uc, N):
    j, s, K = so.SLOTS[slot]
    n = int(2 * j) + 1
    NN = 2 * n
    drop = drop_for(slot, N)
    md = nc.Model.__new__(nc.Model)
    md.ctx = so.mp_setup(j)
    md.n, md.N = n, NN
    md.B = so.mp_basis(n)
    md.beta = mp.mpf(sp.N((2 * j + 1) * (1 - s) / (13 * s), 60))
    md.Ys = {(a, b): [x + y for x, y in zip(so.mp_Y(md.ctx, md.B[a], md.B[b]), so.mp_Y(md.ctx, md.B[b], md.B[a]))]
             for a in range(NN) for b in range(a, NN)}
    md.levels = []
    for J in so.levels(j):
        t = so.tJ(j, s, J)
        L = int(2 * J)
        if L == K or t == 0 or L in drop:
            continue
        wgt = t / ((2 * J + 1) * s ** 3 * (L * (L + 2) - K * (K + 2)))
        md.levels.append((so.mp_table(j, J), mp.mpf(sp.N(wgt, 60))))
    md.u = mp.matrix([mp.re(c) for c in uc] + [mp.im(c) for c in uc])
    md.J = nc.Jmat(n)
    md.w0 = mp.sqrt(K * (K + 2))
    Hh, HR = md.hessians(md.u)
    md.Q = (md.u.T * Hh * md.u)[0] / 12
    spins = [mp.matrix([[mp.mpc(sp.N(Ja[a, b], 60)) for b in range(n)] for a in range(n)]) for Ja in nc.spin(j)]

    def tangents(x):
        y = mp.matrix([mp.mpc(x[a], x[n + a]) for a in range(n)])
        out = []
        for v in [y * 1j] + [-1j * (Ja * y) for Ja in spins]:
            out.append(mp.matrix([mp.re(v[a]) for a in range(n)] + [mp.im(v[a]) for a in range(n)]))
        return out
    Kc = mp.matrix(NN, 4)
    for b, g in enumerate(tangents(md.u)):
        for a in range(NN):
            Kc[a, b] = g[a]
    U, S, V = mp.svd_r(Kc.T, full_matrices=True)
    k = sum(1 for x in S if abs(x) > mp.mpf('1e-30'))
    cols = [V[i, :].T for i in range(NN) if i >= len(S) or abs(S[i]) < mp.mpf('1e-30')]
    md.Nb = mp.matrix(NN, len(cols))
    for b, c in enumerate(cols):
        for a in range(NN):
            md.Nb[a, b] = c[a]
    return md, Hh, k, tangents, drop


def t4_case(name, slot, uc, N, perturb=False):
    md, Hh, k, tangents, drop = t4_model(slot, uc, N)
    NN = md.N
    Mh = Hh - 4 * md.Q * mp.eye(NN)
    crit = mp.norm(Hh * md.u / 3 - 4 * md.Q * md.u)
    kap = 1 / (8 * md.w0 * md.Q)
    T0 = kap * md.J * Mh
    E, Rv = mp.eig(T0, left=False, right=True)
    zeros = sum(1 for e in E if abs(e) < mp.mpf('1e-15'))
    groups = []
    for i, e in enumerate(E):
        if abs(e) >= mp.mpf('1e-15') and mp.re(e) > -mp.mpf('1e-20') * abs(e) and mp.im(e) > -mp.mpf('1e-20') * abs(e):
            r = Rv[:, i]
            re_, im_ = mp.matrix([mp.re(x) for x in r]), mp.matrix([mp.im(x) for x in r])
            q = (re_.T * Mh * re_)[0] + (im_.T * Mh * im_)[0]
            cls = classify(e / kap)
            groups.append(dict(s=e / kap, mu0=e, mult=1, cls=cls, krein=('+' if q > 0 else '-') if cls == 'imag' else None))
    groups.sort(key=lambda g: abs(g['mu0']))
    epss = [mp.mpf('1e-4'), mp.mpf('2e-4'), mp.mpf('4e-4')]
    hs = [[] for _ in groups]
    worst_grad, worst_ann = mp.mpf(0), mp.mpf(0)
    for eps in epss:
        x, Hf, gnorm = md.germ(eps)
        if perturb:
            x = x + mp.mpf('1e-12') * md.Nb[:, 0]
            Hh2, HR2 = md.hessians(x)
            Hf = Hh2 / 2 - 2 * mp.eye(NN) + eps * HR2
        worst_grad = max(worst_grad, gnorm)
        hn = nc.norm2(Hf)
        for t in tangents(x):
            worst_ann = max(worst_ann, mp.norm(Hf * t) / (hn * mp.norm(t)))
        we = mp.sqrt(md.w0 ** 2 + eps)
        C = mp.zeros(2 * NN)
        for a in range(NN):
            C[a, NN + a] = 1
        low = -(eps / 2) * Hf
        for a in range(NN):
            for b in range(NN):
                C[NN + a, b] = low[a, b]
                C[NN + a, NN + b] = -2 * we * md.J[a, b]
        ev = mp.eig(C, left=False, right=False)
        for gi, g in enumerate(groups):
            lam = min(ev, key=lambda z: abs(z - eps * g['mu0']))
            hs[gi].append((lam / eps - g['mu0']) / eps)
    e1, e2, e3 = epss
    for gi, g in enumerate(groups):
        h = hs[gi]
        c = (h[0] * e2 * e3 / ((e1 - e2) * (e1 - e3)) + h[1] * e1 * e3 / ((e2 - e1) * (e2 - e3))
             + h[2] * e1 * e2 / ((e3 - e1) * (e3 - e2)))
        g.update(c=c, rel=c / g['mu0'], cond=None, scalar=True)
    okA_struct = abs(md.Q - T4_Q[slot]) < mp.mpf('1e-14') and k == 4 and zeros == 6 and crit < mp.mpf('1e-40')
    okA_spec, lines = leading_check(name, slot, groups, T4_FROZEN)
    okB = worst_ann < mp.mpf('1e-40') and worst_grad < mp.mpf('1e-40')
    return dict(groups=groups, off=None, drop=list(drop), Q=md.Q, k=k, zeros=zeros, fixed=None, okA=okA_struct and okA_spec,
                okA_lines=lines, okB=okB, okC=True, kap=kap, annihilation=worst_ann, germ_gradient=worst_grad, criticality=crit)


# ---------------------------------------------------------------- claim F's printed pyramid values
def claim_f_p5():
    txt = (NO / 'next_order_check.out').read_text(encoding='utf-8')
    out = {}
    for N, gi, val in re.findall(r'^\s+P5\s+N = (\d+), group (\d+) \([^)]*\): c_g/\(kappa s\) = (\([^)]*\)|[-0-9.e]+);', txt, re.M):
        out[(int(N), int(gi))] = val
    assert sorted(out) == [(N, g) for N in (16, 24, 32) for g in (1, 2, 3)], sorted(out)
    return out


def p5_reproduces(res_by_N, printed):
    ok, lines = True, []
    for N in (16, 24, 32):
        for gi, g in enumerate(res_by_N[N]['groups'], 1):
            mine = nc.fmt(g['rel'], 7)
            want = printed[(N, gi)].strip('()').replace('j', 'j').replace(' ', '')
            m = mine.replace(' ', '').strip('()') == want
            ok &= m
            lines.append('P5 N = %d group %d: %s against claim F %s: %s' % (N, gi, mine, printed[(N, gi)], 'ok' if m else 'DIFFERS'))
    return ok, lines


# ---------------------------------------------------------------- the run
def s(x, d=25):
    x = mp.mpc(x)
    return [mp.nstr(mp.re(x), d), mp.nstr(mp.im(x), d)]


def main():
    failed = []
    me = Path(__file__).resolve()
    root = REPO.resolve()
    loaded = sorted({Path(m.__file__).resolve() for m in list(sys.modules.values())
                     if getattr(m, '__file__', None) and Path(m.__file__).resolve().is_relative_to(root)})
    read = [(NO / 'next_order_check.out').resolve()]                      # claim F's printed values (check F)
    imports = {str(p.relative_to(root)): sha(p) for p in loaded + read}    # every module loaded from MIT, and the data read
    assert len(loaded) == 4, loaded
    record = dict(script=dict(path='run/next_order_values.py', sha256=sha(me)), imports=imports,
                  environment=dict(python=platform.python_version(), sympy=sp.__version__, mpmath=mp.__version__, dps=mp.mp.dps),
                  cutoffs=list(CUTOFFS), cases={}, checks={}, arms={})
    print('M8.16.1: the pinned next-order values, by case, group and cutoff (development, off the instrument)')
    print('imports: ' + '; '.join('%s %s' % (k, v[:12]) for k, v in imports.items()))
    okE = all(drop_for(sl, 16) == nc.DROP16[sl] and drop_for(sl, 24) == () and drop_for(sl, 32) == () for sl in ('R4', 'R5', 'R2'))
    print('E  channels: %s; removed at N = 16: %s; at 24 and 32: none: %s' % (
        {sl: channels(sl) for sl in ('R4', 'R5', 'R2')}, {sl: drop_for(sl, 16) for sl in ('R4', 'R5', 'R2')}, 'PASS' if okE else 'FAIL'))
    if not okE:
        failed.append('E')
    results = {}
    for name, slot, rep, Qt, kt, zt, frozen in ALGEBRAIC:
        results[name] = {N: algebraic_case(name, slot, rep, Qt, kt, zt, frozen, N) for N in CUTOFFS}
        print('%s done' % name, flush=True)
    uc = t4_point()
    for slot in ('R4', 'R5'):
        name = 'T4/' + slot
        results[name] = {N: t4_case(name, slot, uc, N) for N in CUTOFFS}
        print('%s done' % name, flush=True)
    printed = claim_f_p5()
    okF, flines = p5_reproduces(results['P5'], printed)
    for name, byN in results.items():
        okA = all(r['okA'] for r in byN.values())
        okB = all(r['okB'] for r in byN.values())
        okC = all(r['okC'] for r in byN.values())
        okD = all(len(byN[24]['groups']) == len(byN[32]['groups']) and all(
            a['c'] == b['c'] for a, b in zip(byN[24]['groups'], byN[32]['groups'])) for _ in [0])
        if byN[24]['off'] is not None:
            okD &= byN[24]['off'] == byN[32]['off']
        for tag, ok in (('A', okA), ('B', okB), ('C', okC), ('D', okD)):
            if not ok:
                failed.append('%s %s' % (tag, name))
        r16 = byN[16]
        print('%s: Q = %s, k = %d, zero multiplicity %d, fixed directions off the ray %s; A %s, B %s, C %s, D %s'
              % (name, r16['Q'] if not isinstance(r16['Q'], mp.mpf) else mp.nstr(r16['Q'], 16), r16['k'], r16['zeros'], r16['fixed'],
                 *['PASS' if x else 'FAIL' for x in (okA, okB, okC, okD)]))
        for line in byN[24]['okA_lines']:
            print('   ' + line)
        if name.startswith('T4'):
            print('   check i at 50 digits: the Hessian at the germ annihilates every orbit tangent to %s, the germ\'s gradient %s'
                  % (mp.nstr(max(r['annihilation'] for r in byN.values()), 3), mp.nstr(max(r['germ_gradient'] for r in byN.values()), 3)))
        under = UNDER.get(name, lambda g: True)
        cases = {}
        for N in CUTOFFS:
            rr = byN[N]
            cases[str(N)] = dict(dropped=rr['drop'], groups=[dict(
                s=s(g['s']), mult=g['mult'], cls=g['cls'], krein=g['krein'], kappa_s=s(g['mu0']), c_g=s(g['c']),
                c_over_kappa_s=s(g['rel']), cond=None if g['cond'] is None else mp.nstr(g['cond'], 6), scalar=bool(g['scalar']),
                under_bar=bool(under(g)), c_g_without_off_ray=None if rr['off'] is None else s(rr['off'][gi]),
                c_without_off_ray_over_kappa_s=None if rr['off'] is None else s(rr['off'][gi] / g['mu0']))
                for gi, g in enumerate(rr['groups'])])
            print('   N = %d (removed %s): %s' % (N, rr['drop'] or 'none', '; '.join(
                '%s%s: %s%s' % (nc.fmt(g['s'], 8), '' if g['mult'] == 1 else ' (x%d)' % g['mult'], nc.fmt(g['rel'], 8),
                                '' if rr['off'] is None else ', without the off-ray part ' + nc.fmt(rr['off'][gi] / g['mu0'], 8))
                for gi, g in enumerate(rr['groups']))))
        record['cases'][name] = dict(slot=name.split('/')[-1] if '/' in name else 'R4', Q=str(r16['Q']) if not isinstance(r16['Q'], mp.mpf)
                                     else mp.nstr(r16['Q'], 30), k=r16['k'], zero_multiplicity=r16['zeros'], cutoffs=cases,
                                     checks=dict(A=okA, B=okB, C=okC, D=okD))
    print('F  the pyramid against claim F\'s printed values: %s' % ('PASS' if okF else 'FAIL'))
    for line in flines:
        print('   ' + line)
    if not okF:
        failed.append('F')
    record['checks'] = dict(E=okE, F=okF, failed=failed)

    # ------------------------------------------------ the arms
    print('arms, each of which must turn its check red:')
    a1 = {N: algebraic_case(*ALGEBRAIC[0], N, drop=() if N == 16 else None) for N in CUTOFFS}
    red1 = not p5_reproduces(a1, printed)[0]
    a2 = algebraic_case(*ALGEBRAIC[1], 24, s_override=R(2, 7))
    red2 = not a2['okA']
    a3 = algebraic_case(*ALGEBRAIC[0], 24, shift='none')
    red3 = not a3['okB']
    a4 = t4_case('T4/R4', 'R4', uc, 24, perturb=True)
    red4 = not a4['okB']
    swapped = [(c, m, {'-': '+', '+': '-'}.get(k, k)) for c, m, k in STRUCT['C3R/R4']]
    red5 = not structure_ok(results['C3R/R4'][24]['groups'], swapped)
    for label, red in (('N = 16 without its channels removed (F)', red1), ('R4 with s = 2/7 at T1/R4 (A)', red2),
                       ('the germ\'s shift dropped at P5 (B)', red3), ('T4/R4\'s germ moved off the critical point (B)', red4),
                       ('the C3 ray read against its Krein signs swapped (A)', red5)):
        print('   arm: %s: %s' % (label, 'RED' if red else 'GREEN'))
        record['arms'][label] = 'RED' if red else 'GREEN'
        if not red:
            failed.append('arm ' + label)
    OUT.write_text(json.dumps(record, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('wrote %s, SHA-256 %s' % (OUT.name, sha(OUT)))
    print('ALL CHECKS PASS; every arm red' if not failed else 'FAILED: ' + ', '.join(failed))
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
