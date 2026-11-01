import json, os, sys
import math
out = sys.argv[1]
U = 2.220446049250313e-16
KD = 10.0
d = json.load(open(os.path.join(out, 'P5.json'), encoding='utf-8'))
print('P5, eps 0.25: the pair, and the group tolerance tau = max(margin, 10 sqrt(u ||A|| |lam|))')
for N in ('24', '32', '40'):
    p = d['cutoffs'][N]['points']['0.25']
    r = p['record']
    g = p['summary']['groups']
    near = sorted([complex(*x['c']).imag for x in g if abs(abs(complex(*x['c'])) - 4.02029) < 1.5e-5 and x['cls'] == 'imag'])
    sizes = [x['size'] for x in g if abs(abs(complex(*x['c'])) - 4.02029) < 1.5e-5]
    t = max(r['margin'], KD * math.sqrt(U * r['normA'] * 4.02029))
    print(f" N {N}: normA {r['normA']:.3f} margin {r['margin']:.4e} tau {t:.4e}; groups {near} sizes {sizes}", end='')
    if len(near) == 2:
        print(f"; gap {near[1] - near[0]:.4e}; centre {(near[0] + near[1]) / 2:.12f}")
    else:
        print()
# how many pairs of neighbouring eigenvalues in each control sit between tau(32) and tau(40), eps by eps
print()
print('Every control point: adjacent groups, N = 32, whose gap is above tau(32) and below tau(40), so linked at 40 only')
for n in ('C2a', 'C2b', 'C3', 'C2a_R5', 'P5', 'C3R_R4'):
    d = json.load(open(os.path.join(out, n + '.json'), encoding='utf-8'))
    for e in ('0.25', '0.5', '1', '2'):
        p32, p40 = d['cutoffs']['32']['points'][e], d['cutoffs']['40']['points'][e]
        g = sorted(p32['summary']['groups'], key=lambda x: (complex(*x['c']).imag))
        hits = []
        for a, b in zip(g, g[1:]):
            za, zb = complex(*a['c']), complex(*b['c'])
            if a['cls'] != 'imag' or b['cls'] != 'imag':
                continue
            gap = abs(za - zb)
            l = max(abs(za), abs(zb))
            t32 = max(p32['record']['margin'], KD * math.sqrt(U * p32['record']['normA'] * l))
            t40 = max(p40['record']['margin'], KD * math.sqrt(U * p40['record']['normA'] * l))
            if t32 < gap <= t40:
                hits.append((round(l, 6), f'{gap:.3e}', a['neg'], b['neg']))
        print(f' {n:7s} eps {e:>4}: {len(hits)}', hits[:6])
