#!/usr/bin/env python3
"""How one real path scales: K copies of the same path run side by side, each in its own temporary folder, for each K and
thread setting named. Throughput is K times the time of one alone, over the time of K. Nothing is kept but the times.

Usage: scaling.py TAG N THREADS:K [THREADS:K ...]     THREADS 0 leaves VECLIB_MAXIMUM_THREADS unset
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
JOBS = os.path.join(ROOT, 'run', 'jobs.py')


def one(tag, N, threads, K):
    env = dict(os.environ)
    env.pop('VECLIB_MAXIMUM_THREADS', None)
    if threads:
        env['VECLIB_MAXIMUM_THREADS'] = str(threads)
    tmp = tempfile.mkdtemp(prefix='mit_scale_')
    ps, t0, walls, cpu, peak = {}, time.time(), [], 0.0, 0
    for i in range(K):
        out = os.path.join(tmp, str(i))
        os.makedirs(out)
        p = subprocess.Popen([sys.executable, '-I', '-B', '-u', JOBS, out, 'path', tag, str(N)], stdout=subprocess.DEVNULL,
                             env=env, cwd=ROOT)
        ps[p.pid] = p
    while ps:
        pid, status, ru = os.wait4(-1, 0)
        p = ps.pop(pid, None)
        if p is None:
            continue
        if os.waitstatus_to_exitcode(status) != 0:
            raise SystemExit(f'a copy failed: {status}')
        walls.append(time.time() - t0)
        cpu += ru.ru_utime + ru.ru_stime
        peak = max(peak, ru.ru_maxrss)
    shutil.rmtree(tmp)
    return max(walls), sum(walls) / K, cpu / K, peak / 2 ** 30


def main():
    tag, N = sys.argv[1], int(sys.argv[2])
    base = None
    for spec in sys.argv[3:]:
        threads, K = (int(x) for x in spec.split(':'))
        wall, mean, cpu, peak = one(tag, N, threads, K)
        if K == 1 and threads == 1:
            base = wall
        rate = K * base / mean if base else float('nan')
        print(f'threads {threads or "unset"}, {K} side by side: mean job {mean:.0f} s, last {wall:.0f} s, cpu {cpu:.0f} s per job, '
              f'peak {peak:.2f} GB, throughput {rate:.2f} of one job alone at one thread', flush=True)


if __name__ == '__main__':
    main()
