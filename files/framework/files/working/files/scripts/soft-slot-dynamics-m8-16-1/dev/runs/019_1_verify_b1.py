#!/usr/bin/env python3
"""xrodz's B1 on #650, verified at source (case: synthetic; no solve, no seed, nothing sealed is read).

Usage: dev/verify_b1.py, from the folder's root.

For every case the next-order bar reads, a synthetic record holds, at each cutoff and at eps = 0.25, 0.5 and 1, one
group per frozen spectrum entry at exactly lambda = eps kappa s_g + eps^2 c_g(N), from run/next_order_values.json as
cases.py serializes it, with a consistent convergence summary. checks.k1 and checks.converged are stubbed true, so check
1 reduces to the matching. Claims, from the review:
  1. checks.bar reads T5/R2's two lowest groups 'fail', by check 3, at every cutoff, and every other group 'pass'.
  2. checks.match, on the same values, pairs some computed value with another entry's prediction at T5/R2 at eps = 1
     at every cutoff, and nowhere else at eps = 0.5 or below.
Reported: the straight and swapped pairings' costs at T5/R2, eps = 1."""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402

ck.k1 = lambda point, case: True                 # isolate check 1's matching: K1 and convergence are not modelled
ck.converged = lambda case_out, eps, case: True


def exact(case, N, eps):
    """[(entry index, cls, sign, mult, lambda)] at exactly eps kappa s_g + eps^2 c_g, one per frozen group."""
    out = []
    for g in case['next_order'][str(N)]:
        m = case['spectrum'][g['spectrum_index']]
        lam = eps * ck._c(g['kappa_s']) + eps ** 2 * ck._c(g['c_g'])
        out.append((g['spectrum_index'], m['cls'], m['sign'], m['mult'], lam))
    return out


def record(case):
    cut = {}
    for N in case['cutoffs']:
        pts = {}
        for eps in ck.NEXT_EPS:
            groups, k = [], 0
            for j, cls, sign, mult, lam in exact(case, N, eps):
                g = dict(c=[lam.real, lam.imag], cls=cls, status='definite', size=mult,
                         neg=mult if (cls == 'imag' and sign == -1) else 0, idx=list(range(k, k + mult)))
                k += mult
                groups.append(g)
            summary = dict(normA=1.0, groups=[dict(g, ok=True, pnorm=1.0, resid=0.0, why=None) for g in groups])
            pts[ck.key(eps)] = dict(accepted=True, eps_reached=eps, groups=groups, summary=summary)
        cut[str(N)] = dict(seed=dict(ok=True), points=pts)
    return dict(cutoffs=cut)


def pairing(case, N, eps):
    """The entries whose computed value checks.match pairs with another entry's prediction."""
    comp = [(cls, sign, lam) for j, cls, sign, mult, lam in exact(case, N, eps) for _ in range(mult)]
    own = {}
    for j, cls, sign, mult, lam in exact(case, N, eps):
        own[(cls, sign, lam)] = j
    pred = ck.predicted(case, eps)
    pj = {}
    for j, m in enumerate(case['spectrum']):
        pj[(m['cls'], m['sign'], ck.predicted(dict(case, spectrum=[m]), eps)[0][2])] = j
    ok, _, rows = ck.match(pred, comp)
    return ok, sorted({own[(r[0], r[1], r[3])] for r in rows if pj[(r[0], r[1], r[2])] != own[(r[0], r[1], r[3])]})


bar_cases = [n for n, c in cs.CASES.items() if 'next_order' in cs.serialize(n, c)]
failures, swaps = [], []
for name in bar_cases:
    case = cs.serialize(name, cs.CASES[name])
    res = ck.bar(record(case), case)
    for gi, r in sorted(res.items()):
        g = case['next_order'][str(case['cutoffs'][0])][gi]
        tau = case['spectrum'][g['spectrum_index']]['tau']['value']
        line = f"{name:7} group {gi} (entry {g['spectrum_index']}, tau {tau:.4f}): {r['reading']}"
        if r['reading'] != 'pass':
            failures.append((name, gi))
            line += ' | ' + '; '.join(r['why'])
        print(line)
    for N in case['cutoffs']:
        for eps in ck.NEXT_EPS:
            ok, moved = pairing(case, N, eps)
            if moved:
                swaps.append((name, N, eps, tuple(moved)))
print()
print('pairings that move a value to another entry:', swaps if swaps else 'none')
case = cs.serialize('T5/R2', cs.CASES['T5/R2'])
for N in case['cutoffs']:
    vals = {j: lam for j, cls, sign, mult, lam in exact(case, N, 1.0)}
    pred = {j: ck.predicted(dict(case, spectrum=[m]), 1.0)[0][2] for j, m in enumerate(case['spectrum'])}
    lo = sorted(pred, key=lambda j: abs(pred[j]))[:2]
    a, b = lo
    straight = abs(vals[a] - pred[a]) / abs(pred[a]) + abs(vals[b] - pred[b]) / abs(pred[b])
    swapped = abs(vals[b] - pred[a]) / abs(pred[a]) + abs(vals[a] - pred[b]) / abs(pred[b])
    print(f'T5/R2, N = {N}, eps = 1, entries {a} and {b}: straight {straight:.4f}, swapped {swapped:.4f}')
t5 = [f for f in failures if f[0] == 'T5/R2']
others = [f for f in failures if f[0] != 'T5/R2']
t5_swaps = [s for s in swaps if s[0] == 'T5/R2' and s[2] == 1.0]
claim1 = len(t5) == 2 and not others
claim2 = len(t5_swaps) == 3 and all(s[0] == 'T5/R2' and s[2] == 1.0 for s in swaps)
print()
print(f"claim 1, T5/R2's two lowest groups fail and nothing else does: {'holds' if claim1 else 'FAILS'}")
print(f"claim 2, the pairing moves values at T5/R2 at eps = 1 at every cutoff, and nowhere else: {'holds' if claim2 else 'FAILS'}")
sys.exit(0 if claim1 and claim2 else 1)
