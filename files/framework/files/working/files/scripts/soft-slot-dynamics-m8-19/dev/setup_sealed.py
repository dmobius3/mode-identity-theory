"""The dry run's step 7 (DESIGN.md): each sealed case set up at levels 2 and 3 without a solve, so that a broken case
definition shows before the freeze. For T1 and T4 in both slots and C2a in R5 it builds what LevelCase builds before
its first solve, except the lowest level's eigenvalues: the mesh, PinnedCase (orientation, pinned subgroup, seed,
fixed space), Standing's matrices, the rotations and any slice; then the seed's Q against the exact one, with the
control C2a/R4 beside them for scale. No Newton step is taken, and no eigenvalue of the Laplacian or of a
linearization is computed; the one decomposition is PinnedCase's SVD of its symmetry projector, for the fixed space.

  setup_sealed.py      writes dev/setup_sealed.out"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INSTRUMENT = os.path.normpath(os.path.join(ROOT, '..', 'soft-slot-dynamics-m8-15x', 'm8_15x_solver'))
sys.path.insert(0, os.path.join(ROOT, 'run'))
sys.path.insert(0, INSTRUMENT)
import numpy as np  # noqa: E402
from fem import Mesh  # noqa: E402
from m815_common import RS, QEXACT, FROZEN_DIM  # noqa: E402
from pinned import PinnedCase, CASES  # noqa: E402
from standing import Standing  # noqa: E402
from symmetry import Rotations  # noqa: E402
import m819_branch as D  # noqa: E402

lines = []


def say(s):
    print(s, flush=True)
    lines.append(s)


D.inject_coherent_R5()
say('The sealed cases set up without a solve: no Newton step, no eigenvalue of the Laplacian or a linearization')
for level in (2, 3):
    t0 = time.time()
    mesh = Mesh(level, nq=3)
    vol = 120 * mesh.vol.sum()
    say(f'level {level}: mesh built in {time.time() - t0:.0f} s')
    for name, slot in [('C2a', 4)] + sorted(D.SEALED):     # C2a/R4, a control, for scale beside the sealed five
        t1 = time.time()
        case = PinnedCase(mesh, RS, name, slot=slot)
        st = Standing(mesh, case.R, quaternionic=case.quaternionic)
        rot = Rotations(mesh, case.R, st.M)
        P = case.seed
        Q = vol * 4 * st.q.energy(P) * 120 / (120 * np.real(np.vdot(P, st.M @ P))) ** 2
        q = QEXACT[(name, slot)]
        sl = 'slice ' + str(CASES[name].get('slice_axis')) if CASES[name].get('slice_axis') else 'no slice'
        say(f'  {name}/R{slot}: {case.orientation_report()}; frozen cluster dimension {FROZEN_DIM[name]}; {sl}; '
            f'seed Q {Q:.10f} against exact {q:.10f}, relative {Q / q - 1:+.2e}; {time.time() - t1:.0f} s')
        del case, st, rot
with open(os.path.join(HERE, 'setup_sealed.out'), 'w') as f:
    f.write('\n'.join(lines) + '\n')
