#!/usr/bin/env python3
"""The launch command's form, run in zsh on stubs: a stub resume check and a stub census.py in a temporary folder laid
out as the run's is, the command's text taken from FILING_PLAN.md's step 3. It must keep each step's exit status
through tee, put the hash check, the resume check's verdict and the run's output in the console log, start census.py
only after both checks pass, and append on a relaunch. The two forms the review replaced are run as well, to show what
they lost. Writes test_launch_wrapper.out beside it.

Usage: test_launch_wrapper.py
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(os.path.dirname(HERE), 'FILING_PLAN.md')
CHAIN = ("printf '%s  %s\\n' {sha} ../resume_check/resume_check.py | shasum -a 256 -c - && "
         "python3 -I -B ../resume_check/resume_check.py . && python3 -I -B -u run/census.py")
LAUNCH = 'set -o pipefail; caffeinate -i -m -s -w $$ & { ' + CHAIN + '; } 2>&1 | tee -a ../census_console.log'
UNGROUPED = CHAIN + ' 2>&1 | tee -a ../census_console.log'                  # the plan's form before the review
NO_PIPEFAIL = LAUNCH.replace('set -o pipefail; ', '')

STUB_CHECK = """import os, sys
if os.environ.get('STUB_REFUSE'):
    print('refused, stop field: a stub stop')
    print('resume check: REFUSED; census.py is not launched, and the run is not resumed')
    sys.exit(1)
print('run/out/ does not exist: a first launch')
print('resume check: PASS')
"""
STUB_CENSUS = """import os, sys
print('stub census: started', flush=True)
code = int(os.environ.get('STUB_EXIT', '0'))
if code:
    print('Traceback (most recent call last): a stub failure', file=sys.stderr)
    sys.exit(code)
print('stub census: record and transcript written')
"""


def stub(root):
    os.makedirs(os.path.join(root, 'folder', 'run'))
    os.makedirs(os.path.join(root, 'resume_check'))
    with open(os.path.join(root, 'resume_check', 'resume_check.py'), 'w', encoding='utf-8') as f:
        f.write(STUB_CHECK)
    with open(os.path.join(root, 'folder', 'run', 'census.py'), 'w', encoding='utf-8') as f:
        f.write(STUB_CENSUS)
    with open(os.path.join(root, 'resume_check', 'resume_check.py'), 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def launch(root, form, env=None, times=1):
    code = None
    for _ in range(times):
        r = subprocess.run(['zsh', '-c', form], cwd=os.path.join(root, 'folder'), env=dict(os.environ, **(env or {})),
                           capture_output=True, text=True)
        code = r.returncode
    p = os.path.join(root, 'census_console.log')
    log = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    return code, log


def caffeinates():
    r = subprocess.run(['pgrep', '-f', 'caffeinate -i -m -s -w'], capture_output=True, text=True)
    return set(r.stdout.split())


def main():
    lines, failed = [], 0

    def report(ok, what):
        nonlocal failed
        failed += not ok
        lines.append(what + ('' if ok else '  <-- FAILED'))

    plan = open(PLAN, encoding='utf-8').read().splitlines()
    cmd = [l.strip() for l in plan if 'set -o pipefail; caffeinate' in l]
    report(cmd == [LAUNCH.replace('{sha}', 'RESUME_CHECK_SHA256')], "FILING_PLAN.md's step 3 gives the launch command "
           'this test runs, once')
    OK, PASS, REF = 'resume_check.py: OK', 'resume check: PASS', 'resume check: REFUSED'
    STARTED, DONE, TB = 'stub census: started', 'stub census: record and transcript written', 'Traceback'
    before = caffeinates()
    tmp = tempfile.mkdtemp(prefix='launch_wrapper_')
    try:
        cases = [  # (name, form, env, wrong hash, times, exit, in the log, not in the log)
            ('the earlier form, ungrouped: a clean launch', UNGROUPED, {}, False, 1, 0, [STARTED, DONE], [OK, PASS]),
            ('the command without pipefail: census.py fails with exit 3', NO_PIPEFAIL, {'STUB_EXIT': '3'}, False, 1, 0,
             [OK, PASS, STARTED, TB], []),
            ('the command: a clean launch', LAUNCH, {}, False, 1, 0, [OK, PASS, STARTED, DONE], []),
            ('the command: census.py fails with exit 3', LAUNCH, {'STUB_EXIT': '3'}, False, 1, 3, [OK, PASS, STARTED, TB],
             [DONE]),
            ('the command: a wrong hash', LAUNCH, {}, True, 1, 1, ['resume_check.py: FAILED'], [PASS, STARTED]),
            ('the command: the resume check refuses', LAUNCH, {'STUB_REFUSE': '1'}, False, 1, 1, [OK, REF], [STARTED]),
            ('the command, twice: a relaunch appends', LAUNCH, {}, False, 2, 0, [OK, PASS, DONE], []),
        ]
        for i, (name, form, env, wrong, times, want, has, hasnt) in enumerate(cases, 1):
            root = os.path.join(tmp, f'case{i}')
            sha = stub(root)
            code, log = launch(root, form.replace('{sha}', '0' * 64 if wrong else sha), env, times)
            ok = (code == want and all(s in log for s in has) and not any(s in log for s in hasnt)
                  and (times == 1 or log.count(DONE) == times))
            note = ('the log holds only the run, without the hash check or the verdict' if form is UNGROUPED else
                    "the failure's status is lost through tee" if form is NO_PIPEFAIL else
                    'census.py never starts' if STARTED in hasnt else
                    f'the log holds both launches, {log.count(DONE)} records' if times > 1 else
                    'the log holds the hash check, the verdict and the traceback' if TB in has else
                    'the log holds the hash check, the verdict and the run')
            report(ok, f'case {i}, {name}: exit {code}; {note}')
        for _ in range(50):
            if caffeinates() <= before:
                break
            time.sleep(0.1)
        report(caffeinates() <= before, 'no caffeinate left running by the cases')
    finally:
        shutil.rmtree(tmp)
    lines.append(f'{failed} failed')
    text = '\n'.join(lines) + '\n'
    print(text, end='')
    with open(os.path.join(HERE, 'test_launch_wrapper.out'), 'w', encoding='utf-8') as f:
        f.write(text)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
