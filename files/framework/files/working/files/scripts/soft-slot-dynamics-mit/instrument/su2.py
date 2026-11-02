"""SU(2) and its spin representations, in DESIGN.md's conventions (section 3).

A unit quaternion q = q0 + q1 i + q2 j + q3 k maps to U(q) = q0 I - i (q1 sx + q2 sy + q3 sz), a
homomorphism onto SU(2). A point of S^3 is U = [[a, -conj(b)], [b, conj(a)]], |a|^2 + |b|^2 = 1.

V_n = Sym^n(C^2) has the orthonormal basis e_l = xi1^(n-l) xi2^l / sqrt(l! (n-l)!), l = 0..n, and
pi_n(U) p(xi) = p(U^T xi) is unitary. Its generators are exact tridiagonal matrices (gen_matrix).
pi_n is evaluated through the factorization U = D(u) R(phi) D(v), with D(w) = diag(e^{iw}, e^{-iw})
and R(phi) = exp(phi (-i sy)), so pi_n(U) = P_n(u) d_n(phi) P_n(v): P_n(w) = diag(e^{i w (n - 2l)})
and d_n(phi) = exp(phi G_n), G_n = gen_matrix(n, -i sy), real antisymmetric, computed through the
eigendecomposition of the Hermitian i G_n (stable at every n used).
"""
import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
GENS = (-1j * SX, -1j * SY, -1j * SZ)          # unit-speed right-translation generators on S^3


def quat_to_su2(q):
    q = np.asarray(q, dtype=float)
    a = q[..., 0] - 1j * q[..., 3]
    b = q[..., 2] - 1j * q[..., 1]
    U = np.empty(q.shape[:-1] + (2, 2), dtype=complex)
    U[..., 0, 0], U[..., 0, 1], U[..., 1, 0], U[..., 1, 1] = a, -np.conj(b), b, np.conj(a)
    return U


def gen_matrix(n, X):
    """d pi_n(X) on the basis e_l, exactly: (d pi(X) p)(xi) = grad p(xi) . (X^T xi)."""
    G = np.zeros((n + 1, n + 1), dtype=complex)
    for l in range(n + 1):
        G[l, l] = (n - l) * X[0, 0] + l * X[1, 1]
        if l + 1 <= n:
            G[l + 1, l] = np.sqrt((n - l) * (l + 1)) * X[1, 0]
        if l - 1 >= 0:
            G[l - 1, l] = np.sqrt(l * (n - l + 1)) * X[0, 1]
    return G


class SpinRep:
    """pi_n, with its d_n(phi) factor precomputed from the eigendecomposition of i G_n."""

    def __init__(self, n):
        self.n = n
        G = gen_matrix(n, -1j * SY)
        assert np.allclose(G.imag, 0) and np.allclose(G.real, -G.real.T)
        w, V = np.linalg.eigh(1j * G)                  # i G Hermitian; G = -i V diag(w) V^H
        self.w, self.V = w, V
        self.weights = n - 2 * np.arange(n + 1)        # P_n(w) = diag(exp(i w * weights))

    def d(self, phi):
        """d_n(phi) = exp(phi G_n), real orthogonal; phi may be an array (returns stacked)."""
        phi = np.asarray(phi, dtype=float)
        E = np.exp(-1j * np.multiply.outer(phi, self.w))
        M = np.einsum('ij,...j,kj->...ik', self.V, E, self.V.conj())
        return M.real

    def __call__(self, U):
        """pi_n(U) for one U or a stack of them."""
        U = np.asarray(U)
        a, b = U[..., 0, 0], U[..., 1, 0]
        t = np.clip(np.abs(a) ** 2, 0.0, 1.0)
        phi = np.arccos(np.sqrt(t))
        al = np.where(np.abs(a) > 0, np.angle(a), 0.0)
        be = np.where(np.abs(b) > 0, np.angle(b), 0.0)
        u, v = (al - be) / 2, (al + be) / 2
        Pu = np.exp(1j * np.multiply.outer(u, self.weights))
        Pv = np.exp(1j * np.multiply.outer(v, self.weights))
        return Pu[..., :, None] * self.d(phi) * Pv[..., None, :]


_REPS = {}


def spin(n):
    if n not in _REPS:
        _REPS[n] = SpinRep(n)
    return _REPS[n]


def pi(n, U):
    return spin(n)(U)


def chi(n, theta):
    """Character of V_n at rotation angle theta (U conjugate to diag(e^{i theta/2}, e^{-i theta/2}))."""
    theta = np.asarray(theta, dtype=float)
    s = np.sin(theta / 2)
    out = np.empty_like(theta)
    small = np.abs(s) < 1e-12
    out[~small] = np.sin((n + 1) * theta[~small] / 2) / s[~small]
    out[small] = (n + 1) * np.sign(np.cos(theta[small] / 2)) ** n
    return out
