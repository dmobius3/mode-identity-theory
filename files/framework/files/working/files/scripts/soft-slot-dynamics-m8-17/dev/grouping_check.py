"""The census run's grouping check, read-only (UB, 2026-10-26): at each point the convergence rule leaves Unresolved
on a read point of T3/R4 and T5/R2, the failing set's members at each cutoff, their spacings against each cutoff's link
tolerance, and where a spacing falls between two cutoffs' tolerances.

  python3 -I -B grouping_check.py BENCH

BENCH: M8.16.1's bench folder. It reads run/out/T3_R4.json and run/out/T5_R2.json and the frozen instrument's
convergence and linear modules, changes nothing, and opens no point outside K6's read Unresolved points: the five
points the run solved but did not read stay unread. At each point it first replays the frozen rule on the stored
summaries and refuses unless the replay gives the recorded verdict and reasons. T5J/R2 at eps = 0.25, read in the
record, is the control: the link-tolerance merge found there (DEVLOG.md entry 75) must be flagged."""
import json
import os
import sys

import numpy as np

BENCH = sys.argv[1]
sys.path.insert(0, BENCH)
from instrument import convergence as cv  # noqa: E402
from instrument import linear as ln  # noqa: E402

CASES = ('T3_R4', 'T5_R2')
CLOSED = {'T3_R4': (32.0,), 'T5_R2': (45.254834,)}
NS = ('16', '24', '32')
U = np.finfo(float).eps


def stop(m):
    raise SystemExit(f'STOPPED: {m}')


def tau(s, z):
    """The link tolerance at z for a cutoff's summary: max(margin, KAPPA_D sqrt(u ||A|| |z|)) (linear.py)."""
    return max(s['margin'], ln.KAPPA_D * np.sqrt(U * s['normA'] * abs(z)))


def read_sets(sums, band):
    """The groups the rule reads and their sets, as separation() builds them (convergence.py, the pending loop)."""
    levels = [s['groups'] for s in reversed(sums)]
    G = levels[0]
    tested = [i for i, g in enumerate(G) if abs(cv._c(g)) < band / 2 or g['cls'] != 'imag' or g['neg']]
    pending = [(i, 'tested') for i in tested]
    for i in tested:
        if G[i]['cls'] == 'imag':
            j = cv._opposite(G, i)
            if j is not None and j not in tested:
                pending.append((j, 'partner'))
    seen = {i for i, _ in pending}
    chains = {}
    while True:
        for i, _ in pending:
            if i not in chains:
                chains[i] = cv._chain(levels, i)
        sets = cv.merged_sets(levels, sorted({i for i, _ in pending if chains[i] is None}))
        new = []
        for i, role in pending:
            S = sets.get(i)
            if role != 'tested' or S is None or G[i]['cls'] != 'imag':
                continue
            near = cv._nearest_opposite(G, sorted(S[0]))
            if near is not None and near[1] not in seen:
                new.append((near[1], 'partner'))
                seen.add(near[1])
        if not new:
            break
        pending += new
    return levels, pending, chains, sets


def counterparts(lev, allg):
    """At a count change: at each cutoff whose set holds fewer eigenvalues than the fullest, the groups of the set's
    class and Krein sign that lie within the fullest cutoff's span of the set, widened by its least member spacing,
    marked in or out of the set; and how much of the shortfall the ones outside cover (UB). lev and allg are lowest
    cutoff first. Identifying a counterpart by proximity is a reading, not the rule's."""
    counts = [sum(g['size'] for g in gs) for gs in lev]
    full = max(counts)
    ref = [a for a, c in enumerate(counts) if c == full][0]
    key = cv._key(lev[ref][0])
    zs = [cv._c(g) for g in lev[ref]]
    w = min(abs(x - y) for p, x in enumerate(zs) for y in zs[p + 1:])
    lo, hi = min(z.imag for z in zs) - w, max(z.imag for z in zs) + w
    out = []
    for a, c in enumerate(counts):
        if c == full:
            continue
        ids = {id(g) for g in lev[a]}
        near = [g for g in allg[a] if cv._key(g) == key and lo <= cv._c(g).imag <= hi and abs(cv._c(g).real) <= w]
        extra = [g for g in near if id(g) not in ids]
        got = sum(g['size'] for g in extra)
        out.append(dict(cutoff=NS[a], short=full - c, outside=[(cv._c(g), g['size']) for g in extra],
                        covered=min(got, full - c), span=(lo, hi), ref=NS[ref]))
    return out


def window_margin(levels, S):
    """At a count change: the same-class, same-sign eigenvalue outside the set that comes nearest to the closure's
    window, as a multiple of the window's reach, twice the nearest candidate's distance from a member at an adjacent
    cutoff with more members (convergence.closure). levels highest first; None where there is no such eigenvalue."""
    key = cv._key(levels[0][sorted(S[0])[0]])
    cnt = [sum(levels[a][j]['size'] for j in S[a]) for a in range(len(levels))]
    best = None
    for a in range(len(levels)):
        for b in (a - 1, a + 1):
            if not 0 <= b < len(levels) or cnt[b] <= cnt[a]:
                continue
            for m in S[b]:
                zm = cv._c(levels[b][m])
                cand = sorted((abs(cv._c(h) - zm), j) for j, h in enumerate(levels[a]) if cv._key(h) == key)
                for d, j in cand:
                    if j in S[a] or cand[0][0] == 0:
                        continue
                    r = d / (2 * cand[0][0])
                    if best is None or r < best['ratio']:
                        best = dict(ratio=r, cutoff=NS[len(levels) - 1 - a], z=cv._c(levels[a][j]),
                                    of=NS[len(levels) - 1 - b], member=zm)
    return best


def listing(levels, S, pad=1.0):
    """Every same-class, same-sign eigenvalue within the set's range, widened by pad times that range, at each cutoff,
    lowest first, marked in the set or not: the data for a reading by proximity (UB)."""
    key = cv._key(levels[0][sorted(S[0])[0]])
    zs = [cv._c(levels[a][j]).imag for a in range(len(levels)) for j in S[a]]
    lo, hi = min(zs), max(zs)
    w = pad * (hi - lo)
    return [(NS[len(levels) - 1 - a], [(cv._c(g).imag, g['size'], j in S[a]) for j, g in enumerate(levels[a])
             if cv._key(g) == key and lo - w <= cv._c(g).imag <= hi + w and abs(cv._c(g).real) <= w])
            for a in reversed(range(len(levels)))]


def failing(sums, rd):
    """The rule's failing rows at a point, each with its members at N = 16, 24, 32 (lowest first)."""
    res = cv.separation(sums, band=rd['band'])
    if (res['verdict'], res['reasons']) != (rd['verdict'], rd['reasons']):
        stop('the replay differs from the record')
    levels, pending, chains, sets = read_sets(sums, rd['band'])
    out, seen = [], set()
    for row in [x for x in res['rows'] if not x['ok']]:
        top = row['c'] if row['kind'] == 'set' else [row['c']]
        if row['kind'] == 'set':
            want = sorted((round(x, 12), round(y, 12)) for x, y in top)
            hits = [S for S in sets.values() if S is not None and sorted(
                (round(cv._c(levels[0][j]).real, 12), round(cv._c(levels[0][j]).imag, 12))
                for j in sorted(S[0]) for _ in range(levels[0][j]['size'])) == want]
            lev = [[levels[a][j] for j in sorted(hits[0][a])] for a in range(3)]
            Sset = hits[0]
        else:
            z0 = complex(*top[0])
            hits = [js for js in chains.values() if js is not None and abs(cv._c(levels[0][js[0]]) - z0) < 1e-12]
            lev = [[levels[a][hits[0][a]]] for a in range(3)]
            Sset = None
        lev = lev[::-1]
        ident = (row['role'], row['kind'], tuple(sorted((round(z[0], 12), round(z[1], 12)) for z in top)))
        if ident in seen:
            continue
        seen.add(ident)
        zs = [[cv._c(g) for g in gs] for gs in lev]
        tol = [max(tau(sums[a], z) for z in zs[a]) for a in range(3)]
        sp = [min((abs(x - y) for p, x in enumerate(z) for y in z[p + 1:]), default=None) for z in zs]
        # directional: from each member at the lower cutoff to the nearest member at the higher one, so a member the
        # lower cutoff lacks does not enter it
        disp = [max(min(abs(x - y) for y in zs[b]) for x in zs[a]) for a, b in ((0, 1), (1, 2))]
        cross = [s for s in sp if s is not None and min(tol) < s <= max(tol)]
        changes = row['kind'] == 'set' and len({sum(g['size'] for g in gs) for gs in lev}) > 1
        cps = counterparts(lev, [list(L) for L in levels[::-1]]) if changes else None
        win = window_margin(levels, Sset) if changes else None
        near = listing(levels, Sset) if changes else None
        out.append(dict(role=row['role'], kind=row['kind'], why=row['why'] or 'U over a tenth of d', counterparts=cps, window=win, near=near,
                        counts=[sum(g['size'] for g in gs) for gs in lev], sizes=[sorted(g['size'] for g in gs) for gs in lev],
                        spacing=sp, tau=tol, cross=cross, disp=disp, d1=row.get('d1'), d2=row.get('d2'), floor=row.get('floor'),
                        centre=complex(*top[0]), top=[complex(*z) for z in top]))
    return res, out


def points():
    """(case, eps, key) at K6's read Unresolved points of the census rows, then the control."""
    for name in CASES:
        r = json.load(open(os.path.join(BENCH, 'run', 'out', f'{name}.json'), encoding='utf-8'))
        for e in [x['eps'] for x in r['checks']['rows'] if x['status'] == 'unresolved']:
            if any(abs(e - c) < 1e-3 for c in CLOSED[name]):
                stop(f'{name}: {e} is a closed point')
            key = [k for k in r['readings'] if abs(float(k) - e) < 1e-6]
            if len(key) != 1:
                stop(f'{name}: no single reading at {e}')
            yield name, e, r, key[0]
    r = json.load(open(os.path.join(BENCH, 'run', 'out', 'T5J_R2.json'), encoding='utf-8'))
    yield 'T5J_R2 (control)', 0.25, r, '0.25'


def main():
    rep = []
    for name, e, r, key in points():
        sums = [r['cutoffs'][N]['points'][key]['summary'] for N in NS]
        res, rows = failing(sums, r['readings'][key])
        rep.append(dict(case=name, eps=e, rows=rows, structure=len({cv._structure(s) for s in sums}) > 1))
    return rep


if __name__ == '__main__':
    rep = main()
    f = lambda x: '-' if x is None else f'{x:.1e}'
    for p in rep:
        print(f"\n{p['case']} at eps {p['eps']:.4g}" + ('; the cutoffs disagree on the structure' if p['structure'] else ''))
        for x in p['rows']:
            print(f"  {x['role']} {x['kind']} near {x['centre'].imag:.4f}i: {x['why']} | counts {x['counts']} | sizes "
                  f"{x['sizes']} | least spacing {', '.join(f(s) for s in x['spacing'])} | tolerance {f(min(x['tau']))} to "
                  f"{f(max(x['tau']))} | between two tolerances: {len(x['cross'])} | moves 16->24 {f(x['disp'][0])}, "
                  f"24->32 {f(x['disp'][1])}")
    for p in rep:
        for x in p['rows']:
            if x['window'] is not None or x['near'] is not None:
                w = x['window']
                print(f"\n{p['case']} at eps {p['eps']:.4g}, {x['role']} set near {x['centre'].imag:.4f}i: " + (
                    f"nearest same-sign eigenvalue outside it {w['ratio']:.2f} times the closure's reach (N = {w['cutoff']}, {w['z'].imag:.5f}i, "
                    f"from the N = {w['of']} member {w['member'].imag:.5f}i)" if w else 'no same-sign eigenvalue outside it'))
                for N, gs in x['near']:
                    print(f"    N = {N}: " + ', '.join(f"{z:.5f}i x{s}{' (in)' if i else ''}" for z, s, i in sorted(gs)))
    census = [x for p in rep if 'control' not in p['case'] for x in p['rows']]
    ctrl = [x for p in rep if 'control' in p['case'] for x in p['rows']]
    print(f"\ncensus points {sum('control' not in p['case'] for p in rep)}, failing readings {len(census)}, spacings "
          f"between two tolerances {sum(len(x['cross']) for x in census)}; least spacing "
          f"{min(s for x in census for s in x['spacing'] if s is not None):.2e}, largest tolerance "
          f"{max(t for x in census for t in x['tau']):.2e}; the control flags {sum(len(x['cross']) for x in ctrl)}")
