#!/usr/bin/env python3
"""What every job does before its first solve, for every entry the solves will start: the admission, and the seed's orbit
checks, at N = 24 and 40. No continuation runs and no record is made.

Usage: entries_check.py
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import devtools  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402


def main():
    bad, seen = 0, 0
    for tag in list(grid.FRESH) + list(grid.ROWS):
        name, eps, case = grid.entry(tag)
        devtools.require(case['admission'])
        for N in (24, 40):
            t0 = time.time()
            cu = jobs.Cut(name, case, N)
            seen += 1
            bad += not cu.seed_ok
            print(f"{tag:14s} N = {N}: admission {case['admission']}, seed ok {cu.seed_ok}, k, r = {cu.chk['k']}, {cu.chk['r']}, "
                  f"crit {cu.chk['crit']:.1e}, {len(eps)} points from {eps[0]:g} to {eps[-1]:g}, {time.time() - t0:.0f} s", flush=True)
    print(f'{seen} starts, {bad} refused; no solve ran; manifest {devtools.manifest(ROOT)[1]}')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
