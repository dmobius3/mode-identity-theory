#!/usr/bin/env python3
"""The checks between the two pins at N = 48, at solve fields alone, which hold no spectrum (run/TOP48.md, section 7,
step 2): each seed's check and each point's acceptance, with each path's job record, the manifest it names and the
SHA-256 of its two files, and the launch's events in RUNLOG.json. Then, beyond those two checks and deciding nothing,
each point's reached amplitude against its record at N = 40, as run DEVLOG 16 reports it.

Usage: solve_checks_48.py OUT
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import census_lib as lib  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402

TOL = 1e-6   # census.Cutoff.solve accepts a point when |eps reached - eps| <= 1e-6 and every step is accepted


def main():
    out = sys.argv[1]
    bad = 0
    print('1. Each path at N = 48: its job record, its seed and its points')
    pins = set()
    for tag, N in grid.solves_48():
        rec = jobs.record_of(out, f'path_{tag}_N{N}')        # each logged file's SHA-256 checked
        pins.add(rec['manifest'])
        d = lib.load_json(os.path.join(out, f'{tag}_N{N}.json'))
        want = [lib.key(e) for e in grid.entry(tag)[1]]
        pts = d['points']
        acc = [k for k in want if pts.get(k, {}).get('accepted')]
        off = max(abs(pts[k]['eps_reached'] - float(k)) for k in acc) if acc else None
        good = d['seed']['ok'] and acc == want and list(pts) == want and off is not None and off <= TOL
        bad += not good
        print(f"   {tag}: {len(rec['files'])} files as logged, under {rec['manifest'][:8]}; seed's check "
              f"{'passes' if d['seed']['ok'] else 'FAILS'} (crit {d['seed']['crit']:.2g}); {len(acc)} of {len(want)} "
              f"points accepted; largest |eps reached - eps| {off:.2g}, against {TOL:g}; {rec['seconds'] / 3600:.2f} h"
              + ('' if good else '  <- FAILS'))
    print(f"   one manifest for all: {len(pins) == 1}, {sorted(pins)[0]}; in SOLVE_PINS: {pins <= jobs.SOLVE_PINS}")
    bad += not (len(pins) == 1 and pins <= jobs.SOLVE_PINS)

    print('2. The launch, in RUNLOG.json')
    ev = lib.load_json(os.path.join(out, 'RUNLOG.json'))['events']
    i = max(j for j, e in enumerate(ev) if e['event'].startswith('launch: solves48'))
    for e in ev[i:]:
        print(f"   {e['t']} {e['event']}" + (f", exit {e['exit']}" if 'exit' in e else ''))
    names = {f'path_{t}_N{N}' for t, N in grid.solves_48()}
    done = {e['event'][:-len(' completed')] for e in ev[i:] if e['event'].endswith(' completed') and e.get('exit') == 0}
    good = done == names and ev[-1]['event'] == 'launch ended; 0 failed: []'
    bad += not good
    print(f"   every path completed with exit 0 and none failed: {good}")

    print('3. Beyond the two checks, deciding nothing: the reached amplitude against the record at N = 40')
    for tag, N in grid.solves_48():
        a = lib.load_json(os.path.join(out, f'{tag}_N40.json'))['points']
        b = lib.load_json(os.path.join(out, f'{tag}_N{N}.json'))['points']
        diff = [k for k in b if b[k]['eps_reached'] != a[k]['eps_reached']]
        big = max((abs(b[k]['eps_reached'] - a[k]['eps_reached']) / float(k) for k in diff), default=0.0)
        print(f"   {tag}: differs at {len(diff)} of {len(b)} points, by at most {big:.2g} of the amplitude")
    tag = grid.TOP48['row']
    P = {M: lib.load_json(os.path.join(out, f'{tag}_N{M}.json'))['points'] for M in (24, 32, 40)}
    for x, y in ((24, 32), (32, 40)):
        diff = [k for k in P[y] if P[y][k]['eps_reached'] != P[x][k]['eps_reached']]
        big = max(abs(P[y][k]['eps_reached'] - P[x][k]['eps_reached']) / float(k) for k in diff)
        print(f"   beside it, {tag} from N = {x} to {y}: differs at {len(diff)} of {len(P[y])} points, by at most {big:.2g}")
    print(f'{bad} failures')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
