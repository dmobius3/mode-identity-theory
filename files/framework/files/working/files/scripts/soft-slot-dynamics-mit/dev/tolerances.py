#!/usr/bin/env python3
"""Each tolerance that grows with the cutoff, at N = 40 and 48, against what the stored readings at N = 32 hold: the lesson
of #692 (OpenWave's review standards, D12), for every point this computation reads that has a record. Nothing is solved
or read, and every value is a stored known outcome. What it prints is a forecast of where the as-built reading can fail
on a tolerance alone, stated before any solve:

  tau: imaginary neighbours in the tested set at N = 32 whose gap lies under tau(40) or tau(48) and over tau(32), so that
       they merge at the new cutoff alone. Candidate A reads these by their eigenvalues.
  gap: the smallest other gap, over tau(40).
  A0:  the smallest eigenvalue of A outside the cluster, over the top of its gray zone at N = 40 (K1's separation).
  L:   L's smallest genuine eigenvalue, over the top of L's gray zone at N = 40.

D's eigenvalues are not stored at any row, so n(D)'s zone cannot be forecast here: the reads store them. ||A|| and ||L|| at
a new cutoff are the N = 32 value plus the difference of N (N + 2), which M8.18's controls show to 0.01%.

Usage: tolerances.py SCRIPTS_DIR
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import linear as ln  # noqa: E402
import census_lib as lib  # noqa: E402

U = ln.U
FILES = (('T1_R4', 'soft-slot-dynamics-m8-17'), ('T4_R4', 'soft-slot-dynamics-m8-17'), ('T1_R5', 'soft-slot-dynamics-m8-17'),
         ('T5_R2', 'soft-slot-dynamics-m8-17'), ('T5J_R2', 'soft-slot-dynamics-m8-16-1'), ('C2a_R5', 'soft-slot-dynamics-m8-16-1'))


def scale(n32, N):
    return n32 + N * (N + 2) - 32 * 34


def tau(margin, normA, z):
    return max(margin, ln.KAPPA_D * math.sqrt(U * normA * abs(z)))


def main():
    scripts = sys.argv[1]
    total, flagged = 0, 0
    for tag, folder in FILES:
        with open(os.path.join(scripts, folder, 'run', 'out', tag + '.json'), encoding='utf-8') as f:
            d = json.load(f)
        slot = d['case']['slot']
        print(f'{tag}:')
        for k in sorted(d['cutoffs']['32']['points'], key=float):
            p = d['cutoffs']['32']['points'][k]
            if 'summary' not in p:
                print(f'  {float(k):8.3f}: no record at N = 32')
                continue
            r, s = p['record'], p['summary']
            band = lib.band_value(slot, p['lam'])
            nA, m = r['normA'], p['m']
            m40 = 2.0 * math.sqrt(U * scale(nA, 40) * max(m, ln.M0))     # linear.margin at N = 40
            imag = sorted((g for g in s['groups'] if g['cls'] == 'imag'), key=lambda g: g['c'][1])
            hits40, hits48, near = [], [], math.inf
            for a, b in zip(imag, imag[1:]):
                l = max(abs(a['c'][1]), abs(b['c'][1]))
                if not (l < band / 2 or a['neg'] or b['neg']):
                    continue
                gap = abs(a['c'][1] - b['c'][1])
                t32, t40, t48 = (tau(r['margin'], scale(nA, N), l) for N in (32, 40, 48))
                if t32 < gap <= t40:
                    hits40.append((round(l, 5), f'{gap:.3e}', f'{gap / t40:.3f}'))
                elif t32 < gap <= t48:
                    hits48.append((round(l, 5), f'{gap:.3e}', f'{gap / t48:.3f}'))
                elif gap > t48:
                    near = min(near, gap / t40)
            a0 = r['outside_min'] / (ln.GRAY * m40)
            g = p.get('lkernel', {}).get('genuine')
            lr = (g * nA / scale(nA, 40)) / (ln.L_CUT * ln.G_L) if g else None
            total += 1
            flagged += bool(hits40)
            print(f"  {float(k):8.3f}: tau40 {hits40 or '-'}; tau48 {hits48 or '-'}; gap {near:7.2f}; A0 {a0:9.1f}; "
                  + (f'L {lr:9.3g}' if lr is not None else 'L -'))
    print(f'{total} points; a new link at N = 40 alone forecast at {flagged}')


if __name__ == '__main__':
    main()
