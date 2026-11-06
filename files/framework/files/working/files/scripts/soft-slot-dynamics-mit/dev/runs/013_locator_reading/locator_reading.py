"""T4/R4's locator and its reproduction, read from their records alone: nothing is solved or read again.

Usage: python3 -I -B dev/runs/013_locator_reading/locator_reading.py RUN_OUT M818_FOLDER

1. The reproduction (LOCATE_REPRO_T4_R5.json): its verdict, and each file it compared, against M8.18's folder.
2. T4/R4 (LOCATE_T4_R4.json): at each cutoff, every midpoint with both solves' acceptance, K1 and its parts, n(L) and
   the aligned distance; each interval and stop; the location's verdict.
3. INFERRED, outside the locator's rule, which decides nothing here: the eigenvalue of L that changes sign, the fifth
   nearest zero (the four structural zeros lie below 1e-10), at each midpoint; a straight line through it at the
   accepted midpoints within 0.02 of the interval, and its zero; A's eigenvalue on that mode against it,
   |lambda|^2 / |mu|; and from these the neighbourhood of the zero where |lambda| < 3 margin, where the zero cluster is
   not separated (linear.record: the gray zone is (margin/3, 3 margin), and below margin it joins the cluster), so K1
   fails there.
"""
import hashlib
import json
import os
import re
import sys

import numpy as np

out, m818 = sys.argv[1], sys.argv[2]
src = open(os.path.join(os.path.dirname(os.path.abspath(out)), 'census_lib.py'), encoding='utf-8').read()
assert re.search(r'^W = 1e-3 ', src, re.M) and re.search(r'^W_HALF = W / 2 ', src, re.M)
W_HALF = 1e-3 / 2


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


# --- 1. the reproduction ------------------------------------------------------------------------------------------
r = json.load(open(os.path.join(out, 'LOCATE_REPRO_T4_R5.json'), encoding='utf-8'))
print("1. The reproduction: M8.18's Arm B, T4/R5")
print(f"   passed {r['passed']}; stop {r['stop']}; {len(r['differences'])} differences from ARM_B.json; "
      f"{len(r['unequal_arrays'])} of {r['arrays']} arrays unequal")
for f, h in r['compared'].items():
    p = os.path.join(m818, f)
    print(f"   {f}: {'the same file' if os.path.exists(p) and sha(p) == h else 'NOT THE SAME FILE'} in M8.18's folder")

# --- 2. T4/R4 -----------------------------------------------------------------------------------------------------
t = json.load(open(os.path.join(out, 'LOCATE_T4_R4.json'), encoding='utf-8'))
print(f"\n2. {t['row']} on ({t['bracket'][0]:g}, {t['bracket'][1]:.6g}): {t['kind']} bracket, {t['types'][0]} to "
      f"{t['types'][1]}; n(L) at the ends {t['nL']}; signed change {t['delta']}")
for e, b in t['ends_both'].items():
    print(f"   the end {float(e):.6g}: as built {b['as_built']['type']}, changed {b['changed']['type']}, same {b['same']}")
for N, b in t['bisection'].items():
    lo, hi = b['interval']
    print(f"   N = {N}: complete {b['complete']}; interval [{lo!r}, {hi!r}], width {hi - lo:.6g}, "
          f"{(hi - lo) / lo:.4g} of its lower end, where completion asks below {W_HALF:g}; stop: {b['stop']}")
    for i, m in enumerate(b['midpoints']):
        d = m.get('distance')
        print(f"     {i:2d} {m['eps']:.12f}{' moved' if m.get('moved') else '      '} "
              f"distance {'-' if d is None else f'{d:.2e}'}")
        for side in ('from_lower', 'from_upper'):
            s = m[side]
            rec = s['point']['record']
            print(f"          {side}: accepted {s['ok']}, its record {rec['type']} ({rec['nL']}, {rec['nD']}, {rec['K']}); "
                  f"K1 {s['k1']} (V0 {rec['v0_matches']}, chains {rec['blocks']}, "
                  f"separated {rec['separated']}), n(L) {s['nL']}; margin {rec['margin']:.4g}, cluster max "
                  f"{rec['cluster_max']:.3g}, outside min {rec['outside_min']:.4g} = {rec['outside_min'] / rec['margin']:.3g}"
                  f" margin")
print(f"   located {t['located']}; union {t['union']}; span {t['span']}; guards {t.get('guards')}; "
      f"both verdicts {t['both_verdicts']}")
print(f"   failures: {t['failures']}")
print(f"   why: {t['why']}")

# --- 3. INFERRED: where L's eigenvalue changes sign, and K1's neighbourhood of it ---------------------------------
print('\n3. INFERRED, outside the rule: the eigenvalue of L that changes sign, and where K1 cannot hold')
for N, b in t['bisection'].items():
    rows = []
    for m in b['midpoints']:
        s, u = m['from_lower'], m['from_upper']
        p, rec = s['point'], s['point']['record']
        mu = sorted(p['l_near'], key=abs)
        assert max(abs(x) for x in mu[:4]) < 1e-10 < abs(mu[4]), (N, m['eps'], mu[:6])
        lam = rec['outside_min'] if rec['separated'] or rec['v0_matches'] else rec['cluster_max']
        rows.append(dict(eps=m['eps'], mu=mu[4], lam=lam, margin=rec['margin'], k1=s['k1'] and u['k1'],
                         moved=bool(m.get('moved')), nL=s['nL']))
    lo, hi = b['interval']
    near = [x for x in rows if x['k1'] and lo - 0.02 <= x['eps'] <= hi + 0.02]
    e, mu = np.array([x['eps'] for x in near]), np.array([x['mu'] for x in near])
    slope, c0 = np.polyfit(e, mu, 1)
    star = -c0 / slope
    resid = float(np.max(np.abs(mu - (slope * e + c0))))
    ratio = np.array([x['lam'] ** 2 / abs(x['mu']) for x in near])
    refused = sorted((x for x in rows if not x['k1']), key=lambda x: x['eps'])
    a, c = refused[0], refused[-1]
    star2 = a['eps'] - a['mu'] * (c['eps'] - a['eps']) / (c['mu'] - a['mu'])
    margin = float(np.median([x['margin'] for x in rows]))
    h = (3 * margin) ** 2 / (float(np.median(ratio)) * abs(slope))
    print(f"   N = {N}: the line through {len(near)} accepted midpoints, slope {slope:.5g}, largest residual "
          f"{resid:.2g}; its zero {star:.7f}; between the two refused points, by interpolation, {star2:.7f}")
    print(f"          |lambda|^2/|mu| at those midpoints {ratio.min():.4g} to {ratio.max():.4g}; at the refused points "
          + ', '.join(f"{x['eps']:.6f}: mu {x['mu']:.4g}, |lambda| {x['lam']:.4g}, ratio {x['lam'] ** 2 / abs(x['mu']):.4g}"
                      for x in refused))
    print(f"          K1's neighbourhood, |lambda| < 3 margin with margin {margin:.4g}: |eps - zero| < {h:.4g}, "
          f"twice that {2 * h:.4g}, where completion asks an interval below {W_HALF * lo:.4g}")
    print(f"          the interval's ends lie {star - lo:.4g} below and {hi - star:.4g} above the zero; "
          + ', '.join(f"the {'moved point' if x['moved'] else 'midpoint'} {x['eps'] - star:+.3g} from it (n(L) {x['nL']})"
                      for x in refused))
