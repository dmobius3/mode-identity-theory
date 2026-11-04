#!/usr/bin/env python3
"""The jobs' own guards, on real solves at N = 24 and on nothing. Outputs go to a temporary folder.

  1. A killed path resumes at its next point, and ends equal to M8.18's stored path: a resumed path is the path run
     through. SIGKILL lands between two accepted points, as a session restart would.
  2. A checkpoint that is not a prefix of the path refuses.
  3. The note gate: no commit, a commit off origin/main, and a commit whose census page lacks the pin each refuse, and a
     read through jobs.py refuses with no note. A commit whose page names the pin passes.
  4. A stored solution whose file changed refuses, and one whose lam differs from its solve fields refuses. A path solved
     under a manifest not among the solve pins refuses, and the same path passes once its record names the solve pin.
  5. A read runs inside no withheld block, and a solve cannot read: Cutoff.solve under checks.withheld refuses a record.
  6. changed.lifted: only n(D)'s line, only where B's flag clears it.
  7. changed.capture leaves the record's own call unchanged, and restores what it patched.
  8. A read through the note gate, killed after its first point, resumes, and ends equal to M8.18's record, and every
     point holds its linked groups' members.
  9. reread refuses a row, a source whose SHA256SUMS is not M8.18's, and a file that differs from it.
 10. No row is read before the fresh controls pass: with no record, a miss, other marks or a changed file, the gate
     refuses, in jobs.py and in the runner, and a default launch takes the fresh controls alone. The check is named by its
     marks: a pass file other than the one its job logged refuses, a miss stays on record when the marks change, the new
     marks need a pass of their own, and `fresh` is planned only once every fresh reading is complete, so an early launch
     counts no start.
 11. A launch of reads with no note refuses before it counts a start.
 12. changed.identity: an Elliptic point whose flag fires at N = 40 alone keeps its branch under the changed reading.

The test solves its path under this tree, whose pin is not a solve pin, so its reads run jobs.py with this tree's pin added
to the solve pins (jobs_here); item 4 tests the gate itself.

Usage: test_jobs.py M818_OUT MIT_REPO
"""
import copy
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import devtools  # noqa: E402
from instrument import linear as ln  # noqa: E402
import checks as ck  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import fresh  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402
import runner  # noqa: E402

JOBS = os.path.join(ROOT, 'run', 'jobs.py')
WIDENED = ('import sys; sys.path.insert(0, sys.argv.pop(1)); import jobs; '
           'jobs.SOLVE_PINS = jobs.SOLVE_PINS | {sys.argv.pop(1)}; jobs.main()')
ok = True


def jobs_here(*args):
    """jobs.py's command line, with this tree's own pin added to the solve pins: the test's path is solved under it."""
    return [sys.executable, '-I', '-B', '-u', '-c', WIDENED, os.path.join(ROOT, 'run'), devtools.manifest()[1], *args]


def claim(text, good):
    global ok
    ok &= bool(good)
    print(f"{'ok  ' if good else 'FAIL'} {text}", flush=True)


def refuses(f, *a, kind=Exception):
    try:
        f(*a)
    except kind as e:
        return str(e)
    return None


def main():
    m818, repo = sys.argv[1:3]
    tmp = tempfile.mkdtemp(prefix='mit_jobs_')
    out = os.path.join(tmp, 'out')
    os.makedirs(out)
    # 1. kill and resume
    p = subprocess.Popen([sys.executable, '-I', '-B', '-u', JOBS, out, 'path', 'ctl_C2b', '24'], stdout=subprocess.PIPE,
                         text=True, cwd=ROOT)
    seen = 0
    for line in p.stdout:
        seen += line.strip().endswith(' s') and 'accepted' in line
        if seen == 2:
            p.send_signal(signal.SIGKILL)
            break
    p.wait()
    claim('the job was killed after 2 of 4 points', p.returncode == -signal.SIGKILL and seen == 2)
    claim('its checkpoint holds them', os.path.exists(os.path.join(out, 'ctl_C2b_N24.partial.npz')))
    r = subprocess.run([sys.executable, '-I', '-B', '-u', JOBS, out, 'path', 'ctl_C2b', '24'], capture_output=True,
                       text=True, cwd=ROOT)
    claim('the second launch resumed', 'resuming at 0.5, 2 of 4 points held' in r.stdout and r.returncode == 0)
    c = subprocess.run([sys.executable, '-I', '-B', os.path.join(HERE, 'compare_controls.py'), out, m818],
                       capture_output=True, text=True, cwd=ROOT)
    claim(f'the resumed path equals the stored one: {c.stdout.strip().splitlines()[-1]}', c.returncode == 0)
    claim('no checkpoint is left', not os.path.exists(os.path.join(out, 'ctl_C2b_N24.partial.npz')))
    # 2. a checkpoint that is no prefix
    out2 = os.path.join(tmp, 'out2')
    os.makedirs(out2)
    for ext in ('npz', 'json'):
        shutil.copy(os.path.join(out, f'ctl_C2b_N24.{ext}'), os.path.join(out2, f'ctl_C2b_N24.partial.{ext}'))
    meta = json.load(open(os.path.join(out2, 'ctl_C2b_N24.partial.json'), encoding='utf-8'))
    meta['points'].pop('0.25')
    json.dump(meta, open(os.path.join(out2, 'ctl_C2b_N24.partial.json'), 'w', encoding='utf-8'))
    r = subprocess.run([sys.executable, '-I', '-B', JOBS, out2, 'path', 'ctl_C2b', '24'], capture_output=True, text=True,
                       cwd=ROOT)
    claim('a checkpoint that is not a prefix refuses', r.returncode != 0 and 'not a prefix' in r.stderr)
    # 3. the note gate
    claim('no commit refuses', refuses(jobs.note_gate, None, None, kind=PermissionError))
    head = subprocess.run(['git', '-C', repo, 'rev-parse', 'origin/main'], capture_output=True, text=True).stdout.strip()
    why = refuses(jobs.note_gate, head, repo, kind=PermissionError)
    claim(f'a commit whose page lacks the pin refuses: {why}', why and 'does not name the manifest pin' in why)
    why = refuses(jobs.note_gate, '0' * 40, repo, kind=PermissionError)
    claim('a commit off origin/main refuses', why and 'not on origin/main' in why)
    r = subprocess.run([sys.executable, '-I', '-B', JOBS, out, 'read', 'ctl_C2b', '24'], capture_output=True, text=True,
                       cwd=ROOT)
    claim('a read through jobs.py with no note refuses', r.returncode != 0 and 'no read of this computation' in r.stderr)
    r = subprocess.run([sys.executable, '-I', '-B', JOBS, out, 'reading', 'ctl_C2b'], capture_output=True, text=True, cwd=ROOT)
    claim('a reading with no note refuses', r.returncode != 0 and 'no read of this computation' in r.stderr)
    fake = os.path.join(tmp, 'repo')
    subprocess.run(['git', 'init', '-q', fake], check=True)
    page = os.path.join(fake, jobs.NOTE_PAGE)
    os.makedirs(os.path.dirname(page))
    with open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8') as f:
        pin = f.read().strip()
    with open(page, 'w', encoding='utf-8') as f:
        f.write(f'the note names {pin}\n')
    git = lambda *a: subprocess.run(['git', '-C', fake, '-c', 'user.name=t', '-c', 'user.email=t@t', *a], check=True,  # noqa: E731
                                    capture_output=True, text=True).stdout.strip()
    git('add', '.')
    git('commit', '-q', '-m', 'note')
    git('update-ref', 'refs/remotes/origin/main', 'HEAD')
    claim('a commit whose page names the pin passes', jobs.note_gate(git('rev-parse', 'HEAD'), fake) is None)
    # 8. a read, killed and resumed, through the gate
    note = ['--note', git('rev-parse', 'HEAD'), '--repo', fake]
    p = subprocess.Popen(jobs_here(out, 'read', 'ctl_C2b', '24', *note), stdout=subprocess.PIPE, text=True, cwd=ROOT)
    for line in p.stdout:
        if ': read,' in line:
            p.send_signal(signal.SIGKILL)
            break
    p.wait()
    claim('the read was killed after its first point', p.returncode == -signal.SIGKILL)
    r = subprocess.run(jobs_here(out, 'read', 'ctl_C2b', '24', *note), capture_output=True, text=True, cwd=ROOT)
    claim('the second launch finished it', r.returncode == 0 and '0.25: read' not in r.stdout and '2: read' in r.stdout)
    mine = json.load(open(os.path.join(out, 'ctl_C2b_N24_read.json'), encoding='utf-8'))
    theirs = json.load(open(os.path.join(m818, 'C2b_N24_read.json'), encoding='utf-8'))
    d = lib.differences(mine, theirs, ignore=lib.TIMINGS | jobs.NEW_FIELDS | lib.NOT_COMPUTED)
    claim(f'the resumed read equals M8.18\'s record: {len(d)} differences', not d)
    claim('every read point holds its linked groups, by the fields the rule asks', all(
        isinstance(p.get('members'), list) and all(set(m) == {'idx', 'z'} and len(m['idx']) == len(m['z']) > 1 for m in p['members'])
        for p in mine['points'].values()))
    # 4. the solve-state gate
    why = refuses(jobs.stored, out, 'ctl_C2b', 32, kind=PermissionError)
    claim('a path with no completed job refuses', why and 'no completed job' in why)
    shutil.copytree(out, os.path.join(tmp, 'out3'))
    with open(os.path.join(tmp, 'out3', 'ctl_C2b_N24.json'), 'a', encoding='utf-8') as f:
        f.write(' ')
    why = refuses(jobs.stored, os.path.join(tmp, 'out3'), 'ctl_C2b', 24, kind=PermissionError)
    claim('a stored file that changed refuses', why and 'differs from the SHA-256' in why)
    meta = json.load(open(os.path.join(out, 'ctl_C2b_N24.json'), encoding='utf-8'))
    meta['points']['0.5']['lam'] += 1e-12
    os.makedirs(os.path.join(tmp, 'out4'))
    shutil.copy(os.path.join(out, 'ctl_C2b_N24.npz'), os.path.join(tmp, 'out4'))
    json.dump(meta, open(os.path.join(tmp, 'out4', 'ctl_C2b_N24.json'), 'w', encoding='utf-8'))
    why = refuses(jobs.load_path, os.path.join(tmp, 'out4', 'ctl_C2b_N24'), kind=RuntimeError)
    claim('a stored lam that differs from its fields refuses', why and 'differs from its solve fields' in why)
    why = refuses(jobs.stored, out, 'ctl_C2b', 24, kind=PermissionError)
    claim('a path solved under this tree, whose pin is not a solve pin, refuses', why and 'not a solve pin' in why)
    out5 = os.path.join(tmp, 'out5')
    os.makedirs(os.path.join(out5, 'jobs'))
    for ext in ('npz', 'json'):
        shutil.copy(os.path.join(out, f'ctl_C2b_N24.{ext}'), out5)
    rec = json.load(open(os.path.join(out, 'jobs', 'path_ctl_C2b_N24.json'), encoding='utf-8'))
    with open(os.path.join(out5, 'jobs', 'path_ctl_C2b_N24.json'), 'w', encoding='utf-8') as f:
        json.dump(dict(rec, manifest=sorted(jobs.SOLVE_PINS)[0]), f)
    claim('the same path, its record naming the solve pin, passes', len(jobs.stored(out5, 'ctl_C2b', 24)[1]) == 4)
    # 5. a solve cannot read
    with ck.withheld('test'):
        claim('inside withheld a record refuses', refuses(ln.record, None, None, None, None, None, kind=ck.Withheld))
        claim('inside withheld inertia refuses', refuses(ln.inertia, np.eye(2), kind=ck.Withheld))
    # 6. lifted
    s = dict(type='Unresolved', unresolved=[changed.ND_LINE])
    claim('B lifts the line and types a record that held nothing else', changed.lifted(s, True)['type'] == 'Elliptic')
    claim('a flag that does not clear it leaves the record', changed.lifted(s, False) is s)
    s2 = dict(type='Unresolved', unresolved=[changed.ND_LINE, 'another'])
    r2 = changed.lifted(s2, True)
    claim('another item keeps it Unresolved', r2['type'] == 'Unresolved' and r2['unresolved'] == ['another'])
    s3 = dict(type='Hyperbolic', unresolved=[changed.ND_LINE])
    claim('a Hyperbolic record keeps its type', changed.lifted(s3, True)['type'] == 'Hyperbolic')
    # 7. capture
    M = np.diag([-0.016, 0.0, 0.5])
    before = ln.inertia, ck.spectrum_of_L
    with changed.capture() as held:
        got = ln.inertia(M, 1e-8, scale=1632.3)
        ck.spectrum_of_L(M)
    claim("capture leaves the record's call as built", got == before[0](M, 1e-8, scale=1632.3) and got[2] is False)
    claim("B's flag clears the same eigenvalue, the gate's case", held['b_resolved'] is True)
    claim('capture holds D and L', len(held['d_eigs']) == 3 and len(held['l_near']) == 3)
    claim('capture restores what it patched', (ln.inertia, ck.spectrum_of_L) == before)
    summ = changed.cv.summarize
    with changed.capture():
        inner = changed.cv.summarize
    claim('capture restores the summary', changed.cv.summarize is summ and inner is not summ)
    s4 = dict(groups=[dict(size=2, idx=[3, 4], c=[0.0, 1.0])])
    claim('a linked group with no members refuses', refuses(changed.with_members, s4, [], kind=KeyError) is not None)
    claim('its members go beside its centre, by its indices',
          changed.with_members(s4, [dict(idx=[3, 4], z=[[0.0, 0.9], [0.0, 1.1]])])['groups'][0]['members'][1] == [0.0, 1.1])
    # 9. reread's reach
    why = refuses(jobs.m818_files, m818, 'T1_R4', 32, kind=PermissionError)
    claim(f'reread refuses a row: {why}', why and 'M8.18 controls alone' in why)
    claim("M8.18's own files pass", jobs.m818_files(m818, 'ctl_C2b', 24) is None)
    fake5 = os.path.join(tmp, 'm5', 'run', 'out')
    os.makedirs(fake5)
    for ext in ('.npz', '.json', '_read.json'):
        shutil.copy(os.path.join(m818, 'C2b_N24' + ext), fake5)
    shutil.copy(os.path.join(m818, os.pardir, os.pardir, 'SHA256SUMS'), os.path.join(tmp, 'm5'))
    claim('a copy of its files passes', jobs.m818_files(fake5, 'ctl_C2b', 24) is None)
    with open(os.path.join(fake5, 'C2b_N24.json'), 'a', encoding='utf-8') as f:
        f.write(' ')
    why = refuses(jobs.m818_files, fake5, 'ctl_C2b', 24, kind=PermissionError)
    claim(f'a file that differs refuses: {why}', why and "differs from M8.18's SHA256SUMS" in why)
    with open(os.path.join(tmp, 'm5', 'SHA256SUMS'), 'a', encoding='utf-8') as f:
        f.write('\n')
    why = refuses(jobs.m818_files, fake5, 'ctl_C2b', 24, kind=PermissionError)
    claim(f'another SHA256SUMS refuses: {why}', why and 'not the pinned one' in why)
    # 10. the fresh gate
    g = os.path.join(tmp, 'gate')
    os.makedirs(os.path.join(g, 'jobs'))
    gate = lambda: subprocess.run([sys.executable, '-I', '-B', JOBS, g, 'read', 'T1_R4', '24', *note], capture_output=True,  # noqa: E731
                                  text=True, cwd=ROOT)
    r = gate()
    claim('a row with no pass on record refuses', r.returncode != 0 and 'no pass on record' in r.stderr)
    claim('a default launch takes the fresh controls alone', sorted({j[1][1] for j in runner.plan('reads', [], g)}) == sorted(grid.FRESH))
    try:
        runner.plan('reads', ['--tags', 'T1_R4'], g)
        named = False
    except SystemExit as e:
        named = 'no row is read' in str(e)
    claim('a launch naming a row refuses', named)
    r = subprocess.run([sys.executable, '-I', '-B', os.path.join(ROOT, 'run', 'runner.py'), g, 'fresh', *note],
                       capture_output=True, text=True, cwd=ROOT)
    log = json.load(open(os.path.join(g, 'RUNLOG.json'), encoding='utf-8'))
    claim('a fresh launch before the fresh readings waits, and counts no start',
          r.returncode == 0 and 'the fresh check waits for the readings of' in r.stdout and not log['jobs'])
    for tag in grid.FRESH:
        with open(os.path.join(g, tag + '.json'), 'w', encoding='utf-8') as f:
            f.write('{}')
        jobs.write_json(os.path.join(g, 'jobs', f'reading_{tag}.json'), dict(job=f'reading_{tag}'))
    name, pass_file = fresh.names()
    claim('once they are complete it is planned, named by the marks', runner.plan('fresh', [], g) == [(name, ['fresh'], 0.01)])
    rec = dict(results={'fresh_P5 0.24': []}, passed=True, marks=fresh.marks_now(), files=fresh.reading_files(g))

    def write(d):
        """A pass file for run/grid.py's marks, and its job's record logging the file's SHA-256."""
        job, pf = fresh.names()
        with open(os.path.join(g, pf), 'w', encoding='utf-8') as f:
            json.dump(d, f)
        jobs.write_json(os.path.join(g, 'jobs', job + '.json'), dict(job=job, files={pf: jobs.dr.sha(os.path.join(g, pf))}))
    write(dict(rec, results={'fresh_P5 0.24': ['K1 fails at N = 40']}, passed=False))
    r = gate()
    claim('a miss refuses, and names itself', r.returncode != 0 and 'K1 fails at N = 40' in r.stderr)
    write(dict(rec, marks=rec['marks'][:-1]))
    r = gate()
    claim('a pass for other marks refuses', r.returncode != 0 and "not for run/grid.py's marks" in r.stderr)
    with open(os.path.join(g, 'fresh_P5.json'), 'a', encoding='utf-8') as f:
        f.write(' ')
    write(rec)
    r = gate()
    claim('a reading file that changed refuses', r.returncode != 0 and 'differs from the file the pass rests on' in r.stderr)
    rec['files'] = fresh.reading_files(g)
    write(rec)
    with open(os.path.join(g, pass_file), 'a', encoding='utf-8') as f:
        f.write(' ')
    r = gate()
    claim('a pass file other than the one its job logged refuses', r.returncode != 0 and 'differs from the SHA-256 its job logged' in r.stderr)
    write(rec)
    r = gate()
    claim('a pass opens the gate, and the read stops at its own next check', r.returncode != 0 and 'no completed job path_T1_R4_N24' in r.stderr)
    claim('a default launch then takes the rows too', sorted({j[1][1] for j in runner.plan('reads', [], g)}) == sorted(list(grid.FRESH) + list(grid.ROWS)))
    write(dict(rec, results={'fresh_P5 0.24': ['K1 fails at N = 40']}, passed=False))
    missed, marks = fresh.names(), dict(grid.PASS_MARKS)
    grid.PASS_MARKS[('fresh_P5', 0.26)] = ('Unresolved', 'converged', 'link')     # as a dated commit's new mark would
    claim('new marks have no pass of their own until their check runs',
          fresh.names() != missed and fresh.refusal(g) == 'the fresh controls have no pass on record')
    write(dict(rec, marks=fresh.marks_now()))
    claim('their pass opens the gate', fresh.refusal(g) is None)
    claim('the miss stays on record beside it', os.path.exists(os.path.join(g, 'jobs', missed[0] + '.json'))
          and json.load(open(os.path.join(g, missed[1]), encoding='utf-8'))['passed'] is False)
    grid.PASS_MARKS.clear()
    grid.PASS_MARKS.update(marks)
    claim('under the old marks the miss still refuses', 'K1 fails at N = 40' in (fresh.refusal(g) or ''))
    # 11. a launch with no note
    o2 = os.path.join(tmp, 'o2')
    r = subprocess.run([sys.executable, '-I', '-B', os.path.join(ROOT, 'run', 'runner.py'), o2, 'reads'], capture_output=True,
                       text=True, cwd=ROOT)
    claim('reads with no note refuse at the launch', r.returncode != 0 and 'reads need --note' in r.stderr and not os.path.exists(o2))
    # 12. branch identity under B
    d8 = json.load(open(os.path.join(m818, 'C2b.json'), encoding='utf-8'))
    pts = {N: copy.deepcopy(d8['cutoffs'][str(N)]['points']['0.25']) for N in (32, 40)}
    for N in pts:
        pts[N]['b_resolved'] = True
    pts[40]['record'].update(unresolved=[changed.ND_LINE], type='Unresolved')
    idn = dict(aligned_distance=1e-6, same_record=False, kept=False)
    got = changed.identity(idn, pts, (32, 40))
    claim('the flag at N = 40 alone keeps the branch under B', got['same_record'] and got['kept'])
    pts[40]['b_resolved'] = False
    claim('a flag B does not clear leaves it as it was', not changed.identity(idn, pts, (32, 40))['kept'])
    claim('no record leaves it as it was', changed.identity(idn, {32: pts[32], 40: None}, (32, 40)) is idn)
    shutil.rmtree(tmp)
    print('PASS' if ok else 'FAIL')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
