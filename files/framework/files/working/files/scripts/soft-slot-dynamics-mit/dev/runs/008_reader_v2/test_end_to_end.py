#!/usr/bin/env python3
"""The whole read side on data whose answer is on file: M8.18's stored control solutions at N = 24, 32 and 40, read again
by this tree's code, through jobs.py's reread, identity and reading. Nothing new is read and nothing is solved, so no note
is needed for the reads themselves; identity and reading go through note_gate, here on a throwaway repository whose
census page names the pin.

It asks five things:
  1. every read reproduces M8.18's record, field for field, timings and the new fields aside;
  2. the as-built reading of every point equals M8.18's, with the reading beside it and both identities;
  3. the changed reading is converged at all 24, with the type and indices on the record, and it differs from the as-built
     one at exactly P5 and C3R/R4 at 0.25;
  4. B's flag clears the one record holding n(D)'s line, read from the record's own call, not assumed;
  5. P5's pair at 0.25 reads, at every cutoff, the eigenvalues M8.18's diagnostic measured (dev/runs/019_gate_cause/
     pair_gap.out in its folder), in the reading's own row.

Usage: runner.py OUT rereads --source M818_OUT, then test_end_to_end.py OUT M818_OUT
"""
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
import census_lib as lib  # noqa: E402
import driver as dr  # noqa: E402
import grid  # noqa: E402
import jobs  # noqa: E402

JOBS = os.path.join(ROOT, 'run', 'jobs.py')
PAIR = {'24': (4.020284391477, 4.020295736541), '32': (4.020284391423, 4.020295736569), '40': (4.020284391423, 4.020295736569)}


def main():
    out, m818 = sys.argv[1:3]
    fails = []
    tmp = tempfile.mkdtemp(prefix='mit_e2e_')
    fake = os.path.join(tmp, 'repo')
    subprocess.run(['git', 'init', '-q', fake], check=True)
    page = os.path.join(fake, jobs.NOTE_PAGE)
    os.makedirs(os.path.dirname(page))
    with open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8') as f:
        pin = f.read().strip()
    with open(page, 'w', encoding='utf-8') as f:
        f.write(f'names {pin}\n')
    git = lambda *a: subprocess.run(['git', '-C', fake, '-c', 'user.name=t', '-c', 'user.email=t@t', *a], check=True,  # noqa: E731
                                    capture_output=True, text=True).stdout.strip()
    git('add', '.')
    git('commit', '-q', '-m', 'note')
    git('update-ref', 'refs/remotes/origin/main', 'HEAD')
    note = ['--note', git('rev-parse', 'HEAD'), '--repo', fake]
    # 1. the rereads
    total = diffs = 0
    for tag, name in grid.CONTROLS.items():
        for N in grid.LADDER:
            with open(os.path.join(out, f'reread_{tag}_N{N}.json'), encoding='utf-8') as f:
                rec = json.load(f)
            for k, r in rec.items():
                total += 1
                diffs += len(r['differences'])
                if r['differences']:
                    fails.append(f"{tag} N = {N} {k}: {r['differences'][0]}")
                if changedline(r) and not r['b_resolved']:
                    fails.append(f'{tag} N = {N} {k}: B did not clear the line')
            base = f'{dr.safe(name)}_N{N}'
            for ext in ('npz', 'json'):
                shutil.copy(os.path.join(m818, f'{base}.{ext}'), os.path.join(out, f'{tag}_N{N}.{ext}'))
            jobs.Job(out, f'path_{tag}_N{N}').complete([f'{tag}_N{N}.npz', f'{tag}_N{N}.json'])
    print(f'{total} points read again; {diffs} differences from M8.18', flush=True)
    # 2 to 4: the identities and the readings, through note_gate
    moved, conv, lifted = set(), 0, 0
    for tag, name in grid.CONTROLS.items():
        for a, b in zip(grid.LADDER, grid.LADDER[1:]):
            subprocess.run([sys.executable, '-I', '-B', JOBS, out, 'identity', tag, str(a), str(b), *note], check=True, cwd=ROOT)
        subprocess.run([sys.executable, '-I', '-B', JOBS, out, 'reading', tag, *note], check=True, cwd=ROOT)
        mine, theirs = lib.load_json(os.path.join(out, f'{tag}.json')), lib.load_json(os.path.join(m818, f'{dr.safe(name)}.json'))
        for field in ('readings', 'beside', 'identity'):
            d = lib.differences(mine[field], theirs[field], ignore=frozenset())
            if d:
                fails.append(f'{tag} {field}: {d[0]}')
        for k, rd in mine['changed'].items():
            hi = mine['cutoffs']['40']['points'][k]['record']
            good = rd['verdict'] == 'converged' and rd['type'] == mine['case']['type'] and \
                [hi['nL'], hi['nD'], hi['K']] == mine['case']['idx']
            conv += good
            if not good:
                fails.append(f'{tag} {k}: changed {rd["verdict"]}: {rd["reasons"][:1]}')
            if rd['verdict'] != mine['readings'][k]['verdict']:
                moved.add((name, k))
            b = mine['both'][k]
            if not b['changed'].get('classified'):
                fails.append(f"{tag} {k}: not classified under the change: {b['changed'].get('causes')}")
            lifted += b['as_built'] != b['changed']
        print(f"{tag}: as-built reading, reading beside it and both identities equal M8.18's", flush=True)
    # 5. the pair's members, in the row
    mine = lib.load_json(os.path.join(out, 'ctl_P5.json'))
    row = [r for r in mine['changed']['0.25']['rows'] if r.get('kind') == 'set' and 'levels' in r
           and any(abs(z[1] - 4.02029) < 1e-4 for z in r['levels'][0])]
    if len(row) != 1:
        fails.append(f"P5 at 0.25: {len(row)} rows hold the pair")
    else:
        for N, lev in zip(('40', '32', '24'), row[0]['levels']):
            got = sorted(z[1] for z in lev if abs(z[1] - 4.02029) < 1e-4)
            print(f'P5 at 0.25, the pair at N = {N}: {got[0]:.12f}, {got[1]:.12f}, gap {got[1] - got[0]:.4e}', flush=True)
            if any(abs(a - b) > 1e-12 for a, b in zip(got, PAIR[N])):
                fails.append(f'P5 at 0.25, N = {N}: {got} against {PAIR[N]}')
        print(f"its row: d1 {row[0]['d1']:.3e}, d2 {row[0]['d2']:.3e}, U {row[0]['U']:.3e}, d {row[0]['d']:.3e}, ok {row[0]['ok']}", flush=True)
    print(f'changed: {conv} of 24 converged, with the type and indices on the record; moved {sorted(moved)}')
    print(f'classified differently at {lifted} points')
    if moved != {('P5', '0.25'), ('C3R/R4', '0.25')}:
        fails.append(f'the change moved {sorted(moved)}')
    if conv != 24:
        fails.append(f'{conv} of 24 converged')
    shutil.rmtree(tmp)
    print('\n'.join(fails[:12]) if fails else 'no failure')
    print('PASS' if not fails else 'FAIL')
    raise SystemExit(1 if fails else 0)


def changedline(r):
    return any('n(D)' in u and 'gray zone' in u for u in r['unresolved'])


if __name__ == '__main__':
    main()
