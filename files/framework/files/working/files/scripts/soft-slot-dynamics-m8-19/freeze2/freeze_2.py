"""M8.19's freeze written once more, in the order the maintainer's ruling sets (#698, the ruling of 2026-11-10, item 2):

  (a) the first freeze's three files moved out of run/ to where the ruling's item 1 keeps them, each byte unchanged;
  (b) the folder checked against SHA256SUMS at the go's folder commit, and its files the commit's tree;
  (c) run/ENVIRONMENT.json recorded once more, by the launch's route: the run's interpreter with -I -B, from a process
      that has imported the driver, as main() runs the check; the record compared with the first;
  (d) write_guard.py with the ruling's link, the terms read against the OpenWave clone, as at the first writing; the
      two FROZEN.json compared;
  (e) the two calls main() makes before launch(), replayed without launch().

Each step stops the script on its first failure, and nothing is then rewritten. Every hash, link and commit is read
from the go and the ruling as kept, from git or from the files, none typed. Every output is written into OUT, by
exclusive create.

Usage: python3 -I -B freeze_2.py FOLDER DEST OUT"""
import hashlib, json, os, re, subprocess, sys

FOLDER_P, DEST, OUT = (os.path.abspath(p) for p in sys.argv[1:4])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOTB = os.path.dirname(HERE)
WT = os.environ['M819_MIT_CLONE']
MITF = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
CLONE = os.path.expanduser(os.environ['M819_OPENWAVE_CLONE_FROM_HOME'])
OWN = ('ENVIRONMENT.json', 'FROZEN.json', 'FROZEN_PIN')
THREADS = ('MKL_NUM_THREADS', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')
ROUTE = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch; "
         "sys.exit(subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py')]).returncode)")
REPLAY = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch as D; "
          "F = D.validate_frozen(); print('validate_frozen: passed;', len(F['pins']), 'pins; go', F['go'], flush=True); "
          "e = subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py'), '--check'], "
          "capture_output=True, text=True); print(e.stdout, end='', flush=True); sys.exit(e.returncode)")
sha_b = lambda b: hashlib.sha256(b).hexdigest()
sha_f = lambda p: sha_b(open(p, 'rb').read())
RUN = os.path.join(FOLDER_P, 'run')


def say(text):
    print(text, flush=True)


def stop(step, why):
    say(f'STOPPED at {step}: {why}. Nothing is rewritten.')
    sys.exit(1)


def keep(name, text):
    with open(os.path.join(OUT, name), 'x', encoding='utf-8') as f:
        f.write(text)


def flat(d, pre=''):
    for k, v in d.items():
        yield from (flat(v, f'{pre}{k}.') if isinstance(v, dict) else [(f'{pre}{k}', v)])


def git(*a):
    return subprocess.run(['git', '-C', WT] + list(a), capture_output=True, check=True).stdout


go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))
ruling = json.load(open(os.path.join(ROOTB, 'launch_refusal_ask_v2', 'ruling', 'ruling.json'), encoding='utf-8'))
LINK = ruling['html_url']
assert ruling['user']['login'] == 'xrodz' and f"]({go['html_url']})" in ruling['body'] and "this ruling's link" in ruling['body']
sums_h = re.findall(r'\b[0-9a-f]{64}\b', go['body'])[1]
FULL = git('rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').decode().strip()
os.makedirs(OUT, exist_ok=True)
assert not os.listdir(OUT), 'OUT holds files already'
say(f'the folder: {FOLDER_P}\nthe first freeze kept in: {DEST}\nthe ruling: {LINK}\nthe go: {go["html_url"]}')

# before (a): the first freeze in place and valid
F1 = json.load(open(os.path.join(RUN, 'FROZEN.json')))
pin1 = open(os.path.join(RUN, 'FROZEN_PIN')).read().strip()
first = {f: (sha_f(os.path.join(RUN, f)), os.stat(os.path.join(RUN, f)).st_mtime_ns) for f in OWN}
if pin1 != first['FROZEN.json'][0] or F1['pins']['run/ENVIRONMENT.json'] != first['ENVIRONMENT.json'][0] or F1['go'] != go['html_url']:
    stop('the start', 'the first freeze is not as written')
if os.path.exists(DEST) or os.path.exists(os.path.join(RUN, 'out')):
    stop('the start', 'the keeping place exists, or run/out/ does')

# (a) the first freeze's three files moved out of run/
os.makedirs(os.path.join(DEST, 'run'))
for f in OWN:
    os.rename(os.path.join(RUN, f), os.path.join(DEST, 'run', f))
moved = {f: (sha_f(os.path.join(DEST, 'run', f)), os.stat(os.path.join(DEST, 'run', f)).st_mtime_ns) for f in OWN}
if moved != first or any(os.path.exists(os.path.join(RUN, f)) for f in OWN):
    stop('(a)', 'a moved file differs from what it was, or is still in run/')
say('\n(a) the first freeze moved out of run/, each byte and time unchanged:')
for f in OWN:
    say(f'    run/{f} -> {os.path.relpath(os.path.join(DEST, "run", f), ROOTB)}  {moved[f][0]}')

# (b) the folder against SHA256SUMS at the folder commit, and its files the commit's tree
sums = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=FOLDER_P, capture_output=True, text=True)
listed = [ln.split('  ', 1)[1] for ln in open(os.path.join(FOLDER_P, 'SHA256SUMS'), encoding='utf-8').read().splitlines()]
n_ok = sum(ln.endswith(': OK') for ln in sums.stdout.splitlines())
keep('sha256sums_check.out', f'$ shasum -a 256 -c SHA256SUMS\n{sums.stdout}exit {sums.returncode}\n')
files = sorted(os.path.relpath(os.path.join(dp, f), FOLDER_P) for dp, dn, fn in os.walk(FOLDER_P) for f in fn)
tree = sorted(p[len(MITF) + 1:] for p in git('ls-tree', '-r', '--name-only', FULL, '--', MITF + '/').decode().split('\n') if p)
if sums.returncode != 0 or n_ok != len(listed) or sha_f(os.path.join(FOLDER_P, 'SHA256SUMS')) != sums_h or files != tree:
    stop('(b)', f'{n_ok} of {len(listed)} OK; the copy is the tree: {files == tree}')
say(f'\n(b) shasum -a 256 -c SHA256SUMS: {n_ok} of {len(listed)} OK, exit 0; SHA256SUMS at the go\'s SHA-256; '
    f'the folder\'s {len(files)} files are the tree at {FULL[:8]}, nothing else')

# (c) the environment recorded once more, by the launch's route
cmd_c = [sys.executable, '-I', '-B', '-c', ROUTE]
p = subprocess.run(cmd_c, cwd=FOLDER_P, capture_output=True, text=True)
keep('record_environment.out', f'$ (from the folder) {sys.executable} -I -B -c "{ROUTE}"\n{p.stdout}{p.stderr}exit {p.returncode}\n')
if p.returncode != 0:
    stop('(c)', 'the recording failed')
e1 = json.load(open(os.path.join(DEST, 'run', 'ENVIRONMENT.json')))
e2 = json.load(open(os.path.join(RUN, 'ENVIRONMENT.json')))
fa, fb = dict(flat(e1)), dict(flat(e2))
diff = sorted(k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k))
want = ['recorded'] + [f'threading.{t}' for t in THREADS]
say(f'\n(c) recorded by the launch\'s route, from the folder:\n    {sys.executable} -I -B -c "{ROUTE}"\n'
    f'    run/ENVIRONMENT.json {sha_f(os.path.join(RUN, "ENVIRONMENT.json"))}, recorded {e2["recorded"]}\n'
    f'    against the first: {diff}; threading {e2["threading"]}')
if diff != want or any(e2['threading'][t] != '1' for t in THREADS):
    stop('(c)', 'the new record differs from the first in more than the four threading fields and the time')

# (d) write_guard.py with the ruling's link, the terms read against the clone
cmd_d = [sys.executable, '-I', '-B', 'run/write_guard.py', LINK, '--terms-from', CLONE]
p = subprocess.run(cmd_d, cwd=FOLDER_P, capture_output=True, text=True)
keep('write_guard.out', f'$ (from the folder) {" ".join(cmd_d)}\n{p.stdout}{p.stderr}exit {p.returncode}\n')
if p.returncode != 0:
    stop('(d)', 'write_guard.py refused')
F2 = json.load(open(os.path.join(RUN, 'FROZEN.json')))
pin2 = open(os.path.join(RUN, 'FROZEN_PIN')).read().strip()
keys = sorted(k for k in set(F1) | set(F2) if k != 'pins' and F1.get(k) != F2.get(k))
pins = sorted(k for k in set(F1['pins']) | set(F2['pins']) if F1['pins'].get(k) != F2['pins'].get(k))
say(f'\n(d) {" ".join(cmd_d)}\n    {p.stdout.strip()}\n    run/FROZEN.json written {F2["written"]}, pin {pin2}\n'
    f'    against the first: fields {keys}; pins {pins}; {len(F2["pins"])} pins')
if (keys != ['go', 'written'] or pins != ['run/ENVIRONMENT.json'] or F2['go'] != LINK or pin2 != sha_f(os.path.join(RUN, 'FROZEN.json'))
        or F2['pins']['run/ENVIRONMENT.json'] != sha_f(os.path.join(RUN, 'ENVIRONMENT.json')) or list(F1) != list(F2)):
    stop('(d)', 'the second FROZEN.json differs from the first in more than the environment pin, written and go')

# (e) main()'s two calls before launch(), replayed without launch()
cmd_e = [sys.executable, '-I', '-B', '-c', REPLAY]
p = subprocess.run(cmd_e, cwd=FOLDER_P, capture_output=True, text=True)
keep('replay_main_checks.out', f'$ (from the folder) {sys.executable} -I -B -c "{REPLAY}"\n{p.stdout}{p.stderr}exit {p.returncode}\n')
last = p.stdout.rstrip('\n').split('\n')[-1] if p.stdout else ''
say(f'\n(e) replayed: {p.stdout.splitlines()[0] if p.stdout else p.stderr[-200:]}\n    {last}; exit {p.returncode}')
if p.returncode != 0 or last != 'differences: none' or not p.stdout.startswith(f"validate_frozen: passed; {len(F2['pins'])} pins; go {LINK}"):
    stop('(e)', 'a replayed call refused')

# after: the folder's files, and SHA256SUMS read again
files = sorted(os.path.relpath(os.path.join(dp, f), FOLDER_P) for dp, dn, fn in os.walk(FOLDER_P) for f in fn)
sums = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=FOLDER_P, capture_output=True, text=True)
keep('sha256sums_check_after.out', f'$ shasum -a 256 -c SHA256SUMS\n{sums.stdout}exit {sums.returncode}\n')
n_ok = sum(ln.endswith(': OK') for ln in sums.stdout.splitlines())
if files != sorted(tree + [f'run/{f}' for f in OWN]) or sums.returncode != 0 or n_ok != len(listed) or os.path.exists(os.path.join(RUN, 'out')):
    stop('the end', 'the folder holds more than the tree and the second freeze, or SHA256SUMS fails')
say(f'\nafter: the folder is the tree and the second freeze\'s three files; SHA256SUMS {n_ok} of {len(listed)} OK; no run/out/')
say('freeze_2: DONE')
