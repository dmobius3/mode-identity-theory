#!/usr/bin/env python3
"""The quotient-specific half of item 5: what separates the Molien shells' spectral data from the quotient's invariant modes.
Group theory and polynomial identities only: no CMB quantity, no shell weight, no E8 input, no sky covariance.

S^3 = SU(2) as unit quaternions, 2I acting on the left. U_N is the Chebyshev polynomial of the second kind, the character of
Sym^N: chi_N(g) = U_N(Re g). For unit quaternions Re(a b^-1) is the 4-vector dot product a.b.
  A. The Molien multiplicity is a character average, m_N = (1/120) sum_g U_N(Re g). The central pair +-1 gives
     (N+1)(1+(-1)^N)/120; the 118 non-central elements supply the rest, including every zero at N = 2 to 10.
  B. The quotient's shell kernel is the image sum K_P(x, y) = (1/120) sum_g U_N((g x).y): invariant under 2I in each
     argument separately, equal to m_N on the diagonal, and equal to m_N at every image pair (x, g x).
  C. About a point, the central terms of K_P are isotropic and all of its anisotropy comes from the non-central images: the
     spherical-harmonic content of K_P(1, exp(eps n)) in the direction n.
  D. On the cover, a homogeneous law on shell N has covariance K_A(x, y) = Tr(A rho_N(x y^-1)). A = I (every sector equally)
     is isotropic; A = P (the quotient's invariants) and A = I - P (every other sector) are A5-anisotropic, with image-pair
     correlations away from the isotropic baseline. The nearest images lie along the icosahedron's 12 vertex directions.
  E. The 2I character table, and the Sym^N multiplicities: anisotropy with baseline image correlations needs a repeated
     constituent, and this finds where the first one occurs.
  F. Sym^N as unitary matrices (exp of its Lie-algebra action): a homomorphism with character U_N. In it the quotient's kernel
     is Tr(P rho_N(x y^-1)), P = (1/120) sum_g rho_N(g), and a central law's kernel is the character-weighted image sum. The
     weighting is fixed only up to absent constituents, so the whole-shell law has more than one.
  G. The homogeneous laws on the cover's shell N with the observer's A5 are the positive elements of the commutant of
     rho_N(2I); its dimension is the sum of squared multiplicities, the number of A5-invariant harmonics of degree <= N
     (for real kernels, the even-degree ones), and its center is spanned by the isotypic projectors.
  H. In the center, the image correlations Tr(A rho_N(g))/Tr A sit at the isotropic baseline U_N(Re g)/(N+1) at every g only
     when A is a multiple of I, because the constituents' characters are independent on 2I.
  I. Outside the center, which needs a repeated constituent (none at N = 12; present at N = 20, 24, 30), a traceless part T
     commutes with 2I and not with SU(2), changes no image correlation, and gives the local correlation an A5-invariant
     anisotropy; I + T/2 is a positive law with a real kernel.
"""
import itertools

import numpy as np
from scipy.linalg import expm
from scipy.special import eval_chebyu
try:
    from scipy.special import sph_harm_y

    def Yl(l, m, th, ph):
        return sph_harm_y(l, m, th, ph)
except ImportError:
    from scipy.special import sph_harm

    def Yl(l, m, th, ph):
        return sph_harm(m, l, ph, th)

PHI = (1 + 5 ** 0.5) / 2
rng = np.random.default_rng(5)


def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def qmul_arr(A, b):
    w1, x1, y1, z1 = A.T
    w2, x2, y2, z2 = b
    return np.stack([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2], axis=1)


def qinv(a):
    return np.array([a[0], -a[1], -a[2], -a[3]])


def rand_unit():
    q = rng.normal(size=4)
    return q / np.linalg.norm(q)


def even_perms(v):
    for p in itertools.permutations(range(4)):
        if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0:
            yield tuple(v[i] for i in p)


els = {}
for i in range(4):
    for s in (1.0, -1.0):
        e = np.zeros(4)
        e[i] = s
        els[tuple(np.round(e, 9))] = e
for sg in itertools.product((0.5, -0.5), repeat=4):
    els[tuple(np.round(sg, 9))] = np.array(sg)
for sg in itertools.product((1, -1), repeat=3):
    for p in even_perms((0.0, 0.5 * sg[0], 0.5 * sg[1] / PHI, 0.5 * sg[2] * PHI)):
        els[tuple(np.round(p, 9))] = np.array(p)
G = np.array(list(els.values()))
Re = G[:, 0]
central = np.isclose(np.abs(Re), 1.0)
assert len(G) == 120 and central.sum() == 2
c = np.zeros(131, dtype=int)
c[0] = 1
for s in (12, 20):
    for r in range(s):
        c[r::s] = np.cumsum(c[r::s])
m = c.copy()
m[30:] += c[:-30]


def U(N, x):
    return eval_chebyu(N, np.clip(x, -1.0, 1.0))


print("A. The Molien multiplicity as a character average over 2I, split into the central pair and the 118 others")
okA = all(abs(U(N, Re).sum() / 120 - m[N]) < 1e-9 for N in range(0, 61))
print(f"   m_N = (1/120) sum_g U_N(Re g) for N = 0 to 60: {okA}")
print("    N   central pair   118 non-central   total   m_N")
for N in (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 30):
    cp, nc = U(N, Re[central]).sum() / 120, U(N, Re[~central]).sum() / 120
    print(f"   {N:2d}   {cp:+12.6f}   {nc:+15.6f}   {cp + nc:+6.3f}   {m[N]}")


def KP(N, x, y):
    return U(N, qmul_arr(G, x) @ y).mean()


print("\nB. The quotient's shell kernel as the image sum K_P(x, y) = (1/120) sum_g U_N((g x).y)")
for N in (12, 20, 30):
    x, y, g1 = rand_unit(), rand_unit(), G[rng.integers(120)]
    inv = max(abs(KP(N, qmul(g1, x), y) - KP(N, x, y)), abs(KP(N, x, qmul(g1, y)) - KP(N, x, y)))
    diag = max(abs(KP(N, z, z) - m[N]) for z in (rand_unit() for _ in range(5)))
    img = max(abs(KP(N, x, qmul(g, x)) - m[N]) for g in G)
    print(f"   N = {N}: invariant under 2I in each argument to {inv:.0e}; K_P(x, x) = m_N = {m[N]} to {diag:.0e}; "
          f"K_P(x, g x) = m_N at all 120 images to {img:.0e}")

nth, nph, LMAX = 48, 96, 30
xg, wg = np.polynomial.legendre.leggauss(nth)
TH, PH = np.repeat(np.arccos(xg), nph), np.tile(2 * np.pi * np.arange(nph) / nph, nth)
W = np.repeat(wg, nph) * 2 * np.pi / nph
NV = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)], axis=1)
YT = {(l, mm): Yl(l, mm, TH, PH) for l in range(LMAX + 1) for mm in range(-l, l + 1)}


def power(f):
    return np.array([sum(abs(np.sum(W * f * np.conj(YT[(l, mm)]))) ** 2 for mm in range(-l, l + 1)) for l in range(LMAX + 1)])


def ydir(eps, n):
    return np.concatenate([np.full((len(n), 1), np.cos(eps)), np.sin(eps) * n], axis=1)


def ad(b, n):
    return np.array([qmul(qmul(b, np.concatenate([[0.0], v])), qinv(b))[1:] for v in n])


inv_degrees = [l for l in range(LMAX + 1) if m[2 * l] > 0]
eps = 0.3
print(f"\nC. K_P(1, exp(eps n)) as a function of the direction n, eps = {eps} rad; degrees l <= {LMAX} carrying A5 invariants: "
      f"{inv_degrees}")
for N in (12, 20, 30):
    dots = ydir(eps, NV) @ G.T
    fc, fnc = U(N, dots[:, central]).sum(1) / 120, U(N, dots[:, ~central]).sum(1) / 120
    pc, pn = power(fc), power(fnc)
    present = [l for l in range(LMAX + 1) if pn[l] > 1e-24 * pn.sum()]
    probe = rng.normal(size=(30, 3))
    probe /= np.linalg.norm(probe, axis=1, keepdims=True)
    fprobe = U(N, ydir(eps, probe) @ G[~central].T).sum(1) / 120
    a5 = max(np.max(abs(U(N, ydir(eps, ad(b, probe)) @ G[~central].T).sum(1) / 120 - fprobe)) for b in G)
    print(f"   N = {N}: central part isotropic (its direction-dependent rms {np.sqrt(pc[1:].sum() / pc[0]):.0e} of its mean); "
          f"non-central part carries l = {present}, all among the A5-invariant degrees: {set(present) <= set(inv_degrees)}; "
          f"its direction-dependent rms {np.sqrt(pn[1:].sum() / (4 * np.pi)) / m[N]:.2e} of the variance m_N; invariant under "
          f"the 60 rotations to {a5:.0e}")

print(f"\nD. Three homogeneous laws on the cover's shell N (eps = {eps} rad for the direction dependence)")
near = G[np.isclose(Re, PHI / 2)]
ico = np.array([np.array(v, float) for cc in ((0, 1, PHI), (1, PHI, 0), (PHI, 0, 1)) for v in itertools.product(*[(s, -s) if s else (0,) for s in cc])])
ico /= np.linalg.norm(ico, axis=1, keepdims=True)
dirs = near[:, 1:] / np.linalg.norm(near[:, 1:], axis=1, keepdims=True)
match = all(np.min(np.linalg.norm(ico - d, axis=1)) < 1e-9 for d in dirs) and len(near) == 12
print(f"   the nearest images of a point, at distance pi R/5, lie along the icosahedron's 12 vertex directions: {match}")
for N in (12, 20):
    dots = ydir(eps, NV) @ G.T
    fI = np.full(len(NV), U(N, np.cos(eps)))
    fP = U(N, dots).sum(1) / 120
    probe = rng.normal(size=(20, 3))
    probe /= np.linalg.norm(probe, axis=1, keepdims=True)
    b_rand = rand_unit()
    rows = []
    for name, f, kfun in (("A = I", fI, lambda yq: U(N, yq[:, 0])),
                          ("A = P", fP, lambda yq: U(N, yq @ G.T).sum(1) / 120),
                          ("A = I - P", fI - fP, lambda yq: U(N, yq[:, 0]) - U(N, yq @ G.T).sum(1) / 120)):
        pw = power(f)
        base = kfun(ydir(eps, probe))
        rot2i = max(np.max(abs(kfun(ydir(eps, ad(b, probe))) - base)) for b in G)
        rotany = np.max(abs(kfun(ydir(eps, ad(b_rand, probe))) - base))
        rows.append((name, np.sqrt(pw[1:].sum() / (4 * np.pi)), rot2i, rotany))
    x = rand_unit()
    tr = {"A = I": N + 1, "A = P": m[N], "A = I - P": N + 1 - m[N]}
    kimg = {"A = I": U(N, np.dot(x, qmul(near[0], x))), "A = P": KP(N, x, qmul(near[0], x))}
    kimg["A = I - P"] = kimg["A = I"] - kimg["A = P"]
    print(f"   shell N = {N} (m_N = {m[N]}); nearest-image correlation baseline U_N(phi/2)/(N+1) = {U(N, PHI / 2) / (N + 1):+.4f}")
    for name, aniso, rot2i, rotany in rows:
        print(f"     {name:9s}: direction-dependent rms of the correlation {aniso / tr[name]:.2e}; invariant under the observer's 60 rotations to {rot2i:.0e}, under a "
              f"random rotation to {rotany:.0e}; nearest-image correlation {kimg[name] / tr[name]:+.4f}")


def galois(r):
    out = r.copy()
    for a, b in ((PHI / 2, -1 / (2 * PHI)), (-1 / (2 * PHI), PHI / 2), (-PHI / 2, 1 / (2 * PHI)), (1 / (2 * PHI), -PHI / 2)):
        out[np.isclose(r, a)] = b
    return out


CH = {"1": np.ones(120), "2": U(1, Re), "2'": U(1, galois(Re)), "3": U(2, Re), "3'": U(2, galois(Re)),
      "4": U(1, Re) * U(1, galois(Re)), "4s": U(3, Re), "5": U(4, Re), "6": U(5, Re)}
names = list(CH)
gram = np.array([[np.dot(CH[a], CH[b]) / 120 for b in names] for a in names])
dims = [int(round(CH[n][np.isclose(Re, 1.0)][0])) for n in names]
print(f"\nE. The nine irreducible characters of 2I ({', '.join(names)}; 4 is A5's, 4s the spinorial one, spin 3/2), dimensions "
      f"{dims}, squares summing to {sum(d * d for d in dims)}; orthonormal to {np.max(abs(gram - np.eye(9))):.0e}")


def mult(N):
    return {n: int(round(np.dot(U(N, Re), CH[n]) / 120)) for n in names}


first_any = next(N for N in range(0, 60) if max(mult(N).values()) >= 2)
first_even = next(N for N in range(0, 60, 2) if max(mult(N).values()) >= 2)
print(f"   the first Sym^N with a repeated 2I constituent: N = {first_any}; among even N: N = {first_even}")
for N in (12, 16, 20, 24, 30):
    dec = " + ".join((f"{k}x" if k > 1 else "") + n for n, k in mult(N).items() if k)
    print(f"   Sym^{N}: {dec}")


def su2(q):
    w, x, y, z = q
    return np.array([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]])


def dsym(N, A):
    """The derivative of Sym^N at the identity along the 2x2 matrix A, in the orthonormal basis sqrt(C(N, k)) u^(N-k) v^k."""
    k = np.arange(N + 1)
    D = np.diag((N - k) * A[0, 0] + k * A[1, 1])
    D[k[:-1] + 1, k[:-1]] = A[1, 0] * np.sqrt((N - k[:-1]) * (k[:-1] + 1))
    D[k[1:] - 1, k[1:]] = A[0, 1] * np.sqrt(k[1:] * (N - k[1:] + 1))
    return D


def sym(N, q):
    """Sym^N of the unit quaternion q = cos t + v sin t, as exp(t dSym^N(v))."""
    s = np.linalg.norm(q[1:])
    if s < 1e-12:
        return np.eye(N + 1, dtype=complex) * np.sign(q[0]) ** N
    return expm(np.arctan2(s, q[0]) * dsym(N, su2(np.concatenate([[0.0], q[1:] / s]))))


DIM = dict(zip(names, dims))
JQ = np.array([0.0, 0.0, 1.0, 0.0])


def shell(N):
    R = [sym(N, g) for g in G]
    return R, {n: DIM[n] / 120 * sum(CH[n][i] * R[i] for i in range(120)) for n, k in mult(N).items() if k}


def img(R, A):
    return np.array([np.trace(A @ Rg).real for Rg in R]) / np.trace(A).real


SH = {N: shell(N) for N in (12, 20, 24, 30)}
print("\nF. Sym^N as unitary matrices, in which the quotient's kernel and every central law are image sums")
for N in (12, 20, 30):
    R, Pr = SH[N]
    a, b = rand_unit(), rand_unit()
    hom = np.max(abs(sym(N, qmul(a, b)) - sym(N, a) @ sym(N, b)))
    uni = np.max(abs(sym(N, a) @ sym(N, a).conj().T - np.eye(N + 1)))
    chi = max(abs(np.trace(Rg) - U(N, g[0])) for Rg, g in zip(R, G))
    wts = {n: rng.uniform(0.2, 1.0) for n in Pr}
    A = sum(wts[n] * Pr[n] for n in Pr)
    w = sum(wts[n] * DIM[n] * CH[n] for n in Pr)
    wI = sum(DIM[n] * CH[n] for n in Pr)
    kp = form = ki = 0.0
    for _ in range(5):
        x, y = rand_unit(), rand_unit()
        z = sym(N, qmul(x, qinv(y)))
        kp = max(kp, abs(np.trace(Pr["1"] @ z) - KP(N, x, y)))
        form = max(form, abs(np.trace(A @ z) - (w * U(N, qmul_arr(G, x) @ y)).sum() / 120))
        ki = max(ki, abs((wI * U(N, qmul_arr(G, x) @ y)).sum() / 120 - U(N, np.dot(x, y))))
    print(f"   N = {N}: a homomorphism to {hom:.0e}, unitary to {uni:.0e}, trace U_N(Re g) at all 120 to {chi:.0e}; "
          f"Tr(P rho_N(x y^-1)) = K_P(x, y) to {kp:.0e}; a random central law equals its character-weighted image sum to {form:.0e}")
    print(f"      the whole-shell law weighted over its constituents: w = {wI[np.isclose(Re, 1.0)][0]:.0f} at g = 1 and "
          f"{wI[np.isclose(Re, -1.0)][0]:.0f} at g = -1, at most {np.max(abs(wI[~central])):.2f} off the central pair; its kernel is "
          f"U_N(x.y) to {ki:.0e}, as it is with w = 120 at g = 1 alone")

print("\nG. The laws on the cover's shell N with the observer's A5: the commutant of rho_N(2I)")
ok_all = all(sum(k * k for k in mult(N).values()) == sum(m[2 * L] for L in range(N + 1)) for N in range(0, 61))
ok_real = all(sum(k * (k + 1) // 2 for k in mult(N).values()) == sum(m[2 * L] for L in range(0, N + 1, 2)) for N in range(0, 61, 2))
print(f"   dimension = sum of squared multiplicities = number of A5-invariant harmonics of degree <= N (N = 0 to 60): {ok_all}; "
      f"real kernels, sum of m(m+1)/2 = number of even-degree ones (even N): {ok_real}")
for N in (12, 20, 24, 30):
    R, Pr = SH[N]
    Rey = sum(np.kron(Rg, Rg.conj()) for Rg in R) / 120
    ev = np.linalg.eigvalsh((Rey + Rey.conj().T) / 2)
    print(f"   N = {N}: the average over 2I is a projector to {np.max(abs(Rey @ Rey - Rey)):.0e} of rank {int((ev > 0.5).sum())} "
          f"(squared multiplicities sum to {sum(k * k for k in mult(N).values())}; invariant degrees "
          f"{[L for L in range(N + 1) if m[2 * L]]}); the center has dimension {len(Pr)}")

print("\nH. The center: image correlations at the isotropic baseline at every g only when A is a multiple of I")
for N in (12, 20, 24, 30):
    R, Pr = SH[N]
    Mx = np.array([[k * CH[n][i] for n, k in mult(N).items() if k] for i in range(120)])
    base = U(N, Re) / (N + 1)
    eq = np.max(abs(img(R, sum(Pr.values())) - base))
    rnd = min(np.max(abs(img(R, sum(rng.uniform(0.2, 1.0) * P_ for P_ in Pr.values())) - base)) for _ in range(100))
    print(f"   N = {N}: the {len(Pr)} constituent characters are independent on 2I (smallest singular value "
          f"{np.linalg.svd(Mx, compute_uv=False).min():.2f}); equal weights give the baseline to {eq:.0e}; 100 random weightings "
          f"in [0.2, 1] miss it by at least {rnd:.4f}")

print(f"\nI. Outside the center: A5 anisotropy with every image correlation unchanged (eps = {eps} rad)")
even_inv = [l for l in inv_degrees if l % 2 == 0]
for N in (12, 20, 24, 30):
    R, Pr = SH[N]
    X = rng.normal(size=(N + 1, N + 1)) + 1j * rng.normal(size=(N + 1, N + 1))
    X = X + X.conj().T
    X = (X + sym(N, qinv(JQ)) @ X.conj() @ sym(N, JQ)) / 2
    Xb = sum(Rg @ X @ Rg.conj().T for Rg in R) / 120
    T = Xb - sum(np.trace(P_ @ Xb) / np.trace(P_) * P_ for P_ in Pr.values())
    size = np.linalg.norm(T) / np.linalg.norm(Xb)
    if size < 1e-9:
        print(f"   N = {N}: the non-central part is {size:.0e} of the averaged matrix: here the commutant is its center")
        continue
    T = T / np.linalg.norm(T, 2)
    A = np.eye(N + 1) + T / 2
    h = sym(N, rand_unit())
    F = np.array([np.trace(A @ sym(N, np.concatenate([[np.cos(eps)], -np.sin(eps) * n]))).real for n in NV]) / (N + 1)
    pw = power(F)
    degs = [l for l in range(LMAX + 1) if pw[l] > 1e-20 * pw.sum()]
    print(f"   N = {N}: non-central part {size:.2f} of the averaged matrix; with it scaled to unit norm as T, max |Tr(T rho(g))| "
          f"over 2I {max(abs(np.trace(T @ Rg)) for Rg in R):.0e}, [T, rho(g)] {max(np.max(abs(T @ Rg - Rg @ T)) for Rg in R):.0e}, "
          f"[T, rho(h)] for a random h {np.max(abs(T @ h - h @ T)):.2f}")
    print(f"      A = I + T/2: smallest eigenvalue {np.linalg.eigvalsh(A).min():.2f}; kernel real to "
          f"{max(abs(np.trace(A @ sym(N, rand_unit())).imag) for _ in range(5)):.0e}; image correlations minus baseline "
          f"{np.max(abs(img(R, A) - U(N, Re) / (N + 1))):.0e}; direction-dependent rms of the correlation "
          f"{np.sqrt(pw[1:].sum() / (4 * np.pi)):.2e}, in degrees {degs}, all even and A5-invariant: {set(degs) <= set(even_inv)}")

print("\nJ. What the image correlations see: the constituent weights alone, averaging chi_rho(g)/d_rho")
nearest = np.isclose(Re, PHI / 2)
for N in (12, 20, 24, 30):
    R, Pr = SH[N]
    chin = {n: CH[n] / DIM[n] for n in Pr}
    worst = max(np.max(abs(img(R, Pr[n]) - chin[n])) for n in Pr)
    for _ in range(20):
        Y = rng.normal(size=(N + 1, N + 1)) + 1j * rng.normal(size=(N + 1, N + 1))
        A = sum(Rg @ Y @ Y.conj().T @ Rg.conj().T for Rg in R) / 120
        wr = {n: np.trace(Pr[n] @ A).real for n in Pr}
        worst = max(worst, np.max(abs(img(R, A) - sum(wr[n] * chin[n] for n in Pr) / sum(wr.values()))))
    ends = sorted(float(chin[n][nearest][0]) for n in Pr)
    print(f"   N = {N}: for each single-constituent law and 20 random A5 laws, the image correlations equal the average of "
          f"chi_rho(g)/d_rho weighted by Tr(P_rho A), to {worst:.0e}; at the nearest images the family spans "
          f"[{ends[0]:+.4f}, {ends[-1]:+.4f}], with P2 at {ends[-1]:+.4f} and the baseline at {U(N, PHI / 2) / (N + 1):+.4f}")
