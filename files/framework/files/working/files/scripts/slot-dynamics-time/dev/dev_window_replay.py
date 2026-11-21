"""After the registered run (DEVLOG entry 14): control 9's window in R2 at N = 12, replayed on the registered seed.
The multi-level state of controls 4, 7 and 8 is rebuilt from REG, and its energy ladder under Verlet must reproduce
record/09_c9.json's to round-off before anything is read. Then the run at h0/2 is stepped again with every step
observed, where the record observes every second one, and at each step the exact top frequency of the linearization,
sqrt of the largest eigenvalue of K + Hess V4 from the instrument's hess_apply at lambda = 0 on the real form, is read
beside the bound of section 5's inequalities at that step's ||c||^2. Not a control, and nothing here enters record/."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import controls as C  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Reg:
    """The registered inputs, as Ctx draws them, with no output folder: this writes nothing."""
    P = C.REG
    cache = {}

    def rng(self, control, slot, N, draw):
        return np.random.default_rng([self.P['seed'], C.CID[control], C.SID.get(slot, 0), int(N), int(draw)])

    def slot(self, slot, N, dense=False):
        if (slot, N) not in self.cache:
            self.cache[(slot, N)] = C.Slot(slot, N)
        return self.cache[(slot, N)]


def hessian(S, c):
    """K + Hess V4 at c on the real form (Re c, Im c), from hess_apply at lambda = 0, column by column."""
    m = S.B.m
    cols = []
    for k in range(2 * m):
        d = np.zeros(m, complex)
        d[k % m] = 1.0 if k < m else 1j
        w = S.F.hess_apply(c, 0.0, d)
        cols.append(np.concatenate([w.real, w.imag]))
    H = np.array(cols).T
    return 0.5 * (H + H.T), float(np.abs(H - H.T).max())


ctx = Reg()
A = C.setup_A(ctx, 'R2', 12)
S, P = A['S'], ctx.P
rec = json.load(open(os.path.join(HERE, 'record', '09_c9.json'), encoding='utf-8'))
want = next(r for r in rec['result']['rows'] if r.get('key') == 'R2/12/verlet')['errors']
got = C.energy_ladder(A, 'verlet', True, P)
dev = max(abs(g - w) / w for g, w in zip(got, want))
print('levels', S.B.levels, 'm', S.B.m, 'r', S.B.r, 'h0', A['h'], 'K', A['K'], 'every', A['every'], 'cbar', A['cbar'])
print('energy ladder, replayed against the record:', ['%.6e' % g for g in got], 'largest relative difference %.1e' % dev)
assert dev < 1e-9, 'the replay does not reproduce the record'

h, K, every = A['h'] / 2, A['K'] * 2, A['every'] * 2
mr = S.B.m / S.B.r
lam = float(S.e.max())
rows, asym = [], 0.0
E0 = S.D.energy(A['c0'], A['v0'])


def obs(s, c, v):
    global asym
    Hm, a = hessian(S, c)
    asym = max(asym, a)
    top = float(np.linalg.eigvalsh(Hm)[-1])
    n2 = float(np.vdot(c, c).real)
    rows.append((s, h * np.sqrt(top), h * np.sqrt(lam + 3 * mr * n2), n2, abs(S.D.energy(c, v) - E0) / E0))


obs(0, A['c0'], A['v0'])
C.evolve('verlet', A['c0'], A['v0'], h, K, S, S.X.cubic, A['cbar'], 1, obs)
R = np.array(rows)
odd = R[R[:, 0] % every != 0]
even = R[R[:, 0] % every == 0]
print(f'the run at h0/2: h {h:.9f}, {K} steps, the record observing every {every}; Hessian asymmetry {asym:.1e}')
print(f'exact h w_max: largest {R[:, 1].max():.6f} over every step, {even[:, 1].max():.6f} over the observed steps, '
      f'{odd[:, 1].max():.6f} over the others')
print(f'bound from ||c||^2 at each step: largest {R[:, 2].max():.6f}; largest ||c||^2 {R[:, 3].max():.6f}')
print(f'relative energy error: largest {R[:, 4].max():.6e} over every step, {even[:, 4].max():.6e} over the '
      f'observed steps (the record: {want[1]:.6e})')
print(f'the window at the ratio\'s smaller step h0/4 with this run\'s largest frequency: {R[:, 1].max() / 2:.6f}')
