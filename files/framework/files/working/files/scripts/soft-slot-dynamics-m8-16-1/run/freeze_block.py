#!/usr/bin/env python3
"""The freeze block, built from the tree after the go (DRIVER_PLAN.md v2, item 7). Case: synthetic in its tests.

Usage: freeze_block.py SOLVER_COMMIT SEEDCHECK_JSON OUT_MD

M8.16's freeze block named seven of the eleven files its seed check read (its RECORD.md, section 6). Here every value
is read from a file, that list included:
  - the terms' SHA-256 and the go, from run/FROZEN.json, which devtools.frozen validates first;
  - the manifest's table, every file with its SHA-256, and both pins;
  - the environment, as recorded in run/ENVIRONMENT.json and read again now, with their differences;
  - the target records, as FROZEN.json names them;
  - the pinned next-order values' hashes, as FROZEN.json records them;
  - the seeds, from the seed check's own record, with every file it loaded, its child processes included, each with
    its SHA-256 and whether that equals the manifest's line;
  - FROZEN.json in full, and the order.
The seed check's record (step 3) is JSON: {"script": {"path", "sha256"}, "seeds": [{"name", "Q", "Q_exact", "crit",
"k", "r", "ok"}], "loaded": [the files its own process loaded], "children": [the files its child processes loaded]},
each path relative to the tree's root. The block is written once, by exclusive create.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import record_environment as env  # noqa: E402


def _flat(d, pre=''):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from _flat(v, f'{pre}{k}.')
        else:
            yield f'{pre}{k}', v


def build(root, commit, seedcheck):
    """The block's text for the tree at root, with the seed check's record at the relative path seedcheck."""
    F = devtools.frozen(root)
    text, msha = devtools.manifest(root)
    rows = [line.split('  ', 1) for line in text.splitlines()]
    manifest = {path: h for h, path in rows}
    with open(os.path.join(root, 'run', 'MANIFEST_PIN'), encoding='utf-8') as f:
        mpin = f.read().strip()
    with open(os.path.join(root, 'run', 'FROZEN_PIN'), encoding='utf-8') as f:
        fpin = f.read().strip()
    with open(os.path.join(root, 'run', 'ENVIRONMENT.json'), encoding='utf-8') as f:
        recorded = json.load(f)
    live = env.read()
    a, b = dict(_flat({k: v for k, v in recorded.items() if k != 'recorded'})), dict(_flat(live))
    diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    with open(os.path.join(root, seedcheck), encoding='utf-8') as f:
        S = json.load(f)
    loaded = sorted(set(S['loaded']) | set(S['children']))
    with open(os.path.join(root, 'run', 'FROZEN.json'), encoding='utf-8') as f:
        frozen_text = f.read()
    L = ["# M8.16.1: the freeze block", '',
         '## The terms', '',
         f"- The filed terms, `run/m8_16_task_details.md`: SHA-256 `{F['terms_sha256']}`.",
         f"- The go: {F['go']}",
         f"- `run/FROZEN.json` written {F['written']}.", '',
         '## The instrument', '',
         f'- The solver commit: MIT `{commit}`.',
         f'- The manifest: {len(rows)} files, SHA-256 `{msha}`; `run/MANIFEST_PIN` holds `{mpin}`.',
         f'- The freeze pin, `run/FROZEN_PIN`: `{fpin}`.', '',
         '| file | SHA-256 |', '| --- | --- |']
    L += [f'| `{path}` | `{h}` |' for h, path in rows]
    L += ['', '## The environment', '',
          f"- Recorded {recorded.get('recorded')}, and read again when this block was built.",
          f"- Differences: {', '.join(diff) if diff else 'none'}.", '',
          '<details><summary>As recorded</summary>', '', '```json', json.dumps(recorded, indent=1, sort_keys=True), '```',
          '', '</details>', '',
          '<details><summary>Read again</summary>', '', '```json', json.dumps(live, indent=1, sort_keys=True), '```', '',
          '</details>', '',
          '## The target records', '', '| name | MIT commit | blob | SHA-256 |', '| --- | --- | --- | --- |']
    L += [f"| {t['name']} | `{t['commit']}` | `{t['blob']}` | `{t['sha256']}` |" for t in F['targets']]
    no = F['next_order']
    L += ['', '## The next-order values', '',
          f"- `{no['file']}`: SHA-256 `{no['sha256']}`; its cases section `{no['cases_sha256']}`.",
          f"- Its script, `{no['script']['path']}`: SHA-256 `{no['script']['sha256']}`.",
          f"- Its environment: {', '.join(f'{k} {v}' for k, v in no['environment'].items())}.", '',
          '## The seeds', '',
          f"- The seed check, `{S['script']['path']}`: SHA-256 `{S['script']['sha256']}`.", '',
          '| case | Q(u) | its exact value | criticality | (k, r_u) | checked |', '| --- | --- | --- | --- | --- | --- |']
    L += [f"| {s['name']} | {s['Q']!r} | {s['Q_exact']!r} | {s['crit']:.1e} | ({s['k']}, {s['r']}) | "
          f"{'yes' if s['ok'] else 'NO'} |" for s in S['seeds']]
    L += ['', f'- The files the seed check loaded, its child processes included: {len(loaded)}.', '',
          '| file | SHA-256 | equals its manifest line |', '| --- | --- | --- |']
    L += [f"| `{p}` | `{devtools.sha256(os.path.join(root, p))}` | "
          f"{'yes' if manifest.get(p) == devtools.sha256(os.path.join(root, p)) else 'NO'} |" for p in loaded]
    L += ['', '## `FROZEN.json`', '', '<details><summary>In full</summary>', '', '```json', frozen_text.rstrip('\n'),
          '```', '', '</details>', '', '## The order', '']
    L += [f'{i}. {n}' for i, n in enumerate(F['order'], 1)]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    text = build(ROOT, sys.argv[1], sys.argv[2])
    with open(sys.argv[3], 'x', encoding='utf-8') as f:
        f.write(text)
    print('written', sys.argv[3])
