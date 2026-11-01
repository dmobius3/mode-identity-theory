#!/usr/bin/env python3
"""Post-run: made after M8.18's registered run. It builds RECORD.md from the run's files, so that every number and hash
in the record is read from the bytes it names. It follows M8.17's tools/build_record.py, carried to M8.18's two arms:
Arm B's location, Arm A's kernel and control gate, the twelve, the brackets and the row outcomes.

Usage, from this folder: python3 -I -B tools/build_record.py [--check]
  --check:  build the record and compare it with RECORD.md, without writing; exit 1 on any difference.

It refuses if an output differs from the SHA-256 the run's log recorded, if the freeze does not validate, if the run's
record or gate differs from what census_lib gives from the run's files with the frozen code, or if a fact this record
takes from DEVLOG.md is not there as stated."""
import datetime
import hashlib
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import devtools  # noqa: E402
import census  # noqa: E402
import census_lib as lib  # noqa: E402
import driver as dr  # noqa: E402

OUT = os.path.join(ROOT, 'run', 'out')
OW = 'https://github.com/openwave-labs/openwave'
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
DIAG = 'dev/runs/019_gate_cause'
POSTRUN = ('prelaunch_checks_2026-10-31.txt', 'environment_postrun_2026-11-01.txt', 'launch/resume_check.py',
           'launch/test_resume_check.py', 'launch/test_resume_check.out', 'launch/test_launch_wrapper.py',
           'launch/test_launch_wrapper.out', 'launch/prelaunch_checks.py', 'run/out/census_console.log',
           f'{DIAG}/diag_nd.py', f'{DIAG}/diag_nd.out', f'{DIAG}/tau_check.py', f'{DIAG}/tau_check.out',
           f'{DIAG}/tau_band.py', f'{DIAG}/tau_band.out', f'{DIAG}/pair_gap.py', f'{DIAG}/pair_gap.out', 'tools/build_record.py')
CHECKS = ('a stop in the log', "the run's record in the log", 'a `STOP.json` under `run/out/`', 'a JSON file carrying a stop',
          "a completed job's file missing or off its logged SHA-256", '`run/out/` holding files but no `RUNLOG.json`',
          "the log or a completed job's file that does not parse")
SEP = 'the zero cluster is not separated: an eigenvalue lies in (margin/3, 3 margin)'
NDG = 'n(D): an eigenvalue of D lies in its gray zone'


def stop(m):
    raise SystemExit(f'build_record: {m}')


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def J(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def fe(x):
    """An amplitude as the terms write it: 0.25, 0.354, 2.83, 22.63, 132."""
    x = float(x)
    if x == int(x):
        return str(int(x))
    return f'{x:.3f}'.rstrip('0') if x < 1 else f'{x:.2f}'


def sci(x, d=2):
    m, e = f'{x:.{d - 1}e}'.split('e')
    return f'{m}×10{str(int(e)).translate(SUP)}'


def idx(h):
    return f"({h['nL']}, {h['nD']}, {h['K']}), {h['ki']}"


WORDS = 'no one two three four five six seven eight nine ten eleven twelve'.split()


def nw(n, cap=False):
    w = WORDS[n] if 0 <= n < len(WORDS) else str(n)
    return w[0].upper() + w[1:] if cap else w


def sgn(d):
    return f'+{d}' if d > 0 else f'−{-d}' if d < 0 else '0'


def k1_text(mid, prev):
    """K1's failing parts at a midpoint, on both solutions, as the run's records state them, with the midpoint before."""
    recs = [mid[s]['point']['record'] for s in ('from_lower', 'from_upper')]
    if not all(mid[s]['k1'] is False for s in ('from_lower', 'from_upper')) or not all(prev[s]['k1'] for s in ('from_lower', 'from_upper')):
        stop('K1 does not fail on both solutions at the refused midpoint, after holding at the one before')

    def pair(f, d=3):
        a_, b_ = sci(recs[0][f], d), sci(recs[1][f], d)
        return f'{a_} on both solutions' if a_ == b_ else f'{a_} and {b_}'

    parts = []
    if all(SEP in r['unresolved'] for r in recs):
        if sci(recs[0]['margin'], 3) != sci(recs[1]['margin'], 3):
            stop("the two solutions' margins differ at three figures")
        parts.append(f'"{SEP}", with `outside_min` {pair("outside_min")} against `margin` {sci(recs[0]["margin"], 3)}')
    v0 = [any(u.startswith('V0 does not match its expectation') for u in r['unresolved']) for r in recs]
    if all(v0):
        parts.append(f'"V0 does not match its expectation", with a symmetry leak of {pair("leak", 2)}')
    other = [u for r in recs for u in r['unresolved'] if u != SEP and not u.startswith('V0 does not match')]
    if other or not parts or (any(v0) and not all(v0)):
        stop(f'K1 failed on parts this record does not state: {other}')
    return '; and '.join(parts) + ('' if any(v0) else '. `V₀` matches there')


def when(t):
    return datetime.datetime.fromisoformat(t.replace('Z', '+00:00'))


def entry(dev, n):
    """DEVLOG.md's entry n, from its heading to the next."""
    m = re.search(rf'^## {n}\. .*?(?=^## {n + 1}\. |\Z)', dev, re.M | re.S)
    if not m:
        stop(f'DEVLOG.md has no entry {n}')
    return m.group(0)


def fact(text, pat, what):
    m = re.search(pat, text)
    if not m:
        stop(f'DEVLOG.md does not state {what}')
    return m


def main():
    check = '--check' in sys.argv[1:]
    if [a for a in sys.argv[1:] if a != '--check']:
        stop(__doc__)

    # custody: the run's log, its files, the freeze
    log = J(os.path.join(OUT, 'RUNLOG.json'))
    if log.get('stop') or log.get('ended'):
        stop('the run log records a stop, or a job that ended a part of the run')
    files = {f: h for rec in log['completed'].values() for f, h in rec['files'].items()}
    for f, h in files.items():
        if sha(os.path.join(OUT, f)) != h:
            stop(f'run/out/{f} differs from the SHA-256 the run log recorded')
    for k in ('census', 'transcript'):
        if sha(os.path.join(OUT, log[k]['file'])) != log[k]['sha256']:
            stop(f"run/out/{log[k]['file']} differs from the SHA-256 the run log recorded")
    F = devtools.frozen(ROOT)
    if census.frozen() != F:
        stop('census.frozen() does not admit the freeze devtools.frozen() admits')
    mpin = open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8').read().strip()
    fpin = open(os.path.join(ROOT, 'run', 'FROZEN_PIN'), encoding='utf-8').read().strip()
    if not (log['manifest_sha256'] == F['manifest_sha256'] == mpin == devtools.manifest(ROOT)[1]):
        stop('the run log, the freeze and the tree do not all hold the manifest pin')
    if sha(os.path.join(ROOT, 'run', 'FROZEN.json')) != fpin:
        stop('run/FROZEN_PIN is not the SHA-256 of run/FROZEN.json')
    terms = sha(os.path.join(ROOT, 'run', 'm8_16_task_details.md'))
    if not (terms == F['terms_sha256'] == sha(os.path.join(ROOT, 'registration', 'm8_18_task_details.md'))):
        stop('the terms in run/ and registration/ differ from the SHA-256 the freeze records')
    events = log['events']
    t0, t1 = events[0]['t'], log['census']['written']
    if not (events[0]['event'].startswith('run started') and events[-1]['event'] == 'record written'
            and sum(e['event'].startswith('run started') for e in events) == 1):
        stop('the run log records more than one start, or events this record does not read')
    started = [e['event'][:-len(' started')] for e in events[1:-1] if e['event'].endswith(' started')]
    done = [e['event'][:-len(' completed')] for e in events[1:-1] if e['event'].endswith(' completed')]
    if not (len(started) + len(done) == len(events) - 2 and done == list(log['completed'])
            and started == [j for j in done if j != 'gate']):
        stop('the run log holds a job started and not completed, started twice, or an event this record does not read')
    order = re.search(r"order \[(.*)\]", events[0]['event']).group(1).replace("'", '').split(', ')
    if not (order == F['order'] == list(lib.RUN_ORDER)):
        stop(f'the run ran {order}')
    if any(j.split(':')[1] in lib.ROWS if ':' in j else j in lib.ROWS for j in done):
        stop('a target job is in the log, which a gate that did not pass forbids')
    transcript = open(os.path.join(OUT, 'census.out'), encoding='utf-8').read().splitlines()
    console = open(os.path.join(OUT, 'census_console.log'), encoding='utf-8').read().splitlines()
    total = int(re.fullmatch(r'(\d+) s', transcript[-1]).group(1))
    wall = (when(t1) - when(t0)).total_seconds()
    rss = max(v['peak_rss_bytes'] for v in log['completed'].values())

    # the facts this record takes from DEVLOG.md, each recorded there from GitHub's API when it happened
    dev = open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8').read()
    e20, e21, e24, e25, e26 = (entry(dev, n) for n in (20, 21, 24, 25, 26))
    m687 = fact(e20, r'merged at (\S+) as `([0-9a-f]{40})`', "#687's merge")
    o688 = fact(e24, r'Blake opened \[#688\]\([^)]+\) at (\S+)\.', "#688's opening")
    m688 = fact(e26, r'Merged at (\S+), as `([0-9a-f]{40})`', "#688's merge")
    if not (when(o688.group(1)) < when(t0) < when(m688.group(1))):
        stop("the run did not start between the freeze block's opening and its merge, as its body says")
    cmd = fact(e21, r'\n```\n(set -o pipefail; caffeinate .*)\n```\n', 'the launch command').group(1)
    reviewed = fact(cmd, r"printf '%s  %s\\n' ([0-9a-f]{64}) \.\./resume_check/resume_check\.py", "the check's hash").group(1)
    if sha(os.path.join(ROOT, 'launch', 'resume_check.py')) != reviewed:
        stop('launch/resume_check.py is not the reviewed check')
    if f'the run started at {t0}' not in e25 or '"Run"' not in e25:
        stop("DEVLOG.md's entry 25 does not record this launch")
    if console[:4] != ['../resume_check/resume_check.py: OK', 'run/out/ does not exist: a first launch', 'resume check: PASS',
                       'differences: none']:
        stop("the console log does not open with the hash check, the resume check's pass and --check")
    if console[4:] != transcript:
        stop('the console log, after the checks, differs from the transcript')
    pre = open(os.path.join(ROOT, POSTRUN[0]), encoding='utf-8').read()
    post = open(os.path.join(ROOT, POSTRUN[1]), encoding='utf-8').read()
    pre_ok = [l for l in pre.splitlines() if l.startswith('ok ')]
    if not (pre.rstrip().endswith('0 failed') and 'ok    record_environment.py --check: no difference' in pre
            and cmd in pre and post.rstrip().endswith('differences: none')):
        stop('the readings before and after the run are not clean, or the launch command differs from the one checked')
    E = J(os.path.join(ROOT, 'run', 'ENVIRONMENT.json'))
    envtext = (f"Python {E['interpreter']['version']}, NumPy {E['numpy']['version']} and SciPy {E['scipy']['version']}, on "
               f"Accelerate's BLAS and LAPACK as each reports them, under {E['os']['product']} {E['os']['version']} "
               f"({E['os']['build']}) on one {E['machine']['cpu']}")
    arms = open(os.path.join(ROOT, 'launch', 'test_resume_check.out'), encoding='utf-8').read()
    n_arms, n_mut = len(re.findall(r'^arm \d+,', arms, re.M)), len(re.findall(r'^mutant without', arms, re.M))
    if not (arms.endswith('0 failed\n') and n_mut == len(CHECKS)):
        stop("the resume check's arms do not pass")
    if not open(os.path.join(ROOT, 'launch', 'test_launch_wrapper.out'), encoding='utf-8').read().endswith('0 failed\n'):
        stop("the launch command's test on stubs does not pass")

    # the run's record, rebuilt from the run's files with the frozen code
    C = J(os.path.join(OUT, 'CENSUS.json'))
    g = J(os.path.join(OUT, 'GATE.json'))
    a_b = J(os.path.join(OUT, 'ARM_B.json'))
    cases = F['cases']
    res = {n: lib.load_json(os.path.join(OUT, dr.safe(n) + '.json')) for n in lib.READ_CONTROLS}
    c1 = lib.load_json(os.path.join(OUT, 'C1.json'))
    m817 = lib.m817_file('CENSUS.json', ROOT)
    located = {(lib.ARM_B_ROW, lib.key(a_b['bracket'][0]), lib.key(a_b['bracket'][1])): a_b}
    rebuilt = json.loads(json.dumps(dr.jsonable(lib.assemble(lib.classify_rows({}, m817, g['stopped'], {}), located))))
    if rebuilt != C['rows'] or C['stop'] is not None or C['left'] or C['gate'] != g:
        stop("run/out/CENSUS.json differs from census_lib on the run's files")
    for n, out in res.items():
        where = [p['eps'] for p in cases[n]['points']]
        if lib.control_failures(out, cases[n]) != g['control'][n]:
            stop(f"{n}: GATE.json's control reading differs from census_lib on the run's files")
        if lib.kernel_failures(out['cutoffs'][str(lib.TOP)], cases[n], where) != g['kernel'][n]:
            stop(f"{n}: GATE.json's kernel differs from census_lib on the run's files")
    if lib.band_failures({}, res, located, cases) or C['bands'] != {'failures': []}:
        stop('a scored reading is off the frozen band')
    if g['passed'] or not all(not v for v in g['kernel'].values()):
        stop('the gate is not the one this record states: the kernel passed, the control gate did not')
    bad = {n: v for n, v in g['control'].items() if v}
    if list(bad) != ['P5', 'C3R/R4'] or not all(len(v) == 1 for v in bad.values()):
        stop(f'the control gate failed at {bad}')
    if not (c1['checks'].get('K1') and c1['checks'].get('K4')) or lib.differences(c1['cutoffs'], lib.m8161_file('C1.json', ROOT)['cutoffs'], '/cutoffs'):
        stop("C1's check or its reproduction fails")
    rows = C['rows']
    if list(rows) != list(lib.ROWS):
        stop("the record does not hold the five rows in the terms' order")
    unread = [(n, p) for n, r in rows.items() for p in r['points'] if 'not_read' in p]
    if len(unread) != 12 or any(p['not_read'] != g['stopped'] or p['classified'] for _, p in unread):
        stop('the twelve are not all unread, with the gate named')
    tw = {n: [lib.key(e) for e in v] for n, v in lib.TWELVE.items()}
    if sorted((n, lib.key(p['eps'])) for n, p in unread) != sorted((n, k) for n, v in tw.items() for k in v):
        stop('the unread points are not the twelve')

    # Arm B
    bis = a_b['bisection']
    if not (a_b['located'] and a_b['failures'] == [] and bis['24']['interval'] == bis['32']['interval'] == a_b['union']
            and all(bis[N]['complete'] for N in ('16', '24', '32'))):
        stop("Arm B's record is not the one this record states")
    if not all(v['ok'] for v in a_b['path'].values()):
        stop("a point of Arm B's path does not reproduce")
    mv, rf, pv = {}, {}, {}
    for N in ('24', '32'):
        ms = bis[N]['midpoints']
        mv[N] = next(m for m in ms if m.get('moved'))
        rf[N] = next(m for m in ms if m['from_lower']['k1'] is False)
        pv[N] = ms[ms.index(rf[N]) - 1]
        if not (ms[-1] is mv[N] and ms[-2] is rf[N] and mv[N]['from_lower']['k1'] and mv[N]['from_upper']['k1']
                and mv[N]['from_lower']['nL'] == mv[N]['from_upper']['nL'] == 7):
            stop(f"N = {N}: the moved midpoint is not the bisection's last, or does not hold K1 with n(L) = 7")
    width = (a_b['union'][1] - a_b['union'][0]) / a_b['union'][0]
    if not width < lib.W_HALF:
        stop('the interval is not narrower than w/2')
    gd = [dict(g_, side=s) for s in ('lower', 'upper') for g_ in a_b['guards'][s]]
    for g_ in gd:
        q = g_['reading']['records']
        if not lib.band_ok(q['reading'], 'R5', q['points']['32']['lam']):
            stop(f"the guard at {g_['eps']:g}: its stored band is not level 18's")
    if not (len(gd) == 3 and gd[0]['reading']['type'] == 'Elliptic' and not gd[1]['reading']['classified']
            and gd[2]['reading']['type'] == 'Hyperbolic'):
        stop("the guards are not the ones this record states")
    arm_b_s = (when(next(e['t'] for e in events if e['event'] == 'arm_b completed')) - when(t0)).total_seconds()

    # the cause, from the records and the diagnostic beside them
    P = res['P5']
    pair = {}
    for N in ('24', '32', '40'):
        q = P['cutoffs'][N]['points']['0.25']
        near = [x for x in q['summary']['groups'] if abs(abs(complex(*x['c'])) - 4.02029) < 1.5e-5]
        pair[N] = (sorted(complex(*x['c']).imag for x in near), [x['size'] for x in near], q['record'])
    U = 2.220446049250313e-16
    tau = {N: max(pair[N][2]['margin'], 10 * math.sqrt(U * pair[N][2]['normA'] * 4.02029)) for N in pair}
    gap = pair['32'][0][1] - pair['32'][0][0]
    if not (pair['40'][1] == [2] and pair['32'][1] == [1, 1] == pair['24'][1] and tau['32'] < gap < tau['40'] and tau['24'] < gap):
        stop("P5's pair is not the one this record states")
    miss = [x for x in P['readings']['0.25']['rows'] if not x.get('ok')]
    if len(miss) != 1 or miss[0]['why'] != 'non-contracting above the floor':
        stop("P5's failing row is not the one this record states")
    means = [sum(pair[N][0]) / 2 if pair[N][1] == [1, 1] else pair[N][0][0] for N in ('24', '32', '40')]
    dn = open(os.path.join(ROOT, DIAG, 'diag_nd.out'), encoding='utf-8').read()
    ev = {N: float(re.search(rf"C3R/R4 N {N} eps 0\.25: \d+ s; \|\|B\|\| [\d.]+; D's eigenvalues \[(-[\d.e-]+)", dn).group(1)) for N in ('24', '32', '40')}
    nb = {N: float(re.search(rf"C3R/R4 N {N} eps 0\.25: \d+ s; \|\|B\|\| ([\d.]+);", dn).group(1)) for N in ('24', '32', '40')}
    if not (ev['24'] == ev['32'] == ev['40'] and dn.count("'unresolved': True") == 6 and 'False' not in dn):
        stop("the diagnostic's six reads do not reproduce the stored records, or D's eigenvalue moved")
    top = {N: 1e-5 * nb[N] for N in nb}
    zeros = re.search(r"C3R/R4 N 40 eps 0\.25: .*?sorted: \[(.*?)\]", dn, re.S).group(1).split()[:4]
    if not all(float(x) < 1e-17 for x in zeros):
        stop("D's zero eigenvalues do not read below 1e-17 of ||B|| at N = 40")
    if not (top['32'] < abs(ev['32']) and abs(ev['40']) < top['40']):
        stop("n(D)'s gray zone does not cross D's eigenvalue at N = 40 alone")
    q = res['C3R/R4']['cutoffs']['40']['points']['0.25']['record']
    if q['unresolved'] != [NDG] or (q['type'], q['nL'], q['nD'], q['K']) != ('Hyperbolic', 5, 1, 4):
        stop("C3R/R4's N = 40 record is not the one this record states")
    q = pair['40'][2]
    if q['unresolved'] or (q['type'], q['nL'], q['nD'], q['K']) != ('Hyperbolic', 5, 1, 4):
        stop("P5's N = 40 record is not the one this record states")
    pg = open(os.path.join(ROOT, DIAG, 'pair_gap.out'), encoding='utf-8').read()
    gaps = re.findall(r"^N (\d+): .*?gap ([\d.e-]+); tau ([\d.e-]+); one group: (True|False)$", pg, re.M)
    moves = re.findall(r"^from N \d+ to \d+: the lower moves ([\d.e-]+), the upper ([\d.e-]+)$", pg, re.M)
    if not ([g[0] for g in gaps] == ['24', '32', '40'] and len({g[1] for g in gaps}) == 1 and float(gaps[0][1]) == round(gap, 9)
            and [g[3] for g in gaps] == ['False', 'False', 'True'] and len(moves) == 2 and pg.count("'unresolved': True") == 3
            and max(float(x) for x in moves[1]) < 1e-13
            and 'False}' not in pg and 'False,' not in pg):
        stop("the diagnostic's read of P5's pair is not the one this record states: three reads reproducing the stored records, "
             "the gap the same at all three cutoffs, and one group at N = 40 alone")
    tb = open(os.path.join(ROOT, DIAG, 'tau_band.out'), encoding='utf-8').read()
    hits = [int(x) for x in re.findall(r': (\d+) hits', tb)]
    if len(hits) != 24 or sum(hits) != 1:
        stop('the only pair linked at N = 40 alone inside the band is not P5\'s')

    # ---- the text ---------------------------------------------------------------------------------------------
    T = []
    a = T.append
    a('# M8.18 run record')
    a('')
    a(f"The record of M8.18's registered run, the census's two remedies, from {t0} to {t1}. It ran under the governing terms, "
      f"`run/m8_16_task_details.md` (SHA-256 `{terms[:16]}…`), merged in OpenWave [#687]({OW}/pull/687) as "
      f"`{m687.group(2)[:8]}`, and the code frozen at MIT `4bd8bbd` with its manifest pin, `{mpin[:16]}…`. The maintainer's go "
      f"is [#687's comment]({F['go']}), and the freeze block is OpenWave's `research/m8_18/freeze_block.md`, merged in "
      f"[#688]({OW}/pull/688). Every number below is read from the run's files in [`run/out/`](run/out/), and "
      f"`tools/build_record.py` builds this record from them, except § 4, which also reads a diagnostic made after the run. "
      f"`run/out/ARM_B.json` holds the bracket's recomputed path, bisections and guard readings; `run/out/GATE.json` holds the "
      f"kernel and the control gate; the case files hold each control's readings at each cutoff; `run/out/CENSUS.json` holds "
      f"Arm B's outcome, the gate and every row. This record gives what the terms' § DEFINITION OF DONE asks: the kernel check "
      f"and each control's reading on the ladder; each of the twelve with its cause; every bracket, with its location or the "
      f"condition it failed; each of the five rows' standing; and each stop. Adjudication is the maintainers'.")
    a('')
    a(f"**The outcome.** The run completed in one launch, with no stop and no job left unfinished. **Arm B located T4/R5's change "
      f"of type:** with the moved midpoint at {mv['24']['eps']:.6f}, `N = 24` and 32 both complete on "
      f"[{a_b['union'][0]:.6f}, {a_b['union'][1]:.6f}], `n(L)` changing by {sgn(a_b['delta']['24'])}, between the guard readings, "
      f"Elliptic at {a_b['span'][0]:.6f} and Hyperbolic at {a_b['span'][1]:.6f}. T4/R5's row now ends Each change of type located. "
      f"**Arm A ended at the control gate.** The kernel at `N = 40` passed on all seven controls, and 22 of the 24 control points "
      f"read converged, but P5 and C3R/R4 at `ε = 0.25` read Unresolved. So none of Arm A's targets was solved or read, at any "
      f"cutoff, and the twelve stay unclassified, each keeping M8.17's cause. T1/R4, T4/R4, T1/R5 and T5/R2 end not settled by this "
      f"run, with " + ', '.join(str(len(rows[n]['open'])) for n in ('T1/R4', 'T4/R4', 'T1/R5')) + f" and {len(rows['T5/R2']['open'])} items open.")
    a('')
    a('**The rows:**')
    a('')
    a('| Row | Slot | Outcome | Meets an S4 completion condition | Classified | Not classified | Of those, the twelve |')
    a('|---|---|---|---|---|---|---|')
    for n, r in rows.items():
        cls = sum(p['classified'] for p in r['points'])
        a(f"| {n} | `{lib.SLOT[n]}` | {r['outcome']} | {'yes' if r['meets_s4'] else 'no'} | {cls} of {len(r['points'])} | "
          f"{len(r['points']) - cls} | {sum('not_read' in p for p in r['points'])} |")
    a('')

    # 1. custody
    a('## 1. Custody')
    a('')
    a(f"- **The freeze.** `run/FROZEN.json` was written once, at {F['written']}, by `run/write_guard.py`, after the go. It holds "
      f"the allowlist and the order, the twelve cases of `census_lib.RUN_ORDER`; each case with its registered path; the census "
      f"values; what M8.18 inherits from M8.16.1; the terms' and the manifest's SHA-256; the go; and {len(F['targets'])} targets, "
      f"every reference file at its SHA-256 with `reference/SOURCES.json` among them. Its own SHA-256 is `run/FROZEN_PIN`, "
      f"`{fpin[:16]}…`.")
    a(f"- **The freeze block,** built by the pinned `run/freeze_block.py`, carries `FROZEN.json` in full. Its pull request, "
      f"[#688]({OW}/pull/688), was opened at {o688.group(1)}, before the run started, and merged at {m688.group(1)} as "
      f"`{m688.group(2)[:8]}`, after it started, as its body says it may. The maintainer's approval rebuilt the block byte for "
      f"byte from MIT's git objects with its own script, and records that the adjudication reads `resume_check.py` in full and "
      f"reads the run's log against the go, the written time and the pull request's opening. All three are below.")
    a(f"- **Before the launch,** read-only, by `launch/prelaunch_checks.py` with #688's number, at the bench beside this "
      f"folder: {len(pre_ok)} checks, all clean, its output kept as `{POSTRUN[0]}`. Among them: both admissions, "
      f"`devtools.frozen()` and `census.frozen()`; the manifest and the freeze pin; `run/record_environment.py --check`, with no "
      f"difference from `run/ENVIRONMENT.json`; no `run/out/`, so no solve had run at `N = 40`; no census run in progress; no "
      f"file newer than the freeze pin but `DEVLOG.md`; the resume check at its reviewed SHA-256, and passing; mains power; and "
      f"#688 open, its one file the block, equal at its head, with DCO passing.")
    a(f"- **The launch.** One launch, on the author's word, by the command `DEVLOG.md` entry 21 records, run unchanged from this "
      f"folder as a background task, under `caffeinate` on its shell, on mains power:")
    a('')
    a('  ```')
    a(f'  {cmd}')
    a('  ```')
    a('')
    a(f"  It checks the resume check's bytes against `{reviewed[:16]}…`, runs the check, runs `--check`, and only then "
      f"`run/census.py`. Its console log, `run/out/census_console.log`, opens with the hash check's `OK`, the check's `PASS` with "
      f"`run/out/` not yet existing, and `differences: none`, and then holds the run's transcript, `run/out/census.out`, line for "
      f"line. The resume check sat outside the pinned tree, at `../resume_check/`, as the freeze block's pull request states; "
      f"`launch/resume_check.py` is that file, byte for byte, published with its {n_arms} arms, `launch/test_resume_check.py`, and "
      f"their output. It refuses on {nw(len(CHECKS))} checks: " + '; '.join(CHECKS) + '.')
    a(f"- **The run.** It started at {t0} and wrote its record at {t1}, {wall:.0f} s later, against {total} s by its own clock, "
      f"after the go, the freeze's written time and #688's opening, in the recorded environment: {envtext}. Its log, "
      f"`run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, equal to `run/MANIFEST_PIN`; one start, and so no "
      f"resume; each of {len(log['completed'])} jobs, each started once and completed, with its files' SHA-256, its time and the "
      f"process's peak resident size, at most {rss:,} bytes; no stop and no job ended; and the record and the transcript, each "
      f"with its SHA-256.")
    a(f"- **After the run:** every output equals the SHA-256 the log recorded; both admissions pass; the tree still equals the "
      f"manifest pin; and the environment, read again, equals `run/ENVIRONMENT.json` (`{POSTRUN[1]}`). The resume check then "
      f"refuses a relaunch, since the run has completed.")
    a('- **Post-run files.** These files were made or placed after the run, and are not records from it:')
    a(f"  - `{POSTRUN[0]}`, the checks before the launch, read just before it;")
    a(f"  - `{POSTRUN[1]}`, `run/record_environment.py --check`, read after the run, with no difference;")
    a("  - `launch/`, each file byte for byte as it ran from the bench beside this folder: the resume check and its arms; "
      "`prelaunch_checks.py`; and `test_launch_wrapper.py` with its output, the launch command's form run on stubs;")
    a("  - `run/out/census_console.log`, the run's console output, copied byte for byte from beside this folder once the run "
      "had ended;")
    a(f"  - `{DIAG}/`, the diagnostic § 4 reads, made after the run on a copy of this folder;")
    a("  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference;")
    a("  - `SHA256SUMS`, regenerated over the published folder at the record's commit, one line per file but itself. The "
      "pre-run inventory stays at MIT `4bd8bbd`.")
    a('')
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for f in list(files) + [log['census']['file'], log['transcript']['file'], 'RUNLOG.json']:
        a(f'  | `run/out/{f}` | `{sha(os.path.join(OUT, f))}` |')
    a(f"  | `run/FROZEN.json` | `{fpin}` |")
    a('')
    a('  The post-run files:')
    a('')
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for f in POSTRUN:
        a(f"  | `{f}` | `{sha(os.path.join(ROOT, f))}`{', as it built this record' if f == 'tools/build_record.py' else ''} |")
    a('')

    # 2. Arm B
    ends = a_b['ends']
    lo_k, hi_k = lib.key(a_b['bracket'][0]), lib.key(a_b['bracket'][1])
    rl, rh = ends[lo_k]['points']['32']['record'], ends[hi_k]['points']['32']['record']
    a('## 2. Arm B: the revised locator on T4/R5')
    a('')
    a(f"Arm B ran first, and its record was written {arm_b_s:.0f} s after the start, before any solve at `N = 40`.")
    a('')
    a(f"- **The bracket** is T4/R5's ({fe(a_b['bracket'][0])}, {fe(a_b['bracket'][1])}): {rl['type']}, {idx(rl)}, and {rh['type']}, "
      f"{idx(rh)}, at every cutoff, an {a_b['kind']} bracket. The signed change `Δn(L)` is {sgn(a_b['delta']['24'])} at `N = 24`, "
      f"{sgn(a_b['delta']['32'])} at 32, and {sgn(a_b['delta']['16'])} at 16, which is reported and does not decide.")
    a(f"- **The path.** Each cutoff's path was recomputed from its seed to the bracket's upper end, {len(a_b['path'])} points, every "
      f"one equal to its record in M8.17's outputs, timings aside.")
    a("- **M8.17's midpoints.** Each of them, at each cutoff, equals its stored record, timings aside. The run compares them as it "
      "goes, and a difference stops it; it did not stop.")
    a('- **The bisections:**')
    for N in ('16', '24', '32'):
        b = bis[N]
        iv = b['interval']
        a(f"  - `N = {N}`: {len(b['midpoints'])} midpoints, the interval [{iv[0]:.6f}, {iv[1]:.6f}], "
          f"{sci((iv[1] - iv[0]) / iv[0])} of its lower end, complete."
          + (' It is reported, and does not decide.' if N == '16' else ''))
    interp = '1.16×10⁻⁵ and 1.26×10⁻⁵'
    if interp not in open(os.path.join(ROOT, 'run', 'm8_16_task_details.md'), encoding='utf-8').read():
        stop("the terms do not state the moved point's interpolation")
    a('- **The moved midpoint.** At each deciding cutoff, K1 refused M8.17\'s last midpoint on both of its solutions, and that '
      'midpoint stays in the record and decides nothing. One move, to the point 0.4 of the current interval above its lower end, '
      f'as the terms fix it. The terms\' interpolation (INFERRED) put the nearest eigenvalue there at about {interp}, and the run '
      'reads:')
    for N in ('24', '32'):
        r_, m_, p_ = rf[N], mv[N], pv[N]
        rr = m_['from_lower']['point']['record']
        a(f"  - `N = {N}`: K1 fails at `ε = {r_['eps']:.6f}`: {k1_text(r_, p_)}. At the moved point, `ε = {m_['eps']:.6f}`, K1 holds "
          f"on both solutions, with `outside_min` {sci(rr['outside_min'], 3)} against `margin` {sci(rr['margin'], 3)}; `n(L)` reads "
          f"{m_['from_lower']['nL']} on both, and the two solutions lie {sci(m_['distance'], 3)} apart. The midpoint before the "
          f"refused one, `ε = {p_['eps']:.6f}`, held K1 with `outside_min` "
          f"{sci(min(p_[s]['point']['record']['outside_min'] for s in ('from_lower', 'from_upper')), 3)}.")
    a(f"- **The location.** The interval at `N = 24` and 32 is [{a_b['union'][0]:.6f}, {a_b['union'][1]:.6f}], {sci(width)} of its "
      f"lower end, narrower than the `w/2` that completes a bisection, and the union is that same interval, narrower than "
      f"`w = 10⁻³`. The `n(L)` change at `N = 16` lies above both, as M8.17's record has it.")
    a('- **The guards.** Each is read at all three cutoffs at one `ε`, classified by the rule, and solved from its end of the '
      'bracket. The stored band is the one the reading used; Arm B\'s guards are outside the run\'s own band test, so this table '
      'gives each one against `R5`\'s frozen level, 18, for the third note of #687\'s approval:')
    a('')
    a('  | Side | `δ` | `ε` | `n(L)` at 16, 24, 32 | Type at 16, 24, 32 | The rule | Branch identity, 24 to 32 | Stored band | Level 18 at `λ` |')
    a('  |---|---|---|---|---|---|---|---|---|')
    for g_ in gd:
        q = g_['reading']['records']
        pts = q['points']
        lam = pts['32']['lam']
        a(f"  | {g_['side']} | {g_['delta']} | {g_['eps']:.6f} | {', '.join(str(pts[N]['record']['nL']) for N in ('16', '24', '32'))} | "
          f"{', '.join(pts[N]['record']['type'] for N in ('16', '24', '32'))} | "
          f"{'converged: ' + g_['reading']['type'] if g_['reading']['classified'] else 'Unresolved'} | "
          f"{'kept' if q['identity']['24-32']['kept'] else 'fails'}, {sci(q['identity']['24-32']['aligned_distance'], 3)} | "
          f"{q['reading']['band']:.9f} | {lib.band_value('R5', lam):.9f} |")
    a('')
    a(f"  The upper guard at `δ = 0.01` lies below `N = 16`'s change, so `N = 16` reads `n(L) = 7` there against 6 at `N = 24` and "
      f"32, and the rule's structure condition leaves it Unresolved, as § The guards inferred: "
      f"\"{'; '.join(gd[1]['reading']['causes'])}\". The retry at `δ = 0.05` lies above it, and counts.")
    a(f"- **What is located.** The run names it: \"{a_b['why'].replace('`', '')}\". Its resolution is an `n(L)` interval and two "
      f"guard readings, not a crossing point. Its identification with the genuine index crossing is not claimed, and Corollary I "
      f"is not applied.")
    a('')

    # 3. Arm A's gates
    a("## 3. Arm A's gates")
    a('')
    a("- **The paths at `N = 24` and 32.** Each of the six controls' paths was solved and read at each registered point, and "
      "reproduced M8.16.1's record, with branch identity between them. The run compares them as it goes, and a difference stops "
      "it; it did not stop.")
    a(f"- **The kernel at `N = 40` passed** on all seven controls, against K1 as M8.16.1's terms freeze it, with its calibration "
      f"constants unchanged. C1, at its four cutoffs, passes `checks.check_c1`, and its record, `N = 40` included, equals "
      f"M8.16.1's: the first `N = 40` reproduced on this OS.")
    a('')
    a('| Control | Slot | Seed | Points accepted at `N = 40` | K1 at `N = 40` | Path at `N = 40`, s |')
    a('|---|---|---|---|---|---|')
    for n, out in res.items():
        rc = out['cutoffs']['40']
        acc = sum(bool(rc['points'][lib.key(p['eps'])].get('accepted')) for p in cases[n]['points'])
        k1s = sum(bool(lib.ck.k1(rc['points'][lib.key(p['eps'])], cases[n])) for p in cases[n]['points'])
        path = J(os.path.join(OUT, f'{dr.safe(n)}_N40.json'))
        a(f"| {n} | `{cases[n]['slot']}` | {'ok' if rc['seed']['ok'] else 'fails'} | {acc} of {len(cases[n]['points'])} | "
          f"holds at {k1s} of {len(cases[n]['points'])} | {path['setup_seconds']:.0f} |")
    a('')
    a("- **The control gate did not pass.** Each control but C1 was read on `N = 24`, 32 and 40 at its registered points, on the "
      "band above `N = 16`. Each point must read converged with the type and indices on its record, and branch identity must hold "
      "on both pairs. All six were read and recorded before the gate decided. Branch identity held on both pairs at all 24 points. "
      "The reading beside the rule, on the band above `N = 24`, is unscored.")
    a('')
    a('| Control | `ε` | The rule | Type; `(n(L), n(D), K)`, `k_i⁻` at `N = 40` | On record | Aligned distance, 24 to 32 | 32 to 40 | Beside, unscored | Gate |')
    a('|---|---|---|---|---|---|---|---|---|')
    for n, out in res.items():
        for p in cases[n]['points']:
            k = lib.key(p['eps'])
            rd, rc, i_, be = out['readings'][k], out['cutoffs']['40']['points'][k]['record'], out['identity'][k], out['beside'][k]
            ok = lib.ck.converged(out, p['eps'], cases[n])
            a(f"| {n} | {fe(p['eps'])} | {rd['verdict']} | {rc['type']}; {idx(rc)} | {cases[n]['type']}; "
              f"({', '.join(str(x) for x in cases[n]['idx'])}) | {sci(i_['24-32']['aligned_distance'], 3)} | "
              f"{sci(i_['32-40']['aligned_distance'], 3)} | {be['verdict']} | {'passes' if ok else '**fails**'} |")
    a('')
    a('The two failures, as `run/out/GATE.json` states them:')
    a('')
    for n, v in bad.items():
        a(f'- **{n}:** "{v[0]}".')
    rc = res['C3R/R4']['cutoffs']['40']['points']['0.25']['record']
    a('')
    a(f"C3R/R4's record at `N = 40` carries \"{rc['unresolved'][0]}\"; its records at `N = 24` and 32 carry nothing. The record of "
      f"the gate names P5, the first failure: \"{g['stopped']}\".")
    a('')
    a("**What followed, as the terms state:** \"A failure inside Arm A's gates ends Arm A. The twelve stay unclassified, and the "
      "record is written.\" No other level was tried, and the run went on to its record. The log holds no job of any target, at any "
      "cutoff.")
    a('')
    bes = [f"{n} at {fe(k)}" for n in res for k, be in res[n]['beside'].items() if be['verdict'] != 'converged']
    a(f"**The reading beside the rule** reads {', '.join(bes[:-1])} and {bes[-1]} Unresolved. It decides nothing here.")
    a('')

    # 4. the cause
    a('## 4. Why the gate failed: a diagnostic made after the run')
    a('')
    a(f"This section is not a record from the run. It rests on the stored records and on `{DIAG}/`, a diagnostic made after the "
      f"run on a copy of this folder. It scores nothing, changes no record, and moves no verdict: the gate stands as § 3 states it. "
      f"On the recorded machine, the diagnostic's reads of stored solutions, six in `diag_nd.py` and three in `pair_gap.py`, "
      f"reproduce the stored `type`, `nL`, `nD`, `K`, `margin`, `unresolved` and `normA`. The cause the census applies is the one "
      f"the adjudication names.")
    a('')
    a('In both cases a tolerance that grows with the cutoff reaches a value that does not move (DERIVED from the records and '
      'those reads).')
    a('')
    a(f"- **P5 at `ε = 0.25`.** Two Krein-positive eigenvalues near 4.0203 lie {sci(gap, 5)} apart at all three cutoffs, read before "
      f"they are linked. "
      f"`linear.record` links eigenvalues within `τ(λ) = max(margin, 10 sqrt(u ‖A‖ |λ|))`, and ‖A‖ grows with the cutoff: "
      f"{pair['24'][2]['normA']:,.0f}, {pair['32'][2]['normA']:,.0f} and {pair['40'][2]['normA']:,.0f}. So `τ` is {sci(tau['24'], 4)}, "
      f"{sci(tau['32'], 4)} and {sci(tau['40'], 4)}, and it passes the gap at `N = 40` alone, by "
      f"{100 * (tau['40'] / gap - 1):.1f}%. There the pair is stored as one group of size 2 at its mean. The rule then compares that "
      f"one centre with the two below it, and the set's change from `N = 32` is half the gap, {sci(miss[0]['d2'], 4)}, against "
      f"{sci(miss[0]['d1'], 4)} from 24 to 32 and the floor {sci(miss[0]['floor'], 4)}: \"non-contracting above the floor\". The "
      f"pair's mean is {means[0]:.12f}, {means[1]:.12f} and {means[2]:.12f}, changing by {sci(abs(means[2] - means[1]), 1)} from 32 "
      f"to 40, and its members, read before they are linked, move by less than 10⁻¹³, the size of rounding. "
      f"Across all 24 control points, it is the only pair inside the tested band that `τ` links at `N = 40` alone.")
    a(f"- **C3R/R4 at `ε = 0.25`.** D's negative eigenvalue is {ev['40']} at all three cutoffs, to the seven digits printed. "
      f"`n(D)`'s gray zone is read against ‖B‖, {nb['24']:,.3f}, {nb['32']:,.3f} and {nb['40']:,.3f}, and its top, `10⁻⁵ ‖B‖`, is "
      f"{top['24']:.5f}, {top['32']:.5f} and {top['40']:.5f}. It passes {abs(ev['40'])} at `N = 40` alone, by "
      f"{100 * (top['40'] / abs(ev['40']) - 1):.1f}%. D's zero eigenvalues read below 10⁻¹⁷ of ‖B‖ there.")
    a("- **At both points** the `N = 40` record reads Hyperbolic with (5, 1, 4), the recorded type and indices, and both failures "
      "are at the controls' smallest amplitude. The gate asks for a converged reading, and it was applied as the terms state.")
    a("- **What could have seen it.** Neither crossing needed a sealed reading: the pair's gap is in the stored `N = 32` record, D's "
      "eigenvalue can be read at `N = 24`, and ‖A‖ and ‖B‖ at `N = 40` follow from the top level, about `N(N + 2) - λ`. No check of "
      "the frozen tolerances at `N = 40`'s norms was run before the filing.")
    a('')

    # 5. the twelve
    a('## 5. The twelve')
    a('')
    a("None of the twelve was solved or read at any cutoff. Each is not classified, and each keeps M8.17's cause as M8.17 recorded "
      "it, with the gate named beside it in `run/out/CENSUS.json`. As the terms state, \"that is not a second outcome with that "
      "cause\". No band read them, so the two readings § DEFINITION OF DONE asks for, and the Krein-negative distance, do not "
      "apply. No type is claimed.")
    a('')
    for n, p in unread:
        c = [x for x in p['causes'] if not x.startswith('M8.15 holds no record')]
        a(f"- **{n}, `ε = {fe(p['eps'])}`:** " + '; '.join(c) + '.')
    a('')

    # 6. the brackets
    a('## 6. The brackets')
    a('')
    for n, r in rows.items():
        for ch in r['changes']:
            lo, hi = fe(ch['lo']), fe(ch['hi'])
            if ch['kind'] == 'across':
                a(f"- **{n}, ({lo}, {hi}),** {ch['lo_type']} to {ch['hi_type']}, across the unclassified grid point"
                  f"{'s' if len(ch['between']) > 1 else ''} {', '.join(fe(e) for e in ch['between'])}: no type bracket, and not "
                  f"located. The point was not read, so no new bracket exists and the locator did not run.")
            else:
                a(f"- **{n}, ({lo}, {hi}),** {ch['lo_type']} to {ch['hi_type']}: located, § 2.")
    a('')

    # 7. the row outcomes
    a('## 7. The row outcomes')
    a('')
    a("Each row's run outcome under § THE ROW OUTCOMES, and, separately, whether it meets an S4 completion condition. M8.17's "
      "outcomes stand as adjudicated, and these state where each row stands after this run.")
    a('')
    a("| Row | M8.17's outcome | This run's | Meets an S4 completion condition | Open |")
    a('|---|---|---|---|---|')
    for n, r in rows.items():
        op = [fe(o['point']) for o in r['open'] if 'point' in o] + [f"({fe(o['change'][0])}, {fe(o['change'][1])})" for o in r['open'] if 'change' in o]
        a(f"| {n} | {m817['rows'][n]['outcome']} | {r['outcome']} | {'yes' if r['meets_s4'] else 'no'} | {', '.join(op) or 'none'} |")
    a('')
    a("This record does not apply S6: the census page applies it to each item after the adjudication, with the cause the "
      "adjudication names. Four statements bear on that step, and this record only reports them:")
    a("- the sentence quoted in § 5 keeps the gate's stop from being a second outcome with M8.17's causes, which is S6's first "
      "sentence;")
    a("- S6's last sentence closes as instrument-limited the rows a root cause blocks, where the maintainer admits no instrument "
      "that removes it, and the answer of 2026-10-29 leaves a point this run does not classify not offered to this instrument "
      "again;")
    a("- that answer applies S6 to T5's row when its point at 45.25 has been read again, and this run did not read it;")
    a("- the twelve, and T4/R4's change across 4, are in neither case the census page's note of 2026-10-30 names: a remedy was "
      "admitted for them and ran, and its gate stopped before it read them. The request of 2026-10-29 asked: \"if only one remedy is "
      "admitted, or an admitted remedy ends without resolving its obstruction, may the remaining items close the same way, or does "
      "each cause need its own ruling?\", and read the ruling of 2026-10-20 as covering these cases, \"through S6's first sentence "
      "where a remedy meets the same cause again\". The answer reads \"Yes, your reading of S6 holds\", and names two cases: no "
      "remedy admitted for an item, and a remedy that meets the same cause again.")
    a('')

    # 8. what is new
    a('## 8. What is new')
    a('')
    n40 = sum(len(cases[n]['points']) for n in res)
    a("The new evidence the terms name (§ Known outcomes, and what is new), as it fell:")
    a(f"- **At `N = 40`:** the {n40} readings on the six controls, and the kernel on all seven. C1's `N = 40` record is M8.16.1's, "
      f"reproduced. None of the twelve.")
    a(f"- **T4/R5's moved midpoint,** at `N = 24` and 32, each solved from both ends.")
    a(f"- **The guard readings:** {len(gd)}, each at three cutoffs.")
    a("- **A new bracket's midpoints, and the new record at a bracket's end outside the twelve:** none, since no target was read.")
    a('')

    # 9 to 11
    a('## 9. Deviations')
    a('')
    a("- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above, once, with no "
      "resume and no stop. It started after #688's opening and before its merge, as #688's body says.")
    a('')
    a('## 10. Corrections and reading notes')
    a('')
    a("- **No correction.**")
    a(f"- **#687's approval, its four notes.** The first: `--check` read before the launch, by the launch itself and after the run, "
      f"with no difference (§ 1). The second, a global stop: none happened. The third, the stored band of Arm B's guards: § 2. The "
      f"fourth, closure per item: read here only, in § 7.")
    a(f"- **#688's approval, its two notes.** The first: the environment record already carries macOS 15.8.2, so the comparison "
      f"that tests the OS move is the run's own, with M8.16.1's and M8.17's records, and it found no difference. The second: "
      f"`launch/resume_check.py` is published at the SHA-256 that approval pins, with its arms.")
    a('')
    a('## 11. Follow-ups, outside M8.18')
    a('')
    a("- **The catalog.** After the adjudication, the census page's dated note gives each row's ending and catalog status, with S6 "
      "applied per item, and S5's obligation stated as open (the terms, § DEFINITION OF DONE).")
    a("- **T5's row, the twelve and T4/R4's change across 4.** The third and fourth statements in § 7 are questions for the "
      "adjudication.")
    a("- **The location's identification.** T4/R5's location is an `n(L)` interval with two guard readings, not a crossing point; "
      "its identification with the genuine index crossing is not established (the terms, § ARM B).")
    a("- **The twelve.** The terms do not offer them to this instrument again. Anything MIT computes at these points after this run "
      "is outside this registration and is not part of this record.")
    a('')

    # 12. reproduction
    a('## 12. Reproduction')
    a('')
    a('`REPRODUCE.md` gives every command. For the run, from a copy of this folder:')
    a('- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and `python3 -I -B run/record_environment.py --check`;')
    a('- **the registered run:** the launch command above, from a copy without `run/out/`, beside a copy of `launch/` at '
      '`../resume_check/`. In a copy that keeps this `run/out/`, the resume check refuses, since the run has completed;')
    a("- `python3 -I -B tools/build_record.py --check`, which rebuilds this record from the files, recomputes the gate and every "
      "row with `census_lib`, and reports any difference.")
    a('')
    a('Bitwise agreement on another machine is not claimed: the reproduction rules compare bit for bit on the recorded '
      'environment, which the readings before and after the run equal.')

    text = '\n'.join(T) + '\n'
    if '—' in text or '–' in text:
        stop('the record holds a long dash')
    if re.search(r'/Users/|/private/tmp|Desktop/', text):
        stop('the record holds a local path')
    path = os.path.join(ROOT, 'RECORD.md')
    if check:
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else None
        if old != text:
            print('RECORD.md differs from the build')
            sys.exit(1)
        print(f'RECORD.md reproduces: {len(text.split())} words')
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'RECORD.md written: {len(text.split())} words')


if __name__ == '__main__':
    main()
