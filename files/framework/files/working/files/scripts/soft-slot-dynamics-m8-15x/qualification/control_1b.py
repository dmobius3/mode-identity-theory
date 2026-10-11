"""M8.15.x control 1b (REGISTER_1.md, amendment of 2026-10-08T22:09:19Z): the angle solve on the pyramid's circle.

The pyramid P5 in R4 at level 2, at the norm of Branch.first's seed solve at eps_min, with theta_start = pi/10:
  solve:   the frozen rule over one period (the selection) and over two (the symmetry rule), bench solver;
  frozen:  the solver at 6058f95 from the seed at the selected angle (P5b, added to its CASES at run time), traced;
  ref:     the reference run at the selected point over T = 1000 (registered), and the same run at 1a's off-critical
           point, stopped once d_ref passes 0.1 (unregistered diagnostic), side by side in two processes;
  then the registered checks and their mutation arms.

  python3 control_1b.py      # writes control_1b.json, control_1b.log and control_1b_ref_*.npy"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, subprocess, time, datetime, copy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import control_1a as c1

EPS_MIN, LEVEL, SLOT, T, ETA = 0.25, 2, 4, 1000.0, 1e-3
THETA_START = 3.141592653589793 / 10
WORK = os.path.join(HERE, 'control_1b_work')


def bench():
    sys.path.insert(0, os.path.join(c1.BENCH, 'm8_15_solver'))


def stage_solve():
    bench()
    import numpy as np
    from m815_common import LevelCase
    from angle import angle_solve
    lc = LevelCase(LEVEL, 'P5', SLOT)
    m0 = EPS_MIN / (lc.Q / lc.vol) / 120                 # Branch.first's seed norm
    sigma0 = lc.lam0 + EPS_MIN
    t0 = time.time()
    A, PhiA, C = angle_solve(lc, m0, sigma0, theta_start=THETA_START, n_periods=1)
    tA = time.time() - t0
    B, _, _ = angle_solve(lc, m0, sigma0, theta_start=THETA_START, n_periods=2)
    off = C.solve(-THETA_START, m0, sigma0)              # 1a's point, D(-pi/10) u, up to a global phase
    os.makedirs(WORK, exist_ok=True)
    np.save(os.path.join(WORK, 'Phi_sel.npy'), PhiA)
    np.save(os.path.join(WORK, 'Phi_off.npy'), off['Phi'])
    rep = C.rep(A['selected']['theta'])
    out = dict(one_period=A, two_periods=B, seconds_one_period=round(tA, 1),
               off=dict({k: v for k, v in off.items() if k != 'Phi'}),
               rep_selected={str(k - 3): [float(rep[k].real), float(rep[k].imag)] for k in range(7)})   # index k is m = k - 3
    with open(os.path.join(WORK, 'solve.json'), 'w') as f:
        json.dump(out, f, indent=1, default=float)


def stage_frozen():
    sys.path.insert(0, os.path.join(c1.FROZEN, 'm8_15_solver'))
    import inspect
    import numpy as np
    import pinned
    with open(os.path.join(WORK, 'solve.json')) as f:
        rep = json.load(f)['rep_selected']
    assert 'P5b' not in pinned.CASES
    # Condon-Shortley components by m (cs_vector reads m + j/2): the representative at the selected angle
    pinned.CASES['P5b'] = dict(slot=4, j2=6, u={int(m): complex(re, im) for m, (re, im) in rep.items()}, gens=[('z', 5)],
                               slice_axis='z')
    from m815_common import LevelCase
    from continuation import Branch
    lc = LevelCase(LEVEL, 'P5b', SLOT)
    code = pinned.solve_pinned.__code__
    lines, start = inspect.getsourcelines(pinned.solve_pinned)
    hits = [start + i for i, ln in enumerate(lines) if ln.strip() == 'if res < tol:']
    assert len(hits) == 1
    its = []

    def local(frame, event, arg):
        if event == 'line' and frame.f_lineno == hits[0]:
            L = frame.f_locals
            its.append(dict(it=int(L['it']), res=float(L['res']), sigma=float(L['sigma']), mu=float(L['mu'][0]),
                            nu=float(L['nu'][0])))
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is code else None

    br = Branch(lc.st, lc.case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=lambda s: None)
    sys.settrace(glob)
    try:
        ok = br.first(EPS_MIN)
    finally:
        sys.settrace(None)
    with open(os.path.join(WORK, 'frozen.json'), 'w') as f:
        json.dump(dict(ok=bool(ok), end=br.end, iterations=its, orientation=lc.case.orientation_report()), f, indent=1,
                  default=str)


def stage_ref(which):
    """The reference e^{i n theta} Phi run alone, with run_test's step, phase, alignment and observation cadence."""
    bench()
    import numpy as np
    from m815_common import LevelCase
    from integrate import Verlet, omega_max
    from persistence import Aligner
    from nonlinear import to_real
    with open(os.path.join(WORK, 'solve.json')) as f:
        S = json.load(f)
    sigma = S['one_period']['selected']['sigma'] if which == 'sel' else S['off']['sigma']
    Phi = np.load(os.path.join(WORK, f'Phi_{which}.npy'))
    lc = LevelCase(LEVEL, 'P5', SLOT)
    st, Mr = lc.st, lc.st.Mr
    V = Verlet(st)
    dt = 0.8 * 2 / omega_max(st)
    theta = 2 * np.arcsin(dt * np.sqrt(sigma) / 2)
    c0 = (np.exp(1j * theta) - 1 + 0.5 * dt ** 2 * sigma) / dt
    al = Aligner(Phi, st.M, lc.case.quaternionic)
    nP = np.sqrt(np.real(np.vdot(Phi, st.M @ Phi)))
    every = max(1, int(round(1.0 / dt)))
    nsteps = int(round(T / dt))
    stop = None if which == 'sel' else 100 * ETA

    def observe(t, P2, Q2):
        ph = (t / dt) * theta
        rp, _ = al.apply(P2, Q2, ph)
        rr = to_real(rp - Phi)
        return (t, np.sqrt(abs(rr @ (Mr @ rr))) / nP, V.charge(P2, Q2), V.energy(P2, Q2))

    P2, Q2 = Phi.copy(), c0 * Phi
    a2 = V.accel(P2)
    rec = [observe(0.0, P2, Q2)]
    t0 = time.time()
    done = 0
    for s in range(1, nsteps + 1):
        Q2 = Q2 + 0.5 * dt * a2; P2 = P2 + dt * Q2; a2 = V.accel(P2); Q2 = Q2 + 0.5 * dt * a2
        done = s
        if s % every == 0:
            rec.append(observe(s * dt, P2, Q2))
            if stop is not None and rec[-1][1] > stop:
                break
    rec = np.array(rec)
    np.save(os.path.join(HERE, f'control_1b_ref_{which}.npy'), rec)
    with open(os.path.join(WORK, f'ref_{which}.json'), 'w') as f:
        json.dump(dict(dt=dt, every=every, nsteps=nsteps, steps_done=done, T_int=nsteps * dt, last_t=float(rec[-1, 0]),
                       max_dref=float(rec[:, 1].max()), seconds=round(time.time() - t0, 1),
                       charge_drift=float(abs(rec[:, 2] - rec[0, 2]).max() / abs(rec[0, 2])),
                       t_first_above_eta=(float(rec[np.argmax(rec[:, 1] > ETA), 0]) if (rec[:, 1] > ETA).any() else None),
                       stopped_early=bool(stop is not None and rec[-1, 1] > stop)), f, indent=1)


def sym_dist(th):
    P, h = 2 * 3.141592653589793 / 5, 3.141592653589793 / 5
    return min(abs(((th - c) + P / 2) % P - P / 2) for c in (0.0, h))


def nearest_sym(th):
    P, h = 2 * 3.141592653589793 / 5, 3.141592653589793 / 5
    return min((abs(((th - c) + P / 2) % P - P / 2), c) for c in (0.0, h))[1]


def evaluate(R):
    """The registered checks on the record R (one_period, two_periods, frozen, bench_res, ref_sel)."""
    A, B, F = R['one_period'], R['two_periods'], R['frozen']
    sel = A['selected']
    roots = [r for r in A['roots'] if r['resolved']]
    other = [r for r in roots if sel is not None and nearest_sym(r['theta']) != nearest_sym(sel['theta'])]
    ok4 = (sel is not None and sym_dist(sel['theta']) <= 1e-7 and len(other) >= 1
           and all(sel['H'] < r['H'] for r in other))
    bmins = B['minima']
    return [
        ('1. every root within 1e-7 of 0 or pi/5, modulo 2 pi/5',
         len(roots) > 0 and len(roots) == len(A['roots']) and all(sym_dist(r['theta']) <= 1e-7 for r in roots)),
        ('2. at the selected minimum, |nu| <= 1e-12 and |mu| <= 1e-12',
         sel is not None and abs(sel['nu']) <= 1e-12 and abs(sel['mu']) <= 1e-12),
        ('3. the frozen solver passes its own test there, and the bench passes the new one',
         F['ok'] and F['iterations'][-1]['res'] < 1e-11 and sel is not None and sel['res'] < 1e-11),
        ('4. the selection is the lower-energy of the two symmetric angles', ok4),
        ('5. over two periods the selected minimum is found twice and counted once',
         len(bmins) == 2 and B['n_classes'] == 1 and B['selected'] is not None
         and nearest_sym(B['selected']['theta']) == nearest_sym(sel['theta'])),
        ('6. the reference run at the selected point holds d_ref <= 1e-3 over T = 1000',
         R['ref_sel']['max_dref'] <= ETA and R['ref_sel']['steps_done'] == R['ref_sel']['nsteps']),
    ]


def mutations(R):
    def m_root(r):
        r['one_period']['roots'][0]['theta'] += 2e-7
    def m_nu(r):
        r['one_period']['selected']['nu'] = 2e-12
    def m_mu(r):
        r['one_period']['selected']['mu'] = -2e-12
    def m_frozen(r):
        r['frozen']['ok'] = False
    def m_bench(r):
        r['one_period']['selected']['res'] = 2e-11
    def m_swapH(r):
        s = r['one_period']['selected']
        o = [x for x in r['one_period']['roots'] if nearest_sym(x['theta']) != nearest_sym(s['theta'])][0]
        s['H'], o['H'] = o['H'] + 1e-12, s['H']
    def m_classes(r):
        r['two_periods']['n_classes'] = 2
    def m_ref(r):
        r['ref_sel']['max_dref'] = 1.1e-3
    def m_short(r):
        r['ref_sel']['steps_done'] = r['ref_sel']['nsteps'] - 1
    arms = [(0, 'a root moved by 2e-7', m_root), (1, 'nu at 2e-12', m_nu), (1, 'mu at -2e-12', m_mu),
            (2, 'the frozen solve fails', m_frozen), (2, 'the bench test ends at 2e-11', m_bench),
            (3, 'the energies of the two symmetric points swapped', m_swapH),
            (4, 'the two copies counted as two classes', m_classes), (5, 'd_ref reaches 1.1e-3', m_ref),
            (5, 'the reference run stops one step short', m_short)]
    parent = [ok for _, ok in evaluate(R)]
    out = []
    for k, label, f in arms:
        r = copy.deepcopy(R)
        f(r)
        got = [ok for _, ok in evaluate(r)]
        out.append(dict(check=k + 1, mutation=label, verdicts=got,
                        caught=bool(parent[k] and not got[k] and all(got[j] == parent[j] for j in range(len(got)) if j != k))))
    return parent, out


def main():
    nfiles = c1.check_frozen_bytes()
    t0 = time.time()
    me = os.path.abspath(__file__)
    subprocess.run([sys.executable, me, '--stage', 'solve'], check=True)
    subprocess.run([sys.executable, me, '--stage', 'frozen'], check=True)
    procs = [subprocess.Popen([sys.executable, me, '--stage', 'ref', w]) for w in ('sel', 'off')]
    for p in procs:
        if p.wait() != 0:
            raise SystemExit('a reference run failed')
    load = lambda n: json.load(open(os.path.join(WORK, n)))
    S = load('solve.json')
    R = dict(one_period=S['one_period'], two_periods=S['two_periods'], frozen=load('frozen.json'),
             ref_sel=load('ref_sel.json'), ref_off=load('ref_off.json'), off=S['off'])
    checks = evaluate(R)
    parent, muts = mutations(R)
    A = R['one_period']
    summary = dict(control='1b', register='REGISTER_1.md, amendment of 2026-10-08T22:09:19Z',
                   case='P5 (the pyramid), R4, level 2, at the seed norm of eps_min; theta_start = pi/10',
                   frozen_solver=c1.SOLVER_COMMIT, frozen_files_checked=nfiles,
                   written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                   seconds=round(time.time() - t0, 1), checks=[dict(check=c, passed=bool(ok)) for c, ok in checks],
                   all_passed=all(ok for _, ok in checks), mutations=muts,
                   all_mutations_caught=all(m['caught'] for m in muts), **R)
    with open(os.path.join(HERE, 'control_1b.json'), 'w') as f:
        json.dump(summary, f, indent=1, default=str)
    L = [f'M8.15.x control 1b, {summary["written"]}: {summary["case"]}; frozen arm {c1.SOLVER_COMMIT}, '
         f'{nfiles} files checked', '',
         f'one period: {A["n_solves"]} Newton solves in {S["seconds_one_period"]} s; grid energy range {A["H_range"]:.4e}',
         '  grid:  theta        nu           mu           H                     sigma']
    for g in A['grid']:
        L.append(f'        {g["theta"]:.10f}  {g["nu"]:+.4e}  {g["mu"]:+.4e}  {g["H"]:.16f}  {g["sigma"]:.12f}')
    L.append('  roots: theta              off-symmetric   nu           mu           H                     min  res')
    for r in A['roots']:
        L.append(f'        {r["theta"]:.15f}  {sym_dist(r["theta"]):.1e}       {r["nu"]:+.4e}  {r["mu"]:+.4e}  '
                 f'{r["H"]:.16f}  {"yes" if r["minimum"] else "no "}  {r["res"]:.1e}')
    s = A['selected']
    L.append(f'  selected: theta {s["theta"]:.15f} (nearest symmetric angle {nearest_sym(s["theta"]):.6f}), H {s["H"]:.16f}; '
             f'near-degenerate {A["near_degenerate"]}')
    B = R['two_periods']
    L.append(f'two periods: minima {[(round(x["theta"], 12), x["cls"]) for x in B["minima"]]}, classes {B["n_classes"]}, '
             f'pair overlaps {B["pair_overlaps"]}')
    F = R['frozen']
    L.append(f'frozen at the selected angle: ok={F["ok"]}, iterations ' + ', '.join(f'{x["res"]:.2e}' for x in F['iterations']))
    for w in ('sel', 'off'):
        q = R[f'ref_{w}']
        L.append(f'reference run, {"selected point" if w == "sel" else "1a off-critical point (diagnostic)"}: '
                 f'dt {q["dt"]:.15f}, every {q["every"]} steps, to t = {q["last_t"]:.3f} (T_int {q["T_int"]:.6f}); max d_ref '
                 f'{q["max_dref"]:.3e}; first above eta at {q["t_first_above_eta"]}; charge drift {q["charge_drift"]:.1e}; '
                 f'{q["seconds"]} s')
    L.append(f'off-critical point: nu {R["off"]["nu"]:+.4e}, mu {R["off"]["mu"]:+.4e}')
    L.append('')
    L += [f'  {"PASS" if ok else "FAIL"}  {c}' for c, ok in checks]
    L.append(f'all registered checks passed: {summary["all_passed"]}')
    L += [f'  {"caught" if m["caught"] else "MISSED"}  check {m["check"]}: {m["mutation"]}' for m in muts]
    L.append(f'every mutation caught by its own check alone: {summary["all_mutations_caught"]}')
    with open(os.path.join(HERE, 'control_1b.log'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--stage':
        {'solve': stage_solve, 'frozen': stage_frozen}.get(sys.argv[2], lambda: stage_ref(sys.argv[3]))()
    else:
        main()
