#!/usr/bin/env python3
"""
w_star.py: the first self-intersection width W_* of the conic band's image in S^3/2I.

Setting (CONTRIBUTING.md, "The first self-intersection width"; Projective Carrier, Prop. 0.4):
S^3 = unit quaternions, 2I acting by left multiplication, Sigma = purely imaginary unit
quaternions, (N, e) orthonormal in Sigma, b = N x e.  D(W) = points of Sigma within longitude W
of the great circle through N and e, about the poles +-N.  W_*(N, e) = least W at which two
points of D(W), not related by +-1, lie in one 2I-orbit.

Closed form tested here.  For an icosahedral axis n of order m (2, 3 or 5), with components
(n_e, n_b, n_N) in the pose frame and c = cot(pi/m):

    T(n) = (1 - n_b^2) / ( sqrt(c^2 n_N^2 + (1 - n_e^2)(1 - n_b^2)) + c |n_N| )

    W_*(N, e) = min over the 31 axes of arctan T(n)

Derivation.
  1. For p, q in Sigma, q = g p forces g = -q p = <p, q> + p x q.  So the real part of g is the
     cosine of the angle from p to q, and its axis is the normal of their plane.  An element of 2I
     on an axis of order m is cos(pi j/m) + sin(pi j/m) n.  Hence two points of Sigma share a
     2I-orbit exactly when both lie on the great circle C_n orthogonal to an icosahedral axis n,
     at separation pi j/m along it; j = 0 and j = m are the excluded +-1.
  2. D(W) is closed under x -> -x, so a separation delta can be replaced by pi - delta.  That
     leaves delta = pi/2 for m = 2, pi/3 for m = 3, and pi/5 or 2pi/5 for m = 5.
  3. On C_n let s be arc length from the point where C_n crosses the core circle.  Then
     tan(longitude) = k sin(s) / cos(s - sigma), with k = sqrt((1 - n_b^2)/(1 - n_e^2)) and
     cos(sigma) = |n_N| / sqrt((1 - n_e^2)(1 - n_b^2)).  This is monotone in s, so the part of C_n
     within longitude W of the core is an arc from s_- to s_+, where the tangent is -T and +T,
     T = tan W, and tan(s_+ - s_-) = 2 k T cos(sigma) / (k^2 - T^2).
  4. Two points at separation delta first fit when s_+ - s_- = delta.  Solving the quadratic for T
     gives the formula with c = cot(delta).  T increases with delta, so pi/5 governs for m = 5.

The page self-intersection-width.md, two folders up, gives the argument in full.

Parts:
  0  build 2I, check closure, read off the 31 axes and their orders
  1  the closed form against a direct minimisation over every non-central g in 2I
     (the direct route uses quaternion multiplication only, not the angle reduction),
     with two mutation arms that must fail
  2  the maximum of W_* over poses: random search, epigraph refinement, grid cross-check
  3  the distribution of W_* over Haar-random poses

Standard library, numpy, scipy.  Random poses come from numpy's legacy generator, whose stream
does not change between versions.  Quantities at the roundoff level are printed as bounds, and
results of an optimiser to the digits it settles.
Run: python3 -u w_star.py
"""
import itertools
import math

import numpy as np
from scipy.optimize import brentq, minimize, minimize_scalar
from scipy.spatial.transform import Rotation as Rot

PHI = (1 + 5 ** 0.5) / 2
DEG = 180 / math.pi


# ---------------------------------------------------------------- Part 0: the group
def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return np.array([
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    ])


def build_2I():
    els = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0] * 4
            v[i] = s
            els.append(v)
    for signs in itertools.product((1.0, -1.0), repeat=4):
        els.append([s / 2 for s in signs])
    base = [0.0, 0.5, PHI / 2, 1 / (2 * PHI)]
    for perm in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j])
        if inv % 2:
            continue
        for signs in itertools.product((1.0, -1.0), repeat=3):
            v = [0.0] * 4
            k = 0
            for pos, src in enumerate(perm):
                val = base[src]
                if val != 0.0:
                    val *= signs[k]
                    k += 1
                v[pos] = val
            els.append(v)
    return np.array(els)


def key(q):
    return tuple(np.round(q, 9) + 0.0)


def check_group(G):
    keys = {key(g) for g in G}
    assert len(G) == 120 and len(keys) == 120, "not 120 distinct elements"
    for a in G:
        assert abs(np.dot(a, a) - 1) < 1e-12
        for b in G:
            assert key(qmul(a, b)) in keys, "not closed"
    return True


def axes_of(G):
    found = {}
    for g in G:
        im = g[1:]
        nrm = np.linalg.norm(im)
        if nrm < 1e-9:
            continue
        n = im / nrm
        for c in n:
            if abs(c) > 1e-9:
                if c < 0:
                    n = -n
                break
        re = abs(g[0])
        if re < 1e-9:
            m = 2
        elif abs(re - 0.5) < 1e-9:
            m = 3
        else:
            assert abs(re - PHI / 2) < 1e-9 or abs(re - 1 / (2 * PHI)) < 1e-9
            m = 5
        k = tuple(np.round(n, 9) + 0.0)
        if k in found:
            assert found[k][1] == m
        else:
            found[k] = (n, m)
    ax = np.array([v[0] for v in found.values()])
    od = np.array([v[1] for v in found.values()])
    return ax, od


# ---------------------------------------------------------------- Part 1: closed form
def cot_of(orders):
    return np.array([0.0 if m == 2 else 1 / math.tan(math.pi / m) for m in orders])


def T_closed(e, b, N, AX, C, variant="true"):
    """tan of the entry width for each axis.  e, b, N: (..., 3).  Returns (..., number of axes)."""
    ne = e @ AX.T
    nb = b @ AX.T
    nN = N @ AX.T
    A2 = np.maximum(1 - ne ** 2, 0.0)      # rounding can leave -1e-17 when n is e or b exactly
    B2 = np.maximum(1 - nb ** 2, 0.0)
    aN = np.abs(nN)
    if variant == "true":
        den = np.sqrt(C ** 2 * nN ** 2 + A2 * B2) + C * aN
    elif variant == "mut_no_linear_term":       # mutation: drop the c|n_N| term
        den = np.sqrt(C ** 2 * nN ** 2 + A2 * B2)
    else:
        raise ValueError(variant)
    with np.errstate(divide="ignore", invalid="ignore"):
        T = np.where(B2 < 1e-300, 0.0, B2 / den)
    return T


def wstar_closed(e, b, N, AX, C, variant="true"):
    return np.arctan(np.min(T_closed(e, b, N, AX, C, variant), axis=-1))


def wstar_direct(e, b, N, G, nsamp=6001):
    """Direct route.  For every non-central g, p runs over the great circle of Sigma that g
    keeps inside Sigma (Re(g p) = 0), q = g p by quaternion multiplication, and the larger of
    the two longitudes from the core is minimised over the circle."""
    def lam(x):
        return np.arctan2(np.abs(x @ b), np.abs(x @ e))

    best = math.inf
    s_grid = np.linspace(0.0, math.pi, nsamp)
    for g in G:
        im = g[1:]
        if np.linalg.norm(im) < 1e-9:
            continue
        n = im / np.linalg.norm(im)
        tmp = np.array([1.0, 0, 0]) if abs(n[0]) < 0.9 else np.array([0, 1.0, 0])
        u = np.cross(n, tmp)
        u /= np.linalg.norm(u)
        v = np.cross(n, u)

        def pair(s):
            p = math.cos(s) * u + math.sin(s) * v
            q4 = qmul(g, np.array([0.0, *p]))
            assert abs(q4[0]) < 1e-9, "g p left Sigma"
            return p, q4[1:]

        def f(s):
            p, q = pair(s)
            return max(lam(p), lam(q))

        P = np.outer(np.cos(s_grid), u) + np.outer(np.sin(s_grid), v)
        g0, gv = g[0], g[1:]
        Q = g0 * P + np.cross(np.broadcast_to(gv, P.shape), P)   # Im(g p) for p perpendicular to Im g
        vals = np.maximum(lam(P), lam(Q))
        i = int(np.argmin(vals))
        h = s_grid[1] - s_grid[0]
        lo, hi = s_grid[i] - 2 * h, s_grid[i] + 2 * h
        cands = [vals[i]]
        # The minimum of a maximum of two functions sits where they cross, or at an interior
        # minimum of the larger one.  A bounded Brent search on the kinked maximum resolves the
        # argument only to about sqrt(machine epsilon), so the crossing is found by root-finding.
        d = lambda s: lam(pair(s)[0]) - lam(pair(s)[1])
        if d(lo) * d(hi) < 0:
            cands.append(f(brentq(d, lo, hi, xtol=1e-15, rtol=1e-15)))
        for which in (0, 1):
            r = minimize_scalar(lambda s: lam(pair(s)[which]), bounds=(lo, hi), method="bounded",
                                options={"xatol": 1e-14})
            cands.append(f(r.x))
        best = min(best, *cands)
    return best


def frames(K, seed):
    """K Haar-random right-handed frames (e, b, N), from unit quaternions drawn with numpy's
    legacy generator (its stream is frozen, so every machine draws the same poses)."""
    q = np.random.RandomState(seed).normal(size=(K, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    w, x, y, z = q.T
    M = np.empty((K, 3, 3))
    M[:, 0, 0] = 1 - 2 * (y * y + z * z)
    M[:, 0, 1] = 2 * (x * y - z * w)
    M[:, 0, 2] = 2 * (x * z + y * w)
    M[:, 1, 0] = 2 * (x * y + z * w)
    M[:, 1, 1] = 1 - 2 * (x * x + z * z)
    M[:, 1, 2] = 2 * (y * z - x * w)
    M[:, 2, 0] = 2 * (x * z - y * w)
    M[:, 2, 1] = 2 * (y * z + x * w)
    M[:, 2, 2] = 1 - 2 * (x * x + y * y)
    return M[:, :, 0], M[:, :, 1], M[:, :, 2]


# ---------------------------------------------------------------- Part 2: the maximum
def refine(rv0, AX, C):
    """maximise t subject to T_i(pose) >= t, pose = rotation vector.  Returns (rotation vector, t)."""
    def Ts(rv):
        M = Rot.from_rotvec(rv).as_matrix()
        T = T_closed(M[:, 0], M[:, 1], M[:, 2], AX, C)
        return np.minimum(T, 50.0)

    x0 = np.concatenate([rv0, [np.min(Ts(rv0)) - 1e-6]])
    cons = [{"type": "ineq", "fun": lambda x: Ts(x[:3]) - x[3]}]
    r = minimize(lambda x: -x[3], x0, constraints=cons, method="SLSQP",
                 options={"ftol": 1e-15, "maxiter": 500})
    rv = r.x[:3]
    return rv, float(np.min(Ts(rv)))


def grid_cross_check(AX, OD, C, nb=150, npsi=720):
    """b over one (2,3,5) Moebius triangle, e over the half-turn of directions orthogonal to b."""
    v5 = AX[OD == 5][0]
    d3 = AX[OD == 3] @ v5
    v3 = AX[OD == 3][int(np.argmax(np.abs(d3)))]
    v3 = v3 if v3 @ v5 > 0 else -v3
    cand = AX[OD == 2]
    sc = np.abs(cand @ v5) + np.abs(cand @ v3)
    v2 = cand[int(np.argmax(sc))]
    v2 = v2 if v2 @ v5 > 0 else -v2
    best, arg = -1.0, None
    psi = np.linspace(0.0, math.pi, npsi, endpoint=False)
    for i in range(nb + 1):
        bs = []
        for j in range(nb + 1 - i):
            a, bb = i / nb, j / nb
            x = a * v2 + bb * v3 + (1 - a - bb) * v5
            bs.append(x / np.linalg.norm(x))
        bs = np.array(bs)
        tmp = np.where(np.abs(bs[:, :1]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
        u = np.cross(bs, tmp)
        u /= np.linalg.norm(u, axis=1, keepdims=True)
        w = np.cross(bs, u)
        E = np.cos(psi)[None, :, None] * u[:, None, :] + np.sin(psi)[None, :, None] * w[:, None, :]
        Bv = np.broadcast_to(bs[:, None, :], E.shape)
        Nv = np.cross(E, Bv)
        F = np.min(T_closed(E, Bv, Nv, AX, C), axis=-1)
        k = int(np.argmax(F))
        if F.flat[k] > best:
            best = float(F.flat[k])
            ii, jj = np.unravel_index(k, F.shape)
            arg = (E[ii, jj].copy(), bs[ii].copy(), Nv[ii, jj].copy())
    return best, arg


def nearest_axes(vec, AX, OD, count=4):
    ang = np.degrees(np.arccos(np.clip(np.abs(AX @ vec), 0, 1)))
    near = sorted((round(float(ang[i]), 4), int(OD[i])) for i in range(len(AX)))[:count]
    return ", ".join(f"order {m} at {a:.4f} deg" for a, m in near)


def main():
    G = build_2I()
    check_group(G)
    AX, OD = axes_of(G)
    C = cot_of(OD)
    print("Part 0")
    print(f"  2I: {len(G)} elements, closed under multiplication")
    print(f"  axes: {len(AX)} = {int(np.sum(OD == 2))} of order 2 + {int(np.sum(OD == 3))} of order 3"
          f" + {int(np.sum(OD == 5))} of order 5")
    assert (len(AX), int(np.sum(OD == 2)), int(np.sum(OD == 3)), int(np.sum(OD == 5))) == (31, 15, 10, 6)

    print("Part 1: closed form against the direct route")
    K = 120
    e, b, N = frames(K, seed=20261110)
    wc = wstar_closed(e, b, N, AX, C)
    wm = wstar_closed(e, b, N, AX, C, variant="mut_no_linear_term")
    # mutation arm 2: read five-fold axes at separation 2pi/5 instead of pi/5
    C2 = np.array([0.0 if m == 2 else (1 / math.tan(math.pi / 3) if m == 3 else 1 / math.tan(2 * math.pi / 5))
                   for m in OD])
    wm2 = wstar_closed(e, b, N, AX, C2)
    wd = np.array([wstar_direct(e[i], b[i], N[i], G) for i in range(K)])
    d_true = float(np.max(np.abs(wc - wd)))
    d_m1 = float(np.max(np.abs(wm - wd)))
    d_m2 = float(np.max(np.abs(wm2 - wd)))
    first = OD[np.argmin(T_closed(e, b, N, AX, C), axis=-1)]
    print(f"  poses: {K}")
    print(f"  max |closed - direct| below 1e-12 rad   {'PASS' if d_true < 1e-12 else 'FAIL'}")
    print(f"  mutation (no c|n_N| term): max difference {d_m1:.3f} rad   "
          f"{'fails as it should' if d_m1 > 1e-2 else 'NOT DETECTED'}")
    print(f"  mutation (five-fold at 2pi/5): max difference {d_m2:.3f} rad   "
          f"{'fails as it should' if d_m2 > 1e-2 else 'NOT DETECTED'}")
    print(f"  first axis to bind: five-fold in {int(np.sum(first == 5))} of {K} poses,"
          f" three-fold in {int(np.sum(first == 3))}, two-fold in {int(np.sum(first == 2))}")
    assert d_true < 1e-12 and d_m1 > 1e-2 and d_m2 > 1e-2

    print("Part 2: the maximum over poses")
    chunks, per = 30, 100_000
    pool = []
    for chunk in range(chunks):
        e, b, N = frames(per, seed=1000 + chunk)
        F = np.min(T_closed(e, b, N, AX, C), axis=-1)
        for i in np.argsort(F)[-12:]:
            M = np.stack([e[i], b[i], N[i]], axis=1)
            pool.append((float(F[i]), Rot.from_matrix(M).as_rotvec()))
    pool.sort(key=lambda z: -z[0])
    print(f"  random poses: {chunks * per}; best raw W_* = {math.atan(pool[0][0]) * DEG:.4f} deg")
    results = []
    for _, rv0 in pool[:240]:
        rv, t = refine(rv0, AX, C)
        results.append((t, rv))
    results.sort(key=lambda z: -z[0])
    tbest, rvbest = results[0]
    reached = sum(1 for tt, _ in results if tbest - tt < 1e-9)
    print(f"  240 best poses refined: largest W_* = {math.atan(tbest) * DEG:.6f} deg (tan W = {tbest:.8f})")
    print(f"  more than half of the 240 reach it to within 1e-9 in tan W: {reached > 120}")
    M = Rot.from_rotvec(rvbest).as_matrix()
    eb, bb, Nb = M[:, 0], M[:, 1], M[:, 2]
    T = T_closed(eb, bb, Nb, AX, C)
    act = np.where(T - T.min() < 1e-7)[0]
    print(f"  binding axes at the best pose (within 1e-7 in tan W): {len(act)} = {int(np.sum(OD[act] == 2))} two-fold"
          f" + {int(np.sum(OD[act] == 3))} three-fold + {int(np.sum(OD[act] == 5))} five-fold")
    print("  the axis b, nearest axes: " + nearest_axes(bb, AX, OD))
    print("  the pole N, nearest axes: " + nearest_axes(Nb, AX, OD))
    print("  the point e, nearest axes: " + nearest_axes(eb, AX, OD))
    gbest, garg = grid_cross_check(AX, OD, C)
    print(f"  grid cross-check over one (2,3,5) triangle: best grid W_* = {math.atan(gbest) * DEG:.6f} deg"
          f"   {'below the refined maximum' if gbest <= tbest + 1e-9 else 'ABOVE the refined maximum'}")
    Mg = np.stack(garg, axis=1)
    if np.linalg.det(Mg) < 0:
        Mg = Mg * np.array([1.0, 1.0, -1.0])
    rvg, tg = refine(Rot.from_matrix(Mg).as_rotvec(), AX, C)
    print(f"  refined from the grid's best point: W_* = {math.atan(tg) * DEG:.6f} deg")
    assert reached > 120 and gbest <= tbest + 1e-9 and abs(tg - tbest) < 1e-7

    print("Part 3: W_* over Haar-random poses")
    ws_, firsts = [], []
    for chunk in range(20):
        e, b, N = frames(100_000, seed=7700 + chunk)
        T = T_closed(e, b, N, AX, C)
        ws_.append(np.degrees(np.arctan(T.min(axis=-1))))
        firsts.append(OD[np.argmin(T, axis=-1)])
    w, first = np.concatenate(ws_), np.concatenate(firsts)
    qs = np.quantile(w, [0.05, 0.25, 0.5, 0.75, 0.95])
    print(f"  poses: {len(w)};  mean {np.mean(w):.3f} deg;  quantiles 5/25/50/75/95%: "
          + ", ".join(f"{q:.3f}" for q in qs) + f";  largest seen {np.max(w):.3f}")
    print(f"  first axis to bind: five-fold {np.mean(first == 5) * 100:.1f}%, three-fold {np.mean(first == 3) * 100:.1f}%,"
          f" two-fold {np.mean(first == 2) * 100:.1f}%")


if __name__ == "__main__":
    main()
