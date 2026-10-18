#!/usr/bin/env python3
"""The freeze, written once after the maintainer's go (DRIVER_PLAN.md v2, item 2; M8.15.2's write_guard pattern).

Usage: write_guard.py MIT_REPO GO_LINK

Before it runs, run/m8_16_task_details.md is the filed terms, byte for byte, and run/MANIFEST_PIN holds the manifest's
SHA-256 (pin_manifest.py). It refuses if run/FROZEN.json or run/FROZEN_PIN exists, if no go is given, or if the
manifest differs from run/MANIFEST_PIN. It copies each target record named in run/targets.json from MIT_REPO at its
commit into reference/m815_targets/, refusing unless its git blob id matches the named one (UB). Then it writes
run/FROZEN.json and, after it, run/FROZEN_PIN, its SHA-256 (UA), each by exclusive create.

FROZEN.json holds the allowlist and every case (cases.py), the frozen values, the terms' and the manifest's SHA-256,
the go, and each target record's SHA-256. The functions take a root, so the guard's tests run them on temporary trees.
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


def frozen_values():
    return dict(calibration=dict(kappa=ln.KAPPA, m0=ln.M0, G=ln.GRAY, kappa_d=ln.KAPPA_D, kappa_L=ln.KAPPA_L,
                                 leak_cap=ln.LEAK_CAP, L_cut_over_u=ln.L_CUT / ln.U, G_L=ln.G_L, u=ln.U),
                solve=dict(accept_rel=1e-15, halving=1e-8, secant=1e-6, secant_iterations=8, seed_check=1e-12),
                checks=dict(bar=cs.BAR, overlap_xy=0.9, overlap_z=0.1, identity=1e-2, factor=cv.FACTOR,
                            span=cv.SPAN_MIN, left=cv.LEFT_MAX / ln.U, conditioning=cv.COND_MAX * ln.U,
                            idempotence=cv.IDEM_MAX),
                cutoffs=cs.CUTOFFS, c1=dict(eps=cs.C1_EPS, cutoffs=cs.C1_CUTOFFS), sample=cs.SAMPLE)


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
    targets = copy_targets(root, repo)
    F = dict(allowlist=list(cs.ORDER), order=list(cs.ORDER),
             cases={n: cs.serialize(n, cs.CASES[n]) for n in cs.ORDER}, values=frozen_values(),
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
