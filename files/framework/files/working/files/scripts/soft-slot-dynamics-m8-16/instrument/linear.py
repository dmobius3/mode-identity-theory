"""The linear record (DESIGN.md section 7), for any real Hamiltonian triple (A, B, W) with A^T W = B.

first_order(L, omega) builds the instrument's own triple: the rotating frame zeta'' + 2 i omega zeta' + L zeta = 0,
x = (zeta, zeta'), A = [[0, I], [-L, -2 omega J0]], B = diag(L, I), W = [[2 omega J0, I], [-I, 0]], with J0 the real
matrix of multiplication by i. Then Omega(A x, y) = x^T A^T W y = B(x, y), and A^T W + W A = 0.

record() reads, at one point, with the margin its caller sets: margin(normA, m) = KAPPA sqrt(u ||A|| max(m, M0)),
m = ||phi||^2, for the instrument (RECAL_PLAN.md, provisional: UA, UB), or DL's own, for its original claims:
  - the zero cluster, |lambda| < margin, separated only if no eigenvalue lies in the gray zone (margin/G, G margin);
  - V0, the invariant subspace of that cluster, from an ordered real Schur form (never from eigenvectors);
  - its Jordan structure, from the ranks of the leading Schur block and its powers, at a rank floor on the scale
    u ||A||; the cluster's eigenvalues sit near (u ||A||)^(1/j) for chains of length j (UB's c3);
  - n(L) by inertia, with L's cut L_CUT = 1000 u ||L|| and its own gray zone up to G_L = 10 times it (Step 2), and
    n(D), the negative index of B on V0, at its unchanged cut; each unresolved if an eigenvalue lies in its gray zone;
    n(L) is also unresolved where L's zero count differs from V0's chain count: ker A = ker L x {0}, so the two are
    equal, and a small genuine eigenvalue of L read as zero is never a resolution (UB; off under ORIGINAL);
  - outside the cluster, groups of eigenvalues linked within tau(lambda) = max(margin, KAPPA_D sqrt(u ||A|| |lambda|)):
    a defective eigenvalue splits on the scale sqrt(u ||A|| |lambda|), which grows with |lambda| while the margin does
    not (UB), so each group is typed by its centre, which round-off moves only on the scale u ||A||: real, imaginary
    or complex to within tau at its centre, which moves no count of K;
  - the Krein signature of B on each imaginary group i tau, tau > 0: on its eigenvectors when they span it, reported
    unresolved where B is degenerate on them (B is nondegenerate on the eigenspaces of imaginary eigenvalues, so a
    degenerate form there means a member off the axis, or a collision, within the resolution); and where they do not
    span it (a defective group, such as a Krein collision point, where the eigenvectors are B-isotropic), on the
    group's real invariant subspace, with its conjugate's, from an ordered real Schur form. Both routes read
    nondegeneracy against |lambda| ||W||, which bounds a unit eigenvector's Krein form since
    v^H B v = conj(lambda) v^H W v, and n(D)'s inertia is read against ||B|| (UB's c2);
  - an imaginary group carrying both Krein signs is a collision within the margin, possibly a quartet: K counts it,
    and its type is unresolved, with its largest |Re lambda| (UA, UB's c1);
  - K = k_r + 2 k_c + 2 k_i^-, and Theorem K's balance K = n(L) - n(D); a balance that fails is an unresolved item
    (UA);
  - n(D) is unresolved where D's nullity differs from the geometric multiplicity of zero on V0 (the number of Jordan
    chains): the two are equal, since Omega is nondegenerate on V0 and B(x, y) = Omega(A x, y) (UA);
  - V0 against the point's expected V0, its dimension and Jordan ranks, and the symmetry directions' leak, at most
    KAPPA_L u ||A|| / gap, the gap the smallest |lambda| outside the cluster. Where symmetry directions are given, a
    gap that is not finite and positive, or a bound above LEAK_CAP, is an unresolved item, never a pass (UA); without
    them, V0 is checked on its dimension and ranks (UB), but only for a system declared free of symmetry directions
    (symmetry_free=True): an empty list not so declared is an unresolved item, so a driver that loses its tangents
    cannot read Elliptic (UA). A mismatch is an unresolved item, and without an expectation the type is not read (UB);
  - the type: Hyperbolic when a group outside the cluster's gray zone lies off the imaginary axis by more than tau at
    its centre and V0 matches its expectation; otherwise Elliptic only when nothing is unresolved, and Unresolved if
    anything is. The balance never stands in for the type (UA).
  - each eigenvalue's label, for the drivers: 'gray', 'cluster', or its group's type, 'real', 'imag' or 'complex', so
    a driver reads the slow eigenvalues from the record's own classification (UA).
The original calibration, under which DL's original claims ran and still run, is the caller's margin
30 (u ||A||)^(1/j) with gray=10, kappa_d=0 (one margin for every role) and leak_abs=1e-8 (ORIGINAL).
Unresolved is a reportable outcome, never forced. eigvec_annihilator() is the construction that section 7 replaced,
kept for the arm that shows it fails at a defective nonzero eigenvalue.
"""
import numpy as np
from scipy.linalg import schur, null_space
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from . import devtools

U = np.finfo(float).eps
# the section 7 calibration (RECAL_PLAN.md), provisional until its synthetic tests are reviewed (UA, UB)
KAPPA, M0, GRAY, KAPPA_D, KAPPA_L, LEAK_CAP = 2.0, 0.2, 3.0, 10.0, 200.0, 1e-4
# L's inertia cut and its gray zone (SLOWPAIR_PLAN.md, Step 2): the controls' L kernel is round-off, at most 6.2 u,
# so the cut is set in units of u (UA, UB), at 1000 u ||L|| (UB; UA approved 100 u), its gray zone to G_L = 10 times it
L_CUT, G_L = 1000 * U, 10.0
ORIGINAL = dict(gray=10.0, kappa_d=0.0, leak_abs=1e-8, zero_count=False, zero_rel=1e-10, l_gray=1e3)


def margin(normA, m, kappa=KAPPA, m0=M0):
    """The zero cluster's margin at a point with ||A|| = normA and m = ||phi||^2: kappa sqrt(u ||A|| max(m, m0))."""
    return kappa * np.sqrt(U * normA * max(m, m0))


def leak_bound(normA, gap, kappa_l=KAPPA_L, cap=LEAK_CAP):
    """(bound, reason): the symmetry leak's bound kappa_l u ||A|| / gap, and the reason it cannot be used, if any:
    a gap that is not finite and positive, or a bound above cap, too large to discriminate (UA)."""
    if not (np.isfinite(gap) and gap > 0):
        return np.nan, f'the leak bound is undefined: the gap {gap} is not finite and positive'
    bound = kappa_l * U * normA / gap
    if bound > cap:
        return bound, f'the leak bound {bound:.1e} is above {cap:.0e}, too large to discriminate'
    return bound, None


def J0(m):
    return np.block([[np.zeros((m, m)), -np.eye(m)], [np.eye(m), np.zeros((m, m))]])


def first_order(L, omega, G=None):
    devtools.refuse_in_seedcheck('linear.first_order')
    n = L.shape[0]
    G = 2 * omega * J0(n // 2) if G is None else G
    I, Z = np.eye(n), np.zeros((n, n))
    A = np.block([[Z, I], [-L, -G]])
    B = np.block([[L, Z], [Z, I]])
    W = np.block([[G, I], [-I, Z]])
    return A, B, W


def symplectic_defects(A, B, W):
    s = max(1.0, np.abs(B).max())
    return dict(energy=np.abs(A.T @ W - B).max() / s, skew=np.abs(W + W.T).max(),
                hamiltonian=np.abs(A.T @ W + W @ A).max() / s,
                invertible=float(np.linalg.svd(W, compute_uv=False).min()))


def inertia(M, zero_rel=1e-10, gray=1e3, scale=None):
    """(negatives, zeros, resolved) for a symmetric M, with a gray zone (zero_rel, gray zero_rel) times the scale:
    ||M|| unless a scale is given (n(D) is read against ||B||)."""
    if M.size == 0:
        return 0, 0, True
    ev = np.linalg.eigvalsh((M + M.T) / 2)
    s = max(np.abs(ev).max() if scale is None else scale, 1e-300)
    a = np.abs(ev) / s
    resolved = not np.any((a > zero_rel) & (a < gray * zero_rel))
    return int(np.sum(ev < -zero_rel * s)), int(np.sum(a <= zero_rel)), resolved


def group(vals, tol):
    """Groups of indices of complex values linked within tol of each other (single linkage); deterministic order.
    tol is a number, or one tolerance per value, two values linking within the larger of theirs."""
    n = len(vals)
    if n == 0:
        return []
    t = np.broadcast_to(np.asarray(tol, dtype=float), (n,))
    pairs = cKDTree(np.column_stack([vals.real, vals.imag])).query_pairs(float(t.max()), output_type='ndarray')
    if len(pairs) and t.min() < t.max():
        d = np.abs(vals[pairs[:, 0]] - vals[pairs[:, 1]])
        pairs = pairs[d <= np.maximum(t[pairs[:, 0]], t[pairs[:, 1]])]
    G = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(n, n))
    _, lab = connected_components(G, directed=False)
    out = {}
    for i, l in enumerate(lab):
        out.setdefault(l, []).append(i)
    return list(out.values())


def _krein_schur(A, B, W, c, rad, s, krein_sign, own_scale=False):
    """Krein directions of a group of s eigenvalues near c, on the real invariant subspace of the group and its
    conjugate (real dimension 2 s), from an ordered real Schur form; each complex direction counts twice there.
    Nondegeneracy is read against |c| ||W|| (own_scale: against the form's own largest value, for an arm only).
    Returns (negative, positive, resolved)."""
    _, Z, sg = schur(A, output='real',
                     sort=lambda x, y: abs(complex(x, y) - c) < rad or abs(complex(x, y) - np.conj(c)) < rad)
    if sg != 2 * s:
        return 0, 0, False
    X = Z[:, :sg]
    M = krein_sign * (X.T @ B @ X)
    ev = np.linalg.eigvalsh((M + M.T) / 2)
    neg = int(np.sum(ev < 0))
    scale = np.abs(ev).max() if own_scale else abs(c) * np.linalg.norm(W, 2)
    nondeg = np.abs(ev).min() > 1e-8 * scale
    return neg // 2, (sg - neg) // 2, bool(nondeg and neg % 2 == 0)


def record(A, B, W, L, margin, symmetry=(), expected=None, zero_rel=L_CUT, krein_sign=1.0, arm=None, gray=GRAY,
           kappa_d=KAPPA_D, leak_kappa=KAPPA_L, leak_abs=None, symmetry_free=False, zero_count=True, l_gray=G_L):
    """The linear record at one point (module docstring). expected = dict(dim=..., ranks=[...]): the point's expected
    V0, its dimension and the ranks of A's powers on it, derived before the point runs; symmetry: its exact symmetry
    directions; symmetry_free: the explicit declaration that the system has none to check (UA). gray: the gray zone's
    factor G; kappa_d: the nonzero groups' scale, 0 for one margin in every role; leak_kappa: the leak bound's factor,
    or leak_abs, a fixed bound (the original calibration, ORIGINAL, under which an empty list passes as it did).
    zero_rel and l_gray: L's inertia cut and its gray zone's factor (L_CUT and G_L; ORIGINAL keeps 1e-10 and 1e3).
    arm, for DL's arms and diagnostics only: 'krein_own_scale' reads Krein nondegeneracy against the
    form's own largest value, 'd_own_scale' reads n(D) against D's own largest eigenvalue, 'mixed_resolved' types a
    mixed imaginary group as resolved, 'schur_on_degenerate' also takes the Schur route where the eigenvectors span a
    group but B is degenerate on them (UB's c2 patch, as UB ran it), 'index_unguarded' drops the balance and nullity
    checks, and 'v0_unchecked' drops the check against the expected V0. Besides its readings it returns A's eigenvalues
    lam and eigenvectors V, and its groups outside the cluster (indices, centre, class, Krein count), for the
    separation rule (convergence.py); no reading depends on them."""
    devtools.refuse_in_seedcheck('linear.record')
    nA = np.linalg.norm(A, 2)
    nW = np.linalg.norm(W, 2)
    lam, V = np.linalg.eig(A)
    a = np.abs(lam)
    in0 = a < margin
    in_gray = (a >= margin / gray) & (a < gray * margin)
    out = dict(normA=nA, margin=margin, gray=gray, kappa_d=kappa_d, cluster=int(in0.sum()),
               separated=not np.any(in_gray), unresolved=[])
    out['cluster_max'] = float(a[in0].max()) if in0.any() else 0.0
    out['outside_min'] = float(a[~in0].min()) if (~in0).any() else np.inf
    if not out['separated']:
        out['unresolved'].append(f'the zero cluster is not separated: an eigenvalue lies in (margin/{gray:g},'
                                 f' {gray:g} margin)')
    labels = np.where(in_gray, 'gray', np.where(in0, 'cluster', '')).astype(object)
    # V0 from the ordered real Schur form
    T, Z, sdim = schur(A, output='real', sort=lambda x, y: abs(complex(x, y)) < margin)
    V0 = Z[:, :sdim]
    out['sdim'] = int(sdim)
    if sdim != out['cluster']:
        out['unresolved'].append('the Schur reordering and the eigenvalues disagree on the cluster')
    floor = 1e2 * U * nA
    T11 = T[:sdim, :sdim]
    ranks, P = [], np.eye(sdim)
    for _ in range(sdim):
        P = P @ T11
        r = int(np.sum(np.linalg.svd(P, compute_uv=False) > floor))
        ranks.append(r)
        if r == 0:
            break
    out['jordan_ranks'] = ranks                         # rank of T11^p, p = 1, 2, ...
    out['longest_chain'] = next((p + 1 for p, r in enumerate(ranks) if r == 0), None) if sdim else 0
    out['blocks'] = sdim - ranks[0] if sdim else 0
    out['root_scale'] = (U * nA) ** (1.0 / out['longest_chain']) if out['longest_chain'] else 0.0
    out['symmetry_leak'] = max((np.linalg.norm(s - V0 @ (V0.T @ s)) / np.linalg.norm(s) for s in symmetry), default=0.0)
    if leak_abs is not None:
        out['leak_bound'], leak_why = leak_abs, None
    elif len(symmetry):
        out['leak_bound'], leak_why = leak_bound(nA, out['outside_min'], leak_kappa)
    elif symmetry_free:
        out['leak_bound'], leak_why = None, None             # declared: V0 on its dimension and ranks (UB)
    else:
        out['leak_bound'], leak_why = None, 'no symmetry directions were given, and none were declared absent'
    if arm == 'v0_unchecked':
        v0_ok = True
    elif expected is None:
        v0_ok = False
        out['unresolved'].append('no expected V0 given: the type is not read')
    elif leak_why is not None:
        v0_ok = False
        out['unresolved'].append(f'V0 cannot be checked: {leak_why}')
    else:
        v0_ok = (out['sdim'] == expected['dim'] and ranks == list(expected['ranks'])
                 and (out['leak_bound'] is None or out['symmetry_leak'] <= out['leak_bound']))
        if not v0_ok:
            out['unresolved'].append(f"V0 does not match its expectation: dimension {out['sdim']} against"
                                     f" {expected['dim']}, ranks {ranks} against {list(expected['ranks'])},"
                                     f" symmetry leak {out['symmetry_leak']:.1e}")
    out['v0_matches'] = v0_ok
    # n(L) and n(D)
    nL, zL, okL = inertia(L, zero_rel, gray=l_gray)
    out['nL'], out['dimkerL'] = nL, zL
    if not okL:
        out['unresolved'].append('n(L): an eigenvalue of L lies in its gray zone')
    Dm = V0.T @ B @ V0
    nD, zD, okD = inertia(Dm, 1e-8, scale=None if arm == 'd_own_scale' else np.linalg.norm(B, 2))
    out['nD'], out['dimkerD'] = nD, zD
    if not okD:
        out['unresolved'].append('n(D): an eigenvalue of D lies in its gray zone')
    if zD != out['blocks'] and arm != 'index_unguarded':
        out['unresolved'].append(f"n(D): D's nullity {zD} differs from the geometric multiplicity of zero on V0,"
                                 f" {out['blocks']}")
    if zero_count and zL != out['blocks']:
        out['unresolved'].append(f"n(L): L's zero count {zL} differs from V0's chains {out['blocks']}")
    # the spectrum outside the cluster, in groups typed by their centres
    idx_out = np.where(~in0)[0]
    kr = kc = ki = 0
    fallback, spreads, imag_groups, off_axis, groups_out = 0, [], [], 0, []

    def tau(z):
        return np.maximum(margin, kappa_d * np.sqrt(U * nA * np.abs(z)))

    for g in group(lam[idx_out], tau(lam[idx_out])):
        idx = idx_out[g]
        c = lam[idx].mean()
        s = len(idx)
        tc = float(tau(c))
        spread = float(np.abs(lam[idx] - c).max())
        if s > 1:
            spreads.append(spread)
        if abs(c.imag) <= tc:
            labels[idx] = np.where(labels[idx] == 'gray', 'gray', 'real')
            kr += s * int(c.real > 0)
            groups_out.append(dict(idx=idx, centre=complex(c), cls='real', neg=None, status=None))
            off_axis += int(c.real > 0 and abs(c) >= gray * margin)
        elif abs(c.real) <= tc:
            labels[idx] = np.where(labels[idx] == 'gray', 'gray', 'imag')
            if c.imag <= 0:
                groups_out.append(dict(idx=idx, centre=complex(c), cls='imag', neg=None, status=None))
                continue
            Vg = V[:, idx]
            Uq, sv, _ = np.linalg.svd(Vg, full_matrices=False)
            rank = int(np.sum(sv > 1e-6 * sv.max()))
            ok = False
            if rank == s:
                Q = Uq[:, :rank]
                M = krein_sign * (Q.conj().T @ B @ Q)
                ev = np.linalg.eigvalsh((M + M.conj().T) / 2)
                scale = np.abs(ev).max() if arm == 'krein_own_scale' else abs(c) * nW
                ok = np.abs(ev).min() > 1e-8 * scale
                n_neg = int(np.sum(ev < 0))
                n_pos = s - n_neg
            res, route = ok, 'eigenvectors'
            if rank < s or (not ok and arm == 'schur_on_degenerate'):
                n_neg, n_pos, res = _krein_schur(A, B, W, c, spread + tc / 2, s, krein_sign,
                                                 own_scale=arm == 'krein_own_scale')
                fallback += 1
                route = 'Schur'
            max_re = float(np.abs(lam[idx].real).max())
            if not res:
                status = 'degenerate'
                out['unresolved'].append(f'the Krein signature of the group at {c:.6g}')
            elif n_neg and n_pos:
                status = 'mixed'
                if arm != 'mixed_resolved':
                    out['unresolved'].append(f'a mixed imaginary group at {c:.6g}: a collision within the margin,'
                                             f' possibly a quartet (largest |Re| {max_re:.1e})')
            else:
                status = 'definite'
            ki += n_neg
            imag_groups.append((complex(c), s, n_neg, route, status, max_re))
            groups_out.append(dict(idx=idx, centre=complex(c), cls='imag', neg=int(n_neg), status=status))
        else:
            labels[idx] = np.where(labels[idx] == 'gray', 'gray', 'complex')
            groups_out.append(dict(idx=idx, centre=complex(c), cls='complex', neg=None, status=None))
            if c.real > 0 and c.imag > 0:
                kc += s
                off_axis += int(abs(c) >= gray * margin)
    out.update(kr=int(kr), kc=int(kc), ki=int(ki), K=int(kr + 2 * kc + 2 * ki), krein_fallback_groups=fallback,
               multi_groups=len(spreads), max_spread=max(spreads, default=0.0), imag_groups=imag_groups)
    out['balance'] = out['K'] == nL - nD
    if not out['balance'] and arm != 'index_unguarded':
        out['unresolved'].append(f"the index does not balance: K = {out['K']}, n(L) - n(D) = {nL - nD}")
    out['K_resolved'] = not any(g[4] == 'degenerate' for g in imag_groups)
    out['type'] = ('Hyperbolic' if off_axis and v0_ok else
                   ('Elliptic' if not out['unresolved'] else 'Unresolved'))
    out['V0'] = V0
    out['lam'] = lam
    out['V'] = V                                       # for the separation rule (convergence.py)
    out['groups'] = groups_out                         # every group outside the cluster: indices, centre, class, Krein
    out['labels'] = labels.astype(str)
    return out


def eigvec_annihilator(A, W, margin, vectors='exact', null_rel=1e-12, rcond=1e-10):
    """The construction section 7 replaced: the W-annihilator of the eigenvectors of the nonzero eigenvalues.

    vectors='exact': the construction as defined. Each group of eigenvalues linked within the margin contributes
    ker(A - c I) at the round-off cut null_rel ||A||, c its centre; for exactly degenerate or exactly defective
    eigenvalues, as in the synthetic tests, that is the exact eigenspace, so a defective group contributes fewer
    vectors than its multiplicity and the annihilator is larger than V0.
    vectors='eig': as identification_check.py computes it, from the computed eigenvector of each eigenvalue, with
    the null space cut at rcond. Returns an orthonormal basis of the annihilator."""
    nA = np.linalg.norm(A, 2)
    lam, Vc = np.linalg.eig(A)
    nz = np.where(np.abs(lam) >= margin)[0]
    if vectors == 'eig':
        S = Vc[:, nz]
    else:
        vecs = []
        for g in group(lam[nz], margin):
            c = lam[nz[g]].mean()
            _, s, Vh = np.linalg.svd(A - c * np.eye(A.shape[0]))
            vecs.extend(Vh[k].conj() for k in range(len(s)) if s[k] < null_rel * nA)
        S = np.column_stack(vecs) if vecs else np.zeros((A.shape[0], 0))
    if S.shape[1] == 0:
        return np.eye(A.shape[0])
    WS = W @ S
    return null_space(np.vstack([WS.T.real, WS.T.imag]), rcond=rcond)


def principal_angle(X, Y):
    """The largest principal angle between the column spans of X and Y, of equal dimension, in radians, from its
    sine, ||(I - Qx Qx^H) Qy||: the cosine form, arccos of the smallest singular value of Qx^H Qy, cannot resolve
    an angle below sqrt(2u), about 2.1e-8."""
    Qx, _ = np.linalg.qr(X)
    Qy, _ = np.linalg.qr(Y)
    if Qy.shape[1] == 0:
        return 0.0
    s = np.linalg.svd(Qy - Qx @ (Qx.conj().T @ Qy), compute_uv=False)
    return float(np.arcsin(min(s.max(), 1.0)))
