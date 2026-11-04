#!/usr/bin/env python3
"""Where solve_checks.out reports a stored point on a new path, is the difference in m the one the difference in the
amplitude reached gives along the branch? For each such point: the relative difference in m, against dm/deps times the
difference in eps_reached, over m. dm/deps is the central difference between the point's neighbours on each path, this
run's and the stored one, at the same cutoff. Both are computed from the full-precision solve fields, and again from
solve_checks.out's printed values. Solve fields alone; no spectrum.

Usage: slope_check.py OUT SCRIPTS_DIR SOLVE_CHECKS_OUT
"""
import json
import os
import re
import sys

RECORDS = dict(T5_R2='soft-slot-dynamics-m8-17', T5J_R2='soft-slot-dynamics-m8-16-1', C2a_R5='soft-slot-dynamics-m8-16-1')


def slope(points, k):
    """dm/deps at k by the central difference of its neighbours on the path, (m, eps) as stored."""
    ks = sorted(points, key=float)
    i = ks.index(k)
    a, b = ks[max(i - 1, 0)], ks[min(i + 1, len(ks) - 1)]
    return (points[b]['m'] - points[a]['m']) / (points[b]['eps_reached'] - points[a]['eps_reached']), a, b


def main():
    out, scripts, printed = sys.argv[1:4]
    rows = {}
    for line in open(printed, encoding='utf-8'):
        tag, N = re.match(r'(\S+) N = (\d+):', line).groups() if re.match(r'(\S+) N = (\d+):', line) else (None, None)
        for k, m, e in re.findall(r'([0-9.]+): new path, m differs by ([0-9.e+-]+), eps_reached by ([0-9.e+-]+)', line):
            rows.setdefault((tag, int(N)), []).append((k, float(m), float(e)))
    worst = 0.0
    for (tag, N), pts in rows.items():
        mine = json.load(open(os.path.join(out, f'{tag}_N{N}.json'), encoding='utf-8'))['points']
        theirs = json.load(open(os.path.join(scripts, RECORDS[tag], 'run', 'out', tag + '.json'),
                                encoding='utf-8'))['cutoffs'][str(N)]['points']
        for k, dm_p, de_p in pts:
            a, b = mine[k], theirs[k]
            dm, de = (a['m'] - b['m']) / b['m'], a['eps_reached'] - b['eps_reached']
            s_mine, lo, hi = slope(mine, k)
            s_theirs, slo, shi = slope(theirs, k)
            full = s_mine * de / b['m']
            from_printed = s_mine * de_p / b['m']
            worst = max(worst, abs(from_printed / dm_p - 1))
            print(f'{tag} N = {N} at {k}: dm/m {dm:+.4e}, deps {de:+.4e}; dm/deps {s_mine:.5f} on this path ({lo} to {hi}), '
                  f'{s_theirs:.5f} on the stored one ({slo} to {shi}); dm/deps x deps / m {full:+.4e}, ratio {full / dm:.4f}; '
                  f'from the printed values {from_printed:.3e} against {dm_p:.3e}, ratio {from_printed / dm_p:.3f}')
    print(f'largest departure from the printed values: {100 * worst:.1f}%')


if __name__ == '__main__':
    main()
