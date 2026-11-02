"""T5 in R2 at 128 and 132: the quartet's real part under three laws in the cutoff, from M8.17's published records, read
2026-11-02. Nothing is solved. Every input is a stored known outcome; every output is an extrapolation (INFERRED): three
points cannot separate the laws. The values at N = 40 and 48 are stated before any read there.

usage: python3 -I -B t5_laws.py SCRIPTS_DIR
"""
import json
import math
import sys
from scipy.optimize import brentq

R = sys.argv[1]
d = json.load(open(f'{R}/soft-slot-dynamics-m8-17/run/out/T5_R2.json', encoding='utf-8'))
CUTS = ('16', '24', '32')


def quartet(N, key):
    q = [g for g in d['cutoffs'][N]['points'][key]['summary']['groups'] if g['cls'] != 'imag']
    assert len(q) == 1 and q[0]['size'] == 1
    return q[0]['c'][0], q[0]['c'][1]


def key_of(e):
    return [k for k in d['cutoffs']['32']['points'] if abs(float(k) - e) < 1e-6][0]


def geometric(x):
    a, b, c = x
    r = (c - b) / (b - a)
    lim = c + (c - b) * r / (1 - r)
    return lim, r, lambda n: lim + (c - lim) * r ** ((n - 32) / 8)


def algebraic(x, ns=(16, 24, 32)):
    a, b, c = x
    f = lambda p: (ns[0] ** -p - ns[1] ** -p) * (b - c) - (ns[1] ** -p - ns[2] ** -p) * (a - b)
    p = brentq(f, 0.05, 30)
    B = (a - b) / (ns[0] ** -p - ns[1] ** -p)
    lim = c - B * ns[2] ** -p
    return lim, p, lambda n: lim + B * n ** -p


def root(v):
    return math.copysign(math.sqrt(abs(v)), v)


print('stored quartets, real and imaginary parts')
out = {}
for e in (90.5096679918781, 128.0, 132.0):
    k = key_of(e)
    row = []
    for N in CUTS:
        try:
            row.append((N, *quartet(N, k)))
        except AssertionError:
            row.append((N, None, None))
    print(f'  {e:8.3f}', [(N, None if a is None else round(a, 5), None if b is None else round(b, 5)) for N, a, b in row])
    out[e] = row

print('\nlaws')
for e in (128.0, 132.0):
    re = [a for _, a, _ in out[e]]
    lim_g, r, fg = geometric(re)
    lim_a, p, fa = algebraic(re)
    n0 = None
    if lim_a < 0:
        n0 = brentq(lambda n: fa(n), 32, 400)
    sq = [x * x for x in re]
    lim_s, rs, fs = geometric(sq)
    print(f'  eps {e:g}: stored {[round(x, 4) for x in re]}')
    print(f'    geometric in the real part:        limit {lim_g:.4f}, ratio {r:.3f}; N = 40 {fg(40):.4f}, N = 48 {fg(48):.4f}')
    print(f'    algebraic a + b N^-p:              limit {lim_a:.4f}, p {p:.3f}; N = 40 {fa(40):.4f}, N = 48 {fa(48):.4f}; zero near N = {None if n0 is None else round(n0, 1)}')
    print(f'    geometric in its square (collision): limit {root(lim_s):.4f}, ratio {rs:.3f}; N = 40 {root(fs(40)):.4f}, N = 48 {root(fs(48)):.4f}')

print('\nwhere the collision sits, from the square of the real part, linear in eps, per cutoff')
st = {}
for N, i in (('16', 0), ('24', 1), ('32', 2)):
    x, y = out[128.0][i][1], out[132.0][i][1]
    c = (y * y - x * x) / 4
    st[N] = 128 - x * x / c
    print(f'  N = {N}: slope {c:.5f}, from 128 and 132: {st[N]:.2f}')
x, y = out[90.5096679918781][0][1], out[128.0][0][1]
c = (y * y - x * x) / (128 - 90.5096679918781)
alt = 90.5096679918781 - x * x / c
print(f'  N = 16 from 90.51 and 128 instead: slope {c:.5f}, {alt:.2f}')
for label, s16 in (('N = 16 from 128 and 132', st['16']), ('N = 16 from 90.51 and 128', alt)):
    lim, r, f = geometric([s16, st['24'], st['32']])
    print(f'  geometric limit with {label}: {lim:.2f}, ratio {r:.3f}, N = 40 {f(40):.2f}')

print('\nm on the ladder at 128 and 132, the solve field\'s own rate')
for e in (128.0, 132.0):
    k = key_of(e)
    m = [d['cutoffs'][N]['points'][k]['m'] for N in CUTS]
    lim, r, _ = geometric(m)
    print(f'  eps {e:g}: m {[round(x, 4) for x in m]}, ratio {r:.3f}, limit {lim:.4f}')
