#!/usr/bin/env python3
"""M8.17's resume check, run before every launch of run/census.py, the first included, from the run's folder:

    python3 -I -B ../resume_check/resume_check.py . && python3 -I -B -u run/census.py

It reads run/out/ and writes nothing. It passes a first launch, with run/out/ absent or empty, and a resume whose log can
go on. It refuses, with exit status 1, on any sign that the run has stopped or that its outputs cannot be read as logged:
  - log stop:       the run's log records a stop;
  - run complete:   the log records the run's record, so the run has completed;
  - STOP.json:      a STOP.json anywhere under run/out/, interrupted/ included;
  - stop field:     a JSON file anywhere under run/out/ carrying a stop;
  - failed gate:    a JSON file anywhere under run/out/ whose reproduction gate failed at a point;
  - completed file: a completed job's file missing, or not at the SHA-256 the log records;
  - no log:         run/out/ holding files but no RUNLOG.json;
  - unreadable:     RUNLOG.json, or a completed job's file, that does not parse.
A file that does not parse and that no completed job names is reported, not refused (UB): an interruption inside a
write leaves one, and the resume rules census.py inherits from M8.16.1 recover from it. resume() moves a job's partial
file to interrupted/, and the job is computed again; a CENSUS.json the log does not yet record is written again.

Why (reading note 5 of #662's approval): census.py saves a locator job as completed before it saves the run's stop, and
a resume loads a completed job without reading its stop field; resume() also moves a STOP.json the log does not record
into interrupted/. This check closes that gap from outside the frozen tree. A refusal is reported from the files as they
are: nothing is repaired, and the run is not resumed.

Usage: resume_check.py FOLDER
"""
import hashlib
import json
import os
import sys

CHECKS = ('log stop', 'run complete', 'STOP.json', 'stop field', 'failed gate', 'completed file', 'no log', 'unreadable')


def sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def inspect(folder, skip=()):
    """(lines, refusals) for FOLDER's run/out/. Each refusal names its check; a check named in skip is not applied,
    which only the tests' mutants use."""
    out = os.path.join(folder, 'run', 'out')
    lines, refusals = [], []

    def refuse(check, why):
        assert check in CHECKS, check
        if check not in skip:
            refusals.append(f'{check}: {why}')

    if not os.path.isdir(out):
        return ['run/out/ does not exist: a first launch'], []
    files = sorted(os.path.relpath(os.path.join(r, f), out) for r, _, fs in os.walk(out) for f in fs)
    if not files:
        return ['run/out/ is empty: a first launch'], []
    log = None
    if 'RUNLOG.json' not in files:
        refuse('no log', 'run/out/ holds files but no RUNLOG.json')
    else:
        try:
            log = load(os.path.join(out, 'RUNLOG.json'))
        except (OSError, ValueError) as e:
            refuse('unreadable', f'RUNLOG.json does not parse ({e.__class__.__name__})')
    if isinstance(log, dict):
        if log.get('stop'):
            s = log['stop']
            refuse('log stop', f"the log records a stop: {s.get('why') if isinstance(s, dict) else s}")
        if log.get('census'):
            refuse('run complete', "the log records the run's record: the run has completed")
        completed = log.get('completed', {})
        for name, c in sorted(completed.items()):
            for fname, h in sorted(c.get('files', {}).items()):
                p = os.path.join(out, fname)
                if not os.path.isfile(p):
                    refuse('completed file', f'{name}: {fname} is missing')
                elif sha256(p) != h:
                    refuse('completed file', f'{name}: {fname} is not at the SHA-256 the log records')
        lines.append(f"the log: {len(completed)} completed jobs, {len(log.get('events', []))} events")
    elif log is not None:
        refuse('unreadable', 'RUNLOG.json is not a JSON object')
    logged = ({fname for c in log.get('completed', {}).values() for fname in c.get('files', {})}
              if isinstance(log, dict) else set())
    for f in files:
        if os.path.basename(f) == 'STOP.json':
            refuse('STOP.json', f'{f} exists')
        if not f.endswith('.json') or f == 'RUNLOG.json':
            continue
        try:
            obj = load(os.path.join(out, f))
        except (OSError, ValueError) as e:
            if f in logged:
                refuse('unreadable', f'{f} does not parse ({e.__class__.__name__})')
            else:
                lines.append(f'{f} does not parse ({e.__class__.__name__}), and no completed job names it: '
                             + ('the relaunch writes the record again' if f == 'CENSUS.json' else
                                'an earlier resume moved it aside' if f.startswith('interrupted' + os.sep) else
                                "resume() moves it to interrupted/, and its job is computed again, as M8.16.1's "
                                'resume rules do'))
            continue
        if not isinstance(obj, dict):
            continue
        if obj.get('stop'):
            refuse('stop field', f"{f} carries a stop: {obj['stop']}")
        gate = obj.get('gate')
        if isinstance(gate, dict) and gate.get('failed'):
            refuse('failed gate', f"{f}: its reproduction gate failed at {gate['failed']}")
    lines.append(f'run/out/: {len(files)} files')
    return lines, refusals


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    lines, refusals = inspect(sys.argv[1])
    for line in lines:
        print(line)
    for r in refusals:
        print('refused, ' + r)
    print('resume check: ' + ('REFUSED; census.py is not launched, and the run is not resumed' if refusals else 'PASS'))
    sys.exit(1 if refusals else 0)


if __name__ == '__main__':
    main()
