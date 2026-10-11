"""Registered-expectation forecast for the nonflat distance comparison (work order v3, 2026-10-10).

Synthetic data only: the published Λcos flat best fit's own predictions (results/lcos_summary.json),
on the data's redshifts and with the data's covariances. No measured residual vector enters.
The closed model D_M = (c/H0) zeta sin(I/zeta), H(z) unchanged, is fitted to them with M_B and the
BAO amplitude c/(H0 r_d) profiled analytically, both clipped to fit_lcos.py's box (H0 r_d in [8000, 12000],
M_B in [-20, -18], the closure of its strict prior), and s0 profiled on [0.001, 0.99], the same closure.
Also writes the synthetic data sets the gates hold fixed (G3 to G5): synthetic_v3.json, generated here on
20 001 points, independently of the instrument.

Reports, at the pinned readings (A 6.13, C 10.5, B 19.7 Gpc) and both scale rows (H0 67.36, 73.04):
zeta, the expected profiled Δχ², the profiled s0, the real-data spread (Δχ² ~ N(A, 4A) under flat
truth) with the chance of each grade at the bars 9 and 25, and the expected one-sided 95% bound on
zeta (Δχ² = 2.71 above the minimum, flat on the boundary) with Ω0·R in Gpc at both rows.
Writes forecast_registered.json beside itself.
"""
import json, os, sys, numpy as np, pandas as pd
from math import erf, sqrt
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize_scalar, brentq

LC = '/Users/blake/lambda-cos/'
READINGS = {'A': 6.13, 'C': 10.5, 'B': 19.7}       # Gpc
ROWS = (67.36, 73.04)                              # km/s/Mpc
BARS = (9.0, 25.0)
BOUND = 2.71
OL, c = 0.685, 299792.458

bf = json.load(open(LC + 'results/lcos_summary.json'))['best_fit']
S0F, H0RD, MB = bf['s0'], bf['H0rd'], bf['MB']
sn = pd.read_csv(LC + 'data/pantheon_plus.csv'); Csn_i = np.linalg.inv(np.load(LC + 'data/pantheon_plus_cov.npy'))
bao = pd.read_csv(LC + 'data/desi_dr2_bao.csv'); Cb_i = np.linalg.inv(np.load(LC + 'data/desi_dr2_bao_cov.npy'))
z = np.linspace(0, 2.5, 20001)
one = np.ones(len(sn))

def EI(s0):
    E = np.sqrt((1-OL)/(1-s0**2)*(1+z)**3 - (1-OL)*s0**2/(1-s0**2)*(1+z) + OL)
    return E, cumulative_trapezoid(1/E, z, initial=0)

def shapes(s0, zeta):
    E, I = EI(s0)
    Iz, Ez = np.interp(bao.z_eff, z, I), np.interp(bao.z_eff, z, E)
    dm = Iz if np.isinf(zeta) else zeta*np.sin(Iz/zeta)
    dh = 1/Ez
    f = np.array([(zz*m**2*h)**(1/3) if o == 'DV_rd' else (m if o == 'DM_rd' else h)
                  for zz, m, h, o in zip(bao.z_eff, dm, dh, bao.observable)])
    Is = np.interp(sn.zHD, z, I)
    # the published magnitude convention of fit_lcos.py L64: 5 log10((1+z) (c/70) D) + 25, with H0 = 70 absorbed by M_B
    mu = 5*np.log10((1+sn.zHD)*(c/70)*(Is if np.isinf(zeta) else zeta*np.sin(Is/zeta))) + 25
    return f, mu

f0, mu0 = shapes(S0F, np.inf)
bao_syn, sn_syn = (c/H0RD)*f0, MB + mu0

def chi2(s0, zeta):
    f, mu = shapes(s0, zeta)
    A = (f @ Cb_i @ bao_syn)/(f @ Cb_i @ f); A = min(max(A, c/12000), c/8000); db = A*f - bao_syn
    d = sn_syn - mu; off = (one @ Csn_i @ d)/(one @ Csn_i @ one); off = min(max(off, -20), -18); ds = d - off
    return float(db @ Cb_i @ db + ds @ Csn_i @ ds)

def prof(zeta):
    grid = np.concatenate([[0.001], np.arange(0.01, 0.985, 0.01), [0.99]])
    vals = [chi2(s, zeta) for s in grid]
    k = int(np.argmin(vals))
    r = minimize_scalar(lambda s: chi2(s, zeta), bounds=(grid[max(k-1, 0)], grid[min(k+1, len(grid)-1)]),
                        method='bounded', options={'xatol': 1e-6})
    return min((vals[k], grid[k]), (r.fun, r.x))

Phi = lambda x: 0.5*(1+erf(x/sqrt(2)))
out = {'inputs': {'best_fit': bf, 'readings_gpc': READINGS, 'rows_h0': ROWS, 'bars': BARS, 'bound': BOUND,
                  'grid_points': len(z), 'python': sys.version.split()[0], 'numpy': np.__version__},
       'flat_self_check': chi2(S0F, np.inf), 'cells': {}}
for H0 in ROWS:
    for lab, R in READINGS.items():
        zeta = R*1000*H0/c
        d, s_hat = prof(zeta)
        sd = 2*sqrt(d)
        cell = {'zeta': zeta, 'dchi2': d, 's0_hat': s_hat, 'sd': sd,
                'p_excluded': 1-Phi((BARS[1]-d)/sd), 'p_not_excluded': Phi((BARS[0]-d)/sd)}
        cell['p_disfavored'] = 1 - cell['p_excluded'] - cell['p_not_excluded']
        out['cells'][f'{lab}@{H0}'] = cell
        print(f"{lab} R={R:5.2f} Gpc  H0={H0:5.2f}  zeta={zeta:6.4f}  dchi2={d:8.3f}  s0_hat={s_hat:.4f}  sd={sd:6.2f}"
              f"  P(EXCL)={cell['p_excluded']:.3f}  P(DISF)={cell['p_disfavored']:.3f}  P(NOT)={cell['p_not_excluded']:.3f}")
zb = brentq(lambda zt: prof(zt)[0] - BOUND, 2.0, 8.0, xtol=1e-5)
out['bound'] = {'zeta95': zb, 'R95_gpc': {str(H0): zb*c/H0/1000 for H0 in ROWS}}
print(f"expected one-sided 95% bound: zeta >= {zb:.4f}  ->  Omega0 R >= " +
      ", ".join(f"{zb*c/H0/1000:.2f} Gpc at {H0}" for H0 in ROWS))
print(f"flat self-check chi2 = {out['flat_self_check']:.2e}")
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'forecast_registered.json'), 'w'), indent=1)

# the synthetic data sets G3 to G5 hold fixed: flat, and the closed model at each reading's zeta in both rows at s0 = 0.001 and 0.1
syn = {'flat_bao': bao_syn, 'flat_sn': sn_syn}
for H0 in ROWS:
    for lab, R in READINGS.items():
        for s0 in (0.001, 0.1):
            f, mu = shapes(s0, R*1000*H0/c)
            key = f'{lab}_{H0}_{s0}'
            syn[key + '_bao'], syn[key + '_sn'] = (c/H0RD)*f, MB + mu
# JSON, not npz: npz embeds zip timestamps, so its bytes would change on every run
json.dump({k: [float(x) for x in v] for k, v in syn.items()},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'synthetic_v3.json'), 'w'), sort_keys=True, separators=(',', ':'))
print('synthetic sets written:', (len(syn) - 2)//2, 'closed + 1 flat')
