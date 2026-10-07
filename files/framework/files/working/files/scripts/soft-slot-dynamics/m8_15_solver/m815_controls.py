"""M8.15 closing control runs (controls only; no target is touched). Each job writes a JSON record under out/.

  python3 m815_controls.py linear <level>      C1 at eps 6, C2a/C2b/C3 at eps 0.5, 1, 2: verdict data at that level
  python3 m815_controls.py theoremD <level>    C1's fast eigenvalues against Theorem D
  python3 m815_controls.py spreads             s2: the soft slots' level-2 spreads of the lowest level
  python3 m815_controls.py dynamics <case>     persistence test at level 2 (C1 at eps 6, others at eps 1)
  python3 m815_controls.py rate                C3's rate run, eta = 1e-7, same seeded direction
  python3 m815_controls.py summarize           floors, gates and schedule from the records -> out/freeze_numbers.json"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment: one thread, so sums are taken in a fixed order

import sys, os, json, time
import numpy as np
import scipy.sparse.linalg as spla
from m815_common import LevelCase, FROZEN_DIM, predicted, classify, match, schedule, kappa, ladder, EPS_MAX, RS
from linearize import Linearization
from verdict import Verdict
from nonlinear import to_complex
from standing import Standing, lowest_level

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(OUT, exist_ok=True)
CPOINTS = {'C1': [6.0], 'C2a': [0.5, 1.0, 2.0], 'C2b': [0.5, 1.0, 2.0], 'C3': [0.5, 1.0, 2.0]}


def cj(z):
    return [float(np.real(z)), float(np.imag(z))]


def save(name, obj):
    with open(os.path.join(OUT, name), 'w') as f:
        json.dump(obj, f, indent=1)


def tau_re(level):
    """The level's tau_Re = 10 r_f, from the closing record (bench defaults before one exists). The controls read it
    for the representatives only, which are the same for any margin between round-off and a resolved real part."""
    from m815_branch import frozen_numbers
    return 10 * float(frozen_numbers('C1')['r_f'][str(level)])


def verdict_record(lc, rec, eps_k):
    Phi, sigma = to_complex(rec['x']), rec['sigma']
    lin = Linearization(lc.st, Phi, sigma)
    v = Verdict(lc.st, lc.case, lin, Phi, sigma, lc.lam0_min, lc.rot, FROZEN_DIM[lc.name], rigid=lc.rigid,
                slices=lc.slices, tau_re=tau_re(lc.level))
    lv = v.vals[(v.cls == 'lifted') | (v.cls == 'rigid')]
    return v, dict(eps=eps_k, eps_reached=rec['eps'], sigma=sigma, m=rec['m'], newton_it=rec['it'], residual=rec['full'],
                   slice_force=[float(x) for x in rec['nu']],
                   dim=v.dim, frozen_dim=v.frozen_dim, basis_dim=v.basis_dim, closed=bool(v.closed),
                   omega_gram=float(v.omega_gram), lifted=[cj(l) for l in lv],
                   lifted_kind=[str(c) for c in v.cls[(v.cls == 'lifted') | (v.cls == 'rigid')]],
                   genuine=[[cj(l), float(k)] for l, k in v.genuine], nL=v.nL, nB_cluster=v.nB_cluster,
                   L_nearzero=[float(x) for x in v.L_nearzero], max_backward_error=float(v.bwe.max()),
                   slow_gap=[float(v.gap[0]), float(v.gap[1])], all_slow=[cj(l) for l in v.vals],
                   cls=[str(c) for c in v.cls])


def linear(level):
    out = {}
    for name, pts in CPOINTS.items():
        t0 = time.time()
        lc = LevelCase(level, name)
        recs = []
        start = 6.0 if name == 'C1' else 0.25
        targets = ladder(start, max(pts))

        def on_point(k, eps_k, rec):
            if any(abs(eps_k - p) < 1e-9 for p in pts):
                t1 = time.time()
                v, r = verdict_record(lc, rec, eps_k)
                r['seconds'] = time.time() - t1
                recs.append(r)
                print(f'  {name} level {level} eps {eps_k}: ' + ' | '.join(v.report(tau_re=0.0)[:1]), flush=True)
        br = lc.branch(targets, on_point)
        out[name] = dict(level=level, lam0=lc.lam0, lam0_min=lc.lam0_min, spread=lc.spread, Q=lc.Q, points=recs,
                         end=str(br.end[0]), setup_g0=[float(x) for x in lc.case.g0], H=[int(h) for h in lc.case.H],
                         fixed_dim=int(lc.case.Br.shape[1]), seconds=time.time() - t0)
        save(f'linear_L{level}.json', out)
    return out


def theoremD(level):
    """C1's fast eigenvalues against Theorem D: +-2iw twice and +-i sqrt(4w^2 + 2|v|^2), with the discrete w and |v|^2.
    For each predicted value: shift-invert at i mu, the nearest eigenvalues, and their eigenvectors' static parts on the
    lowest level (the fast spectrum is dense near these values, so identity is checked, not assumed)."""
    from standing import germ_seed
    from verdict import static_overlap, real_orthonormal
    from nonlinear import to_real
    lc = LevelCase(level, 'C1')
    hold = {}
    lc.branch([6.0], lambda k, e, r: hold.setdefault('rec', r))
    rec = hold['rec']
    Phi, sigma = to_complex(rec['x']), rec['sigma']
    lin = Linearization(lc.st, Phi, sigma)
    w = lin.omega
    v2 = 120 * rec['m'] / lc.vol
    law = abs((sigma - lc.lam0) - v2) / sigma
    from m815_common import G as G2I
    E0 = real_orthonormal(np.column_stack([to_real(germ_seed(lc.mesh, lc.case.R, 2, c * np.eye(3)[k], G2I))
                                           for k in range(3) for c in (1, 1j)]), lc.st.Mr)
    A, B = lin.Abig.astype(complex), lin.Bbig.astype(complex)
    checks = []
    for mu, mult in ((2 * w, 2), (np.sqrt(4 * w * w + 2 * v2), 1)):
        shift = 1j * mu * (1 + 1e-7)
        op = lin.shift_invert(shift)
        from nonlinear import arpack_v0
        vals, vecs = spla.eigs(A, k=6, M=B, sigma=shift, OPinv=op, which='LM', v0=arpack_v0(A.shape[0], complex))
        del op
        import gc
        gc.collect()          # scipy's ARPACK wrapper holds the operator, and so the factorization, in a reference cycle
        order = np.argsort(abs(vals - 1j * mu))
        near = []
        for i in order:
            rel = abs(vals[i] - 1j * mu) / mu
            ov = static_overlap(vecs[:, i], E0, lc.st.Mr, lin.n2)
            near.append(dict(lam=cj(vals[i]), rel=float(rel), lowest_level_overlap=float(ov)))
        good = [x for x in near if x['rel'] <= 1e-6 and x['lowest_level_overlap'] >= 0.9]
        checks.append(dict(mu=float(mu), multiplicity=mult, found=len(good), nearest=near[:4],
                           ok=len(good) >= mult))
        print(f'  mu {mu:.10f} (x{mult}): {len(good)} within 1e-6 on the lowest level; nearest {near[0]}', flush=True)
    ok = law <= 1e-6 and all(c['ok'] for c in checks)
    worst = max(min((x['rel'] for x in c['nearest'] if x['lowest_level_overlap'] >= 0.9), default=np.inf) for c in checks)
    out = dict(level=level, sigma=sigma, lam0=lc.lam0, v2=v2, frequency_law_rel=law, checks=checks,
               theoremD_rel=float(worst), ok=bool(ok))
    save(f'theoremD_L{level}.json', out)
    print(json.dumps(dict(law=law, theoremD_rel=worst, ok=ok), indent=1))


def spreads():
    from fem import Mesh
    mesh = Mesh(2, nq=3)
    out = {}
    for slot, n0 in ((4, 7), (5, 7), (2, 8)):
        st = Standing(mesh, RS[slot])
        lam = lowest_level(st, n0)
        out[f'R{slot}'] = dict(spread=float(lam.max() - lam.min()), mean=float(lam.mean()), omega0=float(np.sqrt(lam.mean())))
    save('spreads_L2.json', out)
    print(json.dumps(out, indent=1))


def dynamics(name, eta=1e-3, T=1000.0, tag=None, mode='split'):
    from persistence import run_test
    lc = LevelCase(2, name)
    eps = 6.0 if name == 'C1' else 1.0
    hold = {}
    lc.branch(ladder(6.0 if name == 'C1' else 0.25, eps), lambda k, e, r: hold.__setitem__('rec', r) if abs(e - eps) < 1e-9 else None)
    rec = hold['rec']
    Phi, sigma = to_complex(rec['x']), rec['sigma']
    lin = Linearization(lc.st, Phi, sigma)
    v = Verdict(lc.st, lc.case, lin, Phi, sigma, lc.lam0_min, lc.rot, FROZEN_DIM[name], rigid=lc.rigid,
                tau_re=tau_re(2))
    lifted = v.vals[(v.cls == 'lifted') | (v.cls == 'rigid')]
    t0 = time.time()
    res = run_test(lc.st, Phi, sigma, v.ps, v.G, lc.rot, lc.case, lifted, eta=eta, T=T, log=lambda s: print(s, flush=True),
                   progress=100, S=v.slow_basis(), mode=mode)
    recarr = res.pop('rec', None)
    res['seconds'] = time.time() - t0
    res['level2_rates'] = [cj(l) for l, _ in v.genuine]
    res['cluster_dim'] = v.dim
    res['eps'] = eps
    tag = (tag or name) + ('' if mode == 'split' else f'_{mode}')
    save(f'dynamics_{tag}.json', res)
    if recarr is not None:
        np.save(os.path.join(OUT, f'dynamics_{tag}.npy'), recarr)
    print(json.dumps({k: v for k, v in res.items()}, indent=1, default=str))


# --- the summary: floors, gates, schedule -------------------------------------------------------------------------
def load(name):
    p = os.path.join(OUT, name)
    return json.load(open(p)) if os.path.exists(p) else None


def C(z):
    return complex(z[0], z[1])


def summarize():
    from m815_common import SPECTRA, QEXACT, LAM0, predicted, schedule as sched, ladder
    rep = []
    lin = {h: load(f'linear_L{h}.json') for h in (2, 3)}
    spreads = load('spreads_L2.json')
    # floors: the paired lifted modes of C1, C2a, C2b
    rf = {}
    for h in (2, 3):
        if lin[h] is None:
            continue
        mods = [abs(C(z)) for nm in ('C1', 'C2a', 'C2b') for p in lin[h][nm]['points'] for z in p['lifted']]
        rf[h] = max(mods)
    tau0 = {h: 10 * rf[h] for h in rf}
    rep.append(f'floors: r_f(3) {rf.get(3)}, r_f(2) {rf.get(2)}; tau0 = tau_Re = 10 r_f')
    # cluster gate
    gate_cluster = True
    for h in rf:
        for nm, rec in lin[h].items():
            for p in rec['points']:
                ok = p['dim'] == p['frozen_dim'] and p['closed'] and p['omega_gram'] >= 1e-6
                lm = [abs(C(z)) for z in p['lifted']]
                if nm == 'C3':
                    slot = 4
                    bound = 0.5 * max(abs(l) for l, _ in predicted('C3', slot, p['eps']))
                    ok = ok and all(x < bound for x in lm)
                else:
                    ok = ok and all(x <= tau0[h] for x in lm)
                gate_cluster &= ok
                if not ok:
                    rep.append(f'  CLUSTER GATE FAILS: {nm} level {h} eps {p["eps"]}')
    rep.append(f'cluster gate (C1 to C3, levels 2 and 3): {"pass" if gate_cluster else "FAIL"}')
    # linear gates at level 3
    gate_lin = True
    if 3 in lin and lin[3]:
        for nm, slot in (('C2a', 4), ('C2b', 2), ('C3', 4)):
            ratios = {}
            for p in lin[3][nm]['points']:
                comp = [C(z) for z, k in p['genuine']]
                pred = [l for l, _ in predicted(nm, slot, p['eps'])]
                A = [(abs(c), 'x') for c in comp]
                B = [(abs(q), 'x') for q in pred]
                pairs = match(A, B)
                if pairs is None:
                    gate_lin = False
                    rep.append(f'  LINEAR GATE: {nm} eps {p["eps"]}: {len(comp)} computed vs {len(pred)} predicted modes')
                    continue
                ratios[p['eps']] = sorted(a / b for a, b, _ in pairs)
            r05 = ratios.get(0.5, [])
            ok5 = all(abs(r - 1) < 0.05 for r in r05)
            mono = all(abs(ratios[0.5][i] - 1) < abs(ratios[1.0][i] - 1) < abs(ratios[2.0][i] - 1)
                       for i in range(len(r05))) if all(e in ratios for e in (0.5, 1.0, 2.0)) else False
            gate_lin &= ok5 and mono
            rep.append(f'  {nm}: ratios at 0.5 {np.round(r05, 4).tolist()}, at 1 {np.round(ratios.get(1.0, []), 4).tolist()}, '
                       f'at 2 {np.round(ratios.get(2.0, []), 4).tolist()}; within 5% at 0.5: {ok5}; monotone: {mono}')
    tD = load('theoremD_L3.json')
    if tD:
        okD = tD['frequency_law_rel'] <= 1e-6 and tD['theoremD_rel'] <= 1e-6
        gate_lin &= okD
        rep.append(f'  C1: frequency law {tD["frequency_law_rel"]:.1e}, Theorem D {tD["theoremD_rel"]:.1e}: {"pass" if okD else "FAIL"}')
    else:
        rep.append('  C1 Theorem D: not yet run')
        gate_lin = False
    rep.append(f'linear gates (level 3): {"pass" if gate_lin else "FAIL or incomplete"}')
    # level-stability calibration from C3
    d3 = None
    if lin[2] and lin[3]:
        diffs = []
        for p2, p3 in zip(lin[2]['C3']['points'], lin[3]['C3']['points']):
            r2 = np.mean([abs(C(z)) for z, k in p2['genuine']])
            r3 = np.mean([abs(C(z)) for z, k in p3['genuine']])
            diffs.append(abs(r2 - r3) / r3)
        d3 = max(diffs)
        dlev = max(1e-2, 2 * d3)
        rep.append(f'level stability: d3 {d3:.2e}, delta_lev {dlev:.2e} ({"freezes" if dlev <= 5e-2 else "DOES NOT FREEZE"})')
    # dynamics: every record re-read through the first-event evaluation (v7)
    from persistence import evaluate
    gate_dyn = True
    want = {'C1': 'Persists', 'C2a': 'Persists', 'C2b': 'Persists', 'C3': 'Fails'}
    dynsum = {}
    for nm, verdict_wanted in want.items():
        d = load(f'dynamics_{nm}.json')
        if d is None or not os.path.exists(os.path.join(OUT, f'dynamics_{nm}.npy')):
            rep.append(f'  dynamics {nm}: not yet run')
            gate_dyn = False
            continue
        rec = np.load(os.path.join(OUT, f'dynamics_{nm}.npy'))
        Eref = rec[0, 6] * (1 - d['energy_pert'])
        ev = evaluate(rec, 1e-3, Eref)
        ok = ev['verdict'] == verdict_wanted and ev['valid']
        gate_dyn &= ok
        dynsum[nm] = dict(ev, dt=d['dt'], r=d['r'], direction=d.get('direction'))
        rep.append(f'  dynamics {nm}: {ev["verdict"]} (wanted {verdict_wanted}): {"pass" if ok else "FAIL"}; max d_perp {ev["max_dperp"]:.3e}, '
                   f'd_rot max {ev["max_drot"]:.2e}, reference {ev["max_dref"]:.1e}, charge {ev["charge_drift"]:.1e}, '
                   f'energy oscillation {ev["energy_dev_vs_pert"]:.3f} and drift {ev["energy_secular_drift"]:.1e} of E_eta '
                   f'(read until t = {ev["read_until"]:.0f}); t_fail {ev["t_fail"]}, d_rot at fail {ev["drot_at_fail"]}')
    rr = load('dynamics_C3_rate.json')
    if rr is not None and os.path.exists(os.path.join(OUT, 'dynamics_C3_rate.npy')):
        rec = np.load(os.path.join(OUT, 'dynamics_C3_rate.npy'))
        t, dp = rec[:, 0], rec[:, 2]
        eta7 = 1e-7
        sel = (dp >= 10 * eta7) & (dp <= 1e4 * eta7)
        rate = np.polyfit(t[sel], np.log(dp[sel]), 1)[0]
        lin2 = max(abs(C(z)) for z in rr['level2_rates'])
        okr = abs(rate / lin2 - 1) <= 0.05
        gate_dyn &= okr
        dynsum['C3_rate'] = dict(fitted=float(rate), linear_L2=float(lin2), window=[float(t[sel].min()), float(t[sel].max())],
                                 points=int(sel.sum()))
        rep.append(f'  C3 rate: fitted {rate:.6f} on t in [{t[sel].min():.0f}, {t[sel].max():.0f}] ({sel.sum()} points) against the level-2 '
                   f'linear {lin2:.6f}: ratio {rate / lin2:.5f}: {"pass" if okr else "FAIL"}')
    else:
        gate_dyn = False
    rep.append(f'dynamic gates (level 2): {"pass" if gate_dyn else "FAIL or incomplete"}')
    # schedule
    out = dict(r_f={str(k): v for k, v in rf.items()}, tau0={str(k): v for k, v in tau0.items()},
               s2={k: v['spread'] for k, v in spreads.items()} if spreads else None, d3=d3,
               delta_lev=(max(1e-2, 2 * d3) if d3 is not None else None),
               eta=1e-3, eta_ref=1e-3, T=1000.0, dynamics=dynsum if 'dynsum' in dir() else None,
               dt=load('dt_L2.json'), gates=dict(cluster=bool(gate_cluster), linear=bool(gate_lin),
                                                dynamic=bool(gate_dyn)))
    if 3 in rf:
        sch = {}
        for nm, slot in (('T1', 4), ('T1', 5), ('T2', 4), ('T2', 5), ('T3', 4), ('T3', 5), ('T4', 4), ('T4', 5), ('T5', 2)):
            tg = ladder(0.25, EPS_MAX[slot])
            s = sched(nm, slot, rf[3], tg)
            sch[f'{nm}/R{slot}'] = s
            late = [(round(x['tau'], 6), x['first_resolved']) for x in s if x['first_resolved'] != 0.25]
            if late:
                rep.append(f'  schedule {nm}/R{slot}: modes resolved after 0.25: {late}')
        out['schedule'] = sch
    save('freeze_numbers.json', out)
    print('\n'.join(rep))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'linear':
        linear(int(sys.argv[2]))
    elif cmd == 'theoremD':
        theoremD(int(sys.argv[2]))
    elif cmd == 'spreads':
        spreads()
    elif cmd == 'dynamics':
        dynamics(sys.argv[2], mode=(sys.argv[3] if len(sys.argv) > 3 else 'split'))
    elif cmd == 'rate':
        dynamics('C3', eta=1e-7, tag='C3_rate', mode=(sys.argv[2] if len(sys.argv) > 2 else 'split'))
    elif cmd == 'summarize':
        summarize()
    else:
        raise SystemExit(__doc__)
