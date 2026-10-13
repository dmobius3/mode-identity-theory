"""M8.15.2's run: the pre-run checks, M8.15.2's guard, T2/R4 then T3/R5, and the post-run checks.

  python3 run_m8_15_2.py --dry    every pre-run check, with the guard written and validated on a scratch copy of the
                                  locator v2's folder; nothing is written in the real folders
  python3 run_m8_15_2.py --go     the same checks, then out/FROZEN.json in the locator v2's folder, written once by its
                                  write_guard.py, then both targets back to back, then the post-run checks

Under the maintainer's go on openwave-labs/openwave#630 (issuecomment-6147458225). The terms are the merged task document
(1e8a6e2b, SHA-256 c6da782b...); the locator v2 is the frozen folder at MIT 851b2ad, beside M8.15.1's locator at 324fde3
and the instrument at 97a8c08, which it reads unchanged. A target run also reads the instrument's own out/FROZEN.json,
M8.15.1's guard, for r_f, delta_lev and s2 (#630's approval, its correction on the record), so the checks pin that file to
M8.15.1's recorded SHA-256 and its values to freeze_numbers.json. Any failed pre-run check stops before the guard is
written and before any target runs. Progress goes to the locator v2's out/target_chain.log; each target's output to
out/run_<case>_R<slot>.log; the pre-run record to out/prerun_check.json."""
import os, sys, json, re, hashlib, subprocess, datetime, shutil, tempfile, platform, argparse

W = '/Users/blake/mode-identity-theory/.claude/worktrees/m8-15-2-scope-memo-v4-92c6e8'
S = W + '/files/framework/files/working/files/scripts'
LOC = S + '/soft-slot-dynamics-m8-15-2'
INS = S + '/soft-slot-dynamics-m8-15x'
SOL = INS + '/m8_15x_solver'
OLD = S + '/soft-slot-dynamics-m8-15x-target1'
OUT = LOC + '/out'
OW = os.path.expanduser('~/Desktop/MIT/OpenWave/openwave')
TERMS = '/Users/blake/Desktop/MIT/Stress Tensor/m8_carry_home/dynamics/m8_15_2/m8_15_2_task_details.md'
TERMS_SHA = 'c6da782b43bc13d256f445d822d6c1456d71b42a4b5771b054d0c6b344dd4e4d'
TASK_DOC = 'openwave/xperiments/m8_mit/research/tasks/m8_15_2_task_details.md'
GO = 'https://github.com/openwave-labs/openwave/pull/630#issuecomment-6147458225'
MERGE = '1e8a6e2b'
FREEZE, NOTE = '851b2ad', '9eab674'
FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-15-2'
TARGETS = [('T2', 4), ('T3', 5)]
PY = sys.executable
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')

now = lambda: datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
git = lambda *a, cwd=W: subprocess.check_output(['git', '-C', cwd] + list(a), text=True).strip()
ok_git = lambda *a, cwd=W: subprocess.run(['git', '-C', cwd] + list(a), capture_output=True).returncode == 0


HELD = []          # lines logged before the checks end, written to the chain log only after them


def log(msg, path=None, hold=False):
    line = f'{now()} {msg}'
    print(line, flush=True)
    if hold:
        HELD.append(line)
    elif path:
        with open(path, 'a') as f:
            f.write(line + '\n')


def sums(folder):
    r = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=folder, capture_output=True, text=True)
    n = len([ln for ln in open(os.path.join(folder, 'SHA256SUMS')).read().splitlines() if ln.strip()])
    return r.returncode == 0 and r.stdout.count(': OK') == n, r.stdout.count(': OK'), n


def checks():
    """Every pre-run check, as (label, ok, detail)."""
    res = []
    add = lambda label, ok, detail='': res.append((label, bool(ok), detail))
    m = json.load(open(os.path.join(SOL, 'out', 'MANIFEST.json')))
    lm = json.load(open(os.path.join(LOC, 'MANIFEST.json')))
    py = sorted(f for f in os.listdir(SOL) if f.endswith('.py'))
    bad = [f for f in py if m['sha256'].get(f) != sha(os.path.join(SOL, f))]
    add(f'instrument: {len(py) - len(bad)} of {len(py)} .py files equal the manifest', not bad and len(py) == 17, bad)
    fn_path = os.path.join(SOL, 'out', 'freeze_numbers.json')
    add('instrument: out/freeze_numbers.json equals the manifest', m['sha256']['out/freeze_numbers.json'] == sha(fn_path))
    sys.dont_write_bytecode = True
    sys.path.insert(0, LOC)
    import t1_branch
    msha = sha(os.path.join(SOL, 'out', 'MANIFEST.json'))
    add("instrument manifest SHA-256 is the driver's pin and the locator v2's record",
        msha == t1_branch.MANIFEST_SHA256 == lm['instrument']['manifest_sha256'])
    for label, folder in (('locator v2', LOC), ('instrument folder', INS)):
        ok, n_ok, n = sums(folder)
        add(f'{label}: SHA256SUMS passes {n_ok} of {n}', ok)
    add(f'MIT: {FREEZE}, {NOTE}, 97a8c08 and 324fde3 are on origin/main',
        all(ok_git('merge-base', '--is-ancestor', c, 'origin/main') for c in (FREEZE, NOTE, '97a8c08', '324fde3')))
    add(f'MIT: the locator v2 folder here is the folder frozen at {FREEZE}, with no change and no untracked file',
        git('rev-parse', f'{FREEZE}:{FOLDER}') == git('rev-parse', f'HEAD:{FOLDER}')
        and ok_git('diff', '--quiet', 'HEAD', '--', FOLDER) and not git('status', '--porcelain', '--', FOLDER))
    merged = subprocess.check_output(['git', '-C', OW, 'show', f'{MERGE}:{TASK_DOC}'])
    add('terms: the file passed equals the task document merged in 1e8a6e2b, SHA-256 c6da782b...',
        sha(TERMS) == TERMS_SHA == hashlib.sha256(merged).hexdigest())
    # the maintainer's correction on the record: a target run reads the instrument's own FROZEN.json
    ifz = os.path.join(SOL, 'out', 'FROZEN.json')
    pin = re.search(r'm8_15x_solver/out/FROZEN\.json` \| `([0-9a-f]{64})`', open(os.path.join(OLD, 'RECORD.md')).read())
    fn = json.load(open(fn_path))
    if os.path.exists(ifz):
        fz = json.load(open(ifz))
        add("the instrument's FROZEN.json, which a target run reads: its SHA-256 is the pin in M8.15.1's RECORD.md",
            pin is not None and sha(ifz) == pin.group(1))
        add("the instrument's FROZEN.json: every value of freeze_numbers.json unchanged, frozen true, a terms hash",
            all(fz.get(k) == v for k, v in fn.items()) and fz.get('frozen') and fz.get('terms_sha256'))
    else:
        add("the instrument's FROZEN.json exists (a target run reads it)", False)
    env = m['environment']
    import numpy, scipy
    here = dict(python=sys.version.split()[0], numpy=numpy.__version__, scipy=scipy.__version__, platform=platform.platform())
    add('environment: Python, numpy, scipy and platform equal the instrument manifest\'s',
        here['python'] == env['python'].split()[0] and here['numpy'] == env['numpy'] and here['scipy'] == env['scipy']
        and here['platform'] == env['platform'], here)
    add("no M8.15.2 guard yet (this folder's out/FROZEN.json)", not os.path.exists(t1_branch.GUARD))
    return res


def guard_on_scratch():
    """The guard written by the folder's own write_guard.py into a scratch copy, then the driver's check of it, stopped
    before any solve, as R5's pass case does."""
    work = tempfile.mkdtemp(prefix='m8_15_2_guard_')
    here = os.path.join(work, 'soft-slot-dynamics-m8-15-2')
    shutil.copytree(LOC, here, ignore=shutil.ignore_patterns('out', '__pycache__'))
    os.makedirs(os.path.join(here, 'out'))
    for s in ('soft-slot-dynamics', 'soft-slot-dynamics-m8-15x', 'soft-slot-dynamics-m8-15x-target1'):
        os.symlink(os.path.join(S, s), os.path.join(work, s))
    desc = f'openwave-labs/openwave research/tasks/m8_15_2_task_details.md, merged in {MERGE}'
    code = (f'import sys, json, argparse\nsys.path.insert(0, {here!r})\nimport write_guard, t1_branch\n'
            f'write_guard.write({TERMS!r}, {GO!r}, {desc!r})\n'
            f'ns = argparse.Namespace(case="T2", slot=4, terms={TERMS!r}, bracket3=None, bracket2=None, region=None, '
            f'ladder_only=False, full_ladder=False, tag="_dry", instrument=None, test_levels=None, test_maxit=None, '
            f'test_span_no_rotations=False, test_arm_dlev0=False, test_stop_after_guard=True)\n'
            f'print(json.dumps(t1_branch.run(ns, log=lambda s: None)))\n')
    r = subprocess.run([PY, '-B', '-c', code], capture_output=True, text=True, env=ENV)
    shutil.rmtree(work)
    return r.returncode == 0 and '"passed"' in r.stdout, (r.stdout.strip() + ' ' + r.stderr.strip()[-300:]).strip()


def main():
    mode = sys.argv[1] if len(sys.argv) == 2 else ''
    if mode not in ('--dry', '--go'):
        raise SystemExit(__doc__)
    chain = os.path.join(OUT, 'target_chain.log') if mode == '--go' else None
    log(f'M8.15.2 {mode[2:]} run: pre-run checks', chain, hold=True)
    res = checks()
    ok, detail = guard_on_scratch()
    res.append(('the guard, written by write_guard.py on a scratch copy, passes the driver\'s check before any solve', ok, detail))
    for label, k, d in res:
        log(f'  {"PASS" if k else "FAIL"}  {label}' + (f' {d}' if (d and not k) else ''), chain, hold=True)
    allok = all(k for _, k, _ in res)
    if mode == '--go':
        with open(chain, 'a') as f:
            f.write(''.join(ln + '\n' for ln in HELD))
        json.dump(dict(stamp=now(), checks=[dict(check=l, ok=k, detail=str(d)) for l, k, d in res]),
                  open(os.path.join(OUT, 'prerun_check.json'), 'w'), indent=1)
    if not allok:
        log('pre-run checks FAILED: no guard is written and no target runs', chain)
        return 1
    log('pre-run checks ALL PASS', chain)
    if mode == '--dry':
        return 0
    sys.path.insert(0, LOC)
    import write_guard, t1_branch
    write_guard.write(TERMS, GO, f'openwave-labs/openwave research/tasks/m8_15_2_task_details.md, merged in {MERGE}')
    g_ok, why = t1_branch.validate_guard(SOL, TERMS, sha(os.path.join(SOL, 'out', 'MANIFEST.json')))
    log(f'the guard, written once in this folder\'s out/FROZEN.json, SHA-256 {sha(t1_branch.GUARD)}: {why}', chain)
    if not g_ok:
        log('the guard did not pass: no target runs', chain)
        return 1
    guard_sha, ifz_sha = sha(t1_branch.GUARD), sha(os.path.join(SOL, 'out', 'FROZEN.json'))
    for case, slot in TARGETS:
        log(f'{case}/R{slot} start', chain)
        with open(os.path.join(OUT, f'run_{case}_R{slot}.log'), 'w') as f:
            r = subprocess.run([PY, '-B', 't1_branch.py', case, str(slot), '--terms', TERMS], cwd=LOC, stdout=f,
                               stderr=subprocess.STDOUT, env=ENV)
        log(f'{case}/R{slot} end: exit {r.returncode}', chain)
    for label, folder in (('locator v2', LOC), ('instrument folder', INS)):
        k, n_ok, n = sums(folder)
        log(f'post-run: {label} SHA256SUMS {"passes" if k else "FAILS"} ({n_ok} of {n})', chain)
    log(f'post-run: M8.15.2\'s guard unchanged: {sha(t1_branch.GUARD) == guard_sha}; the instrument\'s FROZEN.json unchanged: '
        f'{sha(os.path.join(SOL, "out", "FROZEN.json")) == ifz_sha}', chain)
    log('target chain done', chain)
    return 0


if __name__ == '__main__':
    sys.exit(main())
