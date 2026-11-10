#!/usr/bin/env python3
"""The second freeze block's pull request, read back after its merge and checked against the pushed block: the merge,
by whom and when; its title, body and one file as opened; the one review, its verdict, and the pins it restates
against the files; the merge commit's parents and tree against the pushed commit's; the block at the merge byte for
byte; main at the merge; anything else posted since the ruling. Read-only but for the read-back, saved by exclusive
create in DEST, a new folder, after every read. Every sha, hash and time read from GitHub, git or the files, none
typed.

Usage: python3 -I -B -u merge_703.py DEST"""
import hashlib, json, os, re, subprocess, sys, base64

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
K = os.path.join(ROOTB, 'freeze', 'first_freeze', 'run')
P = os.path.join(ROOTB, 'freeze_block_2_v2')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
BLOCK2 = 'openwave/xperiments/m8_mit/research/m8_19/freeze_block_2.md'
REPO = 'repos/openwave-labs/openwave'
DEST = os.path.abspath(sys.argv[1])
assert not os.path.exists(DEST), DEST
fails = []


def ok(name, cond, detail=''):
    print(('ok    ' if cond else 'FAIL  ') + name + (f': {detail}' if detail != '' else ''), flush=True)
    if not cond:
        fails.append(name)


def info(text):
    print('      ' + text, flush=True)


def run(*a):
    return subprocess.run(a, capture_output=True, check=True).stdout


def gh(path, pages=False):
    d = json.loads(run('gh', 'api', '--paginate', '--slurp', path) if pages else run('gh', 'api', path))
    return [c for page in d for c in page] if pages else d


rd = lambda p: open(p, encoding='utf-8').read()
sha_b = lambda b: hashlib.sha256(b).hexdigest()
sha_f = lambda p: sha_b(open(p, 'rb').read())
nb = lambda s: (s or '').replace('\r\n', '\n').strip()

opened = json.loads(rd(os.path.join(P, 'posted', 'pr_new.json')))
pushed = json.loads(rd(os.path.join(P, 'posted', 'fork_commit.json')))
ru = json.loads(rd(os.path.join(ROOTB, 'launch_refusal_ask_v2', 'ruling', 'ruling.json')))
go = json.loads(rd(os.path.join(ROOTB, 'go_request_v1', 'go.json')))
PRN, HEAD = opened['number'], pushed['sha']
blk = open(os.path.join(P, 'freeze_block_2.md'), 'rb').read()

# every read, before anything is saved
pr = gh(f'{REPO}/pulls/{PRN}')
reviews = gh(f'{REPO}/pulls/{PRN}/reviews', pages=True)
events = gh(f'{REPO}/issues/{PRN}/events', pages=True)
files = gh(f'{REPO}/pulls/{PRN}/files', pages=True)
mc = gh(f"{REPO}/git/commits/{pr['merge_commit_sha']}")
hc = gh(f'{REPO}/git/commits/{HEAD}')
main = gh(f'{REPO}/commits/main')
content = gh(f"{REPO}/contents/{BLOCK2}?ref={pr['merge_commit_sha']}")
posted = {path: gh(f'{REPO}/{path}', pages=True)
          for path in ('issues/698/comments', 'issues/702/comments', f'issues/{PRN}/comments', f'pulls/{PRN}/comments')}
Q = ('query($o:String!,$n:String!,$p:Int!){repository(owner:$o,name:$n){pullRequest(number:$p){lastEditedAt '
     'reviews(first:20){nodes{databaseId state lastEditedAt submittedAt author{login} commit{oid}}}}}}')
gq = json.loads(run('gh', 'api', 'graphql', '-f', f'query={Q}', '-f', 'o=openwave-labs', '-f', 'n=openwave', '-F', f'p={PRN}'))
gpr = gq['data']['repository']['pullRequest']

print(f'== #{PRN}, merged')
ok(f'#{PRN} merged and closed', pr['merged'] is True and pr['state'] == 'closed' and pr['merged_at'] == pr['closed_at'],
   f"merged {pr['merged_at']} by {pr['merged_by']['login']}, opened {pr['created_at']}")
ok('its head the pushed commit, one commit, onto main where it was opened', pr['head']['sha'] == HEAD == opened['head']['sha']
   and pr['commits'] == 1 and pr['base']['ref'] == 'main' and pr['base']['sha'] == opened['base']['sha'], HEAD[:8])
ok('its title and body as opened and as the files hold them', pr['title'] == opened['title'] == rd(os.path.join(P, 'pr_title.txt')).strip()
   and nb(pr['body']) == nb(opened['body']) == nb(rd(os.path.join(P, 'pr_body.md'))))
ok('its body never edited', gpr['lastEditedAt'] is None, gpr['lastEditedAt'] or 'never')
ok('it adds the second block alone', [(f['filename'], f['status']) for f in files] == [(BLOCK2, 'added')])
info('events: ' + '; '.join(f"{e['event']} {e['created_at']} {(e.get('actor') or {}).get('login')}" for e in events))

print('== the review')
r = reviews[0] if len(reviews) == 1 else {}
ok('one review, an approval by the merger, an OpenWave member, on the pushed commit, before the merge',
   len(reviews) == 1 and r['state'] == 'APPROVED' and r['user']['login'] == pr['merged_by']['login']
   and r['author_association'] == 'MEMBER' and r['commit_id'] == HEAD and r['submitted_at'] <= pr['merged_at'],
   f"{len(reviews)} review(s); {r.get('state')} by {(r.get('user') or {}).get('login')} at {r.get('submitted_at')}")
rn = gpr['reviews']['nodes']
ok('the review never edited', len(rn) == 1 and rn[0]['databaseId'] == r.get('id') and rn[0]['lastEditedAt'] is None,
   (rn[0]['lastEditedAt'] or 'never') if rn else 'no review')
body = r.get('body', '')
ver = re.search(r'^\*\*Verdict: (.+?)\*\*$', body, re.M)
ok('its verdict: approve and merge, no findings, no maintainer edits', bool(ver) and ver.group(1).startswith('approve and merge')
   and 'no findings' in ver.group(1) and 'no maintainer edits' in ver.group(1), ver.group(1) if ver else 'no verdict line')
F = json.loads(rd(os.path.join(B, 'run', 'FROZEN.json')))
FULL = run('git', '-C', WT, 'rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').decode().strip()
sums = run('git', '-C', WT, 'show', f'{FULL}:{FOLDER}/SHA256SUMS')
ok("the bench copy's SHA256SUMS is the folder commit's", sums == open(os.path.join(B, 'SHA256SUMS'), 'rb').read())
ok("the second FROZEN_PIN holds the second FROZEN.json's hash", open(os.path.join(B, 'run', 'FROZEN_PIN')).read().strip() == sha_f(os.path.join(B, 'run', 'FROZEN.json')))
full = {'PR head': HEAD, 'freeze_block_2.md': sha_b(blk), 'FROZEN.json': sha_f(os.path.join(B, 'run', 'FROZEN.json')),
        'ENVIRONMENT.json': sha_f(os.path.join(B, 'run', 'ENVIRONMENT.json')),
        'freeze_block_2.py': sha_f(os.path.join(ROOTB, 'freeze2', 'freeze_block_2.py'))}
rows = re.findall(r'^\| (.+?) \| `([0-9a-f]{40}|[0-9a-f]{64})` \|$', body, re.M)
keyed = [(next((k for k in full if k in label), None), v) for label, v in rows]
ok('the pins it restates, five, each equal to ours', len(rows) == 5 and sorted(k for k, v in keyed if k) == sorted(full)
   and all(full[k] == v for k, v in keyed if k), [k for k, v in keyed if not k or full[k] != v] or f'{len(rows)} rows')
known = {'the first ENVIRONMENT.json': sha_f(os.path.join(K, 'ENVIRONMENT.json')), 'the first FROZEN.json': sha_f(os.path.join(K, 'FROZEN.json')),
         'the first FROZEN_PIN': sha_f(os.path.join(K, 'FROZEN_PIN')), 'the second ENVIRONMENT.json': full['ENVIRONMENT.json'],
         'the second FROZEN.json': full['FROZEN.json'], 'the terms': F['terms_sha256'],
         'the instrument manifest': F['instrument_manifest_sha256'], 'SHA256SUMS': sha_b(sums)}
shorts = re.findall(r'`([0-9a-f]{8})…`', body)
named = [[n for n, v in known.items() if v.startswith(s)] for s in shorts]
ok('each short hash it gives names one of ours', bool(shorts) and all(len(n) == 1 for n in named),
   '; '.join(f'{s} {n[0] if len(n) == 1 else n}' for s, n in zip(shorts, named)))
ok("the commits it names: MIT's folder commit and the solver's", f'`{FULL[:8]}`' in body and f"`{F['solver_commit']}`" in body,
   f"{FULL[:8]}, {F['solver_commit']}")
times = sorted(set(re.findall(r'(?<!\d)\d\d:\d\d:\d\dZ', body)))
blk_text = blk.decode('utf-8')
ok("the times it gives: the block's, and the opening's; the ruling's, the second freeze's and the opening's among them",
   bool(times) and all(t in blk_text or t == pr['created_at'][11:] for t in times)
   and {ru['created_at'][11:], F['written'][11:], pr['created_at'][11:]} <= set(times), ', '.join(times))

print('== the merge commit')
ok("its parents main before the merge and the pushed commit", [p['sha'] for p in mc['parents']] == [opened['base']['sha'], HEAD],
   ', '.join(p['sha'][:8] for p in mc['parents']))
ok("its tree the pushed commit's tree", mc['tree']['sha'] == hc['tree']['sha'] == pushed['commit']['tree']['sha'], mc['tree']['sha'][:8])
cb = base64.b64decode(content['content'])
blob = hashlib.sha1(b'blob %d\0' % len(blk) + blk).hexdigest()
ok('the block at the merge commit equals the pushed block, byte for byte', cb == blk and content['sha'] == blob, sha_b(cb))
ok('main at the merge commit', main['sha'] == pr['merge_commit_sha'], f"{main['sha'][:8]}, {main['commit']['committer']['date']}")
info('its message: ' + mc['message'].replace('\n\n', ' / ').replace('\n', ' '))

print('== since the ruling')
after = sorted((path, c['user']['login'], c['created_at']) for path, cs in posted.items() for c in cs
               if c['created_at'] > ru['created_at'] and c['user']['login'] != 'dmobius3')
ok(f'nothing else posted on #698, #702 or #{PRN} since the ruling but the review', not after, after)

os.mkdir(DEST)
for name, obj in (('pr.json', pr), ('reviews.json', reviews), ('events.json', events), ('merge_commit.json', mc),
                  ('main.json', main), ('graphql.json', gq)):
    with open(os.path.join(DEST, name), 'x', encoding='utf-8') as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write('\n')
info(f'read-back saved: {sorted(os.listdir(DEST))}')
print(f'merge {PRN}:', 'PASS' if not fails else f'FAIL ({len(fails)}): {fails}')
sys.exit(1 if fails else 0)
