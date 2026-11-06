#!/usr/bin/env python3
"""T5's top at N = 48: what the readings through N = 40 give, stated before any solve at N = 48 (run/TOP48.md, DESIGN.md
section 4). Nothing is solved or read: every value comes from the reading and path files this run wrote at N = 24, 32
and 40, which are now known outcomes, and from the design's own forecasts, pinned before any read. Every forecast at
N = 48 is INFERRED, and three cutoffs cannot separate the laws.

  A. the targets and the in-row controls on the ladder (24, 32, 40): each cutoff's record, both classifications with
     their causes, and branch identity's aligned distance on both pairs
  B. the three laws for the quartet's real part: the design's values at N = 40 and 48, fitted to M8.17's N = 16, 24
     and 32 and pinned before any read, beside N = 40's reading; then the same laws fitted to N = 24, 32 and 40, at 48
  C. the collision, on the square-root law at each cutoff, and the index drop, by the records at each cutoff
  D. branch identity's aligned distance at (40, 48), by the ratio of the last two pairs, against the guard of 1e-2
  E. each tolerance that grows with the cutoff, at N = 48, from the N = 40 reads, as dev/tolerances.py forecast N = 40
     and 48 from N = 32: a new link at 48 alone, K1's separation, L's gray zone, and n(D)'s two gray-zone tops
  F. the cost: the path and read seconds at N = 32 and 40, and their ratio carried to 48

Usage: expectations.py OUT
"""
import json
import math
import os
import re
import sys

from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import linear as ln  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import checks as ck  # noqa: E402
import grid  # noqa: E402

OUT = sys.argv[1]
U = ln.U
LADDER = grid.LADDER
PAIRS = list(zip(LADDER, LADDER[1:]))
TARGETS = (116.0, 120.0, 124.0, 126.0, 127.0, 128.0, 129.0, 130.0, 132.0)
IN_ROW = (100.0, 106.0, 112.0)
QUARTET_POINTS = (127.0, 128.0, 129.0, 130.0, 132.0)
FRESH = ('fresh_P5', 'fresh_C3R_R4', 'fresh_C2b', 'fresh_C2a_R5')
GUARD = ck.IDENTITY
# the design's values, pinned before any read (dev/t5_laws.out, from M8.17's N = 16, 24 and 32): (N = 40, N = 48)
PINNED = {128.0: dict(geometric=(0.0481, 0.0288), algebraic=(0.0346, -0.0015), square=(0.0534, 0.0420)),
          132.0: dict(geometric=(0.1272, 0.1159), algebraic=(0.1161, 0.0925), square=(0.1359, 0.1311))}
PINNED_LINES = ('geometric in the real part:        limit 0.0161, ratio 0.397; N = 40 0.0481, N = 48 0.0288',
                'algebraic a + b N^-p:              limit -0.1047, p 1.646; N = 40 0.0346, N = 48 -0.0015',
                'geometric in its square (collision): limit 0.0393, ratio 0.168; N = 40 0.0534, N = 48 0.0420',
                'geometric in the real part:        limit 0.1101, ratio 0.340; N = 40 0.1272, N = 48 0.1159',
                'algebraic a + b N^-p:              limit 0.0414, p 2.081; N = 40 0.1161, N = 48 0.0925',
                'geometric in its square (collision): limit 0.1301, ratio 0.177; N = 40 0.1359, N = 48 0.1311')


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def keyed(points, e):
    ks = [k for k in points if abs(float(k) - e) < 1e-9]
    return ks[0] if ks else None


def off_axis(p):
    return [g for g in p['summary']['groups'] if g['cls'] != 'imag']


def cell(p, case):
    if not p or 'record' not in p:
        return 'no record'
    r = p['record']
    off = len(off_axis(p))
    return (f"{r['type'][:4]} ({r['nL']}, {r['nD']}, {r['K']})" + (f' off-axis {off}' if off else '')
            + ('' if ck.k1(p, case) else ' K1 fails'))


def cls_text(c):
    return f"{c['type']} ({c['nL']}, {c['nD']}, {c['K']})" if c['classified'] else 'not classified'


def distances(d, k):
    out = {}
    for pair in PAIRS:
        pts = {N: d['cutoffs'][str(N)]['points'].get(k) for N in pair}
        idn = changed.identity(d['identity'].get(k, {}).get(lib.pair_key(pair)), pts, pair)
        out[pair] = idn['aligned_distance'] if idn else None
    return out


# --- the laws, on three cutoffs ns (lowest first) --------------------------------------------------------------------
def geometric(x, ns):
    a, b, c = x
    r = (c - b) / (b - a)
    lim = c + (c - b) * r / (1 - r)
    step = ns[2] - ns[1]
    return lim, r, (lambda n: lim + (c - lim) * r ** ((n - ns[2]) / step))


def algebraic(x, ns):
    a, b, c = x
    f = lambda p: (ns[0] ** -p - ns[1] ** -p) * (b - c) - (ns[1] ** -p - ns[2] ** -p) * (a - b)  # noqa: E731
    p = brentq(f, 0.05, 60)
    B = (a - b) / (ns[0] ** -p - ns[1] ** -p)
    lim = c - B * ns[2] ** -p
    return lim, p, (lambda n: lim + B * n ** -p)


def root(v):
    return math.copysign(math.sqrt(abs(v)), v)


def laws(re, ns):
    """The three laws on the real parts re at the cutoffs ns: {law: (limit, rate, value at 48)}."""
    lim_g, r, fg = geometric(re, ns)
    lim_a, p, fa = algebraic(re, ns)
    lim_s, rs, fs = geometric([x * x for x in re], ns)
    return dict(geometric=(lim_g, r, fg(48)), algebraic=(lim_a, p, fa(48)), square=(root(lim_s), rs, root(fs(48))))


def main():
    t5 = load(os.path.join(OUT, 'T5_R2.json'))
    case = t5['case']
    pts = {N: t5['cutoffs'][str(N)]['points'] for N in LADDER}

    print('A. The targets and the in-row controls on (24, 32, 40): each cutoff\'s record; both classifications; branch '
          'identity\'s aligned distance on both pairs (the guard is 1e-2)')
    for e in IN_ROW + TARGETS:
        k = keyed(t5['both'], e)
        b = t5['both'][k]
        dist = distances(t5, k)
        role = 'in-row control' if e in IN_ROW else 'target'
        print(f"  {e:6g} ({role}): " + ' | '.join(f'{N} {cell(pts[N][k], case)}' for N in LADDER))
        print(f"          as built {cls_text(b['as_built'])}, changed {cls_text(b['changed'])}; aligned distance "
              + ', '.join(f'({a}, {c}) {v:.4g}' for (a, c), v in dist.items()))
        if not b['as_built']['classified']:
            print('          causes as built: ' + '; '.join(b['as_built']['causes'])[:300])

    print('\nB. The quartet\'s real part: the design\'s three laws, pinned before any read, beside N = 40\'s reading; then '
          'the same laws on N = 24, 32 and 40, at 48 (INFERRED)')
    pinned_out = open(os.path.join(ROOT, 'dev', 't5_laws.out'), encoding='utf-8').read()
    for line in PINNED_LINES:
        assert line in pinned_out, line
    for e in QUARTET_POINTS:
        k = keyed(t5['both'], e)
        re_ = []
        for N in LADDER:
            q = off_axis(pts[N][k])
            assert len(q) == 1 and q[0]['size'] == 1, (e, N, q)
            re_.append(q[0]['c'][0])
        im40 = off_axis(pts[40][k])[0]['c'][1]
        print(f'  {e:g}: real part at N = 24, 32, 40: {", ".join(f"{x:.6f}" for x in re_)}; steps '
              f'{re_[0] - re_[1]:.6f}, {re_[1] - re_[2]:.6f}; imaginary part at 40 {im40:.6f}')
        if e in PINNED:
            print('      pinned (from 16, 24, 32): ' + '; '.join(
                f'{law} {v40:.4f} at 40, {v48:.4f} at 48' for law, (v40, v48) in PINNED[e].items())
                  + f'; N = 40 reads {re_[2]:.4f}, above every law: {all(re_[2] > v[0] for v in PINNED[e].values())}')
        fit = laws(re_, LADDER)
        print('      refitted (from 24, 32, 40): ' + '; '.join(
            f'{law} limit {lim:.5f}, {"p" if law == "algebraic" else "ratio"} {rate:.4g}, at 48 {v48:.5f}'
            for law, (lim, rate, v48) in fit.items()))
        v48 = [v[2] for v in fit.values()]
        print(f'      the step from 40 to 48: {min(re_[2] - x for x in v48):.2e} to {max(re_[2] - x for x in v48):.2e}')

    print('\nC. The collision, the real part squared linear in eps over the Hyperbolic points at each cutoff (the '
          'square-root law, INFERRED), and the index drop by the records')
    zeros = []
    for N in LADDER:
        ks = sorted((k for k in pts[N] if float(k) >= 64), key=float)
        hyp = [k for k in ks if pts[N][k]['record']['type'] == 'Hyperbolic']
        xs = [float(k) for k in hyp]
        ys = [off_axis(pts[N][k])[0]['c'][0] ** 2 for k in hyp]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        zeros.append(mx - my / a)
        cells = [(float(k), pts[N][k]['record']) for k in ks]
        last9 = max(x for x, r in cells if (r['nL'], r['nD'], r['K']) == (9, 3, 6))
        k4 = [x for x, r in cells if r['type'] == 'Elliptic' and r['K'] == 4]
        print(f'  N = {N}: (9, 3, 6) to {last9:g}; Elliptic with K = 4 at {[f"{x:g}" for x in k4]}; Hyperbolic from '
              f'{xs[0]:g}; the collision at {zeros[-1]:.3f} (slope {a:.5f} over {len(xs)} points)')
    d1, d2 = zeros[1] - zeros[0], zeros[2] - zeros[1]
    r = d2 / d1
    print(f'  the zeros {[round(z, 3) for z in zeros]}: ratio {r:.4f}, Aitken limit {zeros[2] - d2 * d2 / (d2 - d1):.3f}, '
          f'at 48 by that ratio {zeros[2] + d2 * r:.3f}; the design\'s "near 127 at N = 40, with a limit of 127.5 to 128" '
          f'missed at 40')

    print('\nD. Branch identity at (40, 48), by the ratio of the last two pairs (INFERRED), against the guard')
    for e in IN_ROW + TARGETS:
        k = keyed(t5['both'], e)
        dist = distances(t5, k)
        a, b = dist[(24, 32)], dist[(32, 40)]
        f = b * b / a
        print(f'  {e:6g}: (24, 32) {a:.4g}, (32, 40) {b:.4g}, ratio {b / a:.3f}; at (40, 48) {f:.2g}, '
              f'{GUARD / f:.0f} times under the guard')

    print('\nE. The tolerances at N = 48, from the N = 40 reads (dev/tolerances.py\'s method: ||A|| at a new cutoff is the '
          'N = 40 value plus the difference of N (N + 2); ||B|| is taken as ||A||, INFERRED)')
    files = [('T5_R2', IN_ROW + TARGETS)] + [(t, tuple(float(k) for k in load(os.path.join(OUT, t + '.json'))['both']))
                                              for t in FRESH]
    for tag, eps in files:
        d = load(os.path.join(OUT, tag + '.json'))
        slot = d['case']['slot']
        for e in eps:
            k = keyed(d['both'], e)
            p = d['cutoffs']['40']['points'][k]
            r, s = p['record'], p['summary']
            nA = r['normA']
            n48 = nA + 48 * 50 - 40 * 42
            m48 = ln.KAPPA * math.sqrt(U * n48 * max(p['m'], ln.M0))
            band = lib.band_value(slot, p['lam'])
            imag = sorted((g for g in s['groups'] if g['cls'] == 'imag'), key=lambda g: g['c'][1])
            new48, near = [], math.inf
            for g1, g2 in zip(imag, imag[1:]):
                lev = max(abs(g1['c'][1]), abs(g2['c'][1]))
                if not (lev < band / 2 or g1['neg'] or g2['neg']):
                    continue
                gap = abs(g1['c'][1] - g2['c'][1])
                t40 = max(r['margin'], ln.KAPPA_D * math.sqrt(U * nA * lev))
                t48 = max(m48, ln.KAPPA_D * math.sqrt(U * n48 * lev))
                if t40 < gap <= t48:
                    new48.append((round(lev, 5), f'{gap:.3e}'))
                elif gap > t48:
                    near = min(near, gap / t48)
            a0 = r['outside_min'] / (ln.GRAY * m48)
            g = p.get('lkernel', {}).get('genuine')
            lr = (g * nA / n48) / (ln.L_CUT * ln.G_L) if g else None
            dz = [x for x in p['d_eigs'] if 1e-8 * nA < abs(x) <= 1e-5 * n48]
            print(f'  {tag} {e:g}: margin {r["margin"]:.3g} at 40, {m48:.3g} at 48; a new link at 48 alone '
                  f'{new48 or "none"}; the nearest other gap {near:.3g} tau(48); K1\'s separation, A\'s smallest eigenvalue '
                  f'outside the cluster over 3 margin at 48, {a0:.3g}; L {"-" if lr is None else f"{lr:.3g}"}; '
                  f"n(D)'s old zone at 48 holds {len(dz)} eigenvalue(s){' ' + str([round(x, 6) for x in dz]) if dz else ''}"
                  f'; under B the top at 48 is {1e-7 * n48:.3g}')
        d = load(os.path.join(OUT, 'fresh_P5.json'))
        if tag == 'fresh_P5':
            for N in LADDER:
                p = d['cutoffs'][str(N)]['points']['0.24']
                groups = [g['size'] for g in p['summary']['groups'] if abs(g['c'][1] - 4.0205) < 1e-3]
                print(f'      P5 0.24 at N = {N}: the groups within 1e-3 of 4.0205i have sizes {groups}')
            nA40 = d['cutoffs']['40']['points']['0.24']['record']['normA']
            for N in (32, 40, 48):
                nA = nA40 + N * (N + 2) - 40 * 42
                print(f'      tau at 4.0205 and N = {N}: {ln.KAPPA_D * math.sqrt(U * nA * 4.0205):.4e}')

    agree, disagree = 0, []
    for tag in FRESH + ('T5_R2', 'T5J_R2', 'T1_R4', 'T4_R4', 'T1_R5', 'C2a_R5'):
        d = load(os.path.join(OUT, tag + '.json'))
        for N in LADDER:
            for k, p in d['cutoffs'][str(N)]['points'].items():
                if not p or 'record' not in p or 'd_eigs' not in p:
                    continue
                nA = p['record']['normA']
                forecast = any(1e-8 * nA < abs(x) <= 1e-5 * nA for x in p['d_eigs'])
                if forecast == (changed.ND_LINE in p['record']['unresolved']):
                    agree += 1
                else:
                    disagree.append((tag, N, k))
    print(f"  n(D)'s inherited flag forecast with ||B|| taken as ||A||, against every read record at N = 24, 32 and 40: "
          f'{agree} agree, {len(disagree)} disagree {disagree or ""}')

    print('\nF. The cost: each path\'s and read\'s seconds at N = 32 and 40, four jobs at a time, and their ratio carried '
          'to 48 (INFERRED; N^9 would give 5.16)')
    for tag in ('T5_R2',) + FRESH:
        row = {}
        for N in (32, 40):
            pth = load(os.path.join(OUT, f'{tag}_N{N}.json'))
            rd = load(os.path.join(OUT, f'{tag}_N{N}_read.json'))
            row[N] = (sum(p.get('seconds', 0) for p in pth['points'].values()),
                      sum(p.get('seconds_record', 0) for p in rd['points'].values()) / max(1, len(rd['points'])),
                      len(pth['points']))
        ratio = row[40][0] / row[32][0]
        expo = math.log(ratio) / math.log(40 / 32)
        r48 = (48 / 40) ** expo
        print(f'  {tag}: {row[40][2]} points; path {row[32][0] / 3600:.2f} h at 32, {row[40][0] / 3600:.2f} h at 40, '
              f'ratio {ratio:.2f} (N^{expo:.2f}), so {r48:.2f} more at 48: {row[40][0] * r48 / 3600:.1f} h to '
              f'{row[40][0] * 5.16 / 3600:.1f} h; a read {row[40][1]:.0f} s a point at 40, {row[40][1] * r48 / 60:.1f} to '
              f'{row[40][1] * 5.16 / 60:.1f} min at 48')
    jobs = {f[:-5]: load(os.path.join(OUT, 'jobs', f)) for f in os.listdir(os.path.join(OUT, 'jobs'))
            if re.match(r'(path|read)_.*_N40\.json$', f)}
    peak = max(j['peak_rss_bytes'] for j in jobs.values()) / 2 ** 30
    print(f'  the largest peak resident size of a path or read job at N = 40: {peak:.2f} GiB')


if __name__ == '__main__':
    main()
