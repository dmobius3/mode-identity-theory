#!/usr/bin/env python3
"""Mutation arms for preflight_checks_2_merged.py's revised checks, the OpenWave ones for the merge. Each arm is a copy
of it, in a new folder under SCRATCH, with one change; each must fail the control's failures and exactly its named
checks besides, and the control, unchanged, must fail none but the machine's (power and Low Power Mode, while on
battery). Nothing is written outside SCRATCH.

Usage: python3 -I -B -u mutations_preflight_2_merged.py SCRATCH"""
import ast, os, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, 'preflight_checks_2_merged.py'), encoding='utf-8').read()
SCRATCH = os.path.abspath(sys.argv[1])
POSTED = 'since the ruling by anyone else but the approval'
APPROVAL = 'the approval, as kept and unedited'
MERGED = 'merged as kept, its head'
ONMAIN = "the second block on OpenWave's main, byte for byte"
MACHINE = {'on mains power', 'Low Power Mode off'}
A_LINE = "a = approval[0] if len(approval) == 1 else {}\n"
ARMS = [
    ('the control, unchanged', None, None, set()),
    ("the kept approval's id one more",
     "RK = json.load(open(os.path.join(MRG, 'reviews.json'), encoding='utf-8'))\n",
     "RK = json.load(open(os.path.join(MRG, 'reviews.json'), encoding='utf-8'))\nRK[0]['id'] += 1\n", {POSTED, APPROVAL}),
    ('the approval read as dismissed', A_LINE, A_LINE + "a = dict(a, state='DISMISSED')\n", {APPROVAL}),
    ("the approval's body read with a space more", A_LINE, A_LINE + "a = dict(a, body=a['body'] + ' ')\n", {APPROVAL}),
    ('the approval read as edited at the merge', A_LINE, A_LINE + "edits = {k: MK['merged_at'] for k in edits}\n", {APPROVAL}),
    ('the pull request read as open',
     "pr = gh(f'repos/openwave-labs/openwave/pulls/{PRN}')\n",
     "pr = gh(f'repos/openwave-labs/openwave/pulls/{PRN}')\npr = dict(pr, merged=False, state='open')\n", {MERGED}),
    ("the kept merge commit taken as main before the merge",
     "MK = json.load(open(os.path.join(MRG, 'pr.json'), encoding='utf-8'))\n",
     "MK = json.load(open(os.path.join(MRG, 'pr.json'), encoding='utf-8'))\nMK['merge_commit_sha'] = MK['base']['sha']\n", {MERGED}),
    ('a byte appended to the pushed block',
     "blk = open(os.path.join(ROOTB, 'freeze_block_2_v2', 'freeze_block_2.md'), 'rb').read()\n",
     "blk = open(os.path.join(ROOTB, 'freeze_block_2_v2', 'freeze_block_2.md'), 'rb').read() + b'x'\n", {ONMAIN}),
]
control, bad = None, []
for name, old, new, want in ARMS:
    if old is not None:
        assert SRC.count(old) == 1, name
    d = tempfile.mkdtemp(prefix='arm_', dir=SCRATCH)
    script = os.path.join(d, 'preflight_checks_2_merged.py')
    with open(script, 'x', encoding='utf-8') as f:
        f.write(SRC if old is None else SRC.replace(old, new))
    t0 = time.time()
    p = subprocess.run([sys.executable, '-I', '-B', '-u', script], capture_output=True, text=True)
    with open(os.path.join(d, 'out.txt'), 'x', encoding='utf-8') as f:
        f.write(p.stdout + p.stderr)
    last = p.stdout.rstrip('\n').split('\n')[-1]
    got = set() if last.endswith(': PASS') else set(ast.literal_eval(last.split(': ', 2)[-1])) if ': FAIL (' in last else None
    if old is None:
        control = got
        good = got is not None and got <= MACHINE and p.returncode == (1 if got else 0)
        said = f'fails only the machine\'s: {sorted(got)}' if good else last + p.stderr[-300:]
    else:
        extra = got - control if got is not None and control is not None else None
        good = (extra is not None and control <= got and len(extra) == len(want)
                and all(any(w in g for g in extra) for w in want) and p.returncode == 1)
        said = f'red on {sorted(extra)} besides the control\'s' if extra is not None else last + p.stderr[-300:]
    print(('ok    ' if good else 'BAD   ') + name + ': ' + said + f' ({time.time() - t0:.0f} s)', flush=True)
    if not good:
        bad.append(name)
print('mutations_preflight_2_merged:', f'PASS {len(ARMS) - 1} arms and the control' if not bad else f'BAD {bad}')
sys.exit(1 if bad else 0)
