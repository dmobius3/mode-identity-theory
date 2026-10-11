"""M8.15.x bench, step 1 of the instrument revision (memo v4, § 2's control 2a): a continuum survey of the census orbits.

For each orbit's small-amplitude slow matrix S = J0 G^-1 M_u (the reduced quartic's, as in branches_check.analyse), it
lists every genuine slow eigenvalue (outside the zero cluster) with the static overlap of its eigenvector with the
structural span the frozen 0.9 rule reads, split into its parts:
  U_full = span_G{ u, i u, J_a u (a = 1, 2, 3) }  (u: the phase partner's static part at small amplitude; R2 adds the
           quaternionic directions theta u, theta i u);  U_rot = span_G{ J_a u };  U_fib = U_full's fibre and partner part.
Overlap of a complex eigenvector v with a real G-orthonormal span W: sqrt(sum_w |w^T G v|^2) / sqrt(v^H G v).
Continuum mathematics on public spectra only: no solver, no mesh, no target run. Targets appear only as labelled
validation rows against the review's published continuum figures; they never enter a control choice."""
import sys
import numpy as np
import sympy as sp

sys.path.insert(0, '/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1/files/framework/'
                   'files/working/files/scripts/soft-slot-branches')
import branches_check as bc

TARGETS = {'v2': 'T1', 'prism': 'T2', 'hexagon': 'T3', 'line {7/2, -3/2}': 'T5'}
CONTROLS = {'coherent v3': 'C2a', 'weight 7/2': 'C2b'}


def g_orthonormal(V, G):
    """Columns of V made G-orthonormal (modified Gram-Schmidt), dropping dependent ones."""
    out = []
    for c in V.T:
        w = c.astype(float).copy()
        for q in out:
            w -= (q @ G @ w) * q
        nw = np.sqrt(w @ G @ w)
        if nw > 1e-10 * max(1.0, np.sqrt(c @ G @ c)):
            out.append(w / nw)
    return np.array(out).T if out else np.zeros((V.shape[0], 0))


def overlap(v, W, G):
    if W.shape[1] == 0:
        return 0.0
    c = W.T @ G @ v
    return float(np.sqrt(np.sum(np.abs(c) ** 2)) / np.sqrt(abs(np.vdot(v, G @ v))))


def survey(name, j2, q, u_exact, quaternionic, nzero):
    hp, grad, hess = bc.setup(j2, q)
    syms = hp.gens
    u = np.array([float(sp.N(x, 30)) for x in u_exact])
    G = np.array(bc.metric(j2)).astype(float)
    J0 = np.array(bc.J0(j2)).astype(float)
    Hf = sp.lambdify(syms, [[e.as_expr() for e in row] for row in hess], 'numpy')
    hf = sp.lambdify(syms, hp.as_expr(), 'numpy')
    nrm = u @ G @ u
    lam = 4 * hf(*u) / nrm
    Mu = np.array(Hf(*u), float) - lam * G
    S = J0 @ np.linalg.solve(G, Mu)
    vals, vecs = np.linalg.eig(S)
    scale = max(1e-300, np.abs(vals).max())
    # the zero cluster by the census's own zero multiplicity: the nzero smallest moduli (a defective zero splits numerically)
    zero_idx = set(np.argsort(np.abs(vals))[:nzero].tolist())
    gl = [J0] + [np.array(g).astype(float) for g in bc.gens(j2)]
    th = [np.array(bc.theta(j2)).astype(float)] if quaternionic else []
    fib_cols = [u, J0 @ u] + ([th[0] @ u, th[0] @ J0 @ u] if th else [])
    rot_cols = [g @ u for g in gl[1:]]
    U_full = g_orthonormal(np.column_stack(fib_cols + rot_cols), G)
    U_rot = g_orthonormal(np.column_stack(rot_cols), G)
    U_fib = g_orthonormal(np.column_stack(fib_cols), G)
    rows = []
    for i, l in enumerate(vals):
        if i in zero_idx or l.real < -1e-9 * scale or l.imag < -1e-9 * scale:
            continue                       # the zero cluster, and the non-representative members of each pair or quartet
        v = vecs[:, i]
        krein = float(np.real(np.vdot(v, Mu @ v)))
        mult = int(np.sum(np.abs(vals - l) <= 1e-7 * scale))
        rows.append((abs(l) / scale, l, krein, mult, overlap(v, U_full, G), overlap(v, U_rot, G), overlap(v, U_fib, G)))
    gap = sorted(np.abs(vals))
    return sorted(rows, key=lambda r: r[0]), (nzero, gap[nzero - 1] / scale if nzero else 0.0, gap[nzero] / scale)


def show(label, rows, nz):
    print(f'\n{label}: zero cluster {nz[0]} (largest zero-cluster |λ|/max {nz[1]:.1e}, smallest genuine {nz[2]:.4f})')
    for rel, l, kr, mult, of, orot, ofib in rows:
        kind = 'real' if abs(l.imag) <= 1e-9 * abs(l) else ('imag' if abs(l.real) <= 1e-9 * abs(l) else 'quartet')
        print(f'   |λ|/max {rel:8.4f}  {kind:7s} Krein {np.sign(kr):+.0f}  mult {mult}  overlap: full {of:.3f}, '
              f'rotations {orot:.3f}, fibre+partner {ofib:.3f}')


if __name__ == '__main__':
    for slot, q in (('R4', bc.Q4), ('R5', bc.Q5)):
        for name, rep, _v, _s, _k, _r, mz, _t in bc.R4_ROWS:
            tag = TARGETS.get(name) or CONTROLS.get(name) or ''
            rows, nz = survey(name, 6, q, bc.vec(6, rep), False, mz)
            show(f'{slot} {name}' + (f' [{tag}]' if tag else ''), rows, nz)
    for name, rep, _v, _s, _k, _r, mz, _t in bc.R2_ROWS:
        tag = TARGETS.get(name) or CONTROLS.get(name) or ''
        rows, nz = survey(name, 7, bc.Q2, bc.vec(7, rep), True, mz)
        show(f'R2 {name}' + (f' [{tag}]' if tag else ''), rows, nz)
    # validation only, against the review's published continuum figure: the third outside orbit (T4) in R4
    pt = [sp.Float(s, 60) for s in bc.OUTSIDE]
    rows, nz = survey('third outside orbit', 6, bc.Q4, pt, False, 6)
    show('R4 third outside orbit [T4, validation only]', rows, nz)
