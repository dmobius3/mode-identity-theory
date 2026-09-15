#!/usr/bin/env python3
"""Checks for the missing spatial projection: R7's construction attempt, run under a work order frozen before it.

The attempt found no map from MIT's existing objects to flat spatial data. These checks back the obstructions the page
gives for why standard geometry cannot supply the missing arrow, and the one existing scale they rule out.

  A  the exponential map at the observer does not carry distances on the round S³ to translation-invariant ones:
     translating a pair of points in the tangent space changes their pulled-back distance, while on flat R³, the
     control, it does not
  B  the same failure for a shell's correlation: the N = 12 whole-shell law on S³, pulled back, is not
     translation-invariant, while a flat shell kernel, used as the control, is
  C  so(3), the Lie algebra of the domain's isometries, has no two-dimensional abelian subalgebra: its bracket is the
     cross product, so two generators commute only when they are parallel
  D  the observer scale sqrt(l_P R_Lambda) ~ 50 micrometres acts on the Molien shells as the identity: a Gaussian
     smoothing of that width changes a shell with N <= 60 by about 2e-58
  E  under the isotropy group A5, built as the 60 rotations of 2I, the symmetric 2-tensors on the tangent space carry
     exactly one invariant, the metric; so a nonconstant homogeneous law's gradient covariance is a positive multiple of it
Mutation arms, each of which must turn its claim red: the flat distance in place of the round one (A), the flat
kernel in place of the shell's (B), the zero bracket in place of the cross product (C), a scale of R/10 (D), the
cyclic group of order 5 in place of A5 (E).
Units: the unit S³ (R = 1) in A-C; metres in D.
"""
import itertools
import math

import numpy as np

RNG = np.random.default_rng(20260915)
PAIRS = 4000
BALL, SHIFT = 0.1, 0.1          # A: all points stay within 0.2 of the observer, inside S³/2I's injectivity radius pi/10
BALL_B, SHIFT_B = 0.15, 0.15    # B: within 0.3, still inside it


def sample(n, radius):
    v = RNG.normal(size=(n, 3))
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    return v * radius * RNG.random((n, 1)) ** (1 / 3)


U, W, A = sample(PAIRS, BALL), sample(PAIRS, BALL), sample(PAIRS, SHIFT)
UB, WB, AB = sample(PAIRS, BALL_B), sample(PAIRS, BALL_B), sample(PAIRS, SHIFT_B)


def exp_s3(u):
    """The exponential map at the identity of the unit quaternions: u in R³ goes to (cos|u|, sin|u| u/|u|)."""
    r = np.linalg.norm(u, axis=-1, keepdims=True)
    safe = np.where(r > 0, r, 1.0)
    return np.concatenate([np.cos(r), np.where(r > 0, np.sin(r) / safe, 1.0) * u], axis=-1)


def d_round(u, w):
    """Geodesic distance on the unit S³ between exp(u) and exp(w)."""
    return np.arccos(np.clip(np.sum(exp_s3(u) * exp_s3(w), axis=-1), -1.0, 1.0))


def d_flat(u, w):
    return np.linalg.norm(u - w, axis=-1)


def shell_round(u, w, N=12):
    """The whole-shell law of shell N on the unit S³, sin((N+1) theta)/((N+1) sin theta), normalized to 1 at theta = 0."""
    th = d_round(u, w)
    small = th < 1e-9
    return np.where(small, 1.0, np.sin((N + 1) * th) / ((N + 1) * np.sin(np.where(small, 1.0, th))))


def shell_flat(u, w, N=12):
    """A flat shell kernel, j0(k r), used as the translation-invariant control; its wavenumber does not matter to claim B."""
    r = d_flat(u, w)
    k = N + 1
    small = r < 1e-9
    return np.where(small, 1.0, np.sin(k * r) / (k * np.where(small, 1.0, r)))


def defect(f, u, w, a):
    return float(np.max(np.abs(f(u + a, w + a) - f(u, w))))


def hat(x):
    return np.array([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])


def bracket_claim(bracket):
    """so(3)'s bracket equals the cross product, and is nonzero on every non-parallel pair sampled."""
    worst_identity, least_norm = 0.0, math.inf
    for _ in range(500):
        x, y = RNG.normal(size=3), RNG.normal(size=3)
        c = bracket(hat(x), hat(y))
        worst_identity = max(worst_identity, float(np.max(np.abs(c - hat(np.cross(x, y))))))
        sin_angle = np.linalg.norm(np.cross(x, y)) / (np.linalg.norm(x) * np.linalg.norm(y))
        if sin_angle > 1e-3:
            least_norm = min(least_norm, float(np.linalg.norm(c)))
    return worst_identity < 1e-12 and least_norm > 0, worst_identity, least_norm


def smoothing_deviation(ratio, nmax=60):
    """Largest change a Gaussian smoothing of width ratio * R makes to a shell N <= nmax, computed as a deviation."""
    return max(-math.expm1(-N * (N + 2) * ratio**2 / 2) for N in range(1, nmax + 1))


def parity(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2


def binary_icosahedral():
    """The 120 unit quaternions of 2I: the 8 axis units, the 16 half-units, and the 96 even permutations of
    (0, +-1, +-phi, +-1/phi)/2."""
    phi = (1 + 5 ** 0.5) / 2
    qs = []
    for i in range(4):
        for s in (1.0, -1.0):
            q = [0.0] * 4
            q[i] = s
            qs.append(q)
    for signs in itertools.product((0.5, -0.5), repeat=4):
        qs.append(list(signs))
    base = [0.0, 1.0, phi, 1 / phi]
    for p in itertools.permutations(range(4)):
        if parity(p):
            continue
        v = [base[p[k]] for k in range(4)]
        nz = [k for k in range(4) if v[k] != 0]
        for signs in itertools.product((1, -1), repeat=3):
            w = list(v)
            for k, s in zip(nz, signs):
                w[k] *= s
            qs.append([x / 2 for x in w])
    return np.array(qs)


def rotation(q):
    w, x, y, z = q
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)],
                     [2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)],
                     [2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)]])


def icosahedral_rotations():
    """A5 as the 60 distinct rotations the 120 quaternions of 2I induce, checked closed under products."""
    key = lambda m: tuple(np.round(m, 9).ravel())
    seen = {}
    for q in binary_icosahedral():
        assert abs(np.dot(q, q) - 1) < 1e-12
        m = rotation(q)
        seen.setdefault(key(m), m)
    group = list(seen.values())
    closed = all(key(a @ b) in seen for a in group for b in group)
    return group, closed


def sym2_invariants(group):
    """The number of invariant symmetric 2-tensors: the group average of the character of Sym², (tr g^2 + tr(g^2))/2."""
    return sum((np.trace(g) ** 2 + np.trace(g @ g)) / 2 for g in group) / len(group)


def main():
    print("A  exponential-map pullback, unit S³, %d pairs within %.2f with shifts up to %.2f" % (PAIRS, BALL, SHIFT))
    a_round, a_flat = defect(d_round, U, W, A), defect(d_flat, U, W, A)
    ok_a = a_round > 1e-4 and a_flat < 1e-12
    print("   the pulled-back distance changes under translation by up to %.2g on the round S³; on flat R³ below 1e-12: %s"
          % (a_round, "PASS" if ok_a else "FAIL"))
    print("B  the N = 12 whole-shell law, %d pairs within %.2f with shifts up to %.2f" % (PAIRS, BALL_B, SHIFT_B))
    b_round, b_flat = defect(shell_round, UB, WB, AB), defect(shell_flat, UB, WB, AB)
    ok_b = b_round > 1e-3 and b_flat < 1e-12
    print("   the pulled-back correlation changes under translation by up to %.2g; the flat shell kernel below 1e-12: %s"
          % (b_round, "PASS" if ok_b else "FAIL"))
    print("C  so(3): the bracket of the domain's isometry generators")
    ok_c, worst, least = bracket_claim(lambda x, y: x @ y - y @ x)
    print("   [x, y] equals the cross product (below 1e-12), nonzero on every non-parallel pair (least %.2g): %s"
          % (least, "PASS" if ok_c else "FAIL"))
    print("D  the observer scale, sqrt(l_P R_Lambda) = 50 micrometres (the engine page)")
    l_p, l_obs = 1.616255e-35, 50e-6
    ratio = l_p / l_obs                     # l_obs / R_Lambda, with R_Lambda = l_obs^2 / l_P
    dev = smoothing_deviation(ratio)
    ok_d = dev < 1e-50
    print("   l_obs / R_Lambda = %.2g; the largest change to a shell N <= 60 is %.2g: %s" % (ratio, dev, "PASS" if ok_d else "FAIL"))
    print("E  the isotropy group A5 on the tangent space")
    group, closed = icosahedral_rotations()
    n_inv = sym2_invariants(group)
    ok_e = len(group) == 60 and closed and abs(n_inv - 1) < 1e-9
    print("   %d rotations, closed under products: %s; invariant symmetric 2-tensors: %d (the metric): %s"
          % (len(group), "yes" if closed else "no", round(n_inv), "PASS" if ok_e else "FAIL"))
    claims = (not ok_a) + (not ok_b) + (not ok_c) + (not ok_d) + (not ok_e)
    five = next(g for g in group if abs(np.trace(g) - (1 + 5 ** 0.5) / 2) < 1e-9)
    cyclic = [np.linalg.matrix_power(five, k) for k in range(5)]
    arm_a = not (defect(d_flat, U, W, A) > 1e-4 and a_flat < 1e-12)
    arm_b = not (defect(shell_flat, UB, WB, AB) > 1e-3 and b_flat < 1e-12)
    arm_c = not bracket_claim(lambda x, y: np.zeros((3, 3)))[0]
    arm_d = not (smoothing_deviation(0.1) < 1e-50)
    arm_e = abs(sym2_invariants(cyclic) - 1) > 1e-9
    arms = (("flat distance in place of the round one (A)", arm_a), ("flat kernel in place of the shell's (B)", arm_b),
            ("zero bracket in place of the cross product (C)", arm_c), ("a scale of R/10 (D)", arm_d),
            ("the cyclic group of order 5 in place of A5 (E)", arm_e))
    print("arms")
    for name, hit in arms:
        print("   arm: %-46s %s" % (name, "RED" if hit else "STAYED GREEN"))
    n_red = sum(hit for _, hit in arms)
    print("%d claims failed; %d/%d arms red" % (claims, n_red, len(arms)))
    return 0 if claims == 0 and n_red == len(arms) else 1


if __name__ == "__main__":
    raise SystemExit(main())
