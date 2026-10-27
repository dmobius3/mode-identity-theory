#!/usr/bin/env python3
"""The files this task copies byte for byte, from MIT's git objects at their named commits (M8.17's terms: THE
INSTRUMENT, THE RULE AND THE CUTOFFS: UNCHANGED, and FROZEN VALUES: WHAT IS NEW).

Usage: copy_from_mit.py MIT_REPO

For each file it reads the blob at its commit and path. A file absent here is written by exclusive create; a file
present must equal the blob, byte for byte. Each copy is then checked against the record that pins it, and the script
refuses on the first mismatch:
  - the instrument and M8.16.1's run code, at d1c0ec8, the commit the terms name: each equals its blob at 292b158, the
    run's record, and the SHA-256 that commit's SHA256SUMS lists for it;
  - M8.16.1's outputs, at 292b158: each equals the SHA-256 its run's log, run/out/RUNLOG.json, records, and the log
    equals the SHA-256 SHA256SUMS lists;
  - M8.15's adjudicated readings, as copied in M8.16.1's reference/m815_targets/: each equals the SHA-256 M8.16.1's
    FROZEN.json records, and FROZEN.json the SHA-256 SHA256SUMS lists;
  - M8.16.1's filed terms, its run/m8_16_task_details.md: the SHA-256 its FROZEN.json records, 47,420 bytes;
  - M8.16's outputs, at 87fc643, for test 3's exact comparison: each against M8.16's run log, as above;
  - amendment 5's ladder, at 292b158, for test 3's categorical comparison: against its own run log, as above;
  - M8.15.2's T3/R5 record, at f1ebda7, for the location the terms keep: against the SHA-256 its RECORD.md's table of
    outputs lists, since its SHA256SUMS does not list it.
It then writes reference/SOURCES.json, by exclusive create, or checks that the one present is the same text. Nothing
else is written. No file is solved, opened as a point, or read beyond its bytes and the pins above.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
P = 'files/framework/files/working/files/scripts'
M1, M0, M2 = f'{P}/soft-slot-dynamics-m8-16-1', f'{P}/soft-slot-dynamics-m8-16', f'{P}/soft-slot-dynamics-m8-15-2'
CODE_AT, RECORD_AT, M816_AT, M8152_AT = 'd1c0ec8', '292b158', '87fc643', 'f1ebda7'
INSTRUMENT = ['__init__.py', 'basis.py', 'branches.py', 'certified.py', 'convergence.py', 'devtools.py',
              'functional.py', 'group2i.py', 'linear.py', 'newton.py', 'quadrature.py', 'su2.py']
RUN_CODE = ['cases.py', 'seeds.py', 'driver.py', 'checks.py', 'next_order_values.json', 'pin_manifest.py',
            'record_environment.py']
ROWS = ['T1_R4', 'T1_R5', 'T4_R4', 'T4_R5', 'T2_R4', 'T2_R5', 'T3_R4', 'T3_R5', 'T5_R2']
CONTROLS = ['C1', 'C2a', 'C2b', 'C3', 'C2a_R5', 'P5']
TARGETS = ['T2_R4', 'T2_R5', 'T3_R4', 'T3_R5', 'T5_R2']


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
            for c in (CODE_AT, RECORD_AT, M816_AT, M8152_AT)}
    s1, s0 = sums(repo, RECORD_AT, M1), sums(repo, M816_AT, M0)
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
    # M8.16.1's outputs, against its run's log
    log1 = json.loads(take('reference/m8_16_1/run/out/RUNLOG.json', RECORD_AT, f'{M1}/run/out/RUNLOG.json',
                           f'SHA256SUMS at {RECORD_AT}', s1['run/out/RUNLOG.json']))
    logged1 = {f: h for c in log1['completed'].values() for f, h in c['files'].items()}
    for n in ROWS + CONTROLS:
        take(f'reference/m8_16_1/run/out/{n}.json', RECORD_AT, f'{M1}/run/out/{n}.json',
             "M8.16.1's run/out/RUNLOG.json", logged1[f'{n}.json'])
    # M8.15's adjudicated readings, as M8.16.1 copied them, against its FROZEN.json
    frozen1 = json.loads(take('reference/m8_16_1/run/FROZEN.json', RECORD_AT, f'{M1}/run/FROZEN.json',
                              f'SHA256SUMS at {RECORD_AT}', s1['run/FROZEN.json']))
    tsha = {t['file']: t['sha256'] for t in frozen1['targets']}
    terms1 = take('reference/m8_16_1/run/m8_16_task_details.md', RECORD_AT, f'{M1}/run/m8_16_task_details.md',
                  "M8.16.1's run/FROZEN.json", frozen1['terms_sha256'])
    if len(terms1) != 47420:
        stop(f"M8.16.1's filed terms are {len(terms1)} bytes, not 47,420")
    for n in TARGETS:
        rel = f'reference/m815_targets/branch_{n}.json'
        take(rel, RECORD_AT, f'{M1}/{rel}', "M8.16.1's run/FROZEN.json", tsha[rel])
    # M8.16's outputs, against its run's log
    log0 = json.loads(take('reference/m8_16/run/out/RUNLOG.json', M816_AT, f'{M0}/run/out/RUNLOG.json',
                           f'SHA256SUMS at {M816_AT}', s0['run/out/RUNLOG.json']))
    logged0 = {f: h for c in log0['completed'].values() for f, h in c['files'].items()}
    for n in CONTROLS:
        take(f'reference/m8_16/run/out/{n}.json', M816_AT, f'{M0}/run/out/{n}.json', "M8.16's run/out/RUNLOG.json",
             logged0[f'{n}.json'])
    # amendment 5's ladder, against its own run log
    lad = 'dev/runs/015_ladder'
    logl = json.loads(take(f'reference/m8_16_1/{lad}/RUNLOG.json', RECORD_AT, f'{M1}/{lad}/RUNLOG.json',
                           f'SHA256SUMS at {RECORD_AT}', s1[f'{lad}/RUNLOG.json']))
    take(f'reference/m8_16_1/{lad}/C2a_R5_ladder.json', RECORD_AT, f'{M1}/{lad}/C2a_R5_ladder.json',
         "the ladder's RUNLOG.json", logl['completed']['C2a/R5:ladder']['files']['C2a_R5_ladder.json'])
    # M8.15.2's T3/R5 record, against its RECORD.md's table of outputs
    _, rec2 = blob(repo, M8152_AT, f'{M2}/RECORD.md')
    pin2 = re.findall(r'^\s*\| `out/t1_T3_R5\.json` \| `([0-9a-f]{64})` \|', rec2.decode('utf-8'), re.M)
    if len(pin2) != 1:
        stop(f"M8.15.2's RECORD.md lists out/t1_T3_R5.json {len(pin2)} times")
    take('reference/m8_15_2/out/t1_T3_R5.json', M8152_AT, f'{M2}/out/t1_T3_R5.json', f"M8.15.2's RECORD.md at "
         f'{M8152_AT}', pin2[0])
    text = json.dumps(dict(commits=full, files=entries), indent=1) + '\n'
    print(f"{len(entries)} files: {done['written']} written, {done['present']} already present and equal")
    print('SOURCES.json', place('reference/SOURCES.json', text.encode('utf-8')))


if __name__ == '__main__':
    main()
