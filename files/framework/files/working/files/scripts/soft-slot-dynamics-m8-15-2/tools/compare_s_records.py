"""Bench check beside RESULT_5: every S plant run through M8.15.1's frozen locator and through the locator v2, on the mock,
and the full records compared once REGISTER_5 § 1 item 4's fields and item 5's trigger are set aside. Only S10 may
differ (REGISTER_5 § 2). Each locator runs in its own process, so neither imports the other's modules.

  python3 compare_s_records.py SCRIPTS          SCRIPTS holds both folders, soft-slot-dynamics-m8-15x-target1 and
                                                soft-slot-dynamics-m8-15-2, beside the instrument
Exit 1 on any difference outside S10, or if S10 shows none. An arm: one S record perturbed in a copy must be caught."""
import os, sys, json, subprocess

NEW_FIELDS = {'start', 'nL_ends', 'clean_ends', 'midpoints', 'branch_step', 'branch_points', 'continuity',
              'identity_cosines_genuine', 'identity_cosines_structural', 'clause3_trigger'}
DUMP = r'''
import os, sys, json
folder = {folder!r}
sys.path.insert(0, os.path.join(folder, 'tests'))
sys.path.insert(0, folder)
import mock, synthetic
tests = getattr(synthetic, 'S_TESTS', None) or synthetic.TESTS
out = {{}}
for name, plant, expect, arm in tests:
    out[name] = mock.run(mock.Plant(**plant))
print(json.dumps(out, default=str))
'''


def strip(x):
    if isinstance(x, dict):
        return {k: strip(v) for k, v in x.items() if k not in NEW_FIELDS}
    if isinstance(x, list):
        return [strip(v) for v in x]
    return x


def records(folder):
    r = subprocess.run([sys.executable, '-B', '-c', DUMP.format(folder=folder)], capture_output=True, text=True, cwd=folder)
    if r.returncode != 0:
        raise SystemExit(f'{folder}: {r.stderr[-2000:]}')
    return {k: strip(v) for k, v in json.loads(r.stdout).items()}


def differing(old, new):
    return sorted(t for t in old if old[t] != new.get(t))


if __name__ == '__main__':
    scripts = sys.argv[1]
    old = records(os.path.join(scripts, 'soft-slot-dynamics-m8-15x-target1'))
    new = records(os.path.join(scripts, 'soft-slot-dynamics-m8-15-2'))
    d = differing(old, new)
    ok = sorted(old) == sorted(new) and d == ['S10']
    print(f'S records: {len(old)} from M8.15.1, {len(new)} from the locator v2; equal outside the new fields: '
          f'{len(old) - len(d)}; differing: {d}')
    # the arm: a copy of the new records with one number in S1's record perturbed must show S1 as differing
    arm = json.loads(json.dumps(new))
    arm['S1']['levels']['3']['steps'][0]['root'] += 1e-12
    caught = differing(old, arm) == ['S1', 'S10']
    print(f'arm (S1\'s level-3 root perturbed by 1e-12 in a copy): {"caught" if caught else "NOT caught"}')
    print('PASS' if ok and caught else 'FAIL')
    sys.exit(0 if ok and caught else 1)
