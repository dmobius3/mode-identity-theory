"""Pinned standing waves: the frozen cases (controls and targets), their orientation into the mesh's right 2I, the fixed
space of the pinned subgroup, and Newton inside it.

A case's representative u is given in Condon-Shortley components on the lowest level V_j; the solver's basis is the
same (index k = m + j). Its pinned subgroup is given by generators (Condon-Shortley axis, order). The orientation g0
carries the subgroup into right 2I: w = pi(g0^-1) u has isotropy g0^-1 H0 g0 inside 2I. On the mesh each h in it acts
on the seed as R_h Phi = (a_h + b_h J) Phi (b = 0 outside the quaternionic slot); the fixed space is
{Psi : (conj(a_h) - b_h J) R_h Psi = Psi for all h}, an exact symmetry of the discrete equations."""
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from math import factorial, sqrt
from irreps import sym, su2
from geometry import qmul, qconj
from standing import germ_seed, EPS
from nonlinear import real_form, real_form_anti, to_real, to_complex
from symmetry import RightAction, orient, to_quat_vec, subgroup_closure, Rotations

# --- the frozen cases -----------------------------------------------------------------------------------------------
CASES = {
    'C1':  dict(slot=3, j2=2, u={1: 1.0}, gens=[('z', 5)]),
    'C2a': dict(slot=4, j2=6, u={3: 1.0}, gens=[('z', 5)]),
    'C2b': dict(slot=2, j2=7, u={3.5: 1.0}, gens=[('z', 5)], quaternionic=True),
    # v2 + v-2 is z(x^2 - y^2): its octahedral 4-fold axes are z and the diagonals (1, +-1, 0), so T's 3-folds lie
    # along (0, sqrt2, 1)-type directions
    'C3':  dict(slot=4, j2=6, u={2: 1.0, -2: 1.0}, gens=[('z', 2), ((1, 1, 0), 2), ((0, sqrt(2), 1), 3)]),
    'T1':  dict(slot=(4, 5), j2=6, u={2: 1.0}, gens=[('z', 5)]),
    'T2':  dict(slot=(4, 5), j2=6, u={3: 1.0, 0: sqrt(23 / 10), -3: 1.0}, gens=[('z', 3), ('x', 2)]),
    'T3':  dict(slot=(4, 5), j2=6, u={3: 1.0, -3: 1.0}, gens=[('z', 3), ('x', 2)]),
    'T4':  dict(slot=(4, 5), j2=6, u='outside', gens=[('J', 2)], slice_axis='J'),
    # the line point's D5: the 5-fold about z with a phase, and 2-folds at 18 + 36k degrees in the xy-plane with J on
    # the fibre (checked in the continuum with the quaternionic structure); the y axis is one of them
    'T5':  dict(slot=2, j2=7, u={3.5: sqrt(3 / 10), -1.5: sqrt(7 / 10)}, gens=[('z', 5), ('y', 2)], quaternionic=True),
    # stand-ins, controls only: T4's path (a 2-fold pin with a slice) on C3, and T5's path (D5 with J) on C2b
    'C3s': dict(slot=4, j2=6, u={2: 1.0, -2: 1.0}, gens=[('z', 2)], slice_axis='z'),
    'C2b_D5': dict(slot=2, j2=7, u={3.5: 1.0}, gens=[('z', 5), ('y', 2)], quaternionic=True),
    # M8.15.x controls (memo v4): the pentagonal pyramid, sqrt(12) v3 + sqrt(13) v-2 (Condon-Shortley), non-target and
    # nondegenerate; its 5-fold about z fixes it up to a phase, and rotation about z is a continuous lifted direction
    'P5':  dict(slot=4, j2=6, u={3: sqrt(12 / 25), -2: sqrt(13 / 25)}, gens=[('z', 5)], slice_axis='z'),
    # control 1a (M8.15.x REGISTER_1.md): the pyramid rotated about z by theta0 = pi/10, the midpoint between its
    # symmetric critical angles 0 and pi/5, so that v-2 carries e^(5 i theta0) relative to v3; no angle solve
    'P5a': dict(slot=4, j2=6, u={3: sqrt(12 / 25), -2: sqrt(13 / 25) * np.exp(5j * np.pi / 10)}, gens=[('z', 5)],
                slice_axis='z'),
}


def cs_vector(j2, comps):
    v = np.zeros(j2 + 1, complex)
    for m, c in comps.items():
        k = int(round(m + j2 / 2))
        v[k] = c
    return v


def outside_point():
    """The third outside orbit's certified point, read from the landed check at the pinned commit, as Condon-Shortley
    components (p-coordinates in the order m = 3, 2, ..., -3, real then imaginary parts)."""
    import ast, os, subprocess
    src = ('d0de8ca61f8e166586731b6167ab895c09368630:files/framework/files/working/files/scripts/'
           'soft-slot-branches/branches_check.py')
    txt = subprocess.run(['git', '-C', os.path.dirname(os.path.abspath(__file__)), 'show', src], capture_output=True, text=True,
                         check=True).stdout
    i0 = txt.index('OUTSIDE = ['); i1 = txt.index(']', i0) + 1
    x = np.array([float(s) for s in ast.literal_eval(txt[i0 + len('OUTSIDE = '):i1])])
    p = x[:7] + 1j * x[7:]
    comps = {}
    for a in range(7):
        m = 3 - a
        comps[m] = sqrt(factorial(3 + m) * factorial(3 - m)) * p[a]
    return comps


def angular_momentum_axis(j2, w):
    from symmetry import spin_matrices
    Js = spin_matrices(j2)
    J = np.array([np.real(np.vdot(w, Jc @ w)) for Jc in Js]) / np.real(np.vdot(w, w))
    return J / np.linalg.norm(J), J


# --- the fibre maps a + b J -----------------------------------------------------------------------------------------
def Jmap(P):
    return (EPS @ P.reshape(-1, 2).T.conj()).T.ravel()


def fit_fibre(RPhi, Phi, quaternionic):
    """(a, b) with R_h Phi = a Phi + b J Phi; residual relative."""
    if not quaternionic:
        a = np.vdot(Phi, RPhi) / np.vdot(Phi, Phi)
        return a, 0.0, np.linalg.norm(RPhi - a * Phi) / np.linalg.norm(RPhi)
    JP = Jmap(Phi)
    A = np.column_stack([Phi, JP])
    coef, *_ = np.linalg.lstsq(A, RPhi, rcond=None)
    a, b = coef
    return a, b, np.linalg.norm(RPhi - A @ coef) / np.linalg.norm(RPhi)


def fibre_inverse_real(a, b, n):
    """Real 2n x 2n matrix of Psi -> (conj(a) - b J) Psi."""
    I = sps.identity(n, format='csr')
    Ar = real_form(np.conj(a) * I)
    if b == 0:
        return Ar
    # J as a real map: Psi -> EPS conj(Psi) per node
    nn = n // 2
    E = sps.kron(sps.identity(nn), sps.csr_matrix(EPS), format='csr')
    Jr = sps.bmat([[E, None], [None, -E]], format='csr')            # (Re, Im) -> (E Re, -E Im)
    bJ = real_form(b * I) @ Jr
    return (Ar - bJ).tocsr()


class PinnedCase:
    def __init__(self, mesh, Rs, name, slot=None, G=None):
        spec = dict(CASES[name])
        self.name, self.mesh = name, mesh
        self.slot = slot if slot is not None else spec['slot']
        self.j2 = spec['j2']
        self.quaternionic = spec.get('quaternionic', False)
        self.R = Rs[self.slot]
        G = mesh.G
        # representative
        comps = outside_point() if spec['u'] == 'outside' else spec['u']
        u = cs_vector(self.j2, comps)
        self.u = u / np.linalg.norm(u)
        gens = []
        for ax, order in spec['gens']:
            if ax == 'J':
                ax = angular_momentum_axis(self.j2, self.u)[0]
            elif isinstance(ax, str):
                ax = {'x': (1, 0, 0), 'y': (0, 1, 0), 'z': (0, 0, 1)}[ax]
            gens.append((np.asarray(ax, float) / np.linalg.norm(ax), order))
        self.gens_cs = gens
        # orientation from the first one or two generators with distinct axes
        axes, orders = [gens[0][0]], [gens[0][1]]
        if len(gens) > 1:
            axes.append(gens[1][0]); orders.append(gens[1][1])
        self.g0 = orient(G, axes, orders)
        self.w = sym(su2(qconj(self.g0)), self.j2) @ self.u
        # the pinned subgroup inside 2I
        self.RA = RightAction(mesh, self.R)
        idx = []
        for ax, order in gens:
            q0 = np.concatenate([[np.cos(np.pi / order)], np.sin(np.pi / order) * to_quat_vec(ax)])
            q = qmul(qmul(qconj(self.g0), q0), self.g0)
            idx.append(self.RA.index(q))
        self.H = subgroup_closure(mesh.mt, idx)
        # the seed and its fibre maps
        self.seed = germ_seed(mesh, self.R, self.j2, self.w, G)
        n = len(self.seed)
        self.fib = []
        worst = 0.0
        for h in self.H:
            a, b, r = fit_fibre(self.RA.matrix(h) @ self.seed, self.seed, self.quaternionic)
            worst = max(worst, r, abs(abs(a) ** 2 + abs(b) ** 2 - 1))
            self.fib.append((a, b))
        self.fibre_residual = worst
        if worst > 1e-6:
            raise ValueError(f'{name}: a pinned generator does not fix the representative (fit residual {worst:.1e})')
        # fixed-space projector (real) and its basis, block by block on the H-orbits of node orbits
        U = [fibre_inverse_real(a, b, n) @ real_form(self.RA.matrix(h)) for h, (a, b) in zip(self.H, self.fib)]
        self.P = (sum(U) / len(U)).tocsr()
        self.Br = self._basis(n)
        x0 = to_real(self.seed)
        self.seed_in_fixed = np.linalg.norm(self.P @ x0 - x0) / np.linalg.norm(x0)

    def _basis(self, n):
        from scipy.sparse.csgraph import connected_components
        d = self.R.shape[1]
        nob = self.mesh.n_orb
        C = self.P.tocoo()
        keep = abs(C.data) > 1e-13
        node = lambda r: (r % n) // d
        A = sps.csr_matrix((np.ones(keep.sum()), (node(C.row[keep]), node(C.col[keep]))), shape=(nob, nob))
        ncomp, lab = connected_components(A + sps.identity(nob), directed=False)
        order = np.argsort(lab, kind='stable')
        cols = []
        starts = np.searchsorted(lab[order], np.arange(ncomp))
        ends = np.append(starts[1:], nob)
        for c in range(ncomp):
            nodes = order[starts[c]:ends[c]]
            comp = (nodes[:, None] * d + np.arange(d)[None, :]).ravel()
            idx = np.concatenate([comp, comp + n])
            Pb = self.P[idx][:, idx].toarray()
            Uu, s, _ = np.linalg.svd(Pb)
            r = int((s > 0.5).sum())
            if r:
                blk = sps.csr_matrix((Uu[:, :r].ravel(), (np.repeat(idx, r), np.tile(np.arange(r), len(idx)))),
                                     shape=(2 * n, r))
                cols.append(blk)
        return sps.hstack(cols, format='csr')

    def orientation_report(self):
        chars = [np.round(a, 6) if b == 0 else (np.round(a, 6), np.round(b, 6)) for a, b in self.fib[:4]]
        return (f'{self.name} (R{self.slot}): |H| = {len(self.H)}, fixed-space dimension {self.Br.shape[1]} of '
                f'{2 * len(self.seed)} real; fibre maps fitted to {self.fibre_residual:.1e}; seed in the fixed space '
                f'to {self.seed_in_fixed:.1e}')


def solve_pinned(st, case, m, sigma0, slices=(), tol=1e-11, maxit=40, x0=None, verbose=False, xref=None):
    """Bordered Newton at fixed norm x^T M x = m, sigma unknown, inside the case's fixed space. Gauges for the exact
    continuous fibre symmetries that survive the pinning; optional slice vectors (with multipliers). xref, the
    reference of the gauges and the slices, is the starting point unless given (M8.15.x § 1b's carry)."""
    from standing import fibre_generators
    Br = case.Br
    Mr = st.Mr
    xs = case.P @ to_real(case.seed) if x0 is None else x0
    x = xs * np.sqrt(m / (xs @ (Mr @ xs)))
    xref = x.copy() if xref is None else np.asarray(xref, float)
    gens = fibre_generators(st.R.shape[1], case.quaternionic)
    T = []
    for gen in gens:
        t = to_real(gen(to_complex(xref)))
        Mt = Mr @ t
        if np.linalg.norm(Br.T @ Mt) > 1e-8 * np.linalg.norm(Mt):
            T.append(Mt)
    # each slice covector M s restricted to the fixed space Newton solves in (M8.15.x REGISTER_1.md, amendment of
    # 2026-10-08): B_r^T is unchanged, so the reduced problem is too; the part outside only set the full test's floor
    S = [Br @ (Br.T @ (Mr @ s)) for s in slices]
    ng, ns = len(T), len(S)
    mu, nu = np.zeros(ng), np.zeros(ns)
    sigma = sigma0
    for it in range(maxit):
        Phi = to_complex(x)
        Mx = Mr @ x
        F = st.Kr @ x - sigma * Mx + st.g * to_real(st.q.force(Phi)) + sum(mu[k] * T[k] for k in range(ng)) \
            + sum(nu[k] * S[k] for k in range(ns))
        c = np.array([x @ Mx - m] + [T[k] @ x for k in range(ng)] + [S[k] @ (x - xref) for k in range(ns)])
        # convergence on the full bordered equation, every multiplier included (M8.15.x § 1a): with a slice the gauge
        # multipliers need not vanish (by phase invariance mu = -nu <p, s>_M / <p, p0>_M at a solution); a slice keeps
        # its multiplier, the residual force along the slice, recorded with the floors
        full = np.linalg.norm(F) / np.linalg.norm(Mx)
        res = full + abs(c[0]) / m
        if verbose:
            print(f'    it {it}: residual {res:.2e}, sigma {sigma:.12f}')
        if res < tol:
            return Phi, sigma, dict(it=it, res=res, full=full, mu=mu.copy(), nu=nu.copy())
        A, B = st.q.jacobian(Phi)
        J = st.Kr - sigma * Mr + st.g * (real_form(A) + real_form_anti(B))
        Jf = (Br.T @ (J @ Br)).tocsc()
        cols = [Br.T @ (-Mx)] + [Br.T @ t for t in T] + [Br.T @ s for s in S]
        top = sps.hstack([Jf] + [sps.csr_matrix(cc[:, None]) for cc in cols])
        rowv = [Br.T @ (2 * Mx)] + [Br.T @ t for t in T] + [Br.T @ s for s in S]
        nb = 1 + ng + ns
        rows = [sps.csr_matrix(np.concatenate([r, np.zeros(nb)])[None, :]) for r in rowv]
        Big = sps.vstack([top] + rows, format='csc')
        rhs = -np.concatenate([Br.T @ F, c])
        dz = spla.spsolve(Big, rhs)
        p = Br.shape[1]
        x = x + Br @ dz[:p]
        sigma += dz[p]
        mu += dz[p + 1:p + 1 + ng]
        nu += dz[p + 1 + ng:]
    raise RuntimeError(f'pinned Newton did not converge: residual {res:.2e}')


def rigid_pair(case, mesh, G):
    """C1 only: the interpolants of the rigid family's two non-symmetry tangent directions at v = |1, 1>, i.e.
    C |1, -1>, oriented like the representative. Real (2n x 2)."""
    assert case.name == 'C1'
    dv = sym(su2(qconj(case.g0)), case.j2) @ cs_vector(case.j2, {-1: 1.0})
    a = germ_seed(mesh, case.R, case.j2, dv, G)
    b = germ_seed(mesh, case.R, case.j2, 1j * dv, G)
    return np.column_stack([to_real(a), to_real(b)])
