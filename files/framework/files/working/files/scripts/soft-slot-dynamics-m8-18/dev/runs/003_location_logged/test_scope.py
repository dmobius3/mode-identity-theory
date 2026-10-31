#!/usr/bin/env python3
"""Test 6: the gates' scope and the read's scope, through the run's whole order, on stub solves, with no solve (M8.18's
terms: THE TESTS BEFORE THE FREEZE, test 6; TWO ARMS, ONE REGISTRATION; ARM A, Solving and reading).

Usage: test_scope.py

It runs census.Run.go, the registered order, on a temporary folder, with the continuation, the record, the rule's
reading, branch identity and Arm B's locator replaced by stubs, each scripted by a scene. Everything else is the run's
own code: Cutoff.solve and read, the jobs, the solve-state gate, the gates, classification, census_lib.settle on a real
bisection of the stub's n(L), and the record. A spy sits on driver.read_point and another on the continuation.

The scenes:
  S1. everything passes, on the replay's pattern. Arm B's record precedes every solve at N = 40. The spy on read_point
      sees at N = 40 only the six controls' registered points, the twelve, T4/R4's bracket end 5.66, and points inside
      that bracket's guards; at the paths' other N = 40 grid points it counts no call, while the continuation reaches them.
      A location reads each midpoint twice, from each end; nothing else is read twice. Every file the run writes is
      logged, so a resume moves none of them aside as partial.
  S2. the kernel fails at C3, N = 40: Arm A ends there, with no later control and no target solved at N = 40. Arm B's
      record stands, and each of the twelve keeps M8.17's causes, the gate named.
  S3. the control gate fails on C2a/R5: no target is read, R4's included.
  S4. Arm B's bracket is not located: Arm A goes on, and T4/R5 ends not settled.
  S5. a reproduction failure at C2b, N = 32: the run stops, nothing at N = 40 runs but C1's, no reading is classified, and
      Arm B's record stands in the record.
  S6. a read at N = 40 outside the scope is refused, by each why: a grid point that is not one of the twelve, a control's
      unregistered point, a bracket's end or a location's point with no bracket open.
  S7. a solve at N = 40 before Arm B's record is written is refused, through Cutoff.solve and through C1.
  S8. a solve not accepted at N = 40 on T1/R4's path, at 8: the path ends there, 1.41 is read, and the four later points
      are untested at N = 40 and not classified.
  S9. an interruption in T1/R4's N = 40 path: the resume moves the partial file aside, solves no completed path again,
      and reaches the same record, row for row.
  S10. a stop Arm B recorded is read again on a resume, and stops the run.
  S11. a target refused on a gate record that did not pass.
  S12. a borrowed end refused: 5.66 fails K1 at N = 40, T4/R4's bracket is not located, no midpoint is solved, and 5.66
      stays Hyperbolic.
  S13. nothing reads a solution before its hash is logged: a read job with no completed path job refuses; an interruption
      after T1/R4's N = 40 files are written and before the log records them leaves no read of them, and the resume moves
      them aside, solves the path again and reaches the same record.
Arms, each a mutation of census.py that must let its scene through: the read's scope check removed (S6, S1); the order
check removed (S7); the gate's check on a target removed (S11); the kernel's stop removed (S2); the reproduction check
removed (S5); a read at every point of a path (S1); the borrowed end's check removed (S12); the solve-state gate
skipped by a read that takes the solutions from memory (S13); a location's solutions file not logged, in Arm A and in
Arm B (S1).
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import types
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import branches as br, devtools  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

out = []
A = lib.ARM_A
W4 = lib.WINDOWS['R4']
KEPT = dict(aligned_distance=0.0, same_record=True, kept=True)
REAL = dict(cont=br.continue_to, read=dr.read_point, run_c1=dr.run_c1, check_c1=ck.check_c1, require=devtools.require,
            theirs=lib.theirs, locate=lib.locate)


def say(s=''):
    print(s, flush=True)
    out.append(s)


class Scene:
    """What the stubs do. k1_bad: {(name, N, eps)} reads with the wrong chain count; rule_bad: {(name, key)} read
    Unresolved; fail: {(name, N, eps)} solves not accepted; arm_b: Arm B's bracket located; arm_b_stop: a stop Arm B
    records; their_bad: {(name, N)} a stored record that differs; crash: (name, N, eps), an interruption."""

    def __init__(self, k1_bad=(), rule_bad=(), fail=(), arm_b=True, arm_b_stop=None, their_bad=(), crash=None):
        self.k1_bad, self.rule_bad, self.fail = set(k1_bad), set(rule_bad), set(fail)
        self.arm_b, self.arm_b_stop, self.their_bad, self.crash = arm_b, arm_b_stop, set(their_bad), crash
        self.solved, self.reads, self.quiet = [], [], False


def k(e):
    return lib.key(e)


def typed(name, case, e):
    """(type, nL, nD, K, ki) of the stub's record: a control's own, T4/R4 changing at 4.5, Elliptic on T1 and T5."""
    if name in lib.CONTROLS:
        i = case['idx']
        return case['type'], i[0], i[1], i[2], 0
    if name == 'T4/R4':
        return ('Elliptic', 7, 1, 6, 3) if e < 4.5 else ('Hyperbolic', 6, 1, 5, 2)
    return 'Elliptic', 2, 0, 2, 1


class Stub(census.Cutoff):
    """A cutoff with no basis: Cutoff's solve, read, step, solves and path, on the stubs."""

    def __init__(self, name, case, N, opened=lambda: True):
        self.name, self.N, self.case, self.opened, self.bracket, self.kept = name, N, case, opened, None, []
        self.B = types.SimpleNamespace(N=N, m=N, index=tuple(range(N)))
        self.Fn = types.SimpleNamespace(B=self.B, name=name)
        self.K, self.u = None, np.ones(N, dtype=complex)
        self.chk = dict(Q=1.0, crit=0.0, k=case['k'], r=case['r'])
        self.seed_ok = True


def stubs(C, scene):
    """Install the scene's stubs on the census module C; undone by unstub()."""
    def cont(Fn, lam0, eps, c0, lam, slope, K=None, prev_accepted=False):
        key_ = (Fn.name, Fn.B.N, eps)
        if not scene.quiet:
            scene.solved.append(key_)
        if key_ == scene.crash and not scene.quiet:
            raise KeyboardInterrupt('the scene')
        if key_ in scene.fail:
            return dict(ok=False, reason='synthetic: not accepted', steps=[dict(evaluations=1, accepted=False)], c=c0, lam=lam)
        return dict(ok=True, steps=[dict(evaluations=1, accepted=True)], c=np.full(Fn.B.N, eps, dtype=complex), lam=lam0 + eps,
                    m=eps, eps=eps, info=dict(floor_rel=0.0), slope=1.0)

    def read(Fn, K, c, lam, case, eps, want):
        name, N = Fn.name, Fn.B.N
        if not scene.quiet:
            scene.reads.append((name, N, eps))
        t, nl, nd, kk, ki = typed(name, case, eps)
        bad = (name, N, eps) in scene.k1_bad
        rec = dict(type=t, nL=nl, nD=nd, K=kk, kr=0, kc=0, ki=ki, sdim=case['dim'], ranks=list(case['ranks']),
                   blocks=case['chains'] + (1 if bad else 0), v0_matches=True, margin=1e-6, separated=True, unresolved=[],
                   krein=[])
        return dict(record=rec, summary=dict(groups=[], name=name, eps=eps), eig=[1.0], lam_read=lam), None, None

    def rule(pts):
        if not all(q and 'summary' in q for q in pts):
            miss = dict(verdict='Unresolved', type=None, reasons=['a cutoff is missing'], rows=[])
            return miss, miss
        hi = pts[-1]
        name, e = hi['summary']['name'], hi['summary']['eps']
        case = C_cases[name]
        slot = case['slot']
        t = hi['record']['type']
        good = dict(verdict='converged', type=t, reasons=[], rows=[], band=lib.band_value(slot, hi['lam']))
        if (name, k(e)) in scene.rule_bad:
            return dict(good, verdict='Unresolved', type=None, reasons=['synthetic']), dict(good, verdict='Unresolved', type=None, reasons=['synthetic'])
        return good, dict(good, band=0.0)

    def identity(cuts, sols, pair):
        a, b = sols.get(pair[0]), sols.get(pair[1])
        if not (a and b and 'record' in a['point'] and 'record' in b['point']):
            return None
        return dict(KEPT)

    def locate(ch, window, case, cuts, readings, aligned, ref, lad, moved=None, gate_mids=None, say=print):
        rec = dict(bracket=[ch['lo'], ch['hi']], types=[ch['lo_type'], ch['hi_type']], ends={}, path={}, kind='index',
                   located=scene.arm_b, why='synthetic: located' if scene.arm_b else 'N = 24: an unsuccessful stop: K1 fails',
                   span=[8.63, 9.16] if scene.arm_b else None, moved_given=moved)
        if scene.arm_b_stop:
            rec['stop'] = scene.arm_b_stop
        return rec, rec.get('stop')

    br.continue_to, dr.read_point = cont, read
    dr.run_c1 = lambda case: (dict(cutoffs=lib.m8161_file('C1.json', ROOT)['cutoffs'], readings={}, identity={}), {})
    ck.check_c1 = lambda o, c: dict(K1=True, K4=True)
    devtools.require = lambda c: None
    lib.locate = locate
    C.rule, C.identity, C.aligned, C.say = rule, identity, (lambda *a: 0.0), (lambda s='': None)
    dr.say = lambda s='': None
    their = {}

    def theirs(name, root=None):
        if name not in their:
            case = C_cases[name]
            eps = [p['eps'] for p in case['points']]
            cut, ids = {}, {}
            scene.quiet = True
            for N in (24, 32):
                cu = Stub(name, case, N)
                sols = cu.solves()
                pts = {k(e): census.roundtrip(cu.read(sols[k(e)], e, 'path')['point']) if sols[k(e)]['state'] is not None
                       else sols[k(e)]['point'] for e in eps if k(e) in sols}
                if (name, N) in scene.their_bad:
                    next(iter(pts.values()))['lam'] += 1e-13
                cut[str(N)] = dict(seed=census.roundtrip(cu.seed()), points=pts)
            scene.quiet = False
            for e in eps:
                ids[k(e)] = dict(KEPT)
            their[name] = dict(cutoffs=cut, identity=ids)
        return their[name]
    lib.theirs = theirs
    scene.solved.clear()
    scene.reads.clear()


def unstub():
    br.continue_to, dr.read_point, dr.run_c1, ck.check_c1 = REAL['cont'], REAL['read'], REAL['run_c1'], REAL['check_c1']
    devtools.require, lib.theirs, lib.locate = REAL['require'], REAL['theirs'], REAL['locate']


C_cases = {n: census.roundtrip(cs.serialize(n, dict(cs.CASES[n], points=lib.path_points(n), cutoffs=lib.cutoffs_of(n))))
           for n in lib.RUN_ORDER}
FROZEN = dict(cases=C_cases)


def scene_run(C, scene, tmp=None):
    """census.Run.go on a scene: (the record, its folder, the run). The caller removes the folder."""
    stubs(C, scene)
    tmp = tmp or tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    run = C.Run(FROZEN, tmp, Stub)
    try:
        rec = run.go()
    finally:
        unstub()
    return rec, tmp, run


def expected_reads():
    want = {(n, 40, e) for n in lib.READ_CONTROLS for e in cs.SAMPLE}
    return want | {(r, 40, e) for r, es in lib.TWELVE.items() for e in es}


def s1(C):
    scene = Scene()
    rec, tmp, run = scene_run(C, scene)
    try:
        r40 = [x for x in scene.reads if x[1] == 40]
        want = expected_reads()
        controls = sum(x[0] in lib.READ_CONTROLS for x in want)
        extra = set(r40) - want
        end = {x for x in extra if x[0] == 'T4/R4' and abs(x[2] - W4[9]) < 1e-12}
        inside = {x for x in extra if x[0] == 'T4/R4' and 4.0 * 0.95 <= x[2] <= W4[9] * 1.05}
        twice = {x for x in extra if r40.count(x) == 2}
        logged = {f for r in run.log['completed'].values() for f in r['files']}
        unlogged = [f for f in os.listdir(tmp) if f.endswith(('.json', '.npz')) and f not in logged | set(C.KEEP)]
        solved40 = {(n, e) for n, N, e in scene.solved if N == 40}
        path_only = {(r, e) for r in lib.TARGETS for e in lib.PATHS[r] if not lib.on(e, lib.TWELVE[r])}
        unread = {x for x in path_only if x in solved40 and (x[0], 40, x[1]) not in set(r40)}
        order = scene.solved.index(next(x for x in scene.solved if x[1] == 40))
        rows = rec['rows']
        ok = (not rec['stop'] and want <= set(r40) and extra == inside and len(end) == 1
              and len(r40) == len(set(r40)) + len(twice) and twice and not twice & end and not unlogged
              and len(unread) == len(path_only) - 1 and rows['T1/R4']['outcome'] == lib.ELLIPTIC_THROUGHOUT
              and rows['T4/R5']['outcome'] == lib.LOCATED_ALL and rows['T4/R4']['changes'][0]['located']
              and rec['bands'] == dict(failures=[]) and order >= 0 and 'arm_b' in run.log['completed'])
        return ok, (f"{len(r40)} reads of {len(set(r40))} points at N = 40: {controls} of the controls, {len(want) - controls} of "
                    f"the twelve, {len(extra)} of T4/R4's location, {len(twice)} of those midpoints read from each end, none "
                    f"elsewhere; {len(unread)} of the paths' other grid points solved and unread; {len(logged)} files logged, "
                    f"{len(unlogged)} left out; {', '.join(r + ': ' + rows[r]['outcome'] for r in lib.ROWS)}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s2(C):
    scene = Scene(k1_bad=[('C3', 40, 1.0)])
    rec, tmp, run = scene_run(C, scene)
    try:
        t40 = [x for x in scene.solved if x[1] == 40 and x[0] not in ('C2a', 'C2b', 'C3')]
        tw = rec['rows']['T1/R4']['points'][5]
        ok = (rec['gate']['passed'] is False and 'the kernel at N = 40: C3' in rec['gate']['stopped'] and not t40
              and not [x for x in scene.solved if x[0] in lib.TARGETS] and rec['arm_b']['located']
              and rec['rows']['T4/R5']['outcome'] == lib.LOCATED_ALL and not tw['classified'] and 'C3' in tw['not_read'])
        return ok, f"{rec['gate']['stopped']}; no later solve at N = 40; T1/R4 at 1.41 keeps M8.17's causes"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s3(C):
    scene = Scene(rule_bad=[('C2a/R5', k(2.0))])
    rec, tmp, run = scene_run(C, scene)
    try:
        ok = (rec['gate']['passed'] is False and 'the control gate: C2a/R5' in rec['gate']['stopped']
              and not [x for x in scene.solved if x[0] in lib.TARGETS]
              and sorted(rec['gate']['control']) == sorted(lib.READ_CONTROLS))
        return ok, f"{rec['gate']['stopped']}; all six recorded; no target solved at any cutoff"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s4(C):
    scene = Scene(arm_b=False)
    rec, tmp, run = scene_run(C, scene)
    try:
        ok = (not rec['stop'] and not rec['arm_b']['located'] and rec['gate']['passed']
              and rec['rows']['T4/R5']['outcome'] == lib.NOT_SETTLED and rec['rows']['T1/R4']['outcome'] == lib.ELLIPTIC_THROUGHOUT)
        return ok, f"Arm B not located; Arm A went on: T1/R4 {rec['rows']['T1/R4']['outcome']}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s5(C):
    scene = Scene(their_bad=[('C2b', 32)])
    rec, tmp, run = scene_run(C, scene)
    try:
        ok = (rec['stop'] and 'reproducibility failure: C2b at N = 32' in rec['stop']['why'] and rec['rows'] == {}
              and rec['arm_b']['located'] and not [x for x in scene.solved if x[1] == 40])
        return ok, (rec['stop'] or {}).get('why', 'no stop')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s6(C):
    res = []
    case = C_cases['T1/R4']
    cu = Stub('T1/R4', case, 40)
    stubs(C, Scene())
    C.Cutoff.read.__globals__['dr'].read_point = dr.read_point
    try:
        s = dict(ok=True, c=np.ones(40), point=dict(lam=50.0, accepted=True))
        for e, why, b in ((2.0, 'twelve', None), (2.0, 'path', None), (W4[9], 'end', None), (W4[9], 'location', None),
                          (2.0, 'control', None), (30.0, 'location', (4.0, W4[9])), (2.0, 'end', (4.0, W4[9]))):
            cu.bracket = b
            try:
                C.Cutoff.read(cu, s, e, why)
                res.append(False)
            except lib.OutOfScope:
                res.append(True)
        c2 = Stub('C2a', C_cases['C2a'], 40)
        try:
            C.Cutoff.read(c2, s, 0.3535533905932738, 'control')
            res.append(False)
        except lib.OutOfScope:
            res.append(True)
    finally:
        unstub()
    return all(res), f'{len(res)} reads refused of {len(res)}: {res}'


def s7(C):
    res = []
    stubs(C, Scene())
    try:
        cu = Stub('C2a', C_cases['C2a'], 40, opened=lambda: False)
        try:
            C.Cutoff.solve(cu, (np.ones(40, dtype=complex), 48.0, 1.0), 0.25)
            res.append(False)
        except PermissionError:
            res.append(True)
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            run = C.Run(FROZEN, tmp, Stub)
            run.log.setdefault('events', [])
            try:
                run.c1()
                res.append(False)
            except PermissionError:
                res.append(True)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    finally:
        unstub()
    return all(res), f'Cutoff.solve refused: {res[0]}; C1 refused: {res[1] if len(res) > 1 else None}'


def s8(C):
    scene = Scene(fail=[('T1/R4', 40, 8.0)])
    rec, tmp, run = scene_run(C, scene)
    try:
        pts = {k(p['eps']): p for p in rec['rows']['T1/R4']['points']}
        late = [pts[k(e)] for e in lib.TWELVE['T1/R4'][1:]]
        after = [x for x in scene.solved if x[0] == 'T1/R4' and x[1] == 40 and x[2] > 8.0]
        ok = (pts[k(lib.TWELVE['T1/R4'][0])]['classified'] and all(not p['classified'] for p in late)
              and all(any('untested at N = 40' in c for c in p['causes']) for p in late) and not after)
        return ok, f"1.41 classified; the four later points untested at N = 40; nothing solved past 8: {not after}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def strip(rows):
    return json.loads(json.dumps(rows, default=str))


def s9(C):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        ref, t2, _ = scene_run(C, Scene())
        shutil.rmtree(t2, ignore_errors=True)
        scene = Scene(crash=('T1/R4', 40, 8.0))
        try:
            scene_run(C, scene, tmp)
            crashed = False
        except KeyboardInterrupt:
            crashed = True
        partial = os.path.join(tmp, 'partial.json')
        with open(partial, 'w', encoding='utf-8') as f:
            f.write('{}')
        again = Scene()
        rec, _, run = scene_run(C, again, tmp)
        moved = any('partial outputs moved' in e['event'] for e in run.log['events'])
        repeated = [x for x in again.solved if x[0] in ('T4/R5', 'C2a', 'C3', 'P5', 'T5/R2')]
        same = strip(rec['rows']) == strip(ref['rows'])
        ok = crashed and moved and not repeated and same and not os.path.exists(partial)
        return ok, f'interrupted: {crashed}; the partial file moved: {moved}; completed paths solved again: {len(repeated)}; the same record: {same}'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s10(C):
    scene = Scene(arm_b_stop='a midpoint does not reproduce at N = 24: synthetic')
    rec, tmp, run = scene_run(C, scene)
    try:
        ok = rec['stop'] and 'Arm B' in rec['stop']['why'] and rec['rows'] == {} and not [x for x in scene.solved if x[1] == 40]
        return ok, (rec['stop'] or {}).get('why', 'no stop')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s11(C):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    stubs(C, Scene())
    try:
        run = C.Run(FROZEN, tmp, Stub)
        run.log['completed']['arm_b'] = dict(files={}, t='the scene')
        run.write('gate', 'GATE.json', dict(passed=False, stopped='synthetic'))
        try:
            run.target('T1/R4')
            return False, 'the target ran'
        except PermissionError as e:
            return 'no target is read' in str(e), str(e)
    finally:
        unstub()
        shutil.rmtree(tmp, ignore_errors=True)


def s12(C):
    scene = Scene(k1_bad=[('T4/R4', 40, W4[9])])
    rec, tmp, run = scene_run(C, scene)
    try:
        r = rec['rows']['T4/R4']
        ch = r['changes'][0]
        p = next(q for q in r['points'] if k(q['eps']) == k(W4[9]))
        mids = [x for x in scene.solved if x[0] == 'T4/R4' and 4.0 < x[2] < W4[9] and x[2] not in W4]
        ok = not ch['located'] and 'K1 fails' in ch['why'] and p['classified'] and p['type'] == 'Hyperbolic' and not mids
        return ok, f"{ch['why']}; 5.66 stays {p['type']}; {len(mids)} midpoints solved"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s13(C):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    stubs(C, Scene())
    try:
        run = C.Run(FROZEN, tmp, Stub)
        try:
            run.read_job('C2a', 24, cs.SAMPLE, 'path')
            first = False
        except KeyError:
            first = True
    finally:
        unstub()
        shutil.rmtree(tmp, ignore_errors=True)
    ref, t2, _ = scene_run(C, Scene())
    shutil.rmtree(t2, ignore_errors=True)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        scene = Scene()

        class Crash(C.Run):
            def complete(self, job, files):
                if job == 'path:T1/R4:40':
                    raise KeyboardInterrupt('after the files, before the log')
                C.Run.complete(self, job, files)
        stubs(C, scene)
        try:
            Crash(FROZEN, tmp, Stub).go()
            crashed = False
        except KeyboardInterrupt:
            crashed = True
        finally:
            unstub()
        unread = not [x for x in scene.reads if x[:2] == ('T1/R4', 40)]
        left = os.path.exists(os.path.join(tmp, 'T1_R4_N40.npz'))
        again = Scene()
        rec, _, run = scene_run(C, again, tmp)
        moved = any('partial outputs moved' in e['event'] for e in run.log['events'])
        solved = len([x for x in again.solved if x[:2] == ('T1/R4', 40)])
        same = strip(rec['rows']) == strip(ref['rows'])
        ok = first and crashed and unread and left and moved and solved >= len(lib.PATHS['T1/R4']) and same
        return ok, (f'a read with no path job refused: {first}; interrupted with the files unlogged: {crashed and left}; no read '
                    f'of them: {unread}; moved aside: {moved}; the path solved again, {solved} steps; the same record: {same}')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def mutant(src, anchor, new, tag, tmp):
    if src.count(anchor) != 1:
        raise SystemExit(f'the anchor for {tag} occurs {src.count(anchor)} times: {anchor[:50]!r}')
    p = os.path.join(tmp, f'census_{tag}.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(src.replace(anchor, new, 1))
    spec = importlib.util.spec_from_file_location(f'census_{tag}', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def red(scene, M):
    """Whether the scene fails on the mutant: its claim false, or the run raising what the real code would not."""
    try:
        return not scene(M)[0]
    except Exception:  # noqa: BLE001
        return True


def main():
    devtools.require('seedcheck')
    say('Test 6, the gates and the read, through the run\'s whole order, on stub solves, in a seedcheck process.')
    fails = 0
    scenes = [('S1', s1), ('S2', s2), ('S3', s3), ('S4', s4), ('S5', s5), ('S6', s6), ('S7', s7), ('S8', s8), ('S9', s9),
              ('S10', s10), ('S11', s11), ('S12', s12), ('S13', s13)]
    for tag, f in scenes:
        ok, d = f(census)
        say(f"{tag}. {'PASS' if ok else 'FAIL'}: {d}")
        fails += not ok
    src = open(census.__file__, encoding='utf-8').read()
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    arms = []
    try:
        scope = ("        if not lib.in_scope(self.name, self.N, eps, why, self.bracket):\n"
                 "            raise lib.OutOfScope(f'{self.name}: a read at N = {self.N}, eps = {eps:g}, as {why}, is outside the scope')\n")
        arms.append(("the read's scope check removed: S6", red(s6, mutant(src, scope, '', 'a1', tmp))))
        order = "        if self.N == lib.TOP and not self.opened():\n            raise PermissionError(f\"a solve at N = {lib.TOP} before Arm B's record is written\")\n"
        arms.append(('the order check in Cutoff.solve removed: S7', red(s7, mutant(src, order, '', 'a2', tmp))))
        g = "                and gate['passed']):\n"
        arms.append(("the gate's check on a target removed: S11", red(s11, mutant(src, g, '                and True):\n', 'a3', tmp))))
        kn = "            if gate['kernel'][name]:\n"
        arms.append(("the kernel's stop removed: S2", red(s2, mutant(src, kn, '            if False:\n', 'a4', tmp))))
        rp = "            self.reproduce(name, N, recs[N], theirs)\n"
        arms.append(('the reproduction check removed: S5', red(s5, mutant(src, rp, '', 'a5', tmp))))
        pth = "            s = self.solve(state, e, prev_accepted=acc)\n"
        arms.append(('a read at every point of a path: S1', red(s1, mutant(src, pth, "            s = self.read(self.solve(state, e, prev_accepted=acc), e, 'path')\n", 'a6', tmp))))
        adm = "            fails += [f'the end at {e:g}: {x}' for x in lib.admissible(rec['ends'][k], cls[k], case, lad)]\n"
        arms.append(("the borrowed end's check removed: S12", red(s12, mutant(src, adm, '', 'a7', tmp))))
        tw = "        recs = {**recs, lib.TOP: self.read_job(row, lib.TOP, twelve, 'twelve')}\n"
        arms.append(('every path point read at N = 40: S1', red(s1, mutant(src, tw, "        recs = {**recs, lib.TOP: self.read_job(row, lib.TOP, where, 'twelve')}\n", 'a8', tmp))))
        hash_ = "        st, cu = self.stored(name, N), self.cutoff(name, N)\n"
        arms.append(('a read that skips the solve-state gate: S13', red(s13, mutant(src, hash_, "        cu = self.cutoff(name, N)\n        st = dict(seed={}, sols={})\n", 'a9', tmp))))
        loc_a = "        return self.write(job, fname, rec, [self.keep_located(job, cuts)])\n"
        arms.append(("Arm A's location, its solutions file not logged: S1", red(s1, mutant(src, loc_a, "        self.keep_located(job, cuts)\n        return self.write(job, fname, rec)\n", 'a10', tmp))))
        loc_b = "            rec = self.write(job, fname, rec, [self.keep_located('arm_b', cuts)])\n"
        arms.append(("Arm B's location, its solutions file not logged: S1", red(s1, mutant(src, loc_b, "            self.keep_located('arm_b', cuts)\n            rec = self.write(job, fname, rec)\n", 'a11', tmp))))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say('arms, each a mutation of census.py that must turn its scene red:')
    for label, r in arms:
        say(f"   {label}: {'RED' if r else 'GREEN'}")
    fails += sum(not r for _, r in arms)
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_scope.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
