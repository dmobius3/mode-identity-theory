"""The smoke test (M8.19's terms: THE TESTS BEFORE THE FREEZE: "a smoke test of four jobs at once on the controls'
recorded points, at a short T and read for nothing: one thread each, each record under its own path, and the
orchestrator's order"). It launches the orchestrator's bench plan 'smoke' into dev/runs/smoke/, samples every job
process's threads and the number running at once every two seconds, then reads the log: the order of starts, each
job's own folder and files. Each job's series, to T = 20, is also compared with the first rows of M8.15.x's recorded
series for the same control (C2a/R4's duration control against the C2a control's), which its path must reproduce.

  smoke.py      writes dev/smoke.out; exits 1 if a check fails"""
import json
import os
import shutil
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'runs', 'smoke')
QOUT = os.path.normpath(os.path.join(ROOT, '..', 'soft-slot-dynamics-m8-15x', 'qualification', 'solver', 'm8_15_solver',
                                     'out'))
lines, fails = [], []


def say(s):
    print(s, flush=True)
    lines.append(s)


def check(name, good, detail=''):
    say(f"{'ok  ' if good else 'FAIL'} {name}" + (f': {detail}' if detail else ''))
    if not good:
        fails.append(name)


if os.path.exists(OUT):
    shutil.rmtree(OUT)
pr = subprocess.Popen([sys.executable, '-I', '-B', '-u', os.path.join(ROOT, 'run', 'm819_run.py'), '--bench', 'smoke', OUT],
                      stdout=open(os.path.join(HERE, 'runs', 'smoke.console'), 'w'), stderr=subprocess.STDOUT)
threads, most = {}, 0
while pr.poll() is None:
    ps = subprocess.run(['ps', '-Ao', 'pid,command'], capture_output=True, text=True).stdout.splitlines()
    jobs = [(int(l.split()[0]), l.split('m819_branch.py ')[1].split()[0]) for l in ps if 'run/m819_branch.py' in l
            and '-I' in l and OUT in l]
    most = max(most, len(jobs))
    for pid, j in jobs:
        t = subprocess.run(['ps', '-M', '-p', str(pid)], capture_output=True, text=True).stdout.splitlines()
        if len(t) > 1:
            threads[j] = max(threads.get(j, 0), len(t) - 1)
    time.sleep(2)
L = json.load(open(os.path.join(OUT, 'RUNLOG.json')))
starts = [e['job'] for e in L['events'] if e['event'] == 'started']
check('four jobs ran at once, never more', most == 4, f'at most {most}')
compute = [j for j in starts if j != 'controls']    # gate 1's reader runs about a second, under the two-second sampling
check('one thread each, every computing job sampled', set(compute) <= set(threads) and all(v == 1 for v in threads.values()),
      str(threads))
check("the orchestrator's order: the four controls, then the duration control as one ends, then gate 1",
      starts == ['dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'c2a_dur', 'controls'], str(starts))
first_end = min(i for i, e in enumerate(L['events']) if e['event'] == 'completed')
fifth = next(i for i, e in enumerate(L['events']) if e['event'] == 'started' and e['job'] == 'c2a_dur')
check('the fifth job started only after one of the four completed', fifth > first_end)
check('every job completed in its own folder', sorted(L['completed']) == sorted(starts)
      and all(os.path.isdir(os.path.join(OUT, j)) for j in starts))
paths = [os.path.join(j, f) for j, r in L['completed'].items() for f in r['files']]
check('no two records share a path', len(paths) == len(set(paths)), f'{len(paths)} files')
for job, tag, npy in (('dyn_C1', 'C1', 'dynamics_C1.npy'), ('dyn_C2a', 'C2a', 'dynamics_C2a.npy'),
                      ('dyn_C2b', 'C2b', 'dynamics_C2b.npy'), ('dyn_C3', 'C3', 'dynamics_C3.npy'),
                      ('c2a_dur', 'C2a', 'test.npy')):
    a = np.load(os.path.join(OUT, job, npy))
    b = np.load(os.path.join(QOUT, f'dynamics_{tag}.npy'))[:len(a)]
    check(f'{job}: its {len(a)} rows to T = 20 equal the first rows of M8.15.x\'s {tag} series, bit for bit',
          a.tobytes() == b.tobytes())
say('PASS' if not fails else f'FAIL: {fails}')
with open(os.path.join(HERE, 'smoke.out'), 'w') as f:
    f.write('\n'.join(lines) + '\n')
raise SystemExit(1 if fails else 0)
