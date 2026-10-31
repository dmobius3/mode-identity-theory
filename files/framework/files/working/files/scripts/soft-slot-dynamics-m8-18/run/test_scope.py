#!/usr/bin/env python3
"""Test 6: the gates' scope and the read's scope, through the run's whole order, on stub solves, with no solve (M8.18's
terms: THE TESTS BEFORE THE FREEZE, test 6; TWO ARMS, ONE REGISTRATION; ARM A, Solving and reading).

Usage: test_scope.py
       test_scope.py --killed FOLDER CENSUS_PY     one launch of S29, in a process of its own

It runs census.Run.go, the registered order, on a temporary folder, with the continuation, the record, the rule's
reading, branch identity and Arm B's locator replaced by stubs, each scripted by a scene. Everything else is the run's
own code: Cutoff.solve and read, the jobs, the solve-state gate, the gates, classification, census_lib.settle on a real
bisection of the stub's n(L), and the record. A spy sits on driver.read_point and another on the continuation.

The scenes:
  S1. everything passes, on the replay's pattern. Arm B's record precedes every solve at N = 40. The spy on read_point
      sees at N = 40 only the six controls' registered points, the twelve, T4/R4's bracket end 5.66, and points inside
      that bracket's guards; at the paths' other N = 40 grid points it counts no call, while the continuation reaches them.
      A location reads each midpoint twice, from each end; nothing else is read twice. Every file the run writes is
      logged, so a resume moves none of them aside as partial, and every job logs the process's peak resident size.
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
  S10. a stop Arm B records stops the run: no solve at N = 40, and no row is assembled.
  S11. a target refused on a gate record that did not pass.
  S12. a borrowed end refused: 5.66 fails K1 at N = 40, T4/R4's bracket is not located, no midpoint is solved, and 5.66
      stays Hyperbolic.
  S13. nothing reads a solution before its hash is logged: a read job with no completed path job refuses; an interruption
      after T1/R4's N = 40 files are written and before the log records them leaves no read of them, and the resume moves
      them aside, solves the path again and reaches the same record.
  S14. a recorded stop met on a resume: a crash between ARM_B.json and STOP.json leaves no stop on record, and the resume
      reads Arm B's stop from its file, stops the run and writes STOP.json.
  S15. a control out of memory at N = 40, in a solve at C3, a read at P5, an identity at C2b, and in C1: each is that
      control's kernel failure with the cause named, GATE.json records it, Arm A ends, and the run reaches its record.
  S16. a scored reading off the frozen band, at a target, at a control and at a location's guard on each side: the run
      stops, and no row is assembled.
  S17. a read refused at N = 40 through the run's whole order: a stop on record, and no row is assembled.
  S18. Arm B's bracket on M8.17's record differs from the frozen one: the run stops before any solve.
  S19. no case's cutoffs at N = 40 are held when another case's are made.
  S20. T5/R2 at 45.25 reads Hyperbolic: its two brackets, each with a borrowed end M8.17 classified on M8.15's instrument
      alone, are refused with that cause, and the end at 64, past the row's path, with that cause too. No midpoint is
      solved, and 32 and 64 stay Elliptic.
  S21. a target's route. Three launches left unfinished in T1/R4's N = 40 path, and a fourth finds it so: no fourth start,
      T1/R4 stays unread with M8.17's causes and the job named, the row before it and the rows after it are classified,
      and the run reaches its record. Out of memory the same, on its first launch, at T1/R4 and at T4/R4, whose own
      location then has no job. A later launch, after an interruption at the next row, does not start the job out of
      memory again.
  S22. a location's route. Three launches left unfinished in T4/R4's bisection: no fourth start, the bracket is not located,
      its kind says why, both ends keep their classifications, and every other row stands. Out of memory the same.
  S23. a control's route. Three launches left unfinished at C3's N = 40 path, and at C1: no fourth start, the kernel check
      fails with the job named, GATE.json records it, no target's job is started, and the run reaches its record.
  S24. Arm B's route. Three launches left unfinished in Arm B: no fourth start, its record is written, not located, of a kind
      of its own and claiming no reproduction, and Arm A goes on. Out of memory the same.
  S25. any other job. Three launches left unfinished at C2a's path at N = 24: no fourth start, a stop on record, no row
      assembled, Arm B's record standing, and a further launch refused. Out of memory the same, with that cause.
  S26. a code defect stops the run on its first launch, with one start of its job, a stop on record, no row assembled and a
      further launch refused: a ValueError at a target, a PermissionError at a control, a KeyError in the assembly.
  S27. attempts are each job's own. Two launches left unfinished at T1/R4 and two at T4/R4, five launches in all, reach the
      same record as an uninterrupted run, each job with three starts.
  S28. a reproduction failure at T4/R4, with T5/R2's and T1/R4's jobs complete, still classifies nothing.
  S29. a real kill. Every other interruption here is an exception, which a kill is not. Each launch runs in a process of its
      own and SIGKILLs itself at T1/R4's N = 40 path, with nothing raised, three times; the fourth, a new process, reads the
      count from the log on disk, starts no fourth attempt, and reaches its record with the row unread.

Arms, each a mutation of census.py, one of census_lib.py, that must let its scene through: the read's scope check removed (S6); that check
removed with every path point read, for the spy's count (S1); the order check removed (S7); the gate's check on a target
removed (S11); the kernel's stop removed (S2); the reproduction check removed (S5); a read at every point of a path (S1);
the borrowed end's check removed (S12); the solve-state gate skipped by a read that takes the solutions from memory (S13);
a location's solutions file not logged, in Arm A and in Arm B (S1); C1's own order check removed (S7); a resume that
passes over a stop Arm B recorded (S14); the memory failure not caught, at a control and at C1 (S15); the band's stop
removed (S16); the guards' band test removed, in census_lib.py (S16); the refused read's stop removed (S17); the bracket's check removed (S18); a control's cutoffs kept (S19);
the path's end taken as on the path for every end (S20); the peak size not logged (S1); each route's two causes, one at a
time, at a target (S21), a location (S22) and Arm B (S24), and the unfinished job at a control and at C1 (S23); out of
memory taken for a defect (S25); the limit ignored, a start not written before the solve, a resume that forgets the
starts, and a job out of memory started again (S21); the count taken from launches (S27); the catch of a defect removed, and a broad handler at a target and at a
control (S26); a broad handler at a target that takes a stop for a limit (S28); a start not written before the solve, under a real kill
(S29).

An arm counts only if it reports a line of its own: one equal to the real code's line is a failure of this test. Each
line is computed from what the scene saw, and nothing in it is fixed text that could be false on a mutant.
"""
import importlib.util
import json
import os
import shutil
import signal
import subprocess
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
    records; their_bad: {(name, N)} a stored record that differs; crash: (name, N, eps), or a test on it, an interruption;
    memory and memory_read: {(name, N, eps)} solves and reads that run out of memory; memory_id: {(name, pair)} identities
    that do; end_b and end_c1: what Arm B's locator and C1 raise, if anything; band_bad: {(name, key)} scored readings off
    the frozen band; hyper: {(name, eps)} points the record reads Hyperbolic; defect: {(name, N, eps): an exception}; kill:
    (name, N, eps) where the process SIGKILLs itself."""

    def __init__(self, k1_bad=(), rule_bad=(), fail=(), arm_b=True, arm_b_stop=None, their_bad=(), crash=None, memory=(),
                 memory_read=(), memory_id=(), end_b=None, end_c1=None, band_bad=(), hyper=(), defect=None, kill=None):
        self.k1_bad, self.rule_bad, self.fail = set(k1_bad), set(rule_bad), set(fail)
        self.arm_b, self.arm_b_stop, self.their_bad, self.crash = arm_b, arm_b_stop, set(their_bad), crash
        self.memory, self.memory_read, self.memory_id, self.band_bad = set(memory), set(memory_read), set(memory_id), set(band_bad)
        self.end_b, self.end_c1, self.hyper, self.defect = end_b, end_c1, set(hyper), defect or {}
        self.solved, self.reads, self.quiet, self.b_calls, self.kill = [], [], False, 0, kill


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


def stub_of(C):
    """A cutoff with no basis, on the Cutoff of the census module C: its solve, read, step, solves and path, on the
    stubs. A mutation of Cutoff reaches a scene only this way."""
    class Stub(C.Cutoff):
        def __init__(self, name, case, N, opened=lambda: True):
            self.name, self.N, self.case, self.opened, self.bracket, self.kept = name, N, case, opened, None, []
            self.B = types.SimpleNamespace(N=N, m=N, index=tuple(range(N)))
            self.Fn = types.SimpleNamespace(B=self.B, name=name)
            self.K, self.u = None, np.ones(N, dtype=complex)
            self.chk = dict(Q=1.0, crit=0.0, k=case['k'], r=case['r'])
            self.seed_ok = True
    return Stub


def stubs(C, scene):
    """Install the scene's stubs on the census module C; undone by unstub()."""
    def cont(Fn, lam0, eps, c0, lam, slope, K=None, prev_accepted=False):
        key_ = (Fn.name, Fn.B.N, eps)
        if not scene.quiet:
            scene.solved.append(key_)
            if key_ == scene.kill:
                os.kill(os.getpid(), signal.SIGKILL)
            if key_ == scene.crash or (callable(scene.crash) and scene.crash(key_)):
                raise KeyboardInterrupt('the scene')
            if key_ in scene.memory:
                raise MemoryError('the scene')
            if key_ in scene.defect:
                raise scene.defect[key_]('the scene')
        if key_ in scene.fail:
            return dict(ok=False, reason='synthetic: not accepted', steps=[dict(evaluations=1, accepted=False)], c=c0, lam=lam)
        return dict(ok=True, steps=[dict(evaluations=1, accepted=True)], c=np.full(Fn.B.N, eps, dtype=complex), lam=lam0 + eps,
                    m=eps, eps=eps, info=dict(floor_rel=0.0), slope=1.0)

    def read(Fn, K, c, lam, case, eps, want):
        name, N = Fn.name, Fn.B.N
        if not scene.quiet:
            scene.reads.append((name, N, eps))
        if (name, N, eps) in scene.memory_read:
            raise MemoryError('the scene')
        t, nl, nd, kk, ki = typed(name, case, eps)
        if (name, eps) in scene.hyper:
            t = 'Hyperbolic'
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
        if (name, k(e)) in scene.band_bad:
            good['band'] += 1e-6
        if (name, k(e)) in scene.rule_bad:
            return dict(good, verdict='Unresolved', type=None, reasons=['synthetic']), dict(good, verdict='Unresolved', type=None, reasons=['synthetic'])
        return good, dict(good, band=0.0)

    def identity(cuts, sols, pair):
        if (cuts[pair[0]].name, tuple(pair)) in scene.memory_id:
            raise MemoryError('the scene')
        a, b = sols.get(pair[0]), sols.get(pair[1])
        if not (a and b and 'record' in a['point'] and 'record' in b['point']):
            return None
        return dict(KEPT)

    def locate(ch, window, case, cuts, readings, aligned, ref, lad, moved=None, gate_mids=None, say=print):
        scene.b_calls += 1
        if scene.end_b:
            raise scene.end_b('the scene')
        rec = dict(bracket=[ch['lo'], ch['hi']], types=[ch['lo_type'], ch['hi_type']], ends={}, path={}, kind='index',
                   located=scene.arm_b, why='synthetic: located' if scene.arm_b else 'N = 24: an unsuccessful stop: K1 fails',
                   span=[8.63, 9.16] if scene.arm_b else None, moved_given=moved)
        if scene.arm_b_stop:
            rec['stop'] = scene.arm_b_stop
        return rec, rec.get('stop')

    def run_c1(case):
        if scene.end_c1:
            raise scene.end_c1('the scene')
        return dict(cutoffs=lib.m8161_file('C1.json', ROOT)['cutoffs'], readings={}, identity={}), {}

    br.continue_to, dr.read_point, dr.run_c1 = cont, read, run_c1
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
                cu = stub_of(census)(name, case, N)
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
    run = C.Run(FROZEN, tmp, stub_of(C))
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
        sized = all(r.get('peak_rss_bytes', 0) > 0 for r in run.log['completed'].values() if r['files'])
        unlogged = [f for f in os.listdir(tmp) if f.endswith(('.json', '.npz')) and f not in logged | set(C.KEEP)]
        solved40 = {(n, e) for n, N, e in scene.solved if N == 40}
        path_only = {(r, e) for r in lib.TARGETS for e in lib.PATHS[r] if not lib.on(e, lib.TWELVE[r])}
        unread = {x for x in path_only if x in solved40 and (x[0], 40, x[1]) not in set(r40)}
        others = len(r40) - len(set(r40)) - len(twice)
        rows = rec['rows']
        if rec['stop']:
            return False, rec['stop']['why']
        ok = (want <= set(r40) and extra == inside and len(end) == 1
              and len(r40) == len(set(r40)) + len(twice) and twice and not twice & end and not unlogged and sized
              and len(unread) == len(path_only) - 1 and rows['T1/R4']['outcome'] == lib.ELLIPTIC_THROUGHOUT
              and rows['T4/R5']['outcome'] == lib.LOCATED_ALL and rows['T4/R4']['changes'][0]['located']
              and rec['bands'] == dict(failures=[]) and 'arm_b' in run.log['completed'])
        return ok, (f"{len(logged)} files logged, {len(unlogged)} left out, each job's peak size logged: {sized}; {len(r40)} reads of {len(set(r40))} points at N = 40: "
                    f"{controls} of the controls, {len(want) - controls} of the twelve, {len(extra)} of T4/R4's location, "
                    f"{len(twice)} of those midpoints read from each end, {others} other points read twice; {len(unread)} of the paths' other grid "
                    f"points solved and unread; {', '.join(r + ': ' + rows[r]['outcome'] for r in lib.ROWS)}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s2(C):
    scene = Scene(k1_bad=[('C3', 40, 1.0)])
    rec, tmp, run = scene_run(C, scene)
    try:
        t40 = [x for x in scene.solved if x[1] == 40 and x[0] not in ('C2a', 'C2b', 'C3')]
        tw = rec['rows']['T1/R4']['points'][5]
        controls = sum(x[1] == 40 and x[0] in lib.CONTROLS for x in scene.solved)
        targets = sum(x[1] == 40 and x[0] in lib.TARGETS for x in scene.solved)
        ok = (rec['gate']['passed'] is False and 'the kernel at N = 40: C3' in rec['gate']['stopped'] and not t40
              and not [x for x in scene.solved if x[0] in lib.TARGETS] and rec['arm_b']['located']
              and rec['rows']['T4/R5']['outcome'] == lib.LOCATED_ALL and not tw['classified'] and 'C3' in tw['not_read'])
        return ok, (f"{rec['gate']['stopped']}; solves at N = 40: {controls} of the controls, {targets} of the targets; "
                    f"T1/R4 at 1.41: classified {tw['classified']}, not read: {tw.get('not_read')}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s3(C):
    scene = Scene(rule_bad=[('C2a/R5', k(2.0))])
    rec, tmp, run = scene_run(C, scene)
    try:
        ok = (rec['gate']['passed'] is False and 'the control gate: C2a/R5' in rec['gate']['stopped']
              and not [x for x in scene.solved if x[0] in lib.TARGETS]
              and sorted(rec['gate']['control']) == sorted(lib.READ_CONTROLS))
        return ok, (f"{rec['gate']['stopped']}; {len(rec['gate']['control'])} recorded; "
                    f"{sum(x[0] in lib.TARGETS for x in scene.solved)} target solves")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s4(C):
    scene = Scene(arm_b=False)
    rec, tmp, run = scene_run(C, scene)
    try:
        ok = (not rec['stop'] and not rec['arm_b']['located'] and rec['gate']['passed']
              and rec['rows']['T4/R5']['outcome'] == lib.NOT_SETTLED and rec['rows']['T1/R4']['outcome'] == lib.ELLIPTIC_THROUGHOUT)
        return ok, f"Arm B located: {rec['arm_b']['located']}; the gate passed: {rec['gate']['passed']}; T1/R4: {rec['rows']['T1/R4']['outcome']}"
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
    cu = stub_of(C)('T1/R4', case, 40)
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
        c2 = stub_of(C)('C2a', C_cases['C2a'], 40)
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
        cu = stub_of(C)('C2a', C_cases['C2a'], 40, opened=lambda: False)
        try:
            C.Cutoff.solve(cu, (np.ones(40, dtype=complex), 48.0, 1.0), 0.25)
            res.append(False)
        except PermissionError:
            res.append(True)
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            run = C.Run(FROZEN, tmp, stub_of(C))
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
        return ok, (f"1.41 classified: {pts[k(lib.TWELVE['T1/R4'][0])]['classified']}; "
                    f"{sum(any('untested at N = 40' in c for c in p['causes']) for p in late)} of the four later points untested at N = 40; "
                    f"{len(after)} solves past 8")
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
        run = C.Run(FROZEN, tmp, stub_of(C))
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
        run = C.Run(FROZEN, tmp, stub_of(C))
        try:
            run.read_job('C2a', 24, cs.SAMPLE, 'path')
            return False, 'a read with no path job was not refused'
        except C.StopRun:
            pass
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
            Crash(FROZEN, tmp, stub_of(C)).go()
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
        ok = crashed and unread and left and moved and solved >= len(lib.PATHS['T1/R4']) and same
        return ok, (f'a read with no path job refused: True; interrupted with the files unlogged: {crashed and left}; no read '
                    f'of them: {unread}; moved aside: {moved}; the path solved again, {solved} steps; the same record: {same}')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s14(C):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        class Crash(C.Run):
            def stop(self, why, detail):
                raise KeyboardInterrupt('after ARM_B.json, before STOP.json')
        stubs(C, Scene(arm_b_stop='a midpoint does not reproduce at N = 24: synthetic'))
        try:
            Crash(FROZEN, tmp, stub_of(C)).go()
            crashed = False
        except KeyboardInterrupt:
            crashed = True
        finally:
            unstub()
        path = os.path.join(tmp, 'STOP.json')
        none = not os.path.exists(path)
        again = Scene()
        rec, _, run = scene_run(C, again, tmp)
        ok = (crashed and none and rec['stop'] and 'Arm B' in rec['stop']['why'] and rec['rows'] == {} and os.path.exists(path)
              and not [x for x in again.solved if x[1] == 40])
        return ok, f"interrupted with no stop on record: {crashed and none}; the resume: {(rec['stop'] or {}).get('why', 'no stop')}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s15(C):
    res, lines = [], []
    for scene, who in ((Scene(memory=[('C3', 40, 1.0)]), 'C3'), (Scene(memory_read=[('P5', 40, 0.5)]), 'P5'),
                       (Scene(memory_id=[('C2b', (32, 40))]), 'C2b'), (Scene(end_c1=MemoryError), 'C1')):
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            rec, _, run = scene_run(C, scene, tmp)
            if rec['stop']:
                res.append(False)
                lines.append(f"{who}: stopped: {rec['stop']['why']}")
                continue
            tw = rec['rows']['T1/R4']['points'][5]
            why = rec['gate']['stopped']
            res.append(rec['gate']['passed'] is False and rec['gate']['kernel'][who] == [lib.NO_MEMORY]
                       and why == f'the kernel at N = 40: {who}: {lib.NO_MEMORY}' and 'gate' in run.log['completed']
                       and not [x for x in scene.solved if x[0] in lib.TARGETS] and rec['arm_b']['located']
                       and not tw['classified'] and who in tw['not_read'])
            lines.append(f"{who}: {why}; GATE.json logged: {'gate' in run.log['completed']}; {len(rec['rows'])} rows")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return all(res), ' | '.join(lines)


def s16(C):
    res, lines = [], []
    ref, t2, _ = scene_run(C, Scene())
    shutil.rmtree(t2, ignore_errors=True)
    lo, hi = ref['rows']['T4/R4']['changes'][0]['span']
    for name, e, at in (('T1/R4', 64.0, 'T1/R4 '), ('C2a', 1.0, 'C2a '), ('T4/R4', lo, 'T4/R4 lower guard at '), ('T4/R4', hi, 'T4/R4 upper guard at ')):
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            rec, _, run = scene_run(C, Scene(band_bad=[(name, k(e))]), tmp)
            why = (rec['stop'] or {}).get('why', 'no stop')
            res.append(why.startswith(f'the band: {at}') and rec['rows'] == {} and bool(rec['bands']['failures'])
                       and os.path.exists(os.path.join(tmp, 'STOP.json')) and rec['arm_b']['located'])
            lines.append(f"{name}: {why}; {len(rec['rows'])} rows assembled")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return all(res), ' | '.join(lines)


def with_band(band):
    """S16 with the band's test from a mutation of census_lib.py."""
    def scene(C):
        real, lib.band_failures = lib.band_failures, band
        try:
            return s16(C)
        finally:
            lib.band_failures = real
    return scene


def s17(C):
    real = lib.in_scope
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    lib.in_scope = lambda name, N, eps, why, bracket=None: (name, N) != ('T1/R5', 40) and real(name, N, eps, why, bracket)
    try:
        rec, _, run = scene_run(C, Scene(), tmp)
        why = (rec['stop'] or {}).get('why', 'no stop')
        ok = ('outside the scope' in why and rec['rows'] == {} and os.path.exists(os.path.join(tmp, 'STOP.json'))
              and rec['arm_b']['located'])
        return ok, why
    finally:
        lib.in_scope = real
        shutil.rmtree(tmp, ignore_errors=True)


def s18(C):
    real = lib.BRACKET_B
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    lib.BRACKET_B = (8.0, 16.0)
    try:
        scene = Scene()
        rec, _, run = scene_run(C, scene, tmp)
        why = (rec['stop'] or {}).get('why', 'no stop')
        return 'not the frozen one' in why and not scene.solved and rec['rows'] == {}, f'{why}; {len(scene.solved)} solves'
    finally:
        lib.BRACKET_B = real
        shutil.rmtree(tmp, ignore_errors=True)


def s19(C):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))

    class Held(C.Run):
        most = 0

        def cutoff(self, name, N):
            Held.most = max(Held.most, len({n for n, M in self.cuts if M == lib.TOP and n != name}))
            return C.Run.cutoff(self, name, N)
    stubs(C, Scene())
    try:
        Held(FROZEN, tmp, stub_of(C)).go()
    finally:
        unstub()
        shutil.rmtree(tmp, ignore_errors=True)
    return Held.most == 0, f"at most {Held.most} other case's cutoffs at N = 40 held when a cutoff is made"


def s20(C):
    e45 = lib.TWELVE['T5/R2'][0]
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        scene = Scene(hyper=[('T5/R2', e45)])
        rec, _, run = scene_run(C, scene, tmp)
        if rec['stop']:
            return False, rec['stop']['why']
        r = rec['rows']['T5/R2']
        whys = [c['why'] for c in r['changes']]
        pts = {k(p['eps']): p for p in r['points']}
        past = [w for w in whys if "the end at 64: it lies past the row's path" in w]
        alone = [w for w in whys if "M8.15's instrument alone" in w]
        mids = [x for x in scene.solved if x[0] == 'T5/R2' and x[2] not in lib.PATHS['T5/R2']]
        ok = (len(whys) == 2 and len(past) == 1 and len(alone) == 2 and not mids and pts[k(e45)]['type'] == 'Hyperbolic'
              and pts[k(32.0)]['type'] == pts[k(64.0)]['type'] == 'Elliptic' and r['outcome'] == lib.NOT_SETTLED)
        return ok, (f"{len(whys)} brackets refused; past-path causes: {len(past)}; M8.15-only causes: {len(alone)}; "
                    f"{len(mids)} midpoints solved: {' | '.join(whys)}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def launches(C, scene_of, n, tmp):
    """n launches on one folder, each meant to end from outside. Returns how many did."""
    ended = 0
    for _ in range(n):
        try:
            scene_run(C, scene_of(), tmp)
        except KeyboardInterrupt:
            ended += 1
    return ended


def starts(tmp, job):
    """The starts of a job in the run's log."""
    return sum(e['event'] == f'{job} started' for e in lib.load_json(os.path.join(tmp, 'RUNLOG.json'))['events'])


def exhausted(C, scene_of, tmp, job):
    """Three launches ended at a job, then one more: (launches ended, the last scene, its record, or None if that launch
    started the job again and was ended too, and the job's starts)."""
    ended = launches(C, scene_of, 3, tmp)
    last = scene_of()
    try:
        rec = scene_run(C, last, tmp)[0]
    except KeyboardInterrupt:
        rec = None
    return ended, last, rec, starts(tmp, job)


def refused(C, tmp):
    """Whether a further launch on a stopped run is refused."""
    try:
        scene_run(C, Scene(), tmp)
        return False
    except PermissionError:
        return True


def twelve(rec, row):
    """A row's twelve, as the record holds them."""
    return [p for p in rec['rows'][row]['points'] if lib.on(p['eps'], lib.TWELVE[row])]


def read_count(rec, row):
    """How many of a row's twelve the record classifies."""
    return sum(p['classified'] for p in twelve(rec, row))


def unread(rec, row, why):
    """Each of a row's twelve is unclassified, keeps M8.17's causes, and names why."""
    held = {k(p['eps']): p for p in lib.m817_file('CENSUS.json', ROOT)['rows'][row]['points']}
    return all(not p['classified'] and why in (p.get('not_read') or '') and p['causes'] == held[k(p['eps'])]['causes']
               for p in twelve(rec, row))


def s21(C):
    job, hit = 'path:T1/R4:40', ('T1/R4', 40, 8.0)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        ended, last, rec, n = exhausted(C, lambda: Scene(crash=hit), tmp, job)
        if rec is None:
            return False, f'{ended} launches ended there, and the next started it again: {n} starts in the log'
        if rec['stop']:
            return False, f"{ended} launches ended there, {n} starts; stopped: {rec['stop']['why']}"
        again = sum(x[:2] == hit[:2] for x in last.solved)
        counts = {r: read_count(rec, r) for r in lib.TARGETS}
        ok = (ended == 3 and n == 3 and not again and unread(rec, 'T1/R4', job) and rec['rows']['T1/R4']['outcome'] == lib.NOT_SETTLED
              and counts == {r: 0 if r == 'T1/R4' else len(lib.TWELVE[r]) for r in lib.TARGETS})
        line = f"{ended} launches ended there, {n} starts, {again} solves of it in the next; of the twelve read: {counts}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    res = []
    for row in ('T1/R4', 'T4/R4'):
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            rec = scene_run(C, Scene(memory=[(row, 40, 8.0)]), tmp)[0]
            if rec['stop']:
                return False, f"{line}; out of memory at {row}: stopped: {rec['stop']['why']}"
            counts = {r: read_count(rec, r) for r in lib.TARGETS}
            res.append(unread(rec, row, lib.NO_MEMORY) and rec['left'] == {row: lib.NO_MEMORY}
                       and counts == {r: 0 if r == row else len(lib.TWELVE[r]) for r in lib.TARGETS})
            line += f"; out of memory at {row}: {counts}"
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        gone, later = ('T1/R4', 40, 8.0), ('T4/R4', 40, 8.0)
        ended = launches(C, lambda: Scene(memory=[gone], crash=later), 1, tmp)
        last = Scene()
        rec = scene_run(C, last, tmp)[0]
        again = sum(x[:2] == gone[:2] for x in last.solved)
        if rec['stop']:
            return False, f"{line}; a later launch: stopped: {rec['stop']['why']}"
        res.append(ended == 1 and not again and unread(rec, 'T1/R4', lib.NO_MEMORY) and read_count(rec, 'T4/R4') == 5)
        line += f"; after an interruption at T4/R4, {again} solves of the job out of memory in the next launch"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return ok and all(res), line


def s22(C):
    lo, hi = 4.0, W4[9]
    job = f'locate:T4/R4:{k(lo)}:{k(hi)}'
    mid = lambda x: x[0] == 'T4/R4' and lo < x[2] < hi  # noqa: E731

    def judge(rec, why):
        r = rec['rows']['T4/R4']
        ch, pts = r['changes'][0], {k(p['eps']): p for p in r['points']}
        ends = (pts[k(lo)]['classified'], pts[k(lo)].get('type'), pts[k(hi)]['classified'], pts[k(hi)].get('type'))
        counts = {x: read_count(rec, x) for x in lib.TARGETS}
        return (not ch['located'] and ch['bracket_kind'] == 'unfinished' and why in ch['why'] and ends == (True, 'Elliptic', True, 'Hyperbolic')
                and counts == {x: len(lib.TWELVE[x]) for x in lib.TARGETS}), f"{ch['why']}; located {ch['located']}, kind {ch.get('bracket_kind')}; ends {ends}; {counts}"
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        ended, last, rec, n = exhausted(C, lambda: Scene(crash=mid), tmp, job)
        if rec is None:
            return False, f'{ended} launches ended there, and the next started it again: {n} starts in the log'
        if rec['stop']:
            return False, f"{ended} launches ended there, {n} starts; stopped: {rec['stop']['why']}"
        again = sum(mid(x) for x in last.solved)
        ok, line = judge(rec, job)
        ok = ok and ended == 3 and n == 3 and not again
        line = f'{ended} launches ended there, {n} starts, {again} midpoints in the next: {line}'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        rec = scene_run(C, Scene(memory=[('T4/R4', 24, (lo + hi) / 2)]), tmp)[0]
        if rec['stop']:
            return False, f"{line}; out of memory: stopped: {rec['stop']['why']}"
        ok2, line2 = judge(rec, lib.NO_MEMORY)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return ok and ok2, f'{line}; out of memory: {line2}'


def s23(C):
    res, lines = [], []
    for who, job, make in (('C3', 'path:C3:40', lambda: Scene(crash=('C3', 40, 1.0))), ('C1', 'C1', lambda: Scene(end_c1=KeyboardInterrupt))):
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        try:
            ended, last, rec, n = exhausted(C, make, tmp, job)
            if rec is None:
                res.append(False)
                lines.append(f'{who}: {ended} launches ended there, and the next started it again: {n} starts in the log')
                continue
            if rec['stop']:
                res.append(False)
                lines.append(f"{who}: {ended} launches ended there, {n} starts; stopped: {rec['stop']['why']}")
                continue
            log = lib.load_json(os.path.join(tmp, 'RUNLOG.json'))
            jobs = [e['event'] for e in log['events'] if e['event'].endswith(' started') and any(r in e['event'] for r in lib.TARGETS)]
            tw = rec['rows']['T1/R4']['points'][5]
            res.append(ended == 3 and n == 3 and rec['gate']['passed'] is False and job in rec['gate']['kernel'][who][0] and not jobs
                       and 'gate' in log['completed'] and not tw['classified'] and who in tw['not_read'] and rec['arm_b']['located'])
            lines.append(f"{who}: {ended} launches ended there, {n} starts: {rec['gate']['stopped']}; {len(jobs)} target jobs started")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    return all(res), ' | '.join(lines)


def s24(C):
    def judge(rec, why):
        b, row = rec['arm_b'], rec['rows']['T4/R5']
        return (b['kind'] == 'unfinished' and b['located'] is False and b['reproduced'] is False and why in b['why'] and rec['gate']['passed']
                and read_count(rec, 'T1/R4') == 5 and row['outcome'] == lib.NOT_SETTLED and why in row['changes'][0]['why']), (
                    f"Arm B: kind {b['kind']}, located {b['located']}, reproduced {b['reproduced']}, {b['why']}; "
                    f"Arm A went on: {read_count(rec, 'T1/R4')} of T1/R4's twelve read; T4/R5: {row['outcome']}")
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        ended, last, rec, n = exhausted(C, lambda: Scene(end_b=KeyboardInterrupt), tmp, 'arm_b')
        if rec is None:
            return False, f'{ended} launches ended there, and the next started it again: {n} starts in the log'
        if rec['stop']:
            return False, f"{ended} launches ended there, {n} starts; stopped: {rec['stop']['why']}"
        ok, line = judge(rec, 'arm_b')
        written = os.path.exists(os.path.join(tmp, 'ARM_B.json'))
        ok = ok and ended == 3 and n == 3 and not last.b_calls and written
        line = f'{ended} launches ended there, {n} starts, {last.b_calls} calls in the next, its record written: {written}: {line}'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        rec = scene_run(C, Scene(end_b=MemoryError), tmp)[0]
        if rec['stop']:
            return False, f"{line}; out of memory: stopped: {rec['stop']['why']}"
        ok2, line2 = judge(rec, lib.NO_MEMORY)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return ok and ok2, f'{line}; out of memory: {line2}'


def s25(C):
    job, hit = 'path:C2a:24', ('C2a', 24, 1.0)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        ended, last, rec, n = exhausted(C, lambda: Scene(crash=hit), tmp, job)
        if rec is None:
            return False, f'{ended} launches ended there, and the next started it again: {n} starts in the log'
        why = (rec['stop'] or {}).get('why', 'no stop')
        again, solved40 = sum(x[:2] == hit[:2] for x in last.solved), sum(x[1] == 40 for x in last.solved)
        no = refused(C, tmp)
        ok = (ended == 3 and n == 3 and not again and job in why and lib.UNFINISHED in why and rec['rows'] == {} and not solved40
              and os.path.exists(os.path.join(tmp, 'STOP.json')) and rec['arm_b']['located'] and no)
        line = f"{ended} launches ended there, {n} starts, {again} solves of it in the next: {why}; {len(rec['rows'])} rows; a further launch refused: {no}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        rec = scene_run(C, Scene(memory=[hit]), tmp)[0]
        why = (rec['stop'] or {}).get('why', 'no stop')
        ok2 = why == lib.NO_MEMORY and rec['rows'] == {} and os.path.exists(os.path.join(tmp, 'STOP.json')) and rec['arm_b']['located']
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return ok and ok2, f"{line}; out of memory: {why}; {len(rec['rows'])} rows"


def s26(C):
    res, lines = [], []
    real = lib.assemble

    def broken(state, located):
        raise KeyError('the scene')
    for tag, job, scene, name in (('a target', 'path:T1/R4:40', Scene(defect={('T1/R4', 40, 8.0): ValueError}), 'ValueError'),
                                  ('a control', 'path:C3:40', Scene(defect={('C3', 40, 1.0): PermissionError}), 'PermissionError'),
                                  ('the assembly', None, Scene(), 'KeyError')):
        tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
        lib.assemble = broken if tag == 'the assembly' else real
        try:
            rec = scene_run(C, scene, tmp)[0]
            lib.assemble = real
            why = (rec['stop'] or {}).get('why', 'no stop')
            n = starts(tmp, job) if job else 0
            no = refused(C, tmp) if rec['stop'] else False
            res.append(why.startswith(f'a defect in the code: {name}') and rec['rows'] == {} and n == (1 if job else 0) and no
                       and os.path.exists(os.path.join(tmp, 'STOP.json')))
            lines.append(f"{tag}: {why}; {n} starts of its job; {len(rec['rows'])} rows; a further launch refused: {no}")
        finally:
            lib.assemble = real
            shutil.rmtree(tmp, ignore_errors=True)
    return all(res), ' | '.join(lines)


def s27(C):
    ref, t2, _ = scene_run(C, Scene())
    shutil.rmtree(t2, ignore_errors=True)
    a, b = ('T1/R4', 40, 8.0), ('T4/R4', 40, 8.0)
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        n1 = launches(C, lambda: Scene(crash=a), 2, tmp)
        n2 = launches(C, lambda: Scene(crash=b), 2, tmp)
        rec = scene_run(C, Scene(), tmp)[0]
        counts = starts(tmp, 'path:T1/R4:40'), starts(tmp, 'path:T4/R4:40')
        runs = sum(e['event'].startswith('run started') for e in lib.load_json(os.path.join(tmp, 'RUNLOG.json'))['events'])
        same = strip(rec['rows']) == strip(ref['rows'])
        return (n1 == n2 == 2 and counts == (3, 3) and runs == 5 and same and not rec['stop'],
                f"{n1} and {n2} launches ended, {runs} launches in all, starts {counts}; the same record: {same}; stop: {(rec['stop'] or {}).get('why')}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def s28(C):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        rec, _, run = scene_run(C, Scene(their_bad=[('T4/R4', 32)]), tmp)
        why = (rec['stop'] or {}).get('why', 'no stop')
        done = [r for r in lib.TARGETS if f'case:{r}' in run.log['completed']]
        return ('reproducibility failure: T4/R4 at N = 32' in why and done == ['T5/R2', 'T1/R4'] and rec['rows'] == {},
                f"{why}; finished before it: {done}; {len(rec['rows'])} rows assembled")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


KILL = ('T1/R4', 40, 8.0)


def killed(tmp, path):
    """One launch of S29, on the census module at path, in this process."""
    spec = importlib.util.spec_from_file_location('census_child', path)
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    C.ROOT = ROOT
    scene_run(C, Scene(kill=KILL), tmp)


def s29(C):
    job = 'path:T1/R4:40'
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        codes = [subprocess.run([sys.executable, '-I', '-B', os.path.abspath(__file__), '--killed', tmp, C.__file__],
                                capture_output=True).returncode for _ in range(4)]
        n = starts(tmp, job)
        if codes != [-signal.SIGKILL] * 3 + [0]:
            return False, f'exit statuses {codes}; {n} starts in the log'
        rec = lib.load_json(os.path.join(tmp, 'CENSUS.json'))
        counts = {r: read_count(rec, r) for r in lib.TARGETS}
        ok = n == 3 and not rec['stop'] and unread(rec, 'T1/R4', job) and counts == {r: 0 if r == 'T1/R4' else len(lib.TWELVE[r]) for r in lib.TARGETS}
        return ok, f"exit statuses {codes}; {n} starts in the log; left: {rec['left']}; of the twelve read: {counts}"
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
    mod.ROOT = ROOT        # the mutant sits in a temporary folder and reads this folder's reference/
    return mod


def red(scene, M, raises=()):
    """(whether the scene fails on the mutant, what it reported): its claim false, or the run raising the one exception
    the mutation lets out. Any other exception is a defect of the arm, and it stops this test."""
    try:
        ok, detail = scene(M)
        return not ok, detail
    except raises as e:
        return True, f'{type(e).__name__}: {e}'


def main():
    devtools.require('seedcheck')
    say('Test 6, the gates and the read, through the run\'s whole order, on stub solves, in a seedcheck process.')
    fails = 0
    scenes = [('S1', s1), ('S2', s2), ('S3', s3), ('S4', s4), ('S5', s5), ('S6', s6), ('S7', s7), ('S8', s8), ('S9', s9),
              ('S10', s10), ('S11', s11), ('S12', s12), ('S13', s13), ('S14', s14), ('S15', s15), ('S16', s16), ('S17', s17),
              ('S18', s18), ('S19', s19), ('S20', s20), ('S21', s21), ('S22', s22), ('S23', s23), ('S24', s24), ('S25', s25),
              ('S26', s26), ('S27', s27), ('S28', s28), ('S29', s29)]
    lines = {}
    for tag, f in scenes:
        ok, lines[tag] = f(census)
        say(f"{tag}. {'PASS' if ok else 'FAIL'}: {lines[tag]}")
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
        id40 = "ids40[name] = self.identity_job(name, lib.ARM_A['pairs'][1], where, tops[name])\n"
        kn = ("                if not gate['kernel'][name]:\n                    " + id40 + "            except (MemoryError, Unfinished) as e:\n"
              "                gate['kernel'][name] = [self.cause(e)]\n            self.cuts.clear()\n            if gate['kernel'][name]:\n")
        un = ("                " + id40 + "            except (MemoryError, Unfinished) as e:\n                gate['kernel'][name] = [self.cause(e)]\n"
              "            self.cuts.clear()\n            if False:\n")
        arms.append(("the kernel's stop removed: S2", red(s2, mutant(src, kn, un, 'a4', tmp))))
        rp = "            self.reproduce(name, N, recs[N], theirs)\n"
        arms.append(('the reproduction check removed: S5', red(s5, mutant(src, rp, '', 'a5', tmp))))
        pth = "            s = self.solve(state, e, prev_accepted=acc)\n"
        arms.append(('a read at every point of a path: S1', red(s1, mutant(src, pth, "            s = self.read(self.solve(state, e, prev_accepted=acc), e, 'path')\n", 'a6', tmp))))
        adm = "            fails += [f'the end at {e:g}: {x}' for x in lib.admissible(rec['ends'][k], cls[k], case, lad, lib.on(e, lib.PATHS[row]))]\n"
        arms.append(("the borrowed end's check removed: S12", red(s12, mutant(src, adm, '', 'a7', tmp))))
        tw = "        recs = {**recs, lib.TOP: self.read_job(row, lib.TOP, twelve, 'twelve')}\n"
        arms.append(('every path point read at N = 40: S1', red(s1, mutant(src, tw, "        recs = {**recs, lib.TOP: self.read_job(row, lib.TOP, where, 'twelve')}\n", 'a8', tmp))))
        hash_ = "        st, cu = self.stored(name, N), self.cutoff(name, N)\n"
        arms.append(('a read that skips the solve-state gate: S13', red(s13, mutant(src, hash_, "        cu = self.cutoff(name, N)\n        st = dict(seed={}, sols={})\n", 'a9', tmp))))
        loc_a = "        return self.write(job, fname, rec, [self.keep_located(job, cuts)])\n"
        arms.append(("Arm A's location, its solutions file not logged: S1", red(s1, mutant(src, loc_a, "        self.keep_located(job, cuts)\n        return self.write(job, fname, rec)\n", 'a10', tmp))))
        loc_b = "            rec = self.write(job, fname, rec, [self.keep_located('arm_b', cuts)])\n"
        arms.append(("Arm B's location, its solutions file not logged: S1", red(s1, mutant(src, loc_b, "            self.keep_located('arm_b', cuts)\n            rec = self.write(job, fname, rec)\n", 'a11', tmp))))
        oc1 = "            if not self.opened():\n                raise PermissionError(f\"a solve at N = {lib.TOP} before Arm B's record is written\")\n"
        arms.append(("the order check in C1 removed: S7", red(s7, mutant(src, oc1, '', 'a12', tmp))))
        rs = "        if self.done(job):\n            rec = lib.load_json(self.at(fname))\n        else:\n            row, lad = lib.ARM_B_ROW, lib.ARM_B\n"
        arms.append(("a resume that passes over Arm B's stop: S14", red(s14, mutant(src, rs, rs.replace('rec = lib', 'return lib'), 'a13', tmp))))
        both = '(MemoryError, Unfinished)'
        mc = f"            except {both} as e:\n                gate['kernel'][name] = [self.cause(e)]\n"
        arms.append(('the memory failure not caught at a control: S15', red(s15, mutant(src, mc, mc.replace(both, 'Unfinished'), 'a14', tmp))))
        arms.append(('the unfinished job not caught at a control: S23', red(s23, mutant(src, mc, mc.replace(both, 'MemoryError'), 'a14b', tmp))))
        m1 = f"        except {both} as e:\n            c1 = [self.cause(e)]\n"
        arms.append(('the memory failure not caught at C1: S15', red(s15, mutant(src, m1, m1.replace(both, 'Unfinished'), 'a15', tmp))))
        arms.append(('the unfinished job not caught at C1: S23', red(s23, mutant(src, m1, m1.replace(both, 'MemoryError'), 'a15b', tmp))))
        bd = "            if bands:\n                raise StopRun(f'the band: {bands[0]}', bands)\n"
        arms.append(("the band's stop removed: S16", red(s16, mutant(src, bd, '', 'a16', tmp))))
        gl = "    for (row, _, _), rec in located.items():\n        if row == ARM_B_ROW:\n"
        off = mutant(open(lib.__file__, encoding='utf-8').read(), gl, gl.replace('located.items()', '{}.items()'), 'a16b', tmp).band_failures
        arms.append(("the guards' band test removed, in census_lib.py: S16", red(with_band(off), census)))
        oos = "        except Exception as e:\n            self.stop(f'a defect in the code: {type(e).__name__}: {e}', traceback.format_exc())\n"
        arms.append(("the refused read's stop removed: S17", red(s17, mutant(src, oos, '', 'a17', tmp), lib.OutOfScope)))
        br_ = "            if (lib.key(ch['lo']), lib.key(ch['hi'])) != tuple(map(lib.key, lib.BRACKET_B)):\n"
        arms.append(("the bracket's check removed: S18", red(s18, mutant(src, br_, '            if False:\n', 'a18', tmp))))
        held = "                gate['kernel'][name] = [self.cause(e)]\n            self.cuts.clear()\n"
        arms.append(("a control's cutoffs kept: S19", red(s19, mutant(src, held, held.replace('            self.cuts.clear()\n', ''), 'a19', tmp))))
        arms.append(('every end taken as on the path: S20', red(s20, mutant(src, 'cls[k], case, lad, lib.on(e, lib.PATHS[row]))]', 'cls[k], case, lad, True)]', 'a20', tmp))))
        pk = ",\n                                          peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)\n"
        arms.append(('the peak size not logged: S1', red(s1, mutant(src, pk, ')\n', 'a21', tmp))))
        tw2 = tw.replace('twelve, ', 'where, ', 1).replace("'twelve'", "'twelve'")
        arms.append(("no scope check, every path point read, for the spy's count: S1", red(s1, mutant(src.replace(scope, ''), tw, tw2, 'a22', tmp))))
        tg = f"                    except {both} as e:\n                        left[row] = self.cause(e)\n"
        arms.append(("the unfinished job not caught at a target: S21", red(s21, mutant(src, tg, tg.replace(both, 'MemoryError'), 'a23', tmp))))
        arms.append(("the memory failure not caught at a target: S21", red(s21, mutant(src, tg, tg.replace(both, 'Unfinished'), 'a24', tmp))))
        lc = f"                    except {both} as e:\n                        located[bracket] = lib.not_located(ch, self.cause(e))\n"
        arms.append(("the unfinished job not caught at a location: S22", red(s22, mutant(src, lc, lc.replace(both, 'MemoryError'), 'a25', tmp))))
        arms.append(("the memory failure not caught at a location: S22", red(s22, mutant(src, lc, lc.replace(both, 'Unfinished'), 'a26', tmp))))
        ab = f"            except {both} as e:\n                rec, cuts = lib.not_located(ch, self.cause(e)), {{}}\n"
        arms.append(("the unfinished job not caught in Arm B: S24", red(s24, mutant(src, ab, ab.replace(both, 'MemoryError'), 'a27', tmp))))
        arms.append(("the memory failure not caught in Arm B: S24", red(s24, mutant(src, ab, ab.replace(both, 'Unfinished'), 'a28', tmp))))
        mo = "        except MemoryError:\n            self.stop(lib.NO_MEMORY, self.job)\n"
        arms.append(("out of memory taken for a defect: S25", red(s25, mutant(src, mo, '', 'a29', tmp))))
        lim = "        if job not in ended and sum(e['event'] == started for e in self.log['events']) >= lib.ATTEMPTS:\n"
        arms.append(("the limit ignored: S21", red(s21, mutant(src, lim, '        if False:\n', 'a30', tmp))))
        wr = "        self.log['events'].append(dict(t=dr.now(), event=started))\n        dr.save_log(self.out, self.log)\n"
        arms.append(("a start not written before the solve: S21", red(s21, mutant(src, wr, wr.split('\n')[0] + '\n', 'a31', tmp))))
        res_ = "        log = self.log\n        if log['completed'] or log['events']:\n"
        arms.append(("a resume that forgets the starts: S21", red(s21, mutant(src, res_, res_.replace("log = self.log\n", "log = self.log\n        log['events'] = [e for e in log['events'] if not e['event'].endswith(' started')]\n"), 'a32', tmp))))
        hd = "            self.log.setdefault('ended', {})[self.job] = lib.NO_MEMORY\n            dr.save_log(self.out, self.log)\n"
        arms.append(("a job out of memory started again: S21", red(s21, mutant(src, hd, '            pass\n', 'a32b', tmp))))
        arms.append(("the count taken from launches: S27", red(s27, mutant(src, lim, lim.replace("e['event'] == started", "e['event'].startswith('run started')"), 'a33', tmp))))
        arms.append(("the catch of a defect removed: S26", red(s26, mutant(src, oos, '', 'a34', tmp), (ValueError, PermissionError, KeyError))))
        arms.append(("a broad handler at a target, a defect taken for a limit: S26", red(s26, mutant(src, tg, tg.replace(both, 'Exception').replace('self.cause(e)', 'str(e)'), 'a35', tmp))))
        arms.append(("a broad handler at a control, a defect taken for a limit: S26", red(s26, mutant(src, mc, mc.replace(both, 'Exception').replace('self.cause(e)', 'str(e)'), 'a36', tmp))))
        arms.append(("a start not written before the solve, under a real kill: S29", red(s29, mutant(src, wr, wr.split('\n')[0] + '\n', 'a38', tmp))))
        arms.append(("a broad handler at a target, a stop taken for a limit: S28", red(s28, mutant(src, tg, tg.replace(both, '(MemoryError, StopRun)'), 'a37', tmp))))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say('arms, each a mutation of census.py, one of census_lib.py, that must turn its scene red:')
    for label, (r, detail) in arms:
        same = detail == lines[label.rsplit(': ', 1)[1]]
        say(f"   {label}: {'GREEN' if not r else 'SAME LINE' if same else 'RED'}: {detail}")
        fails += not r or same
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_scope.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    if sys.argv[1:2] == ['--killed']:
        devtools.require('seedcheck')
        killed(sys.argv[2], sys.argv[3])
    else:
        main()
