"""M8.15.x qualification, after the run: why the stopping test's residual moved. A diagnostic, not a registered check.

Three parts, on the bench solver in the one-thread environment:
  1. the records: every residual in the four regression records with Newton solves (linear_L3, linear_L2 and the two
     branches), against its baseline; how far each moved, against sum |mu| and against the registered bound;
  2. the two codings of the physical residual: the frozen test applies K and M as complex matrices to Phi
     (standing.residual), the bench's inline F applies their real forms Kr and Mr to x; both on a random vector at level 2;
  3. the converged iterate of the level-2 seed solves of C3 and C2a in R4 (eps_min = 0.25), traced as control 1a traced
     its arms: the frozen form, the bench's F without the mu terms, and the bench's F, at the final stopping test; and
     |T| / |M x| for each gauge vector T, which is built at the solve's starting point (added after the units' review).

  python3 diag_residual.py > diag_residual.out"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment, as m815_branch.py sets it
import sys, json, inspect

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, 'solver', 'm8_15_solver')
OUT = os.path.join(SOLVER, 'out')
BASE = os.path.join(HERE, 'qual_2026-10-09', 'baseline')
CF = os.path.join(BASE, 'controls_first_2026-10-07')
sys.path.insert(0, SOLVER)
import numpy as np


def residuals(new, old, out):
    """(new, old, sum |mu|) for every residual in a record, walked in step with its baseline."""
    if isinstance(old, dict):
        if 'residual' in old:
            out.append((new['residual'], old['residual'], float(sum(abs(m) for m in new['gauge_multipliers']))))
        for k in old:
            if k in new:
                residuals(new[k], old[k], out)
    elif isinstance(old, list):
        for a, b in zip(new, old):
            residuals(a, b, out)


def part1():
    print('1. the records')
    allr = []
    for label, pn, po in [('linear_L3', 'linear_L3.json', os.path.join(CF, 'linear_L3.json')),
                          ('linear_L2', 'linear_L2.json', os.path.join(CF, 'linear_L2.json')),
                          ('branch_C3_R4', 'branch_C3_R4.json', os.path.join(BASE, 'branch_C3_R4.json')),
                          ('branch_C2a_R4', 'branch_C2a_R4.json', os.path.join(BASE, 'branch_C2a_R4.json'))]:
        r = []
        residuals(json.load(open(os.path.join(OUT, pn))), json.load(open(po)), r)
        d = [abs(a - b) for a, b, _ in r]
        sm = [s for _, _, s in r]
        print(f'   {label}: {len(r)} residuals, {sum(x > 0 for x in d)} moved; old {min(b for _, b, _ in r):.2e} to '
              f'{max(b for _, b, _ in r):.2e}, new {min(a for a, _, _ in r):.2e} to {max(a for a, _, _ in r):.2e}; '
              f'|new - old| up to {max(d):.2e}, relative {min(x / b for x, (_, b, _) in zip(d, r)):.1e} to '
              f'{max(x / b for x, (_, b, _) in zip(d, r)):.1e}; sum |mu| up to {max(sm):.2e}; '
              f'|new - old| > sum |mu| at {sum(x > y for x, y in zip(d, sm))}')
        allr += r
    d = [abs(a - b) for a, b, _ in allr]
    sm = [s for _, _, s in allr]
    print(f'   all: {len(allr)} residuals; largest |new - old| {max(d):.2e}; largest sum |mu| {max(sm):.2e}; '
          f'largest excess of |new - old| over sum |mu| {max(x - y for x, y in zip(d, sm)):.2e}; '
          f'largest |new - old| / (sum |mu| + 1e-13) {max(x / (y + 1e-13) for x, y in zip(d, sm)):.2f}; '
          f'|new - old| > sum |mu| at {sum(x > y for x, y in zip(d, sm))} of {len(allr)}')


def part2(st):
    from nonlinear import to_real, to_complex
    print('2. the two codings, on a random vector at level 2 (C3)')
    print(f'   K, M: {st.K.dtype} {st.K.shape}; Kr, Mr: {st.Kr.dtype} {st.Kr.shape}')
    x = np.random.default_rng(0).standard_normal(st.Mr.shape[0])
    Phi = to_complex(x)
    for nm, A, Ar in (('K', st.K, st.Kr), ('M', st.M, st.Mr)):
        a, b = to_real(A @ Phi), Ar @ x
        print(f'   |to_real({nm} Phi) - {nm}r x| / |{nm}r x| = {np.linalg.norm(a - b) / np.linalg.norm(b):.2e}; '
              f'bit-identical: {bool(np.array_equal(a, b))}')


def part3(name, lc):
    import pinned
    from continuation import Branch
    from nonlinear import to_real, to_complex
    st, case = lc.st, lc.case
    lines, start = inspect.getsourcelines(pinned.solve_pinned)
    hits = [start + i for i, ln in enumerate(lines) if ln.strip() == 'if res < tol:']
    assert len(hits) == 1
    LINE = hits[0]
    its = []

    def local(frame, event, arg):
        if event == 'line' and frame.f_lineno == LINE:
            L = frame.f_locals
            x, F, Mx, mu, T, sig = L['x'], L['F'], L['Mx'], L['mu'], L['T'], L['sigma']
            nMx = np.linalg.norm(Mx)
            Fnomu = F - sum(mu[k] * T[k] for k in range(len(T)))
            Fold = to_real(st.residual(to_complex(x), sig))
            its.append(dict(it=int(L['it']), frozen_form=float(np.linalg.norm(Fold) / nMx),
                            bench_without_mu=float(np.linalg.norm(Fnomu) / nMx), bench_full=float(L['full']),
                            sum_mu=float(np.abs(mu).sum()), vector_difference=float(np.linalg.norm(Fold - Fnomu) / nMx),
                            gauge_norms=[float(np.linalg.norm(t) / nMx) for t in T]))
        return local

    code = pinned.solve_pinned.__code__
    br = Branch(st, case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=lambda s: None)
    sys.settrace(lambda f, e, a: local if f.f_code is code else None)
    try:
        ok = br.first(0.25)
    finally:
        sys.settrace(None)
    z = its[-1]
    print(f'3. {name} in R4, level 2, the seed solve at eps_min = 0.25: converged {ok} after {len(its)} stopping tests')
    print(f'   at the final iterate, all relative to |M x|: frozen form {z["frozen_form"]:.4e}; bench F without the mu '
          f'terms {z["bench_without_mu"]:.4e}; bench F {z["bench_full"]:.4e}; sum |mu| {z["sum_mu"]:.2e}')
    print(f'   |frozen form - bench F without mu| = {abs(z["frozen_form"] - z["bench_without_mu"]):.2e} (the coding); '
          f'|bench F - bench F without mu| = {abs(z["bench_full"] - z["bench_without_mu"]):.2e} (the mu terms)')
    print(f'   the two residual vectors differ by {z["vector_difference"]:.2e}, '
          f'{z["vector_difference"] / z["frozen_form"]:.2f} of the frozen form\'s own norm')
    print(f'   each gauge vector T, built at the solve\'s starting point, against |M x| at the final iterate: '
          f'{", ".join(f"{g:.6f}" for g in z["gauge_norms"])}')


if __name__ == '__main__':
    import numpy, scipy, platform
    print(f'diag_residual.py: Python {platform.python_version()}, numpy {numpy.__version__}, scipy {scipy.__version__}')
    part1()
    from m815_common import LevelCase
    lc = LevelCase(2, 'C3', 4)
    part2(lc.st)
    part3('C3', lc)
    part3('C2a', LevelCase(2, 'C2a', 4))
