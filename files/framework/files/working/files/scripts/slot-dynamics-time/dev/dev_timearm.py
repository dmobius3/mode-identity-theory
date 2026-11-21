"""Development (DEVLOG entries 3 and 4): the time arm's basic behaviour at N <= 12, on development seeds 900101 up. Not a
control: free modes with the cubic off, a rigid lowest-level orbit's force, the matched standing waves, reversibility,
charges and equivariance on short runs."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import timearm as ta  # noqa: E402
import fftcubic  # noqa: E402
import numpy as np  # noqa: E402
from instrument import basis, functional, su2  # noqa: E402

rng = np.random.default_rng(900101)
zero = lambda c: np.zeros_like(c)
for slot in ('R1', 'R3', 'R4', 'R2'):
    N = 12
    B = basis.Basis(slot, N); Fn = functional.Functional(B); X = fftcubic.FFTCubic(B)
    D = ta.Diagnostics(B, X.quartic, Fn)
    e = B.eig; h = 0.8 * 2 / np.sqrt(N * (N + 2))
    # free mode on one coefficient, cubic off, matched discrete rotation
    j = int(np.argmax(e)); c0 = np.zeros(B.m, complex); c0[j] = 1.0
    for kind in ('verlet', 'strang'):
        z0, dz0, th = ta.matched(kind, h, e[j], 0.0)
        step = ta.verlet if kind == 'verlet' else ta.strang
        out = step(z0 * c0, dz0 * c0, h, 400, e, zero)
        err = np.linalg.norm(out[0] - np.exp(1j * 400 * th) * z0 * c0)
        exp_th = 2 * np.arcsin(h * np.sqrt(e[j]) / 2) if kind == 'verlet' else h * np.sqrt(e[j])
        print(f'{slot} free mode {kind}: theta {th:.12f} vs expected {exp_th:.12f}; state error after 400 steps {err:.1e}')
    # a rigid slot's lowest-level orbit: cubic(c) = ||c||^2 c ?
    n0 = B.levels[0]; low = np.array([n == n0 for n, _, _ in B.index])
    cl = np.zeros(B.m, complex); cl[low] = (rng.standard_normal(low.sum()) + 1j * rng.standard_normal(low.sum())) * 0.3
    dev = np.linalg.norm(X.cubic(cl) - np.vdot(cl, cl).real * cl) / np.linalg.norm(cl) ** 3
    print(f'{slot} lowest level {n0}: |cubic(c) - ||c||^2 c| / ||c||^3 = {dev:.1e}' + ('  (rigid)' if dev < 1e-12 else '  (soft)'))
    if dev < 1e-12:
        kap = np.vdot(cl, cl).real
        for kind in ('verlet', 'strang'):
            z0, dz0, th = ta.matched(kind, h, n0 * (n0 + 2), kap)
            step = ta.verlet if kind == 'verlet' else ta.strang
            out = step(z0 * cl, dz0 * cl, h, 400, e, X.cubic)
            err = np.linalg.norm(out[0] - np.exp(1j * 400 * th) * z0 * cl) / np.linalg.norm(z0 * cl)
            ct = np.cos(np.sqrt(n0 * (n0 + 2)) * h) - kap * h / (2 * np.sqrt(n0 * (n0 + 2))) * np.sin(np.sqrt(n0 * (n0 + 2)) * h)
            exp_th = 2 * np.arcsin(h * np.sqrt(n0 * (n0 + 2) + kap) / 2) if kind == 'verlet' else np.arccos(ct)
            print(f'   standing wave {kind}: theta {th:.12f} vs the formula {exp_th:.12f}; |z0|^2 = {abs(z0) ** 2:.12f}; state error after 400 steps {err:.1e}')
    # random multi-level state with momenta: charges, reversibility, equivariance, short nonlinear run
    c = (rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m)) * 0.1
    v = (rng.standard_normal(B.m) + 1j * rng.standard_normal(B.m)) * 0.1 * np.sqrt(e)
    for kind in ('verlet', 'strang'):
        step = ta.verlet if kind == 'verlet' else ta.strang
        Q0 = D.charges(c, v)
        out = step(c, v, h, 200, e, X.cubic)
        c1, v1 = out[0], out[1]
        Q1 = D.charges(c1, v1)
        scale = np.linalg.norm(c) * np.linalg.norm(v)
        dq = max(abs(Q1[k] - Q0[k]) / (D.norms[k] * scale) for k in Q0)
        back = step(c1, v1, -h, 200, e, X.cubic)
        rev = np.linalg.norm(np.concatenate([back[0] - c, back[1] - v])) / np.linalg.norm(np.concatenate([c, v]))
        q = rng.standard_normal(4); q /= np.linalg.norm(q)
        R = D.right(su2.quat_to_su2(q))
        outR = step(R @ c, R @ v, h, 200, e, X.cubic)
        eqv = np.linalg.norm(np.concatenate([outR[0] - R @ c1, outR[1] - R @ v1])) / np.linalg.norm(np.concatenate([c1, v1]))
        print(f'{slot} {kind}: charges {sorted(Q0)} max rel drift {dq:.1e}; reversibility {rev:.1e}; right-SU(2) equivariance {eqv:.1e}')
