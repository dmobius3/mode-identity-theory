"""T5 in R2 across the step where n(L) falls, from M8.17's published records, read 2026-11-02. Nothing is solved. Every
value is a stored known outcome and none is new evidence.

usage: python3 -I -B t5_top.py SCRIPTS_DIR ENVIRONMENT_JSON
"""
import json, sys
R, ENV = sys.argv[1:3]
d = json.load(open(f'{R}/soft-slot-dynamics-m8-17/run/out/T5_R2.json', encoding='utf-8'))
print('m(eps) on N = 32, and m / eps')
pts = d['cutoffs']['32']['points']
ks = sorted(pts, key=float)
prev = None
for k in ks:
    e, m = float(k), pts[k]['m']
    s = '' if prev is None else f"  dm/deps {(m - prev[1]) / (e - prev[0]):.5f}"
    if e >= 16:
        print(f'  {e:8.3f}  m {m:10.5f}  m/eps {m / e:.5f}{s}')
    prev = (e, m)
print()
F = ('type', 'nL', 'nD', 'K', 'krein', 'sdim', 'ranks', 'cluster', 'blocks', 'dimkerL', 'dimkerD', 'jordan_ranks', 'longest_chain', 'l_resolved', 'unresolved')
for N in ('16', '24', '32'):
    print('N =', N)
    for k in sorted(d['cutoffs'][N]['points'], key=float):
        if float(k) >= 64:
            r = d['cutoffs'][N]['points'][k]['record']
            print(f'  {float(k):7.2f}', {f: r[f] for f in F if f in r})
print()
print('smallest |eigenvalue| on the imaginary axis outside the cluster, N = 32')
for k in ks:
    if float(k) >= 45:
        s = d['cutoffs']['32']['points'][k]['summary']
        im = sorted((abs(g['c'][1]), g['size'], g.get('krein')) for g in s['groups'] if g['cls'] == 'imag')[:5]
        print(f'  {float(k):7.2f}', [(round(a, 4), b, c) for a, b, c in im])
print()
e = json.load(open(ENV))
print('threading:', json.dumps(e['threading'])[:400])
print('os:', json.dumps(e['os'])[:160], 'machine:', json.dumps(e['machine'])[:200])
print()
print('the low pairs and off-axis groups, with the count of negative Krein directions, N = 32')
for k in ks:
    if float(k) >= 45:
        s = d['cutoffs']['32']['points'][k]['summary']
        low = [(round(g['c'][0], 4), round(abs(g['c'][1]), 4), g['cls'], g['neg']) for g in s['groups'] if abs(g['c'][1]) < 3 or g['cls'] != 'imag']
        print(f'  {float(k):7.2f}', low)
