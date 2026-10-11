"""M8.15.x control 1a (REGISTER_1.md): the stopping test on the pyramid held off its critical angle.

Two arms, each in its own process, on the same case P5a (the pyramid rotated about z by pi/10) in R4 at level 2,
through the seed solve that Branch.first makes at eps_min = 0.25:
  frozen: the solver at 6058f95, read from a copy checked byte for byte against the commit when the harness starts,
          with P5a added to its CASES at run time; no file of it changes;
  bench:  the bench solver, whose stopping test includes every multiplier (memo v4, § 1a).
A trace on solve_pinned reads its locals at the stopping test of every iteration; the solve itself is untouched.

  python3 control_1a.py            # both arms, then the registered checks; writes control_1a.json and control_1a.log"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment, as m815_branch.py sets it
import sys, json, subprocess, time, datetime
from math import sqrt

HERE = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.join(HERE, 'solver')
FROZEN = ('/private/tmp/claude-501/-Users-blake-mode-identity-theory--claude-worktrees-confident-varahamihira-0572e1/'
          '0ef115ee-4931-4ef1-a250-32508bad7d9f/scratchpad/frozen_arm')
REPO = '/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1'
SOLVER_COMMIT = '6058f95'
REPO_DIR = 'files/framework/files/working/files/scripts/soft-slot-dynamics'
EPS_MIN, LEVEL, SLOT = 0.25, 2, 4


def spec():
    import numpy as np
    return dict(slot=4, j2=6, u={3: sqrt(12 / 25), -2: sqrt(13 / 25) * np.exp(5j * np.pi / 10)}, gens=[('z', 5)],
                slice_axis='z')


def check_frozen_bytes():
    """Every .py of the solver and math packages at the commit, against the frozen copy."""
    n = 0
    for d in ('m8_15_solver', 'm8_15_math'):
        names = subprocess.run(['git', '-C', REPO, 'ls-tree', '--name-only', SOLVER_COMMIT, f'{REPO_DIR}/{d}/'],
                               capture_output=True, text=True, check=True).stdout.split()
        for f in names:
            if not f.endswith('.py'):
                continue
            ref = subprocess.run(['git', '-C', REPO, 'show', f'{SOLVER_COMMIT}:{f}'], capture_output=True, check=True).stdout
            with open(os.path.join(FROZEN, d, os.path.basename(f)), 'rb') as fh:
                if fh.read() != ref:
                    raise SystemExit(f'frozen copy differs from {SOLVER_COMMIT}: {d}/{os.path.basename(f)}')
            n += 1
    return n


def arm(which, out_path):
    sys.path.insert(0, os.path.join(FROZEN if which == 'frozen' else BENCH, 'm8_15_solver'))
    import inspect
    import numpy as np
    import pinned
    sp = spec()
    if which == 'frozen':
        assert 'P5a' not in pinned.CASES
        pinned.CASES['P5a'] = sp
    else:
        b = pinned.CASES['P5a']
        assert {k: v for k, v in b.items() if k != 'u'} == {k: v for k, v in sp.items() if k != 'u'}
        assert b['u'].keys() == sp['u'].keys() and all(b['u'][m] == sp['u'][m] for m in sp['u'])
    from m815_common import LevelCase
    from continuation import Branch
    from nonlinear import to_real, to_complex
    t0 = time.time()
    lc = LevelCase(LEVEL, 'P5a', SLOT)
    t_setup = time.time() - t0
    case, st = lc.case, lc.st
    s = lc.slices[0]
    S0 = st.Mr @ s
    Br = case.Br
    seed = case.P @ to_real(case.seed)
    p_seed = to_real(1j * to_complex(seed))
    diag = dict(orientation=case.orientation_report(), lam0=float(lc.lam0), Q=float(lc.Q), vol=float(lc.vol),
                slice_outside_fixed=float(np.linalg.norm(case.P @ s - s) / np.linalg.norm(s)),
                Mslice_outside_fixed=float(np.linalg.norm(S0 - Br @ (Br.T @ S0)) / np.linalg.norm(S0)),
                slice_phase_cosine=float((s @ (st.Mr @ p_seed)) / np.sqrt((s @ S0) * (p_seed @ (st.Mr @ p_seed)))),
                setup_seconds=round(t_setup, 1))
    code = pinned.solve_pinned.__code__
    lines, start = inspect.getsourcelines(pinned.solve_pinned)
    hits = [start + i for i, ln in enumerate(lines) if ln.strip() == 'if res < tol:']
    assert len(hits) == 1
    LINE = hits[0]
    its = []

    def local(frame, event, arg):
        if event == 'line' and frame.f_lineno == LINE:
            L = frame.f_locals
            x, F, Mx, mu, nu, T, S = L['x'], L['F'], L['Mx'], L['mu'], L['nu'], L['T'], L['S']
            assert len(T) == 1 and len(S) == 1
            nMx = np.linalg.norm(Mx)
            p = to_real(1j * to_complex(x))
            its.append(dict(
                it=int(L['it']), res=float(L['res']), full=float(L['full']), sigma=float(L['sigma']),
                mu=float(mu[0]), nu=float(nu[0]),
                new_form=float(np.linalg.norm(F) / nMx),
                old_form=float(np.linalg.norm(F - mu[0] * T[0]) / nMx),
                projected=float(np.linalg.norm(L['Br'].T @ F) / nMx),
                norm_constraint=float(abs(L['c'][0]) / L['m']), gauge_constraint=float(L['c'][1]),
                slice_constraint=float(L['c'][2]),
                mu_pred=float(-nu[0] * (p @ S[0]) / (p @ T[0])),
                plateau_pred=float(abs(mu[0]) * np.linalg.norm(T[0]) / nMx)))
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is code else None

    br = Branch(st, case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=lambda s: None)
    t1 = time.time()
    sys.settrace(glob)
    try:
        ok = br.first(EPS_MIN)
    finally:
        sys.settrace(None)
    out = dict(arm=which, ok=bool(ok), end=br.end, iterations=its, diagnostics=diag,
               solve_seconds=round(time.time() - t1, 1))
    if ok:
        r = br.accepted[0]
        out['accepted'] = dict(it=r['it'], full=float(r['full']), sigma=float(r['sigma']), eps=float(r['eps']),
                               m=float(r['m']), nu=[float(v) for v in r['nu']],
                               mu=[float(v) for v in r.get('mu', [])])
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=1, default=str)


def evaluate(fr, be):
    """The registered checks (REGISTER_1.md, 1a), on the two arms' records."""
    fl, bl = fr['iterations'][-1], be['iterations'][-1]
    plateau = fl['res']
    checks = [
        ('old form never below 1e-11 in 40 iterations; frozen seed solve ends in a Newton failure',
         len(fr['iterations']) == 40 and min(r['res'] for r in fr['iterations']) >= 1e-11 and not fr['ok']),
        ('old form plateaus at |mu| |M p0| / |M x| within 1e-3 relative',
         abs(fl['full'] - fl['plateau_pred']) <= 1e-3 * fl['plateau_pred']),
        ('the plateau is at least 1e-8', plateau >= 1e-8),
        ('new form falls below 1e-11', be['ok'] and bl['res'] < 1e-11),
        ('same fixed point: sigma equal to 12 digits', abs(bl['sigma'] - fl['sigma']) <= 1e-12 * abs(bl['sigma'])),
        ('|nu| >= 1e-8', abs(bl['nu']) >= 1e-8),
        ('mu = -nu <p, s>_M / <p, p0>_M within 1e-6 relative', abs(bl['mu'] - bl['mu_pred']) <= 1e-6 * abs(bl['mu_pred'])),
    ]
    return checks, plateau


def main():
    nfiles = check_frozen_bytes()
    res = {}
    for which in ('frozen', 'bench'):
        path = os.path.join(HERE, f'control_1a_{which}.json')
        subprocess.run([sys.executable, os.path.abspath(__file__), '--arm', which, path], check=True)
        with open(path) as f:
            res[which] = json.load(f)
        os.remove(path)
    fr, be = res['frozen'], res['bench']
    checks, plateau = evaluate(fr, be)
    fl, bl = fr['iterations'][-1], be['iterations'][-1]
    summary = dict(
        control='1a', register='REGISTER_1.md', case='P5a (the pyramid rotated about z by pi/10), R4, level 2, '
        'seed solve at eps_min = 0.25', frozen_solver=SOLVER_COMMIT, frozen_files_checked=nfiles,
        written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        checks=[dict(check=c, passed=bool(ok)) for c, ok in checks], all_passed=all(ok for _, ok in checks),
        plateau=plateau, plateau_over_tolerance=plateau / 1e-11,
        frozen_mu_vs_bench_mu=abs(fl['mu'] - bl['mu']) / abs(bl['mu']), arms=res)
    with open(os.path.join(HERE, 'control_1a.json'), 'w') as f:
        json.dump(summary, f, indent=1, default=str)
    L = [f'M8.15.x control 1a, {summary["written"]}: {summary["case"]}',
         f'frozen arm: {SOLVER_COMMIT}, {nfiles} files checked byte for byte; bench arm: m8_15x/solver', '']
    for which in ('frozen', 'bench'):
        a = res[which]
        L.append(f'{which}: ok={a["ok"]}, end={a["end"]}, {len(a["iterations"])} iterations, '
                 f'solve {a["solve_seconds"]} s; {a["diagnostics"]["orientation"]}')
        L.append('  it   res(test)   old form    new form    projected   sigma               mu          nu          mu_pred     plateau_pred')
        for r in a['iterations']:
            L.append(f'  {r["it"]:2d}   {r["res"]:.4e}  {r["old_form"]:.4e}  {r["new_form"]:.4e}  {r["projected"]:.4e}  '
                     f'{r["sigma"]:.14f}  {r["mu"]:+.4e}  {r["nu"]:+.4e}  {r["mu_pred"]:+.4e}  {r["plateau_pred"]:.4e}')
        L.append('')
    d = be['diagnostics']
    L.append(f'diagnostics (not registered): slice outside the fixed space {d["slice_outside_fixed"]:.1e}, M slice '
             f'{d["Mslice_outside_fixed"]:.1e}; slice-phase M-cosine at the seed {d["slice_phase_cosine"]:.4f}; '
             f'frozen-arm mu vs bench mu {summary["frozen_mu_vs_bench_mu"]:.1e} relative')
    L.append(f'plateau {plateau:.4e}, {summary["plateau_over_tolerance"]:.3g} times the tolerance')
    L += [f'  {"PASS" if c["passed"] else "FAIL"}  {c["check"]}' for c in summary['checks']]
    L.append(f'all registered checks passed: {summary["all_passed"]}')
    with open(os.path.join(HERE, 'control_1a.log'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--arm':
        arm(sys.argv[2], sys.argv[3])
    else:
        main()
