#!/usr/bin/env python3
"""The jobs' own guards, on real solves at N = 24 and on nothing. Outputs go to a temporary folder.

  1. A killed path resumes at its next point, and ends equal to M8.18's stored path: a resumed path is the path run
     through. SIGKILL lands between two accepted points, as a session restart would.
  2. A checkpoint that is not a prefix of the path refuses.
  3. The note gate: no commit, a commit off origin/main, and a commit whose census page lacks the pin each refuse, and a
     read through jobs.py refuses with no note. A commit whose page names the pin passes.
  4. A stored solution whose file changed refuses, and one whose lam differs from its solve fields refuses.
  5. A read runs inside no withheld block, and a solve cannot read: Cutoff.solve under checks.withheld refuses a record.
  6. changed.lifted: only n(D)'s line, only where B's flag clears it.
  7. changed.capture leaves the record's own call unchanged, and restores what it patched.
  8. A read through the note gate, killed after its first point, resumes, and ends equal to M8.18's record.

Usage: test_jobs.py M818_OUT MIT_REPO
"""
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
from instrument import linear as ln  # noqa: E402
import checks as ck  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import jobs  # noqa: E402

JOBS = os.path.join(ROOT, 'run', 'jobs.py')
ok = True


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
    p = subprocess.Popen([sys.executable, '-I', '-B', '-u', JOBS, out, 'read', 'ctl_C2b', '24', *note], stdout=subprocess.PIPE,
                         text=True, cwd=ROOT)
    for line in p.stdout:
        if ': read,' in line:
            p.send_signal(signal.SIGKILL)
            break
    p.wait()
    claim('the read was killed after its first point', p.returncode == -signal.SIGKILL)
    r = subprocess.run([sys.executable, '-I', '-B', '-u', JOBS, out, 'read', 'ctl_C2b', '24', *note], capture_output=True,
                       text=True, cwd=ROOT)
    claim('the second launch finished it', r.returncode == 0 and '0.25: read' not in r.stdout and '2: read' in r.stdout)
    mine = json.load(open(os.path.join(out, 'ctl_C2b_N24_read.json'), encoding='utf-8'))
    theirs = json.load(open(os.path.join(m818, 'C2b_N24_read.json'), encoding='utf-8'))
    d = lib.differences(mine, theirs, ignore=lib.TIMINGS | jobs.NEW_FIELDS | lib.NOT_COMPUTED)
    claim(f'the resumed read equals M8.18\'s record: {len(d)} differences', not d)
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
    shutil.rmtree(tmp)
    print('PASS' if ok else 'FAIL')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
