"""The freeze rehearsed (DESIGN.md, the dry run's step 9), as M8.18's run/test_freeze.py rehearsed its own: on a
temporary copy of run/ and reference/, beside a link to the instrument, write_guard.py writes FROZEN.json with a
rehearsal go, validate_frozen reads it back, and each arm changes one thing and must be refused for its reason. This
folder's own run/ gets no FROZEN.json.

  test_freeze.py      prints each arm; exits 1 if any arm is not as named"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INSTR = os.path.normpath(os.path.join(ROOT, '..', 'soft-slot-dynamics-m8-15x'))
GO = 'https://github.com/openwave-labs/openwave/pull/0#rehearsal'
fails = []


def check(name, good, detail=''):
    print(f"{'ok  ' if good else 'FAIL'} {name}" + (f': {detail}' if detail else ''), flush=True)
    if not good:
        fails.append(name)


def fresh():
    t = tempfile.mkdtemp()
    os.symlink(INSTR, os.path.join(t, 'soft-slot-dynamics-m8-15x'))
    r = os.path.join(t, 'soft-slot-dynamics-m8-19')
    shutil.copytree(os.path.join(ROOT, 'run'), os.path.join(r, 'run'), ignore=shutil.ignore_patterns('out', '__pycache__'))
    shutil.copytree(os.path.join(ROOT, 'reference'), os.path.join(r, 'reference'))
    return t, r


def py(r, *args):
    return subprocess.run([sys.executable, '-I', '-B', *args], cwd=r, capture_output=True, text=True)


def validate(r):
    p = py(r, '-c', 'import sys; sys.path.insert(0, "run"); import m819_branch as D\n'
                     'try:\n    D.validate_frozen(); print("VALID")\nexcept D.Refused as e:\n    print("REFUSED", e)')
    return p.stdout.strip() + p.stderr.strip()[-300:]


check("this folder's run/ has no FROZEN.json", not os.path.exists(os.path.join(ROOT, 'run', 'FROZEN.json')))
t, r = fresh()
try:
    out = validate(r)
    check('no FROZEN.json: refused', out == 'REFUSED no FROZEN.json', out)
    p = py(r, 'run/m819_run.py')
    check('the registered orchestrator refuses with no FROZEN.json', p.returncode != 0 and 'no FROZEN.json' in p.stderr,
          p.stderr.strip()[-100:])
    p = py(r, 'run/write_guard.py', GO)
    check('write_guard refuses before the environment is recorded', p.returncode != 0 and 'ENVIRONMENT.json' in p.stderr)
    p = py(r, 'run/record_environment.py')
    check('record_environment writes run/ENVIRONMENT.json', p.returncode == 0
          and os.path.exists(os.path.join(r, 'run', 'ENVIRONMENT.json')), (p.stdout + p.stderr).strip()[-120:])
    p = py(r, 'run/write_guard.py', GO)
    check('write_guard writes FROZEN.json and its pin', p.returncode == 0 and 'FROZEN.json written' in p.stdout,
          (p.stdout + p.stderr).strip()[-160:])
    out = validate(r)
    check('the freeze reads back valid', out == 'VALID', out)
    F = json.load(open(os.path.join(r, 'run', 'FROZEN.json')))
    check('every file under run/ and reference/ is pinned, the freeze files and out/ apart',
          'run/m819_branch.py' in F['pins'] and 'run/ENVIRONMENT.json' in F['pins'] and 'reference/SOURCES.json' in F['pins'] and not any(
              k.startswith('run/out') or k in ('run/FROZEN.json', 'run/FROZEN_PIN') for k in F['pins']), f'{len(F["pins"])} pins')
    p = py(r, 'run/write_guard.py', GO)
    check('a second write_guard is refused', p.returncode != 0 and 'FileExistsError' in p.stderr)

    def arm(name, change, undo, why):
        change()
        out = validate(r)
        check(name, out.startswith('REFUSED') and why in out, out)
        undo()
        check(f'  undone, valid again', validate(r) == 'VALID')

    drv = os.path.join(r, 'run', 'm819_gates.py')
    keep = open(drv, 'rb').read()
    arm('a pinned run file changed', lambda: open(drv, 'ab').write(b'\n'), lambda: open(drv, 'wb').write(keep),
        'run/m819_gates.py differs from its pin')
    extra = os.path.join(r, 'run', 'extra.py')
    arm('an unpinned file under run/', lambda: open(extra, 'w').write('x'), lambda: os.remove(extra), 'not the pinned set')
    ref = os.path.join(r, 'reference', 'm8_17', 'run', 'out', 'T4_R5.json')
    rk = open(ref, 'rb').read()
    arm('a reference file changed', lambda: open(ref, 'ab').write(b' '), lambda: open(ref, 'wb').write(rk),
        'T4_R5.json differs from its pin')
    fz = os.path.join(r, 'run', 'FROZEN.json')
    fk = open(fz, 'rb').read()
    arm('FROZEN.json changed without its pin', lambda: open(fz, 'ab').write(b' '), lambda: open(fz, 'wb').write(fk),
        'not at its pin')
    pin = os.path.join(r, 'run', 'FROZEN_PIN')
    pk = open(pin, 'rb').read()

    def repin(obj):
        open(fz, 'w').write(json.dumps(obj, indent=1) + '\n')
        import hashlib
        open(pin, 'w').write(hashlib.sha256(open(fz, 'rb').read()).hexdigest() + '\n')

    def restore():
        open(fz, 'wb').write(fk)
        open(pin, 'wb').write(pk)

    arm('no go', lambda: repin(dict(F, go='')), restore, 'not marked frozen with a go')
    arm("M8.15's frozen numbers changed", lambda: repin(dict(F, freeze_numbers=dict(F['freeze_numbers'], eta=2e-3))), restore,
        "frozen numbers differ")
    arm("another terms' SHA-256", lambda: repin(dict(F, terms_sha256='0' * 64)), restore, "terms' SHA-256 differs")
    arm("another instrument manifest", lambda: repin(dict(F, instrument_manifest_sha256='0' * 64)), restore,
        'instrument differs from its manifest')
finally:
    shutil.rmtree(t)
print('PASS' if not fails else f'FAIL: {fails}')
raise SystemExit(1 if fails else 0)
