#!/usr/bin/env python3
"""T5's quartet at 128 and 132, its real part at full digits: M8.17's stored values at N = 16, 24 and 32 beside this
run's at N = 24, 32 and 40, and the steps between them. Written for the review of the readings, which took the steps
from rounded values. Nothing is solved or read again.

Usage: quartet_steps.py OUT SCRIPTS_DIR
"""
import json
import os
import sys


def real_part(d, N, e):
    pts = d['cutoffs'][str(N)]['points']
    k = [x for x in pts if abs(float(x) - e) < 1e-9][0]
    return [g['c'][0] for g in pts[k]['summary']['groups'] if g['cls'] == 'complex'][0]


def main():
    out, scripts = sys.argv[1:3]
    with open(os.path.join(out, 'T5_R2.json'), encoding='utf-8') as f:
        mine = json.load(f)
    with open(os.path.join(scripts, 'soft-slot-dynamics-m8-17', 'run', 'out', 'T5_R2.json'), encoding='utf-8') as f:
        stored = json.load(f)
    for e in (128, 132):
        s = {N: real_part(stored, N, e) for N in (16, 24, 32)}
        m = {N: real_part(mine, N, e) for N in (24, 32, 40)}
        print(f'{e}: stored at N = 16, 24, 32: ' + ', '.join(f'{v:.10f}' for v in s.values())
              + '; this run at N = 24, 32, 40: ' + ', '.join(f'{v:.10f}' for v in m.values()))
        print(f'  steps: 16 to 24 {s[16] - s[24]:.6f}, 24 to 32 {s[24] - s[32]:.6f} (stored) and {m[24] - m[32]:.6f} '
              f'(this run), 32 to 40 {m[32] - m[40]:.6f}; the stored and this run\'s N = 32 differ by '
              f'{abs(s[32] - m[32]):.2e}')


if __name__ == '__main__':
    main()
