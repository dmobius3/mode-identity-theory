"""The rotating-frame linearization about a discrete standing wave e^{i w T} Phi:
(1/c^2) M (zeta'' + 2 i w zeta') + L zeta = 0, L = K - sigma M + g (A + B conj), in real form on x = (zeta, eta = zeta').
Slow eigenvalues by shift-invert; the Hessian L's negative index for the Krein count."""
import gc
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from nonlinear import real_form, real_form_anti, to_real, to_complex, arpack_v0


class Linearization:
    def __init__(self, st, Phi, sigma, c=1.0):
        A, B = st.q.jacobian(Phi)
        self.L = (st.Kr - sigma * st.Mr + st.g * (real_form(A) + real_form_anti(B))).tocsr()
        self.Mr = st.Mr
        n2 = self.L.shape[0]
        n = n2 // 2
        I = sps.identity(n, format='csr')
        self.J0 = sps.bmat([[None, -I], [I, None]], format='csr')
        self.omega = c * np.sqrt(sigma)
        self.c = c
        Z = sps.csr_matrix((n2, n2))
        I2 = sps.identity(n2, format='csr')
        self.Abig = sps.bmat([[Z, I2], [-c ** 2 * self.L, -2 * self.omega * (self.Mr @ self.J0)]], format='csc')
        self.Bbig = sps.bmat([[I2, Z], [Z, self.Mr]], format='csc')
        self.n2 = n2

    def slow_eigs(self, k, shift=0.004 + 0.003j):
        vals, vecs = spla.eigs(self.Abig, k=k, M=self.Bbig, sigma=shift, which='LM')
        order = np.argsort(abs(vals))
        vals, vecs = vals[order], vecs[:, order]
        res = np.array([np.linalg.norm(self.Abig @ vecs[:, i] - vals[i] * (self.Bbig @ vecs[:, i])) / np.linalg.norm(vecs[:, i])
                        for i in range(len(vals))])
        return vals, vecs, res

    def shift_invert(self, shift):
        """(Abig - s Bbig)^-1 through the 2n quadratic pencil Q(s) = c^2 L + 2 w s Mr J0 + s^2 Mr: with x = (zeta, eta),
        eta = y1 + s zeta and zeta = -Q(s)^-1 [y2 + (2 w Mr J0 + s Mr) y1]. Half the size of the first-order pencil."""
        c, w, s = self.c, self.omega, shift
        MJ = (self.Mr @ self.J0).tocsc()
        Q = (c ** 2 * self.L + (2 * w * s) * MJ + (s * s) * self.Mr).tocsc()
        dt = complex if np.iscomplexobj(s) and np.imag(s) != 0 else float
        Q = Q.astype(dt)
        lu = spla.splu(Q, permc_spec='MMD_AT_PLUS_A')        # the pattern is symmetric: 3x less fill than COLAMD
        n2 = self.n2
        G = (2 * w) * MJ + s * self.Mr
        def apply(y):
            y = np.asarray(y).ravel()
            y1, y2 = y[:n2], y[n2:]
            z = -lu.solve(np.asarray(y2 + G @ y1, dtype=dt))
            return np.concatenate([z, y1 + s * z])
        return spla.LinearOperator((2 * n2, 2 * n2), matvec=apply, dtype=dt)

    def slow_eigs_q(self, k, shift=0.004):
        """A real shift near 0 keeps the factorization real (half the memory); the slow eigenvalues are the nearest."""
        """Slow eigenvalues by shift-invert through the quadratic pencil; same contract as slow_eigs."""
        op = self.shift_invert(shift)
        kind = complex if op.dtype == complex else float
        vals, vecs = spla.eigs(self.Abig, k=k, M=self.Bbig, sigma=shift, OPinv=op, which='LM',
                               v0=arpack_v0(self.Abig.shape[0], kind))
        del op
        gc.collect()          # scipy's ARPACK wrapper holds the operator, and so the factorization, in a reference cycle
        order = np.argsort(abs(vals))
        vals, vecs = vals[order], vecs[:, order]
        res = np.array([np.linalg.norm(self.Abig @ vecs[:, i] - vals[i] * (self.Bbig @ vecs[:, i])) / np.linalg.norm(vecs[:, i])
                        for i in range(len(vals))])
        return vals, vecs, res

    def krein(self, vec):
        """Sign of the energy H2 on the real span of an eigenvector pair (positive: Krein +)."""
        z, e = vec[:self.n2], vec[self.n2:]
        H = (e.conj() @ (self.Mr @ e)) / self.c ** 2 + z.conj() @ (self.L @ z)
        return float(np.real(H))

    def hessian_negative_index(self, k=60, floor=0.0):
        """Eigenvalues of L relative to M (L v = theta M v) below the floor: the negative directions of the Hessian."""
        th = spla.eigsh(self.L, k=k, M=self.Mr, sigma=-1.0, which='LM', return_eigenvectors=False)
        th = np.sort(th.real)
        return th
