#!/usr/bin/env python3
"""Mutation arms for merge_703.py. Each arm is a copy of it, in a new folder under SCRATCH, with one change, run with
its read-back in that folder; each must fail exactly its named checks, and the control, unchanged, must pass. Nothing is
written outside SCRATCH.

Usage: python3 -I -B -u mutations_merge_703.py SCRATCH"""
import ast, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, 'merge_703.py'), encoding='utf-8').read()
SCRATCH = os.path.abspath(sys.argv[1])
BLOCK_EQ = 'the block at the merge commit equals the pushed block, byte for byte'
PINS = 'the pins it restates, five, each equal to ours'
SHORTS = 'each short hash it gives names one of ours'
POSTED = 'nothing else posted on #'
TIMES = 'the times it gives: '
EDITED = 'the review never edited'
TREE = "its tree the pushed commit's tree"
ARMS = [
    ('the control, unchanged', None, None, set()),
    ('a byte appended to the pushed block',
     "blk = open(os.path.join(P, 'freeze_block_2.md'), 'rb').read()\n",
     "blk = open(os.path.join(P, 'freeze_block_2.md'), 'rb').read() + b'x'\n", {BLOCK_EQ, PINS}),
    ("the second FROZEN.json's hash taken from the first's",
     "'FROZEN.json': sha_f(os.path.join(B, 'run', 'FROZEN.json')),",
     "'FROZEN.json': sha_f(os.path.join(K, 'FROZEN.json')),", {PINS, SHORTS}),
    ("the ruling's time moved to the start of its day",
     "go = json.loads(rd(os.path.join(ROOTB, 'go_request_v1', 'go.json')))\n",
     "go = json.loads(rd(os.path.join(ROOTB, 'go_request_v1', 'go.json')))\nru['created_at'] = ru['created_at'][:11] + '00:00:00Z'\n",
     {POSTED, TIMES}),
    ('the review read as edited at the merge',
     "rn = gpr['reviews']['nodes']\n",
     "rn = gpr['reviews']['nodes']\nrn[0]['lastEditedAt'] = mc['committer']['date']\n", {EDITED}),
    ("the merge commit's tree taken from main before the merge",
     "hc = gh(f'{REPO}/git/commits/{HEAD}')\n",
     "hc = gh(f'{REPO}/git/commits/{HEAD}')\nmc['tree'] = gh(f\"{REPO}/git/commits/{opened['base']['sha']}\")['tree']\n", {TREE}),
    ("the review's first short hash one digit off",
     "shorts = re.findall(r'`([0-9a-f]{8})…`', body)\n",
     "shorts = [s[:7] + ('0' if s[7] != '0' else '1') if i == 0 else s for i, s in enumerate(re.findall(r'`([0-9a-f]{8})…`', body))]\n",
     {SHORTS}),
]
bad = []
for name, old, new, want in ARMS:
    if old is not None:
        assert SRC.count(old) == 1, name
    d = tempfile.mkdtemp(prefix='arm_', dir=SCRATCH)
    script = os.path.join(d, 'merge_703.py')
    with open(script, 'x', encoding='utf-8') as f:
        f.write(SRC if old is None else SRC.replace(old, new))
    p = subprocess.run([sys.executable, '-I', '-B', '-u', script, os.path.join(d, 'dest')], capture_output=True, text=True)
    last = p.stdout.rstrip('\n').split('\n')[-1]
    got = set() if last.endswith(': PASS') else set(ast.literal_eval(last.split(': ', 2)[-1])) if ': FAIL (' in last else None
    match = got is not None and len(got) == len(want) and all(any(g.startswith(w) for g in got) for w in want)
    good = match and p.returncode == (0 if not want else 1) and os.path.isdir(os.path.join(d, 'dest'))
    print(('ok    ' if good else 'BAD   ') + name + ': ' + (f'red on {sorted(got)}' if got else 'passes' if got == set() else last + p.stderr[-300:]), flush=True)
    if not good:
        bad.append(name)
print('mutations_merge_703:', f'PASS {len(ARMS) - 1} arms and the control' if not bad else f'BAD {bad}')
sys.exit(1 if bad else 0)
