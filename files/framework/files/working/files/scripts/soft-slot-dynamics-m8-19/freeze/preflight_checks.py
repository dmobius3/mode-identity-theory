"""M8.19's checks before the launch, read-only: the copy the run uses against the go's bytes and the freeze; the
instrument; OpenWave (the go, anything posted since, #702 and its DCO); the machine (mains power, Low Power Mode, the
lid and displays, sleep holds, macOS updates, scheduled power events); disk and load. Nothing is written but stdout.
Every hash and commit is read from the go as kept, from git or from FROZEN.json, none typed."""
import hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
INSTR = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x'
MATH = 'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_math'
CLONE = os.path.expanduser(os.environ['M819_OPENWAVE_CLONE_FROM_HOME'])
PR = 702
OWN = ('run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN')
fails = []


def ok(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


def info(text):
    print('      ' + text, flush=True)


def run(*a, check=True):
    return subprocess.run(a, capture_output=True, text=True, check=check).stdout


def gh(path, pages=False):
    return json.loads(run('gh', 'api', '--paginate', '--slurp', path) if pages else run('gh', 'api', path))


sha_f = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))
FULL = run('git', '-C', WT, 'rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').strip()
F = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))

print('== the copy the run uses')
sums = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=B, capture_output=True, text=True)
lines = sums.stdout.splitlines()
listed = [l.split('  ', 1)[1] for l in open(os.path.join(B, 'SHA256SUMS'), encoding='utf-8').read().splitlines()]
ok('shasum -a 256 -c SHA256SUMS: every listed file OK', sums.returncode == 0 and len(lines) == len(listed)
   and all(l.endswith(': OK') for l in lines), f'{sum(l.endswith(": OK") for l in lines)} of {len(listed)}')
files = sorted(os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn)
tree = sorted(p[len(FOLDER) + 1:] for p in run('git', '-C', WT, 'ls-tree', '-r', '--name-only', FULL, '--', FOLDER + '/').split('\n') if p)
ok("the copy's files are the commit's tree and the freeze's three, nothing else", files == sorted(tree + list(OWN)),
   sorted(set(files) ^ set(tree + list(OWN)))[:5] if files != sorted(tree + list(OWN)) else f'{len(tree)} + 3')
ok('no run/out/ yet', not os.path.exists(os.path.join(B, 'run', 'out')))
ok('no empty folder, cache or .DS_Store', not [dp for dp, dn, fn in os.walk(B) if (not dn and not fn) or os.path.basename(dp) == '__pycache__']
   and not [f for f in files if os.path.basename(f) == '.DS_Store'])
v = subprocess.run([sys.executable, '-I', '-B', '-c', 'import sys; sys.path.insert(0, "run"); import m819_branch as D; '
                    'F = D.validate_frozen(); print(len(F["pins"]), F["go"])'], cwd=B, capture_output=True, text=True)
ok("validate_frozen passes in a fresh process, with the go's link", v.returncode == 0 and v.stdout.split() == ['16', go['html_url']],
   (v.stdout + v.stderr).strip()[-200:])
e = subprocess.run([sys.executable, '-I', '-B', os.path.join(B, 'run', 'record_environment.py'), '--check'], capture_output=True, text=True)
ok('record_environment.py --check: no difference', e.returncode == 0 and e.stdout.rstrip().endswith('differences: none'))
ok('FROZEN_PIN holds FROZEN.json\'s SHA-256', open(os.path.join(B, 'run', 'FROZEN_PIN')).read().strip() == sha_f(os.path.join(B, 'run', 'FROZEN.json')))

print('== the instrument')
link = os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x')
ok("the bench's instrument link resolves to the worktree's instrument", os.path.realpath(link) == os.path.realpath(os.path.join(WT, INSTR)))
st = run('git', '-C', WT, 'status', '--porcelain', '--untracked-files=all', '--', INSTR, MATH, FOLDER).strip()
ok("the worktree's instrument, m8_15_math and M8.19 folder: nothing changed or untracked", st == '', st[:200])
ok("the worktree's copies equal the folder commit's", subprocess.run(['git', '-C', WT, 'diff', '--quiet', FULL, '--', INSTR, MATH, FOLDER]).returncode == 0)
ok('no cache in the instrument', not [dp for dp, dn, fn in os.walk(os.path.realpath(link)) if os.path.basename(dp) == '__pycache__'])

print('== OpenWave')
live = gh(f"repos/openwave-labs/openwave/issues/comments/{go['id']}")
ok('the go live equals its kept copy, unedited', live['body'] == go['body'] and live['created_at'] == live['updated_at'])
after = []
for path in ('repos/openwave-labs/openwave/issues/698/comments', f'repos/openwave-labs/openwave/issues/{PR}/comments',
             f'repos/openwave-labs/openwave/pulls/{PR}/comments', f'repos/openwave-labs/openwave/pulls/{PR}/reviews'):
    for page in gh(path, pages=True):
        for c in page:
            t = c.get('created_at') or c.get('submitted_at') or ''
            if t > go['created_at'] and c['id'] != go['id'] and c['user']['login'] != 'dmobius3':
                after.append((path.split('/')[-2] + '/' + path.split('/')[-1], c['user']['login'], t))
ok('nothing posted on #698 or #702 since the go by anyone else', not after, after)
pr = gh(f'repos/openwave-labs/openwave/pulls/{PR}')
head = run('git', '-C', CLONE, 'rev-parse', 'm8-19-freeze-block-2026-11-09').strip()
ok(f'#{PR} open, its head the freeze block\'s commit', pr['state'] == 'open' and pr['head']['sha'] == head, f"{pr['state']}, merged {pr['merged']}")
runs = gh(f"repos/openwave-labs/openwave/commits/{head}/check-runs")['check_runs']
ok(f'#{PR}: DCO passes', [r['conclusion'] for r in runs if r['name'] == 'DCO'] == ['success'])

print('== the machine')
batt = run('pmset', '-g', 'batt')
ok('on mains power', "Now drawing from 'AC Power'" in batt, batt.splitlines()[0] if batt else '')
info(batt.splitlines()[1].strip() if len(batt.splitlines()) > 1 else 'no battery line')
pm = run('pmset', '-g')
lpm = re.search(r'lowpowermode\s+(\d)', pm)
ok('Low Power Mode off', bool(lpm) and lpm.group(1) == '0', lpm.group(0) if lpm else 'no lowpowermode line')
info('pmset: ' + '; '.join(m.group(0) for m in re.finditer(r'^\s*(sleep|displaysleep|disksleep|standby|powernap|hibernatemode)\s+\S+.*$', pm, re.M)).replace('  ', ' '))
clam = re.search(r'"AppleClamshellState" = (Yes|No)', run('ioreg', '-r', '-k', 'AppleClamshellState', '-d', '4'))
disp = json.loads(run('system_profiler', 'SPDisplaysDataType', '-json'))
names = [d.get('_name', '') for g in disp.get('SPDisplaysDataType', []) for d in g.get('spdisplays_ndrvs', [])]
builtin = [d for g in disp.get('SPDisplaysDataType', []) for d in g.get('spdisplays_ndrvs', [])
           if d.get('spdisplays_connection_type') == 'spdisplays_internal' or 'Built-in' in d.get('_name', '') or d.get('_name') == 'Color LCD']
external = len(names) - len(builtin)
lid = clam.group(1) if clam else 'unknown'
ok('awake with the lid as it is: open, or closed on mains with an external display', lid == 'No' or (lid == 'Yes' and external > 0 and "AC Power" in batt),
   f'lid closed: {lid}; displays: {names}')
asr = run('pmset', '-g', 'assertions')
holds = {k: int(v) for k, v in re.findall(r'^\s*(PreventUserIdleSystemSleep|PreventUserIdleDisplaySleep|PreventSystemSleep)\s+(\d)', asr, re.M)}
info(f'sleep holds now: {holds}; the orchestrator adds caffeinate -i -s -w on its own pid')
su = {k: run('defaults', 'read', '/Library/Preferences/com.apple.SoftwareUpdate', k, check=False).strip() or 'unset'
      for k in ('AutomaticDownload', 'AutomaticallyInstallMacOSUpdates', 'CriticalUpdateInstall', 'ConfigDataInstall')}
ok('no macOS update set to download or install by itself', su['AutomaticDownload'] in ('0', 'unset') and
   su['AutomaticallyInstallMacOSUpdates'] in ('0', 'unset') and su['CriticalUpdateInstall'] in ('0', 'unset'), su)
sched = run('pmset', '-g', 'sched').strip()
ok('no scheduled restart, shutdown or sleep', not re.search(r'restart|shutdown|sleep', sched, re.I), sched or 'none')
ver = run('sw_vers', '-productVersion').strip() + ' ' + run('sw_vers', '-buildVersion').strip()
env = json.load(open(os.path.join(B, 'run', 'ENVIRONMENT.json')))
ok("macOS is the environment record's", ver == f"{env['os']['version']} {env['os']['build']}", ver)

print('== disk and load')
s = os.statvfs(B)
free = s.f_bavail * s.f_frsize / 2 ** 30
ok('at least 20 GB free on the bench volume', free >= 20, f'{free:.0f} GB')
la = os.getloadavg()
me = {os.getpid(), os.getppid()}
procs = []
for l in run('ps', '-A', '-o', 'pid=,%cpu=,comm=').splitlines():
    pid, cpu, comm = l.split(None, 2)
    if int(pid) not in me:
        procs.append((float(cpu), int(pid), comm.strip()))
procs.sort(reverse=True)
info(f'load average {la[0]:.2f} {la[1]:.2f} {la[2]:.2f}; busiest: ' + '; '.join(f'{c:.0f}% {os.path.basename(n)}' for c, _, n in procs[:5]))
py = [(p, os.path.basename(n)) for c, p, n in procs if os.path.basename(n).startswith('python')]
info(f'other Python processes: {py if py else "none"}')
ok('no other process above 50% of a core', not [n for c, p, n in procs if c > 50], [(round(c), os.path.basename(n)) for c, p, n in procs if c > 50])

print('pre-flight:', 'PASS' if not fails else f'FAIL ({len(fails)}): {fails}')
sys.exit(1 if fails else 0)
