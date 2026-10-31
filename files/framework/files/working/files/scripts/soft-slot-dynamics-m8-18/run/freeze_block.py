#!/usr/bin/env python3
"""The freeze block, built from the tree after the go (M8.18's terms: THE FREEZE, THE GUARD AND THE RUN, inherited from
M8.17's, whose run/freeze_block.py this follows).

Usage: freeze_block.py SOLVER_COMMIT OUT_MD

Every value is read from a file:
  - the terms' SHA-256 and the go, from run/FROZEN.json, which devtools.frozen() validates first, and census.frozen()'s
    own checks after it: the cases, this task's census values, and every reference file at its SHA-256;
  - the manifest's table, every file with its SHA-256, and both pins;
  - the environment, as recorded in run/ENVIRONMENT.json and read again now, with their differences;
  - the reference files, as FROZEN.json's targets name them, each with its MIT commit, path, blob and SHA-256;
  - what is inherited from M8.16.1, as FROZEN.json holds it: its terms' SHA-256, its manifest pin, its go, and its
    pinned next-order values;
  - this task's census values, the order, and FROZEN.json in full.
M8.18 adds no seed: each case's seed is M8.16.1's, checked at every cutoff when the run builds it, as run_case checks
it. The block is written once, by exclusive create.
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


def build(root, commit, F=None):
    """The block's text for the frozen tree at root. F: FROZEN.json as census.frozen() returned it, or None to read it
    through devtools.frozen() alone."""
    F = devtools.frozen(root) if F is None else F
    text, msha = devtools.manifest(root)
    rows = [line.split('  ', 1) for line in text.splitlines()]
    with open(os.path.join(root, 'run', 'MANIFEST_PIN'), encoding='utf-8') as f:
        mpin = f.read().strip()
    with open(os.path.join(root, 'run', 'FROZEN_PIN'), encoding='utf-8') as f:
        fpin = f.read().strip()
    with open(os.path.join(root, 'run', 'ENVIRONMENT.json'), encoding='utf-8') as f:
        recorded = json.load(f)
    live = env.read()
    a, b = dict(_flat({k: v for k, v in recorded.items() if k != 'recorded'})), dict(_flat(live))
    diff = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    with open(os.path.join(root, 'run', 'FROZEN.json'), encoding='utf-8') as f:
        frozen_text = f.read()
    inh, C = F['inherited'], F['census']
    L = ['# M8.18: the freeze block', '',
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
          '## The reference files', '', '| name | MIT commit | blob | SHA-256 |', '| --- | --- | --- | --- |']
    L += [f"| {t['name']} | `{t.get('commit', 'this tree')}` | `{t.get('blob', '')}` | `{t['sha256']}` |"
          for t in F['targets']]
    no = inh['next_order']
    L += ['', "## Inherited from M8.16.1", '',
          f"- Its filed terms: SHA-256 `{inh['terms_sha256']}`.",
          f"- Its manifest pin: `{inh['manifest_sha256']}`.",
          f"- Its go: {inh['go']}",
          f"- Its pinned next-order values, `{no['file']}`: SHA-256 `{no['sha256']}`; its cases section "
          f"`{no['cases_sha256']}`.", '',
          '## The census values', '',
          f"- Arm A's ladder: {', '.join(str(N) for N in C['arm_a']['cutoffs'])}, a location decided at "
          f"{', '.join(str(N) for N in C['arm_a']['deciding'])}.",
          f"- Arm B's ladder: {', '.join(str(N) for N in C['arm_b']['cutoffs'])}, its location decided at "
          f"{', '.join(str(N) for N in C['arm_b']['deciding'])}.",
          f"- The band: n_lo = {C['band_n']}, levels {C['band_level']}; the unscored reading beside it, n_lo = "
          f"{C['beside_n']}.",
          f"- The moved midpoint: {C['moved']} of the interval above its lower end, on T4/R5's "
          f"({C['bracket_b'][0]:g}, {C['bracket_b'][1]:g}) alone.",
          f"- The locator: w = {C['w']}, each cutoff's bisection to {C['w_half']}; the guards at "
          f"{', '.join(str(d) for d in C['deltas'])}; the two-ends agreement {C['agree']}.",
          f"- The twelve: {sum(len(v) for v in C['twelve'].values())} points.",
          f"- The controls: {', '.join(C['controls'])}.", '',
          '## `FROZEN.json`', '', '<details><summary>In full</summary>', '', '```json', frozen_text.rstrip('\n'),
          '```', '', '</details>', '', '## The order', '']
    L += [f'{i}. {n}' for i, n in enumerate(F['order'], 1)]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    import census  # noqa: E402
    text = build(ROOT, sys.argv[1], census.frozen())
    with open(sys.argv[2], 'x', encoding='utf-8') as f:
        f.write(text)
    print('written', sys.argv[2])
