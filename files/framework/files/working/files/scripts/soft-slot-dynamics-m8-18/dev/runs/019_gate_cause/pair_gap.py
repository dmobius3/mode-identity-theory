"""A diagnostic on a scratch copy of the folder, outside the run: P5's pair near 4.0203 at eps = 0.25, read from the stored
solutions at each cutoff, from the eigenvalues before they are linked. Usage: pair_gap.py FOLDER."""
import json, os, sys
import numpy as np
ROOT = sys.argv[1]
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import basis, functional as fn, linear as ln
import driver as dr
F = json.load(open(os.path.join(ROOT, 'run', 'FROZEN.json'), encoding='utf-8'))
orig, cap = ln.group, {}
def spy(vals, tol):
    if np.ndim(tol):
        cap['vals'], cap['tol'] = np.array(vals), np.array(tol)
    return orig(vals, tol)
ln.group = spy
name, key = 'P5', '0.25'
case = F['cases'][name]
pair = {}
for N in (24, 32, 40):
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
    v, t = cap['vals'], cap['tol']
    near = np.where((v.imag > 0) & (np.abs(v.imag - 4.02029) < 1.5e-5))[0]
    near = near[np.argsort(v[near].imag)]
    assert len(near) == 2
    a, b = v[near]
    pair[N] = a, b
    tol = float(max(t[near]))
    groups = [g for g in orig(v, t) if near[0] in g]
    stored = rec['points'][key]
    same = {k: stored['record'][k] == point['record'][k] for k in ('type', 'nL', 'nD', 'K', 'margin', 'unresolved', 'normA')}
    print(f"N {N}: the pair's imaginary parts {a.imag:.12f} and {b.imag:.12f}; real parts below {max(abs(a.real), abs(b.real)):.0e}; "
          f"gap {b.imag - a.imag:.4e}; tau {tol:.4e}; one group: {near[1] in groups[0]}", flush=True)
    print(f"   against the stored read: {same}", flush=True)
for p, q in ((24, 32), (32, 40)):
    print(f"from N {p} to {q}: the lower moves {abs(pair[q][0].imag - pair[p][0].imag):.1e}, the upper {abs(pair[q][1].imag - pair[p][1].imag):.1e}", flush=True)
