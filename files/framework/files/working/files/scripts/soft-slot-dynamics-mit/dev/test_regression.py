#!/usr/bin/env python3
"""The regression on every stored reading (DESIGN.md): a check, and no evidence, since every one of them was known when the
changes were chosen. Nothing is solved.

Over the 262 published readings, M8.18's 24, M8.16.1's 123 and M8.17's 115: this tree's rule as built must give each
stored reading field for field. A stored summary keeps no linked group's members, so A acts on nothing here, and the
changed reading must move exactly one verdict, C3R/R4 at 0.25 by B, and no reason elsewhere. B's flag is not stored, so
the one record holding n(D)'s line is lifted on the fact that D's eigenvalue there, -0.01596075, lies far above B's top
(dev/runs/019_gate_cause in M8.18's folder; the reread reads the flag itself).

A is tested on P5's stored record at 0.25 with its pair's gap at each cutoff set by TABLE, linked or apart, and the
members given: each case must read as TABLE says. dev/test_end_to_end.py tests it on the members of real reads. Each arm
must turn this file red for its named reason.

Usage: test_regression.py SCRIPTS_DIR
"""
import contextlib
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
EXPECTED = {('M8.18 controls', 'C3R_R4', '0.25')}
# (what, the pair's gap at N = 24, 32 and 40, each linked or apart, the verdict as built, the verdict under A)
TABLE = (('stable, as stored', (1.1345e-5, 1.1345e-5, ('L', 1.1345e-5)), 'Unresolved', 'converged'),
         ('closing inside tau(40)', (1.2e-5, 1.0e-5, ('L', 8e-6)), 'Unresolved', 'Unresolved'),
         ('closing inside tau(40), slower', (1.15e-5, 1.0e-5, ('L', 8.5e-6)), 'Unresolved', 'Unresolved'),
         ('closing, its change falling', (1.2e-5, 1.0e-5, ('L', 9.8e-6)), 'Unresolved', 'converged'),
         ('opening, linked at N = 24', (('L', 6e-6), 1.0e-5, 1.4e-5), 'converged', 'Unresolved'),
         ('closing fast', (3e-5, 1.0e-5, ('L', 5e-6)), 'converged', 'converged'),
         ('linked at N = 32 and 40, stable', (8.78e-6, ('L', 8.78e-6), ('L', 8.78e-6)), 'converged', 'converged'))


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


def pair(s):
    return sorted((x for x in s['groups'] if abs(complex(*x['c']).imag - 4.02029) < 1e-5), key=lambda x: x['c'][1])


def with_pair(sums, gaps):
    """P5's summaries with its pair at the given gaps: a number, two groups; ('L', gap), one group of two, with its members,
    about the pair's stored centre."""
    s2 = copy.deepcopy(sums)
    mid = sum(g['c'][1] for g in pair(sums[0])) / 2
    for s, gap in zip(s2, gaps):
        gs = pair(s)
        if isinstance(gap, tuple):
            if len(gs) == 2:
                s['groups'].remove(gs[1])
            g = gs[0]
            g.update(size=2, members=[[0.0, mid - gap[1] / 2], [0.0, mid + gap[1] / 2]])
            g['c'][1] = mid
        else:
            if len(gs) == 1:
                h = copy.deepcopy(gs[0])
                s['groups'].append(h)
                gs = [gs[0], h]
            for g, sign in zip(gs, (-1, 1)):
                g['size'] = 1
                g.pop('members', None)
                g['c'][1] = mid + sign * gap / 2
    return s2


def table(records):
    """TABLE's verdicts, as failures."""
    label, name, e, sums, eig, lam, marg, rd = p5(records)
    fails = []
    for what, gaps, built, under in TABLE:
        s2 = with_pair(sums, gaps)
        got = (ck.reading(s2, eig, lam, marg, N_LO)['verdict'], changed.reading(s2, [True] * 3, eig, lam, marg, N_LO)['verdict'])
        print(f'  {what}: {gaps}: as built {got[0]}, under A {got[1]}', flush=True)
        if got != (built, under):
            fails.append(f'{what}: as built {got[0]}, under A {got[1]}, not {built}, {under}')
    return fails


def quiet(f, *a):
    with open(os.devnull, 'w') as null, contextlib.redirect_stdout(null):
        return f(*a)


def main():
    records = load(sys.argv[1])
    print(f'{len(records)} readings', flush=True)
    fails, moved = check(records)
    print(f'as built reproduces all {len(records)}, field for field; changed moves {sorted(moved)}' if not fails else fails)
    ok = not fails
    print(f"A on P5's pair, its gap set at each cutoff, {len(TABLE)} cases:", flush=True)
    bad = table(records)
    print(bad if bad else 'each reads as stated', flush=True)
    ok &= not bad

    # the arms: each mutation must turn the check red for its own reason
    arms = 0
    sep, own, lift, factor = cv.separation, cv._members, changed.lifted, cv.FACTOR

    def expect(name, reason, got):
        nonlocal arms, ok
        red = reason in ' '.join(got)
        print(f"arm {name}: {'red for its reason' if red else 'NOT RED AS NAMED'}: {got[:1]}", flush=True)
        arms += red
        ok &= red

    cv.separation = lambda sums, band=None, arms=(): sep(sums, band=band)
    expect('A removed', 'stable, as stored: as built Unresolved, under A Unresolved', quiet(table, records))
    cv.separation = sep
    cv._members = lambda g: [cv._c(g)] * g['size']
    expect('the members ignored', 'stable, as stored: as built Unresolved, under A Unresolved', quiet(table, records))
    cv._members = own
    changed.lifted = lambda s, f: s
    expect('B removed', 'the changed reading moves []', check(records)[0])
    changed.lifted = lift
    cv.FACTOR = 0.001
    expect('the rule moved as built', 'as built,', check(records)[0])
    cv.FACTOR = factor
    cv.separation = lambda sums, band=None, arms=(): sep(sums, band=band, arms=tuple(arms) + ('set_centroid',))
    expect('a set read at its centroid', 'closing inside tau(40): as built converged, under A converged', quiet(table, records))
    cv.separation = sep
    print(f'{arms} of 5 arms red for their reasons')
    print('PASS' if ok and arms == 5 else 'FAIL')
    raise SystemExit(0 if ok and arms == 5 else 1)


if __name__ == '__main__':
    main()
