"""M8.15.x Target 1's locator: its core, and the evaluator that reads the frozen instrument.

Registered in REGISTER_4.md v3 (2026-10-09T21:58:26Z) with its dated amendments, under TARGET1_TERMS.md v7. The frozen
instrument is read, never changed: m8_15x_solver/ in ../soft-slot-dynamics-m8-15x/, beside this folder.

The core (the grid, the bisection, the steps, the guards and the naming) reads points through an evaluator:
  goto(level, eps, start, kind)   -> (record, None), or (None, residual history) on a Newton failure
  evaluate(level, eps, record)    -> EvalPoint
  enlarge(point, k)               -> the point with its near-zero spectrum recomputed from k eigenpairs
  inner(level, A, B)              -> A^T M B
InstrumentEvaluator wraps the frozen continuation and point data; tests/mock.py plants spectra instead."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment: one thread, so sums are taken in a fixed order

import sys, ast, gc, hashlib, textwrap
import numpy as np
from scipy.optimize import linear_sum_assignment

HERE = os.path.dirname(os.path.abspath(__file__))
INSTRUMENT = os.path.normpath(os.path.join(HERE, '..', 'soft-slot-dynamics-m8-15x', 'm8_15x_solver'))

# --- the locator's frozen values (TARGET1_TERMS.md v7, Frozen values) -------------------------------------------------
K_L = (16, 32, 64)                     # near-zero eigenpairs, enlarged on a coverage failure
SHIFT = -1e-6                          # the shift-invert shift
OVERLAP = 0.9                          # structural overlap, coverage, structural subspace and crossing identity
GATE_LOW, GATE_HIGH = 0.1, 0.05        # the span's gap gate: sigma_d / sigma_1 >= 0.1, sigma_(d+1) / sigma_1 <= 0.05
NGRID = 8                              # grid sub-intervals
WIDTH = 1e-3                           # bisection width, relative to the lower end
OFFSETS = (0.01, 0.02, 0.05, 0.10, 0.20)
DIM = {'C2a': 3, 'C3': 4, 'T2': 4, 'T3': 4}     # the structural span's frozen continuum dimension

ELLIPTIC, HYPERBOLIC = 'Elliptic', 'Hyperbolic'


# --- linear algebra in the M-inner product ---------------------------------------------------------------------------
def orthonormal(V, inner, rel=1e-10):
    """An M-orthonormal basis of span(V), dropping directions below rel of the largest singular value."""
    if V.shape[1] == 0:
        return V
    C = inner(V, V)
    C = (C + C.T) / 2
    ev, U = np.linalg.eigh(C)
    keep = ev > rel ** 2 * ev.max()
    return V @ (U[:, keep] / np.sqrt(ev[keep]))


def principal_cosines(A, B, inner):
    """Cosines of the principal angles between span(A) and span(B), each given by M-orthonormal columns."""
    if A.shape[1] == 0 or B.shape[1] == 0:
        return np.zeros(0)
    return np.clip(np.linalg.svd(inner(A, B), compute_uv=False), 0.0, 1.0)


def structural_span(V, d, inner):
    """The locator's structural span (step 2): the generator vectors V, each M-normalized; P is their top-d principal
    subspace. Returns (P, singular values over the largest, gate passed)."""
    nrm = np.sqrt(np.clip(np.diag(inner(V, V)), 0, None))
    Vn = V / nrm
    C = inner(Vn, Vn)
    C = (C + C.T) / 2
    ev, U = np.linalg.eigh(C)
    order = np.argsort(ev)[::-1]
    ev, U = np.clip(ev[order], 0, None), U[:, order]
    s = np.sqrt(ev)
    rel = s / s[0]
    P = Vn @ (U[:, :d] / s[:d])
    gate = bool(rel[d - 1] >= GATE_LOW and (len(rel) <= d or rel[d] <= GATE_HIGH))
    return P, rel, gate


def near_zero_data(vals, vecs, P, inner, tolL, d):
    """Classify a near-zero spectrum against P (step 2): classes, overlaps, coverage, the structural subspace, n_S."""
    neg = vals < -tolL
    ov = np.linalg.norm(inner(P, vecs), axis=0) / np.sqrt(np.clip(np.diag(inner(vecs, vecs)), 1e-300, None))
    cover = principal_cosines(P, orthonormal(vecs, inner), inner)
    coverage_ok = bool(len(cover) == d and cover.min() >= OVERLAP)
    struct = ov >= OVERLAP
    sub = principal_cosines(P, orthonormal(vecs[:, struct], inner), inner) if struct.any() else np.zeros(0)
    subspace_ok = bool(int(struct.sum()) == d and len(sub) == d and sub.min() >= OVERLAP)
    return dict(neg=neg, ov=ov, cover=cover, coverage_ok=coverage_ok, struct=struct, sub=sub, subspace_ok=subspace_ok,
                nS=int((struct & neg).sum()))


class EvalPoint:
    """What the locator reads at one point on one level."""
    def __init__(self, level, eps, rec, p, nL, nB, kc, vals, vecs, nz, kL, gate_rel, gate_ok, slow_overlap, residual,
                 tolL, ctx=None):
        self.level, self.eps, self.rec, self.p = level, eps, rec, p
        self.nL, self.nB, self.kc, self.h = int(nL), int(nB), int(kc), int(nL) - int(nB)
        self.vals, self.vecs, self.kL, self.tolL = vals, vecs, kL, tolL
        self.neg, self.ov, self.struct, self.nS = nz['neg'], nz['ov'], nz['struct'], nz['nS']
        self.cover, self.sub = nz['cover'], nz['sub']
        self.coverage_ok, self.subspace_ok = nz['coverage_ok'], nz['subspace_ok']
        self.gate_rel, self.gate_ok = gate_rel, gate_ok
        self.slow_overlap, self.residual, self.ctx = slow_overlap, residual, ctx or {}
        self.balanced = bool(getattr(p, 'balanced', True))      # the slow Krein count balances
        self.fast_skipped = bool(self.ctx.get('fast_skipped', False))
        # the fast-spectrum search: not needed (balanced), skipped (counts only read here) or run (a full frozen point)
        self.fast_state = 'not needed' if self.balanced else ('skipped' if self.fast_skipped else 'run')
        self.checks = []
        if not gate_ok:
            self.checks.append('structural span')
        if not self.coverage_ok:
            self.checks.append('spectral coverage')
        if not self.subspace_ok:
            self.checks.append('structural subspace')
        if slow_overlap is not None and slow_overlap >= OVERLAP:
            self.checks.append('slowest pair overlap')

    @property
    def ok(self):
        return not self.checks

    def counts(self):
        return (self.nL, self.nS)

    def record(self):
        out = dict(level=self.level, eps=float(self.eps), nL=self.nL, nB=self.nB, nS=self.nS, h=self.h, kc=self.kc,
                   kL=int(self.kL), near_zero=[float(v) for v in self.vals], overlaps=[float(o) for o in self.ov],
                   coverage_cosines=[float(c) for c in self.cover], subspace_cosines=[float(c) for c in self.sub],
                   span_singular_values=[float(x) for x in self.gate_rel], slowest_pair_overlap=(
                       None if self.slow_overlap is None else float(self.slow_overlap)),
                   residual=(None if self.residual is None else float(self.residual)), checks=list(self.checks),
                   balanced=self.balanced, fast_search=self.fast_state)
        # the frozen point data (the terms' Reported list): the frozen point's own record; the mock's point has none
        frozen = getattr(self.p, 'record', None)
        if frozen is not None:
            out['frozen'] = frozen()
            if self.fast_state != 'run':
                out['frozen']['fast_search'] = None     # balanced, or skipped: the stand-in's empty output is no search
        return out


def near_zero_loop(eigs, P, inner, tolL, d, k0=K_L[0]):
    """The near-zero spectrum with coverage: k_L from k0 doubling to 64 until P is covered."""
    for k in [k for k in K_L if k >= k0]:
        vals, vecs = eigs(k)
        nz = near_zero_data(vals, vecs, P, inner, tolL, d)
        if nz['coverage_ok']:
            break
    return vals, vecs, nz, k


# --- the core: grid, bisection and steps ------------------------------------------------------------------------------
def match_vectors(A, B, inner):
    """Eigenvectors at a step's two ends matched by the assignment problem on their squared M-overlaps."""
    C = inner(A, B) ** 2
    r, c = linear_sum_assignment(-C)
    return list(zip(r.tolist(), c.tolist()))


def reading_end(pool, ep, direction):
    """A step's reading end (REGISTER_4.md, the amendments after R1 and after the review of the results). An end whose
    slow Krein count does not balance moves outward, point by evaluated point: it stops at the first point that fails
    its checks or whose (n(L), n_S) differs, and takes the first that passes its checks, has the same counts and
    balances. With none, it fails closed: None, and the step is Unresolved (no balanced reading end)."""
    if ep.balanced:
        return ep
    if pool is None:
        return None
    pts = pool.get(ep.level, {})
    beyond = sorted((e for e in pts if (e > ep.eps if direction > 0 else e < ep.eps)), key=lambda e: abs(e - ep.eps))
    for e in beyond:
        c = pts[e]
        if c.counts() != ep.counts() or not c.ok:
            return None
        if c.balanced:
            return c
    return None


def analyse_step(ev, lo, hi, pool=None):
    """A final interval [lo, hi] (step 5): its crossing set, coverage, identity, classes and bookkeeping, read between
    its balanced reading ends."""
    level = lo.level
    inner = lambda A, B: ev.inner(level, A, B)
    final = [float(lo.eps), float(hi.eps)]
    lo_r, hi_r = reading_end(pool, lo, -1), reading_end(pool, hi, +1)
    if lo_r is None or hi_r is None:
        return dict(level=level, lo=final[0], hi=final[1], status='Unresolved', reason='no balanced reading end',
                    unbalanced_ends=[s for s, r in (('lower', lo_r), ('upper', hi_r)) if r is None])
    lo, hi = lo_r, hi_r
    out = dict(level=level, lo=final[0], hi=final[1], reading=[float(lo.eps), float(hi.eps)],
               root=float((final[0] + final[1]) / 2), end_h=dict(lower=lo.h, upper=hi.h), dnL=hi.nL - lo.nL,
               dnS=hi.nS - lo.nS, dh=hi.h - lo.h)
    k = max(lo.kL, hi.kL)
    while True:
        if lo.kL < k:
            lo = ev.enlarge(lo, k)
        if hi.kL < k:
            hi = ev.enlarge(hi, k)
        pairs = match_vectors(lo.vecs, hi.vecs, inner)
        cross = [(i, j) for i, j in pairs if lo.neg[i] != hi.neg[j]]
        signed = [(+1 if hi.neg[j] else -1) for i, j in cross]
        if sum(signed) == hi.nL - lo.nL:
            break
        nxt = next((kk for kk in K_L if kk > k), None)
        if nxt is None:
            return dict(out, status='Unresolved', reason='spectral coverage', kL=k)
        k = nxt
    out['kL'] = int(k)
    if not (lo.ok and hi.ok):
        return dict(out, status='Unresolved', reason=', '.join(sorted(set(lo.checks + hi.checks))))
    out['crossings'] = [dict(lo_value=float(lo.vals[i]), hi_value=float(hi.vals[j]), lo_overlap=float(lo.ov[i]),
                             hi_overlap=float(hi.ov[j]), sign=s) for (i, j), s in zip(cross, signed)]
    if not cross:
        return dict(out, status='Unresolved', reason='index bookkeeping')
    A = orthonormal(lo.vecs[:, [i for i, _ in cross]], inner)
    B = orthonormal(hi.vecs[:, [j for _, j in cross]], inner)
    cos = principal_cosines(A, B, inner)
    out['identity_cosines'] = [float(c) for c in cos]
    if len(cos) < len(cross) or cos.min() < OVERLAP:
        return dict(out, status='Unresolved', reason='crossing identity')
    classes = []
    for (i, j) in cross:
        a, b = lo.ov[i] >= OVERLAP, hi.ov[j] >= OVERLAP
        classes.append('structural' if (a and b) else ('genuine' if not (a or b) else 'mixed'))
    for c, cl in zip(out['crossings'], classes):
        c['class'] = cl
    if 'mixed' in classes:
        return dict(out, status='Unresolved', reason='mixed overlap')
    s_struct = sum(s for s, cl in zip(signed, classes) if cl == 'structural')
    s_gen = sum(s for s, cl in zip(signed, classes) if cl == 'genuine')
    out['signed'] = dict(structural=s_struct, genuine=s_gen)
    if hi.nS - lo.nS != s_struct or hi.h - lo.h != s_gen:
        return dict(out, status='Unresolved', reason='index bookkeeping')
    if s_gen and s_struct:
        return dict(out, status='Unresolved', reason='genuine and structural crossings in one step')
    # the root: each crossing eigenvalue's zero, interpolated linearly between lo and hi, averaged over the crossing set
    # (REGISTER_4.md, amendment on the root of a step); the interval and its midpoint stay in the record
    roots, zeros, clamped = [], [], []
    for (i, j) in cross:
        a, b = float(lo.vals[i]), float(hi.vals[j])
        t = a / (a - b) if a != b else 0.5
        zeros.append(lo.eps + (hi.eps - lo.eps) * t)
        clamped.append(not (0.0 <= t <= 1.0))
        roots.append(lo.eps + (hi.eps - lo.eps) * min(max(t, 0.0), 1.0))
    out['midpoint'] = out['root']
    out['crossing_roots'] = [float(r) for r in roots]
    out['crossing_zeros_unclamped'] = [float(z) for z in zeros]
    out['clamped'] = [bool(c) for c in clamped]
    out['root'] = float(np.mean(roots))      # an estimate read from the reading interval, with no 1e-3 guarantee
    return dict(out, status='genuine' if any(cl == 'genuine' for cl in classes) else 'structural')


def bisect(ev, lo, hi, steps, failures, pool):
    """Bisection of one sub-interval whose ends differ in (n(L), n_S), until its width is at most WIDTH of its lower
    end (step 4). A midpoint matching neither end splits the interval, and both halves are bisected."""
    level = lo.level
    while hi.eps - lo.eps > WIDTH * lo.eps:
        mid = (lo.eps + hi.eps) / 2
        rec, hist = ev.goto(level, mid, lo.rec, kind='bisection')
        if rec is None:
            failures.append(dict(level=level, eps=float(mid), where='bisection', history=hist))
            steps.append(dict(level=level, lo=float(lo.eps), hi=float(hi.eps), status='Unresolved',
                              reason='Newton failure', failed_at=float(mid), history=hist))
            return
        ep = ev.evaluate(level, mid, rec)
        pool.setdefault(level, {})[mid] = ep
        if not ep.ok:
            steps.append(dict(level=level, lo=float(lo.eps), hi=float(hi.eps), status='Unresolved',
                              reason=', '.join(ep.checks), failed_at=float(mid)))
            return
        if ep.counts() == lo.counts():
            lo = ep
        elif ep.counts() == hi.counts():
            hi = ep
        else:
            bisect(ev, lo, ep, steps, failures, pool)
            bisect(ev, ep, hi, steps, failures, pool)
            return
    steps.append(analyse_step(ev, lo, hi, pool))


def scan(ev, level, a, b, ep_a, ep_b, pool):
    """The grid on [a, b] at one level, then the bisection of every sub-interval whose ends differ (steps 3 and 4)."""
    pool.setdefault(level, {})
    pool[level][a], pool[level][b] = ep_a, ep_b
    seq, failures, prev = [ep_a], [], ep_a.rec
    for k in range(1, NGRID):
        e = a + (b - a) * k / NGRID
        rec, hist = ev.goto(level, e, prev, kind='grid')
        if rec is None:
            failures.append(dict(level=level, eps=float(e), where='grid', history=hist))
            continue
        ep = ev.evaluate(level, e, rec)
        pool[level][e] = ep
        seq.append(ep)
        prev = rec
    seq.append(ep_b)
    usable = [p for p in seq if p.ok]
    steps = []
    for lo, hi in zip(usable[:-1], usable[1:]):
        if lo.counts() != hi.counts():
            bisect(ev, lo, hi, steps, failures, pool)
    steps.sort(key=lambda s: s.get('root', s['lo']))
    return steps, failures


def match_levels(steps3, steps2):
    """Genuine steps matched across levels by order within the bracket and signed count (step 6)."""
    g3 = [s for s in steps3 if s['status'] == 'genuine']
    g2 = [s for s in steps2 if s['status'] == 'genuine']
    if len(g3) != len(g2):
        return None
    pairs = list(zip(sorted(g3, key=lambda s: s['root']), sorted(g2, key=lambda s: s['root'])))
    if any(a['signed']['genuine'] != b['signed']['genuine'] for a, b in pairs):
        return None
    return pairs


# --- the guards and the naming ----------------------------------------------------------------------------------------
def nearest_below(pool, level, e):
    pts = pool.get(level, {})
    below = [x for x in pts if x <= e]
    key = max(below) if below else min(pts, key=lambda x: abs(x - e))
    return pts[key]


def offset_guard(ev, decide, s3, s2, side, d, region, pool):
    sgn = -1.0 if side == 'lower' else 1.0
    e3, e2 = s3['root'] * (1 + sgn * d), s2['root'] * (1 + sgn * d)
    g = dict(kind='offset', side=side, d=d, eps3=float(e3), eps2=float(e2))
    if not (region[0] <= e3 <= region[1] and region[0] <= e2 <= region[1]):
        return dict(g, skipped='outside the guard region')
    eps = {}
    for level, e in ((3, e3), (2, e2)):
        rec, hist = ev.goto(level, e, nearest_below(pool, level, e).rec, kind='guard')
        if rec is None:
            return dict(g, decided=False, counting=False, verdict='Unresolved', why=['Newton failure'], history=hist)
        eps[level] = ev.evaluate(level, e, rec, full=True)
        pool[level][e] = eps[level]
    typ, why, cross = decide(e3, eps[3].p, eps[2].p, True)
    checks = eps[3].checks + eps[2].checks
    decided = typ in (ELLIPTIC, HYPERBOLIC) and not checks
    counting = (eps[3].h == s3['end_h'][side] and eps[2].h == s2['end_h'][side])
    # the same-eps diagnostic: level 2 at the level-3 guard's eps
    diag = None
    rec, hist = ev.goto(2, e3, nearest_below(pool, 2, e3).rec, kind='guard')
    if rec is not None:
        ep2s = ev.evaluate(2, e3, rec, full=True)
        pool[2][e3] = ep2s
        t2, w2, _ = decide(e3, eps[3].p, ep2s.p, True)
        diag = dict(verdict=t2, why=list(w2), checks=ep2s.checks)
    else:
        diag = dict(verdict='Unresolved', why=['Newton failure'])
    return dict(g, verdict=typ, why=list(why), cross=cross, checks=checks, decided=bool(decided),
                counting=bool(counting), point3=eps[3].record(), point2=eps[2].record(), same_eps=diag)


def region_end_guard(side, region, ladder_types, pool, s3, s2):
    e = region[0] if side == 'lower' else region[1]
    t = ladder_types.get(e)
    p3, p2 = pool.get(3, {}).get(e), pool.get(2, {}).get(e)
    g = dict(kind='region end', side=side, eps3=float(e), eps2=float(e))
    if t is None or p3 is None or p2 is None:
        return dict(g, decided=False, counting=False, verdict='Unresolved', why=['not evaluated'])
    checks = p3.checks + p2.checks
    decided = t['type'] in (ELLIPTIC, HYPERBOLIC) and not checks
    counting = (p3.h == s3['end_h'][side] and p2.h == s2['end_h'][side])
    return dict(g, verdict=t['type'], why=list(t['why']), checks=checks, decided=bool(decided), counting=bool(counting))


def readings(guards):
    """The reading on each side: its nearest counting decided guard; a side whose counting decided guards disagree is
    mixed."""
    out = {}
    for side in ('lower', 'upper'):
        g = [x for x in guards if x['side'] == side and x.get('decided') and x.get('counting')]
        out[side] = dict(reading=(g[0] if g else None), mixed=len({x['verdict'] for x in g}) > 1)
    return out


def collisions(pool, rd):
    """Genuine quartets (k_c > 0) at any evaluated point between the two readings, at either level, inclusive."""
    lo, hi = rd['lower']['reading'], rd['upper']['reading']
    found = []
    for level, key in ((3, 'eps3'), (2, 'eps2')):
        a = lo[key] if lo else -np.inf
        b = hi[key] if hi else np.inf
        for e, p in sorted(pool.get(level, {}).items()):
            if a <= e <= b and p.kc > 0:
                found.append(dict(level=level, eps=float(e), kc=p.kc))
    return found


def unbalanced_between(pool, rd):
    """Every unbalanced evaluated point between the two readings, at either level, inclusive: the only places where a
    fast-spectrum quartet, which the collision check's slow k_c cannot see, could sit."""
    lo, hi = rd['lower']['reading'], rd['upper']['reading']
    out = []
    for level, key in ((3, 'eps3'), (2, 'eps2')):
        a = lo[key] if lo else -np.inf
        b = hi[key] if hi else np.inf
        for e, p in sorted(pool.get(level, {}).items()):
            if a <= e <= b and not p.balanced:
                out.append(dict(level=level, eps=float(e), fast_search=p.fast_state))
    return out


def name_step(s3, s2, rd, coll, label):
    lo, hi = rd['lower']['reading'], rd['upper']['reading']
    reasons = []
    if lo is None:
        reasons.append('no reading below')
    if hi is None:
        reasons.append('no reading above')
    if rd['lower']['mixed']:
        reasons.append('mixed lower side')
    if rd['upper']['mixed']:
        reasons.append('mixed upper side')
    if coll:
        reasons.append('collision')
    if not reasons and {lo['verdict'], hi['verdict']} != {ELLIPTIC, HYPERBOLIC}:
        reasons.append(f'readings {lo["verdict"]} and {hi["verdict"]}')
    location = dict(root3=s3['root'], interval3=[s3['lo'], s3['hi']], root2=s2['root'], interval2=[s2['lo'], s2['hi']],
                    shift=(s2['root'] - s3['root']) / s3['root'])
    confirmed = None if (lo is None or hi is None) else dict(
        lower=dict(kind=lo['kind'], d=lo.get('d'), eps3=lo['eps3'], eps2=lo['eps2'], verdict=lo['verdict']),
        upper=dict(kind=hi['kind'], d=hi.get('d'), eps3=hi['eps3'], eps2=hi['eps2'], verdict=hi['verdict']))
    if label == 'secondary':
        return dict(name='an index crossing located inside the Hyperbolic range', location=location,
                    readings=confirmed, notes=reasons)
    if reasons:
        return dict(name='an index crossing located; the change of type remains unresolved', reasons=reasons,
                    location=location, readings=confirmed)
    region_end = [s for s in ('lower', 'upper') if confirmed[s]['kind'] == 'region end']
    return dict(name='a located change of type', location=location, readings=confirmed,
                region_end_readings=region_end,
                qualification=('confirmed no finer than the ladder' if region_end else None))


def locate_bracket(ev, decide, brackets, region, label, ep_ends, ladder_types, pool, levels=(3, 2)):
    """One bracket at each level: scan, match, guards, names. brackets[level] = (a, b), the same at both levels for a
    target; ep_ends[level] = (EvalPoint at a, EvalPoint at b); pool[level] holds the guard region's ladder points.
    With one level (a control's test), the steps are located and named, and nothing is matched or guarded."""
    res = dict(label=label, brackets={lv: list(brackets[lv]) for lv in levels}, region=list(region), levels={})
    steps = {}
    for level in levels:
        a, b = brackets[level]
        st, fails = scan(ev, level, a, b, ep_ends[level][0], ep_ends[level][1], pool)
        steps[level] = st
        res['levels'][level] = dict(steps=st, failures=fails,
                                    no_genuine=not any(s['status'] == 'genuine' for s in st))
    names = []
    for level in levels:
        if res['levels'][level]['no_genuine']:
            names.append(dict(level=level, name=f'no genuine crossing detected at level {level}'))
        for s in steps[level]:
            if s['status'] == 'structural':
                names.append(dict(level=level, name='a structural step', root=s['root']))
            elif s['status'] == 'Unresolved':
                names.append(dict(level=level, name=f'an Unresolved step ({s["reason"]})', lo=s['lo'], hi=s['hi']))
    res['steps_named'] = []
    if tuple(levels) != (3, 2):
        res['names'] = names
        res['points'] = {lv: [pool[lv][e].record() for e in sorted(pool.get(lv, {}))] for lv in levels}
        return res
    pairs = match_levels(steps[3], steps[2])
    res['matched'] = pairs is not None
    if pairs is None:
        if any(s['status'] == 'genuine' for lv in (3, 2) for s in steps[lv]):
            names.append(dict(name='an index crossing located; the change of type remains unresolved',
                              reasons=['cross-level disagreement']))
    else:
        for s3, s2 in pairs:
            guards = []
            for side in ('lower', 'upper'):
                for d in OFFSETS:
                    guards.append(offset_guard(ev, decide, s3, s2, side, d, region, pool))
                guards.append(region_end_guard(side, region, ladder_types, pool, s3, s2))
            rd = readings(guards)
            coll = collisions(pool, rd)
            unb = unbalanced_between(pool, rd)
            nm = name_step(s3, s2, rd, coll, label)
            res['steps_named'].append(dict(step3=s3, step2=s2, guards=guards, readings=rd, collisions=coll,
                                           unbalanced_between=unb, name=nm))
            names.append(nm)
    res['names'] = names
    res['points'] = {lv: [pool[lv][e].record() for e in sorted(pool.get(lv, {}))] for lv in (3, 2)}
    return res


# --- the frozen verdict, extracted from the frozen driver ------------------------------------------------------------
def decide_source(instrument=INSTRUMENT):
    """The source of decide, the closure inside m815_branch.run_branch, read through the frozen file's syntax tree."""
    src = open(os.path.join(instrument, 'm815_branch.py')).read()
    tree = ast.parse(src)
    rb = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'run_branch']
    if len(rb) != 1:
        raise RuntimeError('run_branch not found once in m815_branch.py')
    dn = [n for n in rb[0].body if isinstance(n, ast.FunctionDef) and n.name == 'decide']
    if len(dn) != 1:
        raise RuntimeError('decide not found once in run_branch')
    lines = src.splitlines(keepends=True)[dn[0].lineno - 1:dn[0].end_lineno]
    text = textwrap.dedent(''.join(lines))
    return text, hashlib.sha256(text.encode()).hexdigest()


def bind_decide(module, text, name, slot, tau0_3, s2, omega0, dlev, sch):
    """decide, bound as run_branch binds it, with the module's own globals."""
    ns = dict(vars(module))
    ns.update(name=name, slot=slot, tau0_3=tau0_3, s2=s2, omega0=omega0, dlev=dlev, sch=sch)
    exec(compile(text, 'm815_branch.py (decide)', 'exec'), ns)
    return ns['decide']


# --- the instrument's evaluator --------------------------------------------------------------------------------------
def import_instrument(instrument=INSTRUMENT):
    if instrument not in sys.path:
        sys.path.insert(0, instrument)
    import m815_branch
    return m815_branch


class InstrumentEvaluator:
    """Points from the frozen instrument: the continuation's goto, the frozen Point, and the near-zero spectrum."""
    def __init__(self, lcs, brs, tau0, d, hooks=None):
        from m815_branch import Point
        from nonlinear import to_real, to_complex, arpack_v0
        from standing import fibre_generators
        from verdict import real_orthonormal, static_overlap
        from linearize import Linearization
        import pinned
        self.Point, self.to_real, self.to_complex, self.arpack_v0 = Point, to_real, to_complex, arpack_v0
        self.fibre_generators, self.real_orthonormal, self.static_overlap = fibre_generators, real_orthonormal, static_overlap
        self.Linearization, self.pinned = Linearization, pinned
        self.lcs, self.brs, self.tau0, self.d = lcs, brs, tau0, d
        self.hooks = hooks or {}
        self.calls = {}
        self.span_no_rotations = False         # test R1's arm only: P without span{X_a Phi}

    def inner(self, level, A, B):
        return A.T @ (self.lcs[level].st.Mr @ B)

    def goto(self, level, eps, start, kind='grid'):
        br = self.brs[level]
        n = self.calls.get((level, kind), 0)
        self.calls[(level, kind)] = n + 1
        hook = self.hooks.get('maxit')
        forced = hook is not None and hook['level'] == level and hook['kind'] == kind and hook['call'] == n
        saved = br.maxit
        if forced:
            br.maxit = hook['maxit']
        try:
            rec = br.goto(eps, start)
            hist = None
            if rec is None:
                hist = self.trace_goto(br, eps, start)
        finally:
            br.maxit = saved
        return rec, hist

    def trace_goto(self, br, eps, start):
        """The failed goto rerun under a trace of solve_pinned's stopping test: the residual of every iteration of
        every solve (the solve is deterministic, so the trace reproduces the failure)."""
        import inspect
        code = self.pinned.solve_pinned.__code__
        lines, first = inspect.getsourcelines(self.pinned.solve_pinned)
        hit = [first + i for i, ln in enumerate(lines) if ln.strip() == 'if res < tol:']
        assert len(hit) == 1
        solves = []

        def local(frame, event, arg):
            if event == 'call':
                return local
            if event == 'line' and frame.f_lineno == hit[0]:
                L = frame.f_locals
                if int(L['it']) == 0:
                    solves.append([])
                solves[-1].append(dict(it=int(L['it']), res=float(L['res']), full=float(L['full'])))
            return local

        sys.settrace(lambda f, e, a: local if f.f_code is code else None)
        try:
            br.goto(eps, start)
        finally:
            sys.settrace(None)
        return solves

    def eigs(self, lin, k):
        import scipy.sparse.linalg as spla
        n = lin.L.shape[0]
        lu = spla.splu((lin.L - SHIFT * lin.Mr).tocsc(), permc_spec='MMD_AT_PLUS_A')
        op = spla.LinearOperator(lin.L.shape, matvec=lambda y: lu.solve(np.asarray(y, float).ravel()), dtype=float)
        vals, vecs = spla.eigsh(lin.L, k=min(k, n - 2), M=lin.Mr, sigma=SHIFT, which='LM', OPinv=op,
                                v0=self.arpack_v0(n))
        del op, lu
        gc.collect()          # scipy's ARPACK wrapper holds the operator, and so the factorization, in a reference cycle
        order = np.argsort(np.abs(vals - SHIFT))
        return vals[order], vecs[:, order]

    def _span(self, lc, Phi):
        fib = [self.to_real(g(Phi)) for g in self.fibre_generators(lc.st.R.shape[1], lc.case.quaternionic)]
        Xs = [self.to_real(x) for x in lc.rot.all(Phi)]
        return fib, Xs

    def evaluate(self, level, eps, rec, full=False):
        """The point data at eps. full: the full frozen point, its fast-spectrum search included, where a verdict is
        read (the offset guards); otherwise the slow spectrum alone (REGISTER_4.md, amendment after R1)."""
        lc = self.lcs[level]
        import verdict as vmod
        saved = vmod.Verdict.fast_search
        if not full:
            vmod.Verdict.fast_search = lambda self_, *args, **kw: []
        try:
            p = self.Point(lc, rec, eps, self.tau0[level], self.tau0[level], keep_cluster=True)
        finally:
            vmod.Verdict.fast_search = saved
        v, Phi = p.v, p.Phi
        lin = v.lin
        Mr, n2 = lin.Mr, lin.n2
        inner = lambda A, B: A.T @ (Mr @ B)
        fib, Xs = self._span(lc, Phi)
        gens = fib + ([] if self.span_no_rotations else Xs)
        P, rel, gate = structural_span(np.column_stack(gens), self.d, inner)
        tolL = 1e-9 * max(1.0, abs(p.sigma - lc.lam0_min))
        vals, vecs, nz, k = near_zero_loop(lambda kk: self.eigs(lin, kk), P, inner, tolL, self.d)
        Xspan = self.real_orthonormal(np.column_stack(Xs), Mr)
        gi = np.where(v.cls == 'genuine')[0]
        slow = None
        if len(gi):
            i = gi[np.argmin(np.abs(v.vals[gi]))]
            slow = float(self.static_overlap(v.vecs[:, i], Xspan, Mr, n2))
        del p.v, p.S
        p.v = None
        ep = EvalPoint(level, eps, rec, p, p.nL, p.nB, p.kc, vals, vecs, nz, k, rel, gate, slow, rec.get('full'), tolL,
                       ctx=dict(P=P, fast_skipped=not full))
        del lin
        gc.collect()
        return ep

    def enlarge(self, ep, k):
        lc = self.lcs[ep.level]
        lin = self.Linearization(lc.st, self.to_complex(ep.rec['x']), ep.rec['sigma'])
        inner = lambda A, B: A.T @ (lin.Mr @ B)
        vals, vecs = self.eigs(lin, k)
        nz = near_zero_data(vals, vecs, ep.ctx['P'], inner, ep.tolL, self.d)
        new = EvalPoint(ep.level, ep.eps, ep.rec, ep.p, ep.nL, ep.nB, ep.kc, vals, vecs, nz, k, ep.gate_rel, ep.gate_ok,
                        ep.slow_overlap, ep.residual, ep.tolL, ctx=ep.ctx)
        del lin
        gc.collect()
        return new
