#!/usr/bin/env python3
"""Tests 2 and 3: the reader and the band, with no solve (M8.18's terms: THE TESTS BEFORE THE FREEZE, tests 2 and 3; THE
TESTED BAND).

Usage: test_reader.py

It runs in a seedcheck process, where every solver and record path refuses, and reads reference/ only.

Claims, derived before the run:
  1. The reader: census.rule, on M8.17's stored summaries at N = 16, 24 and 32, reproduces M8.17's reading at every
     stored point of the five rows, field for field. The call that changed gives what the call it replaces gave.
  2. A point with a cutoff missing: the rule reads it Unresolved, 'a cutoff is missing', and census_lib.here refuses to
     classify it. M8.17's stored records at the twelve, on Arm A's ladder, hold no N = 40, so all twelve refuse.
  3. The band: at every stored point of the five rows, the reading's stored band is the frozen level's, 17 in R2 and 18
     in R4 and R5, computed apart from the rule (census_lib.band_value). The level is what BAND_N gives on every slot's
     level energies, and band_failures finds nothing.
  4. The reading beside it changes nothing. On N = 24 and 32 alone the rule reads C2a/R5 at 2 and T1/R4 at 64 Unresolved
     on the band above N = 24 and converged on the band above N = 16. On those records, with a synthetic top cutoff, the
     point classifies and the gate passes, and the reading beside it is kept in the record.
  5. The Krein-negative distance: at T4/R4 at 4, T1/R4 at 64 and T4/R4 at 64, each with a Krein-negative group, the
     recorded distance equals a direct computation on the stored summary, and it sits on the classification. A branch
     with no Krein-negative group, C2a, records None.
Arms, each of which must turn its claim red:
  A1. BAND_N set to 24 in a copy of census_lib.py: claim 3, by the band's test.
  A2. the reading beside it read in place of the scored one in census_lib.here: claim 4.
  A3. the Krein-negative distance omitted from census_lib.here: claim 5.
  A4. the left-out set taken as every group, in census_lib.krein_distance: claim 5, by the direct computation.
"""
import copy
import importlib.util
import math
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

out = []
A, B = lib.ARM_A, lib.ARM_B


def say(s=''):
    print(s, flush=True)
    out.append(s)


def case_of(row):
    return census.roundtrip(cs.serialize(row, dict(cs.CASES[row], points=lib.path_points(row), cutoffs=lib.cutoffs_of(row))))


def two(p24, p32, n_lo):
    return ck.reading([p24['summary'], p32['summary']], p32['eig'], p32['lam'], p32['record']['margin'], n_lo)


def synthetic(row, e):
    """A case output on Arm A's ladder, from M8.17's or M8.16.1's records at N = 24 and 32 alone: N = 40 a copy of 32,
    the rule read on the two, both identities kept. Not a reading: the records of claims 4's arms."""
    th = lib.theirs(row, ROOT)
    k = lib.key(e)
    p24, p32 = th['cutoffs']['24']['points'][k], th['cutoffs']['32']['points'][k]
    kept = dict(aligned_distance=0.0, same_record=True, kept=True)
    case = census.roundtrip(cs.serialize(row, dict(cs.CASES[row], cutoffs=[24, 32, 40])))
    return dict(case=case, cutoffs={'24': dict(points={k: p24}), '32': dict(points={k: p32}), '40': dict(points={k: p32})},
                readings={k: two(p24, p32, lib.BAND_N)}, beside={k: two(p24, p32, lib.BESIDE_N)},
                identity={k: {lib.pair_key(p): dict(kept) for p in A['pairs']}})


def direct(summary, reading):
    """The distance, by a loop of its own over the stored groups."""
    read = set()
    for r in reading['rows']:
        read.update(r.get('top', []))
    best = None
    for g in summary['groups']:
        if any(i in read for i in g['idx']):
            continue
        for h in summary['groups']:
            if h['cls'] == 'imag' and h['neg'] > 0:
                d = math.hypot(g['c'][0] - h['c'][0], g['c'][1] - h['c'][1])
                best = d if best is None or d < best else best
    return best


def mutant(src, anchor, new, tag, tmp):
    if src.count(anchor) != 1:
        raise SystemExit(f'the anchor for {tag} occurs {src.count(anchor)} times')
    p = os.path.join(tmp, f'census_lib_{tag}.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(src.replace(anchor, new, 1))
    spec = importlib.util.spec_from_file_location(f'census_lib_{tag}', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def claim1():
    n, bad = 0, []
    for row in lib.ROWS:
        th = lib.theirs(row, ROOT)
        for k, rd in th['readings'].items():
            pts = [th['cutoffs'][str(N)]['points'].get(k) for N in B['cutoffs']]
            scored, _ = census.rule(pts)
            n += 1
            bad += [f'{row} {k}: {d}' for d in lib.differences(census.roundtrip(scored), rd)]
    return n, bad


def claim2():
    bad, n = [], 0
    miss = census.rule([None, {}, {}])[0]
    ok = miss['verdict'] == 'Unresolved' and miss['reasons'] == ['a cutoff is missing']
    for row, es in lib.TWELVE.items():
        th = lib.theirs(row, ROOT)
        for e in es:
            n += 1
            h = lib.here(lib.at(th, e, A), case_of(row), A)
            if h['classified'] or 'untested at N = 40' not in h['causes']:
                bad.append(f'{row} {e:g}')
    return ok, n, bad


def claim3(L):
    """The band at every stored point, on L's level: (points, failures)."""
    n, bad = 0, []
    for row in lib.ROWS:
        th = lib.theirs(row, ROOT)
        slot = lib.SLOT[row]
        results = {row: dict(th, cutoffs=dict(th['cutoffs'], **{'40': th['cutoffs']['32']}))}
        cases = {row: dict(slot=slot)}
        for k, rd in th['readings'].items():
            n += 1
            lam = th['cutoffs']['32']['points'][k]['lam']
            if not L.band_ok(rd, slot, lam):
                bad.append(f'{row} {k}')
        bad += L.band_failures(results, {}, {}, cases)
        eig = th['cutoffs']['32']['points'][next(iter(th['readings']))]['eig']
        lvl = min(e for e in set(round(x, 6) for x in eig) if e > L.BAND_N * (L.BAND_N + 2) + 0.5)
        n1 = L.BAND_LEVEL[slot]
        if lvl != n1 * (n1 + 2):
            bad.append(f'{row}: BAND_N gives the level energy {lvl}, not level {n1}')
    return n, bad


def claim4(L):
    """(ok, detail): the two points classify, and the gate passes, on L."""
    res = []
    for row, e in (('C2a/R5', 2.0), ('T1/R4', 64.0)):
        o = synthetic(row, e)
        k = lib.key(e)
        sc, bs = o['readings'][k], o['beside'][k]
        if not (sc['verdict'] == 'converged' and bs['verdict'] == 'Unresolved'):
            return False, f'{row} at {e:g}: the records no longer split: {sc["verdict"]}, {bs["verdict"]}'
        c = L.here(L.at(o, e, A), o['case'], A)
        res.append(c['classified'])
        if row == 'C2a/R5':
            one = dict(o['case'], points=[dict(eps=e, read=True)])
            res.append(not L.control_failures(o, one))
        else:
            res.append(L._beside(o, e)['verdict'] == 'Unresolved')
    return all(res), res


def claim5(L):
    rows, bad = [], []
    for row, e in (('T4/R4', 4.0), ('T1/R4', 64.0), ('T4/R4', 64.0)):
        o = synthetic(row, e)
        k = lib.key(e)
        hi = o['cutoffs']['40']['points'][k]
        c = L.here(L.at(o, e, A), o['case'], A)
        got = (c.get('krein_distance') or {}).get('distance')
        want = direct(hi['summary'], o['readings'][k])
        rows.append(f'{row} at {e:g}: {got}')
        if got is None or want is None or abs(got - want) > 1e-12:
            bad.append(f'{row} at {e:g}: {got} against {want}')
    o = synthetic('C2a', 2.0)
    c = L.here(L.at(o, 2.0, A), o['case'], A)
    if not c['classified'] or c.get('krein_distance', 'absent') is not None:
        bad.append(f"C2a: {c.get('krein_distance', 'absent')}")
    return rows, bad


def main():
    devtools.require('seedcheck')
    say('Tests 2 and 3, the reader and the band, with no solve, in a seedcheck process.')
    fails = 0
    n, bad = claim1()
    say(f"1. {'PASS' if not bad else 'FAIL'}: census.rule reproduces M8.17's reading at {n} stored points of the five rows"
        + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += bool(bad)
    ok, n, bad = claim2()
    say(f"2. {'PASS' if ok and not bad else 'FAIL'}: a cutoff missing reads Unresolved; the {n} of the twelve, on M8.17's "
        f"records, each refuse: untested at N = 40" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += not ok or bool(bad)
    n, bad = claim3(lib)
    say(f"3. {'PASS' if not bad else 'FAIL'}: the stored band is the frozen level's at {n} points: level 17 in R2, 18 in R4 "
        f"and R5" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += bool(bad)
    ok, d = claim4(lib)
    say(f"4. {'PASS' if ok else 'FAIL'}: where the reading beside it is Unresolved and the scored one converged, the point "
        f"classifies and the gate passes: {d}")
    fails += not ok
    rows, bad = claim5(lib)
    say(f"5. {'PASS' if not bad else 'FAIL'}: the Krein-negative distance equals a direct computation: {rows}; C2a records "
        f"None" + ''.join(f'\n      {b}' for b in bad[:5]))
    fails += bool(bad)
    src = open(lib.__file__, encoding='utf-8').read()
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    arms = []
    try:
        m1 = mutant(src, 'BAND_N = 16 ', 'BAND_N = 24 ', 'a1', tmp)
        m1.BAND_LEVEL = dict(lib.BAND_LEVEL)
        arms.append(('A1. BAND_N set to 24: a level energy no longer the frozen level', bool(claim3(m1)[1])))
        m2 = mutant(src, "    rd = pt['reading']\n    if not rd:\n", "    rd = pt['beside'] or pt['reading']\n    if not rd:\n",
                    'a2', tmp)
        arms.append(('A2. the reading beside it read in place of the scored one', not claim4(m2)[0]))
        m3 = mutant(src, "    if lad['beside']:\n        out['krein_distance'] = krein_distance(hi['summary'], rd)\n", '',
                    'a3', tmp)
        arms.append(('A3. the Krein-negative distance omitted', bool(claim5(m3)[1])))
        m4 = mutant(src, "    left = [g for g in summary['groups'] if not set(g['idx']) & read]\n",
                    "    left = list(summary['groups'])\n", 'a4', tmp)
        arms.append(('A4. the left-out set taken as every group', bool(claim5(m4)[1])))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say('arms, each of which must turn its claim red:')
    for label, red in arms:
        say(f"   {label}: {'RED' if red else 'GREEN'}")
    fails += sum(not r for _, r in arms)
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_reader.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
