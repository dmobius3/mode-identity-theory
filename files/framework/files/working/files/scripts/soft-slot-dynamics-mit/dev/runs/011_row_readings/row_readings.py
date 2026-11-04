#!/usr/bin/env python3
"""The rows' readings, read for the items (DESIGN.md, sections 4 and 6). Nothing is solved or read again: every value
comes from the reading files the runner wrote, each point classified by the run's own code (census_lib.here, stored in
each file's `both`, as built and changed), with checks.k1 and changed.identity beside it. Section 6's statements,
stated before any read, are set beside what the readings give.

  A. the twelve, against M8.17's stored type and indices
  B. every row's ladder
  C. T5's top: the index drop, the Elliptic stretch with K = 4, the quartet, and its real part against section 6
  D. T5's second member: the pair at 0.25, and the set at 0.354
  E. every set the rule formed in the rows, with its group sizes at each cutoff: where a link differs between cutoffs
  F. section 6, statement by statement

Usage: row_readings.py OUT SCRIPTS_DIR
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import checks as ck  # noqa: E402
import grid  # noqa: E402

ROWS = ('T1_R4', 'T4_R4', 'T1_R5', 'T5_R2', 'T5J_R2', 'C2a_R5')
TWELVE = {'T1_R4': [math.sqrt(2), 32, 32 * math.sqrt(2), 64, 72], 'T1_R5': [32],
          'T4_R4': [4, 8, 8 * math.sqrt(2), 64, 72], 'T5_R2': [32 * math.sqrt(2)]}      # dev/stored_readings.py
STORED = dict(T1_R4='soft-slot-dynamics-m8-17', T4_R4='soft-slot-dynamics-m8-17', T1_R5='soft-slot-dynamics-m8-17',
              T5_R2='soft-slot-dynamics-m8-17', T5J_R2='soft-slot-dynamics-m8-16-1', C2a_R5='soft-slot-dynamics-m8-16-1')
PAIRS = list(zip(grid.LADDER, grid.LADDER[1:]))
# section 6's values, as DESIGN.md states them; main() refuses unless the design holds these strings
QUARTET = {128: dict(geometric=0.048, algebraic=0.035, square=0.053), 132: dict(geometric=0.127, algebraic=0.116,
                                                                               square=0.136)}
DESIGN_SAYS = ('The real part at 128 reads about 0.048 if it is geometric in `N`, 0.035 if algebraic, and 0.053 if its '
               'square is geometric', 'At 132: 0.127, 0.116, 0.136.',
               'the collision sits near 127 at `N = 40`, with a limit of 127.5 to 128')
T5J_WINDOW = (6.0150, 6.0153)        # the pair at 0.25, as dev/t5j_tau.py finds it in M8.16.1's summaries


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
    return (f"{r['type'][:4]} {r['nL']},{r['nD']},{r['K']}" + (f' off-axis {off}' if off else '')
            + ('' if ck.k1(p, case) else ' K1 fails'))


def stored_cell(p):
    s = p.get('summary') if p else None
    if not s:
        return 'no record'
    off = [g for g in s['groups'] if g['cls'] != 'imag']
    return f"{s['type'][:4]} {s['nL']},{s['nD']},{s['K']}" + (f' off-axis {len(off)}' if off else '')


def cls_text(c):
    return f"{c['type']} ({c['nL']}, {c['nD']}, {c['K']})" if c['classified'] else 'not classified'


def identities(d, k):
    out = []
    for pair in PAIRS:
        pts = {N: d['cutoffs'][str(N)]['points'].get(k) for N in pair}
        idn = changed.identity(d['identity'].get(k, {}).get(lib.pair_key(pair)), pts, pair)
        out.append((pair, idn))
    return out


def group_of(p, z):
    """The size of the summary group at one cutoff that holds eigenvalue z, by its members or its centre."""
    held = {tuple(m['idx']): m['z'] for m in p['members']}
    for g in p['summary']['groups']:
        zs = held.get(tuple(g['idx']), [g['c']]) if g['size'] > 1 else [g['c']]
        if any(abs(complex(*w) - z) <= 1e-15 * max(1.0, abs(z)) for w in zs):
            return g['size'], tuple(g['idx'])
    return None, None


def set_rows(d, k):
    """Each set the changed reading formed at k, once, though the rule reads a set once for each group it partners: its
    role, centre, and the group sizes at each cutoff, lowest first."""
    out, seen_sets = [], set()
    for row in d['changed'][k]['rows']:
        if row.get('kind') != 'set' or 'levels' not in row:
            continue
        ident = (row['role'], json.dumps(row['levels']))
        if ident in seen_sets:
            continue
        seen_sets.add(ident)
        sizes = []
        for a, lev in enumerate(row['levels']):                       # highest cutoff first
            N = grid.LADDER[-1 - a]
            p = d['cutoffs'][str(N)]['points'][k]
            seen = {}
            for z in lev:
                s, idx = group_of(p, complex(*z))
                seen[idx] = s
            sizes.append(sorted(seen.values(), key=lambda s: -1 if s is None else s))
        out.append(dict(role=row['role'], c=complex(*row['levels'][0][0]), count=row['count'], sizes=sizes[::-1],
                        ok=row['ok'], why=row.get('why'), levels=row['levels'][::-1]))
    return out


def main():
    out, scripts = sys.argv[1:3]
    design = open(os.path.join(ROOT, 'run', 'DESIGN.md'), encoding='utf-8').read()
    assert all(s in design for s in DESIGN_SAYS), 'section 6 does not hold the values this script sets beside it'
    rows = {t: load(os.path.join(out, t + '.json')) for t in ROWS}
    stored = {t: load(os.path.join(scripts, STORED[t], 'run', 'out', t + '.json')) for t in ROWS}

    print('A. The twelve: M8.17\'s stored type and indices at N = 16, 24, 32; this run\'s records at N = 24, 32, 40, '
          'its classification as built and changed, and branch identity\'s aligned distance on both pairs')
    kept = 0
    for tag, eps in TWELVE.items():
        d, s = rows[tag], stored[tag]
        for e in eps:
            k, ks = keyed(d['both'], e), keyed(s['cutoffs']['32']['points'], e)
            was = [stored_cell(s['cutoffs'][N]['points'].get(ks)) for N in ('16', '24', '32')]
            now = [cell(d['cutoffs'][str(N)]['points'][k], d['case']) for N in grid.LADDER]
            b = d['both'][k]
            st = s['cutoffs']['32']['points'][ks]['summary']
            c40 = d['cutoffs']['40']['points'][k]['record']
            same = (b['as_built']['classified'] and b['changed']['classified'] and b['same']
                    and [c40['type'], c40['nL'], c40['nD'], c40['K']] == [st['type'], st['nL'], st['nD'], st['K']]
                    and len({x.split(' off')[0] for x in was + now}) == 1)
            kept += same
            idn = ', '.join(f"{a}-{bb} {i['aligned_distance']:.3g}" for (a, bb), i in identities(d, k))
            print(f"  {tag} {e:8.3f}: stored {' | '.join(was)}; now {' | '.join(now)}; as built "
                  f"{cls_text(b['as_built'])}, changed {cls_text(b['changed'])}; identity {idn}; "
                  f"same type and indices: {same}")
    print(f'  the twelve keep their stored type and indices at N = 40, classified both ways: {kept} of 12')

    print('\nB. Every row\'s ladder: the records at N = 24, 32, 40; the classification as built and changed; branch '
          'identity\'s aligned distance on both pairs (the guard is 1e-2); the causes where a point is not classified')
    for tag in ROWS:
        d = rows[tag]
        ks = sorted(d['both'], key=float)
        nb = sum(d['both'][k]['as_built']['classified'] for k in ks)
        nc = sum(d['both'][k]['changed']['classified'] for k in ks)
        print(f"  {tag} ({d['case']['slot']}), {len(ks)} points: classified {nb} as built, {nc} changed")
        for k in ks:
            b = d['both'][k]
            now = [cell(d['cutoffs'][str(N)]['points'][k], d['case']) for N in grid.LADDER]
            idn = ', '.join(f"{i['aligned_distance']:.3g}" + ('' if i['kept'] else ' fails') for _, i in identities(d, k))
            two = cls_text(b['as_built']) + ('' if b['same'] else f" | changed {cls_text(b['changed'])}")
            print(f"    {float(k):9.4f}  {' | '.join(now)}  ->  {two}; identity {idn}")
            for arm in ('as_built', 'changed'):
                if not b[arm]['classified'] and (arm == 'as_built' or not b['same']):
                    for c in b[arm]['causes']:
                        print(f"               {arm.replace('_', ' ')}: {c}")

    print('\nC. T5\'s top, from 64: the records at each cutoff, then the quartet, the rule\'s row on it at N = 40, and '
          'its real part against section 6')
    d, case = rows['T5_R2'], rows['T5_R2']['case']
    top = [k for k in sorted(d['both'], key=float) if float(k) >= 64]
    for N in grid.LADDER:
        pts = d['cutoffs'][str(N)]['points']
        cells = [(float(k), pts[k]['record']) for k in top]
        last9 = max(e for e, r in cells if (r['nL'], r['nD'], r['K']) == (9, 3, 6))
        k4 = [e for e, r in cells if r['type'] == 'Elliptic' and r['K'] == 4]
        hyp = min(e for e, r in cells if r['type'] == 'Hyperbolic')
        print(f'  N = {N}: (9, 3, 6) to {last9:g}; Elliptic with K = 4 at {[f"{e:g}" for e in k4]}; '
              f'Hyperbolic from {hyp:g}')
    for k in top:
        qs = []
        for N in grid.LADDER:
            p = d['cutoffs'][str(N)]['points'][k]
            qs.append('; '.join(f"{g['c'][0]:.5f}{g['c'][1]:+.5f}i ({g['cls']}, size {g['size']})" for g in off_axis(p))
                      or 'none')
        print(f"  {float(k):6g}: off the axis at N = 24 {qs[0]} | 32 {qs[1]} | 40 {qs[2]}")
        for arm in ('readings', 'changed'):
            for r in d[arm][k]['rows']:
                if r['cls'] != 'imag':
                    c = r['c'] if r['kind'] == 'group' else r['c'][0]
                    print(f"          the rule's {'as-built' if arm == 'readings' else 'changed'} row: {r['role']} "
                          f"{r['kind']} at {c[0]:.5f}{c[1]:+.5f}i, U {r.get('U', float('nan')):.3g}, d {r.get('d', float('nan')):.3g} "
                          f"to {r.get('event')}, U/d {r.get('U', 0) / r['d'] if r.get('d') else float('nan'):.3g}, "
                          f"{'ok' if r['ok'] else 'fails: ' + str(r.get('why'))}")
    for e, law in QUARTET.items():
        k = keyed(d['both'], e)
        re40 = [g['c'][0] for g in off_axis(d['cutoffs']['40']['points'][k])]
        res = [[round(g['c'][0], 5) for g in off_axis(d['cutoffs'][str(N)]['points'][k])] for N in grid.LADDER]
        lo, hi = min(law.values()), max(law.values())
        within = len(re40) == 1 and lo <= re40[0] <= hi
        print(f"  the quartet's real part at {e}: N = 24, 32, 40 {res}; section 6 at N = 40: "
              + ', '.join(f'{n} {v}' for n, v in law.items()) + f'; within [{lo}, {hi}]: {within}')
    print('  the collision at each cutoff: its bracket from the records, then the square-root law, the real part squared '
          'linear in eps over the points off the axis (INFERRED; the collision law of section 6)')
    zeros = []
    for N in grid.LADDER:
        pts = d['cutoffs'][str(N)]['points']
        ks = sorted((k for k in pts if float(k) >= 64), key=float)
        hyp = [k for k in ks if pts[k]['record']['type'] == 'Hyperbolic']
        last = max(float(k) for k in ks if float(k) < float(hyp[0]))
        xs = [float(k) for k in hyp]
        ys = [off_axis(pts[k])[0]['c'][0] ** 2 for k in hyp]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        sl = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(len(xs) - 1)]
        zeros.append(mx - my / a)
        print(f"    N = {N}: between {last:g} ({pts[keyed(pts, last)]['record']['type']}) and {xs[0]:g} by the records; "
              f'slope {min(sl):.5f} to {max(sl):.5f} between neighbours, {a:.5f} fitted over {len(xs)} points; '
              f'zero at {zeros[-1]:.3f}')
    d1, d2 = zeros[1] - zeros[0], zeros[2] - zeros[1]
    limit = zeros[2] - d2 * d2 / (d2 - d1)
    print(f'    the zeros {[round(z, 3) for z in zeros]}, ratio {d2 / d1:.3f}, Aitken limit {limit:.3f} (INFERRED; the rate '
          'is not shown)')
    t5j = rows['T5J_R2']
    for e in (128, 132):
        a, b = keyed(d['both'], e), keyed(t5j['both'], e)
        za = [complex(*g['c']) for g in off_axis(d['cutoffs']['40']['points'][a])]
        zb = [complex(*g['c']) for g in off_axis(t5j['cutoffs']['40']['points'][b])]
        ma, mb = d['cutoffs']['40']['points'][a]['m'], t5j['cutoffs']['40']['points'][b]['m']
        rb = [[round(g['c'][0], 5) for g in off_axis(t5j['cutoffs'][str(N)]['points'][b])] for N in grid.LADDER]
        print(f'  T5 and its second member at {e}, N = 40: m {ma:.12g} and {mb:.12g}; the quartet '
              f'{za[0]:.8f} and {zb[0]:.8f}, apart by {abs(za[0] - zb[0]):.3g}; the second member\'s real part at '
              f'N = 24, 32, 40 {rb}')

    print('\nD. T5\'s second member: the pair at 0.25 (its window as dev/t5j_tau.py takes it), then every set the '
          'changed reading formed on the row')
    k = keyed(t5j['both'], 0.25)
    for N in grid.LADDER:
        p = t5j['cutoffs'][str(N)]['points'][k]
        held = {tuple(m['idx']): m['z'] for m in p['members']}
        gs = [g for g in p['summary']['groups'] if g['cls'] == 'imag' and T5J_WINDOW[0] < g['c'][1] < T5J_WINDOW[1]]
        zs = sorted(w[1] for g in gs for w in (held[tuple(g['idx'])] if g['size'] > 1 else [g['c']]))
        gap = zs[1] - zs[0] if len(zs) == 2 else None
        print(f"  0.25, N = {N}: group sizes {[g['size'] for g in gs]}, members {[f'{z:.10f}' for z in zs]}, "
              f"gap {'n/a' if gap is None else format(gap, '.5e')}, margin {p['summary']['margin']:.3e}")
    for kk in sorted(t5j['both'], key=float):
        for s in set_rows(t5j, kk):
            print(f"  {float(kk):g}: {s['role']} set at {s['c']:.6g}, {s['count']} eigenvalues, group sizes at "
                  f"N = 24, 32, 40 {s['sizes']}, {'ok' if s['ok'] else 'fails: ' + str(s['why'])}")
            for N, lev in zip(grid.LADDER, s['levels']):
                print(f"        N = {N}: {[f'{complex(*z).imag:.10f}' for z in lev]}")
        bb, cc = t5j['readings'][kk], t5j['changed'][kk]
        if bb['verdict'] != cc['verdict']:
            for arm, rd in (('as built', bb), ('changed', cc)):
                for r in rd['rows']:
                    if r.get('kind') == 'set':
                        print(f"        {arm}: {r['role']} set, d2 {r.get('d2', float('nan')):.3e}, d1 "
                              f"{r.get('d1', float('nan')):.3e}, floor {r.get('floor', float('nan')):.3e}, U "
                              f"{r.get('U', float('nan')):.3e}, d {r.get('d', float('nan')):.3e}, "
                              f"{'ok' if r['ok'] else 'fails: ' + str(r.get('why'))}")

    print('\nE. Every set the rule formed in the rows (the changed reading, which keeps the members), with its group '
          'sizes at N = 24, 32, 40; a stored point is one with a record at N = 32 in M8.17\'s or M8.16.1\'s files')
    new40 = []
    for tag in ROWS:
        d, s = rows[tag], stored[tag]
        n = 0
        for k in sorted(d['both'], key=float):
            is_stored = keyed(s['cutoffs']['32']['points'], float(k)) is not None
            for x in set_rows(d, k):
                n += 1
                differ = len({tuple(z) for z in x['sizes']}) > 1
                alone = (any(v and v > 1 for v in x['sizes'][2]) and all(v == 1 for v in x['sizes'][0] + x['sizes'][1]))
                if alone:
                    new40.append((tag, float(k), is_stored))
                print(f"  {tag} {float(k):9.4f}{' (stored)' if is_stored else ''}: {x['role']} set at {x['c']:.6g}, "
                      f"{x['count']} eigenvalues, sizes {x['sizes']}; the link differs between cutoffs: {differ}; at "
                      f"N = 40 alone: {alone}; {'ok' if x['ok'] else 'fails: ' + str(x['why'])}")
        if not n:
            print(f'  {tag}: no set')
    print(f'  a new link at N = 40 alone: {len(new40)} {new40}; at a stored point: {sum(1 for x in new40 if x[2])}')

    print('\nF. Section 6, statement by statement')
    print(f'  the twelve keep their stored type and indices at N = 40: {kept} of 12')
    d = rows['T5_R2']
    for e, law in QUARTET.items():
        k = keyed(d['both'], e)
        p = d['cutoffs']['40']['points'][k]
        re40 = [g['c'][0] for g in off_axis(p)]
        re32 = off_axis(d['cutoffs']['32']['points'][k])[0]['c'][0]
        print(f"  T5's quartet at {e}, N = 40: real part {[round(x, 5) for x in re40]}, section 6 {sorted(law.values())}; "
              f'it moved {re32 - re40[0]:.4f} from N = 32, where the laws asked '
              + ', '.join(f'{n} {re32 - v:.3f}' for n, v in law.items())
              + f"; record {p['record']['type']}; the rule as built {d['readings'][k]['verdict']}, changed "
              f"{d['changed'][k]['verdict']}; classified {d['both'][k]['as_built']['classified']}")
    pts = d['cutoffs']['40']['points']
    first = min(float(k) for k in pts if float(k) >= 64 and pts[k]['record']['type'] == 'Hyperbolic')
    before = max(float(k) for k in pts if float(k) < first)
    print(f'  the quartet first off the axis at N = 40: {first:g}, after {before:g} '
          f"({pts[keyed(pts, before)]['record']['type']}); on the collision law at {zeros[2]:.3f}, with an Aitken limit "
          f'of {limit:.3f} (INFERRED); section 6 put it near 127 at N = 40, with a limit of 127.5 to 128')
    for N in grid.LADDER:
        pts = d['cutoffs'][str(N)]['points']
        k4 = [f"{float(k):g}" for k in sorted(pts, key=float) if pts[k]['record']['type'] == 'Elliptic'
              and pts[k]['record']['K'] == 4]
        print(f'  an Elliptic stretch with K = 4 before the quartet, N = {N}: {k4}')
    print(f'  a new link at N = 40 alone at a stored point of the rows: {sum(1 for x in new40 if x[2])}')


if __name__ == '__main__':
    main()
