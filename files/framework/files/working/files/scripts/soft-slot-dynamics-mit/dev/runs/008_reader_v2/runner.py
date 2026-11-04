#!/usr/bin/env python3
"""Runs jobs.py's jobs side by side, longest first, each in its own process (DESIGN.md).

Usage: runner.py OUT KIND [--jobs K] [--threads T] [--tags A,B] [--cutoffs N1,N2] [--source DIR] [--note COMMIT --repo R]
  KIND: solves     every path of the computation (grid.solves), or the tags and cutoffs named
        controls   M8.18's control paths, for the runner's first test
        rereads    M8.18's control solutions read again, from --source
        reads, identities, readings, fresh   after the dated note: each refuses without --note and --repo. With no
                   --tags the first three take the fresh controls, and the rows once `fresh` has recorded their pass
  --jobs K      how many at once, 4 unless given
  --threads T   VECLIB_MAXIMUM_THREADS for each job; 0, the default, leaves it unset, as M8.18's run did. At 1 a solve
                is unchanged and as fast, but one record field at N = 24 moves in its round-off (dev/runs/005_leak)

A job is done when its record in OUT/jobs/ exists; a done job is not started. A job that exits otherwise is logged, and the
others go on; the next launch starts it again, resuming at its next point, up to ATTEMPTS starts. OUT/RUNLOG.json holds
the manifest at the start, each start and end, each job's seconds and its peak resident size, read from the kernel at
the job's exit. A launch refuses while another's jobs on the same OUT are alive, so two launches cannot write one
checkpoint. A file OUT/STOP lets the jobs under way finish and starts no more.
"""
import datetime
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import fresh  # noqa: E402
import grid  # noqa: E402

JOBS = os.path.join(HERE, 'jobs.py')
ATTEMPTS = 3
THREAD_VARS = ('VECLIB_MAXIMUM_THREADS',)


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def say(s):
    print(s, flush=True)


def option(argv, flag, default=None):
    return argv[argv.index(flag) + 1] if flag in argv else default


def read_tags(tags, out):
    """What a read may touch: the tags named, or the fresh controls, with the rows once those have passed (DESIGN.md,
    section 5). Rows named before the pass refuse here, and in jobs.py."""
    why = fresh.refusal(out)
    if tags is None:
        if why:
            say(f'the rows wait: {why}')
        return list(grid.FRESH) + ([] if why else list(grid.ROWS))
    if why and set(tags) & set(grid.ROWS):
        raise SystemExit(f'refused: no row is read before the fresh controls pass: {why}')
    return tags


def plan(kind, argv, out):
    """[(job name, jobs.py arguments, rough hours)], longest first."""
    tags = option(argv, '--tags')
    tags = tags.split(',') if tags else None
    if kind in ('reads', 'identities', 'readings'):
        tags = read_tags(tags, out)
    cuts = option(argv, '--cutoffs')
    cuts = [int(x) for x in cuts.split(',')] if cuts else list(grid.LADDER)
    src = option(argv, '--source')
    if kind == 'controls':
        base = [(t, N) for t in (tags or grid.CONTROLS) for N in cuts]
        jobs = [(f'path_{t}_N{N}', ['path', t, str(N)], grid.hours(t, N)) for t, N in base]
    elif kind == 'rereads':
        base = [(t, N) for t in (tags or grid.CONTROLS) for N in cuts]
        jobs = [(f'reread_{t}_N{N}', ['reread', t, str(N), src], grid.hours(t, N) / 5) for t, N in base]
    elif kind == 'solves':
        base = [(t, N) for t, N in grid.solves() if (tags is None or t in tags) and N in cuts]
        jobs = [(f'path_{t}_N{N}', ['path', t, str(N)], grid.hours(t, N)) for t, N in base]
    elif kind == 'reads':
        base = [(t, N) for t, N in grid.solves() if t in tags and N in cuts]
        jobs = [(f'read_{t}_N{N}', ['read', t, str(N)], grid.hours(t, N) / 5) for t, N in base]
    elif kind == 'identities':
        pairs = list(zip(grid.LADDER, grid.LADDER[1:]))
        jobs = [(f'identity_{t}_{a}_{b}', ['identity', t, str(a), str(b)], 0.1) for t in tags for a, b in pairs]
    elif kind == 'readings':
        jobs = [(f'reading_{t}', ['reading', t], 0.01) for t in tags]
    elif kind == 'fresh':
        jobs = [('fresh', ['fresh'], 0.01)]
    else:
        raise SystemExit(__doc__)
    return sorted(jobs, key=lambda j: -j[2])


def alive(out):
    """The pids of jobs.py processes already working on OUT."""
    ps = subprocess.run(['/bin/ps', '-axo', 'pid=,command='], capture_output=True, text=True).stdout
    return [int(line.split()[0]) for line in ps.splitlines() if 'jobs.py' in line and f' {out} ' in line]


def load(path, default):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return default


def main():
    argv = sys.argv[1:]
    if len(argv) < 2:
        raise SystemExit(__doc__)
    out, kind = os.path.abspath(argv[0]), argv[1]
    K = int(option(argv, '--jobs', '4'))
    threads = int(option(argv, '--threads', '0'))
    note, repo = option(argv, '--note'), option(argv, '--repo')
    tail = ['--note', note, '--repo', repo] if note else []
    if kind in ('reads', 'identities', 'readings', 'fresh') and not (note and repo):
        raise SystemExit('refused: reads need --note and --repo')
    if alive(out):
        raise SystemExit(f'refused: jobs are alive on {out}: {alive(out)}')
    for d in (out, os.path.join(out, 'jobs'), os.path.join(out, 'logs')):
        os.makedirs(d, exist_ok=True)
    logpath = os.path.join(out, 'RUNLOG.json')
    log = load(logpath, dict(events=[], jobs={}))
    log['events'].append(dict(t=now(), event=f'launch: {kind}, {K} at once, threads {threads}',
                              manifest=devtools.manifest()[1]))

    def save():
        with open(logpath + '.tmp', 'w', encoding='utf-8') as f:
            json.dump(log, f, indent=1)
        os.replace(logpath + '.tmp', logpath)
    save()
    env = dict(os.environ)
    for v in THREAD_VARS:
        env.pop(v, None)
        if threads:
            env[v] = str(threads)
    todo, running, failed = [], {}, []
    for name, args, hours in plan(kind, argv, out):
        rec = log['jobs'].setdefault(name, dict(starts=0))
        if os.path.exists(os.path.join(out, 'jobs', name + '.json')):
            continue
        if rec['starts'] >= ATTEMPTS:
            failed.append(name)
            say(f'{name}: started {ATTEMPTS} times and not completed; not started again')
            continue
        todo.append((name, args))
    say(f'{len(todo)} jobs to run, {K} at once; output in {out}')
    while todo or running:
        while todo and len(running) < K and not os.path.exists(os.path.join(out, 'STOP')):
            name, args = todo.pop(0)
            lf = open(os.path.join(out, 'logs', name + '.log'), 'ab')
            p = subprocess.Popen([sys.executable, '-I', '-B', '-u', JOBS, out, *args, *tail], stdout=lf,
                                 stderr=subprocess.STDOUT, env=env, cwd=ROOT)
            running[p.pid] = (name, p, lf, time.time())
            log['jobs'][name]['starts'] += 1
            log['events'].append(dict(t=now(), event=f'{name} started', pid=p.pid))
            save()
            say(f'{now()} {name} started')
        if os.path.exists(os.path.join(out, 'STOP')):
            todo = []
        if not running:
            break
        pid, status, ru = os.wait4(-1, 0)
        if pid not in running:
            continue
        name, p, lf, t0 = running.pop(pid)
        p.returncode = os.waitstatus_to_exitcode(status)
        lf.close()
        ok = p.returncode == 0 and os.path.exists(os.path.join(out, 'jobs', name + '.json'))
        log['jobs'][name].update(exit=p.returncode, seconds=time.time() - t0, peak_rss_bytes=ru.ru_maxrss,
                                 cpu_seconds=ru.ru_utime + ru.ru_stime, ok=ok)
        log['events'].append(dict(t=now(), event=f"{name} {'completed' if ok else 'failed'}", exit=p.returncode))
        save()
        say(f"{now()} {name} {'completed' if ok else f'FAILED, exit {p.returncode}'}: {time.time() - t0:.0f} s wall, "
            f'{ru.ru_utime + ru.ru_stime:.0f} s cpu, {ru.ru_maxrss / 2 ** 30:.2f} GB peak')
        if not ok:
            failed.append(name)
    log['events'].append(dict(t=now(), event=f"launch ended; {len(failed)} failed: {failed}"))
    save()
    say(f'done; {len(failed)} failed: {failed}')
    raise SystemExit(1 if failed else 0)


if __name__ == '__main__':
    main()
