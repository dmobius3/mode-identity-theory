"""M8.15 freeze input: the third outside orbit's four slow frequencies and their Krein signs, computed at 60 digits
from the certified point in branches_check.py at MIT d0de8ca (R4, unit u, h normalization)."""
import sys, numpy as np, mpmath as mp, sympy as sp
sys.path.insert(0, '.')
from analyse import setup
from core import metric, J0
from sympy import Rational as R
mp.mp.dps = 60
q4 = {6: R(1288, 1287), 4: R(35, 33), 2: R(14, 9), 0: R(7, 3)}
hp, grad, hess = setup(6, q4)
N = 14
G = metric(6); Gd = [int(G[i, i]) for i in range(N)]
syms = sorted(hp.free_symbols, key=lambda s: s.name) if hasattr(hp, 'free_symbols') else None
def compile_poly(P):
    terms = [(mon, sp.Rational(c)) for mon, c in P.terms()]
    def ev(xs):
        tot = mp.mpf(0)
        for mon, c in terms:
            t = mp.mpf(c.p) / c.q
            for xi, e in zip(xs, mon):
                if e: t *= xi**e
            tot += t
        return tot
    return ev
h_ev = compile_poly(hp)
H_ev = [[compile_poly(e) for e in row] for row in hess]
# the certified point, read from the landed check at the pinned commit (not from a local copy)
import ast, os, subprocess
WT = os.path.dirname(os.path.abspath(__file__))          # inside the MIT repo, which holds the pinned commit
SRC = 'd0de8ca61f8e166586731b6167ab895c09368630:files/framework/files/working/files/scripts/soft-slot-branches/branches_check.py'
txt = subprocess.run(['git', '-C', WT, 'show', SRC], capture_output=True, text=True, check=True).stdout
i0 = txt.index('OUTSIDE = ['); i1 = txt.index(']', i0) + 1
OUTSIDE = ast.literal_eval(txt[i0 + len('OUTSIDE = '):i1])
assert len(OUTSIDE) == 14
loc = np.load('outside3_p.npy')
print('pinned point equals the bench copy:', all(mp.mpf(a) == mp.mpf(str(b)) for a, b in zip(OUTSIDE, loc)) if loc.dtype.kind in 'OU' else 'bench copy not string-typed')
xt = [mp.mpf(s) for s in OUTSIDE]
nrm = sum(Gd[i] * xt[i]**2 for i in range(N))
x = [t / mp.sqrt(nrm) for t in xt]                      # unit in the G metric
lam = 4 * h_ev(x)
M = mp.matrix([[H_ev[a][b](x) - (lam * Gd[a] if a == b else 0) for b in range(N)] for a in range(N)])
J = J0(6); Jm = mp.matrix([[int(J[a, b]) for b in range(N)] for a in range(N)])
Ginv = mp.diag([mp.mpf(1) / g for g in Gd])
S = Jm * Ginv * M
ev, V = mp.eig(S)
print('Q(u) =', mp.nstr(h_ev(x), 16), '  nrm before =', mp.nstr(nrm, 6))
S2 = S * S
for nu_s in ['-1.0243294167', '-0.0965299801561', '-0.0193910729839', '-3.29115537456e-5']:
    # refine the root as an eigenvalue of S^2 nearest nu_s, then take the real invariant 2-space
    e2, W = mp.eig(S2)
    i = min(range(N), key=lambda k: abs(e2[k] - mp.mpf(nu_s)))
    nu = mp.re(e2[i])
    A = S2 - nu * mp.eye(N)
    U_, s_, Vt = mp.svd_r(A)
    vecs = [Vt[N - 1 - k, :].T for k in range(2)]        # two smallest singular directions
    sing = [s_[N - 1 - k] for k in range(2)] + [s_[N - 3]]
    B = mp.matrix(2, 2)
    for p in range(2):
        for q in range(2):
            B[p, q] = (vecs[p].T * M * vecs[q])[0]
    eB = mp.eig(B)[0]
    print(f'nu = {mp.nstr(nu, 15)}: tau = {mp.nstr(mp.sqrt(-nu), 12)}; smallest singular values {[mp.nstr(t, 3) for t in sing]}; '
          f'M on the pair: {[mp.nstr(mp.re(t), 6) for t in eB]}')
