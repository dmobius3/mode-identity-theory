"""The linear verdict at one point of a pinned branch, under the frozen rules.

Phase space: x = (zeta, eta = zeta') in real coordinates, each block 2n. The rotating-frame system
(1/c^2) Mr (zeta'' + 2 w J0 zeta') + L zeta = 0 is Hamiltonian for
    Omega(x1, x2) = (1/c^2) [zeta1^T Mr eta2 - eta1^T Mr zeta2 + 2 w zeta1^T Mr J0 zeta2],
with energy B = diag(L, Mr/c^2); on static vectors Omega = (2w/c^2) sigma(.,.) with sigma(a, b) = Re<a, i b>_M.

The tracked cluster G_tol, by structure:
  - the exact fibre vectors (i Phi; in R2 also J Phi, i J Phi), with the phase's Jordan partner
    ((2w/c^2) d_sigma Phi, i Phi), built explicitly;
  - the lifted right-rotation modes: slow eigenvectors whose static part has M-overlap >= 0.9 with the rotation span
    (span{X_a Phi} with the fibre directions projected out), with their Hamiltonian partners;
  - in C1, the rigid family's pair, by the same overlap with the interpolants of pi(x) dv.
Cluster checks: the frozen algebraic dimension k + r_u; closure under lambda -> -lambda, conj(lambda), -conj(lambda);
a nondegenerate Omega-Gram matrix (smallest singular value >= 1e-6 of the largest, in a phase-space M-orthonormal
basis). The Krein count k_r + 2 k_c + 2 k_i^- = n(B) - n(B|G_tol), with n(B) = n(L) by a complete spectrum slice."""
import gc
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from nonlinear import to_real, to_complex, arpack_v0
from standing import fibre_generators, germ_seed
from irreps import sym, su2
from geometry import qconj

OVERLAP = 0.9


class PhaseSpace:
    def __init__(self, lin):
        self.lin = lin
        self.Mr, self.L, self.J0 = lin.Mr, lin.L, lin.J0
        self.w, self.c, self.n2 = lin.omega, lin.c, lin.n2

    def split(self, X):
        return X[:self.n2], X[self.n2:]

    def Omega(self, X, Y):
        z1, e1 = self.split(X)
        z2, e2 = self.split(Y)
        Mr = self.Mr
        return (z1.T @ (Mr @ e2) - e1.T @ (Mr @ z2) + 2 * self.w * (z1.T @ (Mr @ (self.J0 @ z2)))) / self.c ** 2

    def B(self, X, Y):
        z1, e1 = self.split(X)
        z2, e2 = self.split(Y)
        return z1.T @ (self.L @ z2) + e1.T @ (self.Mr @ e2) / self.c ** 2

    def inner(self, X, Y):
        z1, e1 = self.split(X)
        z2, e2 = self.split(Y)
        return z1.T @ (self.Mr @ z2) + e1.T @ (self.Mr @ e2)


def real_orthonormal(V, Mr, rel=1e-6):
    """M-orthonormal real basis of span(V) (columns), dropping directions below rel of the largest singular value."""
    if V.shape[1] == 0:
        return V
    C = V.T @ (Mr @ V)
    C = (C + C.T) / 2
    ev, U = np.linalg.eigh(C)
    keep = ev > rel ** 2 * ev.max()
    return V @ (U[:, keep] / np.sqrt(ev[keep]))


def project_out(V, W, Mr):
    """Columns of V with their M-orthogonal components along the M-orthonormal columns W removed."""
    if W.shape[1] == 0:
        return V
    return V - W @ (W.T @ (Mr @ V))


def static_overlap(vec, Vb, Mr, n2):
    """M-overlap of the static part of a (complex) phase-space vector with the real M-orthonormal span Vb."""
    s = vec[:n2]
    if Vb.shape[1] == 0:
        return 0.0
    c = Vb.T @ (Mr @ s)
    ns = np.sqrt(abs(np.vdot(s, Mr @ s)))
    return float(np.sqrt(np.sum(abs(c) ** 2)) / ns) if ns > 0 else 0.0


def representatives(eigs, tau_re):
    """One representative per Hamiltonian pair or quartet: its member with Re >= 0 and Im >= 0, the signs read at the
    level's tau_Re as the classes are. An imaginary pair's computed real part is round-off of either sign (up to about
    1e-11 on the controls), so a fixed round-off margin can drop a whole pair; a real part beyond tau_Re keeps its sign.
    eigs: (lambda, Krein value) pairs."""
    return [(l, k) for l, k in eigs if l.real >= -tau_re and l.imag >= -tau_re]


def d_sigma_phi(st, case, Phi, sigma, slices=()):
    """d Phi / d sigma along the pinned branch: L chi = M Phi inside the fixed space, with the surviving gauges and the
    slices as constraints (Newton's bordering, without the norm row)."""
    from nonlinear import real_form, real_form_anti
    Br, Mr = case.Br, st.Mr
    A, Bq = st.q.jacobian(Phi)
    L = st.Kr - sigma * Mr + st.g * (real_form(A) + real_form_anti(Bq))
    x = to_real(Phi)
    cons = []
    for gen in fibre_generators(st.R.shape[1], case.quaternionic):
        t = Mr @ to_real(gen(Phi))
        if np.linalg.norm(Br.T @ t) > 1e-8 * np.linalg.norm(t):
            cons.append(t)
    cons += [Mr @ s for s in slices]
    Lf = (Br.T @ (L @ Br)).tocsc()
    nc = len(cons)
    top = sps.hstack([Lf] + [sps.csr_matrix((Br.T @ t)[:, None]) for t in cons])
    rows = [sps.csr_matrix(np.concatenate([Br.T @ t, np.zeros(nc)])[None, :]) for t in cons]
    Big = sps.vstack([top] + rows, format='csc')
    rhs = np.concatenate([Br.T @ (Mr @ x), np.zeros(nc)])
    sol = spla.spsolve(Big, rhs)
    return Br @ sol[:Br.shape[1]]


def negative_index_L(lin, lo, tol_zero, k0=40):
    """Number of eigenvalues of (L, Mr) below -tol_zero, by a complete slice of [lo - 1, tol]: shift-invert at the
    midpoint with k doubled until the k-th nearest eigenvalue lies outside the interval. Returns (count, eigenvalues
    found in the interval, near-zero eigenvalues)."""
    a, b = lo - 1.0, 1e-3
    mid = (a + b) / 2
    k = k0
    n = lin.L.shape[0]
    lu = spla.splu((lin.L - mid * lin.Mr).tocsc(), permc_spec='MMD_AT_PLUS_A')
    op = spla.LinearOperator(lin.L.shape, matvec=lambda y: lu.solve(np.asarray(y, float).ravel()), dtype=float)
    while True:
        k = min(k, n - 2)
        th = spla.eigsh(lin.L, k=k, M=lin.Mr, sigma=mid, which='LM', OPinv=op, return_eigenvectors=False,
                        v0=arpack_v0(n))
        th = np.sort(th.real)
        rad = np.max(abs(th - mid))
        if rad > max(mid - a, b - mid) * 1.01 or k >= n - 2:
            break
        k *= 2
    del op, lu
    gc.collect()              # scipy's ARPACK wrapper holds the operator, and so the factorization, in a reference cycle
    inside = th[(th >= a) & (th <= b)]
    neg = int((inside < -tol_zero).sum())
    nearzero = inside[abs(inside) <= max(tol_zero * 1e6, 1e-3)]
    return neg, inside, nearzero


class Verdict:
    def __init__(self, st, case, lin, Phi, sigma, lam0_min, rot, frozen_dim, rigid=None, slices=(), nslow=None,
                 tau0=None, tau_re=None, eps=None, kappa_tau_max=None):
        self.st, self.case, self.lin = st, case, lin
        self.ps = PhaseSpace(lin)
        Mr, n2 = lin.Mr, lin.n2
        self.n2 = n2
        w, c = lin.omega, lin.c
        x = to_real(Phi)
        # exact fibre vectors and the phase's Jordan partner
        gens = fibre_generators(st.R.shape[1], case.quaternionic)
        fib_static = np.column_stack([to_real(g(Phi)) for g in gens])
        chi = (2 * w / c ** 2) * d_sigma_phi(st, case, Phi, sigma, slices)
        zero = np.zeros(n2)
        F = [np.concatenate([fib_static[:, 0], zero]), np.concatenate([chi, fib_static[:, 0]])]
        for j in range(1, fib_static.shape[1]):
            F.append(np.concatenate([fib_static[:, j], zero]))
        self.F = np.column_stack(F)
        # the fibre part's static content: the exact generators and the phase partner's static part
        Fb = real_orthonormal(np.column_stack([fib_static, chi]), Mr)
        # rotation span with the fibre directions removed
        Xs = np.column_stack([to_real(v) for v in rot.all(Phi)])
        self.Rspan = real_orthonormal(project_out(Xs, Fb, Mr), Mr)
        self.Rig = np.zeros((n2, 0))
        if rigid is not None:
            self.Rig = real_orthonormal(project_out(project_out(rigid, Fb, Mr), self.Rspan, Mr), Mr)
        # the union of the structural spans: a degenerate cluster (C1's six zeros) comes back from the eigensolver in an
        # arbitrary basis, so membership is decided against the union, then each member is labelled where it can be
        self.U = real_orthonormal(np.column_stack([Fb, self.Rspan, self.Rig]), Mr)
        # slow eigenpairs
        nE0 = case.j2 + 1
        ns = nslow or 2 * nE0
        vals, vecs, res = lin.slow_eigs_q(k=ns + 4)
        nA = spla.norm(lin.Abig, 1)
        nB = spla.norm(lin.Bbig, 1)
        bwe = np.array([res[i] / (nA + abs(vals[i]) * nB) for i in range(len(vals))])
        self.vals, self.vecs, self.bwe = vals[:ns], vecs[:, :ns], bwe[:ns]
        self.gap = (abs(vals[ns - 1]), abs(vals[ns]) if len(vals) > ns else np.inf)
        # classify
        cls = []
        for i in range(ns):
            v = self.vecs[:, i]
            if static_overlap(v, self.U, Mr, n2) < OVERLAP:
                cls.append('genuine')
            elif static_overlap(v, Fb, Mr, n2) >= OVERLAP:
                cls.append('fibre')
            elif self.Rig.shape[1] and static_overlap(v, self.Rig, Mr, n2) >= OVERLAP:
                cls.append('rigid')
            else:
                cls.append('lifted')
        self.frozen_dim = frozen_dim
        self._assemble(np.array(cls))
        # n(L) by a complete slice; the lowest possible eigenvalue of L is lam0_min - sigma
        tolL = 1e-9 * max(1.0, abs(sigma - lam0_min))
        self.nL, self.L_inside, self.L_nearzero = negative_index_L(lin, lam0_min - sigma, tolL)
        # outside eigenvalues: every genuine slow eigenvalue with its Krein value, and the representatives at tau_Re
        self.tau0, self.tau_re = tau0, tau_re
        self.eps, self.kappa_tau_max = eps, kappa_tau_max
        if tau_re is None:
            raise ValueError("the representatives are read at the level's tau_Re: pass tau_re")
        self._genuine()

    def reclassify(self, cls):
        """The cluster and the genuine set rebuilt under another classification of the same slow eigenpairs (M8.15.x
        control 2a, REGISTER_2.md); the eigenpairs, n(L) and everything built before the classification stay."""
        self._assemble(np.asarray(cls))
        self._genuine()

    def _assemble(self, cls):
        self.cls = cls
        incl = self.cls != 'genuine'
        self.cluster_vals = self.vals[incl]
        # cluster checks
        self.dim = int(incl.sum())
        tolc = lambda lam: 1e-6 * abs(lam) + 1e-7
        cv = self.cluster_vals
        closed = all(min(abs(cv - t)) <= tolc(l) for l in cv for t in (-l, np.conj(l), -np.conj(l)))
        self.closed = closed
        # real basis of the cluster: explicit fibre part + Re/Im of the lifted/rigid eigenvectors
        lif = self.vecs[:, incl & (self.cls != 'fibre')]
        cols = [self.F] + ([np.real(lif), np.imag(lif)] if lif.shape[1] else [])
        Gc = np.column_stack(cols)
        # orthonormalize in the phase-space inner product
        C = self.ps.inner(Gc, Gc)
        C = (C + C.T) / 2
        ev, U = np.linalg.eigh(C)
        keep = ev > 1e-12 * ev.max()
        self.G = Gc @ (U[:, keep] / np.sqrt(ev[keep]))
        W = self.ps.Omega(self.G, self.G)
        sv = np.linalg.svd(W, compute_uv=False)
        self.omega_gram = (sv.min() / sv.max()) if len(sv) else 0.0
        self.basis_dim = self.G.shape[1]
        # B on the cluster
        Bg = self.ps.B(self.G, self.G)
        Bg = (Bg + Bg.T) / 2
        eb = np.linalg.eigvalsh(Bg)
        tolB = 1e-9 * max(1.0, abs(eb).max())
        self.nB_cluster = int((eb < -tolB).sum())
        self.B_cluster_eigs = eb

    def _genuine(self):
        lin, Mr, n2, c = self.lin, self.lin.Mr, self.n2, self.lin.c
        gv = self.vals[self.cls == 'genuine']
        gvec = self.vecs[:, self.cls == 'genuine']
        self.genuine_all = []
        for lam, v in zip(gv, gvec.T):
            kre = float(np.real(np.vdot(v, np.concatenate([lin.L @ v[:n2], (Mr @ v[n2:]) / c ** 2]))))
            self.genuine_all.append((lam, kre))
        self.genuine = representatives(self.genuine_all, self.tau_re)

    def fast_search(self, omega, tau_re, k=24):
        """The frozen fast-spectrum grid: shifts i j w/20, j = 0..40, and the same shifted off the axis by w/40; the k
        eigenvalues nearest each shift are kept when their backward errors pass. Returns representatives with Krein
        signs, outside the slow set."""
        lin, n2, Mr, c = self.lin, self.n2, self.lin.Mr, self.lin.c
        nA = spla.norm(lin.Abig, 1); nB = spla.norm(lin.Bbig, 1)
        slow_max = float(np.max(np.abs(self.vals)))
        found = []
        for off in (0.0, omega / 40):
            for j in range(41):
                s = off + 1j * j * omega / 20
                if abs(s) < 1e-12:
                    s = 1e-3
                op = lin.shift_invert(s)
                vals, vecs = spla.eigs(lin.Abig.astype(complex), k=k, M=lin.Bbig.astype(complex), sigma=s, OPinv=op,
                                       which='LM', v0=arpack_v0(lin.Abig.shape[0], complex))
                for i, lam in enumerate(vals):
                    x = vecs[:, i]
                    r = np.linalg.norm(lin.Abig @ x - lam * (lin.Bbig @ x)) / np.linalg.norm(x)
                    if r / (nA + abs(lam) * nB) > 1e-10:
                        continue
                    if lam.real < -tau_re or lam.imag < -tau_re:
                        continue
                    # the slow set is the ns eigenvalues of smallest modulus, so anything within its modulus range is a
                    # re-find (a defective or far-from-shift eigenvalue can come back ~1e-7 away); the search counts
                    # only what lies beyond it, de-duplicated at 1e-6 relative
                    if abs(lam) <= slow_max * (1 + 1e-6):
                        continue
                    if any(abs(lam - l) <= 1e-6 * max(1, abs(l)) for l, _ in found):
                        continue
                    kre = float(np.real(np.vdot(x, np.concatenate([lin.L @ x[:n2], (Mr @ x[n2:]) / c ** 2]))))
                    found.append((lam, kre))
                # scipy's ARPACK wrapper holds the operator, and so this shift's factorization, in a reference cycle:
                # without the collection each shift's factorization stays alive (about 4 GB apiece at level 3)
                del op, vals, vecs
                gc.collect()
        return found

    def slow_basis(self):
        """A real, phase-space orthonormal basis of the whole slow spectral subspace: the cluster's explicit basis plus
        the real and imaginary parts of the genuine slow eigenvectors."""
        gen = self.vecs[:, self.cls == 'genuine']
        cols = [self.G] + ([np.real(gen), np.imag(gen)] if gen.shape[1] else [])
        Sc = np.column_stack(cols)
        C = self.ps.inner(Sc, Sc)
        C = (C + C.T) / 2
        ev, U = np.linalg.eigh(C)
        keep = ev > 1e-12 * ev.max()
        return Sc @ (U[:, keep] / np.sqrt(ev[keep]))

    def lifted_moduli(self):
        return np.abs(self.vals[(self.cls == 'lifted') | (self.cls == 'rigid')])

    def count(self, tau_re):
        """k_r, k_c, k_i^- from the genuine slow eigenvalues; the identity's right side n(L) - n(B|G)."""
        kr = kc = kim = 0
        for lam, kre in self.genuine:
            if lam.real > tau_re and abs(lam.imag) <= tau_re:
                kr += 1
            elif lam.real > tau_re:
                kc += 1
            elif kre < 0:
                kim += 1
        return kr, kc, kim, self.nL - self.nB_cluster

    def report(self, tau_re=None):
        lines = []
        lm = self.lifted_moduli()
        lv = self.vals[(self.cls == 'lifted') | (self.cls == 'rigid')]
        rmax = float(np.max(abs(lv.real))) if len(lv) else 0.0
        lines.append(f'cluster: dim {self.dim} (frozen {self.frozen_dim}), basis {self.basis_dim}, closed {self.closed}, '
                     f'Omega-Gram {self.omega_gram:.1e}; lifted |lambda| {np.round(np.sort(lm), 9)}, max |Re| {rmax:.2e}; '
                     f'max backward error {self.bwe.max():.1e}; slow gap {self.gap[0]:.2e} | {self.gap[1]:.2e}')
        if tau_re is not None:
            kr, kc, kim, rhs = self.count(tau_re)
            lines.append(f'Krein: k_r {kr}, k_c {kc}, k_i- {kim} -> {kr + 2 * kc + 2 * kim}; n(L) {self.nL} - n(B|G) '
                         f'{self.nB_cluster} = {rhs}: {"balanced" if kr + 2 * kc + 2 * kim == rhs else "UNBALANCED"}')
        g = sorted(self.genuine, key=lambda t: abs(t[0]))
        lines.append('genuine: ' + ', '.join(f'{l.real:+.3e}{l.imag:+.6e}j({"+" if k > 0 else "-"})' for l, k in g))
        return lines
