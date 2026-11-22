"""Development: the outside part of entry 5's directions (DEVLOG entry 8). For each rigid point of entry 5, in its order and
from its seed, the script rebuilds the point as dev_excitation.py does, and beside it draws each direction again from
the same draws, by a copy of member.directions that keeps the norm of the part outside the targets and the generalized
kernel before and after its projection. Each copy's direction must equal member.directions' bit for bit. Development
seed only.

Usage: python3 -I -B -u dev_outside.py RIGID_JSON OUT_JSON"""
import copy
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.dirname(HERE)]
import member as mb  # noqa: E402
import dev_excitation as dx  # noqa: E402
from instrument import functional as fn  # noqa: E402


def directions_kept(S, rec, c0, lam, target_idx, k, rng, lowest_only=False):
    """member.directions, line for line, keeping |b| before and after the projection off the targets and V0."""
    m = S.B.m
    V = rec['r']['V']
    Vt = np.hstack([V[:, target_idx].real, V[:, target_idx].imag])
    Qt = np.linalg.qr(Vt)[0]
    V0 = rec['r']['V0']
    Qs = np.linalg.qr(np.hstack([Vt, V0]))[0]
    w = np.sqrt(lam)
    lowmask = np.concatenate([S.low, S.low, S.low, S.low])
    out, kept = [], []
    for _ in range(k):
        a = Qt @ rng.normal(size=Qt.shape[1])
        b = rng.normal(size=4 * m)
        if lowest_only:
            b = np.where(lowmask, b, 0.0)
        before = np.linalg.norm(b)
        b = b - Qs @ (Qs.T @ b)
        if lowest_only:
            b = np.where(lowmask, b, 0.0)
        kept.append(float(np.linalg.norm(b) / before))
        x = a / np.linalg.norm(a) + (b / np.linalg.norm(b) if np.linalg.norm(b) > 0 else 0.0)
        zeta, zdot = fn.to_complex(x[:2 * m]), fn.to_complex(x[2 * m:])
        dc, dv = zeta, zdot + 1j * w * zeta
        dq, dp = mb.charge_free(S, c0, 1j * w * c0, fn.to_real(dc), fn.to_real(dv))
        dc, dv = fn.to_complex(dq), fn.to_complex(dp)
        nrm = np.sqrt(np.vdot(dc, dc).real + np.vdot(dv, dv).real)
        out.append((dc / nrm, dv / nrm))
    return out, kept


def main():
    rj, out = sys.argv[1], sys.argv[2]
    with open(rj, encoding='utf-8') as f:
        J = json.load(f)
    assert J['seed'] == dx.SEED
    rng = np.random.default_rng(dx.SEED)
    rows = []
    print(f'dev_outside: seed {dx.SEED}; entry 5\'s points in its order; numpy {np.__version__}', flush=True)
    for p in J['points']:
        twin = copy.deepcopy(rng)
        b = dx.rebuild(p['slot'], p['kappa'], p['N'], rng)
        assert b['h0'] == p['h0'] and b['residual'] == p['residual'], f"{p['slot']} {p['kappa']} {p['N']}: the rebuild differs from entry 5's record"
        if p['slot'] == 'R1':
            n0 = int(b['S'].low.sum())
            twin.normal(size=n0), twin.normal(size=n0)
        dirs, kept = directions_kept(b['S'], b['rec'], b['c0'], b['lam'], [j for t in b['targets'] for j in t['idx']], b['k'], twin, lowest_only=True)
        same = all(np.array_equal(x[0], y[0]) and np.array_equal(x[1], y[1]) for x, y in zip(dirs, b['dirs']))
        assert same, f"{p['slot']} {p['kappa']} {p['N']}: the copy's directions differ from member.directions'"
        rows.append(dict(slot=p['slot'], kappa=p['kappa'], N=p['N'], kept=kept, same=same))
        print(f"  {p['slot']} kappa {p['kappa']} N {p['N']}: outside part kept {', '.join(f'{x:.1e}' for x in kept)} of its norm; "
              'directions bit for bit', flush=True)
    with open(out, 'x', encoding='utf-8') as f:
        json.dump(dict(seed=dx.SEED, points=rows), f, indent=1)


if __name__ == '__main__':
    main()
