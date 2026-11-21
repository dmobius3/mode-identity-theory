"""Development (DEVLOG entry 4): how the matched rigid wave's round-off error grows with the step count, for both
steppers, in R1 and R3 at N = 12, dev seed 900102. Not a control."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import timearm as ta  # noqa: E402
import fftcubic  # noqa: E402
import numpy as np  # noqa: E402
from instrument import basis  # noqa: E402

rng = np.random.default_rng(900102)
for slot in ('R1', 'R3'):
    B = basis.Basis(slot, 12); X = fftcubic.FFTCubic(B); e = B.eig
    n0 = B.levels[0]; low = np.array([n == n0 for n, _, _ in B.index])
    phi = np.zeros(B.m, complex); phi[low] = rng.standard_normal(low.sum()) + 1j * rng.standard_normal(low.sum())
    phi /= np.linalg.norm(phi)                                  # kappa = 1
    h = 0.8 * 2 / np.sqrt(12 * 14)
    for kind in ('verlet', 'strang'):
        z0, dz0, th = ta.matched(kind, h, n0 * (n0 + 2), 1.0)
        step = ta.verlet if kind == 'verlet' else ta.strang
        c, v = z0 * phi, dz0 * phi
        errs, done = [], 0
        for K in (400, 800, 1600, 3200):
            out = step(c, v, h, K - done, e, X.cubic)
            c, v, done = out[0], out[1], K
            ref = np.exp(1j * K * th) * z0 * phi
            ph = np.angle(np.vdot(ref, c))
            errs.append((K, np.linalg.norm(c - ref) / abs(z0), ph, np.vdot(c, c).real / abs(z0) ** 2 - 1))
        print(slot, kind, '; '.join(f'K={K}: error {er:.1e}, phase {ph:+.1e}, norm^2 - kappa {dn:+.1e}' for K, er, ph, dn in errs))
