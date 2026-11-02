#!/usr/bin/env python3
"""The runner's first test: paths run side by side against M8.18's stored paths, every solution vector with ==, and every
solve field but the timings, through census_lib.differences. M8.18's run had VECLIB_MAXIMUM_THREADS unset and one job at
a time, so an equal result says neither the threads nor the neighbours moved a float. The .npz files themselves differ:
numpy stamps the time into them.

Usage: compare_controls.py OUT M818_OUT
"""
import json
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import census_lib as lib  # noqa: E402
import driver as dr  # noqa: E402
import grid  # noqa: E402


def main():
    out, m818 = sys.argv[1:3]
    jobs = sorted(f[len('path_'):-len('.json')] for f in os.listdir(os.path.join(out, 'jobs')) if f.startswith('path_ctl_'))
    bad, leaves, arrays = 0, 0, 0
    for job in jobs:
        tag, N = job.rsplit('_N', 1)
        base = f'{dr.safe(grid.CONTROLS[tag])}_N{N}'
        with open(os.path.join(out, f'{job}.json'), encoding='utf-8') as f:
            mine = json.load(f)
        with open(os.path.join(m818, f'{base}.json'), encoding='utf-8') as f:
            theirs = json.load(f)
        d = lib.differences(mine, theirs, ignore=lib.TIMINGS)
        with np.load(os.path.join(out, f'{job}.npz'), allow_pickle=False) as a, np.load(os.path.join(m818, f'{base}.npz'),
                                                                                       allow_pickle=False) as b:
            names = sorted(a.files)
            if names != sorted(b.files):
                d.append(f'arrays differ in name: {names} against {sorted(b.files)}')
            for n in names:
                arrays += a[n].size
                if a[n].dtype != b[n].dtype or a[n].shape != b[n].shape or not np.array_equal(a[n], b[n]):
                    d.append(f'array {n} differs')
        leaves += sum(len(p) for p in mine['points'].values())
        bad += len(d)
        print(f"{job}: {len(mine['points'])} points, {len(d)} differences" + (f': {d[:3]}' if d else ''))
    print(f'{len(jobs)} paths; {leaves} solve fields and {arrays} array entries compared; {bad} differences')
    raise SystemExit(1 if bad or not jobs else 0)


if __name__ == '__main__':
    main()
