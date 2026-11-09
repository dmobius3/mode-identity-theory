"""The run's failure paths (DESIGN.md, the dry run's step 6), through the orchestrator on cheap control jobs: C1 at 6
at a short T, inside its recorded T = 1000, and armed exceptions at a stage before any solve. Each scenario runs in its
own folder under dev/runs/launch_tests/ and is read from its RUNLOG.json and folders alone.

  1. a job that raises on every start, over three launches: each launch starts it once, each start's folder is moved
     aside, and the first two launches end with it and what needs it pending; on the third it ends, what needs it is
     not run, and what only waits on it runs;
  2. a job killed by a signal: its start ends with the signal, the launch ends with it pending, and a relaunch starts it
     again and it completes;
  3. the orchestrator killed while a job runs: a relaunch refuses while the job's process lives, and once it has ended
     the relaunch ends that start, moves its folder aside and starts the job again, counting the start;
  4. a refusal (a sealed job on the bench): the run stops, and a relaunch refuses the stopped run.
In every scene, no launch starts a job twice (DESIGN.md, reading 4).

  test_launch.py      prints each check; exits 1 if any fails"""
import json
import os
import shutil
import signal
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, 'runs', 'launch_tests')
RUNNER = os.path.join(HERE, 'launch_runner.py')
fails = []


def check(name, good, detail=''):
    print(f"{'ok  ' if good else 'FAIL'} {name}" + (f': {detail}' if detail else ''), flush=True)
    if not good:
        fails.append(name)


def job(id, args=(), needs=(), after=()):
    return dict(id=id, wave=1, args=list(args), needs=list(needs), after=list(after), gate1=False)


def folder(name, jobs):
    d = os.path.join(BASE, name)
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    p = os.path.join(d, 'jobs.json')
    with open(p, 'w') as f:
        json.dump(jobs, f)
    return d, p


def launch(d, p, wait=True):
    cmd = [sys.executable, '-I', '-B', '-u', RUNNER, os.path.join(d, 'out'), p, f'launch test {os.path.basename(d)}']
    log = open(os.path.join(d, 'launches.log'), 'a')
    pr = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
    if wait:
        pr.wait()
    return pr


def runlog(d):
    with open(os.path.join(d, 'out', 'RUNLOG.json')) as f:
        return json.load(f)


def events(L, kind, j=None):
    return [e for e in L['events'] if e['event'] == kind and (j is None or e.get('job') == j)]


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


def wait_for(cond, timeout=600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            if cond():
                return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
        time.sleep(1)
    return False


def alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False


# 1. a job that raises on every start, over three launches
d, p = folder('1_raise', [job('dyn_C1', ['--T', '5', '--test-raise-at', 'dynamics']),
                          job('dyn_C2b', ['--T', '5'], needs=['dyn_C1']), job('controls', after=['dyn_C1', 'dyn_C2b'])])
for _ in range(3):
    launch(d, p)
L = runlog(d)
en = events(L, 'ended', 'dyn_C1')
check('1: three launches, each starting the raising job once, and each start ended',
      len(L['launches']) == 3 and per_launch(L, 'dyn_C1') == [1, 1, 1] and len(en) == 3,
      f"{len(L['launches'])} launches, starts by launch {per_launch(L, 'dyn_C1')}, {len(en)} ends")
check('1: each end names the forced exception and its stage',
      all('RuntimeError at stage dynamics' in e['cause'] for e in en), en[0]['cause'] if en else '')
le = events(L, 'launch ended')
check('1: the first two launches ended with it and what needs it pending',
      len(le) == 3 and all({'dyn_C1', 'dyn_C2b', 'controls'} <= set(e['pending']) for e in le[:2]),
      str([e.get('pending') for e in le]))
third = [i for i, e in enumerate(L['events']) if e['event'] == 'launch'][2]
check('1: on the third launch, the job ended its part of the run', 'dyn_C1' in L['ended']
      and L['ended']['dyn_C1']['starts'] == 3)
check('1: what needs it is not run, with the cause, only on the third launch',
      L['not_run'].get('dyn_C2b', {}).get('why') == 'dyn_C1 did not complete' and at(L, 'not run', 'dyn_C2b') > third)
check('1: what only waits on it runs and completes, on the third launch', 'controls' in L['completed']
      and at(L, 'started', 'controls') > third)
inter = sorted(os.listdir(os.path.join(d, 'out', 'interrupted')))
check("1: each start's folder is moved aside, none into the run", inter == ['dyn_C1.1', 'dyn_C1.2', 'dyn_C1.3']
      and not os.path.exists(os.path.join(d, 'out', 'dyn_C1')), str(inter))
c = json.load(open(os.path.join(d, 'out', 'controls', 'CONTROLS.json')))
check('1: gate 1 reads the ended job as not completed', c['controls']['dyn_C1'] == dict(passed=False, why='not completed')
      and not c['all_passed'])

# 2. a job killed by a signal: the launch ends with it pending, and a relaunch completes it
d, p = folder('2_kill', [job('dyn_C1', ['--T', '5'])])
pr = launch(d, p, wait=False)
ok = wait_for(lambda: events(runlog(d), 'process', 'dyn_C1'))
pid = events(runlog(d), 'process', 'dyn_C1')[0]['pid']
time.sleep(3)
os.kill(pid, signal.SIGKILL)
pr.wait()
L = runlog(d)
en = events(L, 'ended', 'dyn_C1')
check('2: the killed start ended with the signal', len(en) == 1 and en[0]['cause'] == 'ended by signal 9', str(en))
check('2: the launch ended with the job pending, not started again', len(events(L, 'started', 'dyn_C1')) == 1
      and events(L, 'launch ended')[-1].get('pending') == ['dyn_C1'], str(events(L, 'launch ended')))
launch(d, p)
L = runlog(d)
check('2: a relaunch started it again and it completed', len(L['launches']) == 2 and per_launch(L, 'dyn_C1') == [1, 1]
      and L['completed'].get('dyn_C1', {}).get('start') == 2)
check("2: the killed start's folder is aside, the completed one in the run",
      os.listdir(os.path.join(d, 'out', 'interrupted')) == ['dyn_C1.1'] and os.path.isdir(os.path.join(d, 'out', 'dyn_C1')))

# 3. the orchestrator killed while a job runs
d, p = folder('3_orchestrator', [job('dyn_C1', ['--T', '20'])])
pr = launch(d, p, wait=False)
wait_for(lambda: events(runlog(d), 'process', 'dyn_C1'))
pid = events(runlog(d), 'process', 'dyn_C1')[0]['pid']
time.sleep(2)
os.kill(pr.pid, signal.SIGKILL)
pr.wait()
check('3: the job outlives the orchestrator', alive(pid))
r = subprocess.run([sys.executable, '-I', '-B', '-u', RUNNER, os.path.join(d, 'out'), p, 'launch test 3_orchestrator'],
                   capture_output=True, text=True)
check('3: a relaunch refuses while the job lives', r.returncode != 0 and 'still running' in (r.stdout + r.stderr),
      (r.stdout + r.stderr).strip()[-120:])
wait_for(lambda: not alive(pid), timeout=1200)
launch(d, p)
L = runlog(d)
en = events(L, 'ended', 'dyn_C1')
check('3: the relaunch ends the open start', len(en) == 1 and en[0]['start'] == 1
      and en[0]['cause'] == 'the launch that started it ended before it', str(en))
check('3: and starts the job again, counting the start', L['completed'].get('dyn_C1', {}).get('start') == 2
      and len(L['launches']) == 2)
check("3: the open start's folder, complete or not, is aside and not read",
      os.listdir(os.path.join(d, 'out', 'interrupted')) == ['dyn_C1.1'])

# 4. a refusal stops the run
d, p = folder('4_refusal', [job('gates_T1_R4'), job('dyn_C1', ['--T', '5'], needs=['gates_T1_R4'])])
launch(d, p)
L = runlog(d)
check('4: the sealed job refused on the bench and the run stopped', bool(L['stop'])
      and 'sealed' in L['stop']['why'] and 'dyn_C1' not in L['completed'], str(L['stop']))
r = subprocess.run([sys.executable, '-I', '-B', '-u', RUNNER, os.path.join(d, 'out'), p, 'launch test 4_refusal'],
                   capture_output=True, text=True)
check('4: a relaunch refuses the stopped run', r.returncode != 0 and 'the run stopped' in (r.stdout + r.stderr))
for name in ('1_raise', '2_kill', '3_orchestrator', '4_refusal'):
    bad = twice(runlog(os.path.join(BASE, name)))
    check(f'{name[0]}: no launch started a job twice', not bad, str(bad))
print('PASS' if not fails else f'FAIL: {fails}')
raise SystemExit(1 if fails else 0)
