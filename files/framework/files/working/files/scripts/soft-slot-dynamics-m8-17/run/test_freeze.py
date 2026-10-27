#!/usr/bin/env python3
"""The guard procedure, rehearsed end to end on a temporary copy of this folder, never on the folder itself (M8.17's
terms: THE FREEZE, THE GUARD AND THE RUN, inherited from M8.16.1's; the filing plan's steps 3 to 5 and its step after
the merge). Case: synthetic. No solve: nothing here builds a seed or calls a solver.

Usage: test_freeze.py

Each step runs as the procedure runs it, as `python3 -I -B` on the copy's own scripts, in processes of their own:
  1. the filed terms, registration/m8_17_task_details.md, copied by exclusive create to run/m8_16_task_details.md;
  2. run/record_environment.py writes run/ENVIRONMENT.json, and its --check finds no difference;
  3. run/pin_manifest.py writes run/MANIFEST_PIN; the manifest, recomputed, equals it, and a second pin is refused;
  4. run/write_guard.py writes run/FROZEN.json and run/FROZEN_PIN, and a second write is refused;
  5. devtools.frozen() admits the copy, and so does the copy's census.frozen(), with the seven run rows;
  6. run/freeze_block.py writes the block, which names the terms' SHA-256, the go, both pins, every manifest line once,
     no environment difference, every reference file, FROZEN.json in full and the order.
Arms, each on the frozen copy, restored after it, each of which census.frozen() must refuse:
  A1. a byte appended to a manifest file, run/test_gate.out;
  A2. a byte changed in a reference file, M8.16.1's T2/R4 output;
  A3. a space added to FROZEN.json;
  A4. the terms in run/ changed by one byte;
  A5. a forged FROZEN.json, one case's path cut short, with its pin rewritten to match: devtools.frozen() admits it,
      and census.frozen() must not;
  A6. a forged FROZEN.json with the census values' w changed, its pin rewritten to match, likewise;
  A7. the reference list itself, SOURCES.json, changed by one byte.
The copy leaves out the folder's own freeze files, the placed terms, the environment record, the pins and FROZEN.json,
so the rehearsal reads the same before and after the freeze (UB). The folder's freeze files must be as they were.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import census_lib as lib  # noqa: E402

out = []
GO = 'test: the rehearsal, no go'
ADMIT = ("import sys; sys.path.insert(0, sys.argv[1] + '/run'); sys.path.insert(0, sys.argv[1]); import census; "
         "F = census.frozen(); print(' '.join(F['allowlist']))")


def say(s=''):
    print(s, flush=True)
    out.append(s)


def py(root, *args):
    return subprocess.run([sys.executable, '-I', '-B', *args], capture_output=True, text=True, cwd=root)


def admits(root):
    """(admitted, its allowlist or its refusal), from the copy's own census.frozen()."""
    r = py(root, '-c', ADMIT, root)
    return r.returncode == 0, (r.stdout.split() if r.returncode == 0 else r.stderr.strip().split('\n')[-1])


def forged(root, change):
    """FROZEN.json rewritten by change(F), with FROZEN_PIN rewritten to match."""
    p = os.path.join(root, 'run', 'FROZEN.json')
    F = json.load(open(p, encoding='utf-8'))
    change(F)
    text = json.dumps(F, indent=1) + '\n'
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)
    with open(os.path.join(root, 'run', 'FROZEN_PIN'), 'w', encoding='utf-8') as f:
        f.write(hashlib.sha256(text.encode('utf-8')).hexdigest() + '\n')


def main():
    devtools.require('synthetic')
    if len(sys.argv) != 1:
        raise SystemExit(__doc__)
    say("The guard procedure, rehearsed on a temporary copy of this folder; the folder itself is not touched.")
    state = lambda p: devtools.sha256(os.path.join(ROOT, p)) if os.path.exists(os.path.join(ROOT, p)) else None  # noqa: E731
    before = {p: state(p) for p in ('run/FROZEN.json', 'run/FROZEN_PIN', 'run/MANIFEST_PIN', 'run/m8_16_task_details.md', 'run/ENVIRONMENT.json')}
    fails = []
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    skip = lambda d, names: [x for x in names if x in ('__pycache__', '.DS_Store')  # noqa: E731
                             or (os.path.relpath(d, ROOT) == 'run' and x in ('out', 'm8_16_task_details.md',
                                 'ENVIRONMENT.json', 'MANIFEST_PIN', 'FROZEN.json', 'FROZEN_PIN'))]
    try:
        C = os.path.join(tmp, 'folder')
        shutil.copytree(ROOT, C, ignore=skip)
        filed = os.path.join(C, 'registration', 'm8_17_task_details.md')
        terms = os.path.join(C, 'run', 'm8_16_task_details.md')
        with open(filed, 'rb') as f, open(terms, 'xb') as g:
            g.write(f.read())
        ok1 = devtools.sha256(terms) == devtools.sha256(filed)
        say(f"1. {'PASS' if ok1 else 'FAIL'}: the filed terms in run/, equal to registration/'s, SHA-256 "
            f"{devtools.sha256(terms)}")
        r = py(C, 'run/record_environment.py')
        rc = py(C, 'run/record_environment.py', '--check')
        ok2 = r.returncode == 0 and rc.returncode == 0 and 'differences: none' in rc.stdout
        say(f"2. {'PASS' if ok2 else 'FAIL'}: run/ENVIRONMENT.json written, and --check finds no difference")
        r = py(C, 'run/pin_manifest.py')
        text, msha = devtools.manifest(C)
        pin = open(os.path.join(C, 'run', 'MANIFEST_PIN'), encoding='utf-8').read().strip()
        again = py(C, 'run/pin_manifest.py')
        ok3 = r.returncode == 0 and pin == msha and again.returncode != 0 and 'FileExistsError' in again.stderr
        ok3 = ok3 and {'run/m8_16_task_details.md', 'run/ENVIRONMENT.json'} <= {ln.split('  ', 1)[1] for ln in text.splitlines()}
        say(f"3. {'PASS' if ok3 else 'FAIL'}: the manifest pinned, the terms and the environment record among its files, "
            f"and recomputed equal to the pin; a second pin refused")
        r = py(C, 'run/write_guard.py', GO)
        again = py(C, 'run/write_guard.py', GO)
        ok4 = (r.returncode == 0 and os.path.exists(os.path.join(C, 'run', 'FROZEN_PIN'))
               and again.returncode != 0 and 'the freeze is written once' in again.stderr)
        say(f"4. {'PASS' if ok4 else 'FAIL'}: FROZEN.json and its pin written once; a second write refused")
        F = devtools.frozen(C)
        adm, rows = admits(C)
        ok5 = adm and sorted(rows) == sorted(lib.RUN_ORDER) and sorted(F['allowlist']) == sorted(lib.RUN_ORDER)
        say(f"5. {'PASS' if ok5 else 'FAIL'}: devtools.frozen() and the copy's census.frozen() admit it: {rows}")
        block = os.path.join(tmp, 'freeze_block.md')
        r = py(C, 'run/freeze_block.py', 'test-commit', block)
        B = open(block, encoding='utf-8').read() if r.returncode == 0 else ''
        frozen_text = open(os.path.join(C, 'run', 'FROZEN.json'), encoding='utf-8').read().rstrip('\n')
        lines = [ln.split('  ', 1) for ln in text.splitlines()]
        fp = os.path.join(C, 'run', 'FROZEN_PIN')
        fpin = open(fp, encoding='utf-8').read().strip() if os.path.exists(fp) else None
        ok6 = (r.returncode == 0 and B.count(F['terms_sha256']) >= 1 and GO in B and B.count(pin) >= 2
               and fpin is not None and fpin in B
               and all(B.count(f'| `{p}` | `{h}` |') == 1 for h, p in lines) and '- Differences: none.' in B
               and all(t['sha256'] in B for t in F['targets']) and frozen_text in B
               and all(f'{i}. {n}' in B for i, n in enumerate(F['order'], 1)))
        say(f"6. {'PASS' if ok6 else 'FAIL'}: the freeze block: the terms' SHA-256, the go, both pins, every "
            f"manifest line once, no environment difference, the {len(F['targets'])} reference files, FROZEN.json "
            f"in full and the order" + ('' if r.returncode == 0 else f'; {r.stderr.strip()[-300:]}'))
        fails += [n for n, ok in (('1', ok1), ('2', ok2), ('3', ok3), ('4', ok4), ('5', ok5), ('6', ok6)) if not ok]
        say('arms, each of which census.frozen() must refuse, on the frozen copy restored after each:')
        keep = {p: open(os.path.join(C, p), 'rb').read() for p in
                ('run/test_gate.out', 'reference/m8_16_1/run/out/T2_R4.json', 'run/FROZEN.json', 'run/FROZEN_PIN',
                 'run/m8_16_task_details.md', 'reference/SOURCES.json')}

        def flip(p, i=100):
            raw = keep[p]
            with open(os.path.join(C, p), 'wb') as f:
                f.write(raw[:i] + bytes([raw[i] ^ 1]) + raw[i + 1:])

        def restore():
            for p, raw in keep.items():
                with open(os.path.join(C, p), 'wb') as f:
                    f.write(raw)

        def a1():
            with open(os.path.join(C, 'run/test_gate.out'), 'ab') as f:
                f.write(b'x')

        def a3():
            with open(os.path.join(C, 'run/FROZEN.json'), 'ab') as f:
                f.write(b' ')

        def short(F_):
            F_['cases']['T2/R4']['points'] = F_['cases']['T2/R4']['points'][:-1]

        def wide(F_):
            F_['census']['w'] = 2e-3
        arms = [('A1. a byte appended to run/test_gate.out', a1),
                ('A2. a byte changed in M8.16.1\'s T2/R4 output', lambda: flip('reference/m8_16_1/run/out/T2_R4.json')),
                ('A3. a space added to FROZEN.json', a3),
                ('A4. the terms in run/ changed by one byte', lambda: flip('run/m8_16_task_details.md')),
                ("A5. T2/R4's path cut short in a forged FROZEN.json, its pin rewritten", lambda: forged(C, short)),
                ("A6. the census values' w changed in a forged FROZEN.json, its pin rewritten", lambda: forged(C, wide)),
                ('A7. a byte changed in reference/SOURCES.json', lambda: flip('reference/SOURCES.json'))]
        for label, do in arms:
            do()
            dev_ok = True
            try:
                devtools.frozen(C)
            except PermissionError:
                dev_ok = False
            adm, why = admits(C)
            restore()
            red = not adm
            say(f"   {label}: {'RED' if red else 'GREEN'}; devtools.frozen() {'admits' if dev_ok else 'refuses'}; "
                f"census.frozen(): {why if not adm else 'admits'}")
            if not red:
                fails.append(label[:3])
        adm, _ = admits(C)
        if not adm:
            fails.append('restore')
        say(f"   the copy restored: census.frozen() {'admits' if adm else 'REFUSES'} it again")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    left = [p for p, h in before.items() if state(p) != h]
    say(f"the folder itself: {'untouched' if not left else 'CHANGED ' + ', '.join(left)}")
    if left:
        fails.append('folder')
    say(f'{len(fails)} failed')
    with open(os.path.join(HERE, 'test_freeze.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
