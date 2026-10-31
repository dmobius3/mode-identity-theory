#!/usr/bin/env python3
"""The values M8.18's moved midpoint was chosen from, read from M8.17's locator record with no solve.

Usage: moved_midpoint.py LOCATE_JSON [FRACTION]

LOCATE_JSON is M8.17's run/out/locate_T4_R5_8_11.313708499.json. For N = 24 and 32 it prints the five readings on the
n(L) = 7 side and the two on the other, their squares, the rate at which the squares fall, the crossing that rate
extrapolates to, K1's limit (three margins, the frozen GRAY), and what the fraction gives: the moved point, the nearest
eigenvalue there, interpolated in squares between the two readings around it, the interval each n(L) would leave, and
the completion width w/2 of its lower end. Everything past the printed readings is an estimate (INFERRED).
"""
import json
import sys

W_HALF = 5e-4
GRAY = 3.0


def main():
    with open(sys.argv[1], encoding='utf-8') as f:
        d = json.load(f)
    frac = float(sys.argv[2]) if len(sys.argv) > 2 else 0.4
    for N in ('24', '32'):
        r = d['bisection'][N]
        a, b = r['interval']
        rows = []
        for m in r['midpoints']:
            p = m['from_lower']['point']['record']
            rows.append((m['eps'], m['from_lower']['nL'], p['outside_min'], p['margin'], m['from_lower']['k1']))
        rows.sort()
        print(f'N = {N}: stopped at [{a:.6f}, {b:.6f}], width {b - a:.4e}, {(b - a) / a:.3e} of its lower end; '
              f"stop: {r['stop']}")
        near = [x for x in rows if a - 0.05 <= x[0] <= b + 1e-9]
        for e, nl, out, mg, k in near:
            print(f'   eps {e:.6f}  n(L) {nl}  nearest {out:.4e}  square {out * out:.4e}  margin {mg:.3e}  K1 {k}')
        seven = [x for x in near if x[1] == 7]
        e1, e2 = seven[-2][0], seven[-1][0]                 # the last two on the n(L) = 7 side, K1's stop among them
        s1, s2 = seven[-2][2] ** 2, seven[-1][2] ** 2
        rate = (s1 - s2) / (e2 - e1)
        rates = [(x[2] ** 2 - y[2] ** 2) / (y[0] - x[0]) for x, y in zip(seven, seven[1:])]
        cross = e2 + s2 / rate
        mg = seven[-1][3]
        limit = GRAY * mg
        moved = a + frac * (b - a)
        at = (s2 + rate * (e2 - moved)) ** 0.5
        print(f'   squares fall at {min(rates):.3e} to {max(rates):.3e} per unit; from the last two, {rate:.3e}; '
              f'crossing near {cross:.6f}')
        print(f'   K1 refuses below {limit:.3e} (three margins); so roughly from eps {cross - limit ** 2 / rate:.6f}')
        print(f'   fraction {frac}: moved point {moved:.6f}; nearest eigenvalue about {at:.3e}, {at / limit:.2f} times '
              f'the limit')
        print(f'   interval left: n(L) 7 there, [{moved:.6f}, {b:.6f}], width {b - moved:.4e}; n(L) 6 there, '
              f'[{a:.6f}, {moved:.6f}], width {moved - a:.4e}; complete below {W_HALF * moved:.4e} and '
              f'{W_HALF * a:.4e}')
        lo = (b - a - W_HALF * a) / ((b - a) * (1 + W_HALF))
        print(f'   the fraction must exceed {lo:.4f} to complete with n(L) 7 at the moved point')


if __name__ == '__main__':
    main()
