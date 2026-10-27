#!/usr/bin/env python3
"""A plumbing pass of the census run's instrument side, on the GO-list control C2a, at cutoffs the registered run never
uses (12, 16, 20), never scored, and outside the run: development only (BOUNDARY.md's GO list; M8.16.1's plumbing pass
ran its driver at the same cutoffs).

Usage: plumbing_census.py

It checks, with real solves on C2a in R4:
  1. the recomputed path (census.Cutoff.path and census.readings_of) equals driver.run_case's own output, field for
     field, timings aside, at every point to 0.5, by census_lib.gate_full: the replay reproduces run_case bit for bit;
  2. census_lib.locate runs whole on a bracket (0.354, 0.5), its recomputed path reproduced, and reads the bracket as
     the records give it (C2a's n(L) is constant, so 'unchanged');
  3. census_lib.bisect runs on the same bracket with real continuations from both ends, with the upper end's n(L)
     declared one more than the record's, so that every midpoint keeps the lower half's n(L) and the bisection walks to
     the upper end: each midpoint solved twice, recorded, K1 and n(L) read, the two solutions' aligned distance taken;
  4. census_lib.guards reads both guards with real continuations and the rule's reading at three cutoffs. At these
     cutoffs the rule reads C2a Unresolved at its grid points (non-contracting above the floor), so each guard is read
     at delta = 0.01 and again at 0.05, on both sides: every one accepted with K1 and branch identity at every cutoff,
     and unclassified by the rule alone, as the grid points are.
Nothing here is a census reading: C2a is a control, and the bracket and its declared n(L) are plumbing. The transcript
is written to dev/plumbing_census.out.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
sys.path.insert(0, ROOT)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

PLUMB = [12, 16, 20]
lines = []


def say(s=''):
    print(s, flush=True)
    lines.append(s)


def main():
    devtools.require('C2a')
    lib.CUTOFFS, lib.DECIDING = PLUMB, PLUMB[1:]          # this process only: the plumbing cutoffs
    W4 = lib.WINDOWS['R4']
    case = census.roundtrip(cs.serialize('C2a', dict(cs.CASES['C2a'], points=[dict(eps=e, read=True) for e in W4[:3]],
                                                     cutoffs=PLUMB)))
    t0 = time.perf_counter()
    out, _ = dr.run_case('C2a', case, False)
    grid = census.roundtrip(out)
    say(f'run_case: {time.perf_counter() - t0:.0f} s')
    cuts = {N: census.Cutoff('C2a', case, N) for N in PLUMB}
    paths = {N: cuts[N].path(W4[2]) for N in PLUMB}
    fails = 0
    for e in W4[:3]:
        mine = census.readings_of(cuts, {N: paths[N].get(lib.key(e)) for N in PLUMB})
        d = lib.gate_full(mine, lib.at(grid, e))
        say(f'1. eps {e:.6g}: the recomputed path against run_case: {len(d)} differences' + (f' {d[:3]}' if d else ''))
        fails += bool(d)
    ch = dict(kind='type', lo=W4[1], hi=W4[2], lo_type='Elliptic', hi_type='Hyperbolic', between=[])
    rec, stop = lib.locate(ch, W4, case, cuts, lambda sols: census.readings_of(cuts, sols),
                           lambda cu, s1, s2: census.aligned(cu.Fn, cu.K, s1['c'], s2['c']),
                           lambda e: lib.at(grid, e), say=say)
    say(f"2. census_lib.locate: stop {stop}; kind {rec.get('kind')}; n(L) at the ends {rec.get('nL')}")
    fails += bool(stop) or rec.get('kind') != 'unchanged'
    N = PLUMB[-1]
    lo_pt = paths[N][lib.key(W4[1])]
    nl_a = lo_pt['nL']
    t0 = time.perf_counter()
    r = lib.bisect(W4[1], W4[2], nl_a, nl_a + 1, lo_pt['state'], paths[N][lib.key(W4[2])]['state'], cuts[N].step,
                   lambda s1, s2: census.aligned(cuts[N].Fn, cuts[N].K, s1['c'], s2['c']))
    dist = [m['distance'] for m in r['midpoints'] if 'distance' in m]
    k1s = [m['from_lower']['k1'] and m['from_upper']['k1'] for m in r['midpoints']]
    say(f"3. bisect at N = {N}: {len(r['midpoints'])} midpoints, complete {r['complete']}, interval {r['interval']}, "
          f"largest two-ends distance {max(dist):.2e}, K1 at every midpoint {all(k1s)}; {time.perf_counter() - t0:.0f} s")
    fails += not (r['complete'] and r['interval'][1] == W4[2] and max(dist) <= lib.AGREE and all(k1s))

    def read_guard(side, g):
        start = W4[1] if side == 'lower' else W4[2]
        pt = census.readings_of(cuts, {M: cuts[M].step(paths[M][lib.key(start)]['state'], g) for M in PLUMB})
        return dict(lib.here(pt, case), records=pt)
    readings, gfails = lib.guards((W4[1] * 1.0001, W4[1] * 1.0005), W4, {'lower': 'Elliptic', 'upper': 'Elliptic'},
                                  read_guard)
    grid_why = [lib.here(lib.at(grid, e), case) for e in W4[:3]]
    rule_only = lambda c: (not c['classified'] and len(c['causes']) == 1  # noqa: E731
                           and c['causes'][0].startswith('the rule reads it Unresolved'))
    ok4 = all(rule_only(c) for c in grid_why)
    for side, v in readings.items():
        ok4 &= [g['delta'] for g in v] == list(lib.DELTAS)
        for g in v:
            recs = g['reading']['records']
            ok4 &= rule_only(g['reading']) and all(recs['points'][M]['accepted'] for M in PLUMB)
            ok4 &= bool(recs['identity'] and recs['identity']['kept'])
            say(f"4. the {side} guard, delta {g['delta']}, eps {g['eps']:.6g}: {g['reading']['causes'][0][:110]}")
    say(f'   the grid points at these cutoffs: {[c["causes"][0][:40] for c in grid_why]}; the guards\' failures {gfails}')
    fails += not ok4
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'plumbing_census.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(dr.out_lines + lines) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
