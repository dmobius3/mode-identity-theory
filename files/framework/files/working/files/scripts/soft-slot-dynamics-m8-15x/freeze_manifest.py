"""The M8.15.x freeze: m8_15x_solver/out/MANIFEST.json, built as M8.15's m815_freeze.py builds one, and the freeze's
checks. No target is solved.

  python3 freeze_manifest.py manifest QUALIFICATION.json   check every instrument file's SHA-256 against the hashes
                                                           the qualification recorded at its start, and the
                                                           environment against M8.15's; then write MANIFEST.json
  python3 freeze_manifest.py sums                          write SHA256SUMS: every file of the freeze but itself
  python3 freeze_manifest.py check [QUALIFICATION.json]    the freeze's checks; exit status 1 if any fails

The checks:
  1. hashes: each instrument file's SHA-256 equals MANIFEST.json's entry and, given the qualification's record, the
     hash recorded there; the solver folder holds exactly the instrument files;
  2. imports: in a fresh interpreter (-I -B) with only the solver folder added to its path, m815_branch,
     m815_controls, verdict and angle import cleanly, with every other instrument module; the module left out of the
     freeze is never loaded, and nothing loads from outside the solver folder and Python's own installation;
  3. names: no file in the solver folder names the module left out of the freeze;
  4. the static inputs and Theorem D's record are byte-identical to M8.15's;
  5. SHA256SUMS pins every file of the freeze and passes, and M8.15's SHA256SUMS still passes."""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'          # the frozen environment, as m815_freeze.py records it

import sys, json, hashlib, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SOLVER = os.path.join(HERE, 'm8_15x_solver')
OUT = os.path.join(SOLVER, 'out')
M815 = os.path.normpath(os.path.join(HERE, '..', 'soft-slot-dynamics'))     # M8.15's frozen folder, unchanged
M815_OUT = os.path.join(M815, 'm8_15_solver', 'out')
SCRIPTS = ['geometry.py', 'irreps.py', 'fem.py', 'nonlinear.py', 'standing.py', 'linearize.py', 'integrate.py',
           'symmetry.py', 'pinned.py', 'continuation.py', 'verdict.py', 'persistence.py', 'm815_common.py',
           'm815_controls.py', 'm815_branch.py', 'm815_freeze.py', 'angle.py']
LEFT_OUT = 'cluster_rule'          # control 2a's candidate cluster rule, which did not qualify
MATH = ['outside3_krein.py', 'outside3_krein.out', 'analyse.py', 'core.py', 'outside3_p.npy']
STATIC = ['freeze_numbers.json', 'dt_L2.json', 'orientations.json', 'theoremD_L3.json']
ENTRY = ['m815_branch', 'm815_controls', 'verdict', 'angle']
SKIP = {'__pycache__', '.DS_Store'}


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def environment():
    import platform
    import numpy as np, scipy
    env = dict(python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(),
               machine=platform.machine(), processor=platform.processor(),
               threads={k: os.environ.get(k) for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
                                                      'MKL_NUM_THREADS')})
    try:
        env['numpy_config'] = np.show_config(mode='dicts')
        env['scipy_config'] = scipy.show_config(mode='dicts')
    except TypeError:
        pass
    return json.loads(json.dumps(env, default=str))


def recorded_hashes(qual_path):
    q = json.load(open(qual_path))
    return q, q['steps']['controls']['instrument_sha256']


def check_hashes(qual_path=None, manifest=None):
    """Check 1. Returns a list of failures."""
    bad = []
    present = sorted(f for f in os.listdir(SOLVER) if f.endswith('.py'))
    if present != sorted(SCRIPTS):
        bad.append(f'the solver folder holds {present}, not the instrument files')
    files = {s: sha(os.path.join(SOLVER, s)) for s in SCRIPTS if os.path.exists(os.path.join(SOLVER, s))}
    if manifest is not None:
        for s in SCRIPTS:
            if manifest['sha256'].get(s) != files.get(s):
                bad.append(f'{s}: not the hash in MANIFEST.json')
    if qual_path:
        _, rec = recorded_hashes(qual_path)
        if set(rec) != set(SCRIPTS) | {LEFT_OUT + '.py'}:
            bad.append('the qualification recorded a different set of files')
        for s in SCRIPTS:
            if rec.get(s) != files.get(s):
                bad.append(f'{s}: not the hash the qualification recorded')
    return bad


def manifest(qual_path):
    bad = check_hashes(qual_path)
    if bad:
        raise SystemExit('refused: ' + '; '.join(bad))
    m815 = json.load(open(os.path.join(M815_OUT, 'MANIFEST.json')))
    env = environment()
    diff = [k for k in sorted(set(env) | set(m815['environment'])) if env.get(k) != m815['environment'].get(k)]
    if diff:
        raise SystemExit(f'refused: the environment differs from M8.15\'s in {diff}')
    files = {s: sha(os.path.join(SOLVER, s)) for s in SCRIPTS}
    for f in MATH:
        h = sha(os.path.join(M815, 'm8_15_math', f))
        if h != m815['sha256']['m8_15_math/' + f]:
            raise SystemExit(f'refused: M8.15\'s m8_15_math/{f} is not the file its manifest records')
        files['../soft-slot-dynamics/m8_15_math/' + f] = h
    for extra in ('freeze_numbers.json', 'orientations.json'):
        files['out/' + extra] = sha(os.path.join(OUT, extra))
    q, _ = recorded_hashes(qual_path)
    comp = q['steps']['comparisons']
    outcomes = {k: v['outcome'] for k, v in comp.items() if 'outcome' in v}
    outcomes['theoremD_L3'] = dict(gate_passed=bool(comp['theoremD_L3']['record']['ok']),
                                   theoremD_rel=comp['theoremD_L3']['record']['theoremD_rel'])
    outcomes['freeze_numbers'] = dict(s2_as_recorded=comp['freeze_numbers']['s2_as_recorded'],
                                      rest=comp['freeze_numbers']['rest']['outcome'])
    fz = json.load(open(os.path.join(M815_OUT, 'FROZEN.json')))
    old = m815['sha256']
    rec = dict(sha256=files, seed=m815['seed'], arpack_v0_seed=m815['arpack_v0_seed'], levels=m815['levels'],
               environment=env, determinism=m815['determinism'],
               derived_from=dict(solver_commit=fz['solver_commit'], folder='../soft-slot-dynamics/m8_15_solver',
                                 changed=[s for s in SCRIPTS if s in old and old[s] != files[s]],
                                 added=[s for s in SCRIPTS if s not in old]),
               qualification=dict(started=q['started'], finished=q['finished'],
                                  instrument_sha256_as_recorded=True,
                                  environment=q['steps']['environment']['ok'],
                                  frozen_bytes_arm=q['steps']['frozen_bytes_arm']['ok'],
                                  controls=q['steps']['controls']['all_ok'], comparisons=outcomes),
               written=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
               guard='out/FROZEN.json is written once the first target\'s terms are frozen on main, before any '
                     'target runs; until then m815_branch.py refuses every target')
    with open(os.path.join(OUT, 'MANIFEST.json'), 'w') as f:
        json.dump(rec, f, indent=1)
    print(json.dumps(files, indent=1))


def walk(root):
    for d, dirs, names in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x not in SKIP)
        for n in sorted(names):
            if n not in SKIP:
                yield os.path.relpath(os.path.join(d, n), root)


def sums():
    lines = [f'{sha(os.path.join(HERE, p))}  {p}\n' for p in sorted(walk(HERE)) if p != 'SHA256SUMS']
    with open(os.path.join(HERE, 'SHA256SUMS'), 'w') as f:
        f.writelines(lines)
    print(f'SHA256SUMS: {len(lines)} files')


def check_sums(root):
    """(passed, total, failures, unpinned) for root/SHA256SUMS."""
    pinned, bad = {}, []
    for line in open(os.path.join(root, 'SHA256SUMS')):
        h, p = line.rstrip('\n').split('  ', 1)
        pinned[p] = h
        if not os.path.exists(os.path.join(root, p)) or sha(os.path.join(root, p)) != h:
            bad.append(p)
    return len(pinned) - len(bad), len(pinned), bad, pinned


def check_imports():
    code = ("import sys, os, json\n"
            f"sys.path.insert(0, {SOLVER!r})\n"
            f"for m in {[s[:-3] for s in SCRIPTS]!r}: __import__(m)\n"
            f"prefixes = [os.path.realpath(p) for p in {{sys.prefix, sys.base_prefix, sys.exec_prefix}}]\n"
            f"solver = os.path.realpath({SOLVER!r})\n"
            "outside = sorted({os.path.realpath(m.__file__) for m in list(sys.modules.values())\n"
            "                  if getattr(m, '__file__', None)} - {None})\n"
            "outside = [p for p in outside if not p.startswith(solver + os.sep)\n"
            "           and not any(p.startswith(x + os.sep) for x in prefixes)]\n"
            f"print(json.dumps(dict(left_out={LEFT_OUT!r} in sys.modules, outside=outside,\n"
            f"                      entry=all(m in sys.modules for m in {ENTRY!r}))))\n")
    r = subprocess.run([sys.executable, '-I', '-B', '-c', code], cwd=SOLVER, capture_output=True, text=True)
    if r.returncode != 0:
        return [f'an import failed: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else r.returncode}']
    res = json.loads(r.stdout.strip().splitlines()[-1])
    bad = []
    if res['left_out']:
        bad.append(f'{LEFT_OUT} was loaded')
    if res['outside']:
        bad.append(f'modules loaded from outside the solver folder: {res["outside"]}')
    if not res['entry']:
        bad.append('an entry module is missing')
    return bad


def check_names():
    return [p for p in walk(SOLVER) if LEFT_OUT.encode() in open(os.path.join(SOLVER, p), 'rb').read()]


def check(qual_path=None):
    results = []
    man = json.load(open(os.path.join(OUT, 'MANIFEST.json')))
    results.append(('1. hashes', check_hashes(qual_path, man)))
    results.append(('2. imports', check_imports()))
    results.append(('3. names', [f'{p} names {LEFT_OUT}' for p in check_names()]))
    results.append(('4. static inputs and Theorem D', [f for f in STATIC if open(os.path.join(OUT, f), 'rb').read()
                                                      != open(os.path.join(M815_OUT, f), 'rb').read()]))
    ok_n, n, bad, pinned = check_sums(HERE)
    unpinned = sorted(set(walk(HERE)) - set(pinned) - {'SHA256SUMS'})
    results.append((f'5a. SHA256SUMS here ({ok_n} of {n})', bad + [f'unpinned: {p}' for p in unpinned]))
    ok_m, m, bad_m, _ = check_sums(M815)
    results.append((f'5b. M8.15\'s SHA256SUMS ({ok_m} of {m})', bad_m))
    for label, bad in results:
        print(f'  {"PASS" if not bad else "FAIL"}  {label}' + ('' if not bad else f': {bad}'))
    allok = all(not bad for _, bad in results)
    print('freeze checks:', 'ALL PASS' if allok else 'FAIL')
    return allok


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'manifest' and len(sys.argv) == 3:
        manifest(sys.argv[2])
    elif cmd == 'sums':
        sums()
    elif cmd == 'check':
        sys.exit(0 if check(sys.argv[2] if len(sys.argv) > 2 else None) else 1)
    else:
        raise SystemExit(__doc__)
