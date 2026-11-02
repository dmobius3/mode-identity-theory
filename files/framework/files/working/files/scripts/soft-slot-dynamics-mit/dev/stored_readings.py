"""What the published records already hold at the census's open items, read for the recon of 2026-11-02. Nothing is
solved. Every value is M8.17's or M8.18's, as stored; every one is a known outcome and none is new evidence.

usage: python3 -I -B stored_readings.py M817_OUT M818_OUT
"""
import json
import math
import sys

M817, M818 = sys.argv[1:3]
OPEN = {'T1_R4': [math.sqrt(2), 32, 32 * math.sqrt(2), 64, 72], 'T1_R5': [32],
        'T4_R4': [4, 8, 8 * math.sqrt(2), 64, 72], 'T5_R2': [32 * math.sqrt(2)]}
CUTS = ('16', '24', '32')


def load(name):
    with open(f'{M817}/{name}.json', encoding='utf-8') as f:
        return json.load(f)


def cell(p):
    s = p.get('summary') if p else None
    if not s:
        return 'no record'
    off = [g for g in s['groups'] if g['cls'] != 'imag']
    return f"{s['type'][:4]} {s['nL']},{s['nD']},{s['K']}" + (f' off-axis {len(off)}' if off else '')


def key_of(d, e):
    return [k for k in d['cutoffs']['32']['points'] if abs(float(k) - e) < 1e-9][0]


print('A. The twelve: type and n(L), n(D), K at N = 16, 24, 32, and the rule\'s verdict on the record')
same = 0
for name, eps in OPEN.items():
    d = load(name)
    for e in eps:
        k = key_of(d, e)
        cells = [cell(d['cutoffs'][N]['points'].get(k)) for N in CUTS]
        agree = len({c.split(' off')[0] for c in cells}) == 1
        same += agree
        print(f"  {name} {e:8.3f}: {' | '.join(cells)} | {d['readings'][k]['verdict']} | same type and indices: {agree}")
print(f'  same type and indices at all three cutoffs: {same} of 12')

print('\nB. T5 in R2, its whole ladder, with the off-axis groups')
d = load('T5_R2')
for k in sorted(d['cutoffs']['32']['points'], key=float):
    cells = [cell(d['cutoffs'][N]['points'].get(k)) for N in CUTS]
    print(f"  {float(k):8.3f}: {' | '.join(cells)} | {(d['readings'].get(k) or {}).get('verdict')}")
for k in ('90.5096679918781', '128', '132'):
    ks = [x for x in d['cutoffs']['32']['points'] if abs(float(x) - float(k)) < 1e-6]
    for x in ks:
        for N in CUTS:
            p = d['cutoffs'][N]['points'][x]
            g = [(round(q['c'][0], 4), round(q['c'][1], 4), q['size']) for q in p['summary']['groups'] if q['cls'] != 'imag']
            print(f'  off-axis at {float(x):.2f}, N = {N}: {g}')

print('\nC. A three-point extrapolation of the quartet\'s real part, N = 16, 24, 32 (INFERRED; the rate is not shown)')
for x, label in ((128.0, '128'), (132.0, '132')):
    r = []
    k = key_of(d, x)
    for N in CUTS:
        q = [q for q in d['cutoffs'][N]['points'][k]['summary']['groups'] if q['cls'] == 'complex'][0]
        r.append(q['c'][0])
    d1, d2 = r[0] - r[1], r[1] - r[2]
    print(f'  {label}: {[round(v, 4) for v in r]}, ratio {d2 / d1:.3f}, Aitken limit {r[2] - d2 * d2 / (d1 - d2):.4f}')

print('\nD. Solve costs: N = 40 over N = 32 on M8.18\'s six controls (path jobs), then M8.17\'s rows at N = 32')
ev = json.load(open(f'{M818}/RUNLOG.json', encoding='utf-8'))['events']


def stamp(s):
    import datetime
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')


st, dur = {}, {}
for e in ev:
    m = e['event']
    if m.endswith(' started'):
        st[m[:-8]] = stamp(e['t'])
    elif m.endswith(' completed') and m[:-10] in st:
        dur[m[:-10]] = (stamp(e['t']) - st[m[:-10]]).total_seconds()
ratios = {}
for c in ('C2a', 'C2b', 'C3', 'C2a/R5', 'P5', 'C3R/R4'):
    ratios[c] = dur[f'path:{c}:40'] / dur[f'path:{c}:32']
    print(f"  {c}: N = 32 {dur[f'path:{c}:32'] / 60:.1f} min, N = 40 {dur[f'path:{c}:40'] / 60:.1f} min, ratio {ratios[c]:.2f}; "
          f"read at N = 40 {dur[f'read:{c}:40'] / 60:.1f} min for 4 points")
r4 = sum(ratios[c] for c in ('C2a', 'C3', 'P5', 'C3R/R4')) / 4
print(f'  mean ratio in R4: {r4:.2f}; R5, C2a/R5: {ratios["C2a/R5"]:.2f}; R2, C2b: {ratios["C2b"]:.2f}')
tot = 0
for name, ratio in (('T1_R4', r4), ('T4_R4', r4), ('T1_R5', ratios['C2a/R5']), ('T5_R2', ratios['C2b'])):
    pts = load(name)['cutoffs']['32']['points']
    s = sum(p.get('seconds', 0) for p in pts.values())
    print(f'  {name}: {len(pts)} points, N = 32 {s / 3600:.2f} h, projected N = 40 {s * ratio / 3600:.1f} h')
    tot += s * ratio
print(f'  the four rows at N = 40, in series: {tot / 3600:.1f} h (a projection: M8.17\'s seconds carry its records)')
