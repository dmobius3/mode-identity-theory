#!/usr/bin/env python3
"""K3's overlap, tested (DRIVER_PLAN.md, item 4; UB; DEVLOG 258). Case: synthetic.

Usage: test_k3.py MIT_REPO [--synthetic-only]

Claims 2 to 5 read entry 245's kept outputs (the dry run's rerun), each checked against the SHA-256 that entry records.

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
  5. E2 again from the kept outputs (UB). With K3's overlaps on C2a recomputed from the kept arrays under the guard,
     K3 reads 'not resolved, kernel exact', with (b) false and (c) failed with that reason at every cutoff, and E2's
     condition holds with the kept K5 code paths. Skipped with --synthetic-only.
"""
import copy
import hashlib
import json
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
E = 245                        # the dry run's rerun, whose outputs are kept in dev/runs
out, results = [], []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def kept(name):
    """Entry E's kept output, checked against the SHA-256 that entry records for it."""
    path = os.path.join(ROOT, 'dev', 'runs', f'{E:03d}_dry_{name}')
    with open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8') as f:
        line = next(x for x in f if f'kept as `dev/runs/{E:03d}_dry_{name}`' in x)
    with open(path, 'rb') as f:
        if hashlib.sha256(f.read()).hexdigest() != re.search(r'`([0-9a-f]{64})`', line).group(1):
            raise RuntimeError(f'{path} differs from the output entry {E} kept')
    return path


def arrays_at(case):
    Z_ = np.load(kept(f'{case}.npz'))
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


def claim5():
    with open(kept('C2a.json'), encoding='utf-8') as f:
        C2a = json.load(f)
    K5 = {}
    for n in ('C2a', 'C2b', 'C3'):
        with open(kept(f'{n}.json'), encoding='utf-8') as f:
            K5[n] = json.load(f)['checks'].get('K5_code_path')
    out_ = copy.deepcopy(C2a)
    for N, A in arrays_at('C2a'):
        p = out_['cutoffs'][N]['points'][ck.key(0.25)]
        old = p['k3_overlaps']
        p['k3_overlaps'] = dict(ck.k3_overlaps(A), group=old['group'], krein_negative=old['krein_negative'])
    k3c = ck.k3(out_, out_['case'])
    per = k3c['per_N']
    e2 = (all(K5.values()) and k3c['outcome'] == 'not resolved, kernel exact' and not any(v['b'] for v in per.values()))
    ok = e2 and all(not v['c'] and v['c_why'] for v in per.values())
    why = sum(bool(v['c_why']) for v in per.values())
    say(f"5. E2 from the kept outputs, K3's overlaps recomputed under the guard: {k3c['outcome']!r}; (b) at"
        f" {[N for N, v in per.items() if v['b']]}; (c) failed with its reason at {why} of {len(per)} cutoffs; the"
        f" kept K5 code paths {K5}: E2 {e2}: {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    devtools.require('synthetic')
    repo, only = sys.argv[1], '--synthetic-only' in sys.argv
    say(f"K3's overlap, tested{' (the synthetic claim only, before the dry run)' if only else ''}.")
    oks = [claim1()]
    if not only:
        ns = m815_functions(repo)
        oks += [claim2(ns), claim3(ns), claim4(ns), claim5()]
    failed = sum(not x for x in oks)
    say(f'{failed} failed')
    path = os.path.join(HERE, 'test_k3_synthetic.out' if only else 'test_k3.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f"K3's overlap{' (synthetic only)' if only else ''}: {'PASS' if not failed else 'FAIL'} ({failed} failed).",
                      'Each outcome derived before the run (the script\'s docstring).'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
