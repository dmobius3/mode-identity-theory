#!/usr/bin/env python3
"""MIT's pin of this folder (DESIGN.md): run/MANIFEST_PIN, and the run/FROZEN.json and run/FROZEN_PIN that
instrument/devtools.py reads to admit a sealed seed. Unlike M8.18's, they are written again at each change: this is
MIT's own manifest, not an OpenWave freeze, and it answers to nothing but the tree it hashes.

Usage: pin.py
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import devtools  # noqa: E402
import grid  # noqa: E402


def main():
    text, h = devtools.manifest(ROOT)
    terms = devtools.sha256(os.path.join(ROOT, 'run', 'm8_16_task_details.md'))
    F = dict(note="MIT's own manifest; no OpenWave freeze", allowlist=grid.allowlist(), manifest_sha256=h,
             terms_sha256=terms, targets=[])
    raw = json.dumps(F, indent=1, sort_keys=True).encode('utf-8')
    with open(os.path.join(ROOT, 'run', 'FROZEN.json'), 'wb') as f:
        f.write(raw)
    with open(os.path.join(ROOT, 'run', 'FROZEN_PIN'), 'w', encoding='utf-8') as f:
        f.write(hashlib.sha256(raw).hexdigest() + '\n')
    with open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), 'w', encoding='utf-8') as f:
        f.write(h + '\n')
    devtools.frozen(ROOT)
    print(text, end='')
    print('pinned', h)


if __name__ == '__main__':
    main()
