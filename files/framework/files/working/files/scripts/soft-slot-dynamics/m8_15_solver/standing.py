"""Standing waves e^{i w T} Phi of the discrete slot equation (1/c^2) M Psi'' + K Psi + g force(Psi) = 0:
(K - sigma M) Phi + g force(Phi) = 0 with sigma = w^2/c^2, at fixed charge-like norm Phi^dagger M Phi = m.
Newton on the real form, bordered by the norm constraint and by gauge constraints for the exact continuous fibre
symmetries (the phase; in the quaternionic slot also J and iJ), each with a Lagrange multiplier that vanishes at a solution."""
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from nonlinear import Quartic, real_form, real_form_anti, to_real, to_complex
from irreps import sym, su2

EPS = np.array([[0.0, 1.0], [-1.0, 0.0]])


def fibre_generators(d, quaternionic):
    """Maps Psi -> generator(Psi) for the exact continuous fibre symmetries, as functions on the flat complex vector."""
    gens = [lambda P: 1j * P]
    if quaternionic:
        assert d == 2
        Jq = lambda P: (EPS @ P.reshape(-1, 2).T.conj()).T.ravel()
        gens += [Jq, lambda P: 1j * Jq(P)]
    return gens


def intertwiner(R, j2, G, seed=0):
    """T in Hom_2I(V_{j2/2}, rho): T pi(g) = rho(g) T, by averaging."""
    rng = np.random.default_rng(seed)
    d = R.shape[1]
    A = rng.normal(size=(d, j2 + 1)) + 1j * rng.normal(size=(d, j2 + 1))
    T = sum(R[i] @ A @ sym(su2(g), j2).conj().T for i, g in enumerate(G)) / 120
    return T / np.linalg.norm(T)


def germ_seed(mesh, R, j2, w, G):
    """Nodal values of the lowest-level section psi_w(x) = T pi(x) w at the canonical point of each node orbit."""
    T = intertwiner(R, j2, G)
    vals = np.array([T @ sym(su2(x), j2) @ w for x in mesh.canon])
    return vals.ravel()


class Standing:
    def __init__(self, mesh, R, g=1.0, quaternionic=False):
        self.mesh, self.R, self.g = mesh, R, g
        self.K, self.M = mesh.assemble(R)
        self.Kr, self.Mr = real_form(self.K), real_form(self.M)
        self.q = Quartic(mesh, R)
        self.gens = fibre_generators(R.shape[1], quaternionic)

    def residual(self, Phi, sigma):
        return self.K @ Phi - sigma * (self.M @ Phi) + self.g * self.q.force(Phi)

    def solve(self, Phi0, m, sigma0, tol=1e-11, maxit=40, verbose=False):
        x = to_real(Phi0 * np.sqrt(m / np.real(np.vdot(Phi0, self.M @ Phi0))))
        sigma = sigma0
        T = [to_real(gen(to_complex(x))) for gen in self.gens]
        MT = [self.Mr @ t for t in T]
        ng = len(T)
        mu = np.zeros(ng)
        for it in range(maxit):
            Phi = to_complex(x)
            Mx = self.Mr @ x
            F = self.Kr @ x - sigma * Mx + self.g * to_real(self.q.force(Phi)) + sum(mu[k] * MT[k] for k in range(ng))
            c = [x @ Mx - m] + [MT[k] @ x for k in range(ng)]
            res = np.linalg.norm(F) / max(1.0, np.linalg.norm(Mx)) + abs(c[0]) / m
            if verbose:
                print(f'    it {it}: residual {res:.2e}, sigma {sigma:.10f}')
            if res < tol:
                return to_complex(x), sigma, dict(it=it, res=res, mu=mu.copy())
            A, B = self.q.jacobian(Phi)
            J = self.Kr - sigma * self.Mr + self.g * (real_form(A) + real_form_anti(B))
            cols = [sps.csr_matrix(-Mx[:, None])] + [sps.csr_matrix(MT[k][:, None]) for k in range(ng)]
            top = sps.hstack([J] + cols)
            rows = [sps.csr_matrix(np.concatenate([2 * Mx, np.zeros(1 + ng)])[None, :])]
            rows += [sps.csr_matrix(np.concatenate([MT[k], np.zeros(1 + ng)])[None, :]) for k in range(ng)]
            Big = sps.vstack([top] + rows, format='csc')
            rhs = -np.concatenate([F, c])
            dz = spla.spsolve(Big, rhs)
            x = x + dz[:len(x)]
            sigma = sigma + dz[len(x)]
            mu = mu + dz[len(x) + 1:]
        raise RuntimeError(f'Newton did not converge: residual {res:.2e}')


def lowest_level(st, n0, shift=-0.5):
    """The lowest n0 eigenvalues of (K, M), by shift-invert with a symmetric-pattern ordering (the default COLAMD
    fill is prohibitive at level 3). Returns sorted eigenvalues."""
    lu = spla.splu((st.K - shift * st.M).tocsc(), permc_spec='MMD_AT_PLUS_A')
    op = spla.LinearOperator(st.K.shape, matvec=lambda y: lu.solve(np.asarray(y, complex).ravel()), dtype=complex)
    from nonlinear import arpack_v0
    lam = spla.eigsh(st.K, k=n0 + 2, M=st.M, sigma=shift, OPinv=op, return_eigenvectors=False,
                     v0=arpack_v0(st.K.shape[0], complex))
    del op, lu
    import gc
    gc.collect()              # scipy's ARPACK wrapper holds the operator, and so the factorization, in a reference cycle
    return np.sort(lam.real)[:n0]
