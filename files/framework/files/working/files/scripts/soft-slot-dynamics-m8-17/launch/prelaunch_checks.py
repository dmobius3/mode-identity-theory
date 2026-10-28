#!/usr/bin/env python3
"""M8.17's checks before the launch (FILING_PLAN.md step 3), read-only: the frozen tree, the environment, the resume
check's reviewed bytes, no run in progress, the machine's power, and, given the freeze block's pull request number, the
pull request open with DCO passing and its block equal to the bench's. It prints the launch command as DEVLOG.md
entry 26 records it. Exit status 1 if any check fails; lines marked "info" are read for the record and decide nothing.

Usage: prelaunch_checks.py [PR_NUMBER]
"""
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, 'soft-slot-dynamics-m8-17')
BLOCK = os.path.join(HERE, 'freeze_block.md')
BLOCK_PATH = 'openwave/xperiments/m8_mit/research/m8_17/freeze_block.md'
fails = []


def fsha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def run(*a, **k):
    return subprocess.run(list(a), capture_output=True, text=True, **k)


def check(ok, what):
    print(('ok    ' if ok else 'FAIL  ') + what)
    if not ok:
        fails.append(what)


def info(what):
    print('info  ' + what)


dev = open(os.path.join(F, 'DEVLOG.md'), encoding='utf-8').read()
e26 = dev[dev.index('\n## 26.'):]
cmd = re.search(r'\n```\n(set -o pipefail; caffeinate .*)\n```\n', e26).group(1)
reviewed = re.search(r"printf '%s  %s\\n' ([0-9a-f]{64}) \.\./resume_check/resume_check\.py", cmd).group(1)

os.chdir(F)
sys.path.insert(0, F)
sys.path.insert(0, os.path.join(F, 'run'))
from instrument import devtools  # noqa: E402
import census  # noqa: E402

check(isinstance(devtools.frozen(F), dict) and census.frozen() == devtools.frozen(F), 'both admissions: devtools.frozen() and census.frozen()')
check(devtools.manifest(F)[1] == open('run/MANIFEST_PIN').read().strip(), 'the manifest equals the pin')
check(fsha('run/FROZEN.json') == open('run/FROZEN_PIN').read().strip(), 'run/FROZEN_PIN is the SHA-256 of run/FROZEN.json')
e = run(sys.executable, '-I', '-B', 'run/record_environment.py', '--check')
check(e.returncode == 0 and e.stdout.rstrip().endswith('differences: none'), 'record_environment.py --check: no difference')
check(not os.path.exists('run/out'), 'run/out/ does not exist: this is the first launch')
p = run('pgrep', '-f', 'run/census.py')
check(p.stdout.strip() == '', 'no census run in progress')
pin_t = os.path.getmtime('run/FROZEN_PIN')
newer = sorted(os.path.relpath(os.path.join(r, f), F) for r, _, fs in os.walk(F) for f in fs
               if os.path.getmtime(os.path.join(r, f)) > pin_t)
check(newer == ['DEVLOG.md'], f"no file in the folder newer than run/FROZEN_PIN but DEVLOG.md: {', '.join(newer) or 'none'}")
check(fsha(os.path.join(HERE, 'resume_check', 'resume_check.py')) == reviewed, f'the resume check at its reviewed SHA-256, {reviewed[:8]}')
r = run(sys.executable, '-I', '-B', '../resume_check/resume_check.py', '.')
check(r.returncode == 0 and r.stdout.rstrip().endswith('PASS'), 'the resume check passes on the folder')
b = run('pmset', '-g', 'batt').stdout
check("'AC Power'" in b, 'on mains power: ' + b.splitlines()[0].strip() if b else 'pmset gave nothing')
a = run('pmset', '-g', 'assertions').stdout
info('Caffeine: ' + ('holds an assertion' if 'Caffeine' in a else 'no assertion seen'))
s = [l.strip() for l in run('pmset', '-g').stdout.splitlines() if re.match(r'\s*(sleep|disksleep|displaysleep)\s', l)]
info('pmset: ' + '; '.join(s))
u = run('softwareupdate', '--schedule').stdout.strip()
info('software update: ' + (u or 'no reading'))
st = os.statvfs(F)
info(f'free disk space: {st.f_bavail * st.f_frsize / 1e9:.0f} GB')

if len(sys.argv) > 1:
    n = sys.argv[1]
    pr = json.loads(run('gh', 'api', f'repos/openwave-labs/openwave/pulls/{n}').stdout)
    head, merged = pr['head']['sha'], bool(pr.get('merged'))
    check((pr['state'] == 'open' or merged) and pr['base']['repo']['full_name'] == 'openwave-labs/openwave' and pr['base']['ref'] == 'main',
          f"#{n} is {'merged, as ' + pr['merge_commit_sha'][:8] + ',' if merged else 'open'} against openwave-labs/openwave main, head {pr['head']['ref']} at {head[:8]}")
    files = json.loads(run('gh', 'api', f'repos/openwave-labs/openwave/pulls/{n}/files').stdout)
    check([f['filename'] for f in files] == [BLOCK_PATH], f'#{n} changes one file, the block')

    def block_at(repo, ref):
        return subprocess.run(['gh', 'api', '-H', 'Accept: application/vnd.github.raw', f'repos/{repo}/contents/{BLOCK_PATH}?ref={ref}'],
                              capture_output=True).stdout

    check(hashlib.sha256(block_at('openwave-labs/openwave' if merged else pr['head']['repo']['full_name'], head)).hexdigest() == fsha(BLOCK),
          "the block at the pull request's head equals the bench's, byte for byte")
    if merged:
        check(hashlib.sha256(block_at('openwave-labs/openwave', 'main')).hexdigest() == fsha(BLOCK),
              "the block on OpenWave main equals the bench's, byte for byte")
    runs = json.loads(run('gh', 'api', f'repos/openwave-labs/openwave/commits/{head}/check-runs').stdout)['check_runs']
    dco = [c for c in runs if c['name'] == 'DCO']
    check(len(dco) == 1 and dco[0]['status'] == 'completed' and dco[0]['conclusion'] == 'success', f"DCO passes on {head[:8]}")
else:
    info('the pull request: not given, so not checked')

print('the launch command, from the folder, as DEVLOG.md entry 26 records it:')
print('      ' + cmd)
print(f'{len(fails)} failed')
sys.exit(1 if fails else 0)
