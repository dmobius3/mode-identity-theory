#!/usr/bin/env python3
"""The plumbing pass's claims (DRIVER_PLAN.md v2, The development runs in this step, 3). Case: dryrun.

Usage: score_plumbing.py

Read after `driver.py --dry --cutoffs 12 16 20`, from its outputs in run/dry/plumbing/. The pass runs M8.16.1's loop on
the GO controls of run/DRY.json at cutoffs the registered run never uses, so nothing it reads is scored: it records any
stop and continues, so every code path runs. Nothing is solved here.

Claims, derived before the run:
  1. No exception: the run's log ends with its verdict and transcript written, each equal to the SHA-256 it records.
  2. Every case of DRY.json, in its order, completed, with each output equal to the SHA-256 the log records.
  3. The gate record is written and logged, with the pyramid absent and the instrument's record incomplete.
  4. The verdict reads incomplete.
Arm: with one case's output changed in a temporary copy of the outputs, claim 2 fails there.
"""
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from instrument import devtools  # noqa: E402

OUT = os.path.join(HERE, 'dry', 'plumbing')
lines = []


def say(s=''):
    print(s, flush=True)
    lines.append(s)


def safe(name):
    return name.replace('/', '_').replace(':', '_')


def claims(outdir):
    log = json.load(open(os.path.join(outdir, 'RUNLOG.json'), encoding='utf-8'))
    order = json.load(open(os.path.join(HERE, 'DRY.json'), encoding='utf-8'))['order']
    same = lambda rec: rec and devtools.sha256(os.path.join(outdir, rec['file'])) == rec['sha256']  # noqa: E731
    c1 = bool(same(log.get('verdict')) and same(log.get('transcript'))
              and log['events'][-1]['event'].endswith('and transcript written'))
    done = list(log['completed'])
    c2 = done == order and all(devtools.sha256(os.path.join(outdir, f)) == h for r in log['completed'].values()
                               for f, h in r['files'].items()) and all(f'{safe(n)}.json' in log['completed'][n]['files']
                                                                       for n in order)
    gate = json.load(open(os.path.join(outdir, 'GATE.json'), encoding='utf-8'))
    c3 = bool(same(log.get('gate')) and 'P5' in gate['absent'] and gate['complete'] is False)
    v = json.load(open(os.path.join(outdir, 'VERDICT.json'), encoding='utf-8'))
    c4 = v['verdict'] == 'incomplete'
    return [c1, c2, c3, c4], dict(done=done, absent=gate['absent'], verdict=v['verdict'], stop=gate.get('stop'))


def main():
    devtools.require('dryrun')
    say("The plumbing pass's claims (DRIVER_PLAN.md v2), read from run/dry/plumbing/; nothing solved.")
    got, info = claims(OUT)
    for i, (ok, what) in enumerate(zip(got, ('no exception: the verdict and transcript written and logged',
                                             'every case of DRY.json completed, each output as logged',
                                             'the gate record written, the pyramid absent, the record incomplete',
                                             'the verdict incomplete')), 1):
        say(f"{i}. {'PASS' if ok else 'FAIL'}: {what}")
    say(f'   the cases {info["done"]}; absent {info["absent"]}; the gate\'s stop {info["stop"]!r}; the verdict '
        f'{info["verdict"]!r}')
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        dest = os.path.join(tmp, 'plumbing')
        shutil.copytree(OUT, dest)
        with open(os.path.join(dest, 'C2b.json'), 'a', encoding='utf-8') as f:
            f.write('\n')
        arm = claims(dest)[0][1] is False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    say(f"arm: C2b's output changed in a temporary copy: claim 2 {'fails (RED)' if arm else 'still holds (GREEN)'}")
    failed = sum(not x for x in got) + (not arm)
    say(f'{failed} failed')
    with open(os.path.join(HERE, 'score_plumbing.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
