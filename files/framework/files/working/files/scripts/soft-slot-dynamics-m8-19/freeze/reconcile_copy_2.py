"""M8.19: the end of reconcile_copy.py, which stopped after its fourth move: its list of .staging folders, taken before
any move, held those inside the two scratch folders, already moved with them. This moves the .staging folders still in
the copy, directly under dev/runs/, then reads back as reconcile_copy.py would have."""
import hashlib, json, os, re, subprocess

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
F = json.load(open(os.path.join(B, 'run', 'FROZEN.json')))

runs = os.path.join(B, 'dev', 'runs')
left = sorted(os.path.join('dev', 'runs', d, '.staging') for d in os.listdir(runs) if os.path.isdir(os.path.join(runs, d, '.staging')))
for rel in left:
    src, dst = os.path.join(B, rel), os.path.join(ASIDE, rel)
    assert not os.listdir(src) and not os.path.exists(dst) and not any(p.startswith(rel + '/') for p in listed), rel
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    os.rename(src, dst)
    print(f'moved {rel} (empty) to ../bench_scratch_aside/{rel}')

files = sorted(os.path.relpath(os.path.join(dp, f), B) for dp, dn, fn in os.walk(B) for f in fn)
own = ['run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN']
tree = [p[len(FOLDER) + 1:] for p in git('ls-tree', '-r', '--name-only', FULL, '--', FOLDER + '/').decode().split('\n') if p]
assert sorted(set(files) - set(own)) == sorted(tree) and set(own) <= set(files), sorted(set(files) ^ (set(tree) | set(own)))[:5]
assert sorted(tree) == sorted(set(listed) | {'SHA256SUMS'})
empty = [os.path.relpath(dp, B) for dp, dn, fn in os.walk(B) if not dn and not fn]
assert not empty, empty
assert all(sha_b(open(os.path.join(B, p), 'rb').read()) == h for p, h in F['pins'].items())
assert sha_b(open(os.path.join(B, 'DEVLOG.md'), 'rb').read()) == listed['DEVLOG.md']
assert open(AFTER, 'rb').read().startswith(b'\n## 11. ')
aside = sum(len(fn) for _, _, fn in os.walk(ASIDE))
print(f"the copy: {len(files)} files, the commit's {len(tree)} and the freeze's 3; no empty folder; DEVLOG.md at its line; "
      f"the {len(F['pins'])} pinned files at their pins; {aside} files aside")
