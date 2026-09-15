#!/usr/bin/env python3
"""The flattening half of item 5, first pass: what the geometric flat limit does to the laws of the quotient-specific half.
Group theory, spin coherent states and quadrature only: no CMB quantity, no shell weight, no E8 input, no sky covariance.

Units R = 1. Shell N has k_N = sqrt(N(N+2)). The flat limit holds c = k_N |v| fixed while N grows, so the separations it probes
shrink as 1/N and the images of a point, at distance pi/5 or more, recede from them.
  K1. The whole-shell law: its correlation U_N(cos(c/k_N))/(N+1) tends to the flat shell kernel j0(c).
  K2. The quotient's own law P near the observer, at fixed c: the central pair contributes O(N) and each of the other 118 images
      O(1), so the direction average tends to j0(c) and the direction-dependent rms falls like 1/N, slowly (m_N ~ N/60).
  K3. A smooth anisotropic A5 law, A_f = the integral of f(m)|m><m| over spin coherent states, with f an A5 orbit sum: its
      correlation tends to the flat shell kernel with direction weight f, the integral of f(m) exp(-i c w.m), and its
      anisotropy does not fall with N. The flat limit carries A_N to its coherent-state symbol.
  K4. The coherent-state symbol of P, (1/120) sum_g <m|U_g|m>^N: its mean is m_N/(N+1), its direction-dependent rms relative
      to the mean falls with N, and its values on the axis directions (12 vertices, 20 faces, 30 edges) show where it sits:
      zero on step one's Majorana directions at N = 12 and 20, and in spikes on the axes at large N.
  K5. The symbol transfer of P, a flat shell whose direction weight is Q_P, against P's own kernel on the sphere at fixed c:
      the two agree at large N and differ at the low shells.
  K6. The 12 vertex vectors of the icosahedron, the directions of a point's nearest images, span a Z-module of rank 6 in R^3:
      split over Q(sqrt 5), their coordinates have rank 6, so the module is not a lattice.
  K7. On every shell with a unique invariant (m_N = 1, N = 12 to 56) the symbol of P is |<m|psi_N>|^2, so its zeros are the
      roots of the invariant form f12^a f20^b f30^c: the vertices, faces and edges it contains, and no others. At N = 60, where
      m_N = 2, the zeros are gone.
  K8. From N = 60 the source covariance on the invariants is open. A rank-two choice, the invariant parts of the coherent states
      at a generic direction and its antipode (a real law), keeps its anisotropy near the observer in the flat limit, tending to
      the flat kernel of its orbit's measure, where P's falls like 2/N. (The record writes the projector Pi as P.)
"""
import itertools

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
rng = np.random.default_rng(7)


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
central = np.isclose(np.abs(G[:, 0]), 1.0)
assert len(G) == 120 and central.sum() == 2
c = np.zeros(1301, dtype=np.int64)
c[0] = 1
for s in (12, 20):
    for r in range(s):
        c[r::s] = np.cumsum(c[r::s])
m = c.copy()
m[30:] += c[:-30]


def U(N, x):
    """Chebyshev U_N(x) = sin((N+1)t)/sin t, x = cos t, stable for large N."""
    x = np.asarray(x, dtype=float)
    th = np.arccos(np.clip(x, -1.0, 1.0))
    s = np.sin(th)
    lim = np.where(x > 0, N + 1.0, (N + 1.0) * (-1.0) ** N)
    return np.where(s > 1e-9, np.sin((N + 1) * th) / np.where(s > 1e-9, s, 1.0), lim)


def j0(x):
    return np.sinc(x / np.pi)


def grid(nth, nph):
    xg, wg = np.polynomial.legendre.leggauss(nth)
    th, ph = np.repeat(np.arccos(xg), nph), np.tile(2 * np.pi * np.arange(nph) / nph, nth)
    return np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], axis=1), np.repeat(wg, nph) * 2 * np.pi / nph


NV, W = grid(64, 128)


def stats(F, w=W):
    mean = np.sum(w * F) / (4 * np.pi)
    return mean, np.sqrt(np.sum(w * (F - mean) ** 2) / (4 * np.pi))


NS = (12, 20, 60, 120, 600, 1200)
C0 = 6.0
assert all(m[N] >= 1 for N in NS)

print("K1. The whole-shell law in the flat limit: its correlation at c = k_N |v| against the flat shell kernel j0(c)")
for N in NS:
    k = np.sqrt(N * (N + 2))
    err = max(abs(float(U(N, np.cos(cc / k))) / (N + 1) - j0(cc)) for cc in (1.0, 3.0, 6.0))
    print(f"   N = {N:4d}: max |U_N(cos(c/k_N))/(N+1) - j0(c)| over c = 1, 3 and 6: {err:.1e}")

print(f"\nK2. The quotient's own law P near the observer at c = {C0}: K_P(1, exp(v))/m_N over the directions of v, |v| = c/k_N")
for N in NS:
    eps = C0 / np.sqrt(N * (N + 2))
    Y = np.concatenate([np.full((len(NV), 1), np.cos(eps)), np.sin(eps) * NV], axis=1)
    F = U(N, Y @ G.T).sum(1) / 120 / m[N]
    mean, rms = stats(F)
    cen = stats(U(N, Y @ G[central].T).sum(1) / 120 / m[N])[1]
    print(f"   N = {N:4d} (m_N = {m[N]}): direction average {mean:+.5f} against j0(c) = {j0(C0):+.5f}; direction-dependent rms "
          f"{rms:.2e}, times N {rms * N:.1f}; the central pair alone isotropic to {cen:.0e}")

SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


def su2(q):
    w, x, y, z = q
    return np.array([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]])


def bloch(Uq):
    return np.array([[0.5 * np.trace(SIG[a] @ Uq @ SIG[b] @ Uq.conj().T).real for b in range(3)] for a in range(3)])


def coherent(n):
    th, ph = np.arccos(np.clip(n[:, 2], -1, 1)), np.arctan2(n[:, 1], n[:, 0])
    return np.stack([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)], axis=1)


def axes(re):
    """The Bloch-frame directions of the rotation axes of the elements of 2I with real part re (su2 sends i, j, k to
    i sigma_z, i sigma_y, i sigma_x)."""
    sel = G[np.isclose(G[:, 0], re)]
    v = np.stack([sel[:, 3], sel[:, 2], sel[:, 1]], axis=1)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


AX = {"vertex": axes(PHI / 2), "face": axes(0.5), "edge": axes(0.0)}
assert [len(AX[k]) for k in AX] == [12, 20, 30]
MS = coherent(NV)
RG = [bloch(su2(g)) for g in G]
e0 = AX["vertex"][0]
KAPPA = 8.0


def f_of(n):
    return sum(np.exp(KAPPA * n @ (Rg @ e0)) for Rg in RG)


fw = f_of(NV)
probe = rng.normal(size=(50, 3))
probe /= np.linalg.norm(probe, axis=1, keepdims=True)
finv = max(np.max(abs(f_of(probe @ Rg.T) - f_of(probe))) / np.max(f_of(probe)) for Rg in RG)
amp_check = max(abs(np.vdot(MS[i], SIG[a] @ MS[i]).real - NV[i, a]) for i in range(0, len(NV), 97) for a in range(3))
print(f"\nK3. A smooth anisotropic A5 law A_f at c = {C0}: f = sum over 2I of exp({KAPPA} m.(R_g e)), e a vertex direction, so f "
      f"peaks on the 12 vertices; invariant under the 60 Bloch rotations to {finv:.0e} (relative); its direction-dependent rms "
      f"over its mean {stats(fw)[1] / stats(fw)[0]:.2f}; coherent states' Bloch vectors to {amp_check:.0e}")
vdirs = rng.normal(size=(60, 3))
vdirs /= np.linalg.norm(vdirs, axis=1, keepdims=True)
flat = []
for v in vdirs:
    wv = np.array([v[2], v[1], v[0]])
    flat.append(np.sum(W * fw * np.exp(-1j * C0 * (NV @ wv))) / np.sum(W * fw))
flat = np.array(flat)
print(f"   flat shell kernel with weight f, over 60 directions: mean {flat.real.mean():+.4f}, direction-dependent rms "
      f"{flat.real.std():.3e}, imaginary part at most {np.max(abs(flat.imag)):.0e}")
for N in NS:
    t = C0 / np.sqrt(N * (N + 2))
    sph = []
    for v in vdirs:
        wv = np.array([v[2], v[1], v[0]])
        Uv = np.cos(t) * np.eye(2) - 1j * np.sin(t) * sum(wv[a] * SIG[a] for a in range(3))
        amp = np.einsum("ni,ij,nj->n", MS.conj(), Uv, MS)
        sph.append(np.sum(W * fw * amp ** N) / np.sum(W * fw))
    sph = np.array(sph)
    print(f"   N = {N:4d}: sphere kernel against the flat one, largest difference {np.max(abs(sph - flat)):.1e}, times N "
          f"{np.max(abs(sph - flat)) * N:.2f}; its own direction-dependent rms {sph.real.std():.3e}")

NF, WF = grid(300, 600)
MF = coherent(NF)


def QP(N, M):
    """The coherent-state symbol of P, (1/120) sum_g <m|U_g|m>^N, at the spinors M."""
    Q = np.zeros(len(M), dtype=complex)
    for g in G:
        Q += np.einsum("ni,ij,nj->n", M.conj(), su2(g), M) ** N
    return Q / 120


print("\nK4. The coherent-state symbol of P, Q_P(m) = (1/120) sum_g <m|U_g|m>^N, on a 300 x 600 grid, and on the axis directions")
QF = {}
for N in NS:
    Q = QP(N, MF)
    QF[N] = Q.real
    mean, rms = stats(Q.real, WF)
    ax = {k: QP(N, coherent(AX[k])).real / mean for k in AX}
    print(f"   N = {N:4d}: mean {mean:.6f} against m_N/(N+1) = {m[N] / (N + 1):.6f}; imaginary part at most {np.max(abs(Q.imag)):.0e}; "
          f"direction-dependent rms over the mean {rms / mean:.3f}; over the mean at the vertices "
          f"{ax['vertex'].min():.3f} to {ax['vertex'].max():.3f}, faces {ax['face'].min():.3f} to {ax['face'].max():.3f}, "
          f"edges {ax['edge'].min():.3f} to {ax['edge'].max():.3f}")

print(f"\nK5. The symbol transfer of P, the flat shell kernel with direction weight Q_P, against P's own kernel on the sphere, at "
      f"c = {C0}, over 200 random directions")
vd = rng.normal(size=(200, 3))
vd /= np.linalg.norm(vd, axis=1, keepdims=True)
for N in NS:
    fl = np.array([np.sum(WF * QF[N] * np.exp(-1j * C0 * (NF @ np.array([v[2], v[1], v[0]])))) for v in vd]) / np.sum(WF * QF[N])
    eps = C0 / np.sqrt(N * (N + 2))
    Y = np.concatenate([np.full((len(vd), 1), np.cos(eps)), np.sin(eps) * vd], axis=1)
    sp = U(N, Y @ G.T).sum(1) / 120 / m[N]
    print(f"   N = {N:4d}: symbol-transfer kernel mean {fl.real.mean():+.5f}, rms {fl.real.std():.2e} (imaginary part at most "
          f"{np.max(abs(fl.imag)):.0e}); sphere kernel mean {sp.mean():+.5f}, rms {sp.std():.2e}; largest difference "
          f"{np.max(abs(fl.real - sp)):.2e}")

V12 = [v for cc in ((0, 1, PHI), (1, PHI, 0), (PHI, 0, 1)) for v in itertools.product(*[(s, -s) if s else (0,) for s in cc])]
SPLIT = {0: (0.0, 0.0), 1: (1.0, 0.0), -1: (-1.0, 0.0), PHI: (0.5, 0.5), -PHI: (-0.5, -0.5)}
rows = np.array([[p for x in v for p in SPLIT[min(SPLIT, key=lambda s: abs(s - x))]] for v in V12])
back = max(abs(sum(rows[i][2 * a] + rows[i][2 * a + 1] * 5 ** 0.5 for _ in [0]) - V12[i][a]) for i in range(12) for a in range(3))
print(f"\nK6. The 12 vertex vectors split over Q(sqrt 5) (x = p + q sqrt 5, reassembled to {back:.0e}): rank of the 12 x 6 rational "
      f"matrix {np.linalg.matrix_rank(rows)}, so their Z-span has rank 6 in R^3")

print("\nK7. Zeros of the symbol of P: on each shell with a unique invariant, exactly the roots of its form; none at N = 60")


def form(N):
    return [(a, b, cc) for cc in (0, 1) for b in range(N // 20 + 1) for a in range(N // 12 + 1) if 12 * a + 20 * b + 30 * cc == N]


ok_all = True
for N in [n for n in range(12, 61, 2) if m[n] >= 1]:
    sols = form(N)
    assert len(sols) == m[N]
    mean = m[N] / (N + 1)
    ax = {k: QP(N, coherent(AX[k])).real / mean for k in AX}
    if m[N] == 1:
        a, b, cc = sols[0]
        pred = {"vertex": a > 0, "face": b > 0, "edge": cc > 0}
        ok = all((abs(ax[k]).max() < 1e-10) if pred[k] else (ax[k].min() > 1e-3) for k in AX)
        ok_all = ok_all and ok
        print(f"   N = {N}: f12^{a} f20^{b} f30^{cc}; over the mean, largest on the vertices {abs(ax['vertex']).max():.1e}, faces "
              f"{abs(ax['face']).max():.1e}, edges {abs(ax['edge']).max():.1e}; zero exactly on the form's roots: {ok}")
    else:
        Qg = QP(N, MF).real
        print(f"   N = {N} (m_N = {m[N]}, forms {sols}): smallest value over the mean on the {len(MF)}-point grid {Qg.min() / mean:.3f}, "
              f"on the axes {min(ax[k].min() for k in AX):.3f}")
print(f"   every shell with a unique invariant: {ok_all}")

print(f"\nK8. A rank-two source on the invariants at c = {C0}: the invariant parts of the coherent states at a generic n and at -n")
n0 = rng.normal(size=3)
n0 /= np.linalg.norm(n0)
S2 = [su2(g) for g in G]
V60 = vd[:60]
lim = np.array([np.mean([np.cos(C0 * np.array([v[2], v[1], v[0]]) @ (Rg @ n0)) for Rg in RG]) for v in V60])
print(f"   the flat kernel of its orbit's measure, the limit: mean {lim.mean():+.4f}, direction-dependent rms {lim.std():.3e}")
for N in (60, 120, 600, 1200):
    t = C0 / np.sqrt(N * (N + 2))
    num = np.zeros(len(V60), dtype=complex)
    den = 0.0
    for nn in (n0, -n0):
        M0 = coherent(nn[None, :])[0]
        L = np.array([M0.conj() @ Sg for Sg in S2])
        Rr = np.array([Sg @ M0 for Sg in S2])
        den += (np.array([M0.conj() @ Sg @ M0 for Sg in S2]) ** N).sum().real / 120
        for i, v in enumerate(V60):
            wv = np.array([v[2], v[1], v[0]])
            Uv = np.cos(t) * np.eye(2) - 1j * np.sin(t) * sum(wv[a] * SIG[a] for a in range(3))
            num[i] += ((L @ Uv @ Rr.T) ** N).sum() / 120 ** 2
    kern = num / den
    Y = np.concatenate([np.full((len(V60), 1), np.cos(t)), np.sin(t) * V60], axis=1)
    pk = U(N, Y @ G.T).sum(1) / 120 / m[N]
    print(f"   N = {N:4d}: mean {kern.real.mean():+.4f}, direction-dependent rms {kern.real.std():.3e} (imaginary part at most "
          f"{np.max(abs(kern.imag)):.0e}); largest difference from the limit {np.max(abs(kern.real - lim)):.2e}; P's rms on the same "
          f"directions {pk.std():.2e}")
