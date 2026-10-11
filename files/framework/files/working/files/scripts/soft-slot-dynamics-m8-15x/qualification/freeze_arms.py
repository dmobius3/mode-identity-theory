"""Mutation arms for freeze_manifest.py's checks, on scratch copies of the two folders. A green parent first."""
import os, sys, shutil, subprocess, json, tempfile
REPO_SCRIPTS = sys.argv[1]
QUAL = sys.argv[2]
BENCH_CR = sys.argv[3]
SP = sys.argv[4]
NEW, OLD = 'soft-slot-dynamics-m8-15x', 'soft-slot-dynamics'

def fresh(tag):
    root = os.path.join(SP, 'freeze_arms', tag, 'scripts')
    if os.path.exists(root): shutil.rmtree(root)
    os.makedirs(root)
    for d in (NEW, OLD):
        shutil.copytree(os.path.join(REPO_SCRIPTS, d), os.path.join(root, d))
    return root

def run(root, *args):
    r = subprocess.run([sys.executable, os.path.join(root, NEW, 'freeze_manifest.py'), *args], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

def lines(out):
    return {l.split(None, 1)[1].split(' (')[0].split(':')[0]: l.split()[0] for l in out.splitlines() if l.strip().startswith(('PASS', 'FAIL'))}

def append(p, b):
    with open(p, 'ab') as f: f.write(b)

results = []
root = fresh('parent')
rc, out = run(root, 'check', QUAL)
parent = lines(out)
print('green parent:', rc, parent)
assert rc == 0 and all(v == 'PASS' for v in parent.values()), out

def arm(name, target, mutate, args=('check', QUAL), expect_refusal=None):
    root = fresh(name)
    mutate(root)
    rc, out = run(root, *args)
    if expect_refusal:
        ok = rc != 0 and expect_refusal in out
        results.append((name, ok, out.strip().splitlines()[-1][:160]))
        return
    got = lines(out)
    ok = rc == 1 and got.get(target) == 'FAIL'
    results.append((name, ok, f'target {target}: {got.get(target)}; all: {got}'))

S = lambda root: os.path.join(root, NEW, 'm8_15x_solver')
arm('hash: a byte appended to angle.py', '1. hashes', lambda r: append(os.path.join(S(r), 'angle.py'), b'\n'))
arm('hash: the left-out module added', '1. hashes', lambda r: shutil.copy(BENCH_CR, os.path.join(S(r), 'cluster_rule.py')))
def imp_left(r):
    shutil.copy(BENCH_CR, os.path.join(S(r), 'cluster_rule.py'))
    p = os.path.join(S(r), 'verdict.py'); t = open(p).read(); open(p, 'w').write('import cluster_rule\n' + t)
arm('imports: verdict.py imports the left-out module', '2. imports', imp_left)
def imp_out(r):
    os.remove(os.path.join(S(r), 'irreps.py'))
    p = os.path.join(S(r), 'geometry.py'); t = open(p).read()
    open(p, 'w').write(f'import sys as _s; _s.path.append({os.path.join(r, OLD, "m8_15_solver")!r})\n' + t)
arm('imports: a module loads from M8.15\'s folder', '2. imports', imp_out)
arm('names: a file in the solver folder names it', '3. names',
    lambda r: open(os.path.join(S(r), 'out', 'note.txt'), 'w').write('see cluster_rule\n'))
def stat(r):
    p = os.path.join(S(r), 'out', 'dt_L2.json'); b = bytearray(open(p, 'rb').read()); b[-2] ^= 1; open(p, 'wb').write(bytes(b))
arm('static: a byte of dt_L2.json flipped', '4. static inputs and Theorem D', stat)
arm('sums: an unpinned file added', '5a. SHA256SUMS here', lambda r: open(os.path.join(r, NEW, 'extra.txt'), 'w').write('x\n'))
arm('M8.15 sums: a byte appended to its REPRODUCE.md', "5b. M8.15's SHA256SUMS",
    lambda r: append(os.path.join(r, OLD, 'REPRODUCE.md'), b'\n'))
def env(r):
    p = os.path.join(r, OLD, 'm8_15_solver', 'out', 'MANIFEST.json'); m = json.load(open(p))
    m['environment']['numpy'] = m['environment']['numpy'] + '.x'; json.dump(m, open(p, 'w'), indent=1)
arm('manifest: refused on an environment difference', None, env, args=('manifest', QUAL), expect_refusal='environment differs')
qbad = os.path.join(SP, 'freeze_arms', 'QUALIFICATION_mutated.json')
q = json.load(open(QUAL)); h = q['steps']['controls']['instrument_sha256']['angle.py']
q['steps']['controls']['instrument_sha256']['angle.py'] = ('0' if h[0] != '0' else '1') + h[1:]
json.dump(q, open(qbad, 'w'))
arm('manifest: refused on a hash the qualification did not record', None, lambda r: None, args=('manifest', qbad),
    expect_refusal='not the hash the qualification recorded')
for name, ok, info in results:
    print(f'  {"caught " if ok else "MISSED "} {name}: {info}')
print('mutation arms:', 'ALL CAUGHT' if all(ok for _, ok, _ in results) else 'SOME MISSED', f'({sum(ok for _, ok, _ in results)} of {len(results)})')
