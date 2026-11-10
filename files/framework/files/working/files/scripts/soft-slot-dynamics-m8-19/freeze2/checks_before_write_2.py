"""M8.19: the checks before the freeze's second writing, read-only, as the first's (../freeze/checks_before_write.py).
Nothing in the folder is written. Every hash and commit is read from the go and the ruling as kept, from git or from
FROZEN.json, none typed. The last check records the environment by the launch's route in a scratch copy only, and
compares it with the first record.

Usage: python3 -I -B checks_before_write_2.py"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
DEST = os.path.join(ROOTB, 'freeze', 'first_freeze')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
INSTR = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x'
CLONE = os.path.expanduser(os.environ['M819_OPENWAVE_CLONE_FROM_HOME'])
TASK = 'openwave/xperiments/m8_mit/research/tasks/m8_19_task_details.md'
OWN = ('run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN')
THREADS = ('MKL_NUM_THREADS', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')
ROUTE = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch; "
         "sys.exit(subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py')]).returncode)")
fails = []


def ok(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


def run(*a):
    return subprocess.run(a, capture_output=True, check=True).stdout


def gh(path, pages=False):
    d = json.loads(run('gh', 'api', *(['--paginate', '--slurp'] if pages else []), path))
    return [c for page in d for c in page] if pages else d


sha_b = lambda b: hashlib.sha256(b).hexdigest()
sha_f = lambda p: sha_b(open(p, 'rb').read())


def flat(d, pre=''):
    for k, v in d.items():
        yield from (flat(v, f'{pre}{k}.') if isinstance(v, dict) else [(f'{pre}{k}', v)])


# 1. the ruling and the go
go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))
ruling = json.load(open(os.path.join(ROOTB, 'launch_refusal_ask_v2', 'ruling', 'ruling.json'), encoding='utf-8'))
for name, kept in (('the ruling', ruling), ('the go', go)):
    live = gh(f"repos/openwave-labs/openwave/issues/comments/{kept['id']}")
    ok(f'{name} live equals its kept copy, unedited, by xrodz, an OpenWave member',
       live['body'] == kept['body'] and live['created_at'] == live['updated_at'] and live['user']['login'] == 'xrodz'
       and live['author_association'] == 'MEMBER', live['updated_at'])
ok('the ruling links the go and grants the second writing', f"]({go['html_url']})" in ruling['body']
   and 'The freeze is written once more, a one-time exception to § 2' in ruling['body']
   and "Give `write_guard.py` this ruling's link." in ruling['body'])
after = [(p, c['user']['login'], c.get('created_at') or c.get('submitted_at'))
         for p in ('issues/698/comments', 'issues/702/comments', 'pulls/698/comments', 'pulls/702/comments', 'pulls/698/reviews', 'pulls/702/reviews')
         for c in gh(f'repos/openwave-labs/openwave/{p}', pages=True)
         if (c.get('created_at') or c.get('submitted_at') or '') > ruling['created_at']]
ok('nothing posted on #698 or #702 since the ruling', not after, after)
H = re.findall(r'\b[0-9a-f]{64}\b', go['body'])
terms_h, sums_h, sources_h, manifest_h = H
fshort = re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1)
sshort = re.search(r'solver at MIT `([0-9a-f]+)`', go['body']).group(1)
FULL = run('git', '-C', WT, 'rev-parse', fshort + '^{commit}').decode().strip()
SFULL = run('git', '-C', WT, 'rev-parse', sshort + '^{commit}').decode().strip()
ok("the ruling's SHA256SUMS and manifest are the go's", f'`{sums_h[:8]}…`' in ruling['body'] and f'`{manifest_h[:8]}…`' in ruling['body'])

# 2. the terms on OpenWave's main
run('git', '-C', CLONE, 'fetch', '-q', 'upstream')
api_terms = run('gh', 'api', f'repos/openwave-labs/openwave/contents/{TASK}?ref=main', '-H', 'Accept: application/vnd.github.raw')
ok("OpenWave main's task document, read by API, is at the terms' SHA-256", sha_b(api_terms) == terms_h)
up = run('git', '-C', CLONE, 'rev-parse', 'upstream/main').decode().strip()
ok(f"the clone's upstream/main ({up[:8]}, fetched) task document is at the terms' SHA-256",
   sha_b(run('git', '-C', CLONE, 'show', f'upstream/main:{TASK}')) == terms_h)
ok("the bench's run/m8_19_task_details.md is at the terms' SHA-256", sha_f(os.path.join(B, 'run', 'm8_19_task_details.md')) == terms_h)

# 3. MIT
run('git', '-C', WT, 'fetch', '-q', 'origin')
om = run('git', '-C', WT, 'rev-parse', 'origin/main').decode().strip()
ok(f'the folder commit is on origin/main ({om[:8]})', subprocess.run(['git', '-C', WT, 'merge-base', '--is-ancestor', FULL, om]).returncode == 0)
touch = run('git', '-C', WT, 'log', '--format=%h %s', f'{FULL}..{om}', '--', FOLDER, INSTR).decode().strip()
ok('no commit on origin/main since touches the M8.19 folder or the instrument', touch == '', touch)
ok("the worktree's M8.19 folder and instrument equal the folder commit's",
   subprocess.run(['git', '-C', WT, 'diff', '--quiet', FULL, '--', FOLDER, INSTR]).returncode == 0)
st = run('git', '-C', WT, 'status', '--porcelain', '--untracked-files=all', '--', FOLDER, INSTR).decode().strip()
ok("the worktree's M8.19 folder and instrument hold no untracked or changed file", st == '', st)

# 4. the instrument, through the bench's link
link = os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x')
ok("the bench's instrument link resolves to the worktree's instrument", os.path.realpath(link) == os.path.realpath(os.path.join(WT, INSTR)))
solver = os.path.join(link, 'm8_15x_solver')
man_p = os.path.join(solver, 'out', 'MANIFEST.json')
ok("the instrument's MANIFEST.json is at the go's SHA-256", sha_f(man_p) == manifest_h)
man = json.load(open(man_p))
pys = sorted(f for f in os.listdir(solver) if f.endswith('.py'))
ok(f'every instrument .py file is at its manifest and equals its blob at {sshort} ({len(pys)} files)',
   all(man['sha256'].get(f) == sha_f(os.path.join(solver, f)) == sha_b(run('git', '-C', WT, 'show', f'{SFULL}:{INSTR}/m8_15x_solver/{f}')) for f in pys))
fn_p = os.path.join(solver, 'out', 'freeze_numbers.json')
ok(f'out/freeze_numbers.json equals its blob at {fshort}', sha_b(run('git', '-C', WT, 'show', f'{FULL}:{INSTR}/m8_15x_solver/out/freeze_numbers.json')) == sha_f(fn_p))
ok('no __pycache__ in the instrument', not [dp for dp, dn, fn in os.walk(os.path.realpath(link)) if os.path.basename(dp) == '__pycache__'])

# 5. the bench folder: the first freeze in place, the rest at the go's bytes
F1 = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))
pin1 = open(os.path.join(B, 'run', 'FROZEN_PIN')).read().strip()
env1 = sha_f(os.path.join(B, 'run', 'ENVIRONMENT.json'))
ok("the first freeze's three files in run/, at the pins #702 and the ruling name",
   pin1 == sha_f(os.path.join(B, 'run', 'FROZEN.json')) and F1['pins']['run/ENVIRONMENT.json'] == env1
   and f'`{env1[:8]}…`' in ruling['body'] and f'`{pin1[:8]}…`' in ruling['body'] and F1['go'] == go['html_url'])
v = subprocess.run([sys.executable, '-I', '-B', '-c', 'import sys; sys.path.insert(0, "run"); import m819_branch as D; '
                    'F = D.validate_frozen(); print(len(F["pins"]))'], cwd=B, capture_output=True, text=True)
ok('validate_frozen passes on the first freeze', v.returncode == 0 and v.stdout.split() == [str(len(F1['pins']))], (v.stdout + v.stderr)[-200:])
sums = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=B, capture_output=True, text=True)
listed = [ln.split('  ', 1)[1] for ln in open(os.path.join(B, 'SHA256SUMS'), encoding='utf-8').read().splitlines()]
ok("shasum -a 256 -c SHA256SUMS: every listed file OK, SHA256SUMS at the go's SHA-256",
   sums.returncode == 0 and sum(ln.endswith(': OK') for ln in sums.stdout.splitlines()) == len(listed) and sha_f(os.path.join(B, 'SHA256SUMS')) == sums_h,
   f'{sum(ln.endswith(": OK") for ln in sums.stdout.splitlines())} of {len(listed)}')
files = sorted(os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn)
tree = sorted(p[len(FOLDER) + 1:] for p in run('git', '-C', WT, 'ls-tree', '-r', '--name-only', FULL, '--', FOLDER + '/').decode().split('\n') if p)
ok("the copy's files are the commit's tree and the first freeze's three, nothing else: nothing from a rehearsal under run/ or reference/",
   files == sorted(tree + list(OWN)), sorted(set(files) ^ set(tree + list(OWN)))[:5])
ok('no run/out/, cache or .DS_Store in the copy', not os.path.exists(os.path.join(B, 'run', 'out'))
   and not [f for f in files if os.path.basename(f) == '.DS_Store' or '__pycache__' in f.split(os.sep)])
ok("the first freeze's keeping place is free", not os.path.exists(DEST), DEST if os.path.exists(DEST) else '')
env_rec = json.load(open(os.path.join(B, 'run', 'ENVIRONMENT.json')))
ver = run('/usr/bin/sw_vers', '-productVersion').decode().strip() + ' ' + run('/usr/bin/sw_vers', '-buildVersion').decode().strip()
ok("macOS is the first record's", ver == f"{env_rec['os']['version']} {env_rec['os']['build']}", ver)

# 6. the environment by the launch's route, in a scratch copy only, against the first record
base = tempfile.mkdtemp(prefix='m819_env2_')
try:
    os.symlink(os.path.realpath(link), os.path.join(base, 'soft-slot-dynamics-m8-15x'))
    r = os.path.join(base, 'soft-slot-dynamics-m8-19')
    os.makedirs(os.path.join(r, 'run'))
    for f in os.listdir(os.path.join(B, 'run')):
        if 'run/' + f not in OWN:
            shutil.copy2(os.path.join(B, 'run', f), os.path.join(r, 'run', f))
    p = subprocess.run([sys.executable, '-I', '-B', '-c', ROUTE], cwd=r, capture_output=True, text=True)
    a = json.load(open(os.path.join(r, 'run', 'ENVIRONMENT.json'))) if p.returncode == 0 else {}
    fa, fb = dict(flat(a)), dict(flat(env_rec))
    diff = sorted(k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k))
    ok("by the launch's route, in scratch: the record differs from the first in the four threading fields and the time alone",
       p.returncode == 0 and diff == ['recorded'] + [f'threading.{t}' for t in THREADS] and all(a['threading'][t] == '1' for t in THREADS), diff)
finally:
    shutil.rmtree(base)
print(f'      python3: {sys.executable} {sys.version.split()[0]}; isolated {sys.flags.isolated}, dont_write_bytecode {sys.flags.dont_write_bytecode}')
print('checks before the second writing:', 'PASS' if not fails else f'FAIL ({len(fails)}): {fails}')
sys.exit(1 if fails else 0)
