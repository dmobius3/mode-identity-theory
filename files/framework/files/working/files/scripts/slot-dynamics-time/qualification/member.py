"""The member path on M8.16.1's pinned instrument (the terms, § THE READ): a slot at a cutoff, a member's linear record
as M8.16.1's driver computes it, the perturbation directions, the +/- delta pairs under the time arm, and their read
in the member's rotating frame. Development code: nothing here is registered until the freeze.

Coordinates. The instrument's linearization (linear.first_order) acts on x = (zeta, zeta') in the real form of
zeta'' + 2 i omega zeta' + L zeta = 0, with B = diag(L, I) its energy form and W its symplectic form. A run's lab-frame
state (c, v) is taken there by the design's section 2: zeta = e^{-i w t} psi - phi, zeta' = e^{-i w t}(psi' - i w psi),
with w the carrier's measured rotation."""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARM = os.path.dirname(HERE)
for p in (ARM, HERE):
    if p not in sys.path:
        sys.path.insert(0, p)
import fftcubic  # noqa: E402  (checks the instrument's pin and puts it on the path)
import timearm as ta  # noqa: E402
import readcore as rc  # noqa: E402
from instrument import basis, functional as fn, linear as ln, branches as br, group2i  # noqa: E402

MARGIN = 0.8          # the design's section 5 margin, h = 0.8 * 2 / w-bar
DELTA = 1e-5          # the perturbation's relative size


class Slot:
    def __init__(self, slot, N):
        self.name, self.N = slot, N
        self.B = basis.Basis(slot, N)
        self.Fn = fn.Functional(self.B)
        self.X = fftcubic.FFTCubic(self.B)
        self.e = self.B.eig
        self.n = np.array([n for n, _, _ in self.B.index])
        self.n0 = int(self.n.min())
        self.low = self.n == self.n0
        self.lam0 = float(self.n0 * (self.n0 + 2))
        self.spinorial = slot in group2i.SPINORIAL
        self.K = fn.fibre_structure_matrix(self.Fn)[1] if self.spinorial else None
        self.D = ta.Diagnostics(self.B, self.X.quartic, self.Fn if self.spinorial else None)


def step5(S, H0):
    """The design's section 5: C-bar = 2 H(0) / ((1 - 0.8^2) lambda_0), w-bar^2 = N(N+2) + 3 (m/r) C-bar, h0 = 1.6 / w-bar."""
    cbar = 2 * H0 / ((1 - MARGIN ** 2) * S.lam0)
    wbar = float(np.sqrt(S.N * (S.N + 2) + 3 * (S.B.m / S.B.r) * cbar))
    return MARGIN * 2 / wbar, float(cbar), wbar


def linear_record(S, c, lam, expected=None, tangents_K=None):
    """The instrument's linear record at (c, lam), as M8.16.1's driver's read_point builds it."""
    L = S.Fn.hess_dense(c, lam)
    A, Bm, W = ln.first_order(L, np.sqrt(lam))
    margin = ln.margin(np.linalg.norm(A, 2), float(np.vdot(c, c).real))
    T = br.tangent_vectors(S.Fn, c, tangents_K)
    sym = [np.concatenate([t, np.zeros(2 * S.B.m)]) for t in T]
    r = ln.record(A, Bm, W, L, margin, symmetry=sym, expected=expected)
    return dict(r=r, L=L, A=A, B=Bm, W=W, margin=margin)


def omega_complement(rec):
    """The projection onto the W-complement of the generalized kernel V0, along V0: P = I - V0 (V0^T W V0)^-1 V0^T W."""
    V0, W = rec['r']['V0'], rec['W']
    G = V0.T @ W @ V0
    return np.eye(W.shape[0]) - V0 @ np.linalg.solve(G, V0.T @ W)


def charge_free(S, c0, v0, dq, dp):
    """Remove from a lab-frame direction (dq, dp) the first-order change of the charges the rotating frame conserves:
    the phase and the three right-SU(2) charges, whose generators are complex-linear and commute with the phase. The
    Sp(1) charges of R1, R2, R6 and R8 are left: their generators are antilinear, so in the rotating frame they turn at
    2 omega, and their first-order directions are modes the read reads, Theorem 3.7's +/- 2 i omega among them."""
    q0, p0 = fn.to_real(c0), fn.to_real(v0)
    gens = [D for k, D in S.D.D.items() if not k.startswith('sp1')]
    rows = [np.concatenate([D.T @ p0, D @ q0]) for D in gens]                # d J_D = (D^T p0) . dq + (D q0) . dp
    Rm = np.array(rows)
    x = np.concatenate([dq, dp])
    coef = np.linalg.lstsq(Rm @ Rm.T, Rm @ x, rcond=None)[0]
    x = x - Rm.T @ coef
    return x[:len(dq)], x[len(dq):]


def directions(S, rec, c0, lam, target_idx, k, rng, lowest_only=False):
    """k unit directions in the rotating frame, half their norm in the target eigenspaces (the record's eigenvectors at
    target_idx) and half outside them and V0, the first-order charges removed in the lab frame; returned as lab-frame
    (dc, dv) at t = 0, with dc = zeta and dv = zeta' + i w zeta."""
    m = S.B.m
    V = rec['r']['V']
    Vt = np.hstack([V[:, target_idx].real, V[:, target_idx].imag])
    Qt = np.linalg.qr(Vt)[0]
    V0 = rec['r']['V0']
    Qs = np.linalg.qr(np.hstack([Vt, V0]))[0]
    w = np.sqrt(lam)
    lowmask = np.concatenate([S.low, S.low, S.low, S.low])
    out = []
    for _ in range(k):
        a = Qt @ rng.normal(size=Qt.shape[1])
        b = rng.normal(size=4 * m)
        if lowest_only:
            b = np.where(lowmask, b, 0.0)
        b = b - Qs @ (Qs.T @ b)
        if lowest_only:
            b = np.where(lowmask, b, 0.0)
        x = a / np.linalg.norm(a) + (b / np.linalg.norm(b) if np.linalg.norm(b) > 0 else 0.0)
        zeta, zdot = fn.to_complex(x[:2 * m]), fn.to_complex(x[2 * m:])
        dc, dv = zeta, zdot + 1j * w * zeta
        dq, dp = charge_free(S, c0, 1j * w * c0, fn.to_real(dc), fn.to_real(dv))
        dc, dv = fn.to_complex(dq), fn.to_complex(dp)
        nrm = np.sqrt(np.vdot(dc, dc).real + np.vdot(dv, dv).real)
        out.append((dc / nrm, dv / nrm))
    return out


def excitation(rec, dirs, lam, targets):
    """What a set of directions excites, as the record reports it (the terms, THE READ, step 3): each direction's share of
    its rotating-frame squared norm in the target eigenspaces, after the charge removal and the normalization, an even
    split being 0.5; and for each target
    group, the singular values of the directions' spectral coefficients on the group's eigenvectors, from the left
    eigenvectors of the linear map at the group's eigenvalue. A group of size s is spanned when its s values are nonzero.
    Reported, not scored: the mode fraction and the admission judge the read."""
    A, V, ev = rec['A'], rec['r']['V'], rec['r']['lam']
    w = np.sqrt(lam)
    X = np.array([np.concatenate([fn.to_real(dc), fn.to_real(dv - 1j * w * dc)]) for dc, dv in dirs]).T
    idx = [j for t in targets for j in t['idx']]
    Qt = np.linalg.qr(np.hstack([V[:, idx].real, V[:, idx].imag]))[0]
    share = [float(np.linalg.norm(Qt.T @ x) ** 2 / np.linalg.norm(x) ** 2) for x in X.T]
    values = []
    for t in targets:
        Vg = V[:, t['idx']]
        U = np.linalg.svd(A - complex(np.mean(ev[t['idx']])) * np.eye(A.shape[0]))[0]
        L = U[:, -len(t['idx']):]                                                  # the left null space at the eigenvalue
        alpha = np.linalg.solve(L.conj().T @ Vg, L.conj().T @ X)                   # one column of coefficients per direction
        values.append([float(s) for s in np.linalg.svd(alpha, compute_uv=False)])
    return share, values


def pair_runs(S, c0, lam, dirs, h, nsteps, every, cbar, kick=None):
    """For each direction, the +delta and -delta runs from the continuum standing wave (c0, i w c0) under the splitting
    with the FFT cubic, observed every `every` steps: arrays of lab-frame c and v, one column per observation."""
    w = np.sqrt(lam)
    scale = DELTA * np.sqrt(np.vdot(c0, c0).real + w ** 2 * np.vdot(c0, c0).real)
    cubic = S.X.cubic if kick is None else kick
    runs = []
    for dc, dv in dirs:
        pair = []
        for sgn in (1.0, -1.0):
            cs, vs = [c0 + sgn * scale * dc], [1j * w * c0 + sgn * scale * dv]

            def obs(s, c, v):
                cs.append(c.copy())
                vs.append(v.copy())
            ta.strang(cs[0].copy(), vs[0].copy(), h, nsteps, S.e, cubic, cbar=cbar, observe=obs, every=every)
            pair.append((np.array(cs).T, np.array(vs).T))
        runs.append(pair)
    return runs, scale


def carrier_rotation(c0, mean_c, t):
    """The slope of a least-squares line through the unwrapped phase of <phi, c-bar(t)>."""
    ph = np.unwrap(np.angle(np.conj(c0) @ mean_c))
    return float(np.polyfit(t, ph, 1)[0])


def to_frame(runs, scale, c0, lam, dt, P, mode='measured', broken=False):
    """The half differences of each pair in the rotating frame at the carrier's measured rotation, projected by P."""
    trajs, rot = [], []
    w_cont = np.sqrt(lam)
    for (cp, vp), (cm, vm) in runs:
        t = dt * np.arange(cp.shape[1])
        mean = 0.5 * (cp + cm)
        w = carrier_rotation(c0, mean, t) if mode == 'measured' else w_cont
        rot.append(w)
        if broken:       # the -delta run left out: the +delta run against the stationary point at the continuum's rotation
            dcz = (cp - np.exp(1j * w_cont * t) * c0[:, None]) / scale
            dvz = (vp - 1j * w_cont * np.exp(1j * w_cont * t) * c0[:, None]) / scale
        else:
            dcz, dvz = 0.5 * (cp - cm) / scale, 0.5 * (vp - vm) / scale
        ph = np.exp(-1j * w * t)
        zeta = ph * dcz
        zdot = ph * (dvz - 1j * w * dcz)
        x = np.vstack([zeta.real, zeta.imag, zdot.real, zdot.imag])
        trajs.append(P @ x)
    return trajs, rot


def read(trajs, dt, targets, radius):
    """The fit, the admission against `targets` inside `radius`, and the floor."""
    fit = rc.Fit(trajs, dt)
    centres, members = rc.admit(fit, targets, radius=radius)
    fl = rc.floor(trajs, dt, targets, centres, radius=radius)
    return fit, centres, members, fl
