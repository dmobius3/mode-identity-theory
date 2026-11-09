"""M8.19's orchestrator (the terms: THE FREEZE, THE GUARD AND THE RUN; DESIGN.md, The run), frozen with the driver.

  python3 -I -B -u m819_run.py                        the registered run into run/out/, refused unless FROZEN.json validates
  python3 -I -B -u m819_run.py --bench PLAN OUTDIR    a bench plan (BENCH), controls only, into OUTDIR

At most four jobs at once, each a single-thread process of m819_branch.py, a job starting as another ends, in the plan's
order; a job starts only when every job it needs has completed (and, past gate 1, gate 1 has passed), and a job that
waits on others starts only when they have all completed or ended. RUNLOG.json is written by this process alone,
atomically, after every event: the pin, each launch, each job's start before its process starts, its process, each end,
each completion with its files' SHA-256, and any stop. A launch starts each job at most once, so a job's starts, counted
from the log across launches, are the launches that started it (the terms: a job that three launches start and leave
unfinished; DESIGN.md, reading 4). A start that ends without completing leaves the job pending for the next launch, its
staging folder moved to out/interrupted/ and read by nothing, and the launch ends when nothing more can start; after a
third, the job ends its part of the run and what needs it does not run, with the cause recorded. A relaunch is the
whole run, never a chosen job. A refusal stops the run. A relaunch refuses a stopped run, another pin, a completed job
whose file differs, and any process the log started that is still alive; caffeinate holds the machine awake while this
process lives. A registered launch also reads the environment again (run/record_environment.py, M8.18's, byte for
byte) and refuses any difference from run/ENVIRONMENT.json, written at the freeze."""
import datetime
import hashlib
import json
import os
import signal
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DRIVER = os.path.join(HERE, 'm819_branch.py')
CODE = ['m819_branch.py', 'm819_gates.py', 'm819_run.py']
SLOTS = 4                       # the machine's four performance cores, one thread each (the terms: Ownership and run format)
STARTS = 3                      # a job three launches start and leave unfinished ends its part of the run
WAVE1 = ['dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'rate', 'p5a', 'c3e3', 'c2a_dur']
ROWS = ['gates_T1_R4', 'gates_T1_R5', 'gates_T4_R4', 'gates_T4_R5', 'coherent_R5']
LONG_T = 2750.0


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def job(id, wave, args=(), needs=(), after=(), gate1=False, long=False):
    """A job: what it needs completed, what it waits on to complete or end, and whether it needs gate 1 passed (gate1)
    or the longest control Persisting, valid (long)."""
    return dict(id=id, wave=wave, args=list(args), needs=list(needs), after=list(after), gate1=gate1, long=long)


def registered():
    jobs = [job(j, 1) for j in WAVE1] + [job('controls', 1, after=WAVE1)]
    jobs += [job(j, 2, needs=['controls'], gate1=True) for j in ROWS]
    jobs += [job('plan', 2, needs=['controls'], after=ROWS, gate1=True)]
    jobs += [job('record', 5, after=[j['id'] for j in jobs])]
    return jobs


BENCH = {
    # the smoke test: four of M8.15's recorded controls at once at T = 20, then C2a/R4's duration control at T = 20
    # (inside its recorded T = 1000) as a fifth job that starts as one ends; gate 1 read on them, for nothing
    'smoke': lambda: [job(j, 1, ['--T', '20']) for j in ('dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3')]
    + [job('c2a_dur', 1, ['--T', '20']), job('controls', 1, after=['dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'c2a_dur'])],
    # M8.15's dynamics gate whole, at its recorded T = 1000, with control 1a; the fresh controls read without evolving
    'controls': lambda: [job(j, 1) for j in ('dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'rate', 'p5a')]
    + [job('c3e3', 1, ['--no-evolve']), job('c2a_dur', 1, ['--no-evolve']),
       job('controls', 1, after=WAVE1)],
    # the stand-in: C2a/R4 through the target path on its test stretch, the plan, and the test it sets
    'standin': lambda: [job('gates_C2a_R4', 2, ['--standin']), job('plan', 2, ['--standin'], needs=['gates_C2a_R4'])],
    # the dry run in one queue: the stand-in first, so its test can follow, then 'controls'
    'dryrun': lambda: BENCH['standin']() + BENCH['controls'](),
}


class Run:
    def __init__(self, out, jobs, bench, pin, driver=DRIVER):
        self.out, self.jobs, self.bench, self.pin, self.driver = out, {j['id']: j for j in jobs}, bench, pin, driver
        self.order = [j['id'] for j in jobs]
        self.running = {}            # pid -> (job id, start number, staging folder, its Popen, held so that only
                                     # this process reaps it: subprocess's own cleanup reaps a dropped Popen's child)
        self.path = os.path.join(out, 'RUNLOG.json')
        self.stopped = None
        self.started = set()         # the jobs this launch has started: a launch starts each job at most once

    # --- the log ---------------------------------------------------------------------------------------------------
    def write(self):
        tmp = self.path + '.tmp'
        with open(tmp, 'w') as f:
            json.dump(self.log, f, indent=1)
        os.replace(tmp, self.path)

    def event(self, **kw):
        self.log['events'].append(dict(t=now(), **kw))
        self.write()

    def starts(self, j):
        return sum(1 for e in self.log['events'] if e['event'] == 'started' and e['job'] == j)

    def state(self, j):
        if j in self.log['completed']:
            return 'completed'
        if j in self.log['ended']:
            return 'ended'
        if j in self.log['not_run']:
            return 'not_run'
        if any(v[0] == j for v in self.running.values()):
            return 'running'
        return 'pending'

    # --- a launch ----------------------------------------------------------------------------------------------------
    def open(self):
        os.makedirs(os.path.join(self.out, '.staging'), exist_ok=True)
        if os.path.exists(self.path):
            with open(self.path) as f:
                self.log = json.load(f)
            if self.log.get('stop'):
                raise SystemExit(f'REFUSED: the run stopped ({self.log["stop"]})')
            if self.log['pin'] != self.pin:
                raise SystemExit('REFUSED: the log belongs to another pin')
            for j, rec in self.log['completed'].items():
                for f, h in rec['files'].items():
                    if sha(os.path.join(self.out, j, f)) != h:
                        raise SystemExit(f'REFUSED: the completed job {j}: {f} differs from its logged SHA-256')
            # starts the last launch left open: refuse while any process is alive, else end them
            open_starts = self.open_starts()
            for (j, n, pid) in open_starts:
                if pid and alive(pid):
                    raise SystemExit(f'REFUSED: {j} (start {n}, pid {pid}) is still running')
            for (j, n, pid) in open_starts:
                self.ended_start(j, n, 'the launch that started it ended before it')
            self.log['jobs'] = self.order_record()
            self.log['launches'].append(now())
            self.write()
        else:
            self.log = dict(pin=self.pin, bench=self.bench, launches=[now()], jobs=self.order_record(), events=[],
                            completed={}, ended={}, not_run={}, stop=None)
            self.write()
        for d in os.listdir(os.path.join(self.out, '.staging')):
            self.aside(os.path.join(self.out, '.staging', d))
        self.event(event='launch', number=len(self.log['launches']))

    def order_record(self):
        return [dict(self.jobs[j]) for j in self.order]

    def open_starts(self):
        """(job, start, pid) for every start the log holds with no end and no completion after it."""
        out = []
        for e in self.log['events']:
            if e['event'] == 'started':
                out.append([e['job'], e['start'], None])
            elif e['event'] == 'process':
                for s in out:
                    if s[0] == e['job'] and s[1] == e['start']:
                        s[2] = e['pid']
            elif e['event'] in ('ended', 'completed'):
                out = [s for s in out if not (s[0] == e['job'] and s[1] == e['start'])]
        return [tuple(s) for s in out]

    def aside(self, folder):
        dest = os.path.join(self.out, 'interrupted')
        os.makedirs(dest, exist_ok=True)
        base = os.path.basename(folder)
        k = 0
        while os.path.exists(os.path.join(dest, base + (f'.{k}' if k else ''))):
            k += 1
        os.rename(folder, os.path.join(dest, base + (f'.{k}' if k else '')))

    # --- the queue ---------------------------------------------------------------------------------------------------
    def gate1_passed(self):
        if 'controls' not in self.log['completed']:
            return False
        with open(os.path.join(self.out, 'controls', 'CONTROLS.json')) as f:
            return bool(json.load(f)['all_passed'])

    def long_passed(self):
        if 'c2a_long' not in self.log['completed']:
            return False
        with open(os.path.join(self.out, 'c2a_long', 'c2a.json')) as f:
            return bool(json.load(f)['control']['passed'])

    def ready(self, j):
        spec = self.jobs[j]
        for d in spec['needs']:
            if self.state(d) != 'completed':
                return False
        for d in spec['after']:
            if self.state(d) not in ('completed', 'ended', 'not_run'):
                return False
        return not ((spec['gate1'] and not self.gate1_passed()) or (spec.get('long') and not self.long_passed()))

    def blocked(self, j):
        """Why a pending job can never start, or None."""
        spec = self.jobs[j]
        for d in spec['needs']:
            if self.state(d) in ('ended', 'not_run'):
                return f'{d} did not complete'
        if spec['gate1'] and 'controls' in self.log['completed'] and not self.gate1_passed():
            return 'gate 1 did not pass'
        if spec.get('long') and 'c2a_long' in self.log['completed'] and not self.long_passed():
            return 'the longest control did not Persist, valid'
        return None

    def extend(self):
        """After the plan: C2a/R4's longest control if a test needs more than 2750, and each stretch's test."""
        if 'plan' not in self.log['completed'] or any(j.startswith('test_') for j in self.jobs):
            return
        with open(os.path.join(self.out, 'plan', 'PLAN.json')) as f:
            plan = json.load(f)
        new = []
        if plan['long_control']:
            new.append(job('c2a_long', 3, ['--long-T', repr(plan['T_max'])], needs=['plan']))
        for sid, t in plan['tests'].items():
            new.append(job(f'test_{sid}', 4, needs=['plan'] + (['c2a_long'] if t['T'] > LONG_T else []),
                           long=t['T'] > LONG_T))
        at = self.order.index('plan') + 1          # the plan's jobs come next in the queue
        for j in new:
            self.jobs[j['id']] = j
        self.order[at:at] = [j['id'] for j in new]
        if 'record' in self.jobs:
            self.jobs['record']['after'] += [j['id'] for j in new]
        self.log['jobs'] = self.order_record()
        self.event(event='plan read', added=[j['id'] for j in new])

    def start(self, j):
        n = self.starts(j) + 1
        self.started.add(j)
        staging = os.path.join(self.out, '.staging', f'{j}.{n}')
        self.event(event='started', job=j, start=n)
        os.makedirs(staging)
        cmd = [sys.executable, '-I', '-B', '-u', self.driver, j, '--out', staging, '--root', self.out] + self.jobs[j]['args']
        if self.bench:
            cmd.append('--bench')
        with open(os.path.join(staging, 'console.log'), 'w') as log:
            p = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, start_new_session=True, cwd=ROOT)
        self.running[p.pid] = (j, n, staging, p)
        self.event(event='process', job=j, start=n, pid=p.pid)
        print(f'{now()} started {j} (start {n}, pid {p.pid})', flush=True)

    def finish(self, pid, code):
        j, n, staging, _ = self.running.pop(pid)
        if code == 0 and os.path.exists(os.path.join(staging, 'job.json')):
            dest = os.path.join(self.out, j)
            if os.path.exists(dest):
                self.stop(f'{j}: a folder of that name is already in the run')
                self.aside(staging)
                return
            os.rename(staging, dest)
            files = {}
            for dp, dn, fn in os.walk(dest):
                for f in sorted(fn):
                    rel = os.path.relpath(os.path.join(dp, f), dest)
                    files[rel] = sha(os.path.join(dp, f))
            self.log['completed'][j] = dict(files=files, t=now(), start=n)
            self.event(event='completed', job=j, start=n)
            print(f'{now()} completed {j}', flush=True)
            return
        cause = cause_of(staging, code)
        self.event(event='ended', job=j, start=n, code=code, cause=cause)
        self.aside(staging)
        print(f'{now()} {j} start {n} ended unfinished: {cause}', flush=True)
        if code == 3:
            self.stop(f'{j} refused: {cause}')
        elif n >= STARTS:
            self.log['ended'][j] = dict(t=now(), starts=n, cause=cause)
            self.event(event='job ended', job=j, starts=n)

    def ended_start(self, j, n, cause):
        self.event(event='ended', job=j, start=n, code=None, cause=cause)
        if n >= STARTS:
            self.log['ended'][j] = dict(t=now(), starts=n, cause=cause)
            self.event(event='job ended', job=j, starts=n)

    def stop(self, why):
        self.stopped = why
        self.log['stop'] = dict(t=now(), why=why)
        self.event(event='stop', why=why)

    def loop(self):
        while True:
            self.extend()
            if not self.stopped:
                for j in self.order:
                    if self.state(j) == 'pending':
                        why = self.blocked(j)
                        if why:
                            self.log['not_run'][j] = dict(t=now(), why=why)
                            self.event(event='not run', job=j, why=why)
                for j in self.order:
                    if len(self.running) >= SLOTS:
                        break
                    if self.state(j) == 'pending' and j not in self.started and self.starts(j) < STARTS and self.ready(j):
                        self.start(j)
            if not self.running:
                break
            done = None
            while done is None:
                done = next(((pid, p.poll()) for pid, (_, _, _, p) in self.running.items() if p.poll() is not None), None)
                if done is None:
                    time.sleep(1)
            self.finish(*done)
        pending = [j for j in self.order if self.state(j) == 'pending']
        self.event(event='launch ended', pending=pending, stopped=self.stopped)
        print(f'{now()} launch ended; pending {pending}; stop {self.stopped}', flush=True)

    def terminate(self, signum, frame):
        for pid, (j, n, staging, p) in list(self.running.items()):
            try:
                os.killpg(pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
        for pid in list(self.running):
            j, n, staging, p = self.running.pop(pid)
            self.event(event='ended', job=j, start=n, code=p.wait(),
                       cause=f'the orchestrator was ended by signal {signum}')
            self.aside(staging)
            if n >= STARTS:
                self.log['ended'][j] = dict(t=now(), starts=n, cause=f'the orchestrator was ended by signal {signum}')
                self.event(event='job ended', job=j, starts=n)
        self.event(event='launch ended', signal=signum)
        sys.exit(1)


def cause_of(staging, code):
    for name, key in (('crash.json', None), ('refused.json', 'refused')):
        p = os.path.join(staging, name)
        if os.path.exists(p):
            with open(p) as f:
                d = json.load(f)
            return d['refused'] if key else f'{d["exception"]} at stage {d["stage"]}: {d["message"]}'
    if code is not None and code < 0:
        return f'ended by signal {-code}'
    return f'exit status {code} with no record'


def alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    r = subprocess.run(['ps', '-p', str(pid), '-o', 'command='], capture_output=True, text=True)
    return 'm819_branch.py' in r.stdout


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--bench':
        plan, out = sys.argv[2], os.path.abspath(sys.argv[3])
        jobs = BENCH[plan]()
        pin = 'bench ' + plan + ' ' + ' '.join(sha(os.path.join(HERE, c)) for c in CODE)
        bench = True
    else:
        sys.path.insert(0, HERE)
        import m819_branch as D
        try:
            D.validate_frozen()
        except D.Refused as e:
            raise SystemExit(f'REFUSED: {e}')
        env = subprocess.run([sys.executable, '-I', '-B', os.path.join(HERE, 'record_environment.py'), '--check'],
                             capture_output=True, text=True)
        print(env.stdout, end='', flush=True)
        if env.returncode != 0:
            raise SystemExit('REFUSED: the environment differs from run/ENVIRONMENT.json (record_environment.py --check)')
        out, jobs, bench = os.path.join(HERE, 'out'), registered(), False
        pin = sha(os.path.join(HERE, 'FROZEN.json'))
    launch(out, jobs, bench, pin)


def launch(out, jobs, bench, pin, driver=DRIVER):
    """One launch of a run: the log opened or resumed, caffeinate held for this process's life, then the queue. The
    driver is m819_branch.py; the launch tests pass a stub of it, never the registered run."""
    os.makedirs(out, exist_ok=True)
    run = Run(out, jobs, bench, pin, driver)
    run.open()
    subprocess.Popen(['caffeinate', '-i', '-s', '-w', str(os.getpid())])
    signal.signal(signal.SIGTERM, run.terminate)
    signal.signal(signal.SIGINT, run.terminate)
    run.loop()


if __name__ == '__main__':
    main()
