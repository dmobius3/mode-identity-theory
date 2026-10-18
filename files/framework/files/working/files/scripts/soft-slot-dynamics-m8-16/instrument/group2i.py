"""The binary icosahedral group 2I and the eight nontrivial slot representations (DESIGN.md section 3).

2I is the 120 unit quaternions: the 8 of the form +-1, +-i, +-j, +-k; the 16 (+-1 +-i +-j +-k)/2; and the
96 even permutations of (0, +-1/2, +-1/(2 phi), +-phi/2). The Galois map sigma (sqrt5 -> -sqrt5) acts on
coordinates, phi/2 <-> -1/(2 phi) and 1/(2 phi) <-> -phi/2, and is multiplicative on these quaternions.

Slots, as in MIT's soft_quartic.py (McKay distances 1, 7, 2, 6, 6, 3, 4, 5 for R1..R8):
  R1 = V1, R3 = V2, R6 = V3, R7 = V4, R8 = V5 restricted to 2I;  R2 = 2' (V1 of sigma);
  R4 = 3' (V2 of sigma);  R5 = 4 = 2 (x) 2'.
The trivial slot R0 is not built here: nothing in M8.16 runs on it (BOUNDARY.md).
"""
import itertools
import numpy as np
from . import su2

PHI = (1 + 5 ** 0.5) / 2
SLOTS = ('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8')
SPINORIAL = ('R1', 'R2', 'R6', 'R8')            # rho(-1) = -1: quaternionic type, fibre group Sp(1)


def elements():
    els = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0] * 4
            v[i] = s
            els.append(v)
    for s in itertools.product((0.5, -0.5), repeat=4):
        els.append(list(s))
    base = (0.0, 0.5, 1 / (2 * PHI), PHI / 2)
    even = [p for p in itertools.permutations(range(4))
            if sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b]) % 2 == 0]
    for p in even:
        for s in itertools.product((1.0, -1.0), repeat=3):
            vals = (base[0], s[0] * base[1], s[1] * base[2], s[2] * base[3])
            v = [0.0] * 4
            for k in range(4):
                v[p[k]] = vals[k]
            els.append(v)
    E = np.unique(np.round(np.array(els), 14), axis=0)
    assert E.shape == (120, 4)
    return E


def qmul(p, q):
    p0, p1, p2, p3 = (p[..., k] for k in range(4))
    q0, q1, q2, q3 = (q[..., k] for k in range(4))
    return np.stack([p0 * q0 - p1 * q1 - p2 * q2 - p3 * q3,
                     p0 * q1 + p1 * q0 + p2 * q3 - p3 * q2,
                     p0 * q2 - p1 * q3 + p2 * q0 + p3 * q1,
                     p0 * q3 + p1 * q2 - p2 * q1 + p3 * q0], axis=-1)


def galois(q):
    q = np.array(q, dtype=float)
    out = q.copy()
    for a, b in ((PHI / 2, -1 / (2 * PHI)), (-PHI / 2, 1 / (2 * PHI)),
                 (1 / (2 * PHI), -PHI / 2), (-1 / (2 * PHI), PHI / 2)):
        out[np.isclose(q, a, atol=1e-12)] = b
    return out


def index_of(E, q):
    d = np.linalg.norm(E[None, :, :] - np.atleast_2d(q)[:, None, :], axis=-1)
    i = np.argmin(d, axis=1)
    assert np.all(d[np.arange(len(i)), i] < 1e-10)
    return i


def closure(E, gens):
    """Indices reached by words in gens (breadth first)."""
    seen = {0}
    ident = index_of(E, np.array([1.0, 0, 0, 0]))[0]
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for i in frontier:
            for g in gens:
                j = index_of(E, qmul(E[i], E[g]))[0]
                if j not in seen:
                    seen.add(j)
                    nxt.append(j)
        frontier = nxt
    return seen


def generators(E):
    """A deterministic generating pair: (1 + i + j + k)/2, then the first element that completes 2I."""
    g1 = index_of(E, np.array([0.5, 0.5, 0.5, 0.5]))[0]
    for g2 in range(len(E)):
        if g2 != g1 and len(closure(E, (g1, g2))) == 120:
            return g1, g2
    raise RuntimeError('no generating pair')


def rep(slot, q):
    """rho_slot(q) for a stack of quaternions q (..., 4)."""
    U = su2.quat_to_su2(q)
    Us = su2.quat_to_su2(galois(q))
    if slot == 'R1':
        return U
    if slot == 'R2':
        return Us
    if slot == 'R3':
        return su2.pi(2, U)
    if slot == 'R4':
        return su2.pi(2, Us)
    if slot == 'R5':
        return np.einsum('...ij,...kl->...ikjl', U, Us).reshape(q.shape[:-1] + (4, 4))
    if slot == 'R6':
        return su2.pi(3, U)
    if slot == 'R7':
        return su2.pi(4, U)
    if slot == 'R8':
        return su2.pi(5, U)
    raise ValueError(slot)


def dim(slot):
    return {'R1': 2, 'R2': 2, 'R3': 3, 'R4': 3, 'R5': 4, 'R6': 4, 'R7': 5, 'R8': 6}[slot]


def rotation_angle(E):
    return 2 * np.arccos(np.clip(E[:, 0], -1, 1))


def chi_formula(slot, E):
    """soft_quartic.py's character formulas, on 2I."""
    th = rotation_angle(E)
    tr = lambda n: su2.chi(n, th)
    tg = 2 * galois(E)[:, 0]
    return {'R1': tr(1), 'R2': tr(7) - tr(5), 'R3': tr(2), 'R4': tg ** 2 - 1,
            'R5': tr(6) - (tg ** 2 - 1), 'R6': tr(3), 'R7': tr(4), 'R8': tr(5)}[slot]


def multiplicity(n, slot, E):
    return int(round(np.mean(su2.chi(n, rotation_angle(E)) * chi_formula(slot, E))))


def intertwiners(n, slot, E, tol=1e-8, group_order=None, elementary_order=None):
    """The canonical orthonormal basis (Frobenius) of Hom_2I(V_n, W_rho) (DESIGN.md section 3, UB's c1).

    The group average X -> (1/120) sum_g rho(g) X pi_n(g)^{-1} is applied to the elementary matrices E_ab, in
    row-major order (a over W_rho, b over V_n), and modified Gram-Schmidt, run twice, keeps each image whose
    residual exceeds tol; the group average is then applied once more to each kept vector, and Gram-Schmidt rerun
    in the same order, to remove the rounding that normalization amplifies. No phase or unitary is chosen by a
    solver, so the coefficients reproduce on any machine.
    Returns (basis, (smallest kept residual, largest dropped residual)). The orders are for D1's tests only.
    """
    r = dim(slot)
    R = rep(slot, E)
    P = su2.pi(n, su2.quat_to_su2(E))
    if group_order is not None:
        R, P = R[group_order], P[group_order]
    T = np.einsum('gca,gdb->cadb', R, P.conj()) / len(E)        # image of E_ab is T[:, a, :, b]
    pairs = [(x, y) for x in range(r) for y in range(n + 1)]
    if elementary_order is not None:
        pairs = [pairs[i] for i in elementary_order]
    basis, kept, dropped = [], [], []
    for x, y in pairs:
        X = T[:, x, :, y].copy()
        for _ in range(2):
            for A in basis:
                X = X - np.vdot(A, X) * A
        nr = np.linalg.norm(X)
        if nr > tol:
            basis.append(X / nr)
            kept.append(nr)
        else:
            dropped.append(nr)
    # refinement: the group average is a projector, so applying it again removes the rounding that normalizing a
    # small residual amplified; Gram-Schmidt then runs again in the same order (still canonical)
    refined = []
    for A in basis:
        X = np.einsum('gca,ab,gdb->cd', R, A, P.conj()) / len(E)
        for _ in range(2):
            for B in refined:
                X = X - np.vdot(B, X) * B
        refined.append(X / np.linalg.norm(X))
    return refined, (min(kept) if kept else None, max(dropped) if dropped else 0.0)


def intertwiner_nullspace(n, slot, E, gens, tol=1e-9):
    """D1's independent count: an orthonormal basis of Hom_2I(V_n, W_rho) from the nullspace at the two generators."""
    r = dim(slot)
    rows = []
    for g in gens:
        R = rep(slot, E[g])
        P = su2.pi(n, su2.quat_to_su2(E[g]))
        # vec(R A - A P) = (I (x) R - P^T (x) I) vec(A), column-major vec
        rows.append(np.kron(np.eye(n + 1), R) - np.kron(P.T, np.eye(r)))
    M = np.vstack(rows)
    _, s, Vh = np.linalg.svd(M)
    s_full = np.zeros(Vh.shape[0])
    s_full[:len(s)] = s
    null = [Vh[k].conj() for k in range(Vh.shape[0]) if s_full[k] < tol]
    return [v.reshape((n + 1, r)).T for v in null], s_full
