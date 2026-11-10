"""Scratch only: the refused launch reproduced, and the environment recorded by the launch's own route, in copies of
run/ and reference/ beside a link to the instrument, with a rehearsal go. Nothing here touches the bench's folder, and
nothing launches: only main()'s steps before launch() are replayed."""
import json, os, shutil, subprocess, sys, tempfile
B = os.environ['M819_BENCH'] + '/soft-slot-dynamics-m8-19'
INSTR = os.path.realpath(os.path.join(B, '..', 'soft-slot-dynamics-m8-15x'))
GO = 'https://github.com/openwave-labs/openwave/pull/0#rehearsal'
CODE = ['m819_branch.py', 'm819_gates.py', 'm819_run.py', 'm8_19_task_details.md', 'record_environment.py', 'write_guard.py']
PRE = 'import os, subprocess, sys; sys.path.insert(0, "run"); import m819_branch as D; D.validate_frozen(); '

def copy(base):
    t = tempfile.mkdtemp(dir=base)
    os.symlink(INSTR, os.path.join(t, 'soft-slot-dynamics-m8-15x'))
    r = os.path.join(t, 'soft-slot-dynamics-m8-19')
    os.makedirs(os.path.join(r, 'run'))
    for f in CODE:
        shutil.copy2(os.path.join(B, 'run', f), os.path.join(r, 'run', f))
    shutil.copytree(os.path.join(B, 'reference'), os.path.join(r, 'reference'))
    return r

def py(r, *args, env=None):
    return subprocess.run([sys.executable, '-I', '-B'] + list(args), cwd=r, capture_output=True, text=True, env=env)

def launch_check(r):
    """main()'s steps before launch(): import m819_branch, validate_frozen, then record_environment.py --check."""
    p = py(r, '-c', PRE + 'e = subprocess.run([sys.executable, "-I", "-B", "run/record_environment.py", "--check"], capture_output=True, text=True); '
                         'print(e.returncode, e.stdout.strip().splitlines()[-1])')
    return (p.stdout + p.stderr).strip().splitlines()[-1]

base = tempfile.mkdtemp(prefix='m819_env_')
# 1. as the bench did it: the environment recorded from the shell, then the launch's check
r1 = copy(base)
assert py(r1, 'run/record_environment.py').returncode == 0 and py(r1, 'run/write_guard.py', GO).returncode == 0
print('recorded from the shell, the launch reads:', launch_check(r1))
# 2. recorded by the launch's own route: m819_branch imported first, then record_environment.py, inheriting
r2 = copy(base)
p = py(r2, '-c', 'import subprocess, sys; sys.path.insert(0, "run"); import m819_branch; '
                 'sys.exit(subprocess.run([sys.executable, "-I", "-B", "run/record_environment.py"]).returncode)')
assert p.returncode == 0, p.stderr[-300:]
assert py(r2, 'run/write_guard.py', GO).returncode == 0
print('recorded by the launch\'s route, the launch reads:', launch_check(r2))
a = json.load(open(os.path.join(r2, 'run', 'ENVIRONMENT.json')))
b = json.load(open(os.path.join(B, 'run', 'ENVIRONMENT.json')))
def flat(d, pre=''):
    for k, v in d.items():
        yield from (flat(v, f'{pre}{k}.') if isinstance(v, dict) else [(f'{pre}{k}', v)])
fa, fb = dict(flat(a)), dict(flat(b))
print("that record against the bench's:", sorted(k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k)))
print('threading recorded:', a['threading'])
shutil.rmtree(base)
