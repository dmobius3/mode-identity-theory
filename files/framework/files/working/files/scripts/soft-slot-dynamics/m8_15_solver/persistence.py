"""The nonlinear persistence test at level 2, under the frozen protocol.

- The direction: a fresh numpy.random.default_rng(20261006) per test draws standard_normal for the real parts, then the
  imaginary parts, of the reduced unknowns in node-orbit order, taken as a rotating-frame static phase-space vector v.
  The declared split (v7): a slow half (P_S - P_G) v, on the level-2 slow spectral subspace S minus the cluster G_tol,
  and a fast half (1 - P_S) v, both Omega-orthogonal projections; each normalized to energy norm eta/sqrt(2) relative to
  ||Phi||_M, with ||(z, e)||_E^2 = z^T M z + e^T M e / c^2. With no genuine slow mode (C1), the whole eta goes to the
  fast half. ('white', v6: (1 - P_G) v normalized to eta.) Applied as
  (Phi + delta, Pi0(Phi + delta) + p), with (delta, p) the direction's position and rotating-frame velocity parts.
- The run: Stormer-Verlet in lockstep with the exact discrete reference e^{i n theta} Phi, compared every unit of time.
- The measure: the difference aligned modulo the exact continuous symmetries (U(1), or Sp(1) in R2), taken into Phi's
  rotating frame; d its relative M-norm; d_perp the relative M-norm of its part off G_tol (Omega-orthogonal projection);
  d_rot the relative M-norm of its M-orthogonal projection onto span{X_a Phi}.
- The verdict, first event: Invalid (drift) if d_rot exceeds sqrt(eta) before d_perp exceeds 100 eta; Fails if d_perp
  exceeds 100 eta first; a tie is Invalid (drift); otherwise Persists if max d_perp <= 10 eta, Unresolved if not.
- Validity: the reference within eta_ref = eta of its family; charge drift <= 1e-10 relative; with E_eta = E(0) - E_ref,
  the energy's oscillation max |E(t) - E(0)| <= 0.25 E_eta, and its secular drift (the mean over the last tenth of the
  observations minus the mean over the first tenth) <= 1e-2 E_eta in modulus.
- The drift margin (decided before the run): r T <= ln(1/(10 eta)) for r the largest real part in the level-2 cluster."""
import numpy as np
import scipy.sparse.linalg as spla
from nonlinear import to_real, to_complex
from standing import fibre_generators
from integrate import Verlet, omega_max
from pinned import Jmap

SEED = 20261006


def omega_projector(ps, B):
    W = ps.Omega(B, B)
    return lambda v: B @ np.linalg.solve(W, ps.Omega(B, v))


def energy_norm(v, Mr, n2, c=1.0):
    z, e = v[:n2], v[n2:]
    return np.sqrt(z @ (Mr @ z) + (e @ (Mr @ e)) / c ** 2)


def direction(n, eta, Phi, ps, G, Mr, S=None, mode='split'):
    rng = np.random.default_rng(SEED)
    re = rng.standard_normal(n)
    im = rng.standard_normal(n)
    v = np.concatenate([to_real(re + 1j * im), np.zeros(2 * n)])
    nP = np.sqrt(to_real(Phi) @ (Mr @ to_real(Phi)))
    PG = omega_projector(ps, G)
    if mode == 'white':
        w = v - PG(v)
        return w * (eta * nP / energy_norm(w, Mr, 2 * n))
    PS = omega_projector(ps, S)
    pv = PS(v)
    fast = v - pv
    if S.shape[1] <= G.shape[1]:
        # no genuine slow mode (C1: the slow spectrum is the symmetry cluster alone): the whole eta goes to the fast half
        return fast * (eta * nP / energy_norm(fast, Mr, 2 * n))
    slow = pv - PG(v)
    a = (eta / np.sqrt(2)) * nP
    return slow * (a / energy_norm(slow, Mr, 2 * n)) + fast * (a / energy_norm(fast, Mr, 2 * n))


def margin_ok(lifted_vals, T, eta):
    r = float(np.max(lifted_vals.real)) if len(lifted_vals) else 0.0
    return r * T <= np.log(1 / (10 * eta)), r


class Aligner:
    """Best exact-symmetry alignment of a state with the reference's family, as the inverse map applied to the state."""
    def __init__(self, Phi, M, quaternionic):
        self.Phi, self.M, self.q = Phi, M, quaternionic
        self.MP = M @ Phi

    def apply(self, Psi, Pi, phase):
        """Return (zeta-state position, velocity) = s^-1 (Psi, Pi) brought into Phi's rotating frame by e^{-i phase},
        with s the optimal symmetry. U(1): s = e^{i alpha}; Sp(1): s = a + b J."""
        P = np.exp(-1j * phase) * Psi
        V = np.exp(-1j * phase) * Pi
        if not self.q:
            z = np.vdot(self.Phi, self.M @ P)
            u = z / abs(z)
            return np.conj(u) * P, np.conj(u) * V
        # Sp(1): maximize Re<(a + bJ) Phi, P> over unit (a, b): a = <Phi, P>/norm..., b from <J Phi, P>
        JP = Jmap(self.Phi)
        a = np.vdot(self.Phi, self.M @ P)
        b = np.vdot(JP, self.M @ P)
        nrm = np.sqrt(abs(a) ** 2 + abs(b) ** 2)
        a, b = a / nrm, b / nrm
        # inverse of (a + bJ) is (conj(a) - bJ)
        inv = lambda X: np.conj(a) * X - b * Jmap(X)
        return inv(P), inv(V)


def run_test(st, Phi, sigma, ps, G, rot, case, lifted_vals, eta=1e-3, T=1000.0, dt=None, log=print, every_t=1.0,
             progress=None, dt_factor=0.8, S=None, mode='split'):
    Mr = st.Mr
    n = len(Phi)
    ok, r = margin_ok(lifted_vals, T, eta)
    if not ok:
        return dict(verdict='Not run (floor)', r=r)
    V = Verlet(st)
    if dt is None:
        dt = dt_factor * 2 / omega_max(st)
    theta = 2 * np.arcsin(dt * np.sqrt(sigma) / 2)
    c0 = (np.exp(1j * theta) - 1 + 0.5 * dt ** 2 * sigma) / dt
    v = direction(n, eta, Phi, ps, G, Mr, S=S, mode=mode)
    delta, p = to_complex(v[:2 * n]), to_complex(v[2 * n:])
    X0 = (Phi + delta, c0 * (Phi + delta) + p)
    Y0 = (Phi.copy(), c0 * Phi)
    N0, E0 = V.charge(*X0), V.energy(*X0)
    Eref = V.energy(*Y0)
    if not E0 - Eref > 0:
        # the energy floors are multiples of E_eta: without a positive E_eta the test cannot be read (no redraw)
        return dict(verdict='Invalid (energy normalization)', r=r, dt=dt, energy_pert=float((E0 - Eref) / E0),
                    direction=mode)
    al = Aligner(Phi, st.M, case.quaternionic)
    nP = np.sqrt(np.real(np.vdot(Phi, st.M @ Phi)))
    W = ps.Omega(G, G)
    Xs = np.column_stack([to_real(xv) for xv in rot.all(Phi)])
    CX = Xs.T @ (Mr @ Xs)
    every = max(1, int(round(every_t / dt)))
    nsteps = int(round(T / dt))
    rec = []

    def observe(t, P1, Q1, P2, Q2):
        ph = (t / dt) * theta
        zp, zv = al.apply(P1, Q1, ph)
        zeta = zp - Phi
        zdot = (zv - c0 * Phi) - c0 * zeta
        vv = np.concatenate([to_real(zeta), to_real(zdot)])
        vperp = vv - G @ np.linalg.solve(W, ps.Omega(G, vv))
        zr = to_real(zeta)
        d = np.sqrt(abs(zr @ (Mr @ zr))) / nP
        zpp = vperp[:2 * n]
        dperp = np.sqrt(abs(zpp @ (Mr @ zpp))) / nP
        cx = np.linalg.solve(CX, Xs.T @ (Mr @ zr))
        xr = Xs @ cx
        drot = np.sqrt(abs(xr @ (Mr @ xr))) / nP
        rp, _ = al.apply(P2, Q2, ph)
        rr = to_real(rp - Phi)
        dref = np.sqrt(abs(rr @ (Mr @ rr))) / nP
        return (t, d, dperp, drot, dref, V.charge(P1, Q1), V.energy(P1, Q1))

    (P1, Q1), (P2, Q2) = X0, Y0
    a1, a2 = V.accel(P1), V.accel(P2)
    rec.append(observe(0.0, P1, Q1, P2, Q2))
    for s in range(1, nsteps + 1):
        Q1 = Q1 + 0.5 * dt * a1; P1 = P1 + dt * Q1; a1 = V.accel(P1); Q1 = Q1 + 0.5 * dt * a1
        Q2 = Q2 + 0.5 * dt * a2; P2 = P2 + dt * Q2; a2 = V.accel(P2); Q2 = Q2 + 0.5 * dt * a2
        if s % every == 0:
            rec.append(observe(s * dt, P1, Q1, P2, Q2))
            if progress and len(rec) % progress == 0:
                t, d, dp, dr, dref = rec[-1][:5]
                log(f'      t = {t:7.1f}: d {d:.3e}, d_perp {dp:.3e}, d_rot {dr:.3e}, reference {dref:.1e}')
    rec = np.array(rec)
    out = evaluate(rec, eta, float(Eref))
    out.update(r=r, dt=dt, rec=rec, direction=mode, initial_energy_norm=float(energy_norm(v, Mr, 2 * n) / nP))
    return out


def evaluate(rec, eta, Eref):
    """The verdict and the floors from a run's record (columns t, d, d_perp, d_rot, d_ref, N, E), read up to the run's
    first event, or T when there is none: what the run does after its verdict is decided cannot change it."""
    t, d, dp, dr, dref, N, E = rec.T
    i_rot = int(np.argmax(dr > np.sqrt(eta))) if (dr > np.sqrt(eta)).any() else None
    i_fail = int(np.argmax(dp > 100 * eta)) if (dp > 100 * eta).any() else None
    if i_rot is not None and (i_fail is None or i_rot <= i_fail):
        verdict, i_end = 'Invalid (drift)', i_rot
    elif i_fail is not None:
        verdict, i_end = 'Fails', i_fail
    else:
        verdict, i_end = ('Persists' if dp.max() <= 10 * eta else 'Unresolved'), len(t) - 1
    sl = slice(0, i_end + 1)
    N0, E0 = N[0], E[0]
    Eeta = float(E0 - Eref)
    dN = float(abs(N[sl] - N0).max() / abs(N0))
    dE = float(abs(E[sl] - E0).max() / abs(E0))
    dEp = float(abs(E[sl] - E0).max() / abs(Eeta))
    m = i_end + 1
    k10 = max(1, m // 10)
    drift = float(abs(E[m - k10:m].mean() - E[:k10].mean()) / abs(Eeta))
    ok = (dref[sl].max() <= eta) and dN <= 1e-10 and Eeta > 0 and dEp <= 0.25 and drift <= 1e-2
    ok_v6 = (dref[sl].max() <= eta) and dN <= 1e-10 and dE <= 1e-6
    return dict(verdict=verdict if ok else f'Invalid ({verdict} on an invalid run)', valid=bool(ok),
                valid_under_v6_energy_rule=bool(ok_v6), read_until=float(t[i_end]),
                max_d=float(d.max()), max_dperp=float(dp.max()), max_drot=float(dr.max()), max_dref=float(dref[sl].max()),
                charge_drift=dN, energy_drift=dE, energy_pert=float(Eeta / E0), energy_dev_vs_pert=dEp,
                energy_secular_drift=drift, t_fail=(float(t[i_fail]) if i_fail is not None else None),
                drot_at_fail=(float(dr[i_fail]) if i_fail is not None else None))
