"""The numbers M8.15.2's scope memo cites, read from M8.15.1's two target records and, from v4 on, its two real-solver
control records (R1/R4 on C2a, R2/R4 on C3), and nothing else.

  python3 recon_numbers.py [locator folder]      default: M8.15.1's locator folder at MIT 324fde3, ../../soft-slot-dynamics-m8-15x-target1 from this file

For each primary step that ended Unresolved (structural subspace), at each level: the bisection's ends and failing
midpoint, the width at the failure, the counts at all three points, and the near-zero spectrum with each value's
static overlap with P. Then the interpolated zero of the crossing pair between the clean ends, the interval where
n(L) changes, and the gap between the two levels' n(L) intervals.

v2 (2026-10-12, after both units' review of the scope memo v1) adds: the slowest pair's overlap at every point of the
step; the eigenvalue that changes n(L), with its overlaps at the n(L) interval's ends; the identity angle a two-level
mixing model gives, asin of each clean end's crossing-pair overlap, summed, against the check's 0.9; the slopes'
relative difference; and the rotation doublet's level ratio at every common eps with both levels' checks passing.

v3 (2026-10-12, after both units' review of v2) adds a last section that reads no record: the bounds on the identity
comparison outside P at a clean end, from the structural subspace check's 0.9, and Unit A's two-level counterexample.

v4 (2026-10-12, after #625's adjudication) adds a last section: the misses of m against linear continuation that #625
read, against the target eps; the solution-continuity statistic, the miss over h2 (h1 + h2) / 2 against the reached eps,
on the targets (disclosure) and on the controls' ladders (the tolerance's basis); and the secondary's two paths at
level 3, from the critical eigenvalue's slopes and zeros. Every earlier output line is unchanged.

v5 (2026-10-12, after both units' review of v4) adds a last section: rule 11's comparisons as v5 specifies them, on
M8.15.1's steps (the targets', the secondary's and the controls'); the multiples of the controls' largest that give those
records one outcome; and decision 7's numbers from no record, Unit A's family with its ends far from the mixing. Every
earlier output line is unchanged.

v6 (2026-10-12, after both units' review of v5) adds a last section: Unit B's tighter bound on distinct genuine
directions outside P (Wielandt's inequality), the first-cell facts behind rule 11's registered consequence, and how far a
lone failing grid point's first midpoint lies from it on the targets' brackets. Every earlier output line is unchanged.

v7 (2026-10-12, after both units agreed to close rule 4's gap) adds a last section: the exchanged-lift threshold from the
two-level model, a counts-level simulation of rules 1 to 6 on the coupled mock under v6's rule 4 and under the fix, and a
rough two-level fit at the targets' failing midpoints (disclosure). Every earlier output line is unchanged.

v8 (2026-10-12, for REGISTER_5) adds the continuity tolerance to four figures: ten times the controls' largest statistic.
Every earlier output line is unchanged.

v9 (2026-10-12, after both units' review of REGISTER_5 v1) discloses the statistic over the controls' full ladders, beside
the registered basis, the control brackets' pools. Every earlier output line is unchanged."""
import json, math, os, sys

LOC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'soft-slot-dynamics-m8-15x-target1')


def point(pts, e):
    best = min(pts, key=lambda p: abs(p['eps'] - e))
    assert abs(best['eps'] - e) <= 1e-9 * e, (e, best['eps'])
    return best


def spectrum(p, n=6):
    pairs = sorted(zip(p['near_zero'], p['overlaps']), key=lambda t: abs(t[0]))[:n]
    return ', '.join(f'{v:+.3e} ({o:.2f})' for v, o in sorted(pairs))


nl_change, zero, slope, rot = {}, {}, {}, {}
for case in ('T2_R4', 'T3_R5'):
    rec = json.load(open(os.path.join(LOC, 'out', f't1_{case}.json')))
    b = next(x for x in rec['brackets'] if x['label'] == 'primary')
    for lv in ('3', '2'):
        pts = b['points'][lv]
        for s in b['levels'][lv]['steps']:
            if s['status'] != 'Unresolved' or s.get('reason') != 'structural subspace':
                continue
            lo, mid, hi = point(pts, s['lo']), point(pts, s['failed_at']), point(pts, s['hi'])
            print(f'== {case} level {lv}: ends {lo["eps"]:.6f}, {hi["eps"]:.6f}; fails at {mid["eps"]:.6f}; '
                  f'width at the failure {(hi["eps"] - lo["eps"]) / lo["eps"]:.2e} of the lower end')
            for tag, p in (('lo ', lo), ('mid', mid), ('hi ', hi)):
                print(f'   {tag} {p["eps"]:.6f}: n(L) {p["nL"]}, n(B|G_tol) {p["nB"]}, h {p["h"]}, n_S {p["nS"]}, '
                      f'balanced {p["balanced"]}, checks {p["checks"] or "none"}')
                print(f'       near zero (overlap with P): {spectrum(p)}')
            # the rotation doublet at each clean end: the most negative near-zero value with overlap at least 0.9
            rot[(case, lv)] = [min(v for v, o in zip(p['near_zero'], p['overlaps']) if o >= 0.9) for p in (lo, hi)]
            print('   slowest pair overlap: ' + ', '.join(f'{p["eps"]:.6f} {p["slowest_pair_overlap"]:.3g}'
                                                       for p in sorted(pts, key=lambda p: p['eps'])
                                                       if lo['eps'] - 1e-9 <= p['eps'] <= hi['eps'] + 1e-9))
            side = 'upper' if mid['nL'] == lo['nL'] else ('lower' if mid['nL'] == hi['nL'] else None)
            iv = (mid['eps'], hi['eps']) if side == 'upper' else (lo['eps'], mid['eps'])
            nl_change[(case, lv)] = iv
            print(f'   n(L) at the midpoint equals the {"lower" if side == "upper" else "upper"} end: n(L) changes in '
                  f'({iv[0]:.6f}, {iv[1]:.6f}]')
            # the eigenvalue that changes n(L): at the n(L) interval's end with the smaller n(L), the smallest positive
            # doublet; at the other end, the largest negative doublet
            def doublets(p):
                return [(v, o) for v, o in zip(p['near_zero'], p['overlaps'])
                        if sum(1 for w in p['near_zero'] if abs(w - v) <= 1e-6 * abs(v)) == 2]   # numerics split a doublet near 1e-8
            ea, eb = (mid, hi) if side == 'upper' else (lo, mid)
            em, ep_ = (ea, eb) if ea['nL'] < eb['nL'] else (eb, ea)
            vm = min((v, o) for v, o in doublets(em) if v > 0)
            vp = max((v, o) for v, o in doublets(ep_) if v < 0)
            (va, oa), (vb, ob) = (vm, vp) if em is ea else (vp, vm)
            print(f'   the eigenvalue that changes n(L): {va:+.3e} ({oa:.2f}) at {ea["eps"]:.6f} -> {vb:+.3e} ({ob:.2f}) '
                  f'at {eb["eps"]:.6f}')
            # the crossing pair: at each clean end, the near-zero values whose overlap with P is below 0.9 and whose
            # sign differs between the ends; its zero, interpolated linearly as the locator's root rule does
            gl = sorted(v for v, o in zip(lo['near_zero'], lo['overlaps']) if o < 0.9)
            gh = sorted(v for v, o in zip(hi['near_zero'], hi['overlaps']) if o < 0.9)
            a = min(gl, key=abs)
            c = min(gh, key=abs)
            oa = next(o for v, o in zip(lo['near_zero'], lo['overlaps']) if v == a)
            oc = next(o for v, o in zip(hi['near_zero'], hi['overlaps']) if v == c)
            th = math.degrees(math.asin(oa)) + math.degrees(math.asin(oc))
            print(f'   two-level model: the crossing pair at the clean ends, overlaps {oa:.4f} and {oc:.4f}: angle '
                  f'{th:.1f} deg, cosine {math.cos(math.radians(th)):.3f}, against 0.9 ({math.degrees(math.acos(0.9)):.1f} deg)')
            if (a < 0) != (c < 0):
                t = a / (a - c)
                z = lo['eps'] + (hi['eps'] - lo['eps']) * t
                zero[(case, lv)], slope[(case, lv)] = z, (c - a) / (hi['eps'] - lo['eps'])
                inside = iv[0] < z <= iv[1]
                gap = 0.0 if inside else min(abs(z - iv[0]), abs(z - iv[1]))
                print(f'   the genuine pair {a:+.3e} -> {c:+.3e}: interpolated zero {z:.6f}; '
                      f'{"inside" if inside else "outside"} the n(L) interval, gap {gap / z:.2e} to {max(abs(z - iv[0]), abs(z - iv[1])) / z:.2e}')
            else:
                print(f'   the nearest genuine values {a:+.3e}, {c:+.3e} do not change sign between the clean ends')
for case in ('T2_R4', 'T3_R5'):
    (a3, b3), (a2, b2) = nl_change[(case, '3')], nl_change[(case, '2')]
    print(f'== {case}: level 2\'s n(L) change minus level 3\'s, relative to level 3: '
          f'{(a2 - b3) / b3:+.2%} to {(b2 - a3) / a3:+.2%}')
    if (case, '3') in zero and (case, '2') in zero:
        z3, z2 = zero[(case, '3')], zero[(case, '2')]
        print(f'== {case}: level 2\'s interpolated zero minus level 3\'s, relative to level 3: {(z2 - z3) / z3:+.2%}; '
              f'the genuine pair\'s slope, level 3 {slope[(case, "3")]:+.4e}, level 2 {slope[(case, "2")]:+.4e} per unit eps')
    r3, r2 = rot[(case, '3')], rot[(case, '2')]
    print(f'== {case}: the rotation doublet at the clean ends, level 2 over level 3: lower {r2[0] / r3[0]:.1f}, upper {r2[1] / r3[1]:.1f}')
    if (case, '3') in slope and (case, '2') in slope:
        s3, s2 = slope[(case, '3')], slope[(case, '2')]
        print(f'== {case}: the genuine pair\'s slopes differ between the levels by {abs(s2 - s3) / abs(s3):.2%} of level 3\'s')
for case in ('T2_R4', 'T3_R5'):
    rec = json.load(open(os.path.join(LOC, 'out', f't1_{case}.json')))
    b = next(x for x in rec['brackets'] if x['label'] == 'primary')
    at = {}
    for lv in ('3', '2'):
        for p in b['points'][lv]:
            if not p['checks']:
                at.setdefault(round(p['eps'], 9), {})[lv] = min(v for v, o in zip(p['near_zero'], p['overlaps']) if o >= 0.9)
    common = sorted((e, d['2'] / d['3']) for e, d in at.items() if '3' in d and '2' in d)
    print(f'== {case}: the rotation doublet, level 2 over level 3, at every common eps with both levels clean: '
          + ', '.join(f'{e:.6g} {r:.1f}' for e, r in common))

# v3: decision 7's numbers, from no record
c = 0.9
sb = math.sqrt(1 - c * c)                  # the most a vector M-orthogonal to a span within acos(0.9) of P overlaps P
worst = (1 - sb * sb) * c - sb * sb
print(f'== decision 7, the comparison outside P at a clean end: overlap with P at most {sb:.3f}; the projection keeps at '
      f'least {math.sqrt(1 - sb * sb):.1f} of the norm; Gram eigenvalues at least {1 - sb * sb:.2f}; two M-orthogonal genuine '
      f'vectors agree outside P to at most {sb * sb / (1 - sb * sb):.3f}; the worst full cosine it passes is {worst:.3f} '
      f'({math.degrees(math.acos(worst)):.1f} deg)')
k, d = 1.1, 1.0                            # Unit A: L(g) = [[g, k], [k, -d]], P = span(e2)
def branches(g):
    out = []
    for sgn in (-1, 1):
        lam = ((g - d) + sgn * math.sqrt((g + d) ** 2 + 4 * k * k)) / 2
        v = (k, lam - g)
        n = math.hypot(*v)
        out.append((lam, (v[0] / n, v[1] / n)))
    return out                             # lower, upper
ends = {}
for g in (-4.5, 3.0):
    b = branches(g)
    gi = max((0, 1), key=lambda i: abs(b[i][1][0]))
    ends[g] = (gi, b[gi][1])
    print(f'== Unit A\'s counterexample at g = {g:+}: structural overlap {abs(b[1 - gi][1][1]):.3f}; the genuine-like vector '
          f'is on the {"lower" if gi == 0 else "upper"} branch, overlap with P {abs(b[gi][1][1]):.3f}')
(_, u), (_, w) = ends[-4.5], ends[3.0]
print(f'== Unit A\'s counterexample: full cosine {abs(u[0] * w[0] + u[1] * w[1]):.3f}; outside P {abs(math.copysign(1, u[0] * w[0])):.3f}; '
      f'n(L) changes at g = {-k * k / d:.2f}; its eigenvector\'s lift fraction {k * k / (k * k + d * d):.3f}')

# v4: solution continuity and the secondary's two paths, after #625's adjudication; reads the target and control records
REC = {c: json.load(open(os.path.join(LOC, 'out', f't1_{c}.json'))) for c in ('T2_R4', 'T3_R5', 'C2a_R4_R1R4', 'C3_R4_R2R4')}
def bracket(c, label):
    return next(x for x in REC[c]['brackets'] if x['label'] == label)
def continuation(pts, reached):
    """At each point after the first two, in increasing eps: its eps, the step h2 to it, the miss of m against the linear
    continuation from the two evaluated points before it, and that miss over h2 (h1 + h2) / 2."""
    x = (lambda p: p['frozen']['eps_reached']) if reached else (lambda p: p['eps'])
    ps = sorted(pts, key=x)
    out = []
    for a, b, c in zip(ps, ps[1:], ps[2:]):
        h1, h2 = x(b) - x(a), x(c) - x(b)
        miss = abs(c['frozen']['m'] - b['frozen']['m'] - (b['frozen']['m'] - a['frozen']['m']) * h2 / h1)
        out.append((c['eps'], h2, miss, miss / (h2 * (h1 + h2) / 2)))
    return out
def at(rows, e):
    return next(r for r in rows if abs(r[0] - e) <= 1e-9 * e)
sec = bracket('T3_R5', 'secondary')
sw = {'3': sec['levels']['3']['steps'][1]['hi'], '2': sec['levels']['2']['steps'][0]['hi']}   # #625: these steps join two paths
small = max(r[2] for c in ('T2_R4', 'T3_R5') for lv in ('3', '2')
            for r in continuation(bracket(c, 'primary')['points'][lv], False) if r[1] <= 0.026)
miss = {lv: at(continuation(sec['points'][lv], False), sw[lv])[2] for lv in ('3', '2')}
print(f"== v4, #625's continuity reading (the target eps): the primaries' largest miss at steps of 0.026 or less {small:.2e}; "
      f"across the switches, level 3 at {sw['3']:.6f} {miss['3']:.2e}, level 2 at {sw['2']:.6f} {miss['2']:.2e}")
qc = {c: max(r[3] for lv in ('3', '2') for r in continuation(bracket(c, 'control')['points'][lv], True))
      for c in ('C2a_R4_R1R4', 'C3_R4_R2R4')}
qt = max(r[3] for r in continuation(bracket('C2a_R4_R1R4', 'control')['points']['3'], False))
print(f"== v4, the continuity statistic on the controls' ladders (the reached eps): C2a at most {qc['C2a_R4_R1R4']:.1e}, "
      f"C3 at most {qc['C3_R4_R2R4']:.1e}; C2a at level 3 against the target eps instead {qt:.1e}")
qp = {c: max(r[3] for lv in ('3', '2') for r in continuation(bracket(c, 'primary')['points'][lv], True)) for c in ('T2_R4', 'T3_R5')}
qs = {lv: at(continuation(sec['points'][lv], True), sw[lv])[3] for lv in ('3', '2')}
print(f"== v4, the continuity statistic on the targets (the reached eps), disclosure: the primaries at most {qp['T2_R4']:.1e} "
      f"(T2/R4) and {qp['T3_R5']:.1e} (T3/R5), {max(qp.values()) / max(qc.values()):.1f} times the controls' largest; "
      f"across the switches {qs['3']:.1f} (level 3) and {qs['2']:.1f} (level 2), {qs['3'] / max(qc.values()):.1e} and "
      f"{qs['2'] / max(qc.values()):.1e} times it")
# the secondary's two paths at level 3: the critical eigenvalue, the genuine near-zero value nearest zero, on the ladder's
# grid points around the grid cell that holds level 3's two steps, and at the points the bisection evaluated inside it
p3 = sec['points']['3']
lo_b, hi_b = sec['brackets']['3']
grid = [lo_b + k * (hi_b - lo_b) / 8 for k in range(9)]
cell = max(k for k in range(8) if grid[k] <= sec['levels']['3']['steps'][0]['lo'])
def crit(e):
    p = point(p3, e)
    return min((v for v, o in zip(p['near_zero'], p['overlaps']) if o < 0.9), key=abs)
lad = [(grid[k], crit(grid[k])) for k in range(cell - 1, cell + 3)]
slopes = [(b[1] - a[1]) / (b[0] - a[0]) for a, b in zip(lad, lad[1:])]
z_lad = grid[cell] - crit(grid[cell]) / slopes[1]
two = sorted((p['eps'], crit(p['eps'])) for p in p3 if grid[cell] * (1 + 1e-9) < p['eps'] < grid[cell + 1] * (1 - 1e-9))
me, ml = sum(e for e, _ in two) / len(two), sum(v for _, v in two) / len(two)
s = sum((e - me) * (v - ml) for e, v in two) / sum((e - me) ** 2 for e, _ in two)
z = me - ml / s
res = max(abs(v - s * (e - z)) for e, v in two)
ratio = [s / t for t in slopes]
print(f"== v4, the secondary's two paths at level 3: on the ladder's path the critical eigenvalue's local slopes from "
      f"{lad[0][0]:.6f} to {lad[-1][0]:.6f} are " + ', '.join(f'{t:+.3f}' for t in slopes) + f", and it crosses zero near "
      f"{z_lad:.2f}; on the second path, over the {len(two)} points the bisection evaluated between {grid[cell]:.6f} and "
      f"{grid[cell + 1]:.6f}, it fits {s:.3f}(eps - {z:.2f}), residuals at most {res:.1e}; the slope ratio {max(ratio):.1f} "
      f"to {min(ratio):.1f}")

# v5: rule 11 as v5 specifies it, on M8.15.1's steps, and decision 7's numbers from no record (after both units' review)
def pool_of(c, label, lv):
    """The bracket's evaluated points at one level in increasing reached eps, as the record holds them: no guard ran on
    these brackets, so they are the pool when the scan and its bisections ended."""
    return sorted(bracket(c, label)['points'][lv], key=lambda p: p['frozen']['eps_reached'])
def stat5(a, b, c):
    """The miss of c's m against the line through a and b, over h2 (h1 + h2) / 2; None for a degenerate comparison."""
    xa, xb, xc = (p['frozen']['eps_reached'] for p in (a, b, c))
    h1, h2 = xb - xa, xc - xb
    if not (h1 > 1e-9 * xc and h2 > 1e-9 * xc):
        return None
    ma, mb, mc = (p['frozen']['m'] for p in (a, b, c))
    return abs(mc - mb - (mb - ma) * h2 / h1) / (h2 * (h1 + h2) / 2)
def rule11(c, label, lv, s):
    """One step's comparisons: along its span (every pool point in it but the lowest, each against the two pool points
    immediately below it) and across it (the upper reading end against the lower reading end and the point below that)."""
    ps = pool_of(c, label, lv)
    a, b = bracket(c, label)['brackets'][lv]
    usable = [g for g in (a + (b - a) * k / 8 for k in range(9))
              if any(abs(p['eps'] - g) <= 1e-9 * g and not p['checks'] for p in ps)]
    u = max(g for g in usable if g <= s['lo'] * (1 + 1e-12))
    w = min(g for g in usable if g >= s['hi'] * (1 - 1e-12))
    rd = s.get('reading')
    lo_s, hi_s = (min(u, rd[0]), max(w, rd[1])) if rd else (u, w)
    idx = [i for i, p in enumerate(ps) if lo_s * (1 - 1e-12) <= p['eps'] <= hi_s * (1 + 1e-12)]
    along = [(ps[i]['eps'], stat5(ps[i - 2], ps[i - 1], ps[i]) if i >= 2 else None) for i in idx[1:]]
    across = []
    if rd:
        il, iu = (next(i for i, p in enumerate(ps) if abs(p['eps'] - e) <= 1e-9 * e) for e in rd)
        across = [(ps[iu]['eps'], stat5(ps[il - 1], ps[il], ps[iu]) if il >= 1 else None)]
    return (u, w), along + across
def worst(rows):
    return max(q for _, q in rows)
comp = {(c, label, lv, k): rule11(c, label, lv, s) for c, label in (('T2_R4', 'primary'), ('T3_R5', 'primary'),
        ('T3_R5', 'secondary'), ('C2a_R4_R1R4', 'control'), ('C3_R4_R2R4', 'control'))
        for lv in bracket(c, label)['points'] for k, s in enumerate(bracket(c, label)['levels'][lv]['steps'])}
missing = sum(1 for _, rows in comp.values() for _, q in rows if q is None)
dups = sum(1 for c, label in (('T2_R4', 'primary'), ('T3_R5', 'primary'), ('T3_R5', 'secondary'), ('C2a_R4_R1R4', 'control'),
           ('C3_R4_R2R4', 'control')) for lv in bracket(c, label)['points']
           for p, q in zip(pool_of(c, label, lv), pool_of(c, label, lv)[1:]) if abs(q['eps'] - p['eps']) <= 1e-9 * q['eps'])
q5 = {c: max(worst(rows) for (cc, label, lv, k), (_, rows) in comp.items() if cc == c and label != 'secondary')
      for c in ('T2_R4', 'T3_R5', 'C2a_R4_R1R4')}
print(f"== v5, rule 11 on M8.15.1's steps (the reached eps, the completed pool, forward extrapolation): the primaries at most "
      f"{q5['T2_R4']:.1e} (T2/R4) and {q5['T3_R5']:.1e} (T3/R5), {max(q5['T2_R4'], q5['T3_R5']) / max(qc.values()):.1f} times the "
      f"controls' largest; the controls' steps at most {q5['C2a_R4_R1R4']:.1e}; {missing} comparisons lack their two points, "
      f"and {dups} pairs of targets coincide")
(u3, w3), rows3 = comp[('T3_R5', 'secondary', '3', 0)]
(u2, w2), rows2 = comp[('T3_R5', 'secondary', '2', 0)]
r3 = dict(rows3)
ps3 = pool_of('T3_R5', 'secondary', '3')
m1 = (u3 + w3) / 2                     # the bisection's first midpoint, which took the lower end's counts
m2 = (m1 + w3) / 2                     # its second, which matched neither end and split the interval
first, upper = point(ps3, m1), point(ps3, m2)
sub = [p for p in ps3 if first['eps'] * (1 - 1e-12) <= p['eps'] <= upper['eps'] * (1 + 1e-12)]
subq = max(stat5(a, b, c) for a, b, c in zip(sub, sub[1:], sub[2:]))
ps2 = pool_of('T3_R5', 'secondary', '2')
i2 = next(i for i, p in enumerate(ps2) if abs(p['eps'] - grid[cell + 1]) <= 1e-9 * grid[cell + 1])
nxt = min((e for e in r3 if e > first['eps']), key=lambda e: e)
print(f"== v5, rule 11 on #625's secondary: level 3's starting interval {u3:.6f} to {w3:.6f}, at {first['eps']:.6f} "
      f"{r3[first['eps']]:.1e}, at {nxt:.6f} {r3[nxt]:.1e}, at {w3:.6f} {r3[w3]:.1f}; level 2's, {u2:.6f} to {w2:.6f}, at "
      f"{w2:.6f} {worst(rows2):.1f}; the first step's split sub-interval alone, {first['eps']:.6f} to {upper['eps']:.6f}, at most "
      f"{subq:.1e}; level 2's grid switch at {ps2[i2]['eps']:.6f} {stat5(ps2[i2 - 2], ps2[i2 - 1], ps2[i2]):.1e}")
lo_m = max(q5['T2_R4'], q5['T3_R5']) / max(qc.values())
hi_m = min(worst(rows3), worst(rows2)) / max(qc.values())
print(f"== v5, the multiples of the controls' largest that give M8.15.1's records one outcome (the primaries pass, both "
      f"switches stop): {lo_m:.1f} to {hi_m:.1e}")
far = []
for g0 in (20.0, 60.0):
    e = {}
    for g in (-g0, g0):
        bb = branches(g)
        gi = max((0, 1), key=lambda i: abs(bb[i][1][0]))
        e[g] = (gi, bb[gi][1])
    (i1, u_), (i2_, w_) = e[-g0], e[g0]
    far.append((g0, abs(u_[0] * w_[0] + u_[1] * w_[1]), i1, i2_))
cth = math.sqrt(1 - c * c)
print(f"== v5, decision 7 from no record: Unit A's family with the ends at g = -{far[0][0]:g} and {far[0][0]:g}, full cosine "
      f"{far[0][1]:.3f}; at -{far[1][0]:g} and {far[1][0]:g}, {far[1][1]:.3f}; the genuine-like vector on the "
      f"{'lower' if far[0][2] == 0 else 'upper'} branch at the first end and the {'lower' if far[0][3] == 0 else 'upper'} at the "
      f"second, at both; (b)'s {cth:.3f} holds in the two-level model for kappa/delta at most {cth / math.sqrt(1 - cth * cth):.3f}")

# v6: the bound on distinct genuine directions, the first cell, and the lone failing grid point (after both units' v5 review)
lo_g = 1 - sb * sb                     # the projected Gram eigenvalues of a genuine pair lie in [lo_g, 1]
print(f"== v6, distinct genuine directions outside P: the projected Gram eigenvalues lie in [{lo_g:.2f}, 1], so by Wielandt's "
      f"inequality two M-orthogonal genuine vectors agree outside P to at most {(1 - lo_g) / (1 + lo_g):.3f}")
first_cell = {}
for cc in ('T2_R4', 'T3_R5'):
    bp = bracket(cc, 'primary')
    for lv in ('3', '2'):
        a, b = bp['brackets'][lv]
        low = min(p['eps'] for p in bp['points'][lv])
        cell1 = a + (b - a) / 8
        first_cell[(cc, lv)] = (bp['region'][0], a, low, cell1, sum(1 for s in bp['levels'][lv]['steps'] if s['lo'] < cell1 * (1 - 1e-12)))
t3 = {first_cell[('T3_R5', lv)][:4] for lv in ('3', '2')}
assert len(t3) == 1
reg3, a3, low3, c3 = t3.pop()
assert abs(reg3 - a3) <= 1e-12 * a3 and abs(low3 - a3) <= 1e-12 * a3
n3 = sum(first_cell[('T3_R5', lv)][4] for lv in ('3', '2'))
reg2, a2 = first_cell[('T2_R4', '3')][:2]
nfail = sum(1 for c_ in ('T2_R4', 'T3_R5') for l_ in ('3', '2') for a, b in [bracket(c_, 'primary')['brackets'][l_]]
            for k in range(9) for q in bracket(c_, 'primary')['points'][l_]
            if abs(q['eps'] - (a + (b - a) * k / 8)) <= 1e-9 * q['eps'] and q['checks'])
gap = max(abs((x + y) / 2 - z) / z for c_, l_ in (('T2_R4', '3'), ('T3_R5', '3'))
          for a, b in [bracket(c_, 'primary')['brackets'][l_]]
          for x, z, y in [(a + (b - a) * (k - 1) / 8, a + (b - a) * k / 8, a + (b - a) * (k + 1) / 8) for k in range(1, 8)])
print(f"== v6, the first cell: T3/R5's guard region and primary bracket both start at {a3:.6f}, the pool's lowest point at both "
      f"levels, so a step in its first cell, to {c3:.6f}, would have a compared point with one predecessor; M8.15.1 has {n3} steps "
      f"there. T2/R4's guard region starts at {reg2:.6f}, below its bracket's {a2:g}. A lone failing grid point's first midpoint "
      f"lies within {gap:.1e} of it, relative, on the targets' brackets, and M8.15.1's primaries have {nfail} failing grid points")

# v7: the exchanged-lift points, from the two-level model and a counts-level simulation of rules 1 to 6 on the coupled
# mock (reads no record), then a rough two-level fit at the targets' failing midpoints (disclosure)
import numpy as np
cth, sth = c, math.sqrt(1 - c * c)
cw = (cth * cth - sth * sth) / (sth * cth)      # the window: |g + delta| < cw kappa, where the structural subspace check fails
kmin = (cw + math.sqrt(cw * cw + 4)) / 2         # above this kappa/delta a clean interval separates the window from the n(L) change
def mpoint(eps, kap, a=0.05, r=1.0130, dl=1e-5):
    """The coupled mock's counts at eps: e0 exact zero, e1 a lift at -dl, two doubled blocks [[a (r - eps), kap], [kap, -dl]]."""
    g, vals, vecs = a * (r - eps), [1e-14, -dl], [np.eye(6)[0], np.eye(6)[1]]
    for gi, li in ((4, 2), (5, 3)):
        w, v = np.linalg.eigh(np.array([[g, kap], [kap, -dl]]))
        for j in range(2):
            x = np.zeros(6); x[gi], x[li] = v[0, j], v[1, j]
            vals.append(w[j]); vecs.append(x)
    vals, vecs = np.array(vals), np.array(vecs).T
    ov = np.linalg.norm(vecs[:4, :], axis=0)
    st = ov >= c
    ok = st.sum() == 4 and np.linalg.svd(vecs[:4, st], compute_uv=False).min() >= c
    return dict(eps=eps, nL=int((vals < -1e-9).sum()), nS=int(((vals < -1e-9) & st).sum()), ok=bool(ok))
def mbisect(lo, hi, kap, out, fix, failed=False):
    """Rules 1 to 6 on counts alone. fix: after a failure, a clean midpoint with one side's n(L) and an n_S below that
    side's is passed on n(L), never a clean end; otherwise such a point, after a failure, makes the step Unresolved."""
    lo_n, hi_n, lo_c, hi_c, terminal = lo, hi, lo, hi, lo['nL'] == hi['nL']
    while hi_n['eps'] - lo_n['eps'] > 1e-3 * lo_n['eps']:
        m = mpoint((lo_n['eps'] + hi_n['eps']) / 2, kap)
        if not m['ok']:
            if terminal:
                out.append('Unresolved'); return
            failed = True
            if m['nL'] in (lo_n['nL'], hi_n['nL']):
                lo_n, hi_n = (m, hi_n) if m['nL'] == lo_n['nL'] else (lo_n, m)
                continue
            out.append('Unresolved'); return
        cm = (m['nL'], m['nS'])
        if cm == (lo_c['nL'], lo_c['nS']): lo_n = lo_c = m
        elif cm == (hi_c['nL'], hi_c['nS']): hi_n = hi_c = m
        elif failed and fix and m['nL'] in (lo_c['nL'], hi_c['nL']) and m['nS'] < (lo_c if m['nL'] == lo_c['nL'] else hi_c)['nS']:
            lo_n, hi_n = (m, hi_n) if m['nL'] == lo_n['nL'] else (lo_n, m)
        elif failed:
            out.append('Unresolved'); return
        else:
            mbisect(lo_n, m, kap, out, fix, failed); mbisect(m, hi_n, kap, out, fix, failed); return
    out.append('genuine-looking' if hi_c['nS'] == lo_c['nS'] and hi_c['nL'] != lo_c['nL'] else 'Unresolved')
ratios = (0.3, 1, 2, 2.5, 3, 4, 6, 8)
res7 = {}
for fix in (False, True):
    for q in ratios:
        grid = [mpoint(0.8 + 0.05 * k, q * 1e-5) for k in range(9)]
        out = []
        for lo, hi in zip(grid[:-1], grid[1:]):
            if (lo['nL'], lo['nS']) != (hi['nL'], hi['nS']):
                mbisect(lo, hi, q * 1e-5, out, fix)
        res7[(fix, q)] = 'located' if out == ['genuine-looking'] else 'Unresolved'
fmt = lambda fix, want: ', '.join(f'{q:g}' for q in ratios if res7[(fix, q)] == want) or 'none'
print(f"== v7, the exchanged-lift points (two-level model): the structural subspace check fails where |g + delta| < "
      f"{cw:.3f} kappa, so above kappa/delta = {kmin:.2f} a clean interval separates that window from the n(L) change, where "
      f"the coupled lifts sit above zero; on the coupled mock (a = 0.05, delta = 1e-5, r = 1.0130), counts only, v6's rule 4 "
      f"classifies genuine-looking at kappa/delta {fmt(False, 'located')} and leaves Unresolved {fmt(False, 'Unresolved')}; "
      f"with the fix, genuine-looking at {fmt(True, 'located')}, Unresolved {fmt(True, 'Unresolved')}")
fits = []
for cc in ('T2_R4', 'T3_R5'):
    bp = bracket(cc, 'primary')
    for lv in ('3', '2'):
        s_ = next(x for x in bp['levels'][lv]['steps'] if x.get('reason') == 'structural subspace')
        pts_ = {round(p['eps'], 9): p for p in bp['points'][lv]}
        mid_ = pts_[round(s_['failed_at'], 9)]
        reps = []
        for v, o in sorted(zip(mid_['near_zero'], mid_['overlaps'])):
            if 0.3 < o < 0.95 and not any(abs(v - w) <= 1e-6 * abs(v) for w, _ in reps):
                reps.append((v, o))
        (la, oa), (lb, ob) = reps
        hll, hgg = la * oa ** 2 + lb * ob ** 2, la * (1 - oa ** 2) + lb * (1 - ob ** 2)
        kap, dl = abs(la - lb) * oa * math.sqrt(1 - oa ** 2), -hll
        p_lo, p_hi = pts_[round(s_['lo'], 9)], pts_[round(s_['hi'], 9)]
        glo = min((v for v, o in zip(p_lo['near_zero'], p_lo['overlaps']) if o < c), key=abs)
        ghi = min((v for v, o in zip(p_hi['near_zero'], p_hi['overlaps']) if o < c), key=abs)
        sl = (ghi - glo) / (s_['hi'] - s_['lo'])
        rg = s_['failed_at'] - hgg / sl
        e_nl, e_mix, half = rg - kap * kap / (sl * dl), rg - dl / sl, cw * kap / abs(sl)
        btw = tuple(sorted((e_mix + half if sl < 0 else e_mix - half, e_nl))) if kap / dl > kmin else None
        a_, b_ = (s_['failed_at'], s_['hi']) if mid_['nL'] == p_lo['nL'] else (s_['lo'], s_['failed_at'])
        hit = None
        while b_ - a_ > 1e-3 * a_:
            m_ = (a_ + b_) / 2
            if btw is not None and btw[0] < m_ < btw[1]:
                hit = m_; break
            a_, b_ = (m_, b_) if m_ < e_nl else (a_, m_)
        fits.append((cc, lv, kap / dl, btw, hit))
print("== v7, disclosure: a rough two-level fit at each failing midpoint gives kappa/delta " + '; '.join(
      f"{cc.replace('_', '/')} level {lv} {q:.2f}" for cc, lv, q, _, _ in fits) + '; ' + '; '.join(
      f"{cc.replace('_', '/')} level {lv}'s next midpoints meet the clean interval {b[0]:.4f} to {b[1]:.4f} at {h:.4f}"
      for cc, lv, q, b, h in fits if h is not None) + '; no other step meets one')

# v8: the continuity tolerance REGISTER_5 registers: ten times the controls' largest statistic, to four figures
cmax = max((r[3], c_, lv, r[0]) for c_ in ('C2a_R4_R1R4', 'C3_R4_R2R4') for lv in ('3', '2')
           for r in continuation(bracket(c_, 'control')['points'][lv], True))
print(f"== v8, the continuity tolerance: the controls' largest statistic is {cmax[0]:.4e} ({cmax[1].split('_')[0]}, level {cmax[2]}, "
      f"at {cmax[3]:.6f}); ten times it is {10 * cmax[0]:.4e}")

# v9: the controls' full ladders, disclosed beside the registered basis (the control brackets' pools), after both units'
# review of REGISTER_5 v1
def ladder_max(c_):
    rec_ = REC[c_]
    best = None
    for lv, pts in (('3', rec_['points']), ('2', rec_['level2'])):
        ps = sorted(pts, key=lambda p: p['eps_reached'])
        for a, b, d in zip(ps, ps[1:], ps[2:]):
            h1, h2 = b['eps_reached'] - a['eps_reached'], d['eps_reached'] - b['eps_reached']
            q = abs(d['m'] - b['m'] - (b['m'] - a['m']) * h2 / h1) / (h2 * (h1 + h2) / 2)
            if best is None or q > best[0]:
                best = (q, lv, d['eps'], ps[0]['eps'], ps[-1]['eps'])
    return best
lm = max((ladder_max(c_) + (c_,) for c_ in ('C2a_R4_R1R4', 'C3_R4_R2R4')), key=lambda t: t[0])
print(f"== v9, disclosure: over the controls' full ladders, {lm[3]:g} to {lm[4]:g}, the statistic reaches {lm[0]:.4e} "
      f"({lm[5].split('_')[0]}, level {lm[1]}, at {lm[2]:g}); the registered basis is the control brackets' pools, {cmax[0]:.4e}")
