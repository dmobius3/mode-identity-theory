"""REGISTER_5.md v3 § 2: M8.15.1's synthetic tests S1 to S18c (REGISTER_4.md v3 § 2, with S10 changed) and M8.15.2's
plants A1 to A29, on the mock evaluator, each with its arms.

Each test runs its parent and checks the registered expectation; then each arm, whose expectation must fail. The parent
passes before its arms run. An arm acts on the plant, on a module attribute, or on one function's source by named
edits, each of which must match exactly as often as it states, so the arm changes what it names and nothing else.
Every S test also expects rule 11 to pass at every step. "Named with the qualifier" means the name the ceiling function
gives, applying the terms' clauses 1 to 3 to the record (REGISTER_5.md § 1 item 5); the record keeps M8.15.1's names.

  python3 tests/synthetic.py        writes out/synthetic.json and out/synthetic.log"""
import os, sys, json, copy, inspect, textwrap, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import numpy as np
import mock, locate

OUT = os.path.join(os.path.dirname(HERE), 'out')
UNRES = 'an index crossing located; the change of type remains unresolved'
LOCATED = 'a located change of type'


# --- helpers ------------------------------------------------------------------------------------------------------
def steps(res, level, status=None):
    s = res['levels'][level]['steps']
    return [x for x in s if status is None or x['status'] == status]


def named(res):
    return [x['name']['name'] for x in res['steps_named']]


def all_names(res):
    return [n['name'] for n in res['names']]


def guards(res, side=None, kind=None):
    g = res['steps_named'][0]['guards'] if res['steps_named'] else []
    return [x for x in g if (side is None or x['side'] == side) and (kind is None or x['kind'] == kind)]


def reading(res, side):
    return res['steps_named'][0]['readings'][side]['reading'] if res['steps_named'] else None


def check(conds):
    """conds: [(label, bool)]; returns (passed, failed labels)."""
    bad = [lab for lab, ok in conds if not ok]
    return (not bad), bad


def genuine_step_ok(res, level, root, dn=+2):
    g = steps(res, level, 'genuine')
    return (len(g) == 1 and g[0]['dnL'] == dn and g[0]['dnS'] == 0 and g[0]['signed']['genuine'] == dn
            and abs(g[0]['root'] - root) <= 1e-3 * root)


def located_as_s1(res, r3=1.0130, r2=1.0181):
    nm = res['steps_named'][0]['name'] if res['steps_named'] else {}
    sh = nm.get('location', {}).get('shift', np.nan)
    lo, hi = reading(res, 'lower'), reading(res, 'upper')
    return [('one genuine step at level 3, root within 1e-3', genuine_step_ok(res, 3, r3)),
            ('one genuine step at level 2, root within 1e-3', genuine_step_ok(res, 2, r2)),
            ('shift within 0.002 of +0.50%', abs(sh - (r2 - r3) / r3) <= 0.002 and abs(sh - 0.0050) <= 0.002),
            ('lower reading at d = 0.01, Elliptic', lo is not None and lo['kind'] == 'offset' and lo['d'] == 0.01
             and lo['verdict'] == 'Elliptic'),
            ('upper reading at d = 0.01, Hyperbolic', hi is not None and hi['kind'] == 'offset' and hi['d'] == 0.01
             and hi['verdict'] == 'Hyperbolic'),
            ('named a located change of type', named(res) == [LOCATED])]


# --- the expectations -----------------------------------------------------------------------------------------------
def exp_S1(res):
    c = located_as_s1(res)
    for side in ('lower', 'upper'):
        for d in (0.01, 0.02, 0.05, 0.10):
            g = [x for x in guards(res, side, 'offset') if x['d'] == d]
            c.append((f'same-eps diagnostic Unresolved at {side} {d}', bool(g) and g[0]['same_eps']['verdict'] == 'Unresolved'))
    return check(c)


def exp_S2(res):
    c = []
    for lv in (3, 2):
        st = steps(res, lv)
        c.append((f'one structural step at level {lv}', len(st) == 1 and st[0]['status'] == 'structural'
                  and st[0]['dnL'] == -2 and st[0]['dnS'] == -2))
        c.append((f'no genuine crossing detected at level {lv}', f'no genuine crossing detected at level {lv}' in all_names(res)))
    return check(c)


def exp_S3(res):
    c = []
    for lv, r in ((3, 1.0130), (2, 1.0181)):
        st = steps(res, lv)
        c.append((f'two steps at level {lv}, one structural and one genuine', len(st) == 2
                  and sorted(s['status'] for s in st) == ['genuine', 'structural']))
        c.append((f'genuine step at level {lv} as in S1', genuine_step_ok(res, lv, r)))
    c.append(('named a located change of type', named(res) == [LOCATED]))
    return check(c)


def unresolved_named(res, reason):
    nm = res['steps_named'][0]['name'] if res['steps_named'] else {}
    return nm.get('name') == UNRES and reason in nm.get('reasons', [])


def exp_S4(res):
    return check([('no reading above', reading(res, 'upper') is None),
                  ('named unresolved, no reading above', unresolved_named(res, 'no reading above'))])


def exp_S5(res):
    rd = res['steps_named'][0]['readings'] if res['steps_named'] else {}
    return check([('the upper side is mixed', bool(rd) and rd['upper']['mixed']),
                  ('named unresolved, mixed upper side', unresolved_named(res, 'mixed upper side'))])


def exp_S6(res):
    coll = res['steps_named'][0]['collisions'] if res['steps_named'] else []
    return check([('a collision is recorded', len(coll) > 0),
                  ('named unresolved, collision', unresolved_named(res, 'collision'))])


def exp_S7(res):
    st = [s for s in steps(res, 3) if s['status'] == 'Unresolved' and s['reason'] == 'Newton failure']
    return check([('a level-3 step Unresolved (Newton failure)', len(st) == 1),
                  ('with the planted residual history', bool(st) and len(st[0]['history']) > 0),
                  ('over the bracket reached', bool(st) and st[0]['lo'] < 1.0130 < st[0]['hi']),
                  ('the result unresolved', UNRES in all_names(res) and LOCATED not in named(res))])


def exp_S8(res):
    st = [s for s in steps(res, 3) if s['status'] == 'Unresolved']
    return check([('the level-3 step Unresolved by the crossing identity check', len(st) == 1
                   and st[0]['reason'] == 'crossing identity'),
                  ('the result unresolved', LOCATED not in named(res) and UNRES in all_names(res))])


def exp_S9(res):
    st = [s for lv in (3, 2) for s in steps(res, lv) if s['status'] == 'Unresolved']
    return check([('steps Unresolved by index bookkeeping', len(st) == 2
                   and all(s['reason'] == 'index bookkeeping' for s in st)),
                  ('no located change of type', LOCATED not in named(res))])


def passed_at_1025(res, checks):
    """REGISTER_5.md § 2, S10's new expectation, which A8 and A19 share: the bisection passes the failing midpoint at
    1.025 and the step is located as in S1. The record shows that midpoint, with its failed checks, outside the clean
    window, so the step is not a branch step, clause 3 does not apply, and it is named a located change of type."""
    c = located_as_s1(res)
    g = steps(res, 3, 'genuine')
    s = g[0] if len(g) == 1 else {}
    mids = [m for m in s.get('midpoints', []) if m['role'] == 'failed its checks, passed']
    c.append((f'the failing midpoint at 1.025 recorded and passed, its checks {", ".join(checks)}', len(mids) == 1
              and near(mids[0]['eps'], 1.025) and sorted(mids[0]['checks']) == sorted(checks)))
    c.append(('outside the clean window', bool(s) and not (s['clean_ends'][0] <= 1.025 <= s['clean_ends'][1])))
    c.append(('not a branch step', bool(s) and s.get('branch_step') is False))
    c.append(('clause 3 does not apply: adjudicated a located change of type', adjudicated(res) == [LOCATED]))
    return check(c)


def exp_S10(res):
    """S10 changed (REGISTER_5.md § 2): the tilted midpoint at 1.025 is a structural-subspace failure."""
    return passed_at_1025(res, ['structural subspace'])


def exp_S11(res):
    g = [x for x in guards(res, 'upper', 'offset') if x['d'] == 0.01]
    hi = reading(res, 'upper')
    return check([('the upper d = 0.01 guard is Unresolved by the slowest pair overlap', bool(g)
                   and not g[0]['decided'] and 'slowest pair overlap' in g[0]['checks']),
                  ('the reading above is at d = 0.02', hi is not None and hi['kind'] == 'offset' and hi['d'] == 0.02),
                  ('still located', named(res) == [LOCATED])])


def exp_S12(res):
    return check([('one genuine step at level 3', len(steps(res, 3, 'genuine')) == 1),
                  ('none at level 2', len(steps(res, 2, 'genuine')) == 0),
                  ('a cross-level disagreement, unresolved', any(n.get('name') == UNRES and 'cross-level disagreement'
                                                                 in n.get('reasons', []) for n in res['names']))])


def exp_S13(res):
    lo, hi = reading(res, 'lower'), reading(res, 'upper')
    offs = guards(res, None, 'offset')
    return check([('every offset guard undecided', all(not g.get('decided') for g in offs if 'skipped' not in g)),
                  ('the lower reading is the region end, Elliptic', lo is not None and lo['kind'] == 'region end'
                   and lo['verdict'] == 'Elliptic'),
                  ('no reading above', hi is None),
                  ('named unresolved, no reading above', unresolved_named(res, 'no reading above'))])


def exp_S14(res):
    return check([('one step per level, neither lost nor doubled', len(steps(res, 3)) == 1 and len(steps(res, 2)) == 1),
                  ('level 3 root within 1e-3 of 1.0', genuine_step_ok(res, 3, 1.0)),
                  ('level 2 root within 1e-3 of 1.0', genuine_step_ok(res, 2, 1.0))])


def exp_S15(res):
    c = located_as_s1(res)
    g = steps(res, 3, 'genuine')
    c.append(('k_L = 32 recorded', bool(g) and g[0]['kL'] == 32))
    return check(c)


def exp_S16(res):
    ends = [x for x in guards(res, 'upper', 'region end')]
    return check([('the region end does not count', bool(ends) and not ends[0]['counting']),
                  ('no reading above', reading(res, 'upper') is None),
                  ('named unresolved, no reading above', unresolved_named(res, 'no reading above'))])


def exp_S17(res):
    return check(located_as_s1(res))


def exp_unres_no_balanced(res):
    c = []
    for lv in (3, 2):
        st = steps(res, lv)
        c.append((f'the level-{lv} step Unresolved (no balanced reading end)', len(st) == 1
                  and st[0]['status'] == 'Unresolved' and st[0].get('reason') == 'no balanced reading end'))
    c.append(('no structural or genuine step', not any(s['status'] in ('structural', 'genuine')
                                                        for lv in (3, 2) for s in steps(res, lv))))
    return check(c)


def exp_S18(res):
    c = []
    for lv in (3, 2):
        st = steps(res, lv)
        s = st[0] if st else {}
        c.append((f'one structural step at level {lv}, read across the window', len(st) == 1
                  and s.get('status') == 'structural' and s.get('dnL') == -2 and s.get('dnS') == -2 and s.get('dh') == 0
                  and s.get('reading', [0, 0])[1] > s.get('hi', 1e9)))
        c.append((f'no genuine crossing detected at level {lv}', f'no genuine crossing detected at level {lv}' in all_names(res)))
    return check(c)


# --- the plants and the arms -------------------------------------------------------------------------------------
R3, R2 = 1.0130, 1.0181
UP = lambda d: [(3, R3 * (1 + d)), (2, R2 * (1 + d))]
UPPER_GUARDS_L3 = [(3, R3 * (1 + d)) for d in locate.OFFSETS]


class Patch:
    """A temporary change to the locator (or, given module, to that module), for the arms that act on code rather than
    the plant."""
    def __init__(self, module=None, **kw):
        self.mod, self.kw, self.saved = (module or locate), kw, {}

    def __enter__(self):
        for k, v in self.kw.items():
            self.saved[k] = getattr(self.mod, k)
            setattr(self.mod, k, v)

    def __exit__(self, *a):
        for k, v in self.saved.items():
            setattr(self.mod, k, v)


def mutant(module, name, edits):
    """module.name recompiled from its source with each edit (old, new, count) made, where old must occur exactly
    count times: an arm that changes what it names and nothing else. The copy keeps the module's globals."""
    src = textwrap.dedent(inspect.getsource(getattr(module, name)))
    for old, new, count in edits:
        k = src.count(old)
        if k != count:
            raise RuntimeError(f'an arm edit on {name} matches {k} times, not {count}: {old!r}')
        src = src.replace(old, new)
    ns = dict(vars(module))
    exec(compile(src, f'<arm on {module.__name__}.{name}>', 'exec'), ns)
    return ns[name]


_orig_near = locate.near_zero_data
_orig_analyse = locate.analyse_step


def near_le0(vals, vecs, P, inner, tolL, d):
    out = _orig_near(vals, vecs, P, inner, tolL, d)
    out['neg'] = vals <= 0
    return out


def analyse_midpoint(ev, lo, hi, pool=None, **kw):
    """S1's arm (REGISTER_4.md, amendment on S1's arm): the root taken as the final interval's midpoint."""
    out = _orig_analyse(ev, lo, hi, pool, **kw)
    if 'midpoint' in out:
        out = dict(out, root=out['midpoint'])
    return out


def reading_end_off(pool, ep, direction):
    """S18's arm: each step read at its final interval's ends."""
    return ep


_orig_reading_end = locate.reading_end


def reading_end_skip(pool, ep, direction):
    """S18b's arm: the search skips points that fail their checks."""
    if ep.balanced:
        return ep
    pts = pool.get(ep.level, {})
    for e in sorted((e for e in pts if (e > ep.eps if direction > 0 else e < ep.eps)), key=lambda e: abs(e - ep.eps)):
        c = pts[e]
        if c.counts() != ep.counts():
            return None
        if c.ok and c.balanced:
            return c
    return None


def reading_end_fallback(pool, ep, direction):
    """S18c's arm: with no balanced point, the unbalanced end is kept."""
    r = _orig_reading_end(pool, ep, direction)
    return ep if r is None else r


def analyse_individual(ev, lo, hi, pool=None, **kw):
    """S17's arm: identity by individual overlaps of at least 0.9, with no subspace check."""
    out = _orig_analyse(ev, lo, hi, pool, **kw)
    if out.get('status') in ('genuine', 'structural'):
        inner = lambda A, B: ev.inner(lo.level, A, B)
        pairs = locate.match_vectors(lo.vecs, hi.vecs, inner)
        cross = [(i, j) for i, j in pairs if lo.neg[i] != hi.neg[j]]
        if any(abs(float(inner(lo.vecs[:, [i]], hi.vecs[:, [j]])[0, 0])) < 0.9 for i, j in cross):
            return dict(out, status='Unresolved', reason='crossing identity')
    return out


S_TESTS = [
    ('S1', dict(), exp_S1, dict(patch=dict(analyse_step=analyse_midpoint))),
    ('S2', dict(genuine_crossing=False, struct_cross=0.9137), exp_S2, dict(plant=dict(tilt_lifts=0.85))),
    ('S3', dict(struct_cross=0.9137), exp_S3, dict(plant=dict(tilt_lifts=0.85))),
    ('S4', dict(bwe_at=UPPER_GUARDS_L3 + [(3, 1.4)]), exp_S4, dict(plant=dict(bwe_at=[]))),
    ('S5', dict(swap_at=UP(0.05)), exp_S5, dict(plant=dict(swap_at=[]))),
    ('S6', dict(quartet_at=(3, 1.01875)), exp_S6, dict(plant=dict(quartet_at=None))),
    ('S7', dict(newton_fail=(3, 'bisection', 0)), exp_S7, dict(plant=dict(newton_fail=None))),
    ('S8', dict(turn=(3, 0.40, 0.95)), exp_S8, dict(plant=dict(turn=(3, 0.40, 0.40)))),
    ('S9', dict(one_real=True), exp_S9, dict(plant=dict(one_real=False))),
    ('S10', dict(tilt_at=(3, 1.025, 0.85)), exp_S10, dict(plant=dict(tilt_at=(3, 1.025, 0.95)))),
    ('S11', dict(slow_at=(3, R3 * 1.01, 0.90)), exp_S11, dict(plant=dict(slow_at=(3, R3 * 1.01, 0.89)))),
    ('S12', dict(r={3: R3, 2: 1.30}), exp_S12, dict(plant=dict(r={3: R3, 2: R2}))),
    ('S13', dict(r={3: R3, 2: 1.0333}), exp_S13, dict(plant=dict(r={3: R3, 2: R2}))),
    ('S14', dict(r={3: 1.0, 2: 1.0}), exp_S14, dict(patch=dict(near_zero_data=near_le0))),
    ('S15', dict(near_spectators=True), exp_S15, dict(patch=dict(K_L=(16,)))),
    ('S16', dict(bwe_at=UPPER_GUARDS_L3, second_root=1.25), exp_S16, dict(plant=dict(second_root=None))),
    ('S17', dict(rotate=True), exp_S17, dict(patch=dict(analyse_step=analyse_individual))),
    ('S18', dict(genuine_crossing=False, struct_cross=0.9137, nB_lag=0.01), exp_S18,
     dict(patch=dict(reading_end=reading_end_off))),
    ('S18b', dict(genuine_crossing=False, struct_cross=0.9237, nB_lag=0.15,
                  tilt_points=[(lv, e, 0.85) for lv in (3, 2) for e in (0.95, 1.0)]), exp_unres_no_balanced,
     dict(patch=dict(reading_end=reading_end_skip))),
    ('S18c', dict(genuine_crossing=False, struct_cross=0.9137, nB_offset_all=1), exp_unres_no_balanced,
     dict(patch=dict(reading_end=reading_end_fallback))),
]


# --- M8.15.2: helpers, the ceiling, and the A plants' expectations (REGISTER_5.md § 2) -------------------------------
THIS = sys.modules[__name__]
QUALIFIER = ('A change of type is located between the registered guard readings. Its identification with the genuine '
             'index crossing at this step is not established: the crossing subspaces agree after removal of the '
             'structural directions, and the full spectral crossing identity remains unresolved. The step\'s '
             'classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count '
             'fell below its side\'s, by a rule whose changed branch has synthetic controls only.')
FAST = 'fast-spectrum dependence, pending independent verification'
DL = 1e-5                                # the coupled lifts' level, delta


def near(a, b, tol=1e-9):
    return a is not None and abs(a - b) <= tol * max(1.0, abs(b))


def r3(x):
    return round(float(x), 3)


def r6(x):
    return round(float(x), 6)


def un(s, reason):
    """An Unresolved step with this whole reason string."""
    return bool(s) and s.get('status') == 'Unresolved' and s.get('reason') == reason


def classes_of(s):
    """A step's crossing classes from its record: each crossing's class or, where the frozen order stopped before the
    classes, the class its two recorded overlaps give."""
    out = []
    for c in s.get('crossings', []):
        if 'class' in c:
            out.append(c['class'])
        else:
            a, b = c['lo_overlap'] >= locate.OVERLAP, c['hi_overlap'] >= locate.OVERLAP
            out.append('structural' if (a and b) else ('genuine' if not (a or b) else 'mixed'))
    return out


def exchanged(s):
    return [m for m in s.get('midpoints', []) if m['role'] == 'exchanged lift']


def rule11_passes(res, levels=(3, 2)):
    return all(s.get('continuity', {}).get('verdict') == 'passes' for lv in levels for s in steps(res, lv))


def comparisons(s, failing=False):
    rows = s.get('continuity', {}).get('comparisons', [])
    return [c for c in rows if not failing or c['degenerate'] or c['statistic'] > locate.TAU_C]


def stat_at(s, e, kind='along the span'):
    """The statistic of a step's one comparison of this kind at the target e, given to six decimals."""
    rows = [c for c in comparisons(s) if c['kind'] == kind and r6(c['point']['eps']) == e]
    return rows[0]['statistic'] if len(rows) == 1 else None


def cross_level(res):
    return any(n.get('name') == UNRES and 'cross-level disagreement' in n.get('reasons', []) for n in res['names'])


def point_at(res, level, e):
    pts = [p for p in res['points'][level] if near(p['eps'], e)]
    return pts[0] if len(pts) == 1 else None


def ceiling(res):
    """The ceiling, applied in adjudication from the record, in the terms' words (REGISTER_5.md § 1 item 5): M8.15.1's
    clauses 1 and 2, unchanged, then clause 3. One adjudicated name per matched genuine step, beside the record's."""
    out = []
    for sn in res['steps_named']:
        nm = sn['name']
        if nm['name'] != LOCATED:
            out.append(dict(name=nm['name'], reasons=list(nm.get('reasons', [])), record_name=nm['name']))
            continue
        rd = nm['readings']
        pts = {lv: {p['eps']: p for p in res['points'][lv]} for lv in (3, 2)}
        # clause 1: a reading has an unbalanced point, in its offset guard's record or, for a region end, at the
        # rerun ladder's points at that eps
        c1 = False
        for side in ('lower', 'upper'):
            r = rd[side]
            if r['kind'] == 'offset':
                g = [x for x in sn['guards'] if x['kind'] == 'offset' and x['side'] == side and x['d'] == r['d']][0]
                c1 = c1 or not (g['point3']['balanced'] and g['point2']['balanced'])
            else:
                c1 = c1 or not all(pts[lv].get(r[key], {}).get('balanced', False) for lv, key in ((3, 'eps3'), (2, 'eps2')))
        # clause 2: an unbalanced point between the readings, outside the reading interval of every genuine or
        # structural step at its level; every evaluated point at that level is read
        c2 = False
        for lv, key in ((3, 'eps3'), (2, 'eps2')):
            windows = [s['reading'] for s in res['levels'][lv]['steps'] if s['status'] in ('genuine', 'structural')]
            for e, p in pts[lv].items():
                inside = any(w[0] <= e <= w[1] for w in windows)
                if rd['lower'][key] <= e <= rd['upper'][key] and not p['balanced'] and not inside:
                    c2 = True
        # clause 3: a genuine step that is a branch step at either level, whose readings locate a change of type
        branch = [s for s in (sn['step3'], sn['step2']) if s.get('branch_step')]
        if c1 or c2:
            out.append(dict(name=UNRES, reasons=[FAST], clauses=[k for k, f in ((1, c1), (2, c2)) if f],
                            record_name=nm['name']))
        elif branch:
            out.append(dict(name=QUALIFIER, clauses=[3], record_name=nm['name']))
        else:
            out.append(dict(name=LOCATED, clauses=[], record_name=nm['name']))
    return out


def adjudicated(res):
    return [x['name'] for x in ceiling(res)]


# A1: each level's steps as tabled, (status, reason, branch step, exchanged-lift points passed, classes)
def G(branch=True, x=0):
    return ('genuine', None, branch, x, 'genuine')


SUB, BOOK = ('Unresolved', 'structural subspace', False, 0, None), ('Unresolved', 'index bookkeeping', False, 0, 'structural')
A1_TABLE = {
    (+1, 0.3): ([G()], [G(False)], True),
    (+1, 1): ([G()], [('Unresolved', 'crossing identity', False, 0, 'mixed')], False),
    (+1, 2): ([('Unresolved', 'mixed overlap', True, 0, 'mixed')], [G()], False),
    (+1, 2.5): ([G(x=1)], [G()], True),
    (+1, 3): ([G()], [G(x=1)], True),
    (+1, 4): ([G(x=1)], [G(x=2)], True),
    (+1, 6): ([G(x=2)], [SUB, BOOK], False),
    (-1, 0.3): ([G(False)], [G()], True),
    (-1, 1): ([G()], [G()], True),
    (-1, 2): ([G()], [('Unresolved', 'mixed overlap', True, 0, 'mixed')], False),
    (-1, 2.5): ([G()], [G()], True),
    (-1, 3): ([G(x=1)], [G(x=1)], True),
    (-1, 4): ([G(x=2)], [G(x=1)], True),
    (-1, 6): ([G(x=1)], [BOOK, SUB], False),
}


def steps_as(st, want):
    if len(st) != len(want):
        return False
    for s, (status, reason, br, nx, cl) in zip(st, want):
        if s['status'] != status or s.get('reason') != reason or bool(s.get('branch_step')) != br:
            return False
        if len(exchanged(s)) != nx or (cl is not None and set(classes_of(s)) != {cl}):
            return False
    return True


def exp_A1(results):
    c = []
    for (sg, q), res in results.items():
        lab = f'{sg:+d}, {q:g}'
        t3, t2, located = A1_TABLE[(sg, q)]
        for lv, want in ((3, t3), (2, t2)):
            c.append((f'{lab}: level {lv} steps as tabled', steps_as(steps(res, lv), want)))
        if not located:
            c.append((f'{lab}: cross-level disagreement', cross_level(res)))
            continue
        for lv, r in ((3, R3), (2, R2)):
            g = steps(res, lv, 'genuine')
            s = g[0] if len(g) == 1 else {}
            c.append((f'{lab}: level {lv}, one genuine step, dn(L) {2 * sg:+d}, dn_S 0', bool(s) and s['dnL'] == 2 * sg
                      and s['dnS'] == 0 and s['signed']['genuine'] == 2 * sg))
            c.append((f'{lab}: level {lv}, root within 3e-4 of r', bool(s) and abs(s['root'] - r) <= 3e-4 * r))
        nm = res['steps_named'][0]['name'] if res['steps_named'] else {}
        sh = nm.get('location', {}).get('shift', np.nan)
        c.append((f'{lab}: the shift within 0.2% of +0.50%', abs(sh - 0.0050) <= 0.002))
        lo, hi = reading(res, 'lower'), reading(res, 'upper')
        want = ('Elliptic', 'Hyperbolic') if sg > 0 else ('Hyperbolic', 'Elliptic')
        c.append((f'{lab}: a decided, counting reading on each side, {want[0]} below and {want[1]} above',
                  lo is not None and hi is not None and (lo['verdict'], hi['verdict']) == want))
        c.append((f'{lab}: named with the qualifier, the record keeping its name',
                  named(res) == [LOCATED] and adjudicated(res) == [QUALIFIER]))
    return check(c)


A2_WANT = {0.3: ('structural', None), 1: ('Unresolved', 'crossing identity'), 2: ('Unresolved', 'mixed overlap')}
A28_EXCHANGED = {2.5: True, 3: False, 4: True, 6: True}


def exp_A2(results):
    c = []
    for q, res in results.items():
        for lv in (3, 2):
            st = steps(res, lv)
            c.append((f'kappa {q:g} delta, level {lv}: {A2_WANT[q][0]}' + (f' ({A2_WANT[q][1]})' if A2_WANT[q][1] else ''),
                      len(st) == 1 and (st[0]['status'], st[0].get('reason')) == A2_WANT[q]))
            c.append((f'kappa {q:g} delta, level {lv}: never genuine', not steps(res, lv, 'genuine')))
    return check(c)


def exp_A28(results):
    c = []
    for q, res in results.items():
        for lv in (3, 2):
            st = steps(res, lv)
            s = st[0] if len(st) == 1 else {}
            c.append((f'kappa {q:g} delta, level {lv}: structural, a branch step', s.get('status') == 'structural'
                      and s.get('branch_step') is True))
            c.append((f'kappa {q:g} delta, level {lv}: exchanged-lift points passed: {A28_EXCHANGED[q]}',
                      bool(s) and bool(exchanged(s)) == A28_EXCHANGED[q]))
            c.append((f'kappa {q:g} delta, level {lv}: never genuine', not steps(res, lv, 'genuine')))
    return check(c)


def exp_A3(res):
    s3, s2 = steps(res, 3), steps(res, 2)
    return check([('level 3: Unresolved (genuine and structural crossings in one step), a branch step', len(s3) == 1
                   and un(s3[0], 'genuine and structural crossings in one step') and s3[0].get('branch_step') is True),
                  ('level 2: a structural step at 1.0127 and a genuine step', len(s2) == 2
                   and s2[0]['status'] == 'structural' and abs(s2[0]['root'] - 1.0127) <= 1e-3 * 1.0127
                   and s2[1]['status'] == 'genuine'),
                  ('the bracket: cross-level disagreement', cross_level(res))])


def exp_A4(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    m = [x for x in s.get('midpoints', []) if x['role'] == 'failed its checks, matches neither end']
    return check([('level 3: Unresolved (passed midpoint matches neither end)', un(s, 'passed midpoint matches neither end')),
                  ("the passed midpoint at 1.025, its n(L) 6", len(m) == 1 and near(m[0]['eps'], 1.025) and m[0]['nL'] == 6)])


def exp_A5(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    gc = s.get('identity_cosines_genuine', {})
    return check([('level 3: Unresolved (crossing identity)', un(s, 'crossing identity')),
                  ('outside P and in full, cos 30 degrees = 0.866', bool(gc) and r3(min(gc['outside_P'])) == 0.866
                   and r3(min(gc['full'])) == 0.866)])


def exp_A6(res):
    s = [x for x in steps(res, 3) if near(x['lo'], 1.0) and near(x['hi'], 1.025)]
    a, b = point_at(res, 3, 1.0), point_at(res, 3, 1.025)
    return check([('level 3: the sub-interval 1.0 to 1.025 with ends (3, 3) and (3, 1)', a is not None and b is not None
                   and (a['nL'], a['nS'], b['nL'], b['nS']) == (3, 3, 3, 1)),
                  ("M8.15.1's terminal branch: that sub-interval Unresolved (structural subspace) at its failing midpoint "
                   '1.0125', len(s) == 1 and un(s[0], 'structural subspace') and near(s[0].get('failed_at'), 1.0125))])


def exp_A7(reason):
    def f(res):
        s3 = steps(res, 3)
        s = s3[0] if len(s3) == 1 else {}
        return check([(f'level 3: terminal at 1.025, Unresolved with {reason} among the reasons', bool(s)
                       and s['status'] == 'Unresolved' and reason in s.get('reason', '').split(', ')
                       and near(s.get('failed_at'), 1.025))])
    f.__name__ = f'exp_A7_{reason.replace(" ", "_")}'
    return f


def exp_A8(res):
    """Passed: the step located as S10's new expectation, not a branch step; the midpoint fails the slowest pair alone."""
    return passed_at_1025(res, ['slowest pair overlap'])


def exp_A19(res):
    """Passed: as A8, the midpoint failing both passable checks."""
    return passed_at_1025(res, ['structural subspace', 'slowest pair overlap'])


def exp_A9(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    m = [x for x in s.get('midpoints', []) if x['role'] == "clean, neither side's counts"]
    lo = point_at(res, 3, 1.0)
    return check([("level 3: Unresolved (neither side's counts after a failure)", un(s, "neither side's counts after a failure")),
                  ("the clean midpoint 1.0125 carries (4, 4): the lower side's n(L), with n_S above its (4, 3)",
                   len(m) == 1 and near(m[0]['eps'], 1.0125) and (m[0]['nL'], m[0]['nS']) == (4, 4)
                   and lo is not None and (lo['nL'], lo['nS']) == (4, 3))])


def exp_duplicate(agree):
    def f(res):
        c = []
        for lv in (3, 2):
            st = steps(res, lv)
            s = st[0] if len(st) == 1 else {}
            d = s.get('continuity', {}).get('duplicates', [])
            mids = s.get('midpoints', [])
            c.append((f'level {lv}: the bisection starts across 0.95 to 1.05', bool(s) and near(s['start'][0], 0.95)
                      and near(s['start'][1], 1.05)))
            c.append((f'level {lv}: its first midpoint re-evaluates 1.0', bool(mids) and near(mids[0]['eps'], 1.0)))
            c.append((f'level {lv}: the clean window within a cell', bool(s)
                      and s['clean_ends'][1] - s['clean_ends'][0] <= 0.05))
            c.append((f'level {lv}: Unresolved (solution continuity, duplicate target)',
                      un(s, 'solution continuity, duplicate target')))
            if agree:
                c.append((f'level {lv}: its records at 1.0 agreeing value for value', len(d) == 1 and near(d[0]['target'], 1.0)
                          and d[0]['agree'] is True))
            else:
                c.append((f'level {lv}: its records at 1.0 differing by 1e-5', len(d) == 1 and near(d[0]['target'], 1.0)
                          and d[0]['agree'] is False and abs(d[0]['m_spread'] - 1e-5) <= 1e-9))
        return check(c)
    f.__name__ = 'exp_A10' if agree else 'exp_A25'
    return f


def exp_A11a(res):
    return check([('a collision: an index crossing located; the change of type remains unresolved',
                   any(n.get('name') == UNRES and 'collision' in n.get('reasons', []) for n in res['names'])
                   and LOCATED not in named(res))])


def exp_A11b(res):
    sn = res['steps_named'][0] if res['steps_named'] else {}
    s3 = sn.get('step3', {})
    unb = [u for u in sn.get('unbalanced_between', []) if u['level'] == 3 and near(u['eps'], 1.0125)]
    adj = ceiling(res)
    return check([('the unbalanced point at 1.0125 lies between the readings', len(unb) == 1),
                  ("inside the genuine step's reading interval, so clause 2 exempts it", bool(s3)
                   and s3['reading'][0] <= 1.0125 <= s3['reading'][1]),
                  ("located with the qualifier, without clause 2's words", named(res) == [LOCATED]
                   and [a['name'] for a in adj] == [QUALIFIER] and adj[0]['clauses'] == [3])])


def exp_A12(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    passed = [m['eps'] for m in s.get('midpoints', []) if m['role'] == 'failed its checks, passed']
    return check([('level 3: both n(L) ends failing points', bool(s) and near(s['nL_ends'][0], 1.0125)
                   and near(s['nL_ends'][1], 1.01328125) and len(passed) == 2),
                  ('level 3: classified between the clean ends 1.0 and 1.0140625', bool(s) and near(s['clean_ends'][0], 1.0)
                   and near(s['clean_ends'][1], 1.0140625)),
                  ('level 3: genuine, a branch step', s.get('status') == 'genuine' and s.get('branch_step') is True),
                  ('level 2: genuine', len(steps(res, 2, 'genuine')) == 1),
                  ('located, with the qualifier', named(res) == [LOCATED] and adjudicated(res) == [QUALIFIER])])


def exp_A13(res):
    sn = res['steps_named'][0] if res['steps_named'] else {}
    return check([("clause 3's trigger at level 3 only", bool(sn) and sn['step3'].get('branch_step') is True
                   and sn['step2'].get('branch_step') is False and sn.get('clause3_trigger') is True),
                  ('the qualifier applies', adjudicated(res) == [QUALIFIER])])


def exp_A14(res):
    c = []
    for lv in (3, 2):
        g = steps(res, lv, 'genuine')
        c.append((f'level {lv}: genuine, a branch step', len(g) == 1 and g[0].get('branch_step') is True))
    kap = 7.5 * DL
    rH = {lv: r - kap ** 2 / (0.05 * DL) for lv, r in ((3, 1.0120), (2, 1.0130))}     # the n(L) change
    g01 = [x for x in guards(res, 'lower', 'offset') if x['d'] == 0.01]
    s3, s2 = (steps(res, 3, 'genuine') or [{}])[0], (steps(res, 2, 'genuine') or [{}])[0]
    c.append(('the lower guards at d = 0.01 lie between the n(L) change and the root and do not count', len(g01) == 1
              and bool(s3) and bool(s2) and rH[3] < g01[0]['eps3'] < s3['root'] and rH[2] < g01[0]['eps2'] < s2['root']
              and g01[0].get('counting') is False))
    lo, hi = reading(res, 'lower'), reading(res, 'upper')
    c.append(('the lower reading from d = 0.02, Hyperbolic', lo is not None and lo['kind'] == 'offset' and lo['d'] == 0.02
              and lo['verdict'] == 'Hyperbolic'))
    c.append(('the upper reading Elliptic', hi is not None and hi['verdict'] == 'Elliptic'))
    c.append(('located, with the qualifier', named(res) == [LOCATED] and adjudicated(res) == [QUALIFIER]))
    return check(c)


def exp_A15(res):
    g = steps(res, 2, 'genuine')
    gc = g[0].get('identity_cosines_genuine', {}) if len(g) == 1 else {}
    return check([('level 2: genuine, a branch step', len(g) == 1 and g[0].get('branch_step') is True),
                  ('the full cosine at 0.746', bool(gc) and r3(min(gc['full'])) == 0.746),
                  ('the cosine outside P at 1.000', bool(gc) and r3(min(gc['outside_P'])) == 1.0),
                  ('named with the qualifier, never with a positive identification', named(res) == [LOCATED]
                   and adjudicated(res) == [QUALIFIER])])


def exp_A16(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    return check([('level 3: Unresolved (clean window over one grid cell)', un(s, 'clean window over one grid cell')),
                  ('clean ends 0.9 and 1.013086', bool(s) and r6(s['clean_ends'][0]) == 0.9 and r6(s['clean_ends'][1]) == 1.013086),
                  ('level 2: genuine', len(steps(res, 2, 'genuine')) == 1),
                  ('the bracket: cross-level disagreement', cross_level(res))])


def exp_A17(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    gc = s.get('identity_cosines_genuine', {})
    return check([('level 3: Unresolved (crossing identity), a branch step', un(s, 'crossing identity')
                   and s.get('branch_step') is True),
                  ('outside P 0.891', bool(gc) and r3(min(gc['outside_P'])) == 0.891),
                  ('though the full cosine passes at 0.911', bool(gc) and r3(min(gc['full'])) == 0.911)])


def exp_A18(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    gc = s.get('identity_cosines_genuine', {})
    return check([('level 3: Unresolved (crossing identity), a branch step', un(s, 'crossing identity')
                   and s.get('branch_step') is True),
                  ('the wrong pairing at a full cosine of 0.911', bool(gc) and r3(min(gc['full'])) == 0.911),
                  ('the cosine outside P recorded below 0.9', bool(gc) and min(gc['outside_P']) < 0.9)])


def exp_A20(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    x = stat_at(s, 1.015625)
    return check([('level 3: Unresolved (solution continuity)', un(s, 'solution continuity')),
                  ('at 1.015625 the statistic reads 0.546, that comparison recorded', x is not None and r3(x) == 0.546)])


def exp_A21(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    a, b = stat_at(s, 1.0125), stat_at(s, 1.013281)
    x = [c['statistic'] for c in comparisons(s) if c['kind'] == 'across the step']
    return check([('level 3: Unresolved (solution continuity)', un(s, 'solution continuity')),
                  ('along the span at 1.0125: 0.0259', a is not None and abs(a - 0.0259) <= 5e-5),
                  ('along the span at 1.013281: 0.120', b is not None and abs(b - 0.120) <= 5e-4),
                  ('across the step: 0.0241', len(x) == 1 and x[0] is not None and abs(x[0] - 0.0241) <= 5e-5)])


def exp_A22(res):
    ok, bad = exp_A1({(+1, 2.5): res})
    c = [(f'as A1: {b}', False) for b in bad] or [('as A1, slope sign +1, kappa/delta 2.5', True)]
    lg = [s['continuity']['largest'] for lv in (3, 2) for s in steps(res, lv) if 'continuity' in s]
    c.append(('rule 11 passes', rule11_passes(res)))
    c.append(('at most 3.46e-4', bool(lg) and max(lg) <= 3.465e-4))
    return check(c)


def exp_A23(res):
    c = []
    for lv, r in ((3, R3), (2, R2)):
        st = steps(res, lv)
        c.append((f'level {lv}: two steps, structural and genuine', [s['status'] for s in st] == ['structural', 'genuine']))
        c.append((f'level {lv}: the structural step at 1.005, its bisection split from the genuine one', len(st) == 2
                  and abs(st[0]['root'] - 1.005) <= 1e-3 * 1.005 and st[0]['start'] == st[1]['start']))
        c.append((f'level {lv}: the genuine step as in S1', genuine_step_ok(res, lv, r)))
    c.append(('located as S3', named(res) == [LOCATED]))
    c.append(('rule 11 passes through the registered comparisons', rule11_passes(res)))
    return check(c)


def exp_A24(res):
    c = []
    for lv in (3, 2):
        st = steps(res, lv)
        c.append((f'level {lv}: both steps Unresolved (solution continuity)', len(st) == 2
                  and all(un(s, 'solution continuity') for s in st)))
        for s in st:
            # the switch's entry and exit: the first pool points rule 11 read inside the switched targets and after them
            tg = sorted({q['eps'] for x in comparisons(s) for q in [x['point']] + x['predictors']})
            entry = min((e for e in tg if 1.0025 < e < 1.0058), default=None)
            exit_ = min((e for e in tg if e > 1.0058), default=None)
            bad = [b['point']['eps'] for b in comparisons(s, failing=True)]
            c.append((f'level {lv}, the step at {s["lo"]:.6f}: failing at the switch\'s entry and exit', entry is not None
                      and exit_ is not None and any(near(e, entry) for e in bad) and any(near(e, exit_) for e in bad)))
    return check(c)


def exp_A26(res):
    c = []
    for lv in (3, 2):
        st = steps(res, lv)
        s = st[0] if len(st) == 1 else {}
        first = comparisons(s)[:1]
        c.append((f'level {lv}: Unresolved (solution continuity)', un(s, 'solution continuity')))
        c.append((f'level {lv}: the first compared point, 0.8125, has one point below it', len(first) == 1
                  and near(first[0]['point']['eps'], 0.8125) and first[0]['degenerate'] == 'fewer than two pool points below'
                  and len(first[0]['predictors']) == 1))
    return check(c)


def exp_A27(res):
    s3, s2 = steps(res, 3), steps(res, 2)
    a3, b3 = (s3 + [{}, {}])[:2]
    a2, b2 = (s2 + [{}, {}])[:2]
    return check([
        ('level 3: Unresolved (structural subspace) on 1.0 to 1.025, failing at 1.0125', len(s3) == 2
         and un(a3, 'structural subspace') and near(a3['lo'], 1.0) and near(a3['hi'], 1.025)
         and near(a3.get('failed_at'), 1.0125)),
        ('level 3: Unresolved (index bookkeeping) on 1.025781 to 1.026562, classes structural, dn(L) = dn_S = +2, dh = +2',
         un(b3, 'index bookkeeping') and r6(b3['lo']) == 1.025781 and r6(b3['hi']) == 1.026562
         and set(classes_of(b3)) == {'structural'} and (b3['dnL'], b3['dnS'], b3['dh']) == (2, 2, 2)),
        ('level 2: Unresolved (structural subspace) on 1.0125 to 1.025', len(s2) == 2 and un(a2, 'structural subspace')
         and near(a2['lo'], 1.0125) and near(a2['hi'], 1.025)),
        ('level 2: Unresolved (index bookkeeping) on 1.030469 to 1.03125, classes structural',
         un(b2, 'index bookkeeping') and r6(b2['lo']) == 1.030469 and r6(b2['hi']) == 1.03125
         and set(classes_of(b2)) == {'structural'}),
        ('no genuine crossing detected at both levels', all(f'no genuine crossing detected at level {lv}' in all_names(res)
                                                           for lv in (3, 2)))])


def exp_A29(res):
    s3 = steps(res, 3)
    s = s3[0] if len(s3) == 1 else {}
    x = exchanged(s)
    return check([('level 3: Unresolved (genuine and structural crossings in one step), a branch step',
                   un(s, 'genuine and structural crossings in one step') and s.get('branch_step') is True),
                  ('the clean midpoint 1.0125, (3, 2), passed as an exchanged-lift point', len(x) == 1
                   and near(x[0]['eps'], 1.0125) and (x[0]['nL'], x[0]['nS']) == (3, 2)),
                  ('the classification between 1.0 and 1.013281', bool(s) and near(s['clean_ends'][0], 1.0)
                   and r6(s['clean_ends'][1]) == 1.013281),
                  ('meets both crossings', set(classes_of(s)) == {'genuine', 'structural'})])


def with_rule11(expect):
    """An S test's expectation, with rule 11 passing at every step on the default path (REGISTER_5.md § 2)."""
    def f(res):
        ok, bad = expect(res)
        if not rule11_passes(res):
            bad = bad + ['rule 11 passes at every step']
        return (not bad), bad
    f.__name__ = expect.__name__
    return f


# --- M8.15.2's plants and arms (REGISTER_5.md § 2) -----------------------------------------------------------------------
T3 = lambda *pts: [(3, e, 0.85) for e in pts]          # tilts of e0 at level 3
A12_PLANT = dict(tilt_points=T3(1.0125, 1.01328125))
S10_TILT = (3, 1.025, 0.85)
A1_RUNS = [((sg, q), dict(kappa=q * DL, sigma=sg)) for sg in (+1, -1) for q in (0.3, 1, 2, 2.5, 3, 4, 6)]
A2_LIFT = dict(hold=DL, lift_line=(1.0130, 0.05))
CLASS_LINE = "classes.append('structural' if (a and b) else ('genuine' if not (a or b) else 'mixed'))"
OUTSIDE_DROPPED = dict(mutate=[('analyse_step', [('if len(off) < len(gen) or off.min() < OVERLAP:',
                                                  'if len(full) < len(gen) or full.min() < OVERLAP:', 1)])])
CONTINUITY_DROPPED = dict(patch=dict(continuity=lambda steps, log, level: None))
LATEST_KEPT = dict(mutate=[('continuity', [('evals = list(log.get(level, []))',
                                            'evals = list({round(p.eps, 9): p for p in log.get(level, [])}.values())', 1)])])
ARM_DOCS = {}


def arm(label, **kw):
    return dict(label=label, **kw)


A_TESTS = [
    ('A1', A1_RUNS, exp_A1, [
        arm("M8.15.1's terminal branch restored", patch=dict(PASSABLE=())),
        arm("v4's tiered names restored", must_fail=['+1, 0.3'],
            ceiling=[('        elif branch:\n',
                      "        elif branch and min(min(s['identity_cosines_genuine']['full']) for s in branch) < 0.9:\n", 1)]),
        arm('an exchanged-lift point a contradiction, as in v6', must_fail=['+1, 4:', '-1, 4:'],
            mutate=[('bisect', [('elif failed and ep.nL == lo_c.nL and ep.nS < lo_c.nS:', 'elif False:', 1),
                                ('elif failed and ep.nL == hi_c.nL and ep.nS < hi_c.nS:', 'elif False:', 1)])])]),
    ('A2', [(q, dict(A2_LIFT, kappa=q * DL)) for q in (0.3, 1, 2)], exp_A2, [
        arm('every crossing classed genuine', mutate=[('analyse_step', [(CLASS_LINE, "classes.append('genuine')", 2)])])]),
    ('A3', dict(e1_line=(1.0127, 0.01), tilt_points=T3(1.0140625, 1.01328125)), exp_A3, [
        arm('the rule against genuine and structural crossings in one step removed',
            mutate=[('analyse_step', [('if s_gen and s_struct:', 'if False:', 1)])])]),
    ('A4', dict(tilt_at=S10_TILT, glitch=(3, 1.025, -1e-3)), exp_A4, [arm('no glitch', plant=dict(glitch=None))]),
    ('A5', dict(A12_PLANT, turn_out=30), exp_A5, [arm('a turn of 20 degrees', plant=dict(turn_out=20))]),
    ('A6', dict(kappa=8 * DL), exp_A6, [
        arm('the terminal branch removed for ends that share n(L)',
            mutate=[('bisect', [('terminal = lo.nL == hi.nL', 'terminal = False', 1)])])]),
    ('A7(a)', dict(gate_fail=(3, 1.025)), exp_A7('structural span'), [
        arm("the span's gate passable", patch=dict(PASSABLE=locate.PASSABLE + ('structural span',)))]),
    ('A7(b)', dict(cover_fail=(3, 1.025)), exp_A7('spectral coverage'), [
        arm('coverage passable', patch=dict(PASSABLE=locate.PASSABLE + ('spectral coverage',)))]),
    ('A7(c)', dict(gate_fail=(3, 1.025), tilt_at=S10_TILT), exp_A7('structural span'), [
        arm("the span's gate passable", patch=dict(PASSABLE=locate.PASSABLE + ('structural span',)))]),
    ('A8', dict(slow_at=(3, 1.025, 0.95)), exp_A8, [
        arm("a slowest-pair failure made terminal", patch=dict(PASSABLE=('structural subspace',)))]),
    ('A9', dict(tilt_at=S10_TILT, e0_line=(1.004, -0.01), extra=(1.006, 0.05)), exp_A9, [
        arm("a point whose n_S is above its side's also passed",
            mutate=[('bisect', [('ep.nS < lo_c.nS', 'ep.nS != lo_c.nS', 1), ('ep.nS < hi_c.nS', 'ep.nS != hi_c.nS', 1)])])]),
    ('A10', dict(tilt_points=[(lv, 1.0, 0.85) for lv in (3, 2)]), exp_duplicate(True), [
        arm('the latest evaluation kept at a duplicate target', **LATEST_KEPT)]),
    ('A11(a)', dict(A12_PLANT, quartet_at=(3, 1.0125)), exp_A11a, [arm('no quartet', plant=dict(quartet_at=None))]),
    ('A11(b)', dict(A12_PLANT, nB_at=[(3, 1.0125, 1)]), exp_A11b, [
        arm('clause 2 applied to the failing midpoint, in the ceiling function',
            ceiling=[("and not p['balanced'] and not inside:", "and not p['balanced']:", 1)])]),
    ('A12', dict(A12_PLANT), exp_A12, [
        arm('the step classified between its n(L) ends',
            mutate=[('bisect', [('analyse_step(ev, lo_c, hi_c,', 'analyse_step(ev, lo_n, hi_n,', 1)])])]),
    ('A13', dict(A12_PLANT), exp_A13, [
        arm('the qualifier only when both levels trigger, in the ceiling function',
            ceiling=[("branch = [s for s in (sn['step3'], sn['step2']) if s.get('branch_step')]",
                      "branch = [s for s in (sn['step3'], sn['step2']) if s.get('branch_step')] if (sn['step3']"
                      ".get('branch_step') and sn['step2'].get('branch_step')) else []", 1)])]),
    ('A14', dict(kappa=7.5 * DL, sigma=-1, r={3: 1.0120, 2: 1.0130}), exp_A14, [
        arm('every decided guard counting',
            mutate=[('readings', [("x['side'] == side and x.get('decided') and x.get('counting')",
                                   "x['side'] == side and x.get('decided')", 1)])])]),
    ('A15', dict(kappa=2.5 * DL, sigma=-1), exp_A15, [arm('the comparison outside P dropped', **OUTSIDE_DROPPED)]),
    ('A16', dict(tilt_points=[(lv, e, 0.85) for lv in (3, 2) for e in (0.95, 1.0, 0.975, 1.0125)]), exp_A16, [
        arm('rule 10 off', patch=dict(CELL_SLACK=float('inf')))]),
    ('A17', dict(A12_PLANT, a17=(3, 0.905, 27)), exp_A17, [arm('the comparison outside P dropped', **OUTSIDE_DROPPED)]),
    ('A18', dict(A12_PLANT, a17=(3, 0.905, 27), a18=-2e-4), exp_A18, [
        arm('the comparison outside P dropped', **OUTSIDE_DROPPED)]),
    ('A19', dict(tilt_at=S10_TILT, slow_at=(3, 1.025, 0.95)), exp_A19, [
        arm('a midpoint failing both passable checks made terminal',
            mutate=[('bisect', [('if terminal or not set(ep.checks) <= set(PASSABLE):',
                                 'if terminal or not set(ep.checks) <= set(PASSABLE) or len(ep.checks) > 1:', 1)])])]),
    ('A20', dict(m_jump=(1.0150, 9.0, 1e-6)), exp_A20, [
        arm('the bare miss, against a tolerance that clears a grid cell (8.65e-6)',
            mutate=[('continuity', [("bad = [c for c in comps if c['degenerate'] or c['statistic'] > TAU_C]",
                                     "bad = [c for c in comps if c['degenerate'] or c['miss'] > TAU_C * 0.05 ** 2]", 1)])])]),
    ('A21', dict(tilt_points=T3(1.0125), m_jump=(1.0050, 9.0, 1e-5)), exp_A21, [
        arm('the continuity check dropped', **CONTINUITY_DROPPED)]),
    ('A22', dict(kappa=2.5 * DL, slack=True), exp_A22, [
        arm('the target eps as abscissa',
            mutate=[('continuity', [('x = lambda p: float(p.p.eps_reached)', 'x = lambda p: float(p.eps)', 1)])])]),
    ('A23', dict(struct_cross=1.005), exp_A23, [
        arm("each point's predictors taken in evaluation order",
            mutate=[('continuity', [('pts = sorted(evals, key=x)', 'pts = list(evals)', 1)])])]),
    ('A24', dict(struct_cross=1.005, m_jump=(1.0025, 1.0058, 1e-5)), exp_A24, [
        arm('the continuity check dropped', **CONTINUITY_DROPPED),
        arm("the comparisons restricted to the step's final sub-interval",
            mutate=[('continuity', [("lo_s, hi_s = s['start']\n        rd = s.get('reading')\n        if rd:\n"
                                     "            lo_s, hi_s = min(lo_s, rd[0]), max(hi_s, rd[1])\n",
                                     "lo_s, hi_s = s['lo'], s['hi']\n        rd = s.get('reading')\n", 1)])])]),
    ('A25', dict(tilt_points=[(lv, 1.0, 0.85) for lv in (3, 2)], reeval_J=1e-5), exp_duplicate(False), [
        arm('the latest evaluation kept', **LATEST_KEPT)]),
    ('A26', dict(region=(0.8, 1.4), r={3: 0.82, 2: 0.8241}), exp_A26, [
        arm('a degenerate comparison skipped',
            mutate=[('continuity', [("bad = [c for c in comps if c['degenerate'] or c['statistic'] > TAU_C]",
                                     "bad = [c for c in comps if not c['degenerate'] and c['statistic'] > TAU_C]", 1)])])]),
    ('A27', dict(kappa=8 * DL), exp_A27, [
        arm('the bookkeeping check removed',
            mutate=[('analyse_step', [('if hi.nS - lo.nS != s_struct or hi.h - lo.h != s_gen:', 'if False:', 1)])])]),
    ('A28', [(q, dict(A2_LIFT, kappa=q * DL)) for q in (2.5, 3, 4, 6)], exp_A28, [
        arm('every crossing classed genuine', mutate=[('analyse_step', [(CLASS_LINE, "classes.append('genuine')", 2)])])]),
    ('A29', dict(tilt_at=S10_TILT, e1_line=(1.004, 0.01), extra=(1.006, -0.05)), exp_A29, [
        arm('an exchanged-lift point taken as a clean end',
            mutate=[('bisect', [("kept.append(midpoint_record(ep, 'exchanged lift'))\n            lo_n = ep\n",
                                 "kept.append(midpoint_record(ep, 'exchanged lift'))\n            lo_n = lo_c = ep\n", 1),
                                ("kept.append(midpoint_record(ep, 'exchanged lift'))\n            hi_n = ep\n",
                                 "kept.append(midpoint_record(ep, 'exchanged lift'))\n            hi_n = hi_c = ep\n", 1)])])]),
]


TESTS = [(name, plant, with_rule11(expect), [dict(label=('plant ' if 'plant' in a else 'patch ') + 'arm', **a)])
         for name, plant, expect, a in S_TESTS] + A_TESTS


def run_one(plant_kw, label='primary'):
    return mock.run(mock.Plant(**plant_kw), label)


def evaluate(plant, expect, a=None):
    """One run of a test (its parent, or one arm): the plant or plants under the arm's changes, read by its expectation
    while those changes hold. Returns (passed, failed checks, names)."""
    a = a or {}
    patch = dict(a.get('patch', {}))
    for fn, edits in a.get('mutate', []):
        patch[fn] = mutant(locate, fn, edits)
    cpatch = dict(ceiling=mutant(THIS, 'ceiling', a['ceiling'])) if a.get('ceiling') else {}
    with Patch(**patch), Patch(module=THIS, **cpatch):
        if isinstance(plant, dict):
            res = run_one(dict(plant, **a.get('plant', {})))
            ok, bad = expect(res)
            names = res['names']
        else:
            results = {lab: run_one(dict(kw, **a.get('plant', {}))) for lab, kw in plant}
            ok, bad = expect(results)
            names = {str(lab): r['names'] for lab, r in results.items()}
    return ok, bad, names


def main():
    os.makedirs(OUT, exist_ok=True)
    results, lines = [], []
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines.append(f'REGISTER_5.md § 2, the synthetic tests, {stamp}')
    for name, plant, expect, arms in TESTS:
        ok, bad, names = evaluate(plant, expect)
        entry = dict(test=name, parent=dict(passed=ok, failed=bad, names=names), arms=[])
        if ok:
            for a in arms:
                ok_a, bad_a, names_a = evaluate(plant, expect, a)
                must = a.get('must_fail', [])
                caught = (not ok_a) and all(any(m in b for b in bad_a) for m in must)
                entry['arms'].append(dict(label=a['label'], caught=caught, failed_checks=bad_a, must_fail=must,
                                          names=names_a))
        else:
            entry['arms'] = [dict(label=a['label'], caught=None, note='not run: the parent failed') for a in arms]
        entry['passed'] = bool(ok and all(x['caught'] for x in entry['arms']))
        results.append(entry)
        arm_txt = '; '.join(f'{x["label"]}: ' + ('caught' if x['caught'] else 'NOT CAUGHT' if x['caught'] is False
                                                  else 'not run') for x in entry['arms'])
        lines.append(f'  {"PASS" if entry["passed"] else "FAIL"}  {name}: parent {"ok" if ok else "FAILED " + str(bad)}; '
                     f'arms: {arm_txt}')
    n = sum(r['passed'] for r in results)
    lines.append(f'synthetic tests: {n} of {len(results)} pass, each arm caught' if n == len(results)
                 else f'synthetic tests: {n} of {len(results)} pass')
    json.dump(dict(stamp=stamp, register='REGISTER_5.md v3', decide_sha256=mock.mock_decide()[1], results=results),
              open(os.path.join(OUT, 'synthetic.json'), 'w'), indent=1, default=str)
    open(os.path.join(OUT, 'synthetic.log'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    return n == len(results)


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
