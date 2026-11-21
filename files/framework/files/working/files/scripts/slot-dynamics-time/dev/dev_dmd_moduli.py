"""Development (DEVLOG entry 11): which eigenvalues of control 6's fitted one-step map leave the unit circle, at the
development seeds, N = 12, R1 and R3, the ladder's first two steps. Not a control."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import controls as C  # noqa: E402
import numpy as np  # noqa: E402


class Dev:
    P = C.DEV
    cache = {}

    def rng(self, control, slot, N, draw):
        return np.random.default_rng([self.P['seed'], C.CID[control], C.SID.get(slot, 0), int(N), int(draw)])

    def slot(self, slot, N, dense=False):
        if (slot, N) not in self.cache:
            self.cache[(slot, N)] = C.Slot(slot, N)
        return self.cache[(slot, N)]


ctx = Dev()
for slot in ('R1', 'R3'):
    R = C.setup_B(ctx, slot)
    for kind in ('verlet', 'strang'):
        for j in (0, 1):
            S, phi, h = R['S'], R['phi'], R['hs'][j]
            K = R['K6'] * 2 ** j
            z0, dz0, th = C.ta.matched(kind, h, S.lam0, R['kappa'])
            c0, v0 = z0 * phi, dz0 * phi
            dc, dv = R['dpert']
            dN = float(np.imag(np.vdot(dc, v0) + np.vdot(c0, dv)))
            dv = dv - 1j * c0 * dN / np.vdot(c0, c0).real
            sc = C.DEV['eps6'] * C.qp(c0, v0) / C.qp(dc, dv)
            dc, dv = sc * dc, sc * dv
            low, snaps = S.low, []

            def obs(s, c, v):
                ph = np.exp(-1j * s * th)
                zc, zv = ph * c[low] - c0[low], ph * v[low] - v0[low]
                snaps.append(np.concatenate([zc.real, zc.imag, zv.real, zv.imag]))

            obs(0, c0 + dc, v0 + dv)
            C.evolve(kind, c0 + dc, v0 + dv, h, K, S, S.X.cubic, R['cbar'], 1, obs)
            X = np.array(snaps).T
            mu, nu, r = C.dmd(X, h, C.DEV['rank6'])
            U, s, Vh = np.linalg.svd(X[:, :-1], full_matrices=False)
            order = np.argsort(-np.abs(np.abs(nu) - 1))
            print(f'{slot} {kind} h0/{2 ** j}: rank {r}; singular values relative {", ".join(f"{x / s[0]:.1e}" for x in s)}')
            print('   eigenvalues (|nu| - 1, frequency):', '; '.join(f'{abs(nu[i]) - 1:+.2e}, {mu[i]:+.4f}' for i in order))
