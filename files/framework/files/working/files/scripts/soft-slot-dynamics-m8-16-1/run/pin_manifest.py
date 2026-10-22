#!/usr/bin/env python3
"""Pin the manifest at the freeze (DRIVER_PLAN.md v2, item 1, UB): write run/MANIFEST_PIN once, by exclusive create,
with the SHA-256 of devtools.manifest(). The pin lies outside what it pins, and is copied into the freeze block.

Usage: pin_manifest.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import devtools  # noqa: E402


def pin(root):
    text, h = devtools.manifest(root)
    with open(os.path.join(root, 'run', 'MANIFEST_PIN'), 'x', encoding='utf-8') as f:
        f.write(h + '\n')
    return text, h


if __name__ == '__main__':
    text, h = pin(ROOT)
    print(text, end='')
    print('pinned', h)
