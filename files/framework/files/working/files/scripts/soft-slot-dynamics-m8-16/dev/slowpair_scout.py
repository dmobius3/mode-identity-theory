#!/usr/bin/env python3
"""The slow-pair scout: what today's record (the section 7 calibration, L's inertia cut at 1e-10 ||L|| with a gray zone
to 1e-7 ||L||) does with a genuine slow pair near zero, at N = 40's scale. Case: synthetic. Reported, unscored: it informs
SLOWPAIR_PLAN.md, and nothing is calibrated on it.

The systems are dl_recal.py's Elliptic family (the phase chains diag(0, 5) and diag(0, -2), Krein-positive oscillators up
to 1,700, so ||A|| is about 1,700), at omega = 7 and 14, the controls' range at N = 40, with one slow-pair block added.
For a block diag(l1, l2) with the frame's 2 omega J0, the slow pair solves s^4 + (4 omega^2 + l1 + l2) s^2 + l1 l2 = 0,
and its small L eigenvalue k1 is set from the exact quartic so the pair sits at s:
  S1, soft-soft, imaginary, Krein-positive: diag(k1, k1), k1 = s^2 + 2 omega s, about 2 omega s;
  S2, near a crossing, imaginary, Krein-positive: diag(k1, K), K = 1, k1 about 4 omega^2 s^2 / K;
  S3, near a crossing, imaginary, Krein-negative: diag(-k1, -K);
  S4, near a crossing, real: diag(-k1, K).
At s = 1e-5 and 5e-6 (below section 7's 1.04e-5) and 3e-5, at m = 0.2 (A's floor about 1.7e-6), over 5 mixings each.
Each case reports the pair's L eigenvalue against ||L||, the readings over the mixings (type, the pair's label and
Krein group, n(L), n(D), K, the unresolved items), and the leak against its bound.
"""
import os
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import dl_recal as d  # noqa: E402

devtools.require('synthetic')
d.rng = np.random.default_rng(20261017)
out = []
EXPECT = {'S1': ('Elliptic', (1, 1, 0)), 'S2': ('Elliptic', (1, 1, 0)), 'S3': ('Elliptic', (3, 1, 2)),
          'S4': ('Hyperbolic', (2, 1, 1))}


def say(s=''):
    print(s, flush=True)
    out.append(s)


def k1_for(s, omega, K, kind):
    """The small L eigenvalue that puts the block's slow pair at s, from the exact quartic."""
    if kind == 'S1':
        return s * s + 2 * omega * s
    if kind in ('S2', 'S3'):
        x, sg = -s * s, (1 if kind == 'S2' else -1)
        return -(x * x + (4 * omega ** 2 + sg * K) * x) / (sg * x + K)
    x = s * s
    return (x * x + (4 * omega ** 2 + K) * x) / (x + K)


def block(kind, k1, K=1.0):
    return {'S1': np.diag([k1, k1]), 'S2': np.diag([k1, K]), 'S3': np.diag([-k1, -K]), 'S4': np.diag([-k1, K])}[kind]


def main():
    say("The slow-pair scout under today's record (reported, unscored). Derived, for a resolved reading: S1 and S2"
        " Elliptic (1, 1, 0); S3 Elliptic (3, 1, 2) with k_i^- = 1; S4 Hyperbolic (2, 1, 1) with k_r = 1.")
    tally = {}
    for omega in (7.0, 14.0):
        for kind in ('S1', 'S2', 'S3', 'S4'):
            for s in (1e-5, 5e-6, 3e-5):
                k1 = k1_for(s, omega, 1.0, kind)
                reads, leaks = [], []
                for _ in range(5):
                    A, B, W, L, sym = d.system(d.elliptic_blocks([block(kind, k1)]), omega)
                    r = d.rec(A, B, W, L, 0.2, sym)
                    resolved = (r['type'], d.counts(r)) == EXPECT[kind] and r['balance'] and not r['unresolved']
                    wrong = r['type'] not in ('Unresolved', EXPECT[kind][0])
                    reads.append(('RESOLVED' if resolved else ('WRONG TYPE' if wrong else r['type'])) +
                                 ('' if resolved else ' ' + str(sorted({u.split(':')[0] for u in r['unresolved']}))))
                    leaks.append(r['symmetry_leak'] / r['leak_bound'] if r['leak_bound'] else np.nan)
                    tally[(kind, s, omega)] = tally.get((kind, s, omega), 0) + resolved
                k_rel = k1 / np.linalg.norm(L, 2)
                summary = {x: reads.count(x) for x in sorted(set(reads))}
                say(f"omega {omega:4.0f} {kind} s {s:.0e}: L eigenvalue {k1:.2e} = {k_rel:.1e} ||L||; leak / bound"
                    f" {np.nanmin(leaks):.1e} to {np.nanmax(leaks):.1e}; {summary}")
    wrong = sum(1 for x in out if 'WRONG TYPE' in x)
    say(f"Lines with a wrong type: {wrong}. Resolved, of 5 mixings, at s below 1.04e-5: "
        + '; '.join(f"{k} {sum(v for (kk, s, w), v in tally.items() if kk == k and s < 1.04e-5)} of 20" for k in ('S1', 'S2', 'S3', 'S4')))
    path = os.path.join(HERE, 'slowpair_scout.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     ["The slow-pair scout: reported, unscored, under today's record; it informs SLOWPAIR_PLAN.md.",
                      f'Lines with a wrong type: {wrong}.'], outputs=(path,))


if __name__ == '__main__':
    main()
