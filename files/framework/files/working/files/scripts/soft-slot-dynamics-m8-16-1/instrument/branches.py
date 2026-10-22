"""Seeds, orbit checks and continuation for the GO-list controls (DESIGN.md sections 6 and 8; EXPECTED_V0.md).

The GO list's branches are constructed by seed_state: D6's Theorem D member in R3 (case theoremD:R3); D7's C2a, R4's
coherent v_3; C2b, R2's weight-7/2 state v_{7/2}, with complex structure i; C3, R4's octahedron v_2 + v_{-2}; and, by
BOUNDARY.md's amendment 3, C2a/R5, R5's coherent v_3. The sealed seeds (SEALED: the pyramid and the census target rows)
are constructed only by sealed_seed_for_check, for amendment 2's lowest-level check, and seed_state refuses them until
a valid frozen allowlist lists them (BOUNDARY.md, its note to amendments 2 and 3; DRIVER_PLAN.md v2).

The weight basis: the right generator GENS[2] = -i sigma_z is diagonal on each level, with eigenvalue i (2k - n) on
e_k, so e_k has weight m = (n - 2k)/2, and v_m is e_k with k = n/2 - m. With J_a = gen_matrix(n, sigma_a)/2, J_+ e_k =
sqrt(k (n - k + 1)) e_{k-1}, real and positive, so e_k is the Condon-Shortley |n/2, m> with no phase (dev/seed_check.py,
claim 1). The representatives are the Result's section IV entries, in those components.

Continuation (DESIGN.md section 6): Newton on (c, lam) at a fixed m* = ||c||^2, bordered by an orthonormal basis of the
orbit tangents at the slice point, with eps = lam - lam0 as output, and a secant in m* to each target eps, as in
M8.15. A secant slope that is not positive is a fold, and the branch ends there.
"""
import hashlib
import os
import re
import numpy as np
from . import functional as fn, newton, certified, devtools

CASES = {'C1': ('theoremD:R3', 'R3', 2), 'C2a': ('C2a', 'R4', 6), 'C2b': ('C2b', 'R2', 7), 'C3': ('C3', 'R4', 6),
         'C2a/R5': ('C2a/R5', 'R5', 6)}
# the sealed seeds (BOUNDARY.md): name -> (slot, lowest level)
SEALED = {'P5': ('R4', 6), 'T1/R4': ('R4', 6), 'T1/R5': ('R5', 6), 'T2/R4': ('R4', 6), 'T2/R5': ('R5', 6),
          'T3/R4': ('R4', 6), 'T3/R5': ('R5', 6), 'T4/R4': ('R4', 6), 'T4/R5': ('R5', 6), 'T5/R2': ('R2', 7)}


def representative(name):
    """The case's representative in Condon-Shortley components {m: coefficient}, unnormalized, as the Soft-Slot
    Branches' section IV writes it (the third outside orbit at its certified point, instrument/certified.py)."""
    orbit = name.split('/')[0]
    reps = {'C2a': {3: 1.0}, 'C2b': {3.5: 1.0}, 'C3': {2: 1.0, -2: 1.0},
            'P5': {3: np.sqrt(12.0), -2: np.sqrt(13.0)}, 'T1': {2: 1.0},
            'T2': {3: 1.0, 0: np.sqrt(23 / 10), -3: 1.0}, 'T3': {3: 1.0, -3: 1.0},
            'T5': {3.5: np.sqrt(3 / 10), -1.5: np.sqrt(7 / 10)}}
    if orbit == 'T4':
        return certified.outside_point()
    return dict(reps[orbit])


def _unit_vector(B, n0, comps):
    u = np.zeros(B.m, dtype=complex)
    for m, c in comps.items():
        u[weight_index(B, n0, m)] = c
    return u / np.linalg.norm(u)


def sealed_seed_for_check(name, B):
    """A sealed seed's unit lowest-level vector, for BOUNDARY.md's amendment 2 only: Q(u), criticality and (k, r_u),
    with no Newton step and no Hessian, slow matrix, L or A formed at it (the note to amendments 2 and 3). It refuses
    outside a seedcheck process, and inside one every solver path refuses (devtools.SEEDCHECK; UB)."""
    if not devtools.SEEDCHECK:
        raise PermissionError(f'seed {name!r}: sealed seeds are built only in a seedcheck process (BOUNDARY.md, amendment 2)')
    slot, n0 = SEALED[name]
    assert B.slot == slot and B.levels[0] == n0
    return _unit_vector(B, n0, representative(name))


def weight_index(B, n, m):
    """The basis index of v_m on level n, for a level where the slot occurs once."""
    k = n / 2 - m
    assert abs(k - round(k)) < 1e-12
    hits = [j for j, (nn, i, kk) in enumerate(B.index) if nn == n and i == 0 and kk == int(round(k))]
    assert len(hits) == 1 and sum(1 for nn, i, _ in B.index if nn == n and i == 1) == 0
    return hits[0]


def seed_state(name, B):
    """The unit lowest-level representative of the control's orbit, as basis coefficients. A sealed seed is refused
    unless a valid frozen allowlist lists it (devtools.frozen; DRIVER_PLAN.md v2)."""
    if name in SEALED:
        if not devtools.admitted(name):
            raise PermissionError(f'seed {name!r} is sealed and no valid frozen allowlist lists it (BOUNDARY.md)')
        slot, n0 = SEALED[name]
        assert B.slot == slot and B.levels[0] == n0
        return _unit_vector(B, n0, representative(name))
    if name == 'C2a/R5':
        assert B.slot == 'R5' and B.levels[0] == 6
        return _unit_vector(B, 6, representative(name))
    case, slot, n0 = CASES[name]
    assert B.slot == slot and B.levels[0] == n0
    u = np.zeros(B.m, dtype=complex)
    if name == 'C1':
        # a fixed generic member of Theorem D's sphere: neither a weight vector nor isotropic
        idx = [weight_index(B, 2, m) for m in (1, 0, -1)]
        u[idx] = np.array([1.0, 0.6 + 0.3j, -0.4j])
    elif name == 'C2a':
        u[weight_index(B, 6, 3)] = 1.0
    elif name == 'C2b':
        u[weight_index(B, 7, 3.5)] = 1.0
    elif name == 'C3':
        u[weight_index(B, 6, 2)] = 1.0
        u[weight_index(B, 6, -2)] = 1.0
    return u / np.linalg.norm(u)


def tangent_vectors(Fn, c, K=None):
    """The orbit tangents at c, as real vectors: the right generators T_a c, the phase i c and, with the fibre
    structure K (R2), J c = K conj(c) and i J c."""
    T = [fn.to_real(G @ c) for G in fn.right_generators(Fn.B)] + [fn.to_real(1j * c)]
    if K is not None:
        Jc = K @ c.conj()
        T += [fn.to_real(Jc), fn.to_real(1j * Jc)]
    return T


def orbit_checks(Fn, u, K=None, rel=1e-8):
    """At a unit lowest-level u: Q(u) = <u, P(|psi|^2 psi)>; criticality on E0, the residual of
    P0 P(|psi_u|^2 psi_u) = Q(u) u; the tangents' rank k (pivoted QR); and the dimension r_u of the sigma-radical of
    their span, sigma(x, y) = Re<x, i y> = x^T J0 y, with its rank cut rel relative to its largest value."""
    cub = Fn.cubic(u)
    Q = float(np.real(np.vdot(u, cub)))
    n0 = Fn.B.levels[0]
    low = np.array([n == n0 for n, _, _ in Fn.B.index])
    crit = float(np.linalg.norm(np.where(low, cub, 0) - Q * u) / np.linalg.norm(np.where(low, cub, 0)))
    Qb, k, _ = newton.tangent_borders(tangent_vectors(Fn, u, K))
    m = Fn.B.m
    J0 = np.block([[np.zeros((m, m)), -np.eye(m)], [np.eye(m), np.zeros((m, m))]])
    S = Qb.T @ J0 @ Qb
    sv = np.linalg.svd(S, compute_uv=False)
    rank_s = int(np.sum(sv > rel * max(sv.max(), 1.0)))
    return dict(Q=Q, crit=crit, k=int(k), r=int(k - rank_s), sigma_sv=sv)


def continue_to(Fn, lam0, target, c_prev, lam_prev, slope, K=None, prev_accepted=False, tol=1e-6, max_secant=8):
    """From (c_prev, lam_prev), an accepted point or a leading-order seed, to eps = target within tol, by a secant in
    m* = ||c||^2 started on the slope dm*/deps. Returns a dict with the point, its Newton info, and each solve."""
    devtools.refuse_in_seedcheck('branches.continue_to')
    h = np.zeros(Fn.B.m, dtype=complex)
    m_prev = float(np.real(np.vdot(c_prev, c_prev)))
    eps_prev = lam_prev - lam0
    pts = [(m_prev, eps_prev)] if prev_accepted else []
    m = m_prev + slope * (target - eps_prev)
    c_seed, lam_seed = c_prev * np.sqrt(m / m_prev), lam0 + target
    steps = []
    for _ in range(max_secant):
        borders, rank, _ = newton.tangent_borders(tangent_vectors(Fn, c_seed, K))
        c, lam, mu, hist, acc, info = newton.solve(Fn, h, m, c_seed, lam_seed, borders=borders, x_slice=fn.to_real(c_seed))
        eps = lam - lam0
        steps.append(dict(m=m, eps=eps, evaluations=len(hist), accepted=bool(acc), rank=int(rank), floor=info['floor'],
                          floor_rel=info['floor_rel'], unbordered_rel=info['unbordered_rel'], mu_rel=info['mu_rel']))
        if not acc:
            return dict(ok=False, reason='Newton not accepted', steps=steps, c=c, lam=lam)
        if abs(eps - target) <= tol:
            return dict(ok=True, steps=steps, c=c, lam=lam, m=m, eps=eps, info=info, slope=slope)
        pts.append((m, eps))
        if len(pts) >= 2:
            (m0, e0), (m1, e1) = pts[-2], pts[-1]
            slope = (m1 - m0) / (e1 - e0)
        if not np.isfinite(slope) or slope <= 0:
            return dict(ok=False, reason='fold: the secant slope is not positive', steps=steps, c=c, lam=lam)
        m_new = m + slope * (target - eps)
        c_seed, lam_seed, m = c * np.sqrt(m_new / m), lam + (target - eps), m_new
    return dict(ok=False, reason='the secant did not reach the target', steps=steps, c=c, lam=lam)


def expected_v0(root):
    """The controls' expected V0 rows from EXPECTED_V0.md, as dict(dim=..., ranks=[...]), with the file's SHA-256, which
    must equal the SHA-256 that DEVLOG.md logged for it before any control ran (the first in that entry)."""
    path = os.path.join(root, 'EXPECTED_V0.md')
    with open(path, 'rb') as f:
        raw = f.read()
    sha = hashlib.sha256(raw).hexdigest()
    with open(os.path.join(root, 'DEVLOG.md'), encoding='utf-8') as f:
        log = f.read()
    entries = [e for e in re.split(r'\n(?=## \d+\.)', log) if e.startswith('## ') and 'EXPECTED_V0.md' in e.split('\n')[0]]
    if not entries:
        raise PermissionError('EXPECTED_V0.md was never logged')
    logged = re.findall(r'SHA-256 `([0-9a-f]{64})`', entries[0])[0]
    if logged != sha:
        raise PermissionError('EXPECTED_V0.md differs from the version logged before the controls ran')
    rows = {}
    for line in raw.decode('utf-8').splitlines():
        m = re.match(r'\| (C1|C2a|C2b|C3) \(D[67]\) \|.*dim (\d+), ranks \[([0-9, ]+)\] \|\s*$', line)
        if m:
            rows[m.group(1)] = dict(dim=int(m.group(2)), ranks=[int(x) for x in m.group(3).split(',')])
    assert set(rows) == {'C1', 'C2a', 'C2b', 'C3'}
    return rows, sha
