"""Check, by an independent route, a review unit's continuum figures cited in RESULT_2.md (its t4_angle.py and
target1_cond.py run on a library not on this bench): each slow block's principal cosines with the paired-lift plane
(the rotations perpendicular to J) and with the radical direction (the rotation about J), or with the whole rotation span
where J = 0, and its eigenvalue condition number. Route: branches_check's slow matrix S = J0 G^-1 M_u (as
continuum_overlap_survey.py builds it), in G-orthonormal coordinates; fibre and phase-partner directions projected out."""
import sys
import numpy as np
import sympy as sp
sys.path.insert(0, '/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1/files/framework/'
                   'files/working/files/scripts/soft-slot-branches')
import branches_check as bc


def study(name, u_exact, nzero, q=None):
    q = bc.Q4 if q is None else q
    hp, grad, hess = bc.setup(6, q)
    syms = hp.gens
    u = np.array([float(sp.N(x, 30)) for x in u_exact])
    G = np.array(bc.metric(6)).astype(float)
    J0 = np.array(bc.J0(6)).astype(float)
    Hf = sp.lambdify(syms, [[e.as_expr() for e in row] for row in hess], 'numpy')
    hf = sp.lambdify(syms, hp.as_expr(), 'numpy')
    lam = 4 * hf(*u) / (u @ G @ u)
    S = J0 @ np.linalg.solve(G, np.array(Hf(*u), float) - lam * G)
    Lc = np.linalg.cholesky(G)                      # G = Lc Lc^T; orthonormal coordinates z = Lc^T x
    T = Lc.T
    Sz = T @ S @ np.linalg.inv(T)
    uz = T @ u
    gens = [np.array(g).astype(float) for g in bc.gens(6)]
    X = [T @ (g @ u) for g in gens]
    Fb, _ = np.linalg.qr(np.column_stack([uz, T @ (J0 @ u)]))
    proj = lambda v: v - Fb @ (Fb.T @ v)
    Jv = np.array([u @ G @ (J0 @ (g @ u)) for g in gens])
    vals, V = np.linalg.eig(Sz)
    W = np.linalg.inv(V).conj().T
    scale = np.abs(vals).max()
    order = np.argsort(np.abs(vals))
    zero = set(order[:nzero].tolist())
    if np.linalg.norm(Jv) > 1e-9 * np.linalg.norm(u) ** 2:
        n = Jv / np.linalg.norm(Jv)
        a = np.cross(n, [1, 0, 0] if abs(n[0]) < 0.9 else [0, 1, 0]); a /= np.linalg.norm(a); b = np.cross(n, a)
        comb = lambda c: proj(sum(c[k] * X[k] for k in range(3)))
        P, _ = np.linalg.qr(np.column_stack([comb(a), comb(b)]))
        R = comb(n); R = R / np.linalg.norm(R)
        spans = dict(paired=P, radical=R[:, None])
    else:
        Rq, s, _ = np.linalg.svd(np.column_stack([proj(x) for x in X]), full_matrices=False)
        spans = dict(rotations=Rq[:, s > 1e-8 * s[0]])
    print(f'{name}: |J| = {np.linalg.norm(Jv):.3e}; zero cluster {nzero}')
    for k in order:
        l = vals[k]
        if k in zero or l.real < -1e-9 * scale or l.imag < -1e-9 * scale:
            continue
        x, y = V[:, k], W[:, k]
        pl, _ = np.linalg.qr(np.column_stack([x.real, x.imag]) if np.linalg.norm(x.imag) > 1e-9 * np.linalg.norm(x) else x.real[:, None])
        cosines = {nm: np.round(np.linalg.svd(pl.T @ B, compute_uv=False), 4).tolist() for nm, B in spans.items()}
        cond = np.linalg.norm(x) * np.linalg.norm(y) / abs(np.vdot(y, x))
        # for a repeated eigenvalue the per-vector number depends on the basis the solver returns: use the norm of the
        # spectral projector onto the whole eigenspace, which does not
        same = [j for j in range(len(vals)) if abs(vals[j] - l) <= 1e-7 * scale]
        if len(same) > 1:
            Pk = V[:, same] @ W[:, same].conj().T
            cond = float(np.linalg.norm(Pk, 2))
        widest = {nm: round(float(np.degrees(np.arccos(min(1.0, min(c))))), 1) for nm, c in cosines.items()}
        print(f'   |lambda|/max {abs(l) / scale:.4f} ({l / scale:.4f}): cosines {cosines}, widest angle {widest}; condition {cond:.1f}' + (' (projector, repeated eigenvalue)' if len(same) > 1 else ''))


rows = {r[0]: r for r in bc.R4_ROWS}
for nm in ('pyramid', 'prism', 'hexagon'):
    study(nm, bc.vec(6, rows[nm][1]), rows[nm][6])
study('T4, third outside orbit', [sp.Float(s, 60) for s in bc.OUTSIDE], 6)
