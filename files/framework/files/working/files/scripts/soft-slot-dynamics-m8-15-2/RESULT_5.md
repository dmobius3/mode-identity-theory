# M8.15.2: the locator v2, its test results (run finished 2026-10-13T06:41Z)

**Status:** v1, confirmed by both units on 2026-10-13. Every registered test ran once, recorded, on the final code, from 03:08Z to 06:41Z.

**The review.** Unit A checked the records and logs, counted the tests and arms from their records, matched the driver records' locator hashes to the launch hashes, and reran `check_result_5.py`. Unit B rebuilt the six files from `diff_324fde3.patch` on `324fde3` byte for byte, matched each to `prerun_sha256.txt`, reran the mock suite, R4b and R5, and recomputed the regression against RESULT_4's records and rule 11 on every control step, each matching the record. Neither asked for a change.

**The outcome.** The locator v2 passes every registered test, and every arm is caught:
- S1 to S18c and A1 to A29, on the mock evaluator: 52 tests, with A7 and A11 counted by their plants (three and two), and 55 arms;
- R1 to R5 and R4b, on the real solver, for orbits that are not targets;
- on every control record, what REGISTER_5 § 3 says they carry: RESULT_4's runs reproduced value for value outside § 4's fields, the new branch never firing, and rule 11 passing at every step.

**The registration** is `REGISTER_5.md` v3, registered 2026-10-13T02:17:12Z, before any locator code. Its SHA-256, computed from the file, equals the pin recorded at registration in `REGISTER_5.sha256`. No dated amendment was needed: the unrecorded dry runs showed no registered expectation to be wrong (§ The dry runs).

**The code** is on the bench, in the new folder `soft-slot-dynamics-m8-15-2/`.
- It starts from M8.15.1's `locate.py`, `t1_branch.py`, `tests/mock.py`, `tests/synthetic.py` and `tests/real.py` at `324fde3`, copied byte for byte. They change only as REGISTER_5 § 1 says. The diff's base files each have the committed file's SHA-256.
- `diff_324fde3.patch`, beside this page, is the whole diff: 6 files, 1369 lines added and 165 removed, one of them new, `write_guard.py`.
- It reads the frozen instrument at MIT `97a8c08` without changing it. Every run checks the instrument's files against its manifest, and the manifest's SHA-256 equals the pin in `t1_branch.py`.
- `decide` is extracted from the frozen `m815_branch.py` as before. Its source's SHA-256 is in every record and equals M8.15.1's.
- Every driver record carries the SHA-256 of `locate.py` and `t1_branch.py`. `prerun_sha256.txt`, written at the recorded run's launch, holds every code file's SHA-256, and each still matches the code as it stands.

**What changed, by file.**
- **`locate.py`:**
  - `bisect` carries four points and passes the passable failures and the exchanged-lift points (rules 1 to 6);
  - `analyse_step` reads between the clean ends, checks rule 10 first, flags a branch step, and in a branch step reads the classes first, with the genuine crossings' identity outside `P`;
  - `continuity` is rule 11, a pass over each level's steps before any matching or guard, reading every evaluation as its own record;
  - the record gains § 1 item 4's fields and clause 3's trigger.
  The frozen order and checks stand outside a branch step, and nothing else changes.
- **`t1_branch.py`:** the primary brackets alone, so the ladder runs to 32 (T2/R4) and 22.63 (T3/R5); M8.15.2's own guard, `out/FROZEN.json` in the new folder, with every check of § 1; the instrument manifest's SHA-256 pinned, computed from the file.
- **`write_guard.py`, new:** the step that writes the guard once, at the freeze, after the maintainer's go. It refuses if the file exists and creates it exclusively. The driver never writes it.
- **`tests/mock.py`:** each point's `m` and reached `ε`, the coupled blocks, and the plant hooks of § 1, each off by default, so the S tests' plants are unchanged.
- **`tests/synthetic.py`:** S10's new expectation, rule 11 at every S step, the A plants with their arms, and the ceiling function.
- **`tests/real.py`:** R5 on M8.15.2's guard, and the three § 3 carries on every control record.

**The records** are in the folder's `out/`:
- `synthetic.json` and `.log`;
- `r4b.json` and `r5.json`;
- the driver's records `t1_*.json`, with `run_*.log`;
- `real.json` and `.log`;
- `chain.log`, with each step's own output in `step_*.log`. The chain, `run_qualification.py`, ran the steps one at a time, detached, and would have stopped at the first failing step.

**The bench check** is `tools/compare_s_records.py`, with its output `compare_s_records.out`. It runs every S plant through M8.15.1's frozen locator and through the locator v2, each in its own process, and compares the full records once § 1 item 4's fields and item 5's trigger are set aside. Nineteen of the twenty are equal; S10 differs, as registered. Its arm, one number in S1's record moved by `10⁻¹²` in a copy, is caught.

## The results

| Test | Outcome |
|---|---|
| S1 to S18c | 20 of 20 pass, each arm caught, with rule 11 passing at every step. Every S record but S10's equals M8.15.1's outside the new fields (the bench check). |
| S10, changed | Pass, arm caught. The tilted midpoint at 1.025 is passed, its structural-subspace failure recorded outside the clean window; the step is located as S1's and is not a branch step, so it is named "a located change of type". |
| A1 | Pass, three arms caught. All 14 cases are as tabled at both levels. The nine located ones read Elliptic and Hyperbolic on the registered sides, each root within `3×10⁻⁴` of its plant's, each shift within 0.2% of +0.50%, each named with the qualifier. |
| A2 to A29 | Each passes, and each arm is caught. Every outcome is as tabled. |
| R1, C2a/R4 | Pass, arm caught. A structural step at each level, with `Δn(L) = Δn_S = −2` and a genuine change of 0, as in RESULT_4: at level 3 the final interval 33.916 to 33.942, read to 34.071, root 34.042; at level 2 the final interval 14.243 to 14.252, root 14.252. Named "no genuine crossing detected" at both levels. |
| R2, C3/R4 | Pass, arm caught. No step at either level over 11.31 to 16. `n(L) = 9` at all 9 points per level. |
| R3 | Pass, arm caught. The forced failure at the first level-2 midpoint, `ε = 14.536`, is recorded with its three failed attempts, residuals `6.5×10⁻³`, `3.2×10⁻³` and `1.6×10⁻³`. The step is reported over `[14.243, 14.828]`, and the run exits normally. |
| R4, C3 and C2a | Pass. The driver's ladder and the extracted `decide` reproduce the qualification's branch records bit for bit: every type and reason, the cross-level records, and every point's data at both levels. The arm, `dlev = 0`, makes every C3 point Unresolved (level stability). |
| R4b | Pass. Each of the nine Unresolved reasons fires alone, the two passing pairs read Elliptic and Hyperbolic, and each binding's arm is caught. |
| R5 | Pass. The guard refuses a target in each of its eight registered cases, and in one more (the instrument's manifest no longer the pinned one). It passes when everything matches. Both arms are caught: the terms-hash check disabled passes the third case, and M8.15.1's whole predicate, restored from its own driver, passes with M8.15.1's terms and the instrument's `FROZEN.json` where the registered guard refuses. The write-once step wrote the guard and refused a second write. No real guard file was written. |
| RESULT_4 reproduced | Pass. Each of the five control records (C2a, C3, R3, R3's arm, R1's arm) equals its RESULT_4 counterpart value for value once § 4's fields are set aside: 0 differences in each. |
| The new branch | Never fires. No control step has a passed, exchanged-lift or step-ending midpoint, and none is a branch step. |
| Rule 11 | Passes at every control step. On C2a's two steps the statistic reaches `1.17×10⁻⁶` (level 3) and `2.63×10⁻⁶` (level 2), the register's `2.6×10⁻⁶` at its two digits. C3 has no step. The tolerance came from RESULT_4's records, which these reproduce, so this is a consistency check, not a test of it. |

**Which checks the arms broke.** Each arm fails the checks it targets, and the record lists them. Three examples:
- A1's tiered-names arm fails at the seven cases whose full cosine reaches 0.9 at every branch step, +1, 0.3 among them.
- A2's and A28's arm, every crossing classed genuine, never yields a genuine step: the bookkeeping check stops it. The arm is caught on the registered statuses, structural becoming Unresolved.
- A24's second arm, the span restricted to the step's final sub-interval, passes both steps, as UB predicted.

## The dry runs, unrecorded

The new code ran first on a scratch copy of the folder, as § 5 allows, with its records in that copy's `out/`.
- **The mock.** The synthetic suite passed, and every arm was caught. The S-record comparison, now the bench check, showed only S10 changing.
- **The controls.** R3, R3's arm and R1's arm ran on the real solver. Each record reproduced RESULT_4's value for value outside § 4's fields, and rule 11 passed at every step.
- **What changed after the first dry run.** No rule and no expectation. Four edits:
  - **A8's test** first required the structural subspace among the passed midpoint's checks, copied from S10's. A8 plants a slowest-pair failure alone, so the test now names each plant's own failed checks: S10's, A8's, and A19's two.
  - **A24's test** took the switch's entry and exit from the bracket's full point list, which also holds guard points when guards run. It now takes them from the step's own comparisons. The parent runs no guards, so its outcome is the same.
  - **`locate.py`** no longer writes a field naming the grid cell into the rule-10 record, which the register does not list. Four continuation lines were realigned.
  - **`tests/real.py`** stopped setting that field aside.
- **The final code** then passed the synthetic suite and the S-record comparison again before the recorded run.

## What the implementation adds, within the register

- **The arms act on code by named edits.** Each locator or ceiling arm recompiles one function from its source with stated replacements, and each replacement must match exactly as often as stated. So an arm changes what it names and nothing else, and an arm whose text drifts fails loudly.
- **One mock hook beyond § 1's list:** `n(B|G_tol)` too high at one point, which A11(b)'s registered plant needs.
- **A1's classes at +1, 1, level 2.** That step is not a branch step, so the frozen order stops at the identity check before the classes are written. The test reads its classes, mixed, from the two overlaps each crossing records.
- **R5's extra case** (the instrument's manifest no longer the pin) and its write-once check go beyond the registered list. Both test registered properties.
- **The S1 and S17 arms** wrap `analyse_step`, and now forward its new arguments.
- **`tests/real.py`** reports the three § 3 carries as three verdict lines over all five control records.

## What is not covered

- **No real-solver control exercises the new branch, the exchanged-lift pass or a path switch.** They are tested on the mock only, and clause 3 carries it.
- **The oracle is a counts-level model.** The locator reproduced every step, class and reason it registered. Guard readings are registered by type, not offset, except A14's lower guard.
- **The frozen assignment pairs across characters** once the clean ends' admixture angles sum past 45°. Such steps end Unresolved (A1 at `κ/δ` 1 and 2, and A2). That fails closed.
- **Very strong mixing ends Unresolved** when the first midpoint meets the clean interval before any failure, so the split applies (A27, and A1 at `κ/δ = 6` on level 2). That fails closed too.

## Next

1. **The units** confirmed this page and the diff (2026-10-13). Unit B's two optional notes are taken, and neither changes qualified code:
   - before the guard is written, the folder is checked against its frozen `SHA256SUMS`, so the guard pins the frozen code;
   - adjudication applies the ceiling with the function the tests verified, `tests/synthetic.py`'s `ceiling`, to the targets' records, so the adjudicated names and the tested ones come from one implementation.
2. **The terms,** a delta on M8.15.1's merged terms: the rule, its continuity check, clause 3, the brackets, the disclosure and REGISTER_5.
3. **The freeze:** the folder, with REGISTER_5, this page and the `scope/` folder, its manifest and `SHA256SUMS`, and the terms' hash on MIT main. Then the OpenWave filing (row M8.15.2) and the maintainer's go. Then the guard is written once, and the targets run.

## Dated note, 2026-10-13: the adjudication reading

After both units confirmed this page, their review of the terms added one file to the folder, `adjudicate.py`, with its check's output `adjudicate_check.out`. It applies the tests' `ceiling` function to a target's record as loaded from its JSON, reading the level keys as integers, the one difference between a record and the in-memory result the tests read (Unit B). Its check gives the in-memory names on all 70 synthetic results after a JSON round trip, and fails without the key conversion on each of the 25 that locate a change of type. No file the tests ran changed, and no result above changes.

*v1 written 2026-10-13, after the recorded run finished at 06:41:32Z; both units' confirmation recorded the same day.*
