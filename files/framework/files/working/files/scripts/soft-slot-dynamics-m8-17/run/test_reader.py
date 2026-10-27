#!/usr/bin/env python3
"""Test 2: the reader, on M8.16.1's outputs, with no solve (M8.17's terms: THE TESTS BEFORE THE FREEZE, test 2).

Usage: test_reader.py

The whole test runs in a seedcheck process (devtools.require('seedcheck')), where every solver and record path of the
instrument refuses; claim 6 checks that they do. It reads M8.16.1's outputs and M8.15's records from reference/, as
tools/copy_from_mit.py placed them.

Claims, derived before the run:
  1. At every point M8.16.1 read on the nine rows, the convergence rule replayed on its stored summaries
     (checks.reading, with the highest cutoff's stored eigenvalues, lam and margin) equals the stored reading, field for
     field.
  2. At every such point, checks.k1 is applied at every cutoff, branch identity is taken from the stored identity
     record, and the classification on this instrument (census_lib.here) is computed. Its counts are printed.
  3. Combined with M8.15's adjudicated readings (census_lib.known), the classification reproduces M8.16.1's K6: at
     every point K6 marks 'agrees', the point is classified, by both instruments where K1 holds at every cutoff; at
     every point K6 marks 'unresolved', this instrument does not classify it; no point is a contradiction; and the
     counts are 79 points that M8.15 decided and M8.16.1 read, of which 11 are Unresolved on this instrument. T1's and
     T4's four samples are classified on this instrument, Elliptic.
  4. The 56 first-time readings, derived from the records alone (M8.15 left the point undecided and M8.16.1 holds no
     reading of it: unsolved, or withheld), with T3/R5's 16 set apart as inside M8.15.2's location, equal
     census_lib.NEW, point for point.
  5. The reader refuses every one of the 56, the four withheld points among them, T3/R5's withheld point, and points
     off the grid, as the locator's are: census_lib.known raises Sealed at each, before it reads a record.
  6. Sealing: in this tree, before the freeze, the instrument refuses each run row's seed (seeds.seed_state), the
     census driver refuses to start (census.frozen), and, in this process, linear.record, branches.continue_to and
     newton.solve refuse.
Arms, each of which must turn its claim red:
  A1. the slowest imaginary group's centre in one stored summary moved by 1e-9, in a copy of T3/R4's output at
      eps = 8, N = 32: claim 1 names the point.
  A2. census_lib.known with its sealed() check removed, in a temporary copy: claim 5 fails at the 50 points of T1 and
      T4 that M8.16.1 never solved.
  A3. a stored identity record set to kept = False at a point K6 marks 'agrees', in a copy: claim 3 fails there.
"""
import copy
import importlib.util
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools, basis, linear as ln, branches as br, newton  # noqa: E402
import checks as ck  # noqa: E402
import seeds as sd  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402

out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def read_points(theirs):
    """(row, eps) for every point M8.16.1 read on the nine rows."""
    return [(row, p['eps']) for row in lib.ROWS for p in theirs[row]['case']['points'] if p['read']]


def claim1(theirs):
    bad = []
    for row, e in read_points(theirs):
        pt = lib.at(theirs[row], e)
        pts = [pt['points'][N] for N in lib.CUTOFFS]
        if not all(q and 'summary' in q for q in pts):
            bad.append(f'{row} {e:g}: a cutoff lacks its summary')
            continue
        hi = pts[-1]
        mine = json.loads(json.dumps(ck.reading([q['summary'] for q in pts], hi['eig'], hi['lam'],
                                                hi['record']['margin'], lib.CUTOFFS[0]), default=float))
        d = lib.differences(mine, pt['reading'])
        if d:
            bad.append(f'{row} {e:g}: {d[:2]}')
    return bad


def classified(theirs, m815, lib_=lib):
    """Each read point's classification on this instrument and combined, with K6's status beside it."""
    rows = []
    for row, e in read_points(theirs):
        pt = lib_.at(theirs[row], e)
        h = lib_.here(pt, theirs[row]['case'])
        k1s = [ck.k1(pt['points'][N], theirs[row]['case']) for N in lib_.CUTOFFS]
        c = lib_.known(row, e, theirs[row], m815.get(row), theirs[row]['case'])
        k6 = next((r['status'] for r in theirs[row]['checks'].get('rows', []) if abs(r['eps'] - e) < 1e-9), None)
        rows.append(dict(row=row, eps=e, here=h, k1=k1s, combined=c, k6=k6))
    return rows


def claim3(rows):
    bad = []
    for r in rows:
        c, where = r['combined'], f"{r['row']} {r['eps']:g}"
        if c.get('contradiction'):
            bad.append(f'{where}: a contradiction')
        if r['k6'] == 'agrees':
            want = 'both' if all(r['k1']) else "M8.15's"
            if not c['classified'] or c['instrument'] != want:
                bad.append(f"{where}: K6 agrees; classified {c['classified']} by {c.get('instrument')}, not {want}")
        elif r['k6'] == 'unresolved' and r['here']['classified']:
            bad.append(f'{where}: K6 unresolved, and this instrument classifies it')
        elif r['k6'] is None and not (r['here']['classified'] and r['here']['type'] == 'Elliptic'):
            bad.append(f'{where}: a sample not classified Elliptic on this instrument')
    decided = sum(r['k6'] in ('agrees', 'unresolved', 'disagrees') for r in rows)
    unres = sum(r['k6'] == 'unresolved' for r in rows)
    if (decided, unres) != (79, 11):
        bad.append(f'{decided} points decided and read, {unres} Unresolved, not 79 and 11')
    return bad, decided, unres


def derived_new(theirs, m815):
    """The first-time readings from the records alone."""
    out_ = {}
    for row in lib.ROWS:
        tp = {lib.key(p['eps']): p['read'] for p in theirs[row]['case']['points']}
        for e in lib.WINDOWS[lib.SLOT[row]]:
            t = lib.there(m815.get(row), e)
            if not t['decided'] and not tp.get(lib.key(e)):
                out_.setdefault(row, []).append(e)
    return out_


def claim5(theirs, m815, lib_=lib):
    """Every refusal the reader owes: (refused, not refused)."""
    asked = [(r, e) for r, es in lib.NEW.items() for e in es] + [('T3/R5', 16.0)]
    for row in lib.ROWS:                         # off the grid: each interval's midpoint, as a locator's first
        w = lib.WINDOWS[lib.SLOT[row]]
        asked += [(row, (a + b) / 2) for a, b in zip(w, w[1:])]
    refused, not_refused = 0, []
    for row, e in asked:
        try:
            lib_.known(row, e, theirs[row], m815.get(row), theirs[row]['case'])
            not_refused.append(f'{row} {e:g}')
        except lib_.Sealed:
            refused += 1
    return refused, not_refused, len(asked)


def load_copy(src_text, name, tmp):
    p = os.path.join(tmp, f'{name}.py')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(src_text)
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    devtools.require('seedcheck')
    theirs, m815 = lib.theirs_records(), lib.m815_records()
    say('Test 2, the reader, on M8.16.1\'s outputs, with no solve, in a seedcheck process.')
    fails = 0
    bad1 = claim1(theirs)
    n_read = len(read_points(theirs))
    say(f"1. {'PASS' if not bad1 else 'FAIL'}: the rule replayed on the stored summaries equals the stored reading at "
        f"{n_read - len(bad1)} of {n_read} read points" + ''.join(f'\n      {b}' for b in bad1[:8]))
    fails += bool(bad1)
    rows = classified(theirs, m815)
    k1_all = sum(all(r['k1']) for r in rows)
    here_n = sum(r['here']['classified'] for r in rows)
    say(f'2. PASS: K1 at every cutoff at {k1_all} of {len(rows)} read points; this instrument classifies {here_n}; '
        f"identity kept at {sum(bool(lib.at(theirs[r['row']], r['eps'])['identity'] and lib.at(theirs[r['row']], r['eps'])['identity']['kept']) for r in rows)}")
    for r in rows:
        if not r['here']['classified']:
            say(f"      not classified here: {r['row']} {r['eps']:g}: {'; '.join(r['here']['causes'])[:150]}")
    bad3, decided, unres = claim3(rows)
    by = {}
    for r in rows:
        by[r['combined'].get('instrument')] = by.get(r['combined'].get('instrument'), 0) + 1
    say(f"3. {'PASS' if not bad3 else 'FAIL'}: K6 reproduced: {decided} points decided and read, {unres} Unresolved "
        f"here; classified by {by}" + ''.join(f'\n      {b}' for b in bad3[:8]))
    fails += bool(bad3)
    dn = derived_new(theirs, m815)
    want = {r: [lib.key(e) for e in v] for r, v in lib.NEW.items()}
    have = {r: [lib.key(e) for e in v] for r, v in dn.items() if r != 'T3/R5'}
    t3 = [lib.key(e) for e in dn.get('T3/R5', [])]
    loc = lib.known_location(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))
    ok4 = have == want and t3 == [lib.key(16.0)] and loc['lower']['eps'] < 16.0 < loc['upper']['eps']
    say(f"4. {'PASS' if ok4 else 'FAIL'}: the first-time readings from the records alone: "
        f"{sum(len(v) for v in have.values())} on the run's rows, equal to census_lib.NEW, and T3/R5's 16, inside "
        f"M8.15.2's location ({loc['lower']['eps']:.6g}, {loc['upper']['eps']:.6g})")
    fails += not ok4
    refused, not_refused, n_asked = claim5(theirs, m815)
    say(f"5. {'PASS' if not not_refused else 'FAIL'}: refused {refused} of {n_asked}: the 56, T3/R5's withheld 16, and "
        f"every grid interval's midpoint" + ''.join(f'\n      not refused: {b}' for b in not_refused[:8]))
    fails += bool(not_refused)
    seal = []
    for row in lib.RUN_ORDER:
        try:
            sd.seed_state(row, basis.Basis(lib.SLOT[row], 16))
            seal.append(f'{row}: its seed was built')
        except PermissionError:
            pass
    try:
        census.frozen()
        seal.append('census.frozen() admitted the tree')
    except PermissionError as e:
        say(f'      census.frozen(): {e}')
    for what, call in (('linear.record', lambda: ln.record(None, None, None, None, 1.0)),
                       ('branches.continue_to', lambda: br.continue_to(None, 0, 0, None, 0, 0)),
                       ('newton.solve', lambda: newton.solve(None, None, 0, None, 0))):
        try:
            call()
            seal.append(f'{what} ran')
        except PermissionError:
            pass
        except Exception as e:  # noqa: BLE001
            seal.append(f'{what} raised {type(e).__name__}, not PermissionError')
    say(f"6. {'PASS' if not seal else 'FAIL'}: every run row's seed refused, the census driver refused, and the solver "
        f"and record paths refused in this process" + ''.join(f'\n      {b}' for b in seal))
    fails += bool(seal)

    say('arms, each of which must turn its claim red:')
    arms = []
    t1 = copy.deepcopy(theirs)
    gs = t1['T3/R4']['cutoffs']['32']['points'][lib.key(8.0)]['summary']['groups']
    slow = min((g for g in gs if g['cls'] == 'imag'), key=lambda g: abs(g['c'][1]))      # a group the rule tests
    slow['c'] = [slow['c'][0], slow['c'][1] + 1e-9]
    arms.append(('A1. a stored group centre moved by 1e-9, T3/R4 at 8, N = 32',
                 any(b.startswith('T3/R4 8:') for b in claim1(t1))))
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        src = open(lib.__file__, encoding='utf-8').read()
        anchor = '    if sealed(row, eps):\n        raise Sealed('
        if src.count(anchor) != 1:
            raise SystemExit('the A2 anchor moved')
        mut = load_copy(src.replace(anchor, '    if False:\n        raise Sealed(', 1), 'census_lib_a2', tmp)
        _, nr, _ = claim5(theirs, m815, mut)
        arms.append((f'A2. the sealed() check removed: {len(nr)} points not refused', len(nr) >= 50))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    t3c = copy.deepcopy(theirs)
    t3c['T2/R5']['identity'][lib.key(4.0)]['kept'] = False
    arms.append(('A3. identity kept = False at T2/R5, 4', any(b.startswith('T2/R5 4:') for b in claim3(classified(t3c, m815))[0])))
    for label, red in arms:
        say(f"   {label}: {'RED' if red else 'GREEN'}")
    fails += sum(not red for _, red in arms)
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_reader.out'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
