#!/usr/bin/env python3
"""Tests 5 and 7: classification and identity, and the locator, on synthetic records, with no solve (M8.18's terms: THE
TESTS BEFORE THE FREEZE, tests 5 and 7; ARM A, Classifying a point and Locating a change of type; ARM B).

Usage: test_locator.py

It runs in a seedcheck process, where every solver and record path of the instrument refuses. census_lib.locate runs
whole, the recomputed path and its reproduction included, on a synthetic instrument (Fake): per cutoff, n(L) as a
step function of eps, the type the rule reads, K1, the two ends' solutions and the records a recomputed point must
equal. Each record carries the fields census_lib reads, so checks.k1, census_lib.nl_at and census_lib.here read it as
they read the instrument's.

Test 5. A point classified on Arm A's ladder is the baseline. Each condition has an arm, a counterexample the real code
refuses and a mutation of census_lib's source that lets it through: K1 at each cutoff, the rule's verdict, each identity
pair, with M8.17's stored distance at T5/R2's 128 the counterexample for the first, and the type from N = 40.

Test 7. M8.17's arms carry over, on both ladders: on each, a clean bracket (20, 30), with n(L) changing by +1 at 25.004
at every cutoff and the type the rule reads changing there, must be Located, with its name. The conditions: w/2, the
union's w, the guards' first offset and their single retry, the window bound, the two-ends agreement in distance and in
n(L), a bracket end that does not reproduce or has no record, the overlap, the signed change and its being nonzero, the
two-change stop, K1 at a midpoint, the type and index brackets, the unchanged index and the inadequate index evidence,
each guard continued from its own bracket end, and the reported cutoff failing alone, which must not block Located.

With moved = None, census_lib.bisect must equal M8.17's, loaded from reference/, on every model above.

The moved midpoint has its own arms:
  M1. K1 fails at a midpoint and holds at the moved point: the moved point counts, and the refused midpoint stays in the
      record and decides nothing; with moved = None the same model stops at K1;
  M2. K1 fails at the moved point: an unsuccessful stop, with no second move;
  M3. a solve fails at a midpoint: no move;
  M4. K1 holds at a midpoint: no move;
  M5. M8.17's ten stored midpoints on T4/R5, replayed through a stub solver at each deciding cutoff, reach the stop, and
      the moved point, 8.720990, completes the bisection with n(L) 7 and with 6;
  M6. a mutation of the fraction, and of the end, must fail M5.

A bracket's end outside the twelve has its own arms (census_lib.admissible): its N = 40 record failing K1, failing either
identity, or differing from M8.17's type or any index, each refused, and each let through by a mutation; the record's
last claim shows the bracket not located and the end's classification unchanged.

The record, end to end: census_lib.classify_rows, jobs and assemble run on M8.17's CENSUS.json with synthetic outputs of
this run's rows, each synthetic point a copy of M8.17's stored records with the reading the scenario sets:
  R1. the replay's pattern: T1/R4 and T1/R5 'Elliptic throughout', T4/R4 with one job, (4, 5.66), and not settled at 72,
      T4/R5 located by Arm B, T5/R2 not settled, 128 and 132 named;
  R2. a gate stops Arm A: no job, each of the twelve keeping M8.17's causes with the gate named, and no row moved;
  R3. T4/R4 at 4 Unresolved: no job, the change across 4 not located;
  R4. a borrowed end refused: T4/R4's bracket not located, the row not settled, 5.66 still Hyperbolic.
"""
import copy
import importlib.util
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import census_lib as lib  # noqa: E402
import cases as cs  # noqa: E402
import census  # noqa: E402

out = []
CASE = dict(chains=4)
WINDOW = [5.0, 10.0, 20.0, 30.0, 40.0]
CH = dict(kind='type', lo=20.0, hi=30.0, lo_type='Elliptic', hi_type='Hyperbolic', between=[])
A, B = lib.ARM_A, lib.ARM_B
KEPT = dict(aligned_distance=0.0, same_record=True, kept=True)


def say(s=''):
    print(s, flush=True)
    out.append(s)


class Model:
    """A synthetic branch. nl(N, e): n(L) of the solution continued from below; nl_up(N, e): from above (by default the
    same); unres(N, e): n(L) unresolved; typ(e): the type the rule reads, None for Unresolved; k1(N, e); split(N, e):
    the two ends' distance; ref_bad(e): 'missing' or 'differs' at a recomputed point; fail(N, e): the solve fails."""

    def __init__(self, change=None, dn=None, tau=25.004, wrong=(), unclassified=(), k1_fail=None, split=None,
                 nl_up=None, unres=None, nl=None, typ=None, ref_bad=None, typ_up=None, fail=None):
        self.change = {N: 25.004 for N in (16, 24, 32, 40)} | (change or {})
        self.dn = {N: 1 for N in (16, 24, 32, 40)} | (dn or {})
        self.tau, self.wrong, self.unclassified = tau, wrong, unclassified
        self.k1_fail, self.split_, self.nl_up_, self.unres_ = k1_fail or {}, split or {}, nl_up or {}, unres or {}
        self._nl, self._typ, self.ref_bad, self.typ_up, self.fail_ = nl, typ, ref_bad or (lambda e: None), typ_up, fail or {}

    def nl(self, N, e):
        if self._nl:
            return self._nl(N, e)
        return 3 + (self.dn[N] if e >= self.change[N] else 0)

    def nl_up(self, N, e):
        f = self.nl_up_.get(N)
        return f(e) if f else self.nl(N, e)

    def unres(self, N, e):
        return any(a <= e <= b for a, b in self.unres_.get(N, ()))

    def typ(self, e):
        if self._typ:
            return self._typ(e)
        if any(a <= e <= b for a, b in self.unclassified):
            return None
        for a, b, t in self.wrong:
            if a <= e <= b:
                return t
        return 'Hyperbolic' if e >= self.tau else 'Elliptic'

    def k1(self, N, e):
        return not any(a <= e <= b for a, b in self.k1_fail.get(N, ()))

    def split(self, N, e):
        return self.split_.get(N, lambda e: 0.0)(e)

    def fails(self, N, e):
        return any(a <= e <= b for a, b in self.fail_.get(N, ()))


class Fake:
    """One cutoff of the synthetic instrument: the interface census_lib.locate takes."""

    def __init__(self, N, model):
        self.N, self.model, self.seed_ok = N, model, True

    def point(self, e, upper):
        m = self.model
        nl = m.nl_up(self.N, e) if upper else m.nl(self.N, e)
        rec = dict(type=m.typ(e) or 'Unresolved', nL=nl, nD=0, K=0, kr=0, kc=0, ki=0, sdim=8, ranks=[4, 0], blocks=4,
                   krein=[], v0_matches=m.k1(self.N, e), separated=True,
                   unresolved=['n(L): an eigenvalue of L lies in its gray zone'] if m.unres(self.N, e) else [])
        return dict(accepted=True, eps_reached=e, lam=48.0 + e, m=e, evaluations=3, floor_rel=0.0, record=rec,
                    seconds=0.0, from_above=upper, summary=dict(groups=[]))

    def step(self, state, e, prev_accepted=True):
        upper = e < state[0]
        if self.model.fails(self.N, e):
            return dict(ok=False, why='synthetic: the solve fails', state=None, c=None, k1=False, nL=None,
                        point=dict(accepted=False, reason='synthetic'))
        p = self.point(e, upper)
        return dict(ok=True, why=None, state=(e, 'chain'), c=None, k1=lib.ck.k1(p, CASE), nL=lib.nl_at(p), point=p)

    def path(self, upto):
        return {lib.key(x): self.step((0.0, 'path'), x) for x in WINDOW if x <= upto}


def readings(model, lad):
    def f(sols):
        pts = {N: (s['point'] if s else None) for N, s in sols.items()}
        e = next(p['eps_reached'] for p in pts.values() if p)
        up = next(p['from_above'] for p in pts.values() if p)
        t = model.typ_up(e) if (up and model.typ_up) else model.typ(e)
        rd = (dict(verdict='converged', type=t, reasons=[], rows=[]) if t and all(pts.values()) else
              dict(verdict='Unresolved', type=None, reasons=['synthetic: the rule reads it Unresolved'], rows=[]))
        return dict(points=pts, reading=rd, identity={lib.pair_key(p): dict(KEPT) for p in lad['pairs']})
    return f


def run(L, model, lad, ch=CH, window=None, moved=None):
    """census_lib.locate (of the module L, the real one or a mutant) on the synthetic instrument, on ladder lad."""
    cuts = {N: Fake(N, model) for N in lad['cutoffs']}
    rd = readings(model, lad)

    def ref(e):
        bad = model.ref_bad(e)
        if bad == 'missing':
            return None
        r = rd({N: Fake(N, model).step((0.0, 'path'), e) for N in lad['cutoffs']})
        if bad == 'differs':
            top = lad['cutoffs'][-1]
            r['points'][top] = dict(r['points'][top], lam=r['points'][top]['lam'] * (1 + 1e-12))
        return r
    try:
        rec, stop = L.locate(ch, window or WINDOW, CASE, cuts, rd, lambda cu, s1, s2: cu.model.split(cu.N, s1['point']['eps_reached']),
                             ref, lad, moved=moved, say=lambda s: None)
    except Exception as e:  # noqa: BLE001
        return dict(located=False, why=f'raised {type(e).__name__}: {e}', crashed=True), None
    return rec, stop


def mutant(src, anchor, new, tag, tmp):
    if src.count(anchor) != 1:
        raise SystemExit(f'the anchor for {tag} occurs {src.count(anchor)} times: {anchor[:50]!r}')
    p = os.path.join(tmp, f'census_lib_{tag}.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(src.replace(anchor, new, 1))
    spec = importlib.util.spec_from_file_location(f'census_lib_{tag}', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def case_of(row):
    return census.roundtrip(cs.serialize(row, dict(cs.CASES[row], points=lib.path_points(row), cutoffs=lib.cutoffs_of(row))))


# --- test 5 --------------------------------------------------------------------------------------------------------
def fake_pt(e=25.0, typ='Elliptic', k1_bad=(), ident=None, verdict='converged', nl=None):
    """A point on Arm A's ladder, from the synthetic records."""
    f = {N: Fake(N, Model()) for N in A['cutoffs']}
    pts = {N: f[N].point(e, False) for N in A['cutoffs']}
    for N in A['cutoffs']:
        pts[N]['record']['type'] = typ
        pts[N]['record']['v0_matches'] = N not in k1_bad
        if nl:
            pts[N]['record']['nL'] = nl[N]
    return dict(points=pts, reading=dict(verdict=verdict, type=typ, reasons=['synthetic'], rows=[]),
                identity=ident or {lib.pair_key(p): dict(KEPT) for p in A['pairs']})


def test5(src, tmp):
    arms = []

    def arm(label, anchor, new, pt):
        tag = f'c{len(arms) + 1}'
        M = mutant(src, anchor, new, tag, tmp)
        real, mut = lib.here(pt, CASE, A), M.here(pt, CASE, A)
        arms.append((label, not real['classified'], mut['classified']))
    k1a = """{p.get('reason', 'no record')}")\n        elif not ck.k1(p, case):\n"""
    for N in A['cutoffs']:
        arm(f'K1 at N = {N}', k1a, """{p.get('reason', 'no record')}")\n        elif False:\n""", fake_pt(k1_bad=(N,)))
    arm("the rule's verdict: Unresolved, with a type in the record", "    elif rd['verdict'] != 'converged':\n",
        '    elif False:\n', fake_pt(verdict='Unresolved'))
    t5 = lib.theirs('T5/R2', ROOT)['identity'][lib.key(128.0)]
    pair_a = ("    for pair in lad['pairs']:\n        idn = pt['identity'].get(pair_key(pair))\n        if not idn:\n"
              "            causes.append(")
    arm(f"the first pair: M8.17's stored distance at T5/R2's 128, {t5['aligned_distance']:.4g}, kept {t5['kept']}", pair_a,
        pair_a.replace("lad['pairs']:", "lad['pairs'][1:]:"), fake_pt(ident={'24-32': t5, '32-40': dict(KEPT)}))
    arm('the second pair: the distance over 10^-2 between N = 32 and 40', pair_a,
        pair_a.replace("lad['pairs']:", "lad['pairs'][:1]:"),
        fake_pt(ident={'24-32': dict(KEPT), '32-40': dict(aligned_distance=0.0104, same_record=True, kept=False)}))
    pt = fake_pt(nl={24: 5, 32: 5, 40: 7})
    M = mutant(src, "    hi = pt['points'][lad['cutoffs'][-1]]\n    out = dict(classified=True",
               "    hi = pt['points'][lad['cutoffs'][0]]\n    out = dict(classified=True", 'cz', tmp)
    arms.append(('the indices from N = 40, not from the lowest cutoff', lib.here(pt, CASE, A)['nL'] == 7, M.here(pt, CASE, A)['nL'] == 5))
    base = lib.here(fake_pt(), CASE, A)
    return base['classified'], arms


# --- test 7: the moved midpoint ----------------------------------------------------------------------------------------
def replay(L, nl_moved):
    """M8.17's midpoints on T4/R5, replayed at each deciding cutoff through a stub solver: {N: bisect result}."""
    known = lib.m817_file(lib.LOCATED_B, ROOT)
    out_ = {}
    for N in B['deciding']:
        stored = {m['eps']: m for m in known['bisection'][str(N)]['midpoints']}

        def solve(state, e):
            m = stored.get(e)
            if m is None:
                return dict(ok=True, why=None, state=state, k1=True, nL=nl_moved, point=dict(eps=e))
            s = m['from_lower' if state == 'lo' else 'from_upper']
            return dict(ok=s['ok'], why=s['why'], state=state, k1=s['k1'], nL=s['nL'], point=s['point'])
        nl = known['nL'][str(N)]
        out_[N] = L.bisect(lib.BRACKET_B[0], lib.BRACKET_B[1], nl[0], nl[1], 'lo', 'hi', solve,
                           lambda s1, s2: stored.get(s1['point'].get('eps_reached'), {}).get('distance') or 0.0, L.MOVED)
    return out_


def replay_ok(L):
    """(ok, detail): both readings complete, at 8.720990, keeping the half the reading says."""
    res = []
    for nl, keep in ((7, 'upper'), (6, 'lower')):
        for N, r in replay(L, nl).items():
            mids = r['midpoints']
            e = mids[-1]['eps']
            want = [8.720990, 8.724874] if keep == 'upper' else [8.718402, 8.720990]
            res.append(r['complete'] and len(mids) == 11 and mids[-1].get('moved') is True and abs(e - 8.720990) < 1e-6
                       and all(abs(x - y) < 1e-6 for x, y in zip(r['interval'], want)) and not mids[-2]['from_lower']['k1'])
    return all(res), res


def moved_arms(src, tmp):
    arms = []
    D1 = B['deciding'][1]
    one = Model(k1_fail={D1: ((24.999, 25.001),)})
    r = run(lib, one, B, moved=lib.MOVED)[0]
    mids = r.get('bisection', {}).get(D1, {}).get('midpoints', [])
    m1_ok = (r['located'] and mids[0]['eps'] == 25.0 and 'moved' not in mids[0] and mids[1].get('moved') is True
             and abs(mids[1]['eps'] - 24.0) < 1e-12 and mids[2]['eps'] == 27.0)
    r0 = run(lib, one, B)[0]
    arms.append(('M1. K1 fails at the midpoint 25, holds at the moved point 24: located, the refused midpoint in the record '
                 'and deciding nothing; with moved = None it stops at K1',
                 m1_ok, not r0['located'] and 'K1 fails' in r0['why']))
    both = Model(k1_fail={D1: ((23.99, 24.01), (24.999, 25.001))})
    r = run(lib, both, B, moved=lib.MOVED)[0]
    mids = r.get('bisection', {}).get(D1, {}).get('midpoints', [])
    again = mutant(src, "            mids.append(dict(eps=m, from_lower=s_lo, from_upper=s_hi, moved=True))\n",
                   "            mids.append(dict(eps=m, from_lower=s_lo, from_upper=s_hi, moved=True))\n"
                   "            if not (s_lo['k1'] and s_hi['k1']):\n                m = a + moved * moved * (b - a)\n"
                   "                s_lo, s_hi = solve(end_a, m), solve(end_b, m)\n"
                   "                mids.append(dict(eps=m, from_lower=s_lo, from_upper=s_hi, moved=True))\n", 'm2', tmp)
    r2 = run(again, both, B, moved=lib.MOVED)[0]
    arms.append(('M2. K1 fails at the moved point: an unsuccessful stop, with no second move; a mutant moves again',
                 not r['located'] and 'K1 fails' in r['why'] and len(mids) == 2,
                 len(r2.get('bisection', {}).get(D1, {}).get('midpoints', [])) > 2))
    fails = Model(fail={D1: ((24.999, 25.001),)})
    r = run(lib, fails, B, moved=lib.MOVED)[0]
    mids = r.get('bisection', {}).get(D1, {}).get('midpoints', [])
    anchor = "        if moved is not None and s_lo['ok'] and s_hi['ok'] and not (s_lo['k1'] and s_hi['k1']):\n"
    m3 = mutant(src, anchor, "        if moved is not None and not (s_lo['k1'] and s_hi['k1']):\n", 'm3', tmp)
    r3 = run(m3, fails, B, moved=lib.MOVED)[0]
    arms.append(('M3. a solve fails at a midpoint: no move; a mutant moves', len(mids) == 1 and 'a solve fails' in r['why'],
                 len(r3.get('bisection', {}).get(D1, {}).get('midpoints', [])) > 1))
    r = run(lib, Model(), B, moved=lib.MOVED)[0]
    m4 = mutant(src, anchor, "        if moved is not None and s_lo['ok'] and s_hi['ok']:\n", 'm4', tmp)
    r4 = run(m4, Model(), B, moved=lib.MOVED)[0]
    has = lambda x: any(m.get('moved') for v in x.get('bisection', {}).values() for m in v['midpoints'])  # noqa: E731
    arms.append(('M4. K1 holds at every midpoint: no move; a mutant moves', r['located'] and not has(r), has(r4)))
    ok5, d5 = replay_ok(lib)
    m5a = mutant(src, 'MOVED = 0.4 ', 'MOVED = 0.5 ', 'm5a', tmp)
    m5b = mutant(src, "            m = a + moved * (b - a)\n", "            m = b - moved * (b - a)\n", 'm5b', tmp)
    arms.append((f'M5. the ten stored midpoints replayed, the moved point 8.720990 completing with n(L) 7 and 6: {d5}', ok5, True))
    arms.append(('M6. the fraction mutated to 0.5: M5 fails', ok5, not replay_ok(m5a)[0]))
    arms.append(('M6. the end mutated to the upper: M5 fails', ok5, not replay_ok(m5b)[0]))
    return arms


def differential(models):
    """bisect with moved = None against M8.17's, loaded from reference/, on every model: (cases, differences)."""
    p = os.path.join(ROOT, 'reference', 'm8_17', 'run', 'census_lib.py')
    spec = importlib.util.spec_from_file_location('census_lib_m817', p)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    n, bad = 0, []
    for mname, m in models.items():
        for lad in (B, A):
            for N in lad['cutoffs']:
                cu = Fake(N, m)
                args = (20.0, 30.0, m.nl(N, 20.0), m.nl(N, 30.0), (20.0, 'lo'), (30.0, 'hi'), cu.step,
                        lambda s1, s2, cu=cu: m.split(N, s1['point']['eps_reached']))
                a, b = lib.bisect(*args), old.bisect(*args)
                n += 1
                sa = (a['complete'], a['interval'], a['stop'], [x['eps'] for x in a['midpoints']])
                sb = (b['complete'], b['interval'], b['stop'], [x['eps'] for x in b['midpoints']])
                if sa != sb:
                    bad.append(f'{mname}, N = {N}: {sa[:3]} against {sb[:3]}')
    return n, bad


# --- a bracket's borrowed end -----------------------------------------------------------------------------------------
def end_arms(src, tmp):
    arms = []
    cls = dict(type='Hyperbolic', here=dict(nL=4, nD=0, K=0, ki=0))
    base = fake_pt(typ='Hyperbolic', nl={24: 4, 32: 4, 40: 4})
    ok0 = lib.admissible(base, cls, CASE, A) == []

    def arm(label, anchor, new, pt, tag):
        M = mutant(src, anchor, new, tag, tmp)
        arms.append((label, bool(lib.admissible(pt, cls, CASE, A)), not M.admissible(pt, cls, CASE, A)))
    bad = copy.deepcopy(base)
    bad['points'][40]['record']['v0_matches'] = False
    arm('K1 fails at N = 40', "    if not ck.k1(p, case):\n        fails.append(f'K1 fails at N = {top}')\n", '', bad, 'e1')
    want = ("    fails += [f'{f} is {r[f]!r} at N = {top}, {w!r} in M8.17\\'s classification' for f, w in want.items() "
            "if r[f] != w]\n")
    for f, v in (('type', 'Elliptic'), ('nL', 5), ('nD', 1), ('K', 1), ('ki', 1)):
        bad = copy.deepcopy(base)
        bad['points'][40]['record'][f] = v
        arm(f"{f} differs from M8.17's classification", want, '', bad, f'e_{f}')
    idn = ("        elif not idn['kept']:\n            fails.append(f'branch identity fails between N = {pair[0]} and "
           "{pair[1]}')\n    return fails\n")
    for pk in ('24-32', '32-40'):
        bad = copy.deepcopy(base)
        bad['identity'][pk] = dict(aligned_distance=0.02, same_record=True, kept=False)
        arm(f'identity fails on {pk}', idn, '    return fails\n', bad, f'e_{pk}')
    gone = copy.deepcopy(base)
    gone['points'][40] = None
    arms.append(('no accepted record at N = 40', bool(lib.admissible(gone, cls, CASE, A)), True))
    return ok0, arms


# --- the record, end to end --------------------------------------------------------------------------------------------
def like(th, e, typ, verdict='converged'):
    k = lib.key(e)
    p = th['cutoffs']['32']['points'][k]
    return p, dict(verdict=verdict, type=typ if verdict == 'converged' else None, rows=[],
                   reasons=[] if verdict == 'converged' else ['synthetic: Unresolved'])


def synth(row, pattern):
    """A synthetic output of this run's row: the twelve only, copies of M8.17's stored records at N = 32, the rule's
    reading and the record's type set by pattern {eps: type or None}."""
    th = lib.theirs(row, ROOT)
    res = dict(case=case_of(row), cutoffs={str(N): dict(points={}) for N in A['cutoffs']}, readings={}, beside={},
               identity={})
    for e in lib.TWELVE[row]:
        k = lib.key(e)
        t = pattern[lib.key(e)]
        p, rd = like(th, e, t, 'converged' if t else 'Unresolved')
        for N in A['cutoffs']:
            res['cutoffs'][str(N)]['points'][k] = copy.deepcopy(p)
        res['readings'][k], res['beside'][k] = rd, dict(rd)
        res['identity'][k] = {lib.pair_key(q): dict(KEPT) for q in A['pairs']}
    return res


def pattern(row, f):
    return {lib.key(e): f(e) for e in lib.TWELVE[row]}


def record_claims():
    """R1 to R4 (the module docstring): (label, ok, detail)."""
    m817 = lib.m817_file('CENSUS.json', ROOT)
    W4 = lib.WINDOWS['R4']
    t4 = lambda e: 'Elliptic' if e == 4.0 else (None if e == 72.0 else 'Hyperbolic')  # noqa: E731
    results = {'T1/R4': synth('T1/R4', pattern('T1/R4', lambda e: 'Elliptic')),
               'T1/R5': synth('T1/R5', pattern('T1/R5', lambda e: 'Elliptic')),
               'T4/R4': synth('T4/R4', pattern('T4/R4', t4)),
               'T5/R2': synth('T5/R2', pattern('T5/R2', lambda e: 'Elliptic'))}
    bracket_b = dict(located=True, kind='index', why=lib.located_name(-1, B), span=[8.63, 9.16])
    lb = (lib.ARM_B_ROW, lib.key(lib.BRACKET_B[0]), lib.key(lib.BRACKET_B[1]))
    state = lib.classify_rows(results, m817, None)
    js = [(r, (c['lo'], c['hi'])) for r, c in lib.jobs(state)]
    located = {lb: bracket_b, ('T4/R4', lib.key(4.0), lib.key(W4[9])): dict(located=True, kind='index', why='synthetic',
                                                                            span=[3.9, 5.8])}
    rows = lib.assemble(state, located)
    t5 = [o.get('point') for o in rows['T5/R2']['open']]
    ok1 = (js == [('T4/R4', (4.0, W4[9]))] and rows['T1/R4']['outcome'] == rows['T1/R5']['outcome'] == lib.ELLIPTIC_THROUGHOUT
           and rows['T4/R4']['outcome'] == lib.NOT_SETTLED and [o.get('point') for o in rows['T4/R4']['open']] == [72.0]
           and rows['T4/R5']['outcome'] == lib.LOCATED_ALL and rows['T4/R5']['meets_s4'] and t5 == [128.0, 132.0]
           and rows['T5/R2']['outcome'] == lib.NOT_SETTLED)
    out_ = [('R1. the pattern of the replay', ok1, f"jobs {js}; " + '; '.join(f"{r}: {rows[r]['outcome']}" for r in lib.ROWS))]
    gate = 'the control gate: C2a/R5: synthetic'
    st2 = lib.classify_rows({}, m817, gate)
    rows2 = lib.assemble(st2, {lb: bracket_b})
    pts = [p for r in lib.TWELVE for p in rows2[r]['points'] if lib.on(p['eps'], lib.TWELVE[r])]
    m = {(r, lib.key(p['eps'])): p for r in lib.TWELVE for p in m817['rows'][r]['points']}
    same = all(p['causes'] == m[(r, lib.key(p['eps']))]['causes'] and p['not_read'] == gate for r in lib.TWELVE
               for p in rows2[r]['points'] if lib.on(p['eps'], lib.TWELVE[r]))
    ok2 = (not lib.jobs(st2) and len(pts) == 12 and same and all(not p['classified'] for p in pts)
           and rows2['T4/R5']['outcome'] == lib.LOCATED_ALL and rows2['T1/R4']['outcome'] == lib.NOT_SETTLED)
    out_.append(('R2. a gate stops Arm A', ok2, f"{len(pts)} of the twelve keep M8.17's causes, the gate named; Arm B's "
                                                f"row {rows2['T4/R5']['outcome']}"))
    r3 = dict(results)
    r3['T4/R4'] = synth('T4/R4', pattern('T4/R4', lambda e: None if e == 4.0 else t4(e)))
    st3 = lib.classify_rows(r3, m817, None)
    rows3 = lib.assemble(st3, {lb: bracket_b})
    ch3 = rows3['T4/R4']['changes']
    ok3 = (not lib.jobs(st3) and len(ch3) == 1 and ch3[0]['kind'] == 'across' and not ch3[0]['located'])
    out_.append(('R3. T4/R4 at 4 Unresolved', ok3, f"{[(c['lo'], c['hi'], c['kind']) for c in ch3]}"))
    no = dict(located=False, kind='inadmissible', why='the end at 5.65685: K1 fails at N = 40')
    rows4 = lib.assemble(lib.classify_rows(results, m817, None), {lb: bracket_b, ('T4/R4', lib.key(4.0), lib.key(W4[9])): no})
    ch4 = rows4['T4/R4']['changes']
    p566 = next(p for p in rows4['T4/R4']['points'] if lib.key(p['eps']) == lib.key(W4[9]))
    ok4 = (rows4['T4/R4']['outcome'] == lib.NOT_SETTLED and not ch4[0]['located'] and 'K1 fails' in ch4[0]['why']
           and p566['classified'] and p566['type'] == 'Hyperbolic')
    out_.append(('R4. a borrowed end refused', ok4, f"{rows4['T4/R4']['outcome']}; 5.66 stays {p566['type']}"))
    return out_


def main():
    devtools.require('seedcheck')
    say('Tests 5 and 7, classification and the locator, on synthetic records, with no solve, in a seedcheck process.')
    fails = 0
    src = open(lib.__file__, encoding='utf-8').read()
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    arms = []

    def arm(lad, label, anchor, new, check_real, check_mut):
        """check_real(L) and check_mut(L): True when the module behaves as named."""
        tag = f'a{len(arms) + 1}'
        M = mutant(src, anchor, new, tag, tmp)
        arms.append((f"[{'+'.join(str(n) for n in lad['cutoffs'])}] {label}", bool(check_real(lib)), bool(check_mut(M))))
    try:
        base5, a5 = test5(src, tmp)
        say(f"test 5. {'PASS' if base5 else 'FAIL'}: a point classified on Arm A's ladder is the baseline; arms:")
        for label, real, mut in a5:
            say(f"   {label}: real {'as required' if real else 'WRONG'}; mutant {'RED' if mut else 'GREEN'}")
            fails += (not real) + (not mut)
        fails += not base5
        models = {}
        for lad in (B, A):
            D0, D1 = lad['deciding']
            low = lad['cutoffs'][0]

            def located(model, ch=CH, window=None, lad=lad):
                return lambda L: run(L, model, lad, ch, window)[0]['located']

            def refused(model, ch=CH, window=None, why=None, lad=lad):
                def f(L):
                    r = run(L, model, lad, ch, window)[0]
                    return not r['located'] and not r.get('crashed') and (why is None or why in r['why'])
                return f
            base, stop = run(lib, Model(), lad)
            ok = base['located'] and not stop and base['why'] == lib.located_name(1, lad)
            say(f"baseline on {lad['cutoffs']}: {'PASS' if ok else 'FAIL'}: (20, 30), n(L) +1 at 25.004: located "
                f"{base['located']}, union {base.get('union')}, span {base.get('span')}: {base['why']!r}")
            fails += not ok
            apart = Model(change={D0: 25.003, D1: 25.012}, tau=25.008)
            arm(lad, "w/2: the two cutoffs' changes 9e-3 apart, in one interval at w but not at w/2",
                'W_HALF = W / 2 ', 'W_HALF = W ', refused(apart, why='do not overlap'), located(apart))
            lo2 = [[1.0, 1.00049999], [1.00049998, 1.00049998 * (1 + 4.9999e-4)]]
            res2 = {N: dict(complete=True, interval=lo2[i], stop=None, midpoints=[]) for i, N in enumerate(lad['deciding'])}
            dd = {D0: 1, D1: 1}
            arm(lad, "the union's w: two overlapping intervals, each under w/2, their union over w",
                "    if not hi - lo < W * lo:\n        fails.append('the union is not narrower than w of its lower end')\n", '',
                lambda L, r=res2, d=dd, l_=lad: 'the union is not narrower than w of its lower end' in L.location(r, d, l_)[1],
                lambda L, r=res2, d=dd, l_=lad: L.location(r, d, l_)[0] is not None)
            near_wrong = Model(wrong=((24.6, 24.9, 'Hyperbolic'),))
            arm(lad, 'the first offset, 0.01: the lower side reads Hyperbolic at 1% and Elliptic at 5%',
                'DELTAS = (0.01, 0.05) ', 'DELTAS = (0.05,) ', refused(near_wrong, why='the lower guard reads Hyperbolic'),
                located(near_wrong))
            far = Model(unclassified=((23.0, 24.99),))
            arm(lad, 'the single retry at 0.05: the lower side unclassified at 1% and 5%, classified at 10%',
                'DELTAS = (0.01, 0.05) ', 'DELTAS = (0.01, 0.05, 0.10) ', refused(far, why='no lower guard reading'),
                located(far))
            top = Model(change={N: 39.95 for N in lad['cutoffs']}, tau=39.95)
            top_ch = dict(CH, lo=30.0, hi=40.0)
            arm(lad, "the window bound: a change at 39.95, its upper guard past the window's 40",
                '    return window[0] <= g <= window[-1]\n', '    return True\n',
                refused(top, top_ch, why='outside the window'), located(top, top_ch))
            split = Model(split={D1: lambda e: 0.05})
            arm(lad, 'the two-ends distance: the two solutions 5e-2 apart at the top cutoff',
                '            if not d <= AGREE:\n', '            if False:\n', refused(split, why='disagree'), located(split))
            nlsplit = Model(nl_up={D0: lambda e: 4 if abs(e - 25.0) < 1e-12 else (4 if e >= 25.004 else 3)})
            arm(lad, "the two-ends n(L): from above n(L) = 4 at the first midpoint, 25, from below 3",
                "            elif s_lo['nL'] != s_hi['nL']:\n", '            elif False:\n', refused(nlsplit, why='disagree'),
                located(nlsplit))
            differs = Model(ref_bad=lambda e: 'differs' if e == 30.0 else None)
            gate_a = "        fails = ['no record to reproduce'] if r is None else gate_full(mine, r, lad)\n"
            arm(lad, "a bracket end that does not reproduce: the upper end's lam differs by 1e-12",
                gate_a, '        fails = []\n',
                lambda L, m=differs, l_=lad: run(L, m, l_)[1] is not None and not run(L, m, l_)[0].get('located'),
                lambda L, m=differs, l_=lad: run(L, m, l_)[1] is None and run(L, m, l_)[0]['located'])
            missing = Model(ref_bad=lambda e: 'missing' if e == 30.0 else None)
            arm(lad, 'a bracket end with no record to reproduce', gate_a, '        fails = []\n',
                lambda L, m=missing, l_=lad: run(L, m, l_)[1] is not None,
                lambda L, m=missing, l_=lad: run(L, m, l_)[1] is None and run(L, m, l_)[0]['located'])
            arm(lad, "the overlap: the cutoffs' intervals meeting at a point only",
                '    if not max(a1, a2) < min(b1, b2):\n', '    if False:\n', refused(apart, why='do not overlap'),
                located(apart))
            signed = Model(nl=lambda N, e, D1=D1: 3 + ((2 if N == D1 else 1) if e >= 25.004 else 0))
            arm(lad, 'the signed change: +1 at the lower deciding cutoff, +2 at the top',
                '    if delta[n1] != delta[n2]:\n', '    if False:\n',
                refused(signed, why='the signed change differs'), located(signed))
            good = {N: dict(complete=True, interval=[25.0, 25.005], stop=None, midpoints=[]) for N in lad['deciding']}
            zz = {D0: 0, D1: 0}
            arm(lad, 'a zero signed change', '    elif delta[n1] == 0:\n', '    elif False:\n',
                lambda L, g=good, d=zz, l_=lad: 'the signed change is zero' in L.location(g, d, l_)[1],
                lambda L, g=good, d=zz, l_=lad: L.location(g, d, l_)[0] is not None)
            two = Model(nl=lambda N, e: 3 if e < 22.0 else (5 if e < 28.0 else 4), tau=22.0)
            arm(lad, 'the two-change stop: n(L) 3, then 5 from 22, then 4 from 28; the first midpoint reads 5',
                '            elif n == nl_b:\n', '            elif True:\n', refused(two, why='two changes'), located(two))
            k1m = Model(k1_fail={D1: ((24.95, 25.2),)})
            arm(lad, 'K1 at a midpoint: K1 fails at the top cutoff from 24.95 to 25.2, at the midpoints and not the guards',
                "        elif not (s_lo['k1'] and s_hi['k1']):\n", '        elif False:\n', refused(k1m, why='K1 fails'),
                located(k1m))
            across = [(20.0, dict(classified=True, type='Elliptic')), (22.0, dict(classified=False, causes=['x'])),
                      (30.0, dict(classified=True, type='Hyperbolic'))]
            arm(lad, 'the type bracket: a change across an unclassified grid point is no type bracket',
                "kind='type' if not between else 'across'", "kind='type'",
                lambda L, c=across: L.changes(c)[0]['kind'] == 'across', lambda L, c=across: L.changes(c)[0]['kind'] == 'type')
            one = Model(nl=lambda N, e, D1=D1: 3 + (1 if (e >= 25.004 and N != D1) else 0))
            arm(lad, 'the index bracket: n(L) changes at the lower deciding cutoff and not at the top',
                '    if all(changed):\n', '    if any(changed):\n',
                lambda L, m=one, l_=lad: run(L, m, l_)[0].get('kind') == 'inadequate' and run(L, m, l_)[0]['why'] == L.INADEQUATE_INDEX,
                lambda L, m=one, l_=lad: run(L, m, l_)[0].get('kind') == 'index')
            unres = Model(unres={D0: ((19.0, 31.0),), D1: ((19.0, 31.0),)})
            arm(lad, "the inadequate index evidence: both ends' n(L) unresolved at the deciding cutoffs, not read as unchanged",
                "    if any(a is None or b is None for a, b in pairs.values()):\n        return 'inadequate', pairs\n", '',
                lambda L, m=unres, l_=lad: run(L, m, l_)[0].get('kind') == 'inadequate',
                lambda L, m=unres, l_=lad: run(L, m, l_)[0].get('kind') == 'unchanged')
            same = Model(nl=lambda N, e: 3)
            rs = run(lib, same, lad)[0]
            say(f"   the unchanged index, apart: n(L) 3 at both ends, with the type changing: kind {rs.get('kind')!r}, "
                f"{rs['why'] == lib.UNCHANGED_INDEX}")
            fails += not (rs.get('kind') == 'unchanged' and rs['why'] == lib.UNCHANGED_INDEX)
            farside = Model(typ_up=lambda e: None if e > 25.1 else ('Hyperbolic' if e >= 25.004 else 'Elliptic'))
            arm(lad, 'each guard from its own end: from above the upper guards read Unresolved, from below Hyperbolic',
                "            start = 0 if side == 'lower' else 1\n", '            start = 0\n',
                refused(farside, why='no upper guard reading'), located(farside))
            n_a = Model(unres={low: ((19.0, 31.0),)})
            arm(lad, f"the reported cutoff, N = {low}, not bisected, its ends' n(L) unresolved: located from the deciding two",
                "    for N in lad['deciding']:\n        r = res.get(N)\n", "    for N in lad['cutoffs']:\n        r = res.get(N)\n",
                located(n_a), refused(n_a))
            n_b = Model(unres={low: ((25.0, 25.0),)})
            arm(lad, f'the reported cutoff, N = {low}, stopped at its first midpoint: located from the deciding two',
                "    for N in lad['deciding']:\n        r = res.get(N)\n", "    for N in lad['cutoffs']:\n        r = res.get(N)\n",
                located(n_b), refused(n_b))
            n_c = Model(nl=lambda N, e, low=low: 3 + ((2 if e >= 26.3 else 0) if N == low else (1 if e >= 25.004 else 0)))
            r_c = run(lib, n_c, lad)[0]
            ok_c = r_c['located'] and r_c['delta'].get(low) == 2 and r_c['bisection'][low]['complete']
            say(f"   the reported cutoff, N = {low}, bisected with +2 at 26.3: located {r_c['located']}; reported: delta "
                f"{r_c['delta'].get(low)}, interval {r_c['bisection'][low]['interval']}: {'PASS' if ok_c else 'FAIL'}")
            fails += not ok_c
            models.update({f'{k}/{lad["name"]}': v for k, v in dict(apart=apart, near=near_wrong, far=far, split=split,
                                                                    nlsplit=nlsplit, two=two, k1=k1m, one=one, unres=unres).items()})
        n, bad = differential(dict(models, clean=Model()))
        say(f"with moved = None, bisect equals M8.17's: {'PASS' if not bad else 'FAIL'}: {n} bisections, {len(bad)} differ"
            + ''.join(f'\n      {b}' for b in bad[:5]))
        fails += bool(bad)
        say('the moved midpoint:')
        for label, real, mut in moved_arms(src, tmp):
            say(f"   {label}: real {'as required' if real else 'WRONG'}; other side {'RED' if mut else 'GREEN'}")
            fails += (not real) + (not mut)
        ok0, a7 = end_arms(src, tmp)
        say(f"a bracket's borrowed end: {'PASS' if ok0 else 'FAIL'}: an end that carries its classification is admissible; arms:")
        for label, real, mut in a7:
            say(f"   {label}: real {'refuses' if real else 'WRONG'}; mutant {'RED' if mut else 'GREEN'}")
            fails += (not real) + (not mut)
        fails += not ok0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say('arms: the real code refuses or labels as the terms require, and the mutant lets the scenario through:')
    for label, real_ok, mut_through in arms:
        say(f"   {label}: real {'as required' if real_ok else 'WRONG'}; mutant {'RED' if mut_through else 'GREEN'}")
        fails += (not real_ok) + (not mut_through)
    say('the record, end to end, on synthetic outputs beside M8.17\'s classification:')
    for label, ok, detail in record_claims():
        say(f"   {label}: {'PASS' if ok else 'FAIL'}: {detail}")
        fails += not ok
    say(f'{len(arms)} arms on the two ladders; {fails} failed')
    with open(os.path.join(HERE, 'test_locator.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
