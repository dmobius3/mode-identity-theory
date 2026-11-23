"""Development: the member path on the rigid families in R1 and R3 at points the terms leave unregistered, ||phi||^2 =
0.5 and 2, never 1 (DEVLOG entry 1; #512, 19812666, section 2). Each point's member is the exact branch on E0; its
linear record is the instrument's own, and in R3 it is held to M8.16.1's stored record of C1 at the same amplitude and
cutoff, with no evolution of anything M8.16.1 registered. The +/- delta pairs run under the splitting with the FFT cubic,
on E0, and the read holds the two distinct frequencies of Theorem 3.7 on E0, 2 omega n times and (4 omega^2 + 2 kappa)^(1/2),
with their Krein signs. Development seeds only. Its readings are known outcomes for the terms.

Usage: python3 -I -B -u dev_rigid.py OUT_JSON [--smoke]"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import member as mb  # noqa: E402
import readcore as rc  # noqa: E402
import loader as ld  # noqa: E402
from instrument import branches as br, functional as fn  # noqa: E402

SEED = 7300202
OUT = sys.argv[1]
SMOKE = '--smoke' in sys.argv
T = 10.0 if SMOKE else 30.0
LADDER = (1,) if SMOKE else (1, 2, 4, 8, 16, 32)


def stored_c1(N, eps):
    """M8.16.1's stored record of C1 at (N, eps), every group, from its pinned file."""
    rel = 'run/out/C1.json'
    path = os.path.join(ld.M8161, rel)
    assert ld._sha(path) == ld.PINS[rel]
    with open(path, encoding='utf-8') as f:
        j = json.load(f)
    pts = j['cutoffs'][str(N)]['points']
    key = next(k for k in pts if abs(float(k) - eps) < 1e-9)
    return [dict(c=complex(*g['c']), cls=g['cls'], size=g['size'], neg=g['neg']) for g in pts[key]['groups']]


def point(slot, kappa, N, rng, log):
    S = mb.Slot(slot, N)
    if slot == 'R3':
        v = br.seed_state('C1', S.B)
    else:
        v = np.zeros(S.B.m, complex)
        v[S.low] = rng.normal(size=int(S.low.sum())) + 1j * rng.normal(size=int(S.low.sum()))
        v /= np.linalg.norm(v)
    c0, lam = np.sqrt(kappa) * v, S.lam0 + kappa
    resid = np.linalg.norm((S.e - lam) * c0 + S.X.cubic(c0)) / (lam * np.linalg.norm(c0))
    rec = mb.linear_record(S, c0, lam, tangents_K=S.K)
    r = rec['r']
    w = np.sqrt(lam)
    n = int(S.low.sum()) - 1
    exact = [complex(0, 2 * w), complex(0, np.sqrt(4 * w ** 2 + 2 * kappa))]
    # the record's E0 groups: its eigenvectors' zeta part on the lowest level
    m = S.B.m
    lowmask = np.concatenate([S.low, S.low])
    e0 = []
    for g in r['groups']:
        if g['cls'] != 'imag':
            continue
        Vg = r['V'][:2 * m, g['idx']]
        frac = np.linalg.norm(Vg[lowmask]) / np.linalg.norm(Vg)
        if frac > 1 - 1e-8:
            e0.append(g)
    targets = []
    for z, size in zip(exact, (n, 1)):
        g = min(e0, key=lambda g: abs(g['centre'] - z))
        targets.append(dict(c=z, cls='imag', size=size, idx=list(g['idx']), neg=g['neg'], rec_centre=complex(g['centre']),
                            rec_size=len(g['idx'])))
    rec_ok = all(t['rec_size'] == t['size'] and abs(t['rec_centre'] - t['c']) / abs(t['c']) < 1e-10 for t in targets)
    held = None
    if slot == 'R3':
        st = stored_c1(N, kappa)
        mine = sorted(((complex(g['centre']), len(g['idx']), g['neg']) for g in r['groups']), key=lambda x: (round(x[0].imag, 6), round(x[0].real, 6)))
        theirs = sorted(((g['c'], g['size'], g['neg']) for g in st), key=lambda x: (round(x[0].imag, 6), round(x[0].real, 6)))
        held = len(mine) == len(theirs) and all(abs(a[0] - b[0]) <= 1e-10 * max(1.0, abs(b[0])) and a[1] == b[1] and a[2] == b[2] for a, b in zip(mine, theirs))
    P = mb.omega_complement(rec)
    idx = [j for t in targets for j in t['idx']]
    k = max(t['size'] for t in targets)
    dirs = mb.directions(S, rec, c0, lam, idx, k, rng, lowest_only=True)
    H0 = S.D.energy(c0, 1j * w * c0) * (1 + 1e-6)
    h0, cbar, wbar = mb.step5(S, H0)
    radius = 1.5 * abs(exact[1])
    reads = []
    for f in LADDER:
        h = h0 / f
        nsteps = int(np.ceil(T / h0)) * f
        t0 = time.perf_counter()
        runs, scale = mb.pair_runs(S, c0, lam, dirs, h, nsteps, f, cbar)
        trajs, rot = mb.to_frame(runs, scale, c0, lam, h0, P)
        try:
            fit, centres, members, fl = mb.read(trajs, h0, targets, radius)
            err = [abs(cz - t['c']) / abs(t['c']) for cz, t in zip(centres, targets)]
            signs = [rc.krein(rec['B'], fit, members[i]) for i in range(len(targets))]
            row = dict(f=f, h=h, hw=h * wbar, centres=[[c.real, c.imag] for c in centres], rel_err=err, floor=fl, rank=fit.rank,
                       krein=[[int(s), bool(d)] for s, d in signs], rotation=rot, seconds=time.perf_counter() - t0)
        except rc.Admission as e:
            row = dict(f=f, h=h, hw=h * wbar, admission=str(e), seconds=time.perf_counter() - t0)
        reads.append(row)
        log(f'  {slot} kappa {kappa} N {N} h0/{f}: ' + (f"errors {', '.join(f'{x:.2e}' for x in row['rel_err'])}; "
                                                       f"floor/b {max(fv / (1e-3 * abs(t['c'])) for fv, t in zip(row['floor'], targets)):.1e}; "
                                                       f"Krein {row['krein']}" if 'rel_err' in row else row['admission']) + f'; {row["seconds"]:.0f} s')
    out = dict(slot=slot, kappa=kappa, N=N, m=S.B.m, n=n, lam=lam, residual=float(resid), record_E0_ok=bool(rec_ok), held_to_C1=held,
               targets=[dict(c=[t['c'].real, t['c'].imag], size=t['size'], neg=t['neg']) for t in targets], h0=h0, cbar=cbar, wbar=wbar,
               k=k, T=T, reads=reads)
    if len(LADDER) == 6 and all('rel_err' in x for x in reads):
        lam_g = [[complex(*x['centres'][i]) for x in reads] for i in range(len(targets))]
        out['ratios'] = [rc.successive_ratio(lg[3], lg[4], lg[5])[0] for lg in lam_g]
    return out, (S, c0, lam, rec, P, dirs, targets, h0, cbar, radius)


def arms(ctx, log):
    """The registered run's arms, on a development point: the kick with a wrong factor, the broken pair, the flipped form."""
    S, c0, lam, rec, P, dirs, targets, h0, cbar, radius = ctx
    nsteps = int(np.ceil(T / h0))
    runs, scale = mb.pair_runs(S, c0, lam, dirs, h0, nsteps, 1, cbar)
    trajs, _ = mb.to_frame(runs, scale, c0, lam, h0, P)
    fit, centres, members, _ = mb.read(trajs, h0, targets, radius)
    e0 = [abs(cz - t['c']) for cz, t in zip(centres, targets)]
    res = {}
    half = lambda c: 0.5 * S.X.cubic(c)
    runs_k, scale_k = mb.pair_runs(S, c0, lam, dirs, h0, nsteps, 1, cbar, kick=half)
    trajs_k, _ = mb.to_frame(runs_k, scale_k, c0, lam, h0, P)
    try:
        _, ck, _, _ = mb.read(trajs_k, h0, targets, radius)
        res['kick'] = any(abs(a - t['c']) > 1e-3 * abs(t['c']) + 2 * e for a, t, e in zip(ck, targets, e0))
    except rc.Admission:
        res['kick'] = True
    trajs_b, _ = mb.to_frame(runs, scale, c0, lam, h0, P, broken=True)
    try:
        _, cb, _, _ = mb.read(trajs_b, h0, targets, radius)
        res['broken_pair'] = any(abs(a - t['c']) > 1e-3 * abs(t['c']) + 2 * e for a, t, e in zip(cb, targets, e0))
    except rc.Admission:
        res['broken_pair'] = True
    want = [rc.krein(rec['B'], fit, members[i])[0] for i in range(len(targets))]
    got = [rc.krein(-rec['B'], fit, members[i])[0] for i in range(len(targets))]
    res['flipped_form'] = all(a != b for a, b in zip(want, got))
    log(f'  arms: {res}')
    return res


def main():
    rng = np.random.default_rng(SEED)
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)
    log(f'dev_rigid: seed {SEED}; T {T}; ladder {LADDER}; numpy {np.__version__}')
    pts = [('R3', 0.5, 16)] if SMOKE else [(s, k, N) for s in ('R1', 'R3') for k in (0.5, 2.0) for N in (16, 24)]
    results, ctx0 = [], None
    for slot, kappa, N in pts:
        global LADDER
        lad = LADDER
        if N == 24 and not SMOKE:
            LADDER = (1,)
        res, ctx = point(slot, kappa, N, rng, log)
        LADDER = lad
        results.append(res)
        log(f'{slot} kappa {kappa} N {N}: m {res["m"]}, n {res["n"]}, residual {res["residual"]:.1e}, record E0 {res["record_E0_ok"]}, '
            f'held to C1 {res["held_to_C1"]}, ratios {res.get("ratios")}')
        if ctx0 is None and N == 16:
            ctx0 = ctx
    arm = arms(ctx0, log)
    with open(OUT, 'x', encoding='utf-8') as f:
        json.dump(dict(seed=SEED, T=T, points=results, arms=arm, log=lines), f, indent=1)


if __name__ == '__main__':
    main()
