"""M8.19: run/FROZEN.json read back against its sources, independently of the driver's own validate_frozen, which is
then run in a fresh process; and the environment checked again. Read-only."""
import hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
WT = os.environ['M819_MIT_CLONE']
M18 = os.path.join(WT, 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-18/run/ENVIRONMENT.json')
fails = []


def ok(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


sha_f = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
kept = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))
terms_h, sums_h, sources_h, manifest_h = re.findall(r'\b[0-9a-f]{64}\b', kept['body'])
sshort = re.search(r'solver at MIT `([0-9a-f]+)`', kept['body']).group(1)
P = os.path.join(B, 'run', 'FROZEN.json')
F = json.load(open(P))
print(f'      FROZEN.json: {os.path.getsize(P)} bytes, written {F["written"]}, SHA-256 {sha_f(P)}')
ok('FROZEN_PIN holds FROZEN.json\'s SHA-256', open(os.path.join(B, 'run', 'FROZEN_PIN')).read() == sha_f(P) + '\n')
ok('frozen, with the go\'s link', F['frozen'] is True and F['go'] == kept['html_url'], F['go'])
ok("the terms' SHA-256 is the go's", F['terms_sha256'] == terms_h)
ok("the solver commit is the go's", F['solver_commit'] == sshort, F['solver_commit'])
ok("the instrument manifest's SHA-256 is the go's", F['instrument_manifest_sha256'] == manifest_h)
listed = {p: h for h, p in (l.split('  ', 1) for l in open(os.path.join(B, 'SHA256SUMS'), encoding='utf-8').read().splitlines())}
ok("SHA256SUMS on the bench is at the go's SHA-256", sha_f(os.path.join(B, 'SHA256SUMS')) == sums_h)
want = sorted([p for p in listed if p.startswith(('run/', 'reference/'))] + ['run/ENVIRONMENT.json'])
ok('the pins are run/ and reference/ as SHA256SUMS lists them, and run/ENVIRONMENT.json', sorted(F['pins']) == want, f'{len(F["pins"])} pins')
ok('each listed pin is at its SHA256SUMS line', all(F['pins'][p] == listed[p] for p in want if p in listed))
env_p = os.path.join(B, 'run', 'ENVIRONMENT.json')
ok('the ENVIRONMENT.json pin is the file\'s SHA-256', F['pins']['run/ENVIRONMENT.json'] == sha_f(env_p), sha_f(env_p))
ok("reference/SOURCES.json's pin is the go's", F['pins']['reference/SOURCES.json'] == sources_h)
fn = os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x', 'm8_15x_solver', 'out', 'freeze_numbers.json')
ok("freeze_numbers equals the instrument's out/freeze_numbers.json", F['freeze_numbers'] == json.load(open(fn)))
extra = sorted(set(F) - {'frozen', 'go', 'written', 'terms_sha256', 'solver_commit', 'instrument_manifest_sha256', 'pins', 'freeze_numbers'})
ok('FROZEN.json holds no field beyond write_guard.py\'s', not extra, extra if extra else '')
v = subprocess.run([sys.executable, '-I', '-B', '-c', 'import sys; sys.path.insert(0, "run"); import m819_branch as D; F = D.validate_frozen(); print(len(F["pins"]))'],
                   cwd=B, capture_output=True, text=True)
ok("the driver's validate_frozen passes in a fresh process", v.returncode == 0 and v.stdout.strip() == '16', (v.stdout + v.stderr).strip())
e = subprocess.run([sys.executable, '-I', '-B', os.path.join(B, 'run', 'record_environment.py'), '--check'], capture_output=True, text=True)
ok('record_environment.py --check: no difference', e.returncode == 0 and e.stdout.rstrip().endswith('differences: none'))
for x in ('out',):
    ok(f'no run/{x} yet', not os.path.exists(os.path.join(B, 'run', x)))
caches = [dp for dp, dn, fn in os.walk(B) if os.path.basename(dp) == '__pycache__'] + \
         [dp for dp, dn, fn in os.walk(os.path.realpath(os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x'))) if os.path.basename(dp) == '__pycache__']
ok('no __pycache__ in the folder or the instrument', not caches, caches[:3] if caches else '')


def flat(d, pre=''):
    for k, val in d.items():
        if isinstance(val, dict):
            yield from flat(val, f'{pre}{k}.')
        else:
            yield f'{pre}{k}', val


a, b = dict(flat(json.load(open(env_p)))), dict(flat(json.load(open(M18))))
print('      ENVIRONMENT.json against M8.18\'s, the fields that differ:', sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k)))
print('verify FROZEN.json:', 'PASS' if not fails else f'FAIL {fails}')
sys.exit(1 if fails else 0)
