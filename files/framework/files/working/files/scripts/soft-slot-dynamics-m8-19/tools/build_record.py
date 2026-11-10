#!/usr/bin/env python3
"""Post-run: made after M8.19's registered run. It builds RECORD.md from this folder's files, so that every number, time
and hash in the record is read from the bytes it names. It follows M8.18's tools/build_record.py, carried to M8.19's
waves: gate 1, the rows' gates, the coherent row's ladder, the plan, the test and the record job.

Usage, from this folder: python3 -I -B tools/build_record.py [--check]
  --check:  build the record and compare it with RECORD.md, without writing; exit 1 on any difference.

It refuses if a logged output differs from the SHA-256 the run's log recorded (an archival copy: if its index does not
give that SHA-256 for its original), if the freeze does not validate, if a gate recomputed with the frozen
m819_gates from its stored input differs from its record, if a dynamics verdict recomputed from its stored series with
the frozen persistence.evaluate differs from its record, if the plan or the record job's RECORD.json differs from what
the folders give, or if a fact this record takes from DEVLOG.md is not there as stated. It imports the frozen driver,
which sets its four threading variables, and writes nothing but RECORD.md."""
import ast
import datetime
import hashlib
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import numpy as np  # noqa: E402
import m819_branch as D  # noqa: E402
import m819_gates as G  # noqa: E402
from persistence import evaluate  # noqa: E402

OUT = os.path.join(ROOT, 'run', 'out')
OW = 'https://github.com/openwave-labs/openwave'
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
ROWS = list(D.ROWS)
DYN = (('dyn_C1', 'dynamics_C1'), ('dyn_C2a', 'dynamics_C2a'), ('dyn_C2b', 'dynamics_C2b'), ('dyn_C3', 'dynamics_C3'),
       ('rate', 'dynamics_C3_rate'), ('c3e3', 'dynamics_C3_eps3'))
# the archival copies whose originals OpenWave's freeze blocks name by SHA-256, and where
NAMED = {'freeze2/freeze_2.py': "the second block's § The scripts", 'freeze2/freeze_2.out': "the second block's § The scripts",
         'freeze2/checks_before_write_2.py': "the second block's § The scripts",
         'freeze2/verify_frozen_2.py': "the second block's § The scripts",
         'freeze/rehearse_env.py': "the second block's § The scripts", 'freeze/rehearse_launch.py': "the second block's § The scripts",
         'freeze2/freeze_2_rehearsal.out': "the second block's § The scripts",
         'freeze/freeze_block.py': "#702's body", 'freeze2/freeze_block_2.py': "#703's body"}
POSTRUN = ('environment_postrun_2026-11-10.txt', 'tools/postrun_env.py', 'tools/build_record.py', 'ARCHIVAL.json')


class Refused(Exception):
    pass


def need(ok, why):
    if not ok:
        raise Refused(why)


rb = lambda p: open(os.path.join(ROOT, p), 'rb').read()
rd = lambda p: open(os.path.join(ROOT, p), encoding='utf-8').read()
js = lambda p: json.loads(rd(p))
sha = lambda b: hashlib.sha256(b).hexdigest()
ts = lambda s: datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')
rt = lambda o: json.loads(json.dumps(o, default=str))


def sci(x, d=3):
    if x == 0:
        return '0'
    m, e = f'{x:.{d - 1}e}'.split('e')
    return f'{m}×10{str(int(e)).translate(SUP)}'


def fe(x):
    """A ladder point as the census writes it: 0.25, 0.3536, 1.41, 2.83, 22.63, 32."""
    if float(x).is_integer():
        return str(int(x))
    return f'{x:.4g}' if x < 1 else f'{x:.2f}'


def hms(s):
    s = int(round(s))
    return f'{s // 3600} h {(s % 3600) // 60:02d} min' if s >= 3600 else f'{s // 60} min'


def listing(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]


def entry(n, text):
    m = re.search(rf'^## {n}\. .*?(?=^## \d+\. |\Z)', text, re.M | re.S)
    need(m, f'DEVLOG.md has no entry {n}')
    return m.group(0)


def fact(n, text, pat, what):
    m = re.search(pat, entry(n, text), re.S)
    need(m, f'DEVLOG.md entry {n}: {what} is not there as stated')
    return m


def run_eta():
    """The rate run's eta, as job_dyn passes it to m815_controls.dynamics, read from the frozen driver's source."""
    src = open(os.path.join(ROOT, 'run', 'm819_branch.py'), encoding='utf-8').read()
    fn = next(n for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef) and n.name == 'job_dyn')
    calls = [c for c in ast.walk(fn) if isinstance(c, ast.Call) and any(k.arg == 'tag' for k in c.keywords)]
    need(len(calls) == 1, "job_dyn's rate call")
    return ast.literal_eval(next(k.value for k in calls[0].keywords if k.arg == 'eta'))


def recheck_series(rec, j, eta):
    """The frozen evaluate on a stored series against its record: exact on the verdict, validity and distances; within
    10^-8 relative on the three energy fields, whose reference energy is rebuilt from the recorded energy_pert."""
    Eref = rec[0, 6] * (1 - j['energy_pert'])
    ev = evaluate(rec, eta, Eref)
    for k, v in ev.items():
        if k in ('energy_pert', 'energy_dev_vs_pert', 'energy_secular_drift'):
            need(abs(v - j[k]) <= 1e-8 * abs(j[k]), f'{k} recomputed')
        else:
            need(v == j[k], f'{k} recomputed: {v} against {j[k]}')
    return ev


def build():
    a = Lines()
    L = js('run/out/RUNLOG.json')
    F = js('run/FROZEN.json')
    pin = rd('run/FROZEN_PIN').strip()
    E = js('run/ENVIRONMENT.json')
    AR = js('ARCHIVAL.json')
    copies = AR['copies']
    dv = rd('DEVLOG.md')
    terms = rd('run/m8_19_task_details.md')

    # --- the run's log and its files
    ids = [j['id'] for j in L['jobs']]
    need(L['pin'] == pin == sha(rb('run/FROZEN.json')), "the log's pin is not the freeze's")
    need(L['bench'] is False and len(L['launches']) == 1 and L['stop'] is None, 'the log: bench, launches or stop')
    need(sorted(L['completed']) == sorted(ids) and L['ended'] == {} and L['not_run'] == {}, 'a job not completed')
    ev = L['events']
    starts = [e for e in ev if e['event'] == 'started']
    need(sorted(e['job'] for e in starts) == sorted(ids) and all(e['start'] == 1 for e in starts), 'a job started twice')
    need(ev[0]['event'] == 'launch' and ev[0]['number'] == 1 and ev[-1]['event'] == 'launch ended'
         and ev[-1]['pending'] == [] and ev[-1]['stopped'] is None, "the log's ends")
    launch, end = L['launches'][0], ev[-1]['t']
    added = [e for e in ev if e['event'] == 'plan read']
    need(len(added) == 1, 'the plan read once')
    nlogged, as_logged, arch_logged = 0, [], []
    for job, c in L['completed'].items():
        need(sorted(os.listdir(os.path.join(OUT, job))) == sorted(c['files']), f'{job}: its files')
        for f, h in c['files'].items():
            rel = f'run/out/{job}/{f}'
            nlogged += 1
            if rel in copies:
                need(copies[rel]['original_sha256'] == h and sha(rb(rel)) == copies[rel]['copy_sha256'], f'{rel}: archival')
                arch_logged.append(rel)
            else:
                need(sha(rb(rel)) == h, f'{rel}: off its logged SHA-256')
                as_logged.append(rel)
    need(sorted(set(os.listdir(OUT)) - {'RUNLOG.json'}) == sorted(L['completed']), 'a folder outside the log')
    for rel, c in copies.items():
        need(sha(rb(rel)) == c['copy_sha256'], f'{rel}: not at its copy SHA-256')
        marks = (("os.environ['M819_",) if c['kind'] == 'script' else ('<the bench>', '<an MIT clone>', '<an OpenWave clone>'))
        lines = [n for n, ln in enumerate(rd(rel).split('\n'), 1) if any(m in ln for m in marks)]
        need(lines == c['lines'], f'{rel}: its marked lines')

    # --- the freeze
    Fv = D.validate_frozen()
    need(Fv == F, 'validate_frozen')
    K = 'freeze/first_freeze/run'
    F1 = js(f'{K}/FROZEN.json')
    E1 = js(f'{K}/ENVIRONMENT.json')
    pin1 = rd(f'{K}/FROZEN_PIN').strip()
    need(pin1 == sha(rb(f'{K}/FROZEN.json')) and F1['pins']['run/ENVIRONMENT.json'] == sha(rb(f'{K}/ENVIRONMENT.json')),
         'the first freeze is not at its pins')
    need(F['pins']['run/ENVIRONMENT.json'] == sha(rb('run/ENVIRONMENT.json')), 'the second record is not at its pin')
    dF = sorted(k for k in set(F) | set(F1) if F.get(k) != F1.get(k))
    dP = sorted(k for k in set(F['pins']) | set(F1['pins']) if F['pins'].get(k) != F1['pins'].get(k))
    need(dF == ['go', 'pins', 'written'] and dP == ['run/ENVIRONMENT.json'], 'the two FROZEN.json differ beyond the ruling')

    def flat(d, pre=''):
        out = {}
        for k, v in d.items():
            out.update(flat(v, f'{pre}{k}.') if isinstance(v, dict) else {f'{pre}{k}': v})
        return out
    fe1, fe2 = flat(E1), flat(E)
    dE = sorted(k for k in set(fe1) | set(fe2) if fe1.get(k) != fe2.get(k))
    thr = [k for k in dE if k.startswith('threading.')]
    need(dE == ['recorded'] + thr and len(thr) == 4 and all(fe1[k] is None and fe2[k] == '1' for k in thr),
         'the two environment records differ beyond the ruling')
    refused = rd('freeze/launch_1_refused.out')
    need(("differences: " + repr(thr)) in refused and 'REFUSED: the environment differs' in refused,
         "the refused launch's output")
    con = rd('freeze2/launch_2.out').rstrip('\n').split('\n')
    need('differences: none' in con and con[-1] == f'{end} launch ended; pending []; stop None', "the launch's console")
    procs = {e['job']: e['pid'] for e in ev if e['event'] == 'process'}
    for e in starts:
        need(f"{e['t']} started {e['job']} (start 1, pid {procs[e['job']]})" in con, f"the console: {e['job']}")
    post = rd('environment_postrun_2026-11-10.txt')
    tpost = re.match(r'# read after the run, at (\S+)\n', post).group(1)
    need(f"validate_frozen: passed; {len(F['pins'])} pins; go {F['go']}\n" in post
         and post.endswith('differences: none\nexit 0\n'), 'the post-run reading')

    # --- facts from DEVLOG.md
    m = fact(11, dv, r'\*\*The go,\*\* \[`issuecomment-\d+`\]\((\S+?)\), at (\S+Z), unedited', 'the go')
    go_link, t_go = m.group(1), m.group(2)
    folder_commit = fact(11, dv, r"MIT's `origin/main` is at `([0-9a-f]{8})`", 'the folder commit').group(1)
    m = fact(11, dv, r'`shasum -a 256 -c SHA256SUMS` in this folder at (\S+Z): (\d+) of (\d+) OK, exit 0', 'the check')
    t_sums, n_sums = m.group(1), int(m.group(2))
    t_o702 = fact(14, dv, r'Blake opened \[#702\]\(\S+\) at (\S+Z)\.', "#702's opening").group(1)
    t_ref = fact(16, dv, r'the launch ended at (\S+Z), the time of its output', 'the refused launch').group(1)
    m = fact(17, dv, r'merged at (\S+Z) as `([0-9a-f]{8})`', "#702's merge")
    t_m702, c702 = m.group(1), m.group(2)
    m = fact(20, dv, r'\*\*The ruling,\*\* \[`issuecomment-\d+`\]\((\S+?)\), at (\S+Z), unedited', 'the ruling')
    ruling_link, t_ruling = m.group(1), m.group(2)
    need(ruling_link == F['go'], "the ruling is not FROZEN.json's go")
    t_o703 = fact(25, dv, r'\*\*#703\*\*, opened by Blake at (\S+Z)', "#703's opening").group(1)
    m = fact(26, dv, r'merged by xrodz at (\S+Z) as `([0-9a-f]{8})`', "#703's merge")
    t_m703, c703 = m.group(1), m.group(2)
    fact(30, dv, r'\("send it"\), at ' + re.escape(launch), 'the launch on the author\'s word')
    order = [('the go', t_go, 'DEVLOG.md, entry 11'),
             (f'the folder checked against `SHA256SUMS` at `{folder_commit}`', t_sums, 'DEVLOG.md, entry 11'),
             ('the first `run/ENVIRONMENT.json` recorded, from the shell', E1['recorded'], f'`{K}/ENVIRONMENT.json`'),
             ('the first `run/FROZEN.json` written', F1['written'], f'`{K}/FROZEN.json`'),
             ('#702 opened', t_o702, 'DEVLOG.md, entry 14'),
             ('the launch on the first freeze refused, before its first job', t_ref, 'DEVLOG.md, entry 16'),
             ('#702 merged', t_m702, 'DEVLOG.md, entry 17'),
             ('the ruling', t_ruling, 'DEVLOG.md, entry 20'),
             ('the second `run/ENVIRONMENT.json` recorded, by the launch\'s route', E['recorded'], '`run/ENVIRONMENT.json`'),
             ('the second `run/FROZEN.json` written', F['written'], '`run/FROZEN.json`'),
             ('#703 opened', t_o703, 'DEVLOG.md, entry 25'),
             ('#703 merged', t_m703, 'DEVLOG.md, entry 26'),
             ("the launch: the run's log opens", launch, '`run/out/RUNLOG.json`'),
             ("the run's log ends", end, '`run/out/RUNLOG.json`'),
             ('the environment read again, by the launch\'s route', tpost, '`environment_postrun_2026-11-10.txt`')]
    tt = [ts(t) for _, t, _ in order]
    need(all(x <= y for x, y in zip(tt, tt[1:])), 'the order is not in time')

    # --- gate 1, recomputed
    C = js('run/out/controls/CONTROLS.json')
    eta = float(D.frozen_numbers('C1')['eta'])
    eta_rate = run_eta()
    series = {}
    for job, nm in DYN:
        j = js(f'run/out/{job}/{nm}.json')
        series[job] = (j, recheck_series(np.load(os.path.join(OUT, job, f'{nm}.npy')), j, eta_rate if job == 'rate' else eta))
    cd = js('run/out/c2a_dur/c2a.json')
    series['c2a_dur'] = (cd['test'], recheck_series(np.load(os.path.join(OUT, 'c2a_dur', 'test.npy')), cd['test'], eta))
    want = {'dyn_C1': 'Persists', 'dyn_C2a': 'Persists', 'dyn_C2b': 'Persists', 'dyn_C3': 'Fails'}
    for job, w in want.items():
        j = series[job][0]
        need(C['controls'][job] == dict(passed=j['verdict'] == w and j['valid'], verdict=j['verdict'], wanted=w,
                                        max_dperp=j['max_dperp'], t_fail=j['t_fail']), f'gate 1: {job}')
    rec = np.load(os.path.join(OUT, 'rate', 'dynamics_C3_rate.npy'))
    t, dp = rec[:, 0], rec[:, 2]
    sel = (dp >= 10 * eta_rate) & (dp <= 1e4 * eta_rate)
    rate = float(np.polyfit(t[sel], np.log(dp[sel]), 1)[0])
    lin2 = float(max(abs(complex(z[0], z[1])) for z in series['rate'][0]['level2_rates']))
    # the fit's last digits move with the platform's linear algebra: it is compared within 10^-12 relative, the rest exactly
    cr0 = C['controls']['rate']
    need(sorted(cr0) == ['fitted', 'linear_L2', 'passed', 'points'] and abs(cr0['fitted'] - rate) <= 1e-12 * abs(cr0['fitted'])
         and cr0['linear_L2'] == lin2 and cr0['points'] == int(sel.sum())
         and cr0['passed'] == (abs(cr0['fitted'] / lin2 - 1) <= 0.05) == (abs(rate / lin2 - 1) <= 0.05), 'gate 1: the rate')
    p5 = js('run/out/p5a/control_1a_arm.json')
    need(p5['control']['passed'] == (p5['ok'] and p5['iterations'][-1]['res'] < 1e-11) and p5['arm'] == 'bench',
         'gate 1: control 1a')
    need(C['controls']['c3e3'] == dict(series['c3e3'][0]['control'], verdict=series['c3e3'][0]['verdict'])
         and series['c3e3'][0]['verdict'] == 'Fails', 'gate 1: C3 at 3')
    need(C['controls']['c2a_dur'] == cd['control'] and cd['control']['passed'] and cd['T'] == cd['T_gate6'] == 2750
         and cd['test']['verdict'] == 'Persists' and cd['test']['valid'], 'gate 1: C2a/R4 at 1')
    need(C['all_passed'] and all(v['passed'] for v in C['controls'].values()), 'gate 1 did not pass')
    v6 = {job: (s[0]['valid'], s[0]['valid_under_v6_energy_rule']) for job, s in series.items()}

    # --- the rows' gates, recomputed
    Gs = {r: js(f'run/out/{r}/gates.json') for r in ROWS}
    npts = 0
    for r in ROWS:
        g = Gs[r]
        evs = []
        for d in g['points']:
            e2 = rt(G.evaluate(d['input'], D.classify))
            need(e2 == {k: d[k] for k in e2}, f'{r} at {d["eps"]}: a gate recomputed differs')
            evs.append(e2)
            npts += 1
        strs = [s['points'] for s in g['stretches'].values()]
        need(rt(D.stretch_tests(g['row'], strs, evs)) == g['stretches'], f'{r}: the search recomputed differs')
    P = js('run/out/plan/PLAN.json')
    tests, untested = {}, {}
    for r in ROWS:
        for sid, s in Gs[r]['stretches'].items():
            if s['test']:
                tests[sid] = dict(job=r, case=Gs[r]['case'], slot=Gs[r]['slot'], **s['test'])
            else:
                untested[sid] = s['causes']
    T_max = max((x['T'] for x in tests.values()), default=None)
    need(P == rt(dict(tests=tests, untested=untested, gates_not_completed=[], T_max=T_max,
                      long_control=(T_max is not None and T_max > G.LONG_T))), 'the plan recomputed differs')
    need(added[0]['added'] == [f'test_{s}' for s in tests], "the plan's tests are not the jobs added")
    need(all(d['gates']['2']['passed'] is True for r in ROWS for d in Gs[r]['points']), 'gate 2 failed somewhere')

    # --- the test, recomputed
    need(len(tests) == 1, 'one test')
    sid = next(iter(tests))
    tj = js(f'run/out/test_{sid}/test.json')
    trec = np.load(os.path.join(OUT, f'test_{sid}', 'test.npy'))
    recheck_series(trec, tj, eta)
    series[f'test_{sid}'] = (tj, None)
    v6[f'test_{sid}'] = (tj['valid'], tj['valid_under_v6_energy_rule'])
    i_max = int(np.argmax(trec[:, 2]))

    # --- the record job's RECORD.json, against the folders
    RJ = js('run/out/record/RECORD.json')
    need(RJ['controls'] == C and RJ['ended'] == {} and RJ['not_run'] == {} and RJ['newly_identified'] == {}, 'RECORD.json')
    gc = Gs['coherent_R5']
    need(RJ['coherent_ladder'] == gc['ladder_outcome'] and gc['ladder_outcome']['other_elliptic_runs'] == [], 'the ladder')
    for r in ROWS:
        for s_id, s in Gs[r]['stretches'].items():
            x = RJ['stretches'][s_id]
            need((x['label'], x['points'], x['causes']) == (s['label'], s['points'], s['causes']), f'{s_id}')
            if s['test']:
                need(x['outcome'] == 'tested' and x['test_point'] == s['test'] and x['verdict'] == tj['verdict']
                     and (x['T'], x['periods'], x['max_dperp'], x['max_drot'], x['max_dref'], x['valid'])
                     == (tj['T'], tj['periods'], tj['max_dperp'], tj['max_drot'], tj['max_dref'], tj['valid']), s_id)
            else:
                need(x['outcome'] == 'Untested' and x['why'] == 'no point passes gates 2 to 7', s_id)
    S = RJ['stretches']
    unt = [k for k in S if S[k]['outcome'] == 'Untested']
    t1t4 = [d for r in ROWS if r != 'coherent_R5' for d in Gs[r]['points']]
    need(all(d['first_failed'] == 3 for d in t1t4), 'T1 and T4: a first failure other than gate 3')

    # --- the record's text
    J = {j: js(f'run/out/{j}/job.json') for j in ids}
    started = {e['job']: e['t'] for e in starts}
    secs = (ts(end) - ts(launch)).total_seconds()
    ladder = gc['ladder_outcome']
    tps = S[sid]
    a(f"# M8.19 run record\n")
    a(f"The record of M8.19's registered run, the census's persistence tests (S5), from {launch} to {end}. It ran under "
      f"the governing terms, `run/m8_19_task_details.md` (SHA-256 `{F['terms_sha256'][:16]}…`), merged in OpenWave "
      f"[#698]({OW}/pull/698), on this folder as MIT `{folder_commit}` holds it and M8.15.x's solver at MIT "
      f"`{F['solver_commit']}`, its manifest at `{F['instrument_manifest_sha256'][:16]}…`. The maintainer's go is "
      f"[#698's comment]({go_link}). The freeze is recorded by two blocks on OpenWave: `research/m8_19/freeze_block.md`, "
      f"merged in [#702]({OW}/pull/702), and, after the [ruling]({ruling_link}) that the freeze be written once more, "
      f"`research/m8_19/freeze_block_2.md`, merged in [#703]({OW}/pull/703). Every number below is read from this "
      f"folder's files, and `tools/build_record.py` builds this record from them: the run's in [`run/out/`](run/out/), "
      f"the freeze's in `run/`, [`freeze/`](freeze/) and [`freeze2/`](freeze2/), and the facts it takes from `DEVLOG.md`. "
      f"This record gives what the terms' § DEFINITION OF DONE asks: every stretch's outcome, the coherent row's ladder "
      f"with its own, and the record, for adjudication. Adjudication is the maintainers'.\n")
    n_t1 = sum(len(Gs[r]['points']) for r in ROWS if r.startswith('gates_T1'))
    n_t4 = sum(len(Gs[r]['points']) for r in ROWS if r.startswith('gates_T4'))
    a(f"**The outcome.** The run completed in one launch, with no stop and no job left unfinished: all {len(ids)} jobs "
      f"completed, each on its first start. **Gate 1 passed:** every control gave its stated verdict. **The coherent row "
      f"in `R5`:** its ladder is established, Elliptic at all {len(ladder['types'])} points from {fe(ladder['types'][0]['eps'])} "
      f"to {fe(ladder['types'][-1]['eps'])}, and its test, at `ε` = {fe(tps['test_point']['eps'])} with `T` = {tj['T']:g}, "
      f"**Persists, valid**. **T1's three stretches and T4's two end Untested:** at every one of their {n_t1 + n_t4} "
      f"points the first gate that failed is gate 3, the cluster and the mode. No outcome claims orbital stability or "
      f"instability.\n")
    a('**The stretches:**\n')
    a('| Stretch | Points | Outcome | Test | max d_⊥ | max d_rot | Reference floor |')
    a('|---|---|---|---|---|---|---|')
    for r in ROWS:
        for s_id, s in Gs[r]['stretches'].items():
            x = S[s_id]
            pts = f"{len(s['points'])}, {fe(s['points'][0])} to {fe(s['points'][-1])}"
            if x['outcome'] == 'tested':
                a(f"| {s['label']} | {pts} | {x['verdict']}, valid | `ε` = "
                  f"{fe(x['test_point']['eps'])}, `T` = {x['T']:g}, {x['periods']:.2f} periods of `P` = {x['test_point']['P']:.1f} | "
                  f"{sci(x['max_dperp'])} | {sci(x['max_drot'])} | {sci(x['max_dref'])} |")
            else:
                a(f"| {s['label']} | {pts} | Untested: gate 3 first at every point | none | | | |")
    a('')

    # 1. custody
    a('## 1. Custody\n')
    a("### 1.1 The order\n")
    a("The ruling's item 6 reads the run's log against the second freeze's written time and #703's opening; #702's "
      "approval read it against the go, the first freeze's written time and #702's opening. In order, each time from "
      "the file named:\n")
    a('| Event | Time | From |')
    a('|---|---|---|')
    for what, t_, src in order:
        a(f'| {what} | {t_} | {src} |')
    t_e25 = re.search(r'^## 25\. (\S+Z): ', dv, re.M).group(1)
    need(ts(t_o703) < ts(t_e25) < ts(t_m703) and 'refuse on power' in entry(25, dv), "entry 25: the checks while #703 was open")
    a(f"\nThe run's log opens after every event above it, {hms((ts(launch) - ts(t_o703)).total_seconds())} after #703's "
      f"opening: no job had started when either block's pull request was opened. It also opens "
      f"{hms((ts(launch) - ts(t_m703)).total_seconds())} after #703's merge, though #703's body allowed the launch once the "
      f"pull request was open and its DCO check passed: the checks before the launch refused on mains power and Low "
      f"Power Mode while it was open (`DEVLOG.md` entry 25), and passed after the merge (§ 1.4).\n")

    a("### 1.2 The first freeze, kept, and the refused launch\n")
    need(F1['go'] == go_link, "the first FROZEN.json's go is not the go")
    a(f"- **The first freeze.** `run/FROZEN.json` was written once, at {F1['written']}, by `run/write_guard.py`, after "
      f"the go and with [its link]({F1['go']}) as its `go`. It pins {len(F1['pins'])} files: the {len(F1['pins']) - 1} under `run/` "
      f"and `reference/` that `SHA256SUMS` lists at `{folder_commit}`, and `run/ENVIRONMENT.json`, recorded from the "
      f"shell at {E1['recorded']}. Its pin is `{pin1[:16]}…`, and #702's block carries it in full. The three files are "
      f"kept in [`{K}/`]({K}/), every byte unchanged, as the ruling's item 1 has it:\n")
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for f in ('ENVIRONMENT.json', 'FROZEN.json', 'FROZEN_PIN'):
        a(f'  | `{K}/{f}` | `{sha(rb(f"{K}/{f}"))}` |')
    a(f"\n- **The refused launch.** On the first freeze, `python3 -I -B -u run/m819_run.py` refused before its first "
      f"job, at {t_ref}: `validate_frozen` passed, and the environment check read the four threading variables as "
      f"`1`, where that record has them unset, every other field equal (\"differences: {repr(thr)}\"). The cause, which "
      f"the ruling confirms: `main()` imports the driver, which sets the four variables, before it runs the check as "
      f"a subprocess. It started no job and wrote no log, and counts toward no job's three launches (the ruling's item "
      f"5). Its output, [`freeze/launch_1_refused.out`](freeze/launch_1_refused.out), SHA-256 `{sha(rb('freeze/launch_1_refused.out'))}`, "
      f"is published as it is.\n")

    a("### 1.3 The second freeze\n")
    a(f"In the ruling's order, by `freeze2/freeze_2.py`, its output `freeze2/freeze_2.out` and each step's in "
      f"`freeze2/out/`: the first freeze's three files moved out of `run/` to `{K}/`; the folder checked against "
      f"`SHA256SUMS`; `run/ENVIRONMENT.json` recorded once more, at {E['recorded']}, by the launch's route, the run's "
      f"interpreter with `-I -B` from a process that had imported the driver; `run/FROZEN.json` written once more, at "
      f"{F['written']}, with the ruling's link as its `go`; and `main()`'s two calls replayed without `launch()`, "
      f"`validate_frozen` passing and the check reading no difference (`freeze2/out/replay_main_checks.out`). The checks "
      f"before it, read-only, are `freeze2/checks_before_write_2.py` and its output, and the read-back after it "
      f"`freeze2/verify_frozen_2.py` and its output; its rehearsal on a scratch copy is `freeze2/freeze_2_rehearsal.out`.\n")
    a(f"- The second environment record differs from the first in `recorded` and the four threading fields alone, each "
      f"from `null` to `\"1\"`. The second `FROZEN.json` differs from the first in the environment record's pin, "
      f"`written` and `go` alone: the same {len(F['pins']) - 1} other pins at the same SHA-256, and the terms, the "
      f"manifest, `solver_commit` and `freeze_numbers` unchanged. Its pin is `{pin[:16]}…`, the pin the run's log "
      f"records, and #703's block carries it in full.\n")
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for f in ('ENVIRONMENT.json', 'FROZEN.json', 'FROZEN_PIN'):
        a(f'  | `run/{f}` | `{sha(rb(f"run/{f}"))}` |')
    a('')

    a("### 1.4 Before the launch\n")
    pf = rd('freeze2/preflight_checks_2_merged_run2.out')
    pf_ok = [ln[6:].split(':', 1)[0] for ln in pf.split('\n') if ln.startswith('ok    ')]
    need(pf.rstrip('\n').endswith('pre-flight 2, after the merge: PASS') and 'FAIL  ' not in pf, 'the pre-flight')
    f2 = rd('freeze2/preflight_checks_2.out')
    f2_ok = sum(ln.startswith('ok    ') for ln in f2.split('\n'))
    f2_fail = ast.literal_eval(f2.rstrip('\n').split('\n')[-1].split(': ', 2)[-1])
    f3 = rd('freeze2/preflight_checks_2_merged.out')
    f3_ok = sum(ln.startswith('ok    ') for ln in f3.split('\n'))
    f3_fail = ast.literal_eval(f3.rstrip('\n').split('\n')[-1].split(': ', 2)[-1])
    mm = [rd(f'freeze2/mutations_preflight_2_merged{s}.out').rstrip('\n').split('\n')[-1] for s in ('', '_2', '_3')]
    m703 = rd('freeze2/merge_703.out')
    need(m703.rstrip('\n').endswith('merge 703: PASS'), "#703's read-back")
    m703_ok = sum(ln.startswith('ok    ') for ln in m703.split('\n'))
    mu703 = rd('freeze2/mutations_merge_703.out').rstrip('\n').split('\n')[-1]
    pf1 = rd('freeze/preflight_checks.out')
    need(pf1.rstrip('\n').endswith('pre-flight: PASS'), 'the first pre-flight')
    LOAD = 'no other process above 50% of a core'
    for lab in ('shasum -a 256 -c SHA256SUMS', "by the launch's route, in a fresh process", 'no run/out/ yet',
                'the first freeze kept, its three files at the pins #702 records', 'no cache in the instrument',
                'the go live equals its kept copy, unedited', 'the ruling live equals its kept copy, unedited',
                'the approval, as kept and unedited', "the second block on OpenWave's main, byte for byte",
                'on mains power', 'Low Power Mode off', 'no macOS update set to download or install by itself',
                "macOS is the environment record's", LOAD, 'no M8.19 driver or orchestrator process running'):
        need(lab in pf_ok, f'the pre-flight: {lab}')
    mut_bad = []
    for s in ('', '_2'):
        for ln in rd(f'freeze2/mutations_preflight_2_merged{s}.out').split('\n'):
            if ln.startswith('BAD   '):
                red = ast.literal_eval(re.search(r'red on (\[.*\]) besides', ln).group(1))
                need(LOAD in red, 'an arm BAD but for the load check')
                mut_bad.append(ln)
    need(mm[2].endswith('PASS 7 arms and the control') and "'mds_stores'" in f3, 'the arms')
    a(f"- **The checks before the launch,** read-only, by `freeze2/preflight_checks_2_merged.py`, revised for #703's "
      f"merge from `freeze2/preflight_checks_2.py` by the changes `freeze2/preflight_checks_2_to_merged.diff` shows. "
      f"Its run before the launch, `freeze2/preflight_checks_2_merged_run2.out`, passed all {len(pf_ok)}. Among them: the "
      f"bench's copy against `SHA256SUMS`, the commit's tree and the second freeze's three files and nothing else, with no "
      f"`run/out/`; `validate_frozen` and the environment check by the launch's route, in a fresh process; the first "
      f"freeze kept at #702's pins; the instrument at its manifest, with no cache; the go, the ruling and #703's approval "
      f"unedited, #702 and #703 merged and the second block on OpenWave's `main` byte for byte; mains power, Low Power "
      f"Mode off, no macOS update set to install itself and macOS the record's; disk and load; and no M8.19 process.")
    a(f"- **Its earlier runs stand,** with nothing launched after either: `freeze2/preflight_checks_2.out`, before #703's "
      f"merge, {f2_ok} passed and {len(f2_fail)} failed ({'; '.join(f2_fail)}); and `freeze2/preflight_checks_2_merged.out`, "
      f"{f3_ok} passed and {len(f3_fail)} failed ({'; '.join(f3_fail)}), with `mds_stores`, Spotlight's indexer, above "
      f"half a core.")
    a(f"- **The revised checks' mutation arms,** `freeze2/mutations_preflight_2_merged.py`, run three times. In the first "
      f"two, the strict comparison marked {len(mut_bad)} arms BAD in all, each with the load check red beside its named "
      f"checks while a browser ran (`DEVLOG.md` entry 27); the third: \"{mm[2]}\".")
    a(f"- **#703's merge, read back** by `freeze2/merge_703.py`: {m703_ok} checks passed, \"merge 703: PASS\"; its arms: "
      f"\"{mu703}\".")
    a(f"- **On the first freeze,** before the refused launch: `freeze/preflight_checks.py` and its output, \"pre-flight: "
      f"PASS\".\n")

    a("### 1.5 The launch and the run\n")
    np_v, sp_v = E['numpy']['version'], E['scipy']['version']
    a(f"- **The launch.** One launch on the second freeze, on the author's word, by the command `DEVLOG.md` entry 30 "
      f"records, from this folder, as a background task on mains power with Low Power Mode off: `python3 -I -B -u "
      f"run/m819_run.py`, its console into `freeze2/launch_2.out`. Before `launch()`, `main()` ran `validate_frozen` and "
      f"the environment check by the launch's route; the console shows the record, the live reading and \"differences: "
      f"none\". `launch()` held `caffeinate -i -s -w` on the orchestrator's process.")
    a(f"- **The run.** Its log, `run/out/RUNLOG.json`, opened at {launch} at the second freeze's pin, not on the bench, "
      f"its launch numbered 1, and ended at {end}, {int(secs)} s later. Each of its {len(ids)} jobs started once and "
      f"completed, at most four at once and each on one thread; none ended its part of the run, none was not run, and no "
      f"stop was recorded. The plan read the gates and added one test, `test_{sid}`. The environment, as "
      f"`run/ENVIRONMENT.json` records it: {E['interpreter']['implementation']} {E['interpreter']['version']}, NumPy "
      f"{np_v} and SciPy {sp_v}, on Accelerate's BLAS and LAPACK as each reports them, under {E['os']['product']} "
      f"{E['os']['version']} ({E['os']['build']}) on one {E['machine']['cpu']} ({E['machine']['model']}), "
      f"{E['machine']['performance_cores']} performance and {E['machine']['efficiency_cores']} efficiency cores, the four "
      f"threading variables at `1`.\n")
    a('  | Job | Wave | Started | Completed | Seconds | Peak resident, GB |')
    a('  |---|---|---|---|---|---|')
    for j in L['jobs']:
        c = L['completed'][j['id']]
        a(f"  | `{j['id']}` | {j['wave']} | {started[j['id']]} | {c['t']} | {int((ts(c['t']) - ts(started[j['id']])).total_seconds())} | "
          f"{J[j['id']]['peak_gb']:.2f} |")
    a('')

    a("### 1.6 After the run\n")
    fact(31, dv, r'The staging folder is empty, there is no `interrupted/`', 'the staging folder at the end')
    if arch_logged:
        jobs_ = listing([f"`{r.split('/')[2]}`" for r in sorted(arch_logged)])
        a(f"- **The outputs.** The run's log records {nlogged} files for the completed jobs. {len(as_logged)} are published "
          f"byte for byte, each at its logged SHA-256. The console logs of {jobs_} are published as path-redacted archival "
          f"copies, at SHA-256 values of their own (§ 1.7); `ARCHIVAL.json` gives each copy's SHA-256 and its original's, "
          f"the one the log records. The originals are not in this folder, so their logged SHA-256 cannot be recomputed "
          f"from the copies alone. No folder in `run/out/` stands outside the log, and the staging folder was empty when "
          f"the run ended (`DEVLOG.md` entry 31).")
    else:
        a(f"- **The outputs.** The run's log records {nlogged} files for the completed jobs, and each is published byte "
          f"for byte at its logged SHA-256. No folder in `run/out/` stands outside the log, and the staging folder was "
          f"empty when the run ended (`DEVLOG.md` entry 31).")
    a(f"- **The environment, read again** after the run, at {tpost}, by the launch's route, `tools/postrun_env.py`, "
      f"which replays `main()`'s two calls as `freeze2/freeze_2.py` replayed them: `validate_frozen` passed, with "
      f"{len(F['pins'])} pins and the ruling as its go, and the check read no difference "
      f"(`environment_postrun_2026-11-10.txt`).\n")

    a("### 1.7 The published files\n")
    a(f"- **As published from the run:** `run/out/`, {sum(len(c['files']) for c in L['completed'].values()) + 1} files, "
      f"the log among them, each at the SHA-256 below"
      + (f"; the {len(arch_logged)} console logs marked are archival copies, each beside its original's SHA-256, the one "
         f"the log records" if arch_logged else '') + '.\n')
    a('  | File | SHA-256 |')
    a('  |---|---|')
    a(f"  | `run/out/RUNLOG.json` | `{sha(rb('run/out/RUNLOG.json'))}` |")
    for j in ids:
        for f in sorted(L['completed'][j]['files']):
            rel = f'run/out/{j}/{f}'
            if rel in copies:
                a(f"  | `{rel}` | `{copies[rel]['copy_sha256']}`, an archival copy of `{copies[rel]['original_sha256']}` |")
            else:
                a(f"  | `{rel}` | `{sha(rb(rel))}` |")
    fz = sorted(r for r in all_files() if r.startswith(('freeze/', 'freeze2/')))
    fz_as_is = [r for r in fz if r not in copies]
    fz_arch = [r for r in fz if r in copies]
    a(f"\n- **The freeze's files,** from beside the folder on the bench: everything `freeze/` and `freeze2/` held but "
      f"the bench's DEVLOG writers, its packet cover and the pull requests' text builders, which wrote prose, not "
      f"records. {len(fz_as_is)} go out as they are:\n")
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for r in fz_as_is:
        a(f'  | `{r}` | `{sha(rb(r))}` |')
    a(f"\n- **The marked archival copies.** {len(copies)} files name a local path: {len(fz_arch)} of the freeze's, and "
      f"the {len(arch_logged)} console logs. Each goes out as its original with each path replaced: in a script, a quoted "
      f"path by `os.environ['M819_BENCH']`, `os.environ['M819_MIT_CLONE']` or `os.environ['M819_OPENWAVE_CLONE']`, plus "
      f"the rest of the quoted text, and the clone's path from the home folder, inside `os.path.expanduser`, by "
      f"`os.environ['M819_OPENWAVE_CLONE_FROM_HOME']`; in an output, the path by `<the bench>`, `<an MIT clone>` or `<an "
      f"OpenWave clone>`, the placeholder the second block shows. `ARCHIVAL.json` gives the rule, and for each copy its original's SHA-256, "
      f"its own and the lines where they differ; no copy claims its original's. A reader without the paths cannot "
      f"rebuild an original; on the bench, putting them back gives each original byte for byte. Where a block or a "
      f"pull request's body names the original's SHA-256, it is the one below.\n")
    a("  | Copy | Original's SHA-256 | The copy's SHA-256 | Lines that differ | The original named in |")
    a('  |---|---|---|---|---|')
    for r in sorted(copies):
        c = copies[r]
        a(f"  | `{r}` | `{c['original_sha256']}` | `{c['copy_sha256']}` | {', '.join(str(n) for n in c['lines'])} | "
          f"{NAMED.get(r, 'the run log' if r.startswith('run/out/') else 'this record')} |")
    a(f"\n- **Post-run files,** made or placed after the run, not records from it:")
    a(f"  - `environment_postrun_2026-11-10.txt` and `tools/postrun_env.py`, the reading after the run (§ 1.6);")
    a(f"  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference;")
    a(f"  - `ARCHIVAL.json`, the index of the archival copies;")
    a(f"  - `DEVLOG.md`: entries 1 to 10 as MIT `{folder_commit}` holds them, then entries 11 to "
      f"{re.findall(r'^## (\d+)\. ', dv, re.M)[-1]}, kept beside the folder from the freeze to the record, since the go "
      f"pins this file through `SHA256SUMS`, and copied here byte for byte. Their paths are the bench's: `../freeze/` "
      f"and `../freeze2/` beside the folder are this folder's `freeze/` and `freeze2/`, and the review packets they name "
      f"stay on the bench;")
    a(f"  - `SHA256SUMS`, regenerated over the published folder at the record's commit, one line per file but itself. The "
      f"pre-run inventory stays at MIT `{folder_commit}`.\n")
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for r in POSTRUN:
        a(f"  | `{r}` | `{sha(rb(r))}`{', as it built this record' if r == 'tools/build_record.py' else ''} |")
    a('')

    # 2. gate 1
    a('## 2. Gate 1: the controls\n')
    a("`controls` read the eight wave-1 records, and every control passed (`run/out/controls/CONTROLS.json`, "
      "`all_passed`). This record recomputes each dynamics verdict from its stored series with the frozen "
      "`persistence.evaluate`, and the rate as `job_controls` fits it; each equals its record.\n")
    a('| Control | The terms ask | The run reads | Passed |')
    a('|---|---|---|---|')
    for job, label, ask in (('dyn_C1', None, 'Persists'), ('dyn_C2a', None, 'Persists'), ('dyn_C2b', None, 'Persists'),
                            ('dyn_C3', None, 'Fails')):
        j = series[job][0]
        nm = job[4:]
        what = (f"Fails at `t` = {j['t_fail']:.2f}" if j['verdict'] == 'Fails' else f"Persists, max d_⊥ {sci(j['max_dperp'])}")
        a(f"| {nm} at `ε` = {fe(j['eps'])} | {ask} | {what}, {'valid' if j['valid'] else 'not valid'} | "
          f"{'yes' if C['controls'][job]['passed'] else 'no'} |")
    cr = C['controls']['rate']
    a(f"| C3's rate run, `η` = {sci(eta_rate, 1)} | the fitted rate within 5% of the linear one | {cr['fitted']:.6f} "
      f"against {cr['linear_L2']:.6f} at level 2, {abs(cr['fitted'] / cr['linear_L2'] - 1) * 100:.2f}% apart, over "
      f"{cr['points']} points | {'yes' if cr['passed'] else 'no'} |")
    last = p5['iterations'][-1]
    a(f"| `P5a`, control 1a | the seed solve stops under the repaired test below 10⁻¹¹ | stops at iteration "
      f"{last['it']}, at {sci(last['res'])} | {'yes' if C['controls']['p5a']['passed'] else 'no'} |")
    j = series['c3e3'][0]
    a(f"| C3 at `ε` = {fe(j['eps'])} | Fails | Fails at `t` = {j['t_fail']:.2f}, {'valid' if j['valid'] else 'not valid'} | "
      f"{'yes' if C['controls']['c3e3']['passed'] else 'no'} |")
    j = cd['test']
    a(f"| C2a/R4 at `ε` = 1, `T` by gate 6 | Persists, valid, at `T` = 2750 | Persists, valid, at `T` = {cd['T']:g}, "
      f"max d_⊥ {sci(j['max_dperp'])} | {'yes' if cd['control']['passed'] else 'no'} |")
    a(f"\nC3's rate run reads \"{series['rate'][0]['verdict']}\" under the frozen validity rule, as on M8.15's record; "
      f"the control is its fit. C1, C2a, C2b and C3 reproduce M8.15's record: C3 Fails at {series['dyn_C3'][0]['t_fail']:.2f} "
      f"and the rate fits {cr['fitted']:.6f} against {cr['linear_L2']:.6f}, as § Known outcomes gives them. The second "
      f"energy rule, `valid_under_v6_energy_rule`, recorded and not scored, is false on every run the frozen rule reads "
      f"valid, and true only on the rate run, which it reads invalid, as the terms disclose.\n")

    # 3. the gates
    a('## 3. The gates\n')
    a(f"Each row was solved at levels 3 and 2 along its continuation path to its highest classified point, and gates 2 "
      f"to 7 were read and written at every point before any target evolved. This record recomputes every point's gates "
      f"from its stored input with the frozen `m819_gates.evaluate` and the instrument's `classify`, and each stretch's "
      f"search with the driver's `stretch_tests`; all {npts} points and every stretch equal their records, and so does "
      f"the plan.\n")
    a(f"- **Gate 2 passed at all {npts} points:** an accepted Newton solution at levels 3 and 2, on the continuation path "
      f"from the seed, at T4's {n_t4} points as at the others.")
    a(f"- **Gate 3 failed first at every point of T1 and T4,** {n_t1 + n_t4} points. Its reasons, as each row's "
      f"`gates.json` states them:")
    for r in ROWS:
        if r == 'coherent_R5':
            continue
        g = Gs[r]
        groups = {}
        for d in g['points']:
            groups.setdefault(d['gates']['3']['why'], []).append(d['eps'])
        lab = f"{g['case']}/R{g['slot']}"
        if len(groups) == 1:
            a(f"  - **{lab}**, all {len(g['points'])} points: \"{next(iter(groups))}\".")
        else:
            parts = [f"at {listing([fe(e) for e in es])}: \"{w}\"" for w, es in groups.items()]
            a(f"  - **{lab}**, {len(g['points'])} points: {'; '.join(parts)}.")
    unb = {r: [d['eps'] for d in Gs[r]['ladder']['level2'] if d.get('balanced') is False] for r in ROWS}
    srch = {r: [d['eps'] for d in Gs[r]['ladder']['level2'] if d.get('fast_search')] for r in ROWS}
    still = all(d['fast_search']['balanced'] is False for r in ROWS for d in Gs[r]['ladder']['level2'] if d.get('fast_search'))
    need(all(not any(d.get('balanced') is False for d in Gs[r]['ladder']['points']) for r in ROWS), 'level 3 unbalanced')
    need(unb == srch and still and set(r for r in ROWS if unb[r]) == {'gates_T4_R4', 'gates_T4_R5'}, 'the fast search')
    where = '; '.join(f"{Gs[r]['case']}/R{Gs[r]['slot']} at " + listing([fe(e) for e in unb[r]]) for r in ROWS if unb[r])
    a(f"- **The Krein count at level 2.** It does not balance at {sum(len(v) for v in unb.values())} of T4's "
      f"{n_t4} points: {where}. There the frozen code ran its fast-spectrum search, which did not balance it either; "
      f"elsewhere, at both levels and in every row, the count balances. No gate reads the count or the search (§ 9).\n")

    # 4. the coherent row
    a('## 4. The coherent row in `R5`\n')
    ty = ladder['types']
    need(all(x['type'] == 'Elliptic' for x in ty) and ladder['established'] and ladder['why'] == [] and ladder['changes'] == []
         and ladder['stretch_from'] == 'ladder' and ladder['stretch'] == [x['eps'] for x in ty], 'the ladder')
    need(ladder['end'][0] == ladder['end2'][0] == 'eps_max', "the ladder's ends")
    a(f"- **The ladder.** C2a's case in `R5` from its seed along the ladder to {fe(ty[-1]['eps'])}, with M8.15's frozen "
      f"linear types at level 3 cross-checked at level 2: {len(ty)} points, every one Elliptic, no change of type, each "
      f"level's path reaching `ε_max`. The validity check at "
      f"{fe(ty[0]['eps'])} passes, its worst relative {ladder['validity_eps_min']['worst_relative']:.4f}, and the types on "
      f"the stretch on record, {fe(Gs['coherent_R5']['stretches'][sid]['points'][0])} to 2, are M8.16.1's, Elliptic, so the "
      f"ladder is established, no cause named. Its stretch is the unbroken run of Elliptic points that contains 2, here "
      f"the whole ladder, so there is no other Elliptic run, and nothing is newly identified.")
    a(f"- **The gates on its stretch,** each point's as `run/out/coherent_R5/gates.json` gives them: at gate 3 the "
      f"identified mode's Krein sign and modulus at level 2; at gate 4 the levels' relative difference and, where "
      f"OpenWave's record holds a harmonic reading, each level's from it; and gate 7's `r T` against its bound, "
      f"ln(1/(10η)) = {math.log(1 / (10 * eta)):.4f}:\n")
    a('  | `ε` | Reference | Gate 3 | Gate 4 | Gate 5 | Gate 6 | Gate 7: `r T` | First failed |')
    a('  |---|---|---|---|---|---|---|---|')
    for d in gc['points']:
        gg = d['gates']
        g3 = gg['3']
        ref = g3.get('reference') or d['input']['ref']['source']
        c3 = (f"Krein {'+' if g3['sign'] > 0 else '−'}, modulus {sci(abs(complex(*g3['mode2']['lam'])))}" if g3['passed']
              else f"fails: \"{g3['why']}\"")
        if '4' not in gg:
            c4 = 'not read'
        else:
            g4_ = gg['4']
            c4 = f"levels {g4_['levels'] * 100:.3g}%"
            if 'harmonic_3' in g4_:
                c4 += f"; the reading, {g4_['harmonic_3'] * 100:.3g}% and {g4_['harmonic_2'] * 100:.3g}%"
            if not g4_['passed']:
                c4 = f"fails: \"{g4_['why']}\""
        c5 = f"{gg['5']['share']:.4f}" if '5' in gg and gg['5'].get('share') is not None else 'not read'
        c6 = f"`P` {gg['6']['P']:.1f}, `T` {gg['6']['T']:g}" if '6' in gg and gg['6'].get('P') is not None else 'not read'
        c7 = sci(gg['7']['rT']) if '7' in gg and gg['7'].get('rT') is not None else 'not read'
        a(f"  | {fe(d['eps'])} | {ref} | {c3} | {c4} | {c5} | {c6} | {c7} | {d['first_failed'] or 'none'} |")
    a(f"\n- **The search.** The test point is the stretch's highest point at which gates 2 to 7 all pass, "
      f"{fe(tps['test_point']['eps'])}; gate 6 sets its `T` at {tps['T']:g}, from `P` = {tps['test_point']['P']:.1f}, so no "
      f"test needs more than 2750 and no longer control runs (`run/out/plan/PLAN.json`).\n")

    # 5. the test
    a('## 5. The test\n')
    a(f"`test_{sid}` reloaded the stored level-2 state at {fe(tj['eps'])}, rebuilt its point and checked it equal to the "
      f"stored one, read gates 3, 5, 6 and 7 again and found them equal, then ran the frozen `run_test` at `T` = "
      f"{tj['T']:g}: one perturbation draw at `η` = {sci(eta, 1)} with the frozen seed, level 2, split mode. It "
      f"**{tj['verdict']}, valid.** This record recomputes the verdict and every field below from `test.npy` with the "
      f"frozen `persistence.evaluate`; they equal `test.json`.\n")
    a('| Field | Value | The frozen rule |')
    a('|---|---|---|')
    a(f"| verdict | {tj['verdict']} | Fails if d_⊥ exceeds 100η = {100 * eta:g} first; Invalid (drift) if d_rot exceeds √η = {math.sqrt(eta):.4f} first; otherwise Persists if max d_⊥ ≤ 10η = {10 * eta:g} |")
    a(f"| max d_⊥ | {sci(tj['max_dperp'])}, at `t` = {trec[i_max, 0]:g} | ≤ 10η = {10 * eta:g} |")
    a(f"| max d | {sci(tj['max_d'])} | |")
    a(f"| max d_rot | {sci(tj['max_drot'])} | ≤ √η = {math.sqrt(eta):.4f} |")
    a(f"| the reference's distance, the floor | {sci(tj['max_dref'])} | ≤ η = {eta:g} |")
    a(f"| charge drift | {sci(tj['charge_drift'])} | ≤ 10⁻¹⁰ |")
    a(f"| energy oscillation, of the perturbation's energy | {tj['energy_dev_vs_pert']:.4f} | ≤ 0.25 |")
    a(f"| secular drift, of the perturbation's energy | {sci(tj['energy_secular_drift'])} | ≤ 10⁻² |")
    a(f"| read until | `t` = {tj['read_until']:.2f} | |")
    a(f"| `T`, periods of `P` = {tj['P']:.1f} | {tj['T']:g}, {tj['periods']:.2f} | at least one period, never under 1000 |")
    a(f"| `r`, the margin's rate | {sci(tj['r'])} | `r T` ≤ ln(1/(10η)) |")
    a(f"| the step, steps, observations' cadence | {tj['dt']:.6f}, {tj['N_step']}, every {tj['N_obs']} steps | |")
    a(f"| seconds | {tj['seconds']:.0f} | |")
    a(f"\nIts largest d_⊥ is at `t` = {trec[i_max, 0]:g}: the perturbation's own size, which it never exceeded. The second "
      f"energy rule, recorded and not scored, is {str(tj['valid_under_v6_energy_rule']).lower()} here, as on every valid "
      f"test on record.\n")

    # 6. the outcomes
    a('## 6. The outcomes\n')
    a("Per stretch, with no aggregate, as the terms' § THE OUTCOMES gives them:\n")
    a('| Stretch | Outcome | As the terms read it |')
    a('|---|---|---|')
    for r in ROWS:
        for s_id, s in Gs[r]['stretches'].items():
            x = S[s_id]
            if x['outcome'] == 'tested':
                a(f"| {s['label']} | {x['verdict']}, valid, at `ε` = {fe(x['test_point']['eps'])} with `T` = {x['T']:g} | "
                  f"\"the stretch has its test, as S5 asks\" |")
            else:
                a(f"| {s['label']} | Untested, gate 3 first at every point | \"where no point passes the gates, with "
                  f"each point's cause\" |")
    quote = 'a test that Persists is evidence to `T`, not beyond'
    need(quote in terms and 'the stretch has its test, as S5 asks' in terms
         and "where no point passes the gates, with each point's cause" in terms, "the terms' words")
    a(f"\nThe ladder's outcome, recorded apart: established, Elliptic at all {len(ty)} points to {fe(ty[-1]['eps'])}. No "
      f"outcome claims orbital stability or instability: in the terms' words, \"{quote}\". As the terms expected, and "
      f"claimed as no evidence: T1's three stretches untested at the cluster check, as on M8.15's record, and the "
      f"coherent row tested; for T4 they named no expected outcome. This record applies no ending under S5: under the "
      f"answer of 2026-11-07 and the readings the approval of #698 confirmed, that is the adjudication's, stretch by "
      f"stretch.\n")

    # 7. what is new
    a('## 7. What is new\n')
    a(f"- **T4's standing waves on the finite-element instrument:** accepted Newton solutions at levels 3 and 2 at all "
      f"{n_t4} of its points, where M8.15's Newton failed at the seed (the terms, § Known outcomes).")
    a(f"- **The coherent row's ladder in `R5` above `ε` = 2,** on this instrument: Elliptic at all {len(ty)} points to "
      f"{fe(ty[-1]['eps'])}.")
    a(f"- **The coherent row's first persistence test in `R5`,** at {fe(tj['eps'])}.")
    a(f"- **Each point's gate-3 cause** on T1 and T4, at both levels, and the Krein count at T4's level-2 points.")
    a(f"- **C2a/R4 at 1 at `T` = 2750,** a duration no record held, Persisting, valid.\n")

    # 8. deviations
    a('## 8. Deviations\n')
    a("- **None in the run.** It ran in the terms' order, from the pinned tree, by one command, once on the second freeze, "
      "with no relaunch and no stop. The launch refused on the first freeze and the second writing are the ruling's, "
      "recorded in § 1, and are not deviations.\n")

    # 9. corrections and reading notes
    wg = copies.get('freeze2/out/write_guard.out')
    need(wg is not None, "write_guard's output is not an archival copy")
    a('## 9. Corrections and reading notes\n')
    a(f"- **A correction to the second block.** Its § The scripts says that, but for the outputs of `freeze_2.py` and of "
      f"its rehearsal, \"the other outputs go out as they are\". `freeze2/out/write_guard.out`, the writer's step "
      f"output, names the clone of OpenWave the terms were read from, in its command line, so it goes out as a marked "
      f"archival copy like them, its original at `{wg['original_sha256']}`. The block shows that command with `<an "
      f"OpenWave clone>`, the placeholder the copy uses.")
    logs_ = listing([f'`{r}`' for r in sorted(arch_logged)])
    if arch_logged:
        a(f"- **Two console logs** go out as marked archival copies, {logs_}: each holds a warning that names the bench's "
          f"path to the instrument. Their originals are at the SHA-256 the run's log records, and no other output names "
          f"a path.")
    a("- **The fast-spectrum search.** That warning, a `ComplexWarning` from `linearize.py`, is the trace of the "
      "instrument's fast-spectrum search, whose defect M8.15.x's `REPRODUCE.md` records and leaves unrepaired: at its "
      "two real shifts the search hands a real factorization to complex ARPACK. In this run it ran only at level 2 of "
      "T4, at the points § 3 names, where the Krein count does not balance. Its output is in each point's record, "
      "`fast_search`. No gate reads it: the gates read each level's cluster check, `tau_re` and genuine modes alone "
      "(`level_data`), so the defect moves no gate (DERIVED from the frozen code). The count is recorded and read for "
      "nothing here.")
    a("- **Control 1a's arm.** `run/out/p5a/control_1a_arm.json` names its arm `bench`. That is the arm's name in "
      "M8.15.x's qualification, `qualification/control_1a.py`, which the driver writes; the run's mode is in its log, "
      "not on the bench.")
    five = sum(int((ts(L['completed'][j]['t']) - ts(started[j])).total_seconds()) for j in ('dyn_C1', 'dyn_C2a', 'dyn_C2b', 'dyn_C3', 'rate'))
    stage = five + sum(int((ts(L['completed'][j]['t']) - ts(started[j])).total_seconds()) for j in ('p5a', 'c3e3'))
    a(f"- **The approval of #698, its note on the controls' stage.** On M8.15's record the five control runs took about "
      f"12.2 hours on one thread. Here they took {five / 3600:.2f} hours in all, each on one thread beside up to three "
      f"other jobs, and the stage with `P5a` and C3 at 3, {stage / 3600:.2f}.")
    a(f"- **The approval of #698, what it did not check.** Whether T1's cluster check fails on M8.15.x's instrument as "
      f"on M8.15's: it does, at both levels at all {n_t1} points (§ 3). That M8.15.x's persistence code reproduces "
      f"M8.15's: the controls reproduce M8.15's record, C3's failure at {series['dyn_C3'][0]['t_fail']:.2f} and the rate "
      f"fit, to its digits (§ 2).")
    a("- **The go, reading 3.** The coherent ladder's stretch is the whole ladder, so the record names no other Elliptic "
      "run, and the standing the go leaves to the adjudication does not arise. The ladder above 2 stays unruled, as the "
      "go and the answer of 2026-11-07 left it; its outcome is recorded apart (§ 4).")
    a(f"- **#702's approval, what it did not check.** The first freeze's three files: in `{K}/`, at the pins it restates "
      f"(§ 1.2). `freeze_block.py`: an archival copy, its original at the SHA-256 it restates (§ 1.7). That the run had "
      f"not started: the log opens at {launch}, after the go, the first freeze's written time and #702's opening (§ 1.1).")
    a(f"- **#703's approval, what it did not check.** The published freeze files and the refused launch's output: at "
      f"the hashes § 1.2 and § 1.3 give. The scripts and `freeze_block_2.py`: marked archival copies, each beside its "
      f"original's SHA-256 (§ 1.7). The steps and the rehearsals: their outputs, published. That the run had not "
      f"started: the log opens at {launch}, after the second freeze's written time, {F['written']}, and #703's opening, "
      f"{t_o703} (§ 1.1).\n")

    # 10. follow-ups
    a('## 10. Follow-ups, outside M8.19\n')
    a("- **The catalog.** After the adjudication, the census page's dated note gives where S5 stands, in the go's words, "
      "and the roadmap's row its Done.")
    a("- **The coherent row's ladder above 2.** How the census counts it is unruled, for the adjudication.")
    a("- **T1 and T4.** Their types stand as adjudicated; their persistence is untested here, each point's cause named.")
    a("- **The Krein count at T4's level-2 points, and the fast-spectrum search's defect,** recorded, outside this "
      "registration.\n")

    # 11. reproduction
    a('## 11. Reproduction\n')
    a("From a copy of this folder, beside the instrument at `../soft-slot-dynamics-m8-15x/`:")
    a("- `shasum -a 256 -c SHA256SUMS`;")
    a("- `python3 -I -B tools/postrun_env.py OUT`, which replays `main()`'s two calls by the launch's route, "
      "`validate_frozen` and the environment check against `run/ENVIRONMENT.json`, into a new file `OUT`;")
    a("- **the registered run:** `python3 -I -B -u run/m819_run.py`, from a copy without `run/out/`;")
    a("- `python3 -I -B tools/build_record.py --check`, which rebuilds this record from the files, recomputes every gate, "
      "the search, the plan and every dynamics verdict, and reports any difference.\n")
    a("Bitwise agreement on another machine is not claimed: the reproduction rules compare bit for bit on the recorded "
      "environment, which the readings before and after the run equal.")
    text = '\n'.join(a) + '\n'
    need('—' not in text and '–' not in text, 'a dash in the record')
    return text


def all_files():
    out = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = sorted(d for d in dn if d != '__pycache__')
        for f in sorted(fn):
            if f != '.DS_Store':
                out.append(os.path.relpath(os.path.join(dp, f), ROOT))
    return sorted(out)


class Lines(list):
    def __call__(self, s):
        self.append(s)


def main():
    check = sys.argv[1:] == ['--check']
    if sys.argv[1:] and not check:
        sys.exit(__doc__)
    try:
        text = build()
    except Refused as e:
        sys.exit(f'refused: {e}')
    path = os.path.join(ROOT, 'RECORD.md')
    if check:
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else None
        if old != text:
            sys.exit('RECORD.md differs from the record the files give')
        print('RECORD.md: the files give it byte for byte')
        return
    with open(path, 'x', encoding='utf-8') as f:
        f.write(text)
    print(f'RECORD.md written: {len(text.splitlines())} lines')


if __name__ == '__main__':
    main()
