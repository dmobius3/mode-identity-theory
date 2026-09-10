#!/usr/bin/env python3
"""plato-twist.test.py -- the weak coupling's cos(pi/10) as a holonomy invariant of S^3/2I (2026-09-10).

Companion to plato-twist.md. Builds the binary icosahedral group 2I as 120 unit quaternions
and checks, on the closed geodesics of S^3/2I (round metric, 2I acting by left multiplication):

  1. 2I is a group of 120 unit quaternions; its doublet half-traces are
     +-1, +-phi/2, +-1/(2 phi), +-1/2, 0, so cos(pi/10) is never one of them.
  2. cos(pi/10) is a root of 16x^4 - 20x^2 + 5 (irreducible, Eisenstein at 5): degree 4,
     outside Q(sqrt5), where every 2I character lies.
  3. The face-pairing elements are the twelve order-10 elements 36 deg from the identity;
     their doublet half-trace is cos(pi/5) and their rotation of three-space is 72 deg.
  4. Levi-Civita transport around the shortest closed geodesic returns a frame rotated by
     pi/5, the dodecahedral gluing twist. The continuous lift of the frame path to SU(2)
     ends at half-trace cos(pi/10). The mirror quotient gives the opposite handedness.
  5. On every geodesic class the frame rotation equals the class length, so the
     spin-lifted half-trace is sqrt((1 + flat half-trace)/2).
  6. Caveat: a matrix element of flat holonomy on a chosen spinor, polarized along a
     two-fold axis adjacent to the loop's five-fold axis, has modulus cos(pi/10).
  7. The weak-row residuals printed in plato-twist.md.
  Mutation arm: substituting the deck element's own rotation of three-space (72 deg) for the
  transported frame must fail the pi/5 check.

Run from anywhere: python3 plato-twist.test.py   (needs numpy)
"""
import itertools
import math
import sys

import numpy as np

FAILED = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAILED.append(name)
    return ok


PHI = (1 + 5 ** 0.5) / 2
COS5, COS10 = math.cos(math.pi / 5), math.cos(math.pi / 10)
ONE = np.array([1.0, 0.0, 0.0, 0.0])


def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
                     w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
                     w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def conj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def key(q):
    return tuple(np.round(q, 9))


# 1. 2I: 24 Hurwitz units and 96 even permutations of (0, +-1, +-1/phi, +-phi)/2
elements = []
for i in range(4):
    for s in (1, -1):
        v = np.zeros(4)
        v[i] = s
        elements.append(v)
for signs in itertools.product((1, -1), repeat=4):
    elements.append(np.array(signs) / 2)
for perm in itertools.permutations(range(4)):
    if sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4)) % 2:
        continue
    for s in itertools.product((1, -1), repeat=3):
        vals = [0.0, s[0], s[1] / PHI, s[2] * PHI]
        v = np.zeros(4)
        for k in range(4):
            v[perm[k]] = vals[k] / 2
        elements.append(v)
E = np.array(elements)
KEYS = {key(q) for q in E}
check("2I: 120 distinct unit quaternions",
      len(E) == 120 and len(KEYS) == 120 and np.allclose(np.linalg.norm(E, axis=1), 1))
check("2I is closed under multiplication", all(key(qmul(a, b)) in KEYS for a in E for b in E))

half = sorted({round(float(q[0]), 9) for q in E})
expected = sorted({round(x, 9) for x in (1, -1, 0.5, -0.5, 0, PHI / 2, -PHI / 2, (PHI - 1) / 2, -(PHI - 1) / 2)})
check("doublet half-traces are +-1, +-phi/2, +-1/(2 phi), +-1/2, 0", half == expected)
check("cos(pi/10) is not the half-trace of any element", all(abs(h - COS10) > 1e-6 for h in half))

# 2. the degree of cos(pi/10)
check("cos(pi/10) is a root of 16x^4 - 20x^2 + 5", abs(16 * COS10 ** 4 - 20 * COS10 ** 2 + 5) < 1e-12)
check("its square (5 + sqrt5)/8 lies in Q(sqrt5)", abs(COS10 ** 2 - (5 + 5 ** 0.5) / 8) < 1e-12)

# 3. the face pairing
angle_deg = np.degrees(np.arccos(np.clip(E[:, 0], -1, 1)))
nearest = E[np.isclose(angle_deg, 36.0)]
check("twelve elements at 36 deg from the identity (the dodecahedral Dirichlet domain)", len(nearest) == 12)
g = nearest[0]


def order(q):
    r = ONE.copy()
    for k in range(1, 121):
        r = qmul(r, q)
        if np.allclose(r, ONE):
            return k
    return None


def so3(q):
    """Rotation of Im H by conjugation, as a 3x3 matrix whose columns are the images of i, j, k."""
    return np.array([qmul(qmul(q, np.r_[0.0, e]), conj(q))[1:] for e in np.eye(3)]).T


def rotation_angle(R):
    return math.acos(max(-1.0, min(1.0, (np.trace(R) - 1) / 2)))


check("face-pairing element: order 10, doublet half-trace cos(pi/5)",
      order(g) == 10 and abs(g[0] - COS5) < 1e-12)
check("its rotation of three-space is the 72 deg five-fold turn",
      abs(math.degrees(rotation_angle(so3(g))) - 72) < 1e-9)


# 4. Levi-Civita transport around the closed geodesic from 1 to a deck element q
def rot_to_quat(R):
    w = math.sqrt(max(0.0, 1 + np.trace(R))) / 2
    return np.array([w, (R[2, 1] - R[1, 2]) / (4 * w), (R[0, 2] - R[2, 0]) / (4 * w),
                     (R[1, 0] - R[0, 1]) / (4 * w)])


def transport(q, pull, steps=4000, checkpoints=100):
    """Parallel-transport the frame i, j, k along t -> cos t + sin t n, t in [0, a], gamma(a) = q,
    pulling each vector back to the identity with pull(gamma(t), v). Returns the holonomy matrix,
    the continuous SU(2) lift of the frame path started at +1, and the unit axis n."""
    a = math.acos(q[0])
    n = q[1:] / np.linalg.norm(q[1:])
    gam = lambda t: np.r_[math.cos(t), math.sin(t) * n]
    dgam = lambda t: np.r_[-math.sin(t), math.cos(t) * n]
    rhs = lambda t, V: -np.outer(V @ dgam(t), gam(t))      # D/dt V = 0 on the round S^3 in R^4
    V = np.array([np.r_[0.0, e] for e in np.eye(3)])
    h, t, lift = a / steps, 0.0, ONE.copy()
    for s in range(steps):
        k1 = rhs(t, V)
        k2 = rhs(t + h / 2, V + h / 2 * k1)
        k3 = rhs(t + h / 2, V + h / 2 * k2)
        k4 = rhs(t + h, V + h * k3)
        V = V + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
        if (s + 1) % (steps // checkpoints) == 0:
            R = np.array([pull(gam(t), v)[1:] for v in V]).T
            nxt = rot_to_quat(R)
            lift = nxt if nxt @ lift >= 0 else -nxt
    H = np.array([pull(gam(a), v)[1:] for v in V]).T
    return H, lift, n


deck_left = lambda x, v: qmul(conj(x), v)                   # the quotient by x -> g x
deck_right = lambda x, v: qmul(v, conj(x))                  # its mirror image, x -> x g

H, lift, n = transport(g, deck_left)
is_rotation = np.allclose(H @ H.T, np.eye(3), atol=1e-9) and abs(np.linalg.det(H) - 1) < 1e-9
theta = rotation_angle(H)
parent = check("Levi-Civita holonomy on the shortest geodesic is a rotation by pi/5",
               is_rotation and abs(theta - math.pi / 5) < 1e-8, f"{math.degrees(theta):.6f} deg")
check("continuous spin lift of the frame path ends at half-trace cos(pi/10)",
      abs(lift[0] - COS10) < 1e-9, f"{lift[0]:.9f}")

H_m, lift_m, _ = transport(g, deck_right)
axial = lambda M: np.array([M[2, 1] - M[1, 2], M[0, 2] - M[2, 0], M[1, 0] - M[0, 1]])
check("mirror quotient: same angle and half-trace, opposite handedness",
      abs(rotation_angle(H_m) - theta) < 1e-8 and abs(lift_m[0] - lift[0]) < 1e-9
      and np.sign(axial(H) @ n) == -np.sign(axial(H_m) @ n))

if parent:  # a mutation arm needs a green parent
    th_x = rotation_angle(so3(g))     # mutation: the deck element's own rotation in place of the transport
    check("mutation: the deck element's 72 deg rotation in place of the transported frame fails the pi/5 test",
          abs(th_x - math.pi / 5) > 1e-3, f"{math.degrees(th_x):.6f} deg")

# 5. every geodesic class: frame rotation = length, spin half-trace = sqrt((1 + flat)/2)
print("\n  class length | flat half-trace | frame rotation | spin half-trace")
ok = True
for r in sorted({round(float(q[0]), 9) for q in E if abs(q[0]) < 1 - 1e-9}, reverse=True):
    rep = next(q for q in E if abs(q[0] - r) < 1e-9)
    Hc, liftc, _ = transport(rep, deck_left)
    length, th = math.acos(r), rotation_angle(Hc)
    ok = ok and abs(th - length) < 1e-7 and abs(liftc[0] - math.sqrt((1 + r) / 2)) < 1e-9
    print(f"  {math.degrees(length):7.1f} deg  | {r:+.6f}       | {math.degrees(th):8.4f} deg  | {liftc[0]:.6f}")
check("on every class the frame rotation equals the length, so spin = sqrt((1 + flat)/2)", ok)

# 6. caveat: a matrix element of flat holonomy can reach cos(pi/10)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def su2(q):
    w, x, y, z = q
    return w * np.eye(2) - 1j * (x * SX + y * SY + z * SZ)


check("the quaternion-to-SU(2) map is a homomorphism",
      all(np.allclose(su2(qmul(a, b)), su2(a) @ su2(b)) for a in E[::6] for b in E[::6]))
twofold = [q[1:] / np.linalg.norm(q[1:]) for q in E if abs(q[0]) < 1e-9]
m = max(twofold, key=lambda u: abs(u @ n))
evals, evecs = np.linalg.eigh(m[0] * SX + m[1] * SY + m[2] * SZ)
psi = evecs[:, np.argmax(evals)]
amp = abs(np.conj(psi) @ su2(g) @ psi)
check("caveat: |<psi|U|psi>| = cos(pi/10) for a spinor on an adjacent two-fold axis",
      abs(amp - COS10) < 1e-9, f"axis angle {math.degrees(math.acos(abs(m @ n))):.4f} deg, modulus {amp:.9f}")

# 7. weak-row residuals, at the precision printed in plato-twist.md
C = lambda t: 2 * math.sin(math.pi * t) ** 2
untwisted = C(17 / 120) * (1.054e122) ** (-1 / 120)
target = (1 / 127.95) / 0.23122          # alpha-hat(M_Z) / s-hat^2_Z, MS-bar
for name, factor, printed in (("no factor", 1.0, 5.5),
                              ("the spin-lifted half-trace cos(pi/10)", COS10, 0.3),
                              ("its square cos^2(pi/10)", COS10 ** 2, -4.6),
                              ("the flat doublet half-trace cos(pi/5)", COS5, -14.7)):
    residual = 100 * (untwisted * factor / target - 1)
    check(f"weak residual with {name} prints as {printed:+.1f}%", round(residual, 1) == printed,
          f"{residual:+.3f}%")

print("\nALL PASS" if not FAILED else "\nFAILED: " + "; ".join(FAILED))
sys.exit(1 if FAILED else 0)
