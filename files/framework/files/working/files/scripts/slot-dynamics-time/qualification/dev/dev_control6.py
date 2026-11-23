"""Development: the prototype's control 6 at the development points, with each read's floor (DEVLOG entry 10). For R1 and R3
at ||phi||^2 = 0.5 and 2, N = 16, on the six-step ladder h0 to h0/32, the script reads Theorem 3.7's two frequencies on
E0 as the prototype's controls.perturbed_run reads them: from the matched discrete wave, perturbed on E0 with its phase
charge removed, demodulated at the scheme's own rotation and fitted by its dmd, the frequencies above a quarter of the
smaller expected one, as many as the distinct values. It computes each read frequency's floor as the terms' step 8 does,
the change when the fit uses the first nine tenths of the observations, and each ratio's eligibility under the three
readings of (R1)'s "ten floors". Its copy of the read is checked against controls.perturbed_run at h0, value for value.
Development seed 7300303; the prototype's registered parameters for control 6.

Usage: python3 -I -B -u dev_control6.py OUT_JSON"""
import json
import os
import sys
import time

import numpy as np

ARM = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ARM)
import controls as ct  # noqa: E402  (the prototype's controls, read only)
import timearm as ta  # noqa: E402

SEED = 7300303
P = dict(ct.REG)
LADDER = 6
N = 16


def rigid(slot, kappa, rng):
    """controls.setup_B's rigid member and perturbation, from a development seed, at a development point."""
    S = ct.Slot(slot, N)
    phi = ct.on_level(S, rng, S.low, np.sqrt(kappa))
    Om = float(np.sqrt(S.lam0 + kappa))
    h0, cbar, wbar = ct.step5(S, S.D.energy(phi, 1j * Om * phi), P)
    return dict(S=S, slot=slot, phi=phi, Om=Om, kappa=kappa, h0=h0, cbar=cbar, wbar=wbar,
                hs=[h0 / 2 ** j for j in range(LADDER)], K6=int(np.ceil(P['T6'] / h0)),
                dpert=(ct.on_level(S, rng, S.low, 1.0), ct.on_level(S, rng, S.low, 1.0)))


def read(R, h, K):
    """controls.perturbed_run's read with the cubic on, line for line, keeping its snapshots; and the same read on their
    first nine tenths."""
    S, phi, kappa = R['S'], R['phi'], R['kappa']
    z0, dz0, th = ta.matched('strang', h, S.lam0, kappa)
    c0, v0 = z0 * phi, dz0 * phi
    dc, dv = R['dpert']
    dN = float(np.imag(np.vdot(dc, v0) + np.vdot(c0, dv)))
    dv = dv - 1j * c0 * dN / np.vdot(c0, c0).real
    sc = P['eps6'] * ct.qp(c0, v0) / ct.qp(dc, dv)
    dc, dv = sc * dc, sc * dv
    low, snaps = S.low, []

    def obs(s, c, v):
        ph = np.exp(-1j * s * th)
        zc, zv = ph * c[low] - c0[low], ph * v[low] - v0[low]
        snaps.append(np.concatenate([zc.real, zc.imag, zv.real, zv.imag]))

    obs(0, c0 + dc, v0 + dv)
    ct.evolve('strang', c0 + dc, v0 + dv, h, K, S, S.X.cubic, R['cbar'], 1, obs)
    n1 = int(low.sum())
    expect = np.array(([2 * R['Om']] if n1 > 1 else []) + [np.sqrt(4 * R['Om'] ** 2 + 2 * kappa)])
    cut = 0.25 * expect.min()
    X = np.array(snaps).T
    out = {}
    for name, cols in (('full', X.shape[1]), ('nine_tenths', max(3, int(0.9 * X.shape[1])))):
        mu, nu, rank = ct.dmd(X[:, :cols], h, P['rank6'])
        pos = np.sort(mu[mu > cut])
        out[name] = dict(frequencies=[float(x) for x in pos], rank=int(rank), read=len(pos) == len(expect))
    return out, expect


def main():
    path = sys.argv[1]
    rng = np.random.default_rng(SEED)
    rows = []
    print(f'dev_control6: seed {SEED}; N {N}; ladder h0 to h0/{2 ** (LADDER - 1)}; T6 {P["T6"]}; eps6 {P["eps6"]}; '
          f'rank6 {P["rank6"]}; numpy {np.__version__}', flush=True)
    for slot, kappa in (('R1', 0.5), ('R1', 2.0), ('R3', 0.5), ('R3', 2.0)):
        R = rigid(slot, kappa, rng)
        steps = []
        for j in range(LADDER):
            t0 = time.perf_counter()
            r, expect = read(R, R['hs'][j], R['K6'] * 2 ** j)
            if j == 0:      # the copy against the prototype's own read
                ref = ct.perturbed_run(R, 'strang', R['hs'][0], R['K6'], True, P)
                assert [float(x) for x in ref['frequencies']] == r['full']['frequencies'], 'the copy differs from controls.perturbed_run'
            assert r['full']['read'] and r['nine_tenths']['read'], f'{slot} {kappa} h0/{2 ** j}: a read did not admit both frequencies'
            f, g = np.array(r['full']['frequencies']), np.array(r['nine_tenths']['frequencies'])
            steps.append(dict(f=2 ** j, h=R['hs'][j], hw=R['hs'][j] * R['wbar'], frequencies=f.tolist(), rel_err=(np.abs(f - expect) / expect).tolist(),
                              floor=np.abs(f - g).tolist(), rank=r['full']['rank'], seconds=time.perf_counter() - t0))
            print(f"  {slot} kappa {kappa} h0/{2 ** j}: errors {', '.join(f'{x:.2e}' for x in steps[-1]['rel_err'])}; "
                  f"floors {', '.join(f'{x:.1e}' for x in steps[-1]['floor'])}; {steps[-1]['seconds']:.0f} s", flush=True)
        fr = np.array([s['frequencies'] for s in steps])
        fl = np.array([s['floor'] for s in steps])
        d1, d2 = np.abs(fr[3] - fr[4]), np.abs(fr[4] - fr[5])
        elig = dict(finer=np.minimum(d1 / (10 * fl[4]), d2 / (10 * fl[5])).tolist(),
                    larger=np.minimum(d1 / (10 * np.maximum(fl[3], fl[4])), d2 / (10 * np.maximum(fl[4], fl[5]))).tolist(),
                    largest=(np.minimum(d1, d2) / (10 * fl[3:].max(axis=0))).tolist())
        rows.append(dict(slot=slot, kappa=kappa, N=N, h0=R['h0'], wbar=R['wbar'], expected=expect.tolist(), steps=steps,
                         d1=d1.tolist(), d2=d2.tolist(), ratios=(d1 / d2).tolist(), eligibility=elig))
        print(f"{slot} kappa {kappa}: ratios {', '.join(f'{x:.4f}' for x in d1 / d2)}; eligibility, the margin over ten floors: "
              f"finer {', '.join(f'{x:.3g}' for x in elig['finer'])}; larger {', '.join(f'{x:.3g}' for x in elig['larger'])}; "
              f"largest {', '.join(f'{x:.3g}' for x in elig['largest'])}", flush=True)
    with open(path, 'x', encoding='utf-8') as f:
        json.dump(dict(seed=SEED, N=N, ladder=LADDER, params=dict(T6=P['T6'], eps6=P['eps6'], rank6=P['rank6'], margin=P['margin']),
                       points=rows), f, indent=1)


if __name__ == '__main__':
    main()
