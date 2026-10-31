#!/usr/bin/env python3
"""Can os_reproduction.py fail? It found no difference, and that shows nothing unless the same comparison reports the
smallest difference a machine could make. Each arm moves one float of a record on file, in memory, by one unit in the
last place, and runs the script's own main or c1 against it. The arm holds only if the script reports exactly that leaf
and no other: an arm that went red for another reason would say so here.

The first pass moves nothing, at N = 16, and must report 0 differ, so that the arms below it start from a clean
comparison. It is also the script's N = 16 on its final bytes: dev/runs/006_os_reproduction_16/ ran before c1 was added.

Nothing is written but dev/os_reproduction_arm.out. dev/os_reproduction.out is not touched, and no solve is at N = 40.
"""
import copy
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import os_reproduction as o  # noqa: E402

OUT = os.path.join(HERE, 'os_reproduction_arm.out')
lib = o.lib
CUTOFF = '16'
fails = []


def out(s):
    print(s, flush=True)
    with open(OUT, 'a', encoding='utf-8') as f:
        f.write(s + '\n')


def first_float(rec, path=''):
    """The first finite compared float of a record, in sorted order, with the path differences() names it by."""
    if isinstance(rec, dict):
        for k in sorted(rec, key=str):
            if k in lib.TIMINGS | lib.NOT_COMPUTED:
                continue
            hit = first_float(rec[k], f'{path}/{k}')
            if hit:
                return hit
    elif isinstance(rec, list):
        for i, v in enumerate(rec):
            hit = first_float(v, f'{path}[{i}]')
            if hit:
                return hit
    elif isinstance(rec, float) and math.isfinite(rec):
        return path, rec
    return None


def moved(rec, path):
    """A copy of rec with the float at path moved by one unit in the last place."""
    rec = copy.deepcopy(rec)
    parts = [p for p in path.replace('[', '/[').split('/') if p]
    node = rec
    for p in parts[:-1]:
        node = node[int(p[1:-1])] if p.startswith('[') else node[p]
    p = parts[-1]
    i = int(p[1:-1]) if p.startswith('[') else p
    node[i] = math.nextafter(node[i], math.inf)
    return rec


def run(call, argv, patch, value):
    """Runs the script under one patched reader, and returns what it said and what it returned."""
    said, saved_say, saved, saved_argv = [], o.say, getattr(lib, patch), sys.argv
    o.say, sys.argv = said.append, argv
    setattr(lib, patch, value)
    try:
        return said, call()
    finally:
        o.say, sys.argv = saved_say, saved_argv
        setattr(lib, patch, saved)


def judge(label, said, returned, want):
    """One line differs, naming the moved leaf, and no other, and the script's status says so."""
    counts = [s for s in said if 'compared,' in s]
    details = [s for s in said if s.startswith('   ')]
    ok = len(counts) == 1 and ' 1 differ, 1 floats, ' in counts[0] and ', 0 of another kind' in counts[0] \
        and len(details) == 1 and want in details[0] and bool(returned)
    out(f"{label}: {'RED' if ok else 'NOT AS NAMED'}: {counts[0] if counts else said}")
    out(details[0] if details else '   no detail')
    if not ok:
        fails.append(label)


def clean():
    said, _ = [], None
    saved_say, saved_argv = o.say, sys.argv
    o.say, sys.argv = said.append, ['os_reproduction.py', CUTOFF]
    try:
        failed = o.main()
    finally:
        o.say, sys.argv = saved_say, saved_argv
    for s in said:
        out('moved nothing: ' + s)
    if failed or not all(' 0 differ' in s for s in said if 'compared,' in s):
        fails.append('moved nothing')


def arm_control(name):
    case = o.cs.CASES[name]
    epss = [o.census.roundtrip(o.cs.serialize(name, dict(case, cutoffs=[int(CUTOFF)])))['points'][0]['eps']]
    held = lib.theirs(name, o.ROOT)
    k = lib.key(epss[0])
    path, value = first_float(held['cutoffs'][CUTOFF]['points'][k])
    forged = moved(held, f'/cutoffs/{CUTOFF}/points/{k}{path}')
    real = lib.theirs
    said, returned = run(o.main, ['os_reproduction.py', CUTOFF, name], 'theirs',
                         lambda n, root=lib.ROOT: forged if n == name else real(n, root))
    judge(f"{name}, one float of its record moved one place, {path}", said, returned, f'/{path.lstrip("/")}: ')


def arm_c1():
    real = lib.m8161_file
    held = real('C1.json', o.ROOT)
    path, value = first_float(held['cutoffs'][CUTOFF])
    forged = moved(held, f'/cutoffs/{CUTOFF}{path}')
    said, returned = run(o.c1, ['os_reproduction.py', 'C1'], 'm8161_file',
                         lambda n, root=lib.ROOT: forged if n == 'C1.json' else real(n, root))
    judge(f'C1, one float of its record moved one place, {path}', said, returned, f'/cutoffs/{CUTOFF}{path}: ')


def main():
    clean()
    for name in o.GO_CONTROLS:
        arm_control(name)
    arm_c1()
    out(f'{len(fails)} failed')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
