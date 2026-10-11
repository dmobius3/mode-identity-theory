"""REGISTER_4.md v3 § 2: the synthetic tests S1 to S17 on the mock evaluator, each with its mutation arm.

Each test runs its parent and checks the registered expectation; then its arm, whose expectation must fail. The parent
passes before its arm runs.

  python3 tests/synthetic.py        writes out/synthetic.json and out/synthetic.log"""
import os, sys, json, copy, datetime
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


def exp_S10(res):
    st = [s for s in steps(res, 3) if s['status'] == 'Unresolved']
    return check([('the level-3 step Unresolved (structural subspace) over the bracket reached', len(st) == 1
                   and 'structural subspace' in st[0]['reason'] and st[0]['lo'] < 1.0130 < st[0]['hi']),
                  ('no located change of type', LOCATED not in named(res))])


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
    """A temporary change to the locator, for the arms that act on the locator rather than the plant."""
    def __init__(self, **kw):
        self.kw, self.saved = kw, {}

    def __enter__(self):
        for k, v in self.kw.items():
            self.saved[k] = getattr(locate, k)
            setattr(locate, k, v)

    def __exit__(self, *a):
        for k, v in self.saved.items():
            setattr(locate, k, v)


_orig_near = locate.near_zero_data
_orig_analyse = locate.analyse_step


def near_le0(vals, vecs, P, inner, tolL, d):
    out = _orig_near(vals, vecs, P, inner, tolL, d)
    out['neg'] = vals <= 0
    return out


def analyse_midpoint(ev, lo, hi, pool=None):
    """S1's arm (REGISTER_4.md, amendment on S1's arm): the root taken as the final interval's midpoint."""
    out = _orig_analyse(ev, lo, hi, pool)
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


def analyse_individual(ev, lo, hi, pool=None):
    """S17's arm: identity by individual overlaps of at least 0.9, with no subspace check."""
    out = _orig_analyse(ev, lo, hi, pool)
    if out.get('status') in ('genuine', 'structural'):
        inner = lambda A, B: ev.inner(lo.level, A, B)
        pairs = locate.match_vectors(lo.vecs, hi.vecs, inner)
        cross = [(i, j) for i, j in pairs if lo.neg[i] != hi.neg[j]]
        if any(abs(float(inner(lo.vecs[:, [i]], hi.vecs[:, [j]])[0, 0])) < 0.9 for i, j in cross):
            return dict(out, status='Unresolved', reason='crossing identity')
    return out


TESTS = [
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


def run_one(plant_kw, patch=None, label='primary'):
    with Patch(**(patch or {})):
        return mock.run(mock.Plant(**plant_kw), label)


def main():
    os.makedirs(OUT, exist_ok=True)
    results, lines = [], []
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines.append(f'REGISTER_4.md § 2, the synthetic tests, {stamp}')
    for name, plant_kw, expect, arm in TESTS:
        res = run_one(plant_kw)
        ok, bad = expect(res)
        entry = dict(test=name, parent=dict(passed=ok, failed=bad, names=res['names']), decide_sha256=res['decide_sha256'])
        if ok:
            kw = dict(plant_kw, **arm.get('plant', {}))
            res_a = run_one(kw, arm.get('patch'))
            ok_a, bad_a = expect(res_a)
            entry['arm'] = dict(caught=not ok_a, failed_checks=bad_a, names=res_a['names'])
        else:
            entry['arm'] = dict(caught=None, note='not run: the parent failed')
        entry['passed'] = bool(ok and entry['arm']['caught'])
        results.append(entry)
        lines.append(f'  {"PASS" if entry["passed"] else "FAIL"}  {name}: parent {"ok" if ok else "FAILED " + str(bad)}; '
                     f'arm {"caught" if entry["arm"]["caught"] else "NOT CAUGHT" if entry["arm"]["caught"] is False else "not run"}'
                     + (f' ({entry["arm"]["failed_checks"]})' if entry['arm'].get('failed_checks') else ''))
    n = sum(r['passed'] for r in results)
    lines.append(f'synthetic tests: {n} of {len(results)} pass, each arm caught' if n == len(results)
                 else f'synthetic tests: {n} of {len(results)} pass')
    json.dump(dict(stamp=stamp, results=results), open(os.path.join(OUT, 'synthetic.json'), 'w'), indent=1, default=str)
    open(os.path.join(OUT, 'synthetic.log'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    return n == len(results)


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
