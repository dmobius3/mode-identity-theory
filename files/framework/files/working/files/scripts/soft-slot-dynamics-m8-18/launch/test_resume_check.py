#!/usr/bin/env python3
"""The resume check's arms: each state of run/out/ a launch can meet, built in a temporary folder, with the verdict and
the checks that must give it; then each check's mutant, the check run without it, which an arm must catch; then the
command line's exit status. The check must leave every file as it was. Writes test_resume_check.out beside it.

Usage: test_resume_check.py
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resume_check as rc  # noqa: E402

ROW, LOC = 'T5_R2_N24.json', 'ARM_B.json'
STOP = 'a midpoint does not reproduce at N = 24: midpoint 3: /lam: 58.1 against 58.2'


def write(root, rel, obj=None, text=None):
    p = os.path.join(root, 'run', 'out', rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text if text is not None else json.dumps(obj, indent=1))
    return p


def row():
    return dict(seed=dict(ok=True), points={}, setup_seconds=1.0)


def gate(passed=False):
    return dict(kernel=dict(C1=[]), control={}, passed=passed, stopped=None if passed else 'the kernel at N = 40: C3: out of memory')


def loc(stop=False):
    rec = dict(bracket=[8.0, 11.313708499], path={}, ends={}, row='T4/R5', moved=dict(fraction=0.4, end='lower'))
    if stop:
        rec['stop'] = STOP
    else:
        rec.update(kind='index', located=True)
    return rec


def logged(root, jobs, stop=False, census=False, skip_files=()):
    """RUNLOG.json over jobs {name: (file, obj)}: each job's file written and logged at its SHA-256."""
    log = dict(manifest_sha256='0' * 64, completed={}, events=[dict(t='t', event='run started')])
    for name, (fname, obj) in jobs.items():
        p = write(root, fname, obj)
        log['completed'][name] = dict(files={fname: rc.sha256(p)}, t='t')
        if fname in skip_files:
            os.remove(p)
    if stop:
        log['stop'] = dict(file='STOP.json', sha256='0' * 64, why=f'reproducibility failure in Arm B: {STOP}')
    if census:
        log['census'] = dict(file='CENSUS.json', sha256='0' * 64, written='t')
    write(root, 'RUNLOG.json', log)


ROWJOB = {'path:T5/R2:24': (ROW, row())}
LOCJOB = {'arm_b': (LOC, loc())}
LOCSTOP = {'arm_b': (LOC, loc(stop=True))}
GATEJOB = {'gate': ('GATE.json', gate())}
STOPFILE = dict(why=f'reproducibility failure in Arm B: {STOP}', detail={}, t='t')


def arm_absent(root):
    pass


def arm_empty(root):
    os.makedirs(os.path.join(root, 'run', 'out'))


def arm_clean(root):
    logged(root, ROWJOB | LOCJOB)
    write(root, 'interrupted/2026-10-27T000000Z/T1_R4_N24.json', row())


def arm_locator_stop_unsaved(root):        # UA's state 1: the job saved with its stop, the log's stop not
    logged(root, ROWJOB | LOCSTOP)


def arm_stop_file_unsaved(root):           # UA's state 2: STOP.json written, the log's stop not saved
    logged(root, ROWJOB | LOCSTOP)
    write(root, 'STOP.json', STOPFILE)


def arm_stop_file_alone(root):
    logged(root, ROWJOB)
    write(root, 'STOP.json', STOPFILE)


def arm_stopped(root):                     # the control: a stop saved as census.py saves it
    logged(root, ROWJOB | LOCSTOP, stop=True)
    write(root, 'STOP.json', STOPFILE)


def arm_log_stop_alone(root):
    logged(root, ROWJOB, stop=True)


def arm_stop_file_moved(root):             # UB's: an unchecked relaunch moved STOP.json to interrupted/
    logged(root, ROWJOB | LOCSTOP)
    write(root, 'interrupted/2026-10-27T000000Z/STOP.json', STOPFILE)


def arm_stop_file_moved_alone(root):
    logged(root, ROWJOB)
    write(root, 'interrupted/2026-10-27T000000Z/STOP.json', STOPFILE)


def arm_partial_locator_stop(root):        # the job's file written, not yet logged as completed
    logged(root, ROWJOB)
    write(root, LOC, loc(stop=True))


def arm_gate_not_passed(root):             # GATE.json logged, not passed: the run goes on from it to its record
    logged(root, ROWJOB | GATEJOB)


def arm_completed_missing(root):
    logged(root, ROWJOB | LOCJOB, skip_files=(LOC,))


def arm_completed_altered(root):
    logged(root, ROWJOB | LOCJOB)
    write(root, LOC, loc() | dict(seconds=1.0))


def arm_completed_truncated(root):
    logged(root, ROWJOB | LOCJOB)
    write(root, LOC, text=json.dumps(loc())[:40])


def arm_log_unreadable(root):
    write(root, ROW, row())
    write(root, 'RUNLOG.json', text='{"completed": {')


def arm_no_log(root):
    write(root, ROW, row())


def arm_complete(root):
    logged(root, ROWJOB | LOCJOB, census=True)
    write(root, 'CENSUS.json', dict(stop=None, rows={}, unclassified={}))


def arm_truncated_unlogged(root):          # UB: an interruption inside complete()'s write, before the log names it
    logged(root, ROWJOB)
    write(root, 'T1_R4_N24.json', text=json.dumps(row())[:30])


def arm_truncated_moved(root):             # UB: that file, moved aside by an earlier relaunch
    logged(root, ROWJOB)
    write(root, 'interrupted/2026-10-27T000000Z/T1_R4_N24.json', text=json.dumps(row())[:30])


def arm_census_truncated(root):            # UB: CENSUS.json cut short before the log records it
    logged(root, ROWJOB | LOCJOB)
    write(root, 'CENSUS.json', text=json.dumps(dict(stop=None, rows={}, unclassified={}))[:20])


ARMS = [  # (name, builder, the checks that must refuse, none for a pass; and a line the check must print, if any)
    ('run/out/ absent, a first launch', arm_absent, set()),
    ('run/out/ empty, a first launch', arm_empty, set()),
    ('a clean resume, with a moved partial', arm_clean, set()),
    ("Arm B's stop saved, the log's not (UA 1)", arm_locator_stop_unsaved, {'stop field'}),
    ("STOP.json written, the log's stop not (UA 2)", arm_stop_file_unsaved, {'STOP.json', 'stop field'}),
    ('STOP.json alone', arm_stop_file_alone, {'STOP.json'}),
    ('a stopped run, the control', arm_stopped, {'log stop', 'STOP.json', 'stop field'}),
    ("the log's stop alone", arm_log_stop_alone, {'log stop'}),
    ('STOP.json moved to interrupted/ (UB)', arm_stop_file_moved, {'STOP.json', 'stop field'}),
    ('STOP.json moved to interrupted/, alone', arm_stop_file_moved_alone, {'STOP.json'}),
    ("Arm B's stop written, not yet logged", arm_partial_locator_stop, {'stop field'}),
    ('a gate record that did not pass', arm_gate_not_passed, set()),
    ("a completed job's file missing", arm_completed_missing, {'completed file'}),
    ("a completed job's file altered", arm_completed_altered, {'completed file'}),
    ("a completed job's file truncated", arm_completed_truncated, {'completed file', 'unreadable'}),
    ('RUNLOG.json truncated', arm_log_unreadable, {'unreadable'}),
    ('files but no RUNLOG.json', arm_no_log, {'no log'}),
    ('the run complete', arm_complete, {'run complete'}),
    ("a job's file truncated, not yet logged (UB)", arm_truncated_unlogged, set(), 'resume() moves it to interrupted/'),
    ('that file, moved to interrupted/ (UB)', arm_truncated_moved, set(), 'an earlier resume moved it aside'),
    ("CENSUS.json truncated, the log's record not saved (UB)", arm_census_truncated, set(),
     'the relaunch writes the record again'),
]


def tree(root):
    out = {}
    for r, _, fs in os.walk(root):
        for f in fs:
            p = os.path.join(r, f)
            out[os.path.relpath(p, root)] = rc.sha256(p)
    return out


def checks_of(refusals):
    return {r.split(':', 1)[0] for r in refusals}


def main():
    lines, failed = [], 0
    tmp = tempfile.mkdtemp(prefix='resume_check_')
    try:
        built = {}
        for i, arm in enumerate(ARMS, 1):
            name, build, want = arm[:3]
            note = arm[3] if len(arm) > 3 else None
            root = os.path.join(tmp, f'arm{i:02d}')
            os.makedirs(root)
            build(root)
            built[name] = root
            before = tree(root)
            said, refusals = rc.inspect(root)
            got = checks_of(refusals)
            same = tree(root) == before
            noted = note is None or any(note in s for s in said)
            ok = got == want and same and noted
            failed += not ok
            verdict = f"REFUSED by {', '.join(sorted(got))}" if got else 'PASS'
            lines.append(f"arm {i:02d}, {name}: {verdict}; the files unchanged: {same}" + ('' if ok else
                         f" <-- FAILED, expected {', '.join(sorted(want)) or 'PASS'}"
                         + ('' if noted else f", with the line '{note}'")))
        for check in rc.CHECKS:
            caught = [arm[0] for arm in ARMS
                      if arm[2] and not checks_of(rc.inspect(built[arm[0]], skip=(check,))[1])]
            ok = bool(caught)
            failed += not ok
            lines.append(f"mutant without '{check}': " + (f"caught by {len(caught)} arm{'s' * (len(caught) > 1)}"
                         if ok else 'NOT CAUGHT <-- FAILED'))
        script = os.path.join(HERE, 'resume_check.py')
        for name, want in (('run/out/ absent, a first launch', 0), ('a clean resume, with a moved partial', 0),
                           ("Arm B's stop saved, the log's not (UA 1)", 1), ('the run complete', 1),
                           ("a job's file truncated, not yet logged (UB)", 0)):
            r = subprocess.run([sys.executable, '-I', '-B', script, built[name]], capture_output=True, text=True)
            ok = r.returncode == want and r.stdout.strip().endswith('PASS' if want == 0 else 'the run is not resumed')
            failed += not ok
            lines.append(f'the command line, {name}: exit {r.returncode}' + ('' if ok else ' <-- FAILED'))
        r = subprocess.run([sys.executable, '-I', '-B', script], capture_output=True, text=True)
        ok = r.returncode != 0 and 'Usage: resume_check.py FOLDER' in (r.stdout + r.stderr)
        failed += not ok
        lines.append(f'the command line, no folder: refused with its usage' + ('' if ok else ' <-- FAILED'))
    finally:
        shutil.rmtree(tmp)
    lines.append(f'{failed} failed')
    text = '\n'.join(lines) + '\n'
    print(text, end='')
    with open(os.path.join(HERE, 'test_resume_check.out'), 'w', encoding='utf-8') as f:
        f.write(text)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
