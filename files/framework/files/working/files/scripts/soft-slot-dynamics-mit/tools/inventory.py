#!/usr/bin/env python3
"""The folder's SHA256SUMS, in M8.18's form, and the checks before a commit: one line per file but itself, sorted by path;
no cache in the tree; the manifest equal to run/MANIFEST_PIN; the pin's admission valid; every file listed once and
shasum -c passing. A job's outputs under run/out are listed like any other file.

Usage: inventory.py [--write]
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import devtools  # noqa: E402


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def sums(root):
    files = []
    for r, ds, fs in os.walk(root):
        for x in ds + fs:
            if x in ('__pycache__', '.DS_Store'):
                raise SystemExit(f'a cache or .DS_Store is in the tree: {os.path.join(r, x)}')
        files += [os.path.relpath(os.path.join(r, f), root) for f in fs]
    files = sorted(f for f in files if f != 'SHA256SUMS')
    return ''.join(f'{sha(os.path.join(root, f))}  {f}\n' for f in files), files


def main():
    text, files = sums(ROOT)
    path = os.path.join(ROOT, 'SHA256SUMS')
    print(f'{len(files)} files')
    pin = open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8').read().strip()
    ok = devtools.manifest(ROOT)[1] == pin and bool(devtools.frozen(ROOT))
    print(f"{'ok  ' if ok else 'FAIL'} the manifest equals run/MANIFEST_PIN, {pin}, and the admission is valid")
    if '--write' in sys.argv[1:]:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        c = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=ROOT, capture_output=True, text=True)
        good = c.returncode == 0 and sum(x.endswith(': OK') for x in c.stdout.splitlines()) == len(files)
        print(f"{'ok  ' if good else 'FAIL'} shasum -c: {sum(x.endswith(': OK') for x in c.stdout.splitlines())} OK")
        ok &= good
        print(f'SHA256SUMS {sha(path)}')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
