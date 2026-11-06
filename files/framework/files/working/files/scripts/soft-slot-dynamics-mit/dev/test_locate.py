#!/usr/bin/env python3
"""The locator's terms (run/LOCATOR.md) on records alone: nothing is solved, and nothing in OUT is written. Temporary
outputs go to a temporary folder.

  1. The frozen values: the row, the bracket and the reproduction's case (grid.LOCATOR); the allowlist, which gains
     T4/R5 alone; census_lib's locator constants, as M8.18 froze them; and the code the locator runs, byte for byte
     M8.18's, so M8.18's tests of it carry (dev/runs/012_locator_tests/m8_18_test_locator.out).
  2. The bracket, from the reads: the reading file, checked against its job record, gives one change of type both ways,
     on the grid's own values; its ends' n(L), 7 and 6, are resolved and different at N = 32 and 40, and at N = 24, so
     N = 24 is bisected and reported; both ends are classified both ways. A reading that classifies either end otherwise
     refuses. The stored ends pass the solve pins, and their lam is the reads' own.
  3. The changed classification at a guard reading, from its records alone: it equals the reading's at every point of
     T4/R4, keys as numbers or, after a round trip, strings; at T5's second member's 0.354, where the two readings
     differ, it gives the changed one, and a mutation that reads the records as built gives the other.
  4. Both verdicts: a location stands only where the changed classification agrees at the guard readings that count,
     on synthetic records, with the check's mutation letting a disagreement through.
  5. The reproduction's comparison: M8.18's files by its pinned SHA256SUMS, a changed file and a changed list each
     refusing; the record's comparison, which a timing does not move and one field does; the solutions' comparison; T4/R5's
     case here equal to M8.18's frozen one; and as_m818, which sets aside this tree's new fields alone.
  6. The gates: T4/R4 refuses with no reproduction on record, a failed one, a file changed after its job logged it, or a
     file missing; jobs.py refuses either job with no note, and with a note whose census page does not name this
     tree's pin; the runner plans the reproduction first, from --source, then T4/R4 once it has passed, refuses a failed
     one, and refuses a launch with no note.
  7. A reproduction on record that did not pass exits nonzero through jobs.py, past the note gate on a throwaway
     repository whose page names this tree's pin, so the runner reports the job failed; its record stands. A passing
     one exits zero.

Usage: test_locate.py OUT M818_FOLDER MIT_REPO
"""
import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import census  # noqa: E402
import census_lib as lib  # noqa: E402
import driver as dr  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402
import locate  # noqa: E402
import runner  # noqa: E402

JOBS, RUNNER = os.path.join(ROOT, 'run', 'jobs.py'), os.path.join(ROOT, 'run', 'runner.py')
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


def main():
    out, m818, repo = sys.argv[1:4]
    held = {}
    with open(os.path.join(m818, 'SHA256SUMS'), encoding='utf-8') as f:
        for line in f:
            if line.strip():
                held[line.split(None, 1)[1].strip()] = line.split()[0]

    print('1. The frozen values')
    W4 = lib.WINDOWS['R4']
    claim('the row, its bracket on the grid, and the reproduction\'s case',
          grid.LOCATOR == dict(row='T4_R4', bracket=(W4[8], W4[9]), repro='T4/R5') and W4[8] == 4.0
          and abs(W4[9] - 4 * 2 ** 0.5) < 1e-14 and W4[7] < W4[8])
    reads = subprocess.run(['git', '-C', repo, 'log', '-1', '--format=%H', "--grep=the reads' records, before the locator",
                            'origin/main'], capture_output=True, text=True, check=True).stdout.strip()
    before = set(json.loads(subprocess.run(['git', '-C', repo, 'show', f'{reads}:files/framework/files/working/files/scripts/'
                                            'soft-slot-dynamics-mit/run/FROZEN.json'], capture_output=True, text=True,
                                           check=True).stdout)['allowlist'])
    claim(f"the allowlist gains T4/R5 alone, against the run's at the reads' commit, {reads[:8]}",
          set(grid.allowlist()) - before == {'T4/R5'} and before <= set(grid.allowlist()))
    claim("census_lib's locator constants as M8.18 froze them",
          (lib.MOVED, lib.W, lib.W_HALF, lib.DELTAS, lib.AGREE) == (0.4, 1e-3, 5e-4, (0.01, 0.05), 1e-2)
          and lib.ARM_A == dict(name='A', cutoffs=(24, 32, 40), deciding=(32, 40), pairs=((24, 32), (32, 40)), beside=True)
          and lib.ARM_B['cutoffs'] == (16, 24, 32) and lib.ARM_B['deciding'] == (24, 32))
    same = {f: dr.sha(os.path.join(ROOT, f)) == held.get(f) for f in
            ('run/census_lib.py', 'run/census.py', 'run/checks.py', 'run/driver.py', 'run/cases.py', 'run/seeds.py')}
    inst = sorted(os.path.relpath(os.path.join(dp, n), ROOT) for dp, _, ns in os.walk(os.path.join(ROOT, 'instrument'))
                  for n in ns if n.endswith('.py'))
    same.update({f: dr.sha(os.path.join(ROOT, f)) == held.get(f) for f in inst if f != 'instrument/convergence.py'})
    claim(f'the code the locator runs is byte for byte M8.18\'s: {sum(same.values())} of {len(same)} files '
          f'(instrument/convergence.py aside, whose arm the locator does not use)', all(same.values()))

    print('2. The bracket, from the reads')
    jobs.record_of(out, 'reading_T4_R4')
    res = lib.load_json(os.path.join(out, 'T4_R4.json'))
    ch = locate.the_change(res)
    claim('one change of type both ways, Elliptic to Hyperbolic, on the grid\'s own values',
          (ch['kind'], ch['lo'], ch['hi'], ch['lo_type'], ch['hi_type'], ch['between'])
          == ('type', W4[8], W4[9], 'Elliptic', 'Hyperbolic', []))
    ends = {e: lib.at(res, e, locate.LAD) for e in (ch['lo'], ch['hi'])}
    kind, pairs = lib.bracket_kind(ends[ch['lo']]['points'], ends[ch['hi']]['points'], locate.LAD)
    n24 = (lib.nl_at(ends[ch['lo']]['points'][24]), lib.nl_at(ends[ch['hi']]['points'][24]))
    claim(f'index evidence: {kind}, n(L) {pairs} at the deciding cutoffs, and {n24} at N = 24, so it is bisected',
          kind == 'index' and pairs == {32: (7, 6), 40: (7, 6)} and n24 == (7, 6))
    b = {e: res['both'][lib.key(e)] for e in (ch['lo'], ch['hi'])}
    claim('both ends classified both ways: 4 Elliptic (7, 1, 6), 5.66 Hyperbolic (6, 1, 5)',
          all(b[e]['same'] for e in b) and [(b[e]['as_built']['type'], b[e]['as_built']['nL'], b[e]['as_built']['nD'],
                                             b[e]['as_built']['K']) for e in (ch['lo'], ch['hi'])]
          == [('Elliptic', 7, 1, 6), ('Hyperbolic', 6, 1, 5)])
    bad = copy.deepcopy(res)
    bad['both'][lib.key(W4[8])]['changed'] = dict(classified=False, causes=['a mutation'])
    claim('a reading that leaves the end at 4 unclassified changed refuses', refuses(locate.the_change, bad, want='changed'))
    bad = copy.deepcopy(res)
    bad['both'][lib.key(W4[9])]['as_built']['type'] = 'Elliptic'
    claim('a reading that types 5.66 Elliptic as built refuses', refuses(locate.the_change, bad, want='as_built'))
    good = True
    for N in locate.LAD['cutoffs']:
        sols = jobs.stored(out, 'T4_R4', N)[1]
        for e in (ch['lo'], ch['hi']):
            s = sols[lib.key(e)]
            good = good and s['ok'] and s['state'][1] == ends[e]['points'][N]['lam']
    claim('the stored ends pass the solve pins at N = 24, 32 and 40, accepted, their lam the reads\' own', good)

    print('3. The changed classification at a guard reading')
    _, _, case = grid.entry('T4_R4')
    n_same = sum({x: locate.changed_class(lib.at(res, float(k), locate.LAD), case).get(x) for x in res['both'][k]['changed']}
                 == res['both'][k]['changed'] for k in res['both'])
    claim(f"it equals the reading's changed classification at {n_same} of {len(res['both'])} points of T4/R4",
          n_same == len(res['both']) == 18)
    k = lib.key(W4[8])
    rt = census.roundtrip(lib.at(res, W4[8], locate.LAD))
    claim('the same from records after a round trip, their keys strings',
          {x: locate.changed_class(rt, case).get(x) for x in res['both'][k]['changed']} == res['both'][k]['changed']
          and '24' in rt['points'])
    t5j = lib.load_json(os.path.join(out, 'T5J_R2.json'))
    _, _, case_j = grid.entry('T5J_R2')
    kj = lib.key(0.25 * 2 ** 0.5)
    got = locate.changed_class(lib.at(t5j, float(kj), locate.LAD), case_j)
    built = lib.here(lib.at(t5j, float(kj), locate.LAD), case_j, locate.LAD)
    claim("at T5's second member's 0.354 it gives the changed classification, Elliptic, where as built it is not "
          "classified; reading the records as built, the mutation, gives the other",
          got['classified'] and got['type'] == 'Elliptic' and got == t5j['both'][kj]['changed']
          and not built['classified'] and built == t5j['both'][kj]['as_built'])

    print('4. Both verdicts, on synthetic records')

    def guard(eps, delta, cls, typ, mark):
        return dict(delta=delta, eps=eps, reading=dict(classified=cls, type=typ if cls else None, records=dict(mark=mark)))

    def rec_with(lower, upper, located=True):
        return dict(located=located, guards=dict(lower=lower, upper=upper), failures=[], span=[3.96, 5.71] if located else None,
                    why='located' if located else 'a stop')

    def fake(marks):
        return lambda records, case_: dict(classified=marks[records['mark']] is not None, type=marks[records['mark']])

    agree = fake(dict(lo='Elliptic', hi='Hyperbolic', lo1=None))
    r = locate.both_verdicts(rec_with([guard(3.96, 0.01, True, 'Elliptic', 'lo')], [guard(5.71, 0.01, True, 'Hyperbolic', 'hi')]),
                             case, agree)
    claim('both agree at the guards that count: the location stands, the changed readings recorded',
          r['located'] and r['both_verdicts'] and r['changed_guards']['lower'][0]['changed']['type'] == 'Elliptic')
    no_lo = fake(dict(lo=None, hi='Hyperbolic'))
    base = rec_with([guard(3.96, 0.01, True, 'Elliptic', 'lo')], [guard(5.71, 0.01, True, 'Hyperbolic', 'hi')])
    r = locate.both_verdicts(copy.deepcopy(base), case, no_lo)
    claim('the changed reading unclassified at the lower guard that counts: not located, the guard named',
          not r['located'] and r['span'] is None and 'the lower guard at 3.96' in r['why'] and not r['both_verdicts'])
    claim('the mutation that skips the check lets it through', (lambda x: x)(copy.deepcopy(base))['located'])
    flip = fake(dict(lo='Elliptic', hi='Elliptic'))
    r = locate.both_verdicts(copy.deepcopy(base), case, flip)
    claim('the changed reading of another type at the upper guard: not located', not r['located'] and 'upper' in r['why'])
    later = fake(dict(lo1='Hyperbolic', lo='Elliptic', hi='Hyperbolic'))
    r = locate.both_verdicts(rec_with([guard(3.96, 0.01, False, None, 'lo1'), guard(3.80, 0.05, True, 'Elliptic', 'lo')],
                                      [guard(5.71, 0.01, True, 'Hyperbolic', 'hi')]), case, later)
    claim('a guard that does not count does not decide: the 0.05 guard counts, and the location stands',
          r['located'] and len(r['changed_guards']['lower']) == 2)
    r = locate.both_verdicts(rec_with([guard(3.96, 0.01, True, 'Elliptic', 'lo')], [guard(5.71, 0.01, True, 'Hyperbolic', 'hi')],
                                      located=False), case, agree)
    claim('a bracket not located as built stays not located', not r['located'] and r['why'] == 'a stop')
    r = locate.both_verdicts(dict(located=False, why='a stop', failures=['x']), case, agree)
    claim('a stop before the guards records no changed reading', r['changed_guards'] is None and not r['located'])

    print("5. The reproduction's comparison")
    src = locate.m818_source(m818)
    claim(f"M8.18's files by its pinned SHA256SUMS: {len(src['sha256'])} files, each as listed",
          len(src['sha256']) == len(locate.M818) and all(held[f] == h for f, h in src['sha256'].items()))
    with tempfile.TemporaryDirectory() as tmp:
        for rel in list(locate.M818.values()) + ['SHA256SUMS']:
            os.makedirs(os.path.dirname(os.path.join(tmp, rel)) or tmp, exist_ok=True)
            shutil.copyfile(os.path.join(m818, rel), os.path.join(tmp, rel))
        claim('a copy of those files passes', bool(locate.m818_source(tmp)))
        p = os.path.join(tmp, locate.M818['arm_b'])
        raw = open(p, 'rb').read()
        open(p, 'wb').write(raw.replace(b'"located": true', b'"located": false', 1))
        claim('ARM_B.json changed by one field refuses', refuses(locate.m818_source, tmp, want="differs from M8.18's"))
        open(p, 'wb').write(raw)
        with open(os.path.join(tmp, 'SHA256SUMS'), 'a', encoding='utf-8') as f:
            f.write('0' * 64 + '  run/out/extra.json\n')
        claim('a SHA256SUMS other than the pinned one refuses', refuses(locate.m818_source, tmp, want='not the pinned one'))
    a = src['arm_b']
    claim("the record's comparison: ARM_B.json against itself, no difference", lib.differences(a, a) == [])
    m = copy.deepcopy(a)
    m['bisection']['24']['midpoints'][3]['from_lower']['nL'] = 99
    d = lib.differences(m, a)
    claim(f'one midpoint field changed: one difference, named ({d[:1]})', len(d) == 1 and 'midpoints[3]/from_lower/nL' in d[0])
    m = copy.deepcopy(a)
    m['bisection']['24']['midpoints'][3]['from_lower']['point']['seconds'] = 1e9
    claim('a timing changed: no difference', lib.differences(m, a) == [])
    sol = src['solutions']
    claim(f"the solutions' comparison: arm_b_solutions.npz against itself, {len(sol)} arrays, none unequal",
          locate.same_arrays(sol, sol) == [] and len(sol) == 146)
    m = {k: v.copy() for k, v in sol.items()}
    key0 = sorted(m)[0]
    m[key0].flat[0] += 1
    claim(f'one entry changed: that array named ({key0})', locate.same_arrays(m, sol) == [key0])
    mine = census.roundtrip(cs.serialize('T4/R5', dict(cs.CASES['T4/R5'], points=lib.path_points('T4/R5'),
                                                       cutoffs=list(lib.ARM_B['cutoffs']))))
    ch_b = next(c for c in src['census']['rows']['T4/R5']['changes'] if c['kind'] == 'type')
    claim("T4/R5's case here is M8.18's frozen one, and M8.17's bracket is Arm B's",
          lib.differences(mine, src['frozen']['cases']['T4/R5']) == [] and
          (lib.key(ch_b['lo']), lib.key(ch_b['hi'])) == tuple(map(lib.key, lib.BRACKET_B)))
    pt = lib.load_json(os.path.join(out, 'T4_R4_N24_read.json'))['points'][lib.key(W4[8])]
    stripped = locate.as_m818(pt)
    claim('as_m818 sets aside the new fields alone', set(pt) - set(stripped) == set(jobs.NEW_FIELDS)
          and all(stripped[x] == pt[x] for x in stripped))

    print('6. The gates')
    with tempfile.TemporaryDirectory() as tmp:
        claim('T4/R4 refuses with no reproduction on record', locate.refusal(tmp) == 'the reproduction has no record')

        def put(passed, stop=None):
            os.makedirs(os.path.join(tmp, 'jobs'), exist_ok=True)
            jobs.write_json(os.path.join(tmp, locate.REPRO_FILE), dict(passed=passed, stop=stop, differences=[],
                                                                       unequal_arrays=[]))
            jobs.Job(tmp, locate.REPRO_JOB).complete([locate.REPRO_FILE])
        put(True)
        claim('a passing reproduction on record: no refusal', locate.refusal(tmp) is None)
        plan = runner.plan('locate', [], tmp)
        claim(f'the runner then plans T4/R4: {plan}', plan == [(locate.JOB, ['locate'], 8.0)])
        put(False, 'a recomputed point does not reproduce: eps = 2')
        claim('a failed reproduction refuses, naming its stop', 'eps = 2' in (locate.refusal(tmp) or ''))
        claim('and the runner refuses it', refuses(runner.plan, 'locate', [], tmp, want='did not pass'))
        put(True)
        with open(os.path.join(tmp, locate.REPRO_FILE), 'a', encoding='utf-8') as f:
            f.write(' ')
        claim('a reproduction file changed after its job logged it refuses', 'does not check' in (locate.refusal(tmp) or ''))
        os.remove(os.path.join(tmp, locate.REPRO_FILE))
        claim('a reproduction file missing refuses', 'does not check' in (locate.refusal(tmp) or ''))
    with tempfile.TemporaryDirectory() as tmp:
        claim('the runner refuses the reproduction with no --source', refuses(runner.plan, 'locate', [], tmp, want='--source'))
        plan = runner.plan('locate', ['--source', m818], tmp)
        claim('and plans it first, from --source', plan == [(locate.REPRO_JOB, ['locate_repro', os.path.abspath(m818)], 5.3)])
        for kind, extra in (('locate_repro', [m818]), ('locate', [])):
            code, text = run([JOBS, tmp, kind, *extra])
            claim(f'jobs.py {kind} with no note refuses', code != 0 and 'no read of this computation before the dated note' in text)
        note = subprocess.run(['git', '-C', repo, 'log', '-1', '--format=%H', '--grep=the dated note before any read',
                               'origin/main'], capture_output=True, text=True, check=True).stdout.strip()
        code, text = run([JOBS, tmp, 'locate', '--note', note, '--repo', repo])
        claim(f"jobs.py locate with the reads' note, {note[:8]}, whose page names another pin, refuses",
              code != 0 and 'does not name the manifest pin' in text)
        code, text = run([RUNNER, tmp, 'locate', '--source', m818])
        claim('the runner refuses a launch with no note', code != 0 and 'reads need --note and --repo' in text
              and not os.path.exists(os.path.join(tmp, 'RUNLOG.json')))

    print('7. A failed reproduction exits nonzero, through the note gate')
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
        out2 = os.path.join(tmp, 'out')
        os.makedirs(os.path.join(out2, 'jobs'))

        def put2(passed):
            jobs.write_json(os.path.join(out2, locate.REPRO_FILE), dict(passed=passed, stop=None if passed else 'a stop',
                                                                        differences=[], unequal_arrays=[]))
            jobs.Job(out2, locate.REPRO_JOB).complete([locate.REPRO_FILE])
        put2(False)
        code, text = run([JOBS, out2, 'locate_repro', m818, '--note', commit, '--repo', fake])
        claim('a reproduction on record that did not pass exits nonzero, naming its stop, its record standing',
              code != 0 and 'did not pass: a stop; its record stands, and T4/R4 is not read' in text
              and os.path.exists(os.path.join(out2, 'jobs', locate.REPRO_JOB + '.json')))
        put2(True)
        code, text = run([JOBS, out2, 'locate_repro', m818, '--note', commit, '--repo', fake])
        claim('a passing one exits zero', code == 0)
    print('PASS' if ok else 'FAIL')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
