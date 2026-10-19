#!/usr/bin/env python3
"""Post-run, unscored: made after M8.16's registered run, and not a record from it. The pyramid's slow eigenvalues,
extrapolated to zero amplitude, against Theorem R's leading order.

Usage, from this folder: python3 -I -B tools/p5_extrapolation.py
It writes tools/p5_extrapolation.out.

Theorem R(a), in the Soft-Slot Branches, gives the slow eigenvalues as eps (kappa s tau + o(1)) for small eps, in the
terms' notation, and says nothing of the o(1) term's size at a finite eps. The terms' bar, 5% at eps = 0.25, is the
terms' own. This script reads run/out/P5.json alone, with no solve, after checking it against the SHA-256 the run's log
recorded. At each cutoff, each slow group that the pinned checks.leading matches at eps = 0.25, 0.5, 1 and 2 is divided
by eps, and the quotient is extrapolated to eps -> 0 by Richardson's rule: from 0.25 and 0.5, removing the first order,
2 f(0.25) - f(0.5); and from 0.25, 0.5 and 1, removing the second, (8 f(0.25) - 6 f(0.5) + f(1)) / 3. Each is printed
as its distance from Theorem R's kappa s tau, relative. Nothing here changes the run's verdict."""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import checks as ck  # noqa: E402

EPS = (0.25, 0.5, 1.0, 2.0)
NAMES = {('imag', -1): 'the in-span pair, imaginary and Krein-negative',
         ('complex', None): 'the quartet',
         ('imag', 1): 'the Krein-positive pair'}
out = []


def say(s=''):
    print(s)
    out.append(s)


def main():
    path = os.path.join(ROOT, 'run', 'out', 'P5.json')
    with open(path, 'rb') as f:
        raw = f.read()
    with open(os.path.join(ROOT, 'run', 'out', 'RUNLOG.json'), encoding='utf-8') as f:
        logged = json.load(f)['completed']['P5']['files']['P5.json']
    if hashlib.sha256(raw).hexdigest() != logged:
        raise SystemExit('run/out/P5.json differs from the SHA-256 the run log recorded')
    p5 = json.loads(raw.decode('utf-8'))
    case = p5['case']
    say('Post-run, unscored: made after M8.16\'s registered run, from run/out/P5.json alone, with no solve. '
        'Not a record from the run.')
    say(f'run/out/P5.json: SHA-256 {logged}, equal to the run log\'s record of it.')
    say('Each slow group as the pinned checks.leading matches it; lambda/eps against Theorem R\'s kappa s tau, '
        'as a relative distance.')
    for N in sorted(p5['cutoffs'], key=int):
        f, pred = {}, {}
        for e in EPS:
            _, _, rows = ck.leading(p5['cutoffs'][N]['points'][ck.key(e)], case, e)
            for cls, sign, p, c, dev in rows:
                f.setdefault((cls, sign), {})[e] = complex(c) / e
                pred[(cls, sign)] = complex(p) / e
        say()
        say(f'N = {N}')
        for k in NAMES:
            fe, s = f[k], pred[k]

            def rel(z):
                return abs(z - s) / abs(s)
            lin = 2 * fe[0.25] - fe[0.5]
            quad = (8 * fe[0.25] - 6 * fe[0.5] + fe[1.0]) / 3
            say(f'  {NAMES[k]}: at eps = ' + ', '.join(f'{e:g}: {100 * rel(fe[e]):.2f}%' for e in EPS))
            say(f'      extrapolated to eps -> 0: first order removed {100 * rel(lin):.3f}%; '
                f'second order removed {100 * rel(quad):.4f}%')
    with open(os.path.join(HERE, 'p5_extrapolation.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()
