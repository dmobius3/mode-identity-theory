"""Bench diagnostic, post-run, outside the record: the frozen pinned Newton at a case's seed (eps_min = 0.25),
repeated step for step with the multipliers kept, so the frozen stopping test can be split into its parts.

  NIT=10 python3 t4_gauge.py <path to m8_15_solver> <level> <case> <slot>      e.g.  ... 3 T4 4

Imports the frozen modules unchanged; writes nothing. Prints per iteration: the frozen test (gauge term excluded),
the bordered residual (gauge term included), the residual off the pinned fixed space, |mu T|/|Mx|, mu, nu, sigma;
then mu against its phase-invariance prediction -nu <i Phi, M s> / <i Phi, T>."""
import os, sys, time
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
SOLVER = sys.argv[1]
level, name, slot = int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
sys.path.insert(0, SOLVER)
import numpy as np, scipy.sparse as sps, scipy.sparse.linalg as spla
from m815_common import LevelCase
from nonlinear import to_real, to_complex, real_form, real_form_anti
from standing import fibre_generators

t0 = time.time()
lc = LevelCase(level, name, slot)
st, case = lc.st, lc.case
print(f'L{level} {name}/R{slot}: fixed dim {case.Br.shape[1]}, slices {len(lc.slices)}, setup {time.time()-t0:.0f}s', flush=True)
eps0 = 0.25
x = case.P @ to_real(case.seed)
m0 = eps0 / (lc.Q / lc.vol) / 120
x = x * np.sqrt(m0 / (x @ (st.Mr @ x)))
xref = x.copy()
Br, Mr = case.Br, st.Mr
T = []
for gen in fibre_generators(st.R.shape[1], case.quaternionic):
    t = to_real(gen(to_complex(x))); Mt = Mr @ t
    if np.linalg.norm(Br.T @ Mt) > 1e-8 * np.linalg.norm(Mt):
        T.append(Mt)
S = [Mr @ s for s in lc.slices]
ng, ns = len(T), len(S)
# overlap of each slice with the phase direction, in the M inner product, normalized
iP = to_real(1j * to_complex(x))
for k, s in enumerate(lc.slices):
    c = (iP @ (Mr @ s)) / np.sqrt((iP @ (Mr @ iP)) * (s @ (Mr @ s)))
    print(f'  slice {k}: M-cosine with the phase direction i*Phi = {c:.6f}')
mu, nu = np.zeros(ng), np.zeros(ns)
sigma = lc.lam0 + eps0
for it in range(int(os.environ.get("NIT", "8"))):
    Phi = to_complex(x); Mx = Mr @ x
    r0 = to_real(st.residual(Phi, sigma))
    F = st.Kr @ x - sigma * Mx + st.g * to_real(st.q.force(Phi)) + sum(mu[k] * T[k] for k in range(ng)) + sum(nu[k] * S[k] for k in range(ns))
    nMx = np.linalg.norm(Mx)
    full_frozen = np.linalg.norm(r0 + sum(nu[k] * S[k] for k in range(ns))) / nMx
    full_all = np.linalg.norm(F) / nMx
    off = np.linalg.norm(F - Br @ (Br.T @ F)) / nMx
    muT = np.linalg.norm(sum(mu[k] * T[k] for k in range(ng))) / nMx if ng else 0.0
    print(f'  it {it}: frozen test {full_frozen:.3e} | with gauge term {full_all:.3e} | off fixed space {off:.3e} | '
          f'|mu T|/|Mx| {muT:.3e} | mu {mu} | nu {nu} | sigma {sigma:.12f}', flush=True)
    A, B = st.q.jacobian(Phi)
    J = st.Kr - sigma * Mr + st.g * (real_form(A) + real_form_anti(B))
    Jf = (Br.T @ (J @ Br)).tocsc()
    cols = [Br.T @ (-Mx)] + [Br.T @ t for t in T] + [Br.T @ s for s in S]
    top = sps.hstack([Jf] + [sps.csr_matrix(cc[:, None]) for cc in cols])
    rowv = [Br.T @ (2 * Mx)] + [Br.T @ t for t in T] + [Br.T @ s for s in S]
    nb = 1 + ng + ns
    rows = [sps.csr_matrix(np.concatenate([r, np.zeros(nb)])[None, :]) for r in rowv]
    Big = sps.vstack([top] + rows, format='csc')
    c = np.array([x @ Mx - m0] + [T[k] @ x for k in range(ng)] + [S[k] @ (x - xref) for k in range(ns)])
    dz = spla.spsolve(Big, -np.concatenate([Br.T @ F, c]))
    p = Br.shape[1]
    x = x + Br @ dz[:p]; sigma += dz[p]; mu += dz[p + 1:p + 1 + ng]; nu += dz[p + 1 + ng:]
# the prediction from phase invariance: mu = -nu <i Phi, M s> / <i Phi, M i x0>
if ns:
    Phi = to_complex(x); iP = to_real(1j * Phi)
    pred = -sum(nu[k] * (iP @ S[k]) for k in range(ns)) / (iP @ T[0])
    print(f'  predicted mu from phase invariance {pred:.6e}, actual {mu[0]:.6e}')
print(f'done {time.time()-t0:.0f}s')
