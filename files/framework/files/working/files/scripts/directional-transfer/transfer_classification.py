#!/usr/bin/env python3
"""R7's first calculation: classify the shell-to-direction transfers, and test what selects the Q-symbol among them.

Draft 5 (2026-09-15). Representation theory and linear algebra only: no CMB quantity, no shell weight, no cosmology,
no fit.

A transfer carries a shell covariance A on Sym^N (spin j = N/2) to a directional power A^eff(n) >= 0 on S^2.
Ask for linearity, positivity (A >= 0 gives A^eff >= 0 pointwise) and SU(2)-covariance. Then A^eff(n) = Tr[A E(n)]
with E(n) >= 0 and E(g n) = rho(g) E(n) rho(g)^dagger, so E is fixed by E(z) alone, and E(z) must commute with the
U(1) about z. That makes E(z) diagonal in the spin basis: E(z) = sum_m t_m |j,m><j,m| with t_m >= 0. Normalization,
sum_m t_m = 1, gives every transfer the total power P1 and Q share, and cuts the cone of weights to an N-simplex.

  T1. Covariance forces the diagonal. With E(z) diagonal, E(n) = D_n E(z) D_n^dagger does not depend on which
      rotation D_n carries z to n, and the family is covariant; with a generic E(z) it is not. Both are checked on
      random rotations and directions, so the check can fail.
  T2. The barycenter and a vertex. Uniform t, the average of the N + 1 vertices t = delta_{m,m0} of the simplex,
      gives E(n) = I/(N+1) at every n, hence A^eff(n) = Tr[A]/(N+1): P1's spectral transfer, at the barycenter. The
      vertex t_m = delta_{m,j} gives E(n) = |n><n|, hence A^eff(n) = <n|A|n>: the Q-symbol transfer. The vertex at
      m0 = -j is the antipodal symbol <-n|A|-n>.
  T3. Strong zero preservation selects the ray through Q. Require that for EVERY pure source |psi>, <n|psi> = 0
      implies A^eff(n) = 0. At n = z the coherent state is |j,j>, so psi = |j,m0> for any m0 != j is a witness,
      forcing t_{m0} = 0. What is left is a multiple of Q, and normalization fixes it to Q. The theorem is the proof
      on the page; this checks the coherent state that proof uses.
  T4. Weak zero preservation does NOT select Q. Below N = 60 the source on shell N is the single invariant psi_N,
      so the preservation hypothesis that can be formulated from the realized source alone constrains only that
      state. Rotating a nodal direction v to the pole, the condition kills t_m exactly on the support of
      D_v^dagger psi_N. The k-fold stabilizer of v allows only m = 0 mod k, and a half-turn perpendicular to v,
      which also preserves the axis, sends |j,0> to (-1)^j |j,0>, so m = 0 drops out when j is odd.
  T5. The nodal sets on the one-invariant shells, against step one's Majorana constellations, with each zero simple.
  T6. What reaches the prediction. Operators on Sym^N split into multipole ranks k = 0..N, and E(z) has one zonal
      component per rank, so a transfer acts rank by rank: the predicted pattern is sum_k e_k(t) times the source's
      rank-k density multipole. The source psi_N is 2I-invariant, so its multipoles sit only at degrees carrying an
      A5 invariant, and it is fixed by time reversal, so its odd multipoles vanish. Time reversal commutes with
      rotations and, below N = 60, the invariant is unique, which is what fixes psi_N; at N = 60, where the invariants
      form a plane, a generic one is not fixed and its pairing f_-m = f_m fails. The f_m integrate alike, and the
      rank of their span, less one for normalization, is the freedom left in the predicted pattern. Moving weight
      between the vertices at j and -j changes only odd ranks: it gives P1's flat pattern on psi_N, and is
      directional on the coherent source at the pole.
  T7. The real-field quotient. A real field's covariance commutes with time reversal, and on such a covariance a
      transfer acts only through the pair sums u_0 = t_0, u_m = t_m + t_-m: two transfers with the same pair sums
      agree on a random time-reversal-invariant covariance and differ on a generic one, and the j + 1 pair sums give
      independent patterns, so the physical transfers form a j = N/2 simplex. The time-reversal-fixed states behind
      the real-field version of the strong theorem are checked, the real-field counts are taken from the weak
      supports, and the leading anisotropic response, rank 6 over rank 0, is followed across the weak family as a
      ratio to Q's value, which no normalization convention can change.

Time reversal throughout is exp(-i pi J_y) followed by complex conjugation, Theta v_m = (-1)^(j-m) v_-m: the
Surviving Ray's Theta_j with its free phase epsilon_j = 1. Quantities at the roundoff level are printed as bounds, so
that the record does not depend on the platform.
"""
import itertools

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
np.set_printoptions(suppress=True)


def even_perms(v):
    for p in itertools.permutations(range(4)):
        if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0:
            yield tuple(v[i] for i in p)


def binary_icosahedral():
    """The 120 icosian unit quaternions, as (w, x, y, z)."""
    out = set()
    for i in range(4):
        for s in (1.0, -1.0):
            q = [0.0] * 4
            q[i] = s
            out.add(tuple(q))
    for signs in itertools.product((0.5, -0.5), repeat=4):
        out.add(tuple(signs))
    base = (0.0, 0.5, 0.5 / PHI, 0.5 * PHI)
    for signs in itertools.product((1, -1), repeat=3):
        v = (0.0, signs[0] * base[1], signs[1] * base[2], signs[2] * base[3])
        for p in even_perms(v):
            out.add(tuple(round(c, 12) + 0.0 for c in p))
    q = np.array(sorted(out))
    assert q.shape == (120, 4), q.shape
    return q


def spin_ops(j):
    """J_x, J_y, J_z in the |j,m> basis, m running j, j-1, ..., -j."""
    dim = int(round(2 * j)) + 1
    m = np.array([j - k for k in range(dim)])
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((dim, dim), complex)
    for k in range(1, dim):
        mm = m[k]
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - mm * (mm + 1))
    Jm = Jp.conj().T
    return (Jp + Jm) / 2, (Jp - Jm) / (2 * 1j), Jz


def wigner(j, axis, angle):
    from scipy.linalg import expm
    Jx, Jy, Jz = spin_ops(j)
    return expm(-1j * angle * (axis[0] * Jx + axis[1] * Jy + axis[2] * Jz))


def quat_to_axis_angle(q):
    w = np.clip(q[0], -1.0, 1.0)
    angle = 2 * np.arccos(w)
    s = np.sqrt(max(0.0, 1 - w * w))
    axis = np.array([0.0, 0.0, 1.0]) if s < 1e-12 else np.array(q[1:]) / s
    return axis, angle


def rep(j, q):
    axis, angle = quat_to_axis_angle(q)
    return wigner(j, axis, angle)


def quat_to_rotation(q):
    w, x, y, z = q
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ])


def axis_sets(quats):
    """Rotation axes of 2I by order, as direction sets: 12 five-fold, 20 three-fold, 30 two-fold."""
    got = {5: [], 3: [], 2: []}
    for q in quats:
        axis, angle = quat_to_axis_angle(q)
        if angle < 1e-9 or abs(angle - 2 * np.pi) < 1e-9:
            continue
        for k, target in ((5, 2 * np.pi / 5), (3, 2 * np.pi / 3), (2, np.pi)):
            if abs(angle - target) < 1e-9:
                got[k].append(axis)
    out = {}
    for k, v in got.items():
        uniq = []
        for a in v:
            if not any(np.linalg.norm(a - b) < 1e-8 for b in uniq):
                uniq.append(a)
        out[k] = np.array(uniq)
    return out


def invariant_state(j, reps):
    """The 2I-invariant subspace of Sym^N, and the unique unit invariant when it is one-dimensional."""
    P = sum(reps) / len(reps)
    vals, vecs = np.linalg.eigh((P + P.conj().T) / 2)
    return vecs[:, vals > 0.5]


def coherent(j, n):
    """|n> = D(n)|j,j>, built by rotating the pole to n."""
    zhat = np.array([0.0, 0.0, 1.0])
    c = float(np.clip(np.dot(zhat, n), -1.0, 1.0))
    if c > 1 - 1e-14:
        D = np.eye(int(round(2 * j)) + 1, dtype=complex)
    elif c < -1 + 1e-14:
        D = wigner(j, np.array([1.0, 0.0, 0.0]), np.pi)
    else:
        ax = np.cross(zhat, n)
        ax = ax / np.linalg.norm(ax)
        D = wigner(j, ax, np.arccos(c))
    return D[:, 0], D


def bound(x, cut):
    """A roundoff-level quantity printed as a bound; a value that misses the bound is printed and flagged."""
    return "below %.0e" % cut if x < cut else "%.1e, NOT below %.0e" % (x, cut)


def covariance_defect(j, Ez, rots, dirs):
    """Largest entry of E(R_g n) - rho(g) E(n) rho(g)^dagger over the given rotations and directions,
    with E(n) = D_n Ez D_n^dagger and D_n the rotation coherent() uses to carry z to n."""
    worst = 0.0
    for q in rots:
        R = quat_to_rotation(q)
        U = rep(j, q)
        for d in dirs:
            _, Dn = coherent(j, d)
            _, Dgn = coherent(j, R @ d)
            lhs = Dgn @ Ez @ Dgn.conj().T
            rhs = U @ (Dn @ Ez @ Dn.conj().T) @ U.conj().T
            worst = max(worst, float(np.max(np.abs(lhs - rhs))))
    return worst


def weak_support(j, psi, vs):
    """The nodal directions of psi among vs, and the union over them of the supports of D_v^dagger psi."""
    nodal, support = [], np.zeros(psi.shape[0], bool)
    for d in vs:
        cs, D = coherent(j, d)
        if abs(np.vdot(cs, psi)) < 1e-8:
            nodal.append(d)
            support |= np.abs(D.conj().T @ psi) > 1e-8
    return nodal, support


def rank_gap(M, rel=1e-10):
    """Numerical rank, the smallest kept singular value, and the largest dropped one."""
    s = np.linalg.svd(M, compute_uv=False)
    r = int(np.sum(s > rel * s[0]))
    return r, s[r - 1], (s[r] if r < len(s) else 0.0)


def a5_even_invariant_degrees(N):
    """Even degrees l <= N carrying A5-invariant harmonics, listed with multiplicity.
    Molien series for the rotation group of the icosahedron on harmonics: (1 + t^15) / ((1 - t^6)(1 - t^10))."""
    c = [0] * (N + 1)
    for a in range(0, N + 1, 6):
        for b in range(0, N + 1 - a, 10):
            c[a + b] += 1
            if a + b + 15 <= N:
                c[a + b + 15] += 1
    return [l for l in range(0, N + 1, 2) for _ in range(c[l])]


def overlaps(j, v, d):
    """|<j,m| D_d^dagger v>|^2 for every m: the functions f_m of the page, evaluated at direction d."""
    _, D = coherent(j, d)
    return np.abs(D.conj().T @ v) ** 2


def rank_basis(j):
    """The multipole ranks of operators on Sym^N: eigenvectors of the adjoint Casimir sum_a [J_a, [J_a, X]], whose
    eigenvalue on rank-k operators is k(k+1). Returns each eigenvector's rank, and the eigenvectors (row-major vec)."""
    Js = spin_ops(j)
    dim = Js[0].shape[0]
    I = np.eye(dim)
    ads = [np.kron(J, I) - np.kron(I, J.T) for J in Js]
    L2 = sum(a @ a for a in ads)
    vals, vecs = np.linalg.eigh((L2 + L2.conj().T) / 2)
    ks = np.rint((-1 + np.sqrt(1 + 4 * np.clip(vals, 0, None))) / 2).astype(int)
    return ks, vecs


def rank_norms(X, ks, vecs, kmax):
    """The norm of each multipole rank k = 0..kmax of the operator X."""
    c = vecs.conj().T @ X.reshape(-1)
    return np.array([np.sqrt(np.sum(np.abs(c[ks == k]) ** 2)) for k in range(kmax + 1)])


def pattern(j, t, A, d):
    """The directional power the transfer with weights t gives the covariance A at direction d."""
    _, D = coherent(j, d)
    return float(np.real(np.trace(A @ (D @ np.diag(t).astype(complex) @ D.conj().T))))


def main():
    quats = binary_icosahedral()
    axes = axis_sets(quats)
    print("Setup. 2I as %d unit quaternions; rotation axes by order, as directions: %d five-fold, %d three-fold, %d two-fold."
          % (len(quats), len(axes[5]), len(axes[3]), len(axes[2])))
    print()

    print("T1. Covariance forces E(z) to be diagonal, leaving the N + 1 weights t_m >= 0 free.")
    rng = np.random.default_rng(3)
    rots = rng.normal(size=(6, 4))
    rots /= np.linalg.norm(rots, axis=1)[:, None]
    dirs = rng.normal(size=(6, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    for N in (12, 20, 24, 30):
        j = N / 2
        dim = N + 1
        t = rng.random(dim)
        Ez = np.diag(t / t.sum()).astype(complex)
        v = rng.normal(size=dim) + 1j * rng.normal(size=dim)
        v /= np.linalg.norm(v)
        Eg = np.outer(v, v.conj())
        d_diag = covariance_defect(j, Ez, rots, dirs)
        d_gen = covariance_defect(j, Eg, rots, dirs)
        gen = "above 1e-3, so not covariant" if d_gen > 1e-3 else "%.1e, NOT above 1e-3" % d_gen
        print("   N = %2d: diagonal E(z) with random t: covariance defect %s; a generic pure E(z): defect %s"
              % (N, bound(d_diag, 1e-12), gen))
    print("   So the admissible transfers are exactly the nonnegative weights (t_-j, ..., t_j): an (N + 1)-parameter cone,")
    print("   which normalization (sum of t = 1) cuts to an N-simplex. Positivity, covariance and normalization single out no member.")
    print()

    print("T2. The barycenter of the simplex and a vertex.")
    N = 12
    j = N / 2
    dim = N + 1
    rng2 = np.random.default_rng(11)
    B = rng2.normal(size=(dim, dim)) + 1j * rng2.normal(size=(dim, dim))
    A = B @ B.conj().T  # a positive test covariance
    trace_law = np.real(np.trace(A)) / dim
    members = {"barycenter": np.ones(dim) / dim, "Q": np.eye(dim)[0], "antipodal": np.eye(dim)[-1]}
    d5 = [np.array([0, 0, 1.0]), np.array([1, 0, 0.0]), np.array([1, 1, 1.0]) / np.sqrt(3), axes[5][0], axes[3][0]]

    def a_eff(t, d):
        _, D = coherent(j, d / np.linalg.norm(d))
        E = D @ np.diag(t).astype(complex) @ D.conj().T
        return float(np.real(np.trace(A @ E)))

    unif = np.array([a_eff(members["barycenter"], d) for d in d5])
    qv = np.array([a_eff(members["Q"], d) for d in d5])
    anti = np.array([a_eff(members["antipodal"], d) for d in d5])
    q_at_minus = np.array([a_eff(members["Q"], -d) for d in d5])
    print("   uniform t, the barycenter (P1, spectral transfer): A_eff over 5 directions spans %s, and equals Tr A/(N+1) = %.6f (%s)"
          % (bound(unif.max() - unif.min(), 1e-12), trace_law, bound(float(np.max(np.abs(unif - trace_law))), 1e-12)))
    print("   vertex t_m = delta_{m,j} (Q-symbol transfer): A_eff over the same 5 directions spans %.6f"
          % (qv.max() - qv.min()))
    print("   vertex t_m = delta_{m,-j}: equals the Q-symbol at the antipode, <-n|A|-n> (%s)"
          % bound(float(np.max(np.abs(anti - q_at_minus))), 1e-12))
    print("   Uniform t is the average of the N + 1 vertices, the barycenter of the simplex, not a vertex. It keeps the trace")
    print("   and discards every direction; the vertex at m = j keeps the coherent-state value. Different maps.")
    print()

    print("T3. Strong zero preservation (every pure source) forces the vertex at m = j: the ray through Q.")
    for N in (12, 20, 30):
        j = N / 2
        dim = N + 1
        killed = []
        for idx in range(1, dim):  # every m != j
            psi = np.zeros(dim, complex)
            psi[idx] = 1.0
            cs, _ = coherent(j, np.array([0.0, 0.0, 1.0]))
            killed.append(abs(np.vdot(cs, psi)) < 1e-12)
        print("   N = %2d: all %2d states |j,m> with m != j are nodal at the pole, each forcing its own t_m = 0: %s"
              % (N, dim - 1, "yes" if all(killed) else "NO"))
    print("   Therefore t_m = 0 for every m != j, so E(z) is a nonnegative multiple of |j,j><j,j|: the ray through Q.")
    print("   Normalization (sum of t = 1) fixes the multiple at 1, which is Q itself.")
    print()

    print("T4. Weak zero preservation (the shell's own invariant only) does NOT force Q.")
    for N, order, name in ((12, 5, "vertices"), (20, 3, "face centres"), (30, 2, "edge midpoints")):
        j = N / 2
        dim = N + 1
        ji = int(round(j))
        inv = invariant_state(j, [rep(j, q) for q in quats])
        if inv.shape[1] != 1:
            print("   N = %2d: m_N = %d, skipped (shape not unique)" % (N, inv.shape[1]))
            continue
        psi = inv[:, 0]
        vs = axes[order]
        nodal, support = weak_support(j, psi, vs)
        ms = [ji - k for k in range(dim)]
        allowed = [m for m in ms if m % order == 0]
        supp_ms = [ms[k] for k in range(dim) if support[k]]
        v = nodal[0]
        perp = [u for u in axes[2] if abs(np.dot(u, v)) < 1e-9]
        _, Dv = coherent(j, v)
        c0 = float(abs((Dv.conj().T @ psi)[ji]))  # the m = 0 entry sits at index j
        free = dim - int(support.sum())
        print("   N = %2d: %2d/%2d %s are nodal. The %d-fold stabilizer of a nodal direction allows only m = 0 mod %d"
              % (N, len(nodal), len(vs), name, order, order))
        print("           (%d values: %s); the invariant's support there is %d of them: %s"
              % (len(allowed), allowed, len(supp_ms), supp_ms))
        print("           %d half-turn axes perpendicular to the nodal axis also preserve it; each sends |j,0> to (-1)^j |j,0>,"
              % (len(perp) // 2))
        print("           and j = %d is %s, so the m = 0 amplitude of the rotated invariant is %s."
              % (ji, "odd" if ji % 2 else "even", bound(c0, 1e-12) if ji % 2 else "free (here %.4f)" % c0))
        print("           Weak preservation kills %d of the %d weights and leaves a %d-parameter cone; Q is one point in it."
              % (int(support.sum()), dim, free))
        t_alt = np.zeros(dim)
        t_alt[~support] = 1.0
        t_alt /= t_alt.sum()
        worst = 0.0
        for d in nodal:
            _, D = coherent(j, d)
            E = D @ np.diag(t_alt).astype(complex) @ D.conj().T
            worst = max(worst, abs(float(np.real(np.vdot(psi, E @ psi)))))
        probe = axes[5][0] if order != 5 else axes[3][0]
        _, Dp = coherent(j, probe)
        Ea = Dp @ np.diag(t_alt).astype(complex) @ Dp.conj().T
        Eq = Dp @ np.diag(np.eye(dim)[0]).astype(complex) @ Dp.conj().T
        va, vq = float(np.real(np.vdot(psi, Ea @ psi))), float(np.real(np.vdot(psi, Eq @ psi)))
        print("           Explicit second member (uniform on the surviving m): vanishes at every nodal direction (%s),"
              % bound(worst, 1e-15))
        print("           and at a non-nodal axis gives %.6f where Q gives %.6f. Weak preservation does not tell them apart."
              % (va, vq))
    print("   The gap between T3 and T4 is what MIT would have to supply. Preservation for the shell's own invariant can be")
    print("   formulated from the realized source alone; preservation for every pure state on the shell is a statement about")
    print("   the map; only the second gives Q.")
    print()

    print("T5. The nodal sets on the one-invariant shells, against step one's Majorana constellations.")
    for N, order, name in ((12, 5, "vertices"), (20, 3, "face centres"), (30, 2, "edge midpoints")):
        j = N / 2
        ji = int(round(j))
        psi = invariant_state(j, [rep(j, q) for q in quats])[:, 0]
        hits = {}
        for k, vs in axes.items():
            cnt = 0
            for d in vs:
                cs, _ = coherent(j, d)
                if abs(np.vdot(cs, psi)) < 1e-8:
                    cnt += 1
            hits[k] = (cnt, len(vs))
        anti = all(any(np.linalg.norm(-d - e) < 1e-8 for e in axes[order]) for d in axes[order])
        tops = set()
        for d in axes[order]:
            _, D = coherent(j, d)
            comp = np.abs(D.conj().T @ psi) > 1e-8
            tops.add(ji - int(np.argmax(comp)))  # index k holds m = j - k, so the first nonzero entry is the top m
        top = tops.pop() if len(tops) == 1 else None
        print("   N = %2d: zeros at %d/%d five-fold, %d/%d three-fold, %d/%d two-fold axes; 2j = %d zeros expected on %s; antipodally closed: %s"
              % (N, hits[5][0], hits[5][1], hits[3][0], hits[3][1], hits[2][0], hits[2][1], N, name, anti))
        print("           each zero is simple: %s"
              % ("at every nodal direction the rotated invariant's top component is m = %d = j - %d." % (top, ji - top)
                 if top is not None else "NOT one common top component"))
    print("   The zero count matches 2j = N in each case, and each nodal set is antipodally closed, so the zero set of")
    print("   the overlap and the Majorana constellation agree as sets on these shells.")
    print()

    print("T6. What reaches the prediction. Below N = 60 the source is rank one, so a transfer meets it only through")
    print("    f_m(n) = |<j,m|D_n^dagger psi_N>|^2, and the predicted pattern is sum_m t_m f_m.")
    rng6 = np.random.default_rng(5)
    sample = rng6.normal(size=(600, 3))
    sample /= np.linalg.norm(sample, axis=1)[:, None]
    xg, wg = np.polynomial.legendre.leggauss(40)
    nphi = 80
    grid = [(np.array([np.sqrt(1 - x * x) * np.cos(p), np.sqrt(1 - x * x) * np.sin(p), x]), w * 2 * np.pi / nphi)
            for x, w in zip(xg, wg) for p in np.arange(nphi) * 2 * np.pi / nphi]
    gdirs = [d for d, _ in grid]
    gw = np.array([w for _, w in grid])
    rows = []
    conv = 0.0
    for N, order in ((12, 5), (20, 3), (30, 2)):
        j = N / 2
        dim = N + 1
        psi = invariant_state(j, [rep(j, q) for q in quats])[:, 0]
        F = np.array([overlaps(j, psi, d) for d in sample])
        G = np.array([overlaps(j, psi, d) for d in gdirs])
        pair = max(float(np.max(np.abs(F[:, k] - F[:, dim - 1 - k]))) for k in range(dim))
        idev = float(np.max(np.abs(gw @ G - 4 * np.pi / dim)))
        _, support = weak_support(j, psi, axes[order])
        r_all, kept_all, drop_all = rank_gap(F)
        r_weak, kept_weak, drop_weak = rank_gap(F[:, ~support])
        degs = a5_even_invariant_degrees(N)
        distinct = sorted(set(degs))
        t_swap = np.ones(dim) / dim
        t_swap[0] += 0.5 / dim  # the vertex at m = j
        t_swap[-1] -= 0.5 / dim  # the vertex at m = -j
        flat = max(float(np.max(np.abs(F @ t_swap - 1 / dim))), float(np.max(np.abs(G @ t_swap - 1 / dim))))
        pole = np.eye(dim)[0].astype(complex)
        up = float(overlaps(j, pole, np.array([0.0, 0.0, 1.0])) @ t_swap)
        down = float(overlaps(j, pole, np.array([0.0, 0.0, -1.0])) @ t_swap)
        ks, vecs = rank_basis(j)
        mult = rank_norms(np.outer(psi, psi.conj()), ks, vecs, N)
        present = [k for k in range(N + 1) if mult[k] > 1e-10]
        absent_max = max((float(mult[k]) for k in range(N + 1) if mult[k] <= 1e-10), default=0.0)
        diag_resp = [rank_norms(np.diag(np.eye(dim)[m]).astype(complex), ks, vecs, N) for m in range(dim)]
        reach = sum(1 for k in range(N + 1) if max(r[k] for r in diag_resp) > 1e-10)
        q_ranks = sum(1 for k in range(N + 1) if diag_resp[0][k] > 1e-10)
        swap_resp = rank_norms(np.diag(t_swap - np.ones(dim) / dim).astype(complex), ks, vecs, N)
        moved = [k for k in range(N + 1) if swap_resp[k] > 1e-10]
        odd = list(range(1, N + 1, 2))
        Dy = wigner(j, np.array([0.0, 1.0, 0.0]), np.pi)
        expect = np.zeros((dim, dim))
        for k in range(dim):
            expect[dim - 1 - k, k] = (-1) ** k  # index k holds m = j - k, so j - m = k
        conv = max(conv, float(np.max(np.abs(Dy - expect))))
        print("   N = %2d: f_-m = f_m (%s); every f_m integrates to 4 pi/(N+1) (%s)."
              % (N, bound(pair, 1e-12), bound(idev, 1e-12)))
        print("           Density multipoles of psi_N nonzero at ranks %s (%d; smallest %.2g), zero at the other ranks (%s)."
              % (present, len(present), min(float(mult[k]) for k in present), bound(absent_max, 1e-12)))
        print("           Distinct even degrees <= %d carrying an A5 invariant: %s (%d; %d harmonics with multiplicity)."
              % (N, distinct, len(distinct), len(degs)))
        print("           Diagonal transfers reach %d of %d ranks, Q's E(z) answers at %d, and the weight swap changes %s."
              % (reach, N + 1, q_ranks,
                 "exactly the odd ranks (all %d of them)" % len(odd) if moved == odd else "ranks %s, NOT exactly the odd ones" % moved))
        print("           Span over all m: rank %d (smallest kept singular value %.2g, largest dropped %s);"
              % (r_all, kept_all, bound(drop_all, 1e-12)))
        print("           over the %d weights weak preservation leaves: rank %d (smallest kept %.2g, largest dropped %s)."
              % (int((~support).sum()), r_weak, kept_weak, bound(drop_weak, 1e-12)))
        print("           Weight moved from the vertex at -j to the vertex at j, t_{+-j} = (1 +- 1/2)/(N+1): on psi_N the pattern")
        print("           is P1's flat 1/(N+1) (%s); on the coherent source at the pole it is %.6f at the pole and %.6f at the antipode."
              % (bound(flat, 1e-12), up, down))
        rows.append((N, dim - 1, dim - int(support.sum()) - 1, r_all - 1, r_weak - 1))
    print("   After normalization, which is one condition since every f_m has the same integral:")
    for N, tf, tw, pf, pw in rows:
        print("   N = %2d: the transfer keeps %2d free parameters, %2d under weak preservation; the predicted pattern keeps %2d, %d under it."
              % (N, tf, tw, pf, pw))
    print("   N = 60, where the invariant is no longer unique:")
    N = 60
    j = N / 2
    dim = N + 1
    reps60 = [rep(j, q) for q in quats]
    P60 = sum(reps60) / len(reps60)
    P60 = (P60 + P60.conj().T) / 2
    plane = invariant_state(j, reps60).shape[1]
    Dy = wigner(j, np.array([0.0, 1.0, 0.0]), np.pi)
    expect = np.zeros((dim, dim))
    for k in range(dim):
        expect[dim - 1 - k, k] = (-1) ** k
    conv = max(conv, float(np.max(np.abs(Dy - expect))))

    def theta(v):
        return Dy @ v.conj()

    r60 = np.random.default_rng(7)
    v1 = r60.normal(size=dim) + 1j * r60.normal(size=dim)
    v2 = r60.normal(size=dim) + 1j * r60.normal(size=dim)
    e1 = P60 @ v1
    e1 /= np.linalg.norm(e1)
    e2 = P60 @ v2
    e2 = e2 - e1 * np.vdot(e1, e2)
    e2 /= np.linalg.norm(e2)
    generic = e1 + (0.3 + 0.7j) * e2
    generic /= np.linalg.norm(generic)
    fixed = generic + theta(generic)
    fixed /= np.linalg.norm(fixed)
    stats = {}
    for name, v in (("generic", generic), ("fixed", fixed)):
        c = abs(complex(np.vdot(v, theta(v))))
        pair = max(float(np.max(np.abs(fv - fv[::-1]))) for fv in (overlaps(j, v, d) for d in sample[:150]))
        qodd = max(abs(float(overlaps(j, v, d)[0] - overlaps(j, v, -d)[0])) for d in sample[:150])
        stats[name] = (c, pair, qodd)
    c, pair, qodd = stats["generic"]
    print("           The invariants form a plane (dimension %d). A generic one is not fixed by time reversal (|<v|Theta v>| = %.2g):"
          % (plane, c))
    print("           its pairing fails (max |f_m - f_-m| = %.2g) and its constellation is not centrally symmetric (max |Q(n) - Q(-n)| = %.2g)."
          % (pair, qodd))
    c, pair, qodd = stats["fixed"]
    print("           A time-reversal-fixed one pairs (%s), with an even Q-function (%s): below N = 60, uniqueness is what forces the pairing."
          % (bound(pair, 1e-12), bound(qodd, 1e-12)))
    print("   Time reversal throughout is exp(-i pi J_y) then complex conjugation, Theta v_m = (-1)^(j-m) v_-m at N = 12, 20, 30 and 60")
    print("   (%s): the Surviving Ray's Theta_j with epsilon_j = 1." % bound(conv, 1e-12))
    print("   Most of the cone never reaches a rank-one source. The weak condition leaves the predicted pattern undetermined,")
    print("   by the amounts in the last column, and leaves the map undetermined by more.")
    print()

    print("T7. The real-field quotient. A real field's covariance commutes with time reversal, so only the pair sums")
    print("    u_0 = t_0 and u_m = t_m + t_-m act on it; what the weak family leaves open runs through a sign change.")
    rng7 = np.random.default_rng(21)
    dirs7 = rng7.normal(size=(200, 3))
    dirs7 /= np.linalg.norm(dirs7, axis=1)[:, None]
    real_rows = []
    for N, order in ((12, 5), (20, 3), (30, 2)):
        j = N / 2
        dim = N + 1
        ji = int(round(j))
        Dy = np.real(wigner(j, np.array([0.0, 1.0, 0.0]), np.pi))

        def theta_op(X):
            return Dy @ X.conj() @ Dy.T

        B = rng7.normal(size=(dim, dim)) + 1j * rng7.normal(size=(dim, dim))
        A = B @ B.conj().T
        AR = A + theta_op(A)  # a positive, time-reversal-invariant covariance
        inv_defect = float(np.max(np.abs(theta_op(AR) - AR)))
        t1 = rng7.random(dim)
        t1 /= t1.sum()
        t2 = np.array([(t1[k] + t1[dim - 1 - k]) / 2 for k in range(dim)])  # the same pair sums, split evenly
        d_real = max(abs(pattern(j, t1, AR, d) - pattern(j, t2, AR, d)) for d in dirs7[:80])
        d_cplx = max(abs(pattern(j, t1, A, d) - pattern(j, t2, A, d)) for d in dirs7[:80])
        q_anti = max(abs(pattern(j, np.eye(dim)[0], AR, d) - pattern(j, np.eye(dim)[-1], AR, d)) for d in dirs7[:80])
        sym = []
        for m in range(ji + 1):
            t = np.zeros(dim)
            t[ji - m] += 0.5
            t[ji + m] += 0.5
            sym.append(t)
        M = np.array([[pattern(j, t, AR, d) for t in sym] for d in dirs7])
        r_real, _, _ = rank_gap(M)
        fixed_ok = True
        for m0 in range(ji):
            for alpha in (0.0, 1.1):
                v = np.zeros(dim, complex)
                v[ji - m0] += 1.0
                v[ji + m0] += np.exp(1j * alpha)
                v /= np.linalg.norm(v)
                fixed_ok &= abs(abs(np.vdot(v, Dy @ v.conj())) - 1) < 1e-12 and abs(v[0]) < 1e-15
        psi = invariant_state(j, [rep(j, q) for q in quats])[:, 0]
        _, support = weak_support(j, psi, axes[order])
        ms = [ji - k for k in range(dim)]
        killed = sorted({abs(ms[k]) for k in range(dim) if support[k]})
        left = ji + 1 - len(killed)
        ks, vecs = rank_basis(j)
        X = np.diag(np.eye(dim)[0]).astype(complex)
        c = vecs.conj().T @ X.reshape(-1)
        sel = ks == 6
        Z6 = (vecs[:, sel] @ c[sel]).reshape(dim, dim)
        Z6 /= np.linalg.norm(Z6)  # the zonal rank-6 operator, signed so that <j,j|Z6|j,j> > 0
        r6 = np.real(np.diag(Z6)) * np.sqrt(dim)  # e_6/e_0 at each vertex, since e_0 = 1/sqrt(dim) on the simplex
        allowed = [k for k in range(dim) if not support[k]]
        lo = min(allowed, key=lambda k: r6[k])
        hi = max(allowed, key=lambda k: r6[k])
        ex = float(np.mean([r6[k] for k in allowed]))
        print("   N = %2d: on a random time-reversal-invariant covariance (invariance %s), two transfers with the same pair sums"
              % (N, bound(inv_defect, 1e-12)))
        print("           agree (%s); on a generic covariance they differ (%s); Q and the antipodal Q agree on it (%s)."
              % (bound(d_real, 1e-12), "above 1e-3" if d_cplx > 1e-3 else "%.1e, NOT above 1e-3" % d_cplx, bound(q_anti, 1e-12)))
        print("           The j + 1 = %d pair-sum vertices give independent patterns on it (rank %d). The time-reversal-fixed states"
              % (ji + 1, r_real))
        print("           |j,0> and (|j,m0> + e^{ia}|j,-m0>)/sqrt 2, 0 < m0 < j, are nodal at the pole: %s." % ("yes" if fixed_ok else "NO"))
        print("           Weak preservation kills the pair sums at |m| = %s and leaves %d of %d." % (killed, left, ji + 1))
        print("           Leading anisotropic response (rank 6 over rank 0) across the weak family, as a ratio to Q's: from %+.3f (|m| = %d)"
              % (r6[lo] / r6[0], abs(ms[lo])))
        print("           to %+.3f (|m| = %d); the exhibited second member sits at %+.3f." % (r6[hi] / r6[0], abs(ms[hi]), ex / r6[0]))
        real_rows.append((ji, left - 1))
    print("   After normalization the real-field map keeps %s free parameters, and %s under weak preservation."
          % (", ".join(str(r[0]) for r in real_rows), ", ".join(str(r[1]) for r in real_rows)))


if __name__ == "__main__":
    main()
