"""M8.19: the bench folder brought to the folder commit's tree before the SHA256SUMS check. It writes, by exclusive
create and from their blobs at the commit the go names, the files the bench lacks: registration/'s, and SHA256SUMS."""
import hashlib, json, os, re, subprocess, sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
run = lambda *a: subprocess.run(a, capture_output=True, check=True).stdout
sha_b = lambda b: hashlib.sha256(b).hexdigest()

go = json.load(open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8'))['body']
sums_h = re.findall(r'\b[0-9a-f]{64}\b', go)[1]
FULL = run('git', '-C', WT, 'rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go).group(1) + '^{commit}').decode().strip()
sums = run('git', '-C', WT, 'show', f'{FULL}:{FOLDER}/SHA256SUMS')
assert sha_b(sums) == sums_h, 'SHA256SUMS at the commit is not at the go'
listed = {p: h for h, p in (l.split('  ', 1) for l in sums.decode('utf-8').splitlines())}
want = sorted(p for p in listed if not os.path.exists(os.path.join(B, p)))
assert want and all(p.startswith('registration/') for p in want), want
plan = [(p, run('git', '-C', WT, 'show', f'{FULL}:{FOLDER}/{p}'), listed[p]) for p in want] + [('SHA256SUMS', sums, sums_h)]
for p, data, h in plan:
    assert sha_b(data) == h, p
    mode = run('git', '-C', WT, 'ls-tree', FULL, '--', f'{FOLDER}/{p}').decode().split()[0]
    dst = os.path.join(B, p)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'xb') as f:
        f.write(data)
    if mode == '100755':
        os.chmod(dst, 0o755)
    assert sha_b(open(dst, 'rb').read()) == h
    print(f'written {p} ({len(data)} bytes, mode {mode}) {h}')
print(f'{len(plan)} files written from their blobs at {FULL}')
