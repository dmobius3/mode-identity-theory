#!/usr/bin/env python3
"""The files this task copies byte for byte, from MIT's git objects at their named commits (M8.18's terms: THE
INSTRUMENT AND THE LADDERS, and FROZEN VALUES: WHAT IS NEW).

Usage: copy_from_mit.py MIT_REPO

For each file it reads the blob at its commit and path. A file absent here is written by exclusive create; a file
present must equal the blob, byte for byte. Each copy is then checked against the record that pins it, and the script
refuses on the first mismatch:
  - the instrument and M8.16.1's run code, at d1c0ec8, the commit the terms name: each equals its blob at 292b158, the
    run's record, and the SHA-256 that commit's SHA256SUMS lists for it;
  - M8.16.1's outputs of the controls, at 292b158: each equals the SHA-256 its run's log, run/out/RUNLOG.json, records,
    and the log equals the SHA-256 SHA256SUMS lists;
  - M8.16.1's FROZEN.json and filed terms, its run/m8_16_task_details.md: the SHA-256 its FROZEN.json records, 47,420
    bytes;
  - M8.17's outputs of the five rows, its T4/R5 locator file and its CENSUS.json, at 7b66f8a: each equals the SHA-256 its
    run's log records, and the log equals the SHA-256 that commit's SHA256SUMS lists;
  - M8.17's run/census.py and run/census_lib.py, the base of this task's diff, and its filed terms, 27,823 bytes, at
    7b66f8a: each equals the SHA-256 SHA256SUMS lists.
It then writes reference/SOURCES.json, by exclusive create, or checks that the one present is the same text. Nothing
else is written. No file is solved, opened as a point, or read beyond its bytes and the pins above.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
P = 'files/framework/files/working/files/scripts'
M1, M7 = f'{P}/soft-slot-dynamics-m8-16-1', f'{P}/soft-slot-dynamics-m8-17'
CODE_AT, RECORD_AT, M817_AT = 'd1c0ec8', '292b158', '7b66f8a'
INSTRUMENT = ['__init__.py', 'basis.py', 'branches.py', 'certified.py', 'convergence.py', 'devtools.py',
              'functional.py', 'group2i.py', 'linear.py', 'newton.py', 'quadrature.py', 'su2.py']
RUN_CODE = ['cases.py', 'seeds.py', 'driver.py', 'checks.py', 'next_order_values.json', 'pin_manifest.py',
            'record_environment.py']
CONTROLS = ['C1', 'C2a', 'C2b', 'C3', 'C2a_R5', 'P5', 'C3R_R4']
ROWS = ['T1_R4', 'T1_R5', 'T4_R4', 'T4_R5', 'T5_R2']
LOCATED = 'locate_T4_R5_8_11.313708499.json'


def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], check=True, capture_output=True).stdout


def blob(repo, commit, path):
    """(blob id, bytes) of path at commit."""
    b = git(repo, 'rev-parse', f'{commit}:{path}').decode().strip()
    return b, git(repo, 'cat-file', 'blob', b)


def sums(repo, commit, folder):
    """The SHA256SUMS of folder at commit, as {relative path: SHA-256}."""
    _, raw = blob(repo, commit, f'{folder}/SHA256SUMS')
    out = {}
    for line in raw.decode('utf-8').splitlines():
        h, p = line.split('  ', 1)
        out[p] = h
    return out


def stop(m):
    raise SystemExit(f'REFUSED: {m}')


def place(dest, raw):
    """Write raw at dest by exclusive create, or check that the file there equals it."""
    path = os.path.join(ROOT, dest)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            if f.read() != raw:
                stop(f'{dest} differs from its source')
        return 'present'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'xb') as f:
        f.write(raw)
    return 'written'


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    repo = sys.argv[1]
    full = {c: git(repo, 'rev-parse', '--verify', f'{c}^{{commit}}').decode().strip()
            for c in (CODE_AT, RECORD_AT, M817_AT)}
    s1, s7 = sums(repo, RECORD_AT, M1), sums(repo, M817_AT, M7)
    entries, done = [], {'written': 0, 'present': 0}

    def take(dest, commit, path, pinned_by, want=None):
        b, raw = blob(repo, commit, path)
        h = hashlib.sha256(raw).hexdigest()
        if want is not None and h != want:
            stop(f'{dest}: SHA-256 {h} differs from {pinned_by}')
        done[place(dest, raw)] += 1
        entries.append(dict(file=dest, commit=full[commit], path=path, blob=b, sha256=h, pinned_by=pinned_by))
        return raw

    # the instrument and M8.16.1's run code: the commit the terms name, equal to the run's record and its sums
    for sub, names in (('instrument', INSTRUMENT), ('run', RUN_CODE)):
        for n in names:
            rel = f'{sub}/{n}'
            b_code, _ = blob(repo, CODE_AT, f'{M1}/{rel}')
            b_rec, _ = blob(repo, RECORD_AT, f'{M1}/{rel}')
            if b_code != b_rec:
                stop(f'{rel}: its blob at {CODE_AT} differs from the one at {RECORD_AT}')
            take(rel, CODE_AT, f'{M1}/{rel}', f'SHA256SUMS at {RECORD_AT}', s1[rel])
    # M8.16.1's outputs of the controls, against its run's log
    log1 = json.loads(take('reference/m8_16_1/run/out/RUNLOG.json', RECORD_AT, f'{M1}/run/out/RUNLOG.json',
                           f'SHA256SUMS at {RECORD_AT}', s1['run/out/RUNLOG.json']))
    logged1 = {f: h for c in log1['completed'].values() for f, h in c['files'].items()}
    for n in CONTROLS:
        take(f'reference/m8_16_1/run/out/{n}.json', RECORD_AT, f'{M1}/run/out/{n}.json',
             "M8.16.1's run/out/RUNLOG.json", logged1[f'{n}.json'])
    frozen1 = json.loads(take('reference/m8_16_1/run/FROZEN.json', RECORD_AT, f'{M1}/run/FROZEN.json',
                              f'SHA256SUMS at {RECORD_AT}', s1['run/FROZEN.json']))
    terms1 = take('reference/m8_16_1/run/m8_16_task_details.md', RECORD_AT, f'{M1}/run/m8_16_task_details.md',
                  "M8.16.1's run/FROZEN.json", frozen1['terms_sha256'])
    if len(terms1) != 47420:
        stop(f"M8.16.1's filed terms are {len(terms1)} bytes, not 47,420")
    # M8.17's outputs, against its run's log
    log7 = json.loads(take('reference/m8_17/run/out/RUNLOG.json', M817_AT, f'{M7}/run/out/RUNLOG.json',
                           f'SHA256SUMS at {M817_AT}', s7['run/out/RUNLOG.json']))
    logged7 = {f: h for c in log7['completed'].values() for f, h in c['files'].items()}
    for n in ROWS:
        take(f'reference/m8_17/run/out/{n}.json', M817_AT, f'{M7}/run/out/{n}.json', "M8.17's run/out/RUNLOG.json",
             logged7[f'{n}.json'])
    take(f'reference/m8_17/run/out/{LOCATED}', M817_AT, f'{M7}/run/out/{LOCATED}', "M8.17's run/out/RUNLOG.json",
         logged7[LOCATED])
    take('reference/m8_17/run/out/CENSUS.json', M817_AT, f'{M7}/run/out/CENSUS.json', "M8.17's run/out/RUNLOG.json",
         log7['census']['sha256'])
    # M8.17's census code, the base of this task's diff, and its filed terms
    for n in ('census.py', 'census_lib.py'):
        take(f'reference/m8_17/run/{n}', M817_AT, f'{M7}/run/{n}', f'SHA256SUMS at {M817_AT}', s7[f'run/{n}'])
    terms7 = take('reference/m8_17/run/m8_16_task_details.md', M817_AT, f'{M7}/run/m8_16_task_details.md',
                  f'SHA256SUMS at {M817_AT}', s7['run/m8_16_task_details.md'])
    if len(terms7) != 27823:
        stop(f"M8.17's filed terms are {len(terms7)} bytes, not 27,823")
    text = json.dumps(dict(commits=full, files=entries), indent=1) + '\n'
    print(f"{len(entries)} files: {done['written']} written, {done['present']} already present and equal")
    print('SOURCES.json', place('reference/SOURCES.json', text.encode('utf-8')))


if __name__ == '__main__':
    main()
