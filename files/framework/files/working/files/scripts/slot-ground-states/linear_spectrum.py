"""The Slot Ground States, §V: the linear spectrum about the rigid families (Theorem D).

Checks, each able to fail:
  1. the binary icosahedral group 2I (120 unit quaternions) closes; for n = 0 to 5 the restriction of Sym^n C^2
     to 2I is irreducible, occurs at level n and next at level 12 - n, and the gap
     (12 - n)(14 - n) - n(n + 2) equals 28 (6 - n); at n = 6 the restriction is reducible, the control on the
     premise; with level 12's character replaced by level 14's, the occurrence check fails;
  2. on the lowest level, the real linearization about e^{i omega T} pi_n(x) v, for random v, g, c and R, has
     the eigenvalues 0 (algebraic multiplicity 2n + 2, geometric 2n + 1), +-2i omega (n times each) and
     +-i (4 omega^2 + 2 g c^2 |v|^2)^(1/2); with the coupling at 3g, or with the gyroscopic term dropped, it fails;
  3. on finite models with the same structure (sample points x of SU(2), frames pi_n(x), the profile pi_n(x) v,
     an operator that vanishes on the lowest level and has a gap above it): the coupling preserves the lowest
     level and its complement, H_2 is conserved and positive definite on the complement, every eigenvalue is
     imaginary, and the kernel has dimensions 2n + 1 and 2n + 2; arms: a profile of non-constant norm breaks the
     splitting, H_2 with the coupling at 2g is not conserved, and an operator below -omega^2/c^2 puts an
     eigenvalue off the axis.
Double precision throughout. Runs in a few seconds.
"""
import itertools

import numpy as np
from scipy.linalg import expm

PHI = (1 + 5 ** 0.5) / 2


def binary_icosahedral():
    def parity(p):
        p, s = list(p), 0
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                s ^= 1
        return s

    els = set()
    for i in range(4):
        for sg in (1.0, -1.0):
            v = [0.0] * 4
            v[i] = sg
            els.add(tuple(v))
    for sg in itertools.product((0.5, -0.5), repeat=4):
        els.add(sg)
    base = (0.0, 0.5, 0.5 / PHI, 0.5 * PHI)  # even permutations of (0, 1, 1/phi, phi)/2
    for p in itertools.permutations(range(4)):
        if parity(p):
            continue
        for s1, s2, s3 in itertools.product((1, -1), repeat=3):
            vals = (0.0, s1 * base[1], s2 * base[2], s3 * base[3])
            v = [0.0] * 4
            for k in range(4):
                v[p[k]] = vals[k]
            els.add(tuple(round(x, 12) + 0.0 for x in v))
    els = sorted(els)
    assert len(els) == 120
    return [np.array(e) for e in els]


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def spin_matrices(j2):
    j = j2 / 2
    ms = [j - k for k in range(j2 + 1)]
    d = j2 + 1
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - ms[k] * (ms[k] + 1))
    Jm = Jp.conj().T
    return (Jp + Jm) / 2, (Jp - Jm) / 2j, np.diag(ms).astype(complex)


def rep(j2, q):  # Sym^{j2} C^2 at the unit quaternion q
    a, v = q[0], np.array(q[1:])
    s = np.linalg.norm(v)
    if s < 1e-15:
        return np.eye(j2 + 1, dtype=complex) * (1.0 if a > 0 else (-1.0) ** j2)
    t, n = 2 * np.arctan2(s, a), v / s
    Jx, Jy, Jz = spin_matrices(j2)
    return expm(-1j * t * (n[0] * Jx + n[1] * Jy + n[2] * Jz))


def chi(K, q):  # character of Sym^K C^2 at q: sin((K + 1) a) / sin(a), with cos(a) = Re q
    a = np.arccos(np.clip(q[0], -1.0, 1.0))
    if abs(np.sin(a)) < 1e-12:
        return float((K + 1) * (1 if q[0] > 0 else (-1) ** K))
    return float(np.sin((K + 1) * a) / np.sin(a))


G = binary_icosahedral()
keys = {tuple(np.round(g, 9) + 0.0) for g in G}
assert all(tuple(np.round(qmul(g, h), 9) + 0.0) in keys for g in G for h in G)


# ---------------------------------------------------------------- 1. the gap above the lowest level
def gap_verdicts(chi_fn):
    ok = {"irreducible": True, "occurrences": True, "gap": True, "control": True}
    rows = []
    for n in range(6):
        cn = np.array([chi_fn(n, g) for g in G])
        ok["irreducible"] &= bool(abs(np.mean(cn * cn) - 1) < 1e-9)
        occ = []
        for K in range(20):
            m = np.mean(cn * np.array([chi_fn(K, g) for g in G]))
            ok["occurrences"] &= bool(abs(m - round(m)) < 1e-9)
            if round(m) > 0:
                occ.append(K)
        ok["occurrences"] &= len(occ) >= 2 and occ[0] == n and occ[1] == 12 - n
        gap = (occ[1] * (occ[1] + 2) - n * (n + 2)) if len(occ) >= 2 else None
        ok["gap"] &= gap == 28 * (6 - n)
        rows.append((n, tuple(occ[:2]), gap))
    c6 = np.array([chi_fn(6, g) for g in G])
    ok["control"] &= bool(abs(np.mean(c6 * c6) - 2) < 1e-9)
    return ok, rows


ok, rows = gap_verdicts(chi)
assert all(ok.values()), ok
print("1. 2I closes. Rigid n: (first, second occurrence), R^2 (lambda_1 - lambda_0) =", rows,
      "; Sym^6 restricted to 2I has norm 2 (reducible)")
ok, _ = gap_verdicts(lambda K, q: chi(14 if K == 12 else K, q))
assert not ok["occurrences"] and not ok["gap"], ok
print("   arm: with level 12's character replaced by level 14's, the occurrence and gap checks fail")


# ---------------------------------------------------------------- 2. the lowest level, exactly
def lowest_block(v, g, c, om, coup=2.0, gyro=True):
    """Real form of u_TT + 2 i om u_T + coup g c^2 Re(v^dag u) v = 0, state (Re u, Im u, Re u_T, Im u_T)."""
    d = len(v)
    I = np.eye(d)
    A = np.zeros((4 * d, 4 * d))
    A[0:d, 2 * d:3 * d] = I
    A[d:2 * d, 3 * d:4 * d] = I
    if gyro:  # -2 i om w: real part +2 om Im w, imaginary part -2 om Re w
        A[2 * d:3 * d, 3 * d:4 * d] = 2 * om * I
        A[3 * d:4 * d, 2 * d:3 * d] = -2 * om * I
    k = coup * g * c ** 2
    p = np.concatenate([v.real, v.imag])  # Re(v^dag u) = p . (Re u, Im u)
    A[2 * d:4 * d, 0:2 * d] -= k * np.outer(p, p)
    return A


def nullity(M, tol):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < tol * max(1.0, s[0])))


def lowest_verdicts(seed, coup=2.0, gyro=True, trials=4):
    rng = np.random.default_rng(seed)
    ok = {"zeros": True, "kernel": True, "axis": True, "spectrum": True}
    worst = 0.0
    for n in range(6):
        for _ in range(trials):
            v = rng.normal(size=n + 1) + 1j * rng.normal(size=n + 1)
            g, c, R = rng.uniform(0.3, 3.0, size=3)
            v2 = np.vdot(v, v).real
            om = c * np.sqrt(n * (n + 2) / R ** 2 + g * v2)
            A = lowest_block(v, g, c, om, coup, gyro)
            ev = np.linalg.eigvals(A)
            sc = max(1.0, np.abs(ev).max())
            zero, rest = ev[np.abs(ev) < 1e-5 * sc], ev[np.abs(ev) >= 1e-5 * sc]
            ok["zeros"] &= len(zero) == 2 * n + 2
            ok["kernel"] &= nullity(A, 1e-10) == 2 * n + 1 and nullity(A @ A, 1e-10) == 2 * n + 2
            ok["axis"] &= bool(np.abs(rest.real).max(initial=0.0) < 1e-9 * sc)
            amp = np.sqrt(4 * om ** 2 + 2 * g * c ** 2 * v2)
            want = sorted([2 * om] * n + [-2 * om] * n + [amp, -amp])
            got = sorted(rest.imag)
            same = len(got) == len(want) and np.allclose(got, want, rtol=1e-9, atol=1e-9 * sc)
            ok["spectrum"] &= bool(same)
            if same:
                worst = max(worst, max((abs(a - b) for a, b in zip(got, want)), default=0.0) / sc)
    return ok, worst


ok, worst = lowest_verdicts(5)
assert all(ok.values()), ok
print(f"2. lowest level, n = 0..5, 4 random members each: the spectrum is as stated (worst relative deviation "
      f"{worst:.1e}); 0 has algebraic multiplicity 2n + 2 and geometric 2n + 1")
for label, kw in (("coupling at 3g", {"coup": 3.0}), ("gyroscopic term dropped", {"gyro": False})):
    ok, _ = lowest_verdicts(5, **kw)
    assert not ok["spectrum"], (label, ok)
    print(f"   arm: with the {label}, the spectrum check fails")


# ---------------------------------------------------------------- 3. finite models of the higher levels
def realform(M):
    return np.block([[M.real, -M.imag], [M.imag, M.real]])


def random_su2(rng):
    q = rng.normal(size=4)
    return q / np.linalg.norm(q)


def model(n, rng, gap, g, c, om, N=6, profile_scale=None, q_coup=1.0):
    """Perturbations on N sample points of SU(2), values in C^{n+1}; frames pi_n(x); E_0 = {pi_n(x) u}."""
    d = n + 1
    frames = [rep(n, random_su2(rng)) for _ in range(N)]
    v = rng.normal(size=d) + 1j * rng.normal(size=d)
    s = np.ones(N) if profile_scale is None else profile_scale
    phis = [s[x] * frames[x] @ v for x in range(N)]
    D = N * d
    B0 = np.concatenate(frames, axis=0) / np.sqrt(N)  # orthonormal basis of E_0
    P0 = B0 @ B0.conj().T
    Pp = np.eye(D) - P0
    X = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
    K = Pp @ (gap * np.eye(D) + X @ X.conj().T / D) @ Pp  # zero on E_0; at least `gap` on its complement
    C = np.zeros((2 * D, 2 * D))  # Re(phi_x^dag zeta_x) phi_x, pointwise
    for x in range(N):
        p = np.zeros(2 * D)
        p[x * d:(x + 1) * d] = phis[x].real
        p[D + x * d:D + (x + 1) * d] = phis[x].imag
        C += np.outer(p, p)
    Kr, Jr, P0r = realform(K), realform(1j * np.eye(D)), realform(P0)
    Z = np.zeros((2 * D, 2 * D))
    A = np.block([[Z, np.eye(2 * D)], [-c ** 2 * Kr - 2 * g * c ** 2 * C, -2 * om * Jr]])
    Q = np.block([[Kr + 2 * q_coup * g * C, Z], [Z, np.eye(2 * D) / c ** 2]])
    return A, Q, C, P0r


def model_verdicts(seed, models=3, nonunit=False, q_coup=1.0, below=False):
    rng = np.random.default_rng(seed)
    ok = {"split": True, "conserved": True, "positive": True, "axis": True, "kernel": True}
    for n in range(6):
        for _ in range(models):
            g, c, om = rng.uniform(0.3, 3.0, size=3)
            gap = -2 * om ** 2 / c ** 2 if below else rng.uniform(0.5, 3.0)
            scale = rng.uniform(0.5, 2.0, size=6) if nonunit else None
            A, Q, C, P0r = model(n, rng, gap, 0.0 if below else g, c, om, profile_scale=scale, q_coup=q_coup)
            M = len(P0r)
            Ppr = np.eye(M) - P0r
            ok["split"] &= bool(max(np.abs(P0r @ C @ Ppr).max(), np.abs(Ppr @ C @ P0r).max()) < 1e-10)
            ok["conserved"] &= bool(np.abs(Q @ A + A.T @ Q).max() / np.abs(Q).max() < 1e-12)
            Bp = np.linalg.svd(Ppr)[0][:, :M - 2 * (n + 1)]  # real basis of the complement
            Qp = Bp.T @ Q[:M, :M] @ Bp
            ok["positive"] &= bool(np.linalg.eigvalsh(Qp).min() > 1e-9)
            ev = np.linalg.eigvals(A)
            sc = max(1.0, np.abs(ev).max())
            far = ev[np.abs(ev) >= 1e-5 * sc]
            ok["axis"] &= bool(np.abs(far.real).max(initial=0.0) < 1e-8 * sc)
            ok["kernel"] &= nullity(A, 1e-10) == 2 * n + 1 and nullity(A @ A, 1e-10) == 2 * n + 2
    return ok


ok = model_verdicts(7)
assert all(ok.values()), ok
print("3. finite models, n = 0..5, 3 each: the coupling preserves E_0 and its complement; H_2 is conserved and "
      "positive definite on the complement; every eigenvalue is imaginary; 0 has algebraic multiplicity 2n + 2 "
      "and geometric 2n + 1")
for label, kw, target in (("a profile of non-constant norm", {"nonunit": True}, "split"),
                          ("H_2 built with the coupling at 2g", {"q_coup": 2.0}, "conserved"),
                          ("an operator below -omega^2/c^2 on the complement", {"below": True}, "axis")):
    ok = model_verdicts(7, **kw)
    assert not ok[target], (label, ok)
    print(f"   arm: with {label}, the {target} check fails")
print("ALL CHECKS PASS")
