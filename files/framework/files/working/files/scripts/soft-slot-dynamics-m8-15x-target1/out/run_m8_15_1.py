"""M8.15.1's run: the pre-run checks, the guard file, T2/R4 then T3/R5, and the post-run checks.

  python3 run_m8_15_1.py --dry    every pre-run check, with the guard validated on a scratch copy; nothing is written
  python3 run_m8_15_1.py --go     the same checks, then out/FROZEN.json in the instrument, then both targets back to back

Under the maintainer's go on openwave-labs/openwave#624. The terms are the merged task document; the locator is the
frozen folder at MIT 324fde3 and reads the instrument at 97a8c08. Any failed pre-run check stops before a target runs.
Progress goes to the locator's out/target_chain.log; each target's output to out/run_<case>_R<slot>.log."""
import os, sys, json, hashlib, subprocess, datetime, shutil, tempfile

W = '/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1'
S = W + '/files/framework/files/working/files/scripts'
LOC = S + '/soft-slot-dynamics-m8-15x-target1'
INS = S + '/soft-slot-dynamics-m8-15x'
SOL = INS + '/m8_15x_solver'
OUT = LOC + '/out'
OW = os.path.expanduser('~/Desktop/MIT/OpenWave/openwave')
TERMS = '/Users/blake/Desktop/MIT/Stress Tensor/m8_carry_home/dynamics/m8_15x/m8_15_1_task_details.md'
TERMS_SHA = 'fc566c0406fef33d0f2a4ef2540fc6ce841191d292e5767de28d13b617156dbf'
GO = 'https://github.com/openwave-labs/openwave/pull/624#issuecomment-6116132742'
MERGE = 'dcc63851'
TARGETS = [('T2', 4), ('T3', 5)]
PY = sys.executable
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')

now = lambda: datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
git = lambda *a, cwd=W: subprocess.check_output(['git', '-C', cwd] + list(a), text=True).strip()


def log(msg, path=None):
    line = f'{now()} {msg}'
    print(line, flush=True)
    if path:
        with open(path, 'a') as f:
            f.write(line + '\n')


def checks(write_guard):
    """Every pre-run check, as (label, ok, detail). With write_guard false the guard is validated on a scratch copy."""
    res = []
    add = lambda label, ok, detail='': res.append((label, bool(ok), detail))
    m = json.load(open(os.path.join(SOL, 'out', 'MANIFEST.json')))
    py = sorted(f for f in os.listdir(SOL) if f.endswith('.py'))
    bad = [f for f in py if m['sha256'].get(f) != sha(os.path.join(SOL, f))]
    add(f'instrument: {len(py) - len(bad)} of {len(py)} .py files equal the manifest', not bad and len(py) == 17, bad)
    fn_path = os.path.join(SOL, 'out', 'freeze_numbers.json')
    add('instrument: out/freeze_numbers.json equals the manifest', m['sha256']['out/freeze_numbers.json'] == sha(fn_path))
    add('instrument manifest SHA-256 is the one the locator records',
        json.load(open(os.path.join(LOC, 'MANIFEST.json')))['instrument']['manifest_sha256'] == sha(os.path.join(SOL, 'out', 'MANIFEST.json')))
    for label, folder in (('locator', LOC), ('instrument folder', INS)):
        r = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=folder, capture_output=True, text=True)
        n_ok = r.stdout.count(': OK')
        n = len(open(os.path.join(folder, 'SHA256SUMS')).read().strip().split('\n'))
        add(f'{label}: SHA256SUMS passes {n_ok} of {n}', r.returncode == 0 and n_ok == n)
    add('MIT: the locator commit 324fde3 and the instrument commit 97a8c08 are on origin/main',
        subprocess.run(['git', '-C', W, 'merge-base', '--is-ancestor', '324fde3', 'origin/main']).returncode == 0
        and subprocess.run(['git', '-C', W, 'merge-base', '--is-ancestor', '97a8c08', 'origin/main']).returncode == 0)
    merged = subprocess.check_output(['git', '-C', OW, 'show', f'{MERGE}:openwave/xperiments/m8_mit/research/tasks/m8_15_1_task_details.md'])
    add("terms: the file passed equals the merged task document, SHA-256 fc566c04...",
        sha(TERMS) == TERMS_SHA == hashlib.sha256(merged).hexdigest())
    fn = json.load(open(fn_path))
    lm = json.load(open(os.path.join(LOC, 'MANIFEST.json')))
    guard = dict(fn)
    guard.update(frozen=True, terms_sha256=TERMS_SHA,
                 terms=f'openwave-labs/openwave research/tasks/m8_15_1_task_details.md, merged in {MERGE}',
                 go=GO, solver_commit=git('rev-parse', '97a8c08'), locator_commit=git('rev-parse', '324fde3'),
                 tests_first='; '.join(lm['outcomes'].values()), written=now())
    fz_path = os.path.join(SOL, 'out', 'FROZEN.json')
    sys.dont_write_bytecode = True
    sys.path.insert(0, LOC)
    import t1_branch
    if write_guard:
        add('no FROZEN.json before this run', not os.path.exists(fz_path))
        if os.path.exists(fz_path):
            return res, None
        tmp = fz_path + '.tmp'
        with open(tmp, 'w') as f:
            json.dump(guard, f, indent=1)
        os.replace(tmp, fz_path)
        ok, why = t1_branch.validate_guard(SOL, TERMS)
        add(f'the guard, on the real instrument: {why}', ok)
        r = subprocess.run([PY, '-B', 'freeze_manifest.py', 'check'], cwd=INS, capture_output=True, text=True, env=ENV)
        add('the instrument freeze check with FROZEN.json present: ' + (r.stdout.strip().split('\n')[-1] if r.stdout else ''),
            r.returncode == 0)
    else:
        scr = tempfile.mkdtemp(prefix='m8_15_1_guard_')
        os.makedirs(os.path.join(scr, 'out'))
        shutil.copyfile(fn_path, os.path.join(scr, 'out', 'freeze_numbers.json'))
        json.dump(guard, open(os.path.join(scr, 'out', 'FROZEN.json'), 'w'), indent=1)
        ok, why = t1_branch.validate_guard(scr, TERMS)
        add(f'the guard, on a scratch copy: {why}', ok)
        shutil.rmtree(scr)
        add('no FROZEN.json in the instrument yet', not os.path.exists(fz_path))
    return res, guard


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    assert mode in ('--dry', '--go'), __doc__
    chain = os.path.join(OUT, 'target_chain.log') if mode == '--go' else None
    log(f'M8.15.1 {mode[2:]} run: pre-run checks', chain)
    res, guard = checks(write_guard=(mode == '--go'))
    for label, ok, detail in res:
        log(f'  {"PASS" if ok else "FAIL"}  {label}' + (f' {detail}' if detail else ''), chain)
    allok = all(ok for _, ok, _ in res)
    if mode == '--go':
        json.dump(dict(stamp=now(), checks=[dict(check=l, ok=o, detail=str(d)) for l, o, d in res], guard=guard),
                  open(os.path.join(OUT, 'prerun_check.json'), 'w'), indent=1)
    if not allok:
        log('pre-run checks FAILED: no target runs', chain)
        return 1
    log('pre-run checks ALL PASS', chain)
    if mode == '--dry':
        return 0
    for case, slot in TARGETS:
        log(f'{case}/R{slot} start', chain)
        with open(os.path.join(OUT, f'run_{case}_R{slot}.log'), 'w') as f:
            r = subprocess.run([PY, '-B', 't1_branch.py', case, str(slot), '--terms', TERMS], cwd=LOC, stdout=f,
                               stderr=subprocess.STDOUT, env=ENV)
        log(f'{case}/R{slot} end: exit {r.returncode}', chain)
    r = subprocess.run(['shasum', '-a', '256', '-c', 'SHA256SUMS'], cwd=INS, capture_output=True, text=True)
    log(f'post-run: instrument SHA256SUMS {"passes" if r.returncode == 0 else "FAILS"} '
        f'({r.stdout.count(": OK")} OK); FROZEN.json unchanged: {json.load(open(os.path.join(SOL, "out", "FROZEN.json"))) == guard}', chain)
    log('target chain done', chain)
    return 0


if __name__ == '__main__':
    sys.exit(main())
