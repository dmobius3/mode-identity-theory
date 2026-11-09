"""Two bench runs' records, job by job: every JSON leaf exactly, and every .npy and .npz array byte for byte.

  compare_runs.py RUNDIR_A RUNDIR_B JOB [JOB ...]

Prints, for each file in each named job's folder, the number of differing leaves and each one, so that a time or a
memory peak can be told from anything else; console.log is left out. Used in DEVLOG.md, entry 9, for the rerun on the
final code against the dry run."""
import json
import os
import sys

import numpy as np

A, B = sys.argv[1], sys.argv[2]
jobs = sys.argv[3:]


def diff(a, b, path=''):
    out = []
    if type(a) != type(b):
        return [(path, a, b)]
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append((f'{path}/{k}', a.get(k, '<absent>'), b.get(k, '<absent>')))
            else:
                out += diff(a[k], b[k], f'{path}/{k}')
    elif isinstance(a, list):
        if len(a) != len(b):
            return [(path, f'{len(a)} entries', f'{len(b)} entries')]
        for i, (u, v) in enumerate(zip(a, b)):
            out += diff(u, v, f'{path}[{i}]')
    elif a != b:
        out.append((path, a, b))
    return out


for j in jobs:
    fa, fb = os.path.join(A, j), os.path.join(B, j)
    names = sorted(set(os.listdir(fa)) | set(os.listdir(fb)))
    for n in names:
        if n in ('console.log',):
            continue
        pa, pb = os.path.join(fa, n), os.path.join(fb, n)
        if not os.path.exists(pa) or not os.path.exists(pb):
            print(f'{j}/{n}: only in', 'B' if not os.path.exists(pa) else 'A')
            continue
        if n.endswith('.json'):
            d = diff(json.load(open(pa)), json.load(open(pb)))
            print(f'{j}/{n}: {len(d)} differing leaves')
            for p, u, v in d[:40]:
                print(f'    {p}: {str(u)[:90]} | {str(v)[:90]}')
        elif n.endswith('.npy'):
            u, v = np.load(pa), np.load(pb)
            print(f'{j}/{n}: shape {u.shape} vs {v.shape}, bytes equal {u.shape == v.shape and u.dtype == v.dtype and u.tobytes() == v.tobytes()}')
        elif n.endswith('.npz'):
            u, v = np.load(pa), np.load(pb)
            ks = sorted(set(u.files) | set(v.files))
            bad = [k for k in ks if k not in u.files or k not in v.files or u[k].dtype != v[k].dtype or u[k].shape != v[k].shape or u[k].tobytes() != v[k].tobytes()]
            print(f'{j}/{n}: {len(ks)} arrays, differing {bad}')
        else:
            print(f'{j}/{n}: not compared')
