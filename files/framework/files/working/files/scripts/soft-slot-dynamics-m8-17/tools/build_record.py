#!/usr/bin/env python3
"""Post-run: made after M8.17's registered run. It builds RECORD.md from the run's files, so that every number and
hash in the record is read from the bytes it names. It follows M8.16.1's tools/build_record.py, carried to the census
run: the reproduction gate, every point's classification, the brackets and the row outcomes.

Usage, from this folder: python3 -I -B tools/build_record.py [--check]
  --check:  build the record and compare it with RECORD.md, without writing; exit 1 on any difference.

It refuses if an output differs from the SHA-256 the run's log recorded, if the freeze does not validate, if the
run's record differs from what census_lib.assemble gives from the run's files with the frozen code, or if a fact this
record takes from DEVLOG.md is not there as stated."""
import datetime
import hashlib
import json
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
POSTRUN = ('prelaunch_checks_2026-10-27.txt', 'environment_postrun_2026-10-28.txt', 'launch/resume_check.py',
           'launch/test_resume_check.py', 'launch/test_resume_check.out', 'launch/test_launch_wrapper.py',
           'launch/test_launch_wrapper.out', 'launch/prelaunch_checks.py',
           'run/out/census_console.log', 'tools/build_record.py')
CHECKS = ('a stop in the log', "the run's record in the log", 'a `STOP.json` under `run/out/`', 'a JSON file carrying a stop',
          'a failed reproduction gate', "a completed job's file missing or off its logged SHA-256",
          '`run/out/` holding files but no `RUNLOG.json`', "the log or a completed job's file that does not parse")


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


WORDS = 'no one two three four five six seven eight nine ten'.split()


def nw(n, cap=False):
    w = WORDS[n] if 0 <= n < len(WORDS) else str(n)
    return w[0].upper() + w[1:] if cap else w


def sgn(d):
    return f'+{d}' if d > 0 else f'\u2212{-d}' if d < 0 else '0'


SEP = 'the zero cluster is not separated: an eigenvalue lies in (margin/3, 3 margin)'


def k1_parts(mids):
    """K1's failing parts at a bisection's last midpoint, on both solutions, as the run's records state them, with the
    midpoint before."""
    last, prev = mids[-1], mids[-2]
    recs = [last[s]['point']['record'] for s in ('from_lower', 'from_upper')]
    if not all(last[s]['k1'] is False for s in ('from_lower', 'from_upper')) or not all(prev[s]['k1'] for s in ('from_lower', 'from_upper')):
        stop('K1 does not fail on both solutions at the last midpoint, after holding at the one before')

    def pair(f, d=3):
        a_, b_ = sci(recs[0][f], d), sci(recs[1][f], d)
        return f'{a_} on both solutions' if a_ == b_ else f'{a_} and {b_}'

    parts, known = [], {SEP}
    if all(SEP in r['unresolved'] for r in recs):
        if sci(recs[0]['margin'], 3) != sci(recs[1]['margin'], 3):
            stop('the two solutions\' margins differ at three figures')
        parts.append(f'"{SEP}", with `outside_min` {pair("outside_min")} against `margin` {sci(recs[0]["margin"], 3)}')
    v0 = [any(u.startswith('V0 does not match its expectation') for u in r['unresolved']) for r in recs]
    if all(v0):
        parts.append(f'"V0 does not match its expectation", with a symmetry leak of {pair("leak", 2)}')
    other = [u for r in recs for u in r['unresolved'] if u not in known and not u.startswith('V0 does not match')]
    if other or not parts or (any(v0) and not all(v0)):
        stop(f'K1 failed on parts this record does not state: {other}')
    prev_out = sci(min(prev[s]['point']['record']['outside_min'] for s in ('from_lower', 'from_upper')), 3)
    return (f" It stopped at the midpoint `ε = {last['eps']:.6f}`, where K1 fails on both of its solutions, from the lower end "
            f"and from the upper end, as the run's record states it: " + '; and '.join(parts)
            + ('' if any(v0) else '. `V₀` matches there')
            + f". At the midpoint before, `ε = {prev['eps']:.6f}`, K1 held, with `outside_min` {prev_out}.")


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
    if log.get('stop'):
        stop('the run log records a stop')
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
    if not (terms == F['terms_sha256'] == sha(os.path.join(ROOT, 'registration', 'm8_17_task_details.md'))):
        stop('the terms in run/ and registration/ differ from the SHA-256 the freeze records')
    events = log['events']
    t0, t1 = events[0]['t'], log['census']['written']
    if not (len(events) == len(log['completed']) + 2 and events[0]['event'].startswith('run started')
            and [e['event'] for e in events[1:-1]] == [f'{n} completed' for n in log['completed']]
            and events[-1]['event'] == 'record and transcript written'):
        stop('the run log records more than one start, or events this record does not read')
    order = re.search(r"rows \[(.*)\]", events[0]['event']).group(1).replace("'", '').split(', ')
    rows_run = [n for n in log['completed'] if not n.startswith('locate:')]
    jobs = [n for n in log['completed'] if n.startswith('locate:')]
    if not (rows_run == order == F['order'] == list(lib.RUN_ORDER)):
        stop(f'the run ran {rows_run}')
    transcript = open(os.path.join(OUT, 'census.out'), encoding='utf-8').read().splitlines()
    console = open(os.path.join(OUT, 'census_console.log'), encoding='utf-8').read().splitlines()
    total = int(re.fullmatch(r'(\d+) s', transcript[-1]).group(1))
    wall = (when(t1) - when(t0)).total_seconds()

    # the facts this record takes from DEVLOG.md, each recorded there from GitHub's API when it happened
    dev = open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8').read()
    e19, e26, e28, e29, e30 = (entry(dev, n) for n in (19, 26, 28, 29, 30))
    m662 = fact(e19, r'merged at (\S+) as `([0-9a-f]{40})`', "#662's merge")
    o673 = fact(e28, r'Blake opened \[#673\]\([^)]+\) at (\S+),', "#673's opening")
    m673 = fact(e29, r'merged it at (\S+) as `([0-9a-f]{40})`', "#673's merge")
    if not (when(o673.group(1)) < when(m673.group(1)) < when(t0)):
        stop("the freeze block's pull request was not opened and merged before the run")
    cmd = fact(e26, r'\n```\n(set -o pipefail; caffeinate .*)\n```\n', 'the launch command').group(1)
    reviewed = fact(cmd, r"printf '%s  %s\\n' ([0-9a-f]{64}) \.\./resume_check/resume_check\.py", "the check's hash").group(1)
    if sha(os.path.join(ROOT, 'launch', 'resume_check.py')) != reviewed:
        stop('launch/resume_check.py is not the reviewed check')
    if f'the run started at {t0}' not in e30 or '"launch."' not in e30:
        stop("DEVLOG.md's entry 30 does not record this launch")
    if console[:3] != ['../resume_check/resume_check.py: OK', 'run/out/ does not exist: a first launch', 'resume check: PASS']:
        stop("the console log does not open with the hash check and the resume check's pass")
    if console[3:] != transcript:
        stop('the console log, after the checks, differs from the transcript')
    pre = open(os.path.join(ROOT, POSTRUN[0]), encoding='utf-8').read()
    post = open(os.path.join(ROOT, POSTRUN[1]), encoding='utf-8').read()
    pre_lines = [l for l in pre.splitlines() if l.startswith(('ok ', 'FAIL', 'info'))]
    if not (pre.rstrip().endswith('0 failed') and 'ok    record_environment.py --check: no difference' in pre
            and cmd in pre and post.rstrip().endswith('differences: none')):
        stop('the readings before and after the run are not clean, or the launch command differs from the one checked')
    E = J(os.path.join(ROOT, 'run', 'ENVIRONMENT.json'))
    envtext = (f"Python {E['interpreter']['version']}, NumPy {E['numpy']['version']} and SciPy {E['scipy']['version']}, on "
               f"Accelerate's BLAS and LAPACK as each reports them, under {E['os']['product']} {E['os']['version']} "
               f"({E['os']['build']}) on one {E['machine']['cpu']}")
    for f in ('test_launch_wrapper.py', 'test_launch_wrapper.out'):
        if f'`{sha(os.path.join(ROOT, "launch", f))}`' not in e26:
            stop(f'launch/{f} is not at the SHA-256 DEVLOG.md entry 26 records')
    if not open(os.path.join(ROOT, 'launch', 'test_launch_wrapper.out'), encoding='utf-8').read().endswith('0 failed\n'):
        stop("the launch command's test on stubs does not pass")
    arms = open(os.path.join(ROOT, 'launch', 'test_resume_check.out'), encoding='utf-8').read()
    n_arms, n_mut = len(re.findall(r'^arm \d+,', arms, re.M)), len(re.findall(r'^mutant without', arms, re.M))
    if not (arms.endswith('0 failed\n') and n_mut == len(CHECKS)):
        stop("the resume check's arms do not pass")

    # the run's record, rebuilt from the run's files with the frozen code
    C = J(os.path.join(OUT, 'CENSUS.json'))
    results = {n: lib.load_json(os.path.join(OUT, dr.safe(n) + '.json')) for n in rows_run}
    L = {n: lib.load_json(os.path.join(OUT, dr.safe(n) + '.json')) for n in jobs}
    extra, located = {}, {}
    for n, rec in L.items():
        for k, v in rec['ends'].items():
            extra[(rec['row'], k)] = lib.pt_from_json(v)
        located[(rec['row'], lib.key(rec['bracket'][0]), lib.key(rec['bracket'][1]))] = rec
    theirs, m815 = lib.theirs_records(), lib.m815_records()
    loc = lib.known_location(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))
    rebuilt = json.loads(json.dumps(dr.jsonable(lib.assemble(results, extra, located, theirs, m815, loc))))
    if rebuilt != C['rows'] or C['stop'] is not None or C['unclassified']:
        stop("run/out/CENSUS.json differs from census_lib.assemble on the run's files")
    rows = C['rows']
    if list(rows) != list(lib.ROWS):
        stop('the record does not hold the nine rows in the terms\' order')
    for n, r in rows.items():
        for p in r['points']:
            if any('disagree' in c for c in p.get('causes', [])):
                stop(f'{n} at {p["eps"]}: the instruments disagree, which this record must report')

    # the reproduction gate
    gate = {}
    for n in rows_run:
        g = results[n]['gate']
        if g['failed']:
            stop(f'{n}: the reproduction gate failed, which the run would have stopped on')
        gate[n] = {r: [p['eps'] for p in g['points'] if p['rule'] == r and p['ok']] for r in (1, 2, 3)}
        if sum(len(v) for v in gate[n].values()) != len(g['points']):
            stop(f'{n}: a gate point is not ok')
    paths = {n: (len(rec['path']), sum(not v['ok'] for v in rec['path'].values())) for n, rec in L.items()}
    if any(bad for _, bad in paths.values()):
        stop("a locator's recomputed path does not reproduce")

    # what is new
    new = {n: [e for e in v] for n, v in lib.NEW.items()}
    newcls = {n: [e for e in v if next(p for p in rows[n]['points'] if lib.key(p['eps']) == lib.key(e))['classified']]
              for n, v in new.items()}
    n_new, n_newcls = sum(map(len, new.values())), sum(map(len, newcls.values()))
    if n_new != 56:
        stop(f'{n_new} first-time readings, not 56')

    def rec_of(n, e):
        """This instrument's records of a point: this run's, on its row's path, or M8.16.1's."""
        src = results.get(n) if n in results and lib.at(results[n], e)['points'][lib.CUTOFFS[-1]] else theirs.get(n)
        return lib.at(src, e) if src else None

    # ---- the text ---------------------------------------------------------------------------------------------
    T = []
    a = T.append
    settled = [n for n in rows if rows[n]['meets_s4']]
    unsettled = [n for n in rows if not rows[n]['meets_s4']]
    a('# M8.17 run record')
    a('')
    a(f"The record of M8.17's registered run, the census run on the nine rows M8.16.1 qualified, from {t0} to {t1}. It ran under "
      f"the governing terms, `run/m8_16_task_details.md` (SHA-256 `{terms[:16]}…`), merged in OpenWave "
      f"[#662]({OW}/pull/662) as `{m662.group(2)[:8]}`, and the census run's code frozen at MIT `338b873` with its manifest pin, "
      f"`{mpin[:16]}…`. The maintainer's go is [#662's comment]({F['go']}), and the freeze block is OpenWave's "
      f"`research/m8_17/freeze_block.md`, merged in [#673]({OW}/pull/673). Every number below is read from the run's files "
      f"in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them. `run/out/CENSUS.json` holds "
      f"every point's classification, its instrument and, where it is not classified, its causes; the case files hold every "
      f"point's readings at every cutoff; the locator's files hold each bracket's recomputed path, bisections and guard "
      f"readings. This record gives what the terms' § DEFINITION OF DONE asks: every point of the nine rows' windows with "
      f"its classification, its instrument and, on this instrument, the convergence rule's reading; every point not "
      f"classified, with its cause; every bracket, with its location or the condition it failed; and each row's ending. "
      f"Adjudication is the maintainers'.")
    a('')
    a(f"**The outcome.** The run completed, with no stop. Every point on the seven computed paths was accepted at all three "
      f"cutoffs, the reproduction gate held at all {sum(len(v) for g in gate.values() for v in g.values())} known points it "
      f"compared, and both of the locator's recomputed paths reproduced. Of the {n_new} first-time readings, {n_newcls} are "
      f"classified and {n_new - n_newcls} are not. {nw(len(settled), True)} rows meet an S4 completion condition: "
      + ', and '.join(' and '.join(n for n in settled if rows[n]['outcome'] == o)
                      + (', with each change of type located' if o.startswith('Each') else f', {o}')
                      for o in dict.fromkeys(rows[n]['outcome'] for n in settled))
      + f". {nw(len(unsettled), True)} rows end not settled by this run: "
      + ', '.join(unsettled[:-1]) + f" and {unsettled[-1]}, with "
      + ', '.join(str(len(rows[n]['open'])) for n in unsettled[:-1]) + f" and {len(rows[unsettled[-1]]['open'])} items open"
      + ' (§ 5). The locator located T2/R4\'s change of type, and did not locate T4/R5\'s (§ 4).')
    a('')
    a('**The rows:**')
    a('')
    a('| Row | Slot | Outcome | Meets an S4 completion condition | Classified | Not classified | Brackets |')
    a('|---|---|---|---|---|---|---|')
    def accounted(n, e):
        return n == loc['row'] and loc['lower']['eps'] < e < loc['upper']['eps']

    for n, r in rows.items():
        cls = sum(p['classified'] for p in r['points'])
        acc = sum(accounted(n, p['eps']) for p in r['points'] if not p['classified'])
        a(f"| {n} | `{lib.SLOT[n]}` | {r['outcome']} | {'yes' if r['meets_s4'] else 'no'} | {cls} of {len(r['points'])} | "
          f"{len(r['points']) - cls}{f', accounted for by its location' if acc else ''} | {len(r['changes'])} |")
    a('')

    # 1. custody
    a('## 1. Custody')
    a('')
    a(f"- **The freeze.** `run/FROZEN.json` was written once, at {F['written']}, by `run/write_guard.py`, after the go. It holds "
      f"the allowlist and the order, the seven rows of `census_lib.RUN_ORDER`; each row's case with its registered path; the "
      f"census values; what M8.17 inherits from M8.16.1; the terms' and the manifest's SHA-256; the go; and "
      f"{len(F['targets'])} targets, every reference file at its SHA-256 with `reference/SOURCES.json` among them. Its own "
      f"SHA-256 is `run/FROZEN_PIN`, `{fpin[:16]}…`.")
    a(f"- **The freeze block,** built by the pinned `run/freeze_block.py`, carries `FROZEN.json` in full. Its pull request, "
      f"[#673]({OW}/pull/673), was opened at {o673.group(1)} and merged at {m673.group(1)} as `{m673.group(2)[:8]}`, before "
      f"the run started. The maintainer's approval rebuilt the block byte for byte from MIT's git objects with its own "
      f"script, and records two reading notes: the adjudication reads #662's approval note 1 from the run's own environment "
      f"readings at its start and its end, and checks the published resume check against the SHA-256 the pull request "
      f"names. Both are below.")
    a(f"- **Before the launch,** read-only, by `launch/prelaunch_checks.py` with #673's number, at the bench beside this "
      f"folder: {len([l for l in pre_lines if l.startswith('ok')])} checks, all clean, its output kept as "
      f"`{POSTRUN[0]}`. Among them: both admissions, `devtools.frozen()` and `census.frozen()`; the manifest and the freeze "
      f"pin; `run/record_environment.py --check`, with no difference from `run/ENVIRONMENT.json`; no `run/out/`; no census "
      f"run in progress; the resume check at its reviewed SHA-256, and passing; mains power; and #673 merged, its one file "
      f"the block, equal at its head and on OpenWave `main`, with DCO passing.")
    a(f"- **The launch.** One launch, on the author's word, by the command `DEVLOG.md` entry 26 records, run unchanged from "
      f"this folder as a background task, under `caffeinate` on its shell, on mains power:")
    a('')
    a('  ```')
    a(f'  {cmd}')
    a('  ```')
    a('')
    a(f"  It checks the resume check's bytes against `{reviewed[:16]}…`, runs the check, and only then `run/census.py`. Its "
      f"console log, `run/out/census_console.log`, opens with the hash check's `OK` and the check's `PASS`, `run/out/` not "
      f"yet existing, and then holds the run's transcript, `run/out/census.out`, line for line. The resume check sat "
      f"outside the pinned tree, at `../resume_check/`, as the freeze block's pull request states; `launch/resume_check.py` "
      f"is that file, byte for byte, published with its {n_arms} arms, `launch/test_resume_check.py`, and their output. It "
      f"refuses on {nw(len(CHECKS))} checks: " + '; '.join(CHECKS) + '.')
    a(f"- **The run.** It started at {t0} and wrote its record at {t1}, {wall:.0f} s later, against {total} s by its own clock, "
      f"in the recorded environment: {envtext}. Its log, `run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, "
      f"equal to `run/MANIFEST_PIN`; one start, and so no resume; each completed job with its file's SHA-256, the seven rows "
      f"in their registered order and then the locator's {nw(len(jobs))} brackets; no stop; and the record and the transcript, "
      f"each with its SHA-256.")
    a(f"- **After the run:** every output equals the SHA-256 the log recorded; both admissions pass; the tree still equals the "
      f"manifest pin; and the environment, read again, equals `run/ENVIRONMENT.json` (`{POSTRUN[1]}`). The resume check then "
      f"refuses a relaunch, since the run has completed.")
    a('- **Post-run files.** These files were made or placed after the run, and are not records from it:')
    a(f"  - `{POSTRUN[0]}`, the checks before the launch, read just before it;")
    a(f"  - `{POSTRUN[1]}`, `run/record_environment.py --check`, read after the run, with no difference;")
    a("  - `launch/`, each file byte for byte as it ran from the bench beside this folder: the resume check and its arms; "
      "`prelaunch_checks.py`; and `test_launch_wrapper.py` with its output, the launch command's form run on stubs, as "
      "`DEVLOG.md` entry 26 records it. Its first check reads the command from `FILING_PLAN.md`'s step 3, which stays on the "
      "bench, so it reruns only beside that plan;")
    a('  - `run/out/census_console.log`, the run\'s console output, copied byte for byte from beside this folder once the run '
      'had ended;')
    a('  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference;')
    a("  - `SHA256SUMS`, regenerated over the published folder at the record's commit, one line per file but itself. The "
      "pre-run inventory stays at MIT `338b873`.")
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

    # 2. the reproduction gate
    a('## 2. The reproduction gate')
    a('')
    a("The terms' three rules (§ THE FREEZE, THE GUARD AND THE RUN), applied when each row's `run_case` returned, to every "
      "point of its path that M8.16.1 solved: rule 1, full equality with M8.16.1's record, timings aside, at a point M8.16.1 "
      "read and reached by its own steps; rule 2, the solve and acceptance fields at a point M8.16.1 withheld; rule 3, "
      "type, indices, `V₀`'s dimension and ranks, chains, Krein counts and the rule's verdict, at T1's and T4's 0.5, 1 "
      "and 2. Every compared point passed.")
    a('')
    a('| Row | Rule 1 | Rule 2 | Rule 3 | Failed | Path | s |')
    a('|---|---|---|---|---|---|---|')
    for n in rows_run:
        g = gate[n]
        a(f"| {n} | {len(g[1])} | {', '.join(fe(e) for e in g[2]) or 'none'} | {', '.join(fe(e) for e in g[3]) or 'none'} | 0 | "
          f"{len(results[n]['case']['points'])} points, to {fe(results[n]['case']['points'][-1]['eps'])} | {round(results[n]['seconds'])} |")
    a('')
    for n, rec in L.items():
        a(f"- **{rec['row']}'s bracket ({fe(rec['bracket'][0])}, {fe(rec['bracket'][1])}):** each cutoff's path recomputed from "
          f"its seed to the bracket's upper end, {paths[n][0]} points, every one equal to its record, field for field, "
          f"before the bisection began.")
    a('')

    # 3. the points
    a('## 3. The points, row by row')
    a('')
    a("Each row's window, every point with its classification, the instrument that supplies it, this instrument's reading "
      "and M8.15's. A point is classified on this instrument when it is accepted and K1 holds at every cutoff, the convergence "
      "rule reads it converged, and branch identity holds between `N = 24` and 32; the type is the rule's, with "
      "`(n(L), n(D), K)` and `k_i⁻` from the highest cutoff. On M8.15's, a point is classified where M8.15 decided it. "
      "\"Both\" means each instrument classifies it, and they agree. The source is this run's computation, or, beyond this "
      "run's paths, M8.16.1's and M8.15's records. The aligned distance is branch identity's, between `N = 24` and 32.")
    a('')
    for n, r in rows.items():
        a(f"### {n}, `{lib.SLOT[n]}`: {r['outcome']}")
        a('')
        a('| `ε` | Classification | Instrument | This instrument: the rule\'s reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |')
        a('|---|---|---|---|---|---|---|')
        unc = []
        for p in r['points']:
            h, m = p.get('here') or {}, p.get('m815') or {}
            hc = h.get('causes', [])
            if h.get('classified'):
                here = f"converged: {h['type']}; {idx(h)}"
            elif any('not computed here' in c for c in hc):
                here = 'not computed'
            else:
                parts = [c for c in hc if c.startswith(('K1 fails', 'untested', 'branch identity'))]
                here = '; '.join(parts + (['Unresolved'] if any(c.startswith('the rule reads it Unresolved') for c in hc) else []))
            ms = (m['type'] if m.get('decided') else
                  'no record' if any('holds no record' in c for c in m.get('causes', [])) else 'undecided')
            cl = (p['type'] if p['classified'] else
                  "not classified; accounted for by M8.15.2's location" if accounted(n, p['eps']) else 'not classified')
            inst = {'both': 'both', 'this instrument': 'this instrument', "M8.15's": "M8.15's"}.get(p.get('instrument'), 'none')
            src = {'this run': 'this run', "M8.16.1's and M8.15's records": "M8.16.1's and M8.15's records"}.get(p.get('source'), 'none')
            rc = rec_of(n, p['eps']) if src != 'none' else None
            dist = sci(rc['identity']['aligned_distance'], 3) if rc and rc.get('identity') else ''
            a(f"| {fe(p['eps'])} | {cl} | {inst} | {here} | {ms} | {src} | {dist} |")
            if not p['classified'] or not h.get('classified'):
                unc.append((p, hc, m))
        a('')
        if unc:
            a("**This instrument's causes,** at each point it does not classify, as the run's record states them:")
            a('')
            for p, hc, m in unc:
                tail = (f" Classified {p['type']} by M8.15's adjudicated reading." if p['classified'] else
                        f" It lies between M8.15.2's guard readings, {loc['lower']['eps']:.4f} and {loc['upper']['eps']:.4f}, "
                        "which account for it." if accounted(n, p['eps']) else ' Not classified.')
                a(f"- **`ε = {fe(p['eps'])}`:** " + '; '.join(hc) + '.' + tail)
            a('')

    # 4. the brackets
    a('## 4. The brackets')
    a('')
    a("A type bracket is two consecutive registered grid points of a row, both classified, whose types differ; an index "
      "bracket is one whose ends' `n(L)` is resolved at `N = 24` and 32 and different between them at both. A change across "
      "an unclassified grid point has no type bracket and is not located. The locator ran on each index bracket "
      "(§ LOCATING A CHANGE OF TYPE).")
    a('')
    for n, r in rows.items():
        for ch in r['changes']:
            lo, hi = fe(ch['lo']), fe(ch['hi'])
            if ch['kind'] == 'across':
                if n == loc['row']:
                    a(f"- **{n}, ({lo}, {hi}),** {ch['lo_type']} to {ch['hi_type']}, across the grid point "
                      f"{', '.join(fe(e) for e in ch['between'])}: accounted for by {ch['why']}, between its guard readings, "
                      f"{loc['lower']['type']} at {loc['lower']['eps']:.4f} and {loc['upper']['type']} at {loc['upper']['eps']:.4f}. "
                      f"The locator does not rerun it.")
                else:
                    a(f"- **{n}, ({lo}, {hi}),** {ch['lo_type']} to {ch['hi_type']}, across the unclassified grid point"
                      f"{'s' if len(ch['between']) > 1 else ''} {', '.join(fe(e) for e in ch['between'])}: no type bracket, "
                      f"and not located.")
                continue
            rec = located[(n, lib.key(ch['lo']), lib.key(ch['hi']))]
            ends = {tuple(v) for v in rec['nL'].values()}
            dd = {N: d for N, d in rec['delta'].items()}
            a(f"- **{n}, ({lo}, {hi}),** {ch['lo_type']} to {ch['hi_type']}: an {rec['kind']} bracket, `n(L)` "
              + (f"{next(iter(ends))[0]} to {next(iter(ends))[1]} at both `N = 24` and 32" if len(ends) == 1 else
                 ' and '.join(f"{a_} to {b_} at `N = {N}`" for N, (a_, b_) in rec['nL'].items()))
              + f"; the signed change `Δn(L)` is {sgn(dd['24'])} at `N = 24`, {sgn(dd['32'])} at 32, and {sgn(dd['16'])} at 16, "
                "the diagnostic. "
              + (f"**Located:** {ch['why']}." if ch['located'] else
                 f"**Not located:** the bisections at `N = 24` and 32 each made an unsuccessful stop, K1 failing."
                 if all('K1 fails' in f for f in rec['failures']) else f"**Not located:** {ch['why']}."))
            for N, b in rec['bisection'].items():
                mids = b['midpoints']
                iv = b['interval']
                width = (iv[1] - iv[0]) / iv[0] if iv else None
                last = mids[-1] if mids else None
                tail = ''
                if not b['complete'] and last:
                    sides = [s for s in ('from_lower', 'from_upper') if s in last and last[s].get('k1') is False]
                    tail = (k1_parts(mids) if b['stop'] == 'K1 fails' and len(sides) == 2 else
                            f" It stopped at the midpoint `ε = {last['eps']:.6f}`, where {b['stop']}.")
                a(f"  - `N = {N}`: {len(mids)} midpoints, the interval [{iv[0]:.6f}, {iv[1]:.6f}], {sci(width)} of its lower end, "
                  f"{'complete' if b['complete'] else 'not complete'}.{tail}"
                  + ('' if N in [str(x) for x in lib.DECIDING] else ' It is reported, and does not decide.'))
            if ch['located']:
                u = rec['union']
                a(f"  - The union at `N = 24` and 32: [{u[0]:.6f}, {u[1]:.6f}], {sci((u[1] - u[0]) / u[0])} of its lower end, "
                  f"narrower than `w = 10⁻³`.")
                for side, gs in rec['guards'].items():
                    g = gs[-1]
                    rd = g['reading']
                    a(f"  - The {side} guard, `δ = {g['delta']}`, at `ε = {g['eps']:.6f}`, solved from the bracket's "
                      f"{'lower' if side == 'lower' else 'upper'} end: {rd['type']}; {idx(rd)}, classified on this instrument.")
    a('')

    # 5. the row outcomes
    a('## 5. The row outcomes')
    a('')
    a("Each row's run outcome under § THE ROW OUTCOMES, and, separately, whether it meets an S4 completion condition. A row "
      "not settled by this run is not declared closed under S6 here: S6's condition is for the census page to establish, "
      "after the adjudication. Under the ruling of 2026-10-20, a point this run does not classify is not offered to this "
      "instrument again without a ruling on #512.")
    a('')
    a('| Row | Outcome | Meets an S4 completion condition | Open |')
    a('|---|---|---|---|')
    for n, r in rows.items():
        op = [fe(o['point']) for o in r['open'] if 'point' in o] + [f"({fe(o['change'][0])}, {fe(o['change'][1])})"
                                                                    for o in r['open'] if 'change' in o]
        a(f"| {n} | {r['outcome']} | {'yes' if r['meets_s4'] else 'no'} | {', '.join(op) or 'none'} |")
    a('')
    def change_text(n, o):
        ch = next(c for c in rows[n]['changes'] if [c['lo'], c['hi']] == o['change'])
        if ch['kind'] == 'across':
            return (f"across the unclassified grid point{'s' if len(ch['between']) > 1 else ''} "
                    f"{', '.join(fe(e) for e in ch['between'])}, with no type bracket")
        return 'its bisections at `N = 24` and 32 stopped by K1' if 'K1 fails' in o['why'] else o['why']

    for n in unsettled:
        r = rows[n]
        pts = [o for o in r['open'] if 'point' in o]
        chs = [o for o in r['open'] if 'change' in o]
        refs = ("Each point's cause is in § 3, and the bracket's in § 4." if pts and chs else
                "Each point's cause is in § 3." if pts else "The bracket's cause is in § 4.")
        a(f"- **{n}:** "
          + (f"{nw(len(pts))} point{'s' if len(pts) != 1 else ''} not classified, at `ε` = "
             f"{', '.join(fe(o['point']) for o in pts)}" if pts else 'every point classified')
          + (f"; {'and ' if pts else ''}its change of type in "
             + ', '.join(f"({fe(o['change'][0])}, {fe(o['change'][1])})" for o in chs)
             + f" not located, {'; '.join(change_text(n, o) for o in chs)}" if chs else '')
          + f'. {refs} No type is claimed there.')
    a('')

    # 6. what is new
    a('## 6. What is new')
    a('')
    a("The new evidence the terms name (§ Known outcomes, and what is new): the points beyond T1's and T4's samples, the four "
      "points M8.16.1 solved without a linear record, T5/R2 at 128 and 132, and the locator's points.")
    a('')
    a('| Row | First-time readings | Classified | Not classified |')
    a('|---|---|---|---|')
    for n, v in new.items():
        nc = [e for e in v if e not in newcls[n]]
        a(f"| {n} | {len(v)} | {len(newcls[n])} | {', '.join(fe(e) for e in nc) or 'none'} |")
    a(f"| all | {n_new} | {n_newcls} | {n_new - n_newcls} |")
    a('')
    wh = []
    for n, v in lib.WITHHELD.items():
        for e in v:
            p = next(q for q in rows[n]['points'] if lib.key(q['eps']) == lib.key(e))
            h = p.get('here') or {}
            wh.append(f"{n} at {fe(e)}, " + (f"{h['type']}; {idx(h)}" if h.get('classified') else 'not classified'))
    a(f"- **The four points M8.16.1 withheld,** their spectral records computed here for the first time: {'; '.join(wh)}.")
    nm = {n: sum(len(b['midpoints']) for b in rec['bisection'].values()) for n, rec in L.items()}
    ng = {n: sum(len(gs) for gs in rec.get('guards', {}).values()) for n, rec in L.items()}
    a(f"- **The locator's points:** " + '; '.join(f"on {L[n]['row']}'s bracket, {nm[n]} midpoints across the three cutoffs, "
                                                  f"each solved from both ends, and {ng[n] * 3 if ng[n] else 'no'} guard solves"
                                                  for n in L) + '.')
    a('')

    # 7 to 9
    a('## 7. Deviations')
    a('')
    a("- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above, once, with "
      "no resume and no stop.")
    a('')
    a('## 8. Corrections')
    a('')
    a("- **None.** The two reading notes in #673's approval need no change to the run; § 1 gives the readings they name.")
    a('')
    a('## 9. Follow-ups, outside M8.17')
    a('')
    a("- **The catalog.** After the adjudication, the census page's dated note gives each row's ending and catalog status, "
      "any S6 question this record raises, and S5's obligation as open (the terms, § DEFINITION OF DONE).")
    a("- **The S6 questions this record raises,** for the census page: the points § 5 leaves open, each with its cause in "
      "§ 3; T4/R4's change of type across its unclassified point; and T4/R5's bracket, where K1 stopped the bisections at "
      "`N = 24` and 32. Whether any of them is instrument-limited is the census page's to establish, not this record's.")
    a("- **S5.** The persistence tests for the Elliptic stretches this run classifies on T1 and T4 stay open, under a "
      "pre-registration of their own (the terms, § What this task is not).")
    a("- **The location's identification.** T2/R4's location is an `n(L)` interval with two guard readings, not a crossing "
      "point; its identification with the genuine index crossing is not established (the terms, § STATED LIMITS: WHAT IS "
      "ADDED).")
    a('')

    # 10. reproduction
    a('## 10. Reproduction')
    a('')
    a('`REPRODUCE.md` gives every command. For the run, from a copy of this folder:')
    a('- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and `python3 -I -B run/record_environment.py --check`;')
    a('- **the registered run:** the launch command above, from a copy without `run/out/`, beside a copy of `launch/` at '
      '`../resume_check/`. In a copy that keeps this `run/out/`, the resume check refuses, since the run has completed;')
    a('- `python3 -I -B tools/build_record.py --check`, which rebuilds this record from the files, recomputes every row\'s '
      'record with `census_lib.assemble`, and reports any difference.')
    a('')
    a('Bitwise agreement on another machine is not claimed: the reproduction rules compare bit for bit on the recorded '
      'environment, which the readings before and after the run equal.')

    text = '\n'.join(T) + '\n'
    if '—' in text:
        stop('the record holds an em-dash')
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
