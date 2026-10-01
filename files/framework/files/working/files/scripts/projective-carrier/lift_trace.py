#!/usr/bin/env python3
"""Proposition 5 of projective-carrier.md: the lift of the conic band's edge to the great S² ⊂ S³; R = 1.

The band is the rectangle [0, π] × [−W, W] with the seam (0, w) ~ (π, −w). First eigenvalue Proposition 4.2's trivialization maps it
onto the lune L: (y, w) ↦ (latitude y, longitude w) for y ≤ π/2, and (latitude −(π − y), longitude −w) for y ≥ π/2.
The preimages of a band point in S³ are ±Φ(y, w), in the pieces L and −L. Over the smooth locus, which is simply
connected, these are the cover's two sheets; their closures meet only at N and −N, over the cone point. The oriented
edge runs w = +W from y = 0 to π, crosses the seam, then w = −W from y = 0 to π. The lift picks, at each step, the
preimage nearest the last point.

Checks at W ∈ {0.3, 0.7, 1.2, 1.5} (exit 1 on any failure):
  L1  the lift is continuous (every step shorter than 0.05) and closes after one traversal
  L2  it passes N once and S = −N once
  L3  it passes from L to −L and back, once at each pole
  L4  its four stretches match the table in §VII: longitude, piece and direction
  L5  it bounds the lune between longitudes W and π − W; with its image under −I it fills the two great circles
      through N and S at longitudes ±W and π ± W
--arms plants a defect for each check and requires it to fire."""
import sys
import numpy as np

WIDTHS = (0.3, 0.7, 1.2, 1.5)
N_STEP = 4001


def sphere(la, lo):
    return np.array([np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)])


ROT90 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.0]])


def phi(yv, wv, plant=None):
    if yv <= np.pi / 2:
        q = sphere(yv, wv)
    else:
        q = sphere(-(np.pi - yv), wv if plant == "seam" else -wv)
    return ROT90 @ q if plant == "shift" else q


def lon_of(p):
    return np.mod(np.arctan2(p[1], p[0]), 2 * np.pi)


def trace(W, plant=None):
    ys = np.linspace(0, np.pi, N_STEP)
    ys = ys[np.abs(ys - np.pi / 2) > 1e-9]
    path = [(yv, +W) for yv in ys] + [(yv, -W) for yv in ys]
    pts, pieces = [], []
    for yv, wv in path:
        q = phi(yv, wv, plant)
        if not pts:
            pts.append(q), pieces.append(+1)
            continue
        if plant == "one-piece":
            s = +1
        else:
            s = +1 if np.linalg.norm(q - pts[-1]) <= np.linalg.norm(-q - pts[-1]) else -1
        pts.append(s * q), pieces.append(s)
    return path, np.array(pts), np.array(pieces)


def same_set(vals, targets, tol=1e-9):
    """Every value sits within tol of a target (mod 2π), and every target is hit."""
    d = lambda a, b: abs(np.mod(a - b + np.pi, 2 * np.pi) - np.pi)
    return all(min(d(v, t) for t in targets) < tol for v in vals) and all(min(d(v, t) for v in vals) < tol for t in targets)


def near(pts, target, eps=0.02):
    runs, inside = 0, False
    for p in pts:
        d = np.linalg.norm(p - target) < eps
        runs += d and not inside
        inside = d
    return runs


def checks(W, plant=None):
    path, pts, pieces = trace(W, plant)
    Np, Sp = np.array([0, 0, 1.0]), np.array([0, 0, -1.0])
    start = phi(0.0, W, plant)
    steps = np.linalg.norm(np.diff(pts, axis=0), axis=1)
    closes = np.linalg.norm(pts[-1] - start) < 1e-9   # (π, −W) is the seam image of (0, W)
    r = {"L1 continuous and closes after one traversal": steps.max() < 0.05 and closes,
         "L2 passes N once and S once": near(pts, Np) == 1 and near(pts, Sp) == 1}
    crossings = np.nonzero(np.diff(pieces))[0]
    at_poles = all(min(np.linalg.norm(pts[i] - Np), np.linalg.norm(pts[i] - Sp)) < 0.02 for i in crossings)
    r["L3 passes from L to −L and back, once at each pole"] = len(crossings) == 2 and at_poles
    half = len(path) // 2
    q = half // 2
    stretches = [(0, q), (q, half), (half, half + q), (half + q, len(path))]
    expect = [(W, +1, "up N"), (np.pi - W, -1, "down N"), (np.pi - W, -1, "down S"), (W, +1, "up S")]
    ok4 = True
    for (a, b), (lo, sh, how) in zip(stretches, expect):
        seg, ss = pts[a:b], pieces[a:b]
        away = [p for p in seg if abs(p[2]) < 0.999]
        ok4 &= all(abs(lon_of(p) - lo) < 1e-9 for p in away) and np.all(ss == sh)
        z0, z1 = seg[0][2], seg[-1][2]
        ok4 &= {"up N": z1 > z0 and z1 > 0.99, "down N": z0 > 0.99 and z1 < z0,
                "down S": z1 < z0 and z1 < -0.99, "up S": z0 < -0.99 and z1 > z0}[how]
    r["L4 the four stretches match §VII's table"] = bool(ok4)
    away = [p for p in pts if abs(p[2]) < 0.999]
    lons = [lon_of(p) for p in away]
    both = lons + [lon_of(-p) for p in away]                      # the image under −I
    lune = [W, np.pi - W]
    circles = [W, np.pi - W, np.pi + W, 2 * np.pi - W]
    r["L5 bounds the complementary lune; with −I, two great circles"] = (same_set(lons, lune) and same_set(both, circles)
                                                                      and W < np.pi / 2 < np.pi - W)
    return r


def main():
    allres = {W: checks(W) for W in WIDTHS}
    names = list(next(iter(allres.values())))
    for name in names:
        ok = all(allres[W][name] for W in WIDTHS)
        print(("PASS " if ok else "FAIL ") + name)
    green = all(all(v.values()) for v in allres.values())
    if "--arms" in sys.argv:
        assert green, "arms need a green parent"
        rc = 0
        L1, L2, L3, L4, L5 = names
        plants = {"seam": [L1, L4],            # the seam glued without its flip: an annulus-like gluing
                  "one-piece": [L1, L2, L3],   # the lift kept on L: it jumps N to S and visits each pole twice
                  "shift": [L4, L5]}           # the band placed on the wrong lune, longitudes shifted by π/2
        for plant, targets in plants.items():
            res = checks(0.7, plant)
            for t in targets:
                fired = not res[t]
                print(("ARM FIRED " if fired else "ARM SILENT ") + f"{t} [{plant}]")
                rc |= 0 if fired else 1
        return rc
    return 0 if green else 1


if __name__ == "__main__":
    sys.exit(main())
