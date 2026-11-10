"""M8.19: the run's copy of the folder brought back to the go's bytes before the launch (UA's custody point on the
freeze block, v1). DEVLOG.md returns to its blob at the folder commit, and the entries appended since the check, entry 11
on, are kept beside the folder in ../DEVLOG_after_freeze.md, byte for byte, until the run's record is published; the
tests' scratch, which no line of SHA256SUMS lists, moves beside the folder too, in ../bench_scratch_aside/. Nothing is
deleted and no pinned file is touched. Every check is read back."""
import hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
ASIDE = os.path.join(ROOTB, 'bench_scratch_aside')
AFTER = os.path.join(ROOTB, 'DEVLOG_after_freeze.md')
sha_b = lambda b: hashlib.sha256(b).hexdigest()
git = lambda *a: subprocess.run(['git', '-C', WT] + list(a), capture_output=True, check=True).stdout

go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))['body']
FULL = git('rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go).group(1) + '^{commit}').decode().strip()
listed = {p: h for h, p in (l.split('  ', 1) for l in open(os.path.join(B, 'SHA256SUMS'), encoding='utf-8').read().splitlines())}
pins_before = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))['pins']
pinned_sha = {p: sha_b(open(os.path.join(B, p), 'rb').read()) for p in pins_before}

# 1. DEVLOG.md: the committed bytes back, the suffix kept beside the folder
dl = os.path.join(B, 'DEVLOG.md')
now_b = open(dl, 'rb').read()
blob = git('show', f'{FULL}:{FOLDER}/DEVLOG.md')
assert sha_b(blob) == listed['DEVLOG.md'] and now_b.startswith(blob) and len(now_b) > len(blob)
suffix = now_b[len(blob):]
assert suffix.startswith(b'\n## 11. ') and suffix.count(b'\n## ') == 1, 'only entry 11 is expected after the commit'
with open(AFTER, 'xb') as f:
    f.write(suffix)
assert open(AFTER, 'rb').read() == suffix
tmp = dl + '.restore.tmp'
with open(tmp, 'xb') as f:
    f.write(blob)
os.replace(tmp, dl)
assert sha_b(open(dl, 'rb').read()) == listed['DEVLOG.md'] and blob + open(AFTER, 'rb').read() == now_b
print(f'DEVLOG.md back at its blob ({len(blob)} bytes); entry 11, {len(suffix)} bytes, kept in ../DEVLOG_after_freeze.md')

# 2. the scratch no line lists, moved beside the folder with its relative paths
moves = ['dev/runs/launch_tests', 'dev/runs/scope_tests'] + sorted(
    os.path.relpath(os.path.join(dp, d), B) for dp, dn, fn in os.walk(os.path.join(B, 'dev', 'runs')) for d in dn if d == '.staging')
for rel in moves:
    src, dst = os.path.join(B, rel), os.path.join(ASIDE, rel)
    assert not any(p == rel or p.startswith(rel + '/') for p in listed), rel
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    assert not os.path.exists(dst)
    os.rename(src, dst)
    n = sum(len(fn) for _, _, fn in os.walk(dst))
    print(f'moved {rel} ({n} files) to ../bench_scratch_aside/{rel}')

# 3. read back: the copy's files are the list's, SHA256SUMS and the freeze's three; no empty folder; pins untouched
files = sorted(os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn)
own = ['run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN']
tree = sorted(git('ls-tree', '-r', '--name-only', FULL, '--', FOLDER + '/').decode().split('\n')[:-1])
tree = [p[len(FOLDER) + 1:] for p in tree]
assert files == sorted(set(listed) | {'SHA256SUMS'} | set(own)), sorted(set(files) ^ (set(listed) | {'SHA256SUMS'} | set(own)))[:5]
assert sorted(set(files) - set(own)) == tree, 'the copy, but the freeze\'s three, is the commit\'s tree'
empty = [os.path.relpath(dp, B) for dp, dn, fn in os.walk(B) if not dn and not fn]
assert not empty, empty
assert all(sha_b(open(os.path.join(B, p), 'rb').read()) == h for p, h in pinned_sha.items())
print(f'the copy: {len(files)} files, the commit\'s {len(tree)} and the freeze\'s 3; no empty folder; the 16 pinned files untouched')
