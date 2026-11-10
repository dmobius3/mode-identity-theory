"""M8.19's checks before the launch on the second freeze, after the second block's merge: preflight_checks_2.py, whose
first run stands with its output, with its OpenWave checks for #703 merged in place of open and the rest unchanged.
Read-only, on the form of the first's (../freeze/preflight_checks.py): the copy the run uses against the go's bytes and
the second freeze, with the environment check run by the launch's route, the driver imported first, as main() runs it,
since from the shell it now reads the four threading variables as unset against the record's 1; the first freeze as
kept; the instrument; OpenWave (the go, the ruling, nothing posted since but the approval, as kept and unedited, #702
merged, the second block's pull request merged at the pushed commit as kept, the block on main byte for byte, its DCO
check passed); the machine (mains power, Low Power Mode, the lid and displays, sleep holds, macOS updates, scheduled
power events); disk and load. Nothing is written but stdout. Every hash, link and commit is read from the go, the
ruling and the merge as kept, from git, from GitHub or from the files, none typed."""
import base64, hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
K = os.path.join(ROOTB, 'freeze', 'first_freeze', 'run')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
INSTR = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x'
MATH = 'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_math'
CLONE = os.path.expanduser(os.environ['M819_OPENWAVE_CLONE_FROM_HOME'])
BRANCH = 'm8-19-freeze-block-2-2026-11-10'
BLOCK2 = 'openwave/xperiments/m8_mit/research/m8_19/freeze_block_2.md'
OWN = ('run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN')
ROUTE_CHECK = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch as D; "
               "F = D.validate_frozen(); print(len(F['pins']), F['go'], flush=True); "
               "e = subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py'), '--check'], "
               "capture_output=True, text=True); print(e.stdout.rstrip().splitlines()[-1], flush=True); sys.exit(e.returncode)")
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
    d = json.loads(run('gh', 'api', '--paginate', '--slurp', path) if pages else run('gh', 'api', path))
    return [c for page in d for c in page] if pages else d


sha_f = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))
ru = json.load(open(os.path.join(ROOTB, 'launch_refusal_ask_v2', 'ruling', 'ruling.json'), encoding='utf-8'))
PRN = json.load(open(os.path.join(ROOTB, 'freeze_block_2_v2', 'posted', 'pr_new.json'), encoding='utf-8'))['number']
MRG = os.path.join(ROOTB, 'freeze_block_2_v2', 'posted', 'merged')
MK = json.load(open(os.path.join(MRG, 'pr.json'), encoding='utf-8'))
RK = json.load(open(os.path.join(MRG, 'reviews.json'), encoding='utf-8'))
FULL = run('git', '-C', WT, 'rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').strip()
F = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))
F1 = json.load(open(os.path.join(K, 'FROZEN.json')))

print('== the copy the run uses, on the second freeze')
sums = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=B, capture_output=True, text=True)
lines = sums.stdout.splitlines()
listed = [l.split('  ', 1)[1] for l in open(os.path.join(B, 'SHA256SUMS'), encoding='utf-8').read().splitlines()]
ok('shasum -a 256 -c SHA256SUMS: every listed file OK', sums.returncode == 0 and len(lines) == len(listed)
   and all(l.endswith(': OK') for l in lines), f'{sum(l.endswith(": OK") for l in lines)} of {len(listed)}')
files = sorted(os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn)
tree = sorted(p[len(FOLDER) + 1:] for p in run('git', '-C', WT, 'ls-tree', '-r', '--name-only', FULL, '--', FOLDER + '/').split('\n') if p)
ok("the copy's files are the commit's tree and the second freeze's three, nothing else", files == sorted(tree + list(OWN)),
   sorted(set(files) ^ set(tree + list(OWN)))[:5] if files != sorted(tree + list(OWN)) else f'{len(tree)} + 3')
ok('no run/out/ yet', not os.path.exists(os.path.join(B, 'run', 'out')))
ok('no empty folder, cache or .DS_Store', not [dp for dp, dn, fn in os.walk(B) if (not dn and not fn) or os.path.basename(dp) == '__pycache__']
   and not [f for f in files if os.path.basename(f) == '.DS_Store'])
ok("FROZEN.json at FROZEN_PIN, with the ruling's link as its go", open(os.path.join(B, 'run', 'FROZEN_PIN')).read().strip() == sha_f(os.path.join(B, 'run', 'FROZEN.json'))
   and F['go'] == ru['html_url'])
v = subprocess.run([sys.executable, '-I', '-B', '-c', ROUTE_CHECK], cwd=B, capture_output=True, text=True)
ok("by the launch's route, in a fresh process: validate_frozen passes with the ruling's link, and the environment check reads no difference",
   v.returncode == 0 and v.stdout.split('\n')[:2] == [f"16 {ru['html_url']}", 'differences: none'], (v.stdout + v.stderr).strip()[-300:])
ok('the first freeze kept, its three files at the pins #702 records',
   sorted(os.listdir(K)) == ['ENVIRONMENT.json', 'FROZEN.json', 'FROZEN_PIN'] and open(os.path.join(K, 'FROZEN_PIN')).read().strip() == sha_f(os.path.join(K, 'FROZEN.json'))
   and F1['pins']['run/ENVIRONMENT.json'] == sha_f(os.path.join(K, 'ENVIRONMENT.json')) and F1['go'] == go['html_url'])

print('== the instrument')
link = os.path.join(ROOTB, 'soft-slot-dynamics-m8-15x')
ok("the bench's instrument link resolves to the worktree's instrument", os.path.realpath(link) == os.path.realpath(os.path.join(WT, INSTR)))
st = run('git', '-C', WT, 'status', '--porcelain', '--untracked-files=all', '--', INSTR, MATH, FOLDER).strip()
ok("the worktree's instrument, m8_15_math and M8.19 folder: nothing changed or untracked", st == '', st[:200])
ok("the worktree's copies equal the folder commit's", subprocess.run(['git', '-C', WT, 'diff', '--quiet', FULL, '--', INSTR, MATH, FOLDER]).returncode == 0)
ok('no cache in the instrument', not [dp for dp, dn, fn in os.walk(os.path.realpath(link)) if os.path.basename(dp) == '__pycache__'])

print('== OpenWave')
for name, kept in (('the go', go), ('the ruling', ru)):
    live = gh(f"repos/openwave-labs/openwave/issues/comments/{kept['id']}")
    ok(f'{name} live equals its kept copy, unedited', live['body'] == kept['body'] and live['created_at'] == live['updated_at'])
after, ours, approval = [], [], []
for path in ('issues/698/comments', 'issues/702/comments', f'issues/{PRN}/comments', f'pulls/{PRN}/comments', f'pulls/{PRN}/reviews'):
    for c in gh(f'repos/openwave-labs/openwave/{path}', pages=True):
        t = c.get('created_at') or c.get('submitted_at') or ''
        if t > ru['created_at']:
            if path == f'pulls/{PRN}/reviews' and len(RK) == 1 and c['id'] == RK[0]['id']:
                approval.append(c)
            else:
                (ours if c['user']['login'] == 'dmobius3' else after).append((path, c['user']['login'], t))
ok(f'nothing posted on #698, #702 or #{PRN} since the ruling by anyone else but the approval', not after, after)
info(f'ours since the ruling: {ours if ours else "none"}')
Q = 'query($o:String!,$n:String!,$p:Int!){repository(owner:$o,name:$n){pullRequest(number:$p){reviews(first:20){nodes{databaseId lastEditedAt}}}}}'
edits = {n['databaseId']: n['lastEditedAt'] for n in json.loads(run('gh', 'api', 'graphql', '-f', f'query={Q}', '-f', 'o=openwave-labs',
         '-f', 'n=openwave', '-F', f'p={PRN}'))['data']['repository']['pullRequest']['reviews']['nodes']}
a = approval[0] if len(approval) == 1 else {}
ok(f"the approval, as kept and unedited: by #{PRN}'s merger, on the pushed commit, before the merge", len(RK) == 1 and len(approval) == 1
   and a['state'] == 'APPROVED' == RK[0]['state'] and a['body'] == RK[0]['body'] and a['commit_id'] == RK[0]['commit_id'] == MK['head']['sha']
   and a['user']['login'] == RK[0]['user']['login'] == MK['merged_by']['login'] and a['submitted_at'] == RK[0]['submitted_at'] <= MK['merged_at']
   and a['id'] in edits and edits[a['id']] is None, f"{a.get('state')} by {(a.get('user') or {}).get('login')} at {a.get('submitted_at')}")
p702 = gh('repos/openwave-labs/openwave/pulls/702')
ok('#702 merged, as the record of the first freeze', p702['merged'] and p702['state'] == 'closed')
pr = gh(f'repos/openwave-labs/openwave/pulls/{PRN}')
head = run('git', '-C', CLONE, 'rev-parse', BRANCH).strip()
fork = run('git', '-C', CLONE, 'ls-remote', 'origin', f'refs/heads/{BRANCH}').split('\t')[0]
mc = gh(f"repos/openwave-labs/openwave/git/commits/{pr['merge_commit_sha']}") if pr.get('merged') else {}
ok(f"#{PRN} merged as kept, its head the second block's commit, as pushed", pr['merged'] is True and pr['state'] == 'closed'
   and pr['head']['sha'] == head == MK['head']['sha'] and fork in (head, '') and pr['base']['ref'] == 'main'
   and pr['merge_commit_sha'] == MK['merge_commit_sha'] and pr['merged_at'] == MK['merged_at']
   and [p['sha'] for p in mc.get('parents', [])] == [MK['base']['sha'], head],
   f"{pr['state']}, merged {pr['merged']}, head {pr['head']['sha'][:8]}, the fork's branch {fork[:8] if fork else 'deleted'}")
blk = open(os.path.join(ROOTB, 'freeze_block_2_v2', 'freeze_block_2.md'), 'rb').read()
om = base64.b64decode(gh(f'repos/openwave-labs/openwave/contents/{BLOCK2}?ref=main')['content'])
ok("the second block on OpenWave's main, byte for byte", om == blk, hashlib.sha256(om).hexdigest()[:8])
pf = gh(f'repos/openwave-labs/openwave/pulls/{PRN}/files', pages=True)
ok(f"#{PRN} adds the second block alone", [(f['filename'], f['status']) for f in pf] == [(BLOCK2, 'added')])
runs = gh(f"repos/openwave-labs/openwave/commits/{head}/check-runs")['check_runs']
ok(f'#{PRN}: DCO passes', [r['conclusion'] for r in runs if r['name'] == 'DCO'] == ['success'])
info(f"#{PRN} opened {pr['created_at']}, merged {pr['merged_at']}; the second freeze written {F['written']}")

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
left = [l for l in run('ps', '-A', '-o', 'pid=,command=').splitlines() if 'm819_branch.py' in l or 'm819_run.py' in l]
ok('no M8.19 driver or orchestrator process running', not left, left)

print('pre-flight 2, after the merge:', 'PASS' if not fails else f'FAIL ({len(fails)}): {fails}')
sys.exit(1 if fails else 0)
