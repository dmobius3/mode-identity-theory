#!/usr/bin/env python3
"""Test 8: a plumbing pass of this run's instrument side, on the GO-list control C2a, at cutoffs the registered run never
uses (12, 16, 20), never scored, and outside the run: development only (M8.18's terms: THE TESTS BEFORE THE FREEZE,
test 8, as M8.17's plumbing pass). No solve at N = 40.

Usage: plumbing_census.py

It checks, with real solves on C2a in R4:
  1. the path solved and then read (census.Cutoff.solves, then read) equals driver.run_case's own output, field for
     field, timings aside, at every point to 2, at every cutoff, with the rule's reading and the top pair's identity
     (census.rule, census.identity): splitting the step changes nothing, and the solve runs inside checks.withheld;
  2. a read at a chosen point only: with a spy on driver.read_point, the path at the top cutoff calls it at those points
     and at no other; a read outside the scope is refused;
  3. the stored solutions: Run.path_job writes them, Run.stored returns them through the solve-state gate, and a read
     from a stored solution equals a read from the live one, field for field, timings aside; a changed byte in the
     file stops the run, and so does a changed lam;
  4. a resume: a continuation from a stored state equals one from the live state;
  5. both identity pairs, the band's call and the reading beside it: the scored reading's band is the level above
     BAND_N on the patched ladder, the band beside it the level above the middle cutoff; both are read;
  6. census_lib.bisect with moved, on real continuations from both ends of (0.5, 2), the upper end's n(L) declared one
     more than the record's and K1 forced to fail at the first midpoint: it moves once, the moved point is solved from
     both ends and read, and the refused midpoint stays in the record.
Nothing here is a census reading: C2a is a control, and the bracket and its declared n(L) are plumbing. The transcript is
written to dev/plumbing_census.out.
"""
import os
import sys
import tempfile
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
sys.path.insert(0, ROOT)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

PLUMB = (12, 16, 20)
lines = []


def say(s=''):
    print(s, flush=True)
    lines.append(s)


def main():
    devtools.require('C2a')
    lib.ARM_A = dict(name='A', cutoffs=PLUMB, deciding=PLUMB[1:], pairs=((12, 16), (16, 20)), beside=True)
    lib.TOP, lib.BAND_N, lib.BESIDE_N = 20, 12, 16          # this process only: the plumbing ladder
    lad = lib.ARM_A
    t0 = time.perf_counter()
    case = census.roundtrip(cs.serialize('C2a', dict(cs.CASES['C2a'], cutoffs=list(PLUMB))))
    fails = 0

    def claim(n, ok, what):
        nonlocal fails
        say(f"{n}. {'PASS' if ok else 'FAIL'}: {what}")
        fails += not ok
    ref, _ = dr.run_case('C2a', case, False)
    eps = [p['eps'] for p in case['points']]
    cuts = {N: census.Cutoff('C2a', case, N) for N in PLUMB}
    live = {N: cuts[N].solves() for N in PLUMB}
    read = {N: {k: cuts[N].read(s, s['eps'], 'path') for k, s in live[N].items()} for N in PLUMB[:2]}
    read[20] = {k: cuts[20].read(s, s['eps'], 'control') for k, s in live[20].items()}
    bad = []
    for N in PLUMB:
        bad += lib.differences({k: census.roundtrip(s['point']) for k, s in read[N].items()},
                               census.roundtrip(ref['cutoffs'][str(N)]['points']), f'/{N}')
    for e in eps:
        k = lib.key(e)
        sols = {N: read[N][k] for N in PLUMB}
        pts = [sols[N]['point'] for N in PLUMB]
        hi = pts[-1]
        rd = dr.ck.reading([q['summary'] for q in pts], hi['eig'], hi['lam'], hi['record']['margin'], PLUMB[0])
        bad += lib.differences(census.roundtrip(rd), census.roundtrip(ref['readings'][k]), f'/reading/{k}')
        bad += lib.differences(census.roundtrip(census.identity(cuts, sols, (16, 20))), census.roundtrip(ref['identity'][k]),
                               f'/identity/{k}')
    claim(1, not bad, f'the split step equals run_case at {len(eps)} points at each of {PLUMB}: {len(bad)} differences'
          + ''.join(f'\n      {b}' for b in bad[:5]))
    # 2. a read at chosen points only
    calls, real = [], dr.read_point
    dr.read_point = lambda Fn, K, c, lam, cs_, e, w: (calls.append((Fn.B.N, e)), real(Fn, K, c, lam, cs_, e, w))[1]
    try:
        sols = cuts[20].solves()
        before = list(calls)
        cuts[20].read(sols[lib.key(0.5)], 0.5, 'control')
        cuts[20].read(sols[lib.key(2.0)], 2.0, 'control')
        refused = False
        cuts[20].name = 'T1/R4'
        try:
            cuts[20].read(sols[lib.key(1.0)], 1.0, 'twelve')
        except lib.OutOfScope:
            refused = True
        cuts[20].name = 'C2a'
    finally:
        dr.read_point = real
    claim(2, before == [] and calls == [(20, 0.5), (20, 2.0)] and refused,
          f'a path at the top cutoff called read_point {len(before)} times; two reads then called it at {calls}; a read '
          f'outside the scope was refused: {refused}')
    with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as tmp:
        F = dict(cases={'C2a': case})
        run = census.Run(F, tmp, lambda n, c, N, o: cuts[N])
        run.log.setdefault('events', [])
        run.log['completed']['arm_b'] = dict(files={}, t='plumbing')
        run.path_job('C2a', 20)
        st = run.stored('C2a', 20)
        k = lib.key(1.0)
        a, b = cuts[20].read(st['sols'][k], 1.0, 'control'), cuts[20].read(sols[k], 1.0, 'control')
        diff = lib.differences(census.roundtrip(a['point']), census.roundtrip(b['point']))
        path = run.at('C2a_N20.npz')
        raw = open(path, 'rb').read()
        with open(path, 'wb') as f:
            f.write(raw[:200] + bytes([raw[200] ^ 1]) + raw[201:])
        try:
            run.stored('C2a', 20)
            byte = False
        except census.StopRun:
            byte = True
        with open(path, 'wb') as f:
            f.write(raw)
        js = run.at('C2a_N20.json')
        rec = lib.load_json(js)
        rec['points'][k]['lam'] += 1e-13
        keep = open(js, 'rb').read()
        with open(js, 'w', encoding='utf-8') as f:
            census.json.dump(rec, f, indent=1)
        run.complete('path:C2a:20', ['C2a_N20.npz', 'C2a_N20.json'])
        try:
            run.stored('C2a', 20)
            lam = False
        except census.StopRun:
            lam = True
        with open(js, 'wb') as f:
            f.write(keep)
        run.complete('path:C2a:20', ['C2a_N20.npz', 'C2a_N20.json'])
        claim(3, not diff and byte and lam, f'a read from the stored solution equals a live one: {len(diff)} differences; a '
              f'changed byte stops it: {byte}; a changed lam stops it: {lam}')
        st = run.stored('C2a', 20)
        m = 1.5
        s1, s2 = cuts[20].solve(st['sols'][k]['state'], m), cuts[20].solve(sols[k]['state'], m)
        same = bool(np.array_equal(s1['c'], s2['c']))
        claim(4, same, f'a continuation to {m} from the stored state equals one from the live state, bit for bit: {same}')
    k = lib.key(2.0)
    sols = {N: dict(read[N][k]) for N in PLUMB}
    pt = census.readings_of(cuts, sols, lad)
    want = (np.sqrt(14 * 16.0) - np.sqrt(sols[20]['point']['lam']), np.sqrt(18 * 20.0) - np.sqrt(sols[20]['point']['lam']))
    both = abs(pt['reading']['band'] - want[0]) < 1e-12 and abs(pt['beside']['band'] - want[1]) < 1e-12
    pairs = sorted(pt['identity'])
    ok5 = both and pairs == ['12-16', '16-20'] and all(v and v['kept'] for v in pt['identity'].values())
    claim(5, ok5, f"both identity pairs {pairs}, kept: {[v['kept'] for v in pt['identity'].values()]}; the scored band "
          f"{pt['reading']['band']:.6f}, level 14; the band beside it {pt['beside']['band']:.6f}, level 18")
    cu = cuts[16]
    e_lo, e_hi = 0.5, 2.0
    lo, hi = read[16][lib.key(e_lo)], read[16][lib.key(e_hi)]
    forced = dict(left=2)

    def solve(state, e):
        s = cu.step(state, e)
        if forced['left']:
            forced['left'] -= 1
            s = dict(s, k1=False)
        return s
    n0 = lo['nL']
    r = lib.bisect(e_lo, e_hi, n0, n0 + 1, lo['state'], hi['state'], solve,
                   lambda s1, s2: census.aligned(cu.Fn, cu.K, s1['c'], s2['c']), moved=lib.MOVED)
    mids = r['midpoints']
    m1 = (e_lo + e_hi) / 2
    ok6 = (len(mids) >= 2 and mids[0]['eps'] == m1 and 'moved' not in mids[0] and mids[1].get('moved') is True
           and abs(mids[1]['eps'] - (e_lo + lib.MOVED * (e_hi - e_lo))) < 1e-15 and r['complete'])
    claim(6, ok6, f"bisect with K1 forced to fail at the first midpoint, {m1}: moved to {mids[1]['eps']}, then "
          f"{len(mids) - 2} more midpoints, complete {r['complete']}, interval {r['interval']}")
    say(f'{time.perf_counter() - t0:.0f} s; {fails} failed')
    with open(os.path.join(HERE, 'plumbing_census.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
