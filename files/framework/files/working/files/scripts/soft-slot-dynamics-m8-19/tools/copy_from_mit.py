#!/usr/bin/env python3
"""The records M8.19's driver reads, copied byte for byte from MIT's git objects at their record commits, as M8.18's
tools/copy_from_mit.py copied them (DESIGN.md, Layout).

Usage: copy_from_mit.py MIT_REPO

  - M8.17's readings of T1 and T4 in both slots (adjudicated on #676), at 7b66f8a: each equals the SHA-256 its run's
    log, run/out/RUNLOG.json, records, and the log equals the SHA-256 that commit's SHA256SUMS lists;
  - M8.16.1's controls C2a and C2a/R5 (adjudicated on #653), at 292b158, pinned the same way by its run's log.
A file absent here is written by exclusive create; a file present must equal its blob. reference/SOURCES.json is then
written by exclusive create, or checked equal. Nothing else is written, and no file is read beyond its bytes."""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
P = 'files/framework/files/working/files/scripts'
M1, M7 = f'{P}/soft-slot-dynamics-m8-16-1', f'{P}/soft-slot-dynamics-m8-17'
M1_AT, M7_AT = '292b158', '7b66f8a'
FILES = [('m8_17', M7, M7_AT, ['T1_R4', 'T1_R5', 'T4_R4', 'T4_R5']), ('m8_16_1', M1, M1_AT, ['C2a', 'C2a_R5'])]


def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], check=True, capture_output=True).stdout


def stop(m):
    raise SystemExit(f'REFUSED: {m}')


def main():
    repo = sys.argv[1]
    sources = dict(commits={}, files=[])

    def take(dest, commit, path, pinned_by, want):
        full = git(repo, 'rev-parse', commit).decode().strip()
        sources['commits'][commit] = full
        b = git(repo, 'rev-parse', f'{commit}:{path}').decode().strip()
        raw = git(repo, 'cat-file', 'blob', b)
        h = hashlib.sha256(raw).hexdigest()
        if h != want:
            stop(f'{path} at {commit} is not at the SHA-256 {pinned_by} records')
        p = os.path.join(ROOT, dest)
        if os.path.exists(p):
            if open(p, 'rb').read() != raw:
                stop(f'{dest} differs from its source')
        else:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, 'xb') as f:
                f.write(raw)
        sources['files'].append(dict(file=dest, commit=full, path=path, blob=b, sha256=h, pinned_by=pinned_by))
        return raw

    for tag, folder, at, names in FILES:
        sums = {}
        for line in git(repo, 'show', f'{at}:{folder}/SHA256SUMS').decode().splitlines():
            h, pth = line.split('  ', 1)
            sums[pth] = h
        log = json.loads(take(f'reference/{tag}/run/out/RUNLOG.json', at, f'{folder}/run/out/RUNLOG.json',
                              f'SHA256SUMS at {at}', sums['run/out/RUNLOG.json']))
        logged = {f: h for c in log['completed'].values() for f, h in c['files'].items()}
        for n in names:
            take(f'reference/{tag}/run/out/{n}.json', at, f'{folder}/run/out/{n}.json',
                 f"{'M8.17' if tag == 'm8_17' else 'M8.16.1'}'s run/out/RUNLOG.json", logged[f'{n}.json'])
    text = json.dumps(sources, indent=1) + '\n'
    p = os.path.join(ROOT, 'reference', 'SOURCES.json')
    if os.path.exists(p):
        if open(p, encoding='utf-8').read() != text:
            stop('reference/SOURCES.json differs')
    else:
        with open(p, 'x', encoding='utf-8') as f:
            f.write(text)
    print(f'{len(sources["files"])} files, each at its pin; SOURCES.json in place')


if __name__ == '__main__':
    main()
