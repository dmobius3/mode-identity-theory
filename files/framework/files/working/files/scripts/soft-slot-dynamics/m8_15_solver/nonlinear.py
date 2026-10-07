"""The density quartic V4 = (1/4) int |psi|^4 on the P2 space, by quadrature on the representative elements, with its
gradient (the force g |psi|^2 psi in weak form) and its real-linear Jacobian. All quadratic forms carry the same dropped
factor 120 as the stiffness and mass matrices."""
import numpy as np
import scipy.sparse as sps


class Quartic:
    def __init__(self, mesh, R):
        self.mesh, self.R, self.d = mesh, R, R.shape[1]
        self.Rn = R[mesh.gidx]                                     # (nT, 10, d, d): node value = Rn @ Psi[orbit]
        self.N = np.array([q[0] for q in mesh.qdata])              # (nq, 10)
        self.W = np.stack([q[1] for q in mesh.qdata], 1)           # (nT, nq)
        self.n = mesh.n_orb * self.d

    def at_quad(self, Psi):
        U = np.einsum('tiab,tib->tia', self.Rn, Psi.reshape(-1, self.d)[self.mesh.orbit])
        return np.einsum('qi,tia->tqa', self.N, U, optimize=True)   # (nT, nq, d)

    def energy(self, Psi):
        ph = self.at_quad(Psi)
        r2 = np.einsum('tqa,tqa->tq', ph.conj(), ph).real
        return 0.25 * float((self.W * r2 ** 2).sum())

    def _scatter(self, fq):
        fn = np.einsum('qi,tqa->tia', self.N, fq, optimize=True)
        fo = np.einsum('tiba,tib->tia', self.Rn.conj(), fn)
        out = np.zeros((self.mesh.n_orb, self.d), complex)
        np.add.at(out, self.mesh.orbit, fo)
        return out.ravel()

    def force(self, Psi):
        """The complex gradient: dV4 = Re <force, dPsi>."""
        ph = self.at_quad(Psi)
        r2 = np.einsum('tqa,tqa->tq', ph.conj(), ph).real
        return self._scatter((self.W * r2)[..., None] * ph)

    def jacobian(self, Psi):
        """D force[delta] = A delta + B conj(delta), returned as sparse complex A (Hermitian) and B (symmetric)."""
        d, m = self.d, self.mesh
        ph = self.at_quad(Psi)
        r2 = np.einsum('tqa,tqa->tq', ph.conj(), ph).real
        Aq = self.W[..., None, None] * (r2[..., None, None] * np.eye(d) + ph[..., :, None] * ph[..., None, :].conj())
        Bq = self.W[..., None, None] * (ph[..., :, None] * ph[..., None, :])
        # element blocks: sum_q N_i N_j Rn_i^dagger Aq Rn_j  (and Rn_i^dagger Bq conj(Rn_j) for the antilinear part)
        NN = np.einsum('qi,qj->qij', self.N, self.N)
        nq = NN.shape[0]
        NNf = NN.reshape(nq, -1)
        nT_, d_ = Aq.shape[0], Aq.shape[-1]
        Ae = np.einsum('qk,tqm->tkm', NNf, Aq.reshape(nT_, nq, -1), optimize=True).reshape(nT_, 10, 10, d_, d_)
        Be = np.einsum('qk,tqm->tkm', NNf, Bq.reshape(nT_, nq, -1), optimize=True).reshape(nT_, 10, 10, d_, d_)
        RA = np.einsum('tica,tijcd,tjdb->tijab', self.Rn.conj(), Ae, self.Rn, optimize=True)
        RB = np.einsum('tica,tijcd,tjdb->tijab', self.Rn.conj(), Be, self.Rn.conj(), optimize=True)
        nT = len(m.T)
        rows = np.broadcast_to((m.orbit[:, :, None, None, None] * d + np.arange(d)[None, None, None, :, None]), (nT, 10, 10, d, d)).ravel()
        cols = np.broadcast_to((m.orbit[:, None, :, None, None] * d + np.arange(d)[None, None, None, None, :]), (nT, 10, 10, d, d)).ravel()
        A = sps.csr_matrix((RA.ravel(), (rows, cols)), shape=(self.n, self.n))
        B = sps.csr_matrix((RB.ravel(), (rows, cols)), shape=(self.n, self.n))
        return A, B


def real_form(C):
    """Real 2n x 2n matrix of the complex-linear map C on (Re, Im)."""
    return sps.bmat([[C.real, -C.imag], [C.imag, C.real]], format='csr')


def real_form_anti(B):
    """Real matrix of the antilinear map delta -> B conj(delta)."""
    return sps.bmat([[B.real, B.imag], [B.imag, -B.real]], format='csr')


def arpack_v0(n, kind=float):
    """The frozen ARPACK starting vector: a fixed-seed draw, so the solver is deterministic under the frozen
    environment (ARPACK's default start is random)."""
    rng = np.random.default_rng(271828)
    v = rng.standard_normal(n)
    if kind is complex:
        v = v + 1j * rng.standard_normal(n)
    return v / np.linalg.norm(v)


def to_real(z):
    return np.concatenate([z.real, z.imag])


def to_complex(x):
    n = len(x) // 2
    return x[:n] + 1j * x[n:]
