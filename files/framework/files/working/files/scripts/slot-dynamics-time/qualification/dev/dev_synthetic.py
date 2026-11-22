"""Development: the read core on synthetic linear systems with known eigenvalues, Krein signs and multiplicities (the terms'
test 2). No census point and no member: each system is a quadratic Hamiltonian built from blocks, mixed by a random
symplectic map, with fast modes outside the slow circle and weakly excited zero-frequency directions planted as the
prototype's DEVLOG entry 11 found them. The rotating-frame perturbation is seen through a carrier turning at a frequency
the read must measure, with a second-order term the +/- delta pair must cancel. Development seeds only.

Usage: python3 -I -B dev_synthetic.py"""
import os
import sys

import numpy as np
from scipy.linalg import expm

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import readcore as rc  # noqa: E402

SEED = 7300101          # a development seed
DT = 0.09               # about h0 at N = 16
DELTA = 1e-5
RNG = np.random.default_rng(SEED)


def block_system(blocks, n_fast, n_weak):
    """A quadratic Hamiltonian on R^{2n}, x = (q, p), x' = J H x, from blocks; returns (A, H, slow, groups).
    Blocks: ('imag', tau, sign, mult), ('real', gamma, mult), ('quartet', a, b). Fast modes: elliptic, Krein +, at
    frequencies from 2 to 20. Weak directions: neutral degrees of freedom, H = 0 on them."""
    qs, ps, Hd, groups = [], [], [], []
    rows = []      # (H block on its dofs, number of dofs, slow?)
    for b in blocks:
        if b[0] == 'imag':
            _, tau, sign, mult = b
            for _ in range(mult):
                rows.append((sign * tau * np.eye(2), 1, True))
            groups.append({'c': complex(0, tau), 'cls': 'imag', 'size': mult, 'sign': sign})
        elif b[0] == 'real':
            _, g, mult = b
            for _ in range(mult):
                rows.append((g * np.array([[0.0, 1.0], [1.0, 0.0]]), 1, True))
            groups.append({'c': complex(g, 0), 'cls': 'real', 'size': mult, 'sign': None})
        else:
            _, a, bq = b
            H4 = np.zeros((4, 4))
            # H = a (q1 p1 + q2 p2) + b (q1 p2 - q2 p1), in (q1, q2, p1, p2)
            H4[0, 2] = H4[2, 0] = a
            H4[1, 3] = H4[3, 1] = a
            H4[0, 3] = H4[3, 0] = bq
            H4[1, 2] = H4[2, 1] = -bq
            rows.append((H4, 2, True))
            groups.append({'c': complex(a, bq), 'cls': 'complex', 'size': 1, 'sign': None})
    for w in np.linspace(2.0, 20.0, n_fast):
        rows.append((w * np.eye(2), 1, False))
    for _ in range(n_weak):
        rows.append((np.zeros((2, 2)), 1, None))
    n = sum(d for _, d, _ in rows)
    H = np.zeros((2 * n, 2 * n))
    kind = np.empty(n, dtype=object)
    i = 0
    for Hb, d, slow in rows:
        qi, pi = np.arange(i, i + d), np.arange(n + i, n + i + d)
        idx = np.concatenate([qi, pi])
        H[np.ix_(idx, idx)] = Hb
        kind[i:i + d] = 'slow' if slow else ('fast' if slow is False else 'weak')
        i += d
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    # a random symplectic map, S = expm(J K) with K symmetric, mixes the blocks
    K = RNG.normal(size=(2 * n, 2 * n))
    K = 0.15 * (K + K.T) / np.sqrt(2 * n)
    S = expm(J @ K)
    Si = np.linalg.inv(S)
    A = S @ (J @ H) @ Si
    Hm = Si.T @ H @ Si
    return A, Hm, S, kind, n, groups


def directions(S, kind, n, k):
    """k unit directions with half their norm in the slow modes and half in the fast, and the weak directions excited
    at 2.3e-5, as DEVLOG entry 11 found them."""
    out = []
    for _ in range(k):
        u = RNG.normal(size=2 * n)
        dof = np.concatenate([kind, kind])
        slow, fast, weak = (dof == 'slow'), (dof == 'fast'), (dof == 'weak')
        x = np.zeros(2 * n)
        x[slow] = u[slow] / np.linalg.norm(u[slow])
        x[fast] = u[fast] / np.linalg.norm(u[fast])
        x[weak] = 2.3e-5 * u[weak] / max(np.linalg.norm(u[weak]), 1e-300)
        y = S @ x
        out.append(y / np.linalg.norm(y))
    return out


def lab(A, x0s, T, omega_c, phi, eta_scale=1.0):
    """The +/- delta pairs seen in the lab frame: a carrier phi turning at omega_c, the rotating-frame perturbation
    +/- delta x(t), and a second-order term delta^2 eta(t), even in delta. The real state (q, p) is read as complex
    pairs z = q + i p, which the carrier's phase turns."""
    steps = int(np.ceil(T / DT))
    Phi = expm(A * DT)
    pairs = []
    for x0 in x0s:
        xs = np.empty((len(x0), steps + 1))
        xs[:, 0] = x0
        for s in range(steps):
            xs[:, s + 1] = Phi @ xs[:, s]
        n = len(x0) // 2
        z = xs[:n] + 1j * xs[n:]                   # rotating-frame perturbation, complex form
        eta = eta_scale * z ** 2                   # a second-order term
        t = DT * np.arange(steps + 1)
        rot = np.exp(1j * omega_c * t)
        plus = rot * (phi[:, None] + DELTA * z + DELTA ** 2 * eta)
        minus = rot * (phi[:, None] - DELTA * z + DELTA ** 2 * eta)
        pairs.append((plus, minus))
    return pairs, DT * np.arange(steps + 1)


def measured_rotation(mean, phi, t):
    """The slope of a least-squares line through the unwrapped phase of <phi, mean(t)>."""
    ph = np.unwrap(np.angle(np.conj(phi) @ mean))
    return float(np.polyfit(t, ph, 1)[0])


def read(pairs, t, phi, omega_nominal, mode='measured', broken=False):
    trajs = []
    for plus, minus in pairs:
        mean = 0.5 * (plus + minus)
        om = measured_rotation(mean, phi, t) if mode == 'measured' else omega_nominal
        if broken:
            half = (plus - np.exp(1j * omega_nominal * t) * phi[:, None]) / DELTA   # the -delta run left out
        else:
            half = 0.5 * (plus - minus) / DELTA
        z = np.exp(-1j * om * t) * half
        trajs.append(np.vstack([z.real, z.imag]))
    return trajs


def checks():
    out = []

    def c(name, ok, det):
        out.append((name, bool(ok), det))
        print(f'{"PASS" if ok else "FAIL"}  {name}: {det}')

    systems = {
        'elliptic five, Krein +': ([('imag', t, +1, 1) for t in (2.0e-3, 2.6e-3, 3.4e-3, 4.1e-3, 5.0e-3)], 1),
        'hexagon-like, Krein -, simple and double': ([('imag', 1.6e-2, -1, 1), ('imag', 1.27e-2, -1, 2)], 2),
        'C3-like, a real triple': ([('real', 9.7e-3, 3)], 3),
        'P5-like, a quartet and two pairs': ([('quartet', 7.3e-4, 1.06e-3), ('imag', 9.5e-4, -1, 1), ('imag', 1.67e-2, +1, 1)], 1),
    }
    omega_c, omega_nom = 6.93, 6.93 - 5.5e-5      # the carrier turns 5.5e-5 faster than the continuum, as at N = 16
    for name, (blocks, k) in systems.items():
        A, Hm, S, kind, n, groups = block_system(blocks, n_fast=6, n_weak=2)
        slowest = min(abs(g['c']) for g in groups)
        reals = [g['c'].real for g in groups if g['cls'] in ('real', 'complex')]
        imags = [g['c'].imag for g in groups if g['cls'] in ('imag',)]
        T = max(([3 / min(reals)] if reals else []) + ([2 * np.pi / min(imags)] if imags else []))
        phi = RNG.normal(size=n) + 1j * RNG.normal(size=n)
        phi /= np.linalg.norm(phi)
        pairs, t = lab(A, directions(S, kind, n, k), T, omega_c, phi)
        trajs = read(pairs, t, phi, omega_nom)
        fit = rc.Fit(trajs, DT)
        try:
            centres, members = rc.admit(fit, groups)
            errs = [abs(cz - g['c']) / abs(g['c']) for cz, g in zip(centres, groups)]
            c(f'{name}: recovered', max(errs) < 1e-6, f'rank {fit.rank}; worst relative error {max(errs):.2e} over {len(groups)} groups; T {T:.0f}')
        except rc.Admission as e:
            c(f'{name}: recovered', False, str(e))
            continue
        fl = rc.floor(trajs, DT, groups, centres)
        c(f'{name}: floor below a tenth of b_g', all(f < 0.1 * rc.tolerance(g['c']) for f, g in zip(fl, groups)),
          f'floor / b_g at most {max(f / rc.tolerance(g["c"]) for f, g in zip(fl, groups)):.2e}')
        # the Krein form in the read's coordinates: the Hamiltonian's form, x = (q, p) read as (Re z, Im z)
        signs = []
        for i, g in enumerate(groups):
            if g['cls'] == 'imag':
                s, definite = rc.krein(Hm, fit, members[i])
                signs.append(definite and s == g['sign'])
        c(f'{name}: Krein signs', all(signs), f'{sum(signs)} of {len(signs)} imaginary groups definite with their sign')
        # the arms, each refused
        try:
            rc.admit(rc.Fit(trajs, DT), groups, fraction=0.0)
            weak_refused = False
        except rc.Admission:
            weak_refused = True
        c(f'{name}: arm, the mode fraction off', weak_refused, 'the weak directions fail the admission without the fraction')
        trajs_d = read(pairs, t, phi, omega_nom, mode='nominal')
        try:
            cd, _ = rc.admit(rc.Fit(trajs_d, DT), groups)
            off = max(abs(a - g['c']) / rc.tolerance(g['c']) for a, g in zip(cd, groups))
            refused = off > 1
        except rc.Admission:
            refused, off = True, float('nan')
        c(f'{name}: arm, demodulation at the continuum', refused, f'worst error / b_g {off:.1f}')
        trajs_b = read(pairs, t, phi, omega_nom, broken=True)
        try:
            cb, _ = rc.admit(rc.Fit(trajs_b, DT), groups)
            offb = max(abs(a - g['c']) / rc.tolerance(g['c']) for a, g in zip(cb, groups))
            refused_b = offb > 1
        except rc.Admission as e:
            refused_b, offb = True, str(e)[:40]
        c(f'{name}: arm, the broken pair', refused_b, f'{offb}')
        if any(g['cls'] == 'imag' for g in groups):
            flipped = [rc.krein(-Hm, fit, members[i]) for i, g in enumerate(groups) if g['cls'] == 'imag']
            c(f'{name}: arm, the flipped form', all(s != g['sign'] for (s, _), g in zip(flipped, [g for g in groups if g['cls'] == 'imag'])),
              'every imaginary group refused by its sign')
        if k > 1:
            try:
                rc.admit(rc.Fit(trajs[:1], DT), groups)
                lost = False
            except rc.Admission:
                lost = True
            c(f'{name}: arm, one direction for a multiple group', lost, 'the multiplicity is lost and the admission fails')
    return out


if __name__ == '__main__':
    print(f'seed {SEED}; dt {DT}; delta {DELTA}; numpy {np.__version__}')
    res = checks()
    print(f'{sum(ok for _, ok, _ in res)} of {len(res)} checks pass')
    sys.exit(0 if all(ok for _, ok, _ in res) else 1)
