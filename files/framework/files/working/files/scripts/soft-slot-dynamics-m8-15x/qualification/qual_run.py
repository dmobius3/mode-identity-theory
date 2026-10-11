"""M8.15.x qualification (REGISTER_3.md v2, registered 2026-10-09T14:33:42Z, with its amendment of the branch floors): the
orchestrated run. Every step writes under qual_2026-10-09/.

  1  the environment, compared field by field with M8.15's MANIFEST.json; any difference stops the run
  2  the frozen-bytes arm: `spreads` from 6058f95, which must equal controls_first's spreads_L2.json bit for bit
  3  a clean out/: the bench's earlier out/ archived, the static inputs copied from M8.15's frozen out/ and checked
  4  § 6's controls on the final bytes: control 4's two arms, 1a and its amendment, 1b's angle solve and frozen arm,
     the carry and the nu-sign kind
  5  the three streams: A (level 3, one job at a time: linear 3, theoremD 3, the C3 branch, the C2a branch); B (dynamics
     C1, C2a, then rate); C (dynamics C2b, C3, linear 2, spreads)
  6  summarize, once B and C are done and both branches have started; its output is kept beside the governing file
  7  the comparisons (qual_compare.py) and § 4's unit check
  8  the report: QUALIFICATION.json and QUALIFICATION.log

  python3 qual_run.py          (under caffeinate; about 10 to 11 h)"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, json, time, shutil, hashlib, subprocess, threading, datetime, platform, copy
import numpy as np
import scipy

X = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(X, 'solver', 'm8_15_solver')
Q = os.path.join(X, 'qual_2026-10-09')
B = os.path.join(Q, 'baseline')
CF = os.path.join(B, 'controls_first_2026-10-07')
LOGS = os.path.join(Q, 'logs')
QC = os.path.join(Q, 'controls')
FROZEN = ('/private/tmp/claude-501/-Users-blake-mode-identity-theory--claude-worktrees-confident-varahamihira-0572e1/'
          '0ef115ee-4931-4ef1-a250-32508bad7d9f/scratchpad/frozen_arm')
REPO = '/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1'
OUTREPO = 'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_solver/out'
sys.path.insert(0, X)
import qual_compare as qc

STATE = dict(started=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), steps={})
LOCK = threading.Lock()


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def log(s):
    with LOCK:
        line = f'[{now()}] {s}'
        print(line, flush=True)
        with open(os.path.join(Q, 'QUALIFICATION.progress'), 'a') as f:
            f.write(line + '\n')


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def save_state():
    with LOCK:
        json.dump(STATE, open(os.path.join(Q, 'QUALIFICATION.json'), 'w'), indent=1, default=str)


def run(job, args, cwd, expect=0):
    """One job: its own log; returns (exit code, seconds)."""
    t0 = time.time()
    with open(os.path.join(LOGS, f'{job}.log'), 'w') as f:
        rc = subprocess.run([sys.executable] + args, cwd=cwd, stdout=f, stderr=subprocess.STDOUT).returncode
    dt = round(time.time() - t0, 1)
    log(f'{job}: exit {rc} in {dt} s' + ('' if rc == expect else f'  (expected {expect})'))
    return rc, dt


def environment():
    env = dict(python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(),
               machine=platform.machine(), processor=platform.processor(),
               threads={k: os.environ.get(k) for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS',
                                                      'MKL_NUM_THREADS')})
    env['numpy_config'] = np.show_config(mode='dicts')
    env['scipy_config'] = scipy.show_config(mode='dicts')
    env = json.loads(json.dumps(env, default=str))
    base = json.load(open(os.path.join(B, 'MANIFEST.json')))['environment']

    def diff(a, b, p=''):
        if isinstance(b, dict) and isinstance(a, dict):
            out = []
            for k in sorted(set(a) | set(b)):
                out += [(f'{p}/{k}', 'missing')] if (k not in a or k not in b) else diff(a[k], b[k], f'{p}/{k}')
            return out
        return [] if a == b else [(p, f'{a!r} against {b!r}')]
    d = diff(env, base)
    json.dump(dict(environment=env, differences=d), open(os.path.join(Q, 'ENVIRONMENT.json'), 'w'), indent=1)
    return d


def git_bytes(path):
    return subprocess.run(['git', '-C', REPO, 'show', f'origin/main:{path}'], capture_output=True, check=True).stdout


def instrument_hashes():
    return {f: sha(os.path.join(S, f)) for f in sorted(os.listdir(S)) if f.endswith('.py')}


def step_controls():
    """§ 6: control 4, 1a (and its amendment), 1b's angle solve and frozen arm, the carry, the nu-sign kind."""
    res = dict(instrument_sha256=instrument_hashes())
    out = os.path.join(S, 'out')
    # control 4
    rc, _ = run('control4_a', ['m815_branch.py', 'C2a', '4', '--test-levels', '2,1', '--eps-max', '0.5',
                               '--test-newton-maxit', '1'], S)
    ra = json.load(open(os.path.join(out, 'branch_C2a_R4_test21.json')))
    res['control4_a'] = dict(exit=rc, end=ra.get('end'), ok=bool(rc == 0 and ra.get('end', [None])[0] == 'Newton failure at the seed'))
    rc, _ = run('control4_b', ['m815_branch.py', 'C2a', '4', '--test-levels', '2,1', '--eps-max', '0.5',
                               '--test-raise-at', 'level 2'], S, expect=1)
    rb = json.load(open(os.path.join(out, 'crash_C2a_R4_test21.json')))
    res['control4_b'] = dict(exit=rc, stage=rb.get('stage'), frozen=rb.get('frozen') is not None,
                             traceback=len(rb.get('traceback', [])),
                             ok=bool(rc == 1 and rb.get('crash') and rb.get('stage') == 'level 2' and rb.get('frozen')
                                     and rb.get('traceback')))
    # 1a, its mutation arms, then the amendment against the original unprojected run
    os.makedirs(QC, exist_ok=True)
    if not os.path.exists(os.path.join(QC, 'solver')):
        os.symlink(os.path.join(X, 'solver'), os.path.join(QC, 'solver'))
    for f in ('control_1a.py', 'control_1a_amended.py', 'control_1a_mutations.py', 'control_1b.py', 'control_carry.py',
              'control_kind.py', 'control_2a_synthetic.py'):
        shutil.copy2(os.path.join(X, f), os.path.join(QC, f))
    shutil.copy2(os.path.join(X, 'control_1b.json'), os.path.join(QC, 'control_1b.json'))      # 1b's original record
    rc, _ = run('control_1a', ['control_1a.py'], QC)
    r1 = json.load(open(os.path.join(QC, 'control_1a.json')))
    rcm, _ = run('control_1a_mutations', ['control_1a_mutations.py'], QC)
    mut = open(os.path.join(LOGS, 'control_1a_mutations.log')).read()
    os.replace(os.path.join(QC, 'control_1a.json'), os.path.join(QC, 'control_1a_rerun.json'))
    os.replace(os.path.join(QC, 'control_1a.log'), os.path.join(QC, 'control_1a_rerun.log'))
    shutil.copy2(os.path.join(X, 'control_1a.json'), os.path.join(QC, 'control_1a.json'))      # the unprojected 21:01Z run
    rc2, _ = run('control_1a_amended', ['control_1a_amended.py'], QC)
    r1b = json.load(open(os.path.join(QC, 'control_1a_amended.json')))
    res['control_1a'] = dict(checks_1a=r1['all_passed'], mutations_1a='every mutation caught by its own check alone: True' in mut,
                             checks_amendment=r1b['all_passed'], mutations_amendment=r1b['all_mutations_caught'],
                             ok=bool(rc == 0 and rc2 == 0 and r1['all_passed'] and r1b['all_passed']
                                     and r1b['all_mutations_caught'] and 'every mutation caught by its own check alone: True' in mut))
    # 1b: the angle solve and the frozen arm; check 6 carried forward only if the selection is bit for bit the same
    rs, _ = run('control_1b_solve', ['control_1b.py', '--stage', 'solve'], QC)
    rf, _ = run('control_1b_frozen', ['control_1b.py', '--stage', 'frozen'], QC)
    sys.path.insert(0, QC)
    import importlib
    c1b = importlib.import_module('control_1b')
    W = os.path.join(QC, 'control_1b_work')
    Snew = json.load(open(os.path.join(W, 'solve.json')))
    orig = json.load(open(os.path.join(QC, 'control_1b.json')))
    same_sel = bool(np.array_equal(np.load(os.path.join(W, 'Phi_sel.npy')), np.load(os.path.join(X, 'control_1b_work', 'Phi_sel.npy'))))
    R = dict(one_period=Snew['one_period'], two_periods=Snew['two_periods'], frozen=json.load(open(os.path.join(W, 'frozen.json'))),
             ref_sel=orig['ref_sel'], ref_off=orig['ref_off'], off=Snew['off'])
    ch = c1b.evaluate(R)
    res['control_1b'] = dict(checks=[dict(check=c, passed=bool(ok)) for c, ok in ch], selection_bit_identical=same_sel,
                             check6_carried=same_sel,
                             ok=bool(rs == 0 and rf == 0 and all(ok for _, ok in ch[:5]) and same_sel and ch[5][1]))
    # the carry and the kind
    rc, _ = run('control_carry', ['control_carry.py'], QC)
    rcr = json.load(open(os.path.join(QC, 'control_carry.json')))
    res['control_carry'] = dict(ok=bool(rc == 0 and rcr['all_passed'] and rcr['all_mutations_caught']),
                                checks=rcr['all_passed'], mutations=rcr['all_mutations_caught'])
    rc, _ = run('control_kind', ['control_kind.py'], QC)
    rk = json.load(open(os.path.join(QC, 'control_kind.json')))
    res['control_kind'] = dict(ok=bool(rc == 0 and rk['all_passed'] and rk['all_mutations_caught']),
                               checks=rk['all_passed'], mutations=rk['all_mutations_caught'])
    res['all_ok'] = all(v['ok'] for k, v in res.items() if isinstance(v, dict) and 'ok' in v)
    return res


def stream(name, jobs, done):
    for job, args in jobs:
        STATE['steps'].setdefault('streams', {}).setdefault(name, []).append(dict(job=job, started=now()))
        save_state()
        rc, dt = run(job, args, S)
        STATE['steps']['streams'][name][-1].update(exit=rc, seconds=dt)
        save_state()
        if rc != 0:
            log(f'stream {name} stops at {job}')
            break
    done[name] = True


def unit_check_s5(rec, arr, T=1000.0):
    dt = rec['dt']
    ok = (rec.get('N_obs') == int(round(1 / dt)) and rec.get('N_step') == int(round(T / dt))
          and rec.get('T_int') == rec['N_step'] * dt)
    k = np.arange(rec['N_step'] // rec['N_obs'] + 1)
    times = (k * rec['N_obs']) * dt
    ok_t = bool(arr.shape[0] == len(k) and np.array_equal(arr[:, 0], times))
    return dict(fields=bool(ok), times=ok_t, ok=bool(ok and ok_t))


def main():
    os.makedirs(LOGS, exist_ok=True)
    log('qualification starts')
    # 1
    d = environment()
    STATE['steps']['environment'] = dict(differences=d, ok=not d)
    save_state()
    if d:
        log(f'STOP: the environment differs from MANIFEST.json in {len(d)} fields')
        return
    log('environment: identical to MANIFEST.json')
    # 2
    import control_1a
    nfiles = control_1a.check_frozen_bytes()
    fo = os.path.join(FROZEN, 'm8_15_solver', 'out')
    for f in ('spreads_L2.json',):
        if os.path.exists(os.path.join(fo, f)):
            os.replace(os.path.join(fo, f), os.path.join(fo, f + '.before_qual'))
    rc, _ = run('frozen_spreads', ['m815_controls.py', 'spreads'], os.path.join(FROZEN, 'm8_15_solver'))
    same = rc == 0 and sha(os.path.join(fo, 'spreads_L2.json')) == sha(os.path.join(CF, 'spreads_L2.json'))
    STATE['steps']['frozen_bytes_arm'] = dict(files_checked=nfiles, exit=rc, spreads_bit_identical=bool(same), ok=bool(same))
    save_state()
    if not same:
        log('STOP: the frozen-bytes spreads arm does not reproduce controls_first')
        return
    log(f'frozen-bytes arm: {nfiles} files checked; spreads reproduces controls_first bit for bit')
    # 3
    out = os.path.join(S, 'out')
    arch = os.path.join(S, 'out_pre_qual_2026-10-09')
    if os.path.exists(out) and not os.path.exists(arch):
        os.replace(out, arch)
    os.makedirs(out, exist_ok=True)
    statics = {}
    for f in ('freeze_numbers.json', 'dt_L2.json', 'orientations.json'):
        shutil.copy2(os.path.join(B, f), os.path.join(out, f))
        statics[f] = bool(sha(os.path.join(out, f)) == hashlib.sha256(git_bytes(f'{OUTREPO}/{f}')).hexdigest())
    STATE['steps']['static_inputs'] = dict(checked=statics, ok=all(statics.values()), archived=os.path.basename(arch))
    save_state()
    if not all(statics.values()):
        log('STOP: a static input does not match the repo')
        return
    log('static inputs copied and checked against the repo')
    # 4
    res = step_controls()
    STATE['steps']['controls'] = res
    save_state()
    log(f'§ 6 controls: {"all pass" if res["all_ok"] else "A CONTROL FAILED"}')
    # 5
    done = {}
    A = [('linear_3', ['m815_controls.py', 'linear', '3']), ('theoremD_3', ['m815_controls.py', 'theoremD', '3']),
         ('branch_C3', ['m815_branch.py', 'C3', '4']), ('branch_C2a', ['m815_branch.py', 'C2a', '4'])]
    Bj = [('dynamics_C1', ['m815_controls.py', 'dynamics', 'C1']), ('dynamics_C2a', ['m815_controls.py', 'dynamics', 'C2a']),
          ('rate', ['m815_controls.py', 'rate'])]
    C = [('dynamics_C2b', ['m815_controls.py', 'dynamics', 'C2b']), ('dynamics_C3', ['m815_controls.py', 'dynamics', 'C3']),
         ('linear_2', ['m815_controls.py', 'linear', '2']), ('spreads', ['m815_controls.py', 'spreads'])]
    th = [threading.Thread(target=stream, args=(n, j, done)) for n, j in (('A', A), ('B', Bj), ('C', C))]
    for t in th:
        t.start()
    th[1].join(); th[2].join()
    # 6: summarize once both branches have started (they read the governing freeze numbers at their start)
    while not (os.path.exists(os.path.join(LOGS, 'branch_C2a.log')) and os.path.getsize(os.path.join(LOGS, 'branch_C2a.log')) > 0) \
            and th[0].is_alive():
        time.sleep(30)
    time.sleep(60)
    rc, _ = run('summarize', ['m815_controls.py', 'summarize'], S)
    if rc == 0:
        os.replace(os.path.join(out, 'freeze_numbers.json'), os.path.join(out, 'freeze_numbers_regen.json'))
        shutil.copy2(os.path.join(B, 'freeze_numbers.json'), os.path.join(out, 'freeze_numbers.json'))
    STATE['steps']['summarize'] = dict(exit=rc, governing_restored=bool(sha(os.path.join(out, 'freeze_numbers.json'))
                                                                        == sha(os.path.join(B, 'freeze_numbers.json'))))
    save_state()
    th[0].join()
    # 7
    comp = {}
    for name in ('linear_L3', 'linear_L2', 'spreads_L2', 'dynamics_C1', 'dynamics_C2a', 'dynamics_C2b', 'dynamics_C3',
                 'dynamics_C3_rate'):
        p_new = os.path.join(out, f'{name}.json')
        if not os.path.exists(p_new):
            comp[name] = dict(outcome='MISSING')
            continue
        rep = qc.compare(json.load(open(p_new)), json.load(open(os.path.join(CF, f'{name}.json'))), 'bitwise')
        c = dict(outcome=rep.outcome(), n=rep.n, fail=rep.fail[:20], diff=rep.diff[:20], iter_moved=rep.iter_moved)
        if name.startswith('dynamics'):
            c['npy_bit_identical'] = qc.compare_npy(os.path.join(out, f'{name}.npy'), os.path.join(CF, f'{name}.npy'))
            c['s5'] = unit_check_s5(json.load(open(p_new)), np.load(os.path.join(out, f'{name}.npy')))
        comp[name] = c
    tD = os.path.join(out, 'theoremD_L3.json')
    comp['theoremD_L3'] = (dict(present=True, record=json.load(open(tD))) if os.path.exists(tD) else dict(present=False))
    fz_new, fz_old = os.path.join(out, 'freeze_numbers_regen.json'), os.path.join(B, 'freeze_numbers.json')
    if os.path.exists(fz_new):
        a, b = json.load(open(fz_new)), json.load(open(fz_old))
        s2 = {k: abs(a['s2'][k] - b['s2'][k]) / abs(b['s2'][k]) for k in b['s2']}
        a2, b2 = copy.deepcopy(a), copy.deepcopy(b)
        a2.pop('s2', None); b2.pop('s2', None)
        rest = qc.compare(a2, b2, 'bitwise')
        rec = {'R4': 1.054e-10, 'R5': 2.23e-11, 'R2': 2.00e-11}
        comp['freeze_numbers'] = dict(s2_relative=s2, s2_as_recorded={k: bool(f'{s2[k]:.3g}' == f'{rec[k]:.3g}') for k in rec},
                                      rest=rep_summary(rest))
    for case in ('C3_R4', 'C2a_R4'):
        p_new = os.path.join(out, f'branch_{case}.json')
        if not os.path.exists(p_new):
            comp[f'branch_{case}'] = dict(outcome='MISSING')
            continue
        rep = qc.compare(json.load(open(p_new)), json.load(open(os.path.join(B, f'branch_{case}.json'))), 'branch')
        comp[f'branch_{case}'] = dict(outcome=rep.outcome(), n=rep.n, fail=rep.fail[:30], n_diff=len(rep.diff),
                                     floor_used=rep.floor_used[:40], n_floor=len(rep.floor_used), iter_moved=rep.iter_moved)
    STATE['steps']['comparisons'] = comp
    STATE['finished'] = now()
    save_state()
    L = [f'M8.15.x qualification, started {STATE["started"]}, finished {STATE["finished"]}']
    for k, v in STATE['steps'].items():
        L.append(f'{k}: {json.dumps(v, default=str)[:1500]}')
    open(os.path.join(Q, 'QUALIFICATION.log'), 'w').write('\n'.join(L) + '\n')
    log('qualification finished')


def rep_summary(rep):
    return dict(outcome=rep.outcome(), fail=rep.fail[:20], diff=rep.diff[:20])


if __name__ == '__main__':
    main()
