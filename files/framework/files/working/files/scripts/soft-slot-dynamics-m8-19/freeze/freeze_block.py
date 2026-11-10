#!/usr/bin/env python3
"""M8.19's freeze block (the terms: THE FREEZE, THE GUARD AND THE RUN, "As M8.18"), built after the freeze from the copy
of the folder the run uses, by a script outside the pinned tree, on the form of M8.18's run/freeze_block.py.

Usage: python3 -I -B freeze_block.py OUT_MD

Every value is read from a file or from git:
  - the terms' SHA-256, the go and the time, from run/FROZEN.json, which m819_branch.validate_frozen() validates first;
  - the folder: its MIT commit, as the go names it; SHA256SUMS, equal to its blob there, its SHA-256 and its count;
    the check's output before the freeze and again after it, each as kept when it ran, with the copy's files read now
    against the commit's tree; the freeze pin; FROZEN.json's pins, each at its SHA256SUMS line;
  - the instrument: the solver commit, as FROZEN.json records it; the manifest's SHA-256 and its rows, each checked
    against its file in the solver commit's tree;
  - the environment, as recorded in run/ENVIRONMENT.json and read again now, before m819_branch is imported, since
    that import sets the threading variables; record_environment.py --check is run too, as a launch runs it;
  - the reference files, as reference/SOURCES.json lists them, each with its MIT commit, blob and SHA-256;
  - FROZEN.json in full, and the order of the registered jobs, from run/m819_run.py.
The block is written once, by exclusive create."""
import hashlib
import json
import os
import posixpath
import re
import subprocess
import sys

ROOTB = os.environ['M819_BENCH']
B = os.path.join(ROOTB, 'soft-slot-dynamics-m8-19')
WT = os.environ['M819_MIT_CLONE']
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-19'
INSTR = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15x'
FREEZE_OWN = ('run/ENVIRONMENT.json', 'run/FROZEN.json', 'run/FROZEN_PIN')

ENV0 = dict(os.environ)
sys.path.insert(0, os.path.join(B, 'run'))
import record_environment as E  # noqa: E402  (before m819_branch: see the docstring)

LIVE = E.read()


def sha_b(b):
    return hashlib.sha256(b).hexdigest()


def sha_f(p):
    with open(p, 'rb') as f:
        return sha_b(f.read())


def git(*a):
    return subprocess.run(['git', '-C', WT] + list(a), capture_output=True, check=True).stdout


def build():
    chk = subprocess.run([sys.executable, '-I', '-B', os.path.join(B, 'run', 'record_environment.py'), '--check'],
                         env=ENV0, capture_output=True, text=True)
    assert chk.returncode == 0 and chk.stdout.rstrip().endswith('differences: none'), chk.stdout[-400:]
    import m819_branch as D
    import m819_run as R
    F = D.validate_frozen()

    with open(os.path.join(ROOTB, 'go_request_v1', 'go.json'), encoding='utf-8') as f:
        go = json.load(f)
    assert go['html_url'] == F['go']
    full = git('rev-parse', re.search(r'the folder at MIT `([0-9a-f]+)`', go['body']).group(1) + '^{commit}').decode().strip()
    sfull = git('rev-parse', F['solver_commit'] + '^{commit}').decode().strip()

    sums_p = os.path.join(B, 'SHA256SUMS')
    with open(sums_p, encoding='utf-8') as f:
        sums_text = f.read()
    assert sha_b(git('show', f'{full}:{FOLDER}/SHA256SUMS')) == sha_f(sums_p)
    listed = {p: h for h, p in (line.split('  ', 1) for line in sums_text.splitlines())}
    def read_check(name):
        with open(os.path.join(ROOTB, 'freeze', name), encoding='utf-8') as f:
            c = f.read().rstrip('\n').split('\n')
        n = sum(line.endswith(': OK') for line in c)
        assert c[-1] == 'exit 0' and n == len(listed) == len(c) - 2 and [ln[:-4] for ln in c[1:-1]] == list(listed)
        return c, n, re.search(r', (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)$', c[0]).group(1)
    check, n_ok, t_check = read_check('sha256sums_check.out')
    check2, n_ok2, t_check2 = read_check('sha256sums_check_2.out')
    assert check2[1:] == check[1:] and t_check < F['written'] < t_check2

    # now: every listed file at its line, and the copy's files the commit's tree and the freeze's own three, no more
    assert all(sha_f(os.path.join(B, p)) == h for p, h in listed.items())
    allf = sorted(os.path.relpath(os.path.join(dp, n), B) for dp, dn, fn in os.walk(B) for n in fn)
    tree = sorted(p[len(FOLDER) + 1:] for p in git('ls-tree', '-r', '--name-only', full, '--', FOLDER + '/').decode().split('\n') if p)
    assert allf == sorted(tree + list(FREEZE_OWN)) and tree == sorted(list(listed) + ['SHA256SUMS'])

    with open(os.path.join(B, 'run', 'FROZEN_PIN'), encoding='utf-8') as f:
        fpin = f.read().strip()
    frozen_p = os.path.join(B, 'run', 'FROZEN.json')
    with open(frozen_p, encoding='utf-8') as f:
        frozen_text = f.read()
    assert fpin == sha_f(frozen_p)
    pins = F['pins']
    own = [p for p in pins if p not in listed]
    assert own == ['run/ENVIRONMENT.json'] and all(pins[p] == listed[p] for p in pins if p in listed)
    assert sorted(p for p in pins if p in listed) == sorted(p for p in listed if p.startswith(('run/', 'reference/')))
    n_run = sum(p.startswith('run/') for p in pins if p in listed)
    n_ref = sum(p.startswith('reference/') for p in pins)

    man_p = os.path.join(D.INSTRUMENT, 'out', 'MANIFEST.json')
    with open(man_p, encoding='utf-8') as f:
        man = json.load(f)
    assert sha_f(man_p) == F['instrument_manifest_sha256']
    rows = sorted(man['sha256'].items())

    def at_commit(p):
        for base in (f'{INSTR}/m8_15x_solver', INSTR):
            r = subprocess.run(['git', '-C', WT, 'show', f'{sfull}:{posixpath.normpath(posixpath.join(base, p))}'],
                               capture_output=True)
            if r.returncode == 0:
                return sha_b(r.stdout)
    assert all(at_commit(p) == h for p, h in rows)
    pys = sorted(n for n in os.listdir(D.INSTRUMENT) if n.endswith('.py'))
    assert all(man['sha256'][n] == sha_f(os.path.join(D.INSTRUMENT, n)) for n in pys)
    others = [p for p, _ in rows if p not in pys and p != 'out/freeze_numbers.json']
    math5 = [p for p in others if '/m8_15_math/' in p]
    assert len(others) == len(rows) - len(pys) - 1 and sorted(set(others) - set(math5)) == ['out/orientations.json']
    # who reads those rows' files: among the solver's, m815_freeze.py alone, which nothing imports; nothing under run/
    for n in pys:
        with open(os.path.join(D.INSTRUMENT, n), encoding='utf-8') as f:
            code = f.read()
        assert ('m8_15_math' in code or 'orientations.json' in code) == (n == 'm815_freeze.py'), n
        assert 'import m815_freeze' not in code and 'from m815_freeze' not in code, n
    for n in sorted(os.listdir(os.path.join(B, 'run'))):
        if n.endswith('.py'):
            with open(os.path.join(B, 'run', n), encoding='utf-8') as f:
                code = f.read()
            assert 'm8_15_math' not in code and 'orientations' not in code and 'm815_freeze' not in code, n

    with open(os.path.join(B, 'run', 'ENVIRONMENT.json'), encoding='utf-8') as f:
        recorded = json.load(f)
    a = dict(E._flat({k: v for k, v in recorded.items() if k != 'recorded'}))
    b = dict(E._flat(LIVE))
    diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))

    with open(os.path.join(B, 'reference', 'SOURCES.json'), encoding='utf-8') as f:
        src = json.load(f)
    for s in src['files']:
        assert s['sha256'] == pins[s['file']] == sha_b(git('show', f"{s['commit']}:{s['path']}"))

    jobs = R.registered()
    with open(os.path.join(B, 'run', 'm819_run.py'), encoding='utf-8') as f:
        rsrc = f.read()
    assert "job('c2a_long', 3," in rsrc and "job(f'test_{sid}', 4," in rsrc
    wave = {w: [j['id'] for j in jobs if j['wave'] == w] for w in (1, 2, 5)}
    assert [j['id'] for j in jobs] == wave[1] + wave[2] + wave[5] and wave[1][-1] == 'controls' and wave[2][-1] == 'plan'
    assert all(j['gate1'] for j in jobs if j['wave'] == 2) and wave[5] == ['record']
    cs = lambda xs: ', '.join(f'`{x}`' for x in xs)

    L = ['# M8.19: the freeze block', '',
         '## The terms', '',
         f"- The filed terms, `run/m8_19_task_details.md`: SHA-256 `{F['terms_sha256']}`.",
         f"- The go: {F['go']}",
         f"- `run/FROZEN.json` written {F['written']}.", '',
         '## The folder', '',
         f'- MIT `{full}`, `{FOLDER}/`.',
         f'- Its `SHA256SUMS`: {len(listed)} files, SHA-256 `{sha_f(sums_p)}`.',
         f'- The check, `shasum -a 256 -c SHA256SUMS`, on the copy of the folder the run uses, at {t_check}, before '
         f'the freeze: {n_ok} of {len(listed)} OK, exit 0.',
         f'- The check again, at {t_check2}, after the freeze: {n_ok2} of {len(listed)} OK, exit 0. Beside the files '
         '`SHA256SUMS` lists and `SHA256SUMS` itself, the copy holds only the three the freeze wrote: '
         '`run/ENVIRONMENT.json`, `run/FROZEN.json` and `run/FROZEN_PIN`.',
         f'- The freeze pin, `run/FROZEN_PIN`: `{fpin}`.',
         f'- The pins of `FROZEN.json`: {len(pins)} files, the {n_run} under `run/` and the {n_ref} under '
         '`reference/` that `SHA256SUMS` lists, each at its line there, and `run/ENVIRONMENT.json`.', '',
         '| file | SHA-256 |', '| --- | --- |']
    L += [f'| `{p}` | `{h}` |' for p, h in sorted(pins.items())]
    L += ['', "<details><summary>The check's output</summary>", '', '```'] + check + ['```', '', '</details>', '',
          '<details><summary>The check again</summary>', '', '```'] + check2 + ['```', '', '</details>', '',
          '## The instrument', '',
          f'- The solver commit: MIT `{sfull}`.',
          f'- The manifest, `soft-slot-dynamics-m8-15x/m8_15x_solver/out/MANIFEST.json`: {len(rows)} rows, SHA-256 '
          f"`{F['instrument_manifest_sha256']}`, each row at its file in that commit's tree. `write_guard.py` and "
          f"every launch check the solver's {len(pys)} `.py` files against it, the manifest against `FROZEN.json`, "
          "and `out/freeze_numbers.json` by content against `FROZEN.json`'s `freeze_numbers`. The other "
          f"{len(others)} rows, `m8_15_math`'s {len(math5)} files and `out/orientations.json`, are read only by "
          '`m815_freeze.py`, which built the manifest; nothing in the run reads them.', '',
          '| file | SHA-256 |', '| --- | --- |']
    L += [f'| `{p}` | `{h}` |' for p, h in rows]
    L += ['', '## The environment', '',
          f"- Recorded {recorded['recorded']}, and read again when this block was built.",
          f"- Differences: {', '.join(diff) if diff else 'none'}.", '',
          '<details><summary>As recorded</summary>', '', '```json', json.dumps(recorded, indent=1, sort_keys=True),
          '```', '', '</details>', '',
          '<details><summary>Read again</summary>', '', '```json', json.dumps(LIVE, indent=1, sort_keys=True), '```',
          '', '</details>', '',
          '## The reference files', '', '| name | MIT commit | blob | SHA-256 |', '| --- | --- | --- | --- |']
    L += [f"| {s['file']} | `{s['commit']}` | `{s['blob']}` | `{s['sha256']}` |" for s in src['files']]
    L += [f"| reference/SOURCES.json | `this tree` | `` | `{pins['reference/SOURCES.json']}` |", '',
          '## `FROZEN.json`', '', '<details><summary>In full</summary>', '', '```json', frozen_text.rstrip('\n'),
          '```', '', '</details>', '',
          '## The order', '',
          'At most four jobs at once, each on one thread, in this order, a job starting as another ends:', '',
          f'1. The controls: {cs(wave[1][:-1])}; then `controls`, gate 1.',
          f'2. The gates, once gate 1 has passed: {cs(wave[2][:-1])}; then `plan`.',
          '3. From the plan, `c2a_long`: C2a/R4 at 1 at the longest `T`, if a test needs more than 2750.',
          '4. From the plan, `test_<stretch>`: each stretch\'s test, one longer than 2750 only after `c2a_long` has '
          'Persisted, valid.',
          '5. The record: `record`.']
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    text = build()
    assert '\u2014' not in text and '\u2013' not in text and '/Users/' not in text and '/private/' not in text
    with open(sys.argv[1], 'x', encoding='utf-8') as f:
        f.write(text)
    print('written', os.path.basename(sys.argv[1]), len(text.splitlines()), 'lines', sha_b(text.encode('utf-8')))
