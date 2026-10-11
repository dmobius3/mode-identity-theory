"""M8.15.x control 1a, rerun under REGISTER_1.md's amendment of 2026-10-08T22:00:59Z: the slice covector projected
into the solve space. It runs control_1a.py's two arms unchanged, with their seven registered checks; then the
amendment's checks, against the unprojected run of 21:01Z (control_1a.json); then every armed mutation.

  python3 control_1a_amended.py      # writes control_1a_amended.json and control_1a_amended.log"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, subprocess, datetime, copy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import control_1a as c1
from control_1a_mutations import ARMS as ARMS_1A


def diag(out_path):
    """Bench solver, in its own process: the seed solve with a trace that keeps the solver's own slice covector at the
    stopping test, and the amendment's quantities at the converged point, with those of the mutations."""
    sys.path.insert(0, os.path.join(c1.BENCH, 'm8_15_solver'))
    import inspect
    import numpy as np
    import pinned
    from m815_common import LevelCase
    from continuation import Branch
    lc = LevelCase(c1.LEVEL, 'P5a', c1.SLOT)
    st, case = lc.st, lc.case
    Br = case.Br
    S0 = st.Mr @ lc.slices[0]                         # the raw covector M s
    code = pinned.solve_pinned.__code__
    lines, start = inspect.getsourcelines(pinned.solve_pinned)
    hits = [start + i for i, ln in enumerate(lines) if ln.strip() == 'if res < tol:']
    assert len(hits) == 1
    LINE = hits[0]
    keep = {}

    def local(frame, event, arg):
        if event == 'line' and frame.f_lineno == LINE:
            L = frame.f_locals
            keep.update(S=L['S'][0].copy(), F=L['F'].copy(), Mx=L['Mx'].copy(), nu=float(L['nu'][0]), res=float(L['res']))
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is code else None

    br = Branch(st, case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=lambda s: None)
    sys.settrace(glob)
    try:
        ok = br.first(c1.EPS_MIN)
    finally:
        sys.settrace(None)
    assert ok
    nrm = np.linalg.norm
    Sh, F, nMx, nu = keep['S'], keep['F'], nrm(keep['Mx']), keep['nu']
    out = lambda v: v - Br @ (Br.T @ v)
    j = int(np.argmax(np.abs(Br.T @ S0)))
    Bd = Br[:, [k for k in range(Br.shape[1]) if k != j]]
    Sm = Bd @ (Bd.T @ S0)                              # mutation for check 1: a projection missing one basis column
    res = dict(
        q1=nrm(Br.T @ (Sh - S0)) / nrm(Br.T @ S0), q2=nrm(out(Sh)) / nrm(Sh), q4nu=abs(nu) * nrm(out(Sh)) / nMx,
        m1=nrm(Br.T @ (Sm - S0)) / nrm(Br.T @ S0), m2=nrm(out(S0)) / nrm(S0), m4nu=abs(nu) * nrm(out(S0)) / nMx,
        final_res=keep['res'], inside=nrm(Br.T @ F) / nMx, outside=nrm(out(F)) / nMx)
    with open(out_path, 'w') as f:
        json.dump({k: float(v) for k, v in res.items()}, f, indent=1)


def amend_checks(d, floor, acc, ref):
    rel = lambda a, b: abs(a - b) / abs(b)
    return [
        ('1. B_r^T S_hat = B_r^T M s to 1e-12 relative', d['q1'] <= 1e-12),
        ('2. S_hat outside the fixed space at most 1e-12', d['q2'] <= 1e-12),
        ('4a. the floor is at most 6e-13', floor <= 6e-13),
        ('4b. the nu term outside the fixed space is at most 1e-15', d['q4nu'] <= 1e-15),
        ('5a. sigma unchanged to 12 digits', rel(acc['sigma'], ref['sigma']) <= 1e-12),
        ('5b. mu unchanged to 1e-9 relative', rel(acc['mu'][0], ref['mu'][0]) <= 1e-9),
        ('5c. nu unchanged to 1e-9 relative', rel(acc['nu'][0], ref['nu'][0]) <= 1e-9),
    ]


def scaled(acc, key, f):
    a = copy.deepcopy(acc)
    a[key] = [v * f for v in a[key]] if isinstance(a[key], list) else a[key] * f
    return a


def main():
    nfiles = c1.check_frozen_bytes()
    res = {}
    for which in ('frozen', 'bench'):
        path = os.path.join(HERE, f'control_1a_amended_{which}.json')
        subprocess.run([sys.executable, os.path.join(HERE, 'control_1a.py'), '--arm', which, path], check=True)
        with open(path) as f:
            res[which] = json.load(f)
        os.remove(path)
    dpath = os.path.join(HERE, 'control_1a_amended_diag.json')
    subprocess.run([sys.executable, os.path.abspath(__file__), '--diag', dpath], check=True)
    with open(dpath) as f:
        d = json.load(f)
    os.remove(dpath)
    with open(os.path.join(HERE, 'control_1a.json')) as f:
        ref = json.load(f)                             # the unprojected run of 21:01Z
    fr, be = res['frozen'], res['bench']
    rfr, rbe = ref['arms']['frozen'], ref['arms']['bench']
    checks7, plateau = c1.evaluate(fr, be)
    floor = be['iterations'][-1]['res']
    acc, racc = be['accepted'], rbe['accepted']
    checks = amend_checks(d, floor, acc, racc)
    parent = [ok for _, ok in checks]
    # armed mutations of the amendment's checks: each must be caught by its own check alone
    muts = [
        (0, 'a projection missing one basis column', dict(d, q1=d['m1']), floor, acc),
        (1, 'the unprojected covector M s', dict(d, q2=d['m2']), floor, acc),
        (2, 'the unprojected run\'s floor', d, rbe['iterations'][-1]['res'], acc),
        (3, 'the unprojected covector\'s nu term', dict(d, q4nu=d['m4nu']), floor, acc),
        (4, 'sigma moved by 2e-12 relative', d, floor, scaled(acc, 'sigma', 1 + 2e-12)),
        (5, 'mu moved by 2e-9 relative', d, floor, scaled(acc, 'mu', 1 + 2e-9)),
        (6, 'nu moved by 2e-9 relative', d, floor, scaled(acc, 'nu', 1 + 2e-9)),
    ]
    mres = []
    for k, label, dm, fm, am in muts:
        got = [ok for _, ok in amend_checks(dm, fm, am, racc)]
        caught = parent[k] and not got[k] and all(got[j] == parent[j] for j in range(len(got)) if j != k)
        mres.append(dict(check=checks[k][0], mutation=label, caught=bool(caught), verdicts=got))
    # check 3's mutations: 1a's own ten arms on the new record
    p7 = [ok for _, ok in checks7]
    for k, label, mut in ARMS_1A:
        f2, b2 = copy.deepcopy(fr), copy.deepcopy(be)
        mut(f2, b2)
        got = [ok for _, ok in c1.evaluate(f2, b2)[0]]
        caught = p7[k] and not got[k] and all(got[j] == p7[j] for j in range(len(got)) if j != k)
        mres.append(dict(check=f'3. (1a check {k + 1})', mutation=label, caught=bool(caught), verdicts=got))
    # not registered: reproducibility against the run of 21:01Z
    same_frozen = fr['iterations'] == rfr['iterations']
    it_rel = max(max(abs(a[key] - b[key]) / max(abs(b[key]), 1e-300) for key in ('sigma', 'mu', 'nu'))
                 for a, b in zip(be['iterations'][1:], rbe['iterations'][1:]))
    summary = dict(
        control='1a, rerun under the amendment', register='REGISTER_1.md, amendment of 2026-10-08T22:00:59Z',
        reference='control_1a.json (the unprojected run of 2026-10-08T21:01:30Z)', frozen_files_checked=nfiles,
        written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        checks_1a=[dict(check=c, passed=bool(ok)) for c, ok in checks7],
        checks_amendment=[dict(check=c, passed=bool(ok)) for c, ok in checks],
        all_passed=all(p7) and all(parent), mutations=mres, all_mutations_caught=all(m['caught'] for m in mres),
        diagnostics=d, floor=floor, plateau=plateau, frozen_arm_identical_to_2101=same_frozen,
        bench_iterates_max_rel_diff_sigma_mu_nu=it_rel, newton_iterations=(acc['it'], racc['it']), arms=res)
    with open(os.path.join(HERE, 'control_1a_amended.json'), 'w') as f:
        json.dump(summary, f, indent=1, default=str)
    L = [f'M8.15.x control 1a rerun under the amendment, {summary["written"]}: '
         f'P5a, R4, level 2, seed solve at eps_min = 0.25; frozen arm {c1.SOLVER_COMMIT}, {nfiles} files checked', '']
    L.append(f'bench: ok={be["ok"]}, {len(be["iterations"])} iterations (unprojected run: {len(rbe["iterations"])})')
    L.append('  it   res(test)   old form    new form    projected   sigma               mu          nu')
    for r in be['iterations']:
        L.append(f'  {r["it"]:2d}   {r["res"]:.4e}  {r["old_form"]:.4e}  {r["new_form"]:.4e}  {r["projected"]:.4e}  '
                 f'{r["sigma"]:.14f}  {r["mu"]:+.4e}  {r["nu"]:+.4e}')
    L.append('')
    L.append(f'floor {floor:.4e} (unprojected {rbe["iterations"][-1]["res"]:.4e}); at the converged point: inside '
             f'{d["inside"]:.4e}, outside {d["outside"]:.4e}; nu term outside {d["q4nu"]:.1e} (unprojected {d["m4nu"]:.1e})')
    L.append(f'B_r^T(S_hat - M s) {d["q1"]:.1e} relative; S_hat outside {d["q2"]:.1e} (M s: {d["m2"]:.1e})')
    L.append(f'not registered: frozen arm identical to 21:01Z: {same_frozen}; bench iterates vs 21:01Z, sigma, mu, nu '
             f'within {it_rel:.1e} relative; Newton iterations {acc["it"]} (unprojected {racc["it"]})')
    L.append('')
    L += [f'  {"PASS" if ok else "FAIL"}  1a check {i + 1}: {c}' for i, (c, ok) in enumerate(checks7)]
    L += [f'  {"PASS" if ok else "FAIL"}  {c}' for c, ok in checks]
    L.append(f'all registered checks passed: {summary["all_passed"]}')
    L.append('')
    L += [f'  {"caught" if m["caught"] else "MISSED"}  {m["check"]}: {m["mutation"]}' for m in mres]
    L.append(f'every mutation caught by its own check alone: {summary["all_mutations_caught"]}')
    with open(os.path.join(HERE, 'control_1a_amended.log'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--diag':
        diag(sys.argv[2])
    else:
        main()
