#!/usr/bin/env python3
"""The freeze, written once after the maintainer's go (M8.16's DRIVER_PLAN.md v2, item 2; M8.15.2's write_guard
pattern), with M8.16.1's additions (M8.16.1's DRIVER_PLAN.md v2, item 6).

Usage: write_guard.py MIT_REPO GO_LINK

Before it runs, run/m8_16_task_details.md is the filed terms, byte for byte, and run/MANIFEST_PIN holds the manifest's
SHA-256 (pin_manifest.py). It refuses if run/FROZEN.json or run/FROZEN_PIN exists, if no go is given, or if the
manifest differs from run/MANIFEST_PIN. It copies each target record named in run/targets.json from MIT_REPO at its
commit into reference/m815_targets/, refusing unless its git blob id matches the named one (UB). Then it writes
run/FROZEN.json and, after it, run/FROZEN_PIN, its SHA-256 (UA), each by exclusive create.

FROZEN.json holds the allowlist and the seventeen cases (cases.py), each case the next-order bar reads with its
values; the frozen values of both terms' FROZEN VALUES, D's cut and K3's axis guard among them, with the new
constants; the pinned values file's SHA-256 and its cases section's, with its environment; the terms' and the
manifest's SHA-256, the go, and each target record's SHA-256. Before any of that is written, the values file is
checked: its cases section hashes to the SHA-256 it records, every check it records holds, A to F and X, each multiple
group's correction is scalar, and its inventory equals cases.py's. The functions take a root, so the guard's tests run
them on temporary trees.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools, linear as ln, convergence as cv  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402


def frozen_values():
    """Every item of both terms' FROZEN VALUES that the code reads: M8.16's, with D's cut and K3's axis guard, which
    M8.16's file omitted (its RECORD.md, section 5); M8.16.1's new constants; and the constants of M8.16's that M8.16.1's
    terms bring into FROZEN VALUES: K2's slow band, the band-edge guard's half, K3's orthonormal cut, K6's agreement at
    eps <= 2, and C1's four bounds. The nominal weights are the code's own, computed at the nominal points.
    test_constants.py checks each against the code and the terms."""
    w = ck.lagrange0(list(ck.NEXT_EPS))
    return dict(calibration=dict(kappa=ln.KAPPA, m0=ln.M0, G=ln.GRAY, kappa_d=ln.KAPPA_D, kappa_L=ln.KAPPA_L,
                                 leak_cap=ln.LEAK_CAP, L_cut_over_u=ln.L_CUT / ln.U, G_L=ln.G_L, D_cut=1e-8, u=ln.U),
                solve=dict(accept_rel=1e-15, halving=1e-8, secant=1e-6, secant_iterations=8, seed_check=1e-12),
                checks=dict(bar=cs.BAR, overlap_xy=0.9, overlap_z=0.1, identity=ck.IDENTITY, axis=ck.AXIS_MIN,
                            factor=cv.FACTOR, span=cv.SPAN_MIN, left=cv.LEFT_MAX / ln.U, conditioning=cv.COND_MAX * ln.U,
                            idempotence=cv.IDEM_MAX, slow_band=2, band_edge=0.5, orthonormal=1e-6, k6_eps=2),
                next_order=dict(points=list(ck.NEXT_EPS), ceiling=list(ck.CEILING), resolution=ck.RESOLUTION,
                                floor=ck.FLOOR, nominal_weights=[abs(wi) / x ** 2 for wi, x in zip(w, ck.NEXT_EPS)]),
                cutoffs=cs.CUTOFFS, c1=dict(eps=cs.C1_EPS, cutoffs=cs.C1_CUTOFFS, residual=1e-15, off_level=1e-14,
                                            spectrum=1e-10, along=1e-12), sample=cs.SAMPLE)


def next_order_values(root):
    """The pinned values file, checked before FROZEN.json is written (DRIVER_PLAN.md v2, item 6); returns what
    FROZEN.json records of it. It refuses unless its cases section hashes to the SHA-256 it records, every check it
    records holds (A to F and X, and its run's E and F), each multiple group's correction is scalar, its groups tie to
    the frozen cases through cases.py's own loader, which refuses groups that change order across the cutoffs and bar
    memberships other than the registered ones (UA), and its inventory, by case, cutoff and group (class, Krein sign,
    multiplicity, bar membership), equals cases.py's."""
    path = os.path.join(root, 'run', 'next_order_values.json')
    with open(path, 'rb') as f:
        raw = f.read()
    V = json.loads(raw.decode('utf-8'))
    csha = hashlib.sha256(json.dumps(V['cases'], sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=False).encode('utf-8')).hexdigest()
    if csha != V.get('cases_sha256'):
        raise PermissionError('the values file\'s cases section differs from the SHA-256 it records')
    bad = [f'{n}: {k}' for n, c in V['cases'].items() for k, ok in c['checks'].items() if not ok]
    if bad or V['checks'].get('failed') or not (V['checks'].get('E') and V['checks'].get('F')):
        raise PermissionError(f"the values file records a failed check: {bad or V['checks']}")
    if [g for c in V['cases'].values() for x in c['cutoffs'].values() for g in x['groups'] if g['mult'] > 1
            and not g['scalar']]:
        raise PermissionError("the values file records a multiple group whose correction is not scalar")
    if sorted(V['cases']) != sorted(cs.BAR_CASES):
        raise PermissionError(f"the values file's cases {sorted(V['cases'])} are not the bar's")
    try:
        mine = {n: cs._next_order(n, cs.CASES[n], V) for n in cs.BAR_CASES}
    except (ValueError, KeyError) as e:
        raise PermissionError(f'the values file does not tie to the frozen cases: {e}')
    inv = lambda gs: [(g['cls'], g['krein'], g['mult'], g['under_bar']) for g in gs]  # noqa: E731
    want = {n: {N: inv(x) for N, x in cs.CASES[n]['next_order'].items()} for n in cs.BAR_CASES}
    have = {n: {N: inv(x) for N, x in mine[n].items()} for n in cs.BAR_CASES}
    if have != want:
        raise PermissionError("the values file's inventory differs from cases.py's")
    return dict(file='run/next_order_values.json', sha256=hashlib.sha256(raw).hexdigest(), cases_sha256=csha,
                script=V['script'], environment=V['environment'])


def copy_targets(root, repo):
    with open(os.path.join(root, 'run', 'targets.json'), encoding='utf-8') as f:
        named = json.load(f)['records']
    out = []
    os.makedirs(os.path.join(root, 'reference', 'm815_targets'), exist_ok=True)
    for t in named:
        blob = subprocess.run(['git', '-C', repo, 'rev-parse', f"{t['commit']}:{t['path']}"], check=True,
                              capture_output=True, text=True).stdout.strip()
        if blob != t['blob']:
            raise PermissionError(f"{t['name']}: blob {blob} differs from the named {t['blob']}")
        raw = subprocess.run(['git', '-C', repo, 'cat-file', '-p', t['blob']], check=True, capture_output=True).stdout
        dest = os.path.join(root, t['file'])
        with open(dest, 'xb') as f:
            f.write(raw)
        out.append(dict(t, sha256=hashlib.sha256(raw).hexdigest()))
    return out


def write(root, repo, go):
    run = os.path.join(root, 'run')
    for p in ('FROZEN.json', 'FROZEN_PIN'):
        if os.path.exists(os.path.join(run, p)):
            raise PermissionError(f'run/{p} exists: the freeze is written once')
    if not go:
        raise PermissionError('no go')
    _, msha = devtools.manifest(root)
    mpin = os.path.join(run, 'MANIFEST_PIN')
    if not os.path.exists(mpin) or open(mpin, encoding='utf-8').read().strip() != msha:
        raise PermissionError('the manifest differs from run/MANIFEST_PIN')
    terms = os.path.join(run, 'm8_16_task_details.md')
    if not os.path.exists(terms):
        raise PermissionError('the filed terms are not in run/')
    values = next_order_values(root)
    targets = copy_targets(root, repo)
    F = dict(allowlist=list(cs.ORDER), order=list(cs.ORDER),
             cases={n: cs.serialize(n, cs.CASES[n]) for n in cs.ORDER}, values=frozen_values(), next_order=values,
             terms_sha256=devtools.sha256(terms), manifest_sha256=msha, go=go, targets=targets,
             written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
    text = json.dumps(F, indent=1) + '\n'
    with open(os.path.join(run, 'FROZEN.json'), 'x', encoding='utf-8') as f:
        f.write(text)
    with open(os.path.join(run, 'FROZEN_PIN'), 'x', encoding='utf-8') as f:
        f.write(hashlib.sha256(text.encode('utf-8')).hexdigest() + '\n')
    return F


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    F = write(ROOT, sys.argv[1], sys.argv[2])
    print('FROZEN.json written; pin', open(os.path.join(HERE, 'FROZEN_PIN')).read().strip())
