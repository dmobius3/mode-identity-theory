#!/usr/bin/env python3
"""Work item 4b, Surviving Ray v2: the full isotropy (unitary and antiunitary) of the three outside orbits,
and Kawaguchi and Ueda's Table II at the coupling point. Frozen packet: ../work_item_4b_packet.md.

The definitions of certify_outside_orbits.py (everything before its controls) are executed verbatim from its
source, so the model, the critical system, the Krawczyk test and the star certificate are the ones work item 4
certified with. Its own provenance lines print first.
"""
import hashlib
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SRC = HERE / 'certify_outside_orbits.py'
PACKET_4B = HERE.parent / 'work_item_4b_packet.md'
print(f'packet {PACKET_4B.name}: SHA-256 {hashlib.sha256(PACKET_4B.read_bytes()).hexdigest()}')
print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
print(f'definitions from {SRC.name}: SHA-256 {hashlib.sha256(SRC.read_bytes()).hexdigest()}')
text = SRC.read_text(encoding='utf-8')
marker = '# ---------------------------------------------------------------- 6. controls'
assert text.count(marker) == 1
g = {'__file__': str(SRC), '__name__': 'certify_defs'}
print('--- the definitions\' own checks (work item 4 provenance and model) ---')
exec(compile(text.split(marker)[0], str(SRC), 'exec'), g)
print('--- work item 4b ---')
mp, iv = g['mp'], g['iv']
ipB, Dmat, find_axis, mp_rotate = g['ipB'], g['Dmat'], g['find_axis'], g['mp_rotate']
CritSystem, newton, certify, INV = g['CritSystem'], g['newton'], g['certify'], g['INV']
invariants, same_fingerprint, fmt = g['invariants'], g['same_fingerprint'], g['fmt']
Ty, char_subspace, w_to_x = g['Ty'], g['char_subspace'], g['w_to_x']
from scipy.optimize import minimize

RES = []


def gate(name, ok):
    RES.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    return bool(ok)


def theta_np(w):
    """v1's time reversal on the coefficients: (Theta w)_j = (-1)^(j+1) conj(w_(6-j))."""
    return np.array([(-1) ** (j + 1) * np.conj(w[6 - j]) for j in range(7)])


# ---------------------------------------------------------------- convention gate (F1)
rng = np.random.default_rng(11)
dev = 0.0
for _ in range(20):
    w = rng.normal(size=7) + 1j * rng.normal(size=7)
    dev = max(dev, np.max(np.abs(theta_np(Dmat([0, 1, 0], np.pi) @ w) + np.conj(w))))
gate(f'Theta o D(R_y(pi)) acts as w -> -conj(w) in these coordinates (max deviation {dev:.1e})', dev < 1e-12)
dev2 = 0.0
for _ in range(20):
    w = rng.normal(size=7) + 1j * rng.normal(size=7)
    R = Dmat([0.3, -0.5, 0.8], 1.1)
    dev2 = max(dev2, np.max(np.abs(theta_np(R @ w) - R @ theta_np(w))))
gate(f'Theta commutes with rotations (max deviation {dev2:.1e})', dev2 < 1e-12)


def defect_anti(w, n):
    return 1 - abs(ipB(w, theta_np(Dmat(n, np.pi) @ w))) / ipB(w, w).real


def unit(v):
    return v / np.linalg.norm(v)


FIB = [(np.arccos(1 - 2 * (i + 0.5) / 1500), np.pi * (1 + 5 ** 0.5) * i) for i in range(1500)]


def sph(t, p):
    return np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])


def find_mirror(w, perp_to=None):
    if perp_to is None:
        cands = sorted((defect_anti(w, sph(*q)), q) for q in FIB)[:8]
        best = None
        for _, q in cands:
            res = minimize(lambda v: defect_anti(w, sph(*v)), np.array(q), method='Nelder-Mead',
                           options={'xatol': 1e-14, 'fatol': 1e-17, 'maxiter': 6000})
            if best is None or res.fun < best[0]:
                best = (res.fun, sph(*res.x))
        return best
    n1 = unit(perp_to)
    e1 = unit(np.cross(n1, [1.0, 0, 0] if abs(n1[0]) < 0.9 else [0, 1.0, 0]))
    e2 = np.cross(n1, e1)
    vec = lambda ph: np.cos(ph) * e1 + np.sin(ph) * e2
    grid = np.linspace(0, np.pi, 1200, endpoint=False)
    cands = sorted((defect_anti(w, vec(p)), p) for p in grid)[:6]
    best = None
    for _, p in cands:
        res = minimize(lambda v: defect_anti(w, vec(v[0])), np.array([p]), method='Nelder-Mead',
                       options={'xatol': 1e-15, 'fatol': 1e-17, 'maxiter': 4000})
        if best is None or res.fun < best[0]:
            best = (res.fun, vec(res.x[0]))
    return best


def upper_bound(w, label):
    full = g['certify_full'](w, f'{label} (full sphere)')
    if not full['ok']:
        return full, None
    pts = g['star_boxes'](full['box'][:7], full['box'][7:14])
    sv = g['rotation_survivors'](pts) if pts is not None else None
    if sv is not None:
        print(f'  {label}: upper bound from the stars: {len(sv["rot"])} unitary + {len(sv["refl"])} antiunitary '
              f'(undecided {len(sv["undecided"])})', flush=True)
    return full, sv


def d2d_basis(vr):
    """Exact joint fixed set for a D2d-type group in the frame z = the C2 axis inside the mirror, y = the mirror
    normal: C2 about z, C2 about the diagonal (1, 1, 0)/sqrt2 (Gaussian-rational matrix
    (Ud w)_k = -(-i)^(k-3) w_(6-k)), and the antiunitary Theta R_y(pi) = -conj (real vectors). Characters are read
    from the aligned state and snapped to {1, -1, i, -i}; the fixed set is the exact rational null space."""
    import sympy as sp_
    Uz = [[(-1) ** (k - 3) if i == k else 0 for k in range(7)] for i in range(7)]
    Ud = [[0] * 7 for _ in range(7)]
    for k in range(7):
        Ud[k][6 - k] = -(-sp_.I) ** (k - 3)
    Uzn = np.array(Uz, dtype=complex)
    Udn = np.array([[complex(sp_.N(x)) for x in row] for row in Ud])
    snap = lambda c: min((1, -1, 1j, -1j), key=lambda s: abs(c - s))
    chis = [snap(ipB(vr, M @ vr) / ipB(vr, vr)) for M in (Uzn, Udn)]
    rows = []
    for M, chi in ((Uz, chis[0]), (Ud, chis[1])):
        chi_s = sp_.nsimplify(complex(chi).real) + sp_.I * sp_.nsimplify(complex(chi).imag)
        Mc = sp_.Matrix(M) - chi_s * sp_.eye(7)
        Re, Im = Mc.applyfunc(sp_.re), Mc.applyfunc(sp_.im)
        rows.append(Re.row_join(-Im))
        rows.append(Im.row_join(Re))
    rows.append(sp_.zeros(7, 7).row_join(sp_.eye(7)))          # Im w = 0
    Csys = sp_.Matrix.vstack(*rows)
    ns = Csys.nullspace()
    B = [[Fr(int(sp_.Rational(v[i]).p), int(sp_.Rational(v[i]).q)) for v in ns] for i in range(14)]
    return B, chis


def certify_joint(w, label, k_main=None, dihedral=False, d2d=False):
    """Align (principal axis -> z, mirror normal -> y) and certify inside the joint fixed set."""
    if d2d:
        dm, nm = find_mirror(w)
        _, n1 = find_axis(w, 2, perp_to=nm)
        n1 = unit(n1)
        z_, y_ = n1, unit(nm - np.dot(nm, n1) * n1)
    elif k_main:
        _, n1 = find_axis(w, k_main)
        n1 = unit(n1)
        if dihedral:
            _, n2 = find_axis(w, 2, perp_to=n1)
            nm = unit(np.cross(n1, unit(n2)))
            dm = defect_anti(w, nm)
        else:
            dm, nm = find_mirror(w, perp_to=n1)
        z_, y_ = n1, unit(nm - np.dot(nm, n1) * n1)
    else:
        dm, nm = find_mirror(w)
        y_ = unit(nm)
        z_ = unit(np.cross(y_, [1.0, 0, 0] if abs(y_[0]) < 0.9 else [0, 1.0, 0]))
    x_ = np.cross(y_, z_)
    A = np.array([x_, y_, z_])
    print(f'  {label}: mirror normal found with antiunitary defect {dm:.1e}', flush=True)
    xw = w_to_x(w)
    best = None
    for Acand in (A, A.T):
        xr = mp_rotate(xw, Acand)
        wr = np.array([complex(float(xr[k]), float(xr[7 + k])) for k in range(7)])
        alpha = np.angle(np.sum(wr ** 2 * g['gB'])) / 2
        vr = wr * np.exp(-1j * alpha)
        if d2d:
            Breal, chis_d = d2d_basis(vr)
            m0, chix = chis_d, None
            Bf = np.array([[float(v) for v in row] for row in Breal])
            xf = np.concatenate([vr.real, vr.imag])
            yls, *_ = np.linalg.lstsq(Bf, xf, rcond=None)
            resid = np.linalg.norm(Bf @ yls - xf)
            if best is None or resid < best[0]:
                best = (resid, Breal, vr, m0, chix, Acand)
            continue
        if k_main:
            chi = ipB(vr, Dmat([0, 0, 1], 2 * np.pi / k_main) @ vr) / ipB(vr, vr)
            m0 = int(round(-k_main * np.angle(chi) / (2 * np.pi))) % k_main
            chix = None
            if dihedral:
                cx = ipB(vr, g['Rxf'] @ vr) / ipB(vr, vr)
                chix = 1 if cx.real > 0 else -1
            Bc = char_subspace(k_main, m0, chix)
        else:
            m0, chix = None, None
            Bc = char_subspace(1, 0, None)
        Breal = [[row[c] for c in range(0, len(row), 2)] for row in Bc]
        if not Breal[0]:
            continue
        Bf = np.array([[float(v) for v in row] for row in Breal])
        xf = np.concatenate([vr.real, vr.imag])
        yls, *_ = np.linalg.lstsq(Bf, xf, rcond=None)
        resid = np.linalg.norm(Bf @ yls - xf)
        if best is None or resid < best[0]:
            best = (resid, Breal, vr, m0, chix, Acand)
    resid, Breal, vr, m0, chix, Aused = best
    print(f'  {label}: aligned state lies in the joint fixed set to residual {resid:.1e}', flush=True)
    if resid > 1e-5:
        return None
    Bmp = mp.matrix([[mp.mpf(v.numerator) / v.denominator for v in row] for row in Breal])
    xv = mp.matrix([mp.mpf(float(t)) for t in np.concatenate([vr.real, vr.imag])])
    y0 = mp.lu_solve(Bmp.T * Bmp, Bmp.T * xv)
    y0 = [y0[i] for i in range(len(Breal[0]))]
    slices = [] if (k_main or d2d) else [Ty]
    S = CritSystem(Breal, slices, y0)
    xx = S.xof(y0, mp)
    r0, N0 = INV(xx, mp)[:2]
    z, res = newton(S, y0 + [2 * r0 / N0 ** 2] + [0] * len(slices))
    out = certify(S, z)
    unitary_order = 4 if d2d else ((2 * k_main if dihedral else k_main) if k_main else 1)
    out.update(order=2 * unitary_order, m0=m0, chix=chix, S=S, z=z, dim=S.d)
    if out['ok']:
        xbox = S.xof(out['box'][:S.d], iv)
        out['inv'] = invariants(xbox)
        vc = np.array([complex(float(z[k] if k < S.d else 0), 0) for k in range(7)])
        xc = S.xof(z[:S.d], mp)
        wc = np.array([complex(float(xc[k]), float(xc[7 + k])) for k in range(7)])
        lift = np.max(np.abs(theta_np(Dmat([0, 1, 0], np.pi) @ wc) + wc))
        chis = []
        if d2d:
            chis.append(f'C2 about z: {m0[0]}, C2 about (1, 1, 0)/sqrt2: {m0[1]}')
        elif k_main:
            chis.append(f'C{k_main} about z: e^(-2 pi i {m0}/{k_main})')
            if dihedral:
                chis.append(f'C2 about x: {chix}')
        print(f'  {label}: CERTIFIED in the joint fixed set (real dimension {S.d}, slices {len(slices)}) at radius '
              f'{out["rho"]}; 924 r6 in {fmt(out["inv"]["v924"])}; generated group of order {2 * unitary_order}; '
              f'phase lifts: {", ".join(chis) if chis else "no unitary part"}; '
              f'Theta D(R_y(pi)) w = -w to {lift:.1e}', flush=True)
        # the coherent state and the hexagon, in this frame, fixed by every element of the group?
        e6 = np.zeros(7, dtype=complex); e6[6] = 1.0
        hexa = np.zeros(7, dtype=complex); hexa[0] = hexa[6] = 1 / np.sqrt(2)
        elems = [lambda v: v]
        if k_main:
            Uz = Dmat([0, 0, 1], 2 * np.pi / k_main)
            elems = [lambda v, p=p: np.linalg.matrix_power(Uz, p) @ v for p in range(k_main)]
            if dihedral:
                elems = elems + [lambda v, p=p: g['Rxf'] @ (np.linalg.matrix_power(Uz, p) @ v) for p in range(k_main)]
        anti = [lambda v, f=f: theta_np(Dmat([0, 1, 0], np.pi) @ f(v)) for f in elems]
        def fixed(v, f):
            u = f(v)
            return abs(abs(ipB(v, u)) - 1) < 1e-12
        out['extremes_fixed'] = all(fixed(v, f) for v in (e6, hexa) for f in elems + anti)
    else:
        print(f'  {label}: NOT CERTIFIED in the joint fixed set (smallest singular value {mp.nstr(out["smin"], 6)})',
              flush=True)
    return out


# ---------------------------------------------------------------- part 1: controls, arm, targets
seeds = g['seeds']
SPEC = {'pyramid': (5, False), 'prism': (3, True), 'D2ray': (2, 'd2d'),
        'T1': (2, False), 'T2': (None, False), 'T3': (2, False)}
results = {}
print('\npart 1: controls first')
for name in ('pyramid', 'prism', 'D2ray', 'T1', 'T2', 'T3'):
    if name == 'T1':
        print('\npart 1: targets')
    k, dih = SPEC[name]
    w = seeds[('r4', name)]
    full, sv = upper_bound(w, name)
    joint = certify_joint(w, name, k, dihedral=(dih is True), d2d=(dih == 'd2d'))
    ub = None if sv is None else len(sv['rot']) + len(sv['refl'])
    ok = (full['ok'] and sv is not None and not sv['undecided'] and joint is not None and joint['ok']
          and joint['order'] == ub and len(sv['rot']) == joint['order'] // 2
          and same_fingerprint(full['inv'], joint['inv']))
    results[name] = dict(full=full, sv=sv, joint=joint, ok=ok)
    kind = 'control' if name in ('pyramid', 'prism', 'D2ray') else 'target'
    gate(f'{kind} {name}: isotropy certified exactly, order {ub} '
         f'({len(sv["rot"]) if sv else "?"} unitary, {len(sv["refl"]) if sv else "?"} antiunitary); fingerprints agree',
         ok)
    if name == 'D2ray':
        # the arm: the displaced pyramid of work item 4 has no mirror
        pc = results['pyramid']['full']['z']
        rng2 = np.random.default_rng(20260922)
        delta = rng2.normal(size=14)
        delta /= np.linalg.norm(delta)
        xp = [pc[i] + mp.mpf(float(1e-6 * delta[i])) for i in range(14)]
        Np = INV(xp, mp)[1]
        wp = np.array([complex(float(xp[kk] / mp.sqrt(Np)), float(xp[7 + kk] / mp.sqrt(Np))) for kk in range(7)])
        dmin, _ = find_mirror(wp)
        gate(f'arm: the displaced pyramid admits no antiunitary element (smallest defect {dmin:.1e} > 1e-14)',
             dmin > 1e-14)

gate('F2: in every certified fixed set, the coherent state and the hexagon are fixed by every element',
     all(results[n]['joint'] and results[n]['joint'].get('extremes_fixed') for n in ('T1', 'T2', 'T3')))

# ---------------------------------------------------------------- part 2: [KU]'s Table II at the point
print('\npart 2: [KU] Table II at (c_gamma, c_alpha, c_beta) = (1, -32, -12)')
cg_, ca, cb = Fr(1), Fr(-32), Fr(-12)
Gd_ = ca * cb - 4 * cb * cg_ + 3 * cg_ ** 2
etaG = (5 * cb - 6 * cg_) * (ca - 4 * cg_) / (8 * Gd_)
xiG = cb * (2 * ca - 3 * cg_) / (4 * Gd_)
Rd = 12 * cg_ ** 2 - cg_ * cb - ca * cb
etaR = cg_ * (108 * cg_ - 12 * ca - 25 * cb) / (9 * Rd)
etaJ = 2 * cb / (12 * cg_ - cb)
print(f'  G: eta = {etaG}, xi = {xiG}, 1 - eta - xi = {1 - etaG - xiG}')
print(f'  R: eta = {etaR}')
print(f'  J: eta = {etaJ}, amplitudes squared ({(1 + etaJ) / 4}, {(3 - etaJ) / 4}) on m = 3 and m = -1')
gate('G does not exist at the point (its a_pm need the square root of 1 - eta - xi < 0)', 1 - etaG - xiG < 0)
gate('R does not exist at the point (its sqrt(eta) has eta < 0)', etaR < 0)
gate('J reduces to the weight state m = -1 (state P, 924 r6 = 225) at the point', etaJ == -1)
TABLE_UNITARY = {'FF': 'SO(2)', 'F': 'SO(2)', 'P': 'SO(2)', 'Q': 'D_inf', 'D': 'O', 'A': 'D6', 'H': 'C5', 'J': 'C4',
                 'E': 'D3', 'I': 'C3', 'R': 'C3', 'B': 'D2', 'G': 'C2', 'C': 'C2'}
print(f'  unitary part of each row\'s isotropy group (read from Table II): {TABLE_UNITARY}')
gate('every row of Table II has a nontrivial unitary part, so none has T2\'s isotropy type',
     all(v != '1' for v in TABLE_UNITARY.values()))
for name in ('T1', 'T3'):
    j = results[name]['joint']
    gate(f'{name}\'s certified isotropy is of state C\'s type: e^(i pi) C2z on odd m, with an antiunitary '
         f'C2 T about a perpendicular axis', j is not None and j['ok'] and j['m0'] == 1 and j['order'] == 4)

print('\nsummary')
for name in ('T1', 'T2', 'T3'):
    r = results[name]
    sv, j = r['sv'], r['joint']
    print(f'  {name}: isotropy order {len(sv["rot"]) + len(sv["refl"])} ({len(sv["rot"])} unitary + '
          f'{len(sv["refl"])} antiunitary), {"exact" if r["ok"] else "not certified exactly"}; joint-set 924 r6 in '
          f'{fmt(j["inv"]["v924"], 20) if j and j["ok"] else "n/a"}')
n_fail = sum(1 for _, ok in RES if not ok)
print('ALL PASS' if n_fail == 0 else f'{n_fail} FAILED')
