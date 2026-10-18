"""K1 to K6, the band-edge guard, the withheld-point guard and the verdict, as the terms state them
(registration/m8_16_task_details.md: THE CHECKS, THE CONVERGENCE RULE, THE VERDICT RULE; DRIVER_PLAN.md v2).

A case's output (driver.py) holds, per cutoff N and point eps: the solve, and at a read point the record's summary,
its representative groups, the convergence summary and the level energies; per eps, the separation reading from the
three cutoffs; and per read eps, branch identity between N = 24 and 32. The checks read only that output, and K6 also
M8.15's record of the branch.
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
RATIO = 10.0                 # the separation test's factor, 1/10
AXIS_MIN = 1e-6              # below it the axis rotation lies in the fibre span, and Q_Z is undefined (UB)


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
    cluster's gray zone (UA)."""
    band = cv.band_edge(eig_hi, n_lo, lam_hi)
    if not band / 2 > ln.GRAY * margin_hi:
        return dict(verdict='Unresolved', type=None, reasons=['the band edge lies within the gray zone (UA)'],
                    rows=[], band=float(band))
    res = cv.separation(sums, band=band)
    return dict(verdict=res['verdict'], type=res['type'], reasons=list(res['reasons']), rows=res['rows'],
                band=float(band))


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
    """K1 and K4 for C1, as D6 registered them."""
    ok_pts = all(p.get('d6_ok') for c in case_out['cutoffs'].values() for p in c['points'].values())
    kern = all(k1(p, case) for c in case_out['cutoffs'].values() for p in c['points'].values())
    along = case_out.get('d6_along_ok', False)
    return dict(K1=kern, K4=ok_pts and along and kern)


def k3(case_out, case):
    """The pyramid's in-span mode at eps = 0.25, at every cutoff: (a) accepted, K1 and K2; (b) exactly one definite
    Krein-negative imaginary group in the slow band, outside the gray zone, within the bar of 0.25 kappa tau_in;
    (c) its static overlaps, at least 0.9 with XY and at most 0.1 with Z, failing with its reason where Q_Z is
    undefined (k3_overlaps); (d) its separation passes."""
    eps = 0.25
    tau_in = [num(m['tau']) for m in case['spectrum'] if m['cls'] == 'imag' and m['sign'] == -1]
    target = [p for p in predicted(case, eps) if p[0] == 'imag' and p[1] == -1]
    per_N, a_all, rest_all = {}, True, True
    rd = case_out['readings'].get(key(eps))
    for N, c in case_out['cutoffs'].items():
        p = c['points'].get(key(eps))
        a = bool(p and k1(p, case) and k2(p, case, eps))
        neg = [g for g in (p or {}).get('groups', []) if g['cls'] == 'imag' and g['status'] == 'definite'
               and g['neg'] == g['size'] and abs(complex(*g['c'])) <= slow_band(case, eps)]
        b = (len(neg) == 1 and neg[0]['size'] == 1 and len(target) == 1 and len(tau_in) == 1
             and abs(complex(*neg[0]['c'])) >= ln.GRAY * p['record']['margin']
             and abs(complex(*neg[0]['c']) - target[0][2]) / abs(target[0][2]) <= BAR)
        ov = p.get('k3_overlaps') if p else None
        cc = bool(ov and ov['xy'] is not None and ov['xy'] >= 0.9 and ov['z'] <= 0.1)
        d = False
        if b and rd and rd['rows']:
            c0 = complex(*neg[0]['c'])
            rows = [r for r in rd['rows'] if 'ratio' in r]
            if rows:
                own = min(rows, key=lambda r: abs(cv.row_centre(r) - c0))
                d = bool(abs(cv.row_centre(own) - c0) <= 1e-3 * abs(c0) and own['ratio'] >= RATIO)
        per_N[N] = dict(a=a, b=b, c=cc, d=d, overlaps=ov, c_why=(ov or {}).get('why'))
        a_all &= a
        rest_all &= b and cc and d
    outcome = 'resolved' if a_all and rest_all else ('not resolved, kernel exact' if a_all else 'instrument failure')
    return dict(outcome=outcome, per_N=per_N)


def check_pyramid_k4(case_out, case):
    """K4 for the pyramid, at 0.25: converged, Hyperbolic, (5, 1, 4); its quartet and Krein-positive pair within the
    bar, at every cutoff."""
    conv = converged(case_out, 0.25, case)
    bar = True
    for c in case_out['cutoffs'].values():
        p = c['points'].get(key(0.25))
        ok, _, _ = leading(p, case, 0.25, classes={('complex', None), ('imag', 1)}) if p and 'record' in p else (False, 0, 0)
        bar &= ok
    return dict(K4=conv and bar, converged=conv, bar=bar)


def check_row_k5(case_out, case):
    """K5 at eps = 0.25, at every cutoff: accepted with the seed checked; V0 as expected (K1); every mode within the
    bar; converged with the expected type and indices."""
    ok = all(c['seed']['ok'] for c in case_out['cutoffs'].values())
    for c in case_out['cutoffs'].values():
        p = c['points'].get(key(0.25))
        ok &= bool(p and k1(p, case) and leading(p, case, 0.25)[0])
    return dict(K5=ok and converged(case_out, 0.25, case))


def m815_point(m815, eps):
    """M8.15's reading at eps: its type, K = n(B) - n(B|G_tol), and k_i^-, from its level-3 record."""
    p3 = next(p for p in m815['points'] if abs(p['eps'] - eps) < 1e-9)
    t15 = next(t['type'] for t in m815['types'] if abs(t['eps'] - eps) < 1e-9)
    return dict(type=t15, K=p3['nL'] - p3['nB_cluster'], ki=p3['ki_minus'])


def check_row_k6(case_out, case, m815):
    """K6 at every read point: agrees, disagrees or unresolved against M8.15's record, with branch identity between
    N = 24 and 32. Scored: every point accepted to the last at every cutoff; no disagreement; agreement at every read
    point with eps <= 2."""
    eps_all = [p['eps'] for p in case['points']]
    accepted = all(c['points'].get(key(e), {}).get('accepted') for c in case_out['cutoffs'].values() for e in eps_all)
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
        if conv and hi:
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
                         identity=ident, reasons=rd['reasons'] if rd else ['no reading']))
    return dict(K6=accepted and disagree == 0 and low_ok, accepted=accepted, disagree=disagree, low_ok=low_ok,
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


def verdict(results, dry=False):
    """THE VERDICT RULE: the instrument qualifies on K1 to K4; a row on K5, and K6 where it has a ladder, with the R5
    control passed for an R5 row (BOUNDARY.md's amendment 4). A control or the pyramid that failed a check makes the
    verdict NOT QUALIFIED, naming the check, though later cases did not run; `incomplete` is kept for a dry run and for
    an interruption (UB)."""
    ctrl = [results.get(n) for n in STOPPING]
    r5 = not r5_failed(results)
    failed = {n: stop_checks(n, results[n]['checks']) for n in STOPPING if n in results}
    named = [f'{n}: {k}' for n, f in failed.items() for k in f]
    if dry or (any(r is None for r in ctrl) and not named):
        return dict(verdict='incomplete', instrument=None, r5_gate=r5, rows={}, failed=named)
    if any(r is None for r in ctrl):
        return dict(verdict='NOT QUALIFIED', instrument=False, r5_gate=r5, rows={},
                    failing=[k for k in ('K1', 'K2', 'K3', 'K4') if any(k in f for f in failed.values())], failed=named)
    inst = (all(r['checks']['K1'] for r in ctrl) and results['C2a']['checks']['K2'] and results['C2b']['checks']['K2']
            and results['P5']['checks']['K2'] and results['P5']['checks']['K3']['outcome'] == 'resolved'
            and all(r['checks']['K4'] for r in ctrl))
    rows = {}
    for n, r in results.items():
        if r['case']['role'] != 'row':
            continue
        ok = inst and r['checks']['K5'] and r['checks'].get('K6', True) and (r5 or r['case']['slot'] != 'R5')
        rows[n] = ok
    failing = [] if inst else [k for k in ('K1', 'K2', 'K3', 'K4') if not _passed(results, k)]
    return dict(verdict='QUALIFIED' if inst else 'NOT QUALIFIED', instrument=inst, r5_gate=r5, rows=rows,
                failing=failing, failed=named, k3=results['P5']['checks']['K3']['outcome'])


def _passed(results, k):
    if k == 'K3':
        return results['P5']['checks']['K3']['outcome'] == 'resolved'
    if k == 'K2':
        return all(results[n]['checks']['K2'] for n in ('C2a', 'C2b', 'P5'))
    return all(results[n]['checks'][k] for n in ('C1', 'C2a', 'C2b', 'C3', 'P5'))
