#!/usr/bin/env python3
"""Name M8.15's target-row records by MIT commit, path and git blob id, as git ls-tree lists them, without opening
them (DRIVER_PLAN.md v2, item 5: they are sealed with their rows until the freeze, UB). Writes run/targets.json once.

Usage: name_targets.py MIT_REPO
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = 'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_solver/out'
NAMES = ['T2_R4', 'T2_R5', 'T3_R4', 'T3_R5', 'T5_R2']


def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], check=True, capture_output=True, text=True).stdout.strip()


def main():
    repo = sys.argv[1]
    git(repo, 'fetch', '-q', 'origin')
    out = []
    for n in NAMES:
        path = f'{DIR}/branch_{n}.json'
        commit = git(repo, 'log', '-1', '--format=%H', 'origin/main', '--', path)
        ls = git(repo, 'ls-tree', commit, path).split()
        assert len(ls) == 4 and ls[1] == 'blob' and ls[3] == path, ls
        out.append(dict(name=n, path=path, commit=commit, blob=ls[2],
                        file=f'reference/m815_targets/branch_{n}.json'))
    text = json.dumps(dict(source='mode-identity-theory', records=out), indent=1) + '\n'
    dest = os.path.join(HERE, 'targets.json')
    with open(dest, 'x', encoding='utf-8') as f:
        f.write(text)
    print('written', dest, [(r['name'], r['commit'][:7], r['blob'][:12]) for r in out])


if __name__ == '__main__':
    main()
