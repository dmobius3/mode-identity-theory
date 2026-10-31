#!/usr/bin/env python3
"""Test 1: every constant (M8.18's terms: THE TESTS BEFORE THE FREEZE, test 1), M8.17's test_constants.py carried to this
task's document.

Usage: test_constants.py TERMS_MD

It reads the terms, TERMS_MD, and runs on a test FROZEN.json that write_guard.build() makes and writes nowhere, in a
seedcheck process, with no solve.

Claims, derived before the run:
  1. Forward. Every numeric item of the document is one of three kinds:
     (a) a literal the code reads, located by name, and FROZEN.json holds, equal;
     (b) a value its calculation reproduces, from M8.17's and M8.16.1's records in reference/ and the constants' own
         formulas;
     (c) an unscored report, with its reason: the word budget, the estimate, Lemma F's levels, M8.16's development record,
         the maintainer's measure and the plumbing's cutoffs.
  2. Coverage. Every number in the document is claimed by exactly one item, or is a reference or a name, not a
     value: a section number after a section sign, the 256 of SHA-256, a pull request or discussion after '#', a date,
     anything inside a link's target, a numeric link text, a list item's number, and a label after 'step', 'clause',
     'level', 'amendment' or 'test'. Every item's anchor occurs once in the document.
  3. Reverse (M8.16.1's scan). Every numeric literal of this task's new code, census_lib.py, census.py,
     write_guard.py and freeze_block.py, outside the structural contexts (subscripts and slices, the exponents 2 and 0.5,
     the numbers 0 and +-1, range bounds), is on exactly one list, each entry with its function, its line's anchor and
     its reason, and no entry is stale. M8.16.1's own run code is byte for byte, and its scan is M8.16.1's test 2.
Arms, each of which must turn its claim red:
  A1. FROZEN.json without the census values' band_n: claim 1 names the missing entry.
  A2. a registered literal changed, MOVED to 0.5, in a temporary copy of census_lib.py: claim 1, by equality.
  A3. a new tolerance, 1.07 times AGREE, in a temporary copy of census_lib.py, with no list entry: claim 3.
  A4. a number put in a copy of the document right after a reference, '#512 and 0.37', claimed by no item: claim 2.
  4. The freeze writer, on a temporary copy of this folder, never on the folder itself: with the terms placed at
     run/m8_16_task_details.md with one byte changed and the copy's manifest pinned, write_guard.write() refuses and
     names the terms (A5, which must be red), and writes no FROZEN.json; with the terms placed exactly, it writes
     FROZEN.json and its pin in the copy, which devtools.frozen() admits, and so does the copy's own census.frozen(),
     run in a process of its own, with the run's order on its allowlist. No solve. The copy leaves out the folder's own
     freeze files (the placed terms, the environment record, the pins and FROZEN.json), so the claim reads the same
     before and after the freeze, and the folder's freeze files must be as they were.
"""
import ast
import copy
import importlib.util
import math
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
A, B = lib.ARM_A, lib.ARM_B
# the document's numbers, line by line: (anchor, tokens, kind, the checks that claim them)
ITEMS = [
    (" runs at `N = 40` on a control or a target, at T4/R5's moved midpoint, or at a guard reading. § Known outcomes names what is already on record at `N = 40`.",
     ['40', '40'], 'a', ['top']),
    ("oints at `N = 40`:** T1/R4 at 1.41, 32, 45.25, 64 and 72; T1/R5 at 32; T4/R4 at 4, 8, 11.31, 64 and 72; and T5/R2 at 45.25. M8.17's rule read each of them Unresolved on `N = 16`, 24 and 32, with K1 and branch identity holding. This arm reads them on the ladder `N = 24`, 32 and 40, and lo",
     ['40', '1.41', '32', '45.25', '64', '72', '32', '4', '8', '11.31', '64', '72', '45.25', '16', '24', '32', '24', '32', '40'], 'a', ['twelve', 'a', 'b']),
    ("R5's bracket (8, 11.31):** every grid point is classified, and `n(L)` goes from 7 to 6 at `N = 24` and 32, but K1 refused both deciding bisections at the midpoint 8.721638. This a",
     ['8', '11.31', '7', '6', '24', '32', '8.721638'], 'b', ['bracket', 'nl_ends', 'b', 'refused']),
    ("T5/R2's 128 and 132 are not here. Branch identity between `N = 24` and 32 failed ",
     ['128', '132', '24', '32'], 'b', ['t5_out', 'a']),
    ('ading at `N = 24` and 32 is on record, so this task claims no new evidence from them. The new evidence is at `N = 40`, at T4',
     ['24', '32', '40'], 'a', ['a']),
    ('wn path; `N = 16` not re',
     ['16'], 'a', ['b']),
    ('or byte; `N = 40` an inp',
     ['40'], 'a', ['top']),
    ('ernel at `N = 40`, measu',
     ['40'], 'a', ['top']),
    ('ntity between 24 and 32 and between 32 and 40; the type from `N = 40`, with ',
     ['24', '32', '32', '40', '40'], 'a', ['a']),
    ('et only, `N = 24` and 32 deciding, `N = 16` run an',
     ['24', '32', '16'], 'a', ['b']),
    (' Within about 8,000 words |',
     ['8', '000'], 'c', ['words']),
    ("dget.** About 7,000 words, inside § 12.2's cap of about 8,000.",
     ['7', '000', '8', '000'], 'c', ['words']),
    ('7159c3…`, the 27,823-byte pr',
     ['27', '823'], 'b', ['terms17']),
    ('tions at `N = 40`, and a',
     ['40'], 'a', ['top']),
    ('No cutoff but 24, 32 and 40 in Arm A, and none but 16, 24 and 32 in Arm B.** `N = 16` is not',
     ['24', '32', '40', '16', '24', '32', '16'], 'a', ['a', 'b']),
    ('Arm A.** `N = 40` solves',
     ['40'], 'a', ['top']),
    ("ed there, the 19 count changes among them, and T4/R4's two non-contractions, at 64 and 72.",
     ['19', '64', '72'], 'b', ['known19', 'nc']),
    ('s locator on (8, 11.31)** (`RE',
     ['8', '11.31'], 'b', ['bracket']),
    ('e stored `N = 24` and 32 summari',
     ['24', '32'], 'a', ['a']),
    ("ls,** at `N = 16`, 24 and 32, and C1's at `N = 40`.",
     ['16', '24', '32', '40'], 'b', ['c1_40', 'b']),
    ("** holds `N = 40` on C2a, C2b and C3 at `ε` = 0.5, 1 and 2 (`DEVLOG.md`, entry 78), and at each ladder's top three points (entry 106), on th",
     ['40', '0.5', '1', '2', '78', '106'], 'c', ['dev16']),
    ('- the `N = 40` record',
     ['40'], 'a', ['top']),
    ('fore any `N = 40` solve.',
     ['40'], 'a', ['top']),
    ("paths at `N = 24` and 32, each reproducing M8.16.1's record; then the kernel at `N = 40`; then ",
     ['24', '32', '40'], 'a', ['a']),
    (' path at `N = 24`, then 32, then 40.',
     ['24', '32', '40'], 'a', ['a']),
    ('ading at `N = 40`, and i',
     ['40'], 'a', ['top']),
    ('or byte. `N = 40` is an ',
     ['40'], 'a', ['top']),
    (" A's are `N = 24`, 32 and 40, each from its own seed, along its own continuation path. Arm B's are M8.17's, `N = 16`, 24 and 32.",
     ['24', '32', '40', '16', '24', '32'], 'a', ['a', 'b']),
    ("**Why `N = 16` is left out (DERIVED).** Order `ε²` reaches only Lemma F's channels ([`soft-slot-branches.md`](https://github.com/dmobius3/mode-identity-theory/blob/7a2c638cd1b1bda1df57db1d47304d14aaa3249b/files/framework/files/working/files/soft-slot-branches.md), § III): levels 10, 14, 16 and 18 in `R4`; 8, 12, 14, 16 and 18 in `R5`; and 13, 17 and 19 in `R2`. `N = 16`'s truncated space stops at level 16, so it lacks level 18 in `R4` and `R5`, and levels 17 and 19 in `R2`. `N = 24`, 32 and 40 hold every one. The answers of 2026-10-20 (§ 1) recorded the same, and § III's check vi removes those channels to reproduce `N = 16`'s coef",
     ['16', '10', '14', '16', '18', '8', '12', '14', '16', '18', '13', '17', '19', '16', '17', '19', '24', '32', '40', '16'], 'c', ['lemma_f', 'b']),
    ("pen there are 22 count-change reasons, 20 of them distinct, and at every one `N = 16` holds the fewer members, while `N = 24` and 32 agree (`dev/replay_14.py`, which reproduces each recorded verdict before it reads a count; the maintainer's port confirms it). Only T4/R4 at 64 and T5/R2 at 132 have no",
     ['22', '20', '16', '24', '32', '64', '132'], 'b', ['counts22']),
    (" lies within `10⁻²` of its norm once the orbit-tangent components are removed, and the two records agree in type, `n(L)`, `n(D)`, `K`, Krein counts, `V₀`'s dimension and ranks. Between `N = 24` and 32 it must",
     ['10⁻²', '24', '32'], 'a', ['identity', 'a']),
    (' cutoff, `N = 16`", levels 17 and 18, and the floors 8.02, 10.03 and 5.58 |',
     ['16', '17', '18', '8.02', '10.03', '5.58'], 'b', ['band', 'floors']),
    ('While `N = 16` is read they agree. With it left out, the docstring moves the band and the terms\' values do not. The answer of 2026-10-30 admits an exception, and this registration takes it: to the docstring\'s wording, and to the terms\' reason for the level, "where the lowest cutoff\'s basis first lacks modes that the higher cutoffs carry". The level stays at 17 in `R2` and 18 in `R4`',
     ['16', '17', '18'], 'a', ['band']),
    ('**Where the 16 enters.** `checks.reading` takes the cutoff as its argument `n_lo`, and `band_edge` derives the level from it. M8.17\'s `census.readings_of` passes the ladder\'s lowest cutoff, so on this ladder it would pass 24, and "byte for byte" does not reach this call. The change is one line of the census\'s own code, with `BAND_N = 16` a froz',
     ['16', '24', '16'], 'a', ['band']),
    (' B keeps `N = 16` among ',
     ['16'], 'a', ['band']),
    ('nd above `N = 24`, from ',
     ['24'], 'a', ['band']),
    (' one, at `N = 40`, that ',
     ['40'], 'a', ['top']),
    ('e stored `N = 24` and 32, the band above `N = 24` gives 23 of the 24 control points their recorded type and reads 7 of the twelve converged; the band above `N = 16` gives 24 of 24 and 11 of 12. T4/R4 at 72 reads Unresolved on both. Nothing here establishes what `N = 40` will r',
     ['24', '32', '24', '23', '24', '7', '16', '24', '24', '11', '12', '72', '40'], 'b', ['replay', 'band']),
    ('ADING AT `N = 40`',
     ['40'], 'a', ['top']),
    ('| T1/R4 | 1.41, 32, 45.25, 64, 72 | the whole grid, to 72 |',
     ['1.41', '32', '45.25', '64', '72', '72'], 'a', ['twelve']),
    ('| T4/R4 | 4, 8, 11.31, 64, 72 | the whole grid, to 72 |',
     ['4', '8', '11.31', '64', '72', '72'], 'a', ['twelve']),
    ('| T1/R5 | 32 | the whole grid, to 32 |',
     ['32', '32'], 'a', ['twelve']),
    ('| T5/R2 | 45.25 | the grid, to 45.25 |',
     ['45.25', '45.25'], 'a', ['twelve']),
    (' seed at `ε = 0.25` and co',
     ['0.25'], 'a', ['grid']),
    (' with no `N = 40` solve,',
     ['40'], 'a', ['top']),
    ('At `N = 24` and 32 every grid point is solved and read, so that each can be compared with its record. At `N = 40` every ',
     ['24', '32', '40'], 'a', ['a']),
    (' read at `N = 40` anywhe',
     ['40'], 'a', ['top']),
    ('# The kernel at `N = 40`',
     ['40'], 'a', ['top']),
    ("points, `ε` = 0.25, 0.5, 1 and 2, and C1's 0.5, 1 and 2.",
     ['0.25', '0.5', '1', '2', '0.5', '1', '2'], 'a', ['sample']),
    ('when, at `N = 40`, each ',
     ['40'], 'a', ['top']),
    (' further `N = 40` solve runs, no point is classified at `N = 40`, and t',
     ['40', '40'], 'a', ['top']),
    (' read on `N = 24`, 32 and 40 at its registered points, on the band above `N = 16`. Each ',
     ['24', '32', '40', '16'], 'a', ['a', 'band']),
    ('- at `N = 24`, 32 and 40, it is ',
     ['24', '32', '40'], 'a', ['a']),
    (' with `n_lo = 16`), read',
     ['16'], 'a', ['band']),
    (' between `N = 24` and 32, and between 32 and 40.',
     ['24', '32', '32', '40'], 'a', ['a']),
    ("pe, with `N = 40`'s indi",
     ['40'], 'a', ['top']),
    ("offs are `N = 32` and 40.** `N = 24` is bisected where its ends' `n(L)` is resolved and different, and reported otherwise. Where M8.17's text has `N = 24` and 32 deciding and `N = 16` reported, this ladder reads `N = 32` and 40 deciding and `N = 24` report",
     ['32', '40', '24', '24', '32', '16', '32', '40', '24'], 'a', ['a', 'b']),
    (" has its `N = 40` record computed from its stored solution, and it keeps the classification M8.17 gave it. M8.17's locator reads two ends classified on one ladder, so before such an end enters a bracket it must meet that condition on this one: its `N = 40` record is accepted and K1 holds, its type, `n(L)`, `n(D)`, `K` and `k_i⁻` agree with M8.17's classification, and branch identity holds on both pairs. If any of these fails, the bracket is not located under this registration. The end's adjudicated classification stays unchanged. Its `N = 40` record",
     ['40', '40', '40'], 'a', ['top']),
    ('with "at `N = 32` and 40". The l',
     ['32', '40'], 'a', ['a']),
    ("* is T4/R5's (8, 11.31), and no other. Its ends read Elliptic with `(n(L), n(D), K) = (7, 1, 6)` and Hyperbolic with `(6, 1, 5)`, at every cutoff. `N = 24` and 32 decide, and `N = 16` is run",
     ['8', '11.31', '7', '1', '6', '6', '1', '5', '24', '32', '16'], 'b', ['bracket', 'ends', 'b']),
    ('m its seed to 11.31, and ea',
     ['11.31'], 'a', ['bracket']),
    (' to the point 0.4 of the current interval above its lower end, and solved there from both ends. K1 failing at the moved point is an unsuccessful stop, as now. In `census_lib.bisect`, with `moved` frozen at 0.4 for Arm',
     ['0.4', '0.4'], 'a', ['moved']),
    ('the interval [8.718402, 8.724874] at both cutoffs, 6.472×10⁻³ wide, 7.4×10⁻⁴ of its lower end against the 5×10⁻⁴ that co',
     ['8.718402', '8.724874', '6.472×10⁻³', '7.4×10⁻⁴', '5×10⁻⁴'], 'b', ['stop']),
    ('cluster, `N = 24` | `N = 32` |',
     ['24', '32'], 'b', ['header']),
    ('| 8.673097 | 7 | 9.4335×10⁻⁵ | 9.4456×10⁻⁵ |',
     ['8.673097', '7', '9.4335×10⁻⁵', '9.4456×10⁻⁵'], 'b', ['table']),
    ('| 8.698985 | 7 | 6.4790×10⁻⁵ | 6.4970×10⁻⁵ |',
     ['8.698985', '7', '6.4790×10⁻⁵', '6.4970×10⁻⁵'], 'b', ['table']),
    ('| 8.711930 | 7 | 4.2603×10⁻⁵ | 4.2879×10⁻⁵ |',
     ['8.711930', '7', '4.2603×10⁻⁵', '4.2879×10⁻⁵'], 'b', ['table']),
    ('| 8.718402 | 7 | 2.4808×10⁻⁵ | 2.5282×10⁻⁵ |',
     ['8.718402', '7', '2.4808×10⁻⁵', '2.5282×10⁻⁵'], 'b', ['table']),
    ('| 8.721638 | 7, K1 fails | 3.6937×10⁻⁶ | 6.1163×10⁻⁶ |',
     ['8.721638', '7', '3.6937×10⁻⁶', '6.1163×10⁻⁶'], 'b', ['table']),
    ('| 8.724874 | 6 | 2.4280×10⁻⁵ | 2.3785×10⁻⁵ |',
     ['8.724874', '6', '2.4280×10⁻⁵', '2.3785×10⁻⁵'], 'b', ['table']),
    ('hree margins: 6.1×10⁻⁶ at `N = 24` and 8.2×10⁻⁶ at `N = 32`. The squares on the `n(L) = 7` side fall at 1.82 to 1.86×10⁻⁷ per unit of `ε` at both cutoffs. Extrapolating them (INFERRED), the pair reaches zero near 8.72171 at `N = 24` and 8.72184 at `N = 32`, and K1 refuses from about 8.7215.',
     ['6.1×10⁻⁶', '24', '8.2×10⁻⁶', '32', '7', '1.82', '1.86×10⁻⁷', '8.72171', '24', '8.72184', '32', '8.7215'], 'b', ['margins']),
    ("oved point is 8.720990, between two readings on the record. Interpolating their squares (INFERRED) puts the nearest eigenvalue there at about 1.16×10⁻⁵ and 1.26×10⁻⁵, 1.9 and 1.5 times K1's limit. The interval it leaves is 3.88×10⁻³ wide if `n(L)` reads 7 there, and 2.59×10⁻³ if it reads 6, each narrower than the 4.36×10⁻³ that co",
     ['8.720990', '1.16×10⁻⁵', '1.26×10⁻⁵', '1.9', '1.5', '3.88×10⁻³', '7', '2.59×10⁻³', '6', '4.36×10⁻³'], 'b', ['movedvals']),
    ('n read either 7 or 6; the tw',
     ['7', '6'], 'b', ['nl_ends']),
    ("ord puts `N = 16`'s change of `n(L)` in [8.851079, 8.854315], above both deciding cutoffs'. The upper guard at `δ = 0.01`, near 8.812, lies below it, so `N = 16` should read `n(L) = 7` there against 6 at `N = 24` and 32, and the rule's structure condition should leave that guard Unresolved (INFERRED). The retry at `δ = 0.05`, near 9.161, lies a",
     ['16', '8.851079', '8.854315', '0.01', '8.812', '16', '7', '6', '24', '32', '0.05', '9.161'], 'b', ['n16']),
    ('erval at `N = 24` and 32. Its id',
     ['24', '32'], 'a', ['b']),
    (' run whatever 45.25 reads, since 128 and 132 are not',
     ['45.25', '128', '132'], 'a', ['t5']),
    ("ence. T5/R2's 128 and 132 are the two such items, and S6 is applied to T5's row once 45.25 has bee",
     ['128', '132', '45.25'], 'a', ['t5']),
    ('range.** `N = 40` sits at the edge of K1\'s calibrated range: "Above `N = 40`, K1\'s ',
     ['40', '40'], 'a', ['top']),
    ("ads the steps 24 to 32 and 32 to 40, not 16 to 24 and 24 to 32. The control gate shows that it reads the controls correctly at `ε ≤ 2`. The twelve reach `ε = 72`, and no registered control is read there on this ladder, so the gate is necessary, not sufficient. M8.16's development record read C2a, C2b and C3 at `N = 40` at their ladders' top three points, each accepted, with branch identity kept (`DEVLOG.md`, entry 106): unscored evidence above `ε = 2`, on th",
     ['24', '32', '32', '40', '16', '24', '24', '32', '2', '72', '40', '106', '2'], 'b', ['limits']),
    ("its C2a/R5 at 2 and T4/R4 at 4. It does not describe T1/R5 at 32, T1/R4 at 64 or T4/R4 at 64 on its own: those sets are still moving between `N = 24` and 32. The maintainer's measure, which is not the rule's, gives 5.3×10⁻³, 4.8×10⁻³, and 8.3×10⁻³ to 1.3×10⁻² there, against 2.3×10⁻⁵ and 7.0×10⁻⁵ (the an",
     ['2', '4', '32', '64', '64', '24', '32', '5.3×10⁻³', '4.8×10⁻³', '8.3×10⁻³', '1.3×10⁻²', '2.3×10⁻⁵', '7.0×10⁻⁵'], 'c', ['maint']),
    (' rest on `N = 16`, 24 and 32, and th',
     ['16', '24', '32'], 'a', ['b']),
    ("hange, across 4, is the likeliest such bracket: its ends carry T4/R5's indices, (7, 1, 6) and (6, 1, 5), so it",
     ['4', '7', '1', '6', '6', '1', '5'], 'b', ['t4ix']),
    ('-256. No `N = 40` solve ',
     ['40'], 'a', ['top']),
    ('oint, on `N = 16`, 24 and 32. On a p',
     ['16', '24', '32'], 'a', ['b']),
    ("ozen level's: 17 in `R2`, 18 in `R4` and `R5`. A mutation that passes 24 must fail the test. The run applies the same test to every scored reading before it writes the record. The reading beside it, on the band above `N = 24`, is re",
     ['17', '18', '24', '24'], 'a', ['band']),
    (" path at `N = 24` and 32 against M8.17's outputs and M8.16.1's controls, with P5's `k3_overlaps` at 0.25 left ou",
     ['24', '32', '0.25'], 'a', ['a', 'sample']),
    ("ype from `N = 40`. M8.17's stored distances at T5/R2's 128 and 132 are the",
     ['40', '128', '132'], 'b', ['t5id']),
    (" read at `N = 40` outside its frozen scope must be refused, and so must a `N = 40` solve started before Arm B's record is written. At the paths' other `N = 40` grid p",
     ['40', '40', '40'], 'a', ['top']),
    ('n with `n(L)` 7 and with 6;',
     ['7', '6'], 'b', ['nl_ends']),
    ('rms: its `N = 40` record',
     ['40'], 'a', ['top']),
    ('l C2a at `N = 12`, 16 and 20: paths ',
     ['12', '16', '20'], 'c', ['plumb']),
    ("m A's ladder, 24, 32 and 40, and its deciding cutoffs, 32 and 40;",
     ['24', '32', '40', '32', '40'], 'a', ['a']),
    ("m B's ladder, 16, 24 and 32, and its deciding cutoffs, 24 and 32;",
     ['16', '24', '32', '24', '32'], 'a', ['b']),
    ('- `BAND_N = 16`, and the band above `N = 24` as the',
     ['16', '24'], 'a', ['band']),
    ("- `moved = 0.4`, from the lower end, for T4/R5's (8, 11.31) alone;",
     ['0.4', '8', '11.31'], 'a', ['moved', 'bracket']),
    ("h identity's `10⁻²` are M8",
     ['10⁻²'], 'a', ['identity']),
    ('paths at `N = 24` and 32 must eq',
     ['24', '32'], 'a', ['a']),
    (' gate.** `N = 40` has no',
     ['40'], 'a', ['top']),
    (".16's at `N = 40`: about 55 to 70 hours o",
     ['40', '55', '70'], 'c', ['est']),
    ('  - about 6 hours f',
     ['6'], 'c', ['est']),
    ('  - 10 to 13 for the',
     ['10', '13'], 'c', ['est']),
    ('  - about 7 for the targets at `N = 24` and 32;',
     ['7', '24', '32'], 'c', ['est']),
    ("  - 31 to 44 for the targets' `N = 40` paths;",
     ['31', '44', '40'], 'c', ['est']),
    ('  - about 9 to 13 more fo',
     ['9', '13'], 'c', ['est']),
    ("measures `N = 40`'s time and memory on the controls, before any of Arm A's targets. No target's path at `N = 40`, and n",
     ['40', '40'], 'a', ['top']),
]


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
    if '×10' in tok:
        m, e = tok.split('×10')
        d = len(m.split('.')[1]) if '.' in m else 0
        return round(x * 10.0 ** -int(e.translate(SUP)), d) == float(m)
    d = len(tok.split('.')[1]) if '.' in tok else 0
    return round(x, d) == val(tok)


def spans(text):
    return [(m.start(), m.end()) for p in NOT_VALUES for m in re.finditer(p, text)]


def reference(text, i, sp):
    return any(a <= i < b for a, b in sp)


def design():
    """The moved midpoint's values, from M8.17's locator record, as dev/moved_midpoint.py reads them."""
    known = lib.m817_file(lib.LOCATED_B, ROOT)
    out_ = {}
    for N in ('24', '32'):
        r = known['bisection'][N]
        a, b = r['interval']
        rows = sorted((m['eps'], m['from_lower']['nL'], m['from_lower']['point']['record']['outside_min'],
                       m['from_lower']['point']['record']['margin']) for m in r['midpoints'])
        near = [x for x in rows if a - 0.05 <= x[0] <= b + 1e-9]
        seven = [x for x in near if x[1] == 7]
        s1, s2 = seven[-2][2] ** 2, seven[-1][2] ** 2
        e1, e2 = seven[-2][0], seven[-1][0]
        rate = (s1 - s2) / (e2 - e1)
        rates = [(x[2] ** 2 - y[2] ** 2) / (y[0] - x[0]) for x, y in zip(seven, seven[1:])]
        limit = lib.ck.ln.GRAY * seven[-1][3] if hasattr(lib.ck, 'ln') else 3.0 * seven[-1][3]
        moved = a + lib.MOVED * (b - a)
        at = (s2 + rate * (e2 - moved)) ** 0.5
        out_[int(N)] = dict(a=a, b=b, rows={x[0]: x for x in near}, rates=rates, cross=e2 + s2 / rate, limit=limit,
                            from_=e2 + s2 / rate - limit ** 2 / rate, moved=moved, at=at, ratio=at / limit)
    return out_, known


def categories(F):
    """Each check: check(tokens) -> (ok, detail)."""
    C = F['census']
    d, known = design()
    m817 = lib.m817_file('CENSUS.json', ROOT)
    t5 = lib.theirs('T5/R2', ROOT)
    t44 = {p['eps']: p for p in m817['rows']['T4/R4']['points']}
    two = lambda p24, p32, n: ck.reading([p24['summary'], p32['summary']], p32['eig'], p32['lam'], p32['record']['margin'], n)  # noqa: E731
    fourteen = {r: list(v) for r, v in lib.TWELVE.items()}
    fourteen['T5/R2'] = fourteen['T5/R2'] + [128.0, 132.0]

    def reasons(pts):
        out_ = []
        for r, es in pts.items():
            th = lib.theirs(r, ROOT)
            for e in es:
                out_ += [(r, lib.key(e), x) for x in th['readings'][lib.key(e)]['reasons'] if 'count differs' in x]
        return out_

    def replay():
        c = [0, 0]
        ctrl = [0, 0]
        for name in lib.READ_CONTROLS:
            th = lib.theirs(name, ROOT)
            for k, p24 in th['cutoffs']['24']['points'].items():
                p32 = th['cutoffs']['32']['points'][k]
                for i, n in enumerate((lib.BESIDE_N, lib.BAND_N)):
                    r = two(p24, p32, n)
                    ctrl[i] += r['verdict'] == 'converged' and r['type'] == th['case']['type']
        for row, es in lib.TWELVE.items():
            th = lib.theirs(row, ROOT)
            for e in es:
                k = lib.key(e)
                p24, p32 = th['cutoffs']['24']['points'][k], th['cutoffs']['32']['points'][k]
                for i, n in enumerate((lib.BESIDE_N, lib.BAND_N)):
                    c[i] += two(p24, p32, n)['verdict'] == 'converged'
        return ctrl, c
    rp = replay()
    rs14, rs12 = reasons(fourteen), reasons(lib.TWELVE)

    def always(detail):
        return lambda t: (True, detail)

    def known_vals(t):
        return [shown(x, s) for x, s in zip(t[0], t[1])]
    cats = dict(
        top=lambda t: (lib.TOP == 40 == C['top'] == A['cutoffs'][-1], lib.TOP),
        a=lambda t: (A['cutoffs'] == (24, 32, 40) == tuple(C['arm_a']['cutoffs']) and A['deciding'] == (32, 40)
                     == tuple(C['arm_a']['deciding']) and A['pairs'] == ((24, 32), (32, 40)), A['cutoffs']),
        b=lambda t: (B['cutoffs'] == (16, 24, 32) == tuple(C['arm_b']['cutoffs']) == tuple(cs.CUTOFFS) and B['deciding']
                     == (24, 32) == tuple(C['arm_b']['deciding']) and B['pairs'] == ((24, 32),), B['cutoffs']),
        twelve=lambda t: (sum(len(v) for v in lib.TWELVE.values()) == 12 and C['twelve'] == {r: list(v) for r, v in lib.TWELVE.items()}
                          and all(shown(x, s) for x, s in ((lib.TWELVE['T1/R4'][0], '1.41'), (lib.TWELVE['T4/R4'][2], '11.31'),
                                                           (lib.TWELVE['T5/R2'][0], '45.25')))
                          and lib.TWELVE['T1/R4'][1:] == [32.0, W4[15], 64.0, 72.0] and lib.TWELVE['T4/R4'][:2] == [4.0, 8.0]
                          and lib.PATHS['T1/R4'][-1] == 72.0 == lib.PATHS['T4/R4'][-1] and lib.PATHS['T1/R5'][-1] == 32.0
                          and shown(lib.PATHS['T5/R2'][-1], '45.25'), 'the twelve and their paths'),
        bracket=lambda t: (lib.BRACKET_B[0] == 8.0 and shown(lib.BRACKET_B[1], '11.31') and C['bracket_b'] == list(lib.BRACKET_B),
                           lib.BRACKET_B),
        nl_ends=lambda t: (known['nL'] == {'24': [7, 6], '32': [7, 6]}, known['nL']),
        refused=lambda t: (shown(known['bisection']['24']['midpoints'][-1]['eps'], '8.721638')
                           and not known['bisection']['24']['midpoints'][-1]['from_lower']['k1']
                           and not known['bisection']['32']['midpoints'][-1]['from_lower']['k1'], 'the refused midpoint'),
        t5_out=lambda t: (not t5['identity'][lib.key(128.0)]['kept'] and not t5['identity'][lib.key(132.0)]['kept'],
                          "the identity failed at T5/R2's 128 and 132"),
        words=always('the word budget, reported'),
        terms17=lambda t: (os.path.getsize(os.path.join(ROOT, 'reference', 'm8_17', 'run', 'm8_16_task_details.md')) == 27823,
                           "M8.17's filed terms"),
        known19=lambda t: (len(set(rs12)) == 19, len(set(rs12))),
        nc=lambda t: (all('non-contracting' in ' '.join(lib.theirs('T4/R4', ROOT)['readings'][lib.key(e)]['reasons']) for e in (64.0, 72.0)),
                      "T4/R4's two non-contractions"),
        c1_40=lambda t: ('40' in lib.m8161_file('C1.json', ROOT)['cutoffs'], "C1's record at N = 40"),
        dev16=always("M8.16's development record, reported: DEVLOG entries 78 and 106"),
        lemma_f=always("Lemma F's levels, quoted from soft-slot-branches.md, section III, at MIT 7a2c638; N = 16 stops at 16"),
        counts22=lambda t: (len(rs14) == 22 and len(set(rs14)) == 20
                            and not [x for x in rs14 if x[:2] in (('T4/R4', lib.key(64.0)), ('T5/R2', lib.key(132.0)))],
                            (len(rs14), len(set(rs14)))),
        identity=lambda t: (ck.IDENTITY == 1e-2 == C['agree'] == lib.AGREE, ck.IDENTITY),
        band=lambda t: (lib.BAND_N == 16 == C['band_n'] and lib.BESIDE_N == 24 == C['beside_n']
                        and lib.BAND_LEVEL == {'R2': 17, 'R4': 18, 'R5': 18} == C['band_level'], (lib.BAND_N, lib.BAND_LEVEL)),
        floors=lambda t: (shown(lib.band_value('R4', 48.0 + 72.0), '8.02') and shown(lib.band_value('R5', 48.0 + 32.0), '10.03')
                          and shown(lib.band_value('R2', 63.0 + W2[17]), '5.58'), 'the floors'),
        replay=lambda t: (rp == ([23, 24], [7, 11]) and sum(len(lib.theirs(n, ROOT)['cutoffs']['24']['points']) for n in lib.READ_CONTROLS) == 24
                          and t[:2] == ['24', '32'], rp),
        grid=lambda t: (all(lib.PATHS[r][0] == 0.25 for r in lib.PATHS), 'the paths start at 0.25'),
        sample=lambda t: (cs.SAMPLE == [0.25, 0.5, 1.0, 2.0] and cs.C1_EPS == [0.5, 1.0, 2.0], cs.SAMPLE),
        moved=lambda t: (lib.MOVED == 0.4 == C['moved'], lib.MOVED),
        ends=lambda t: ([known['ends'][lib.key(lib.BRACKET_B[0])]['points'][str(N)]['record']['nL'] for N in (16, 24, 32)] == [7, 7, 7]
                        and [known['ends'][lib.key(lib.BRACKET_B[1])]['points'][str(N)]['record']['K'] for N in (16, 24, 32)] == [5, 5, 5]
                        and t[2:8] == ['7', '1', '6', '6', '1', '5'], "T4/R5's ends"),
        stop=lambda t: (shown(d[24]['a'], t[0]) and shown(d[24]['b'], t[1]) and d[24]['a'] == d[32]['a'] and d[24]['b'] == d[32]['b']
                        and shown(d[24]['b'] - d[24]['a'], t[2]) and shown((d[24]['b'] - d[24]['a']) / d[24]['a'], t[3])
                        and lib.W_HALF == val(t[4]), 'the stop'),
        header=lambda t: (t == ['24', '32'], 'the table'),
        table=lambda t: (shown(next(e for e in d[24]['rows'] if shown(e, t[0])), t[0]) and all(
            shown(next(x for e, x in d[N]['rows'].items() if shown(e, t[0]))[2], t[i]) and
            next(x for e, x in d[N]['rows'].items() if shown(e, t[0]))[1] == int(t[1]) for N, i in ((24, 2), (32, 3))), t[0]),
        margins=lambda t: (shown(d[24]['limit'], t[0]) and shown(d[32]['limit'], t[2]) and t[4] == '7'
                           and all(shown(min(d[N]['rates']), '1.82×10⁻⁷') and shown(max(d[N]['rates']), '1.86×10⁻⁷') for N in (24, 32))
                           and t[5] == '1.82' and t[6] == '1.86×10⁻⁷' and shown(d[24]['cross'], t[7]) and shown(d[32]['cross'], t[9])
                           and shown(d[24]['from_'], t[11]) and shown(d[32]['from_'], t[11]), 'the margins and the extrapolation'),
        movedvals=lambda t: (shown(d[24]['moved'], t[0]) and shown(d[24]['at'], t[1]) and shown(d[32]['at'], t[2])
                             and shown(d[24]['ratio'], t[3]) and shown(d[32]['ratio'], t[4])
                             and shown(d[24]['b'] - d[24]['moved'], t[5]) and shown(d[24]['moved'] - d[24]['a'], t[7])
                             and shown(lib.W_HALF * d[24]['moved'], t[9]) and shown(lib.W_HALF * d[24]['a'], t[9]), 'the moved point'),
        n16=lambda t: (known['bisection']['16']['complete'] and all(shown(x, s) for x, s in zip(known['bisection']['16']['interval'], t[1:3]))
                       and lib.DELTAS == (0.01, 0.05) == tuple(C['deltas']) and shown(d[24]['b'] * 1.01, t[4])
                       and shown(d[24]['b'] * 1.05, t[11]), "N = 16's change and the guards"),
        t5=lambda t: (shown(lib.TWELVE['T5/R2'][0], '45.25') and W2[-2:] == [128.0, 132.0], 'T5/R2'),
        limits=lambda t: (A['pairs'] == ((24, 32), (32, 40)) and cs.SAMPLE[-1] == 2.0 and W4[-1] == 72.0, 'the rule on this ladder'),
        maint=always("the maintainer's measure and the points it read, quoted from the answer of 2026-10-30, section 3"),
        t4ix=lambda t: (t44[W4[7]]['here']['nL'] == 7 and t44[W4[9]]['here']['K'] == 5 and t[1:] == ['7', '1', '6', '6', '1', '5'],
                        "T4/R4's ends, from M8.17's classification"),
        t5id=lambda t: (t5['identity'][lib.key(128.0)]['aligned_distance'] > 1e-2 and t5['identity'][lib.key(132.0)]['aligned_distance'] > 1e-2,
                        "M8.17's stored distances"),
        plumb=always("the plumbing's cutoffs, dev/plumbing_census.py's PLUMB, never used by the run"),
        est=always('the estimate, reported'),
    )
    return cats


# ------------------------------------------------------------------------------------------------------------ claim 1
def claim1_2(F, text):
    bad1, bad2, claimed = [], [], []
    sp = spans(text)
    cats = categories(F)
    for anchor, toks, kind, keys in ITEMS:
        if text.count(anchor) != 1:
            bad2.append(f'the anchor {anchor[:50]!r} occurs {text.count(anchor)} times')
            continue
        i = text.index(anchor)
        got = [m.group(1) for m in TOKEN.finditer(anchor) if not reference(text, i + m.start(), sp)]
        if got != toks:
            bad2.append(f'{anchor[:50]!r} holds {got}, not {toks}')
        claimed.append((i, i + len(anchor)))
        for key_ in keys:
            try:
                ok, detail = cats[key_](toks)
            except KeyError as e:
                ok, detail = False, f'FROZEN.json lacks {e.args[0]!r}'
            if not ok:
                bad1.append(f'({kind}, {key_}) {anchor[:60]!r}: {detail}')
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
                         "a name: the usage's argument count")
LISTS = [
    ('census_lib', '<module>', 'BAND_N = 16 ', None, REG, "the band's n_lo"),
    ('census_lib', '<module>', 'BESIDE_N = 24 ', None, REG, 'the n_lo of the reading beside it'),
    ('census_lib', '<module>', "BAND_LEVEL = {'R2': 17", None, REG, 'the frozen level, slot by slot'),
    ('census_lib', '<module>', 'MOVED = 0.4 ', None, REG, "Arm B's moved midpoint"),
    ('census_lib', '<module>', "ARM_A = dict(name='A'", None, REG, "Arm A's ladder"),
    ('census_lib', '<module>', "ARM_B = dict(name='B'", None, REG, "Arm B's deciding cutoffs and pair"),
    ('census_lib', '<module>', "WINDOWS = {'R4': cs.ladder(16, 72.0)", None, REG, "the windows, M8.17's"),
    ('census_lib', '<module>', 'W = 1e-3 ', None, REG, "the union's w, M8.17's"),
    ('census_lib', '<module>', 'W_HALF = W / 2 ', None, REG, "each cutoff's w/2, M8.17's"),
    ('census_lib', '<module>', 'DELTAS = (0.01, 0.05) ', None, REG, "the guards' offsets, M8.17's"),
    ('census_lib', 'band_value', 'math.sqrt(n * (n + 2))', None, FORM, "a level's free frequency"),
    ('census_lib', 'band_ok', "abs(reading['band'] - band_value(slot, lam)) <= 1e-12", None, LOOK, 'the stored band against the formula'),
    ('census_lib', 'bisect', 'm = (a + b) / 2', None, FORM, 'the arithmetic midpoint'),
    ('census_lib', 'locate', 'x <= hi * (1 + 1e-12)', None, LOOK, "the bracket's upper end among the grid values"),
    ('census', 'solve', "accepted = abs(res['eps'] - eps) <= 1e-6", None, REG, "run_case's acceptance, the secant's 1e-6"),
    ('census', '__init__', "self.seed_ok = bool(abs(self.chk['Q'] - Qx) / Qx < 1e-12 and self.chk['crit'] <= 1e-12",
     None, REG, "run_case's seed check, Q and criticality"),
    ('census', 'solves', "p['eps'] <= upto * (1 + 1e-12)", None, LOOK, "the path's last grid value"),
    ('write_guard', '<module>', 'if len(sys.argv) != 2:', None, NAME, 'the usage: one argument, the go'),
    ('freeze_block', '<module>', 'if len(sys.argv) != 3:', None, NAME, "the usage: the solver commit and the block's path"),
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
    filed = os.path.join(ROOT, 'registration', 'm8_18_task_details.md')
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
            a5 = 'run/m8_16_task_details.md differs from registration/m8_18_task_details.md' in str(e)
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
                              "import census; F = census.frozen(); print('|'.join(F['allowlist']))", good],
                             capture_output=True, text=True)
        rows = res.stdout.strip().split('|')
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
    say("Test 1, every constant: M8.18's terms against the code, a test FROZEN.json and the records on file.")
    say(f'   the terms {devtools.sha256(sys.argv[1])}')
    F = wg.build(ROOT, 'test')
    paths = {m: os.path.join(HERE, f'{m}.py') for m in SCAN}
    bad1, bad2 = claim1_2(F, text)
    say(f"1. {'PASS' if not bad1 else 'FAIL'}: the forward items, {len(ITEMS)}: "
        + ', '.join(f"{sum(1 for x in ITEMS if x[2] == k)} of kind ({k})" for k in 'abc') + ''.join(f'\n      {b}' for b in bad1))
    n_tok = len(list(TOKEN.finditer(text)))
    n_ref = sum(reference(text, m.start(), spans(text)) for m in TOKEN.finditer(text))
    say(f"2. {'PASS' if not bad2 else 'FAIL'}: coverage: {n_tok} numbers, {n_ref} references or names, the rest each "
        f"claimed once" + ''.join(f'\n      {b}' for b in bad2[:12]))
    cats = categories(F)
    for _, toks, kind, keys in ITEMS:
        if kind == 'c':
            say(f'      (c) {toks}: {cats[keys[0]](toks)[1]}')
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
    del G['census']['band_n']
    arms.append(("A1. FROZEN.json without the census values' band_n", any("lacks 'band_n'" in b for b in claim1_2(G, text)[0])))
    tmp = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
    try:
        src = open(paths['census_lib'], encoding='utf-8').read()
        p2 = os.path.join(tmp, 'census_lib_a2.py')
        with open(p2, 'w', encoding='utf-8') as f_:
            f_.write(src.replace('MOVED = 0.4 ', 'MOVED = 0.5 ', 1))
        spec = importlib.util.spec_from_file_location('census_lib_a2', p2)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        saved = lib.MOVED
        lib.MOVED = mod.MOVED
        try:
            arms.append(('A2. MOVED changed to 0.5 in a copy of census_lib.py', bool(claim1_2(F, text)[0])))
        finally:
            lib.MOVED = saved
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
