#!/usr/bin/env python3
"""The margins behind B1's fix on #650 (case: synthetic; arithmetic on the pinned values alone, nothing scored).

Usage: dev/b1_margins.py, from the folder's root.

For every case the next-order bar reads, at each cutoff and at eps = 0.25, 0.5 and 1, within each class-and-sign
bucket of its frozen spectrum, from run/next_order_values.json as cases.py serializes it:
  1. the order of the groups by |eps kappa s_g| against their order by |eps kappa s_g + eps^2 c_g(N)|: where these
     differ, keeping the order of |lambda|, the review's third option, would exchange two groups on an exact spectrum;
  2. the smallest distance between two groups' next-order predictions, in units of the largest ceiling there as a
     shift of lambda, eps^2 C_g(N): matching against the next-order values, the first option, can move a value only on a
     spectrum some group of which lies about half that far from its prediction.
Reported, with the four smallest margins."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402

crossings, margins = [], []
for name, c0 in cs.CASES.items():
    case = cs.serialize(name, c0)
    if 'next_order' not in case:
        continue
    for N in case['cutoffs']:
        for eps in ck.NEXT_EPS:
            buckets = {}
            for g in case['next_order'][str(N)]:
                m = case['spectrum'][g['spectrum_index']]
                ks, cg = ck._c(g['kappa_s']), ck._c(g['c_g'])
                ceiling = max(ck.CEILING[0] * abs(cg), ck.CEILING[1] * abs(ks))
                buckets.setdefault((m['cls'], m['sign']), []).append(
                    (g['spectrum_index'], abs(eps * ks), eps * ks + eps ** 2 * cg, ceiling))
            for b, xs in buckets.items():
                if len(xs) < 2:
                    continue
                if [x[0] for x in sorted(xs, key=lambda x: x[1])] != [x[0] for x in sorted(xs, key=lambda x: abs(x[2]))]:
                    crossings.append((name, N, eps, b))
                sep = min(abs(x[2] - y[2]) for i, x in enumerate(xs) for y in xs[i + 1:])
                margins.append((sep / (eps ** 2 * max(x[3] for x in xs)), name, N, eps, b))
margins.sort()
print('1. groups whose order by |lambda| changes within a bucket:', crossings if crossings else 'none')
print('2. the smallest separations of next-order predictions, in ceilings as a shift of lambda:')
for r in margins[:4]:
    print(f'   {r[0]:6.1f}  {r[1]} N = {r[2]} eps = {r[3]:g} {r[4]}')
print(f'   over {len(margins)} buckets of two groups or more')
