#!/usr/bin/env python3
"""Every import (M8.16.1's terms, THE TESTS BEFORE THE FREEZE, test 3; DRIVER_PLAN.md v2, The tests). Case: synthetic.

Usage: test_imports.py [SEEDCHECK_JSON]

On a temporary copy of the tree, with a test FROZEN.json and its pins, a synthetic terms file and the environment
read now, freeze_block.py builds the block. M8.16's block named seven of the eleven files its seed check read (its
RECORD.md, section 6). The seed check is step 3's: until its record exists, the seeds line is tested on a synthetic
record of the same form, which lists the files that `import seeds` loads in a fresh process, and, as its child
processes, those a fresh `python3 -I -B -c` loading instrument.linear loads, the form M8.16's seed check's claim 6
took. Given SEEDCHECK_JSON, a path relative to the tree's root, the test reads that record instead. Nothing is solved.

Claims, derived before the run:
  1. Each of driver.py, write_guard.py and freeze_block.py, and the seed check when its record is given, imported in a
     fresh python3 -I -B process on the copy, loads only module files that are in the manifest, and the block names
     each with its SHA-256. The seed check's own file, outside the manifest as M8.16's was, must instead equal the
     SHA-256 its record and the block give it.
  2. The block's seeds line names exactly the files the seed check's record lists, its child processes included,
     each with its SHA-256 equal to its manifest line.
Arms, each of which must turn its claim red:
  A1. the block with one of the record's files dropped from its seeds line, M8.16's defect: claim 2.
  A2. a module loaded from outside the manifest, dev/extra.py, imported by a copy of driver.py: claim 1.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import driver as dr  # noqa: E402
import freeze_block as fb  # noqa: E402
import record_environment as env  # noqa: E402
import write_guard as wg  # noqa: E402

ENTRIES = ('driver', 'write_guard', 'freeze_block')
# a fixed environment, for the test's ENVIRONMENT.json and the block's reading again alike: the claims need the block to
# name the files, not this machine, and record_environment.read() reads macOS's sw_vers and sysctl (UB)
ENV = dict(interpreter=dict(version='test'), numpy=dict(version='test'), scipy=dict(version='test'), threading={},
           os=dict(product='test'), machine=dict(arch='test'))
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def loaded(root, code):
    """The module files under root that a fresh python3 -I -B process loads running code, relative to root."""
    probe = (f"import os, sys, json\nsys.path.insert(0, {root!r})\nsys.path.insert(0, {os.path.join(root, 'run')!r})\n{code}\n"
             f"r = os.path.realpath({root!r}) + os.sep\n"
             "print(json.dumps(sorted({os.path.relpath(os.path.realpath(m.__file__), r) for m in list(sys.modules.values())"
             " if getattr(m, '__file__', None) and os.path.realpath(m.__file__).startswith(r)})))")
    p = subprocess.run([sys.executable, '-I', '-B', '-c', probe], capture_output=True, text=True, cwd=root)
    if p.returncode:
        raise RuntimeError(p.stderr.strip()[-400:])
    return json.loads(p.stdout.strip().splitlines()[-1])


def copy_tree(script=None):
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    if script:
        os.makedirs(os.path.join(tmp, os.path.dirname(script)))
        shutil.copy(os.path.join(ROOT, script), os.path.join(tmp, script))
    for d in ('instrument', 'reference/m815', 'run'):
        shutil.copytree(os.path.join(ROOT, d), os.path.join(tmp, d),
                        ignore=shutil.ignore_patterns('__pycache__', 'out', 'dry', 'FROZEN.json', 'FROZEN_PIN', 'MANIFEST_PIN',
                                                      'ENVIRONMENT.json', 'm8_16_task_details.md'))
    return tmp


def freeze(tmp, record):
    """A test freeze on the copy: the synthetic terms, the environment read now, the manifest pin, a FROZEN.json from
    write_guard.py's own functions with no target record, its pin, and the seed check's record."""
    with open(os.path.join(tmp, 'run', 'm8_16_task_details.md'), 'w', encoding='utf-8') as f:
        f.write('synthetic terms\n')
    with open(os.path.join(tmp, 'run', 'ENVIRONMENT.json'), 'w', encoding='utf-8') as f:
        json.dump(dict(ENV, recorded='test'), f, indent=1, sort_keys=True)
    os.makedirs(os.path.join(tmp, 'dev'), exist_ok=True)
    with open(os.path.join(tmp, 'dev', 'seed_check.json'), 'w', encoding='utf-8') as f:
        json.dump(record, f, indent=1)
    _, msha = devtools.manifest(tmp)
    with open(os.path.join(tmp, 'run', 'MANIFEST_PIN'), 'w', encoding='utf-8') as f:
        f.write(msha + '\n')
    F = dict(allowlist=list(cs.ORDER), order=list(cs.ORDER), cases={n: cs.serialize(n, cs.CASES[n]) for n in cs.ORDER},
             values=wg.frozen_values(), next_order=wg.next_order_values(tmp), go='test',
             terms_sha256=devtools.sha256(os.path.join(tmp, 'run', 'm8_16_task_details.md')), manifest_sha256=msha,
             targets=[], written='test')
    text = json.dumps(dr.jsonable(F), indent=1) + '\n'
    with open(os.path.join(tmp, 'run', 'FROZEN.json'), 'w', encoding='utf-8') as f:
        f.write(text)
    with open(os.path.join(tmp, 'run', 'FROZEN_PIN'), 'w', encoding='utf-8') as f:
        f.write(hashlib.sha256(text.encode('utf-8')).hexdigest() + '\n')
    return fb.build(tmp, 'test', 'dev/seed_check.json')


def table(block):
    return {p: h for p, h in re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \|$', block, re.M)}


def seeds_line(block):
    return {p: (h, eq) for p, h, eq in re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \| (yes|NO) \|$', block, re.M)}


def claim1(tmp, block, entries, script=None):
    man = {path: h for h, path in (line.split('  ', 1) for line in devtools.manifest(tmp)[0].splitlines())}
    tab, bad = table(block), []
    for name, code in entries:
        for f in loaded(tmp, code):
            if script and f == script['path']:
                if devtools.sha256(os.path.join(tmp, f)) != script['sha256'] or f"`{f}`: SHA-256 `{script['sha256']}`" not in block:
                    bad.append(f'{name}: {f} differs from the SHA-256 its record and the block give it')
            elif f not in man:
                bad.append(f'{name}: {f} is not in the manifest')
            elif tab.get(f) != man[f]:
                bad.append(f'{name}: {f} is not named in the block with its SHA-256')
    return bad


def claim2(block, record):
    want = set(record['loaded']) | set(record['children'])
    got = seeds_line(block)
    return [f'the seeds line: {sorted(set(got) ^ want)}'] * (set(got) != want) + [
        f'{p}: its SHA-256 differs from its manifest line' for p, (_, eq) in got.items() if eq != 'yes']


def main():
    devtools.require('synthetic')
    say("Every import (M8.16.1's DRIVER_PLAN.md v2), on a temporary copy of the tree; nothing solved.")
    env.read = lambda: dict(ENV)
    record = None
    if len(sys.argv) > 1:
        with open(os.path.join(ROOT, sys.argv[1]), encoding='utf-8') as f:
            record = json.load(f)
    tmp = copy_tree(record['script']['path'] if record else None)
    try:
        if record:
            say(f"   the seed check's record: {sys.argv[1]}, for {record['script']['path']}")
        else:
            record = dict(script=dict(path='dev/seed_check.py', sha256='0' * 64),
                          seeds=[dict(name='synthetic', Q=1.0, Q_exact=1.0, crit=0.0, k=0, r=0, ok=True)],
                          loaded=loaded(tmp, 'import seeds'),
                          children=loaded(tmp, 'from instrument import linear'))
            say('   the seed check is step 3\'s: its seeds line is tested on a synthetic record of the same form')
        block = freeze(tmp, record)
        entries = [(m, f'import {m}') for m in ENTRIES]
        script = record['script'] if len(sys.argv) > 1 else None
        if script:
            entries.append(('the seed check', "import importlib.util\nspec = importlib.util.spec_from_file_location("
                            f"'seed_check', os.path.join({tmp!r}, {script['path']!r}))\n"
                            "spec.loader.exec_module(importlib.util.module_from_spec(spec))"))
        b1 = claim1(tmp, block, entries, script)
        say(f"1. {'PASS' if not b1 else 'FAIL'}: {', '.join(n for n, _ in entries)} load only manifest files, each named in"
            f" the block with its SHA-256" + ''.join(f'\n      {b}' for b in b1))
        for name, code in entries:
            say(f'      {name}: {len(loaded(tmp, code))} files')
        b2 = claim2(block, record)
        say(f"2. {'PASS' if not b2 else 'FAIL'}: the seeds line names exactly the record's {len(seeds_line(block))} files, its"
            f" child processes' included, each equal to its manifest line" + ''.join(f'\n      {b}' for b in b2))
        say('arms, each of which must turn its claim red:')
        drop = sorted(set(record['loaded']) | set(record['children']))[0]
        cut = '\n'.join(line for line in block.splitlines() if not line.startswith(f'| `{drop}` |') or '| yes |' not in line)
        a1 = bool(claim2(cut, record))
        say(f"   A1. {drop} dropped from the seeds line: {'RED' if a1 else 'GREEN'}")
        with open(os.path.join(tmp, 'dev', 'extra.py'), 'w', encoding='utf-8') as f:
            f.write('VALUE = 1\n')
        src = open(os.path.join(tmp, 'run', 'driver.py'), encoding='utf-8').read()
        with open(os.path.join(tmp, 'run', 'driver_a2.py'), 'w', encoding='utf-8') as f:
            f.write(src.replace('import seeds as sd  # noqa: E402\n', 'import seeds as sd  # noqa: E402\n'
                                f'sys.path.insert(0, os.path.join(ROOT, "dev"))\nimport extra  # noqa: E402\n', 1))
        a2 = any('dev/extra.py is not in the manifest' in x for x in claim1(tmp, block, [('driver_a2', 'import driver_a2')]))
        say(f"   A2. dev/extra.py imported by a copy of driver.py: {'RED' if a2 else 'GREEN'}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    n = bool(b1) + bool(b2) + (not a1) + (not a2)
    say(f'{n} failed')
    with open(os.path.join(HERE, 'test_imports.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if n:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
