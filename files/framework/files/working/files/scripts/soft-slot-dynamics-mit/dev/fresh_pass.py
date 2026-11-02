#!/usr/bin/env python3
"""The fresh controls against their pass marks (run/grid.py, PASS_MARKS; DESIGN.md, section 5): each point's as-built and
changed verdicts as stated first, what the as-built Unresolved rests on, K1 and the case's indices at all three cutoffs,
the case's type under the changed reading, and branch identity on both pairs. No row is read until this passes, or a miss
is diagnosed and disclosed.

An Unresolved mark names its cause, tested from the records, so that an Unresolved for any other reason misses it:
  link   every reason names a set that is two groups at N = 24 and 32 and one group of two members at N = 40
  flag   the one reason is the structure line, and D's flag is the only unresolved item, at N = 40 alone, with B clearing it

Usage: fresh_pass.py OUT                    the marks in run/grid.py, on OUT's reading files
       fresh_pass.py --test OUT             the same code on M8.18's controls, read again in dev/runs: their marks are on
                                            record, and each wrong mark, its verdict or its cause, must be reported as a miss
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import checks as ck  # noqa: E402
import grid  # noqa: E402

KNOWN = {('ctl_P5', 0.25): ('Unresolved', 'converged', 'link'), ('ctl_P5', 0.5): ('converged', 'converged', None),
         ('ctl_C3R_R4', 0.25): ('Unresolved', 'converged', 'flag'), ('ctl_C3R_R4', 0.5): ('converged', 'converged', None),
         ('ctl_C2b', 0.25): ('converged', 'converged', None), ('ctl_C2a_R5', 0.25): ('converged', 'converged', None)}
WRONG = (('ctl_P5', 0.25, ('converged', 'converged', None)), ('ctl_P5', 0.25, ('Unresolved', 'converged', 'flag')),
         ('ctl_C3R_R4', 0.25, ('Unresolved', 'converged', 'link')))
SET = re.compile(r'set at (\S+)j ')
STRUCTURE = 'structure: a record is unresolved'


def linked_alone(d, k, reason):
    """Whether the set a reason names is two groups at N = 24 and 32 and one of two members at N = 40."""
    m = SET.search(reason)
    if not m:
        return False
    v = complex(m.group(1) + 'j').imag
    near = [[g['size'] for g in d['cutoffs'][str(N)]['points'][k]['summary']['groups'] if abs(g['c'][1] - v) < 5e-6 * abs(v)]
            for N in grid.LADDER]
    return near == [[1, 1], [1, 1], [2]]


def link(d, k, reasons):
    return bool(reasons) and all(linked_alone(d, k, r) for r in reasons)


def flag(d, k, reasons):
    pts = [d['cutoffs'][str(N)]['points'][k] for N in grid.LADDER]
    return (reasons == [STRUCTURE] and [p['record']['unresolved'] for p in pts] == [[], [], [changed.ND_LINE]]
            and pts[-1]['b_resolved'] is True)


CAUSES = dict(link=link, flag=flag)


def misses(out, tag, e, marks):
    """What keeps one point from its marks: an empty list is a pass."""
    with open(os.path.join(out, tag + '.json'), encoding='utf-8') as f:
        d = json.load(f)
    k, case, got = lib.key(e), d['case'], []
    built, chg = d['readings'].get(k), d['changed'].get(k)
    if not built or not chg:
        return ['no reading']
    if built['verdict'] != marks[0]:
        got.append(f"as built {built['verdict']}, marked {marks[0]}: {built['reasons'][:1]}")
    elif marks[2] and not CAUSES[marks[2]](d, k, built['reasons']):
        got.append(f"as built Unresolved, and not by the mark's {marks[2]}: {built['reasons'][:1]}")
    if chg['verdict'] != marks[1]:
        got.append(f"changed {chg['verdict']}, marked {marks[1]}: {chg['reasons'][:1]}")
    elif chg['type'] != case['type']:
        got.append(f"changed type {chg['type']}, the case's {case['type']}")
    for N in grid.LADDER:
        p = d['cutoffs'][str(N)]['points'].get(k)
        if not p or 'record' not in p:
            got.append(f'no record at N = {N}')
            continue
        r = p['record']
        if not ck.k1(p, case):
            got.append(f'K1 fails at N = {N}')
        if [r['nL'], r['nD'], r['K']] != case['idx']:
            got.append(f"indices {[r['nL'], r['nD'], r['K']]} at N = {N}, the case's {case['idx']}")
    for pair in zip(grid.LADDER, grid.LADDER[1:]):
        idn = d['identity'].get(k, {}).get(lib.pair_key(pair))
        if not idn or not idn['kept']:
            got.append(f'branch identity fails between N = {pair[0]} and {pair[1]}')
    return got


def main():
    test = '--test' in sys.argv
    out = sys.argv[-1]
    marks = KNOWN if test else grid.PASS_MARKS
    bad = 0
    for (tag, e), m in marks.items():
        got = misses(out, tag, e, m)
        bad += bool(got)
        print(f"{tag} {e:g}: {'pass' if not got else 'MISS: ' + '; '.join(got)}", flush=True)
    if test:
        for tag, e, m in WRONG:
            wrong = misses(out, tag, e, m)
            print(f"a wrong mark, {tag} {e:g} {m}, is reported: {wrong[:1]}")
            bad += not wrong
    print(f'{bad} missed')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
