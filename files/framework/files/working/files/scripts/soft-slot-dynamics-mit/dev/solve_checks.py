#!/usr/bin/env python3
"""The only look at the solves before the dated note, and it is at solve fields alone: no spectrum exists yet (DESIGN.md,
section 7). A path at N = 24 or 32 on a stored path's own grid must equal its record, field for field. Where the grid
differs the path is new, and a stored point's m and eps_reached are reported beside the stored ones. At T5, a difference
in m at 128 beyond numerical tolerance is evidence of path dependence; whether the coarse path stepped onto another
solution stays OPEN.

Usage: solve_checks.py OUT SCRIPTS_DIR
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import census_lib as lib  # noqa: E402
import grid  # noqa: E402

FIELDS = ('accepted', 'eps_reached', 'lam', 'm', 'evaluations', 'floor_rel')
RECORDS = dict(T1_R4='soft-slot-dynamics-m8-17', T4_R4='soft-slot-dynamics-m8-17', T1_R5='soft-slot-dynamics-m8-17',
               T5_R2='soft-slot-dynamics-m8-17', T5J_R2='soft-slot-dynamics-m8-16-1', C2a_R5='soft-slot-dynamics-m8-16-1')


def main():
    out, scripts = sys.argv[1:3]
    bad = 0
    for tag, folder in RECORDS.items():
        with open(os.path.join(scripts, folder, 'run', 'out', tag + '.json'), encoding='utf-8') as f:
            theirs = json.load(f)
        for N in (24, 32):
            path = os.path.join(out, f'{tag}_N{N}.json')
            if not os.path.exists(path):
                print(f'{tag} N = {N}: not solved yet')
                continue
            with open(path, encoding='utf-8') as f:
                mine = json.load(f)['points']
            stored = theirs['cutoffs'][str(N)]['points']
            same_path, rows = True, []
            for e in grid.entry(tag)[1]:
                k = lib.key(e)
                if k not in stored:
                    same_path = False
                    continue
                if k not in mine:
                    rows.append(f'{k}: not reached')
                    bad += 1
                    continue
                d = lib.differences({f: mine[k].get(f) for f in FIELDS}, {f: stored[k].get(f) for f in FIELDS})
                if same_path and d:
                    rows.append(f'{k}: DIFFERS on its own path: {d[0]}')
                    bad += 1
                elif not same_path:
                    rows.append(f"{k}: new path, m differs by {abs(mine[k]['m'] - stored[k]['m']) / stored[k]['m']:.2e}, "
                                f"eps_reached by {abs(mine[k]['eps_reached'] - stored[k]['eps_reached']):.1e}")
            print(f"{tag} N = {N}: {len(mine)} points" + (f"; {'; '.join(rows)}" if rows else '; all equal their record'))
    print(f'{bad} failures')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
