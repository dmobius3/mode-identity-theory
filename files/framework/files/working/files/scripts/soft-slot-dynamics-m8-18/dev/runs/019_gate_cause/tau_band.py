import json, math, os, sys
out = sys.argv[1]
U, KD = 2.220446049250313e-16, 10.0
print('Inside the tested band (|lam| < band/2): imaginary neighbours at N = 32 whose gap lies in (tau(32), tau(40)], and the smallest gap/tau(40) above 1')
for n in ('C2a', 'C2b', 'C3', 'C2a_R5', 'P5', 'C3R_R4'):
    d = json.load(open(os.path.join(out, n + '.json'), encoding='utf-8'))
    for e in ('0.25', '0.5', '1', '2'):
        band = d['readings'][e]['band']
        p32, p40 = d['cutoffs']['32']['points'][e], d['cutoffs']['40']['points'][e]
        g = sorted((x for x in p32['summary']['groups'] if x['cls'] == 'imag'), key=lambda x: complex(*x['c']).imag)
        n40 = len(p40['summary']['groups'])
        hits, near = [], []
        for a, b in zip(g, g[1:]):
            za, zb = complex(*a['c']), complex(*b['c'])
            l = max(abs(za), abs(zb))
            if l >= band / 2:
                continue
            gap = abs(za - zb)
            t32 = max(p32['record']['margin'], KD * math.sqrt(U * p32['record']['normA'] * l))
            t40 = max(p40['record']['margin'], KD * math.sqrt(U * p40['record']['normA'] * l))
            if t32 < gap <= t40:
                hits.append((round(l, 6), f'{gap:.3e}', f'{t40:.3e}'))
            elif gap > t40:
                near.append((gap / t40, round(l, 6)))
        near.sort()
        print(f' {n:7s} eps {e:>4}: {len(hits)} hits {hits}; nearest gap/tau40 above 1: {near[0][0]:.2f} at {near[0][1]}' if near else f' {n:7s} eps {e:>4}: {len(hits)} hits {hits}')
