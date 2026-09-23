#!/usr/bin/env python3
"""Supplement to work items 4, 4b and 4c (F2's redline on Sections 7.1 and 7.2, 2026-09-22): every entry of a row of
Section 7.2's second table computed at ONE certified point. Not part of any frozen packet.

In the 4c run a row joined up to three certificates by fingerprint (full sphere, isotropy fixed set, complex C2
subspace). Here each outside orbit is certified once, inside the fixed set of its full isotropy group, and at that
single box: the isotropy from both sides (the stars of this box above, the fixed set below), the value enclosure,
and the three signatures (full transverse, on the isotropy fixed set, on the complex C2 fixed set). A critical point
of r6 in a fixed set is critical on the whole sphere by symmetric criticality, with the same Lagrange multiplier, so
the full bordered second variation may be evaluated over this box.

Controls: the pyramid, prism and D2 ray, certified the same way in their own fixed sets, must give M8.12's exact full
signatures (5, 0, 4), (3, 0, 6), (5, 0, 4), and on their fixed sets (1, 0, 0), (0, 0, 1), (0, 0, 1): the pyramid is the
maximum of r6 on its C5 line (an exact downward parabola), the prism and the D2 ray the minima on their lines.
Arms, each on a green parent: dropping -2 mu G changes the pyramid's full signature; without slice columns the full
bordered matrix at T1's point is not certified; T1's fixed set is not inside the even-weight C2 subspace.
Cross-check, not load-bearing: the invariants agree with work item 4's full-sphere certificates.
The definitions of certify_inertia.py (everything before its seeds section) are executed verbatim, and through them
those of certify_isotropy.py and certify_outside_orbits.py.
"""
import hashlib
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'certify_inertia.py'
print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
print(f'definitions from {SRC.name}: SHA-256 {hashlib.sha256(SRC.read_bytes()).hexdigest()}')
text = SRC.read_text(encoding='utf-8')
marker = '# ---------------------------------------------------------------- seeds: add the octahedron and the hexagon'
assert text.count(marker) == 1
ns = {'__file__': str(SRC), '__name__': 'inertia_defs'}
exec(compile(text.split(marker)[0], str(SRC), 'exec'), ns)
print('--- supplement ---')
h, g = ns['h'], ns['g']
mp, iv = g['mp'], g['iv']
inertia = ns['inertia']
CritSystem, char_subspace, invariants = g['CritSystem'], g['char_subspace'], g['invariants']
T0, Tx, Ty, Tz = g['T0'], g['Tx'], g['Ty'], g['Tz']
RADII = ('1e-55', '1e-50', '1e-45', '1e-40', '1e-30')
base_certify = g['certify']
h['certify'] = lambda S, z: base_certify(S, z, radii=RADII)      # certify_joint resolves this name at call time

RES = []


def gate(name, ok):
    RES.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    return bool(ok)


def exact(x):
    m, e = mp.mpf(x).man_exp
    return Fr(int(m)) * (Fr(2) ** int(e))


def full_at(j, drop_mu=False, with_slices=True):
    """The full transverse signature at the joint-set certificate j, over its own box."""
    S, z, box = j['S'], j['z'], j['box']
    d = S.d
    xc = S.xof(z[:d], mp)
    xb = S.xof(box[:d], iv)
    Sf = CritSystem(None, [T0, Tx, Ty, Tz], xc)
    return inertia(Sf, xc + [z[d]], xb + [box[d]], drop_mu=drop_mu, with_slices=with_slices)


def c2_at(j, m0):
    """The signature on the complex C2 fixed set of character m0, at the joint-set certificate j, over its own box.
    Returns (signature, whether the joint set's columns are columns of that subspace's basis)."""
    S, z, box = j['S'], j['z'], j['box']
    d = S.d
    Bc = char_subspace(2, m0, None)
    inside = all(all(S.B[i][c] == Bc[i][2 * c] for i in range(14)) for c in range(d)) and len(Bc[0]) == 2 * d
    if not inside:
        return None, False
    yc = []
    yb = []
    for c in range(d):
        yc += [z[c], mp.mpf(0)]
        yb += [box[c], iv.mpf(0)]
    Sc = CritSystem(Bc, [T0, Tz], yc)
    return inertia(Sc, yc + [z[d]], yb + [box[d]]), True


def stars_order(j):
    xb = j['S'].xof(j['box'][:j['S'].d], iv)
    pts = g['star_boxes'](xb[:7], xb[7:14])
    sv = g['rotation_survivors'](pts) if pts is not None else None
    if sv is None or sv['undecided']:
        return None
    return len(sv['rot']), len(sv['refl'])


seeds = g['seeds']
SPEC = {'pyramid': (5, False, False), 'prism': (3, True, False), 'D2ray': (2, False, True),
        'T1': (2, False, False), 'T2': (None, False, False), 'T3': (2, False, False)}
EXPECT_FULL = {'pyramid': (5, 0, 4), 'prism': (3, 0, 6), 'D2ray': (5, 0, 4)}
EXPECT_JOINT = {'pyramid': (1, 0, 0), 'prism': (0, 0, 1), 'D2ray': (0, 0, 1)}
CERT4C = {'T1': ((4, 0, 5), (1, 0, 2), (2, 0, 3)), 'T2': ((6, 0, 3), (4, 0, 1), None),
          'T3': ((7, 0, 2), (2, 0, 1), (3, 0, 2))}
J = {}

print('\ncontrols')
for name in ('pyramid', 'prism', 'D2ray'):
    k, dih, d2d = SPEC[name]
    j = h['certify_joint'](seeds[('r4', name)], name, k, dihedral=dih, d2d=d2d)
    J[name] = j
    so = stars_order(j) if j and j['ok'] else None
    sf = full_at(j) if j and j['ok'] else None
    sj = inertia(j['S'], j['z'], j['box']) if j and j['ok'] else None
    print(f'  {name}: radius {j["rho"] if j else None}; stars {so}; full {sf}; on its fixed set {sj}', flush=True)
    gate(f'control {name}: isotropy of order {j["order"] if j else "?"} from the stars of this one box',
         so is not None and sum(so) == j['order'] and so[0] == j['order'] // 2)
    gate(f'control {name}: full signature at the fixed-set point equals M8.12\'s exact {EXPECT_FULL[name]}',
         sf == EXPECT_FULL[name])
    gate(f'control {name}: signature on its fixed set is {EXPECT_JOINT[name]}, its line extremum', sj == EXPECT_JOINT[name])

print('\narms (each on a green parent)')
parent = full_at(J['pyramid']) == EXPECT_FULL['pyramid']
arm1 = full_at(J['pyramid'], drop_mu=True) if parent else None
gate(f'arm: without -2 mu G the pyramid\'s full signature changes (to {arm1})', parent and arm1 is not None
     and arm1 != EXPECT_FULL['pyramid'])

print('\ntargets')
rows = {}
for name in ('T1', 'T2', 'T3'):
    k, dih, d2d = SPEC[name]
    j = h['certify_joint'](seeds[('r4', name)], f'{name} (isotropy fixed set)', k, dihedral=dih, d2d=d2d)
    J[name] = j
    ok = j is not None and j['ok']
    gate(f'{name}: certified in the fixed set of its full isotropy at radius {j["rho"] if j else None} (below 1e-50)',
         ok and mp.mpf(j['rho']) < mp.mpf('1e-50'))
    if not ok:
        continue
    so = stars_order(j)
    gate(f'{name}: isotropy of order {j["order"]} from the stars of this one box ({so})',
         so is not None and sum(so) == j['order'] and so[0] == j['order'] // 2)
    sf, sj = full_at(j), inertia(j['S'], j['z'], j['box'])
    sc = None
    if k == 2:
        sc, inside = c2_at(j, j['m0'])
        gate(f'{name}: its fixed set lies inside the complex C2 subspace of character m0 = {j["m0"]}', inside)
    v = invariants(j['S'].xof(j['box'][:j['S'].d], iv))['v924']
    lo, hi = exact(v.a), exact(v.b)
    width = mp.mpf(v.b) - mp.mpf(v.a)
    rows[name] = dict(full=sf, joint=sj, c2=sc, lo=lo, hi=hi, width=width)
    print(f'  {name}: 924 r6 in [{mp.nstr(mp.mpf(v.a), 55)}, {mp.nstr(mp.mpf(v.b), 55)}], width {mp.nstr(width, 3)}; '
          f'signatures: full {sf}, on the isotropy fixed set {sj}' + (f', on the C2 fixed set {sc}' if k == 2 else ''),
          flush=True)
    dj = j['S'].d - 1 - len(j['S'].T)
    gate(f'{name}: all signatures certified, with dimensions 9, {dj}' + (', 5' if k == 2 else ''),
         sf is not None and sum(sf) == 9 and sj is not None and sum(sj) == dj
         and (k != 2 or (sc is not None and sum(sc) == 5)))
    gate(f'{name}: the counts nest (fixed set within C2 set within full)',
         sf is not None and sj is not None and sj[0] <= (sc or sf)[0] <= sf[0] and sj[2] <= (sc or sf)[2] <= sf[2])
    gate(f'{name}: the one-point signatures equal 4c\'s separately certified ones {CERT4C[name]}',
         (sf, sj, sc) == CERT4C[name])
    gate(f'{name}: the value enclosure is narrower than 1e-45', width < mp.mpf('1e-45'))

if 'T1' in J and J['T1']['ok']:
    parent = rows.get('T1', {}).get('full') == CERT4C['T1'][0]
    arm2 = full_at(J['T1'], with_slices=False) if parent else 'parent red'
    gate('arm: without its slice columns the full bordered matrix at T1\'s point is not certified', parent and arm2 is None)
    parent_c2 = rows.get('T1', {}).get('c2') == CERT4C['T1'][2]
    _, inside_even = c2_at(J['T1'], 1 - J['T1']['m0'])
    gate('arm: T1\'s fixed set does not lie inside the complex C2 subspace of the other character',
         parent_c2 and not inside_even)

if 'T2' in rows:
    q = Fr(28800, 121)
    lo, hi = rows['T2']['lo'], rows['T2']['hi']
    gate('T2: 28800/121 lies in the value enclosure of this certificate', lo <= q <= hi)
    for label, p in (('28801/121', Fr(28801, 121)), ('28800/121 + 1e-40', q + Fr(1, 10 ** 40)),
                     ('28800/121 - 1e-40', q - Fr(1, 10 ** 40))):
        gate(f'arm: {label} lies outside it', not (lo <= p <= hi))

print('\ncross-check, not load-bearing: work item 4\'s full-sphere certificates carry the same invariants')
for name in ('T1', 'T2', 'T3'):
    if name not in J or not J[name]['ok']:
        continue
    full = g['certify_full'](seeds[('r4', name)], f'{name} (work item 4 route, full sphere)')
    ij = invariants(J[name]['S'].xof(J[name]['box'][:J[name]['S'].d], iv))
    print(f'  {name}: invariants overlap: {full["ok"] and g["same_fingerprint"](full["inv"], ij)}')
print('\nsummary: one certified point per row')
for name, r in rows.items():
    print(f'  {name}: full {r["full"]}; isotropy fixed set {r["joint"]}; C2 fixed set {r["c2"]}; value width '
          f'{mp.nstr(r["width"], 3)}')
print('ALL PASS' if all(RES) else 'SOME FAILED')
