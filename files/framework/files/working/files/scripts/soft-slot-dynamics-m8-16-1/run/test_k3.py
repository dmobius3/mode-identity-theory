#!/usr/bin/env python3
"""K3's overlap, tested (M8.16's DRIVER_PLAN.md, item 4; UB; its DEVLOG 258), carried into M8.16.1 (M8.16.1's
DRIVER_PLAN.md v2, The tests). Case: synthetic.

Usage: test_k3.py MIT_REPO [--synthetic-only]

Claims 2 to 4 read M8.16's entry 245's kept outputs (its dry run's rerun) from M8.16's folder in MIT_REPO's history at
the record's commit, 87fc643, each checked against the SHA-256 that entry records. M8.16's claims 5 and 7 read K3(a)'s
slow-band clause on C2a, a control with no next-order values; they are test_verdicts.py's now, on pyramid records.
This script writes no development log entry.

Claims, derived before the run:
  1. A synthetic vector of known overlap. In R^6, with rotations e1, e2, e3, the fibre direction e4, the phase partner
     e5 and the axis rotation z = e3 + 0.158 e4, the spans are XY = span{e1, e2} and Z = span{e3}. For
     s = (a e1 + b e3 + c e6) e^{i alpha}, normalized, checks.static_overlap reads |a| on XY and |b| on Z, to 1e-14.
     Arm: Z taken as z itself, unprojected, reads |b| / sqrt(1 + 0.158^2) instead, which differs from |b| (UB's
     point at the pyramid's seed).
  2. Against M8.15.x's own functions. real_orthonormal, project_out and static_overlap, read from verdict.py at MIT
     2c27cea and applied with M = I as control_2a.py's point_record applies them, give the same two overlaps of the
     point's static part as checks.k3_spans and checks.static_overlap, to 1e-12, at C3's points (eps = 0.25, every
     cutoff). C2a's points, where Q_Z is undefined, are claim 4's. Skipped with --synthetic-only.
  3. Order one (UB). At C3's points, T_x phi and T_y phi read (XY 1, Z 0) and T_z phi reads (XY 0, Z 1), to 1e-12, in
     both implementations. Skipped with --synthetic-only.
  4. The arm (UB). At C2a's points, the axis rotation's part outside the fibre span, ||P_R z||/||z||, is below 1e-6 at
     every cutoff, so checks.k3_spans gives no spans and K3's overlap record reads (c) failed with that reason.
     Reported: M8.15.x's functions, which have no such guard, form a Z from the round-off there. Skipped with
     --synthetic-only.
  6. K3(d) by the rule's own row (xrodz, B1), through convergence.separation on synthetic summaries: a Krein-negative
     imaginary group at i(0.1 + 3 delta), i(0.1 + delta), i 0.1 at N = 16, 24, 32 (delta = 2e-4, so U = delta), and a
     Krein-positive one D above it at each cutoff. At D = 10.5 delta the rule passes the group and (d) holds; at
     D = 9.5 delta it fails it and (d) fails with the rule's reason. Arm: the filed test, the N = 16 centre within
     1e-3 of the row's, fails the point the rule passes. (d) fails when no row, or more than one, reads the group, and
     when (b) found none.
  8. K3's pick never crashes (xrodz, B3): one definite Krein-negative group in the band is picked; with none, the
     smallest group in the band; with groups but none in the band, or no groups, nothing is picked. Arm: the filed
     expression raises ValueError on groups none of which lies in the band.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import checks as ck  # noqa: E402

SRC = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x/m8_15x_solver/verdict.py'
E = 245                        # M8.16's dry run's rerun, whose outputs are kept in its dev/runs
RECORD = '87fc643'
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
out, results = [], []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def kept(name):
    """M8.16's entry E's kept output, read from MIT's history and checked against the SHA-256 that entry records."""
    show = lambda path: subprocess.run(['git', '-C', sys.argv[1], 'show', f'{RECORD}:{M816}/{path}'], check=True,  # noqa: E731
                                       capture_output=True).stdout
    line = next(x for x in show('DEVLOG.md').decode('utf-8').splitlines() if f'kept as `dev/runs/{E:03d}_dry_{name}`' in x)
    raw = show(f'dev/runs/{E:03d}_dry_{name}')
    if hashlib.sha256(raw).hexdigest() != re.search(r'`([0-9a-f]{64})`', line).group(1):
        raise RuntimeError(f'{name} differs from the output entry {E} kept')
    return raw


def arrays_at(case):
    Z_ = np.load(io.BytesIO(kept(f'{case}.npz')))
    for N in sorted({k.split('_N')[1] for k in Z_.files}, key=int):
        yield N, {k: Z_[f'{k}_N{N}'] for k in ('s', 'X', 'fib', 'chi', 'z')}


def claim1():
    e = np.eye(6)
    X = e[:, :3]
    fib = e[:, 3:4]
    chi = e[:, 4]
    z = e[:, 2] + 0.158 * e[:, 3]
    a, b, c = 0.8, 0.5, np.sqrt(1 - 0.8 ** 2 - 0.5 ** 2)
    s = (a * e[:, 0] + b * e[:, 2] + c * e[:, 5]) * np.exp(0.7j)
    XY, Z, _ = ck.k3_spans(X, fib.T, chi, z)
    xy, zz = ck.static_overlap(s, XY), ck.static_overlap(s, Z)
    ok = abs(xy - a) < 1e-14 and abs(zz - b) < 1e-14 and XY.shape[1] == 2 and Z.shape[1] == 1
    raw = ck.static_overlap(s, (z / np.linalg.norm(z))[:, None])
    arm = abs(raw - b / np.sqrt(1 + 0.158 ** 2)) < 1e-14 and abs(raw - b) > 1e-3
    say(f"1. the synthetic vector: XY {xy:.15f} against {a}, Z {zz:.15f} against {b}: {'PASS' if ok else 'FAIL'};"
        f" the arm, Z unprojected, reads {raw:.6f}, not {b}: {'PASS' if arm else 'FAIL'}")
    return ok and arm


def m815_functions(repo):
    src = subprocess.run(['git', '-C', repo, 'show', f'2c27cea:{SRC}'], check=True, capture_output=True, text=True).stdout
    ns = {'np': np}
    for name in ('real_orthonormal', 'project_out', 'static_overlap'):
        i0 = src.index(f'def {name}(')
        i1 = src.index('\ndef ', i0 + 1)
        exec(src[i0:i1], ns)
    return ns


def m815_spans(ns, A):
    """M8.15.x's spans, as control_2a.py's point_record forms them, with M = I."""
    I = np.eye(A['X'].shape[0])
    Fb = ns['real_orthonormal'](np.column_stack([A['fib'], A['chi']]), I)
    R = ns['real_orthonormal'](ns['project_out'](A['X'], Fb, I), I)
    Zm = ns['real_orthonormal']((R @ (R.T @ (I @ A['z'])))[:, None], I)
    XYm = ns['real_orthonormal'](R - Zm @ (Zm.T @ (I @ R)), I)
    return XYm, Zm, lambda v, B: ns['static_overlap'](v, B, I, len(v))


def claim2(ns):
    worst, n = 0.0, 0
    for N, A in arrays_at('C3'):
        XY, Zs, _ = ck.k3_spans(A['X'], A['fib'].T, A['chi'], A['z'])
        mine = (ck.static_overlap(A['s'], XY), ck.static_overlap(A['s'], Zs))
        XYm, Zm, ov = m815_spans(ns, A)
        theirs = (ov(A['s'], XYm), ov(A['s'], Zm))
        d = max(abs(mine[0] - theirs[0]), abs(mine[1] - theirs[1]))
        worst, n = max(worst, d), n + 1
        say(f"   C3 N = {N}: mine (XY {mine[0]:.12f}, Z {mine[1]:.12f}), M8.15.x's (XY {theirs[0]:.12f},"
            f" Z {theirs[1]:.12f}): {d:.1e}")
    ok = n > 0 and worst <= 1e-12
    say(f"2. against M8.15.x's functions at C3's {n} points: largest difference {worst:.1e}:"
        f" {'PASS' if ok else 'FAIL'}")
    return ok


def claim3(ns):
    want = [(1.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    worst, n = 0.0, 0
    for N, A in arrays_at('C3'):
        XY, Zs, axis = ck.k3_spans(A['X'], A['fib'].T, A['chi'], A['z'])
        XYm, Zm, ov = m815_spans(ns, A)
        for j, (wx, wz) in enumerate(want):
            t = A['X'][:, j]
            got = [(ck.static_overlap(t, XY), ck.static_overlap(t, Zs)), (ov(t, XYm), ov(t, Zm))]
            worst = max([worst] + [max(abs(x - wx), abs(y - wz)) for x, y in got])
            n += 1
        say(f"   C3 N = {N}: ||P_R z||/||z|| = {axis:.3f}; T_x, T_y, T_z read as wanted in both implementations to"
            f" {worst:.1e}")
    ok = n == 9 and worst <= 1e-12
    say(f"3. order one at C3's points: (XY 1, Z 0), (XY 1, Z 0), (XY 0, Z 1), largest departure {worst:.1e}:"
        f" {'PASS' if ok else 'FAIL'}")
    return ok


def claim4(ns):
    ok, xs = True, []
    for N, A in arrays_at('C2a'):
        rec = ck.k3_overlaps(A)
        XYm, Zm, ov = m815_spans(ns, A)
        xs.append(ov(A['X'][:, 0], XYm))
        ok &= rec['xy'] is None and rec['axis'] < ck.AXIS_MIN and rec['why'] is not None
        say(f"   C2a N = {N}: ||P_R z||/||z|| = {rec['axis']:.1e}; the record: (c) {rec['why']!r}")
    say(f"4. the arm at C2a's points: Q_Z undefined at every cutoff, with the reason: {'PASS' if ok else 'FAIL'}."
        f" Reported: M8.15.x's functions, with no guard, read T_x's XY as {', '.join(f'{x:.2f}' for x in xs)}")
    return ok


def summaries(y_in, y_opp):
    """Three cutoffs' convergence summaries, lowest first: a Krein-negative imaginary group at i y_in[k] (eigenvalue
    index 0) and a Krein-positive one at i y_opp[k] (index 1), with the fields convergence.summarize writes."""
    def g(y, neg, i):
        return dict(c=[0.0, y], cls='imag', size=1, neg=neg, status='definite', idx=[i], resid=0.0, left=0.0,
                    cond=1.0, pnorm=1.0, idem=0.0, ok=True, why=None)
    return [dict(type='Elliptic', nL=0, nD=0, K=0, sdim=0, ranks=[0, 0], v0=True, unresolved=[], margin=1e-14,
                 gray=10.0, normA=1.0, krein=[1], groups=[g(a, 1, 0), g(b, 0, 1)]) for a, b in zip(y_in, y_opp)]


def claim6():
    from instrument import convergence as cv
    dl = 2e-4
    y = [0.1 + 3 * dl, 0.1 + dl, 0.1]
    reads = {}
    for name, D in (('pass', 10.5 * dl), ('fail', 9.5 * dl)):
        res = cv.separation(summaries(y, [v + D for v in y]))
        reads[name] = dict(rows=res['rows'])
    d_ok, why_ok, row_ok = ck.k3_d(reads['pass'], [0])
    d_no, why_no, _ = ck.k3_d(reads['fail'], [0])
    c0 = complex(0, y[0])
    filed = abs(complex(*row_ok['c']) - c0) <= 1e-3 * abs(c0)
    none_ = ck.k3_d(reads['pass'], [7])[0]
    twice = ck.k3_d(dict(rows=reads['pass']['rows'] + [dict(row_ok)]), [0])[0]
    nob = ck.k3_d(reads['pass'], None)[0]
    ok = d_ok and not filed and not d_no and why_no and not none_ and not twice and not nob
    say(f"6. K3(d) by the rule's own row: at D = 10.5 delta (d) {d_ok} (ratio {row_ok['ratio']:.2f}); at 9.5 delta"
        f" (d) {d_no} ({why_no}); the filed 1e-3 test on the point the rule passes: {filed}; no row {none_}, two rows"
        f" {twice}, none found by (b) {nob}: {'PASS' if ok else 'FAIL'}")
    return ok


def claim8():
    def G(y, neg=0):
        return dict(c=[0.0, y], cls='imag', size=1, neg=neg, status='definite', idx=[0])
    band = 1.0
    cases = [('one definite Krein-negative group in the band', [G(0.5, 1), G(0.3)], (0.5, True)),
             ('none Krein-negative: the smallest in the band', [G(0.5), G(0.3), G(2.0)], (0.3, False)),
             ('groups, none in the band', [G(2.0), G(3.0)], (None, False)),
             ('no groups', [], (None, False))]
    ok, lines = True, []
    for label, groups, want in cases:
        g, neg = ck.k3_pick(groups, band)
        got = (g['c'][1] if g else None, neg)
        ok &= got == want
        lines.append(f"     {'PASS' if got == want else 'FAIL'}  {label}: {got}")
    groups = cases[2][1]
    try:
        neg = [g for g in groups if g['cls'] == 'imag' and g['status'] == 'definite' and g['neg'] == g['size']
               and np.hypot(*g['c']) <= band]
        _ = neg[0] if len(neg) == 1 else (min((g for g in groups if np.hypot(*g['c']) <= band),
                                              key=lambda g: np.hypot(*g['c'])) if groups else None)
        arm = 'no exception'
    except ValueError as e:
        arm = f'ValueError: {e}'
    ok &= arm.startswith('ValueError')
    say(f"8. K3's pick never crashes: {'PASS' if ok else 'FAIL'}; arm, the filed expression on groups none in the band:"
        f" {arm}")
    for line in lines:
        say(line)
    return ok


def main():
    devtools.require('synthetic')
    repo, only = sys.argv[1], '--synthetic-only' in sys.argv
    say(f"K3's overlap, tested{' (the synthetic claim only, before the dry run)' if only else ''}.")
    oks = [claim1(), claim6(), claim8()]
    if not only:
        ns = m815_functions(repo)
        oks += [claim2(ns), claim3(ns), claim4(ns)]
    failed = sum(not x for x in oks)
    say(f'{failed} failed')
    path = os.path.join(HERE, 'test_k3_synthetic.out' if only else 'test_k3.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
