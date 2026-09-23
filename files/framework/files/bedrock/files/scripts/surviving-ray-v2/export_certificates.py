#!/usr/bin/env python3
"""Export the three outside-orbit certificates of Section 7.2 as data, for the published reproduction layer.

Local and one-off: it needs the exploratory census files, which are not published. The definitions of
certify_inertia.py (everything before its seeds section) are executed verbatim, and through them those of
certify_isotropy.py and certify_outside_orbits.py, exactly as one_certificate_rows.py executes them, and each of
T1, T2, T3 is certified once in the fixed set of its full isotropy, at the radii one_certificate_rows.py uses.

For each orbit the data file records what a verifier needs and nothing about how the point was found: the fixed
set (the unitary group's character and the antiunitary element, as certify_isotropy.py specifies them), the slice
generators, the box centre (the point's coordinates in that fixed set, the Lagrange multiplier and the slice
multipliers, recorded to 64 significant digits) and the radius. The run then checks that its value enclosures are
the ones one_certificate_rows_log.txt prints, so the exported boxes are the ones Section 7.2's table rests on.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'certify_inertia.py'
LOG = HERE / 'one_certificate_rows_log.txt'
OUT = HERE / 'sr_v2_certificates.json'
print(f'script {Path(__file__).name}: SHA-256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}')
print(f'definitions from {SRC.name}: SHA-256 {hashlib.sha256(SRC.read_bytes()).hexdigest()}')
print(f'input {LOG.name}: SHA-256 {hashlib.sha256(LOG.read_bytes()).hexdigest()}')
text = SRC.read_text(encoding='utf-8')
marker = '# ---------------------------------------------------------------- seeds: add the octahedron and the hexagon'
assert text.count(marker) == 1
ns = {'__file__': str(SRC), '__name__': 'inertia_defs'}
exec(compile(text.split(marker)[0], str(SRC), 'exec'), ns)
print('--- export ---')
h, g = ns['h'], ns['g']
mp, iv = g['mp'], g['iv']
RADII = ('1e-55', '1e-50', '1e-45', '1e-40', '1e-30')
base_certify = g['certify']
h['certify'] = lambda S, z: base_certify(S, z, radii=RADII)      # as one_certificate_rows.py does
NAMES = {id(g['T0']): 'T0', id(g['Tx']): 'Tx', id(g['Ty']): 'Ty', id(g['Tz']): 'Tz'}

RES = []


def gate(name, ok):
    RES.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    return bool(ok)


logtext = LOG.read_text(encoding='utf-8')
seeds = g['seeds']
SPEC = {'T1': 2, 'T2': None, 'T3': 2}
data = {'about': 'Certified critical points of r6 = ||rho_6||^2 on the unit sphere of V_3, Surviving Ray v2, Section '
                 '7.2: for each outside orbit, its fixed set, slices, box centre and radius. Coordinates: '
                 'the 14 real numbers (Re w_0..Re w_6, Im w_0..Im w_6) of the binary sextic P_u = sum w_k x^k y^(6-k), '
                 'Bombieri metric, as in the verifier.',
        'orbits': {}}
for name, k in SPEC.items():
    j = h['certify_joint'](seeds[('r4', name)], f'{name} (isotropy fixed set)', k, dihedral=False, d2d=False)
    ok = j is not None and j['ok']
    gate(f'{name}: certified in the fixed set of its full isotropy at radius {j["rho"] if j else None}', ok)
    if not ok:
        continue
    S, z = j['S'], j['z']
    v = g['invariants'](S.xof(j['box'][:S.d], iv))['v924']
    lo, hi = mp.nstr(mp.mpf(v.a), 55), mp.nstr(mp.mpf(v.b), 55)
    m = re.search(rf'^  {name}: 924 r6 in \[([0-9.]+), ([0-9.]+)\]', logtext, re.M)
    gate(f'{name}: the value enclosure is the one one_certificate_rows_log.txt prints', m is not None and
         (m.group(1), m.group(2)) == (lo, hi))
    data['orbits'][name] = {
        'fixed_set': ({'unitary': 'C2 about z', 'character_m0': j['m0'],
                       'antiunitary': 'Theta R_y(pi), acting as w -> -conj(w): real vectors'} if k == 2 else
                      {'unitary': 'none', 'antiunitary': 'Theta R_y(pi), acting as w -> -conj(w): real vectors'}),
        'isotropy_order': j['order'],
        'basis_14xd': [[str(q) for q in row] for row in S.B],
        'slices': [NAMES[id(T)] for T in S.T],
        'centre': [mp.nstr(t, 64) for t in z],
        'centre_layout': f'{S.d} fixed-set coordinates, then the Lagrange multiplier mu, then {len(S.T)} slice '
                         f'multiplier(s)',
        'radius': j['rho'],
        'value_924_r6_enclosure_as_run': [lo, hi],
    }
    print(f'  {name}: exported (fixed-set dimension {S.d}, slices {data["orbits"][name]["slices"]}, radius '
          f'{j["rho"]})', flush=True)

body = json.dumps(data, indent=1) + '\n'
OUT.write_text(body, encoding='utf-8')
print(f'wrote {OUT.name}: SHA-256 {hashlib.sha256(body.encode()).hexdigest()}')
print('ALL PASS' if all(RES) and len(RES) == 6 else 'SOME FAILED')
