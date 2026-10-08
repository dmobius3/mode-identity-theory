"""POST-RUN DIAGNOSTIC ONLY, added after observing a target's failure; it cannot alter the frozen target verdict.
It repeats the continuation's first Newton solve at eps_min from the germ seed, the call Branch.first makes, with
solve_pinned's existing verbose switch on, so each iteration's residual and sigma are printed. No frozen file is changed.

  python3 m815_posthoc_newton.py <case> <slot>"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, time
import numpy as np
SOLVER = ('/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1/'
          'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_solver')
sys.path.insert(0, SOLVER)
os.chdir(SOLVER)
from m815_common import LevelCase, ladder, EPS_MAX
import m815_branch          # the run's full import closure; nothing runs on import
from nonlinear import to_real
from pinned import solve_pinned
name, slot = sys.argv[1], int(sys.argv[2])
eps0 = ladder(0.25, EPS_MAX[slot])[0]
lc = LevelCase(3, name, slot)
case, st = lc.case, lc.st
# Branch.first and Branch.newton, verbatim in effect
x = case.P @ to_real(case.seed)
m0 = eps0 / (lc.Q / lc.vol) / 120
m_x = x @ (st.Mr @ x)
x0 = x * np.sqrt(m0 / m_x)
t0 = time.time()
try:
    Phi, sigma, info = solve_pinned(st, case, m0, lc.lam0 + eps0, slices=lc.slices, tol=1e-11, maxit=40, x0=x0, verbose=True)
    print(f'converged: it {info["it"]}, sigma {sigma:.12f}, eps {sigma - lc.lam0:.9f}, {time.time() - t0:.0f} s')
except Exception as e:
    print(f'no convergence: {type(e).__name__}: {e}; {time.time() - t0:.0f} s')
