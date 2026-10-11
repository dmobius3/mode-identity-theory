"""Control 1a, a diagnostic beside the registered checks (not registered): where the new test's floor comes from, at
the bench arm's converged point. F, the full bordered residual, splits into its part inside the fixed space (what
Newton solves) and its part outside, which Newton cannot reach; the slice's own part outside, times nu, is compared
with the latter. Writes control_1a_floor.log."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'solver', 'm8_15_solver'))
from m815_common import LevelCase
from continuation import Branch
from nonlinear import to_real, to_complex

lc = LevelCase(2, 'P5a', 4)
st, case = lc.st, lc.case
br = Branch(st, case, lc.lam0, lc.Q, lc.vol, slices=lc.slices, log=lambda s: None)
assert br.first(0.25)
r = br.accepted[0]
x, sigma, mu, nu = r['x'], r['sigma'], r['mu'][0], r['nu'][0]
# the gauge vector exactly as solve_pinned builds it, from the seed solve's starting point
x_seed = case.P @ to_real(case.seed)
m0 = 0.25 / (lc.Q / lc.vol) / 120
xs = x_seed * np.sqrt(m0 / (x_seed @ (st.Mr @ x_seed)))
xi = xs * np.sqrt(m0 / (xs @ (st.Mr @ xs)))
T = st.Mr @ to_real(1j * to_complex(xi))
S = st.Mr @ lc.slices[0]
Mx = st.Mr @ x
F = st.Kr @ x - sigma * Mx + st.g * to_real(st.q.force(to_complex(x))) + mu * T + nu * S
Br = case.Br
out = lambda v: v - Br @ (Br.T @ v)
n = np.linalg.norm(Mx)
rows = [
    ('full bordered residual |F| / |Mx| (the recorded test value)', np.linalg.norm(F) / n, r['full']),
    ('its part inside the fixed space, |Br^T F| / |Mx|', np.linalg.norm(Br.T @ F) / n, None),
    ('its part outside the fixed space', np.linalg.norm(out(F)) / n, None),
    ('nu times the slice force vector outside the fixed space, |nu out(M s)| / |Mx|', abs(nu) * np.linalg.norm(out(S)) / n, None),
    ('the remainder outside, |out(F) - nu out(M s)| / |Mx|', np.linalg.norm(out(F) - nu * out(S)) / n, None),
    ('the slice term, |nu M s| / |Mx|', abs(nu) * np.linalg.norm(S) / n, None),
    ('the phase term, |mu M p0| / |Mx|', abs(mu) * np.linalg.norm(T) / n, None),
    ('the fraction of M s outside the fixed space', np.linalg.norm(out(S)) / np.linalg.norm(S), None),
]
L = ['control 1a, the new test\'s floor at the bench arm\'s converged point (not registered)']
for label, v, ref in rows:
    L.append(f'  {v:.4e}  {label}' + (f'  [recorded {ref:.4e}]' if ref is not None else ''))
open(os.path.join(HERE, 'control_1a_floor.log'), 'w').write('\n'.join(L) + '\n')
print('\n'.join(L))
