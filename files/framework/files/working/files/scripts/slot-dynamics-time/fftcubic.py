"""The instrument's cubic and quartic energy, through two-dimensional FFTs on its rule's uniform angular nodes
(DESIGN.md section 7). New code: every result that uses it rests on new code.

The basis evaluates pi_n at a t node as pi_n(x)_{lk} = e^{i alpha (n - l - k)} e^{i beta (l - k)} d_{lk}(phi), with
d real (basis.py). So at each t node g, each fibre component r of psi on the M x M grid of (alpha, beta) is the
Fourier series with coefficients

    C_g[r; p, q] = sum_{n,i} sqrt(n+1) A_{n,i}[r, l] d^n_{lk}(phi_g) c_{n,i,k},  (l, k) = ((n-p+q)/2, (n-p-q)/2),

in the bins (p mod M, q mod M), alpha along axis 1 and beta along axis 2 of an (r, M, M) array. Within one level the map
(l, k) -> (p, q) is one to one and M > 2n, so no two of a level's terms share a bin; terms of different levels that
share a bin are summed. Then psi = M^2 ifft2(C_g); the density s = sum_r |psi_r|^2; F = s psi; its normalized
coefficients F_g = fft2(F) / M^2; and the projection G_{n,i,k} = sqrt(n+1) sum_g wt[g] sum_{r,l} conj(A_{n,i}[r, l])
d^n_{lk}(phi_g) F_g[r; n-l-k, l-k], with wt the rule's Gauss weights. The angular normalization 1/M^2 is applied once:
the dense path's node_weight(g) = wt[g] / M^2 already holds it. At M = 4N + 1 these are the dense path's own sums.

`mutation` plants one of the traps of DESIGN.md section 7, for control 1's arms only; None is the instrument. The
aliased grid is M = 4 max(levels), one point short of exactness for the levels present (DEVLOG entry 7). The missing
conjugation of A bites only where A is complex; the instrument's intertwiners are real, so control 1 plants it in a
basis whose intertwiners carry a complex phase per copy."""
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import pin  # noqa: E402

_INST = pin.instrument_path()
if _INST not in sys.path:
    sys.path.insert(0, _INST)
from instrument import quadrature, su2  # noqa: E402

MUTATIONS = (None, 'transform_sign', 'negative_frequency', 'overwritten_bin', 'unconjugated_A', 'doubled_normalization',
             'aliased_grid')


class FFTCubic:
    def __init__(self, B, M=None, mutation=None):
        assert mutation in MUTATIONS, mutation
        self.B, self.mutation = B, mutation
        if mutation == 'aliased_grid':
            M = 4 * max(B.levels)
        self.rule = quadrature.HopfRule(B.N, M=M)
        self.M, self.r, self.wt = self.rule.M, B.r, self.rule.wt
        phis = np.arccos(np.sqrt(self.rule.t))
        self.blocks, col = [], 0
        for n in B.levels:
            A = np.stack(B.A[n])                                    # (mult, r, n+1)
            mult = A.shape[0]
            l, k = np.arange(n + 1)[:, None], np.arange(n + 1)[None, :]
            p, q = n - l - k, l - k
            if mutation == 'negative_frequency':
                p = np.abs(p)
            P, Q = p % self.M, q % self.M
            d = np.stack([su2.spin(n).d(phi) for phi in phis])       # (n_t, n+1, n+1), real
            self.blocks.append((n, A, np.sqrt(n + 1), P, Q, slice(col, col + mult * (n + 1)), mult, d))
            col += mult * (n + 1)
        assert col == B.m

    def coefficients(self, c, g):
        X = np.zeros((self.r, self.M, self.M), dtype=complex)
        for n, A, s, P, Q, sl, mult, d in self.blocks:
            Y = s * np.einsum('irl,ik->rlk', A, c[sl].reshape(mult, n + 1)) * d[g][None]
            if self.mutation == 'overwritten_bin':
                X[:, P, Q] = Y
            else:
                X[:, P, Q] += Y
        return X

    def field(self, c, g):
        """psi on the rule's angular grid at the g-th t node: an (r, M, M) array, alpha along axis 1."""
        X = self.coefficients(c, g)
        if self.mutation == 'transform_sign':
            return np.fft.fft2(X, axes=(1, 2))
        return self.M ** 2 * np.fft.ifft2(X, axes=(1, 2))

    def cubic(self, c):
        """The Galerkin projection of |psi|^2 psi, as the instrument's Functional.cubic."""
        out = np.zeros(self.B.m, dtype=complex)
        for g in range(self.rule.n_t):
            psi = self.field(c, g)
            dens = np.sum(np.abs(psi) ** 2, axis=0)
            Fh = np.fft.fft2(dens[None] * psi, axes=(1, 2)) / self.M ** 2
            if self.mutation == 'doubled_normalization':
                Fh = Fh / self.M ** 2
            for n, A, s, P, Q, sl, mult, d in self.blocks:
                Ac = A if self.mutation == 'unconjugated_A' else A.conj()
                out[sl] += (s * self.wt[g] * np.einsum('irl,lk,rlk->ik', Ac, d[g], Fh[:, P, Q])).reshape(-1)
        return out

    def quartic(self, c):
        """V4 = (1/4) int |psi|^4 dmu, by the same rule: (1/4) sum_g wt[g] mean over the grid of s^2."""
        return 0.25 * sum(self.wt[g] * np.mean(np.sum(np.abs(self.field(c, g)) ** 2, axis=0) ** 2)
                          for g in range(self.rule.n_t))
