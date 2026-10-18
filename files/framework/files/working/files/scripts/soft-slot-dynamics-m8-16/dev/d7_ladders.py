#!/usr/bin/env python3
"""D7's full-window ladders, under LADDER_PLAN.md (both units' conditions folded; Blake's base budget, 2026-10-16).
Cases: C2a, C2b, C3.

Usage: d7_ladders.py CONTROL [--trial [--arm guard_distance|guard_record|guard_unsafe]]
  base:    M8.15's ladder(0.25, eps_max) at N = 24 and at N = 32, each from the germ at eps = 0.25, continued point by
           point; then N = 40 at the ladder's top three points, each seeded from N = 32's accepted point at the same
           eps, embedded exactly, with UA's branch-identity guard; then the pause: the points whose 24 -> 32 change
           exceeds the fraction, and their estimated N = 40 cost, are reported, and no further N = 40 point runs.
  --trial: the same code at N = 16 to eps = 2, then N = 24 at that range's top two points, seeded from N = 16.
  --arm:   a mutation arm, on the trial only (UA, 2026-10-16): the guard forced to fail by its distance (the bound set
           below any distance) or by its record (the record treated as differing from N = 16's). Each must leave
           every N = 24 comparison Unresolved, with no agreement and no cross-N change; the run fails if it does not.
           guard_unsafe forces the distance failure with the fail-safe off, which is the reporting path as the base
           ladders ran it; there the check must fail, and the run fails if it does not.

Claims at each point, fixed before the run:
  1. accepted (the enforced bound), at the target eps within 1e-6;
  2. V0 matches EXPECTED_V0.md's row, with the actual tangents' leak at most 1e-8; otherwise the point is Unresolved
     and reported, never re-expected (not a failure);
  3. where both are resolved, the type agrees with M8.15's at that eps, K with M8.15's nL - nB_cluster, and k_i^-
     with M8.15's ki_minus. The Krein part is that count, not each slow mode's sign (UA). A comparison that is not
     resolved is reported Unresolved, and neither agrees nor fails.
Reported, unscored:
  - n(L) and n(D), beside M8.15's nL and nB_cluster;
  - M8.15's tracked slow eigenvalues (its `genuine` list at level 3: five imaginary for C2a and C2b, three real for
    C3), each matched to the nearest M8.16 eigenvalue of its class and compared per unit eps, beside M8.15's own
    level-2 to level-3 change;
  - the matched slow eigenvalues' change per unit eps from N = 24 to 32, against the fraction 1e-6, and at N = 40
    from 32 to 40;
  - at N = 40, UA's guard: the embedding's residual, the symmetry-aligned distance, both norms and both frequencies.
    The identity is Unresolved if the distance exceeds 1e-2, or if the type, indices, the imaginary groups' negative
    Krein counts or V0 differ from N = 32's. A point whose identity is Unresolved has its comparison marked Unresolved,
    and no cross-N change: it is never treated as one branch (LADDER_PLAN.md; the fail-safe, UA, 2026-10-16);
  - the time per point.
The expectations (Q, k, r_u, the type and the indices at small amplitude) are d7_controls.py's, repeated here.
M8.15's records: reference/m815/branch_*.json, copied from MIT at 6058f95 (DEVLOG 100).
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import basis, functional as fn, linear as ln, newton, branches as br, devtools  # noqa: E402

U = np.finfo(float).eps
FRACTION, GUARD = 1e-6, 1e-2
ARMS = ('guard_distance', 'guard_record', 'guard_unsafe')
ARM = None
EXPECT = {
    'C2a': dict(lam0=48.0, Q=Fr(1288, 1287), k=3, r=1, kind='i', eps_max=72.0, record='branch_C2a_R4.json'),
    'C2b': dict(lam0=63.0, Q=Fr(144, 143), k=5, r=1, kind='i', eps_max=132.0, record='branch_C2b_R2.json'),
    'C3': dict(lam0=48.0, Q=Fr(175, 143), k=4, r=4, kind='r', eps_max=72.0, record='branch_C3_R4.json'),
}
out, rec_json = [], {}


def say(s):
    print(s, flush=True)
    out.append(s)


def ladder(eps_min, eps_max):
    """M8.15's ladder, as in soft-slot-dynamics/m8_15_solver/continuation.py at MIT 6058f95."""
    out_, k = [], 0
    while True:
        e = 0.25 * 2 ** (k / 2)
        if e > eps_max * (1 + 1e-12):
            break
        if e >= eps_min * (1 - 1e-12):
            out_.append(e)
        k += 1
    if not out_ or abs(out_[-1] - eps_max) > 1e-9 * eps_max:
        out_.append(eps_max)
    return out_


def summary(r):
    return dict(type=r['type'], nL=r['nL'], nD=r['nD'], K=r['K'], kr=r['kr'], kc=r['kc'], ki=r['ki'], sdim=r['sdim'],
                ranks=r['jordan_ranks'], blocks=r['blocks'], leak=r['symmetry_leak'], v0_matches=r['v0_matches'],
                margin=r['margin'], cluster_max=r['cluster_max'], outside_min=r['outside_min'], balance=r['balance'],
                unresolved=r['unresolved'], krein=sorted(g[2] for g in r['imag_groups'] if g[2] > 0))


def candidates(r, kind):
    """The slow eigenvalues as the record itself classifies them (UA): typed, outside the gray zone."""
    lam, lab = r['lam'], r['labels']
    if kind == 'i':
        return np.sort(lam.imag[(lab == 'imag') & (lam.imag > 0)])
    return np.sort(lam.real[(lab == 'real') & (lam.real > 0)])


def m815_slow(p, kind):
    vals = [z[0][1] for z in p['genuine'] if z[0][1] > 0] if kind == 'i' else \
           [z[0][0] for z in p['genuine'] if z[0][0] > 0 and abs(z[0][1]) < 1e-9]
    return sorted(vals)


def match(targets, pool):
    """Each target matched to the nearest unused value of pool, in order of the targets; None if the pool runs out."""
    used, outv = set(), []
    for t in targets:
        order = [j for j in np.argsort(np.abs(pool - t)) if j not in used]
        if not order:
            return None
        used.add(order[0])
        outv.append(float(pool[order[0]]))
    return outv


def point_record(Fn, K, c, lam, expected):
    t0 = time.perf_counter()
    L = Fn.hess_dense(c, lam)
    t_h = time.perf_counter() - t0
    A, Bm, W = ln.first_order(L, np.sqrt(lam))
    margin = ln.margin(np.linalg.norm(A, 2), float(np.vdot(c, c).real))
    sym = [np.concatenate([t, np.zeros(2 * Fn.B.m)]) for t in br.tangent_vectors(Fn, c, K)]
    t1 = time.perf_counter()
    r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=expected)
    return r, t_h, time.perf_counter() - t1


def compare(name, E, eps, r, eps_reached, m15):
    """Claim 3 and the unscored readings against M8.15's records at this eps."""
    p3 = next(p for p in m15['points'] if abs(p['eps'] - eps) < 1e-9)
    p2 = next(p for p in m15['level2'] if abs(p['eps'] - eps) < 1e-9)
    t15 = next(t['type'] for t in m15['types'] if abs(t['eps'] - eps) < 1e-9)
    K15 = p3['nL'] - p3['nB_cluster']
    resolved = r['type'] in ('Elliptic', 'Hyperbolic') and t15 in ('Elliptic', 'Hyperbolic')
    agree = bool(r['type'] == t15 and r['K'] == K15 and r['ki'] == p3['ki_minus']) if resolved else None
    s3 = [v / p3['eps_reached'] for v in m815_slow(p3, E['kind'])]
    s2 = [v / p2['eps_reached'] for v in m815_slow(p2, E['kind'])]
    pool = candidates(r, E['kind']) / eps_reached
    mine = match(s3, pool)
    dev = max(abs(a - b) / abs(b) for a, b in zip(mine, s3)) if mine else None
    d23 = max(abs(a - b) / abs(b) for a, b in zip(s2, s3)) if len(s2) == len(s3) and s3 else None
    return dict(type15=t15, K15=K15, nL15=p3['nL'], nB15=p3['nB_cluster'], ki15=p3['ki_minus'], resolved=resolved,
                agree=agree, slow=mine, dev_vs_m815_l3=dev, m815_l2_vs_l3=d23,
                why=None if resolved else 'not both resolved')


def status(cmpd):
    """The comparison as reported: agree, DISAGREE, or Unresolved with its reason; an Unresolved one never agrees."""
    if cmpd['agree'] is None:
        return f"Unresolved ({cmpd['why']})"
    return 'agree' if cmpd['agree'] else 'DISAGREE'


def run_ladder(name, E, N, targets, expected, m15):
    case, slot, n0 = br.CASES[name]
    t0 = time.perf_counter()
    B = basis.Basis(slot, N)
    Fn = fn.Functional(B)
    K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
    u = br.seed_state(name, B)
    chk = br.orbit_checks(Fn, u, K)
    Qx = float(E['Q'])
    seed_ok = abs(chk['Q'] - Qx) / Qx < 1e-12 and chk['crit'] < 1e-12 and (chk['k'], chk['r']) == (E['k'], E['r'])
    say(f"{name} N = {N}, m = {B.m}: the seed {'PASS' if seed_ok else 'FAIL'}  Q(u) {chk['Q']:.15f} against {Qx:.15f},"
        f" criticality {chk['crit']:.1e}, (k, r_u) = ({chk['k']}, {chk['r']}); setup {time.perf_counter() - t0:.1f} s")
    fails = 0 if seed_ok else 1
    pts = {}
    c_prev, lam_prev, slope, acc_prev = np.sqrt(targets[0] / chk['Q']) * u, E['lam0'] + targets[0], 1 / chk['Q'], False
    for eps in targets:
        t1 = time.perf_counter()
        res = br.continue_to(Fn, E['lam0'], eps, c_prev, lam_prev, slope, K=K, prev_accepted=acc_prev)
        if not res['ok']:
            fails += 1
            say(f"   eps {eps:.4f}: FAIL  {res['reason']}; the ladder at N = {N} ends here")
            rec_json[f'N{N}_eps{eps}'] = dict(ok=False, reason=res['reason'], steps=res['steps'])
            break
        r, t_h, t_r = point_record(Fn, K, res['c'], res['lam'], expected)
        cmpd = compare(name, E, eps, r, res['eps'], m15)
        ok1 = abs(res['eps'] - eps) <= 1e-6 and all(s['accepted'] for s in res['steps'])
        fails += (not ok1) + (cmpd['agree'] is False)
        n_eval = sum(s['evaluations'] for s in res['steps'])
        secs = time.perf_counter() - t1
        pts[eps] = dict(c=res['c'], lam=res['lam'], m=res['m'], eps=res['eps'], slope=res['slope'], rec=summary(r),
                        cmp=cmpd, seconds=secs)
        rec_json[f'N{N}_eps{eps}'] = dict(ok=True, eps=res['eps'], lam=res['lam'], m=res['m'], steps=res['steps'],
                                          evaluations=n_eval, seconds=secs, seconds_hessian=t_h, seconds_record=t_r,
                                          record=summary(r), compare=cmpd)
        say(f"   eps {eps:8.4f}: {'accepted' if ok1 else 'NOT ACCEPTED'}, {n_eval} evaluations; V0"
            f" {'as expected' if r['v0_matches'] else 'MISMATCH'} (dim {r['sdim']}, ranks {r['jordan_ranks']}, leak"
            f" {r['symmetry_leak']:.1e}); {r['type']} ({r['nL']}, {r['nD']}, {r['K']}); M8.15 {cmpd['type15']} K"
            f" {cmpd['K15']} (nL {cmpd['nL15']}, nB {cmpd['nB15']}): {status(cmpd)}; slow vs M8.15 level 3"
            f" {cmpd['dev_vs_m815_l3'] if cmpd['dev_vs_m815_l3'] is None else format(cmpd['dev_vs_m815_l3'], '.1e')}"
            f" (M8.15 level 2 vs 3 {cmpd['m815_l2_vs_l3'] if cmpd['m815_l2_vs_l3'] is None else format(cmpd['m815_l2_vs_l3'], '.1e')});"
            f" unresolved {r['unresolved']}; {secs:.0f} s")
        c_prev, lam_prev, slope, acc_prev = res['c'], res['lam'], res['slope'], True
    return B, pts, fails


def change(a, b):
    if a['cmp']['slow'] is None or b['cmp']['slow'] is None:
        return None
    return max(abs(x - y) / abs(y) for x, y in zip(a['cmp']['slow'], b['cmp']['slow']))


def run_high(name, E, N_lo, B_lo, pts_lo, N_hi, tops, expected, m15):
    """N_hi at the given points, each seeded from N_lo's accepted point at the same eps, with UA's guard."""
    case, slot, n0 = br.CASES[name]
    t0 = time.perf_counter()
    B = basis.Basis(slot, N_hi)
    assert B.index[:B_lo.m] == B_lo.index, 'the lower basis is not the leading block'
    Fn = fn.Functional(B)
    K = fn.fibre_structure_matrix(Fn)[1] if slot == 'R2' else None
    say(f"{name} N = {N_hi}, m = {B.m}, seeded from N = {N_lo} at the top points: setup {time.perf_counter() - t0:.1f} s")
    fails, unresolved_identity, times = 0, [], []
    for eps in tops:
        if eps not in pts_lo:
            say(f"   eps {eps:.4f}: no N = {N_lo} point to seed from")
            fails += 1
            continue
        t1 = time.perf_counter()
        p = pts_lo[eps]
        c_seed = np.concatenate([p['c'], np.zeros(B.m - B_lo.m, dtype=complex)])
        cub = Fn.cubic(c_seed)
        res0 = np.linalg.norm((Fn.e - p['lam']) * c_seed + cub)
        size0 = np.linalg.norm(Fn.e * c_seed) + p['lam'] * np.linalg.norm(c_seed) + np.linalg.norm(cub)
        res = br.continue_to(Fn, E['lam0'], eps, c_seed, p['lam'], p['slope'], K=K, prev_accepted=False)
        if not res['ok']:
            fails += 1
            say(f"   eps {eps:.4f}: FAIL  {res['reason']}")
            continue
        Qb, _, _ = newton.tangent_borders(br.tangent_vectors(Fn, c_seed, K))
        dx = fn.to_real(res['c']) - fn.to_real(c_seed)
        d_al = float(np.linalg.norm(dx - Qb @ (Qb.T @ dx)) / np.linalg.norm(fn.to_real(c_seed)))
        r, t_h, t_r = point_record(Fn, K, res['c'], res['lam'], expected)
        cmpd = compare(name, E, eps, r, res['eps'], m15)
        lo = p['rec']
        same = ((r['type'], r['nL'], r['nD'], r['K'], sorted(g[2] for g in r['imag_groups'] if g[2] > 0), r['sdim'],
                 r['jordan_ranks']) == (lo['type'], lo['nL'], lo['nD'], lo['K'], lo['krein'], lo['sdim'], lo['ranks']))
        if ARM == 'guard_record':
            same = False
        identity = d_al <= (-1.0 if ARM in ('guard_distance', 'guard_unsafe') else GUARD) and same
        safe = ARM != 'guard_unsafe'
        if not identity:
            unresolved_identity.append(eps)
            if safe:
                # the fail-safe (UA): an ambiguous identity is never treated as one branch, so the comparison is Unresolved
                cmpd = dict(cmpd, resolved=False, agree=None, why='branch identity')
        ok1 = abs(res['eps'] - eps) <= 1e-6 and all(s['accepted'] for s in res['steps'])
        fails += (not ok1) + (cmpd['agree'] is False)
        hi = dict(rec=summary(r), cmp=cmpd)
        ch = change(p, hi) if identity or not safe else None
        n_eval = sum(s['evaluations'] for s in res['steps'])
        secs = time.perf_counter() - t1
        times.append(secs)
        rec_json[f'N{N_hi}_eps{eps}'] = dict(ok=True, eps=res['eps'], lam=res['lam'], m=res['m'], steps=res['steps'],
                                             evaluations=n_eval, seconds=secs, seconds_hessian=t_h, seconds_record=t_r,
                                             record=summary(r), compare=cmpd,
                                             guard=dict(embedding_residual=res0 / size0, aligned_distance=d_al,
                                                        norm_lo=p['m'], norm_hi=res['m'], omega_lo=float(np.sqrt(p['lam'])),
                                                        omega_hi=float(np.sqrt(res['lam'])), same_record=bool(same),
                                                        identity=bool(identity)),
                                             change_from_lo=ch)
        say(f"   eps {eps:8.4f}: {'accepted' if ok1 else 'NOT ACCEPTED'}, {n_eval} evaluations; guard: embedding"
            f" {res0 / size0:.1e}, aligned distance {d_al:.1e}, norms {p['m']:.12f} -> {res['m']:.12f}, omega"
            f" {np.sqrt(p['lam']):.12f} -> {np.sqrt(res['lam']):.12f}, record as at N = {N_lo}: {same} -> identity"
            f" {'kept' if identity else 'UNRESOLVED'}; {r['type']} ({r['nL']}, {r['nD']}, {r['K']}), M8.15 {cmpd['type15']}:"
            f" {status(cmpd)}; slow change {N_lo} -> {N_hi} per unit eps"
            f" {ch if ch is None else format(ch, '.1e')}; {secs:.0f} s")
    return fails, unresolved_identity, times


def main():
    global ARM
    args = sys.argv[1:]
    name = args[0]
    assert name in EXPECT
    trial = '--trial' in args
    if '--arm' in args:
        ARM = args[args.index('--arm') + 1]
        assert ARM in ARMS and trial, 'a mutation arm runs on the trial only'
    label = f"{name}{' (trial)' if trial else ''}{f', arm {ARM}' if ARM else ''}"
    case = br.CASES[name][0]
    devtools.require(case)
    E = EXPECT[name]
    rows, sha = br.expected_v0(ROOT)
    expected = rows[name]
    with open(os.path.join(ROOT, 'reference', 'm815', E['record']), encoding='utf-8') as f:
        m15 = json.load(f)
    full = ladder(0.25, E['eps_max'])
    targets = [e for e in full if e <= 2.0 + 1e-12] if trial else full
    lo_Ns, hi_N, tops = ([16], 24, targets[-2:]) if trial else ([24, 32], 40, full[-3:])
    say(f"D7 ladders, {label}: {len(targets)} ladder points to {targets[-1]}; N = {lo_Ns}, then"
        f" N = {hi_N} at {[round(t, 4) for t in tops]}; EXPECTED_V0.md SHA-256 {sha}, row {expected}")
    t_all = time.perf_counter()
    fails, ladders = 0, {}
    for N in lo_Ns:
        B, pts, f = run_ladder(name, E, N, targets, expected, m15)
        ladders[N] = (B, pts)
        fails += f
    exceed = []
    if len(lo_Ns) == 2:
        pa, pb = ladders[lo_Ns[0]][1], ladders[lo_Ns[1]][1]
        for eps in targets:
            if eps in pa and eps in pb:
                ch = change(pa[eps], pb[eps])
                rec_json.setdefault('changes', {})[str(eps)] = ch
                if ch is None or ch > FRACTION:
                    exceed.append((eps, ch))
        say(f"{name}: the slow eigenvalues' change per unit eps from N = {lo_Ns[0]} to {lo_Ns[1]}, against the fraction"
            f" {FRACTION:.0e}: {len(exceed)} of {len(targets)} points over it or unmatched"
            f" {[(round(e, 4), None if c is None else float(f'{c:.1e}')) for e, c in exceed]}")
    B_lo, pts_lo = ladders[lo_Ns[-1]]
    f, unres, times = run_high(name, E, lo_Ns[-1], B_lo, pts_lo, hi_N, tops, expected, m15)
    fails += f
    arm_ok = None
    if ARM:
        hp = [rec_json.get(f'N{hi_N}_eps{e}') for e in tops]
        unresolved_all = len(unres) == len(tops) and all(
            h is not None and h['ok'] and not h['guard']['identity'] and h['compare']['resolved'] is False
            and h['compare']['agree'] is None and h['change_from_lo'] is None for h in hp)
        expect = ARM != 'guard_unsafe'
        arm_ok = unresolved_all == expect
        say(f"{name}: arm {ARM}: the guard fired at {len(unres)} of {len(tops)} points; every comparison Unresolved, with no"
            f" agreement and no cross-N change: {unresolved_all}; expected {expect}"
            f"{'' if expect else ' (the fail-safe off: the check must fail)'}: {'PASS' if arm_ok else 'FAIL'}")
    extra = [e for e, _ in exceed if e not in tops]
    per = (sum(times) / len(times)) if times else float('nan')
    say(f"{name}: the pause. {len(extra)} points beyond the top three exceed the fraction or are unmatched"
        f" {[round(e, 4) for e in extra]}; at the measured {per / 60:.1f} min per N = {hi_N} point, about"
        f" {len(extra) * per / 60:.0f} min more. None runs before Blake authorizes it. Branch identity unresolved at"
        f" {unres or 'no point'}.")
    say(f"{name}: {fails} failed (claims 1 and 3); compute {(time.perf_counter() - t_all) / 60:.1f} min")
    tag = f"{name}{'_trial' if trial else ''}{f'_arm_{ARM}' if ARM else ''}"
    path = os.path.join(HERE, f'd7_ladders_{tag}.out')
    jpath = os.path.join(HERE, f'd7_ladders_{tag}.json')
    with open(path, 'w', encoding='utf-8') as f_:
        f_.write('\n'.join(out) + '\n')
    with open(jpath, 'w', encoding='utf-8') as f_:
        json.dump(rec_json, f_, indent=1, default=float)
    ok = not fails and arm_ok is not False
    devtools.log_run(os.path.abspath(__file__), case,
                     [f"D7's ladders, {label}: {'PASS' if ok else 'FAIL'}; {fails} failures of claims 1 and 3;"
                      + (f" the arm: the guard fired at {len(unres)} of {len(tops)} points; the comparisons"
                         f" {'Unresolved, as required' if ARM != 'guard_unsafe' else 'left typed, so the check fails, as required'}:"
                         f" {'PASS' if arm_ok else 'FAIL'}." if ARM else
                         f" {len(extra)} extra points held at the pause; branch identity unresolved at {unres or 'no point'}."),
                      f'EXPECTED_V0.md SHA-256 {sha} (as logged before any control ran), row {expected}.',
                      'Tolerances: fixed before the run (as in D7; the fraction 1e-6, provisional; the guard 1e-2, proposed).'
                      ' The run informed none.'], outputs=(path, jpath))
    if not ok:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
