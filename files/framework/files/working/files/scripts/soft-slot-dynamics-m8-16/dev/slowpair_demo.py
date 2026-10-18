#!/usr/bin/env python3
"""Step 3 of SLOWPAIR_PLAN.md: the slow-pair demonstration, under Step 2's L cut (linear.L_CUT = 1000 u ||L||, with its
gray zone up to G_L = 10 times it) and section 7's calibration otherwise. Case: synthetic. Scored: the gate, every other
row's derived outcome, no wrong type anywhere, three claims behind the arms, and four arms that must turn red. Nothing
sealed is touched, and nothing is tuned on it.

The systems are the scout's: dl_recal.py's Elliptic family (the phase chains diag(0, 5) and diag(0, -2), Krein-positive
oscillators up to 1,700, so ||L|| = 1,700 and ||A|| about 1,700, N = 40's scale), with one slow-pair block added, each
mixed by a random unitary, 10 mixings per row. A block diag(l1, l2) under the frame's 2 omega J0 has its pair at
x = lambda^2 with x^2 + (4 omega^2 + l1 + l2) x + l1 l2 = 0, and its small L eigenvalue mu is set from it so the pair sits
at s exactly:
  S1+, soft-soft, imaginary, Krein-positive: diag(k, k), k = s^2 + 2 omega s;
  S1-, soft-soft, imaginary, Krein-negative: diag(-k, -k), k = 2 omega s - s^2;
  S1r, soft-soft, real, anisotropic: diag(-k1, r k1), k1 from the quadratic at x = s^2, about 2 omega s / sqrt(r);
  S2, S3 and S4, near a crossing (K = 1): diag(k1, K), diag(-k1, -K) and diag(-k1, K), mu about 4 omega^2 s^2 / K.
Derived for a resolved reading: S1+ and S2 Elliptic, (n(L), n(D), K) = (1, 1, 0); S1- and S3 Elliptic (3, 1, 2) with
k_i^- = 1; S1r and S4 Hyperbolic (2, 1, 1) with k_r = 1. "Resolved" means all of: that type, those counts,
(k_r, k_c, k_i^-) and the balance; nothing unresolved; the pair and its partner found within s/2 of their exact places
and labelled as derived (imag or real), and, where imaginary, the pair's group definite with the derived Krein sign; and
L's zero count 2, the kernel's, equal to V0's chains (the plan's three conditions).

Derived before the run, from each system's exact ||A|| and ||L|| (unmixed) and the pair's exact mu (printed first):
  - A's gray zone: at m = 0.2 every s in {5e-6, 1e-5, 3e-5} clears it, 5e-6 by a factor of 3.03 (G margins 1.65e-6). At
    m = 72 (G margins 3.13e-5), s = 5e-6 and 1e-5 sit inside it, at 0.16 and 0.32 of its top and above margin/G, so
    those rows read Unresolved with the separation flagged; s = 1e-4 clears it by a factor of 3.2.
  - L's inertia: every S1 row's mu sits at least 1.9e3 times above L's gray zone (S1r at r = 100, omega = 7, s = 5e-6),
    and S2 to S4's at least 1.3 times above it (omega = 7, s = 5e-6; L's floor near a crossing is 4.4e-6 at omega = 7
    and 2.2e-6 at omega = 14). No row is blocked by L.
  - V0's leak: S1's sat at most 6.4e-4 of its bound in the scout (DEVLOG 133), so the S1 rows read resolved. Near a
    crossing it ran 0.05 to 6.1 times its bound there, through sigma_min(T22), so S2 to S4, and S1r at r = 10 and 100,
    are derived as resolved, or Unresolved through the leak alone, never a wrong type.
The rows, per structure and omega in {7, 14}: s = 5e-6, 1e-5 and 3e-5 at m = 0.2; s = 5e-6, 1e-5 and 1e-4 at m = 72.

Scored:
  1. The gate: S1+, S1- and S1r at the controls' largest measured r, 1.66 (Step 1: 1.658), resolved at every mixing for
     s = 1e-5 and 5e-6, at m = 0.2 and both omega (UB). A pass is the minimum demonstrated resolution capability for slow
     pairs of the controls' structure, not proof that the sealed in-span mode will resolve (UA).
  2. Every other row as derived: the S1 controls resolved (s = 3e-5 at m = 0.2, s = 1e-4 at m = 72); every structure
     Unresolved with the separation flagged at m = 72, s = 5e-6 and 1e-5; S2 to S4, and S1r at r = 10 and 100, resolved
     or Unresolved through the leak alone (its bound exceeded, with neither the separation nor L's gray zone flagged).
  3. No wrong type anywhere: a reading that is not Unresolved has the derived type, and one with nothing unresolved is
     resolved as derived.
  4. The claims behind arms (b) to (d), and the four arms, each red. Each arm reads the same systems as its claim.
     (a) The cut before Step 2 (1e-10 ||L||, gray zone to 1e-7 ||L||), on the gate's own systems: the gate fails.
     (b) L's gray zone removed (G_L = 1). A slow pair near a crossing, diag(mu, K) with K = 1000 at omega = 14, mu at
         the gray zone's geometric centre, sqrt(10) L_CUT ||L||, its pair at s = 2.59e-5 from the quadratic, 15.7 G
         margins out, with the leak bound held vacuous (leak_abs = 1, as dl_recal.py's claim 9), so L's check stands
         alone. Claim: under G_L = 10, L's gray-zone item at every mixing. Arm: under G_L = 1, at least one mixing reads
         Elliptic with nothing unresolved.
     (c) A cut below the controls' measured lift. The Elliptic family with both phase chains' zero lifted by the
         controls' largest measured lift, 1.37e-15 ||L|| (6.2 u; Step 1), at m = 72 and omega in {7, 14}: the lifted
         chains split at 7.7e-8 to 2.4e-7, inside the cluster, and stay chains at the rank floor. Claim: under L_CUT,
         Elliptic (1, 1, 0) with nothing unresolved and L's zero count 2, at every mixing. Arm: under a cut of 1 u ||L||,
         at least one mixing reads otherwise.
     (d) The zero-count check dropped. dl_recal.py's claim 9 (UB): diag(k1, K) with K = 1000 at omega = 14, its pair at
         s = 3e-6, its k1 about 43 u ||L||, below L_CUT, the leak bound held vacuous. Claim: the zero-count item at
         every mixing. Arm: without the check, at least one mixing reads Elliptic with nothing unresolved. The plan's
         S2 (K = 1) no longer reaches the check: its mu now sits above L's gray zone (UB, on claim 9).
Reported: S2 to S4's resolvable floors within the grid, with sigma_min(T22), the smallest singular value of the ordered
Schur form's outside block, beside the gap (UB); the leak against its bound; the pair's distance from its exact place.
"""
import json
import os
import sys
import numpy as np
from scipy.linalg import schur
from scipy.optimize import brentq
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from instrument import linear as ln, devtools  # noqa: E402
import dl_recal as d  # noqa: E402

devtools.require('synthetic')
d.rng = np.random.default_rng(20261022)
N_MIX = 10
OMEGAS = (7.0, 14.0)
K_CROSS = 1.0
R_GATE = 1.66                 # the controls' largest measured r, 1.658 (Step 1)
LIFT = 1.37e-15               # the controls' largest measured kernel lift, against ||L|| (Step 1)
OLD_CUT = dict(zero_rel=1e-10, l_gray=1e3)
ROWS = [(5e-6, 0.2), (1e-5, 0.2), (3e-5, 0.2), (5e-6, 72.0), (1e-5, 72.0), (1e-4, 72.0)]
STRUCTS = [('S1+', None), ('S1-', None), ('S1r', R_GATE), ('S1r', 10.0), ('S1r', 100.0), ('S2', None), ('S3', None),
           ('S4', None)]
EXPECT = {'S1+': ('Elliptic', (1, 1, 0), (0, 0, 0), 'imag', 0), 'S2': ('Elliptic', (1, 1, 0), (0, 0, 0), 'imag', 0),
          'S1-': ('Elliptic', (3, 1, 2), (0, 0, 1), 'imag', 1), 'S3': ('Elliptic', (3, 1, 2), (0, 0, 1), 'imag', 1),
          'S1r': ('Hyperbolic', (2, 1, 1), (1, 0, 0), 'real', None), 'S4': ('Hyperbolic', (2, 1, 1), (1, 0, 0), 'real', None)}
GRAY_ITEM = 'n(L): an eigenvalue of L lies in its gray zone'
ZERO_ITEM = "n(L): L's zero count"
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def name(kind, r):
    return kind if r is None else f'{kind} r={r:g}'


def pair_block(kind, s, omega, r=None, K=K_CROSS):
    """The slow-pair block that puts its pair at s exactly, and its small L eigenvalue's magnitude mu."""
    if kind == 'S1+':
        k = s * s + 2 * omega * s
        return np.diag([k, k]), k
    if kind == 'S1-':
        k = 2 * omega * s - s * s
        return np.diag([-k, -k]), k
    if kind == 'S1r':
        x = s * s
        k = ((r - 1) * x + np.sqrt((r - 1) ** 2 * x * x + 4 * r * (x * x + 4 * omega ** 2 * x))) / (2 * r)
        return np.diag([-k, r * k]), k
    if kind == 'S2':
        x = -s * s
        k = -(x * x + (4 * omega ** 2 + K) * x) / (x + K)
        return np.diag([k, K]), k
    if kind == 'S3':
        x = -s * s
        k = -(x * x + (4 * omega ** 2 - K) * x) / (K - x)
        return np.diag([-k, -K]), k
    x = s * s
    k = (x * x + (4 * omega ** 2 + K) * x) / (x + K)
    return np.diag([-k, K]), k


def exact(blocks, omega):
    """||L|| and ||A|| of the unmixed system; the mixing is orthogonal and commutes with J0, so neither moves."""
    Lp = d.place(blocks)
    return float(np.abs(np.linalg.eigvalsh(Lp)).max()), float(np.linalg.norm(ln.first_order(Lp, omega)[0], 2))


def derive(kind, r, omega, s, m):
    blk, mu = pair_block(kind, s, omega, r)
    nL, nA = exact(d.elliptic_blocks([blk]), omega)
    mg = ln.margin(nA, m)
    a = 'clear' if s >= ln.GRAY * mg else ('gray' if s >= mg / ln.GRAY else 'cluster')
    mu_rel = mu / nL
    lc = 'clear' if mu_rel >= ln.G_L * ln.L_CUT else ('gray' if mu_rel > ln.L_CUT else 'zero')
    assert a != 'cluster'
    if a != 'clear':
        want = 'A'
    elif lc != 'clear':
        want = 'L'
    elif kind in ('S1+', 'S1-') or r == R_GATE:
        want = 'resolved'
    else:
        want = 'leak'
    gate = (kind in ('S1+', 'S1-') or r == R_GATE) and m == 0.2 and s in (5e-6, 1e-5)
    return dict(kind=kind, r=r, omega=omega, s=s, m=m, blk=blk, mu=mu, normL=nL, normA=nA, margin=mg,
                a_ratio=s / (ln.GRAY * mg), a=a, l_ratio=mu_rel / (ln.G_L * ln.L_CUT), l=lc, want=want, gate=gate)


def blockers(r):
    b = set()
    for u in r['unresolved']:
        if u.startswith(d.SEP):
            b.add('A')
        elif u.startswith(GRAY_ITEM):
            b.add('L gray')
        elif u.startswith(ZERO_ITEM):
            b.add('L zero count')
        elif u.startswith('V0 does not match'):
            if r['sdim'] != d.TWO_CHAINS['dim'] or r['jordan_ranks'] != d.TWO_CHAINS['ranks']:
                b.add('V0 dim/ranks')
            if r['leak_bound'] is not None and r['symmetry_leak'] > r['leak_bound']:
                b.add('leak')
        else:
            b.add('other: ' + u.split(':')[0])
    return sorted(b)


def read(A, B, W, L, sym, row, **kw):
    r = d.rec(A, B, W, L, row['m'], sym, **kw)
    typ, cnt, ks, lab, nneg = EXPECT[row['kind']]
    s = row['s']
    tgt = 1j * s if lab == 'imag' else s
    lam = r['lam']
    j, jc = int(np.argmin(np.abs(lam - tgt))), int(np.argmin(np.abs(lam + tgt)))
    dev = float(max(abs(lam[j] - tgt), abs(lam[jc] + tgt)) / s)
    found = dev < 0.5 and r['labels'][j] == lab and r['labels'][jc] == lab
    krein = True
    if lab == 'imag':
        g = [x for x in r['imag_groups'] if abs(x[0] - tgt) < 0.5 * s]
        krein = len(g) == 1 and g[0][1] == 1 and g[0][4] == 'definite' and g[0][2] == nneg
    resolved = bool(r['type'] == typ and d.counts(r) == cnt and (r['kr'], r['kc'], r['ki']) == ks and r['balance']
                    and not r['unresolved'] and found and krein and r['dimkerL'] == 2 and r['blocks'] == 2)
    wrong = bool(r['type'] not in ('Unresolved', typ) or (not r['unresolved'] and not resolved))
    T, _, sdim = schur(A, output='real', sort=lambda x, y: abs(complex(x, y)) < r['margin'])
    smin = float(np.linalg.svd(T[sdim:, sdim:], compute_uv=False).min())
    return dict(type=r['type'], counts=list(d.counts(r)), ks=[r['kr'], r['kc'], r['ki']], resolved=resolved, wrong=wrong,
                blockers=blockers(r), unresolved=[u.split(':')[0] for u in r['unresolved']], dev=dev,
                gap=float(r['outside_min']), smin=smin, leak=float(r['symmetry_leak']), bound=r['leak_bound'],
                zeros=int(r['dimkerL']), chains=int(r['blocks']), label=str(r['labels'][j]))


def row_ok(row, reads):
    want = row['want']
    if want == 'resolved':
        return all(x['resolved'] for x in reads)
    if want == 'A':
        return all(x['type'] == 'Unresolved' and 'A' in x['blockers'] for x in reads)
    if want == 'L':
        return all(not x['resolved'] and any(b.startswith('L') for b in x['blockers']) for x in reads)
    return all(x['resolved'] or (x['type'] == 'Unresolved' and 'leak' in x['blockers'] and 'A' not in x['blockers']
                                 and 'L gray' not in x['blockers']) for x in reads)


def l_floor(kind, omega, r=None):
    """The s at which the pair's mu meets the top of L's gray zone, G_L L_CUT ||L||."""
    nL = exact(d.elliptic_blocks([pair_block(kind, 1e-5, omega, r)[0]]), omega)[0]
    return 10 ** brentq(lambda ls: pair_block(kind, 10 ** ls, omega, r)[1] / nL - ln.G_L * ln.L_CUT, -12, -2)


def summary(reads):
    h = {}
    for x in reads:
        key = 'RESOLVED' if x['resolved'] else ('WRONG ' + x['type'] if x['wrong'] else
                                                f"{x['type']} {x['blockers']}")
        h[key] = h.get(key, 0) + 1
    return h


def claim_gray():
    omega, K = 14.0, 1000.0
    nL = exact(d.elliptic_blocks([np.diag([1.0, K])]), omega)[0]
    mu = np.sqrt(ln.G_L) * ln.L_CUT * nL
    b = 4 * omega ** 2 + mu + K
    x = -2 * mu * K / (b + np.sqrt(b * b - 4 * mu * K))      # the small root, in its stable form
    s = float(np.sqrt(-x))
    blocks = d.elliptic_blocks([np.diag([mu, K])])
    rows = []
    for _ in range(N_MIX):
        A, B, W, L, sym = d.system(blocks, omega)
        r10 = d.rec(A, B, W, L, 0.2, sym, leak_abs=1.0)
        r1 = d.rec(A, B, W, L, 0.2, sym, leak_abs=1.0, l_gray=1.0)
        rows.append((bool(r10['type'] == 'Unresolved' and any(u.startswith(GRAY_ITEM) for u in r10['unresolved'])),
                     bool(r1['type'] == 'Elliptic' and not r1['unresolved']), r10['type'], r1['type'],
                     float(s / (ln.GRAY * r10['margin']))))
    return all(x[0] for x in rows), any(x[1] for x in rows), dict(mu_rel=mu / nL, mu_cut=mu / nL / ln.L_CUT, s=s, rows=rows)


def claim_lift():
    rows = []
    for omega in OMEGAS:
        blocks = d.elliptic_blocks()
        delta = LIFT * exact(blocks, omega)[0]
        blocks[0], blocks[1] = np.diag([delta, 5.0]), np.diag([delta, -2.0])
        for _ in range(N_MIX):
            A, B, W, L, sym = d.system(blocks, omega)
            ok = []
            for kw in ({}, dict(zero_rel=ln.U)):
                r = d.rec(A, B, W, L, 72.0, sym, **kw)
                ok.append((bool(r['type'] == 'Elliptic' and d.counts(r) == (1, 1, 0) and not r['unresolved']
                                and r['dimkerL'] == 2 and r['blocks'] == 2), r['type'], [u.split(':')[0] for u in r['unresolved']]))
            ev = np.sort(np.abs(np.linalg.eigvalsh((L + L.T) / 2)))[:2] / np.linalg.norm(L, 2) / ln.U
            rows.append((omega, ok[0][0], ok[1][0], float(ev[0]), float(ev[1]), ok[1][1], ok[1][2]))
    return all(x[1] for x in rows), not all(x[2] for x in rows), rows


def claim_zero():
    omega, s, K = 14.0, 3e-6, 1000.0
    x = -s * s
    k1 = -(x * x + (4 * omega ** 2 + K) * x) / (x + K)
    blocks = d.elliptic_blocks([np.diag([k1, K])])
    rows = []
    for _ in range(N_MIX):
        A, B, W, L, sym = d.system(blocks, omega)
        rc = d.rec(A, B, W, L, 0.2, sym, leak_abs=1.0)
        rn = d.rec(A, B, W, L, 0.2, sym, leak_abs=1.0, zero_count=False)
        rows.append((any(u.startswith(ZERO_ITEM) for u in rc['unresolved']), bool(rn['type'] == 'Elliptic' and not rn['unresolved']),
                     int(rc['dimkerL']), int(rc['blocks'])))
    return all(x_[0] for x_ in rows), any(x_[1] for x_ in rows), dict(k1_u=k1 / np.linalg.norm(L, 2) / ln.U, rows=rows)


def main():
    say(f"Step 3, the slow-pair demonstration: L's cut {ln.L_CUT:.2e} ||L|| (1000 u), its gray zone to"
        f" {ln.G_L * ln.L_CUT:.2e} ||L|| (G_L = {ln.G_L:g}); A's margin = 2 sqrt(u ||A|| max(m, 0.2)), G = {ln.GRAY:g},"
        f" the leak at most {ln.KAPPA_L:g} u ||A|| / gap. {N_MIX} mixings per row.")
    rows = [derive(k, r, w, s, m) for k, r in STRUCTS for w in OMEGAS for s, m in ROWS]
    say('Derived before the run (A: s against the top of A\'s gray zone; L: mu against the top of L\'s):')
    for k, r in STRUCTS:
        for w in OMEGAS:
            rr = [x for x in rows if (x['kind'], x['r'], x['omega']) == (k, r, w)]
            say(f"  {name(k, r):10s} omega {w:4.0f}: " + '; '.join(
                f"{x['s']:.0e} m {x['m']:g}: A {x['a_ratio']:.2f}, L {x['l_ratio']:.1e} -> {x['want']}" for x in rr))
    say()
    failed, n_wrong, gate_rows = 0, 0, []
    for row in rows:
        reads, old = [], []
        for _ in range(N_MIX):
            A, B, W, L, sym = d.system(d.elliptic_blocks([row['blk']]), row['omega'])
            reads.append(read(A, B, W, L, sym, row))
            if row['gate']:
                old.append(read(A, B, W, L, sym, row, **OLD_CUT))
        row['reads'], row['old'] = reads, old
        row['ok'] = row_ok(row, reads)
        n_wrong += sum(x['wrong'] for x in reads)
        if row['gate']:
            gate_rows.append(row)
        leaks = [x['leak'] / x['bound'] for x in reads if x['bound']]
        say(f"{'GATE ' if row['gate'] else '     '}{name(row['kind'], row['r']):10s} omega {row['omega']:4.0f} s {row['s']:.0e}"
            f" m {row['m']:4g}: {'as derived' if row['ok'] else 'NOT AS DERIVED'} ({row['want']}); {summary(reads)};"
            f" leak/bound {min(leaks):.1e} to {max(leaks):.1e}; gap {np.median([x['gap'] for x in reads]):.2e},"
            f" sigma_min(T22) {np.median([x['smin'] for x in reads]):.2e}; pair off by {max(x['dev'] for x in reads):.1e} s")
    gate = all(x['ok'] for x in gate_rows)
    failed += not gate
    others = [x for x in rows if not x['gate']]
    n_bad = sum(not x['ok'] for x in others)
    failed += n_bad + (n_wrong > 0)
    say()
    say(f"1. The gate (S1+, S1- and S1r at r = {R_GATE:g}; s = 1e-5 and 5e-6; m = 0.2; omega 7 and 14): {'PASS' if gate else 'FAIL'},"
        f" {sum(x['ok'] for x in gate_rows)} of {len(gate_rows)} rows resolved at every mixing")
    say(f"2. Every other row as derived: {'PASS' if not n_bad else 'FAIL'}, {len(others) - n_bad} of {len(others)}")
    say(f"3. No wrong type: {'PASS' if not n_wrong else 'FAIL'}, {n_wrong} wrong of {sum(len(x['reads']) for x in rows)} readings")
    say('Floors near a crossing, and S1r at r = 10 and 100 (reported): resolved of 10 at m = 0.2 by s, and at m = 72, s = 1e-4;'
        " A's floor (G margins at m = 0.2) and L's floor (mu at the top of L's gray zone); sigma_min(T22) / gap, medians")
    for k, r in [('S1r', 10.0), ('S1r', 100.0), ('S2', None), ('S3', None), ('S4', None)]:
        for w in OMEGAS:
            rr = [x for x in rows if (x['kind'], x['r'], x['omega']) == (k, r, w)]
            res = '; '.join(f"{x['s']:.0e}{' m 72' if x['m'] == 72.0 else ''} {sum(y['resolved'] for y in x['reads'])}"
                            for x in rr if x['want'] != 'A')
            ratio = ', '.join(f"{np.median([y['smin'] / y['gap'] for y in x['reads']]):.1e}" for x in rr if x['want'] != 'A')
            say(f"  {name(k, r):10s} omega {w:4.0f}: {res}; A's floor {ln.GRAY * rr[0]['margin']:.2e}, L's floor"
                f" {l_floor(k, w, r):.2e}; sigma_min(T22)/gap {ratio}")
    say()
    say('4. The claims behind the arms, and the arms:')
    arm_a = not all(all(x['resolved'] for x in row['old']) for row in gate_rows)
    old_res = sum(sum(x['resolved'] for x in row['old']) for row in gate_rows)
    say(f"   (a) the cut before Step 2, on the gate's systems: the gate resolved at {old_res} of"
        f" {sum(len(row['old']) for row in gate_rows)} readings; " + '; '.join(
            f"{name(row['kind'], row['r'])} omega {row['omega']:g} s {row['s']:.0e} {summary(row['old'])}" for row in gate_rows))
    ok_b, arm_b, info_b = claim_gray()
    say(f"   (b) L's gray zone: mu = {info_b['mu_cut']:.3f} L_CUT ({info_b['mu_rel']:.2e} ||L||), s = {info_b['s']:.3e},"
        f" {info_b['rows'][0][4]:.1f} G margins out. Claim, under G_L = 10: {'PASS' if ok_b else 'FAIL'}, the gray-zone item"
        f" at {sum(x[0] for x in info_b['rows'])} of {len(info_b['rows'])}; under G_L = 1, clean Elliptic at"
        f" {sum(x[1] for x in info_b['rows'])} of {len(info_b['rows'])}")
    ok_c, arm_c, rows_c = claim_lift()
    hist_c = {}
    for x in rows_c:
        hist_c[f'{x[5]} {x[6]}'] = hist_c.get(f'{x[5]} {x[6]}', 0) + 1
    say(f"   (c) the lifted kernel, {LIFT:.2e} ||L||: computed at {min(x[3] for x in rows_c):.2f} to {max(x[4] for x in rows_c):.2f} u ||L||."
        f" Claim, under L_CUT: {'PASS' if ok_c else 'FAIL'}, resolved at {sum(x[1] for x in rows_c)} of {len(rows_c)};"
        f" under a cut of 1 u ||L||, resolved at {sum(x[2] for x in rows_c)} of {len(rows_c)}: {hist_c}")
    ok_d, arm_d, info_d = claim_zero()
    say(f"   (d) the zero count: k1 = {info_d['k1_u']:.1f} u ||L||. Claim, with the check: {'PASS' if ok_d else 'FAIL'}, its item"
        f" at {sum(x[0] for x in info_d['rows'])} of {len(info_d['rows'])} (zero count against chains"
        f" {sorted({(x[2], x[3]) for x in info_d['rows']})}); without it, clean Elliptic at {sum(x[1] for x in info_d['rows'])}"
        f" of {len(info_d['rows'])}")
    failed += (not ok_b) + (not ok_c) + (not ok_d)
    arms = [("(a) the cut before Step 2: the gate", arm_a), ('(b) G_L = 1: the gray-zone claim', arm_b),
            ('(c) a cut of 1 u ||L||: the lifted-kernel claim', arm_c), ('(d) the zero-count check dropped: its claim', arm_d)]
    for label, red in arms:
        failed += not red
        say(f"   arm {label}: {'red, as it must be' if red else 'NOT RED'}")
    say(f"{failed} failed")
    path = os.path.join(HERE, 'slowpair_demo.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    jpath = os.path.join(HERE, 'slowpair_demo.json')
    keep = ('kind', 'r', 'omega', 's', 'm', 'mu', 'normL', 'normA', 'margin', 'a_ratio', 'l_ratio', 'want', 'gate', 'ok',
            'reads', 'old')
    with open(jpath, 'w', encoding='utf-8') as f:
        json.dump(dict(L_CUT=ln.L_CUT, G_L=ln.G_L, seed=20261022, n_mix=N_MIX,
                       rows=[{k: x[k] for k in keep} for x in rows],
                       arm_b=dict(claim=ok_b, red=arm_b, **{k: v for k, v in info_b.items() if k != 'rows'},
                                  rows=[list(x) for x in info_b['rows']]),
                       arm_c=dict(claim=ok_c, red=arm_c, rows=[list(x) for x in rows_c]),
                       arm_d=dict(claim=ok_d, red=arm_d, k1_u=info_d['k1_u'], rows=[list(x) for x in info_d['rows']]),
                       failed=failed), f, indent=1)
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f"Step 3, the slow-pair demonstration under Step 2's cut: the gate {'PASS' if gate else 'FAIL'};"
                      f" every other row as derived {'PASS' if not n_bad else 'FAIL'} ({len(others) - n_bad} of {len(others)});"
                      f" {n_wrong} wrong types; the claims behind arms (b) to (d) {'PASS' if ok_b and ok_c and ok_d else 'FAIL'};"
                      f" arms red {sum(r_ for _, r_ in arms)} of 4; {failed} failed.",
                      'Each outcome derived before the run (SLOWPAIR_PLAN.md, Step 3; the derivation printed first).'],
                     outputs=(path, jpath))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
