#!/usr/bin/env python3
"""MIT's locator for T4/R4's change of type (run/LOCATOR.md; DESIGN.md, section 4): census_lib.settle, M8.17's locator,
on this computation's ladder, from the ends' stored solutions, with Arm B's moved midpoint, and named only where both
verdicts agree at the guard readings it takes. Before it reads T4/R4, the same code reproduces M8.18's location of
T4/R5's change on this tree.

repro(out, source)  M8.18's Arm B, run again as M8.18's census.py ran it: census_lib.locate on T4/R5's bracket (8, 11.31)
                    and Arm B's ladder, each cutoff's path recomputed from its seed, every recomputed point equal to
                    M8.17's record, each of M8.17's midpoints equal, a midpoint K1 refuses moved once. Its whole record
                    must equal M8.18's ARM_B.json, timings aside, and its solutions M8.18's arm_b_solutions.npz. source
                    is M8.18's published folder, each file it reads checked against M8.18's SHA256SUMS, whose SHA-256
                    jobs.M818_SUMS pins.
locate(out)         T4/R4's bracket on N = 24, 32 and 40, refused without a passing reproduction on record (refusal).

Both jobs read, so each waits for the census page's note on this tree's pin (jobs.note_gate). A midpoint's and a guard
reading's solutions are solved and read inside the job and kept in a file of their own: no job here loads a solution
through jobs.stored but the bracket's ends, which this computation's solves hold.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import census  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import driver as dr  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402

TAG, BRACKET, REPRO = grid.LOCATOR['row'], grid.LOCATOR['bracket'], grid.LOCATOR['repro']
LAD = lib.ARM_A
JOB, FILE = f'locate_{TAG}', f'LOCATE_{TAG}.json'
REPRO_JOB, REPRO_FILE = 'locate_repro_T4_R5', 'LOCATE_REPRO_T4_R5.json'
# what the reproduction reads from M8.18's folder, each by M8.18's SHA256SUMS
M818 = dict(arm_b='run/out/ARM_B.json', solutions='run/out/arm_b_solutions.npz', frozen='run/FROZEN.json',
            path='reference/m8_17/run/out/T4_R5.json', midpoints='reference/m8_17/run/out/locate_T4_R5_8_11.313708499.json',
            census='reference/m8_17/run/out/CENSUS.json')


def m818_source(source):
    """M8.18's files the reproduction reads, refused unless source's SHA256SUMS is M8.18's, pinned, and each file is the
    one it lists: {name: the parsed JSON, or the .npz's arrays}, with each file's SHA-256 under 'sha256'."""
    sums = os.path.join(source, 'SHA256SUMS')
    if not os.path.exists(sums) or dr.sha(sums) != jobs.M818_SUMS:
        raise PermissionError(f"{source} is not M8.18's published folder: its SHA256SUMS is not the pinned one")
    with open(sums, encoding='utf-8') as f:
        held = {line.split(None, 1)[1].strip(): line.split()[0] for line in f if line.strip()}
    out = dict(sha256={})
    for name, rel in M818.items():
        p = os.path.join(source, rel)
        h = dr.sha(p) if os.path.exists(p) else None
        if h is None or h != held.get(rel):
            raise PermissionError(f"{rel} differs from M8.18's SHA256SUMS")
        out['sha256'][rel] = h
        if rel.endswith('.npz'):
            with np.load(p, allow_pickle=False) as z:
                out[name] = {k: z[k] for k in z.files}
        else:
            out[name] = lib.load_json(p)
    return out


def as_m818(point):
    """A read point without the fields this tree's read adds (jobs.NEW_FIELDS): M8.18's form."""
    return {k: v for k, v in point.items() if k not in jobs.NEW_FIELDS}


class ReproCut(jobs.Cut):
    """jobs.Cut, the read this computation's jobs make, with its new fields set aside, so a reproduced record is M8.18's
    form and compares with M8.18's field for field. K1 and n(L) are read before they are set aside."""

    def read(self, s, eps, why='mit'):
        r = super().read(s, eps, why)
        return dict(r, point=as_m818(r['point']))


def keep(out, job, cuts):
    """A location's midpoints and guard readings: their solutions, in a file of their own, as census.Run.keep_located
    writes them. Returns the file's name."""
    arrays = {}
    for N, cu in cuts.items():
        for i, (e, st) in enumerate(cu.kept):
            arrays[f'N{N}_{i}_c'], arrays[f'N{N}_{i}_ls'] = st[0], np.array([e, float(st[1]), float(st[2])])
        cu.kept = []
    fname = dr.safe(job) + '_solutions.npz'
    jobs.atomic(os.path.join(out, fname), lambda f: np.savez(f, **arrays))
    return fname


def same_arrays(a, b):
    """The keys in which two solution files differ, by key and by every entry."""
    keys = sorted(set(a) | set(b))
    return [k for k in keys if k not in a or k not in b or a[k].shape != b[k].shape or not np.array_equal(a[k], b[k])]


def repro(out, source):
    """M8.18's Arm B on this tree (the module docstring). Writes REPRO_FILE: the record, its differences from ARM_B.json
    and the solutions' from arm_b_solutions.npz, any stop, and whether it passed."""
    job = jobs.Job(out, REPRO_JOB)
    if job.done():
        return
    src = m818_source(source)
    lad, row = lib.ARM_B, REPRO
    case = src['frozen']['cases'][row]
    mine = census.roundtrip(cs.serialize(row, dict(cs.CASES[row], points=lib.path_points(row),
                                                   cutoffs=list(lad['cutoffs']))))
    diff = lib.differences(mine, case)
    if diff:
        raise PermissionError(f"T4/R5's case here differs from M8.18's frozen one: {diff[0]}")
    devtools.require(case['admission'])
    ch = next(dict(c) for c in src['census']['rows'][row]['changes'] if c['kind'] == 'type')
    if (lib.key(ch['lo']), lib.key(ch['hi'])) != tuple(map(lib.key, lib.BRACKET_B)):
        raise PermissionError(f"M8.17's bracket ({ch['lo']:g}, {ch['hi']:g}) is not Arm B's")
    cuts = {N: ReproCut(row, case, N) for N in lad['cutoffs']}
    known = src['midpoints']
    jobs.say(f"the reproduction: M8.18's Arm B, {row} on ({ch['lo']:g}, {ch['hi']:g})")
    rec, stop = lib.locate(ch, lib.WINDOWS[case['slot']], case, cuts, lambda sols: census.readings_of(cuts, sols, lad),
                           lambda cu, s1, s2: census.aligned(cu.Fn, cu.K, s1['c'], s2['c']),
                           lambda e: lib.at(src['path'], e, lad), lad, moved=lib.MOVED,
                           gate_mids=lambda N, mids: lib.gate_midpoints(census.roundtrip(mids),
                                                                        known['bisection'][str(N)]['midpoints']),
                           say=jobs.say)
    rec.update(row=row, moved=dict(fraction=lib.MOVED, end='lower'))
    rec = census.roundtrip(rec)
    sol_file = keep(out, REPRO_JOB, cuts)
    with np.load(os.path.join(out, sol_file), allow_pickle=False) as z:
        arrays = {k: z[k] for k in z.files}
    differences, unequal = lib.differences(rec, src['arm_b']), same_arrays(arrays, src['solutions'])
    passed = stop is None and not differences and not unequal
    res = dict(record=rec, stop=stop, differences=differences, unequal_arrays=unequal, arrays=len(arrays),
               compared=src['sha256'], passed=passed)
    jobs.write_json(job.at(REPRO_FILE), res)
    job.complete([REPRO_FILE, sol_file])
    jobs.say(f"   the reproduction {'passed' if passed else 'failed'}: stop {stop}; {len(differences)} differences "
             f"from ARM_B.json; {len(unequal)} of {len(arrays)} arrays unequal")


def refusal(out):
    """Why T4/R4 may not be located yet, or None: a passing reproduction on record, its file the one its job logged."""
    if not os.path.exists(os.path.join(out, 'jobs', REPRO_JOB + '.json')):
        return 'the reproduction has no record'
    try:
        jobs.record_of(out, REPRO_JOB)
    except (PermissionError, OSError) as e:
        return f'the reproduction record does not check: {e}'
    r = lib.load_json(os.path.join(out, REPRO_FILE))
    if not r['passed']:
        first = r['stop'] or (r['differences'] or r['unequal_arrays'])[0]
        return f'the reproduction did not pass: {first}'
    return None


def the_change(res):
    """T4/R4's one change of type, from the row's classified points, as built and changed: refused unless each reading
    gives the frozen bracket alone, between consecutive grid points, with the same types. Its ends are the grid's own
    values, not the reading's keys, which round them."""
    ks = sorted(res['both'], key=float)
    chs = {arm: lib.changes([(float(k), res['both'][k][arm]) for k in ks]) for arm in ('as_built', 'changed')}
    for arm, c in chs.items():
        if len(c) != 1 or c[0]['kind'] != 'type' or (lib.key(c[0]['lo']), lib.key(c[0]['hi'])) != tuple(map(lib.key, BRACKET)):
            raise PermissionError(f'the {arm} classification does not give the frozen bracket alone: {c}')
    a, b = chs['as_built'][0], chs['changed'][0]
    if (a['lo_type'], a['hi_type']) != (b['lo_type'], b['hi_type']):
        raise PermissionError(f'the two classifications type the bracket differently: {a} and {b}')
    return dict(a, lo=BRACKET[0], hi=BRACKET[1])


def _pts(records, cutoffs):
    """A record's points by cutoff, whether its keys are numbers or, after a round trip, strings."""
    p = records['points']
    return {N: p.get(N, p.get(str(N))) for N in cutoffs}


def changed_class(records, case, lad=LAD):
    """One point's changed classification from its records, as jobs.reading makes it: the changed reading, and branch
    identity with the records as B types them (changed.identity)."""
    pts = _pts(records, lad['cutoffs'])
    _, _, chg = jobs.rule([pts[N] for N in lad['cutoffs']])
    ids = {lib.pair_key(p): changed.identity((records.get('identity') or {}).get(lib.pair_key(p)), {N: pts[N] for N in p}, p)
           for p in lad['pairs']}
    return lib.here(dict(points=pts, reading=chg, identity=ids), case, lad)


def both_verdicts(rec, case, classify=changed_class):
    """The changed classification at every guard reading the locator took, and the location named only where it agrees
    with the as-built one at the guard readings that count, the first classified on each side (DESIGN.md, section 4).
    A disagreement leaves the bracket not located, with the guard and both readings named."""
    if not rec.get('guards'):
        rec['changed_guards'], rec['both_verdicts'] = None, None
        return rec
    out, disagree = {}, []
    for side, readings in rec['guards'].items():
        out[side] = []
        for g in readings:
            c = classify(g['reading']['records'], case)
            out[side].append(dict(delta=g['delta'], eps=g['eps'], changed={k: v for k, v in c.items() if k != 'records'}))
            if g['reading']['classified']:
                if not (c['classified'] and c['type'] == g['reading']['type']):
                    disagree.append(f"the {side} guard at {g['eps']:.6g} reads {g['reading']['type']} as built and "
                                    f"{c['type'] if c['classified'] else 'not classified'} changed")
                break
    rec['changed_guards'], rec['both_verdicts'] = out, not disagree
    if rec.get('located') and disagree:
        rec['located'], rec['span'] = False, None
        rec['failures'] = list(rec.get('failures') or []) + disagree
        rec['why'] = 'the two verdicts disagree at a guard reading that counts: ' + '; '.join(disagree)
    return rec


def locate(out):
    """T4/R4's bracket (the module docstring). Writes FILE: the ends' records, both ways, each cutoff's bisection with
    every midpoint from both ends, the location, the guard readings both ways, and the verdict."""
    job = jobs.Job(out, JOB)
    if job.done():
        return
    why = refusal(out)
    if why:
        raise PermissionError(f'T4/R4 is not located before the reproduction passes: {why}')
    name, _, case = grid.entry(TAG)
    devtools.require(case['admission'])
    jobs.record_of(out, f'reading_{TAG}')
    res = lib.load_json(job.at(f'{TAG}.json'))
    ch = the_change(res)
    lo, hi = ch['lo'], ch['hi']
    cuts = {N: jobs.Cut(name, case, N) for N in LAD['cutoffs']}
    st = {N: jobs.stored(out, TAG, N)[1] for N in LAD['cutoffs']}
    ends = {lib.key(e): lib.at(res, e, LAD) for e in (lo, hi)}
    for e in (lo, hi):
        for N in LAD['cutoffs']:
            s = st[N][lib.key(e)]
            if not s['ok'] or s['state'][1] != ends[lib.key(e)]['points'][N]['lam']:
                raise PermissionError(f"the stored end at {e:g}, N = {N}, is not the one the reads classified")
    rec = dict(bracket=[lo, hi], types=[ch['lo_type'], ch['hi_type']], seeds={N: cu.seed_ok for N, cu in cuts.items()},
               path={}, ends=ends, row=name, ends_both={lib.key(e): res['both'][lib.key(e)] for e in (lo, hi)},
               moved=dict(fraction=lib.MOVED, end='lower'))
    states = {N: (st[N][lib.key(lo)]['state'], st[N][lib.key(hi)]['state']) for N in cuts}
    jobs.say(f'{name} on ({lo:g}, {hi:g})')
    rec, _ = lib.settle(rec, ch, lib.WINDOWS[case['slot']], case, cuts, lambda sols: census.readings_of(cuts, sols, LAD),
                        lambda cu, s1, s2: census.aligned(cu.Fn, cu.K, s1['c'], s2['c']), LAD, states, moved=lib.MOVED,
                        say=jobs.say)
    rec = both_verdicts(census.roundtrip(rec), case)
    sol_file = keep(out, JOB, cuts)
    jobs.write_json(job.at(FILE), rec)
    job.complete([FILE, sol_file])
    jobs.say(f"   {name}: {rec.get('kind')}; located: {rec.get('located')}; {rec.get('why')}")
