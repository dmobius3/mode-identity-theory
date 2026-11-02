"""The case guard and the development log (BOUNDARY.md, DESIGN.md section 6, DRIVER_PLAN.md v2).

Admission. A GO-list case (BOUNDARY.md and its amendments) runs at any time. A sealed case runs only under the frozen
allowlist, run/FROZEN.json, and frozen() admits it only if all of these hold:
  - the file's SHA-256 equals its pin, run/FROZEN_PIN, checked before anything else is read (UA);
  - its manifest SHA-256 equals the running tree's and run/MANIFEST_PIN's (UB);
  - its terms SHA-256 equals that of the filed terms, run/m8_16_task_details.md;
  - each target record's SHA-256 equals the file's (UB);
  - it lists the case.
R0 is never admitted. A FREEZE file, the development guard's old trigger, admits nothing (UB).

Every development run appends one entry to DEVLOG.md with its script's SHA-256, its case and its outcome, and keeps a
copy of each output under dev/runs/, named by its entry number, so a later run never overwrites an earlier record.
Past entries are never edited.
"""
import datetime
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN_ROOT = ROOT          # the tree frozen() reads; a test points it at a temporary copy
GO = {'synthetic', 'manufactured', 'theoremD:R1', 'theoremD:R3', 'theoremD:R6', 'theoremD:R7',
      'theoremD:R8', 'C2a', 'C2b', 'C3',          # BOUNDARY.md, with amendment 1 (C3)
      'seedcheck',                                # amendment 2: the sealed seeds' lowest-level check, and its note
      'C2a/R5',                                   # amendments 3 and 4: R5's coherent branch
      'dryrun'}                                   # step 3's dry run, a run label: the driver admits GO cases only in it
# Amendment 2's scope, enforced here (UB): require('seedcheck') marks the process. Only a marked process may build a
# sealed seed (branches.sealed_seed_for_check), and no marked process may solve: every solver path refuses in it.
SEEDCHECK = False
# The manifest: every file under these folders, except the pins, FROZEN.json and the run's outputs (UB).
MANIFEST_DIRS = ('instrument', 'run', 'reference/m815')
PIN_FILES = ('run/FROZEN.json', 'run/FROZEN_PIN', 'run/MANIFEST_PIN')
OUTPUT_DIRS = ('run/out', 'run/dry')


def refuse_in_seedcheck(what):
    if SEEDCHECK:
        raise PermissionError(f'{what} refused: a seedcheck process may not solve (BOUNDARY.md, the note to amendments'
                              ' 2 and 3)')


def sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def manifest(root=None):
    """(text, SHA-256): one line 'sha256  path' per file under MANIFEST_DIRS, sorted by path, skipping PIN_FILES,
    OUTPUT_DIRS, caches and .DS_Store."""
    root = RUN_ROOT if root is None else root
    entries = []
    for d in MANIFEST_DIRS:
        for dp, dn, fns in os.walk(os.path.join(root, d)):
            rel_dp = os.path.relpath(dp, root).replace(os.sep, '/')
            dn[:] = sorted(x for x in dn if x != '__pycache__' and f'{rel_dp}/{x}' not in OUTPUT_DIRS)
            for fn in fns:
                rel = f'{rel_dp}/{fn}'
                if rel in PIN_FILES or fn.endswith('.pyc') or fn == '.DS_Store':
                    continue
                entries.append((rel, sha256(os.path.join(root, rel))))
    text = ''.join(f'{h}  {rel}\n' for rel, h in sorted(entries))
    return text, hashlib.sha256(text.encode('utf-8')).hexdigest()


def frozen(root=None):
    """run/FROZEN.json, validated (the module docstring), or PermissionError."""
    root = RUN_ROOT if root is None else root
    path, pin = os.path.join(root, 'run', 'FROZEN.json'), os.path.join(root, 'run', 'FROZEN_PIN')
    if not (os.path.exists(path) and os.path.exists(pin)):
        raise PermissionError('no freeze: run/FROZEN.json or its pin is absent')
    with open(path, 'rb') as f:
        raw = f.read()
    with open(pin, encoding='utf-8') as f:
        pinned = f.read().strip()
    if hashlib.sha256(raw).hexdigest() != pinned:
        raise PermissionError('run/FROZEN.json differs from its pin, run/FROZEN_PIN (UA)')
    F = json.loads(raw.decode('utf-8'))
    _, msha = manifest(root)
    mpin = os.path.join(root, 'run', 'MANIFEST_PIN')
    if not os.path.exists(mpin):
        raise PermissionError('run/MANIFEST_PIN is absent')
    with open(mpin, encoding='utf-8') as f:
        mpinned = f.read().strip()
    if mpinned != msha or F.get('manifest_sha256') != msha:
        raise PermissionError('the running tree differs from the frozen manifest')
    terms = os.path.join(root, 'run', 'm8_16_task_details.md')
    if not os.path.exists(terms) or sha256(terms) != F.get('terms_sha256'):
        raise PermissionError('the terms differ from the frozen terms')
    for t in F.get('targets', []):
        f_ = os.path.join(root, t['file'])
        if not os.path.exists(f_) or sha256(f_) != t['sha256']:
            raise PermissionError(f"the target record {t['file']} differs from FROZEN.json's")
    return F


def admitted(case, root=None):
    """Whether a valid frozen allowlist lists the case."""
    try:
        return case in frozen(root)['allowlist']
    except PermissionError:
        return False


def require(case):
    global SEEDCHECK
    if not __debug__:
        raise PermissionError('refused under python -O, which removes asserts')
    if case == 'seedcheck':
        SEEDCHECK = True
    if case == 'R0' or str(case).endswith('/R0'):
        raise PermissionError('R0 is never run (BOUNDARY.md)')
    if case in GO:
        return
    F = frozen()
    if case in F['allowlist']:
        return
    raise PermissionError(f'case {case!r} is neither on the GO list nor on the frozen allowlist')


def log_run(script, case, outcome_lines, outputs=()):
    require(case)
    ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    with open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8') as f:
        n = sum(1 for line in f if line.startswith('## '))
    rel = os.path.relpath(script, ROOT)
    lines = [f'\n## {n}. {ts}: run `{rel}` (case: {case})\n',
             f'Script SHA-256 `{sha256(script)}`; the instrument package as hashed below.']
    for p in sorted(os.listdir(os.path.join(ROOT, 'instrument'))):
        if p.endswith('.py'):
            lines.append(f'- `instrument/{p}` `{sha256(os.path.join(ROOT, "instrument", p))}`')
    runs = os.path.join(ROOT, 'dev', 'runs')
    os.makedirs(runs, exist_ok=True)
    for o in outputs:
        kept = os.path.join(runs, f'{n:03d}_{os.path.basename(o)}')
        if os.path.exists(kept):
            raise PermissionError(f'{kept} exists: kept outputs are written once')
        with open(o, 'rb') as src, open(kept, 'wb') as dst:
            dst.write(src.read())
        lines.append(f'- output `{os.path.relpath(o, ROOT)}` `{sha256(o)}`, kept as `{os.path.relpath(kept, ROOT)}`')
    lines.append('')
    lines.extend(outcome_lines)
    lines.append('')
    with open(os.path.join(ROOT, 'DEVLOG.md'), 'a', encoding='utf-8') as f:
        f.write('\n'.join(lines))
