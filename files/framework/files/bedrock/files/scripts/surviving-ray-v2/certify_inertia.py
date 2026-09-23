#!/usr/bin/env python3
"""Work item 4c, Surviving Ray v2: certified inertia at the three outside orbits, on the full transverse space and
restricted to their fixed sets. Frozen packet: ../work_item_4c_packet.md.

The definitions of certify_isotropy.py (everything before its part 1) are executed verbatim, and through them those
of certify_outside_orbits.py, so every critical-point certificate here is built by the machinery work items 4 and
4b used.

Inertia: the bordered matrix M = [[H_L, C], [C^T, 0]] (H_L = Hess r - 2 mu G in the system's coordinates, C the
sphere gradient and the slice normals) is formed in interval arithmetic over the certified box, made congruent by
the approximate eigenvectors of its centre (Sylvester), and each eigenvalue is placed by a Gershgorin disc. When
every disc excludes zero the inertia holds for every matrix in the box, the true one included, and
In(M) = In(H_L on ker C^T) + (m, 0, m).
"""
import hashlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SRC = HERE / 'certify_isotropy.py'
PACKET = HERE.parent / 'work_item_4c_packet.md'
print(f'packet {PACKET.name}: SHA-256 {hashlib.sha256(PACKET.read_bytes()).hexdigest()}')
print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
print(f'definitions from {SRC.name}: SHA-256 {hashlib.sha256(SRC.read_bytes()).hexdigest()}')
text = SRC.read_text(encoding='utf-8')
marker = '# ---------------------------------------------------------------- part 1: controls, arm, targets'
assert text.count(marker) == 1
h = {'__file__': str(SRC), '__name__': 'isotropy_defs'}
print("--- the definitions' own checks ---")
exec(compile(text.split(marker)[0], str(SRC), 'exec'), h)
print('--- work item 4c ---')
g = h['g']
mp, iv = g['mp'], g['iv']
HESS, INV, Gd = g['HESS'], g['INV'], g['Gd']
T0, Tz = g['T0'], g['Tz']
CritSystem, newton, certify = g['CritSystem'], g['newton'], g['certify']
find_axis, frame, mp_rotate, char_subspace = g['find_axis'], g['frame'], g['mp_rotate'], g['char_subspace']
ipB, Dmat, w_to_x = g['ipB'], g['Dmat'], g['w_to_x']
invariants, same_fingerprint, fmt = g['invariants'], g['same_fingerprint'], g['fmt']

RES = []


def gate(name, ok):
    RES.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    return bool(ok)


def hess_L(x, mu, ctx, drop_mu=False):
    G = [ctx.mpf(q.numerator) / q.denominator for q in Gd]
    hv = HESS(x, ctx)
    H = [[ctx.mpf(0)] * 14 for _ in range(14)]
    for (i, j), v in zip(g['hess_pairs'], hv):
        H[i][j] = v
        H[j][i] = v
    if not drop_mu:
        for i in range(14):
            H[i][i] = H[i][i] - 2 * mu * G[i]
    return H, G


def bordered(S, y, mu, ctx, drop_mu=False, with_slices=True):
    """[[B^T H_L B, C], [C^T, 0]] in the system's coordinates; C = sphere gradient (and the slice normals)."""
    x = S.xof(y, ctx)
    H, G = hess_L(x, mu, ctx, drop_mu)
    d = S.d
    if S.B is None:
        A = H
    else:
        HB = [[sum((H[i][l] * (ctx.mpf(S.B[l][j].numerator) / S.B[l][j].denominator)
                    for l in range(14) if S.B[l][j] != 0), ctx.mpf(0)) for j in range(d)] for i in range(14)]
        cols_ = [S.BT([HB[i][j] for i in range(14)], ctx) for j in range(d)]
        A = [[cols_[j][i] for j in range(d)] for i in range(d)]
    cols = [S.BT([G[i] * x[i] for i in range(14)], ctx)]
    if with_slices:
        cols += [[ctx.mpf(v) for v in c] for c in S.cov]
    m = len(cols)
    n = d + m
    M = [[ctx.mpf(0)] * n for _ in range(n)]
    for i in range(d):
        for j in range(d):
            M[i][j] = A[i][j]
    for k, c in enumerate(cols):
        for i in range(d):
            M[i][d + k] = c[i]
            M[d + k][i] = c[i]
    return M, m


def inertia(S, zc, box, drop_mu=False, with_slices=True):
    """Certified transverse (n-, 0, n+), or None when some Gershgorin disc meets zero."""
    d = S.d
    Mi, m = bordered(S, box[:d], box[d], iv, drop_mu, with_slices)
    Mc, _ = bordered(S, zc[:d], zc[d], mp, drop_mu, with_slices)
    n = len(Mi)
    E, Q = mp.eigsy(mp.matrix(Mc))
    Qi = [[iv.mpf(Q[i, j]) for j in range(n)] for i in range(n)]
    MQ = [[sum((Mi[i][l] * Qi[l][j] for l in range(n)), iv.mpf(0)) for j in range(n)] for i in range(n)]
    K = [[sum((Qi[l][i] * MQ[l][j] for l in range(n)), iv.mpf(0)) for j in range(n)] for i in range(n)]
    neg = pos = und = 0
    for i in range(n):
        rad = sum((abs(K[i][j]) for j in range(n) if j != i), iv.mpf(0))
        lo, hi = (K[i][i] - rad).a, (K[i][i] + rad).b
        if lo > 0:
            pos += 1
        elif hi < 0:
            neg += 1
        else:
            und += 1
    if und:
        return None
    return (neg - m, 0, pos - m)


def c2_complex_system(w, label):
    """Certify inside the complex character subspace of the unitary C2 alone; slices: phase and z-rotation."""
    _, n1 = find_axis(w, 2)
    A = frame(n1)
    xw = w_to_x(w)
    best = None
    for Acand in (A, A.T):
        xr = mp_rotate(xw, Acand)
        wr = np.array([complex(float(xr[k]), float(xr[7 + k])) for k in range(7)])
        chi = ipB(wr, Dmat([0, 0, 1], np.pi) @ wr) / ipB(wr, wr)
        m0 = int(round(-2 * np.angle(chi) / (2 * np.pi))) % 2
        Bc = char_subspace(2, m0, None)
        Bf = np.array([[float(v) for v in row] for row in Bc])
        xf = np.array([float(v) for v in xr])
        yls, *_ = np.linalg.lstsq(Bf, xf, rcond=None)
        resid = np.linalg.norm(Bf @ yls - xf)
        if best is None or resid < best[0]:
            best = (resid, Bc, xr, m0)
    resid, Bc, xr, m0 = best
    print(f'  {label}: aligned state lies in the C2 character subspace (m0 = {m0}) to residual {resid:.1e}', flush=True)
    if resid > 1e-5:
        return None
    Bmp = mp.matrix([[mp.mpf(v.numerator) / v.denominator for v in row] for row in Bc])
    y0 = mp.lu_solve(Bmp.T * Bmp, Bmp.T * mp.matrix(xr))
    y0 = [y0[i] for i in range(len(Bc[0]))]
    S = CritSystem(Bc, [T0, Tz], y0)
    r0, N0 = INV(S.xof(y0, mp), mp)[:2]
    z, _ = newton(S, y0 + [2 * r0 / N0 ** 2, 0, 0])
    out = certify(S, z)
    out.update(S=S, z=z, m0=m0)
    if out['ok']:
        out['inv'] = invariants(S.xof(out['box'][:S.d], iv))
        print(f'  {label}: CERTIFIED in the complex C2 subspace (real dimension {S.d}, slices 2) at radius '
              f'{out["rho"]}; 924 r6 in {fmt(out["inv"]["v924"])}', flush=True)
    else:
        print(f'  {label}: NOT CERTIFIED in the complex C2 subspace', flush=True)
    return out


def seed(name):
    for sector in ('r4', 'r5'):
        if (sector, name) in seeds:
            return sector, seeds[(sector, name)]
    return None, None


def leq(a, b):
    return a is not None and b is not None and a[0] <= b[0] and a[2] <= b[2]


# ---------------------------------------------------------------- seeds: add the octahedron and the hexagon
seeds = dict(g['seeds'])
for sector in ('r4', 'r5'):
    dd = np.load(g['MIT'] / f'OpenWave/M8_DYNAMICS/out/pencil_census_{sector}.npz')
    for i in range(12):
        w = g['to_w'](dd[f'orb{i:02d}'])
        v = g['r924_at'](w)
        if abs(v - 288) < 1e-6:
            seeds[(sector, 'octahedron')] = w
        if abs(v - 463) < 1e-6:
            seeds[(sector, 'hexagon')] = w
gate('the census holds the six controls', all(seed(n)[0] for n in
                                               ('octahedron', 'hexagon', 'pyramid', 'prism', 'C3ray', 'D2ray')))

# ---------------------------------------------------------------- controls: M8.12's exact signatures
print('\ncontrols: the six finite-stabiliser census orbits against M8.12\'s exact signatures')
EXPECT = {'octahedron': (6, 0, 3), 'hexagon': (9, 0, 0), 'pyramid': (5, 0, 4), 'prism': (3, 0, 6),
          'C3ray': (5, 0, 4), 'D2ray': (5, 0, 4)}
ctrl = {}
for name, exp in EXPECT.items():
    sector, w = seed(name)
    S, x0 = g['full_system'](w)
    full = g['certify_full'](w, f'{name} ({sector}, full sphere)')
    sig = inertia(S, full['z'], full['box']) if full['ok'] else None
    ctrl[name] = dict(S=S, full=full, sig=sig)
    print(f'  {name}: certified transverse signature {sig}; M8.12 exact {exp}', flush=True)
    gate(f'control {name}: certified signature equals M8.12\'s exact {exp}', sig == exp)

print('\narms (each on a green parent)')
hx = ctrl['hexagon']
parent = hx['sig'] == (9, 0, 0)
sig_arm = inertia(hx['S'], hx['full']['z'], hx['full']['box'], drop_mu=True) if parent else None
print(f'  hexagon without the -2 mu G term: {sig_arm}')
gate('arm (packet): dropping the -2 mu G term gives a certified signature different from the hexagon\'s (9, 0, 0)',
     parent and sig_arm is not None and sig_arm != (9, 0, 0))
sig_ns = inertia(hx['S'], hx['full']['z'], hx['full']['box'], with_slices=False) if parent else 'parent red'
print(f'  hexagon without the slice columns: {sig_ns}')
gate('arm (added): without the slice columns the orbit directions are null and no signature is certified',
     parent and sig_ns is None)

# ---------------------------------------------------------------- targets
print('\ntargets')
summary = {}
for name, k in (('T1', 2), ('T2', None), ('T3', 2)):
    sector, w = seed(name)
    S, x0 = g['full_system'](w)
    full = g['certify_full'](w, f'{name} ({sector}, full sphere)')
    sig_full = inertia(S, full['z'], full['box']) if full['ok'] else None
    recon = g['signature'](full['z'])
    joint = h['certify_joint'](w, f'{name} (isotropy fixed set)', k, dihedral=False, d2d=False)
    jok = joint is not None and joint['ok']
    sig_joint = inertia(joint['S'], joint['z'], joint['box']) if jok else None
    c2 = c2_complex_system(w, f'{name}') if k == 2 else None
    cok = c2 is not None and c2['ok']
    sig_c2 = inertia(c2['S'], c2['z'], c2['box']) if cok else None
    summary[name] = dict(full=sig_full, joint=sig_joint, c2=sig_c2, v924=full['inv']['v924'] if full['ok'] else None)
    print(f'  {name}: certified signatures: full transverse {sig_full} (work item 4 reconnaissance {recon}); '
          f'isotropy fixed set {sig_joint}' + (f'; complex C2 subspace {sig_c2}' if k == 2 else ''), flush=True)
    gate(f'{name}: full transverse signature certified, dimension 9, agreeing with the reconnaissance',
         sig_full is not None and sum(sig_full) == 9 and sig_full == recon)
    dj = joint['S'].d - 1 - len(joint['S'].T) if jok else None
    gate(f'{name}: restricted signature on the isotropy fixed set certified, dimension {dj}, same orbit',
         sig_joint is not None and sum(sig_joint) == dj and same_fingerprint(full['inv'], joint['inv']))
    gate(f'{name}: fixed-set counts bounded by the full counts (block diagonality)', leq(sig_joint, sig_full))
    if k == 2:
        dc = c2['S'].d - 1 - len(c2['S'].T) if cok else None
        gate(f'{name}: restricted signature on the complex C2 subspace certified, dimension {dc}, same orbit',
             sig_c2 is not None and sum(sig_c2) == dc and same_fingerprint(full['inv'], c2['inv']))
        gate(f'{name}: fixed set within C2 subspace within full, counts nested', leq(sig_joint, sig_c2) and
             leq(sig_c2, sig_full))
        if name == 'T1':
            arm = inertia(c2['S'], c2['z'], c2['box'], with_slices=False) if sig_c2 is not None else 'parent red'
            gate('arm (added): in the C2 subspace without its slice columns, no signature is certified',
                 sig_c2 is not None and arm is None)

print('\nreading at the two signs: a local minimum of the energy on a set has restricted n- = 0 at g = 1, '
      'n+ = 0 at g = -1')
for name, s in summary.items():
    for label, key in (('full transverse space', 'full'), ('isotropy fixed set', 'joint'),
                       ('complex C2 subspace', 'c2')):
        sg = s[key]
        if sg is None:
            continue
        print(f'  {name} on the {label}: {sg}; local minimum at g = 1: {"yes" if sg[0] == 0 else "no"}; '
              f'at g = -1: {"yes" if sg[2] == 0 else "no"}')
oc = ctrl['octahedron']['full']
print(f'\nT3 against the octahedron at g = 1: T3 index {summary["T3"]["full"][0] if summary["T3"]["full"] else "?"} '
      f'(certified here) at 924 r6 in {fmt(summary["T3"]["v924"])}; octahedron index 6 (M8.12 exact; certified here '
      f'as a control) at 924 r6 in {fmt(oc["inv"]["v924"])}')
n_fail = sum(1 for _, ok in RES if not ok)
print('ALL PASS' if n_fail == 0 else f'{n_fail} FAILED')
