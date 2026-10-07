"""Stormer-Verlet for (1/c^2) M Psi'' + K Psi + g force(Psi) = 0 with the consistent mass, factorized once.
Conserved: the energy H = Pi^dagger M Pi / 2c^2 + Psi^dagger K Psi / 2 + g V4 (to O(dt^2), bounded), and the charge
N = Im(Psi^dagger M Pi)/c^2, a bilinear invariant of the symmetric phase rotation (exactly, to round-off)."""
import numpy as np
import scipy.sparse.linalg as spla
from nonlinear import arpack_v0


class Verlet:
    def __init__(self, st, c=1.0):
        self.st, self.c = st, c
        self.lu = spla.splu(st.M.tocsc())

    def accel(self, Psi):
        return -self.c ** 2 * self.lu.solve(self.st.K @ Psi + self.st.g * self.st.q.force(Psi))

    def energy(self, Psi, Pi):
        st = self.st
        return float(np.real(np.vdot(Pi, st.M @ Pi)) / (2 * self.c ** 2) + np.real(np.vdot(Psi, st.K @ Psi)) / 2
                     + st.g * st.q.energy(Psi))

    def charge(self, Psi, Pi):
        return float(np.imag(np.vdot(Psi, self.st.M @ Pi)) / self.c ** 2)

    def run(self, Psi, Pi, dt, nsteps, every, observe):
        a = self.accel(Psi)
        obs = [observe(0.0, Psi, Pi)]
        for s in range(1, nsteps + 1):
            Pi = Pi + 0.5 * dt * a
            Psi = Psi + dt * Pi
            a = self.accel(Psi)
            Pi = Pi + 0.5 * dt * a
            if s % every == 0:
                obs.append(observe(s * dt, Psi, Pi))
        return Psi, Pi, obs


def omega_max(st, c=1.0):
    lam = spla.eigsh(st.K, k=1, M=st.M, which='LA', return_eigenvectors=False, v0=arpack_v0(st.K.shape[0], complex))[0]
    return c * np.sqrt(lam)


def family_distance(Psi, Phi_ref, M, gens):
    """Relative M-distance from Psi to the exact-symmetry orbit of Phi_ref: U(1) (gens = [i]) or Sp(1) (gens = [i, J, iJ]):
    max over unit (p0, p) of Re<Psi, (p0 + sum p_a G_a) Phi_ref> is the norm of the coefficient vector."""
    MP = M @ Phi_ref
    cvec = [np.real(np.vdot(Psi, MP))] + [np.real(np.vdot(Psi, M @ g(Phi_ref))) for g in gens[1:]]
    if len(gens) == 1:
        best = abs(np.vdot(Psi, MP))
    else:
        best = np.linalg.norm([np.real(np.vdot(Psi, M @ Phi_ref))] + [np.real(np.vdot(Psi, M @ g(Phi_ref))) for g in gens])
    nP = np.real(np.vdot(Psi, M @ Psi)); nR = np.real(np.vdot(Phi_ref, MP))
    return float(np.sqrt(max(nP + nR - 2 * best, 0.0) / nR))


def orbit_distance(Psi, Ref, M, gens):
    """Relative M-distance between Psi and the exact-symmetry orbit of Ref (U(1), or Sp(1) when gens has three entries)."""
    MR = M @ Ref
    if len(gens) == 1:
        best = abs(np.vdot(Psi, MR))
    else:
        best = np.linalg.norm([np.real(np.vdot(Psi, MR))] + [np.real(np.vdot(Psi, M @ g(Ref))) for g in gens])
    nP = np.real(np.vdot(Psi, M @ Psi)); nR = np.real(np.vdot(Ref, MR))
    return float(np.sqrt(max(nP + nR - 2 * best, 0.0) / nR))


def lockstep(V, X0, Y0, dt, nsteps, every, observe, progress=None):
    """Integrate two states together (perturbed and reference) with the same steps."""
    (P1, Q1), (P2, Q2) = X0, Y0
    a1, a2 = V.accel(P1), V.accel(P2)
    obs = [observe(0.0, P1, Q1, P2, Q2)]
    for s in range(1, nsteps + 1):
        Q1 = Q1 + 0.5 * dt * a1; P1 = P1 + dt * Q1; a1 = V.accel(P1); Q1 = Q1 + 0.5 * dt * a1
        Q2 = Q2 + 0.5 * dt * a2; P2 = P2 + dt * Q2; a2 = V.accel(P2); Q2 = Q2 + 0.5 * dt * a2
        if s % every == 0:
            obs.append(observe(s * dt, P1, Q1, P2, Q2))
            if progress and len(obs) % progress == 0:
                print(f'      t = {s * dt:7.1f}: distance {obs[-1][1]:.3e}, reference off family {obs[-1][2]:.1e}', flush=True)
    return obs


def standing_velocity(Psi, sigma, dt, c=1.0):
    """Initial velocity that makes velocity-Verlet carry e^{i n theta} Psi exactly when Psi is a standing-wave profile:
    the two-step scheme gives -4 sin^2(theta/2) Psi = dt^2 a(Psi) = -c^2 dt^2 sigma Psi, so theta = 2 arcsin(c dt sqrt(sigma)/2)."""
    theta = 2 * np.arcsin(c * dt * np.sqrt(sigma) / 2)
    return (np.exp(1j * theta) - 1 + 0.5 * dt ** 2 * c ** 2 * sigma) * Psi / dt
