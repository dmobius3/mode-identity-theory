#!/usr/bin/env python3
"""M8.19's second freeze block (the maintainer's ruling on #698 of 2026-11-10, item 3), built after the second writing
from the copy of the folder the run uses, by a script outside the pinned tree, on the form of the first block's builder,
../freeze/freeze_block.py, which is unchanged.

Usage: python3 -I -B freeze_block_2.py OUT_MD

Every value is read from a file or from git, none typed:
  - the ruling and the go, as kept; #702's merged block, from the OpenWave clone's upstream/main;
  - the first freeze, as kept beside the folder in ../freeze/first_freeze/run/, against the pins #702's block records;
  - the folder: its MIT commit, as the go names it; SHA256SUMS and the check's output before the second writing and
    after it, as freeze_2.py kept them, with the copy's files read now against the commit's tree;
  - the environment: the exact command that recorded it, from its kept output; the two records, side by side; and
    the launch's two checks, replayed as freeze_2.py kept them, and again now, by the launch's route;
  - the two FROZEN.json and their pins, field by field and line by line;
  - the scripts that ran the steps, checked them and rehearsed them, each with its SHA-256, and which of them, with the
    first block's builder, go out as archival copies because they name the bench's home folder or a scratch path;
  - #702's merge commit, from GitHub, to which the links to the first block are pinned.
v2 (the reviews of v1): the published copies stated; the links pinned; write_guard.py's command shown, the clone's
path a placeholder. The block is written once, by exclusive create."""
import datetime
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
K = os.path.join(ROOTB, 'freeze', 'first_freeze', 'run')
F2D = os.path.join(ROOTB, 'freeze2')
WT = os.environ['M819_MIT_CLONE']
CLONE = os.path.expanduser(os.environ['M819_OPENWAVE_CLONE_FROM_HOME'])
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
BLOCK1 = 'openwave/xperiments/m8_mit/research/m8_19/freeze_block.md'
OWN = ('run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN')
THREADS = ('MKL_NUM_THREADS', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')
ROUTE = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch; "
         "sys.exit(subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py')]).returncode)")
REPLAY = ("import os, subprocess, sys; sys.path.insert(0, os.path.abspath('run')); import m819_branch as D; "
          "F = D.validate_frozen(); print('validate_frozen: passed;', len(F['pins']), 'pins; go', F['go'], flush=True); "
          "e = subprocess.run([sys.executable, '-I', '-B', os.path.join(os.path.abspath('run'), 'record_environment.py'), '--check'], "
          "capture_output=True, text=True); print(e.stdout, end='', flush=True); sys.exit(e.returncode)")


def sha_b(b):
    return hashlib.sha256(b).hexdigest()


def sha_f(p):
    with open(p, 'rb') as f:
        return sha_b(f.read())


def rd(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def mtime(p):
    return datetime.datetime.fromtimestamp(os.stat(p).st_mtime, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def git(*a, repo=WT):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, check=True).stdout


def flat(d, pre=''):
    for k, v in d.items():
        yield from (flat(v, f'{pre}{k}.') if isinstance(v, dict) else [(f'{pre}{k}', v)])


def kept(name):
    """A step's output as freeze_2.py kept it: its command line, without the prompt, and the rest."""
    text = rd(os.path.join(F2D, 'out', name)).rstrip('\n').split('\n')
    assert text[-1] == 'exit 0', (name, text[-1])
    head = text[0]
    for prompt in ('$ (from the folder) ', '$ '):
        if head.startswith(prompt):
            return head[len(prompt):], text[1:], mtime(os.path.join(F2D, 'out', name))
    raise AssertionError(name)


def build():
    go = json.loads(rd(os.path.join(ROOTB, 'go_request_v1', 'go.json')))
    ru = json.loads(rd(os.path.join(ROOTB, 'launch_refusal_ask_v2', 'ruling', 'ruling.json')))
    assert ru['user']['login'] == 'xrodz' and ru['author_association'] == 'MEMBER' and f"]({go['html_url']})" in ru['body']
    full = git('rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').decode().strip()
    terms_h, sums_h, sources_h, manifest_h = re.findall(r'\b[0-9a-f]{64}\b', go['body'])

    # the second freeze, valid by the launch's route now
    now = subprocess.run([sys.executable, '-I', '-B', '-c', REPLAY], cwd=B, capture_output=True, text=True)
    assert now.returncode == 0 and now.stdout.rstrip('\n').endswith('differences: none'), now.stdout[-300:] + now.stderr[-300:]
    assert now.stdout.startswith(f"validate_frozen: passed; 16 pins; go {ru['html_url']}\n")
    F2, F1 = json.loads(rd(os.path.join(B, 'run', 'FROZEN.json'))), json.loads(rd(os.path.join(K, 'FROZEN.json')))
    t2, t1 = rd(os.path.join(B, 'run', 'FROZEN.json')), rd(os.path.join(K, 'FROZEN.json'))
    pin2, pin1 = rd(os.path.join(B, 'run', 'FROZEN_PIN')).strip(), rd(os.path.join(K, 'FROZEN_PIN')).strip()
    E2, E1 = json.loads(rd(os.path.join(B, 'run', 'ENVIRONMENT.json'))), json.loads(rd(os.path.join(K, 'ENVIRONMENT.json')))
    assert pin2 == sha_f(os.path.join(B, 'run', 'FROZEN.json')) and pin1 == sha_f(os.path.join(K, 'FROZEN.json'))
    assert F2['go'] == ru['html_url'] and F1['go'] == go['html_url'] and ru['created_at'] < E2['recorded'] <= F2['written']
    first = {f: sha_f(os.path.join(K, os.path.basename(f))) for f in OWN}
    assert sorted(os.listdir(K)) == sorted(os.path.basename(f) for f in OWN)

    # #702's merged block records the first freeze's pins
    git('fetch', '-q', 'upstream', repo=CLONE)
    block1 = git('show', f'upstream/main:{BLOCK1}', repo=CLONE).decode('utf-8')
    assert sha_b(block1.encode('utf-8')) == sha_f(os.path.join(ROOTB, 'freeze_block_v2', 'freeze_block.md'))
    assert f'`{pin1}`' in block1 and f"| `run/ENVIRONMENT.json` | `{first['run/ENVIRONMENT.json']}` |" in block1
    assert t1.rstrip('\n') in block1
    pr702 = json.loads(subprocess.run(['gh', 'api', 'repos/openwave-labs/openwave/pulls/702'], capture_output=True, check=True).stdout)
    msha = pr702['merge_commit_sha']
    assert pr702['merged'] and re.fullmatch(r'[0-9a-f]{40}', msha) and git('show', f'{msha}:{BLOCK1}', repo=CLONE).decode('utf-8') == block1
    URL1 = f'https://github.com/openwave-labs/openwave/blob/{msha}/{BLOCK1}'
    fb_sha = sha_f(os.path.join(ROOTB, 'freeze', 'freeze_block.py'))
    assert f'`freeze_block.py`, SHA-256 `{fb_sha}`' in pr702['body']
    t_end = mtime(os.path.join(ROOTB, 'freeze', 'launch_1_refused.out'))

    # the two FROZEN.json: the environment pin, written and go alone
    keys = sorted(k for k in set(F1) | set(F2) if k != 'pins' and F1.get(k) != F2.get(k))
    pins = sorted(k for k in set(F1['pins']) | set(F2['pins']) if F1['pins'].get(k) != F2['pins'].get(k))
    assert keys == ['go', 'written'] and pins == ['run/ENVIRONMENT.json'] and list(F1) == list(F2)
    assert F2['pins']['run/ENVIRONMENT.json'] == sha_f(os.path.join(B, 'run', 'ENVIRONMENT.json'))
    assert (F2['terms_sha256'], F2['instrument_manifest_sha256']) == (terms_h, manifest_h)
    diff_lines = list(difflib.unified_diff(t1.split('\n'), t2.split('\n'), 'the first: run/FROZEN.json', 'the second: run/FROZEN.json', n=0, lineterm=''))
    assert sum(ln.startswith('-') and not ln.startswith('---') for ln in diff_lines) == 3

    # the two environment records: the four threading fields and the time alone
    fa, fb = dict(flat(E1)), dict(flat(E2))
    ediff = sorted(k for k in set(fa) | set(fb) if fa.get(k) != fb.get(k))
    assert ediff == ['recorded'] + [f'threading.{t}' for t in THREADS] and E1['interpreter'] == E2['interpreter']
    assert all(E1['threading'][t] is None and E2['threading'][t] == '1' for t in THREADS)

    # the folder, before the second writing and after it, and now
    listed = {p: h for h, p in (ln.split('  ', 1) for ln in rd(os.path.join(B, 'SHA256SUMS')).splitlines())}
    assert sha_f(os.path.join(B, 'SHA256SUMS')) == sums_h == sha_b(git('show', f'{full}:{FOLDER}/SHA256SUMS'))
    checks = {}
    for name in ('sha256sums_check.out', 'sha256sums_check_after.out'):
        cmd, body, t = kept(name)
        assert cmd == 'shasum -a 256 -c SHA256SUMS' and [ln[:-4] for ln in body[:-1]] == list(listed) and all(ln.endswith(': OK') for ln in body[:-1])
        checks[name] = (body, t)
    allf = sorted(os.path.relpath(os.path.join(dp, n), B) for dp, dn, fn in os.walk(B) for n in fn)
    tree = sorted(p[len(FOLDER) + 1:] for p in git('ls-tree', '-r', '--name-only', full, '--', FOLDER + '/').decode().split('\n') if p)
    assert allf == sorted(tree + list(OWN)) and all(sha_f(os.path.join(B, p)) == h for p, h in listed.items())
    assert not os.path.exists(os.path.join(B, 'run', 'out'))

    # the steps' outputs, as kept, in their order
    rec_cmd, rec_body, t_c = kept('record_environment.out')
    assert rec_body[-2] == f"ENVIRONMENT.json written; {F2['pins']['run/ENVIRONMENT.json']}" and json.loads('\n'.join(rec_body[:-2])) == E2
    assert rec_cmd.endswith(' -I -B -c "' + ROUTE + '"') and rec_cmd.split()[0] == E2['interpreter']['executable']
    wg_cmd, wg_body, t_d = kept('write_guard.out')
    assert wg_body[0] == f'FROZEN.json written: 16 files pinned; pin {pin2}' and wg_cmd.split()[1:5] == ['-I', '-B', 'run/write_guard.py', ru['html_url']]
    assert wg_cmd.split()[5] == '--terms-from' and wg_cmd.split()[6] == CLONE and wg_cmd.count(CLONE) == 1
    wg_shown = wg_cmd.replace(CLONE, '<an OpenWave clone>')
    assert not any(m in wg_shown for m in ('/Users/', '/private/', '/var/folders', '~/'))
    rp_cmd, rp_body, t_e = kept('replay_main_checks.out')
    assert rp_cmd.endswith(' -I -B -c "' + REPLAY + '"') and rp_body[0] == f"validate_frozen: passed; 16 pins; go {ru['html_url']}"
    assert rp_body[-2] == 'differences: none'
    t_b, t_after = checks['sha256sums_check.out'][1], checks['sha256sums_check_after.out'][1]
    assert ru['created_at'] < t_b <= t_c <= t_d <= t_e <= t_after

    # the scripts, each run on the bytes it has now
    def script(*p):
        q = os.path.join(ROOTB, *p)
        return os.path.join(*p), sha_f(q), os.stat(q).st_mtime
    s_freeze = script('freeze2', 'freeze_2.py')
    s_out = script('freeze2', 'freeze_2.out')
    s_reh = script('freeze2', 'freeze_2_rehearsal.out')
    s_pre, s_pre_o = script('freeze2', 'checks_before_write_2.py'), script('freeze2', 'checks_before_write_2.out')
    s_ver, s_ver_o = script('freeze2', 'verify_frozen_2.py'), script('freeze2', 'verify_frozen_2.out')
    s_env, s_env_o = script('freeze', 'rehearse_env.py'), script('freeze', 'rehearse_env.out')
    s_lau, s_lau_o = script('freeze', 'rehearse_launch.py'), script('freeze', 'rehearse_launch.out')
    assert s_freeze[2] < s_reh[2] < s_out[2] and s_pre[2] < s_pre_o[2] and s_ver[2] < s_ver_o[2]
    assert s_env[2] < s_env_o[2] and s_lau[2] < s_lau_o[2]
    out_text = rd(os.path.join(ROOTB, 'freeze2', 'freeze_2.out'))
    reh_text = rd(os.path.join(ROOTB, 'freeze2', 'freeze_2_rehearsal.out'))
    assert out_text.rstrip('\n').endswith('freeze_2: DONE') and 'freeze_2: DONE\nfreeze_2.py exit 0' in reh_text
    pre_text, ver_text = rd(os.path.join(F2D, 'checks_before_write_2.out')), rd(os.path.join(F2D, 'verify_frozen_2.out'))
    assert pre_text.rstrip('\n').endswith('PASS') and ver_text.rstrip('\n').endswith('PASS')
    n_pre = sum(ln.startswith('ok    ') for ln in pre_text.split('\n'))
    n_ver = sum(ln.startswith('ok    ') for ln in ver_text.split('\n'))
    assert "recorded by the launch's route, the launch reads: 0 differences: none" in rd(os.path.join(ROOTB, 'freeze', 'rehearse_env.out'))
    assert rd(os.path.join(ROOTB, 'freeze', 'rehearse_launch.out')).rstrip('\n').endswith('rehearse_launch: PASS')

    LOCALS = ('/Users/', '/var/folders', '/private/', '~/')
    has_local = lambda *p: any(m in rd(os.path.join(ROOTB, *p)) for m in LOCALS)
    assert all(has_local(*p) for p in (('freeze2', 'freeze_2.py'), ('freeze2', 'checks_before_write_2.py'), ('freeze2', 'verify_frozen_2.py'),
                                       ('freeze', 'rehearse_env.py'), ('freeze', 'rehearse_launch.py'), ('freeze2', 'freeze_block_2.py'),
                                       ('freeze', 'freeze_block.py'), ('freeze2', 'freeze_2.out'), ('freeze2', 'freeze_2_rehearsal.out')))
    assert not any(has_local(*p) for p in (('freeze2', 'checks_before_write_2.out'), ('freeze2', 'verify_frozen_2.out'),
                                           ('freeze', 'rehearse_env.out'), ('freeze', 'rehearse_launch.out')))
    show = lambda v: '`null`' if v is None else f'`{json.dumps(v)}`'
    L = ['# M8.19: the second freeze block', '',
         '## The ruling', '',
         f"- The maintainer's ruling: {ru['html_url']}, at {ru['created_at']}: the freeze written once more, a one-time "
         f"exception to § 2 of the go, {go['html_url']}.",
         f"- The first freeze: recorded by #702's block, [`freeze_block.md`]({URL1}), which stays as merged; "
         'kept as below.',
         f"- `run/FROZEN.json` written once more at {F2['written']}, with the ruling's link as its `go`, as the ruling's "
         'item 4 sets it.', '',
         '## The first freeze, kept', '',
         '- Kept beside the folder the run uses, every byte unchanged, in `freeze/first_freeze/run/`, with the refused '
         "launch's output, `freeze/launch_1_refused.out`; published with the record in MIT's M8.19 folder.",
         f"- Its `FROZEN_PIN` holds `FROZEN.json`'s SHA-256, `{pin1}`, and its `run/ENVIRONMENT.json` is at "
         f"`{first['run/ENVIRONMENT.json']}`, the pins #702's block records.",
         f"- The refused launch, which refused at {t_end} before its first job, started no job and wrote no log; it "
         "counts toward no job's three launches (the ruling's item 5).", '',
         '| file | SHA-256 |', '| --- | --- |']
    L += [f'| `{f}` | `{first[f]}` |' for f in OWN]
    L += ['', '## The folder', '',
          f'- MIT `{full}`, `{FOLDER}/`; its `SHA256SUMS`: {len(listed)} files, SHA-256 `{sums_h}`.',
          f"- With the first freeze's three files out of `run/`, the check, `shasum -a 256 -c SHA256SUMS`, at {t_b}: "
          f"{len(checks['sha256sums_check.out'][0]) - 1} of {len(listed)} OK, exit 0; the copy's files were the "
          "commit's tree, nothing else.",
          f"- The check again, at {t_after}, after the second writing: {len(checks['sha256sums_check_after.out'][0]) - 1} "
          f"of {len(listed)} OK, exit 0. Beside the tree, the copy holds only the three the second writing wrote: "
          '`run/ENVIRONMENT.json`, `run/FROZEN.json` and `run/FROZEN_PIN`. No other byte changed.', '',
          "<details><summary>The check's output</summary>", '', '```', '$ shasum -a 256 -c SHA256SUMS']
    L += checks['sha256sums_check.out'][0] + ['```', '', '</details>', '',
                                             '<details><summary>The check again</summary>', '', '```', '$ shasum -a 256 -c SHA256SUMS']
    L += checks['sha256sums_check_after.out'][0] + ['```', '', '</details>', '',
          '## The environment', '',
          f"- Recorded once more at {E2['recorded']}, by the launch's route: the run's interpreter with `-I -B`, from a "
          'process that had imported the driver, as `main()` runs the check. The exact command, from the folder:', '',
          '```', rec_cmd, '```', '',
          '- The two records differ in the four threading fields and the time alone, the interpreter\'s path and flags '
          'included:', '',
          '| field | the first record | the second |', '| --- | --- | --- |']
    L += [f'| `{k}` | {show(fa[k])} | {show(fb[k])} |' for k in ediff]
    L += ['', "- Read again when this block was built, by the launch's route: differences: none.", '',
          '<details><summary>The first record, in full</summary>', '', '```json', json.dumps(E1, indent=1, sort_keys=True),
          '```', '', '</details>', '',
          '<details><summary>The second record, in full</summary>', '', '```json', json.dumps(E2, indent=1, sort_keys=True),
          '```', '', '</details>', '',
          '## `FROZEN.json`', '',
          f"- The second `FROZEN.json`, written at {F2['written']} by `write_guard.py`, given the ruling's link, with the "
          "terms read against OpenWave's main, as at the first writing; its pin, `run/FROZEN_PIN`: "
          f"`{pin2}`. The command, from the folder, with the clone's path given here as a placeholder:", '',
          '```', wg_shown, '```', '',
          f"- Its {len(F2['pins'])} pins: the same {len(F2['pins']) - 1} files at the same SHA-256 as the first's, each at "
          "its `SHA256SUMS` line, and the new record. Its terms' SHA-256, solver commit `"
          f"{F2['solver_commit']}`, manifest SHA-256 and `freeze_numbers` are the first's.",
          '- The two differ in the environment record\'s pin, `written` and `go` alone:', '',
          '| field | the first `FROZEN.json` | the second |', '| --- | --- | --- |',
          f"| `go` | {F1['go']} | {F2['go']} |",
          f"| `written` | `{F1['written']}` | `{F2['written']}` |",
          f"| `pins[\"run/ENVIRONMENT.json\"]` | `{F1['pins']['run/ENVIRONMENT.json']}` | `{F2['pins']['run/ENVIRONMENT.json']}` |",
          f'| its SHA-256, in `FROZEN_PIN` | `{pin1}` | `{pin2}` |', '',
          '<details><summary>The difference, line by line</summary>', '', '```diff'] + diff_lines + [
          '```', '', '</details>', '',
          '<details><summary>The second, in full</summary>', '', '```json', t2.rstrip('\n'), '```', '', '</details>', '',
          f"The first, in full, is in [`freeze_block.md`]({URL1}).", '',
          "## The launch's two checks, replayed", '',
          f"- The two calls `main()` makes before `launch()`, replayed without `launch()` at {t_e}, from the folder:", '',
          '```', rp_cmd, '```', '',
          f"- `validate_frozen()` passed, {len(F2['pins'])} pins, the ruling's link as the go; `record_environment.py "
          "--check`, as its subprocess, read no difference.", '',
          '<details><summary>The output</summary>', '', '```'] + rp_body + ['```', '', '</details>', '',
          '## The scripts', '',
          f'- The steps, in the ruling\'s order: `freeze_2.py`, SHA-256 `{s_freeze[1]}`, run once on the folder; its '
          f"output, SHA-256 `{s_out[1]}`, and each step's, kept with it.",
          f'- The checks before the second writing, read-only: `checks_before_write_2.py`, SHA-256 `{s_pre[1]}`, '
          f'{n_pre} of {n_pre} passed. The read-back after it: `verify_frozen_2.py`, SHA-256 `{s_ver[1]}`, {n_ver} of {n_ver}.',
          f'- The rehearsals in scratch copies, read for nothing: `rehearse_env.py`, SHA-256 `{s_env[1]}`, its output '
          f'`{s_env_o[1]}`; `rehearse_launch.py`, SHA-256 `{s_lau[1]}`, its output `{s_lau_o[1]}`; and `freeze_2.py` '
          f'run whole on a scratch copy of the folder before the second writing, its output `{s_reh[1]}`.',
          "- All published with the record in MIT's M8.19 folder. The scripts, and the outputs of `freeze_2.py` and of its "
          "rehearsal, name the bench's home folder or a scratch path, so they go out as marked archival copies, the path "
          "configurable in a script and a placeholder in an output: each copy names its original's SHA-256, given here, and "
          "differs from it only where the path was. The other outputs go out as they are. The first block's builder, "
          f"`freeze_block.py`, whose original is at `{fb_sha[:8]}…` as #702's pull request names it, goes out the same way.", '',
          '## Unchanged', '',
          "- The terms, the instrument, the reference files and the order of the run's jobs are the first block's: every "
          'file the freeze pins is at its first SHA-256 but `run/ENVIRONMENT.json`, and `FROZEN.json`\'s '
          'terms, solver commit, manifest and frozen numbers are the first\'s.']
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    text = build()
    assert '—' not in text and '–' not in text and '/Users/' not in text and '/private/' not in text and '/var/folders' not in text
    with open(sys.argv[1], 'x', encoding='utf-8') as f:
        f.write(text)
    print('written', os.path.basename(sys.argv[1]), len(text.splitlines()), 'lines', sha_b(text.encode('utf-8')))
