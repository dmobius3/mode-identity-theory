#!/usr/bin/env python3
"""Test 3: the reproduction gate, on data already on record, with no solve (M8.17's terms: THE TESTS BEFORE THE
FREEZE, test 3; THE FREEZE, THE GUARD AND THE RUN, the three rules).

Usage: test_gate.py

It runs in a seedcheck process, where every solver and record path refuses, and reads reference/ only: M8.16.1's and
M8.16's outputs, and amendment 5's ladder, each as tools/copy_from_mit.py placed and checked it.

Claims, derived before the run:
  1. Rule 1, the exact comparison (census_lib.gate_full): at every point of M8.16.1's controls and pyramid, C1, C2a,
     C2b, C3, C2a/R5 and P5, M8.16.1's record equals M8.16's, timings aside. Beside it, the whole of each case's points,
     readings and identity records is compared, C1's N = 40 included, since the rule reads N = 16, 24 and 32 only.
  2. Rule 3, the categorical comparison (census_lib.gate_categorical): amendment 5's ladder reached 0.5, 1 and 2 by
     other steps than the registered C2a/R5 sample, and equals it in every categorical field at each. Beside it: rule 1
     holds at 0.25, reached by the same step, and fails at 0.5, 1 and 2, which is why rule 3 governs there.
  3. Rule 2, the withheld-point comparison (census_lib.gate_solve): at M8.16.1's five withheld points, a record made of
     the stored solve and acceptance fields, with spectral fields added, as the run's record of the point will carry
     them, equals the stored record.
  4. Mutations: every compared field, mutated alone, fails its rule:
     - rule 1: every leaf of one point's records, C2a at 0.25 and P5 at 0.25, each cutoff's point, the reading and the
       identity record; and a field added or removed;
     - rule 3: each categorical field at each cutoff, and the rule's verdict and type, at the ladder's 0.5; a Krein
       count added, since these records carry none;
     - rule 2: each solve and acceptance field at each cutoff, at each withheld point, and each removed.
  5. What the rules leave out: a timing changed passes every rule; a non-categorical field, lam, changed passes
     rule 3; a spectral field changed passes rule 2.
"""
import copy
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import census_lib as lib  # noqa: E402

out = []
REF = os.path.join(ROOT, 'reference')
CONTROLS = ['C1', 'C2a', 'C2b', 'C3', 'C2a_R5', 'P5']
WITHHELD5 = [('T2/R4', 16.0), ('T2/R4', lib.T2_END), ('T3/R4', 32.0), ('T3/R5', 16.0), ('T5/R2', lib.WINDOWS['R2'][15])]


def say(s=''):
    print(s, flush=True)
    out.append(s)


def load(*p):
    return lib.load_json(os.path.join(REF, *p))


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


def mutated(rec, path):
    r = copy.deepcopy(rec)
    parent = get(r, path[:-1])
    parent[path[-1]] = mutate(parent[path[-1]])
    return r


def caught(rule, rec, ref, path):
    """Whether rule fails on rec with the leaf at path mutated alone; rec is changed in place and restored."""
    parent = get(rec, path[:-1])
    old = parent[path[-1]]
    parent[path[-1]] = mutate(old)
    try:
        return bool(rule(rec, ref))
    finally:
        parent[path[-1]] = old


def main():
    devtools.require('seedcheck')
    say('Test 3, the reproduction gate, on data already on record, with no solve, in a seedcheck process.')
    fails = 0
    # 1. rule 1 on the controls and the pyramid
    bad, n, whole = [], 0, []
    for c in CONTROLS:
        mine, theirs = load('m8_16_1', 'run', 'out', f'{c}.json'), load('m8_16', 'run', 'out', f'{c}.json')
        for p in mine['case']['points']:
            n += 1
            d = lib.gate_full(lib.at(mine, p['eps']), lib.at(theirs, p['eps']))
            if d:
                bad.append(f"{c} {p['eps']:g}: {d[:2]}")
        for part in ('cutoffs', 'readings', 'identity'):
            whole += [f'{c}: {x}' for x in lib.differences(mine[part], theirs[part], '/' + part)]
    say(f"1. {'PASS' if not bad else 'FAIL'}: rule 1 at {n} points of the controls and the pyramid: M8.16.1's equal "
        f"M8.16's; the whole points, readings and identity, C1's N = 40 included: {len(whole)} differences"
        + ''.join(f'\n      {b}' for b in (bad + whole)[:8]))
    fails += bool(bad) + bool(whole)
    # 2. rule 3 on the ladder against the sample
    lad = load('m8_16_1', 'dev', 'runs', '015_ladder', 'C2a_R5_ladder.json')
    smp = load('m8_16_1', 'run', 'out', 'C2a_R5.json')
    bad2, side = [], []
    for e in (0.5, 1.0, 2.0):
        d = lib.gate_categorical(lib.at(lad, e), lib.at(smp, e))
        if d:
            bad2.append(f'{e:g}: {d[:3]}')
        side.append((e, len(lib.gate_full(lib.at(lad, e), lib.at(smp, e)))))
    at25 = lib.gate_full(lib.at(lad, 0.25), lib.at(smp, 0.25))
    steps = [p['eps'] for p in lad['case']['points']]
    ok2 = not bad2 and not at25 and all(k for _, k in side) and not lib.same_steps(steps, [p['eps'] for p in
                                                                                       smp['case']['points']], 0.5)
    say(f"2. {'PASS' if ok2 else 'FAIL'}: rule 3 holds at 0.5, 1 and 2 on the ladder against the sample; beside it, "
        f"rule 1 holds at 0.25 ({len(at25)} differences) and fails at "
        + ', '.join(f'{e:g} ({k} differences)' for e, k in side) + ''.join(f'\n      {b}' for b in bad2))
    fails += not ok2
    # 3. rule 2 at the five withheld points
    bad3, base = [], {}
    for row, e in WITHHELD5:
        theirs = lib.at(lib.load_json(os.path.join(REF, 'm8_16_1', 'run', 'out', row.replace('/', '_') + '.json')), e)
        neighbour = lib.at(lib.load_json(os.path.join(REF, 'm8_16_1', 'run', 'out', row.replace('/', '_') + '.json')),
                           lib.WINDOWS[lib.SLOT[row]][lib.WINDOWS[lib.SLOT[row]].index(e) - 1])
        mine = dict(points={}, reading=neighbour['reading'], identity=neighbour['identity'])
        for N in lib.CUTOFFS:
            p = {k: v for k, v in theirs['points'][N].items() if k != 'withheld'}
            p.update({k: v for k, v in neighbour['points'][N].items() if k not in lib.SOLVE_FIELDS and k not in lib.TIMINGS})
            mine['points'][N] = p
        base[(row, e)] = (mine, theirs)
        d = lib.gate_solve(mine, theirs)
        if d:
            bad3.append(f'{row} {e:g}: {d[:2]}')
    say(f"3. {'PASS' if not bad3 else 'FAIL'}: rule 2 at the five withheld points, each record carrying spectral fields "
        f"beside the stored solve" + ''.join(f'\n      {b}' for b in bad3))
    fails += bool(bad3)
    # 4. mutations
    held = []
    for c in ('C2a', 'P5'):
        mine = lib.at(load('m8_16_1', 'run', 'out', f'{c}.json'), 0.25)
        theirs = lib.at(load('m8_16', 'run', 'out', f'{c}.json'), 0.25)
        paths = [('points', N) + x for N in lib.CUTOFFS for x in leaves(mine['points'][N])] + \
                [('reading',) + x for x in leaves(mine['reading'])] + [('identity',) + x for x in leaves(mine['identity'])]
        paths = [p for p in paths if not set(p) & lib.TIMINGS]
        missed = [p for p in paths if not caught(lib.gate_full, mine, theirs, p)]
        extra = copy.deepcopy(mine)
        extra['points'][16]['added'] = 1
        gone = copy.deepcopy(mine)
        del gone['points'][32]['lam']
        held.append((f'rule 1, {c} at 0.25: {len(paths)} leaves mutated, {len(missed)} passed; a field added and one '
                     f'removed fail', not missed and bool(lib.gate_full(extra, theirs)) and bool(lib.gate_full(gone, theirs)),
                     missed[:3]))
    mine3, theirs3 = lib.at(lad, 0.5), lib.at(smp, 0.5)
    cat = [('points', N, 'record', f) for N in lib.CUTOFFS for f in lib.CATEGORICAL] + [('reading', 'verdict'),
                                                                                         ('reading', 'type')]
    missed = [p for p in cat if not lib.gate_categorical(mutated(mine3, p), theirs3)]
    kr = copy.deepcopy(mine3)
    kr['points'][24]['record']['krein'] = [1]
    held.append((f'rule 3, the ladder at 0.5: {len(cat)} categorical fields mutated, {len(missed)} passed; a Krein '
                 f'count added fails', not missed and bool(lib.gate_categorical(kr, theirs3)), missed[:3]))
    n2, missed2 = 0, []
    for (row, e), (mine, theirs) in base.items():
        for N in lib.CUTOFFS:
            for f in lib.SOLVE_FIELDS:
                n2 += 2
                if not lib.gate_solve(mutated(mine, ('points', N, f)), theirs):
                    missed2.append(f'{row} {e:g} N = {N} {f} mutated')
                g = copy.deepcopy(mine)
                del g['points'][N][f]
                if not lib.gate_solve(g, theirs):
                    missed2.append(f'{row} {e:g} N = {N} {f} removed')
    held.append((f'rule 2, five points: {n2} mutations and removals, {len(missed2)} passed', not missed2, missed2[:3]))
    ok4 = all(ok for _, ok, _ in held)
    say(f"4. {'PASS' if ok4 else 'FAIL'}: every compared field, mutated alone, fails its rule")
    for label, ok, m in held:
        say(f"      {label}{'' if ok else ': FAIL ' + str(m)}")
    fails += not ok4
    # 5. what the rules leave out
    t1 = copy.deepcopy(lib.at(load('m8_16_1', 'run', 'out', 'C2a.json'), 0.25))
    for N in lib.CUTOFFS:
        t1['points'][N]['seconds'] = t1['points'][N]['seconds'] + 1.0
        t1['points'][N]['seconds_record'] = t1['points'][N].get('seconds_record', 0.0) + 1.0
    lam3 = copy.deepcopy(mine3)
    lam3['points'][32]['lam'] = lam3['points'][32]['lam'] * (1 + 1e-9)
    (row, e), (m2, t2) = next(iter(base.items()))
    spec = copy.deepcopy(m2)
    spec['points'][32]['record']['nL'] += 1
    keep = [('a timing changed, rule 1', not lib.gate_full(t1, lib.at(load('m8_16', 'run', 'out', 'C2a.json'), 0.25))),
            ('a timing changed, rule 3', not lib.gate_categorical(dict(mine3, points={N: dict(mine3['points'][N],
                                                                                                seconds=0.0)
                                                                                     for N in lib.CUTOFFS}), theirs3)),
            ('lam changed, rule 3', not lib.gate_categorical(lam3, theirs3)),
            ('a spectral field changed, rule 2', not lib.gate_solve(spec, t2))]
    ok5 = all(ok for _, ok in keep)
    say(f"5. {'PASS' if ok5 else 'FAIL'}: " + '; '.join(f"{w} {'passes' if ok else 'FAILS'}" for w, ok in keep))
    fails += not ok5
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_gate.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
