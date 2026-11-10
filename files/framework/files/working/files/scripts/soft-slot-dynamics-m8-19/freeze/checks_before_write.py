"""M8.19: the checks before the freeze's write, read-only, as M8.18's (its DEVLOG, entry 21). Nothing in the folder is
written. Every hash and commit is read from the go as kept (go_request_v1/go.json) or from git, none typed."""
import hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
PK = os.path.join(ROOTB, 'go_request_v1')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
INSTR = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x'
CLONE = os.path.expanduser(os.environ['M819_OPENWAVE_CLONE_FROM_HOME'])
TASK = 'openwave/xperiments/m8_mit/research/tasks/m8_19_task_details.md'
GO_ID = 6749289423
THREADS = ('VECLIB_MAXIMUM_THREADS', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS')
fails = []


def ok(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


def run(*a):
    return subprocess.run(a, capture_output=True, check=True).stdout


sha_b = lambda b: hashlib.sha256(b).hexdigest()
sha_f = lambda p: sha_b(open(p, 'rb').read())

# 1. the go
kept = json.load(open(os.path.join(PK, 'go.json'), encoding='utf-8'))
live = json.loads(run('gh', 'api', f'repos/openwave-labs/openwave/issues/comments/{GO_ID}'))
ok('the go live equals its kept copy', live['body'] == kept['body'])
ok('the go is unedited', live['created_at'] == live['updated_at'], live['updated_at'])
ok('the go is by xrodz, an OpenWave member', live['user']['login'] == 'xrodz' and live['author_association'] == 'MEMBER')
H = re.findall(r'\b[0-9a-f]{64}\b', kept['body'])
ok('the go names four SHA-256 values', len(H) == 4, len(H))
terms_h, sums_h, sources_h, manifest_h = H
fshort = re.search(r'the folder at MIT `([0-9a-f]+)`', kept['body']).group(1)
sshort = re.search(r'solver at MIT `([0-9a-f]+)`', kept['body']).group(1)
FULL = run('git', '-C', WT, 'rev-parse', fshort + '^{commit}').decode().strip()
SFULL = run('git', '-C', WT, 'rev-parse', sshort + '^{commit}').decode().strip()
print(f'      the go names the folder at {fshort} ({FULL}) and the solver at {sshort} ({SFULL})')
print(f'      the go link: {kept["html_url"]}')

# 2. the terms on OpenWave's main
api_terms = run('gh', 'api', f'repos/openwave-labs/openwave/contents/{TASK}?ref=main', '-H', 'Accept: application/vnd.github.raw')
ok("OpenWave main's task document, read by API, is at the terms' SHA-256", sha_b(api_terms) == terms_h)
up = run('git', '-C', CLONE, 'rev-parse', 'upstream/main').decode().strip()
ok(f"the clone's upstream/main ({up[:8]}) task document is at the terms' SHA-256",
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
ok("the bench's instrument link resolves to the worktree's instrument",
   os.path.realpath(link) == os.path.realpath(os.path.join(WT, INSTR)), os.readlink(link))
solver = os.path.join(link, 'm8_15x_solver')
man_p = os.path.join(solver, 'out', 'MANIFEST.json')
ok("the instrument's MANIFEST.json is at the go's SHA-256", sha_f(man_p) == manifest_h)
man = json.load(open(man_p))
pys = sorted(f for f in os.listdir(solver) if f.endswith('.py'))
bad = [f for f in pys if man['sha256'].get(f) != sha_f(os.path.join(solver, f))]
ok(f'every instrument .py file is at its manifest ({len(pys)} files)', not bad, bad if bad else '')
blob_bad = [f for f in pys if sha_b(run('git', '-C', WT, 'show', f'{SFULL}:{INSTR}/m8_15x_solver/{f}')) != sha_f(os.path.join(solver, f))]
ok(f'every instrument .py file equals its blob at {sshort}', not blob_bad, blob_bad if blob_bad else '')
ok(f'MANIFEST.json equals its blob at {sshort}', sha_b(run('git', '-C', WT, 'show', f'{SFULL}:{INSTR}/m8_15x_solver/out/MANIFEST.json')) == manifest_h)
fn_p = os.path.join(solver, 'out', 'freeze_numbers.json')
ok(f'out/freeze_numbers.json equals its blob at {fshort}', os.path.isfile(fn_p) and
   sha_b(run('git', '-C', WT, 'show', f'{FULL}:{INSTR}/m8_15x_solver/out/freeze_numbers.json')) == sha_f(fn_p))
cache = [os.path.join(dp, d) for dp, dn, fn in os.walk(os.path.realpath(link)) for d in dn if d == '__pycache__']
ok('no __pycache__ in the instrument', not cache, cache[:3] if cache else '')

# 5. the bench folder
for x in ('ENVIRONMENT.json', 'FROZEN.json', 'FROZEN_PIN', 'out'):
    ok(f'no run/{x} on the bench', not os.path.exists(os.path.join(B, 'run', x)))
sums_blob = run('git', '-C', WT, 'show', f'{FULL}:{FOLDER}/SHA256SUMS')
ok(f"SHA256SUMS at {fshort} is at the go's SHA-256", sha_b(sums_blob) == sums_h)
listed = {p: h for h, p in (l.split('  ', 1) for l in sums_blob.decode('utf-8').splitlines())}
ok('SHA256SUMS lists 183 files', len(listed) == 183, len(listed))
present = {p for p in listed if os.path.exists(os.path.join(B, p))}
equal = {p for p in present if sha_f(os.path.join(B, p)) == listed[p]}
missing = sorted(set(listed) - present)
ok('every listed file the bench holds is at its SHA-256', equal == present, f'{len(equal)} of {len(present)}')
ok("the bench lacks only registration/'s files", bool(missing) and all(p.startswith('registration/') for p in missing), f'{len(missing)} missing')
ok('no SHA256SUMS or registration/ on the bench yet', not os.path.exists(os.path.join(B, 'SHA256SUMS')) and not os.path.exists(os.path.join(B, 'registration')))
allf = [os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn]
unlisted = sorted(p for p in allf if p not in listed)
ok('no unlisted file under run/ or reference/', not any(p.startswith(('run/', 'reference/')) for p in unlisted))
print(f'      unlisted on the bench: {len(unlisted)} files, under', sorted({"/".join(p.split("/")[:3]) for p in unlisted}))
junk = [p for p in allf if os.path.basename(p) == '.DS_Store' or '__pycache__' in p.split(os.sep)]
ok('no .DS_Store or __pycache__ in the bench folder', not junk, junk[:5] if junk else '')
src = json.load(open(os.path.join(B, 'reference', 'SOURCES.json')))
ok("reference/SOURCES.json is at the go's SHA-256", sha_f(os.path.join(B, 'reference', 'SOURCES.json')) == sources_h)
rb = [f['file'] for f in src['files'] if not (sha_b(run('git', '-C', WT, 'show', f"{f['commit']}:{f['path']}")) == sha_f(os.path.join(B, f['file'])) == f['sha256'])]
ok(f"the {len(src['files'])} reference copies equal their blobs and SOURCES.json's SHA-256", not rb, rb if rb else '')

# 6. the environment, read without writing
print(f'      python3: {sys.executable} {sys.version.split()[0]}; isolated {sys.flags.isolated}, dont_write_bytecode {sys.flags.dont_write_bytecode}')
print('      threading variables in this shell:', {k: os.environ.get(k) for k in THREADS})
print('      macOS', run('/usr/bin/sw_vers', '-productVersion').decode().strip(), run('/usr/bin/sw_vers', '-buildVersion').decode().strip())
print('checks before the write:', 'PASS' if not fails else f'FAIL {fails}')
sys.exit(1 if fails else 0)
