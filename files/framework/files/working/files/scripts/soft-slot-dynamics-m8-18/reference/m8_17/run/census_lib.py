"""M8.17's census logic, with no solve: the points, the reproduction rules, classifying a point, the brackets, the
locator's decisions and the row outcomes (M8.17's terms: THE POINTS, CLASSIFYING A POINT, LOCATING A CHANGE OF TYPE,
THE ROW OUTCOMES, and THE FREEZE, THE GUARD AND THE RUN).

Everything here reads records: M8.16.1's outputs, M8.15's adjudicated readings, M8.15.2's location, and this run's own
records. The solves and the records of the run's points are census.py's, through M8.16.1's driver and the frozen
instrument. The locator's bisection takes its solve and its agreement measure as arguments, so the same code runs on
the instrument in the run and on synthetic records in test 4.

Readings of the terms that the code makes, each stated where it is made:
  - n(L) is resolved at a cutoff when the point was solved and accepted there and its record holds no n(L) item among
    its unresolved, its gray zone or L's zero count against V0's chains (nl_at);
  - two intervals overlap when their interiors meet: intervals that only touch hold the two cutoffs' changes on
    opposite sides of a point both sampled (location);
  - the two-ends agreement measures the solution continued from the upper end against the one continued from the
    lower, as branch identity measures N = 32's against N = 24's embedded (census.aligned);
  - categorical equality compares, at every cutoff, the record's type, its indices (n(L), n(D), K and K's parts k_r,
    k_c and k_i^-), V0's dimension and ranks, its chains and its Krein counts, and the rule's verdict and type.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402

# --- the points (THE POINTS) ----------------------------------------------------------------------------------------
CUTOFFS = cs.CUTOFFS                       # 16, 24 and 32, M8.16.1's
DECIDING = CUTOFFS[1:]                     # the cutoffs that decide a location, N = 24 and 32
WINDOWS = {'R4': cs.ladder(16, 72.0), 'R5': cs.ladder(14, 32.0), 'R2': cs.ladder(18, 132.0)}
ROWS = ['T1/R4', 'T4/R4', 'T1/R5', 'T4/R5', 'T2/R4', 'T2/R5', 'T3/R4', 'T3/R5', 'T5/R2']
RUN_ORDER = ['T2/R4', 'T3/R4', 'T5/R2', 'T1/R4', 'T4/R4', 'T1/R5', 'T4/R5']
SLOT = {r: r.split('/')[1] for r in ROWS}
M815 = {'T2/R4': 'T2_R4', 'T2/R5': 'T2_R5', 'T3/R4': 'T3_R4', 'T3/R5': 'T3_R5', 'T5/R2': 'T5_R2'}
T2_END, T2_ON = WINDOWS['R4'][13], WINDOWS['R4'][14]          # 22.63 and 32
PATHS = {'T1/R4': WINDOWS['R4'], 'T4/R4': WINDOWS['R4'], 'T1/R5': WINDOWS['R5'], 'T4/R5': WINDOWS['R5'],
         'T2/R4': WINDOWS['R4'][:14], 'T3/R4': WINDOWS['R4'][:15], 'T5/R2': WINDOWS['R2']}
ON_TO = {'T2/R4': (T2_END, T2_ON)}          # the path goes on to 32 where its type bracket is (22.63, 32)
# the 56 first-time readings, sealed until the freeze
NEW = {'T1/R4': [e for e in WINDOWS['R4'] if e not in cs.SAMPLE], 'T4/R4': [e for e in WINDOWS['R4'] if e not in cs.SAMPLE],
       'T1/R5': [e for e in WINDOWS['R5'] if e not in cs.SAMPLE], 'T4/R5': [e for e in WINDOWS['R5'] if e not in cs.SAMPLE],
       'T2/R4': [16.0, T2_END], 'T3/R4': [32.0], 'T5/R2': [WINDOWS['R2'][15], 128.0, 132.0]}
WITHHELD = {'T2/R4': [16.0, T2_END], 'T3/R4': [32.0], 'T5/R2': [WINDOWS['R2'][15]]}   # computed here, rule 2
# the locator (LOCATING A CHANGE OF TYPE)
W = 1e-3                                    # the union's width, relative to its lower end
W_HALF = W / 2                              # each cutoff's bisection completes below it
DELTAS = (0.01, 0.05)                       # the guards' offsets, the second a single retry
AGREE = ck.IDENTITY                         # the two-ends agreement: branch identity's 1e-2
# the reproduction rules (THE FREEZE, THE GUARD AND THE RUN)
TIMINGS = frozenset(('seconds', 'seconds_record', 'setup_seconds'))
SOLVE_FIELDS = ('accepted', 'eps_reached', 'lam', 'm', 'floor_rel', 'evaluations')
CATEGORICAL = ('type', 'nL', 'nD', 'K', 'kr', 'kc', 'ki', 'sdim', 'ranks', 'blocks', 'krein')
ELLIPTIC_THROUGHOUT, LOCATED_ALL, NOT_SETTLED = ('Elliptic throughout', 'Each change of type located',
                                                 'Not settled by this run')
UNCHANGED_INDEX = ('Type change detected without an `n(L)` change. The registered index locator is inapplicable; '
                   'the location remains OPEN. No location or S6 closure is claimed.')
INADEQUATE_INDEX = 'The index evidence is inadequate; it is not evidence of no index change.'
M8152_FILE = ('reference', 'm8_15_2', 'out', 't1_T3_R5.json')


def key(eps):
    return ck.key(eps)


class Sealed(Exception):
    pass


def sealed(row, eps):
    """Whether (row, eps) is one of the 56 first-time readings, or a point off the row's grid, as the locator's are."""
    if not any(abs(e - eps) <= 1e-12 * e for e in WINDOWS[SLOT[row]]):
        return True
    return key(eps) in {key(e) for e in NEW.get(row, [])}


def path_points(row):
    """The row's registered path, as its FROZEN.json case lists it: every point read."""
    return [dict(eps=e, read=True) for e in PATHS[row]]


def on_path(row, eps):
    return row in PATHS and key(eps) in {key(e) for e in PATHS[row]}


def known_location(m8152):
    """M8.15.2's location on T3/R5, from its record: the guard readings of its located change of type, at level 3."""
    names = [n for b in m8152['brackets'] for n in b['names'] if n.get('name') == 'a located change of type']
    if len(names) != 1:
        raise ValueError(f"M8.15.2's record names {len(names)} located changes of type, not one")
    rd = names[0]['readings']
    if (rd['lower']['verdict'], rd['upper']['verdict']) != ('Elliptic', 'Hyperbolic'):
        raise ValueError("M8.15.2's guard readings are not Elliptic below and Hyperbolic above")
    return dict(row='T3/R5', lower=dict(eps=rd['lower']['eps3'], type='Elliptic'),
                upper=dict(eps=rd['upper']['eps3'], type='Hyperbolic'), source="M8.15.2's location (#632), level 3")


def frozen_values(m8152):
    """FROZEN VALUES: WHAT IS NEW, as FROZEN.json's census section holds them."""
    return dict(cutoffs=list(CUTOFFS), deciding=list(DECIDING), windows={s: list(w) for s, w in WINDOWS.items()},
                rows=list(ROWS), run_order=list(RUN_ORDER), paths={r: list(p) for r, p in PATHS.items()},
                on_to={r: list(v) for r, v in ON_TO.items()}, new={r: list(v) for r, v in NEW.items()},
                withheld={r: list(v) for r, v in WITHHELD.items()}, w=W, w_half=W_HALF, deltas=list(DELTAS),
                agree=AGREE, known_location=known_location(m8152))


# --- one point's records ------------------------------------------------------------------------------------------
def at(case_out, eps):
    """A case output's records of one point: each cutoff's point, the rule's reading and the identity record."""
    k = key(eps)
    return dict(points={N: case_out['cutoffs'].get(str(N), {}).get('points', {}).get(k) for N in CUTOFFS},
                reading=case_out.get('readings', {}).get(k), identity=case_out.get('identity', {}).get(k))


def pt_from_json(pt):
    """One point's records as JSON holds them, each cutoff's point keyed by its cutoff again."""
    return dict(points={int(N): p for N, p in pt['points'].items()}, reading=pt['reading'], identity=pt['identity'])


def same_steps(path_a, path_b, eps):
    """Whether two paths reach eps by the same continuation steps: their grid points up to eps are the same."""
    ka = [key(e) for e in path_a]
    kb = [key(e) for e in path_b]
    k = key(eps)
    return k in ka and k in kb and ka[:ka.index(k) + 1] == kb[:kb.index(k) + 1]


def rule_for(row, eps, theirs):
    """The reproduction rule for a point of this run's path, against M8.16.1's case output theirs: 1, 2, 3, or None for
    a point M8.16.1 never solved."""
    tp = [p['eps'] for p in theirs['case']['points']]
    read = {key(p['eps']): p['read'] for p in theirs['case']['points']}
    k = key(eps)
    if k not in read:
        return None
    if same_steps(tp, PATHS[row], eps):
        return 1 if read[k] else 2
    return 3 if read[k] else None


# --- the reproduction rules ---------------------------------------------------------------------------------------
def _equal(a, b):
    if isinstance(a, float) and isinstance(b, float) and math.isnan(a) and math.isnan(b):
        return True
    return type(a) is type(b) and a == b


def differences(a, b, path=''):
    """Every field in which two records differ, their timings aside, as paths."""
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b), key=str):
            if k in TIMINGS:
                continue
            if k not in a or k not in b:
                out.append(f'{path}/{k}: in one record only')
            else:
                out += differences(a[k], b[k], f'{path}/{k}')
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f'{path}: {len(a)} entries against {len(b)}']
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, f'{path}[{i}]')]
    return [] if _equal(a, b) else [f'{path}: {a!r} against {b!r}']


def gate_full(mine, theirs):
    """Rule 1: a point M8.16.1 read, reached by its own steps, equals its record field for field, timings aside: each
    cutoff's point, the rule's reading and the identity record."""
    out = []
    for N in CUTOFFS:
        out += [f'N = {N}: {d}' for d in differences(mine['points'][N], theirs['points'][N])]
    out += [f'reading: {d}' for d in differences(mine['reading'], theirs['reading'])]
    out += [f'identity: {d}' for d in differences(mine['identity'], theirs['identity'])]
    return out


def gate_solve(mine, theirs):
    """Rule 2: a point M8.16.1 withheld, reached by its own steps, equals its stored solve and acceptance fields."""
    out = []
    for N in CUTOFFS:
        p, q = mine['points'][N], theirs['points'][N]
        if not (q and q.get('withheld')):
            out.append(f'N = {N}: M8.16.1 holds no withheld record here')
            continue
        if not p:
            out.append(f'N = {N}: not reached')
            continue
        out += [f'N = {N}: {f}: {p.get(f)!r} against {q.get(f)!r}' for f in SOLVE_FIELDS
                if f not in p or f not in q or not _equal(p[f], q[f])]
    return out


def gate_categorical(mine, theirs):
    """Rule 3: T1's and T4's points at 0.5, 1 and 2, reached from other predecessors, equal M8.16.1's record in type,
    indices, V0's dimension and ranks, chains, Krein counts and the rule's verdict."""
    out = []
    for N in CUTOFFS:
        p, q = mine['points'][N], theirs['points'][N]
        if not (p and 'record' in p and q and 'record' in q):
            out.append(f'N = {N}: no record to compare')
            continue
        out += [f'N = {N}: {f}: {p["record"][f]!r} against {q["record"][f]!r}' for f in CATEGORICAL
                if not _equal(p['record'][f], q['record'][f])]
    r, s = mine['reading'] or {}, theirs['reading'] or {}
    out += [f'reading: {f}: {r.get(f)!r} against {s.get(f)!r}' for f in ('verdict', 'type') if not _equal(r.get(f), s.get(f))]
    return out


GATES = {1: gate_full, 2: gate_solve, 3: gate_categorical}


# --- classifying a point (CLASSIFYING A POINT) ---------------------------------------------------------------------
def here(pt, case):
    """This instrument's classification: at every cutoff accepted and K1 holding, the rule's reading converged, and
    branch identity kept between N = 24 and 32. The type is the rule's, with the highest cutoff's indices."""
    causes = []
    for N in CUTOFFS:
        p = pt['points'][N]
        if not p:
            causes.append(f'untested at N = {N}')
        elif not p.get('accepted') or 'record' not in p:
            causes.append(f"untested at N = {N}: {p.get('reason', 'no record')}")
        elif not ck.k1(p, case):
            causes.append(f'K1 fails at N = {N}')
    rd, idn = pt['reading'], pt['identity']
    if not rd:
        causes.append('no reading')
    elif rd['verdict'] != 'converged':
        causes.append('the rule reads it Unresolved: ' + '; '.join(rd['reasons']))
    elif rd['type'] not in ('Elliptic', 'Hyperbolic'):
        causes.append(f"the rule reads it converged with no type: {rd['type']!r}")
    if not idn:
        causes.append('no branch identity record')
    elif not idn['kept']:
        causes.append(f"branch identity fails: aligned distance {idn['aligned_distance']:.3g}, the records "
                      f"{'agree' if idn['same_record'] else 'differ'}")
    if causes:
        return dict(classified=False, causes=causes)
    hi = pt['points'][CUTOFFS[-1]]['record']
    return dict(classified=True, type=rd['type'], nL=hi['nL'], nD=hi['nD'], K=hi['K'], ki=hi['ki'])


def there(m815, eps):
    """M8.15's classification: decided, by its adjudicated reading, or not."""
    if m815 is None:
        return dict(decided=False, causes=['M8.15 holds no record of this row'])
    t = [x['type'] for x in m815['types'] if abs(x['eps'] - eps) < 1e-9]
    if len(t) != 1:
        return dict(decided=False, causes=["not on M8.15's grid"])
    if t[0] not in ('Elliptic', 'Hyperbolic'):
        return dict(decided=False, causes=[f'M8.15 left it {t[0]}'])
    p = ck.m815_point(m815, eps)
    return dict(decided=True, type=p['type'], K=p['K'], ki=p['ki'])


def classify(h, t):
    """A point is classified when either instrument classifies it and neither contradicts the other: where both do,
    they agree in type, K and k_i^-. The instrument that supplies the type is named; an Unresolved reading here is not
    a second confirmation of M8.15's."""
    if h['classified'] and t['decided']:
        if (h['type'], h['K'], h['ki']) == (t['type'], t['K'], t['ki']):
            return dict(classified=True, type=h['type'], instrument='both', here=h, m815=t)
        return dict(classified=False, instrument=None, contradiction=True, here=h, m815=t,
                    causes=[f"the instruments disagree: {h['type']}, K = {h['K']}, k_i^- = {h['ki']} here; "
                            f"{t['type']}, K = {t['K']}, k_i^- = {t['ki']} on M8.15's"])
    if h['classified']:
        return dict(classified=True, type=h['type'], instrument='this instrument', here=h, m815=t)
    if t['decided']:
        return dict(classified=True, type=t['type'], instrument="M8.15's", here=h, m815=t)
    return dict(classified=False, instrument=None, here=h, m815=t, causes=h['causes'] + t['causes'])


# --- the brackets (LOCATING A CHANGE OF TYPE, The brackets) ---------------------------------------------------------
def nl_at(p):
    """n(L) at one cutoff, or None where it is missing or unresolved."""
    if not p or not p.get('accepted') or 'record' not in p:
        return None
    r = p['record']
    if any(u.startswith('n(L):') for u in r['unresolved']):
        return None
    return r['nL']


def bracket_kind(lo, hi):
    """'index', 'unchanged' or 'inadequate', from the ends' n(L) at N = 24 and 32 (lo, hi: each cutoff's point)."""
    pairs = {N: (nl_at(lo[N]), nl_at(hi[N])) for N in DECIDING}
    if any(a is None or b is None for a, b in pairs.values()):
        return 'inadequate', pairs
    changed = [a != b for a, b in pairs.values()]
    if all(changed):
        return 'index', pairs
    if not any(changed):
        return 'unchanged', pairs
    return 'inadequate', pairs


def changes(row_points):
    """Each change of type between the row's classified points, in grid order: a type bracket where the two are
    consecutive grid points, and otherwise a change across the unclassified points between them, named."""
    cl = [(i, e, c) for i, (e, c) in enumerate(row_points) if c['classified']]
    out = []
    for (i, e1, c1), (j, e2, c2) in zip(cl, cl[1:]):
        if c1['type'] == c2['type']:
            continue
        between = [row_points[k][0] for k in range(i + 1, j)]
        out.append(dict(kind='type' if not between else 'across', lo=e1, hi=e2, lo_type=c1['type'],
                        hi_type=c2['type'], between=between))
    return out


def known_located(ch, loc):
    """Whether a known location accounts for a change: its guards inside the change's ends, with their types, and every
    grid point between the ends inside the guards."""
    return bool(loc and ch['lo'] < loc['lower']['eps'] < loc['upper']['eps'] < ch['hi']
                and (ch['lo_type'], ch['hi_type']) == (loc['lower']['type'], loc['upper']['type'])
                and all(loc['lower']['eps'] < e < loc['upper']['eps'] for e in ch['between']))


# --- the bisection and the location -------------------------------------------------------------------------------
def bisect(a, b, nl_a, nl_b, end_a, end_b, solve, agree):
    """One cutoff's bisection of an index bracket (a, b), its ends' n(L) nl_a and nl_b, from their continuation states.
    solve(state, eps) -> dict(ok, why, state, k1, nL): a continuation to eps, recorded, with K1 and n(L) by inertia
    (None if unresolved); agree(sol_lower, sol_upper) -> the aligned distance. Each midpoint is solved from both ends;
    the half whose ends differ in n(L) is kept; it completes when the interval is narrower than w/2 of its lower end.
    Returns dict(complete, interval, stop, midpoints)."""
    mids = []
    while not b - a < W_HALF * a:
        m = (a + b) / 2
        s_lo, s_hi = solve(end_a, m), solve(end_b, m)
        mids.append(dict(eps=m, from_lower=s_lo, from_upper=s_hi))
        stop = None
        if not (s_lo['ok'] and s_hi['ok']):
            stop = 'a solve fails or is not accepted: ' + '; '.join(s['why'] for s in (s_lo, s_hi) if not s['ok'])
        elif not (s_lo['k1'] and s_hi['k1']):
            stop = 'K1 fails'
        elif s_lo['nL'] is None or s_hi['nL'] is None:
            stop = 'n(L) unresolved'
        else:
            d = agree(s_lo, s_hi)
            mids[-1]['distance'] = d
            if not d <= AGREE:
                stop = f'the two solutions disagree: aligned distance {d:.3g}'
            elif s_lo['nL'] != s_hi['nL']:
                stop = f"the two solutions disagree: n(L) = {s_lo['nL']} from below, {s_hi['nL']} from above"
        if stop is None:
            n = s_lo['nL']
            if n == nl_a:
                a, end_a = m, s_lo['state']
            elif n == nl_b:
                b, end_b = m, s_hi['state']
            else:
                stop = f'n(L) = {n} matches neither end ({nl_a}, {nl_b}): two changes in the bracket'
        if stop is not None:
            return dict(complete=False, interval=[a, b], stop=stop, midpoints=mids)
    return dict(complete=True, interval=[a, b], stop=None, midpoints=mids)


def location(res, delta):
    """The location's conditions at N = 24 and 32 (res: {N: bisect result or a stop}, delta: {N: the signed change}):
    (union, failures). N = 16's result is reported and does not decide."""
    fails = []
    for N in DECIDING:
        r = res.get(N)
        if r is None or not r['complete']:
            fails.append(f"N = {N}: an unsuccessful stop: {r['stop'] if r else 'not bisected'}")
        elif not r['interval'][1] - r['interval'][0] < W_HALF * r['interval'][0]:
            fails.append(f'N = {N}: the interval is not narrower than w/2 of its lower end')
    if fails:
        return None, fails
    (a1, b1), (a2, b2) = (res[N]['interval'] for N in DECIDING)
    lo, hi = min(a1, a2), max(b1, b2)
    if not max(a1, a2) < min(b1, b2):
        fails.append('the intervals at N = 24 and 32 do not overlap')
    if not hi - lo < W * lo:
        fails.append('the union is not narrower than w of its lower end')
    if delta[DECIDING[0]] != delta[DECIDING[1]]:
        fails.append(f'the signed change differs: {delta[DECIDING[0]]:+d} at N = 24, {delta[DECIDING[1]]:+d} at N = 32')
    elif delta[DECIDING[0]] == 0:
        fails.append('the signed change is zero')
    return (None, fails) if fails else ((lo, hi), [])


def inside(g, window):
    """Whether an amplitude lies inside the row's window."""
    return window[0] <= g <= window[-1]


def guard_offsets(union, window):
    """Each side's guard amplitudes, by delta in order: the lower at the union's lower end times 1 - delta, the upper at
    its upper end times 1 + delta, None where it would fall outside the window."""
    lo, hi = union
    return {'lower': [(d, lo * (1 - d) if inside(lo * (1 - d), window) else None) for d in DELTAS],
            'upper': [(d, hi * (1 + d) if inside(hi * (1 + d), window) else None) for d in DELTAS]}


def guards(union, window, types, read_guard):
    """The guard readings: each side's first classified reading counts, at delta = 0.01 and then 0.05, and must carry
    its bracket end's type (types: {'lower': ..., 'upper': ...}); a guard outside the window is not computed.
    read_guard(side, eps) -> this instrument's classification. Returns (readings, failures)."""
    readings, fails = {}, []
    for side, offs in guard_offsets(union, window).items():
        readings[side], got, outside = [], None, False
        for d, g in offs:
            if g is None:
                fails.append(f'the {side} guard at delta = {d} would fall outside the window: not computed')
                outside = True
                break
            c = read_guard(side, g)
            readings[side].append(dict(delta=d, eps=g, reading=c))
            if c['classified']:
                got = c
                break
        if got is None and not outside:
            fails.append(f'no {side} guard reading is classified')
        elif got is not None and got['type'] != types[side]:
            fails.append(f"the {side} guard reads {got['type']}, not its end's {types[side]}")
    return readings, fails


def span(readings):
    """The guard readings that count, the first classified on each side, as (lower, upper)."""
    first = [next(g['eps'] for g in readings[side] if g['reading']['classified']) for side in ('lower', 'upper')]
    return tuple(first)


def located_name(delta):
    return (f'a change of type located between the guard readings, with `n(L)` changing by {delta:+d} inside the '
            f'interval at `N = 24` and 32')


def public(s):
    """A step's record for the output: its outcome, K1, n(L) and point, without its arrays."""
    return dict(ok=s['ok'], why=s['why'], k1=s['k1'], nL=s['nL'], point=s['point'])


def locate(ch, window, case, cuts, readings, aligned, ref, say=print):
    """One bracket (LOCATING A CHANGE OF TYPE). cuts: {N: a cutoff with seed_ok, path(upto) -> {key: step}, the
    registered path from its seed along the window's grid, and step(state, eps) -> step, a continuation, recorded};
    a step is dict(ok, why, state, c, k1, nL, point). readings(sols) -> one point's records from each cutoff's step;
    aligned(cutoff, s1, s2) -> the two-ends distance; ref(eps) -> the record a recomputed point must equal, or None.
    Each cutoff's path is recomputed to the bracket's upper end, and every recomputed point must equal its record,
    timings aside, before any inward continuation; then the index evidence, each cutoff's bisection, the location and
    the guard readings. Returns (record, stop), stop naming the first recomputed point that does not reproduce."""
    lo, hi = ch['lo'], ch['hi']
    paths = {N: (cu.path(hi) if cu.seed_ok else {}) for N, cu in cuts.items()}
    rec = dict(bracket=[lo, hi], types=[ch['lo_type'], ch['hi_type']], seeds={N: cu.seed_ok for N, cu in cuts.items()},
               path={}, ends={})
    failed = []
    for e in [x for x in window if x <= hi * (1 + 1e-12)]:
        k = key(e)
        mine = readings({N: paths[N].get(k) for N in CUTOFFS})
        r = ref(e)
        fails = ['no record to reproduce'] if r is None else gate_full(mine, r)
        rec['path'][k] = dict(ok=not fails, failures=fails)
        if fails:
            failed.append(e)
        if k in (key(lo), key(hi)):
            rec['ends'][k] = mine
    say(f"   ({lo:g}, {hi:g}): the recomputed path, {len(rec['path'])} points, {len(failed)} not reproduced")
    if failed:
        rec['stop'] = f'a recomputed point does not reproduce: eps = {failed[0]:g}'
        return rec, rec['stop']
    lo_pts, hi_pts = rec['ends'][key(lo)]['points'], rec['ends'][key(hi)]['points']
    kind, pairs = bracket_kind(lo_pts, hi_pts)
    rec['kind'], rec['nL'] = kind, {N: list(p) for N, p in pairs.items()}
    if kind != 'index':
        rec['located'], rec['why'] = False, UNCHANGED_INDEX if kind == 'unchanged' else INADEQUATE_INDEX
        return rec, None
    res, delta = {}, {}
    for N in CUTOFFS:
        a_nl, b_nl = nl_at(lo_pts[N]), nl_at(hi_pts[N])
        if N not in DECIDING and (a_nl is None or b_nl is None or a_nl == b_nl):
            res[N] = dict(complete=False, interval=None, stop=f"not bisected: its ends' n(L) are {a_nl} and {b_nl}",
                          midpoints=[])
            continue
        delta[N] = b_nl - a_nl
        cu = cuts[N]
        res[N] = bisect(lo, hi, a_nl, b_nl, paths[N][key(lo)]['state'], paths[N][key(hi)]['state'], cu.step,
                        lambda s1, s2, cu=cu: aligned(cu, s1, s2))
        for mpt in res[N]['midpoints']:
            mpt['from_lower'], mpt['from_upper'] = public(mpt['from_lower']), public(mpt['from_upper'])
        say(f"   N = {N}: {len(res[N]['midpoints'])} midpoints, interval {res[N]['interval']}, "
            f"{'complete' if res[N]['complete'] else 'stopped: ' + res[N]['stop']}")
    rec['bisection'], rec['delta'] = res, delta
    union, fails = location(res, delta)
    rec['union'], rec['failures'] = union, fails
    if union is not None:
        def read_guard(side, g):
            start = lo if side == 'lower' else hi
            pt = readings({N: cuts[N].step(paths[N][key(start)]['state'], g) for N in CUTOFFS})
            c = here(pt, case)
            say(f"   the {side} guard at {g:.6g}, from {start:g}: "
                f"{c['type'] if c['classified'] else 'not classified: ' + '; '.join(c['causes'])}")
            return dict(c, records=pt)
        readings_, gfails = guards(union, window, {'lower': ch['lo_type'], 'upper': ch['hi_type']}, read_guard)
        rec['guards'], rec['failures'] = readings_, fails + gfails
    rec['located'] = union is not None and not rec['failures']
    rec['span'] = list(span(rec['guards'])) if rec['located'] else None
    rec['why'] = located_name(delta[DECIDING[0]]) if rec['located'] else '; '.join(rec['failures'])
    return rec, None


# --- the row outcomes (THE ROW OUTCOMES) --------------------------------------------------------------------------
def row_outcome(row_points, chs, spans):
    """The row's run outcome and what leaves it unsettled. row_points: [(eps, classification)]; chs: its changes, each
    with 'located' and 'why'; spans: each located change's guard readings (lower, upper), whose points between it
    accounts for."""
    open_ = []
    for e, c in row_points:
        if not c['classified'] and not any(lo < e < hi for lo, hi in spans):
            open_.append(dict(point=e, causes=c['causes']))
    for ch in chs:
        if not ch['located']:
            open_.append(dict(change=[ch['lo'], ch['hi']], kind=ch['kind'], why=ch['why']))
    if open_:
        return NOT_SETTLED, open_
    if not chs and all(c['classified'] and c['type'] == 'Elliptic' for _, c in row_points):
        return ELLIPTIC_THROUGHOUT, []
    return LOCATED_ALL, []


def meets_s4(outcome):
    """S4's first and second endings; its third, an Unresolved point documented after an adequacy test, is not reached."""
    return outcome in (ELLIPTIC_THROUGHOUT, LOCATED_ALL)


# --- the known outcomes, from the records on file --------------------------------------------------------------------
def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def m815_records(root=ROOT):
    return {r: load_json(os.path.join(root, 'reference', 'm815_targets', f'branch_{n}.json')) for r, n in M815.items()}


def theirs_records(root=ROOT):
    """M8.16.1's case outputs of the nine rows."""
    return {r: load_json(os.path.join(root, 'reference', 'm8_16_1', 'run', 'out', r.replace('/', '_') + '.json'))
            for r in ROWS}


def known(row, eps, theirs, m815, case):
    """A point's classification from the records on file alone, M8.16.1's outputs and M8.15's: refused at the 56
    first-time readings and off the grid, where nothing on file may be read."""
    if sealed(row, eps):
        raise Sealed(f'{row} at eps = {eps:g} is sealed until the run')
    pt = at(theirs, eps)
    if all(p is None for p in pt['points'].values()):
        h = dict(classified=False, causes=['M8.16.1 did not solve it'])
    elif any(p and p.get('withheld') for p in pt['points'].values()):
        raise Sealed(f'{row} at eps = {eps:g} is a withheld point')
    else:
        h = here(pt, case)
    return classify(h, there(m815, eps))


# --- the windows, the jobs and the record ---------------------------------------------------------------------------
def records_at(row, e, results, extra, theirs):
    """A point's records on this instrument, with the case they ran under and their source: this run's, from its
    row's path or the locator's recomputation; else none, with M8.16.1's case."""
    if row in results and on_path(row, e):
        return at(results[row], e), results[row]['case'], 'this run'
    if (row, key(e)) in extra:
        return extra[(row, key(e))], results[row]['case'], 'this run'
    return None, theirs[row]['case'], None


def classify_rows(results, extra, theirs, m815, loc):
    """Each row's points, classified, and its changes of type. results: this run's row outputs; extra: {(row, key):
    records} the locator recomputed off its rows' paths; theirs: M8.16.1's outputs; m815: M8.15's records; loc:
    M8.15.2's location."""
    rows = {}
    for row in ROWS:
        pts = []
        for e in WINDOWS[SLOT[row]]:
            t = there(m815.get(row), e)
            pt, case, src = records_at(row, e, results, extra, theirs)
            if pt is not None:
                pts.append((e, dict(classify(here(pt, case), t), source=src)))
                continue
            try:
                pts.append((e, dict(known(row, e, theirs[row], m815.get(row), case),
                                    source="M8.16.1's and M8.15's records")))
            except Sealed as why:
                pts.append((e, dict(classify(dict(classified=False, causes=[f'{why}; not computed here']), t),
                                    source='none')))
        chs = changes(pts)
        for ch in chs:
            if ch['kind'] == 'across':
                ch['located'] = known_located(ch, loc if row == loc['row'] else None)
                ch['why'] = (loc['source'] if ch['located'] else
                             f"a change of type across the unclassified grid points {ch['between']}: not located")
        rows[row] = dict(points=pts, changes=chs)
    return rows


def end_kind(row, ch, results, extra, theirs):
    """A type bracket's kind, from its ends' records on this instrument: this run's, else M8.16.1's."""
    lo = records_at(row, ch['lo'], results, extra, theirs)[0] or at(theirs[row], ch['lo'])
    hi = records_at(row, ch['hi'], results, extra, theirs)[0] or at(theirs[row], ch['hi'])
    return bracket_kind(lo['points'], hi['points'])


def jobs(state, results, extra, theirs):
    """The locator's brackets, in row order: each index bracket, and T2/R4's (22.63, 32) wherever it is a type
    bracket, the path going on to 32."""
    out = []
    for row in RUN_ORDER:
        for ch in state[row]['changes']:
            if ch['kind'] != 'type':
                continue
            on = row in ON_TO and [key(x) for x in ON_TO[row]] == [key(ch['lo']), key(ch['hi'])]
            if on or end_kind(row, ch, results, extra, theirs)[0] == 'index':
                out.append((row, ch))
    return out


def assemble(results, extra, located, theirs, m815, loc):
    """Each row's record: its points, classified, its changes, each with its location or the condition it failed, its
    outcome, what leaves it open, and whether it meets an S4 completion condition. located: {(row, key(lo), key(hi)):
    the locator's record}."""
    state = classify_rows(results, extra, theirs, m815, loc)
    rows = {}
    for row in ROWS:
        chs = state[row]['changes']
        for ch in chs:
            if ch['kind'] != 'type':
                continue
            r = located.get((row, key(ch['lo']), key(ch['hi'])))
            if r is None:
                kind, _ = end_kind(row, ch, results, extra, theirs)
                ch.update(located=False, bracket_kind=kind, why=UNCHANGED_INDEX if kind == 'unchanged' else
                          INADEQUATE_INDEX if kind == 'inadequate' else 'an index bracket the locator did not run')
            else:
                ch.update(located=r['located'], bracket_kind=r.get('kind'), why=r['why'], span=r.get('span'))
        spans = [tuple(ch['span']) for ch in chs if ch.get('located') and ch.get('span')]
        if row == loc['row']:
            spans.append((loc['lower']['eps'], loc['upper']['eps']))
        outcome, open_ = row_outcome(state[row]['points'], chs, spans)
        rows[row] = dict(points=[dict(eps=e, **c) for e, c in state[row]['points']], changes=chs, outcome=outcome,
                         open=open_, meets_s4=meets_s4(outcome))
    return rows


def stopped(log):
    """After a stop: every completed job's files, a row's with its first-time points, kept and not classified."""
    if not log.get('stop'):
        return {}
    return {name: dict(files=c['files'], first_time=NEW.get(name, []),
                       cause='the run stopped; the records are kept, and the classification is withheld')
            for name, c in log['completed'].items()}
