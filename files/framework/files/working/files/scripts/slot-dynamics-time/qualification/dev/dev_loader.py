"""Development: the loader on M8.16.1's stored records (the terms' test 3), with no evolution. It loads every planned
read's stored point, pairs each stored slow group with Theorem 4.2's leading order, reproduces M8.16.1's recorded
deviations from leading order as RECORD.md states them, and refuses the arms: N = 16's point for a read at N = 24, a
point of another amplitude, and a record that is not the pinned one.

Usage: python3 -I -B dev_loader.py"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import loader as ld  # noqa: E402

PLAN = {'C2a': (1.0, 2.0), 'C2a_R5': (1.0, 2.0), 'C2b': (0.25, 1.0, 2.0), 'C3': (0.25, 0.5, 1.0, 2.0), 'P5': (1.0, 2.0),
        'C3R_R4': (1.0, 2.0), 'T3_R4': (1.0, 2.0)}
cuts = lambda e: (16, 24) + ((32,) if e == 2.0 else ())


def main():
    res = []

    def c(name, ok, det):
        res.append(ok)
        print(f'{"PASS" if ok else "FAIL"}  {name}: {det}')

    n, worst_rel = 0, []
    for stem, el in PLAN.items():
        for e in el:
            for N in cuts(e):
                p = ld.load(stem, N, e)
                ld.check(p, stem, N, e)
                pl = ld.pair_leading(p)
                assert abs(p.eps_reached - e) < 1e-5 * max(1, e), (stem, N, e, p.eps_reached)
                worst_rel.append(max(abs(g['c'] - g['L']) / abs(g['L']) for g in pl))
                n += 1
    c('every planned read loads and pairs with the frozen spectrum', n == 41, f'{n} points; deviation from leading order up to {100 * max(worst_rel):.1f} %')
    # M8.16.1's recorded deviations, reproduced: C2a's controls row at each eps and cutoff
    with open(os.path.join(ld.M8161, 'RECORD.md'), encoding='utf-8') as f:
        rec = f.read()
    row = {l.split('|')[3].strip(): [float(x) for x in re.findall(r'([\d.]+)%', l.split('|')[5])] for l in rec.split('\n') if re.match(r'\| C2a \| `R4` \| [\d.]+ \|', l)}
    got = {}
    for e in (1.0, 2.0):
        got[e] = []
        for N in (16, 24, 32):
            p = ld.load('C2a', N, e)
            got[e].append(round(100 * max(abs(g['c'] - g['L']) / abs(g['L']) for g in ld.pair_leading(p)), 2))
    ok = all(got[e] == row[str(int(e))] for e in (1.0, 2.0))
    c("C2a's recorded deviations reproduced", ok, f'computed {got}, RECORD.md {{1: {row["1"]}, 2: {row["2"]}}}')
    # the arms
    p16 = ld.load('C2a', 16, 1.0)
    for what, args in (('N = 16 for a read at N = 24', ('C2a', 24, 1.0)), ('eps = 1 for a read at eps = 2', ('C2a', 16, 2.0)),
                       ('another member', ('C2b', 16, 1.0))):
        try:
            ld.check(p16, *args)
            refused = False
        except ld.Refused:
            refused = True
        c(f'arm refused: {what}', refused, 'by its case, cutoff or amplitude, before any value')
    p16.sha = '0' * 64
    try:
        ld.check(p16, 'C2a', 16, 1.0)
        refused = False
    except ld.Refused:
        refused = True
    c('arm refused: a record that is not the pinned one', refused, 'by its SHA-256')
    print(f'{sum(res)} of {len(res)} checks pass')
    return all(res)


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
