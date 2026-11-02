#!/usr/bin/env python3
"""The regression on every stored reading (DESIGN.md): a check, and no evidence, since every one of them was known when the
changes were chosen. Nothing is solved.

Over the 262 published readings, M8.18's 24, M8.16.1's 123 and M8.17's 115: this tree's rule as built must give each
stored reading field for field, and the changed reading must move exactly three verdicts, C3R/R4 and P5 at 0.25 on
M8.18's ladder and T5J at 0.25 on M8.16.1's, and no reason elsewhere. B's flag is not stored, so the one record holding
n(D)'s line is lifted on the fact that D's eigenvalue there, -0.01596075, lies far above B's top (dev/runs/019_gate_cause
in M8.18's folder; the reread reads the flag itself). Each arm must turn it red for its named reason.

Usage: test_regression.py SCRIPTS_DIR
"""
import copy
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import convergence as cv  # noqa: E402
import checks as ck  # noqa: E402
import census  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402

N_LO = 16
SETS = (('M8.18 controls', 'soft-slot-dynamics-m8-18/run/out', 24), ('M8.16.1', 'soft-slot-dynamics-m8-16-1/run/out', 123),
        ('M8.17 rows', 'soft-slot-dynamics-m8-17/run/out', 115))
EXPECTED = {('M8.18 controls', 'C3R_R4', '0.25'), ('M8.18 controls', 'P5', '0.25'), ('M8.16.1', 'T5J_R2', '0.25')}


def load(scripts):
    """Every stored reading: (set, case, key, summaries, eig, lam, margin, stored reading)."""
    out = []
    for label, rel, want in SETS:
        n = 0
        for f in sorted(glob.glob(os.path.join(scripts, rel, '*.json'))):
            with open(f, encoding='utf-8') as fh:
                d = json.load(fh)
            if 'readings' not in d or 'cutoffs' not in d:
                continue
            if label == 'M8.17 rows' and not os.path.basename(f).startswith('T'):
                continue
            cuts = sorted(d['cutoffs'], key=int)
            for e, rd in d['readings'].items():
                pts = [d['cutoffs'][N]['points'].get(e) for N in cuts]
                if not rd or not all(q and 'summary' in q for q in pts):
                    continue
                hi = pts[-1]
                out.append((label, os.path.basename(f)[:-5], e, [q['summary'] for q in pts], hi['eig'], hi['lam'],
                            hi['record']['margin'], rd))
                n += 1
        if n != want:
            raise SystemExit(f'{label}: {n} readings, not {want}')
    return out


def check(records):
    """(failures, moved): whatever departs from the as-built reading, and what the changed reading moves."""
    fails, moved, reasons_moved = [], set(), []
    for label, name, e, sums, eig, lam, marg, rd in records:
        new = census.roundtrip(ck.reading(sums, eig, lam, marg, N_LO))
        d = lib.differences(new, rd, ignore=frozenset())
        if d:
            fails.append(f'as built, {label} {name} {e}: {d[0]}')
        ch = changed.reading(sums, [True] * len(sums), eig, lam, marg, N_LO)
        if ch['verdict'] != rd['verdict']:
            moved.add((label, name, e))
        elif ch['reasons'] != rd['reasons']:
            reasons_moved.append((label, name, e))
    if moved != EXPECTED:
        fails.append(f'the changed reading moves {sorted(moved)}')
    if reasons_moved:
        fails.append(f'reasons moved with no verdict moved: {reasons_moved[:3]}')
    return fails, moved


def p5(records):
    return next(r for r in records if r[:3] == ('M8.18 controls', 'P5', '0.25'))


def motion_caught(records, shift=3e-6):
    """A motion of the merged group at N = 40 alone is real, and A must still read it Unresolved."""
    label, name, e, sums, eig, lam, marg, rd = p5(records)
    s2 = copy.deepcopy(sums)
    g = [x for x in s2[-1]['groups'] if x['size'] == 2 and abs(complex(*x['c']).imag - 4.02029) < 1e-5][0]
    g['c'][1] += shift
    return changed.reading(s2, [True] * 3, eig, lam, marg, N_LO)['verdict'] == 'Unresolved'


def closing_caught(records):
    """A pair really closing, 4e-5 apart at N = 24 and 3e-5 at N = 32, both wider than tau(40), and one group at N = 40:
    the links A forgives are the top cutoff's only, so A must read this Unresolved. A centroid would pass it, which is why
    the rule's arm 'set_centroid' is a mutation and A is not that arm."""
    label, name, e, sums, eig, lam, marg, rd = p5(records)
    s2 = copy.deepcopy(sums)
    for lev, gap in ((0, 4e-5), (1, 3e-5)):
        g = sorted((x for x in s2[lev]['groups'] if abs(complex(*x['c']).imag - 4.02029) < 1e-5), key=lambda x: x['c'][1])
        mid = (g[0]['c'][1] + g[1]['c'][1]) / 2
        g[0]['c'][1], g[1]['c'][1] = mid - gap / 2, mid + gap / 2
    return changed.reading(s2, [True] * 3, eig, lam, marg, N_LO)['verdict'] == 'Unresolved'


def main():
    records = load(sys.argv[1])
    print(f'{len(records)} readings', flush=True)
    fails, moved = check(records)
    print(f'as built reproduces all {len(records)}, field for field; changed moves {sorted(moved)}' if not fails else fails)
    ok = not fails
    good = motion_caught(records)
    print(f'a motion of 3e-6 at N = 40 alone stays Unresolved under A: {good}', flush=True)
    ok &= good
    good = closing_caught(records)
    print(f'a pair really closing stays Unresolved under A: {good}', flush=True)
    ok &= good

    # the arms: each mutation must turn the check red for its own reason
    arms = 0
    sep, blur, lift, factor = cv.separation, cv._blur, changed.lifted, cv.FACTOR

    def expect(name, reason, got):
        nonlocal arms, ok
        red = reason in ' '.join(got)
        print(f"arm {name}: {'red for its reason' if red else 'NOT RED AS NAMED'}: {got[:1]}", flush=True)
        arms += red
        ok &= red

    cv.separation = lambda sums, band=None, arms=(): sep(sums, band=band)
    expect('A removed', "the changed reading moves [('M8.18 controls', 'C3R_R4', '0.25')]", check(records)[0])
    cv.separation = sep
    cv._blur = lambda p, hi: p
    expect('the blur made a no-op', "the changed reading moves [('M8.18 controls', 'C3R_R4', '0.25')]", check(records)[0])
    cv._blur = blur
    changed.lifted = lambda s, f: s
    expect('B removed', "the changed reading moves [('M8.16.1', 'T5J_R2', '0.25'), ('M8.18 controls', 'P5', '0.25')]",
           check(records)[0])
    changed.lifted = lift
    cv.FACTOR = 0.001
    expect('the rule moved as built', 'as built,', check(records)[0])
    cv.FACTOR = factor
    cv._blur = lambda p, hi: [sum(p) / len(p)] * len(p)
    res = closing_caught(records)
    print(f"arm the blur as a centroid: the closing pair {'still caught' if res else 'missed, red for its reason'}", flush=True)
    cv._blur = blur
    arms += not res
    ok &= not res
    print(f'{arms} of 5 arms red for their reasons')
    print('PASS' if ok and arms == 5 else 'FAIL')
    raise SystemExit(0 if ok and arms == 5 else 1)


if __name__ == '__main__':
    main()
