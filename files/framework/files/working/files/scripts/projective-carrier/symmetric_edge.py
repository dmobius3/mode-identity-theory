#!/usr/bin/env python3
"""Proposition 3.2 of projective-carrier.md: edge loops kept by deck transformations of RP³ → S³/2I; R = 1.

S³ is the unit quaternions, 2I acts by left multiplication, and the carrier's RP² lifts to the great sphere Σ of
purely imaginary quaternions. For an icosahedral axis a, G_a is the great circle of Σ orthogonal to a. No width is
printed: the checks are structural.

Checks (exit 1 on any failure):
  E1  2I has 120 elements, is closed under multiplication, and its 118 non-central elements lie on 31 axes
  E2  for every non-central g with axis a, Σ ∩ gΣ is G_a
  E3  the elements on a's axis map G_a onto itself and move a point of it through 2, 3 or 5 points of the projective
      line, for 2-, 3- and 5-fold axes
  E4  for every pair of distinct axes, G_a and G_b cross at ±a×b/|a×b| at the angle between a and b
  E5  for every pair of distinct axes, no non-central element maps G_a ∪ G_b onto itself
--arms plants a defect for each check and requires it to fire."""
import itertools
import sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-9
TS = np.linspace(0, 2 * np.pi, 25, endpoint=False)


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


def conj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def binary_icosahedral(plant=None):
    els = {}
    def add(v):
        els[tuple(np.round(v, 12))] = np.array(v, dtype=float)
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; add(v)
    for signs in itertools.product((0.5, -0.5), repeat=4):
        add(np.array(signs))
    even = [p for p in itertools.permutations(range(4))
            if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
    for s1, s2, s3 in itertools.product((1, -1), repeat=3):
        base = [0.0, s1 * 0.5, s2 * PHI / 2, s3 / (2 * PHI)]
        for p in even:
            add(np.array([base[p[k]] for k in range(4)]))
    G = list(els.values())
    if plant == "drop":
        G = G[1:]
    if plant == "nudge":                                   # one element turned slightly about its own axis:
        i = next(k for k, g in enumerate(G) if abs(abs(g[0]) - 1) > TOL)   # 120 elements and 31 axes remain
        th, a = np.arccos(G[i][0]) + 0.01, G[i][1:] / np.linalg.norm(G[i][1:])
        G = G[:i] + [np.concatenate([[np.cos(th)], np.sin(th) * a])] + G[i + 1:]
    return G


def axis_of(g):
    v = g[1:]
    return v / np.linalg.norm(v)


def axes_of(G):
    out = []
    for g in G:
        if abs(abs(g[0]) - 1) > TOL:
            a = axis_of(g)
            if not any(abs(abs(a @ b) - 1) < TOL for b in out):
                out.append(a)
    return out


def circle(a):
    """Points of G_a, as imaginary quaternions, and an orthonormal pair spanning its plane."""
    u = np.cross(a, [1.0, 0.0, 0.0] if abs(a[0]) < 0.9 else [0.0, 1.0, 0.0]); u /= np.linalg.norm(u)
    v = np.cross(a, u)
    return [np.concatenate([[0.0], np.cos(t) * u + np.sin(t) * v]) for t in TS], u, v


def on_axis(G, a):
    return [g for g in G if abs(abs(g[0]) - 1) > TOL and np.linalg.norm(np.cross(g[1:], a)) < 1e-9]


def on_circle(x, a):
    """x lies on G_a: purely imaginary, unit, orthogonal to a."""
    return abs(x[0]) < 1e-9 and abs(x[1:] @ a) < 1e-9 and abs(np.linalg.norm(x) - 1) < 1e-9


def checks(plant=None):
    r = {}
    G = binary_icosahedral(plant)
    keys = {tuple(np.round(k, 9)) for k in G}
    closed = all(tuple(np.round(qmul(g, h), 9)) in keys for g in G for h in G)      # every product, all 120 × 120
    A = axes_of(G)
    r["E1 2I: 120 elements, closed, 31 axes"] = len(G) == 120 and closed and len(A) == 31
    ok2 = True
    for g in G:
        if abs(abs(g[0]) - 1) < TOL:
            continue
        a = axis_of(g)
        if plant == "wrong-circle":
            a = np.array([a[1], a[2], a[0]])
        pts, u, v = circle(a)
        ok2 &= all(abs(qmul(conj(g), x)[0]) < 1e-9 for x in pts)          # G_a lies in gΣ as well as Σ
        off = np.concatenate([[0.0], (u + 0.3 * a) / np.linalg.norm(u + 0.3 * a)])
        ok2 &= abs(qmul(conj(g), off)[0]) > 1e-6                          # a point of Σ off G_a is not in gΣ
    r["E2 Σ ∩ gΣ is the great circle G_a"] = bool(ok2)
    ok3, kinds = True, set()
    for i, a in enumerate(A):
        H = on_axis(G, a)
        acting = on_axis(G, A[(i + 1) % len(A)]) if plant == "other-axis" else H
        pts, _, _ = circle(a)
        ok3 &= all(on_circle(qmul(h, x), a) for h in acting for x in pts)
        orbit = [qmul(h, pts[0]) for h in H + [np.array([1.0, 0, 0, 0])]]
        proj = {tuple(np.round(p if p[1:][np.argmax(np.abs(p[1:]) > 1e-9)] > 0 else -p, 9)) for p in orbit}
        kinds.add((len(H) + 2, len(proj)))
    ok3 &= kinds == {(4, 2), (6, 3), (10, 5)}
    r["E3 axis elements keep G_a, moving a point through 2, 3 or 5 points"] = bool(ok3)
    ok4 = True
    for a, b in itertools.combinations(A, 2):
        p = np.cross(a, b); p /= np.linalg.norm(p)
        if plant == "wrong-crossing":
            p = (a + b) / np.linalg.norm(a + b)
        ta, tb = np.cross(a, p), np.cross(b, p)
        ang = np.arccos(np.clip(abs(ta @ tb) / np.linalg.norm(ta) / np.linalg.norm(tb), -1, 1))
        theta = np.arccos(np.clip(abs(a @ b), -1, 1))
        ok4 &= abs(p @ a) < 1e-9 and abs(p @ b) < 1e-9 and abs(ang - theta) < 1e-9
    r["E4 G_a and G_b cross at ±a×b at the angle between a and b"] = bool(ok4)
    ok5 = True
    nonc = [g for g in G if abs(abs(g[0]) - 1) > TOL]
    for a, b in itertools.combinations(A, 2):
        if plant == "same-axis":
            b = a
        pa, _, _ = circle(a)
        pb, _, _ = circle(b)
        for g in nonc:
            keeps = all(on_circle(qmul(g, x), a) or on_circle(qmul(g, x), b) for x in pa + pb)
            ok5 &= not keeps
            if not ok5:
                break
        if not ok5:
            break
    r["E5 no non-central element keeps the two-loop edge"] = bool(ok5)
    return r


def main():
    res = checks()
    names = list(res)
    for name in names:
        print(("PASS " if res[name] else "FAIL ") + name)
    green = all(res.values())
    if "--arms" in sys.argv:
        assert green, "arms need a green parent"
        rc = 0
        E1, E2, E3, E4, E5 = names
        plants = {"drop": [E1],                 # one element of 2I removed
                  "nudge": [E1],                # one element turned about its axis: closure fails alone
                  "wrong-circle": [E2],         # the great circle orthogonal to a permuted axis
                  "other-axis": [E3],           # G_a acted on by the elements of a different axis
                  "wrong-crossing": [E4],       # the crossing put at the normalized a + b
                  "same-axis": [E5]}            # both loops on one axis, which its elements keep
        for plant, targets in plants.items():
            res_p = checks(plant)
            for t in targets:
                fired = not res_p[t]
                print(("ARM FIRED " if fired else "ARM SILENT ") + f"{t} [{plant}]")
                rc |= 0 if fired else 1
        return rc
    return 0 if green else 1


if __name__ == "__main__":
    sys.exit(main())
