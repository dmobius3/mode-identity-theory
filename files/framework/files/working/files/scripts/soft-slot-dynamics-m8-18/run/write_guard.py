#!/usr/bin/env python3
"""The freeze, written once after the maintainer's go (M8.18's terms: THE FREEZE, THE GUARD AND THE RUN, inherited from
M8.17's, with new pins).

Usage: write_guard.py GO_LINK

Before it runs: run/m8_16_task_details.md holds M8.18's filed terms, byte for byte, since devtools.frozen() reads the
terms at that path, which the instrument fixes, as M8.16.1's terms placed theirs; run/MANIFEST_PIN holds the manifest's
SHA-256 (pin_manifest.py); and reference/ holds what tools/copy_from_mit.py placed, as reference/SOURCES.json lists it.
It refuses if run/FROZEN.json or run/FROZEN_PIN exists, if no go is given, if the manifest differs from its pin, if
run/m8_16_task_details.md differs from registration/m8_18_task_details.md, or if a reference file differs from
SOURCES.json. Then it writes run/FROZEN.json and, after it, run/FROZEN_PIN, its SHA-256, each by exclusive create.

FROZEN.json holds the allowlist and the order, census_lib.RUN_ORDER; each case, M8.16.1's serialized, with this task's
points and ladder; this task's frozen values (census_lib.frozen_values); M8.16.1's frozen values and pinned next-order
record, as its FROZEN.json holds them, inherited unchanged; the terms' and the manifest's SHA-256; the go; and the
targets, every reference file with its SHA-256. build() takes a root and writes nothing, so the tests run it on this
tree.
"""
import datetime
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402


def targets(root):
    """Every reference file SOURCES.json lists, each checked on disk against its SHA-256."""
    src = lib.load_json(os.path.join(root, 'reference', 'SOURCES.json'))
    out = []
    for s in src['files']:
        if not s['file'].startswith('reference/'):
            continue
        path = os.path.join(root, s['file'])
        if not os.path.exists(path) or devtools.sha256(path) != s['sha256']:
            raise PermissionError(f"{s['file']} differs from reference/SOURCES.json")
        out.append(dict(name=s['file'], file=s['file'], sha256=s['sha256'], commit=s['commit'],
                        path=s['path'], blob=s['blob']))
    sp = os.path.join(root, 'reference', 'SOURCES.json')
    out.append(dict(name='SOURCES.json', file='reference/SOURCES.json', sha256=devtools.sha256(sp)))
    return out


def build(root, go):
    """FROZEN.json's content, written nowhere."""
    f161 = lib.load_json(os.path.join(root, 'reference', 'm8_16_1', 'run', 'FROZEN.json'))
    terms = os.path.join(root, 'run', 'm8_16_task_details.md')
    return dict(allowlist=list(lib.RUN_ORDER), order=list(lib.RUN_ORDER),
                cases={n: json.loads(json.dumps(dr.jsonable(cs.serialize(n, dict(cs.CASES[n], points=lib.path_points(n),
                                                                                   cutoffs=lib.cutoffs_of(n))))))
                       for n in lib.RUN_ORDER},
                census=json.loads(json.dumps(lib.frozen_values())),
                inherited=dict(values=f161['values'], next_order=f161['next_order'], terms_sha256=f161['terms_sha256'],
                               manifest_sha256=f161['manifest_sha256'], go=f161['go']),
                terms_sha256=devtools.sha256(terms) if os.path.exists(terms) else None,
                manifest_sha256=devtools.manifest(root)[1], go=go, targets=targets(root),
                written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))


def write(root, go):
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
    terms, filed = os.path.join(run, 'm8_16_task_details.md'), os.path.join(root, 'registration', 'm8_18_task_details.md')
    if not os.path.exists(terms) or devtools.sha256(terms) != devtools.sha256(filed):
        raise PermissionError('run/m8_16_task_details.md differs from registration/m8_18_task_details.md')
    F = build(root, go)
    text = json.dumps(F, indent=1) + '\n'
    with open(os.path.join(run, 'FROZEN.json'), 'x', encoding='utf-8') as f:
        f.write(text)
    with open(os.path.join(run, 'FROZEN_PIN'), 'x', encoding='utf-8') as f:
        f.write(hashlib.sha256(text.encode('utf-8')).hexdigest() + '\n')
    return F


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    write(ROOT, sys.argv[1])
    print('FROZEN.json written; pin', open(os.path.join(HERE, 'FROZEN_PIN')).read().strip())
