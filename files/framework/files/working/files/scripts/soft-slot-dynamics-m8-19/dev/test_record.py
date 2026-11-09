"""The record job (wave 5) on the dry run's real outputs, which the dry run's queue did not run: job_record as written,
reading the completed folders through completed(), which checks every file against the log's SHA-256. Each scenario
writes RECORD.json to a temporary folder; nothing in dev/runs/dryrun/ is written.
  A. ROWS narrowed to the stand-in's gates job as a target row: its stretch, its test at 8 and gate 1, read as filed.
  B. The same folders as the coherent row (a temporary root whose log names the stand-in's gates job coherent_R5):
     the ladder's outcome recorded apart, and nothing newly identified.
  B2. As B, with the ladder's outcome naming two other Elliptic runs (DESIGN.md, reading 3): each named apart from the
     terms' stretches, as a newly identified Elliptic stretch with no test fixed, S5 open for it, for the maintainer.
  C. The registered ROWS on the dry run's root, where no target's job ran: every stretch the terms name sent for
     adjudication with its job's cause, and so is the coherent row's ladder.

  test_record.py      prints each check; exits 1 if any fails"""
import argparse
import copy
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import m819_branch as D  # noqa: E402

RUN = os.path.join(HERE, 'runs', 'dryrun')
fails = []


def check(name, good, detail=''):
    print(f"{'ok  ' if good else 'FAIL'} {name}" + (f': {detail}' if detail else ''))
    if not good:
        fails.append(name)


def record(root, rows):
    keep = D.ROWS
    out = tempfile.mkdtemp()
    try:
        D.OUT, D.ROWS = out, rows
        D.job_record(argparse.Namespace(root=root))
        with open(os.path.join(out, 'RECORD.json')) as f:
            return json.load(f)
    finally:
        D.ROWS = keep
        shutil.rmtree(out)


def load(*p):
    with open(os.path.join(*p)) as f:
        return json.load(f)


g = load(RUN, 'gates_C2a_R4', 'gates.json')
t = load(RUN, 'test_C2a_R4_standin_1', 'test.json')
C = load(RUN, 'controls', 'CONTROLS.json')

# A
rec = record(RUN, {'gates_C2a_R4': ('C2a', 4, 'C2a_R4')})
check('A: gate 1 recorded as filed', rec['controls'] == C)
check('A: one stretch, the stand-in\'s', sorted(rec['stretches']) == ['C2a_R4_standin_1'], str(sorted(rec['stretches'])))
s = rec['stretches'].get('C2a_R4_standin_1', {})
s0 = g['stretches']['C2a_R4_standin_1']
check('A: its points, causes and test point as gates.json holds them',
      s.get('points') == s0['points'] and s.get('causes') == s0['causes'] and s.get('test_point') == s0['test'])
want = dict(outcome='tested', verdict='Persists', T=1000.0, periods=t['periods'], valid=True, max_dperp=t['max_dperp'],
            max_drot=t['max_drot'], max_dref=t['max_dref'])
check('A: the test at 8 recorded from test.json', all(s.get(k) == v for k, v in want.items()),
      json.dumps({k: s.get(k) for k in want}))
check('A: no coherent ladder, nothing newly identified, ended or not run', rec['coherent_ladder'] is None
      and rec['newly_identified'] == {} and rec['ended'] == {} and rec['not_run'] == {})

# B
tmp = tempfile.mkdtemp()
try:
    L = copy.deepcopy(load(RUN, 'RUNLOG.json'))
    L['completed']['coherent_R5'] = L['completed'].pop('gates_C2a_R4')
    with open(os.path.join(tmp, 'RUNLOG.json'), 'w') as f:
        json.dump(L, f)
    for src, dst in (('gates_C2a_R4', 'coherent_R5'), ('test_C2a_R4_standin_1', 'test_C2a_R4_standin_1'),
                     ('controls', 'controls')):
        os.symlink(os.path.join(RUN, src), os.path.join(tmp, dst))
    rec = record(tmp, {'coherent_R5': ('C2a', 5, 'C2a_R5')})
    check('B: the ladder\'s outcome recorded apart, as gates.json holds it',
          rec['coherent_ladder'] == g['ladder_outcome'] and rec['coherent_ladder']['established'] is True)
    check('B: the stretch tested as in A', rec['stretches'].get('C2a_R4_standin_1', {}).get('outcome') == 'tested')
    check('B: nothing newly identified', rec['newly_identified'] == {})
finally:
    shutil.rmtree(tmp)

# B2
tmp = tempfile.mkdtemp()
try:
    L = copy.deepcopy(load(RUN, 'RUNLOG.json'))
    entry = L['completed'].pop('gates_C2a_R4')
    os.makedirs(os.path.join(tmp, 'coherent_R5'))
    for f in entry['files']:
        if f != 'gates.json':
            os.symlink(os.path.join(RUN, 'gates_C2a_R4', f), os.path.join(tmp, 'coherent_R5', f))
    g2 = copy.deepcopy(g)
    g2['ladder_outcome']['other_elliptic_runs'] = [[16.0], [22.627416997969522, 32.0]]
    p = os.path.join(tmp, 'coherent_R5', 'gates.json')
    with open(p, 'w') as f:
        json.dump(g2, f)
    entry['files']['gates.json'] = D.sha(p)
    L['completed']['coherent_R5'] = entry
    with open(os.path.join(tmp, 'RUNLOG.json'), 'w') as f:
        json.dump(L, f)
    for src in ('test_C2a_R4_standin_1', 'controls'):
        os.symlink(os.path.join(RUN, src), os.path.join(tmp, src))
    rec = record(tmp, {'coherent_R5': ('C2a', 5, 'C2a_R5')})
    N = rec['newly_identified']
    check('B2: each other Elliptic run named apart, numbered, with its points',
          sorted(N) == ['C2a_R5_new_1', 'C2a_R5_new_2'] and N['C2a_R5_new_1']['points'] == [16.0]
          and N['C2a_R5_new_2']['points'] == [22.627416997969522, 32.0]
          and N['C2a_R5_new_1']['label'] == 'The coherent row in R5, Elliptic at 16'
          and N['C2a_R5_new_2']['label'] == 'The coherent row in R5, Elliptic from 22.6274 to 32', json.dumps(N))
    check('B2: each with no test fixed, and S5 open for it, for the maintainer',
          all(v['outcome'] == 'no test fixed' and v['why'].endswith('so S5 stays open for it, for the maintainer')
              for v in N.values()))
    check("B2: none among the terms' stretches, and none Untested", sorted(rec['stretches']) == ['C2a_R4_standin_1']
          and rec['stretches']['C2a_R4_standin_1']['outcome'] == 'tested'
          and all(v['outcome'] != 'Untested' for v in N.values()))
finally:
    shutil.rmtree(tmp)

# C
rec = record(RUN, D.ROWS)
labels = {sid for sid in D.LABELS if any(sid.startswith(ref + '_') for _, _, ref in D.ROWS.values())}
check('C: every stretch the terms name is in the record', set(rec['stretches']) == labels,
      f'{len(rec["stretches"])} of {len(labels)}')
check('C: each sent for adjudication with its job\'s cause',
      all(v['outcome'] == 'for adjudication' and v['why'].endswith(': not run') for v in rec['stretches'].values()),
      str(sorted({v['why'] for v in rec['stretches'].values()})))
check("C: the coherent row's ladder sent for adjudication with its job's cause",
      rec['coherent_ladder'] == dict(outcome='for adjudication', why='coherent_R5: not run') and rec['newly_identified'] == {},
      json.dumps(rec['coherent_ladder']))
print('stretches named:', sorted(labels))
print('PASS' if not fails else f'FAIL: {fails}')
raise SystemExit(1 if fails else 0)
