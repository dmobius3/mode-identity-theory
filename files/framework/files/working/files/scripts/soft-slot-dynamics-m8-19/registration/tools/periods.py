"""The slow time scales of the stretches S5's terms name, read from OpenWave's adjudicated records alone: at each point
a record classifies Elliptic, the slowest genuine slow mode's |lambda| at the record's top cutoff, its Krein sign, its
period P = 2 pi / |lambda|, and how many periods T = 1000 and T_max = 4000 cover.
Sources: M8.17's stored readings (soft-slot-dynamics-m8-17/run/out/<row>.json, adjudicated on #676) for T1 and T4, and
M8.16.1's control C2a/R5 (soft-slot-dynamics-m8-16-1/run/out/C2a_R5.json, adjudicated on #653) for the coherent row in
R5. Nothing is solved; MIT's own computation is not read.
Usage: periods.py SCRIPTS   (the repository's files/framework/files/working/files/scripts)"""
import json
import math
import os
import sys

S = sys.argv[1]
SRC = [('T1/R4', 'soft-slot-dynamics-m8-17/run/out/T1_R4.json'), ('T1/R5', 'soft-slot-dynamics-m8-17/run/out/T1_R5.json'),
       ('T4/R4', 'soft-slot-dynamics-m8-17/run/out/T4_R4.json'), ('T4/R5', 'soft-slot-dynamics-m8-17/run/out/T4_R5.json'),
       ('coherent/R5', 'soft-slot-dynamics-m8-16-1/run/out/C2a_R5.json')]


def mag(v):
    return abs(complex(v[0], v[1])) if isinstance(v, (list, tuple)) else abs(v)


print('row          eps       |lambda|    Krein   P = 2pi/|lambda|   periods in 1000   in 4000')
for row, rel in SRC:
    d = json.load(open(os.path.join(S, rel), encoding='utf-8'))
    for e, r in d['readings'].items():
        if r.get('type') != 'Elliptic' or r.get('verdict') != 'converged':
            continue
        slow = sorted((mag(x['c'][-1]), x.get('neg', 0)) for x in r['rows']
                      if x.get('cls') == 'imag' and mag(x['c'][-1]) > 1e-9)
        lam, neg = slow[0]
        P = 2 * math.pi / lam
        print(f'{row:12s} {float(e):8.4f}   {lam:.4e}   {"neg" if neg else "pos"}     {P:12.0f}       {1000 / P:8.2f}        '
              f'{4000 / P:6.2f}')
