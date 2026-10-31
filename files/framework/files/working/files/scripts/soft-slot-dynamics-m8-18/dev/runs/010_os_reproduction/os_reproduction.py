#!/usr/bin/env python3
"""A check of the machine, outside the terms' numbered tests and outside the run: does a solve on this macOS reproduce
the records? M8.16.1's and M8.17's records were made on macOS 15.8 (24H23), this machine is on 15.8.2 (24H232) since
2026-10-29, and NumPy and SciPy both link Accelerate, which ships with the OS. The reproduction gate compares every float
with ==, so a changed Accelerate could stop the run on the machine alone, and tests 4 and 8 cannot see it: test 4 has no
solve, and test 8 compares this machine with itself.

Usage: os_reproduction.py N [CASE ...]
       os_reproduction.py C1

It takes the GO-list controls only, unless cases are named, at a cutoff M8.16.1 holds, through the run's own code:
Run.path_job, Run.read_job and census_lib.gate_cutoff, the comparison Run.reproduce makes. C1 goes through run_c1 at
N = 16, 24 and 32, against its record, as Run.c1 compares it. Outputs go to a temporary folder. No solve at N = 40: it
refuses that cutoff, and a case off the GO list, before any solve. The lines are appended to dev/os_reproduction.out.
"""
import os
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
sys.path.insert(0, ROOT)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

GO_CONTROLS = ['C2b', 'C2a', 'C3', 'C2a/R5']
OUT = os.path.join(HERE, 'os_reproduction.out')


def say(s):
    print(s, flush=True)
    with open(OUT, 'a', encoding='utf-8') as f:
        f.write(s + '\n')


def leaves(o, ignore):
    """The compared leaves of a record."""
    if isinstance(o, dict):
        return sum(leaves(v, ignore) for k, v in o.items() if k not in ignore)
    if isinstance(o, list):
        return sum(leaves(v, ignore) for v in o)
    return 1


def gaps(a, b, ignore):
    """Every compared pair of floats, as a relative difference, and the count of pairs that differ otherwise."""
    if isinstance(a, dict) and isinstance(b, dict):
        rel, other = [], 0
        for k in set(a) | set(b):
            if k in ignore:
                continue
            if k not in a or k not in b:
                other += 1
                continue
            r, o = gaps(a[k], b[k], ignore)
            rel, other = rel + r, other + o
        return rel, other
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        rel, other = [], 0
        for x, y in zip(a, b):
            r, o = gaps(x, y, ignore)
            rel, other = rel + r, other + o
        return rel, other
    if isinstance(a, float) and isinstance(b, float):
        return ([abs(a - b) / max(abs(a), abs(b), 1e-300)] if a != b and a == a and b == b else []), 0
    return [], int(a != b)


def c1():
    """C1 through run_c1 at its cutoffs below N = 40, against its record."""
    case = census.roundtrip(cs.serialize('C1', dict(cs.CASES['C1'], cutoffs=[16, 24, 32])))
    devtools.require(case['admission'])
    theirs = lib.m8161_file('C1.json', ROOT)['cutoffs']
    t0 = time.perf_counter()
    mine = census.roundtrip(dr.run_c1(case)[0]['cutoffs'])
    held = {k: theirs[k] for k in mine}
    fails = lib.differences(mine, held, '/cutoffs')
    rel, other = gaps(mine, held, lib.TIMINGS)
    say(f"C1 (R3), N = 16, 24 and 32: {leaves(held, lib.TIMINGS)} leaves compared, {len(fails)} differ"
        + (f', {len(rel)} floats, the largest relative difference {max(rel, default=0):.2e}, {other} of another kind' if fails else '')
        + f'; {time.perf_counter() - t0:.0f} s')
    for d in fails[:3]:
        say('   ' + d[:160])
    return len(fails)


def main():
    if sys.argv[1] == 'C1':
        return c1()
    N = int(sys.argv[1])
    names = sys.argv[2:] or GO_CONTROLS
    if N == lib.TOP:
        raise SystemExit(f'no solve at N = {lib.TOP}')
    bad = [n for n in names if n not in devtools.GO]
    if bad:
        raise SystemExit(f'not on the GO list: {bad}')
    ignore = lib.TIMINGS | lib.NOT_COMPUTED
    say(f"N = {N}, on macOS {sys.platform and __import__('platform').mac_ver()[0]}")
    failed = 0
    for name in names:
        case = census.roundtrip(cs.serialize(name, dict(cs.CASES[name], cutoffs=[N])))
        eps = [p['eps'] for p in case['points']]
        theirs = lib.theirs(name, ROOT)['cutoffs'][str(N)]
        t0 = time.perf_counter()
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as tmp:
            run = census.Run(dict(cases={name: case}), tmp)
            run.log.setdefault('events', [])
            run.path_job(name, N)
            rec = run.read_job(name, N, eps, 'path')
        fails = lib.gate_cutoff(rec, theirs, eps)
        n = leaves(dict(seed=theirs.get('seed'), points={lib.key(e): theirs['points'][lib.key(e)] for e in eps}), ignore)
        rel, other = gaps(dict(seed=rec.get('seed'), points=rec['points']),
                          dict(seed=theirs.get('seed'), points=theirs['points']), ignore)
        say(f"{name} ({case['slot']}), N = {N}, {len(eps)} points: {n} leaves compared, {len(fails)} differ"
            + (f', {len(rel)} floats, the largest relative difference {max(rel, default=0):.2e}, {other} of another kind' if fails else '')
            + f'; {time.perf_counter() - t0:.0f} s')
        for d in fails[:3]:
            say('   ' + d[:160])
        failed += bool(fails)
    say(f'{failed} of {len(names)} differ')
    return failed


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
