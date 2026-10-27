#!/usr/bin/env python3
"""Test 1: every constant (M8.17's terms: THE TESTS BEFORE THE FREEZE, test 1), M8.16.1's test_constants.py carried to
the whole of this task's document.

Usage: test_constants.py TERMS_MD

It reads the terms, TERMS_MD, and runs on a test FROZEN.json that write_guard.build() makes and writes nowhere, in a
seedcheck process, with no solve.

Claims, derived before the run:
  1. Forward. Every numeric item of the document is one of three kinds:
     (a) a literal the code reads, located by name, and FROZEN.json holds, equal;
     (b) a value its calculation reproduces: from the grid, the windows and paths, M8.15's and M8.15.2's records, or
         M8.16.1's outputs and filed terms, each read from reference/;
     (c) an unscored report, with its reason: the word budget, the estimate, M8.16.1's stated limit, the grouping
         check's range.
  2. Coverage. Every number in the document is claimed by exactly one item, or is a reference or a name, not a
     value: a section number after a section sign, the 256 of SHA-256, a pull request or discussion after '#', a date,
     anything inside a link's target, a numeric link text, a list item's number, and a label after 'step', 'clause',
     'level', 'amendment' or 'test'. Every item's anchor occurs once in the document.
  3. Reverse (M8.16.1's scan). Every numeric literal of this task's new code, census_lib.py, census.py,
     write_guard.py and freeze_block.py, outside the structural contexts (subscripts and slices, the exponents 2 and 0.5, the numbers 0
     and +-1, range bounds), is on exactly one list, each entry with its function, its line's anchor and its reason, and
     no entry is stale. M8.16.1's own run code is byte for byte, and its scan is M8.16.1's test 2.
Arms, each of which must turn its claim red:
  A1. FROZEN.json without the census values' w: claim 1 names the missing entry.
  A2. a registered literal changed, W to 2e-3, in a temporary copy of census_lib.py: claim 1, by equality.
  A3. a new tolerance, 1.07 times AGREE, in a temporary copy of census_lib.py, with no list entry: claim 3.
  A4. a number put in a copy of the document right after a reference, '#512 and 0.37', claimed by no item: claim 2.
  4. The freeze writer, on a temporary copy of this folder, never on the folder itself (UB): with the terms placed at
     run/m8_16_task_details.md with one byte changed and the copy's manifest pinned, write_guard.write() refuses and
     names the terms (A5, which must be red), and writes no FROZEN.json; with the terms placed exactly, it writes
     FROZEN.json and its pin in the copy, which devtools.frozen() admits, and so does the copy's own census.frozen(),
     run in a process of its own (UA's rehearsal), with the seven run rows on its allowlist. No solve. The copy leaves
     out the folder's own freeze files (the placed terms, the environment record, the pins and FROZEN.json), so the
     claim reads the same before and after the freeze, and the folder's freeze files must be as they were (UB).
"""
import ast
import copy
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import census_lib as lib  # noqa: E402
import write_guard as wg  # noqa: E402
import pin_manifest as pm  # noqa: E402

SUP = str.maketrans('⁻⁰¹²³⁴⁵⁶⁷⁸⁹', '-0123456789')
TOKEN = re.compile(r'(?<![A-Za-z0-9_.])(\d+(?:\.\d+)?×10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+|10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+|\d+(?:\.\d+)?(?:/\d+)?%?)'
                   r'(?![A-Za-z0-9_])')
NOT_VALUES = [r'§ [0-9]+(?:\.[0-9]+)?', r'SHA-256', r'#[0-9]+', r'[0-9]{4}-[0-9]{2}-[0-9]{2}', r'\]\([^)]*\)',
              r'\[[0-9]+\]', r'(?m)^[0-9]+\. ', r'(?:step|clause|level|amendment|test) [0-9]+']
out = []
W4, W5, W2 = lib.WINDOWS['R4'], lib.WINDOWS['R5'], lib.WINDOWS['R2']


def say(s=''):
    print(s, flush=True)
    out.append(s)


def val(tok):
    if '×10' in tok:
        m, e = tok.split('×10')
        return float(m) * 10.0 ** int(e.translate(SUP))
    if re.fullmatch(r'10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+', tok):
        return 10.0 ** int(tok[2:].translate(SUP))
    return float(tok) if '.' in tok else int(tok)


def shown(x, tok):
    """Whether x, printed to the digits tok shows, is tok."""
    d = len(tok.split('.')[1]) if '.' in tok else 0
    return round(x, d) == val(tok)


def spans(text):
    return [(m.start(), m.end()) for p in NOT_VALUES for m in re.finditer(p, text)]


def reference(text, i, sp):
    return any(a <= i < b for a, b in sp)


def records():
    theirs, m815 = lib.theirs_records(), lib.m815_records()
    loc = lib.known_location(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))
    return theirs, m815, loc


def types(m815, row, which):
    return [t['eps'] for t in m815[row]['types'] if t['type'] == which]


def read_eps(theirs, row):
    return [p['eps'] for p in theirs[row]['case']['points'] if p['read']]


def withheld_eps(theirs, row):
    return [p['eps'] for p in theirs[row]['case']['points'] if not p['read']]


def offsets_ok():
    """The guards at the union's ends times 1 - delta and 1 + delta, for a union inside a wide window."""
    g = lib.guard_offsets((10.0, 11.0), [1.0, 100.0])
    want = {'lower': [(0.01, 9.9), (0.05, 9.5)], 'upper': [(0.01, 11.11), (0.05, 11.55)]}
    return all(d == wd and abs(x - wx) < 1e-12 for side in want for (d, x), (wd, wx) in zip(g[side], want[side]))


def all_shown(xs, toks):
    return len(xs) == len(toks) and all(shown(x, t) for x, t in zip(xs, toks))


# ------------------------------------------------------------------------------------------------------------ claim 1
def items(F):
    """(anchor, tokens, kind, check) with check() -> (ok, detail)."""
    theirs, m815, loc = records()
    C, D = F['census'], F['inherited']['values']
    A, B, Cc = 'a', 'b', 'c'
    cut = lambda: (lib.CUTOFFS == [16, 24, 32] == C['cutoffs'] == cs.CUTOFFS, lib.CUTOFFS)  # noqa: E731
    dec = lambda: (lib.DECIDING == [24, 32] == C['deciding'] == lib.CUTOFFS[-2:], lib.DECIDING)  # noqa: E731
    dec16 = lambda: (dec()[0] and lib.CUTOFFS[0] == 16, (lib.DECIDING, lib.CUTOFFS[0]))  # noqa: E731
    n_new = sum(len(v) for v in lib.NEW.values())
    m15 = {r: [x['eps'] for x in m815[r]['types'] if x['type'] not in ('Elliptic', 'Hyperbolic')] for r in m815}
    lo4, hi4 = loc['lower']['eps'], loc['upper']['eps']
    kw = [r for r in ('T1/R4', 'T4/R4', 'T1/R5', 'T4/R5')]
    rows_decided_read = sum(1 for r in m815 for e in read_eps(theirs, r) if lib.there(m815[r], e)['decided'])
    lad = lib.load_json(os.path.join(ROOT, 'reference', 'm8_16_1', 'dev', 'runs', '015_ladder', 'C2a_R5_ladder.json'))
    smp = lib.load_json(os.path.join(ROOT, 'reference', 'm8_16_1', 'run', 'out', 'C2a_R5.json'))['case']['points']
    rule3 = sorted({e for r in lib.RUN_ORDER for e in lib.PATHS[r] if lib.rule_for(r, e, theirs[r]) == 3})
    rule1_t = sorted({e for r in kw for e in lib.PATHS[r] if lib.rule_for(r, e, theirs[r]) == 1})
    terms161 = os.path.join(ROOT, 'reference', 'm8_16_1', 'run', 'm8_16_task_details.md')
    return [
        ('all 56 first-time spectral readings', ['56'], B, lambda: (n_new == 56, n_new)),
        ('`ε` = 0.25, 0.5, 1 and 2, which read Elliptic and converged', ['0.25', '0.5', '1', '2'], A,
         lambda: (cs.SAMPLE == [0.25, 0.5, 1.0, 2.0] == D['sample'] and all(read_eps(theirs, r) == cs.SAMPLE for r in kw),
                  cs.SAMPLE)),
        ('bracketed in (11.31, 32)', ['11.31', '32'], B,
         lambda: (shown(max(e for e in types(m815, 'T2/R4', 'Elliptic')), '11.31')
                  and min(types(m815, 'T2/R4', 'Hyperbolic')) == 32.0, 'M8.15 on T2/R4')),
        ('**T3 in `R4`:** `ε = 32`, which M8.15 left undecided', ['32'], B, lambda: (m15['T3/R4'] == [32.0], m15['T3/R4'])),
        ('`ε` = 45.25, 128 and 132, which M8.15 left Unresolved', ['45.25', '128', '132'], B,
         lambda: (all_shown(m15['T5/R2'], ['45.25', '128', '132']), m15['T5/R2'])),
        ('Elliptic at 15.6356 and Hyperbolic at 16.5832 at level 3. Its one undecided grid point, `ε = 16`',
         ['15.6356', '16.5832', '16'], B,
         lambda: (shown(lo4, '15.6356') and shown(hi4, '16.5832') and m15['T3/R5'] == [16.0] and lo4 < 16 < hi4, loc)),
        ('The new evidence is the 56 points above', ['56'], B, lambda: (n_new == 56, n_new)),
        ('| A cutoff other than 16, 24 and 32 only after', ['16', '24', '32'], A, cut),
        ('this run uses 16, 24 and 32 only', ['16', '24', '32'], A, cut),
        ("About 4,500 words, inside § 12.2's cap of about 8,000.", ['4', '500', '8', '000'], Cc,
         lambda: (True, 'the word budget, reported')),
        ('the 47,420-byte prefix', ['47', '420'], B,
         lambda: (os.path.getsize(terms161) == 47420 and devtools.sha256(terms161) == F['inherited']['terms_sha256'],
                  os.path.getsize(terms161))),
        ('branch identity between `N = 24` and 32, as M8.16', ['24', '32'], A, dec),
        ('**No cutoff but 16, 24 and 32.**', ['16', '24', '32'], A, cut),
        ("T1 and T4's points beyond the samples: 50 in all", ['50'], B,
         lambda: (sum(len(lib.NEW[r]) for r in kw) == 50, [len(lib.NEW[r]) for r in kw])),
        ('T2/R4 at 16 and 22.63, T3/R4 at 32, and T5/R2 at 45.25. Its fifth such point, T3/R5 at 16',
         ['16', '22.63', '32', '45.25', '16'], B,
         lambda: (all_shown(withheld_eps(theirs, 'T2/R4'), ['16', '22.63']) and withheld_eps(theirs, 'T3/R4') == [32.0]
                  and all_shown(withheld_eps(theirs, 'T5/R2'), ['45.25']) and withheld_eps(theirs, 'T3/R5') == [16.0]
                  and {r: [lib.key(e) for e in v] for r, v in lib.WITHHELD.items()}
                  == {r: [lib.key(e) for e in withheld_eps(theirs, r)] for r in ('T2/R4', 'T3/R4', 'T5/R2')},
                  "M8.16.1's withheld points")),
        ('T5/R2 at 128 and 132, never solved on this instrument', ['128', '132'], B,
         lambda: ([e for e in W2 if lib.key(e) not in {lib.key(p['eps']) for p in theirs['T5/R2']['case']['points']}]
                  == [128.0, 132.0], 'T5/R2')),
        ('The cutoffs are `N = 16, 24` and 32', ['16', '24', '32'], A, cut),
        ("Branch identity between `N = 24` and 32 is M8.16.1's driver's: the `N = 24` solution, embedded at `N = 32`, "
         'lies within `10⁻²` of its norm', ['24', '32', '24', '32', '10⁻²'], A,
         lambda: (dec()[0] and ck.IDENTITY == 1e-2 == C['agree'] == D['checks']['identity'], ck.IDENTITY)),
        ('`ε_k = 0.25 · 2^{k/2}`: in `R4`, `k = 0` to 16 with 72 appended, 18 points; in `R5`, `k = 0` to 14, 15 points; '
         'in `R2`, `k = 0` to 18 with 132 appended, 20 points.',
         ['0.25', '2', '2', '0', '16', '72', '18', '0', '14', '15', '0', '18', '132', '20'], A,
         lambda: (W4 == [0.25 * 2 ** (k / 2) for k in range(17)] + [72.0] and W5 == [0.25 * 2 ** (k / 2) for k in range(15)]
                  and W2 == [0.25 * 2 ** (k / 2) for k in range(19)] + [132.0] and (len(W4), len(W5), len(W2)) == (18, 15, 20)
                  and C['windows'] == {'R4': W4, 'R5': W5, 'R2': W2}, (len(W4), len(W5), len(W2)))),
        ('| T1/R4, T4/R4 | none | 0.25, 0.5, 1, 2 | the other 14 | the whole grid, to 72 |',
         ['0.25', '0.5', '1', '2', '14', '72'], B,
         lambda: (read_eps(theirs, 'T1/R4') == read_eps(theirs, 'T4/R4') == cs.SAMPLE and len(lib.NEW['T1/R4']) == 14
                  == len(lib.NEW['T4/R4']) and lib.PATHS['T1/R4'] == lib.PATHS['T4/R4'] == W4 and W4[-1] == 72.0, 'R4')),
        ('| T1/R5, T4/R5 | none | 0.25, 0.5, 1, 2 | the other 11 | the whole grid, to 32 |',
         ['0.25', '0.5', '1', '2', '11', '32'], B,
         lambda: (read_eps(theirs, 'T1/R5') == read_eps(theirs, 'T4/R5') == cs.SAMPLE and len(lib.NEW['T1/R5']) == 11
                  == len(lib.NEW['T4/R5']) and lib.PATHS['T1/R5'] == lib.PATHS['T4/R5'] == W5 and W5[-1] == 32.0, 'R5')),
        ('| T2/R4 | Elliptic to 11.31; Hyperbolic from 32 | 16 points | 16 and 22.63, and the change of type | the grid to '
         '22.63, and on to 32 where its type bracket is (22.63, 32), then the locator |',
         ['11.31', '32', '16', '16', '22.63', '22.63', '32', '22.63', '32'], B,
         lambda: (shown(max(types(m815, 'T2/R4', 'Elliptic')), '11.31') and min(types(m815, 'T2/R4', 'Hyperbolic')) == 32.0
                  and len(read_eps(theirs, 'T2/R4')) == 16 and all_shown(lib.NEW['T2/R4'], ['16', '22.63'])
                  and shown(lib.PATHS['T2/R4'][-1], '22.63') and lib.ON_TO['T2/R4'] == (lib.T2_END, 32.0)
                  and shown(lib.T2_END, '22.63'), 'T2/R4')),
        ('| T2/R5 | Elliptic at all 15 | all 15 |', ['15', '15'], B,
         lambda: (len(types(m815, 'T2/R5', 'Elliptic')) == 15 == len(W5) and len(read_eps(theirs, 'T2/R5')) == 15, 'T2/R5')),
        ('| T3/R4 | Elliptic at 17, all but 32 | 17 points | 32 | the grid to 32 |', ['17', '32', '17', '32', '32'], B,
         lambda: (len(types(m815, 'T3/R4', 'Elliptic')) == 17 and m15['T3/R4'] == [32.0]
                  and len(read_eps(theirs, 'T3/R4')) == 17 and lib.NEW['T3/R4'] == [32.0] and lib.PATHS['T3/R4'][-1] == 32.0,
                  'T3/R4')),
        ('| T3/R5 | Elliptic to 11.31; Hyperbolic at 22.63 and 32; the change located between 15.6356 and 16.5832 | 14 '
         'points | none: `ε = 16` lies inside the location | none |',
         ['11.31', '22.63', '32', '15.6356', '16.5832', '14', '16'], B,
         lambda: (shown(max(types(m815, 'T3/R5', 'Elliptic')), '11.31')
                  and all_shown(types(m815, 'T3/R5', 'Hyperbolic'), ['22.63', '32']) and shown(lo4, '15.6356')
                  and shown(hi4, '16.5832') and len(read_eps(theirs, 'T3/R5')) == 14 and lo4 < 16.0 < hi4, 'T3/R5')),
        ('| T5/R2 | Elliptic at 17, all but 45.25, 128 and 132 | 17 points, to 90.51 | 45.25, 128 and 132 | the grid to 132 |',
         ['17', '45.25', '128', '132', '17', '90.51', '45.25', '128', '132', '132'], B,
         lambda: (len(types(m815, 'T5/R2', 'Elliptic')) == 17 and all_shown(m15['T5/R2'], ['45.25', '128', '132'])
                  and len(read_eps(theirs, 'T5/R2')) == 17 and shown(read_eps(theirs, 'T5/R2')[-1], '90.51')
                  and all_shown(lib.NEW['T5/R2'], ['45.25', '128', '132']) and lib.PATHS['T5/R2'][-1] == 132.0, 'T5/R2')),
        ("**Each path** starts at the case's seed at `ε = 0.25`", ['0.25'], A,
         lambda: (all(p[0] == 0.25 for p in lib.PATHS.values()) and all(w[0] == 0.25 for w in C['windows'].values()),
                  'the paths')),
        ('- branch identity holds between `N = 24` and 32.', ['24', '32'], A, dec),
        ("M8.16.1's K6 found none at the 79 points", ['79'], B, lambda: (rows_decided_read == 79, rows_decided_read)),
        ('its grid point inside the location, `ε = 16`, is accounted for', ['16'], B,
         lambda: (lo4 < 16.0 < hi4 and m15['T3/R5'] == [16.0], (lo4, hi4))),
        ("resolved at `N = 24` and 32, and different between the ends at both. These are the cutoffs that decide a "
         "location. `N = 16` is bisected", ['24', '32', '16'], A, dec16),
        ("**A type bracket whose ends' `n(L)` is resolved and equal at `N = 24` and 32**", ['24', '32'], A, dec),
        ('missing or unresolved at `N = 24` or 32', ['24', '32'], A, dec),
        ("is within `10⁻²` of the solution's norm", ['10⁻²'], A,
         lambda: (lib.AGREE == ck.IDENTITY == 1e-2 == C['agree'], lib.AGREE)),
        ('narrower than `w/2 = 5×10⁻⁴` of its lower end', ['2', '5×10⁻⁴'], A,
         lambda: (lib.W_HALF == lib.W / 2 == 5e-4 == C['w_half'], lib.W_HALF)),
        ("The bisections at `N = 24` and 32 both complete, with no unsuccessful stop. `N = 16`'s is run",
         ['24', '32', '16'], A, dec16),
        ('narrower than `w = 10⁻³` of its lower end', ['10⁻³'], A, lambda: (lib.W == 1e-3 == C['w'], lib.W)),
        ("`Δn(L)` at `N = 24` equals `Δn(L)` at `N = 32`, and is not zero. A discrepancy is reported. `N = 16`'s",
         ['24', '32', '16'], A, dec16),
        ("times `1 − δ` and the upper at its upper end times `1 + δ`, with `δ = 0.01`", ['1', '1', '0.01'], A,
         lambda: (lib.DELTAS[0] == 0.01 == C['deltas'][0] and offsets_ok(), lib.DELTAS)),
        ('each is read at all three cutoffs at one `ε`, with branch identity between `N = 24` and 32', ['24', '32'], A, dec),
        ('read once more at `δ = 0.05`', ['0.05'], A, lambda: (lib.DELTAS == (0.01, 0.05) and C['deltas'] == [0.01, 0.05],
                                                              lib.DELTAS)),
        ('inside the interval at `N = 24` and 32"', ['24', '32'], A,
         lambda: (lib.located_name(1).endswith('inside the interval at `N = 24` and 32') and dec()[0], 'the name')),
        ("At T5's read points from 5.66 to 90.51, M8.16.1's eigenvalues are still moving between `N = 24` and 32 (the "
         "grouping check). So T5's 45.25, 128 and 132", ['5.66', '90.51', '24', '32', '45.25', '128', '132'], B,
         lambda: (shown(W2[9], '5.66') and shown(W2[17], '90.51') and dec()[0]
                  and all_shown(lib.NEW['T5/R2'], ['45.25', '128', '132']), 'the grouping check\'s range')),
        ("T3/R5's `ε = 16` stays unclassified", ['16'], B, lambda: (m15['T3/R5'] == [16.0], m15['T3/R5'])),
        ('the ten-fold headroom is missed at 54 of 381 points', ['54', '381'], Cc,
         lambda: (True, "M8.16.1's stated limit, inherited: its RECORD.md")),
        ('beyond `ε = 2`', ['2'], B, lambda: (max(max(read_eps(theirs, r)) for r in kw) == 2.0, 'the samples')),
        ("still moving between `N = 24` and 32 at T5's larger amplitudes", ['24', '32'], A, dec),
        ('Elliptic at 15.6356 and Hyperbolic at 16.5832 at level 3. Its evidence', ['15.6356', '16.5832'], B,
         lambda: (shown(lo4, '15.6356') and shown(hi4, '16.5832'), loc)),
        ('narrower than `10⁻³` of its lower end, with two guard readings', ['10⁻³'], A, lambda: (lib.W == 1e-3, lib.W)),
        ('It refuses all 56 first-time readings', ['56'], B, lambda: (n_new == 56, n_new)),
        ('which reached 0.5, 1 and 2 by other steps', ['0.5', '1', '2'], B,
         lambda: (all(not lib.same_steps([p['eps'] for p in lad['case']['points']], [p['eps'] for p in smp], e)
                      for e in (0.5, 1.0, 2.0)), 'the ladder against the sample')),
        ("- `w/2` and the union's `w`;", ['2'], A, lambda: (lib.W_HALF == lib.W / 2, lib.W_HALF)),
        ('- the cutoffs, 16, 24 and 32;', ['16', '24', '32'], A, cut),
        ("- `w = 10⁻³`, its half for each cutoff's bisection, and `δ` = 0.01 and 0.05;", ['10⁻³', '0.01', '0.05'], A,
         lambda: (lib.W == 1e-3 == C['w'] and lib.DELTAS == (0.01, 0.05), (lib.W, lib.DELTAS))),
        ("- the two-ends agreement's `10⁻²`, branch identity's own;", ['10⁻²'], A,
         lambda: (lib.AGREE == ck.IDENTITY == 1e-2 == C['agree'], lib.AGREE)),
        ('and `ε = 0.25` on T1 and T4', ['0.25'], B, lambda: (rule1_t == [0.25], rule1_t)),
        ("**T1's and T4's points at `ε` = 0.5, 1 and 2,**", ['0.5', '1', '2'], B,
         lambda: (rule3 == [0.5, 1.0, 2.0], rule3)),
        ('about 15 to 16 hours of compute', ['15', '16'], Cc, lambda: (True, 'the estimate, reported')),
        ("about 7.7 hours for T1's and T4's paths", ['7.7'], Cc, lambda: (True, 'the estimate, reported')),
        ('3.8 for the paths of T2/R4, T3/R4 and T5/R2', ['3.8'], Cc, lambda: (True, 'the estimate, reported')),
        ("about 4 for the locator on T2/R4's change", ['4'], Cc, lambda: (True, 'the estimate, reported')),
        ('its path recomputed from the seed to 32', ['32'], B,
         lambda: (lib.ON_TO['T2/R4'][1] == 32.0 == C['on_to']['T2/R4'][1], lib.ON_TO['T2/R4'])),
        ("about 2 to 6 more for each further bracket in `R4`, about 2 in `R2`, and about 4 to 9 in `R5`",
         ['2', '6', '2', '4', '9'], Cc, lambda: (True, 'the estimate, reported')),
    ]


def claim1_2(F, text):
    bad1, bad2, claimed = [], [], []
    sp = spans(text)
    for anchor, toks, kind, check in items(F):
        if text.count(anchor) != 1:
            bad2.append(f'the anchor {anchor[:50]!r} occurs {text.count(anchor)} times')
            continue
        i = text.index(anchor)
        got = [m.group(1) for m in TOKEN.finditer(anchor) if not reference(text, i + m.start(), sp)]
        if got != toks:
            bad2.append(f'{anchor[:50]!r} holds {got}, not {toks}')
        claimed.append((i, i + len(anchor)))
        try:
            ok, detail = check()
        except KeyError as e:
            ok, detail = False, f'FROZEN.json lacks {e.args[0]!r}'
        if not ok:
            bad1.append(f'({kind}) {anchor[:60]!r}: {detail}')
    loose = []
    for m in TOKEN.finditer(text):
        if reference(text, m.start(), sp):
            continue
        hits = sum(a <= m.start() < b for a, b in claimed)
        if hits != 1:
            loose.append(f"{m.group(1)!r} at {text[max(0, m.start() - 40):m.start()]!r}, claimed {hits} times")
    return bad1, bad2 + loose


# ------------------------------------------------------------------------------------------------------------ claim 3
REG, FORM, LOOK, NAME = ('registered', "a formula's own constant", 'a lookup or float guard',
                         "a name: a rule's number, or the usage's argument count")
LISTS = [
    ('census_lib', '<module>', "WINDOWS = {'R4': cs.ladder(16, 72.0)", None, REG, 'the windows, THE POINTS'),
    ('census_lib', '<module>', "'T2/R4': [16.0, T2_END], 'T3/R4': [32.0], 'T5/R2': [WINDOWS['R2'][15], 128.0, 132.0]}",
     None, REG, 'the first-time readings beyond T1 and T4, THE POINTS'),
    ('census_lib', '<module>', "WITHHELD = {'T2/R4': [16.0, T2_END], 'T3/R4': [32.0]", None, REG,
     "the withheld points this run computes, the reproduction's rule 2"),
    ('census_lib', '<module>', 'W = 1e-3 ', None, REG, "the union's w"),
    ('census_lib', '<module>', 'W_HALF = W / 2 ', None, REG, "each cutoff's w/2"),
    ('census_lib', '<module>', 'DELTAS = (0.01, 0.05) ', None, REG, "the guards' offsets"),
    ('census_lib', 'sealed', 'abs(e - eps) <= 1e-12 * e', None, LOOK, "a grid value's own float"),
    ('census_lib', 'there', "abs(x['eps'] - eps) < 1e-9", None, LOOK, "M8.15's type at the same grid value, as K6 reads it"),
    ('census_lib', 'bisect', 'm = (a + b) / 2', None, FORM, 'the arithmetic midpoint'),
    ('census_lib', 'locate', 'x <= hi * (1 + 1e-12)', None, LOOK, "the bracket's upper end among the grid values"),
    ('census', 'step', "accepted = abs(res['eps'] - eps) <= 1e-6", None, REG, "run_case's acceptance, the secant's 1e-6"),
    ('census', '__init__', "self.seed_ok = bool(abs(self.chk['Q'] - Qx) / Qx < 1e-12 and self.chk['crit'] <= 1e-12",
     None, REG, "run_case's seed check, Q and criticality"),
    ('census_lib', '<module>', 'GATES = {1: gate_full, 2: gate_solve, 3: gate_categorical}', None, NAME,
     'the reproduction rules, by number'),
    ('census_lib', 'rule_for', 'return 1 if read[k] else 2', None, NAME, 'the reproduction rules, by number'),
    ('census_lib', 'rule_for', 'return 3 if read[k] else None', None, NAME, 'the reproduction rules, by number'),
    ('write_guard', '<module>', 'if len(sys.argv) != 2:', None, NAME, 'the usage: one argument, the go'),
    ('freeze_block', '<module>', 'if len(sys.argv) != 3:', None, NAME, "the usage: the solver commit and the block's path"),
    ('census', 'path', 'e <= upto * (1 + 1e-12)', None, LOOK, "the path's last grid value"),
]
SCAN = ('census_lib', 'census', 'write_guard', 'freeze_block')


def structural(n, parents):
    p, v, me = parents.get(n), n.value, n
    if isinstance(p, ast.UnaryOp) and isinstance(p.op, ast.USub):
        me, p, v = p, parents.get(p), -v
    if isinstance(p, (ast.Subscript, ast.Slice)) or (isinstance(p, ast.Tuple) and isinstance(parents.get(p), ast.Subscript)):
        return True
    if isinstance(p, ast.BinOp) and isinstance(p.op, ast.Pow) and p.right is me and v in (2, 0.5):
        return True
    if v in (0, 1, -1):
        return True
    return isinstance(p, ast.Call) and getattr(p.func, 'id', None) == 'range'


def literals(path):
    src = open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    parents = {c: n for n in ast.walk(tree) for c in ast.iter_child_nodes(n)}

    def func_of(n):
        while n in parents:
            n = parents[n]
            if isinstance(n, ast.FunctionDef):
                return n.name
        return '<module>'
    lines = src.splitlines()
    return [(func_of(n), n.value, lines[n.lineno - 1]) for n in ast.walk(tree) if isinstance(n, ast.Constant)
            and type(n.value) in (int, float, complex) and not structural(n, parents)]


def claim3(paths):
    used, unlisted, by = {i: 0 for i in range(len(LISTS))}, [], {}
    for mod in SCAN:
        for fn_, v, line in literals(paths[mod]):
            hits = [i for i, (m, f, a, x, _, _) in enumerate(LISTS) if m == mod and f == fn_ and a in line
                    and (x is None or x == v)]
            if len(hits) != 1:
                unlisted.append(f'{mod}.{fn_}: {v!r} on {line.strip()[:70]!r} ({len(hits)} entries)')
                continue
            used[hits[0]] += 1
            by.setdefault(LISTS[hits[0]][4], []).append((mod, fn_, v))
    stale = [f'{LISTS[i][0]}.{LISTS[i][1]} {LISTS[i][2]!r}' for i, k in used.items() if k == 0]
    return unlisted, stale, by


def freeze_copy():
    """Claim 4 and arm A5, on temporary copies of this folder: (claim 4 holds, its detail, A5 red)."""
    filed = os.path.join(ROOT, 'registration', 'm8_17_task_details.md')
    raw = open(filed, 'rb').read()
    state = lambda p: devtools.sha256(os.path.join(ROOT, p)) if os.path.exists(os.path.join(ROOT, p)) else None  # noqa: E731
    before = {p: state(p) for p in ('run/FROZEN.json', 'run/FROZEN_PIN', 'run/MANIFEST_PIN', 'run/m8_16_task_details.md', 'run/ENVIRONMENT.json')}
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    skip = lambda d, names: [x for x in names if x in ('__pycache__', '.DS_Store')  # noqa: E731
                             or (os.path.relpath(d, ROOT) == 'run' and x in ('out', 'm8_16_task_details.md',
                                 'ENVIRONMENT.json', 'MANIFEST_PIN', 'FROZEN.json', 'FROZEN_PIN'))]
    try:
        bad = os.path.join(tmp, 'changed')
        shutil.copytree(ROOT, bad, ignore=skip)
        with open(os.path.join(bad, 'run', 'm8_16_task_details.md'), 'xb') as f:
            f.write(raw[:100] + bytes([raw[100] ^ 1]) + raw[101:])
        pm.pin(bad)
        try:
            wg.write(bad, 'test')
            a5 = False
        except PermissionError as e:
            a5 = 'run/m8_16_task_details.md differs from registration/m8_17_task_details.md' in str(e)
        a5 = a5 and not os.path.exists(os.path.join(bad, 'run', 'FROZEN.json'))
        good = os.path.join(tmp, 'exact')
        shutil.copytree(ROOT, good, ignore=skip)
        with open(os.path.join(good, 'run', 'm8_16_task_details.md'), 'xb') as f:
            f.write(raw)
        pm.pin(good)
        wg.write(good, 'test')
        F = devtools.frozen(good)
        res = subprocess.run([sys.executable, '-I', '-B', '-c',
                              "import sys; sys.path.insert(0, sys.argv[1] + '/run'); sys.path.insert(0, sys.argv[1]); "
                              "import census; F = census.frozen(); print(' '.join(F['allowlist']))", good],
                             capture_output=True, text=True)
        rows = res.stdout.split()
        ok = (F['terms_sha256'] == devtools.sha256(filed) and sorted(F['allowlist']) == sorted(lib.RUN_ORDER)
              and res.returncode == 0 and sorted(rows) == sorted(lib.RUN_ORDER)
              and all(state(p) == h for p, h in before.items()))
        return ok, (f"exact terms: FROZEN.json written in the copy, admitted by devtools.frozen() and by the copy's "
                    f"census.frozen(), allowlist {rows}" + ('' if res.returncode == 0 else f'; {res.stderr[-300:]}')), a5
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    devtools.require('seedcheck')
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    text = open(sys.argv[1], encoding='utf-8').read()
    say("Test 1, every constant: M8.17's terms against the code, a test FROZEN.json and the records on file.")
    say(f'   the terms {devtools.sha256(sys.argv[1])}')
    F = wg.build(ROOT, 'test')
    paths = {m: os.path.join(HERE, f'{m}.py') for m in SCAN}
    bad1, bad2 = claim1_2(F, text)
    its = items(F)
    say(f"1. {'PASS' if not bad1 else 'FAIL'}: the forward items, {len(its)}: "
        + ', '.join(f"{sum(1 for x in its if x[2] == k)} of kind ({k})" for k in 'abc') + ''.join(f'\n      {b}' for b in bad1))
    n_tok = len(list(TOKEN.finditer(text)))
    n_ref = sum(reference(text, m.start(), spans(text)) for m in TOKEN.finditer(text))
    say(f"2. {'PASS' if not bad2 else 'FAIL'}: coverage: {n_tok} numbers, {n_ref} references or names, the rest each "
        f"claimed once" + ''.join(f'\n      {b}' for b in bad2[:12]))
    for _, toks, kind, check in its:
        if kind == 'c':
            say(f'      (c) {toks}: {check()[1]}')
    unlisted, stale, by = claim3(paths)
    ok3 = not unlisted and not stale
    say(f"3. {'PASS' if ok3 else 'FAIL'}: the reverse scan of {', '.join(SCAN)}: every literal on exactly one list, no "
        f"entry stale" + ''.join(f'\n      unlisted: {u}' for u in unlisted) + ''.join(f'\n      stale: {s}' for s in stale))
    for k in (REG, FORM, LOOK, NAME):
        say(f'      {k}: {len(by.get(k, []))} literals')
    for m, f, a, x, lst, why in LISTS:
        if lst != REG:
            say(f'        [{lst}] {m}.{f} {a.strip()[:44]!r}: {why}')
    fails = bool(bad1) + bool(bad2) + (not ok3)
    arms = []
    G = copy.deepcopy(F)
    del G['census']['w']
    arms.append(("A1. FROZEN.json without the census values' w", any("lacks 'w'" in b for b in claim1_2(G, text)[0])))
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        src = open(paths['census_lib'], encoding='utf-8').read()
        p2 = os.path.join(tmp, 'census_lib_a2.py')
        with open(p2, 'w', encoding='utf-8') as f_:
            f_.write(src.replace('W = 1e-3 ', 'W = 2e-3 ', 1))
        spec = importlib.util.spec_from_file_location('census_lib_a2', p2)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        saved = (lib.W, lib.W_HALF)
        lib.W, lib.W_HALF = mod.W, mod.W_HALF
        try:
            arms.append(('A2. W changed to 2e-3 in a copy of census_lib.py', bool(claim1_2(F, text)[0])))
        finally:
            lib.W, lib.W_HALF = saved
        anchor = '            if not d <= AGREE:\n'
        if src.count(anchor) != 1:
            raise SystemExit('the A3 anchor moved')
        p3 = os.path.join(tmp, 'census_lib.py')
        with open(p3, 'w', encoding='utf-8') as f_:
            f_.write(src.replace(anchor, '            if not d <= 1.07 * AGREE:\n', 1))
        arms.append(('A3. a new tolerance, 1.07, in a copy of census_lib.py', bool(claim3(dict(paths, census_lib=p3))[0])))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    mark = 'all on #512:'
    if text.count(mark) != 1:
        raise SystemExit('the A4 anchor moved')
    t4 = text.replace(mark, 'all on #512 and 0.37:', 1)
    arms.append(("A4. '#512 and 0.37' in a copy of the document", any("'0.37'" in b for b in claim1_2(F, t4)[1])))
    ok4, why4, a5 = freeze_copy()
    arms.append(('A5. the placed terms with one byte changed: write() refuses and names them', a5))
    say(f"4. {'PASS' if ok4 else 'FAIL'}: the freeze writer on a temporary copy: {why4}")
    fails += not ok4
    say('arms, each of which must turn its claim red:')
    for label, red in arms:
        say(f"   {label}: {'RED' if red else 'GREEN'}")
    fails += sum(not red for _, red in arms)
    say(f'{fails} failed')
    with open(os.path.join(HERE, 'test_constants.out'), 'w', encoding='utf-8') as f_:
        f_.write('\n'.join(out) + '\n')
    if fails:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
