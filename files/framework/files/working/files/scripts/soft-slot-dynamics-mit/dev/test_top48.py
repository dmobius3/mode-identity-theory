#!/usr/bin/env python3
"""T5's top at N = 48 (run/TOP48.md) on records alone: nothing is solved or read, and nothing in OUT is written.
Temporary outputs go to a temporary folder.

  1. The frozen values: the targets and in-row controls follow from T5's reading file on the first ladder, checked
     against its job record, by section 1's rule, and the in-row controls' marks are their classification there; the
     points the new ladder reads; the new ladder, its pairs, the band and the guard; the paths at N = 48, T5's first;
     SOLVE_PINS, the solves' pin alone; the fresh marks on the same six points; and every module a read runs, byte for
     byte the one the reads at N = 32 and 40 ran.
  2. The first ladder unchanged: jobs.ladder_reading on it gives every reading file on record, T5's and the four fresh
     controls', field for field, and fresh.evaluate gives the pass on record.
  3. The marks on the new ladder, on a first-ladder file read as the new ladder's: C3R/R4's flag, at its top cutoff
     alone, passes flag_48 and misses flag_40_48 until a flag is added at 40; P5's as-built Unresolved passes an
     unmarked as-built verdict and misses a converged one; a changed verdict, an index or a seed's check moved by one
     each misses; and the fresh48 pass gates T5 as the first pass gates the rows.
  4. The jobs' gates, in process: a path at N = 48 outside grid.PATHS_48 refuses, as does any cutoff above 48; the
     recheck refuses any cutoff but 32 and 40, and its refusal reads a missing, a differing and a passing record; the
     points the new ladder reads refuse any other entry.
  5. The gates through jobs.py, past the note gate on a throwaway repository whose page names this tree's pin: the old
     read and identity refuse N = 48; T5's reads at 48 and top48 refuse without the fresh48 pass; a fresh control's
     read at 48 refuses without its recheck; T5's recheck passes the fresh48 gate and stops at its stored path; fresh48
     refuses without the new ladder's readings.
  6. The runner: solves48 plans T5's whole grid first and the four fresh paths, with no note; the reads plan the fresh
     controls alone before the fresh48 pass and T5 after it; T5 named before the pass refuses, as does any entry
     outside grid.PATHS_48; top48 refuses before the pass; fresh48 waits for the readings; a read launch refuses with
     no note.
  7. top48 on synthetic readings: with the in-row controls holding their marks each target keeps its readings both ways;
     with one control's type moved, no target is classified on the new ladder, and each reading is kept as reported.

Usage: test_top48.py OUT MIT_REPO
"""
import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
import census  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import checks as ck  # noqa: E402
import fresh  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402
import runner  # noqa: E402

JOBS, RUNNER = os.path.join(ROOT, 'run', 'jobs.py'), os.path.join(ROOT, 'run', 'runner.py')
COMMITTED = 'files/framework/files/working/files/scripts/soft-slot-dynamics-mit'
READ_PATH = ('run/driver.py', 'run/census.py', 'run/checks.py', 'run/changed.py', 'run/census_lib.py', 'run/cases.py',
             'run/seeds.py')
ok = True


def claim(text, good):
    global ok
    ok = ok and bool(good)
    print(f"{'ok  ' if good else 'FAIL'} {text}", flush=True)


def refuses(f, *a, want=''):
    try:
        f(*a)
    except (PermissionError, SystemExit) as e:
        return want in str(e)
    return False


def run(argv):
    p = subprocess.run([sys.executable, '-I', '-B', *argv], capture_output=True, text=True, cwd=ROOT)
    return p.returncode, p.stdout + p.stderr


def as_new_ladder(d):
    """A first-ladder reading file as if its cutoffs were the new ladder's: N = 24, 32 and 40 read as 32, 40 and 48."""
    cut = dict(zip((str(N) for N in grid.LADDER), (str(N) for N in grid.LADDER_48)))
    pk = {lib.pair_key(a): lib.pair_key(b) for a, b in zip(lib.ARM_A['pairs'], grid.LAD_48['pairs'])}
    out = copy.deepcopy(d)
    out['cutoffs'] = {cut[N]: v for N, v in d['cutoffs'].items()}
    out['identity'] = {k: {pk[p]: v for p, v in ids.items()} for k, ids in d['identity'].items()}
    out['case'] = dict(d['case'], cutoffs=list(grid.LADDER_48))
    return out


def put(out, fname, obj, job):
    jobs.write_json(os.path.join(out, fname), obj)
    jobs.Job(out, job).complete([fname])


def main():
    out, repo = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    t5 = grid.TOP48['row']

    print('1. The frozen values')
    jobs.record_of(out, f'reading_{t5}')
    first = lib.load_json(os.path.join(out, f'{t5}.json'))
    above = {k: b for k, b in first['both'].items() if float(k) > 90.51}
    none = sorted((k for k, b in above.items() if not (b['as_built']['classified'] or b['changed']['classified'])), key=float)
    both = sorted((k for k, b in above.items() if b['as_built']['classified'] and b['changed']['classified']), key=float)
    claim(f"T5's points above 90.51 not classified on the first ladder, both ways, are the targets: {none}",
          none == [lib.key(e) for e in grid.TOP48['targets']])
    claim(f'those classified both ways are the in-row controls: {both}, and no point above 90.51 is classified one way only',
          both == [lib.key(e) for e in grid.TOP48['in_row']] and len(none) + len(both) == len(above))
    marks = grid.TOP48['in_row_marks']
    claim(f"the in-row controls' marks are their classification on the first ladder, both ways: {marks}",
          all(above[k][arm][f] == v for k in both for arm in ('as_built', 'changed') for f, v in marks.items()))
    pts = jobs.points_48(t5)
    claim(f'the new ladder reads those twelve on T5, on its own grid values: {[round(e, 4) for e in pts]}',
          sorted(lib.key(e) for e in pts) == sorted(none + both, key=float) and set(pts) <= set(grid.entry(t5)[1]))
    claim("a fresh control's points are its whole entry, and any other entry refuses",
          all(jobs.points_48(t) == grid.entry(t)[1] for t in grid.FRESH)
          and refuses(jobs.points_48, 'T1_R4', want='T5 and the fresh controls alone'))
    claim(f"the new ladder is N = 32, 40 and 48 with pairs (32, 40) and (40, 48), and the band beside it: {grid.LAD_48}",
          grid.LAD_48 == dict(name='48', cutoffs=(32, 40, 48), deciding=(40, 48), pairs=((32, 40), (40, 48)), beside=True)
          and grid.LADDER_48 == (32, 40, 48))
    claim(f'the band and the guard are unchanged: BAND_N {lib.BAND_N}, BESIDE_N {lib.BESIDE_N}, the guard {ck.IDENTITY}',
          (lib.BAND_N, lib.BESIDE_N, ck.IDENTITY) == (16, 24, 1e-2))
    claim(f"the paths at N = 48 are T5's whole grid, first, and the four fresh entries: {grid.solves_48()}",
          grid.solves_48()[0] == (t5, 48) and sorted(t for t, _ in grid.solves_48()) == sorted([t5, *grid.FRESH]))
    pin = jobs.record_of(out, f'path_{t5}_N40')['manifest']
    claim(f"SOLVE_PINS is the solves' pin alone, {pin[:8]}, the one T5's path at N = 40 ran under",
          jobs.SOLVE_PINS == frozenset((pin,)))
    claim('the fresh marks on the new ladder are for the same six points as the first ladder\'s',
          set(grid.PASS_MARKS_48) == set(grid.PASS_MARKS))
    reader = subprocess.run(['git', '-C', repo, 'log', '-1', '--format=%H', "--grep=the reader's changes, landed after the "
                             'last solve', 'origin/main'], capture_output=True, text=True, check=True).stdout.strip()
    inst = sorted(f'instrument/{f}' for f in os.listdir(os.path.join(ROOT, 'instrument')) if f.endswith('.py'))
    differ = []
    for rel in inst + list(READ_PATH):
        theirs = subprocess.run(['git', '-C', repo, 'show', f'{reader}:{COMMITTED}/{rel}'], capture_output=True).stdout
        with open(os.path.join(ROOT, rel), 'rb') as f:
            if f.read() != theirs:
                differ.append(rel)
    claim(f"every module a read runs, {len(inst) + len(READ_PATH)} files, is byte for byte the reader's at {reader[:8]}, "
          f'under which the reads at N = 32 and 40 ran: {differ or "none differs"}', not differ)
    theirs = subprocess.run(['git', '-C', repo, 'show', f'{reader}:{COMMITTED}/run/jobs.py'], capture_output=True,
                            text=True).stdout

    def cut_block(text):
        i = text.index('class Cut(census.Cutoff):')
        return text[i:text.index('\n\n\nclass ', i)]
    with open(JOBS, encoding='utf-8') as f:
        claim("and jobs.Cut, which solves and reads each point, is byte for byte the reader's", cut_block(f.read()) == cut_block(theirs))

    print('2. The first ladder unchanged')
    for tag in (t5, *grid.FRESH):
        jobs.record_of(out, f'reading_{tag}')
        mine = census.roundtrip(jobs.ladder_reading(out, tag, grid.LADDER, lib.ARM_A))
        claim(f'ladder_reading on the first ladder gives {tag}.json on record, field for field',
              mine == lib.load_json(os.path.join(out, f'{tag}.json')))
    name, pass_file = fresh.names()
    jobs.record_of(out, name)
    claim(f'fresh.evaluate gives the pass on record, {pass_file}', fresh.evaluate(out) == lib.load_json(os.path.join(out, pass_file)))
    claim('and the rows still pass the first gate', fresh.refusal(out) is None)

    print('3. The marks on the new ladder, on first-ladder files read as the new ladder\'s')
    with tempfile.TemporaryDirectory() as tmp:
        c3 = as_new_ladder(lib.load_json(os.path.join(out, 'fresh_C3R_R4.json')))
        p5 = as_new_ladder(lib.load_json(os.path.join(out, 'fresh_P5.json')))

        def misses(d, tag, e, m):
            jobs.write_json(os.path.join(tmp, f'{tag}_L48.json'), d)
            return fresh.misses(tmp, tag, e, m, grid.LADDER_48, fresh.CAUSES_48, f'{tag}_L48.json', seeds=True)
        k = lib.key(0.20)
        claim('C3R/R4 at 0.20, its flag at the top cutoff alone, passes flag_48',
              misses(c3, 'fresh_C3R_R4', 0.20, ('Unresolved', 'converged', 'flag_48')) == [])
        got = misses(c3, 'fresh_C3R_R4', 0.20, ('Unresolved', 'converged', 'flag_40_48'))
        claim(f'and misses flag_40_48: {got}', len(got) == 1 and "not by the mark's flag_40_48" in got[0])
        c3b = copy.deepcopy(c3)
        c3b['cutoffs']['40']['points'][k]['record']['unresolved'] = [changed.ND_LINE]
        c3b['cutoffs']['40']['points'][k]['b_resolved'] = True
        claim('with the flag added at N = 40 too, flag_40_48 passes and flag_48 misses',
              misses(c3b, 'fresh_C3R_R4', 0.20, ('Unresolved', 'converged', 'flag_40_48')) == []
              and misses(c3b, 'fresh_C3R_R4', 0.20, ('Unresolved', 'converged', 'flag_48')) != [])
        c3c = copy.deepcopy(c3)
        c3c['cutoffs']['48']['points'][k]['b_resolved'] = False
        claim('a flag B does not clear misses flag_48', misses(c3c, 'fresh_C3R_R4', 0.20, ('Unresolved', 'converged', 'flag_48')) != [])
        k = lib.key(0.24)
        claim("P5 at 0.24, Unresolved as built, passes an unmarked as-built verdict",
              misses(p5, 'fresh_P5', 0.24, (None, 'converged', None)) == [])
        got = misses(p5, 'fresh_P5', 0.24, ('converged', 'converged', None))
        claim(f'and misses a converged one: {got}', len(got) == 1 and got[0].startswith('as built Unresolved, marked converged'))
        m = copy.deepcopy(p5)
        m['changed'][k] = dict(m['changed'][k], verdict='Unresolved')
        claim('a changed verdict moved misses', any(g.startswith('changed Unresolved') for g in misses(m, 'fresh_P5', 0.24, (None, 'converged', None))))
        m = copy.deepcopy(p5)
        m['cutoffs']['48']['points'][k]['record']['nL'] += 1
        claim('an index moved at N = 48 misses', any('at N = 48' in g for g in misses(m, 'fresh_P5', 0.24, (None, 'converged', None))))
        m = copy.deepcopy(p5)
        m['cutoffs']['48']['seed']['ok'] = False
        claim("a seed's check failed at N = 48 misses", "the seed's check fails at N = 48" in misses(m, 'fresh_P5', 0.24, (None, 'converged', None)))
    with tempfile.TemporaryDirectory() as tmp:
        claim('T5 waits with no fresh48 pass on record', fresh.refusal_48(tmp) == 'the fresh controls have no pass on record')
        name48, pass48 = fresh.names_48()
        claim(f'the fresh48 job and file are named by the new marks, not the first: {name48}, {pass48}',
              name48 != fresh.names()[0] and name48.startswith('fresh48_') and pass48 == f'fresh48_pass_{name48[8:]}.json')
        put(tmp, pass48, dict(results={'fresh_C2b 0.3': ['a miss']}, passed=False, marks=fresh.marks_48(), files={}), name48)
        claim('a failed pass refuses, naming the miss', 'a fresh control missed its marks: fresh_C2b 0.3: a miss' in fresh.refusal_48(tmp))
        put(tmp, pass48, dict(results={}, passed=True, marks=fresh.marks_now(), files={}), name48)
        claim("a pass for other marks refuses", fresh.refusal_48(tmp) == "the pass on record is not for run/grid.py's marks")
        put(tmp, pass48, dict(results={}, passed=True, marks=fresh.marks_48(), files={}), name48)
        claim('a pass for the new marks lets T5 through', fresh.refusal_48(tmp) is None)

    print('4. The jobs\' gates, in process')
    with tempfile.TemporaryDirectory() as tmp:
        claim('a path at N = 48 outside grid.PATHS_48 refuses', refuses(jobs.path, tmp, 'T1_R4', 48, want='grid.PATHS_48 alone'))
        claim('a path above N = 48 refuses', refuses(jobs.path, tmp, t5, 56, want='no path for'))
        claim('no job record was written', not os.path.exists(os.path.join(tmp, 'jobs')) or not os.listdir(os.path.join(tmp, 'jobs')))
        claim('the recheck refuses N = 24 and 48', refuses(jobs.recheck48, tmp, 'fresh_C2b', 24, want='32 and 40 alone')
              and refuses(jobs.recheck48, tmp, 'fresh_C2b', 48, want='32 and 40 alone'))
        claim("with no recheck on record, a read at 48 refuses", 'no completed job recheck48_fresh_C2b_N32' in jobs.recheck_refusal(tmp, 'fresh_C2b'))
        for N, same in ((32, True), (40, False)):
            put(tmp, f'recheck48_fresh_C2b_N{N}.json', dict(differences={}, same=same), f'recheck48_fresh_C2b_N{N}')
        claim('a recheck that found a difference refuses', jobs.recheck_refusal(tmp, 'fresh_C2b') == 'recheck48_fresh_C2b_N40 found a difference from the stored read')
        put(tmp, 'recheck48_fresh_C2b_N40.json', dict(differences={}, same=True), 'recheck48_fresh_C2b_N40')
        claim('a passing recheck at both cutoffs lets the read through', jobs.recheck_refusal(tmp, 'fresh_C2b') is None)
        with open(os.path.join(tmp, 'recheck48_fresh_C2b_N32.json'), 'a', encoding='utf-8') as f:
            f.write(' ')
        claim('a recheck file changed after its job logged it refuses', 'differs from the SHA-256 its job logged' in jobs.recheck_refusal(tmp, 'fresh_C2b'))

    print('5. The gates through jobs.py, past the note gate')
    pin = open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8').read().strip()
    with tempfile.TemporaryDirectory() as tmp:
        fake = os.path.join(tmp, 'repo')

        def g(*a):
            return subprocess.run(['git', '-C', fake, '-c', 'user.name=t', '-c', 'user.email=t@t', *a],
                                  capture_output=True, text=True, check=True).stdout.strip()
        subprocess.run(['git', 'init', '-q', fake], check=True)
        page = os.path.join(fake, jobs.NOTE_PAGE)
        os.makedirs(os.path.dirname(page))
        with open(page, 'w', encoding='utf-8') as f:
            f.write(f'a census page whose note names the pin {pin}\n')
        g('add', '.')
        g('commit', '-q', '-m', 'the note')
        commit = g('rev-parse', 'HEAD')
        g('update-ref', 'refs/remotes/origin/main', commit)
        o = os.path.join(tmp, 'out')
        os.makedirs(os.path.join(o, 'jobs'))
        name, pass_file = fresh.names()
        for f in [pass_file, *lib.load_json(os.path.join(out, pass_file))['files']]:
            shutil.copyfile(os.path.join(out, f), os.path.join(o, f))
        shutil.copyfile(os.path.join(out, 'jobs', name + '.json'), os.path.join(o, 'jobs', name + '.json'))
        note = ['--note', commit, '--repo', fake]
        claim('in the copy the rows pass the first gate, and T5 waits at the second',
              fresh.refusal(o) is None and fresh.refusal_48(o) is not None)
        for argv in (['read', t5, '48'], ['identity', t5, '40', '48']):
            code, text = run([JOBS, o, *argv, *note])
            claim(f"jobs.py {' '.join(argv)} refuses N = 48", code != 0 and 'read by read48 and identity48 alone' in text)
        for argv in (['read48', t5], ['identity48', t5], ['reading48', t5], ['top48']):
            code, text = run([JOBS, o, *argv, *note])
            claim(f"jobs.py {' '.join(argv)} refuses before the fresh48 pass",
                  code != 0 and "no read of T5's top at N = 48 before the fresh controls pass" in text)
        code, text = run([JOBS, o, 'read48', 'fresh_C2b', *note])
        claim("a fresh control's read at 48 refuses before its recheck", code != 0 and 'no read at N = 48 before the recheck passes' in text)
        code, text = run([JOBS, o, 'recheck48', t5, '32', *note])
        claim("T5's recheck passes the fresh48 gate and stops at its stored path, none here",
              code != 0 and 'no completed job path_T5_R2_N32' in text and 'fresh controls pass' not in text)
        code, text = run([JOBS, o, 'fresh48', *note])
        claim('fresh48 refuses without the new ladder\'s readings', code != 0 and 'no completed job reading48_' in text)
        claim('nothing was written but what the copy holds', sorted(os.listdir(os.path.join(o, 'jobs'))) == [name + '.json'])
        code, text = run([JOBS, o, 'read48', 'fresh_C2b'])
        claim('jobs.py read48 with no note refuses', code != 0 and 'no read of this computation before the dated note' in text)

    print('6. The runner')
    with tempfile.TemporaryDirectory() as tmp:
        plan = runner.plan('solves48', [], tmp)
        claim(f"solves48 plans T5's whole grid first, then the four fresh paths: {[j[0] for j in plan]}",
              [j[0] for j in plan] == [f'path_{t}_N48' for t, _ in grid.solves_48()] and plan[0][1] == ['path', t5, '48'])
        claim('the reads plan the fresh controls alone before the fresh48 pass',
              [j[0] for j in runner.plan('reads48', [], tmp)] == [f'read_{t}_N48' for t in sorted(grid.FRESH, key=lambda t: -grid.hours(t, 48))])
        claim('T5 named before the pass refuses', refuses(runner.plan, 'reads48', ['--tags', t5], tmp, want="T5's top is not read at N = 48"))
        claim('an entry outside grid.PATHS_48 refuses', refuses(runner.plan, 'rechecks48', ['--tags', 'T1_R4'], tmp, want='alone'))
        claim('top48 refuses before the pass', refuses(runner.plan, 'top48', [], tmp, want="T5's top waits"))
        claim('fresh48 waits for the new ladder\'s readings', runner.plan('fresh48', [], tmp) == [])
        claim('the rechecks plan N = 32 and 40 for each fresh control',
              sorted(j[0] for j in runner.plan('rechecks48', [], tmp)) == sorted(f'recheck48_{t}_N{N}' for t in grid.FRESH for N in (32, 40)))
        put(tmp, fresh.names_48()[1], dict(results={}, passed=True, marks=fresh.marks_48(), files={}), fresh.names_48()[0])
        claim('after the pass the reads add T5, and top48 is planned',
              f'read_{t5}_N48' in [j[0] for j in runner.plan('reads48', [], tmp)]
              and runner.plan('top48', [], tmp) == [('top48', ['top48'], 0.01)])
        for t in grid.FRESH:
            jobs.Job(tmp, f'reading48_{t}').complete([])
        claim('with every reading on the new ladder, fresh48 is planned', runner.plan('fresh48', [], tmp) == [(fresh.names_48()[0], ['fresh48'], 0.01)])
        code, text = run([RUNNER, tmp, 'reads48'])
        claim('a read launch with no note refuses', code != 0 and 'reads need --note and --repo' in text
              and not os.path.exists(os.path.join(tmp, 'RUNLOG.json')))

    print('7. top48 on synthetic readings')

    def cls(t, idx, classified=True):
        return dict(classified=True, type=t, nL=idx[0], nD=idx[1], K=idx[2], ki=0) if classified else \
            dict(classified=False, causes=['branch identity fails between N = 24 and 32'])
    for moved in (False, True):
        with tempfile.TemporaryDirectory() as tmp:
            new, old = {}, {}
            for e in grid.TOP48['in_row']:
                c = cls('Hyperbolic' if moved and e == 106.0 else 'Elliptic', (9, 3, 6))
                new[lib.key(e)] = dict(as_built=c, changed=c, same=True)
            for e in grid.TOP48['targets']:
                c = cls('Hyperbolic', (4, 0, 4))
                new[lib.key(e)] = dict(as_built=c, changed=c, same=True)
                o = cls(None, None, False)
                old[lib.key(e)] = dict(as_built=o, changed=o, same=True)
            put(tmp, f'{t5}_L48.json', dict(both=new), f'reading48_{t5}')
            put(tmp, f'{t5}.json', dict(both=old), f'reading_{t5}')
            jobs.top48(tmp)
            r = lib.load_json(os.path.join(tmp, 'TOP48.json'))
            tk = [lib.key(e) for e in grid.TOP48['targets']]
            if not moved:
                claim('with the in-row controls holding, each target keeps its readings both ways, beside the first ladder\'s',
                      r['in_row_held'] and all(r['targets'][k]['on_48'][a] == new[k][a] for k in tk for a in ('as_built', 'changed'))
                      and all(r['targets'][k]['on_first'] == old[k] for k in tk))
            else:
                claim(f"with 106's type moved, the miss is named: {r['in_row'][lib.key(106.0)]}",
                      not r['in_row_held'] and r['in_row'][lib.key(106.0)] and not r['in_row'][lib.key(100.0)])
                claim('and no target is classified on the new ladder, each reading kept as reported',
                      all(not r['targets'][k]['on_48'][a]['classified'] and r['targets'][k]['on_48'][a]['reported'] == new[k][a]
                          for k in tk for a in ('as_built', 'changed')))
    print('PASS' if ok else 'FAIL')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
