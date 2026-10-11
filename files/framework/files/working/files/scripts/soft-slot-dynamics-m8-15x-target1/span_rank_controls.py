"""Controls only, kept as the basis of REGISTER_4.md's structural-span gate: the singular values of the locator's
structural span (fibre generators and X_a Phi, without chi, columns M-normalized) on C2a/R4 and C3/R4 at level 2,
at eps = 0.25, 2 and 16. No target is solved.

  python3 span_rank_controls.py > span_rank_controls.out"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
sys.path.insert(0, '/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1/files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x/m8_15x_solver')
import numpy as np
from m815_common import LevelCase
from standing import fibre_generators
from nonlinear import to_real, to_complex
for name, slot in (('C2a', 4), ('C3', 4)):
    lc = LevelCase(2, name, slot)
    st, case = lc.st, lc.case
    recs = {}
    br = lc.branch([0.25, 0.3535533905932738, 0.5, 0.7071067811865476, 1.0, 1.4142135623730951, 2.0, 2.8284271247461903, 4.0, 5.656854249492381, 8.0, 11.313708498984761, 16.0],
                   lambda k, e, rec: recs.__setitem__(e, rec))
    for e in (0.25, 2.0, 16.0):
        if e not in recs:
            print(name, e, 'not reached'); continue
        Phi = to_complex(recs[e]['x'])
        gens = fibre_generators(st.R.shape[1], case.quaternionic)
        cols = [to_real(g(Phi)) for g in gens] + [to_real(v) for v in lc.rot.all(Phi)]
        V = np.column_stack(cols)
        Mr = st.Mr
        nrm = np.sqrt(np.einsum('ij,ij->j', V, Mr @ V))
        Vn = V / nrm
        C = Vn.T @ (Mr @ Vn); C = (C + C.T) / 2
        ev = np.sort(np.linalg.eigvalsh(C))[::-1]
        sv = np.sqrt(np.clip(ev, 0, None))
        print(f'{name} L2 eps {e}: {len(gens)} fibre + {V.shape[1]-len(gens)} rotation vectors; singular values / largest: ' + ', '.join(f'{s/sv[0]:.3e}' for s in sv))
