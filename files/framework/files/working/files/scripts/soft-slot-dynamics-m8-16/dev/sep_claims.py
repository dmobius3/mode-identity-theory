#!/usr/bin/env python3
"""The separation rule's claims (SEPARATION_PLAN.md, Step 2, with the units' rulings of 2026-10-17). Case: synthetic.
The rule is instrument/convergence.py. Every outcome is derived before the run from exact roots, and printed first.

The families are the scout's ladders in N (dev/sep_scout.py, entry 149): four cutoffs, N = 16 to 40, and a limit, on
dl_recal.py's Elliptic family at m = 0.2, mixed by one random unitary per ladder, 10 mixings each. Added here:
  N (UA), non-contracting: UB's collision block with delta stepped geometrically at 0.95 a step, from a separation of
     1e-3 at N = 40 to a quartet with real part 1e-3 in the limit; its roots accelerate into the collision, so d2 > d1,
     above the floor. Elliptic at every cutoff, Hyperbolic in the limit.
  K' (UB), the partner: two modes joined by a weak conjugate coupling c = 1e-4 (Re-Re +c, Im-Im -c), an S1- mode whose
     Krein-negative slow pair sits at 1e-2, and an S1+ mode whose Krein-positive slow pair converges onto it, 1e-3 above
     at N = 40 (stepping by 3, which keeps each match unique against the oscillator at 0.0357), to a quartet with real part 7.1e-6 in the limit. The band edge is declared at
     2 (1e-2 + 1e-4), so the positive pair lies above half of it and only the partner rule tests it. Elliptic at every
     cutoff, Hyperbolic in the limit.
  M (UA, UB), the harmless permutation: two decoupled Krein-positive slow pairs near 0.15 that exchange order between
     cutoffs, so no unique match exists; as one set they converge far from every event. Elliptic throughout.
  M' (UB), the dangerous approach: K' 's coupled pair with a second, decoupled Krein-positive pair, the two positive
     pairs about a fixed centre, the lower converging onto the Krein-negative pair. As one set they do not contract;
     read at their centroid they would not move. Elliptic at every cutoff, Hyperbolic in the limit.
  In M and M', each S1+ block's fast pair sits at exactly 2 omega + f, so the fast pairs form a mirror set with the
  same steps, about 14 from zero: converged in M, non-contracting in M', fixed at its centroid in both.
  F15, reported (UB): F with its pair at 15 margins, the rule's stated limit.
  R2, reported (UB): R read from its two highest cutoffs, the same limit.

Claims:
  1. The analytic projector (UA). convergence.projector against ||P|| in closed form: (1 + k)/(2 sqrt k) for the
     oscillator x'' + k x = 0 and for the real pair x'' - k x = 0 at k = 4; (1 + s^2 k)/(2 s sqrt k) for the oscillator
     under the scaling diag(1, s), s = 10; and (1 + k)/(2 sqrt k) for the doubled oscillator's group of two. Each within
     1e-12 relative, with the pairing (the left vectors' residual), the conditioning and the normalization passing. At
     UB's exact Krein collision, the defective group's projector is not usable; and a converged point whose tested group
     is marked not usable reads Unresolved, naming it.
  2. P, P', PK and M: converged, with their types, at every mixing.
  3. Z, K, X, R, F, N, K' and M': Unresolved at every mixing, never converged.
  4. The arms, each red: under it, a designated counterexample reads converged with its finite-N type, which its limit
     does not have, at some mixing:
     (a) a factor of 1: R and F;
     (b) the last change for the remaining error: R;
     (c) no floor, dropped from U, with the margin kept as the non-contraction threshold: F;
     (d) no gray-zone event: Z and F;
     (e) no axis event: X;
     (f) no Krein event: K and R;
     (g) no numerical estimate, at the module (UB): P's summaries with the tested pair's ||P_g|| set so that
         ||P_g|| u ||A|| is a fifth of its distance: Unresolved with the estimate, converged without it;
     (h) the partner untested: K';
     (i) non-contraction ignored (read by the last change): N;
     (j) a set's change read at its centroid (UB): M'.
Reported, unscored: F15 and R2, converged with their finite-N types (the stated limit); each tested group's U and d.
"""
import os
import sys
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from instrument import linear as ln, convergence as cv, devtools  # noqa: E402
import dl_recal as d  # noqa: E402
import sep_scout as sc  # noqa: E402

devtools.require('synthetic')
d.rng = np.random.default_rng(20261025)
mp.mp.dps = 50
OMEGA, M, N_MIX, C_K = 7.0, 0.2, 10, mp.mpf('1e-4')
FM = mp.mpf('1e-2')
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


# ---- the families' systems: (L unmixed, omega) at the four cutoffs and in the limit ----

def from_blocks(f):
    return dict(f, sys=[(d.place(b), w) for b, w in f['sys']])


def family_N():
    dk, dx = sc.delta_for_sep(mp.mpf('1e-3')), sc.delta_for_re(mp.mpf('1e-3'))
    rho = mp.mpf('0.95')
    c = (dk - dx) / rho ** 3
    dl = [dx + c * rho ** j for j in range(4)] + [dx]
    sysm = [(d.place(d.elliptic_blocks([np.diag([-float(sc.A_C), -2 * float(sc.A_C)])])), float(mp.sqrt(sc.W2S + x)))
            for x in dl]
    return dict(sys=sysm, lam=[sc.coll_roots(x)[-1] for x in dl], fin='Elliptic', lim='Hyperbolic', dl=dl)


def family_F(k):
    m_ = mp.mpf(sc.MG)
    s3, s_inf = k * m_, 4 * m_
    k2 = 2 * OMEGA * s3
    sig_inf = -s_inf ** 2
    r1, r2 = mp.mpf(1) / 4, mp.mpf('0.999')
    a = 2 * s3 * mp.mpf('0.03') * m_ / (r1 ** 2 * (1 - r1))
    b = (s3 ** 2 - sig_inf - a * r1 ** 3) / r2 ** 3
    sig = [sig_inf + a * r1 ** j + b * r2 ** j for j in range(4)] + [sig_inf]
    sysm = [(d.place(d.elliptic_blocks([sc.soft_block(-x, k2)])), OMEGA) for x in sig]
    lam = [mp.mpc(0, mp.sqrt(x)) if x > 0 else mp.sqrt(-x) for x in sig]
    return dict(sys=sysm, lam=lam, fin='Elliptic', lim='Hyperbolic')


def kp_fp(j):
    return FM if j == 4 else FM + mp.mpf('1e-3') * mp.mpf(3) ** (3 - j)


def kp_L(fp, c=C_K, extra=()):
    kA, kB = 2 * OMEGA * FM - FM * FM, 2 * OMEGA * fp + fp * fp
    blocks = d.elliptic_blocks(list(extra) + [np.diag([-float(kA)] * 2), np.diag([float(kB)] * 2)])
    L = d.place(blocks)
    m = len(blocks)
    a, b = m - 2, m - 1
    L[a, b] = L[b, a] = float(c)
    L[m + a, m + b] = L[m + b, m + a] = -float(c)
    return L


def kp_roots(fp, c=C_K):
    """The two coupled modes' slow eigenvalues in the upper half plane, with their Krein values, at 50 digits."""
    kA, kB = 2 * OMEGA * FM - FM * FM, 2 * OMEGA * fp + fp * fp
    L = mp.matrix([[-kA, c, 0, 0], [c, kB, 0, 0], [0, 0, -kA, -c], [0, 0, -c, kB]])
    J = mp.matrix([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]])
    A, Bm = mp.zeros(8, 8), mp.zeros(8, 8)
    for i in range(4):
        A[i, 4 + i] = 1
        Bm[4 + i, 4 + i] = 1
        for k in range(4):
            A[4 + i, k] = -L[i, k]
            A[4 + i, 4 + k] = -2 * OMEGA * J[i, k]
            Bm[i, k] = L[i, k]
    E, ER = mp.eig(A)
    rows = [(E[t], mp.re((ER[:, t].H * Bm * ER[:, t])[0])) for t in range(8) if mp.im(E[t]) > 0 and abs(E[t]) < 0.2]
    return sorted(rows, key=lambda z: (mp.re(z[0]), mp.im(z[0])))


def family_Kp():
    sysm = [(kp_L(kp_fp(j)), OMEGA) for j in range(5)]
    seqs = [kp_roots(kp_fp(j)) for j in range(5)]
    neg = [min((z for z in s if z[1] < 0), key=lambda z: mp.im(z[0]))[0] for s in seqs[:4]]
    pos = [min((z for z in s if z[1] > 0), key=lambda z: mp.im(z[0]))[0] for s in seqs[:4]]
    lim = seqs[4]
    return dict(sys=sysm, neg=neg, pos=pos, lim_roots=[z[0] for z in lim], fin='Elliptic', lim='Hyperbolic',
                band=float(2 * (FM + mp.mpf('1e-4'))))


def s1p(f):
    """S1+ diag(k, k) with its slow pair at +-i f exactly."""
    return np.diag([float(f * f + 2 * OMEGA * f)] * 2)


def family_M():
    """M (UA, UB): two decoupled Krein-positive slow pairs that exchange order between cutoffs, f1 = 0.150 + 1e-3 3^(3-j)
    and f2 = 0.1502 - 1e-3 3^(3-j), converging far from every event. Elliptic at every cutoff and in the limit."""
    f1 = [mp.mpf('0.150') + mp.mpf('1e-3') * mp.mpf(3) ** (3 - j) for j in range(4)] + [mp.mpf('0.150')]
    f2 = [mp.mpf('0.1502') - mp.mpf('1e-3') * mp.mpf(3) ** (3 - j) for j in range(4)] + [mp.mpf('0.1502')]
    sysm = [(d.place(d.elliptic_blocks([s1p(a), s1p(b)])), OMEGA) for a, b in zip(f1, f2)]
    return dict(sys=sysm, sets=[[mp.mpc(0, a), mp.mpc(0, b)] for a, b in zip(f1, f2)], fin='Elliptic', lim='Elliptic')


def family_Mp():
    """M' (UB): K' 's coupled pair, its Krein-negative slow pair at 1e-2, with two Krein-positive slow pairs about a fixed
    centre c0 = 1e-2 + D: the lower, coupled, at c0 - D_j, converging onto the negative pair; the upper, decoupled, at
    c0 + D_j; D_j = D (0.01, 0.06, 0.2, 0.7), D = 1e-3 / 0.3, so the lower sits 1e-3 above it at N = 40. The pair
    exchanges candidates between cutoffs, so it forms a set. Elliptic at every cutoff, Hyperbolic in the limit."""
    D = mp.mpf('1e-3') / mp.mpf('0.3')
    c0 = FM + D
    Dj = [D * mp.mpf(x) for x in ('0.01', '0.06', '0.2', '0.7')] + [D]
    sysm = [(kp_L(c0 - x, extra=[s1p(c0 + x)]), OMEGA) for x in Dj]
    neg, sets = [], []
    for x in Dj[:4]:
        r_ = kp_roots(c0 - x)
        neg.append(min((z for z in r_ if z[1] < 0), key=lambda z: mp.im(z[0]))[0])
        pos = min((z for z in r_ if z[1] > 0), key=lambda z: mp.im(z[0]))[0]
        sets.append([pos, mp.mpc(0, c0 + x)])
    return dict(sys=sysm, neg=neg, sets=sets, fin='Elliptic', lim='Hyperbolic')


def families():
    F = {k: from_blocks(sc.family(k)) for k in ('P', "P'", 'PK', 'Z', 'K', 'X', 'R', 'F')}
    F['N'] = family_N()
    F["K'"] = family_Kp()
    F['M'] = family_M()
    F["M'"] = family_Mp()
    F['F15'] = family_F(15)
    F['R2'] = F['R']
    return F


# ---- the derivation, from exact roots: the binding group's numbers under the rule and each arm ----

def margins(f):
    return [cv_margin(*f['sys'][j]) for j in range(4)]


def cv_margin(L, w):
    return ln.margin(np.linalg.norm(ln.first_order(L, w)[0], 2), M)


def exact_rule(seq, dist_ev, floor, arms=(), cutoffs=3, partner=None):
    """The rule's arithmetic on an exact sequence (highest last) of the binding group, against its events; partner: a
    second exact sequence tested against the opposite-sign distance (UB)."""
    factor = 1.0 if 'factor_one' in arms else cv.FACTOR
    fl = 0 if 'no_floor' in arms else floor

    def unc(s):
        d2 = abs(s[-1] - s[-2])
        if cutoffs == 3 and 'last_change' not in arms:
            d1 = abs(s[-2] - s[-3])
            if d2 < d1:
                return max(d2 * d2 / (d1 - d2), fl), None
            if d2 > floor and 'contract_ignored' not in arms:
                return mp.inf, 'non-contracting'
        return max(d2, fl), None
    U_, why = unc(seq)
    ev = {k: v for k, v in dist_ev.items() if not (k == 'gray' and 'no_gray' in arms) and not (k == 'axis' and 'no_axis' in arms)
          and not (k == 'krein' and 'no_krein' in arms)}
    dmin = min(ev.values()) if ev else mp.inf
    ok = why is None and U_ <= factor * dmin
    if partner is not None and 'no_partner' not in arms:
        Up, whyp = unc(partner)
        ok = ok and whyp is None and Up <= factor * dist_ev['krein']
    return ok, U_, dmin


def exact_set_rule(sets, dist_ev, floor, arms=()):
    """The rule's arithmetic on an exact two-member set (highest cutoff last): its change between cutoffs is the
    bottleneck between the two pairs of members, written out here, or the centroid's under 'set_centroid'."""
    factor = 1.0 if 'factor_one' in arms else cv.FACTOR
    fl = 0 if 'no_floor' in arms else floor

    def step(A, B):
        if 'set_centroid' in arms:
            return abs((A[0] + A[1]) / 2 - (B[0] + B[1]) / 2)
        return min(max(abs(A[0] - B[0]), abs(A[1] - B[1])), max(abs(A[0] - B[1]), abs(A[1] - B[0])))
    d2, d1 = step(sets[3], sets[2]), step(sets[2], sets[1])
    if 'last_change' in arms:
        U_, why = max(d2, fl), None
    elif d2 < d1:
        U_, why = max(d2 * d2 / (d1 - d2), fl), None
    elif d2 > floor and 'contract_ignored' not in arms:
        U_, why = mp.inf, 'non-contracting'
    else:
        U_, why = max(d2, fl), None
    ev = {k: v for k, v in dist_ev.items() if not (k == 'gray' and 'no_gray' in arms) and not (k == 'krein' and 'no_krein' in arms)}
    dmin = min(ev.values()) if ev else mp.inf
    return why is None and U_ <= factor * dmin, U_, dmin


ARM_FAMILIES = [('a', 'factor_one', ('R', 'F')), ('b', 'last_change', ('R',)), ('c', 'no_floor', ('F',)),
                ('d', 'no_gray', ('Z', 'F')), ('e', 'no_axis', ('X',)), ('f', 'no_krein', ('K', 'R')),
                ('h', 'no_partner', ("K'",)), ('i', 'contract_ignored', ('N',)), ('j', 'set_centroid', ("M'",))]
SCORED = ('P', "P'", 'PK', 'M', 'Z', 'K', 'X', 'R', 'F', 'N', "K'", "M'")


def derive(F):
    """name -> (expected verdict under the full rule, {arm: verdict}), and the printed derivation."""
    D = {}
    for name in SCORED + ('F15', 'R2'):
        f = F[name]
        mg = margins(f)
        floor = max(mg[2], mg[3])
        gray = lambda z: abs(z) - ln.GRAY * mg[3]      # noqa: E731
        partner, cut = None, 2 if name == 'R2' else 3
        if name in ('M', "M'"):
            S = f['sets']
            ev = dict(gray=min(gray(z) for z in S[3]))
            if name == "M'":
                ev['krein'] = min(abs(z - f['neg'][3]) for z in S[3])
            ok, U_, dmin = exact_set_rule(S, ev, floor)
            arms = {a: exact_set_rule(S, ev, floor, arms=(a,))[0] for _, a, _ in ARM_FAMILIES}
            if name == "M'":            # the negative pair alone, nearly fixed: separated, so the set decides
                okn = exact_rule(f['neg'], dict(gray=gray(f['neg'][3]), krein=ev['krein']), floor)[0]
                ok, arms = ok and okn, {a: v and okn for a, v in arms.items()}
            D[name] = (('converged' if ok else 'Unresolved'), arms)
            say(f"  {name:4s} at the cutoffs {f['fin']}, in the limit {f['lim']}: the set U {mp.nstr(U_, 3)}, distance"
                f" {mp.nstr(dmin, 3)} ({min(ev, key=ev.get)}); under the rule {D[name][0]}; arms converging it: "
                f"{[a for a, v in arms.items() if v] or 'none'}")
            continue
        if name == "K'":
            seq, partner = f['neg'], f['pos']
            ev = dict(gray=gray(seq[3]), krein=abs(partner[3] - seq[3]))
        elif name in ('PK', 'K', 'R', 'R2', 'N'):
            seq = f['lam'][:4]
            ev = dict(gray=gray(seq[3]), krein=sc.coll_sep(f['dl'][3]))
        elif name == 'X':
            seq = f['lam'][:4]
            ev = dict(gray=gray(seq[3]), axis=sc.coll_re(f['dl'][3]))
        elif name == "P'":
            seq = f['lam'][:4]
            ev = dict(gray=gray(seq[3]), axis=abs(mp.re(seq[3])))
        else:
            seq = f['lam'][:4]
            ev = dict(gray=gray(seq[3]))
        ok, U_, dmin = exact_rule(seq, ev, floor, cutoffs=cut, partner=partner)
        arms = {a: exact_rule(seq, ev, floor, arms=(a,), cutoffs=cut, partner=partner)[0] for _, a, _ in ARM_FAMILIES}
        D[name] = (('converged' if ok else 'Unresolved'), arms)
        say(f"  {name:4s} at the cutoffs {f['fin']}, in the limit {f['lim']}: the binding group U {mp.nstr(U_, 3)}, distance"
            f" {mp.nstr(dmin, 3)} ({min(ev, key=ev.get)}); under the rule {D[name][0]}; arms converging it: "
            f"{[a for a, v in arms.items() if v] or 'none'}")
    return D


# ---- the computed side ----

def ladder_sums(f, R):
    sums = []
    for j in range(4):
        L0, w = f['sys'][j]
        L = R.T @ L0 @ R
        A, B, W = ln.first_order(L, w)
        m2 = L.shape[0]
        sym = [np.concatenate([R.T @ np.eye(m2)[i], np.zeros(m2)]) for i in range(2)]
        r = ln.record(A, B, W, L, ln.margin(np.linalg.norm(A, 2), M), symmetry=sym, expected=d.TWO_CHAINS)
        sums.append(cv.summarize(r, A, W))
    return sums


def claim_projector():
    rows = []

    def osc(k, s=1.0, real=False):
        A = np.array([[0.0, 1.0 / s], [(k if real else -k) * s, 0.0]])
        W = np.array([[0.0, 1.0 / s], [-1.0 / s, 0.0]])
        return A, W
    cases = [('oscillator, k = 4', osc(4.0), 2j, (1 + 4) / (2 * 2)),
             ('real pair, k = 4', osc(4.0, real=True), 2.0, (1 + 4) / (2 * 2)),
             ('oscillator under diag(1, 10), k = 4', osc(4.0, s=10.0), 2j, (1 + 100 * 4) / (2 * 10 * 2))]
    A2, W2 = osc(4.0)
    A4 = np.zeros((4, 4))
    W4 = np.zeros((4, 4))
    for i in (0, 1):
        A4[np.ix_([i, i + 2], [i, i + 2])] = A2
        W4[np.ix_([i, i + 2], [i, i + 2])] = W2
    cases.append(("the doubled oscillator's group of two", (A4, W4), 2j, (1 + 4) / (2 * 2)))
    for label, (A, W), target, exact in cases:
        lam, V = np.linalg.eig(A)
        idx = [i for i in range(len(lam)) if abs(lam[i] - target) < 1e-8]
        pidx = [i for i in range(len(lam)) if abs(lam[i] + np.conj(target)) < 1e-8]
        p = cv.projector(A, W, lam, V, idx, pidx)
        rel = abs(p['pnorm'] - exact) / exact
        rows.append((label, p['pnorm'], exact, rel, p['ok'], p['left'], p['cond'], p['idem']))
    blocks, w, _ = d.collision_blocks()
    A, B, W, L, sym = d.system(blocks, w)
    r = ln.record(A, B, W, L, ln.margin(np.linalg.norm(A, 2), M), symmetry=sym, expected=d.TWO_CHAINS)
    g = min((g for g in r['groups'] if g['cls'] == 'imag' and g['centre'].imag > 0), key=lambda g: abs(g['centre'] - 35.7j))
    pc = cv.projector(A, W, r['lam'], r['V'], g['idx'], g['idx'])
    return rows, (len(g['idx']), pc)


def main():
    F = families()
    say(f"The separation rule's claims (instrument/convergence.py), factor {cv.FACTOR:g}, m = {M}, {N_MIX} mixings a family."
        " Derived before the run, from exact roots:")
    D = derive(F)
    say()
    failed = 0
    rows, (gsize, pc) = claim_projector()
    ok1 = all(r_[3] < 1e-12 and r_[4] for r_ in rows) and not pc['ok']
    # (6b) a converged point whose tested group is marked not usable
    R0 = d.random_unitary_real(F['P']['sys'][0][0].shape[0] // 2)
    sumsP = ladder_sums(F['P'], R0)
    base = cv.separation(sumsP)
    gi = min(range(len(sumsP[-1]['groups'])), key=lambda i: abs(complex(*sumsP[-1]['groups'][i]['c']) - 1e-3j))
    bad = [dict(s) for s in sumsP]
    bad[-1] = dict(bad[-1], groups=[dict(g) for g in bad[-1]['groups']])
    bad[-1]['groups'][gi].update(ok=False, why='marked not usable (claim 1)')
    rb = cv.separation(bad)
    ok1 = ok1 and base['verdict'] == 'converged' and rb['verdict'] == 'Unresolved' and any('not usable' in x for x in rb['reasons'])
    failed += not ok1
    say(f"1. The analytic projector: {'PASS' if ok1 else 'FAIL'}  " + '; '.join(
        f"{lab}: {pn:.15g} against {ex:.15g} ({rel:.1e}), usable {okp} (left {lf:.1e}, condition {cd:.2g}, P X - X {idm:.1e})"
        for lab, pn, ex, rel, okp, lf, cd, idm in rows))
    say(f"   at UB's exact collision, the group of {gsize}: usable {pc['ok']} ({pc['why']}); a converged point with its"
        f" tested group marked not usable: {rb['verdict']}, {[x for x in rb['reasons'] if 'not usable' in x]}")
    res = {}
    for name in SCORED + ('F15',):
        f = F[name]
        m_ = f['sys'][0][0].shape[0] // 2
        band = f.get('band')
        per = []
        for _ in range(N_MIX):
            R = d.random_unitary_real(m_)
            sums = ladder_sums(f, R)
            full = cv.separation(sums, band=band)
            arms = {a: cv.separation(sums, band=band, arms=(a,)) for _, a, _ in ARM_FAMILIES}
            two = cv.separation(sums[-2:], band=band) if name == 'R' else None
            per.append((sums, full, arms, two))
        res[name] = per
    for name in SCORED:
        f, per = F[name], res[name]
        verdicts = [p[1]['verdict'] for p in per]
        types = [p[1]['type'] for p in per]
        want = D[name][0]
        if want == 'converged':
            ok = all(v == 'converged' and t == f['fin'] for v, t in zip(verdicts, types))
        else:
            ok = all(v == 'Unresolved' for v in verdicts)
        failed += not ok
        bind = [r_ for r_ in per[0][1]['rows'] if not r_.get('ok', True)] or sorted(per[0][1]['rows'], key=lambda r_: r_.get('ratio', np.inf))[:1]
        b = bind[0]
        say(f"{'2' if want == 'converged' else '3'}. {name:3s}: {'PASS' if ok else 'FAIL'}  {verdicts.count('converged')} converged,"
            f" {verdicts.count('Unresolved')} Unresolved of {N_MIX} (derived: {want}); at mixing 1 the binding group"
            f" {cv.row_centre(b):.6g} ({b['role']}, {b.get('kind', 'group')}): U {b.get('U', np.nan):.2e}, d {b.get('d', np.nan):.2e}"
            f" ({b.get('event')}){'; ' + b['why'] if b.get('why') else ''}")
    say('4. The arms, each red where a designated counterexample reads converged with its finite-N type:')
    for tag, arm, fams in ARM_FAMILIES:
        counts = {nm: sum(p[2][arm]['verdict'] == 'converged' and p[2][arm]['type'] == F[nm]['fin'] != F[nm]['lim']
                          for p in res[nm]) for nm in fams}
        red = any(v > 0 for v in counts.values())
        failed += not red
        say(f"   ({tag}) {arm}: {'red, as it must be' if red else 'NOT RED'}  converged with the wrong type: " +
            ', '.join(f"{nm} {c} of {N_MIX}" for nm, c in counts.items()) + f" (derived: {', '.join(nm for nm in fams if D[nm][1][arm])})")
    # (g) at the module (UB)
    G = [dict(s, groups=[dict(g) for g in s['groups']]) for s in sumsP]
    dP = base['rows'][[i for i, r_ in enumerate(base['rows']) if abs(cv.row_centre(r_) - 1e-3j) < 1e-6][0]]['d']
    for s in G[-2:]:
        k = min(range(len(s['groups'])), key=lambda i: abs(complex(*s['groups'][i]['c']) - 1e-3j))
        s['groups'][k]['pnorm'] = 0.2 * dP / (cv.U * s['normA'])
    gw, gwo = cv.separation(G), cv.separation(G, arms=('no_numerical',))
    red_g = gw['verdict'] == 'Unresolved' and gwo['verdict'] == 'converged'
    failed += not red_g
    say(f"   (g) no_numerical, at the module: {'red, as it must be' if red_g else 'NOT RED'}  ||P_g|| u ||A|| set to {0.2 * dP:.2e},"
        f" a fifth of the distance {dP:.2e}: with the estimate {gw['verdict']}, without it {gwo['verdict']}")
    # reported
    f15 = res['F15']
    say(f"Reported, unscored: F15 (the pair at 15 margins): {sum(p[1]['verdict'] == 'converged' for p in f15)} of {N_MIX}"
        f" converged with its finite-N type ({F['F15']['fin']}; in the limit {F['F15']['lim']}; derived: {D['F15'][0]}). R2 (R from"
        f" its two highest cutoffs): {sum(p[3]['verdict'] == 'converged' for p in res['R'])} of {N_MIX} converged (derived:"
        f" {D['R2'][0]}).")
    allrows = [r_ for nm in SCORED for p in res[nm] for r_ in p[1]['rows'] if 'U' in r_ and np.isfinite(r_['U'])]
    nums = [r_['num'] for r_ in allrows]
    say(f"Reported: {len(allrows)} tested groups read; the numerical estimate {min(nums):.1e} to {max(nums):.1e}, against floors"
        f" near {sc.MG:.1e}.")
    say(f"{failed} failed")
    path = os.path.join(HERE, 'sep_claims.out')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f"The separation rule's claims: {'PASS' if not failed else 'FAIL'} ({failed} failed): the analytic projector,"
                      " the converged controls, seven counterexamples Unresolved, and nine arms.",
                      'Each outcome derived before the run from exact roots (SEPARATION_PLAN.md; printed first).'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
