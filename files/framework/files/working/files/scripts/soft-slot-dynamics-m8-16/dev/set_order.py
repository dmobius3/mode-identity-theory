#!/usr/bin/env python3
"""The separation rule read in any order of the groups (DEVLOG 219). Cases: C2a, C2b, C2a/R5.

Usage: set_order.py CONTROL

convergence.separation is applied to the saved summaries of every reading of CONTROL that carries them, with each
point's band edge as the driver read it: C2a's development sample and ladders and the dry run's points; C2b's ladders;
the R5 control's sample. Nothing is solved. Each reading is read in its stored order, then with every cutoff's groups
shuffled, SHUFFLES times from a fixed seed, under the rule and under the arm 'one_way_set' (the sets as built before
DEVLOG 218).

Claims, derived before the run from DEVLOG 218's diagnosis and checked first by DEVLOG 219's unlogged preview:
  1. Under the rule, no reading's verdict or type changes under any shuffle.
  2. C2a only, the arm's failing side: at eps = 2, in each of the three readings that carry it (the sample, the ladders
     and the dry run), the two tested groups near 4.039i at the highest cutoff have closures that differ, one inside
     the other. Exchanging their stored positions changes the arm's verdict and leaves the rule's unchanged; and the
     shuffles change the arm's verdict.
  3. C2a only: the dry run's eps = 2 in stored order reads converged, Elliptic, under the rule, its set near 4.039i
     counting 2 at every cutoff; under the arm it reads Unresolved, as DEVLOG 218 shipped it.
Reported, unscored: how many readings the shuffles turn under the arm, and the largest set the rule forms.
"""
import glob
import json
import os
import random
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import convergence as cv, devtools  # noqa: E402

SHUFFLES = 24
ARM = ('one_way_set',)
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def latest(pattern):
    paths = sorted(glob.glob(os.path.join(HERE, 'runs', pattern)))
    return paths[-1] if paths else None


def readings(name):
    """(source, eps, summaries lowest cutoff first, band) for every saved reading of the control that carries summaries."""
    found = []
    if name in ('C2a', 'C2b'):
        runs = {}
        for path in sorted(glob.glob(os.path.join(HERE, 'runs', f'*_sep_controls_{name}_*.json'))):
            J = json.load(open(path, encoding='utf-8'))
            if any(k.startswith('N') and 'summary' in v for k, v in J.items()):
                runs[path.rsplit('_', 1)[1][:-5]] = (path, J)
        for mode, (path, J) in sorted(runs.items()):
            Ns = sorted({int(k[1:].split('_')[0]) for k in J if k.startswith('N')})
            for e in sorted((k[len('rule_eps'):] for k in J if k.startswith('rule_eps')), key=float):
                top = J[f'N{Ns[-1]}_eps{e}']
                found.append((os.path.basename(path), float(e), [J[f'N{N}_eps{e}']['summary'] for N in Ns],
                              cv.band_edge(top['eig'], Ns[0], top['lam'])))
    if name == 'C2a':
        path = os.path.join(HERE, 'runs', f'{218:03d}_dry_C2a.json')     # entry 218's, not the newest (DEVLOG 253)
        J = json.load(open(path, encoding='utf-8'))
        Ns = sorted(J['cutoffs'], key=int)
        for e in sorted(J['readings'], key=float):
            found.append((os.path.basename(path), float(e), [J['cutoffs'][N]['points'][e]['summary'] for N in Ns],
                          J['readings'][e]['band']))
    if name == 'C2a/R5':
        path = latest('*_r5_control.json')
        J = json.load(open(path, encoding='utf-8'))
        Ns = sorted({int(k[1:].split('_')[0]) for k in J if k.startswith('N')})
        for k in sorted((k for k in J if k.startswith('rule_eps')), key=lambda k: float(k[len('rule_eps'):])):
            e = k[len('rule_eps'):]
            found.append((os.path.basename(path), float(e), [J[f'N{N}_eps{e}']['summary'] for N in Ns], J[k]['band']))
    return found


def vt(r):
    return r['verdict'], r['type']


def shuffled(sums, rng):
    perm = []
    for s in sums:
        g = list(s['groups'])
        rng.shuffle(g)
        perm.append(dict(s, groups=g))
    return perm


def tested(sums, band):
    G = sums[-1]['groups']
    return [i for i, g in enumerate(G) if band is None or abs(cv._c(g)) < band / 2 or g['cls'] != 'imag' or g['neg']]


def the_pair(sums, band):
    """The two tested groups nearest 4.039i at the highest cutoff, and whether their closures differ, one inside the
    other."""
    levels = [s['groups'] for s in reversed(sums[-3:])]
    T = sorted(tested(sums, band), key=lambda i: abs(cv._c(levels[0][i]) - 4.039j))[:2]
    A, B = (cv.closure(levels, i) for i in T)
    inside = all(a <= b for a, b in zip(A, B)) or all(b <= a for a, b in zip(A, B))
    return T, A != B and inside, [len(x) for x in A], [len(x) for x in B]


def swapped(sums, i, j):
    g = list(sums[-1]['groups'])
    g[i], g[j] = g[j], g[i]
    return sums[:-1] + [dict(sums[-1], groups=g)]


def main():
    name = sys.argv[1]
    assert name in ('C2a', 'C2b', 'C2a/R5')
    devtools.require(name)
    rng = random.Random(20261018)
    R = readings(name)
    say(f"The separation rule read in any order of the groups, on {name}'s saved summaries: {len(R)} readings,"
        f" {SHUFFLES} shuffles each.")
    failed, turned_rule, turned_arm, largest = 0, [], [], 0
    for src, e, sums, band in R:
        base, arm = cv.separation(sums, band=band), cv.separation(sums, band=band, arms=ARM)
        largest = max([largest] + [r['count'] for r in base['rows'] if r.get('kind') == 'set'])
        rule_turns = arm_turns = 0
        for _ in range(SHUFFLES):
            perm = shuffled(sums, rng)
            rule_turns += vt(cv.separation(perm, band=band)) != vt(base)
            arm_turns += vt(cv.separation(perm, band=band, arms=ARM)) != vt(arm)
        if rule_turns:
            turned_rule.append((src, e))
        if arm_turns:
            turned_arm.append((src, e))
        say(f"   {src} eps {e:g}: the rule {base['verdict']} {base['type'] or ''}, turned by {rule_turns} of {SHUFFLES};"
            f" the arm {arm['verdict']} {arm['type'] or ''}, turned by {arm_turns}")
    ok1 = not turned_rule and len(R) > 0
    failed += not ok1
    say(f"1. {'PASS' if ok1 else 'FAIL'}: under the rule, {len(R) - len(turned_rule)} of {len(R)} readings keep their"
        f" verdict under every shuffle{'' if ok1 else '; turned: ' + str(turned_rule)}")
    if name == 'C2a':
        at2 = [(src, sums, band) for src, e, sums, band in R if e == 2.0]
        ok2 = len(at2) == 3
        for src, sums, band in at2:
            (i, j), nested, nA, nB = the_pair(sums, band)
            G = sums[-1]['groups']
            sw = swapped(sums, i, j)
            arm0, arm1 = vt(cv.separation(sums, band=band, arms=ARM)), vt(cv.separation(sw, band=band, arms=ARM))
            rul0, rul1 = vt(cv.separation(sums, band=band)), vt(cv.separation(sw, band=band))
            good = nested and arm0 != arm1 and rul0 == rul1 and (src, 2.0) in turned_arm
            ok2 = ok2 and good
            say(f"   {src}: the pair {cv._c(G[i]).imag:.6f}i and {cv._c(G[j]).imag:.6f}i at positions {i} and {j},"
                f" closures {nA} and {nB} ({'nested and different' if nested else 'NOT nested and different'}); the arm"
                f" {arm0[0]} stored, {arm1[0]} swapped; the rule {rul0[0]} both ways")
        failed += not ok2
        say(f"2. {'PASS' if ok2 else 'FAIL'}: the arm's failing side, at eps = 2 in {len(at2)} readings: the swap turns the arm"
            f" and not the rule, and the shuffles turn the arm")
        src, e, sums, band = [x for x in R if x[0].endswith('_dry_C2a.json') and x[1] == 2.0][0]
        rule, arm = cv.separation(sums, band=band), cv.separation(sums, band=band, arms=ARM)
        near = [r for r in rule['rows'] if r.get('kind') == 'set' and abs(cv.row_centre(r) - 4.039j) < 1e-2]
        count = near[0]['count'] if len(near) == 1 and near[0]['ok'] else None
        ok3 = vt(rule) == ('converged', 'Elliptic') and count == 2 and arm['verdict'] == 'Unresolved'
        failed += not ok3
        say(f"3. {'PASS' if ok3 else 'FAIL'}: the dry run's eps = 2 ({src}), stored order: the rule {rule['verdict']}"
            f" {rule['type'] or ''}, its set near 4.039i counting {count} at every cutoff (a set whose count differs"
            f" does not pass); the arm {arm['verdict']} ({arm['reasons'][:1]})")
    say(f"Reported, unscored: the shuffles turn {len(turned_arm)} of {len(R)} readings under the arm"
        f"{': ' + ', '.join(f'{s} eps {e:g}' for s, e in turned_arm) if turned_arm else ''}; the largest set the rule"
        f" forms counts {largest} at the highest cutoff.")
    say(f"{failed} failed")
    path = os.path.join(HERE, f"set_order_{name.replace('/', '_')}.out")
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), name,
                     [f"The separation rule read in any order of the groups, on {name}'s saved summaries:"
                      f" {'PASS' if not failed else 'FAIL'} ({failed} failed), {len(R)} readings, {SHUFFLES} shuffles each."
                      f" Under the arm, the shuffles turn {len(turned_arm)}. No solve.",
                      'Each claim derived before the run (the script\'s docstring).'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
