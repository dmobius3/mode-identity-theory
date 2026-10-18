"""Section dimensions of E_rho at complete levels n <= N, from 2I's characters (arithmetic only)."""
import itertools, math
import numpy as np
phi = (1 + 5 ** 0.5) / 2
q = set()
for s in itertools.product((1, -1), repeat=1):
    pass
els = []
for i in range(4):
    for s in (1, -1):
        v = [0, 0, 0, 0]; v[i] = s; els.append(tuple(v))
for s in itertools.product((0.5, -0.5), repeat=4):
    els.append(tuple(s))
base = (0, 0.5, 1 / (2 * phi), phi / 2)  # (0, 1/2, 1/(2phi), phi/2) up to even permutations and signs
even = [p for p in itertools.permutations(range(4)) if sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b]) % 2 == 0]
for p in even:
    for s in itertools.product((1, -1), repeat=3):
        v = [0.0] * 4
        vals = [base[0], s[0] * base[1], s[1] * base[2], s[2] * base[3]]
        for k in range(4):
            v[p[k]] = vals[k]
        els.append(tuple(v))
E = np.unique(np.round(np.array(els), 12), axis=0)
assert len(E) == 120, len(E)
q0 = E[:, 0]
theta = 2 * np.arccos(np.clip(q0, -1, 1))
def chi(n, th):
    s = np.sin(th / 2)
    out = np.empty_like(th)
    small = np.abs(s) < 1e-12
    out[~small] = np.sin((n + 1) * th[~small] / 2) / s[~small]
    out[small] = (n + 1) * np.sign(np.cos(th[small] / 2)) ** n
    return out
# Galois conjugate of the trace 2 q0: sqrt5 -> -sqrt5
def galois_trace(t):
    out = t.copy()
    for a, b in ((phi, -1 / phi), (-phi, 1 / phi), (1 / phi, -phi), (-1 / phi, phi)):
        out[np.isclose(t, a)] = b
    return out
tg = galois_trace(2 * q0)
chis = {"R1": chi(1, theta), "R2": chi(7, theta) - chi(5, theta), "R3": chi(2, theta), "R4": tg ** 2 - 1,
        "R5": chi(6, theta) - (tg ** 2 - 1), "R6": chi(3, theta), "R7": chi(4, theta), "R8": chi(5, theta)}
dimr = {k: int(round(v[np.isclose(q0, 1)][0])) for k, v in chis.items()}
def mult(n, r):
    return int(round(np.mean(chi(n, theta) * chis[r])))
print('dims', dimr)
print('lowest level', {r: min(n for n in range(20) if mult(n, r) > 0) for r in chis})
for N in (16, 24, 32, 40, 48):
    row = {r: sum(mult(n, r) * (n + 1) for n in range(N + 1)) for r in chis}
    nodes = (4 * N + 1) ** 2 * (N + 1)
    print(f'N={N:2d} complex dims', row, '| product-rule nodes', nodes)
