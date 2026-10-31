"""K1 to K6, the band-edge guard, the withheld-point guard and the verdict, as the terms state them: M8.16's (its terms:
THE CHECKS, THE CONVERGENCE RULE, THE VERDICT RULE), with M8.16.1's next-order bar and the checks that read it (M8.16.1's
terms: THE NEXT-ORDER BAR, THE CASES: WHAT IS ADDED, THE VERDICT RULE: WHAT CHANGES; DRIVER_PLAN.md v2, items 3 and 4).

A case's output (driver.py) holds, per cutoff N and point eps: the solve, and at a read point the record's summary,
its representative groups, the convergence summary and the level energies; per eps, the separation reading from the
three cutoffs; and per read eps, branch identity between N = 24 and 32. The checks read only that output, the case's
frozen next-order values, and K6 also M8.15's record of the branch.
"""
import contextlib
import math
import os
import sys
import numpy as np
from scipy.optimize import linear_sum_assignment

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import linear as ln, convergence as cv  # noqa: E402

BAR = 0.05
IDENTITY = 1e-2              # D7's aligned-distance guard (UA)
AXIS_MIN = 1e-6              # below it the axis rotation lies in the fibre span, and Q_Z is undefined (UB)
FRACTION = 1e-6              # the provisional fraction the rule retired as a gate: reported beside it, unscored
# the next-order bar (M8.16.1's terms, THE NEXT-ORDER BAR and FROZEN VALUES: WHAT IS NEW)
NEXT_EPS = (0.25, 0.5, 1.0)  # the extrapolation's points
CEILING = (0.1, 1e-3)        # C_g(N) = max(0.1 |c_g(N)|, 1e-3 |kappa s_g|)
RESOLUTION = 0.1             # check 2: E_c at most a tenth of the ceiling
FLOOR = 0.1                  # check 4: the tolerance's floor, a tenth of the ceiling
TWO_TERM = 0.01              # the two-term residual at 0.25 is reported beside 1%, unscored


def num(d):
    """A serialized number (cases.serialize): a fraction or float as a float, a complex as a complex."""
    if 're' in d:
        return complex(d['re'], d['im'])
    return float(d['value'])


def key(eps):
    return f'{eps:.12g}'


# --- the leading order, and matching by class and Krein sign ------------------------------------------------------
def predicted(case, eps):
    """[(cls, sign, lambda)] with multiplicity: lambda = eps kappa s tau, as its pair's or quartet's representative."""
    kappa = 1 / (8 * math.sqrt(case['lam0']) * num(case['Q']))
    s = num(case['s'])
    out = []
    for m in case['spectrum']:
        t = num(m['tau'])
        lam = 1j * eps * kappa * s * t if m['cls'] == 'imag' else eps * kappa * s * t
        out += [(m['cls'], m['sign'], complex(lam))] * m['mult']
    return out


def computed(point, band):
    """The record's representative groups with |centre| <= band, as (cls, sign, lambda) with multiplicity. A definite
    imaginary group's sign is -1 when all its Krein signs are negative, +1 when none is; a mixed or degenerate group
    gets the sign 'unresolved', which matches nothing."""
    out = []
    for g in point['groups']:
        c = complex(*g['c'])
        if abs(c) > band:
            continue
        sign = None
        if g['cls'] == 'imag':
            sign = 'unresolved' if g['status'] != 'definite' else (-1 if g['neg'] == g['size'] else 1)
        out += [(g['cls'], sign, c)] * g['size']
    return out


def match(pred, comp):
    """One to one within each (class, sign), with multiplicity, by the least total relative distance. Returns
    (counts equal, the largest relative deviation, per-mode deviations as (cls, sign, predicted, computed, dev))."""
    buckets = {}
    for p in pred:
        buckets.setdefault((p[0], p[1]), [[], []])[0].append(p[2])
    for c in comp:
        buckets.setdefault((c[0], c[1]), [[], []])[1].append(c[2])
    ok, rows = True, []
    for (cls, sign), (P, C) in buckets.items():
        if len(P) != len(C):
            ok = False
            continue
        if not P:
            continue
        cost = np.array([[abs(c - p) / abs(p) for c in C] for p in P])
        i, j = linear_sum_assignment(cost)
        rows += [(cls, sign, P[a], C[b], float(cost[a, b])) for a, b in zip(i, j)]
    worst = max((r[4] for r in rows), default=math.inf)
    return ok and bool(rows), worst, rows


def slow_band(case, eps):
    return 2 * max(abs(p[2]) for p in predicted(case, eps))


# --- the separation reading, with the band-edge guard ------------------------------------------------------------
def reading(sums, eig_hi, lam_hi, margin_hi, n_lo):
    """The convergence rule from the cutoffs' summaries; Unresolved if half the band edge lies within the zero
    cluster's gray zone (UA). Reported beside it, unscored: the largest relative change of a tested row between the
    two highest cutoffs, against FRACTION (the terms, THE CONVERGENCE RULE)."""
    band = cv.band_edge(eig_hi, n_lo, lam_hi)
    if not band / 2 > ln.GRAY * margin_hi:
        return dict(verdict='Unresolved', type=None, reasons=['the band edge lies within the gray zone (UA)'],
                    rows=[], band=float(band), rel_change_max=None, rel_change_ok=None)
    res = cv.separation(sums, band=band)
    rel = [r['rel_change'] for r in res['rows'] if r.get('role') == 'tested' and 'rel_change' in r]
    return dict(verdict=res['verdict'], type=res['type'], reasons=list(res['reasons']), rows=res['rows'],
                band=float(band), rel_change_max=float(max(rel)) if rel else None,
                rel_change_ok=bool(rel) and max(rel) <= FRACTION)


# --- the withheld points ------------------------------------------------------------------------------------------
class Withheld(Exception):
    pass


@contextlib.contextmanager
def withheld(label):
    """While a withheld point is processed, every call that would compute its record refuses: first_order, record,
    summarize, and L's inertia or spectrum read through ln.inertia or spectrum_of_L. Newton's own hess_dense stays
    open, since the solve needs it (UB)."""
    targets = [(ln, 'first_order'), (ln, 'record'), (ln, 'inertia'), (cv, 'summarize'), (sys.modules[__name__],
                                                                                          'spectrum_of_L')]
    saved = []
    try:
        for obj, attr in targets:
            saved.append((obj, attr, getattr(obj, attr)))

            def refuse(*a, _what=f'{getattr(obj, "__name__", obj)}.{attr}', **k):
                raise Withheld(f'{_what} refused at the withheld point {label}')
            setattr(obj, attr, refuse)
        yield
    finally:
        for obj, attr, f in saved:
            setattr(obj, attr, f)


def spectrum_of_L(L):
    """L's eigenvalues, for the L-kernel readings (development's calibration conditions)."""
    return np.linalg.eigvalsh(L)


# --- K3's overlap, as M8.15.x forms its spans (control_2a.py, point_record; verdict.py; MIT 2c27cea), with M = I ----
def real_orthonormal(V, rel=1e-6):
    if V.shape[1] == 0:
        return V
    C = V.T @ V
    C = (C + C.T) / 2
    ev, U = np.linalg.eigh(C)
    keep = ev > rel ** 2 * ev.max()
    return V @ (U[:, keep] / np.sqrt(ev[keep]))


def project_out(V, W):
    if W.shape[1] == 0:
        return V
    return V - W @ (W.T @ V)


def static_overlap(s, Vb):
    if Vb.shape[1] == 0:
        return 0.0
    c = Vb.T @ s
    ns = np.sqrt(abs(np.vdot(s, s)))
    return float(np.sqrt(np.sum(abs(c) ** 2)) / ns) if ns > 0 else 0.0


def k3_spans(X, fib, chi, z):
    """The rotation span with the fibre directions and the phase partner's static part projected out; Z, the axis
    rotation projected into it; XY, its complement (UB). Also the axis rotation's part outside the fibre span,
    ||P_R z||/||z||: below AXIS_MIN, Q_Z is undefined, and the spans are None (UB, DEVLOG 258)."""
    Fb = real_orthonormal(np.column_stack(list(fib) + [chi]))
    R = real_orthonormal(project_out(X, Fb))
    pz = R @ (R.T @ z)
    axis = float(np.linalg.norm(pz) / np.linalg.norm(z))
    if axis < AXIS_MIN:
        return None, None, axis
    Z = real_orthonormal(pz[:, None])
    XY = real_orthonormal(R - Z @ (Z.T @ R))
    return XY, Z, axis


def k3_overlaps(arrays):
    """K3's (c) record from a point's arrays: the static part's overlaps with XY and with Z, the axis rotation's part
    outside the fibre span, and the reason (c) fails where Q_Z is undefined."""
    XY, Z, axis = k3_spans(arrays['X'], arrays['fib'].T, arrays['chi'], arrays['z'])
    if XY is None:
        return dict(xy=None, z=None, axis=axis,
                    why=f'Q_Z is undefined: the axis rotation lies in the fibre span (||P_R z||/||z|| = {axis:.1e})')
    return dict(xy=static_overlap(arrays['s'], XY), z=static_overlap(arrays['s'], Z), axis=axis, why=None)


# --- the checks ---------------------------------------------------------------------------------------------------
def k1(point, case):
    """The structural kernel at round-off: accepted; V0 as expected, with the leak within its bound (v0_matches);
    case['chains'] chains; and the zero cluster separated."""
    if not point.get('accepted') or 'record' not in point:
        return False
    r = point['record']
    return bool(r['v0_matches'] and r['blocks'] == case['chains'] and r['separated'])


def k2(point, case, eps):
    """No lifted pair: the slow band holds exactly the predicted modes, matched one to one by class and Krein sign
    with multiplicity, and nothing outside the zero cluster lies within its gray zone."""
    if not k1(point, case):
        return False
    ok, _, _ = match(predicted(case, eps), computed(point, slow_band(case, eps)))
    return ok and point['record']['gray_count'] == 0


def leading(point, case, eps, classes=None):
    """(within the bar, the largest deviation, rows) for the predicted modes of the given classes."""
    pred = [p for p in predicted(case, eps) if classes is None or (p[0], p[1]) in classes]
    comp = [c for c in computed(point, slow_band(case, eps)) if classes is None or (c[0], c[1]) in classes]
    ok, worst, rows = match(pred, comp)
    return ok and worst <= BAR, worst, rows


def converged(case_out, eps, case):
    rd = case_out['readings'].get(key(eps))
    hi = case_out['cutoffs'][str(case['cutoffs'][-1])]['points'].get(key(eps), {}).get('record')
    return bool(rd and rd['verdict'] == 'converged' and rd['type'] == case['type'] and hi
                and [hi['nL'], hi['nD'], hi['K']] == case['idx'])


def points_at(case_out, eps):
    return [(N, c['points'].get(key(eps))) for N, c in case_out['cutoffs'].items()]


def check_control(case_out, case):
    """K1 and K4 for C2a, C2b, C3 and the R5 control: every point's kernel; every eps converged with the expected
    type and indices; at 0.25 every mode within the bar; and the largest deviation at 0.25 below that at 2, at each N."""
    eps_all = [p['eps'] for p in case['points']]
    seeds = all(c['seed']['ok'] for c in case_out['cutoffs'].values())
    kern = seeds and all(p is not None and k1(p, case) for e in eps_all for _, p in points_at(case_out, e))
    conv = all(converged(case_out, e, case) for e in eps_all)
    bar, trend, dev = True, True, {}
    for N, c in case_out['cutoffs'].items():
        p25, p2 = c['points'].get(key(0.25)), c['points'].get(key(2.0))
        if not (p25 and p2 and 'record' in p25 and 'record' in p2):
            bar = trend = False
            continue
        ok25, w25, _ = leading(p25, case, 0.25)
        _, w2, _ = leading(p2, case, 2.0)
        dev[N] = (w25, w2)
        bar &= ok25
        trend &= w25 < w2
    return dict(K1=kern, K4=conv and bar and trend and kern, converged=conv, bar=bar, trend=trend, deviations=dev)


def check_k2(case_out, case):
    eps_all = [p['eps'] for p in case['points']]
    return all(p is not None and k2(p, case, e) for e in eps_all for _, p in points_at(case_out, e))


def check_c1(case_out, case):
    """K1 and K4 for C1, as D6 registered them: every registered point at every cutoff, each cutoff's seed checked; an
    empty cutoff never passes (a failed seed ends the case, the terms, Seeds)."""
    pts = [c['points'].get(key(p['eps'])) for c in case_out['cutoffs'].values() for p in case['points']]
    full = len(case_out['cutoffs']) == len(case['cutoffs']) and bool(pts) and all(q is not None for q in pts)
    ok_pts = full and all(q.get('d6_ok') for q in pts)
    kern = full and seeds_ok(case_out) and all(k1(q, case) for q in pts)
    along = case_out.get('d6_along_ok', False)
    return dict(K1=kern, K4=ok_pts and along and kern)


def seeds_ok(case_out):
    """Every cutoff's seed passed its check; a failed check ends the case as an instrument failure (the terms, Seeds)."""
    return all(c['seed']['ok'] for c in case_out['cutoffs'].values())


def kernel_exact(point, case):
    """K3(a)'s certificate that the structural kernel is exact, read from L alone and never from A's zero cluster, so an
    in-span mode merged into that cluster does not fail it: the point accepted; every orbit tangent t with ||L t|| at
    most L's cut, L_CUT ||L|| ||t||; and L's zero count at that cut equal to the case's chains, with nothing in L's
    gray zone. A point that does not carry the certificate fails it."""
    if not point or not point.get('accepted') or 'kernel' not in point:
        return False
    k = point['kernel']
    return bool(k['tangent'] <= ln.L_CUT and k['dimkerL'] == case['chains'] and k['l_resolved'])


def theorem_r_outside(point, case, eps):
    """K3(a)'s slow-band test (UB on #637): outside the in-span pair's class, imaginary of negative Krein signature, the
    slow band is Theorem R's, the predicted and computed modes matched class by class with multiplicity, equal counts,
    each within BAR, and no other group."""
    if not point or 'groups' not in point:
        return False
    pred = [p for p in predicted(case, eps) if (p[0], p[1]) != ('imag', -1)]
    comp = [c for c in computed(point, slow_band(case, eps)) if (c[0], c[1]) != ('imag', -1)]
    if not pred and not comp:
        return True
    ok, worst, _ = match(pred, comp)
    return bool(ok and worst <= BAR)


# --- the next-order bar (M8.16.1's terms, THE NEXT-ORDER BAR; DRIVER_PLAN.md v2, item 3) ------------------------------
def _c(pair):
    """A value of the pinned values file, a pair of decimal strings, as a complex."""
    return complex(float(pair[0]), float(pair[1]))


def lagrange0(xs):
    """The Lagrange weights at 0 of the nodes xs."""
    return [math.prod((0 - xs[k]) / (xs[i] - xs[k]) for k in range(len(xs)) if k != i) for i in range(len(xs))]


def predicted_next(case, eps, N):
    """Per frozen spectrum entry, its modes [(cls, sign, lambda)] with multiplicity at lambda = eps kappa s_g +
    eps^2 c_g(N), the next-order prediction the bar scores, from the case's values at the cutoff N; None when the
    values lack an entry. Against the leading order, two groups of one class and sign whose next-order shifts match
    their separation are exchanged, as T5's two lowest are at eps = 1 (xrodz, B1 on #650)."""
    vals = {g['spectrum_index']: g for g in (case.get('next_order') or {}).get(str(N), [])}
    if sorted(vals) != list(range(len(case['spectrum']))):
        return None
    return [[(m['cls'], m['sign'], complex(eps * _c(vals[j]['kappa_s']) + eps ** 2 * _c(vals[j]['c_g'])))] * m['mult']
            for j, m in enumerate(case['spectrum'])]


def mode_values(point, case, eps, j, N, outside=False):
    """The computed values the next-order assignment gives the predicted modes of the frozen spectrum's entry j at eps,
    with the record groups holding them: (matched, values, groups, deviation). The assignment is K2's, one to one by
    class and Krein sign with multiplicity and the least total relative distance, but against each entry's next-order
    prediction at the cutoff N (predicted_next) in place of its leading order (xrodz, B1 on #650). Without outside it
    runs over the whole slow band; with it, outside the in-span pair's class, as K3(a) reads it. matched is False when
    the counts differ in any class-and-sign bucket, the values lack an entry, or the entry's modes are not all
    assigned. A value held by no record group of its class and sign, or by two, leaves groups None: check 2 reads
    that. The deviation is the largest of the entry's values from its leading order, as M8.16 reports it."""
    if not point or 'groups' not in point:
        return False, None, None, None
    per = predicted_next(case, eps, N)
    if per is None:
        return False, None, None, None
    keep = (lambda x: (x[0], x[1]) != ('imag', -1)) if outside else (lambda x: True)
    band = slow_band(case, eps)
    ok, _, rows = match([x for e in per for x in e if keep(x)], [x for x in computed(point, band) if keep(x)])
    m = case['spectrum'][j]
    pj = per[j][0][2]
    mine = [r for r in rows if (r[0], r[1]) == (m['cls'], m['sign']) and r[2] == pj]
    if not ok or len(mine) != m['mult']:
        return False, None, None, None
    vals = [r[3] for r in mine]
    lead = predicted(dict(case, spectrum=[m]), eps)[0][2]
    dev = max(abs(v - lead) / abs(lead) for v in vals)
    groups, seen = [], set()
    for v in vals:
        hits = [i for i, g in enumerate(point['groups']) if complex(*g['c']) == v and g['cls'] == m['cls']
                and computed(dict(groups=[g]), math.inf)[0][1] == m['sign']]
        if len(hits) != 1:
            return True, vals, None, dev
        if hits[0] not in seen:
            seen.add(hits[0])
            groups.append(point['groups'][hits[0]])
    return True, vals, groups, dev


def association(point, groups):
    """Check 2's association (UA): each record group holding the mode's values is associated, by its exact eigenvalue-
    index set, with one entry of the point's convergence summary, which must agree with it in centre, class, size and
    Krein count, as the same record gives both, and be usable. Returns (ok, E, why), with E the largest
    ||P_g|| max(||R_g||, u ||A||) over the entries; a missing, duplicated or inconsistent association fails it."""
    if groups is None:
        return False, None, "a mode's value is held by no record group, or by two"
    summ = point.get('summary') or {}
    entries, nA, Es = summ.get('groups', []), summ.get('normA'), []
    for g in groups:
        hits = [e for e in entries if sorted(e['idx']) == sorted(g['idx'])]
        if not hits:
            return False, None, f"no summary entry holds the indices {g['idx']}"
        if len(hits) > 1:
            return False, None, f"{len(hits)} summary entries hold the indices {g['idx']}"
        e = hits[0]
        if (e['c'], e['cls'], e['size'], e['neg']) != (g['c'], g['cls'], g['size'], g['neg']):
            return False, None, f"the summary entry for the indices {g['idx']} disagrees with its record group"
        if not e['ok']:
            return False, None, f"the projector for the indices {g['idx']} is not usable: {e['why']}"
        Es.append(e['pnorm'] * max(e['resid'], ln.U * nA))
    return True, max(Es), None


def bar_cutoff(case_out, case, N, g, form='full'):
    """The bar at cutoff N for the frozen group g (an entry of case['next_order'][N]): checks 1 to 4 and the reading's
    quantities. form 'full' is check 1 as the terms write it: at each point, accepted, its seed checked, K1, converged,
    and K2's matching. form 'k3a' is K3(a)'s: accepted, its seed checked, and matched outside the in-span pair's class.
    Checks 3 and 4 are computed wherever check 1 holds; the reading counts them only where checks 1 and 2 hold."""
    c = case_out['cutoffs'].get(str(N)) or {}
    seed = bool((c.get('seed') or {}).get('ok'))
    ks, cg = _c(g['kappa_s']), _c(g['c_g'])
    ceiling = max(CEILING[0] * abs(cg), CEILING[1] * abs(ks))
    out = dict(N=str(N), c1=True, c2=True, c3=None, c4=None, why=[], c_g=cg, ceiling=ceiling)
    xs, lams, Es, devs = [], [], [], []
    for eps in NEXT_EPS:
        p = (c.get('points') or {}).get(key(eps))
        one = bool(p and p.get('accepted') and seed and 'groups' in p)
        if one and form == 'full':
            one = k1(p, case) and converged(case_out, eps, case)
        matched, vals, groups, dev = mode_values(p, case, eps, g['spectrum_index'], N, outside=form == 'k3a') if one \
            else (False, None, None, None)
        if not matched:
            out['c1'] = False
            out['why'].append(f'check 1 at N = {N}, eps = {eps:g}')
            continue
        xs.append(float(p['eps_reached']))
        lams.append(sum(vals) / len(vals))
        devs.append(dev)
        ok2, E, why2 = association(p, groups)
        if not ok2:
            out['c2'] = False
            out['why'].append(f'check 2 at N = {N}, eps = {eps:g}: {why2}')
        Es.append(E)
    if not out['c1']:
        return out
    h = [(lam / x - ks) / x for lam, x in zip(lams, xs)]
    w = lagrange0(xs)
    c2hat = sum(wi * hi for wi, hi in zip(lagrange0(xs[:2]), h[:2]))
    c3hat = sum(wi * hi for wi, hi in zip(w, h))
    spread = abs(c3hat - c2hat)
    E_c = sum(abs(wi) * Ei / xi ** 2 for wi, Ei, xi in zip(w, Es, xs)) if out['c2'] else None
    if out['c2'] and not E_c <= RESOLUTION * ceiling:
        out['c2'] = False
        out['why'].append(f'check 2 at N = {N}: E_c {E_c:.2e} over a tenth of the ceiling, {RESOLUTION * ceiling:.2e}')
    out.update(c3=spread <= ceiling, c4=abs(cg - c3hat) <= max(spread, FLOOR * ceiling), c2hat=c2hat, c3hat=c3hat,
               spread=spread, E_c=E_c, x=xs, lam=lams, deviation=devs,
               two_term=abs(lams[0] - xs[0] * ks - xs[0] ** 2 * cg) / (xs[0] * abs(ks)))
    if not out['c3']:
        out['why'].append(f'check 3 at N = {N}: the spread {spread:.2e} over the ceiling {ceiling:.2e}')
    if not out['c4']:
        out['why'].append(f'check 4 at N = {N}: |c_g - c3| {abs(cg - c3hat):.2e} over {max(spread, FLOOR * ceiling):.2e}')
    return out


def bar_group(case_out, case, gi, form='full'):
    """The bar's reading for the case's frozen group gi, over the cutoffs: pass when checks 1 to 4 hold at every cutoff;
    fail when check 3 or 4 fails at a cutoff where checks 1 and 2 hold, whatever the others read; otherwise Unresolved,
    naming the failing check and point. A record missing a cutoff, or holding one the values lack, cannot pass."""
    want = [str(N) for N in case['cutoffs']]
    have = sorted(case_out['cutoffs'], key=int)
    vals = case.get('next_order') or {}
    if have != want or sorted(vals, key=int) != want:
        return dict(reading='Unresolved', why=[f'the cutoffs differ: the record {have}, the values {sorted(vals, key=int)},'
                                                f' the case {want}'], per_N={})
    per = {N: bar_cutoff(case_out, case, int(N), vals[N][gi], form) for N in want}
    held = [r for r in per.values() if r['c1'] and r['c2']]
    if len(held) == len(per) and all(r['c3'] and r['c4'] for r in held):
        reading = 'pass'
    elif any(not (r['c3'] and r['c4']) for r in held):
        reading = 'fail'
    else:
        reading = 'Unresolved'
    return dict(reading=reading, why=[w for r in per.values() for w in r['why']], per_N=per)


def bar(case_out, case, form='full'):
    """The bar's reading for every group the case's frozen values put under it, by its index there."""
    groups = (case.get('next_order') or {}).get(str(case['cutoffs'][0]), [])
    return {gi: bar_group(case_out, case, gi, form) for gi, g in enumerate(groups) if g['under_bar']}


def k3_pick(groups, band):
    """(group, Krein-negative) for K3's overlaps: the one definite Krein-negative imaginary group in the slow band, if
    there is exactly one; otherwise the smallest group in the band; (None, False) when none lies there, a registered
    failure and never a crash (xrodz, B3)."""
    inside = [g for g in groups if np.hypot(*g['c']) <= band]
    neg = [g for g in inside if g['cls'] == 'imag' and g['status'] == 'definite' and g['neg'] == g['size']]
    if len(neg) == 1:
        return neg[0], True
    return min(inside, key=lambda g: np.hypot(*g['c']), default=None), False


def reading_row(rd, idx):
    """The convergence rule's own row for the group whose eigenvalues at the highest cutoff are idx: the one tested row
    whose top members include them, by the rule's one-to-one matching or its set; None otherwise."""
    if not rd or not idx:
        return None
    hits = [r for r in rd.get('rows', []) if r.get('role') == 'tested' and set(idx) <= set(r.get('top') or [])]
    return hits[0] if len(hits) == 1 else None


def k3_d(rd, idx):
    """(d) for the group whose eigenvalues at the highest cutoff are idx: (passes, reason, row), as the convergence rule
    reads its separation from the three cutoffs. No location tolerance enters: the group is found by the rule's own
    matching (xrodz, B1)."""
    if idx is None:
        return False, '(b) fails at the highest cutoff, so no group is read', None
    row = reading_row(rd, idx)
    if row is None:
        return False, 'no one row of the convergence rule reads this group', None
    return bool(row.get('ok')), None if row.get('ok') else (row.get('why') or 'its separation fails the rule'), row


def k3(case_out, case):
    """The pyramid's in-span mode at eps = 0.25, at every cutoff: (a) accepted, its seed checked, the kernel exact by
    L's certificate (kernel_exact), apart from A's zero cluster, and the slow band outside the in-span pair's class
    passing the next-order bar, check 1 read as K3(a) reads it (bar_cutoff, form 'k3a'; DRIVER_PLAN.md v2, item 3);
    (b) K1 and K2 hold, and exactly one definite
    Krein-negative imaginary group lies in the slow band, outside the gray zone, within the bar of 0.25 kappa tau_in;
    (c) its static overlaps, at least 0.9 with XY and at most 0.1 with Z, failing with its reason where Q_Z is
    undefined (k3_overlaps); (d) its separation passes, as the convergence rule reads it from the three cutoffs for the
    group (b) finds at the highest (k3_d). Not resolved with the kernel exact, the outcome says the diagnosis is
    wrong; an instrument failure leaves it untested. The leading-order test theorem_r_outside is reported beside (a),
    unscored."""
    eps = 0.25
    tau_in = [num(m['tau']) for m in case['spectrum'] if m['cls'] == 'imag' and m['sign'] == -1]
    target = [p for p in predicted(case, eps) if p[0] == 'imag' and p[1] == -1]
    seeds = seeds_ok(case_out)
    top = str(case['cutoffs'][-1])
    slow = bar(case_out, case, 'k3a')
    per_N, a_all, rest_all, idx = {}, bool(slow), True, None
    for N, c in case_out['cutoffs'].items():
        p = c['points'].get(key(eps))
        held = bool(slow) and all(N in r['per_N'] and r['per_N'][N]['c1'] and r['per_N'][N]['c2'] and r['per_N'][N]['c3']
                                  and r['per_N'][N]['c4'] for r in slow.values())
        a = bool(seeds and kernel_exact(p, case) and held)
        kk = bool(p and k1(p, case) and k2(p, case, eps))
        neg = [g for g in (p or {}).get('groups', []) if g['cls'] == 'imag' and g['status'] == 'definite'
               and g['neg'] == g['size'] and abs(complex(*g['c'])) <= slow_band(case, eps)]
        b = bool(kk and len(neg) == 1 and neg[0]['size'] == 1 and len(target) == 1 and len(tau_in) == 1
                 and abs(complex(*neg[0]['c'])) >= ln.GRAY * p['record']['margin']
                 and abs(complex(*neg[0]['c']) - target[0][2]) / abs(target[0][2]) <= BAR)
        if N == top and b:
            idx = neg[0].get('idx')
        ov = p.get('k3_overlaps') if p else None
        cc = bool(ov and ov['xy'] is not None and ov['xy'] >= 0.9 and ov['z'] <= 0.1)
        per_N[N] = dict(a=a, k1k2=kk, b=b, c=cc, overlaps=ov, c_why=(ov or {}).get('why'),
                        leading_outside=theorem_r_outside(p, case, eps))
        a_all &= a
        rest_all &= b and cc
    d, d_why, row = k3_d(case_out['readings'].get(key(eps)), idx)
    for v in per_N.values():
        v['d'] = d
    rest_all &= d
    if a_all and rest_all:
        outcome = 'resolved'
    elif a_all:
        outcome = 'not resolved, kernel exact: the diagnosis is wrong'
    else:
        outcome = 'instrument failure: the diagnosis is untested'
    return dict(outcome=outcome, per_N=per_N, d=d, d_why=d_why, d_row=row, next_order=slow)


def k3_probe(case_out, case):
    """For the dry run (DRIVER_PLAN.md: E2): (d) read for the case's smallest slow imaginary group at the highest cutoff,
    at eps = 0.25, so the rule's lookup runs on instrument data where (b) does not hold. Reported, unscored."""
    eps = 0.25
    p = case_out['cutoffs'].get(str(case['cutoffs'][-1]), {}).get('points', {}).get(key(eps))
    if not p:
        return dict(d=None, why='no point at the highest cutoff')
    band = slow_band(case, eps)
    imag = [g for g in p.get('groups', []) if g['cls'] == 'imag' and abs(complex(*g['c'])) <= band]
    if not imag:
        return dict(d=None, why='no imaginary group in the slow band')
    g = min(imag, key=lambda g: abs(complex(*g['c'])))
    d, why, row = k3_d(case_out['readings'].get(key(eps)), g.get('idx'))
    return dict(d=d, why=why, group=g['c'], row=row)


def check_pyramid_k1(case_out, case):
    """K1 for the pyramid: every cutoff's seed passed its check (xrodz, B2), and every point's kernel (k1)."""
    return bool(seeds_ok(case_out) and all(q is not None and k1(q, case) for e in [p['eps'] for p in case['points']]
                                           for _, q in points_at(case_out, e)))


def check_pyramid_k4(case_out, case):
    """K4 for the pyramid: converged at 0.25, Hyperbolic, (5, 1, 4); its quartet and Krein-positive pair passing the
    next-order bar, check 1 as the terms write it (M8.16.1's terms, THE NEXT-ORDER BAR); every seed passed its check
    (xrodz, B2). Each group's leading-order deviation at 0.25 is reported beside it, unscored."""
    conv = converged(case_out, 0.25, case)
    slow = bar(case_out, case, 'full')
    ok_bar = bool(slow) and all(r['reading'] == 'pass' for r in slow.values())
    seeds = seeds_ok(case_out)
    lead = {}
    for N, c in case_out['cutoffs'].items():
        p = c['points'].get(key(0.25))
        lead[N] = leading(p, case, 0.25, classes={('complex', None), ('imag', 1)})[1] if p and 'record' in p else None
    return dict(K4=conv and ok_bar and seeds, converged=conv, bar=ok_bar, seeds=seeds, next_order=slow, leading=lead)


def check_row_k5(case_out, case):
    """K5 (M8.16.1's terms, THE NEXT-ORDER BAR): at every cutoff the seed checked, and at eps = 0.25 the point accepted
    with V0 as expected (K1); converged at 0.25 with the expected type and indices; and every predicted slow group
    passing the next-order bar, whose check 1 scores 0.5 and 1. At 0.5, 1 and 2 the leading-order readings, with each
    mode's deviation, are reported, unscored, as M8.16 reports them."""
    ok = all(c['seed']['ok'] for c in case_out['cutoffs'].values())
    for c in case_out['cutoffs'].values():
        p = c['points'].get(key(0.25))
        ok &= bool(p and k1(p, case))
    slow = bar(case_out, case, 'full')
    ok_bar = bool(slow) and all(r['reading'] == 'pass' for r in slow.values())
    reported = {}
    for e in (0.5, 1.0, 2.0):
        for N, c in case_out['cutoffs'].items():
            p = c['points'].get(key(e))
            if p and 'record' in p:
                within, largest, modes = leading(p, case, e)
                reported.setdefault(key(e), {})[N] = dict(k1=k1(p, case), within=within, largest=largest, modes=modes)
        if key(e) in reported:
            reported[key(e)]['converged'] = converged(case_out, e, case)
    return dict(K5=ok and converged(case_out, 0.25, case) and ok_bar, bar=ok_bar, next_order=slow, reported=reported)


def check_ray(case_out, case):
    """The C3 ray (M8.16.1's terms, THE CASES: WHAT IS ADDED): K1 and K2 at its four points, as for the pyramid; the
    next-order bar on its three groups; and the off-ray discrimination: wherever checks 1 and 2 hold, the prediction with
    the off-ray part left out, c_g°(N), fails check 4 at c_g's tolerance, max(spread, 0.1 C_g(N)). Scored, gating
    nothing: its outcome is 'passed', or 'failed' with the failing checks named."""
    K1 = check_pyramid_k1(case_out, case)
    K2 = check_k2(case_out, case)
    slow = bar(case_out, case, 'full')
    ok_bar = bool(slow) and all(r['reading'] == 'pass' for r in slow.values())
    disc, rows = True, []
    for gi, r in slow.items():
        for N, x in r['per_N'].items():
            if not (x['c1'] and x['c2']):
                continue
            off = _c(case['next_order'][N][gi]['c_g_off'])
            tol = max(x['spread'], FLOOR * x['ceiling'])
            fails = abs(off - x['c3hat']) > tol
            disc &= fails
            rows.append(dict(group=gi, N=N, distance=abs(off - x['c3hat']), tolerance=tol, fails_check_4=fails))
    failing = [k for k, v in (('K1', K1), ('K2', K2), ('the next-order bar', ok_bar), ('the discrimination', disc))
               if not v]
    return dict(K1=K1, K2=K2, bar=ok_bar, discrimination=disc, outcome='passed' if not failing else
                'failed: ' + ', '.join(failing), next_order=slow, discrimination_rows=rows)


def _classed(pairs):
    """Values [re, im] by class, each as its pair's or quartet's representative: real, imaginary or complex."""
    out = dict(real=[], imag=[], complex=[])
    for x, y in pairs:
        if abs(y) < 1e-9 and x > 0:
            out['real'].append(x)
        elif abs(x) < 1e-9 and y > 0:
            out['imag'].append(y)
        elif x > 0 and y > 0:
            out['complex'].append(complex(x, y))
    return out


def _nearest(targets, pool):
    """Each target matched to the nearest unused value of pool, in order of the targets; None if the pool runs out
    (dev/d7_ladders.py, match)."""
    used, outv = set(), []
    for t in targets:
        order = [j for j in np.argsort(np.abs(pool - t)) if j not in used]
        if not order:
            return None
        used.add(order[0])
        outv.append(pool[order[0]])
    return outv


def slow_compare(m815, eps, groups):
    """K6's reported reading (the terms, K6): each of M8.15's tracked slow eigenvalues, its level-3 genuine list, against
    the nearest here of its class at the highest cutoff, per unit eps, beside M8.15's own level-2 to level-3 change,
    as D7 read the controls (dev/d7_ladders.py, compare). Unscored."""
    p3 = next((p for p in m815['points'] if abs(p['eps'] - eps) < 1e-9), None)
    p2 = next((p for p in m815.get('level2', []) if abs(p['eps'] - eps) < 1e-9), None)
    if p3 is None:
        return dict(why='no M8.15 point at this eps')
    t3, t2 = _classed(z[0] for z in p3['genuine']), _classed(z[0] for z in p2['genuine']) if p2 else None
    mine = dict(real=[g['c'][0] for g in groups if g['cls'] == 'real'],
                imag=[g['c'][1] for g in groups if g['cls'] == 'imag'],
                complex=[complex(*g['c']) for g in groups if g['cls'] == 'complex'])
    js = lambda v: [v.real, v.imag] if isinstance(v, complex) else float(v)
    out = {}
    for cls in ('imag', 'real', 'complex'):
        s3 = [v / p3['eps_reached'] for v in sorted(t3[cls], key=abs)]
        if not s3:
            continue
        m = _nearest(s3, np.array([v / eps for v in mine[cls]]))
        s2 = [v / p2['eps_reached'] for v in sorted(t2[cls], key=abs)] if t2 else []
        out[cls] = dict(m815=[js(v) for v in s3], mine=[js(complex(v) if cls == 'complex' else v) for v in m] if m else None,
                        dev=max(abs(a - b) / abs(b) for a, b in zip(m, s3)) if m else None,
                        m815_l2_vs_l3=max(abs(a - b) / abs(b) for a, b in zip(s2, s3)) if len(s2) == len(s3) else None)
    return out


def m815_point(m815, eps):
    """M8.15's reading at eps: its type, K = n(B) - n(B|G_tol), and k_i^-, from its level-3 record."""
    p3 = next(p for p in m815['points'] if abs(p['eps'] - eps) < 1e-9)
    t15 = next(t['type'] for t in m815['types'] if abs(t['eps'] - eps) < 1e-9)
    return dict(type=t15, K=p3['nL'] - p3['nB_cluster'], ki=p3['ki_minus'])


def check_row_k6(case_out, case, m815):
    """K6 at every read point: agrees, disagrees or unresolved against M8.15's record, with branch identity between
    N = 24 and 32. Scored: every point accepted to the last at every cutoff; no disagreement; agreement at every read
    point with eps <= 2. A point under a seed that failed its check is invalid and never agrees (xrodz, B2).
    Reported beside each, unscored: M8.15's tracked slow eigenvalues against the nearest here (slow_compare)."""
    eps_all = [p['eps'] for p in case['points']]
    accepted = all(c['points'].get(key(e), {}).get('accepted') for c in case_out['cutoffs'].values() for e in eps_all)
    seeds = seeds_ok(case_out)
    top = str(case['cutoffs'][-1])
    rows, disagree, low_ok = [], 0, True
    for p in case['points']:
        if not p['read']:
            continue
        e = p['eps']
        theirs = m815_point(m815, e)
        hi = case_out['cutoffs'][str(case['cutoffs'][-1])]['points'].get(key(e), {}).get('record')
        ident = case_out['identity'].get(key(e), {})
        rd = case_out['readings'].get(key(e))
        conv = bool(rd and rd['verdict'] == 'converged' and ident.get('kept'))
        if not seeds:
            status = 'invalid'
        elif conv and hi:
            same = rd['type'] == theirs['type'] and hi['K'] == theirs['K'] and hi['ki'] == theirs['ki']
            status = 'agrees' if same else 'disagrees'
        else:
            status = 'unresolved'
        disagree += status == 'disagrees'
        if e <= 2 + 1e-12:
            low_ok &= status == 'agrees'
        rows.append(dict(eps=e, status=status, m815=theirs, mine=dict(type=rd['type'] if rd else None,
                                                                     K=hi['K'] if hi else None,
                                                                     ki=hi['ki'] if hi else None),
                         identity=ident, reasons=(['a seed failed its check'] if not seeds else [])
                         + (rd['reasons'] if rd else ['no reading']),
                         slow=slow_compare(m815, e, case_out['cutoffs'].get(top, {}).get('points', {})
                                           .get(key(e), {}).get('groups', []))))
    return dict(K6=accepted and seeds and disagree == 0 and low_ok, accepted=accepted, seeds=seeds,
                disagree=disagree, low_ok=low_ok,
                rows=rows, agree_above_2=sum(r['status'] == 'agrees' and r['eps'] > 2 for r in rows))


STOPPING = ('C1', 'C2a', 'C2b', 'C3', 'P5')


def stop_checks(name, chk):
    """The scored checks that a control or the pyramid failed; any one stops the run before the next case (THE RUN):
    K1, K2 and K4, and K3 at the pyramid."""
    failed = [k for k in ('K1', 'K2') if not chk.get(k, True)]
    if name == 'P5' and chk['K3']['outcome'] != 'resolved':
        failed.append('K3')
    return failed + (['K4'] if not chk.get('K4', True) else [])


def r5_failed(results):
    """The R5 control's failed checks among K1 and K4 (BOUNDARY.md's amendment 4); ['not run'] if it did not run."""
    r = results.get('C2a/R5')
    if r is None:
        return ['not run']
    return [k for k in ('K1', 'K4') if not r['checks'][k]]


def k6_holds(r):
    """K6 where the row has a ladder: a row whose case names M8.15's record qualifies only on its own K6 key, and one
    whose record has none fails closed (xrodz on #650); a row with no ladder has no K6."""
    return r['checks'].get('K6', False) if r['case'].get('m815') else True


def verdict(results, dry=False):
    """THE VERDICT RULE, with M8.16.1's changes: the instrument qualifies on K1 to K4, K3(a) and K4's pyramid item read
    by the next-order bar; a row on K5, read by the bar, and K6 where it has a ladder, with the R5 control passed for an
    R5 row (BOUNDARY.md's amendment 4); T5's second member as a member, on its own K5. The C3 ray is scored and gates
    nothing: its outcome is reported under its own key. QUALIFIED names the rows and members it qualifies. A control or
    the pyramid that failed a check makes the verdict NOT QUALIFIED, naming the check, though later cases did not run;
    `incomplete` is kept for a dry run and for an interruption (UB)."""
    ctrl = [results.get(n) for n in STOPPING]
    r5 = not r5_failed(results)
    failed = {n: stop_checks(n, results[n]['checks']) for n in STOPPING if n in results}
    named = [f'{n}: {k}' for n, f in failed.items() for k in f]
    if dry or (any(r is None for r in ctrl) and not named):
        return dict(verdict='incomplete', instrument=None, r5_gate=r5, rows={}, members={}, c3_ray={}, qualified=[],
                    failed=named)
    if any(r is None for r in ctrl):
        return dict(verdict='NOT QUALIFIED', instrument=False, r5_gate=r5, rows={}, members={}, c3_ray={}, qualified=[],
                    failing=[k for k in ('K1', 'K2', 'K3', 'K4') if any(k in f for f in failed.values())], failed=named)
    inst = (all(r['checks']['K1'] for r in ctrl) and results['C2a']['checks']['K2'] and results['C2b']['checks']['K2']
            and results['P5']['checks']['K2'] and results['P5']['checks']['K3']['outcome'] == 'resolved'
            and all(r['checks']['K4'] for r in ctrl))
    rows, members, ray = {}, {}, {}
    for n, r in results.items():
        role = r['case']['role']
        if role == 'row':
            rows[n] = bool(inst and r['checks']['K5'] and k6_holds(r) and (r5 or r['case']['slot'] != 'R5'))
        elif role == 'member':
            members[n] = bool(inst and r['checks']['K5'])
        elif role == 'ray':
            ray[n] = r['checks'].get('outcome')
    failing = [] if inst else [k for k in ('K1', 'K2', 'K3', 'K4') if not _passed(results, k)]
    return dict(verdict='QUALIFIED' if inst else 'NOT QUALIFIED', instrument=inst, r5_gate=r5, rows=rows,
                members=members, c3_ray=ray, qualified=[n for n, ok in list(rows.items()) + list(members.items()) if ok],
                failing=failing, failed=named, k3=results['P5']['checks']['K3']['outcome'])


def _passed(results, k):
    if k == 'K3':
        return results['P5']['checks']['K3']['outcome'] == 'resolved'
    if k == 'K2':
        return all(results[n]['checks']['K2'] for n in ('C2a', 'C2b', 'P5'))
    return all(results[n]['checks'][k] for n in ('C1', 'C2a', 'C2b', 'C3', 'P5'))
