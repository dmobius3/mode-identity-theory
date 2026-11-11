#!/usr/bin/env python3
"""
w_star_max.py: numerical checks on the maximum of W_* found by w_star.py.  The proof is on
the page self-intersection-width.md and its own checks are in w_star_proof.py; this file is the evidence gathered
before the proof, kept because each part tests something the proof also uses.

  A  the pose of Theorem 3 built from the axes: N a two-fold axis, the lune's two edge circles
     the great circles orthogonal to the adjacent three-fold and five-fold axes that lie in the
     plane orthogonal to N.  T(n) for all 31 axes at 60 digits, against tan(theta/2),
     tan(theta) = 3 - sqrt 5
  B  the direct route (quaternion multiplication over all of 2I) at that pose
  C  Corollary 2, T(n) <= tan(angle(n, b)), on random poses, and the covering radius of the axes
  D  the one-sided slope of min T at the pose, sampled over directions (a sharp peak)
  E  a scan of the directions for b that Corollary 2 alone leaves open

Quantities at the roundoff level are printed as bounds.
Run from the directory holding w_star.py: python3 -u w_star_max.py
"""
import itertools
import math

import mpmath as mp
import numpy as np
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation as Rot

import w_star as ws

mp.mp.dps = 60
DEG = 180 / math.pi


def mp_axes():
    """the 31 axes and their orders at working precision, from the same icosian construction."""
    phi = (1 + mp.sqrt(5)) / 2
    els = []
    for i in range(4):
        for s in (1, -1):
            v = [mp.mpf(0)] * 4
            v[i] = mp.mpf(s)
            els.append(v)
    for signs in itertools.product((1, -1), repeat=4):
        els.append([mp.mpf(s) / 2 for s in signs])
    base = [mp.mpf(0), mp.mpf(1) / 2, phi / 2, 1 / (2 * phi)]
    for perm in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
        if inv % 2:
            continue
        for signs in itertools.product((1, -1), repeat=3):
            v = [mp.mpf(0)] * 4
            k = 0
            for pos, src in enumerate(perm):
                val = base[src]
                if val != 0:
                    val = val * signs[k]
                    k += 1
                v[pos] = val
            els.append(v)
    assert len(els) == 120
    found = {}
    for g in els:
        im = g[1:]
        nrm = mp.sqrt(sum(c * c for c in im))
        if nrm < mp.mpf(10) ** -40:
            continue
        n = [c / nrm for c in im]
        for c in n:
            if abs(c) > mp.mpf(10) ** -40:
                if c < 0:
                    n = [-x for x in n]
                break
        re = abs(g[0])
        if re < mp.mpf(10) ** -40:
            m = 2
        elif abs(re - mp.mpf(1) / 2) < mp.mpf(10) ** -40:
            m = 3
        else:
            m = 5
        k = tuple(round(float(x), 9) + 0.0 for x in n)
        found.setdefault(k, (n, m))
    ax = [v[0] for v in found.values()]
    od = [v[1] for v in found.values()]
    assert (len(ax), od.count(2), od.count(3), od.count(5)) == (31, 15, 10, 6)
    return ax, od


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def unit(a):
    n = mp.sqrt(dot(a, a))
    return [x / n for x in a]


def T_mp(n, m, e, b, N):
    ne, nb, nN = dot(n, e), dot(n, b), dot(n, N)
    c = mp.mpf(0) if m == 2 else mp.cot(mp.pi / m)
    A2, B2 = 1 - ne ** 2, 1 - nb ** 2
    den = mp.sqrt(c ** 2 * nN ** 2 + A2 * B2) + c * abs(nN)
    return B2 / den if den > 0 else mp.inf


def main():
    ax, od = mp_axes()
    tiny = mp.mpf(10) ** -45
    small = mp.mpf(10) ** -55

    print("Part A: the pose of Theorem 3, 60 digits")
    N = next(n for n, m in zip(ax, od) if m == 2)
    in3 = [n for n, m in zip(ax, od) if m == 3 and abs(dot(n, N)) < tiny]
    in5 = [n for n, m in zip(ax, od) if m == 5 and abs(dot(n, N)) < tiny]
    print(f"  axes orthogonal to the chosen two-fold axis N: {len(in3)} three-fold, {len(in5)} five-fold,"
          f" {sum(1 for n, m in zip(ax, od) if m == 2 and abs(dot(n, N)) < tiny)} two-fold")
    best = None
    for a3 in in3:
        for a5 in in5:
            for s in (1, -1):
                a5s = [s * x for x in a5]
                ang = mp.acos(dot(a3, a5s))
                if best is None or ang < best[0]:
                    best = (ang, a3, a5s)
    theta, a3, a5 = best
    print(f"  angle between the adjacent three-fold and five-fold axes: {mp.nstr(theta * 180 / mp.pi, 15)} deg;"
          f"  tan(theta) = 3 - sqrt 5 to within 1e-55: {abs(mp.tan(theta) - (3 - mp.sqrt(5))) < small}")
    b = unit([x + y for x, y in zip(a3, a5)])
    e = cross(b, N)
    Ts = [T_mp(n, m, e, b, N) for n, m in zip(ax, od)]
    tmin = min(Ts)
    target = mp.tan(mp.atan(3 - mp.sqrt(5)) / 2)
    closed = (mp.sqrt(15 - 6 * mp.sqrt(5)) - 1) / (3 - mp.sqrt(5))
    print(f"  min over 31 axes of T      = {mp.nstr(tmin, 40)}")
    print(f"  tan(arctan(3 - sqrt 5)/2)  = {mp.nstr(target, 40)}")
    print(f"  the two agree to within 1e-55: {abs(tmin - target) < small};"
          f"  so does (sqrt(15 - 6 sqrt 5) - 1)/(3 - sqrt 5): {abs(closed - target) < small}")
    binding = [(m, T) for m, T in zip(od, Ts) if abs(T - tmin) < tiny]
    slack = sorted(T - tmin for T in Ts if abs(T - tmin) >= tiny)
    print(f"  axes at the minimum (within 1e-45): {len(binding)} = "
          f"{sum(1 for m, _ in binding if m == 2)} two-fold + {sum(1 for m, _ in binding if m == 3)} three-fold"
          f" + {sum(1 for m, _ in binding if m == 5)} five-fold")
    print(f"  the other {len(slack)} axes exceed it by at least {mp.nstr(slack[0], 8)} in T")
    Wmax = mp.atan(tmin)
    print(f"  W_max = arctan(3 - sqrt 5)/2 = {mp.nstr(Wmax, 30)} rad = {mp.nstr(Wmax * 180 / mp.pi, 20)} deg")
    print(f"  the edge circles: longitude of the three-fold axis from b = {mp.nstr(mp.acos(dot(a3, b)) * 180 / mp.pi, 15)} deg,"
          f" of the five-fold axis = {mp.nstr(mp.acos(dot(a5, b)) * 180 / mp.pi, 15)} deg (both equal W_max)")
    assert abs(tmin - target) < small and abs(closed - target) < small and len(binding) == 10

    print("Part B: the direct route at that pose")
    G = ws.build_2I()
    ef, bf, Nf = (np.array([float(x) for x in v]) for v in (e, b, N))
    W0 = float(Wmax)
    t0 = math.tan(W0)
    wd = ws.wstar_direct(ef, bf, Nf, G, nsamp=20001)
    print(f"  direct W_* agrees with W_max to within 1e-12 rad: {abs(wd - W0) < 1e-12}")
    assert abs(wd - W0) < 1e-12

    print("Part C: Corollary 2, W_* <= angle from b to the nearest axis")
    AX, OD = ws.axes_of(G)
    C = ws.cot_of(OD)
    worst, count = -1.0, 0
    for chunk in range(20):
        E, B, NN = ws.frames(100_000, seed=500 + chunk)
        T = ws.T_closed(E, B, NN, AX, C)
        nbv = np.abs(B @ AX.T)
        tan_ang = np.sqrt(np.maximum(1 - nbv ** 2, 0.0)) / nbv
        worst = max(worst, float(np.max(T - tan_ang)))
        count += len(E)
    print(f"  {count} poses x 31 axes: T(n) never exceeds tan(angle(n, b)) by more than 1e-12: {worst < 1e-12}")
    assert worst < 1e-12

    def neg_min_ang(x):
        v = np.array([math.sin(x[0]) * math.cos(x[1]), math.sin(x[0]) * math.sin(x[1]), math.cos(x[0])])
        return -float(np.min(np.arccos(np.clip(np.abs(AX @ v), 0, 1))))

    rs = np.random.RandomState(11)
    rho = 0.0
    for _ in range(400):
        x0 = np.array([math.acos(rs.uniform(-1, 1)), rs.uniform(0, 2 * math.pi)])
        r = minimize(neg_min_ang, x0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-14})
        rho = max(rho, -r.fun)
    rho_formula = math.atan(t0 / math.cos(math.pi / 60))
    print(f"  covering radius of the 31 axes: {rho * DEG:.6f} deg (search);"
          f"  arctan(tan(W_max)/cos(pi/60)) = {rho_formula * DEG:.6f} deg")
    print(f"  so Corollary 2 alone gives W_* <= {rho_formula * DEG:.6f} deg, and W_max = {W0 * DEG:.6f} deg sits"
          f" {(rho_formula - W0) * DEG:.6f} deg below that")
    assert abs(rho - rho_formula) * DEG < 1e-6

    print("Part D: the peak at that pose")
    M0 = np.stack([ef, bf, Nf], axis=1)
    if np.linalg.det(M0) < 0:
        M0 = np.stack([ef, bf, -Nf], axis=1)
    T0 = ws.T_closed(M0[:, 0], M0[:, 1], M0[:, 2], AX, C)
    act = np.where(T0 - T0.min() < 1e-9)[0]
    print(f"  binding axes: {len(act)}")
    # T(n) carries |n_N|, so min T has a kink at this pose and a gradient test does not apply.
    # The one-sided slope of min T is sampled over directions instead.
    dirs = np.random.RandomState(3).normal(size=(200000, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    top = -math.inf
    for h in (1e-3, 1e-5, 1e-7):
        Ms = Rot.from_rotvec(h * dirs).as_matrix() @ M0
        F = np.min(ws.T_closed(Ms[:, :, 0], Ms[:, :, 1], Ms[:, :, 2], AX, C), axis=-1)
        slope = (F - T0.min()) / h
        top = max(top, float(slope.max()))
        print(f"  step {h:.0e} rad, 200000 directions: one-sided slope of min T between {slope.min():.3f} and {slope.max():.3f} per rad")
    print(f"  every sampled direction lowers min T at first order: {top < 0}")
    assert top < 0

    print("Part E: the directions for b that Corollary 2 leaves open")
    # Where b is within W_max of some axis, Corollary 2 already gives W_* <= W_max.  The rest is a
    # thin sliver about the midpoint of each three-fold/five-fold edge; this scans one of them.
    b0, N0 = bf, Nf
    a3f = np.array([float(x) for x in a3])
    t1 = a3f - (a3f @ b0) * b0
    t1 /= np.linalg.norm(t1)
    xs = np.deg2rad(np.arange(-0.06, 0.0600001, 0.001))
    ys = np.deg2rad(np.arange(-1.1, 1.1000001, 0.005))
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    Bs = b0[None, :] + X.reshape(-1, 1) * t1[None, :] + Y.reshape(-1, 1) * N0[None, :]
    Bs /= np.linalg.norm(Bs, axis=1, keepdims=True)
    dist = np.min(np.arccos(np.clip(np.abs(Bs @ AX.T), 0, 1)), axis=1)
    keep = dist > W0 - np.deg2rad(0.002)
    inside = dist > W0 + 1e-9
    edge_hit = bool(np.any(inside & ((np.abs(X.reshape(-1)) > np.deg2rad(0.0585)) | (np.abs(Y.reshape(-1)) > np.deg2rad(1.0925)))))
    print(f"  grid about the edge midpoint: {len(Bs)} directions for b; {int(keep.sum())} of them lie farther than"
          f" W_max - 0.002 deg from every axis and are scanned (largest distance {dist.max() * DEG:.6f} deg)")
    print(f"  the open set stays inside the grid: {not edge_hit}")
    Bs = Bs[keep]
    psi = np.deg2rad(np.arange(0.0, 180.0, 0.02))
    tmp = np.where(np.abs(Bs[:, :1]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
    U = np.cross(Bs, tmp)
    U /= np.linalg.norm(U, axis=1, keepdims=True)
    Wv = np.cross(Bs, U)
    best, pool, count = -1.0, [], 0
    for s in range(0, len(Bs), 20):
        bb, uu, ww = Bs[s:s + 20], U[s:s + 20], Wv[s:s + 20]
        Nn = np.cos(psi)[None, :, None] * uu[:, None, :] + np.sin(psi)[None, :, None] * ww[:, None, :]
        Bb = np.broadcast_to(bb[:, None, :], Nn.shape)
        Ee = np.cross(Bb, Nn)
        F = np.min(ws.T_closed(Ee, Bb, Nn, AX, C), axis=-1)
        count += F.size
        for kk in np.argsort(F, axis=None)[-2:]:
            i, j = np.unravel_index(kk, F.shape)
            pool.append((float(F[i, j]), np.stack([Ee[i, j], Bb[i, j], Nn[i, j]], axis=1)))
        best = max(best, float(F.max()))
    print(f"  poses scanned: {count};  none has min T above tan W_max + 1e-12: {best <= t0 + 1e-12}")
    pool.sort(key=lambda z: -z[0])
    vals = []
    for F0, Mx in pool[:150]:
        if np.linalg.det(Mx) < 0:
            Mx = Mx * np.array([1.0, 1.0, -1.0])
        rv, t = ws.refine(Rot.from_matrix(Mx).as_rotvec(), AX, C)
        vals.append(t)
    print(f"  150 best scanned poses refined: none above tan W_max + 1e-9: {max(vals) <= t0 + 1e-9}")
    assert not edge_hit and best <= t0 + 1e-12 and max(vals) <= t0 + 1e-9


if __name__ == "__main__":
    main()
