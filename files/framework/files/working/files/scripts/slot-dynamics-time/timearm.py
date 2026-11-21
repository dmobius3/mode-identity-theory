"""The time arm (DESIGN.md sections 4 and 5) and the diagnostics the controls read. New code.

The state is the instrument's complex coefficients c and their time derivative v; the real form of DESIGN.md is
q = (Re c, Im c), p = (Re v, Im v). The equation is c'' = -e c - cubic(c), with e the levels' n(n+2).

- verlet: velocity Stormer-Verlet, one cubic per step, the force at a step's end reused as the next step's first.
- strang: the exact linear flow over h/2, a kick by -h cubic(c), the exact linear flow over h/2; one cubic per step.
- Both stop when ||c||^2 exceeds cbar, checked at the start and at every step (DESIGN.md section 5), by raising
  Ceiling.
- matched(...): the initial state that each stepper carries as an exact discrete rotation on a rigid slot's
  lowest-level orbit, where the force is -(e0 + ||c||^2) c, and the rotation angle per step.
- Diagnostics: the energy H; the charges J_D = p^T D q for the phase, right SU(2) and, in the quaternionic slots, the
  two further Sp(1) generators J and iJ; the quadratic energy of each level; the symmetry maps for equivariance."""
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import fftcubic  # noqa: E402,F401  (checks the pin and puts the instrument on the path)
from instrument import functional as fn, group2i  # noqa: E402


class Ceiling(Exception):
    """||c||^2 rose above the run's fixed ceiling: the step bound's premise failed, and the run stops."""


def _guard(c, cbar, step):
    if cbar is not None and np.vdot(c, c).real > cbar:
        raise Ceiling(f'||c||^2 = {np.vdot(c, c).real:.6e} > {cbar:.6e} at step {step}')


def verlet(c, v, h, nsteps, e, cubic, a=None, cbar=None, observe=None, every=1):
    _guard(c, cbar, 0)
    if a is None:
        a = -e * c - cubic(c)
    for s in range(1, nsteps + 1):
        v = v + 0.5 * h * a
        c = c + h * v
        _guard(c, cbar, s)
        a = -e * c - cubic(c)
        v = v + 0.5 * h * a
        if observe is not None and s % every == 0:
            observe(s, c, v)
    return c, v, a


def strang(c, v, h, nsteps, e, cubic, cbar=None, observe=None, every=1):
    """The exact rotation of each mode over h/2 is applied as three shears, c += a v, v += b c, c += a v, with
    a = tan(phi/2)/w, b = -w sin(phi) and phi = w h/2: the same map in exact arithmetic, and of determinant exactly 1
    for the rounded a and b, so round-off does not bias each mode's energy step after step (DEVLOG entry 5)."""
    assert np.all(e > 0), 'the exact linear flow here needs every level above n = 0'
    w = np.sqrt(e)
    phi = 0.5 * h * w
    assert np.max(np.abs(phi)) < np.pi, 'the three-shear rotation needs |w h / 2| < pi'
    a, b = np.tan(0.5 * phi) / w, -w * np.sin(phi)
    _guard(c, cbar, 0)

    def rotate(c, v):
        c = c + a * v
        v = v + b * c
        return c + a * v, v

    for s in range(1, nsteps + 1):
        c, v = rotate(c, v)
        _guard(c, cbar, s)
        v = v - h * cubic(c)
        c, v = rotate(c, v)
        _guard(c, cbar, s)
        if observe is not None and s % every == 0:
            observe(s, c, v)
    return c, v


def rotation(t, w):
    """The exact linear flow of z'' = -w^2 z over time t, as a real 2 x 2 map on (z, z')."""
    return np.array([[np.cos(t * w), np.sin(t * w) / w], [-w * np.sin(t * w), np.cos(t * w)]])


def matched(kind, h, w2, kappa):
    """(z0, dz0, theta) on a rigid slot's lowest-level orbit, where the force is -(w2 + ||c||^2) c (DESIGN.md section 4).
    For any phi on the orbit with ||phi||^2 = kappa, the stepper started at (z0 phi, dz0 phi) carries the exact discrete
    rotation c_n = e^{i n theta} z0 phi, 0 < theta < pi, with every kick reading the orbit at norm^2 kappa, so that the
    force is linear on it.
      Verlet's kicks read the state at the step's ends: z0 = 1, theta = 2 arcsin(h sqrt(w2 + kappa) / 2) and
    dz0 = i sin(theta) / h, the velocity standing_velocity sets.
      The splitting's kick reads the state after the first half rotation, so the wave is normalized there: (1, mu) is
    the eigenvector of the map R(h) S(kappa) from one kick to the next, and (z0, dz0) = R(-h/2) (1, mu). Its
    cos theta = cos(w0 h) - (kappa h / 2 w0) sin(w0 h), the trace of R(h/2) S(kappa) R(h/2), which R(h) S(kappa)
    shares; the norm^2 at the step's ends is kappa |z0|^2. In closed form, 1 - cos theta = 2 sin^2(w0 h / 2) +
    (kappa h / 2 w0) sin(w0 h), with no cancellation, and mu = kappa h / 2 + i w0 sin(theta) / sin(w0 h)."""
    if kind == 'verlet':
        theta = 2 * np.arcsin(h * np.sqrt(w2 + kappa) / 2)
        return 1.0 + 0j, 1j * np.sin(theta) / h, float(theta)
    w = np.sqrt(w2)
    one_minus = 2 * np.sin(0.5 * w * h) ** 2 + 0.5 * kappa * h * np.sin(w * h) / w
    assert 0 < one_minus < 2 and np.sin(w * h) > 0, (one_minus, w * h)
    theta = float(2 * np.arcsin(np.sqrt(0.5 * one_minus)))
    mu = 0.5 * kappa * h + 1j * w * np.sin(theta) / np.sin(w * h)
    z0, dz0 = rotation(-0.5 * h, w) @ np.array([1.0, mu])
    return complex(z0), complex(dz0), theta


class Diagnostics:
    """Energy, charges, level energies and symmetry maps for one basis, with the given quartic energy."""

    def __init__(self, B, quartic, Fn=None):
        self.B, self.e, self.quartic = B, B.eig, quartic
        self.T = fn.right_generators(B)
        self.spinorial = B.slot in group2i.SPINORIAL
        self.K = None
        if Fn is not None:
            _, self.K = fn.fibre_structure_matrix(Fn)
        m = B.m
        self.D = {'phase': fn.real_of_linear(1j * np.eye(m))}
        for a, T in enumerate(self.T):
            self.D[f'su2_{a}'] = fn.real_of_linear(T)
        if self.spinorial and self.K is not None:
            DJ = fn.real_of_antilinear(self.K)
            self.D['sp1_J'] = DJ
            self.D['sp1_iJ'] = fn.real_of_linear(1j * np.eye(m)) @ DJ
        self.norms = {k: float(np.linalg.norm(Dk, 2)) for k, Dk in self.D.items()}
        self.levels = sorted(set(n for n, _, _ in B.index))
        self.level_of = np.array([n for n, _, _ in B.index])

    def energy(self, c, v):
        return 0.5 * np.vdot(v, v).real + 0.5 * np.sum(self.e * np.abs(c) ** 2) + self.quartic(c)

    def charges(self, c, v):
        q, p = fn.to_real(c), fn.to_real(v)
        return {k: float(p @ D @ q) for k, D in self.D.items()}

    def level_energy(self, c, v):
        return {n: float(0.5 * np.sum(np.abs(v[self.level_of == n]) ** 2 + n * (n + 2) * np.abs(c[self.level_of == n]) ** 2))
                for n in self.levels}

    def right(self, U):
        return fn.right_rotation(self.B, U)

    def conj_map(self, c):
        """c -> K conj(c): Sp(1)'s J in the quaternionic slots, charge conjugation in the real ones."""
        return self.K @ np.conj(c)
