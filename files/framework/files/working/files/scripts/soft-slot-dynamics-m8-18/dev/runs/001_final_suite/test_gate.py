#!/usr/bin/env python3
"""Test 4: the reproduction gate, on data on record, with no solve (M8.18's terms: THE TESTS BEFORE THE FREEZE, test 4;
THE FREEZE, THE GUARD AND THE RUN).

Usage: test_gate.py

It runs in a seedcheck process, where every solver and record path refuses, and reads reference/ only, as
tools/copy_from_mit.py placed and checked it.

Claims, derived before the run:
  1. The exact comparison on two computations of one point: M8.17's locator recomputed T4/R5's path through Cutoff, and
     its stored ends, 8 and 11.31, equal its row's records from run_case, field for field, at every cutoff, by
     census_lib.gate_full, with their reading and identity record.
  2. A path at N = 24 and 32 against its record (census_lib.gate_cutoff): a copy of each of the five rows and six
     controls passes at every registered point, with P5's k3_overlaps left out of the copy at 0.25, since Cutoff does not
     compute them, and no other field.
  3. The identity between N = 24 and 32 (census_lib.gate_identity): each row's records, in this run's shape, pass.
  4. M8.17's midpoints (census_lib.gate_midpoints): a copy passes at every cutoff, and a copy with a moved point after
     the record's ten passes, since M8.17 never computed it.
  5. Mutations: every compared field, mutated alone, fails its gate: every leaf of one point's records on C2a at 0.25,
     at N = 24 and 32, and on T4/R4 at 4, at N = 24, since the comparison is the same at every cutoff and the larger
     record costs an hour; every leaf of the seed; every leaf of one identity record; every leaf of T4/R5's last midpoint
     at N = 32, the one K1 refused; a midpoint removed; a field added or removed.
  6. What the gates leave out: a timing changed passes every gate, and the band's reading beside it is not compared.
  7. The solve-state gate, on a stored file (census.Run.stored): a path's files written and logged pass, with each
     solution equal to what was written; a byte changed in either file stops the run, and so does a stored lam
     that differs from the job's record, with both files logged again; a solution with no job is not used.
"""
import copy
import os
import sys
import tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

out = []
A, B = lib.ARM_A, lib.ARM_B


def say(s=''):
    print(s, flush=True)
    out.append(s)


def leaves(o, path=()):
    """Every leaf of a record, as a path of keys and indices."""
    if isinstance(o, dict):
        return [x for k, v in o.items() for x in leaves(v, path + (k,))]
    if isinstance(o, list):
        return [x for i, v in enumerate(o) for x in leaves(v, path + (i,))] or [path]
    return [path]


def get(o, path):
    for k in path:
        o = o[k]
    return o


def mutate(v):
    """A value changed in the smallest way its type allows."""
    if isinstance(v, bool):
        return not v
    if isinstance(v, int):
        return v + 1
    if isinstance(v, float):
        return v + max(abs(v), 1e-300) * 4.4e-16 if v == v else 0.0
    if isinstance(v, str):
        return v + 'x'
    if v is None:
        return 0
    if isinstance(v, list):
        return v + [0]
    raise TypeError(type(v))


def caught(check, rec, path):
    """Whether check(rec) fails with the leaf at path mutated alone; rec is restored."""
    parent = get(rec, path[:-1])
    old = parent[path[-1]]
    parent[path[-1]] = mutate(old)
    try:
        return bool(check(rec))
    finally:
        parent[path[-1]] = old


def main():
    devtools.require('seedcheck')
    say('Test 4, the reproduction gate, on data on record, with no solve, in a seedcheck process.')
    fails = 0
    row = lib.ARM_B_ROW
    th, known = lib.theirs(row, ROOT), lib.m817_file(lib.LOCATED_B, ROOT)
    bad = []
    for k, mine in known['ends'].items():
        m = dict(points={int(N): p for N, p in mine['points'].items()}, reading=mine['reading'],
                 identity={lib.pair_key((24, 32)): mine['identity']})
        bad += lib.gate_full(m, lib.at(th, float(k), B), B)
    ok1 = not bad
    say(f"1. {'PASS' if ok1 else 'FAIL'}: M8.17's recomputed ends of T4/R5 equal its row's records at every cutoff: "
        f"{len(bad)} differences" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += not ok1
    # 2. a path against its record
    names, n, bad = lib.ROWS + lib.READ_CONTROLS, 0, []
    for name in names:
        rec = lib.theirs(name, ROOT)
        eps = [p['eps'] for p in rec['case']['points']]
        for N in ('24', '32'):
            mine = copy.deepcopy(rec['cutoffs'][N])
            for p in mine['points'].values():
                p.pop('k3_overlaps', None)
            n += len(eps)
            bad += [f'{name} N = {N}: {d}' for d in lib.gate_cutoff(mine, rec['cutoffs'][N], eps)]
    p5 = lib.theirs('P5', ROOT)
    other = copy.deepcopy(p5['cutoffs']['24'])
    other['points'][lib.key(0.25)].pop('coefficient')
    extra = bool(lib.gate_cutoff(other, p5['cutoffs']['24'], [0.25]))
    has = 'k3_overlaps' in p5['cutoffs']['24']['points'][lib.key(0.25)]
    ok2 = not bad and extra and has
    say(f"2. {'PASS' if ok2 else 'FAIL'}: {n} points of the five rows and six controls at N = 24 and 32; P5's k3_overlaps "
        f"left out at 0.25 passes ({has}), and another field left out fails ({extra})" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += not ok2
    # 3. the identity between N = 24 and 32
    bad, n = [], 0
    for r in lib.ROWS:
        rec = lib.theirs(r, ROOT)
        mine = {k: {lib.pair_key((24, 32)): v} for k, v in rec['identity'].items()}
        eps = [p['eps'] for p in rec['case']['points'] if p['read']]
        n += len(eps)
        bad += lib.gate_identity(mine, rec['identity'], eps)
    say(f"3. {'PASS' if not bad else 'FAIL'}: the identity records at {n} points" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += bool(bad)
    # 4. the midpoints
    bad, n = [], 0
    for N, res in known['bisection'].items():
        theirs = res['midpoints']
        n += len(theirs)
        bad += lib.gate_midpoints(copy.deepcopy(theirs), theirs)
        moved = copy.deepcopy(theirs) + [dict(copy.deepcopy(theirs[-1]), eps=8.72099, moved=True)]
        bad += lib.gate_midpoints(moved, theirs)
    say(f"4. {'PASS' if not bad else 'FAIL'}: {n} of M8.17's midpoints, at every cutoff, alone and with a moved point after "
        f"them" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += bool(bad)
    # 5. mutations
    held = []
    for name, e, cuts in (('C2a', 0.25, ('24', '32')), ('T4/R4', 4.0, ('24',))):
        rec = lib.theirs(name, ROOT)
        k = lib.key(e)
        for N in cuts:
            ref = rec['cutoffs'][N]
            mine = copy.deepcopy(ref)
            paths = [('points', k) + x for x in leaves(mine['points'][k])] + [('seed',) + x for x in leaves(mine['seed'])]
            paths = [p for p in paths if not set(p) & lib.TIMINGS]
            missed = [p for p in paths if not caught(lambda m: lib.gate_cutoff(m, ref, [e]), mine, p)]
            added = copy.deepcopy(mine)
            added['points'][k]['added'] = 1
            gone = copy.deepcopy(mine)
            del gone['points'][k]['lam']
            held.append((f'{name} at {e:g}, N = {N}: {len(paths)} leaves mutated, {len(missed)} passed; a field added and one '
                         f'removed fail', not missed and bool(lib.gate_cutoff(added, ref, [e]))
                         and bool(lib.gate_cutoff(gone, ref, [e])), missed[:3]))
    rec = lib.theirs('T4/R4', ROOT)
    k = lib.key(4.0)
    mine = {k: {lib.pair_key((24, 32)): copy.deepcopy(rec['identity'][k])}}
    paths = [(k, lib.pair_key((24, 32))) + x for x in leaves(rec['identity'][k])]
    missed = [p for p in paths if not caught(lambda m: lib.gate_identity(m, rec['identity'], [4.0]), mine, p)]
    held.append((f'the identity at 4: {len(paths)} leaves mutated, {len(missed)} passed', not missed, missed[:3]))
    theirs = known['bisection']['32']['midpoints']
    mine = copy.deepcopy(theirs)
    paths = [(9,) + x for x in leaves(mine[9]) if not set(x) & lib.TIMINGS]
    missed = [p for p in paths if not caught(lambda m: lib.gate_midpoints(m, theirs), mine, p)]
    short = bool(lib.gate_midpoints(mine[:-1], theirs))
    held.append((f'the refused midpoint, N = 32: {len(paths)} leaves mutated, {len(missed)} passed; a midpoint removed '
                 f'fails', not missed and short, missed[:3]))
    ok5 = all(ok for _, ok, _ in held)
    say(f"5. {'PASS' if ok5 else 'FAIL'}: every compared field, mutated alone, fails its gate")
    for label, ok, m in held:
        say(f"      {label}{'' if ok else ': FAIL ' + str(m)}")
    fails += not ok5
    # 6. what the gates leave out
    ref = lib.theirs('C2a', ROOT)['cutoffs']['24']
    t1 = copy.deepcopy(ref)
    for p in t1['points'].values():
        p['seconds'] += 1.0
        p['seconds_record'] += 1.0
    t1['setup_seconds'] = 0.0
    mids = copy.deepcopy(known['bisection']['24']['midpoints'])
    for m in mids:
        m['from_lower']['point']['seconds'] += 1.0
    ok6 = not lib.gate_cutoff(t1, ref, [0.25, 0.5]) and not lib.gate_midpoints(mids, known['bisection']['24']['midpoints'])
    say(f"6. {'PASS' if ok6 else 'FAIL'}: a timing changed passes the path's gate and the midpoints'")
    fails += not ok6
    # 7. the solve-state gate
    with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as tmp:
        run = census.Run(dict(cases={}), tmp, None)
        base = 'C2a_N24'
        c = [np.arange(4.0) + 1j * i for i in range(2)]
        lam, slope = [48.25, 48.5], [0.9, 0.8]
        np.savez(run.at(base + '.npz'), keys=np.array(['0.25', '0.5']), c0=c[0], c1=c[1], lam=np.array(lam), slope=np.array(slope))
        pts = {'0.25': dict(accepted=True, lam=lam[0]), '0.5': dict(accepted=True, lam=lam[1])}
        census.json.dump(dict(seed=dict(ok=True), points=pts), open(run.at(base + '.json'), 'w', encoding='utf-8'))
        run.complete('path:C2a:24', [base + '.npz', base + '.json'])
        st = run.stored('C2a', 24)
        good = (np.array_equal(st['sols']['0.5']['c'], c[1]) and st['sols']['0.25']['state'][1:] == (lam[0], slope[0])
                and st['sols']['0.5']['ok'])

        def stops():
            try:
                run.stored('C2a', 24)
                return False
            except census.StopRun:
                return True
        res = {}
        for f_ in (base + '.npz', base + '.json'):
            raw = open(run.at(f_), 'rb').read()
            with open(run.at(f_), 'wb') as g:
                g.write(raw[:60] + bytes([raw[60] ^ 1]) + raw[61:])
            res[f'a byte in {f_}'] = stops()
            with open(run.at(f_), 'wb') as g:
                g.write(raw)
        raw = open(run.at(base + '.json'), 'rb').read()
        census.json.dump(dict(seed=dict(ok=True), points={'0.25': dict(accepted=True, lam=lam[0] + 1e-13), '0.5': pts['0.5']}),
                         open(run.at(base + '.json'), 'w', encoding='utf-8'))
        run.complete('path:C2a:24', [base + '.npz', base + '.json'])
        res['a lam that differs, the files logged again'] = stops()
        with open(run.at(base + '.json'), 'wb') as g:
            g.write(raw)
        run.complete('path:C2a:24', [base + '.npz', base + '.json'])
        nojob = False
        try:
            run.stored('C2b', 24)
        except KeyError:
            nojob = True
        res['no job'] = nojob
        ok7 = good and all(res.values()) and not stops()
    say(f"7. {'PASS' if ok7 else 'FAIL'}: the solve-state gate: solutions returned as written: {good}; "
        + '; '.join(f'{k}: {v}' for k, v in res.items()))
    fails += not ok7
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_gate.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
