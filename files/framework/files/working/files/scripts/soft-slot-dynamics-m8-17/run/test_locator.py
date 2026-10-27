#!/usr/bin/env python3
"""Test 4: the locator and the classification, on synthetic records, with no solve (M8.17's terms: THE TESTS BEFORE THE
FREEZE, test 4; LOCATING A CHANGE OF TYPE; CLASSIFYING A POINT).

Usage: test_locator.py

It runs in a seedcheck process, where every solver and record path of the instrument refuses. census_lib.locate runs
whole, the recomputed path and its reproduction included, on a synthetic instrument (Fake): per cutoff, n(L) as a
step function of eps, the type the rule reads, K1, the two ends' solutions and the records a recomputed point must
equal. Each record carries the fields census_lib reads, so checks.k1, census_lib.nl_at and census_lib.here read it as
they read the instrument's.

The baseline is a clean bracket, (20, 30), with n(L) changing by +1 at 25.004 at every cutoff and the type the rule
reads changing there: it must be Located, with its name. Each condition then has an arm: a scenario the real code
must refuse, or label as the terms require, and a mutation of census_lib's source that removes the condition and must
let the scenario through. The conditions: w/2, the union's w, the guards' first offset and their single retry, the
window bound, the two-ends agreement in distance and in n(L), a bracket end that does not reproduce or has no record,
the overlap, the signed change and its being nonzero, the two-change stop, K1 at a midpoint, the type and index
brackets, the unchanged index and the inadequate index evidence, the known location's precedence, the instrument
named when this instrument reads Unresolved, and the contradiction, in type, K and k_i^-; each guard continued from
its own bracket end, the mutant continuing the upper guard from the lower end through the change; and UA's case,
N = 16 failing alone while N = 24 and 32 meet every deciding condition, which must stay eligible for Located.

The record, end to end: census_lib.classify_rows, jobs and assemble run on synthetic outputs of this run's rows beside
the real known outcomes, M8.16.1's outputs and M8.15's records, with a synthetic locator record. Each synthetic row
carries M8.16.1's records at the points it read on the same steps, as the reproduction requires, and copies of a known
point's records elsewhere, with their types set by the scenario:
  R1. T2/R4 Elliptic at 16 and 22.63: the only job is (22.63, 32), the path going on to 32; with that bracket located,
      T2/R4 ends 'Each change of type located', each point's instrument named;
  R2. T2/R4 Elliptic at 16, Unresolved at 22.63: no job; T2/R4 is not settled, with 22.63 and the change across it
      named;
  R3. on the known outcomes alone, T2/R5 ends 'Elliptic throughout' and T3/R5 'Each change of type located', its 16
      unclassified and accounted for by M8.15.2's location;
  R4. T1/R4 Elliptic at every point: 'Elliptic throughout', on this instrument alone; with 8 read Hyperbolic and n(L)
      unchanged, its two brackets are not located, each named with the unchanged-index wording, and no job runs;
  R5. T5/R2 Elliptic at 45.25 and Unresolved at 128 and 132: not settled, with 128 and 132 named.
  R6. The stop record (census_lib.stopped): a log that stops in a locator job names all seven rows, each with its
      first-time points, and that job's file; a log that stops at T3/R4 names T2/R4 and T3/R4; the same log without its
      stop gives nothing. An arm removes the stop condition, and the mutant marks a completed run as stopped.
"""
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
import copy  # noqa: E402
import json  # noqa: E402

out = []
CASE = dict(chains=4)
WINDOW = [5.0, 10.0, 20.0, 30.0, 40.0]
CH = dict(kind='type', lo=20.0, hi=30.0, lo_type='Elliptic', hi_type='Hyperbolic', between=[])


def say(s=''):
    print(s, flush=True)
    out.append(s)


class Model:
    """A synthetic branch. nl(N, e): n(L) of the solution continued from below; nl_up(N, e): from above (by default the
    same); unres(N, e): n(L) unresolved; typ(e): the type the rule reads, None for Unresolved; k1(N, e); split(N, e):
    the two ends' distance; ref_bad(e): 'missing' or 'differs' at a recomputed point."""

    def __init__(self, change=None, dn=None, tau=25.004, wrong=(), unclassified=(), k1_fail=None, split=None,
                 nl_up=None, unres=None, nl=None, typ=None, ref_bad=None, typ_up=None):
        self.change = {16: 25.004, 24: 25.004, 32: 25.004} | (change or {})
        self.dn = {16: 1, 24: 1, 32: 1} | (dn or {})
        self.tau, self.wrong, self.unclassified = tau, wrong, unclassified
        self.k1_fail, self.split_, self.nl_up_, self.unres_ = k1_fail or {}, split or {}, nl_up or {}, unres or {}
        self._nl, self._typ, self.ref_bad, self.typ_up = nl, typ, ref_bad or (lambda e: None), typ_up

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
                    seconds=0.0, from_above=upper)

    def step(self, state, e, prev_accepted=True):
        upper = e < state[0]
        p = self.point(e, upper)
        return dict(ok=True, why=None, state=(e, 'chain'), c=None, k1=lib.ck.k1(p, CASE), nL=lib.nl_at(p), point=p)

    def path(self, upto):
        return {lib.key(x): self.step((0.0, 'path'), x) for x in WINDOW if x <= upto}


def readings(model):
    def f(sols):
        pts = {N: (s['point'] if s else None) for N, s in sols.items()}
        e = next(p['eps_reached'] for p in pts.values() if p)
        up = next(p['from_above'] for p in pts.values() if p)
        t = model.typ_up(e) if (up and model.typ_up) else model.typ(e)
        rd = (dict(verdict='converged', type=t, reasons=[]) if t and all(pts.values()) else
              dict(verdict='Unresolved', type=None, reasons=['synthetic: the rule reads it Unresolved']))
        return dict(points=pts, reading=rd, identity=dict(aligned_distance=0.0, same_record=True, kept=True))
    return f


def run(L, model, ch=CH, window=None):
    """census_lib.locate (of the module L, the real one or a mutant) on the synthetic instrument."""
    cuts = {N: Fake(N, model) for N in L.CUTOFFS}
    rd = readings(model)

    def ref(e):
        bad = model.ref_bad(e)
        if bad == 'missing':
            return None
        r = rd({N: Fake(N, model).step((0.0, 'path'), e) for N in L.CUTOFFS})
        if bad == 'differs':
            r['points'][32] = dict(r['points'][32], lam=r['points'][32]['lam'] * (1 + 1e-12))
        return r
    try:
        rec, stop = L.locate(ch, window or WINDOW, CASE, cuts, rd, lambda cu, s1, s2: cu.model.split(cu.N, s1['point']['eps_reached']),
                             ref, say=lambda s: None)
    except Exception as e:  # noqa: BLE001
        return dict(located=False, why=f'raised {type(e).__name__}: {e}', crashed=True), None
    return rec, stop


def mutant(src, anchor, new, tag, tmp):
    if src.count(anchor) != 1:
        raise SystemExit(f'the anchor for {tag} occurs {src.count(anchor)} times')
    p = os.path.join(tmp, f'census_lib_{tag}.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(src.replace(anchor, new, 1))
    spec = importlib.util.spec_from_file_location(f'census_lib_{tag}', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def synth(theirs, row, fill):
    """A synthetic output of this run's row: M8.16.1's records where it read the point on the same steps, and fill(e)'s
    records elsewhere on the path."""
    th = theirs[row]
    case = json.loads(json.dumps(cs.serialize(row, dict(cs.CASES[row], points=lib.path_points(row))), default=float))
    out = dict(case=case, cutoffs={str(N): dict(points={}) for N in lib.CUTOFFS}, readings={}, identity={})
    for e in lib.PATHS[row]:
        k = lib.key(e)
        pt = lib.at(th, e) if lib.rule_for(row, e, th) == 1 else fill(e)
        for N in lib.CUTOFFS:
            out['cutoffs'][str(N)]['points'][k] = copy.deepcopy(pt['points'][N])
        out['readings'][k], out['identity'][k] = copy.deepcopy(pt['reading']), copy.deepcopy(pt['identity'])
    return out


def like(theirs, row, e0, typ=None, verdict='converged'):
    """fill(e): copies of the records M8.16.1 holds at e0 on row, the rule's reading set to typ and verdict."""
    def f(e):
        pt = copy.deepcopy(lib.at(theirs[row], e0))
        pt['reading'] = dict(pt['reading'], verdict=verdict, type=(typ or pt['reading']['type']) if verdict == 'converged'
                             else None, reasons=[] if verdict == 'converged' else ['synthetic: Unresolved'])
        return pt
    return f


def record_claims():
    """R1 to R5 (the module docstring): (label, ok, detail)."""
    theirs, m815 = lib.theirs_records(), lib.m815_records()
    loc = lib.known_location(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))
    e11, e16, e22, e32 = lib.WINDOWS['R4'][11], 16.0, lib.T2_END, 32.0
    out_ = []
    res = {'T2/R4': synth(theirs, 'T2/R4', like(theirs, 'T2/R4', e11))}
    st = lib.classify_rows(res, {}, theirs, m815, loc)
    js = [(r, (ch['lo'], ch['hi'])) for r, ch in lib.jobs(st, res, {}, theirs)]
    fake = {('T2/R4', lib.key(e22), lib.key(e32)): dict(located=True, kind='index', why=lib.located_name(1),
                                                        span=[e22 * 0.99, e32 * 1.01], ends={})}
    rows = lib.assemble(res, {}, fake, theirs, m815, loc)
    inst = {lib.key(p['eps']): p['instrument'] for p in rows['T2/R4']['points']}
    ok = (js == [('T2/R4', (e22, e32))] and rows['T2/R4']['outcome'] == lib.LOCATED_ALL and rows['T2/R4']['meets_s4']
          and inst[lib.key(e16)] == inst[lib.key(e22)] == 'this instrument' and inst[lib.key(e11)] == 'both'
          and inst[lib.key(e32)] == 'both')
    out_.append(('R1. T2/R4 Elliptic at 16 and 22.63', ok, f"jobs {js}; {rows['T2/R4']['outcome']}"))
    fill2 = lambda e: (like(theirs, 'T2/R4', e11) if e == e16 else like(theirs, 'T2/R4', e11, verdict='Unresolved'))(e)  # noqa: E731
    res2 = {'T2/R4': synth(theirs, 'T2/R4', fill2)}
    st2 = lib.classify_rows(res2, {}, theirs, m815, loc)
    rows2 = lib.assemble(res2, {}, {}, theirs, m815, loc)
    op = rows2['T2/R4']['open']
    ok2 = (not lib.jobs(st2, res2, {}, theirs) and rows2['T2/R4']['outcome'] == lib.NOT_SETTLED
           and any(o.get('point') == e22 for o in op) and any(o.get('change') == [e16, e32] and o['kind'] == 'across'
                                                               for o in op))
    out_.append(('R2. T2/R4 Unresolved at 22.63', ok2, f"{rows2['T2/R4']['outcome']}; open {[o.get('point') or o.get('change') for o in op]}"))
    t3 = rows['T3/R5']
    p16 = next(p for p in t3['points'] if p['eps'] == 16.0)
    ok3 = (rows['T2/R5']['outcome'] == lib.ELLIPTIC_THROUGHOUT and t3['outcome'] == lib.LOCATED_ALL
           and not p16['classified'] and t3['changes'][0]['located'] and t3['changes'][0]['kind'] == 'across')
    out_.append(('R3. T2/R5 and T3/R5 on the known outcomes', ok3, f"T2/R5 {rows['T2/R5']['outcome']}; T3/R5 "
                                                                  f"{t3['outcome']}, 16 classified {p16['classified']}"))
    res4 = {'T1/R4': synth(theirs, 'T1/R4', like(theirs, 'T1/R4', 0.25))}
    rows4 = lib.assemble(res4, {}, {}, theirs, m815, loc)
    ok4a = (rows4['T1/R4']['outcome'] == lib.ELLIPTIC_THROUGHOUT
            and all(p['instrument'] == 'this instrument' for p in rows4['T1/R4']['points']))
    fill4 = lambda e: like(theirs, 'T1/R4', 0.25, typ='Hyperbolic' if e == 8.0 else None)(e)  # noqa: E731
    res4b = {'T1/R4': synth(theirs, 'T1/R4', fill4)}
    st4b = lib.classify_rows(res4b, {}, theirs, m815, loc)
    rows4b = lib.assemble(res4b, {}, {}, theirs, m815, loc)
    chs = rows4b['T1/R4']['changes']
    ok4b = (not lib.jobs(st4b, res4b, {}, theirs) and len(chs) == 2 and all(c['bracket_kind'] == 'unchanged' and
                                                                              c['why'] == lib.UNCHANGED_INDEX for c in chs)
            and rows4b['T1/R4']['outcome'] == lib.NOT_SETTLED)
    out_.append(('R4. T1/R4 Elliptic throughout; then Hyperbolic at 8 with n(L) unchanged', ok4a and ok4b,
                 f"{rows4['T1/R4']['outcome']}; then {[(c['lo'], c['hi'], c['bracket_kind']) for c in chs]}"))
    e45 = lib.WINDOWS['R2'][15]
    fill5 = lambda e: like(theirs, 'T5/R2', 32.0, typ='Elliptic', verdict='converged' if e == e45 else 'Unresolved')(e)  # noqa: E731
    res5 = {'T5/R2': synth(theirs, 'T5/R2', fill5)}
    rows5 = lib.assemble(res5, {}, {}, theirs, m815, loc)
    pts5 = [o.get('point') for o in rows5['T5/R2']['open']]
    ok5 = (rows5['T5/R2']['outcome'] == lib.NOT_SETTLED and pts5 == [128.0, 132.0] and not rows5['T5/R2']['changes'])
    pts5b = [p['eps'] for p in rows5['T5/R2']['points'] if not p['classified']]
    ok5 = ok5 and pts5b == [128.0, 132.0]
    out_.append(('R5. T5/R2 Unresolved at 128 and 132', ok5, f"{rows5['T5/R2']['outcome']}; open {pts5}"))
    files = lambda n: {n.replace('/', '_').replace(':', '_') + '.json': 'sha'}  # noqa: E731
    job = f"locate:T2/R4:{lib.key(e22)}:{lib.key(e32)}"
    in_job = dict(stop=dict(why='a recomputed point does not reproduce'),
                  completed={**{r: dict(files=files(r)) for r in lib.RUN_ORDER}, job: dict(files=files(job))})
    at_t3 = dict(stop=dict(why='reproducibility failure: T3/R4'), completed={r: dict(files=files(r)) for r in ('T2/R4', 'T3/R4')})
    s1, s2 = lib.stopped(in_job), lib.stopped(at_t3)
    s3 = lib.stopped({k: v for k, v in at_t3.items() if k != 'stop'})
    ok6 = (set(s1) == set(lib.RUN_ORDER) | {job} and all(s1[r]['first_time'] == lib.NEW[r] for r in lib.RUN_ORDER)
           and s1[job]['files'] == files(job) and s1[job]['first_time'] == [] and set(s2) == {'T2/R4', 'T3/R4'}
           and s3 == {})
    out_.append(('R6. the stop record', ok6, f'stopped in a locator job: {len(s1)} jobs named; at T3/R4: {sorted(s2)}; '
                                             f'no stop: {s3}'))
    return out_


def main():
    devtools.require('seedcheck')
    say('Test 4, the locator and the classification, on synthetic records, with no solve, in a seedcheck process.')
    fails = 0
    base, stop = run(lib, Model())
    ok = base['located'] and not stop and base['why'] == lib.located_name(1)
    say(f"baseline: {'PASS' if ok else 'FAIL'}: (20, 30), n(L) +1 at 25.004 at every cutoff: located "
        f"{base['located']}, union {base.get('union')}, span {base.get('span')}: {base['why']!r}")
    fails += not ok
    src = open(lib.__file__, encoding='utf-8').read()
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    arms = []

    def arm(label, anchor, new, check_real, check_mut):
        """check_real(L) and check_mut(L): True when the module behaves as named."""
        tag = f'a{len(arms) + 1}'
        M = mutant(src, anchor, new, tag, tmp)
        arms.append((label, bool(check_real(lib)), bool(check_mut(M))))

    def located(model, ch=CH, window=None):
        return lambda L: run(L, model, ch, window)[0]['located']

    def refused(model, ch=CH, window=None, why=None):
        def f(L):
            r = run(L, model, ch, window)[0]
            return not r['located'] and not r.get('crashed') and (why is None or why in r['why'])
        return f

    try:
        apart = Model(change={24: 25.003, 32: 25.012}, tau=25.008)
        arm("w/2: the two cutoffs' changes 9e-3 apart, in one interval at w but not at w/2",
            'W_HALF = W / 2 ', 'W_HALF = W ', refused(apart, why='do not overlap'), located(apart))
        lo2 = [[1.0, 1.00049999], [1.00049998, 1.00049998 * (1 + 4.9999e-4)]]
        res2 = {N: dict(complete=True, interval=lo2[i], stop=None, midpoints=[]) for i, N in enumerate(lib.DECIDING)}
        arm("the union's w: two overlapping intervals, each under w/2, their union over w (location())",
            "    if not hi - lo < W * lo:\n        fails.append('the union is not narrower than w of its lower end')\n", '',
            lambda L: 'the union is not narrower than w of its lower end' in L.location(res2, {24: 1, 32: 1})[1],
            lambda L: L.location(res2, {24: 1, 32: 1})[0] is not None)
        near_wrong = Model(wrong=((24.6, 24.9, 'Hyperbolic'),))
        arm('the first offset, 0.01: the lower side reads Hyperbolic at 1% and Elliptic at 5%',
            'DELTAS = (0.01, 0.05) ', 'DELTAS = (0.05,) ', refused(near_wrong, why='the lower guard reads Hyperbolic'),
            located(near_wrong))
        far = Model(unclassified=((23.0, 24.99),))
        arm('the single retry at 0.05: the lower side unclassified at 1% and 5%, classified at 10%',
            'DELTAS = (0.01, 0.05) ', 'DELTAS = (0.01, 0.05, 0.10) ', refused(far, why='no lower guard reading'),
            located(far))
        top = Model(change={16: 39.95, 24: 39.95, 32: 39.95}, tau=39.95)
        top_ch = dict(CH, lo=30.0, hi=40.0)
        arm("the window bound: a change at 39.95, its upper guard past the window's 40",
            '    return window[0] <= g <= window[-1]\n', '    return True\n',
            refused(top, top_ch, why='outside the window'), located(top, top_ch))
        split = Model(split={32: lambda e: 0.05})
        arm('the two-ends distance: the two solutions 5e-2 apart at N = 32',
            '            if not d <= AGREE:\n', '            if False:\n', refused(split, why='disagree'), located(split))
        nlsplit = Model(nl_up={24: lambda e: 4 if abs(e - 25.0) < 1e-12 else (4 if e >= 25.004 else 3)})
        arm("the two-ends n(L): from above n(L) = 4 at the first midpoint, 25, from below 3",
            "            elif s_lo['nL'] != s_hi['nL']:\n", '            elif False:\n', refused(nlsplit, why='disagree'),
            located(nlsplit))
        differs = Model(ref_bad=lambda e: 'differs' if e == 30.0 else None)
        arm("a bracket end that does not reproduce: the upper end's lam differs by 1e-12 at N = 32",
            "        fails = ['no record to reproduce'] if r is None else gate_full(mine, r)\n", '        fails = []\n',
            lambda L: run(L, differs)[1] is not None and not run(L, differs)[0].get('located'),
            lambda L: run(L, differs)[1] is None and run(L, differs)[0]['located'])
        missing = Model(ref_bad=lambda e: 'missing' if e == 30.0 else None)
        arm('a bracket end with no record to reproduce',
            "        fails = ['no record to reproduce'] if r is None else gate_full(mine, r)\n", '        fails = []\n',
            lambda L: run(L, missing)[1] is not None, lambda L: run(L, missing)[1] is None and run(L, missing)[0]['located'])
        arm("the overlap: the cutoffs' intervals meeting at a point only",
            '    if not max(a1, a2) < min(b1, b2):\n', '    if False:\n', refused(apart, why='do not overlap'),
            located(apart))
        signed = Model(dn={32: 2}, nl=lambda N, e: 3 + ((2 if N == 32 else 1) if e >= 25.004 else 0))
        arm('the signed change: +1 at N = 24, +2 at N = 32',
            '    if delta[DECIDING[0]] != delta[DECIDING[1]]:\n', '    if False:\n',
            refused(signed, why='the signed change differs'), located(signed))
        good = {N: dict(complete=True, interval=[25.0, 25.005], stop=None, midpoints=[]) for N in lib.DECIDING}
        arm('a zero signed change (location())', '    elif delta[DECIDING[0]] == 0:\n', '    elif False:\n',
            lambda L: 'the signed change is zero' in L.location(good, {24: 0, 32: 0})[1],
            lambda L: L.location(good, {24: 0, 32: 0})[0] is not None)
        two = Model(nl=lambda N, e: 3 if e < 22.0 else (5 if e < 28.0 else 4), tau=22.0)
        arm('the two-change stop: n(L) 3, then 5 from 22, then 4 from 28; the first midpoint reads 5',
            '            elif n == nl_b:\n', '            elif True:\n', refused(two, why='two changes'), located(two))
        k1m = Model(k1_fail={32: ((24.95, 25.2),)})
        arm('K1 at a midpoint: K1 fails at N = 32 from 24.95 to 25.2, at the midpoints and not the guards',
            "        elif not (s_lo['k1'] and s_hi['k1']):\n", '        elif False:\n', refused(k1m, why='K1 fails'),
            located(k1m))
        across = [(20.0, dict(classified=True, type='Elliptic')), (22.0, dict(classified=False, causes=['x'])),
                  (30.0, dict(classified=True, type='Hyperbolic'))]
        arm('the type bracket: a change across an unclassified grid point is no type bracket',
            "kind='type' if not between else 'across'", "kind='type'",
            lambda L: L.changes(across)[0]['kind'] == 'across', lambda L: L.changes(across)[0]['kind'] == 'type')
        one = Model(nl=lambda N, e: 3 + (1 if (e >= 25.004 and N != 32) else 0))
        arm('the index bracket: n(L) changes at N = 24 and not at 32',
            '    if all(changed):\n', '    if any(changed):\n',
            lambda L: run(L, one)[0].get('kind') == 'inadequate' and run(L, one)[0]['why'] == L.INADEQUATE_INDEX,
            lambda L: run(L, one)[0].get('kind') == 'index')
        unres = Model(unres={24: ((19.0, 31.0),), 32: ((19.0, 31.0),)})
        arm("the inadequate index evidence: both ends' n(L) unresolved at N = 24 and 32, not read as unchanged",
            "    if any(a is None or b is None for a, b in pairs.values()):\n        return 'inadequate', pairs\n", '',
            lambda L: run(L, unres)[0].get('kind') == 'inadequate',
            lambda L: run(L, unres)[0].get('kind') == 'unchanged')
        same = Model(nl=lambda N, e: 3)
        say(f"   the unchanged index, apart: n(L) 3 at both ends, with the type changing: kind "
            f"{run(lib, same)[0].get('kind')!r}, {run(lib, same)[0]['why'] == lib.UNCHANGED_INDEX}")
        fails += not (run(lib, same)[0].get('kind') == 'unchanged' and run(lib, same)[0]['why'] == lib.UNCHANGED_INDEX)
        loc = lib.known_location(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))
        t3 = dict(kind='across', lo=lib.WINDOWS['R5'][11], hi=lib.WINDOWS['R5'][13], lo_type='Elliptic',
                  hi_type='Hyperbolic', between=[16.0])
        arm("the precedence: M8.15.2's location accounts for T3/R5's change across its unclassified 16",
            '    return bool(loc and ', '    return bool(False and ',
            lambda L: L.known_located(t3, loc), lambda L: not L.known_located(t3, loc))
        h_un = dict(classified=False, causes=['the rule reads it Unresolved'])
        t_e = dict(decided=True, type='Elliptic', K=6, ki=3)
        arm("the instrument named: an Unresolved reading here is no second confirmation of M8.15's",
            """        return dict(classified=True, type=t['type'], instrument="M8.15's", here=h, m815=t)""",
            """        return dict(classified=True, type=t['type'], instrument='both', here=h, m815=t)""",
            lambda L: L.classify(h_un, t_e)['instrument'] == "M8.15's", lambda L: L.classify(h_un, t_e)['instrument'] == 'both')
        for what, h in (('type', dict(classified=True, type='Hyperbolic', K=6, ki=3)),
                        ('K', dict(classified=True, type='Elliptic', K=4, ki=3)),
                        ('k_i^-', dict(classified=True, type='Elliptic', K=6, ki=2))):
            arm(f'the contradiction, in {what}: the instruments disagree',
                "        if (h['type'], h['K'], h['ki']) == (t['type'], t['K'], t['ki']):\n", '        if True:\n',
                lambda L, h=h: (not L.classify(h, t_e)['classified']) and L.classify(h, t_e).get('contradiction'),
                lambda L, h=h: L.classify(h, t_e)['classified'])
        farside = Model(typ_up=lambda e: None if e > 25.1 else ('Hyperbolic' if e >= 25.004 else 'Elliptic'))
        arm('each guard from its own end: from above the upper guards read Unresolved, from below Hyperbolic',
            "            start = lo if side == 'lower' else hi\n", '            start = lo\n',
            refused(farside, why='no upper guard reading'), located(farside))
        done_log = dict(completed={'T2/R4': dict(files={'T2_R4.json': 'h'})})
        arm('the stop record: a completed run is not marked stopped',
            "    if not log.get('stop'):\n        return {}\n", '',
            lambda L: L.stopped(done_log) == {}, lambda L: L.stopped(done_log) != {})
        n16a = Model(unres={16: ((19.0, 31.0),)})
        arm("UA's case, N = 16 not bisected, its ends' n(L) unresolved: located from N = 24 and 32",
            '    for N in DECIDING:\n        r = res.get(N)\n', '    for N in CUTOFFS:\n        r = res.get(N)\n',
            located(n16a), refused(n16a))
        n16b = Model(unres={16: ((25.0, 25.0),)})
        arm("UA's case, N = 16 stopped at its first midpoint, n(L) unresolved there: located from N = 24 and 32",
            '    for N in DECIDING:\n        r = res.get(N)\n', '    for N in CUTOFFS:\n        r = res.get(N)\n',
            located(n16b), refused(n16b))
        n16c = Model(change={16: 26.3}, dn={16: 2}, nl=lambda N, e: 3 + ((2 if e >= 26.3 else 0) if N == 16 else
                                                                         (1 if e >= 25.004 else 0)))
        r16 = run(lib, n16c)[0]
        ok16 = r16['located'] and r16['delta'].get(16) == 2 and r16['bisection'][16]['complete']
        say(f"   UA's case, N = 16 bisected with +2 at 26.3: located {r16['located']}; N = 16 reported: delta "
            f"{r16['delta'].get(16)}, interval {r16['bisection'][16]['interval']}: {'PASS' if ok16 else 'FAIL'}")
        fails += not ok16
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say('arms: the real code refuses or labels as the terms require, and the mutant lets the scenario through:')
    for label, real_ok, mut_through in arms:
        say(f"   {label}: real {'as required' if real_ok else 'WRONG'}; mutant {'RED' if mut_through else 'GREEN'}")
        fails += (not real_ok) + (not mut_through)
    say('the record, end to end, on synthetic outputs beside the known outcomes:')
    for label, ok, detail in record_claims():
        say(f"   {label}: {'PASS' if ok else 'FAIL'}: {detail}")
        fails += not ok
    say(f'{len(arms)} arms; {fails} failed')
    with open(os.path.join(HERE, 'test_locator.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
