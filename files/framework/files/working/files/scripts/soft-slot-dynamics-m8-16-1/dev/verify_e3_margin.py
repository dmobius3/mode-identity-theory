#!/usr/bin/env python3
"""The units on the margin behind B1's fix (case: synthetic; no solve, no seed, nothing sealed is read).

Usage: dev/verify_e3_margin.py MIT_REPO, from the folder's root.

UA and UB on entry 42: checks 3 and 4 pass a pure eps^3 term at any size, so the 9.8 ceilings separating T5/R2's two
lowest next-order predictions at eps = 1 are the whole margin against an exchange. On entry 39's harness (checks.k1 and
checks.converged stubbed true), with the repaired run/checks.py:
  1. a pure eps^3 term, 50 ceilings at eps = 1, on T5/R2's lowest group, away from the next: every group passes;
  2. eps^3 terms on T5/R2's two lowest groups toward each other, k ceilings each at eps = 1, each group's own C_g(N):
     at k = 4.5 every group passes and each keeps its own value; at k = 5.5 the two read fail, their values exchanged.
Reported, unscored, for scale (UB): at the pyramid, M8.16's recorded departure from eps kappa s_g + eps^2 c_g(N) at the
point nearest eps = 1, in ceilings, for the quartet and the Krein-positive pair, from M8.16's record at MIT 87fc643,
checked against the SHA-256 its RUNLOG.json records."""
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402

REPO = sys.argv[1]
real_k1, real_conv = ck.k1, ck.converged


def record(case, extra):
    """The harness's record, each entry's lambda at eps kappa s_g + eps^2 c_g(N) + eps^3 extra[(N, entry)]."""
    cut = {}
    for N in case['cutoffs']:
        pts = {}
        for eps in ck.NEXT_EPS:
            groups, k = [], 0
            for g in sorted(case['next_order'][str(N)], key=lambda g: g['spectrum_index']):
                j = g['spectrum_index']
                m = case['spectrum'][j]
                lam = eps * ck._c(g['kappa_s']) + eps ** 2 * ck._c(g['c_g']) + eps ** 3 * extra.get((N, j), 0)
                groups.append(dict(c=[lam.real, lam.imag], cls=m['cls'], status='definite', size=m['mult'],
                                   neg=m['mult'] if (m['cls'] == 'imag' and m['sign'] == -1) else 0,
                                   idx=list(range(k, k + m['mult']))))
                k += m['mult']
            summary = dict(normA=1.0, groups=[dict(g, ok=True, pnorm=1.0, resid=0.0, why=None) for g in groups])
            pts[ck.key(eps)] = dict(accepted=True, eps_reached=eps, groups=groups, summary=summary)
        cut[str(N)] = dict(seed=dict(ok=True), points=pts)
    return dict(cutoffs=cut)


def own_values(case, rec, N, extra):
    """Whether mode_values gives each entry its own value at eps = 1."""
    p = rec['cutoffs'][str(N)]['points'][ck.key(1.0)]
    for g in case['next_order'][str(N)]:
        j = g['spectrum_index']
        lam = ck._c(g['kappa_s']) + ck._c(g['c_g']) + extra.get((N, j), 0)
        ok, vals, _, _ = ck.mode_values(p, case, 1.0, j, N)
        if not ok or vals != [lam]:
            return False
    return True


ck.k1 = lambda point, case: True
ck.converged = lambda case_out, eps, case: True
case = cs.serialize('T5/R2', cs.CASES['T5/R2'])
lo, nxt = sorted(case['next_order'][str(case['cutoffs'][0])], key=lambda g: abs(ck._c(g['kappa_s'])))[:2]
lo, nxt = lo['spectrum_index'], nxt['spectrum_index']


def by(N, j):
    return next(g for g in case['next_order'][str(N)] if g['spectrum_index'] == j)


def ceiling(g):
    return max(ck.CEILING[0] * abs(ck._c(g['c_g'])), ck.CEILING[1] * abs(ck._c(g['kappa_s'])))


def pred1(g):
    return ck._c(g['kappa_s']) + ck._c(g['c_g'])


def toward(k):
    extra = {}
    for N in case['cutoffs']:
        a, b = by(N, lo), by(N, nxt)
        u = (pred1(b) - pred1(a)) / abs(pred1(b) - pred1(a))
        extra[(N, lo)] = k * ceiling(a) * u
        extra[(N, nxt)] = -k * ceiling(b) * u
    return extra


away = {}
for N in case['cutoffs']:
    a, b = by(N, lo), by(N, nxt)
    away[(N, lo)] = -50 * ceiling(a) * (pred1(b) - pred1(a)) / abs(pred1(b) - pred1(a))
res = {gi: r['reading'] for gi, r in ck.bar(record(case, away), case).items()}
claim1 = all(x == 'pass' for x in res.values())
print(f'1. a pure eps^3 term of 50 ceilings on the lowest group, away from the next: {res}:', 'holds' if claim1 else 'FAILS')
out2 = {}
for k in (4.5, 5.5):
    extra = toward(k)
    rec = record(case, extra)
    res = {gi: r['reading'] for gi, r in ck.bar(rec, case).items()}
    own = all(own_values(case, rec, N, extra) for N in case['cutoffs'])
    out2[k] = (res, own)
    print(f'2. eps^3 terms toward each other, {k} ceilings each: readings {res}, each keeps its own value: {own}')
low_gis = [gi for gi, g in enumerate(case['next_order'][str(case['cutoffs'][0])]) if g['spectrum_index'] in (lo, nxt)]
claim2 = (all(x == 'pass' for x in out2[4.5][0].values()) and out2[4.5][1]
          and all(out2[5.5][0][gi] == 'fail' for gi in low_gis) and not out2[5.5][1])
print('   claim 2:', 'holds' if claim2 else 'FAILS')

# for scale: the pyramid's recorded departure at the point nearest eps = 1
ck.k1, ck.converged = real_k1, real_conv
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
show = lambda p: subprocess.run(['git', '-C', REPO, 'show', f'87fc643:{M816}/{p}'], check=True, capture_output=True).stdout  # noqa: E731
log = json.loads(show('run/out/RUNLOG.json'))
files = {f: h for r in log['completed'].values() for f, h in r['files'].items()}
raw = show('run/out/P5.json')
assert hashlib.sha256(raw).hexdigest() == files['P5.json'], 'P5.json differs from its RUNLOG.json'
P0, PC = json.loads(raw), cs.serialize('P5', cs.CASES['P5'])
print("reported, unscored: the pyramid's recorded departure from eps kappa s_g + eps^2 c_g(N) at the point nearest 1, in ceilings:")
for gi, g in enumerate(PC['next_order']['24']):
    if not g['under_bar']:
        continue
    row = []
    for N in PC['cutoffs']:
        x = ck.bar_cutoff(P0, PC, N, PC['next_order'][str(N)][gi])
        gN = PC['next_order'][str(N)][gi]
        ks, cg = ck._c(gN['kappa_s']), x['c_g']
        e, lam = x['x'][-1], x['lam'][-1]
        row.append(f"N = {N}: {abs(lam - e * ks - e ** 2 * cg) / x['ceiling']:.2f} at eps {e:.6f}")
    print(f"   group {gi} ({g['cls']}, Krein {g['krein']}): " + '; '.join(row))
sys.exit(0 if claim1 and claim2 else 1)
