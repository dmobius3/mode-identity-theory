"""The complete-level twisted harmonic basis of sections of E_rho (DESIGN.md section 3).

At level n the basis is f_{n,i,k}(x) = sqrt(n + 1) A_i pi_n(x) e_k, with A_i the canonical orthonormal
(Frobenius) basis of Hom_2I(V_n, W_rho) from group2i.intertwiners. By Schur orthogonality these are orthonormal in L^2(S^3) with the
normalized measure, and -Laplacian is n(n + 2) on level n. Equivariance: f(gamma x) = rho(gamma) f(x).
"""
import numpy as np
from . import su2, group2i


class Basis:
    def __init__(self, slot, N, E=None, gens=None):
        if slot not in group2i.SLOTS:         # never R0
            raise PermissionError(f'slot {slot!r} is refused: R0 never runs')
        self.slot, self.N = slot, N
        self.E = group2i.elements() if E is None else E
        self.gens = group2i.generators(self.E) if gens is None else gens
        self.r = group2i.dim(slot)
        self.levels, self.A, self.index = [], {}, []
        for n in range(N + 1):
            if group2i.multiplicity(n, slot, self.E) == 0:
                continue
            A, _ = group2i.intertwiners(n, slot, self.E)            # canonical (DESIGN.md section 3)
            self.levels.append(n)
            self.A[n] = A
            for i in range(len(A)):
                for k in range(n + 1):
                    self.index.append((n, i, k))
        self.m = len(self.index)
        self.eig = np.array([n * (n + 2) for n, _, _ in self.index], dtype=float)

    def evaluate(self, U):
        """Phi(x) for a stack of SU(2) points U (P, 2, 2): array (P, r, m)."""
        U = np.asarray(U)
        cols = []
        for n in self.levels:
            Pn = su2.pi(n, U)                            # (P, n+1, n+1)
            for A in self.A[n]:
                cols.append(np.sqrt(n + 1) * np.einsum('rl,plk->prk', A, Pn))
        return np.concatenate(cols, axis=2)

    def evaluate_at_t_node(self, rule, g, rows=None):
        """Phi on the rule's (alpha, beta) grid at the g-th t node: array (M, M, r, m); with rows = (u0, u1), only the
        alpha rows u0 <= u < u1, array (u1 - u0, M, r, m)."""
        phi = np.arccos(np.sqrt(rule.t[g]))
        al = rule.angles
        au = al if rows is None else al[rows[0]:rows[1]]
        cols = []
        for n in self.levels:
            d = su2.spin(n).d(phi)                       # (n+1, n+1), real
            l = np.arange(n + 1)
            # pi_n(x)_{lk} = e^{i alpha (n - l - k)} e^{i beta (l - k)} d_{lk}
            Ea = np.exp(1j * np.multiply.outer(au, n - l[:, None] - l[None, :]))      # (rows, l, k)
            Eb = np.exp(1j * np.multiply.outer(al, l[:, None] - l[None, :]))          # (M, l, k)
            for A in self.A[n]:
                # f[u, v, r, k] = sqrt(n+1) sum_l A[r, l] d[l, k] Ea[u, l, k] Eb[v, l, k]
                cols.append(np.sqrt(n + 1) * np.einsum('rl,lk,ulk,vlk->uvrk', A, d, Ea, Eb, optimize=True))
        return np.concatenate(cols, axis=3)
