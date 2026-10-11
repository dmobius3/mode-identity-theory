"""Continuum only, no solve: the locator's span-gate statistic for C2a/R4, C3/R4, T2/R4 and T3/R5 in each case's frozen
frame, the orientation g0 in the instrument's out/orientations.json, at levels 2 and 3; and, as a check of an independent
review's figures, its smallest value over 20000 random frames. The structural vectors are i w and X_a w for
w = pi(g0^-1) u, pi(q) = sym(su2(q), j2) as the instrument orients a representative (pinned.py), X_a the derivative of
pi along exp(t e_a / 2); each column normalized, then the singular values over the largest.

  python3 span_gate_continuum.py > span_gate_continuum.out"""
import os, sys, json
INSTR = ('/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1/files/framework/files/'
         'working/files/scripts/soft-slot-dynamics-m8-15x/m8_15x_solver')
sys.path.insert(0, INSTR)
import numpy as np
from irreps import sym, su2
from geometry import qconj
from pinned import CASES, cs_vector

J2 = 6
def pi(q):
    return sym(su2(np.asarray(q, float)), J2)

def gens(w, h=1e-6):
    out = []
    for a in range(3):
        e = np.zeros(3); e[a] = 1.0
        qp = np.concatenate([[np.cos(h / 2)], np.sin(h / 2) * e])
        qm = np.concatenate([[np.cos(h / 2)], -np.sin(h / 2) * e])
        out.append((pi(qp) - pi(qm)) @ w / (2 * h))
    return out

def stat(w):
    cols = [1j * w] + gens(w)
    R = np.column_stack([np.concatenate([c.real, c.imag]) for c in cols])
    R = R / np.linalg.norm(R, axis=0)
    s = np.linalg.svd(R, compute_uv=False)
    return s / s[0], [float(np.linalg.norm(c)) for c in cols]

def unit_u(name):
    u = cs_vector(J2, CASES[name]['u'])
    return u / np.linalg.norm(u)

ori = json.load(open(os.path.join(INSTR, 'out', 'orientations.json')))
D = {'C2a': 3, 'C3': 4, 'T2': 4, 'T3': 4}
print('In each frozen frame (g0 from orientations.json):')
for name, slot in (('C2a', 4), ('C3', 4), ('T2', 4), ('T3', 5)):
    u = unit_u(name)
    for lev in (2, 3):
        g0 = np.array(ori[f'{name}/R{slot}/L{lev}']['g0'])
        w = pi(qconj(g0)) @ u
        s, norms = stat(w)
        d = D[name]
        extra = f', sigma_{d + 1}/sigma_1 = {s[d]:.4f}' if d < len(s) else ''
        print(f'  {name}/R{slot} L{lev}: singular values / largest = {", ".join(f"{x:.4f}" for x in s)}; '
              f'gate statistic sigma_{d}/sigma_1 = {s[d - 1]:.4f}{extra}; generator norms {", ".join(f"{x:.3f}" for x in norms)}')
print('Smallest sigma_d/sigma_1 over 20000 random frames (numpy default_rng(20261009)):')
rng = np.random.default_rng(20261009)
qs = rng.standard_normal((20000, 4)); qs /= np.linalg.norm(qs, axis=1)[:, None]
for name in ('C2a', 'C3', 'T2', 'T3'):
    u = unit_u(name); d = D[name]
    vals = [stat(pi(q) @ u)[0][d - 1] for q in qs]
    print(f'  {name}: min {min(vals):.4f}, max {max(vals):.4f}')
