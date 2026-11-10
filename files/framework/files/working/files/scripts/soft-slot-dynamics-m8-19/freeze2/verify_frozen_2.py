"""M8.19's second freeze read back, read-only, apart from the script that wrote it: run/FROZEN.json field by field
against the go, the ruling, SHA256SUMS and the instrument; the first freeze as kept; the two environment records; the
launch's two checks, replayed in a fresh process by the launch's route; and the environment check from the shell, which
must now read the four threading variables as unset against the record's '1', as the launch's route never does.
Every hash, link and commit is read from the go and the ruling as kept, from git or from the files, none typed."""
import hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
K = os.path.join(ROOTB, 'freeze', 'first_freeze', 'run')
WT = os.environ['M819_MIT_CLONE']
MITF = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
INSTR = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x'
THREADS = ('MKL_NUM_THREADS', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')
fails = []


def ok(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


sha_b = lambda b: hashlib.sha256(b).hexdigest()
sha_f = lambda p: sha_b(open(p, 'rb').read())
git = lambda *a: subprocess.run(['git', '-C', WT] + list(a), capture_output=True, check=True).stdout


def flat(d, pre=''):
    for k, v in d.items():
        yield from (flat(v, f'{pre}{k}.') if isinstance(v, dict) else [(f'{pre}{k}', v)])


go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))
ru = json.load(open(os.path.join(ROOTB, 'launch_refusal_ask_v2', 'ruling', 'ruling.json'), encoding='utf-8'))
terms_h, sums_h, sources_h, manifest_h = re.findall(r'\b[0-9a-f]{64}\b', go['body'])
sshort = re.search(r'solver at MIT `([0-9a-f]+)`', go['body']).group(1)
FULL = git('rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').decode().strip()
F2 = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))
F1 = json.load(open(os.path.join(K, 'FROZEN.json')))
pin2 = open(os.path.join(B, 'run', 'FROZEN_PIN')).read().strip()
pin1 = open(os.path.join(K, 'FROZEN_PIN')).read().strip()
E2 = json.load(open(os.path.join(B, 'run', 'ENVIRONMENT.json')))
E1 = json.load(open(os.path.join(K, 'ENVIRONMENT.json')))
listed = {p: h for h, p in (ln.split('  ', 1) for ln in open(os.path.join(B, 'SHA256SUMS'), encoding='utf-8').read().splitlines())}

print('== the second FROZEN.json, field by field')
ok('its fields, in the first one\'s order, and no other', list(F2) == list(F1) == ['frozen', 'go', 'written', 'terms_sha256', 'solver_commit',
   'instrument_manifest_sha256', 'pins', 'freeze_numbers'], list(F2))
ok('frozen, with the ruling\'s link as its go', F2['frozen'] is True and F2['go'] == ru['html_url'])
ok("the terms' SHA-256, the solver commit and the manifest's SHA-256, each as the go names it",
   F2['terms_sha256'] == terms_h and F2['solver_commit'] == sshort and F2['instrument_manifest_sha256'] == manifest_h)
solver = os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x', 'm8_15x_solver')
ok("freeze_numbers equal to the instrument's out/freeze_numbers.json and to the first freeze's",
   F2['freeze_numbers'] == json.load(open(os.path.join(solver, 'out', 'freeze_numbers.json'))) == F1['freeze_numbers'])
n15 = {p: h for p, h in F2['pins'].items() if p != 'run/ENVIRONMENT.json'}
ok('15 pins at their SHA256SUMS lines, equal to the first freeze\'s, and the new record',
   len(n15) == 15 and all(listed.get(p) == h for p, h in n15.items()) and n15 == {p: h for p, h in F1['pins'].items() if p != 'run/ENVIRONMENT.json'}
   and F2['pins']['run/ENVIRONMENT.json'] == sha_f(os.path.join(B, 'run', 'ENVIRONMENT.json')), len(F2['pins']))
ok('every pin at its file now', all(sha_f(os.path.join(B, p)) == h for p, h in F2['pins'].items()))
ok("FROZEN_PIN holds the second FROZEN.json's SHA-256", pin2 == sha_f(os.path.join(B, 'run', 'FROZEN.json')))
ok('written after the ruling, the environment recorded before it was written',
   ru['created_at'] < E2['recorded'] <= F2['written'], f"{ru['created_at']} < {E2['recorded']} <= {F2['written']}")
keys = sorted(k for k in set(F1) | set(F2) if k != 'pins' and F1.get(k) != F2.get(k))
pins = sorted(k for k in set(F1['pins']) | set(F2['pins']) if F1['pins'].get(k) != F2['pins'].get(k))
ok('the two FROZEN.json differ in the environment pin, written and go alone', keys == ['go', 'written'] and pins == ['run/ENVIRONMENT.json'], (keys, pins))

print('== the first freeze, as kept')
ok('kept beside the folder: its three files alone', sorted(os.listdir(K)) == ['ENVIRONMENT.json', 'FROZEN.json', 'FROZEN_PIN'], sorted(os.listdir(K)))
ok("at the pins #702 records and the ruling names, the go's link in it",
   pin1 == sha_f(os.path.join(K, 'FROZEN.json')) and F1['pins']['run/ENVIRONMENT.json'] == sha_f(os.path.join(K, 'ENVIRONMENT.json'))
   and f'`{pin1[:8]}…`' in ru['body'] and f"`{F1['pins']['run/ENVIRONMENT.json'][:8]}…`" in ru['body'] and F1['go'] == go['html_url'])
fa, fb = dict(flat(E1)), dict(flat(E2))
diff = sorted(k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k))
ok('the two environment records differ in the four threading fields and the time alone, the interpreter path and flags included',
   diff == ['recorded'] + [f'threading.{t}' for t in THREADS] and all(E1['threading'][t] is None and E2['threading'][t] == '1' for t in THREADS)
   and E1['interpreter'] == E2['interpreter'], diff)

print('== the folder')
files = sorted(os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn)
tree = sorted(p[len(MITF) + 1:] for p in git('ls-tree', '-r', '--name-only', FULL, '--', MITF + '/').decode().split('\n') if p)
ok("the folder's files are the commit's tree and the second freeze's three, nothing else",
   files == sorted(tree + ['run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN']), sorted(set(files) ^ set(tree))[:6])
s = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=B, capture_output=True, text=True)
ok("SHA256SUMS: every listed file OK, at the go's SHA-256", s.returncode == 0 and sum(ln.endswith(': OK') for ln in s.stdout.splitlines()) == len(listed)
   and sha_f(os.path.join(B, 'SHA256SUMS')) == sums_h)
ok('no run/out/, and no cache in the folder or the instrument', not os.path.exists(os.path.join(B, 'run', 'out'))
   and not [dp for top in (B, os.path.realpath(os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x'))) for dp, dn, fn in os.walk(top) if os.path.basename(dp) == '__pycache__'])
st = git('status', '--porcelain', '--untracked-files=all', '--', MITF, INSTR).decode().strip()
ok("the worktree's M8.19 folder and instrument unchanged", st == '' and subprocess.run(['git', '-C', WT, 'diff', '--quiet', FULL, '--', MITF, INSTR]).returncode == 0, st)

print("== the launch's two checks, in a fresh process, by the launch's route")
REPLAY = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch as D; "
          "F = D.validate_frozen(); print(len(F['pins']), F['go'], flush=True); "
          "e = subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py'), '--check'], "
          "capture_output=True, text=True); print(e.stdout.rstrip().splitlines()[-1], flush=True); sys.exit(e.returncode)")
p = subprocess.run([sys.executable, '-I', '-B', '-c', REPLAY], cwd=B, capture_output=True, text=True)
ok('validate_frozen passes, with the ruling\'s link, and the check reads no difference',
   p.returncode == 0 and p.stdout.split('\n')[:2] == [f"16 {ru['html_url']}", 'differences: none'], (p.stdout + p.stderr)[-300:])
print('== the environment check from the shell, which the launch never runs')
q = subprocess.run([sys.executable, '-I', '-B', os.path.join(B, 'run', 'record_environment.py'), '--check'], capture_output=True, text=True,
                   env={k: v for k, v in os.environ.items() if k not in THREADS})
ok("from the shell, with the four unset, it reads the four threading differences, as the launch's route never does",
   q.returncode == 1 and q.stdout.rstrip().splitlines()[-1] == 'differences: ' + str([f'threading.{t}' for t in THREADS]), q.stdout.rstrip().splitlines()[-1:])
print('verify_frozen_2:', 'PASS' if not fails else f'FAIL ({len(fails)}): {fails}')
sys.exit(1 if fails else 0)
