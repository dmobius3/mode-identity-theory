# M8.17 development log

The census run's development record. Entries are appended, never edited. A correction is a new entry.

## 1. 2026-10-26T22:01:09Z: carried in from M8.16.1's log: the recon memo and the grouping check

Both were made under M8.16.1's log, before this task had an ID.
- **The recon memo, v2,** `census_run_recon_v2.md`, SHA-256 `76b129cac08ba8c19724b7765a539227ad558c8e4326e7ab8ee42d7563f3d4f1`. M8.16.1's `DEVLOG.md` entries 69 to 72 cover it, and entry 84 corrects one sentence: the five points M8.16.1 solved without reading carry no linear record, so their readings are this task's new evidence.
- **The grouping check,** `grouping_check.py`, SHA-256 `a69dd214142225177026de9b891102f65d04e9323ababdb9bd5b472839f4d19d`, and its memo, `grouping_check.md`, SHA-256 `f430c5fb6c644bf260471c5cdd9e33d5c436fd9173839cc59c73e78d3fe96cb4`. M8.16.1's `DEVLOG.md` entries 80 to 82 cover it. It is read-only on M8.16.1's outputs and reproduces the rule's recorded reasons at all 11 read Unresolved points. Its findings:
  - no link-tolerance merge at any of them (DERIVED); the control, T5J, is flagged;
  - at 9 of the 10 count changes, a same-sign eigenvalue lies just outside the closure's window (DERIVED), most of them read by proximity as the member the set lacks (INFERRED);
  - the non-contractions are eigenvalues still moving between `N = 24` and 32 at T5's larger amplitudes.

## 2. 2026-10-26T22:01:09Z: the pre-registration drafted, for review

On Blake's word ("go ahead with the census pre-registration draft"). `m8_17_task_details.md`, 3378 words, a delta on M8.16.1's terms, SHA-256 `2c16636070c900245d315c20512a48f2dc6f132de7f18130f34738c59a57f16e`.
- **The scope, from the catalog's statuses** (MIT `e09d453`, § III): 57 points never classified on any instrument, plus T2/R4's change of type, located:
  - T1 and T4 beyond M8.16.1's samples, 50 points;
  - T2/R4 at 16 and 22.63;
  - T3/R4 at 32;
  - T3/R5 at 16;
  - T5/R2 at 45.25, 128 and 132.

  T2/R5 owes nothing here. T3/R5 keeps M8.15.2's location.
- **The design:** the frozen instrument, rule and cutoffs 16, 24 and 32, unchanged. A point is classified when either instrument classifies it and neither contradicts the other. A locator bisects on `n(L)` to a relative width of `10⁻³`, with guard readings. Rows end under S4 and S6.
- **Facts read for it:**
  - M8.15's adjudicated types, from M8.16.1's `reference/m815_targets/`;
  - M8.16.1's timings, about 16 hours for this run;
  - the withheld points' stored fields;
  - the census page's § II, § V and § VI.

**Next:** the units' review.

## 3. 2026-10-26T22:29:41Z: the units on v1; terms v2

On Blake's word ("go on v2 if/when gucci w/"), after both units' reviews of v1 and of the plan for v2.

**N = 40 stays out,** on Blake's decision, with both units now agreeing. v2 states the consequence for T5's upper window and leaves S6 to the census page.

**T3/R5 is dropped,** 57 points to 56. M8.15.2's record (MIT, `soft-slot-dynamics-m8-15-2/RECORD.md`, its guard table) locates the change between its guard readings: Elliptic at 15.6356 and Hyperbolic at 16.5832 at level 3. The upper guards at 15.9515 and 16.1094 read Unresolved, and the record says the evidence "does not place it at the interpolated zeros". So `ε = 16` lies inside the location, and any reading there is consistent with it. Both units had treated the `n(L)` interval as the location; both now agree.

**Adopted, each verified at source:**
- **Reproduction (UB, FATAL as written in v1).** Amendment 5's ladder against the registered C2a/R5 sample agrees exactly at 0.25, and differs at 0.5, 1 and 2, by 2.4×10⁻¹² to 9.0×10⁻¹¹ in `λ`, with the group centres different at every cutoff. So exact equality holds only where this run retraces M8.16.1's steps, and categorical equality is asked at T1's and T4's 0.5, 1 and 2.
- **Classification (UB):** "converged" is the rule's verdict (`checks.reading`), not `checks.converged`, which asks the expected type. Branch identity between `N = 24` and 32 is required, as `run/driver.py`, lines 312 to 326, computes it. K1 is checked at every point, since `check_row_k5` checks it at `ε = 0.25` only (UA).
- **The locator:**
  - the brackets, type and index, defined apart;
  - each cutoff's bisection completes at `w/2`, so the union is narrower than `w`;
  - every unsuccessful stop is named, and none can yield Located;
  - each midpoint is solved from both ends, the two solutions agreeing to branch identity's `10⁻²` with the same `n(L)`;
  - branch identity applies at grid points and guards;
  - each guard continues from its own end and stays inside the window;
  - a type change with no `n(L)` change takes UA's wording, with the location OPEN.
- **Row outcomes (UA, UB):** a point between a located change's guard readings is accounted for by the location. The record names each limitation and its cause and declares no row closed under S6.
- **T2/R5's reading** is named a known outcome (UB).

**Corrections** of M8.16.1's log entry 84 and of the recon memo, on `m` and the aggregates: M8.16.1's `DEVLOG.md`, entry 85.

**The terms, v2:** 4138 words, SHA-256 `53f48ceb92e0b39a9df64875217a3eb9f50d3f3fee376cfe8454112b441a3f09`. The diff from v1 is `m8_17_v1_to_v2.diff`. The estimate is about 14 hours.

**Next:** the units on v2.

## 4. 2026-10-26T22:38:21Z: the units on v2; terms v3

Blake relayed both units ("Feedback from the units on v2:").

**UA:** HOLD on (c) and (f), and GO on the rest. UA's terms file hash matches entry 3's.

**UB:** GO on every item, once one sentence v2 dropped goes back in. UB ran test 3's categorical comparison on its named data, and it passes.

**Adopted, each verified at source:**
- **T3/R5 (UB).** v2's bracket definition, with v1's sentence on M8.15.2's location removed, would have caught T3/R5. Its change crosses the unclassified point at 16, so the row would end "not settled", against § THE POINTS. The sentence is back as the first bracket bullet, and § THE ROW OUTCOMES names T2/R5's and T3/R5's outcomes on known outcomes.
- **The locator's upper end (UA).** The bracket could be (22.63, 32), and no solution vector is stored at 32. So the path recomputes a known end, which passes the reproduction gate before any inward continuation. A missing or nonreproducing end is an unsuccessful stop. T2/R4's path now runs to its type bracket's upper end, at most 32.
- **The signed `Δn(L)` (UA).** `N = 24` and 32 must agree on it, and it must not be zero.
- **The withheld points' reproduction (UA).** The four points this run computes carry only solve and acceptance fields. The gate now has three rules: full equality for points M8.16.1 read, solve-field equality at the withheld points, and categorical equality at T1's and T4's changed steps. Test 3 adds the withheld-point comparison on the stored solves.
- **NITs:**
  - the run-outcome wording (UA);
  - the sealing wording, the 56 first-time readings and the four withheld points (UA);
  - test 3's note on Krein counts, which C2a/R5's records do not carry, all empty, as checked (UB).

**The terms, v3:** 4429 words, SHA-256 `f96379993dd4dc09f23cb776c5173bf2c228a2cf5a13684d009732dab37eaa81`. The diff from v2 is `m8_17_v2_to_v3.diff`. No scope, cutoff or bar moved.

**Next:** the units on v3.

## 5. 2026-10-26T22:44:40Z: the units on v3; terms v4

Blake relayed both units ("Feedback from the units on v3:").
- **UA:** GO on every item but (c). UA reapplied the v2-to-v3 diff, which reproduces both files byte for byte.
- **UB:** GO on every item, once one cell is fixed. UB's hash of v3 matches entry 4's, and UB checked the withheld points' stored fields against the second reproduction rule.

**Adopted, each verified at source:**
- **T2/R4's path (UB).** "To its type bracket's upper end" depends on readings the path itself produces. A Hyperbolic reading at 16 would have stopped it before 22.63, one of the 56 points. The cell now reads: the grid to 22.63, and on to 32 where its type bracket is (22.63, 32).
- **Missing index is not unchanged index (UA).** v3 called every type bracket that is not an index bracket "a type change with no `n(L)` change", but an end can lack a resolved `n(L)`. v4 separates the two cases:
  - resolved and equal: the index locator is inapplicable, and the location is OPEN;
  - missing, unresolved or inconsistent: the index evidence is inadequate, not evidence of no change.

  Neither is located, and neither claims S6. Test 4 keeps the cases apart.
- **One consistency change of mine,** which UA's fix needs: the index evidence is judged at `N = 24` and 32, the cutoffs that decide a location, and `N = 16` is bisected where its ends allow and reported otherwise, as v3 already made it a diagnostic.
- **NIT (UA):** the opening now says each row's outcome is recorded, with its S4 completion stated separately.

**The terms, v4:** 4544 words, SHA-256 `2d933f585f99e1f6961b675b1ccde90dff960cc62693ad9e44a1de16c6409c0c`. The diff from v3 is `m8_17_v3_to_v4.diff`.

**Next:** the units on v4. With both GO, the code and the tests before the freeze follow, each on Blake's word.

## 6. 2026-10-26T22:51:04Z: the units on v4: GO from both; the terms' design closed

Blake relayed both units' reviews, with no words of his own, so this entry records them and changes nothing.
- **UA:** GO on every item, with no further redlines. UA's word count, hash (`2d933f58…`) and diff match entry 5's. UA authorizes, for its part, the next stage: the driver, the classification reader, the locator, the reproduction guard and the tests before the freeze. The freeze, the filing, any sealed reading and the run are not authorized.
- **UA's implementation check, nonblocking.** Test 4 adds a synthetic case where `N = 16` disagrees, or lacks an index, while `N = 24` and 32 meet every deciding condition. It must stay eligible for Located, with `N = 16`'s discrepancy reported.
- **UB:** GO on every item. UB checked that every type bracket falls in exactly one of the three cases, and that an end classified by M8.15 alone may lack a resolved `n(L)` on this instrument. UB's scan of the full text finds no wording left from earlier versions.

**The terms stand at v4,** SHA-256 `2d933f585f99e1f6961b675b1ccde90dff960cc62693ad9e44a1de16c6409c0c`, as the text the build implements. A change to any word of it reopens the review.

**Next,** on Blake's word: the build and the tests before the freeze, with the code and its evidence to the units before any freeze.

## 7. 2026-10-26T23:58:28Z: the build and the tests before the freeze

On Blake's word ("go on the build"), within UA's authorization of entry 6: the driver, the classification reader, the locator, the reproduction guard and the tests before the freeze. Nothing is frozen or filed, no sealed reading is opened, and nothing under `run/out/` exists.

**The folder,** `census_run/soft-slot-dynamics-m8-17/`, laid out as M8.16.1's:
- this log at its root;
- the terms and their three diffs under `registration/`, and the recon memos and the grouping check under `dev/`, each moved with its bytes unchanged, at the SHA-256 entries 1 to 5 record;
- the packets and their zips stay in `census_run/`.

**The copies,** by `tools/copy_from_mit.py` (`394e642663896f47e47ad8f7bf83b3930105fce9d0b3ed24eb894cf4e2355007`), from MIT's git objects at their named commits. Each is checked against the record that pins it. `reference/SOURCES.json` (`8833e7e9376f2b93c80a027feb7a798242d3b272a1d56dfb7b6b3d2acc6e8e90`) lists all 52, each with its commit, path, blob and SHA-256:
- `instrument/`, 12 files, and M8.16.1's `run/cases.py`, `seeds.py`, `driver.py`, `checks.py`, `next_order_values.json`, `pin_manifest.py` and `record_environment.py`, at `d1c0ec8`: each equals its blob at `292b158` and the SHA-256 that commit's SHA256SUMS lists;
- at `292b158`, M8.16.1's outputs of the nine rows, its controls and pyramid, its run log, its FROZEN.json and its filed terms, 47,420 bytes, each against the pin its run log, FROZEN.json or SHA256SUMS records;
- M8.15's five records, as M8.16.1 copied them; M8.16's controls and pyramid, at `87fc643`; amendment 5's ladder; and M8.15.2's T3/R5 record, at `f1ebda7`, against its `RECORD.md`'s table of outputs.

**The code,** new:
- `run/census_lib.py` `88def7ebbfef2d5183778efeaacc6b4a2b895969aa3ee173c555e16e47d2dc5b`: the points, the reproduction's three rules, classifying a point, the brackets, the locator (`locate`, which takes the instrument as an argument), the row outcomes and the record;
- `run/census.py` `32ca2a525b991e401a22ccca045f7c92cbe60764d9d3ec86d7b5090143e3b143`: the run, M8.16.1's `driver.run_case` on each row's path, then the locator on the instrument;
- `run/write_guard.py` `ca4b9dc21163564f31cbf78b1776114c5203edaf0de6792dbbb0517fe393fd19`: the freeze's writer, not run.

**The tests before the freeze,** each run as `python3 -I -B` in a seedcheck process, where every solver and record path refuses, with no solve:
1. `run/test_constants.py` `ee4d19a6086e8b54f30bbdf3d2cdb7a7b6597e87393724bbba3f65518360381e`, run on `registration/m8_17_task_details.md`; output `run/test_constants.out` `edee4f0324d14110bd09d99be3e21c10baef060ab8b9924cf079462df1de96bd`:
   - PASS: the forward items, 61: 28 of kind (a), 27 of kind (b), 6 of kind (c)
   - PASS: coverage: 244 numbers, 71 references or names, the rest each claimed once
   - PASS: the reverse scan of census_lib, census, write_guard: every literal on exactly one list, no entry stale
   - arms A1 to A4 red.
2. `run/test_reader.py` `1519d5f2c494658511f90a3389d03ffc947bbfaa764acc88d7bbfbf2b7651c40`; output `run/test_reader.out` `2c23ef352411787f97d2a3bfb71c4b2f2f8d7e2de3b04f26b0e4d1aab1169cce`:
   - PASS: the rule replayed on the stored summaries equals the stored reading at 95 of 95 read points
   - PASS: K6 reproduced: 79 points decided and read, 11 Unresolved here; classified by {'this instrument': 16, 'both': 68, "M8.15's": 11}
   - PASS: the first-time readings from the records alone: 56 on the run's rows, equal to census_lib.NEW, and T3/R5's 16, inside M8.15.2's location (15.6356, 16.5832)
   - PASS: refused 200 of 200: the 56, T3/R5's withheld 16, and every grid interval's midpoint
   - PASS: every run row's seed refused, the census driver refused, and the solver and record paths refused in this process
   - arms A1 to A3 red.
3. `run/test_gate.py` `8452e2862267d44662394a114a9b367bc5cbba9cf14c539309202823b71f2d4a`; output `run/test_gate.out` `62fd6ebf90325f9f662605a9f8f8538c34409e4074c483d03fab4fbdad5f6d35`:
   - PASS: rule 1 at 23 points of the controls and the pyramid: M8.16.1's equal M8.16's; the whole points, readings and identity, C1's N = 40 included: 0 differences
   - PASS: rule 3 holds at 0.5, 1 and 2 on the ladder against the sample; beside it, rule 1 holds at 0.25 (0 differences) and fails at 0.5 (11342 differences), 1 (11727 differences), 2 (12189 differences)
   - PASS: rule 2 at the five withheld points, each record carrying spectral fields beside the stored solve
   - mutations: rule 1, C2a at 0.25: 18540 leaves mutated, 0 passed; a field added and one removed fail; rule 1, P5 at 0.25: 16723 leaves mutated, 0 passed; a field added and one removed fail; rule 3, the ladder at 0.5: 35 categorical fields mutated, 0 passed; a Krein count added fails; rule 2, five points: 180 mutations and removals, 0 passed;
   - PASS: a timing changed, rule 1 passes; a timing changed, rule 3 passes; lam changed, rule 3 passes; a spectral field changed, rule 2 passes
4. `run/test_locator.py` `310f3cd8390f031bbb9aef7bef6fe315c1e7baab069832507279eebab0ea5bea`; output `run/test_locator.out` `271ce8d19bc59d819e39adf5e7e57392b40f7ca9ab377a0adc2e2b6e0726a445`:
   - the baseline located, with its name;
   - 24 arms, each condition of the terms' list with a mutation that lets its counterexample through, and UA's case, `N = 16` failing alone, located from `N = 24` and 32;
   - the record end to end, R1 to R5, on synthetic outputs beside the known outcomes: T2/R5 ends Elliptic throughout and T3/R5 with its change located, on the known outcomes alone.

**A plumbing pass,** development, not a registered test: `dev/plumbing_census.py` `0c75b9c36d8125f66a543f6390a3a583e73f13ef2c4bcef5f92b07f530894709`, on the GO-list control C2a at cutoffs 12, 16 and 20, which the run never uses; output `dev/plumbing_census.out` `34f07b7210913c7d4bfc8d8de1c705e2eaf102cbef61d50935acd2acfd78d71b`. It checks the instrument's side, which no test before the freeze can solve:
- eps 0.5: the recomputed path against run_case: 0 differences, and likewise at 0.25 and 0.354: the recomputed path reproduces `run_case`, field for field;
- `census_lib.locate` runs whole on the instrument;
- bisect at N = 20: 10 midpoints, complete True, interval [0.49985698573300125, 0.5], largest two-ends distance 6.96e-07, K1 at every midpoint True; 122 s;
- the guards run on both sides at both offsets. At these cutoffs the rule reads C2a Unresolved at its grid points, non-contracting above the floor, so the guards are unclassified by the rule alone. The pass's first version expected them classified; that expectation was mine and wrong, and the corrected check is the one above.

**Readings the build makes, for the units** (each stated in the code):
- **The stop falls at a row's end.** `run_case` returns a whole row, so a point that does not reproduce stops the run when its row completes, and none of that row's readings is classified.
- **A bracket end beyond a row's path.** The locator recomputes each end on the registered grid path from the seed, reading every point as `run_case` does. Every recomputed point must then equal this run's record of it or M8.16.1's, field for field. That covers T2/R4's 32, which its path cell names, and T3/R4's 45.25, which its cell does not: if T3/R4's 32 reads Hyperbolic, (32, 45.25) is a type bracket. The build reads "the registered path recomputes that end" as covering it. The other reading leaves that end missing, and the change not located.
- **The terms' place in the tree.** `devtools.frozen()`, byte for byte, reads the terms at `run/m8_16_task_details.md`. At the freeze, this task's filed terms go there, under M8.16.1's file name.
- **`n(L)` resolved:** solved and accepted at the cutoff, with no `n(L)` item among the record's unresolved.
- **Overlap:** two intervals overlap when their interiors meet. Intervals that only touch put the two cutoffs' changes on opposite sides of a point both cutoffs sampled.
- **The two-ends agreement:** the solution continued from the upper end, against the one from the lower end, with the orbit tangents taken at the lower one.
- **Categorical equality:** "indices" reads as `n(L)`, `n(D)`, `K` and `K`'s parts; the rule's type is compared beside its verdict.
- **The order:** T2/R4, T3/R4 and T5/R2 first, whose paths are mostly known points, so that a reproduction failure shows early; then T1 and T4; then the locator, in row order.
- **The guards:** both are read whenever the location's first conditions hold, and every failing condition is named.

**The estimate, revised.** Recomputing a bracket's path adds its row's solves up to the bracket's upper end. For T2/R4's (22.63, 32), that is about 1.4 hours, from M8.16.1's timings at `N = 32`. In the pass, a midpoint's solve took about what a grid step takes. So the run is about 15 to 16 hours if that is its only bracket. Each further bracket adds about 2 to 5 hours, depending on its row and its end.

**Next:** the units' review of the code and this evidence. The freeze, the filing, any sealed reading and the run each need a separate go.

## 8. 2026-10-27T00:37:28Z: the units on the build; three corrections

On Blake's word ("continue when gucci w/"), with both units' reviews of the build and of the plan for these corrections.

**The units on entry 7:**
- **UA:** GO on the build and on all nine readings, with no blocking finding. UA reran tests 1, 2 and 4, checked the 52 references' SHA-256, and rehearsed the freeze on a temporary copy: v4's terms at the inherited path, a manifest pin, a FROZEN.json, and `census.frozen()` admitting the seven run rows.
- **UB:** GO on (a) to (i), with one FIXABLE and two NITs. UB ran `copy_from_mit.py` against a clone of MIT, and all 52 copies are equal. UB reran tests 1 to 4 on a copy, each output byte-equal, test 3's at `62fd6ebf…`. UB reran the plumbing pass, equal apart from timings and real parts below 10⁻¹⁴.

**Adopted, each verified at source:**
- **(a) The stop is global (UB; UA's first observation).** Entry 7's reading (a) understated the code. On any stop, `census.py` records no row, so no reading of this run is classified, including the rows before the stop. The code keeps that. What a stop keeps and what it withholds, as UA asks:
  - each completed row's records, written to its case file before its reproduction is read, the stopped row's among them;
  - any locator job completed before the stop, with its file and its entry in the run's log;
  - neither is classified after the stop.

  The record names them: `CENSUS.json`'s `unclassified`, from `census_lib.stopped(log)`, UB's function as given, lists every completed job's files with their SHA-256 and a row's first-time points, with the cause "the run stopped; the records are kept, and the classification is withheld". UB's first replacement set it on every run, which would have marked a completed run's rows as stopped. It is set after a stop only, and a completed run's is empty. `census.py`'s docstring now says so.
- **(c) The terms' path is inherited (UB).** Line 376 of M8.16.1's terms places the filed terms at `run/m8_16_task_details.md`; it is not a reading of this build. `write_guard.write()` now refuses unless that file equals `registration/m8_17_task_details.md`, byte for byte.
- **(i) A 25th arm (UB):** each guard continues from its own bracket end. From above, the upper guards read Unresolved; from below, Hyperbolic. The real code reads no upper guard classified and does not locate. The mutant continues the upper guard from the lower end, through the change, and locates it.
- **Tests of the stop record and the guard (UB's FIXABLE and NIT):**
  - R6, in test 4: a log that stops in a locator job names all seven rows, each with its first-time points, and that job's file; one that stops at T3/R4 names T2/R4 and T3/R4; the same without its stop gives nothing;
  - claim 4 and arm A5, in test 1: on a temporary copy, with the terms placed with one byte changed and the copy's manifest pinned, `write()` refuses and names the terms; with the terms placed exactly, it writes FROZEN.json and its pin in the copy.
- **Two additions of mine:**
  - a 26th arm in test 4, which removes `stopped()`'s stop condition, so the mutant marks a completed run as stopped;
  - in claim 4, the written copy is admitted by `devtools.frozen()` and by the copy's own `census.frozen()`, run in a process of its own, with the seven run rows: UA's rehearsal, made a test.
- **UA's procedure:** once the manifest is pinned, nothing under `run/` is rerun or rewritten. Any rerun runs in a scratch copy. The tests' outputs are deterministic: tests 1, 2 and 4, each run twice on these files, give byte-identical outputs.

**The files after the corrections:**
- `run/census_lib.py` `4873006e94e09bdf1b03396e2e9e85881ce503d2def0a2036858691706d6a321`;
- `run/census.py` `f4c60943215bea341656638ec431ee79206d0561fd266906b018196cfdb5421d`;
- `run/write_guard.py` `394b2f138a28b641e301a36607722d9a7832ca011c9df7ecea3e4de1a07417ba`;
- `run/test_constants.py` `81c17ef71c8072555be7e497b246c5a191c23bda5f1ad2d609d139427bd6f3ae`;
- `run/test_locator.py` `a80ee133112468c703aa48463e01410fdb446b785047d3d0297001dc71d788a2`.

**The tests, all four rerun, since `census_lib.py` changed (UB),** each as `python3 -I -B` in a seedcheck process:
1. `run/test_constants.py`; output `run/test_constants.out` `5a53308e81936581cf5cc1239d7ee670bb4147ee8b8c881598b86212055ab881`:
   - PASS: the forward items, 61: 28 of kind (a), 27 of kind (b), 6 of kind (c); PASS: coverage: 244 numbers, 71 references or names, the rest each claimed once;
   - PASS: the reverse scan of census_lib, census, write_guard: every literal on exactly one list, no entry stale;
   - PASS: the freeze writer on a temporary copy: exact terms: FROZEN.json written in the copy, admitted by devtools.frozen() and by the copy's census.frozen(), allowlist ['T2/R4', 'T3/R4', 'T5/R2', 'T1/R4', 'T4/R4', 'T1/R5', 'T4/R5'];
   - arms A1 to A5 red.
2. `run/test_reader.py` `1519d5f2c494658511f90a3389d03ffc947bbfaa764acc88d7bbfbf2b7651c40`, unchanged; output `run/test_reader.out` `2c23ef352411787f97d2a3bfb71c4b2f2f8d7e2de3b04f26b0e4d1aab1169cce`, unchanged from entry 7.
3. `run/test_gate.py` `8452e2862267d44662394a114a9b367bc5cbba9cf14c539309202823b71f2d4a`, unchanged; output `run/test_gate.out` `62fd6ebf90325f9f662605a9f8f8538c34409e4074c483d03fab4fbdad5f6d35`, unchanged from entry 7.
4. `run/test_locator.py`; output `run/test_locator.out` `af817a26aff21ed883a775f14c07c4cdfdb39921cef142bd7ca66579831e133d`: 26 arms, the baseline, UA's `N = 16` case, and R1 to R6, all passing.

The plumbing pass is not rerun. The functions it calls, `census.Cutoff`, `readings_of`, `aligned`, and `census_lib`'s `locate`, `bisect` and `guards`, are unchanged; the corrections touch `stopped()`, `main()`'s record and `write()`.

**Next:** the freeze-and-filing packet, which both units authorized. The freeze, any commit, the filing, the sealed readings and the run each need their own go.

## 9. 2026-10-27T00:49:53Z: the freeze-and-filing packet

Both units authorized it in entry 8's round, and Blake's word ("continue") covers it. Nothing is frozen, committed or filed, and no sealed reading is computed.

**The terms, v5,** `registration/m8_17_task_details.md` `2cd6de8a2f5ff5b1a3d6ce0d2941b81b52ee4c4efcb931f4f7080b1da6c3df57`, 4,574 words. v5 is v4 with two changes and nothing else, in `registration/m8_17_v4_to_v5.diff` `2d3424c54eb43d3c4eaf2eb248075e08f9b83937d2e97412e47334049f982b92`:
- the opening's "draft v4" goes, since M8.16.1's filed text opens "Pre-registration, for review.";
- the estimate is the build's (entry 7): about 15 to 16 hours, about 4 of them for the locator on T2/R4's change, and about 1 to 6 more for each further bracket.

Neither unit has seen v5's bytes; the filing plan asks for them.

**New code, under the manifest:**
- `run/freeze_block.py` `74128b75dbbdcf990274e921355b8b9e5decf0cb075c864c86eda76f5d9f158d`: M8.16.1's builder, without its seed section, since M8.17 adds no seed and the run checks each row's seed as `run_case` does. It records the terms, the go, the manifest with both pins, the environment as recorded and read again, every reference file, what is inherited from M8.16.1, the census values, `FROZEN.json` in full and the order. It builds only after `census.frozen()` admits the tree.
- `run/test_freeze.py` `cbebb59fce6430c012399de6ad0b17d0beafed0c50d5a1f5b73e17ccd8eb392b`: the guard procedure rehearsed end to end on a temporary copy, never on this folder. Output `run/test_freeze.out` `43fd45b446a4bb7df8177042c87f74beab4682ee7ee2a8f4972b2617c7350da5`, byte-identical across two runs:
  - PASS: the filed terms in run/, equal to registration/'s, SHA-256 2cd6de8a2f5ff5b1a3d6ce0d2941b81b52ee4c4efcb931f4f7080b1da6c3df57;
  - PASS: the manifest pinned, the terms and the environment record among its files, and recomputed equal to the pin; a second pin refused;
  - PASS: FROZEN.json and its pin written once; a second write refused;
  - PASS: devtools.frozen() and the copy's census.frozen() admit it: ['T2/R4', 'T3/R4', 'T5/R2', 'T1/R4', 'T4/R4', 'T1/R5', 'T4/R5'];
  - PASS: the freeze block: the terms' SHA-256, the go, both pins, every manifest line once, no environment difference, the 34 reference files, FROZEN.json in full and the order;
  - seven arms red, each a change after the freeze that `census.frozen()` refuses. Two are forged `FROZEN.json` files with their pins rewritten to match, one cutting T2/R4's path short and one changing `w`: `devtools.frozen()` admits both, and `census.frozen()` refuses both.
- `run/test_constants.py` `523138be968baf738ec6d7bed8f670ae2d560cec921a55ba43cf0056e4ac02f1`: its scan now reads `freeze_block.py`, and its items follow v5's estimate. Output `run/test_constants.out` `42037a495fdcba88b158e9e3cd4a1fc8b1736e93a9684b034bb64b30402c993d`:
  - PASS: the forward items, 63: 28 of kind (a), 28 of kind (b), 7 of kind (c); PASS: coverage: 248 numbers, 71 references or names, the rest each claimed once;
  - PASS: the reverse scan of census_lib, census, write_guard, freeze_block: every literal on exactly one list, no entry stale;
  - claim 4 and arms A1 to A5 as in entry 8.

Tests 2 to 4 read nothing these changes touch, and their outputs stand: `run/test_reader.out` `2c23ef352411787f97d2a3bfb71c4b2f2f8d7e2de3b04f26b0e4d1aab1169cce`, `run/test_gate.out` `62fd6ebf90325f9f662605a9f8f8538c34409e4074c483d03fab4fbdad5f6d35` and `run/test_locator.out` `af817a26aff21ed883a775f14c07c4cdfdb39921cef142bd7ca66579831e133d`.

**The plan,** `../FILING_PLAN.md` `65aa2b6f8ac591edca127811ea28449b8884496b93ca2952c51d4474f853ddc9`. It is M8.16.1's filing, step for step: MIT through the pin and the local commit; the push on Blake's word; OpenWave's branch on Blake's word after it; the freeze and the run after the merge. Facts read today for it:
- MIT `origin/main` is still `e09d453`, the terms' base, and `tools/copy_from_mit.py` finds all 52 copies equal.
- OpenWave `upstream/main` is at `0567ec74`: #655 to #659 since #654, all M5. No M8 file has changed, "M8.17" occurs nowhere upstream, and no pull request is open.
- **The scan** of the folder's 80 files finds no local path, home folder, email, credential or session internal. A control string is found in 24 files, and `check_no_local.py --require-files` is clean, reading 70.
- The live environment equals M8.16.1's record in every field apart from the time.
- The manifest holds 33 files today, and the pin will cover 35, with the placed terms and the environment record.

**The drafts,** `../filing_drafts/`, 6 files: `REPRODUCE.md`, `census_note.md`, `commit_mit.txt`, `commit_openwave.txt`, `m8_roadmap_edits.md`, `pr_body.md`. On a scratch copy of the roadmap at `0567ec74`, the four edits leave `check_roadmaps.py` clean, at +4 −3. The row's title is 5 words and its description 58, by the checker's own count, and a description 20 words longer fails it. The pull request's body closes with the reviewer's minor-corrections line.

**Next:** the units' review of the packet. Step 1 then waits for Blake's word.

## 10. 2026-10-27T01:20:25Z: the units on the packet; the fixes; terms v6

On Blake's word ("make the fixes and I'll send back to the review units"), after both units' reviews of entry 9's packet.

**The units on the packet:**
- **UA:** GO on (a) v5, (b) `freeze_block.py` and (c) the rehearsal; HOLD on (d), step 6, and on `REPRODUCE.md`'s instructions in (e). Tests 1 and 5 copy the whole folder and then place the terms and the pin by exclusive create, so after step 5 both raise `FileExistsError`; UA reproduced it in both. UA would keep the test code and run both tests before the pin only.
- **UB:** HOLD on (a), (c) and (d), each with a FIXABLE; GO on (b) and (e), with NITs. UB found the same defect, and an estimate too low for brackets in `R5`. UB rebuilt v5 from the diff, reran tests 1 to 4 byte-equal, ran steps 3 to 5 on a copy, and checked the roadmap's edits and the scan.

**Adopted, each verified at source:**
- **The defect.** On a scratch copy carrying the placed terms, the environment record and the pin, both tests raise `FileExistsError`. UB's fix is in:
  - tests 1 and 5 leave the folder's freeze files out of their own copies: the placed terms, the environment record, the pins and `FROZEN.json`;
  - the rehearsal checks that the folder's freeze files are as they were, rather than absent;
  - test 1's claim 4 makes the same check, in place of "no `FROZEN.json` in the folder", which would fail on the published, frozen folder. That last change is mine.

  UA's alternative, running both tests before the pin only, would leave `REPRODUCE.md`'s promise false on the filed folder. UB's fix keeps one procedure, and both tests still start from the unfrozen state they rehearse.
- **The dress rehearsal (UB):** before step 1, steps 3 to 5 and then the five tests on a scratch copy, outputs byte-equal. The record names each test's snapshot (UA).
- **The estimate (UB).** From M8.16.1's timings, a bracket costs its row's path to its upper end, plus 22 solves at each cutoff there:
  - in `R4`, 1.6 to 5.6 hours;
  - in `R2`, 1.9 to 2.2, at the upper ends a T5/R2 bracket can have;
  - in `R5`, 3.6 to 9.3, of which 5.6 to 9.3 above `ε = 2`.

  T2/R4's (22.63, 32) is 4.4, as UB has it. UB's "6 to 9" for `R5` counts upper ends above 2 only, while T1 and T4 in `R5` can bracket below 2. So v6 says about 2 to 6 in `R4`, about 2 in `R2` and about 4 to 9 in `R5`.
- **The NITs (UB):**
  - the rehearsal checks the freeze pin in the block, not only the manifest pin twice;
  - its docstring names steps 3 to 5;
  - `SOLVER_COMMIT` is step 11's commit;
  - the plumbing pass also differs across machines in real parts below 10⁻¹⁴;
  - the pull request says "every nondegenerate row born elliptic".
- **UA's optional point** goes to Blake: the MIT commit's author address, which 1,158 of MIT's commits already carry.

**The terms, v6,** `registration/m8_17_task_details.md` `667159c3db993396a10a75775acf79e78f744d161c641ebc37c9e6baf3af7cea`, 4,587 words: v5 with the estimate's last line changed and nothing else, in `registration/m8_17_v5_to_v6.diff` `d30d0b0f16ae1f9a3773e5b61cdd8d53d2d84724cbb0e4ddd008573fc91ffde1`.

**The tests, rerun to verify the fixes,** each as `python3 -I -B`, on the bench folder:
- `run/test_constants.py` `0fc55fb2a2a1b8b92c4aa9279958937f54edbe38dd1a46cc56bf5077fe6167b4`, with v6's estimate items; output `run/test_constants.out` `a7bc641368360c891ce2bd2f3b2aee1ee7236209ad7ae759c9f26b94b58489ea`:
  - PASS: the forward items, 63: 28 of kind (a), 28 of kind (b), 7 of kind (c);
  - PASS: coverage: 251 numbers, 71 references or names, the rest each claimed once;
  - claims 3 and 4 and arms A1 to A5 as before.
- `run/test_freeze.py` `a3a8290338bc42926b56772f701d59cc090625f010e6f0add6c37f8c9fefbc7d`; output `run/test_freeze.out` `0d8ac70d99e1cb7485dbeb0ae728b6c4ad5471c7c0a7fb3eee296e7777a3ae58`:
  - steps 1 to 6 and arms A1 to A7 as before;
  - the folder itself: untouched.

On a scratch copy carrying the placed terms, the environment record and the pin, both tests pass. Each output is byte-equal to the bench's, and the copy's manifest still equals its pin afterwards. Tests 2 to 4 read nothing these changes touch, and their outputs stand. The full dress rehearsal, with test 3, is the plan's step before step 1.

**The plan, v2,** `../FILING_PLAN.md` `1e53bb5ab3be2abe0080e87dd564420fae83ec0a915d15b6d32505ba67930c37`: the dress rehearsal, step 6 on the pinned folder with all five tests, the snapshots recorded, `SOLVER_COMMIT`, and "The units on v1". The scan of the folder's 81 files is clean, and `check_no_local.py` reads 70.

**The drafts,** `../filing_drafts/`:
- `REPRODUCE.md`, which notes that tests 1 and 5 leave the folder's freeze files out of their copies, with the plumbing line and the resources line;
- `pr_body.md`'s "nondegenerate";
- `census_note.md`, whose terms are dated by this entry.

**Next:** the units on the v2 packet; then the dress rehearsal and step 1, on Blake's word.

## 11. 2026-10-27T01:45:58Z: the units on v2; the dress rehearsal; step 1 begins

On Blake's word ("keep moving if/when good w/"), with both units' GO on the v2 packet.

**The units on v2:**
- **UA:** GO on (a) to (e). UA withdraws its pre-pin-only alternative and accepts UB's fix, and exercised the copies' exclusion on a synthetic pinned copy. UA reconstructed v5 from the v5-to-v6 diff and checked v6's hash and word count. UA authorizes the dress rehearsal and the local MIT preparation on Blake's go; the production pin, the commit, the push, the pull request, the production `FROZEN.json` and the sealed readings each need their own. One NIT: three of the plan's references still said v5.
- **UB:** GO on (a) to (e). UB reran its estimate model over every possible upper end and now matches v6's line. UB ran the dress rehearsal by hand on a copy, with `record_environment.py`'s macOS reads stubbed, and all five tests were byte-equal. One NIT for after the freeze, needing no change now. On a frozen copy, test 2's claim 6 fails by design: it asserts the unfrozen state, and on a frozen tree the run rows' seeds build and `census.frozen()` admits it. When the run's record edits `REPRODUCE.md`, it says that test 2 runs on a copy without `run/FROZEN.json` and `run/FROZEN_PIN`, or claim 6 gets tests 1 and 5's treatment.

**Adopted:** UA's NIT, in place. Step 3 now names v6 and its five diffs, and step 14 v6. `../FILING_PLAN.md` `bbb1c34d1ab727391f236645de7bd838e944a3cae44777bdce11327485241cfd`. UB's NIT is queued for the run's record.

**Blake, on UA's optional point:** the MIT commit keeps its author address, `blake@Blakes-MacBook-Air.local`.

**The dress rehearsal,** on a scratch copy of this folder, never the folder itself: steps 3 to 5 as written, then step 6's five tests, run as `python3 -I -B`. Its transcript:
  - the copy: 81 files
  - step 3: the terms placed in run/ by exclusive create
  - step 4: ENVIRONMENT.json written; --check: no difference
  - step 5: MANIFEST_PIN written over 35 files
  - step 6, test_constants: exit 0; output byte-equal to the folder; 7 s
  - step 6, test_reader: exit 0; output byte-equal to the folder; 6 s
  - step 6, test_gate: exit 0; output byte-equal to the folder; 550 s
  - step 6, test_locator: exit 0; output byte-equal to the folder; 4 s
  - step 6, test_freeze: exit 0; output byte-equal to the folder; 9 s
  - the copy's manifest after the tests: equal to its pin
  - the copy holds no FROZEN.json and no FROZEN_PIN: True
  - 0 failed

**Next:** step 1 of the plan, through the local commit, which is not pushed.

## 12. 2026-10-27T01:54:37Z: the filing, steps 1 to 5: the pin

On Blake's word ("continue if/when gucci w/"), with UB's ruling on the scan's one hit.

1. **The sync.** MIT fetched: `origin/main` is `e09d453`, the terms' base, and the worktree is clean at it. `tools/copy_from_mit.py`, rerun against the fetched clone, finds all 52 copies present and equal, each with its pin, and `SOURCES.json` equal.
2. **The scan,** on the folder's 81 files, found one hit, then none under UB's ruling:
   - entry 11 names the MIT commit identity. UB rules it a known string (2026-10-27): every MIT commit carries it, MIT's files name it five times, in M8.16.1's and M8.16's `DEVLOG.md`, and M8.16.1's re-filing accepted it in its entry 35. I checked each of those facts at source;
   - the exception is narrow: this one string, once, in `DEVLOG.md`. Later entries say "the MIT commit identity", any other email-shaped string still stops the plan, and step 10's scan runs under the same rule. The plan's step 2 records it, `../FILING_PLAN.md` `e3044eda9ad7dfd62b23a8a06df1dbaa55c57a362fa4c488020d9f0398ee4ee4`;
   - rerun under the rule: the known string once, in `DEVLOG.md`; no other email-shaped string; no local path, home folder, credential or session internal; the control string in 24 files; `check_no_local.py --require-files` clean, reading 70.
3. **The terms in `run/`:** `run/m8_16_task_details.md` `667159c3db993396a10a75775acf79e78f744d161c641ebc37c9e6baf3af7cea`, written by exclusive create, equal to `registration/m8_17_task_details.md`, v6.
4. **The environment record:** `run/ENVIRONMENT.json` `68c5747196a16091450c790d8ca40764ee07f7f294703051534a4c5776da960f`, written by exclusive create, as `python3 -I -B`. `--check` finds no difference. It records macOS 15.8 (24H23) on one Apple M3, with Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0: M8.16.1's record, field for field, apart from the time.
5. **The pin:** `run/MANIFEST_PIN` holds `2deed9aa564a6ccb4af36734e8ee6bdc787c9265b1be97cca22f0c76a4da9299`, the manifest's SHA-256 over 35 files: `instrument/` (12) and `run/` (23), the terms and the environment record among them. The manifest, recomputed, equals it, and a second pin is refused with `FileExistsError`.

From here no manifest-covered file changes, and every test runs in a scratch copy only. No `FROZEN.json` exists.

**Next:** step 6, the scratch tests on a copy of the pinned folder.

## 13. 2026-10-27T02:09:48Z: the filing, steps 6 to 9

6. **The scratch tests,** on a copy of the pinned folder, never the folder itself, each as `python3 -I -B`. The snapshot is step 6's: the folder after step 5, pinned. The dress rehearsal's snapshot, a copy of the unpinned folder with steps 3 to 5 applied, is entry 11's. The transcript:
   - the snapshot: a copy of the pinned folder, 84 files
   - test_constants: exit 0; output byte-equal to the folder; 7 s
   - test_reader: exit 0; output byte-equal to the folder; 6 s
   - test_gate: exit 0; output byte-equal to the folder; 539 s
   - test_locator: exit 0; output byte-equal to the folder; 4 s
   - test_freeze: exit 0; output byte-equal to the folder; 9 s
   - the copy's manifest after the tests: equal to the pin
   - arm, one byte appended to run/test_gate.out in a second copy: the comparison catches it, the manifest catches it
   - the plumbing pass: exit 0; 3 lines differ from the folder's, all of them in their timings only; 246 s
   - 0 failed
7. **`REPRODUCE.md`** `3c6b7cc9799c098a9b7162fda44538df339fae85900ea91648886c4fdcda213b`, from `../filing_drafts/REPRODUCE.md`, with its three values read from the files: the manifest's 35 files, and the recorded machine and OS from `run/ENVIRONMENT.json`. Its checks, run from the folder:
   - the manifest command prints the pin;
   - `record_environment.py --check` finds no difference;
   - `tools/copy_from_mit.py MIT_REPO` finds all 52 copies present and equal, and writes nothing.
8. **The MIT folder,** `files/framework/files/working/files/scripts/soft-slot-dynamics-m8-17/` in this worktree: 85 files copied from the bench, without caches and `.DS_Store`. Each equals the bench's, and the manifest, recomputed there, equals the pin.
9. **The census note,** under § V, step 5, as its last item, from `../filing_drafts/census_note.md`. It names the terms' SHA-256 and the pin once each, read from the folder's files, and links `REPRODUCE.md`. The page's math is unchanged, 125 inline spans, and its Status line is unchanged. `metadata-lint.py` reports 0 FAIL and 0 WARN. The page, edited: `9eb1653b31b6a4a3b09c2b539fa78c867936d8f466accecb1b830feac8982cb4`.

**Next:** this log is copied into the worktree's folder; then step 10, `SHA256SUMS`, and step 11, the local commit, not pushed.
