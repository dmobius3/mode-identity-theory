#!/usr/bin/env python3
"""The next-order bar's check 2 at the pyramid, read from M8.16's record (development, off the instrument; M8.16.1's
terms, THE NEXT-ORDER BAR, check 2). Each point's summary keeps every slow group's projector output from
instrument/convergence.py's projector(): pnorm, resid and the usability flag ok, with normA beside them. So the
numerical estimate E = pnorm * max(resid, u normA) is on the record, and E_c = sum |w_i| E(x_i)/x_i^2, with w_i the
Lagrange weights at 0 of the reached amplitudes x_i, can be set against a tenth of the group's ceiling,
C_g = max(0.1 |c_g|, 1e-3 |kappa s_g|), with c_g and kappa s_g from the pinned next_order_values.json. Each pinned group
is read from the record's group of its class nearest x kappa s_g, and the next one must lie more than ten times as far.

  python3 -I -B pyramid_check2_from_record.py M8_16_P5_JSON NEXT_ORDER_VALUES_JSON"""
import hashlib
import json
import math
import sys

import numpy as np

P5, VALS = sys.argv[1:3]
rec, vals = json.load(open(P5)), json.load(open(VALS))
u = np.finfo(float).eps
cplx = lambda p: complex(float(p[0]), float(p[1]))
print('check 2 at the pyramid, from M8.16\'s record (P5.json SHA-256 %s; values SHA-256 %s)'
      % (hashlib.sha256(open(P5, 'rb').read()).hexdigest(), hashlib.sha256(open(VALS, 'rb').read()).hexdigest()))
ratios, seps, usable = [], [], True
for N in ('16', '24', '32'):
    for g in [g for g in vals['cases']['P5']['cutoffs'][N]['groups'] if g['under_bar']]:
        ks, cg = cplx(g['kappa_s']), cplx(g['c_g'])
        ceil = max(0.1 * abs(cg), 1e-3 * abs(ks))
        xs, Es, oks, sep = [], [], [], math.inf
        for e in ('0.25', '0.5', '1'):
            pt = rec['cutoffs'][N]['points'][e]
            x = float(pt['eps_reached'])
            near = sorted((h for h in pt['summary']['groups'] if h['cls'] == g['cls']), key=lambda h: abs(complex(*h['c']) - x * ks))
            h = near[0]
            if len(near) > 1:                                 # the only group of its class is matched by its class alone
                sep = min(sep, abs(complex(*near[1]['c']) - x * ks) / abs(complex(*h['c']) - x * ks))
            xs.append(x)
            Es.append(h['pnorm'] * max(h['resid'], u * pt['summary']['normA']))
            oks.append(bool(h['ok']))
        w = [math.prod((0 - xs[k]) / (xs[i] - xs[k]) for k in range(3) if k != i) for i in range(3)]
        Ec = sum(abs(w[i]) * Es[i] / xs[i] ** 2 for i in range(3))
        ratios.append(Ec / (ceil / 10))
        usable &= all(oks)
        print(f"N = {N} {g['cls']:7s}: E = {', '.join(f'{x:.2e}' for x in Es)} at 0.25, 0.5 and 1, usable {all(oks)}; "
              f"E_c {Ec:.2e} against {ceil / 10:.2e}: {'passes' if Ec <= ceil / 10 else 'FAILS'}, {math.log10((ceil / 10) / Ec):.1f} decades; "
              + (f"the next group of its class at least {sep:.0f} times as far from x kappa s_g" if sep < math.inf else 'the only group of its class'))
        seps.append(sep)
ok = usable and max(ratios) <= 1 and min(seps) > 10
print(f'check 2 at the pyramid: {"PASS" if ok else "FAIL"}; the largest E_c over its trigger {max(ratios):.1e}')
sys.exit(0 if ok else 1)
