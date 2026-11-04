"""The fresh controls against their pass marks (grid.PASS_MARKS; DESIGN.md, section 5), and the gate they put on the rows.
misses() asks of each point its as-built and changed verdicts as stated first, what the as-built Unresolved rests on, K1
and the case's indices at all three cutoffs, the case's type under the changed reading, and branch identity on both pairs.

An Unresolved mark names its cause, tested from the records, so that an Unresolved for any other reason misses it:
  link   every reason names a set that is two groups at N = 24 and 32 and one group of two members at N = 40
  flag   the one reason is the structure line, and D's flag is the only unresolved item, at N = 40 alone, with B clearing it

refusal() is what run/jobs.py and run/runner.py ask before a row: a pass, written by the job `fresh`, whose marks are
run/grid.py's and whose reading files are unchanged. A miss is diagnosed and disclosed, and moving past it takes a dated
commit, since the marks are in the manifest.
"""
import json
import os
import re

import census_lib as lib
import changed
import checks as ck
import driver as dr
import grid

PASS_FILE = 'fresh_pass.json'
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
        idn = changed.identity(d['identity'].get(k, {}).get(lib.pair_key(pair)),
                               {N: d['cutoffs'][str(N)]['points'].get(k) for N in pair}, pair)
        if not idn or not idn['kept']:
            got.append(f'branch identity fails between N = {pair[0]} and {pair[1]}')
    return got


def marks_now():
    return [[tag, e, *m] for (tag, e), m in grid.PASS_MARKS.items()]


def reading_files(out):
    return {f'{t}.json': dr.sha(os.path.join(out, f'{t}.json')) for t in sorted({tag for tag, _ in grid.PASS_MARKS})}


def evaluate(out):
    """Every mark's misses, the marks, and the reading files they rest on."""
    results = {f'{tag} {e:g}': misses(out, tag, e, m) for (tag, e), m in grid.PASS_MARKS.items()}
    return dict(results=results, passed=not any(results.values()), marks=marks_now(), files=reading_files(out))


def refusal(out):
    """Why no row may be read yet, or None once the fresh controls have passed."""
    path = os.path.join(out, PASS_FILE)
    if not os.path.exists(path):
        return 'the fresh controls have no pass on record'
    rec = lib.load_json(path)
    if not rec['passed']:
        return 'a fresh control missed its marks: ' + '; '.join(f'{k}: {v[0]}' for k, v in rec['results'].items() if v)
    if rec['marks'] != marks_now():
        return "the pass on record is not for run/grid.py's marks"
    for f, h in rec['files'].items():
        if not os.path.exists(os.path.join(out, f)) or dr.sha(os.path.join(out, f)) != h:
            return f'{f} differs from the file the pass rests on'
    return None
