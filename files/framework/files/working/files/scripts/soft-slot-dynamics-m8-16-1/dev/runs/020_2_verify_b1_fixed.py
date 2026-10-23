#!/usr/bin/env python3
"""xrodz's B1 on #650, after the repair (case: synthetic; no solve, no seed, nothing sealed is read).

Usage: dev/verify_b1_fixed.py, from the folder's root.

The harness of dev/verify_b1.py, on the repaired run/checks.py: for every case the next-order bar reads, a synthetic
record holds one group per frozen spectrum entry at exactly lambda = eps kappa s_g + eps^2 c_g(N), at each cutoff and
at eps = 0.25, 0.5 and 1, with a consistent convergence summary; checks.k1 and checks.converged are stubbed true, so
check 1 reduces to the matching. Claims:
  1. checks.bar reads every group under the bar 'pass', in all 12 cases, at every cutoff.
  2. checks.mode_values gives every entry its own exact value, at every case, cutoff and point.
Arm: checks.predicted_next replaced by the leading order, as filed at MIT 0d6beae, turns claim 1 red, at T5/R2's two
lowest groups alone."""
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
    """{entry index: (cls, sign, mult, lambda)} at exactly eps kappa s_g + eps^2 c_g(N)."""
    out = {}
    for g in case['next_order'][str(N)]:
        m = case['spectrum'][g['spectrum_index']]
        out[g['spectrum_index']] = (m['cls'], m['sign'], m['mult'],
                                    eps * ck._c(g['kappa_s']) + eps ** 2 * ck._c(g['c_g']))
    return out


def record(case):
    cut = {}
    for N in case['cutoffs']:
        pts = {}
        for eps in ck.NEXT_EPS:
            groups, k = [], 0
            for j, (cls, sign, mult, lam) in sorted(exact(case, N, eps).items()):
                groups.append(dict(c=[lam.real, lam.imag], cls=cls, status='definite', size=mult,
                                   neg=mult if (cls == 'imag' and sign == -1) else 0, idx=list(range(k, k + mult))))
                k += mult
            summary = dict(normA=1.0, groups=[dict(g, ok=True, pnorm=1.0, resid=0.0, why=None) for g in groups])
            pts[ck.key(eps)] = dict(accepted=True, eps_reached=eps, groups=groups, summary=summary)
        cut[str(N)] = dict(seed=dict(ok=True), points=pts)
    return dict(cutoffs=cut)


def score():
    """(groups under the bar, those not passing, entries mode_values gives another's value)."""
    total, bad, moved = 0, [], []
    for name in BAR:
        case = cs.serialize(name, cs.CASES[name])
        rec = record(case)
        for gi, r in sorted(ck.bar(rec, case).items()):
            total += 1
            if r['reading'] != 'pass':
                bad.append((name, gi, r['reading'], r['why'][:1]))
        for N in case['cutoffs']:
            for eps in ck.NEXT_EPS:
                ex = exact(case, N, eps)
                p = rec['cutoffs'][str(N)]['points'][ck.key(eps)]
                for j, (cls, sign, mult, lam) in ex.items():
                    ok, vals, _, _ = ck.mode_values(p, case, eps, j, N)
                    if not ok or any(v != lam for v in vals):
                        moved.append((name, N, eps, j))
    return total, bad, moved


BAR = [n for n, c in cs.CASES.items() if 'next_order' in cs.serialize(n, c)]
total, bad, moved = score()
print(f'{len(BAR)} cases, {total} groups under the bar')
print('claim 1, every group passes:', 'holds' if not bad else f'FAILS: {bad}')
print('claim 2, every entry gets its own exact value:', 'holds' if not moved else f'FAILS: {moved}')
saved = ck.predicted_next
ck.predicted_next = lambda c, e, N: [[(m['cls'], m['sign'], ck.predicted(dict(c, spectrum=[m]), e)[0][2])] * m['mult']
                                     for m in c['spectrum']]
_, arm_bad, _ = score()
ck.predicted_next = saved
arm = sorted({(n, gi) for n, gi, *_ in arm_bad})
print('arm, the leading-order pairing as filed: claim 1 red at', arm)
arm_ok = [n for n, _ in arm] == ['T5/R2', 'T5/R2']
print('the arm is red at T5/R2\'s two lowest groups alone:', 'holds' if arm_ok else 'FAILS')
sys.exit(0 if not bad and not moved and arm_ok else 1)
