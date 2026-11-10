"""Scratch only: M8.19's registered launch as it runs, `python3 -I -B -u run/m819_run.py` from the folder, past both of
main()'s checks into launch(), in a copy of run/ and reference/ beside a link to the instrument, with the environment
recorded by the launch's route and a rehearsal go. The registered order starts wave 1's first four controls at once, and
no target can start before the controls job has completed with gate 1 passed. Once the four jobs have run for SETTLE
seconds, the orchestrator is ended by SIGTERM, as an interrupted launch ends. Nothing here touches the bench's folder;
the copy is deleted at the end, after its run log, its consoles and the processes have been read."""
import json, os, shutil, signal, subprocess, sys, tempfile, time
B = os.environ['M819_BENCH'] + '/soft-slot-dynamics-m8-19'
INSTR = os.path.realpath(os.path.join(B, '..', 'soft-slot-dynamics-m8-15x'))
GO = 'https://github.com/openwave-labs/openwave/pull/0#rehearsal'
CODE = ['m819_branch.py', 'm819_gates.py', 'm819_run.py', 'm8_19_task_details.md', 'record_environment.py', 'write_guard.py']
SETTLE = 30
fails = []


def check(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


def copy(base):
    t = tempfile.mkdtemp(dir=base)
    os.symlink(INSTR, os.path.join(t, 'soft-slot-dynamics-m8-15x'))
    r = os.path.join(t, 'soft-slot-dynamics-m8-19')
    os.makedirs(os.path.join(r, 'run'))
    for f in CODE:
        shutil.copy2(os.path.join(B, 'run', f), os.path.join(r, 'run', f))
    shutil.copytree(os.path.join(B, 'reference'), os.path.join(r, 'reference'))
    return r


def py(r, *args):
    return subprocess.run([sys.executable, '-I', '-B'] + list(args), cwd=r, capture_output=True, text=True)


def ps(*args):
    return subprocess.run(['ps'] + list(args), capture_output=True, text=True).stdout


def events(path):
    try:
        with open(path) as f:
            return json.load(f)['events']
    except (FileNotFoundError, json.JSONDecodeError):
        return []


bench_run = sorted(os.listdir(os.path.join(B, 'run')))
check("the bench's run/ before: no out/", not os.path.exists(os.path.join(B, 'run', 'out')), bench_run)
base = tempfile.mkdtemp(prefix='m819_launch_')
r = copy(base)
# the environment recorded by the launch's route, then the freeze written with the rehearsal go
p = py(r, '-c', 'import subprocess, sys; sys.path.insert(0, "run"); import m819_branch; '
                'sys.exit(subprocess.run([sys.executable, "-I", "-B", "run/record_environment.py"]).returncode)')
assert p.returncode == 0, p.stderr[-300:]
assert py(r, 'run/write_guard.py', GO).returncode == 0
Fr = json.load(open(os.path.join(r, 'run', 'FROZEN.json')))
Fb = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))
diff = sorted(k for k in set(Fr['pins']) | set(Fb['pins']) if Fr['pins'].get(k) != Fb['pins'].get(k))
check("the rehearsal freeze's pins against the bench's: the environment record alone", diff == ['run/ENVIRONMENT.json'], diff)

# the launch, as registered
con_p = os.path.join(base, 'orchestrator.console')
con = open(con_p, 'w')
orch = subprocess.Popen([sys.executable, '-I', '-B', '-u', 'run/m819_run.py'], cwd=r, stdout=con, stderr=subprocess.STDOUT)
log_p = os.path.join(r, 'run', 'out', 'RUNLOG.json')
t0 = time.time()
while sum(e['event'] == 'process' for e in events(log_p)) < 4 and orch.poll() is None and time.time() - t0 < 300:
    time.sleep(0.5)
ev = events(log_p)
procs = [(e['job'], e['pid']) for e in ev if e['event'] == 'process']
check('the orchestrator passed both checks and launched', orch.poll() is None and any(e['event'] == 'launch' for e in ev),
      f'exit {orch.poll()}')
check("four jobs started, wave 1's first four controls", [j for j, _ in procs] == ['dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3'], procs)
time.sleep(SETTLE)
ev = events(log_p)
check(f'after {SETTLE} s: no job ended, completed or refused, and no stop',
      not [e for e in ev if e['event'] in ('ended', 'completed', 'stop', 'not run', 'job ended')], [e['event'] for e in ev])
for j, pid in procs:
    line = ps('-o', 'pid=,stat=,time=,etime=,command=', '-p', str(pid)).strip()
    staged = sorted(os.listdir(os.path.join(r, 'run', 'out', '.staging', f'{j}.1')))
    check(f'{j}: its process alive and computing, its staging folder holding its console alone',
          'm819_branch.py' in line and staged == ['console.log'], f'{line.split(" -I ")[0]} ... {j}; staged {staged}')

# ended as an interrupted launch ends
orch.send_signal(signal.SIGTERM)
code = orch.wait(timeout=120)
con.close()
time.sleep(2)
print('\n== the orchestrator, ended by SIGTERM: exit', code, flush=True)
print(open(con_p).read().rstrip(), flush=True)
L = json.load(open(log_p))
print('\n== the run log, in full', flush=True)
print(json.dumps(L, indent=1), flush=True)
print('\n== out/ after the launch', flush=True)
listing = sorted(os.path.relpath(os.path.join(dp, f), os.path.join(r, 'run', 'out')) for dp, dn, fn in
                 os.walk(os.path.join(r, 'run', 'out')) for f in fn)
for f in listing:
    print(f'{os.path.getsize(os.path.join(r, "run", "out", f)):>8}  {f}', flush=True)
print(flush=True)
ended = [e for e in L['events'] if e['event'] == 'ended']
check('exit 1, from the signal handler', code == 1)
check('each start ended by the signal, the launch ended with it, no stop and nothing completed',
      [(e['job'], e['start'], e['code']) for e in ended] == [(j, 1, -15) for j, _ in procs]
      and all(e['cause'] == 'the orchestrator was ended by signal 15' for e in ended)
      and L['events'][-1] == dict(t=L['events'][-1]['t'], event='launch ended', signal=15)
      and L['stop'] is None and L['completed'] == {} and L['ended'] == {} and L['not_run'] == {})
check("the run log holds the registered order and the rehearsal freeze's pin, not a bench run",
      [j['id'] for j in L['jobs']][:9] == ['dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'rate', 'p5a', 'c3e3', 'c2a_dur', 'controls']
      and L['bench'] is False and L['pin'] == open(os.path.join(r, 'run', 'FROZEN_PIN')).read().strip())
check('the four staging folders moved to out/interrupted/, nothing else written',
      listing == ['RUNLOG.json'] + [f'interrupted/{j}.1/console.log' for j, _ in sorted(procs)], listing)
left = [l for l in ps('-A', '-o', 'pid=,command=').splitlines()
        if base in l or os.path.realpath(base) in l or f'caffeinate -i -s -w {orch.pid}' in l]
check('no process left: no job, no caffeinate', not left, left)
check("the bench's run/ after: unchanged, no out/", sorted(os.listdir(os.path.join(B, 'run'))) == bench_run
      and not os.path.exists(os.path.join(B, 'run', 'out')))
check('no cache written in the instrument', not [dp for dp, dn, fn in os.walk(INSTR) if os.path.basename(dp) == '__pycache__'])
shutil.rmtree(base)
print('rehearse_launch:', 'PASS' if not fails else f'FAIL ({len(fails)}): {fails}', flush=True)
sys.exit(1 if fails else 0)
