"""Exact-geometry P2 finite elements on S^3 (radius 1) for rho-equivariant sections, psi(g x) = rho(g) psi(x).

Each element is a flat tetrahedron of R^4 with vertices on S^3, mapped onto S^3 by radial projection; the metric is
evaluated exactly at the quadrature points. Only one representative element per 2I-orbit is integrated; the global
quadratic forms are 120 times their sum, a factor dropped throughout. The unknowns are the values at one canonical
point per node orbit, d = dim(rho) complex components each."""
import numpy as np
import scipy.sparse as sps
from geometry import representatives, p2_nodes, orbit_ids, binary_icosahedral, group_tables

EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
DL = np.array([[-1.0, -1.0, -1.0], [1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]])


def tet_quadrature(n, symmetric=True):
    """Collapsed Gauss-Legendre rule on the reference tetrahedron; averaged over the 24 permutations of the
    barycentric coordinates when symmetric, so the rule commutes with every symmetry of the element."""
    x, w = np.polynomial.legendre.leggauss(n)
    x, w = (x + 1) / 2, w / 2
    P, W = [], []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                u, v, s = x[i], x[j], x[k]
                P.append((u, (1 - u) * v, (1 - u) * (1 - v) * s))
                W.append(w[i] * w[j] * w[k] * (1 - u) ** 2 * (1 - v))
    P, W = np.array(P), np.array(W)
    if not symmetric:
        return P, W
    import itertools
    L = np.column_stack([1 - P.sum(1), P])
    PS, WS = [], []
    for perm in itertools.permutations(range(4)):
        Lp = L[:, perm]
        PS.append(Lp[:, 1:])
        WS.append(W / 24)
    return np.concatenate(PS), np.concatenate(WS)


def p2_shape(xi):
    L = np.array([1 - xi[0] - xi[1] - xi[2], xi[0], xi[1], xi[2]])
    N = [L[a] * (2 * L[a] - 1) for a in range(4)] + [4 * L[i] * L[j] for i, j in EDGES]
    dN = [(4 * L[a] - 1) * DL[a] for a in range(4)] + [4 * (L[i] * DL[j] + L[j] * DL[i]) for i, j in EDGES]
    return L, np.array(N), np.array(dN)


class Mesh:
    def __init__(self, level, nq=4, rule='sym', symmetric=True):
        self.G = binary_icosahedral()
        self.mt, self.inv = group_tables(self.G)
        self.T = representatives(level, self.G, rule)              # (nT, 4, 4)
        nodes = np.concatenate([p2_nodes(t) for t in self.T])       # (nT*10, 4)
        oid, h, keys = orbit_ids(nodes, self.G)
        self.orbit = oid.reshape(-1, 10)                           # orbit index of each element node
        self.gidx = self.inv[h].reshape(-1, 10)                    # node = G[gidx] * canonical point
        self.canon = keys                                          # canonical point of each orbit
        self.n_orb = len(keys)
        self.level = level
        self.quad = tet_quadrature(nq, symmetric)
        self._element_matrices()

    def _element_matrices(self):
        X = self.T
        nT = len(X)
        D = np.stack([X[:, 1] - X[:, 0], X[:, 2] - X[:, 0], X[:, 3] - X[:, 0]], -1)   # (nT, 4, 3)
        Ke = np.zeros((nT, 10, 10))
        Me = np.zeros((nT, 10, 10))
        vol = np.zeros(nT)
        P, W = self.quad
        self.qdata = []
        for xi, w in zip(P, W):
            L, N, dN = p2_shape(xi)
            y = np.einsum('a,tac->tc', L, X)
            ny = np.linalg.norm(y, axis=1)
            x = y / ny[:, None]
            Pm = np.eye(4)[None] - x[:, :, None] * x[:, None, :]
            J = np.einsum('tij,tjk->tik', Pm, D) / ny[:, None, None]
            Gm = np.einsum('tki,tkj->tij', J, J)
            det = np.linalg.det(Gm)
            Gi = np.linalg.inv(Gm)
            s = w * np.sqrt(det)
            Ke += s[:, None, None] * np.einsum('ik,tkl,jl->tij', dN, Gi, dN)
            Me += s[:, None, None] * np.outer(N, N)[None]
            vol += s
            self.qdata.append((N, s, x))
        self.Ke, self.Me, self.vol = Ke, Me, vol

    def assemble(self, R):
        """Reduced stiffness and mass for the representation R (120, d, d)."""
        d = R.shape[1]
        Rn = R[self.gidx]                                           # (nT, 10, d, d)
        B = np.einsum('tiab,tjac->tijbc', Rn.conj(), Rn)            # R_i^dagger R_j
        nT = len(self.T)
        rows = (self.orbit[:, :, None, None, None] * d + np.arange(d)[None, None, None, :, None])
        cols = (self.orbit[:, None, :, None, None] * d + np.arange(d)[None, None, None, None, :])
        rows = np.broadcast_to(rows, (nT, 10, 10, d, d)).ravel()
        cols = np.broadcast_to(cols, (nT, 10, 10, d, d)).ravel()
        n = self.n_orb * d
        K = sps.csr_matrix(((self.Ke[:, :, :, None, None] * B).ravel(), (rows, cols)), shape=(n, n))
        M = sps.csr_matrix(((self.Me[:, :, :, None, None] * B).ravel(), (rows, cols)), shape=(n, n))
        return K, M
