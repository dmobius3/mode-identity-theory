"""The fresh controls against their pass marks (grid.PASS_MARKS; DESIGN.md, section 5), and the gate they put on the rows.
misses() asks of each point its as-built and changed verdicts as stated first, what the as-built Unresolved rests on, K1
and the case's indices at all three cutoffs, the case's type under the changed reading, and branch identity on both pairs.

An Unresolved mark names its cause, tested from the records, so that an Unresolved for any other reason misses it:
  link   every reason names a set that is two groups at N = 24 and 32 and one group of two members at N = 40
  flag   the one reason is the structure line, and D's flag is the only unresolved item, at N = 40 alone, with B clearing it

refusal() is what run/jobs.py and run/runner.py ask before a row: a pass for run/grid.py's marks, written by the fresh
check's job, its file the one that job logged and its reading files unchanged. The job and its file are named by the marks
they test (names), so a miss stays on record. A miss is diagnosed and disclosed, and moving past it takes a dated commit,
since the marks are in the manifest; the new marks get a job of their own.

The same test on the new ladder of run/TOP48.md (grid.LADDER_48, grid.PASS_MARKS_48), on each control's reading there,
`TAG_L48.json`: misses() with that ladder, its causes and the seed's check at each cutoff; an as-built mark of None is
reported and not marked. Its causes, each at the new ladder's cutoffs:
  flag_40_48  the one reason is the structure line, and D's flag is the only unresolved item, at N = 40 and 48 alone,
              with B clearing it at both
  flag_48     the same, at N = 48 alone
refusal_48() is what T5's reads at N = 48 ask: a pass for those marks, by the fresh48 check's job (names_48).
"""
import hashlib
import json
import os
import re

import census_lib as lib
import changed
import checks as ck
import driver as dr
import grid

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


def flag_at(d, k, reasons, flagged):
    """Whether the as-built Unresolved rests on D's flag alone, at the new ladder's cutoffs flagged and no other, with B
    clearing it at each."""
    pts = [d['cutoffs'][str(N)]['points'][k] for N in grid.LADDER_48]
    return (reasons == [STRUCTURE]
            and [p['record']['unresolved'] for p in pts] == [[changed.ND_LINE] if N in flagged else [] for N in grid.LADDER_48]
            and all(p['b_resolved'] is True for N, p in zip(grid.LADDER_48, pts) if N in flagged))


CAUSES_48 = dict(flag_40_48=lambda d, k, reasons: flag_at(d, k, reasons, (40, 48)),
                 flag_48=lambda d, k, reasons: flag_at(d, k, reasons, (48,)))


def misses(out, tag, e, marks, ladder=None, causes=None, fname=None, seeds=False):
    """What keeps one point from its marks: an empty list is a pass. By default the first ladder's, on TAG.json; the
    new ladder passes its own ladder, causes and file, and asks the seed's check at each cutoff."""
    ladder = grid.LADDER if ladder is None else ladder
    causes = CAUSES if causes is None else causes
    with open(os.path.join(out, fname or tag + '.json'), encoding='utf-8') as f:
        d = json.load(f)
    k, case, got = lib.key(e), d['case'], []
    built, chg = d['readings'].get(k), d['changed'].get(k)
    if not built or not chg:
        return ['no reading']
    if marks[0] is None:
        pass
    elif built['verdict'] != marks[0]:
        got.append(f"as built {built['verdict']}, marked {marks[0]}: {built['reasons'][:1]}")
    elif marks[2] and not causes[marks[2]](d, k, built['reasons']):
        got.append(f"as built Unresolved, and not by the mark's {marks[2]}: {built['reasons'][:1]}")
    if chg['verdict'] != marks[1]:
        got.append(f"changed {chg['verdict']}, marked {marks[1]}: {chg['reasons'][:1]}")
    elif chg['type'] != case['type']:
        got.append(f"changed type {chg['type']}, the case's {case['type']}")
    for N in ladder:
        if seeds and not d['cutoffs'][str(N)].get('seed', {}).get('ok'):
            got.append(f"the seed's check fails at N = {N}")
        p = d['cutoffs'][str(N)]['points'].get(k)
        if not p or 'record' not in p:
            got.append(f'no record at N = {N}')
            continue
        r = p['record']
        if not ck.k1(p, case):
            got.append(f'K1 fails at N = {N}')
        if [r['nL'], r['nD'], r['K']] != case['idx']:
            got.append(f"indices {[r['nL'], r['nD'], r['K']]} at N = {N}, the case's {case['idx']}")
    for pair in zip(ladder, ladder[1:]):
        idn = changed.identity(d['identity'].get(k, {}).get(lib.pair_key(pair)),
                               {N: d['cutoffs'][str(N)]['points'].get(k) for N in pair}, pair)
        if not idn or not idn['kept']:
            got.append(f'branch identity fails between N = {pair[0]} and {pair[1]}')
    return got


def marks_now():
    return [[tag, e, *m] for (tag, e), m in grid.PASS_MARKS.items()]


def names():
    """The fresh check's job and its file, named by the marks they test: (job, file)."""
    h = hashlib.sha256(json.dumps(marks_now()).encode('utf-8')).hexdigest()[:12]
    return f'fresh_{h}', f'fresh_pass_{h}.json'


def reading_files(out):
    return {f'{t}.json': dr.sha(os.path.join(out, f'{t}.json')) for t in sorted({tag for tag, _ in grid.PASS_MARKS})}


def evaluate(out):
    """Every mark's misses, the marks, and the reading files they rest on."""
    results = {f'{tag} {e:g}': misses(out, tag, e, m) for (tag, e), m in grid.PASS_MARKS.items()}
    return dict(results=results, passed=not any(results.values()), marks=marks_now(), files=reading_files(out))


def refusal(out):
    """Why no row may be read yet, or None once the fresh controls have passed."""
    return _refusal(out, *names(), marks_now())


def _refusal(out, name, pass_file, marks):
    job = os.path.join(out, 'jobs', name + '.json')
    if not os.path.exists(job):
        return 'the fresh controls have no pass on record'
    path = os.path.join(out, pass_file)
    if not os.path.exists(path) or dr.sha(path) != lib.load_json(job)['files'].get(pass_file):
        return f'{pass_file} differs from the SHA-256 its job logged'
    rec = lib.load_json(path)
    if not rec['passed']:
        return 'a fresh control missed its marks: ' + '; '.join(f'{k}: {v[0]}' for k, v in rec['results'].items() if v)
    if rec['marks'] != marks:
        return "the pass on record is not for run/grid.py's marks"
    for f, h in rec['files'].items():
        if not os.path.exists(os.path.join(out, f)) or dr.sha(os.path.join(out, f)) != h:
            return f'{f} differs from the file the pass rests on'
    return None


# --- the new ladder (run/TOP48.md, section 4) -------------------------------------------------------------------------
def marks_48():
    return [[tag, e, *m] for (tag, e), m in grid.PASS_MARKS_48.items()]


def names_48():
    """The fresh48 check's job and its file, named by the marks they test: (job, file)."""
    h = hashlib.sha256(json.dumps(marks_48()).encode('utf-8')).hexdigest()[:12]
    return f'fresh48_{h}', f'fresh48_pass_{h}.json'


def evaluate_48(out):
    """Every new-ladder mark's misses, the marks, and the reading files they rest on."""
    results = {f'{tag} {e:g}': misses(out, tag, e, m, grid.LADDER_48, CAUSES_48, f'{tag}_L48.json', seeds=True)
               for (tag, e), m in grid.PASS_MARKS_48.items()}
    files = {f'{t}_L48.json': dr.sha(os.path.join(out, f'{t}_L48.json'))
             for t in sorted({tag for tag, _ in grid.PASS_MARKS_48})}
    return dict(results=results, passed=not any(results.values()), marks=marks_48(), files=files)


def refusal_48(out):
    """Why T5's top may not be read at N = 48 yet, or None once the fresh controls have passed on the new ladder."""
    return _refusal(out, *names_48(), marks_48())
