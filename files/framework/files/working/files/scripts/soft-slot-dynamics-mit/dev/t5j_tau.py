"""T5J at eps = 0.25, from M8.16.1's stored summaries: the partner set's pair against the linking distance
tau(lam) = max(margin, KAPPA_D sqrt(u ||A|| |lam|)) at each cutoff. Usage: t5j_tau.py T5J_R2.json FOLDER, with FOLDER
holding instrument/."""
import json, math, sys
sys.path.insert(0, sys.argv[2])
from instrument import linear as ln
U = 2.220446049250313e-16
d = json.load(open(sys.argv[1], encoding='utf-8'))
for e, r in d['readings'].items():
    print('eps', e, r['verdict'], sorted(set(r.get('reasons', []))))
for N in ('16', '24', '32'):
    s = d['cutoffs'][N]['points']['0.25']['summary']
    gs = sorted((g for g in s['groups'] if g['cls'] == 'imag' and 6.0150 < g['c'][1] < 6.0153), key=lambda g: g['c'][1])
    vals = [g['c'][1] for g in gs]
    tau = max(s['margin'], ln.KAPPA_D * math.sqrt(U * s['normA'] * vals[0]))
    gap = vals[1] - vals[0] if len(vals) > 1 else None
    print(f"N = {N}: normA {s['normA']:.3f}, margin {s['margin']:.3e}, tau {tau:.4e}, sizes {[g['size'] for g in gs]}, "
          f"gap {'not stored (linked)' if gap is None else format(gap, '.4e')}" + ('' if gap is None else f', gap / tau {gap / tau:.3f}'))
