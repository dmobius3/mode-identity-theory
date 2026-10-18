"""The exact product rule on S^3 (DESIGN.md section 4), derived here.

Hopf coordinates a = sqrt(t) e^{i alpha}, b = sqrt(1 - t) e^{i beta}, with the normalized measure
dt d(alpha) d(beta) / (4 pi^2): M uniform nodes in each angle and n_t Gauss-Legendre nodes in t on [0, 1].
With M >= 4N + 1 and n_t = N + 1 it integrates every polynomial of degree <= 4N in (a, b, conj a, conj b)
exactly: the angles are exact for frequencies |k| <= 4N < M, and what survives is a polynomial in t of
degree <= 2N, which N + 1 Gauss nodes integrate exactly (degree 2N + 1).
"""
import numpy as np
from math import factorial


class HopfRule:
    def __init__(self, N, M=None, n_t=None):
        self.N = N
        self.M = 4 * N + 1 if M is None else M
        self.n_t = N + 1 if n_t is None else n_t
        x, w = np.polynomial.legendre.leggauss(self.n_t)
        self.t = (x + 1) / 2
        self.wt = w / 2                                # sums to 1 on [0, 1]
        self.angles = 2 * np.pi * np.arange(self.M) / self.M

    def angular_mean(self, k):
        """(1/M) sum over the uniform nodes of e^{i k angle}."""
        return np.mean(np.exp(1j * np.multiply.outer(np.atleast_1d(k), self.angles)), axis=-1)

    def t_moment(self, j):
        return np.sum(self.wt * self.t ** j)

    def monomial(self, p, q, r, s):
        """The rule's value of the monomial a^p conj(a)^q b^r conj(b)^s."""
        tpart = np.sum(self.wt * self.t ** ((p + q) / 2) * (1 - self.t) ** ((r + s) / 2))
        return tpart * self.angular_mean(p - q)[0] * self.angular_mean(r - s)[0]

    def points(self, g):
        """The (a, b) grid at the g-th t node: arrays (M, M) indexed [alpha, beta]."""
        al = self.angles[:, None]
        be = self.angles[None, :]
        a = np.sqrt(self.t[g]) * np.exp(1j * al) * np.ones_like(be)
        b = np.sqrt(1 - self.t[g]) * np.exp(1j * be) * np.ones_like(al)
        return a, b

    def node_weight(self, g):
        return self.wt[g] / self.M ** 2

    @property
    def size(self):
        return self.n_t * self.M ** 2


def exact_monomial(p, q, r, s):
    """The exact normalized-measure integral of a^p conj(a)^q b^r conj(b)^s over S^3."""
    if p != q or r != s:
        return 0.0
    return factorial(p) * factorial(r) / factorial(p + r + 1)
