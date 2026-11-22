"""Development: what entry 5's directions excited (the terms, THE READ, step 3; DEVLOG entry 7). For each rigid point of
entry 5, in its order and from its seed, the script rebuilds the point and its directions as dev_rigid.py builds them,
without the ladder, and checks the rebuild against entry 5's rigid.json: the record, the step, the targets and, at N = 16,
the read at h0 again, value for value. It then reports each direction's share in the target eigenspaces after the charge
removal, and the singular values of the directions' spectral coefficients on each target group. Development seed only.

Usage: python3 -I -B -u dev_excitation.py RIGID_JSON OUT_JSON"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import member as mb  # noqa: E402
from instrument import branches as br  # noqa: E402

SEED, T = 7300202, 30.0


def rebuild(slot, kappa, N, rng):
    """dev_rigid.py's point, up to its ladder: the same draws, in the same order."""
    S = mb.Slot(slot, N)
    if slot == 'R3':
        v = br.seed_state('C1', S.B)
    else:
        v = np.zeros(S.B.m, complex)
        v[S.low] = rng.normal(size=int(S.low.sum())) + 1j * rng.normal(size=int(S.low.sum()))
        v /= np.linalg.norm(v)
    c0, lam = np.sqrt(kappa) * v, S.lam0 + kappa
    resid = np.linalg.norm((S.e - lam) * c0 + S.X.cubic(c0)) / (lam * np.linalg.norm(c0))
    rec = mb.linear_record(S, c0, lam, tangents_K=S.K)
    r = rec['r']
    w = np.sqrt(lam)
    n = int(S.low.sum()) - 1
    exact = [complex(0, 2 * w), complex(0, np.sqrt(4 * w ** 2 + 2 * kappa))]
    m = S.B.m
    lowmask = np.concatenate([S.low, S.low])
    e0 = [g for g in r['groups'] if g['cls'] == 'imag'
          and np.linalg.norm(r['V'][:2 * m, g['idx']][lowmask]) / np.linalg.norm(r['V'][:2 * m, g['idx']]) > 1 - 1e-8]
    targets = []
    for z, size in zip(exact, (n, 1)):
        g = min(e0, key=lambda g: abs(g['centre'] - z))
        targets.append(dict(c=z, cls='imag', size=size, idx=list(g['idx']), neg=g['neg']))
    P = mb.omega_complement(rec)
    k = max(t['size'] for t in targets)
    dirs = mb.directions(S, rec, c0, lam, [j for t in targets for j in t['idx']], k, rng, lowest_only=True)
    h0, cbar, wbar = mb.step5(S, S.D.energy(c0, 1j * w * c0) * (1 + 1e-6))
    return dict(S=S, c0=c0, lam=lam, rec=rec, P=P, dirs=dirs, targets=targets, exact=exact, h0=h0, cbar=cbar, wbar=wbar,
                residual=float(resid), n=n, k=k, m=m)


def main():
    rj, out = sys.argv[1], sys.argv[2]
    with open(rj, encoding='utf-8') as f:
        J = json.load(f)
    assert J['seed'] == SEED and J['T'] == T
    rng = np.random.default_rng(SEED)
    rows = []
    print(f'dev_excitation: seed {SEED}; entry 5\'s points in its order; numpy {np.__version__}', flush=True)
    for p in J['points']:
        b = rebuild(p['slot'], p['kappa'], p['N'], rng)
        same = (b['m'] == p['m'] and b['n'] == p['n'] and b['lam'] == p['lam'] and b['residual'] == p['residual'] and b['k'] == p['k']
                and b['h0'] == p['h0'] and b['cbar'] == p['cbar'] and b['wbar'] == p['wbar']
                and [dict(c=[t['c'].real, t['c'].imag], size=t['size'], neg=t['neg']) for t in b['targets']] == p['targets'])
        assert same, f"{p['slot']} {p['kappa']} {p['N']}: the rebuild differs from entry 5's record"
        again = None
        if p['N'] == 16:
            S, c0, lam, h0 = b['S'], b['c0'], b['lam'], b['h0']
            runs, scale = mb.pair_runs(S, c0, lam, b['dirs'], h0, int(np.ceil(T / h0)), 1, b['cbar'])
            trajs, _ = mb.to_frame(runs, scale, c0, lam, h0, b['P'])
            fit, centres, members, fl = mb.read(trajs, h0, b['targets'], 1.5 * abs(b['exact'][1]))
            err = [abs(cz - t['c']) / abs(t['c']) for cz, t in zip(centres, b['targets'])]
            again = err == p['reads'][0]['rel_err'] and fl == p['reads'][0]['floor']
            assert again, f"{p['slot']} {p['kappa']}: the read at h0 again differs from entry 5's"
        share, values = mb.excitation(b['rec'], b['dirs'], b['lam'], b['targets'])
        rows.append(dict(slot=p['slot'], kappa=p['kappa'], N=p['N'], k=b['k'], sizes=[t['size'] for t in b['targets']],
                         share=share, singular=values, h0_read_again=again))
        print(f"  {p['slot']} kappa {p['kappa']} N {p['N']}: rebuilt as entry 5 ran it{'; the read at h0 again, value for value' if again else ''}; "
              f"share {', '.join(f'{x:.3f}' for x in share)}; singular values {values}", flush=True)
    with open(out, 'x', encoding='utf-8') as f:
        json.dump(dict(seed=SEED, points=rows), f, indent=1)


if __name__ == '__main__':
    main()
