"""A diagnostic on a scratch copy of the folder, outside the run: D's eigenvalues against ||B||, from the stored solutions."""
import json, os, sys, time
import numpy as np
ROOT = sys.argv[1]
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import basis, functional as fn, linear as ln
import driver as dr
F = json.load(open(os.path.join(ROOT, 'run', 'FROZEN.json'), encoding='utf-8'))
orig, cap = ln.inertia, {}
def spy(M, zero_rel=1e-10, gray=1e3, scale=None):
    if scale is not None:
        cap['ev'], cap['scale'] = np.linalg.eigvalsh((M + M.T) / 2), scale
    return orig(M, zero_rel, gray=gray, scale=scale)
ln.inertia = spy
JOBS = [('C3R/R4', 24, '0.25'), ('C3R/R4', 32, '0.25'), ('C3R/R4', 40, '0.25'), ('C3R/R4', 40, '0.5'),
        ('P5', 32, '0.25'), ('P5', 40, '0.25')]
for name, N, key in JOBS:
    t0 = time.time()
    case = F['cases'][name]
    B = basis.Basis(case['slot'], N)
    Fn = fn.Functional(B)
    K = fn.fibre_structure_matrix(Fn)[1] if case['slot'] == 'R2' else None
    base = os.path.join(ROOT, 'run', 'out', f'{dr.safe(name)}_N{N}')
    rec = json.load(open(base + '_read.json', encoding='utf-8'))
    with np.load(base + '.npz', allow_pickle=False) as z:
        keys = [str(x) for x in z['keys']]
        i = keys.index(key)
        c, lam = z[f'c{i}'], float(z['lam'][i])
    point, _, r = dr.read_point(Fn, K, c, lam, case, float(key), False)
    ev, s = cap['ev'], cap['scale']
    a = np.sort(np.abs(ev)) / s
    print(f"{name} N {N} eps {key}: {time.time() - t0:.0f} s; ||B|| {s:.6g}; D's eigenvalues {np.array2string(ev, precision=6)}", flush=True)
    print(f"   |ev| / ||B||, sorted: {np.array2string(a, precision=4)}; gray zone (1e-8, 1e-5); gray's top in units of ev: {1e-5 * s:.6g}", flush=True)
    print(f"   this read: unresolved {point['record']['unresolved']}, margin {point['record']['margin']:.10e}, nD {point['record']['nD']}", flush=True)
    stored = rec['points'][key] if 'points' in rec else None
    if stored is not None:
        same = {k: stored['record'][k] == point['record'][k] for k in ('type', 'nL', 'nD', 'K', 'margin', 'unresolved', 'normA')}
        print(f"   against the stored read: {same}", flush=True)
