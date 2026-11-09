"""The registered run's whole order on a stub (DESIGN.md, the dry run's steps 6 and 9): the orchestrator's registered
plan, launched as the run launches it but with dev/stub_branch.py as the driver, in four scenarios. Read from each run's
RUNLOG.json, its records and the spy's log of the sealed jobs' guard calls. Nothing is solved.

  A. Gate 1 passes; T1's three stretches untested; T4/R4 tested at T = 2750; T4/R5 at T = 15750, so the longest control
     runs at 15750 and that test waits for it; the coherent row tested at 1000. The waves in order, at most four at
     once, every sealed job's guard after gate 1, the T4/R5 test after the longest control, and the record.
  B. C3 at 3 does not Fail: gate 1 fails, no sealed job starts, and the record says why.
  C. The longest control does not Persist: the test it covers is not run, with the cause; the others run.
  D. A gates job raises on every start, over three launches, each starting it once: it ends on the third, its stretch
     goes to adjudication, and the plan, which waits for it, and the rest run.
  E. A wave-1 control, C2a, raises on every start, over three launches: gate 1 runs only after the third and fails on
     it; no gates job or plan ever starts, each is not run with gate 1 named, no sealed guard is called, and the record
     sends every stretch and the coherent row's ladder to adjudication.
  F. The longest control raises on every start, over three launches: the test longer than 2750 never starts and is not
     run, with the cause; the tests up to 2750 run on the first launch; the record sends T4/R5 to adjudication.
In every scenario, no launch starts a job twice (DESIGN.md, reading 4).

  test_scope.py      prints each check; exits 1 if any fails"""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import m819_run as R  # noqa: E402

BASE = os.path.join(HERE, 'runs', 'scope_tests')
fails = []


def check(name, good, detail=''):
    print(f"{'ok  ' if good else 'FAIL'} {name}" + (f': {detail}' if detail else ''), flush=True)
    if not good:
        fails.append(name)


def st(sid, label, test=None, causes=None):
    return {sid: dict(label=label, points=[0.25, 1.0], test=test, causes=causes or {'0.25': 3, '1.0': 3})}


def scenario(**kw):
    sc = dict(dyn={'C3': 'Fails'}, p5a=True, c3e3=True, c2a_dur=True, c2a_long=True,
              gates={'gates_T1_R4': dict(stretches={**st('T1_R4_1', 'T1/R4, lower'), **st('T1_R4_2', 'T1/R4, upper')}),
                     'gates_T1_R5': dict(stretches=st('T1_R5_1', 'T1/R5')),
                     'gates_T4_R4': dict(stretches=st('T4_R4_1', 'T4/R4', dict(eps=2.8284271247461903, T=2750.0, P=2700.0), {})),
                     'gates_T4_R5': dict(stretches=st('T4_R5_1', 'T4/R5', dict(eps=5.656854249492381, T=15750.0, P=15658.0), {})),
                     'coherent_R5': dict(stretches=st('C2a_R5_1', 'The coherent row in R5', dict(eps=32.0, T=1000.0, P=157.0), {}))},
              verdicts={'T4_R4_1': 'Persists', 'T4_R5_1': 'Unresolved', 'C2a_R5_1': 'Persists'})
    sc.update(kw)
    return sc


def run(name, sc, launches=1):
    d = os.path.join(BASE, name)
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    scp, jobs, spy = os.path.join(d, 'scenario.json'), os.path.join(d, 'jobs.json'), os.path.join(d, 'spy.log')
    json.dump(sc, open(scp, 'w'))
    json.dump(R.registered(), open(jobs, 'w'))
    env = dict(os.environ, M819_SCENARIO=scp, M819_SPY=spy)
    for _ in range(launches):
        subprocess.run([sys.executable, '-I', '-B', '-u', os.path.join(HERE, 'launch_runner.py'), os.path.join(d, 'out'),
                        jobs, f'scope {name}', os.path.join(HERE, 'stub_branch.py'), '--registered-order'],
                       env=env, stdout=open(os.path.join(d, 'console.log'), 'a'), stderr=subprocess.STDOUT, check=False)
    L = json.load(open(os.path.join(d, 'out', 'RUNLOG.json')))
    calls = [json.loads(x) for x in open(spy)] if os.path.exists(spy) else []
    rec = json.load(open(os.path.join(d, 'out', 'record', 'RECORD.json'))) if 'record' in L['completed'] else None
    return L, calls, rec


def at(L, kind, j):
    return next((i for i, e in enumerate(L['events']) if e['event'] == kind and e.get('job') == j), None)


def per_launch(L, j):
    """The starts of job j in each launch, in order."""
    n = []
    for e in L['events']:
        if e['event'] == 'launch':
            n.append(0)
        elif e['event'] == 'started' and e['job'] == j:
            n[-1] += 1
    return n


def twice(L):
    """The jobs some launch started more than once."""
    seen, bad = set(), []
    for e in L['events']:
        if e['event'] == 'launch':
            seen = set()
        elif e['event'] == 'started':
            if e['job'] in seen:
                bad.append(e['job'])
            seen.add(e['job'])
    return bad


def most_at_once(L):
    n = m = 0
    for e in L['events']:
        if e['event'] == 'process':
            n += 1
        elif e['event'] in ('completed', 'ended'):
            n -= 1
        m = max(m, n)
    return m


# A
L, calls, rec = run('A', scenario())
order = [e['job'] for e in L['events'] if e['event'] == 'started']
check('A: every job completed, nothing ended or not run', not L['ended'] and not L['not_run']
      and set(L['completed']) == set(order), f'{len(L["completed"])} completed')
check('A: at most four at once', most_at_once(L) <= 4, str(most_at_once(L)))
check('A: wave 1 in the terms\' order, gate 1 after all of it', order[:9] == R.WAVE1 + ['controls']
      and at(L, 'started', 'controls') > max(at(L, 'completed', j) for j in R.WAVE1), str(order[:9]))
check('A: no gates job before gate 1 completed', min(at(L, 'started', j) for j in R.ROWS) > at(L, 'completed', 'controls'))
check('A: the plan after every gates job', at(L, 'started', 'plan') > max(at(L, 'completed', j) for j in R.ROWS))
long_ = next(j for j in L['jobs'] if j['id'] == 'c2a_long')
check('A: the longest control at the longest T', long_['args'] == ['--long-T', '15750.0'], str(long_['args']))
check('A: the T4/R5 test (T = 15750) after the longest control', at(L, 'started', 'test_T4_R5_1') > at(L, 'completed', 'c2a_long'))
check('A: the shorter tests need no longest control', at(L, 'started', 'test_T4_R4_1') < at(L, 'completed', 'c2a_long')
      and at(L, 'started', 'test_C2a_R5_1') < at(L, 'completed', 'c2a_long'))
check('A: the record last', at(L, 'started', 'record') > max(at(L, 'completed', j) for j in L['completed'] if j != 'record'))
sealed = sorted(c['job'] for c in calls)
check("A: each sealed job's guard was called", sealed == sorted(R.ROWS + ['test_C2a_R5_1', 'test_T4_R4_1', 'test_T4_R5_1']),
      str(sealed))
S = rec['stretches']
check('A: the record: T1 untested, T4/R4 tested, T4/R5 Unresolved, the coherent row tested',
      [S[k]['outcome'][:9] for k in ('T1_R4_1', 'T1_R4_2', 'T1_R5_1', 'T4_R4_1', 'T4_R5_1', 'C2a_R5_1')]
      == ['Untested', 'Untested', 'Untested', 'tested', 'tested, U', 'tested'], str({k: v['outcome'] for k, v in S.items()}))
check("A: the coherent row's ladder recorded apart, nothing newly identified",
      rec['coherent_ladder'] == dict(established=True, stub=True, other_elliptic_runs=[]) and rec['newly_identified'] == {})

# B
L, calls, rec = run('B', scenario(c3e3=False))
c = json.load(open(os.path.join(BASE, 'B', 'out', 'controls', 'CONTROLS.json')))
check('B: gate 1 fails on C3 at 3', not c['all_passed'] and not c['controls']['c3e3']['passed'])
check('B: no sealed job started', not calls and all(j not in [e.get('job') for e in L['events'] if e['event'] == 'started']
                                                    for j in R.ROWS))
check('B: the gates jobs and the plan not run, gate 1 named', all(L['not_run'].get(j, {}).get('why') == 'gate 1 did not pass'
                                                                  for j in R.ROWS + ['plan']))
check('B: the record runs and sends every stretch to adjudication', rec is not None
      and all(v['outcome'] == 'for adjudication' for v in rec['stretches'].values()) and len(rec['stretches']) == 6)
check("B: the coherent row's ladder sent for adjudication, gate 1 named",
      rec['coherent_ladder'] == dict(outcome='for adjudication', why='coherent_R5: gate 1 did not pass'))

# C
L, calls, rec = run('C', scenario(c2a_long=False))
check('C: the T4/R5 test not run, the longest control named',
      L['not_run'].get('test_T4_R5_1', {}).get('why') == 'the longest control did not Persist, valid')
check('C: the shorter tests ran', 'test_T4_R4_1' in L['completed'] and 'test_C2a_R5_1' in L['completed'])
check("C: the record sends T4/R5 to adjudication with the cause", rec['stretches']['T4_R5_1']['outcome'] == 'for adjudication'
      and 'longest control' in rec['stretches']['T4_R5_1']['why'], rec['stretches']['T4_R5_1'].get('why', ''))
check('C: the run did not stop', not L['stop'])

# D
sc = scenario()
sc['gates']['gates_T4_R4'] = 'crash'
L, calls, rec = run('D', sc, launches=3)
check('D: three launches, each starting the raising gates job once', len(L['launches']) == 3
      and per_launch(L, 'gates_T4_R4') == [1, 1, 1], str(per_launch(L, 'gates_T4_R4')))
third = [i for i, e in enumerate(L['events']) if e['event'] == 'launch'][2]
check('D: the plan waited for the third launch', at(L, 'started', 'plan') > third)
check('D: the raising gates job ended after three starts', L['ended'].get('gates_T4_R4', {}).get('starts') == 3)
check('D: the plan ran without it and the other tests ran', 'plan' in L['completed'] and 'test_T4_R5_1' in L['completed'])
check('D: the record sends T4/R4 to adjudication with the cause', rec['stretches']['T4_R4_1']['outcome'] == 'for adjudication'
      and 'RuntimeError' in rec['stretches']['T4_R4_1']['why'], rec['stretches']['T4_R4_1'].get('why', ''))
# E
L, calls, rec = run('E', scenario(raising=['dyn_C2a']), launches=3)
launches = [i for i, e in enumerate(L['events']) if e['event'] == 'launch']
started = {e['job'] for e in L['events'] if e['event'] == 'started'}
check('E: three launches, each starting the raising control once, then it ended',
      per_launch(L, 'dyn_C2a') == [1, 1, 1] and L['ended'].get('dyn_C2a', {}).get('starts') == 3, str(per_launch(L, 'dyn_C2a')))
c = json.load(open(os.path.join(BASE, 'E', 'out', 'controls', 'CONTROLS.json')))
check('E: gate 1 ran only on the third launch, and failed on the control',
      len(launches) == 3 and at(L, 'started', 'controls') > launches[2]
      and c['controls']['dyn_C2a'] == dict(passed=False, why='not completed') and not c['all_passed'])
check('E: no gates job and no plan ever started', not started & set(R.ROWS + ['plan']), str(sorted(started & set(R.ROWS + ['plan']))))
check('E: each not run, gate 1 named', all(L['not_run'].get(j, {}).get('why') == 'gate 1 did not pass' for j in R.ROWS + ['plan']))
check('E: no sealed guard was called', not calls, str(calls))
check("E: the record sends every stretch and the coherent row's ladder to adjudication", rec is not None
      and len(rec['stretches']) == 6 and all(v['outcome'] == 'for adjudication' for v in rec['stretches'].values())
      and rec['coherent_ladder'] == dict(outcome='for adjudication', why='coherent_R5: gate 1 did not pass'))

# F
L, calls, rec = run('F', scenario(raising=['c2a_long']), launches=3)
launches = [i for i, e in enumerate(L['events']) if e['event'] == 'launch']
check('F: three launches, each starting the longest control once, then it ended',
      per_launch(L, 'c2a_long') == [1, 1, 1] and L['ended'].get('c2a_long', {}).get('starts') == 3, str(per_launch(L, 'c2a_long')))
check('F: the test longer than 2750 never started, and is not run with the cause',
      at(L, 'started', 'test_T4_R5_1') is None and L['not_run'].get('test_T4_R5_1', {}).get('why') == 'c2a_long did not complete'
      and not any(x['job'] == 'test_T4_R5_1' for x in calls), str(L['not_run'].get('test_T4_R5_1')))
check('F: the tests up to 2750 ran on the first launch', all(j in L['completed'] and at(L, 'completed', j) < launches[1]
                                                             for j in ('test_T4_R4_1', 'test_C2a_R5_1')))
check('F: the record sends T4/R5 to adjudication with the cause, and records the others tested',
      rec['stretches']['T4_R5_1']['outcome'] == 'for adjudication' and 'c2a_long did not complete' in rec['stretches']['T4_R5_1']['why']
      and rec['stretches']['T4_R4_1']['outcome'] == 'tested' and rec['stretches']['C2a_R5_1']['outcome'] == 'tested',
      rec['stretches']['T4_R5_1'].get('why', ''))
check('F: the run did not stop', not L['stop'])

for name in 'ABCDEF':
    bad = twice(json.load(open(os.path.join(BASE, name, 'out', 'RUNLOG.json'))))
    check(f'{name}: no launch started a job twice', not bad, str(bad))
print('PASS' if not fails else f'FAIL: {fails}')
raise SystemExit(1 if fails else 0)
