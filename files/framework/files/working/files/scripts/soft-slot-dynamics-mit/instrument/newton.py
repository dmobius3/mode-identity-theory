"""Newton on (c, lam) at fixed ||c||^2, with optional slice borders (DESIGN.md section 6, UB's c2 and c3).

The equations are G(c, lam) = F'_lam(c) - h + sum_j mu_j t_j = 0, ||c||^2 - m* = 0, and, when bordered,
<t_j, c - c_slice> = 0, in real form. The borders t_j are an orthonormal basis of the orbit tangents' span at the
slice point, with the span's rank read by a pivoted QR (so dependent tangents, as at a weight vector, give no
singular border). The spectrum is never read on this bordered system; it is read on the unbordered F''.
"""
import numpy as np
from scipy.linalg import qr
from . import functional as fn, devtools


def tangent_borders(tangent_vectors, rel_tol=1e-10):
    """An orthonormal basis of the span of the given real vectors, its rank by pivoted QR; returns (Q, rank, diag)."""
    T = np.column_stack(tangent_vectors)
    Q, R, piv = qr(T, mode='economic', pivoting=True)
    d = np.abs(np.diag(R))
    rank = int(np.sum(d > rel_tol * d[0])) if d.size and d[0] > 0 else 0
    return Q[:, :rank], rank, d


def solve(Fn, h, m_star, c0, lam0, borders=None, x_slice=None, maxit=40, stop=None, damping=1.0, hess=None,
          accept_rel=1e-15):
    """Newton from (c0, lam0). Returns (c, lam, mu, history of residual norms, accepted, info).

    The stop is read from the iteration (UB's c3): once the residual is below 1e-8 times the size of the
    equation's terms before they cancel, S = ||(-Laplacian) c|| + |lam| ||c|| + ||P(|psi|^2 psi)|| (+ ||h|| when
    forced), Newton keeps stepping while the residual at least halves, and returns the iterate with the smallest
    residual. The terms before they cancel, since lam's own rounding puts a branch's floor near ulp(lam) ||c|| / 2,
    which against the cancelled terms, about 2 eps ||c||, reads as about u lam/(4 eps) (UB).
    Acceptance is enforced here (UA, UB's (d)): the best iterate is accepted only if three things are below
    accept_rel times S, each relative to S: the floor (the bordered residual); the unbordered residual, the
    equation and the norm row without the multipliers' term; and the multipliers. So the halving rule's false floor
    on a linear iteration is refused, and so is a small bordered residual with nonzero multipliers. A fixed stop, if
    given, is a further test (D5's forced problems use 1e-12). info gives the floor, absolute and relative, the
    unbordered residual and the multipliers, both relative, and S.
    hess (for arms only) replaces the dense Jacobian block; damping < 1 only in D5's arm.
    """
    devtools.refuse_in_seedcheck('newton.solve')
    x = fn.to_real(c0)
    lam = float(lam0)
    hR = fn.to_real(h)
    k = 0 if borders is None else borders.shape[1]
    mu = np.zeros(k)
    hist, best, floor_mode = [], None, False
    for _ in range(maxit):
        c = fn.to_complex(x)
        cub = Fn.cubic(c)
        Gu = fn.to_real((Fn.e - lam) * c + cub) - hR
        G = Gu + (borders @ mu if k else 0.0)
        Nn = np.array([x @ x - m_star])
        S_ = borders.T @ (x - x_slice) if k else np.zeros(0)
        res = np.concatenate([G, Nn, S_])
        r = np.linalg.norm(res)
        size = np.linalg.norm(Fn.e * c) + abs(lam) * np.linalg.norm(c) + np.linalg.norm(cub) + np.linalg.norm(h)
        hist.append(r)
        if best is None or r < best[0]:
            best = (r, fn.to_complex(x.copy()), lam, mu.copy(), size, np.linalg.norm(np.concatenate([Gu, Nn])))
        if floor_mode and r > hist[-2] / 2:
            break                                                     # stopped halving: at the floor
        if r < 1e-8 * size:
            floor_mode = True
        H = Fn.hess_dense(c, lam) if hess is None else hess(c, lam)
        n2 = len(x)
        J = np.zeros((n2 + 1 + k, n2 + 1 + k))
        J[:n2, :n2] = H
        J[:n2, n2] = -x
        J[n2, :n2] = 2 * x
        if k:
            J[:n2, n2 + 1:] = borders
            J[n2 + 1:, :n2] = borders.T
        step = damping * np.linalg.solve(J, -res)
        x = x + step[:n2]
        lam = lam + step[n2]
        if k:
            mu = mu + step[n2 + 1:]
    r_best, c_best, lam_best, mu_best, size_best, ru_best = best
    info = dict(floor=r_best, floor_rel=r_best / size_best, unbordered_rel=ru_best / size_best,
                mu_rel=(np.linalg.norm(mu_best) / size_best) if k else 0.0, size=size_best)
    accepted = (floor_mode and info['floor_rel'] <= accept_rel and info['unbordered_rel'] <= accept_rel
                and info['mu_rel'] <= accept_rel and (stop is None or r_best < stop))
    return c_best, lam_best, mu_best, hist, accepted, info
