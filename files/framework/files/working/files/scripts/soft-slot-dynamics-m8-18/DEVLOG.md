# M8.18 development log

The census's two remedies: the development record. Entries are appended, never edited. A correction is a new entry.

## 1. 2026-10-30T17:20:40Z: the terms, v1 to v3

The answers of 2026-10-29 and 2026-10-30 on #512 admitted both remedies and fixed the first one's band. The census page recorded them before any terms were drafted, at MIT `2a4bccb` and `7a2c638`.

- **v1,** SHA-256 `125deea19db393309493456f6f58f9016104465dcf4de327df1f8f911cbd38f1`: one registration, two independent arms, a delta on M8.17's terms, drafted from stored records with no solve.
- **v2,** SHA-256 `1d142bc6d918913d04e2bffd5cdd639d21c3944fc878731bdb6cfb0e77775253`: solving and reading separated at `N = 40`, the read's scope frozen, a solve-state gate where no record exists, a bracket's borrowed end required to carry its classification on the new ladder, Arm A's gates scoped by the ruling's sections, and tests for the unscored reading and the Krein-negative distance.
- **v3,** SHA-256 `d3d833ff5de6254cb49865a9845b0c9fa698b412abcfa0119be0d3479a6207e0`, 7050 words: the locator's wording where Arm A's rules apply, and M8.17's code and terms told apart on a stored end; two wording notes; the interruption line naming the run's real jobs.

The reviews found nothing FATAL, and both closed at GO on the specification. Whether the code enforces the sparse read can be shown only by the code, so that stays for the build's review. No `N = 40` solve has run.

**The moved midpoint's values,** `dev/moved_midpoint.py` on M8.17's locator record, with no solve: the moved point 8.720990 lies between two readings, and the interpolation in squares gives 1.9 and 1.5 times K1's limit. `n(L)`'s gray zone is no risk there: its top is about 2.2×10⁻¹² relative, against 6.9×10⁻¹⁰ at the refused midpoint.

## 2. 2026-10-30T19:15:30Z: the build and its tests

The run folder is built from MIT's git objects (`tools/copy_from_mit.py`, `reference/SOURCES.json`). No solve has run at `N = 40`. The only real solves are the plumbing pass's.

**The code,** SHA-256:

- `run/census_lib.py`: `e07c5b57224dee8e7418aef37b9d755e4d5867add6a8835f46418b93a6048e4c`
- `run/census.py`: `9e7320cb559cf65054e127804b2a2c67778baa9aae6630a1874ac44bcd71d171`
- `run/write_guard.py`: `b971bd13fc351f2ed1485878fcdac7da11fbc29c21cf137b8450119ebfb1d7a2`
- `run/freeze_block.py`: `70d2cfd85c32490ab25c2ac99122cbc9e847befa443bb91e892aaeb590cea89f`

**The tests,** every script on this code, every one with exit 0. The suite ran from 17:20:16Z to 19:11:37Z; `dev/runs/001_final_suite/` keeps its scripts and outputs.

- Test 1, `run/test_constants.py`, `bcf081113ee16a4f2cd5a618aeff0f01b46024e66a5a31f55ba5c8b57f06529a`: 105 items, 510 numbers, 110 references, 5 arms red.
- Test 2, 3, `run/test_reader.py`, `83d909fc44018b96a22b6f02003c1b3e08b5fc1e486daf8c40f9228f00d664fa`: 86 stored points reproduced, 12 refusals, 4 arms red.
- Test 4, `run/test_gate.py`, `fcfcf72befaf467c98118e3f389e99e7a1d3428b66f2aa401f9f31abe3430941`: 220 points, 86 identity records, 30 midpoints, 55,877 leaves mutated with 0 passed, 1 h 48 min.
- Test 5, 7, `run/test_locator.py`, `102e36b176cd6e1e97c6ec8b101a8bc8b1a634dfa1cf0762adce9f1f40df13a0`: 7 arms for test 5, 40 arms on the two ladders, 114 bisections equal to M8.17's, the moved midpoint's arms, 9 borrowed-end arms, 4 records.
- Test 6, `run/test_scope.py`, `59983ccbaf31806329789aed8c336bf2eb7369bdfad9746aca0c71e001f34bb5`: 13 scenes, 9 arms red, rerun after the change below.
- Test 8, `dev/plumbing_census.py`, `a9e7a5e7106f5dee6d2726b642477025848db0a104ac4bda56e761b47d630c93`: 6 claims, real solves on C2a at N = 12, 16, 20, 129 s.
- Test 9, `run/test_freeze.py`, `7d3207c51a51089ca52be3eefdcac03a874e7827c8a3b959a860fbb18219cb4f`: 6 claims, 7 arms red, rerun after the change below.

**A line changed after the suite:** S1 printed 59 reads at `N = 40` beside parts that sum to 49. The other 10 are T4/R4's midpoints, each read from both ends as M8.17's locator does, so nothing was out of scope. `run/test_scope.py` now prints 59 reads of 49 points and fails if anything else is read twice. Tests 6 and 9 were rerun after the edit, and `dev/runs/002_scope_count/` keeps them. No other file changed; the seven outputs in `001_final_suite/` carry the scripts as they ran.

**What the tests caught in the draft, all fixed before the suite:**

1. `dict(recs, **{40: …})` raised on an integer key, at the gate; test 6 hit it.
2. A location's solutions file was not logged, so a resume would have moved it aside as partial; test 6 hit it.
3. Reading `gates()` against a real run: every control's `N = 40` basis stayed cached. Each control's cutoffs are now released when it finishes.
4. `run/write_guard.py` still named M8.17's terms.
5. S9 counted the fake record's solves as repeats, and S11's arm passed for the wrong reason, on the order check. Both tests are fixed.

**Not kept:** the tests' runs before the suite, on earlier drafts of this code. Their defects are the list above; no result here rests on them.

**Not built yet:** the launch scripts, `tools/build_record.py`, `REPRODUCE.md` and the filing drafts. They follow the build's review.

## 3. 2026-10-30T19:18:49Z: a correction to entry 2, and a gap in test 6

Entry 2 says test 6 hit the unlogged location file. It did not. With that logging removed from a copy of `census.py`, test 6 passed, so no test covered the fix. How the defect was first found is not on record.

S1 now fails if any `.json` or `.npz` the run writes goes unlogged, and two new arms, one for Arm A's location and one for Arm B's, turn it red. `run/test_scope.py`, `cd613eb27abad1f96bf90518a51f7c4d4eb006bc956327757a5b3f94f83dcdc8`: 13 scenes, 11 arms red, 126 files logged and 0 left out in S1. Tests 6 and 9 were rerun on it, and `dev/runs/003_location_logged/` keeps them. `census.py` and every other file are as in entry 2.

## 4. 2026-10-30T23:47:11Z: v4, the final code, test 6's arms, and the machine

Both units reviewed v1's build. One gave GO to complete the pre-freeze package, not to freeze, file or run. The other held for two FIXABLEs and gave six NITs, with all seven code choices GO. Every item was verified at source and taken. Nothing here is committed, pushed, filed or frozen, and no solve has run at `N = 40`.

**The terms, v4,** SHA-256 `007a0097c6c7d91877733ba38586bfa5229851d87341f622099d79bbc34584a6`, 7,235 words: the two FIXABLEs as worded, the sentence on a refused read, the two kinds of borrowed end, the new cases of tests 6 and 7, and the memory measure. `registration/m8_18_v3_to_v4.diff` has the change.

**The code,** SHA-256:

- `run/census_lib.py`: `fc48c67d69f92959bc14891f0e493a8b7547421f897d9419e7c16e925a341d16`
- `run/census.py`: `4c18892e913853468d568ab376ce0f0e0b35e6f2cda7770045bb07f9634fc2a6`
- `run/write_guard.py`: `b971bd13fc351f2ed1485878fcdac7da11fbc29c21cf137b8450119ebfb1d7a2`
- `run/freeze_block.py`: `70d2cfd85c32490ab25c2ac99122cbc9e847befa443bb91e892aaeb590cea89f`

**The review's items, in the code:** `gates()` catches `MemoryError` around each control's `N = 40` path and read and around C1, as that control's kernel failure with its cause; a stop survives a resume between `ARM_B.json` and `STOP.json`; a read refused at `N = 40` is a stop in `go()`; `arm_b()` stops unless M8.17's first type change equals `BRACKET_B`, before any solve; `jobs()` requires an end among the twelve and says why a bracket got no job; `admissible` names each cause.

**Added beyond the reviews' lists:** each job's log entry holds the process's peak resident size (`peak_rss`), a floor on this Mac, since RSS reads low once the compressor takes pages. `Run.stored` with no logged job is a stop by the solve-state gate, not a bare `KeyError`.

**A correction to entries 2 and 3: most of test 6's arms were red for the wrong reason.** A mutant loaded from a temporary folder took that folder for its `ROOT`, so `lib.m817_file` raised `FileNotFoundError` at Arm B, and `red()` counted any exception as red. That hit 8 of v1's 11 arms, every one that goes through `Run.go`. Entry 3's two arms on the location files were among them, so the claim there that they turn S1 red held only for that reason. Behind it, `Stub` subclassed the real `Cutoff`, so a mutation of `Cutoff` never reached a scene. The scenes on the real code were sound, so no result changes, but those arms showed nothing.

The fix: a mutant reads this folder's `reference/`, `stub_of(C)` builds the stub on the mutant's own class, `red()` takes only the one exception an arm names, and any other stops the test. Every arm now prints what its scene reported.

**The tests,** every script on this code, every one with exit 0. The suite's outputs are stamped 20:16:53Z to 22:20:40Z, and `dev/runs/005_final_suite/` keeps its scripts and outputs, equal to the folder's.

- Test 1, `run/test_constants.py`, `f83bc2a04ed3a06841e46abd05f99b4d8a230ca1b8665980e495703526d81911`: 106 items, 513 numbers, 110 references, 5 arms red.
- Test 2, 3, `run/test_reader.py`, `83d909fc44018b96a22b6f02003c1b3e08b5fc1e486daf8c40f9228f00d664fa`: 86 stored points, 12 refusals, 4 arms red.
- Test 4, `run/test_gate.py`, `3ef342b7a19fcd2a8df3eb258126662db675b2426d825d5bbdd634637488efe5`: 220 points, 86 identity records, 30 midpoints, 55,877 leaves mutated with 0 passed, the solve-state gate's 4 refusals.
- Test 5, 7, `run/test_locator.py`, `9e62381164f1d2ddfe76892fe05ed41261d991d341f642314777cb880e09e351`: 7 arms for test 5, 40 arms on the two ladders, 114 bisections equal to M8.17's, 7 moved-midpoint arms, 12 borrowed-end arms, 5 records.
- Test 6, `run/test_scope.py`, `80b79d124252667dc9a9c897065337348ee36c4d2a5d83ec97d4c8c68fbf0fe8`: 20 scenes, 21 arms, each red with its printed reason; S1 logs 126 files with 59 reads of 49 points at `N = 40`.
- Test 8, `dev/plumbing_census.py`, `a9e7a5e7106f5dee6d2726b642477025848db0a104ac4bda56e761b47d630c93`: 6 claims, real solves on C2a at `N` = 12, 16 and 20, 228 s.
- Test 9, `run/test_freeze.py`, `7d3207c51a51089ca52be3eefdcac03a874e7827c8a3b959a860fbb18219cb4f`: 6 claims, 7 arms red.

Test 4 also ran on a pinned copy of this code and these terms, beside the suite's, in 1 h 59 min, with an output byte-equal to the folder's. `dev/runs/004_ub_items/` keeps the runs on the review's items before this code.

**`tools/build_record.py` is deferred.** The build's cover listed it for this package, wrongly. M8.17's was written after its run, since it reads the run's outputs and this log. It stays outside the manifest, neither the freeze nor the launch uses it, and it follows the run here.

**The machine.** The dress rehearsal's environment record differs from M8.16.1's and M8.17's in one field besides the time: macOS 15.8 (24H23) then, 15.8.2 (24H232) now, installed 2026-10-29, after M8.17's run. The kernel's version is the same. NumPy and SciPy both link Accelerate, which ships with the OS, and the reproduction gate compares every float with `==`, so a changed Accelerate would stop the run at its first reproduced point, and no numbered test could show it first.

- `dev/os_reproduction.py`, `38cfd21060c2abfcc985ebca9a4baa9f09c9c25220f9f914454620dcbe3e9902`, a check of the machine outside the terms' numbered tests, runs the GO-list controls C2b, C2a, C3 and C2a/R5 through `Run.path_job`, `Run.read_job` and `gate_cutoff`, each at `N` = 16, 24 and 32, and C1 through `run_c1` at the same three, against their records. All 13 comparisons are exact: 316,571 leaves, in `R2`, `R3`, `R4` and `R5`, 0 differ. `dev/runs/006_os_reproduction_16/` keeps the script before C1 was added, with its first pass at `N = 16`; `dev/runs/007_os_reproduction/` keeps the final script and the whole output.
- `dev/os_reproduction_arm.py`, `a93071479d0e67f4b84629c0b51e2a1ca5c84ddcc1d6245d9ace4c359cf18a08`, moves one float of a record by one unit in the last place, on each control and on C1, and requires the script to report that leaf and no other. All 5 arms hold, and a first pass that moves nothing reports 0 differ, on the script's final bytes. `dev/runs/008_os_reproduction_arm/` keeps it.
- It adds no evidence: it reproduces public records, and it solves nothing at `N = 40`. The instrument refuses P5, C3R/R4 and the rows before the freeze, so they first reproduce in the run. Every one is in a slot the check covered.

**What changed because of it, all outside the folder:** the launch chain runs `run/record_environment.py --check`, so a first launch and every relaunch refuse a changed environment; `prelaunch_checks.py` requires the machine check on this OS and lists the updates on offer; `resume_check/test_launch_wrapper.py` has two more cases. The filing plan has a section on it, with macOS 27.2 left uninstalled until the run's record is written. No file under `instrument/` or `run/` changed, and the terms did not.

**Beside the folder,** SHA-256: `resume_check/resume_check.py` `9405929a8518f5f5df68b0206c71d64fce90d4ea4921b01cebd4f1f4caae0971`; `resume_check/test_resume_check.py` `dfad45fa8de64c84e8bc1a6ba2ce3c7b182f457537e8efe233cb6af6a29a4072`; `resume_check/test_launch_wrapper.py` `ef7a9dc99983aaeca27b1b16ae62f5f4f5196075fce130a0b7a440dd1b2d97f5`; `prelaunch_checks.py` `d49147d7a89d9079bd3c143d95119d31aca1910e124c8e90226679bc7c86b23c`.

**The dress rehearsal,** on a scratch copy of the final folder on this Mac: steps 3 to 5, tests 1, 2 and 3, 5 and 7, 6 and 9 with each output byte-equal to the folder's, test 8 equal apart from its time, the freeze with a dummy go, both admissions, the freeze block, and `prelaunch_checks.py`, 13 ok and 0 failed. Four arms turn the new guards red: three forged machine-check outputs, and a forged OS at the real `--check` in the chain's pipe.

## 5. 2026-10-31T04:26:03Z: v5, what ends a part of the run

Both units reviewed v2. UA gave GO to build v5 with both amendments, not to freeze, file or run, and asked for a short delta packet. UB gave GO with three refinements and corrected its own last review on S2 and S16. Both kept the OS check as a plan matter, with no line in the terms. Every item was verified at source and taken. Nothing here is committed, pushed, filed or frozen, and no solve has run at `N = 40`.

**The terms, v5,** SHA-256 `020793c0b5e98c458b78ac5f4c9c3adce9318c0a3f14c932eee9ca4465523db7`, 7,726 words. A job that runs out of memory, or that three launches start and leave unfinished, ends the part of the run it belongs to, with the cause named: a control's `N = 40` path, read or identity, or C1, fails the kernel check; a target's job leaves that row unread; a location leaves its bracket not located; Arm B ends, and Arm A goes on; any other job stops the run. Any other exception is a defect in the code, and it stops the run on its first launch. `ATTEMPTS = 3` is a frozen value. `registration/m8_18_v4_to_v5.diff` has the whole change.

**The code,** SHA-256:

- `run/census_lib.py`: `509b562200d9faeae02b730b4cd97a646ba3ccc4d6790d41ac04f0357bb86857`
- `run/census.py`: `20462a77045778623d77956abbe678f75868c1acab7a4b46d377b991c0897217`

**The rule, in the code.** `Run.begin` counts the job's own start events in the log, on every launch, and writes the start before anything solves. A job with three starts and no completion, or one out of memory, raises `Unfinished`. Each route catches `(MemoryError, Unfinished)` and nothing wider. `go()` catches `StopRun`, then `MemoryError`, then `Exception`, the last as a defect in the code, which covers the order checks' `PermissionError`. `classify_rows` and `assemble` take a partial set of targets, `left` names each unread row's cause, and `not_located` gives an unfinished bracket its own kind, `reproduced` false. The assembly moved inside `go()`'s catch, with the rows set last. `self.resume()` stays outside it, so a refused resume writes no stop.

**Corrections from the reviews.** S2 printed fixed text. S16 said no row was assembled on mutants that built all 5, which I had written. S20's line and the arm runner's were cut at 95 and 150 characters, past what told an arm from its scene. All three print computed values now, with both cuts removed, and S3, S4 and S8 do too. S1's `order >= 0` always held, so it went, and its count of other points read twice is computed. `peak_rss` is `peak_rss_bytes`, since `ru_maxrss` is in bytes on macOS and the terms now say so. The drafts say the spy is on the read.

**Found beyond the reviews:**

- **A job out of memory left no durable trace.** `MemoryError` took it down its route, but the log held nothing, so an interruption at the next row solved it again on the resume. `ended` in the log now holds it. With that removed, S21's next launch runs 18 solves of the job; with it, 0.
- **A real kill.** Every other interruption in test 6 is an exception, which a kill is not. In S29 each launch runs in a process of its own and SIGKILLs itself at T1/R4's `N = 40` path, with nothing raised. Exit statuses -9, -9, -9 and 0: the fourth launch reads the count from the log on disk, starts nothing, and writes its record with the row unread.
- **An arm can no longer pass on fixed text.** The runner fails an arm whose line equals the real scene's, printed as SAME LINE.
- **A control's identity record is on the kernel route,** which the reviews' wording did not name. The terms say "path, read or identity".

**The tests,** every script on this code, every one with exit 0 and empty stderr. The suite started at 02:05:58Z with the machine check beside it. S29 went in one second after the suite's test 6 finished, so test 6 ran again by hand on its final script: that output is the folder's. `dev/runs/009_final_suite/` keeps every script and output, equal to the folder's.

- Test 1, `run/test_constants.py`, `a1bfafe853457e4ab172db9f8ed3001ccaa22a3d26789c558f11ab84ea5859d9`: 108 items (70 a, 26 b, 12 c), 515 numbers, 110 references, 5 arms red.
- Test 2, 3, `run/test_reader.py`, `83d909fc44018b96a22b6f02003c1b3e08b5fc1e486daf8c40f9228f00d664fa`: 86 stored points, 12 refusals, 4 arms red; output byte-equal to entry 4's.
- Test 4, `run/test_gate.py`, `3ef342b7a19fcd2a8df3eb258126662db675b2426d825d5bbdd634637488efe5`: 220 points, 86 identity records, 30 midpoints, 55,877 leaves mutated with 0 passed, the solve-state gate's 4 refusals.
- Test 5, 7, `run/test_locator.py`, `9e62381164f1d2ddfe76892fe05ed41261d991d341f642314777cb880e09e351`: output byte-equal to entry 4's.
- Test 6, `run/test_scope.py`, `f17b155099de30c9a89ee0a5c22ad1063cec9e3143a78a5d53a149e194b85e1a`: 29 scenes, 41 arms, each red with its printed reason.
- Test 8, `dev/plumbing_census.py`, `a9e7a5e7106f5dee6d2726b642477025848db0a104ac4bda56e761b47d630c93`: 6 claims, real solves on C2a at `N` = 12, 16 and 20, 363 s beside the other jobs.
- Test 9, `run/test_freeze.py`, `7d3207c51a51089ca52be3eefdcac03a874e7827c8a3b959a860fbb18219cb4f`: 6 claims, 7 arms red.

**The machine check, again,** on this code, on macOS 15.8.2: 13 comparisons exact, 316,571 leaves, 0 differ, and 5 arms, each reporting its leaf and no other. `dev/os_reproduction.py` and `dev/os_reproduction_arm.py` are entry 4's bytes. `dev/runs/010_os_reproduction/` and `dev/runs/011_os_reproduction_arm/` keep the outputs.

**Beside the folder,** SHA-256: `resume_check/resume_check.py` `9405929a8518f5f5df68b0206c71d64fce90d4ea4921b01cebd4f1f4caae0971`; `resume_check/test_resume_check.py` `dfad45fa8de64c84e8bc1a6ba2ce3c7b182f457537e8efe233cb6af6a29a4072`; `resume_check/test_launch_wrapper.py` `ef7a9dc99983aaeca27b1b16ae62f5f4f5196075fce130a0b7a440dd1b2d97f5`; `prelaunch_checks.py` `d49147d7a89d9079bd3c143d95119d31aca1910e124c8e90226679bc7c86b23c`. None changed from entry 4.

**The filing plan:** "If a launch ends from outside" replaces the paragraph on a kill, and it says what a kill is called. C1 is named as the first `N = 40` on this OS.

**The dress rehearsal, again,** on a scratch copy of the final folder on this Mac: steps 3 to 5; tests 1, 2 and 3, 5 and 7, 6 and 9, each output byte-equal to the folder's; test 8 equal apart from its time; `dev/gen_items.py`'s 108 items in test 1's order; the manifest after them equal to the pin; the freeze with a dummy go, both admissions, the freeze block, and `prelaunch_checks.py`, 13 ok and 0 failed, with `run/out/` still absent. The four arms on the guards are red. The environment record differs from M8.16.1's and M8.17's only in the OS and the time. Test 4's sweep did not run on that copy; it ran in the suite.

## 6. 2026-10-31T10:07:00Z: the units' replies to v3, Blake's word, and one line of code

Both units reviewed v3 and gave GO on items (a) to (e), with nothing FATAL or FIXABLE and no HOLD left. UA reran tests 1, 2 and 3, 5 and 7, 6 and the resume tests, each output byte-equal, verified the terms' hash, the diffs and the 40 source pins, and closed its S20 HOLD. UB reran tests 1, 2 and 3, 5 and 7, 6 and 9, the plumbing pass, the resume check and the wrapper, each byte-equal apart from the plumbing pass's timings, read test 4's claims 1 to 7, and read every arm's line against its scene's. The machine check and the dress rehearsal need this Mac, so both read those outputs and neither repeated them. UA did not repeat the sweep either; UB's full sweep on v1 covers claim 5, whose script and gate functions have not changed since.

Blake's word, on both replies: "proceed if/when gucci:". By the filing plan's gates that starts step 1, through the local commit, which stops. The push, the OpenWave filing, the go, the freeze and the run each wait for Blake's word.

**UB's second NIT, taken.** A located Arm B record carried `reproduced: None` in `census['arm_b']`, since only the unfinished kind sets the field. Verified at source. UB offered two fixes: True on a record the locator wrote, or no key, with `kind` marking the difference. True would call an unsuccessful numerical location a reproduction, which UA's third boundary rules out, so `census['arm_b']` now takes each listed key only where the record has it. An unfinished Arm B keeps `reproduced: False`, as S24 shows, and a located record has no such key.

`run/census.py` is now `6000ecc7dbd570b0bb6fee6493ff01634bcca1e94a350e4a46c2483d109cb8e3`: one statement changed, in `go()`, which the solves, the reads and the gates do not reach. `registration/census_vs_m8_17.diff` is regenerated and still gives this file from M8.17's. `dev/runs/012_arm_b_key/` keeps the file.

**On this code:** tests 1, 2 and 3, 5 and 7, 6 and 9 reran, each with exit 0, empty stderr and an output byte-equal to `dev/runs/009_final_suite/`, and test 8 reran, equal apart from its time. A one-off run of the real scene shows a located record with no `reproduced` key. The dress rehearsal reran on a scratch copy of this folder: steps 3 to 5, those tests, the freeze with a dummy go, both admissions, the freeze block, and `prelaunch_checks.py`, 13 ok and 0 failed, and its four arms on the guards red.

**UB's first NIT, not taken.** It touches the terms, and UB asked for it only if something else reopens them. Nothing has. The interruption rule's list of jobs leaves out Arm B and C1, which are counted per job and have their routes in What stops what. If review reopens the terms, this sentence goes in:

> M8.16.1's rules apply to each job in place of each case: Arm B, C1, a path at one cutoff, its read, an identity, a case's reading, the gate or a location.

**The machine check runs again,** since the filing plan says it does if the code changes before the freeze, though this statement is not on its path. Step 6 runs the sweep on the pinned copy, so entry 5's sweep is not relied on for this code.

## 7. 2026-10-31T10:07:40Z: the filing plan's steps 1 to 5

MIT's `origin/main`, fetched, is `7a2c638cd1b1bda1df57db1d47304d14aaa3249b`, the commit the terms cite for the census page. `tools/copy_from_mit.py` against that clone finds all 40 copies present and equal to their blobs at their named commits, each with its pin.

**The scan,** before the pin: every file the folder holds, 151 files, 97.6 MB, text and binary, with no hit and the control string found 1,177 times. `check_no_local.py --require-files` is clean on the 101 files it reads. No cache and no `.DS_Store`.

**The terms in `run/`,** by exclusive create: `run/m8_16_task_details.md`, `020793c0b5e98c458b78ac5f4c9c3adce9318c0a3f14c932eee9ca4465523db7`, equal to `registration/m8_18_task_details.md`.

**The environment record,** by exclusive create: `run/ENVIRONMENT.json`, `79f009089a3b983d9f0e48e3e80dc0d17bc354520d20c332fc2cf7274eff6e80`, recorded 2026-10-31T10:07:21Z, on macOS 15.8.2 (24H232) on one Apple M3. `--check` finds no difference. It differs from M8.16.1's and from M8.17's in the OS and the time, and in nothing else.

**The pin,** by exclusive create: `run/MANIFEST_PIN`, the manifest's SHA-256 over 37 files, `866f12a992cb2ed4c885f09722b150d737587b718d71132e7c90b4b488896838`. A second pin is refused, and the manifest, recomputed, equals it. From here no manifest-covered file changes, and every test runs in a scratch copy only.

Step 6 and the machine check run next, side by side.

## 8. 2026-10-31T11:54:43Z: the filing plan's steps 6 to 9, and the machine check on the final code

**The machine check on the final code.** Entry 6's statement changed the code after the last check, so the plan's rule ran it again, beside step 6, on the pinned folder. All 13 comparisons are exact: 316,571 leaves, 0 differing, on macOS 15.8.2 at `N` = 16, 24 and 32. Each of the 5 arms reports the one float it moved, and the first pass, which moves nothing, reports 0 differ. Both outputs equal those in `dev/runs/010_os_reproduction/` and `011_os_reproduction_arm/` apart from their seconds, and the scripts are the same files. `dev/runs/013_os_reproduction/` and `014_os_reproduction_arm/` keep this pass.

**Step 6,** on a scratch copy of the pinned folder, 154 files, under `python3 -I -B`: `run/test_constants.py run/m8_16_task_details.md`, `run/test_reader.py`, `run/test_gate.py`, `run/test_locator.py`, `run/test_scope.py` and `run/test_freeze.py`. Each exited 0 with nothing on stderr, and each output is byte-equal to the folder's. Each output's modification time in the copy falls at its own test's end, so each comparison read a file that test wrote. The sweep took 1 h 40 min, and this is the sweep the final code rests on. The copy's manifest after them equals the pin. On a second copy, one byte appended to `run/test_gate.out` is caught by the comparison and by the manifest alike.

`dev/plumbing_census.py`, rerun on the copy, shows no difference from the folder's at all: both passes took 133 s, so even its time line matches. `dev/gen_items.py` on the placed terms lists the same 108 items as `run/test_constants.py`, in the same order.

The dress rehearsal ran on a copy of the unpinned folder with steps 3 to 5 applied, and step 6 on a copy of the pinned folder.

**Step 7.** `REPRODUCE.md`, by exclusive create, `6f8552aa6040924b11cea94f5acda53c00d03dc3299053b2798258614b37d30b`, its values read from the files it describes: 37 files, macOS 15.8.2 (24H232), one Apple M3. From the folder, the manifest command prints the pin, `run/record_environment.py --check` finds no difference, and `tools/copy_from_mit.py` finds all 40 copies present and equal.

**Step 8.** The folder in MIT's worktree, at its path, without caches and `.DS_Store`: 159 files, each equal to the bench's, and the manifest recomputed there equals the pin. It is copied again after this entry, so that it holds this entry.

**Step 9.** The census note, under § V, step 5, as its last item, directly before the sequel: one line added, the terms' SHA-256 and the pin each read from the folder's files. The page's `$` count is 302 before and after, `metadata-lint.py` reports 0 FAIL, 0 WARN and 41 INFO, and the Status stands. The three relative links, two in `REPRODUCE.md` and one in the note, resolve, M8.16.1's `#what-is-here` among them.

Step 10 and the local commit run next.

## 9. 2026-10-31T11:56:43Z: steps 10 and 11, the local commit

**Step 10.** `SHA256SUMS`, fresh from the final inventory, in M8.17's form: 159 lines, one per file but itself, sorted by path. `shasum -a 256 -c SHA256SUMS` passes on every line from the folder. The final scan read all 160 files, 97.7 MB, with no hit and the control string found 1,235 times, and `check_no_local.py --require-files` is clean on the 108 files it reads of the 160 selected. No cache and no `.DS_Store`. The sums are copied to the bench.

**Step 11.** MIT commit `7942d9b81ea48cc4237beba8413cb0b3722121af`, on `7a2c638cd1b1bda1df57db1d47304d14aaa3249b`, with `origin/main` fetched again just before and still there: 161 files, the folder's 160 and the census page. Verified from its own tree, extracted by `git archive`: `shasum -c` passes on all 159 lines, the manifest equals the pin, and the census note names the terms' SHA-256 and the pin once each. On that extract, one byte appended to `run/test_gate.out` is caught by the sums and by the manifest alike.

It is not pushed: `origin/main` stays at the base. This entry stays on the bench, since a commit cannot hold its own hash, and reaches the folder with the run's record. The plan stops here. The push, the OpenWave filing, the go, the freeze, the freeze block and the run each wait for Blake's word.

## 10. 2026-10-31T13:12:47Z: step 12, the push

Blake's word: "push". MIT was fetched again, and `origin/main` was still `7a2c638cd1b1bda1df57db1d47304d14aaa3249b`, so the push was a fast-forward of one commit. `git push origin HEAD:main` put `main` at `7942d9b81ea48cc4237beba8413cb0b3722121af`; `ls-remote` and GitHub's API both show it.

Read back live through GitHub's API: `REPRODUCE.md`, `SHA256SUMS`, the terms, `run/MANIFEST_PIN` and the census page each hash equal to the local file. The live page renders all 151 math spans, with no "Unable to render", and holds the note once.

This entry and entry 9 stay on the bench and reach the folder with the run's record. OpenWave's filing waits for Blake's word.

## 11. 2026-10-31T13:48:21Z: the filing plan's steps 14 to 17, the fork

Blake's word: "start the OpenWave filing".

**Step 14,** with `upstream` fetched again. All 11 links in the terms resolve, each at its source and over HTTP: the blobs at their commits in MIT and OpenWave, the heading's anchor at OpenWave `e8762263`, five comment ids on #512, the review on #676 and #677. "M8.18" occurs nowhere under `m8_mit/` or `dev_docs/`, and no pull request is open. Run-before-write holds: #676 and #677 are merged. M8.16.1's and M8.17's task docs open with their title and "Pre-registration, for review.", as v5 does.

**`upstream/main` moved during the step,** from the plan's `e8762263612a3e981f67009079c2cdae66a0071c` to `6b0b24f45e56e7d7746d5546bac836e60a9d2d9a`: the merge of #685, 4 files, all under `m5_liquid_crystal`. Nothing under M8, `dev_docs/`, `.github/` or MODELS.md changed, and the roadmap's blob is the same, so the four edits apply as drafted. "M8.18" still occurs nowhere, and no pull request is open. The plan puts the branch on `upstream/main`, so it is on `6b0b24f4`. My script's stop was stricter than the plan and stopped before the branch, with nothing changed. The terms' link at `e8762263` is a fixed commit and stays as filed.

**Step 15.** Branch `m8-18-census-remedies-2026-10-31`, with two files: `research/tasks/m8_18_task_details.md`, new, byte for byte MIT's `run/m8_16_task_details.md`, and `research/m8_roadmap.md`, one line added and three changed, +4 −3, each edit taken from the draft's fenced blocks: the BACKLOG row, the snapshot's date, and the two M8 status rows.

**Step 16.** `check_roadmaps.py`, `check_models_md.py` and `check_no_local.py --require-files` on both files are clean. On a scratch copy of the roadmap, 14 words added to the row's Description stay clean, and 15 fail with "description is 66 words, cap 65", so the Description is 51 words.

**Step 17.** OpenWave commit `39723a07f79c4c0bdf406670a62e75896b4f1324`, on `6b0b24f45e56e7d7746d5546bac836e60a9d2d9a`, in the clone's local identity, signed off in its message, with the Co-Authored-By line: 2 files, +390 −3. It is pushed to the fork, and `ls-remote` shows it. Read back raw from the fork through the API, the task doc hashes to the terms' SHA-256, `020793c0b5e98c458b78ac5f4c9c3adce9318c0a3f14c932eee9ca4465523db7`, and the roadmap equals the branch's. GitHub's compare shows the branch 1 ahead of `main` and 0 behind.

The pull request is Blake's to open. `m8_18_pr_title_v1.txt`, `b6e34a327fd47d7a8d35623ec9385c898316f88e8cba3e992cbd79417ce04709`, and `m8_18_pr_body_v1.md`, `5c1297499213e076fa993879a4a6703e23b6a466d81b1f0cbd0fddf1ece51e70`, sit beside the folder, filled from the files, with every link answering 200. GitHub's renderer gives 1 table, 3 rows and 7 list items. No pull request is open and nothing is posted. The go, the resume check, the freeze, the freeze block and the run wait for the merge and Blake's word.

## 12. 2026-10-31T13:58:37Z: UA's last sweep of the pull request's body, and a correction

Blake's word: "last sweep for NITs if you want them:", with UA's GO to file and three wording NITs on `m8_18_pr_body_v1.md`. Each was checked at source.

**NIT 1, taken, in the terms' own words.** The body said "three launches leave unfinished". A launch can leave a job unfinished by never reaching it, and `ATTEMPTS` counts starts per job. The terms say "three launches start and leave unfinished", and the body now does too.

**NIT 2, taken, in other words, and a correction.** The body said the plumbing pass solved C2a "at cutoffs the run never uses". Read as a statement about the run's cutoffs, that is wrong at `N = 16`: `census_lib.cutoffs_of` gives T4/R5, Arm B's row, 16, 24 and 32, and C1 16, 24, 32 and 40. What holds is narrower. It gives C2a 24, 32 and 40, so the run never solves C2a at 12, 16 or 20. UA's wording, "outside the registered control and target ladders", has the same fault at `N = 16`, so the body now reads "at `N` = 12, 16 and 20, where the run never solves it".

The same phrase stands where this round changes nothing: test 8 in the terms, in `run/` and `registration/`; two sentences of `REPRODUCE.md`; and the docstring of `dev/plumbing_census.py`. All of them are in MIT `7942d9b`. No rule, number, reading or job depends on the phrase: the terms fix each ladder elsewhere, in § The instrument and the ladders, and the pass solved no point the run reads.

- **The terms stay v5.** Reopening them for this means a new hash, pin, sums and census note after both units' GO, and test 8 reads truly as "never uses on C2a". This entry is the dated correction. If review reopens the terms, test 8 takes "where the run never solves it", with UB's sentence from entry 6.
- **`REPRODUCE.md`** is corrected with the run's record, in the folder's next commit: the plan allows no commit touching the folder between step 11's and the write.

**NIT 3, not taken.** It would replace the body's last sentence, which is Blake's own line, used verbatim on every M8 pull request. "Data-sensitive" there carries the filed terms, and the body's "After the merge" paragraph already says that any change to the terms' words redoes the hash and the pin on MIT `main` before the go.

**The body:** `m8_18_pr_body_v2.md`, `48c1ada9a0b0bbcc5cb67a275689641ad5db322a4cc8f2c34d0fde16507a5e93`, the draft `filing_drafts/pr_body.md` carrying both edits. Its checks ran again: every link answers 200, and GitHub's renderer gives 1 table, 3 rows and 7 list items. It replaces v1 on Blake's clipboard.

## 13. 2026-10-31T14:09:02Z: the terms reopened; the sweep; v6's edits

Blake's word, on the choice entry 12 left open: "do it the right way, we have the time." Entry 12's decision to keep v5 is superseded. The terms are corrected before they are filed, so that the text OpenWave reviews is exact, and the plan's path for a change to the terms applies: the terms in `registration/` and `run/`, test 1 and the rehearsal in a scratch copy, the pin, `SHA256SUMS` and a new census note. MIT `7942d9b` stands as history, and the correction is a new commit on it.

**The sweep.** One phrase was not the proposition. Before any edit, v5 was read whole against the code, for any claim of that kind: prose about the run or its code that no numbered test reads.

**What held:**
- every quotation: the boundary, 123 words, verbatim in 18955679; the docstring; M8.16's two; M8.17's one; the answers' two. The sweep's comparison reported one miss, the line under "The calibration's range": it is verbatim in 19076863, and the terms add only the backticks around `N = 40`;
- M8.17's 27,823-byte prefix, at its SHA-256;
- all 19 files called byte for byte, `instrument/` and M8.16.1's run code, against `d1c0ec8`;
- the 14 files the terms name, and the calls they name, with `driver.run_case` never called;
- the moved midpoint's diff, line for line against `census_lib.bisect` and M8.17's;
- the jobs: `arm_b`, `C1`, `path:`, `read:`, `identity:`, `case:`, `gate` and `locate:`, which are the eight kinds UB's sentence lists;
- `REPRODUCE.md`'s "a few kilobytes": a seed state is 352 to 6,928 bytes at `N` = 16, 24 and 32.

**What did not, and v6's seven edits.** None changes a rule, a point, a frozen value or a file the run executes.
1. **The band's diff.** The terms called the change one line and showed a `+` line that is not in the code. It was true of v1. The call moved to `census.rule`, which also takes the reading beside it, and `run/census.py` holds neither that line nor one like it. Two edits: the sentence, and the diff's `+` lines, now the code's two. The `-` line is M8.17's, unchanged. Every line of both diffs now stands verbatim in the file it names, and that was checked mechanically.
2. **Test 8.** "at cutoffs the run never uses" is wrong at `N = 16`, as entry 12 sets out. It now reads "at `N = 12`, 16 and 20, where the run never solves it".
3. **"No point but the twelve in Arm A."** A new bracket's midpoints and guard readings are points of Arm A, and a guard is classified. The bullet is about the paths' grid points, as its next sentence says, so it now reads "No grid point but the twelve is classified in Arm A."
4. **Test 6** had "left unfinished by three launches", the shorthand UA caught in the pull request's body. It now uses the rule's words: "that three launches start and leave unfinished".
5. **The interruption rule** takes UB's sentence from entry 6 as worded, with Arm B and C1 in the list of jobs.
6. **The word budget** said "About 7,000 words", v2's figure. v6 is 7,752 words by `wc -w`, so it now says "About 7,750 words". Test 1 reports this item unscored, which is why no test caught it.

`run/test_constants.py` changes in three anchors only, with the budget's tokens, since its items are anchored in the text. `dev/gen_items.py` on v6 finds the same 108 items, and these three are the only ones that differ. `dev/plumbing_census.py`'s docstring and two sentences of `REPRODUCE.md` take test 8's correction. `run/census.py`, `run/census_lib.py` and `instrument/` do not change, so the machine check does not rerun.

**The units see v6 before it leaves this machine.** Both gave GO on v5's bytes. So the plan runs through the local commit and stops, and the push and the fork wait for their reply and Blake's word.

## 14. 2026-10-31T16:02:44Z: v6: the pin, step 6, and steps 7 to 9

**The terms,** v6: SHA-256 `12aa29f76c4bd94afbac6e6ce97e8b8e67cf85f1f6addf3685ad3045dc4716f1`, 7,752 words by `wc -w`, equal in `registration/` and `run/`. `registration/m8_18_v5_to_v6.diff` shows every word.

**What moved in the manifest,** against MIT `7942d9b`: 37 files before and after, and four moved: `run/m8_16_task_details.md`, `run/test_constants.py`, now `dd1b54be49f7a4433f4ee8c60a684779078c3157b87e8d453d86346c34b66993`, `run/test_constants.out` and `run/test_freeze.out`. `instrument/`, `run/census.py` and `run/census_lib.py` are as they were. `run/ENVIRONMENT.json` stands, at `79f009089a3b983d9f0e48e3e80dc0d17bc354520d20c332fc2cf7274eff6e80`, and `--check` finds no difference. The OS is still 15.8.2.

**Tests 1 and 9** ran on a scratch copy of the folder before the pin, and their outputs came into the folder from there. `dev/runs/015_v6_tests/` keeps them, with `run/test_constants.py`.

**The scan,** before the pin: 163 files, 97.8 MB, the control string found 1,329 times, 0 hits. `check_no_local.py --require-files` is clean on 108 of 163 files. `tools/copy_from_mit.py` finds all 40 reference copies present and equal.

**The pin:** `e5e4b0433fd05034ecd37b67674d88a61f0fc4a1bfc159b197a2be34c9b94fe2`, over 37 files. A second pin is refused, and the manifest, recomputed, equals it.

**Step 6,** on a scratch copy of the pinned folder (164 files), from 14:11:19Z to 15:59:36Z. All six tests: exit 0, empty stderr, each output byte-equal to the folder's, and each output's time inside its test's window, so each test wrote its own. Test 4's sweep took 1 h 44 min. The copy's manifest after them equals the pin. The plumbing pass: exit 0, empty stderr, and the only difference from the folder's output is its time, 138 s for 133 s. `dev/gen_items.py` finds the same 108 items in test 1's order. On a second copy, one byte appended to `run/test_gate.out` is caught by the comparison and by the manifest.

`dev/runs/016_v6_step6/` keeps the outputs and the plumbing script. `dev/plumbing_census.out` is now this run's, so it is the output of `dev/plumbing_census.py` at its final hash, `d7fef57fbd7df584c89b6738993d9ced0a3d48dbd6bb7317c0cac6d894cce51d`. Both are outside the manifest.

**The dress rehearsal did not run again.** Step 6 ran every test on the real pin. What the rehearsal adds past that is the freeze with a dummy go, both admissions, the freeze block and `prelaunch_checks.py`. Test 9 ran the first three on v6, and `prelaunch_checks.py` holds no value of the terms and did not change.

**Step 7.** `REPRODUCE.md` is rewritten from its draft, with the two sentences on the plumbing pass changed: `3a9b4c96247a503c3ebe607b21fe636343efea47afb6705a2d42f9108e3e23bc`. From the folder the manifest prints the pin, `--check` finds no difference, and all 40 reference copies are present and equal.

**Step 8.** v5's `SHA256SUMS` is off the bench until step 10. The worktree's folder is recopied: 171 files before this entry's copy, each equal to the bench's, and the manifest there equals the pin.

**Step 9.** The second dated note on M8.18's terms stands directly after the first, which stands as made, under § V, step 5. It gives the new SHA-256 and pin and says they replace the two values in the note above. The page's `$` count is unchanged at 302, `metadata-lint.py` reports 0 FAIL, 0 WARN and 42 INFO, and the Status stands.

**Entries 9 to 13.** Entry 9 said it would reach the folder with the run's record. A folder commit comes sooner now, so entries 9 to 13 reach it with v6's commit, and only the entries after it stay on the bench.

**The state.** MIT `main` is `7942d9b`. The fork's branch still holds v5's task doc, no M8.18 pull request is open, and Blake's clipboard holds a body with v5's hash, which is not to be used. Next are steps 10 and 11, and the units' packet on v6. The push and the fork wait for their reply and Blake's word.

## 15. 2026-10-31T16:09:37Z: steps 10 and 11 for v6, the local commit, and the units' packet

**Step 10.** `SHA256SUMS`, fresh, 171 lines, `a3771e4ecdef83545be77dd6cec658726ad070a1acdd9736851853ebc4d00692`. `shasum -c` passes from the folder. The scan of the final folder read 172 files, 97.8 MB, with the control found 1,389 times and 0 hits, and `check_no_local.py --require-files` is clean on 110 of 172 files. The sums are on the bench.

**Step 11.** MIT `87613f4f70d8443baa80b92ee05805879d848f25`, on `7942d9b81ea48cc4237beba8413cb0b3722121af`, which `origin/main` still is: 24 files, 12 modified and 12 added, the folder's and the census page. Extracted by `git archive`, its tree passes `shasum -c` on 171 files, its manifest equals the pin, the page names the terms' SHA-256 and the pin once each, and one byte appended to `run/test_gate.out` is caught by the sums and by the manifest. It is not pushed.

**The sweep, on v6.** `sweep_v6.py` is extended to `sweep_v6b.py`: every line of both diffs in the terms against the file it names, the run's ladders, its kinds of job, and each corrected sentence. It reran on v6 with 0 failed. Two checks failed on their first pass, and both were mine: a regex with its backslashes doubled, and a job pattern that looked only at literal arguments of `begin`. The one quotation that differs only by the terms' backticks is now reported as that.

**The units' packet:** `m8_18_v6_review.zip`, `0ee6670318027b47a704a4ac8ab0c43b970989f5db3240fb5608f2ac6ef8e79f`, 196 files, with the folder as the commit's tree. From a clean extract, every byte equals its source, `shasum -c` passes on 171 files, the manifest equals the pin, and tests 1, 2 and 3, 5 and 7, 6 and 9 exit 0 with outputs byte-equal to the folder's. The cover is on Blake's clipboard in place of the body with v5's hash.

This entry stays on the bench, since a commit cannot hold its own hash. The push and the fork wait for the units' replies and Blake's word.

## 16. 2026-10-31T16:30:02Z: both units on v6; v7's edits

Blake's word: "proceed if/when gucci:", with UA's GO and UB's GO on v6.

**UA:** GO on items (a) to (f), with no finding. Its two filing safeguards are already the plan: section v3 supersedes the steps' historical values, and the fork's commit is rebuilt rather than pushed as it stands.

**UB:** GO on (a), (c), (d), (e) and (f). On (b), three NITs of the kind entry 13's sweep looked for, and on (e) one stale line in the plan. UB left the choice to Blake and advised taking them while v6 is local. Each was checked at source.

1. **Line 19, taken.** It said every reading at `N = 24` and 32 is on record. `census_lib.settle` bisects a new bracket at each deciding cutoff, 32 among them, and at 24 where its ends' `n(L)` are resolved and differ, so those midpoints are new readings, and § Known outcomes lists them. UB's replacement goes in as worded.
2. **The list under "New evidence", added here.** A bracket's end outside the twelve is read at `N = 40`, and that record can refuse the bracket (§ ARM A), but the list does not name it. It now does, with no number, so test 1 gains no item.
3. **Line 123, taken, in other words.** `locate` and `settle` return a stop for a point that does not reproduce, and `arm_b` writes `ARM_B.json` with that stop and then raises. So "if written" admits a record whose path did not reproduce, and the sentence's "since" is false of it, as UB says. UB's "if Arm B finished before the stop" leaves a second case: a record from `not_located`, which ended Arm B and whose docstring says nothing in it was reproduced. So the sentence now reads "Arm B's record, if its own path and midpoints reproduced, stands as written, with the stop named beside it." Either other record is kept under the sentence before it.
4. **The guards' band, taken.** UB's mutation reproduces: with the guard loop of `band_failures` removed from a copy of `census_lib.py`, tests 2 and 3, 5 and 7, and 6 all pass with outputs byte-equal. S16 now takes a guard off the band on each side of T4/R4's location, and a new arm, the first mutation of `census_lib.py` in test 6, removes the loop. The terms' test 6 already says a scored reading off the band stops the run, so its text does not change.
5. **The plan's stale line,** under "What is filed": fixed in place, with the final scan.

**The decision.** These are the kind of claim v6 was reopened for, and Blake's word on that choice was "do it the right way, we have the time." UA's "no v7" stands against no finding of UB's: UA reports none, and UB's hold at source. So: v7.

- `instrument/`, `run/census.py` and `run/census_lib.py` do not change, so the machine check does not rerun. All of step 6 reruns on the new pin, so that the commit's claim covers every test on it.
- v7 is a commit on `87613f4`, which stays in the history, so every hash in this log resolves once it is pushed.
- The census note made in `87613f4` has never been public, so it takes v7's values in place, and the page keeps two notes.
- No further unit round: both gave GO on v6, the wording is UB's but for items 2 and 3 above, and no rule, point or frozen value moves. On Blake's word the push and the fork follow.

## 17. 2026-10-31T18:25:47Z: v7: the pin, step 6, and steps 7 to 9

**The terms,** v7: SHA-256 `924e7ee363a756a88ba2a9ee9bc03eb56c4fe27778c6e8f920a42a5229034a4c`, 7,768 words by `wc -w`, equal in `registration/` and `run/`, and "About 7,750 words" still holds. `registration/m8_18_v6_to_v7.diff` shows every word: three lines.

**What moved in the manifest,** against `87613f4`: 37 files before and after, and six moved: `run/m8_16_task_details.md`, `run/test_constants.py`, now `7bffcf90f8021ef54f8783f53a0a55acea9973526a559d32ab8069825dc29fc8`, in one anchor, `run/test_scope.py`, now `43a928cd87d540ca86df0fdd4bde37a70094a4e385eccfdd75d863eb3a6aa846`, and the outputs of tests 1, 6 and 9. `instrument/`, `run/census.py` and `run/census_lib.py` are as they were, `run/ENVIRONMENT.json` stands, `--check` finds no difference, and the OS is still 15.8.2. `dev/gen_items.py` finds the same 108 items.

**Test 6:** 29 scenes and 42 arms, every arm red. S16 reports a guard off the band on each side of T4/R4's location, each a stop with no row assembled. The new arm takes the loop out of `census_lib.band_failures`: the target and the control still stop, and both guards read "no stop; 5 rows assembled", so it goes red for its named reason. The arm that removes the band's stop now reads "no stop" four times.

**Tests 1, 6 and 9** ran on a scratch copy before the pin, and their outputs came into the folder from there. `dev/runs/017_v7_tests/` keeps them, with both scripts.

**The scan,** before the pin: 176 files, 97.9 MB, the control string found 1,479 times, 0 hits. `check_no_local.py --require-files` is clean on 110 of 176 files. All 40 reference copies are present and equal.

**The pin:** `6d244f4af56b71d60f17077724628b7489b278e84a7d24565c17038ed19ba43a`, over 37 files. A second pin is refused, and the manifest, recomputed, equals it.

**Step 6,** on a scratch copy of the pinned folder (177 files), from 16:33:25Z to 18:25:17Z. All six tests: exit 0, empty stderr, each output byte-equal to the folder's. Test 4's sweep took 1 h 47 min. The copy's manifest after them equals the pin. The plumbing pass: exit 0, empty stderr, and the only difference from the folder's output is its time, 136 s for 138 s. `dev/gen_items.py` finds the same 108 items in test 1's order. On a second copy, one byte appended to `run/test_gate.out` is caught by the comparison and by the manifest. `dev/runs/018_v7_step6/` keeps the outputs. `dev/plumbing_census.py` did not change, so its output in `dev/` stands.

**Step 7.** `REPRODUCE.md`, from its draft, is v6's bytes again. From the folder the manifest prints the pin, `--check` finds no difference, and all 40 reference copies are present and equal.

**Step 8.** The worktree's folder is recopied: 185 files before this entry's copy, each equal to the bench's, and the manifest there equals the pin.

**Step 9.** The note `87613f4` made takes v7's words and values in place, so the page has two notes on M8.18's terms. The note of v5 stands as made. The page's `$` count is unchanged at 302, `metadata-lint.py` reports 0 FAIL, 0 WARN and 42 INFO, and the Status stands.

**Entries 15 to 17** reach the folder with v7's commit. Next are steps 10 and 11, then the push and the fork, on Blake's word in entry 16.

## 18. 2026-10-31T18:28:03Z: steps 10 to 17 for v7: the commit, the push, the fork

**Step 10.** `SHA256SUMS`, fresh, 185 lines, `b324720ccb41c2f3f892262c9db367b5e7f0daac5042fc7b8abf8e8977094a8b`. `shasum -c` passes from the folder. The scan of the final folder read 186 files, 98.0 MB, with the control found 1,564 times and 0 hits, and `check_no_local.py --require-files` is clean on 113 of 186 files.

**Step 11.** MIT `4bd8bbd8e3c60a387210c4464bf0c7915d10bdc3`, on `87613f4f70d8443baa80b92ee05805879d848f25`: 25 files, 11 modified and 14 added, the folder's and the census page. Extracted by `git archive`, its tree passes `shasum -c` on 185 files, its manifest equals the pin, the page names the terms' SHA-256 and the pin once each, and one byte appended to `run/test_gate.out` is caught by the sums and by the manifest.

**Step 12,** on Blake's word in entry 16: pushed, two commits, a fast-forward from `7942d9b`. `ls-remote` and GitHub's API show `4bd8bbd`. `REPRODUCE.md`, `SHA256SUMS`, the terms, the pin and the census page each hash equal live, the page renders 151 of 151 math spans, and it holds two notes on M8.18's terms, the corrected one once.

**Steps 14 to 17.** `upstream/main` moved to `daa5f631`, #686, M5 only, with the roadmap's blob the same. "M8.18" occurs nowhere under `m8_mit/` upstream, and no pull request is on the branch or open. The fork's branch is rebuilt as one commit on `daa5f631`: `f23dad7504020c1e7aa7cd483f38a1025394a69d`, pushed with a lease on `39723a0`, v5's. The task doc reads back raw at `924e7ee363a756a88ba2a9ee9bc03eb56c4fe27778c6e8f920a42a5229034a4c`, and the roadmap reads back equal. `check_roadmaps.py`, `check_models_md.py` and `check_no_local.py --require-files` are clean, and the Description's arm fails at 66 words. The terms' 11 links resolve.

**The body:** `m8_18_pr_body_v3.md`, `af659bbcf5b21e6817037b13c79a8dd4345433d559689606b0a05935076a0f28`, with the new values, and its sentence on new evidence takes the terms' list. All its links answer 200, and GitHub's renderer gives 1 table, 3 rows and 7 list items. The title file stays v1. The body is on Blake's clipboard, and `m8_18_pr_body_v2.md`, with v5's hash, is not to be used.

Blake opens the pull request. Nothing is frozen, and no solve has run at `N = 40`. This entry stays on the bench until the folder's next commit.

## 19. 2026-10-31T19:06:07Z: the pull request

Blake opened OpenWave #687 at 2026-10-31T18:40:01Z, https://github.com/openwave-labs/openwave/pull/687. Its title and body equal `m8_18_pr_title_v1.txt` and `m8_18_pr_body_v3.md`, byte for byte. Its head is `f23dad7504020c1e7aa7cd483f38a1025394a69d`, one commit, and the task doc at the pull request's head has the terms' SHA-256, `924e7ee363a756a88ba2a9ee9bc03eb56c4fe27778c6e8f920a42a5229034a4c`. DCO passes, and it waits for review.

Next: the maintainer's review, and after the merge the merged tree diffed against this head. The go is kept unedited, and the freeze waits for it and Blake's word.

## 20. 2026-10-31T21:10:48Z: #687 merged; the approval and the go, read

Blake: "PR merged". Read through GitHub's API:
- **The merge:** [#687](https://github.com/openwave-labs/openwave/pull/687) merged at 2026-10-31T20:40:20Z as `a81d50c996694f32a750efc1d1014c5debb9b35b`, on `main` at `daa5f631`, by the maintainer. The diff from the head `f23dad7` to the merge is empty, so nothing was edited, and the merged task doc equals the terms, 44,825 bytes, `924e7ee363a756a88ba2a9ee9bc03eb56c4fe27778c6e8f920a42a5229034a4c`.
- **The approval,** [review 5724825686](https://github.com/openwave-labs/openwave/pull/687#pullrequestreview-5724825686): approved, with no blocking finding and no maintainer edits, at the reviewed head. It checked the terms, MIT `4bd8bbd` and the 185 sums, the copies byte for byte, the pin by its own listing, the twelve, the rule on 110 stored points by its own port, the moved midpoint, the rulings, the code against the terms and the code's intent. Its "Not checked" says the author's tests were read and not rerun.
- **The go,** [comment 6548866246](https://github.com/openwave-labs/openwave/pull/687#issuecomment-6548866246), unedited, names the terms `924e7ee3…`, MIT `4bd8bbd`, the pin `6d244f4a…` over 37 files and `SOURCES.json` at `c90e734e…`, and covers that pinned tree. Its order: `write_guard.py`, then the freeze block at `research/m8_18/freeze_block.md` with `FROZEN.json` in full, before the run. The adjudication will apply the reading notes in the approval.
- **Recomputed here:** the terms, the pin and `SOURCES.json` equal the go's, and the two run logs the approval names are the two `SOURCES.json` lists.
- **Kept verbatim,** each the API's body with one trailing newline: `../xrodz_approval_687_5724825686.md` `1ec0aafe20fcf217e52b1e6613db12370655e5c45134ce01d8151052555c6386` and `../xrodz_go_687_6548866246.md` `e239250116ca2d42bb07e80d19ee72acdce060bfacc14eb12352f977496d1df7`.

**The reading notes, each read at source. No note asks for a change, and none leaves a re-pin.**
1. **The exact rules assume the recorded environment.** Holds. `census.py` reads no environment before it starts. The launch chain runs `record_environment.py --check` before it, and the plan runs it after the run, as M8.17's did.
2. **A global stop and the rows.** Holds. § THE ROW OUTCOMES covers a gate's stop and a job's end, and not a global stop, so its "A failure" applies. `census['rows']` stays empty, and `census['arm_b']` stays None if Arm B itself stopped, with its record in `ARM_B.json`.
3. **The band's test at run time.** Holds. `band_failures` runs once, after the gate and the targets, and it skips Arm B's row. So the record must let the adjudication read the stored band of Arm B's guards: `tools/build_record.py` should show them.
4. **Closure per item.** Holds as a reading: the sentence is the terms', and the note rules nothing on S5.

**The checks before the write,** read-only, all clean: the go live equals its kept copy and has not been edited; the task doc on OpenWave `main` is at the terms' SHA-256; MIT `main` is `4bd8bbd`, with no commit touching the folder or the census page since; the manifest equals the pin; no freeze and no `run/out/`; `--check` finds no difference; all 40 reference copies equal their blobs; the OS is 15.8.2; the resume check is at its reviewed `9405929a…` and passes. One check read red on my own `cut` of a long path. Read in full, the only file that differs from the commit's tree is `DEVLOG.md`, and the commit's copy is a prefix of the bench's.

The Mac was on battery at this reading. macOS 27.2 is still on offer and not installed.

**Next, each on Blake's word:** `write_guard.py` with the go; the admissions and `--check`; the freeze block with `SOLVER_COMMIT` `4bd8bbd`, and its branch on the fork; Blake opens its pull request; `prelaunch_checks.py`, on mains power; the launch.

## 21. 2026-10-31T21:13:27Z: Blake's word for the freeze; the resume check and the launch command

Blake's word: "freeze it", after the checks in entry 20. They ran again just now, each clean, with this folder's files hashed before and after and unchanged: the go, live, equal to its kept copy and not edited; the task doc on OpenWave `main` at the terms' SHA-256; MIT `main` at `4bd8bbd`, with no commit touching the folder or the census page since; the manifest equal to the pin; the placed terms equal to `registration/`'s; no freeze and no `run/out/`; `--check` with no difference; all 40 reference copies equal to their blobs; the OS 15.8.2.

**The resume check,** recorded before the write: `../resume_check/resume_check.py`, `9405929a8518f5f5df68b0206c71d64fce90d4ea4921b01cebd4f1f4caae0971`, outside the folder. It reads `run/out/`, writes nothing, and refuses a launch on any sign of a stop. `test_resume_check.py` has 21 arms, with each check's removal caught, and `test_launch_wrapper.py` runs the command's form on stubs: both report 0 failed, and both were in the units' build review. It passes on the folder now.

**The launch command,** from the plan's text with that SHA-256 in place, from the folder, every launch the same:

```
set -o pipefail; caffeinate -i -m -s -w $$ & { printf '%s  %s\n' 9405929a8518f5f5df68b0206c71d64fce90d4ea4921b01cebd4f1f4caae0971 ../resume_check/resume_check.py | shasum -a 256 -c - && python3 -I -B ../resume_check/resume_check.py . && python3 -I -B run/record_environment.py --check | tail -1 && python3 -I -B -u run/census.py; } 2>&1 | tee -a ../census_console.log
```

Next: `write_guard.py` with the go.

## 22. 2026-10-31T21:15:04Z: the freeze written, `run/FROZEN.json` and its pin; the freeze block built

**The write:** `python3 -I -B run/write_guard.py` with the go wrote `run/FROZEN.json` at 2026-10-31T21:13:28Z, 72,874 bytes, `b5902494f927ec5daee1562fdf3d64bf3f402eb2cc9cac777de7a29aaa7c32d5`, and then `run/FROZEN_PIN`, which holds that SHA-256.

**Checked after it:**
- both admissions: `devtools.frozen()` admits the tree, and `census.frozen()` admits it with the same `FROZEN.json`;
- its fields against their sources: the terms' SHA-256; the manifest's, still equal to the pin; both also as the go names them; the go's link; the allowlist and the order, the 12 rows of `census_lib.RUN_ORDER`; 22 targets, the 21 reference files and `SOURCES.json`, each on disk at its SHA-256; the inherited section, equal to M8.16.1's `FROZEN.json`; the census values, equal to `census_lib.frozen_values()`;
- `record_environment.py --check`: no difference; the resume check: PASS; no `run/out/`.

**The freeze block:** `python3 -I -B run/freeze_block.py` with MIT's commit `4bd8bbd` in full wrote `../freeze_block.md` by exclusive create, outside the folder, 4,111 lines, `1ec71f2f0e1c8e92b17cdfeffc6d3b7d05ed72b5c6528b9e6c815c326e42ecfd`. Checked against its sources: the terms and the go; `FROZEN.json`'s time and pin; the solver commit; the manifest's 37 rows and pin; the environment as recorded, with no difference read again; the 22 reference rows; what is inherited from M8.16.1; `FROZEN.json` in full, byte for byte; and the order. No home-folder or scratch path, and `check_no_local.py --require-files` is clean. It names the interpreter's system path, as M8.17's did.

No sealed reading has been computed. Next, on Blake's word in this round: the block on the fork, for Blake to open. Then the launch, on Blake's word, on mains power, after `prelaunch_checks.py`.

## 23. 2026-10-31T21:16:05Z: the freeze block's branch on the fork; the pull request's text on Blake's clipboard

- **Before branching,** with `upstream` and the fork fetched: OpenWave `main` at the merge `a81d50c9`, with no M8 commit since it; no `research/m8_18/` upstream; the task doc on `main` at the terms' SHA-256; the branch's name free; the clone clean, in its local identity, the noreply address.
- **The branch,** `m8-18-freeze-block-2026-10-31`, on `upstream/main` `a81d50c9`, adds one file, `openwave/xperiments/m8_mit/research/m8_18/freeze_block.md`: the bench's `../freeze_block.md`, byte for byte.
- **The checks,** on the branch: `check_no_local.py --require-files` is clean on the block, and `check_roadmaps.py` and `check_models_md.py` are clean.
- **The commit,** `23393ced03ab519f73ecb6ab017b145919e8d78c`, parent `a81d50c996694f32a750efc1d1014c5debb9b35b`: 1 file, with author and committer the clone's identity. Its message is `../filing_drafts/commit_freeze_block.txt` with its values filled, with the DCO sign-off and the Co-Authored-By line.
- **Pushed to the fork,** and read back through GitHub's API: the block equals the bench's, `1ec71f2f0e1c8e92b17cdfeffc6d3b7d05ed72b5c6528b9e6c815c326e42ecfd`, and the branch is one commit ahead of `main`, with one file.

**The pull request's text:** the title in `../m8_18_freeze_pr_title_v1.txt`, and the body `../m8_18_freeze_pr_body_v1.md`, `adcc3b6f9bdc2195a6b0b42bc142d10b752059c73799991ee88a7facff81c58d`, on Blake's clipboard. It carries Blake's reviewer line. Both links answer 200, and GitHub's renderer gives 1 table, 2 rows and 7 list items.

**`prelaunch_checks.py`, read-only, with no pull request yet:** 12 ok and 1 failed. The failure is mains power: the Mac is on battery. It reports 346 GB free and macOS 27.2 on offer, not installed.

**Next:** Blake opens the pull request; it is read back; then `prelaunch_checks.py` with its number, on mains power, and the launch on Blake's word, once it is open and DCO passes.

## 24. 2026-10-31T21:45:39Z: #688, the freeze block's pull request, opened by Blake; read back; the checks before the launch, clean

Blake opened [#688](https://github.com/openwave-labs/openwave/pull/688) at 2026-10-31T21:17:17Z. Read back: the title and body as drafted, byte for byte; head `23393ced03ab519f73ecb6ab017b145919e8d78c`, one commit, one file, the block equal to the bench's byte for byte, `1ec71f2f0e1c8e92b17cdfeffc6d3b7d05ed72b5c6528b9e6c815c326e42ecfd`; DCO passes.

`prelaunch_checks.py 688`: 17 ok, 0 failed, on mains power, with `run/out/` absent, so no solve has run at `N = 40`. For the record: 346 GB free, and macOS 27.2 on offer, not installed.

**Next:** the launch, on Blake's word, with the checks read again just before it.

## 25. 2026-10-31T21:52:29Z: the registered run, launched on Blake's word

**The go:** Blake's own word, "Run", with #688 open and DCO passing, before its merge, as its body says.

**The checks before the launch,** read just before it: `../prelaunch_checks.py 688`, 0 failed, kept as `../prelaunch_checks_launch.out`, `820dc69ed28b0f1d1c626475a7172afa1aead21f351580135955028e548be236`.

**The command:** entry 21's, read from this log and run unchanged, from this folder, as a background task in the app's shell, zsh (task `bgg8fplvd`). Its output shows live in the app's background-task panel and goes, through `tee -a`, to `../census_console.log`.

**The start, read back:**
- the console log: the hash check `OK`; the resume check `PASS`, with `run/out/` not yet existing; `--check` with no difference; and the run's first line;
- `run/out/RUNLOG.json`: the manifest at the pin, `6d244f4af56b71d60f17077724628b7489b278e84a7d24565c17038ed19ba43a`, no job completed, the run started at 2026-10-31T21:51:23Z with the twelve rows in their registered order, and `arm_b` started;
- `census.py` running as one process, with `caffeinate -i -m -s -w` on its shell.

**Power:** mains.

**The cores.** As the run started, Blake: "You know I have multiple cores too...". The facts: the machine has 8 cores, 4 performance and 4 efficiency, and 24 GB. The pinned code has no pool or second process, and it runs one job at a time in the order the terms fix. Sampled just after the start, `census.py` used 100% of a core. Its BLAS is Accelerate's, with no thread variable set, as the environment record fixes. Using more cores would change the pinned code and the terms' order, so it needs a new pin, go and freeze. The launch went ahead on Blake's word.

## 26. 2026-11-01T13:33:46Z: the run's end: T4/R5 located; Arm A ended at the control gate

**The end.** Task `bgg8fplvd` exited 0, in one launch: started 2026-10-31T21:51:23Z, record written 2026-11-01T13:17:32Z, 55,569 s. No stop, and no job was left unfinished. 57 jobs completed, and the largest peak resident size logged is 3,702,833,152 bytes. `/Library/Logs/DiagnosticReports/` holds no `JetsamEvent` report from the run. The 55 to 70 hours estimated included the targets, which did not run.

**Arm B.** All 12 recomputed path points and all of M8.17's midpoints reproduced. At `N = 24` and 32, K1 refused the midpoint 8.721637690696875, which stays in the record and decides nothing, and it held at the moved point, 8.720990482005668, where `n(L)` reads 7. Both deciding cutoffs complete on [8.720990482005668, 8.724873734152915]. `N = 16` completes on [8.851079428938467, 8.854315472394507], reported. The lower guard at 8.633780577185611 reads Elliptic. The upper guard at `δ = 0.01`, 8.812122471494444, reads Unresolved, with `n(L)` 7 at `N = 16` against 6 at `N = 24` and 32, as § The guards inferred. The retry at `δ = 0.05`, 9.161117420860561, reads Hyperbolic. The run names it: "a change of type located between the guard readings, with n(L) changing by -1 inside the interval at N = 24 and 32". T4/R5's outcome is Each change of type located, and `meets_s4` is true. Every guard's stored band equals `sqrt(18 × 20) - sqrt(λ)`, `R5`'s frozen level, for the third note of #687's approval.

**Arm A's gates.** The controls' paths at `N = 24` and 32 ran with no reproduction failure. The kernel at `N = 40` passed on all seven controls: each seed passed, every point was accepted, K1 held, and C1 passed at its four cutoffs. The control gate did not pass: 22 of the 24 points read converged with their recorded type and indices, and branch identity held on both pairs at all 24. The two that did not:
- P5 at `ε = 0.25`: "eps = 0.25: Unresolved, None: tested set at 8.67568e-16+4.02029j (+1): non-contracting above the floor";
- C3R/R4 at `ε = 0.25`: "eps = 0.25: Unresolved, None: structure: a record is unresolved", from the `N = 40` record's "n(D): an eigenvalue of D lies in its gray zone".

As the terms state: "A failure inside Arm A's gates ends Arm A. The twelve stay unclassified, and the record is written." No target was solved or read, at any cutoff.

**The rows.** T1/R4, open 5; T4/R4, open 6, its five points and the change across 4, not located; T1/R5, open 1; T5/R2, open 3, 45.25 and the unadmitted 128 and 132; T4/R5, located. Each of the twelve carries `not_read`, naming the gate, and keeps M8.17's cause. § THE ROW OUTCOMES: "that is not a second outcome with that cause". So S6's first sentence is not reached for them, and S6 on T5's row, which waits for 45.25 to be read again, is not reached either.

**The cause, read after the run.** This is a diagnostic outside the run, in `dev/runs/019_gate_cause/`, on a scratch copy and the stored outputs. It scores nothing and changes no record. Its six reads reproduce the stored `type`, `nL`, `nD`, `K`, `margin`, `unresolved` and `normA`.
- **P5.** Two Krein-positive eigenvalues near 4.0203 sit 1.1345×10⁻⁵ apart at `N = 24` and 32, and each moves by less than 1×10⁻¹⁰ from 24 to 32. `linear.record` links eigenvalues within `τ(λ) = max(margin, 10 sqrt(u ‖A‖ |λ|))`, and ‖A‖ grows with the cutoff: 576, 1,040 and 1,632. So `τ` is 7.1726×10⁻⁶, 9.6363×10⁻⁶ and 1.2071×10⁻⁵, and it passes the gap at `N = 40` alone, by 6.4%. There the pair is stored as one group of size 2 at its mean, and the set's change from `N = 32` is half the gap, 5.6726×10⁻⁶, against 5.3902×10⁻¹¹ from 24 to 32 and the floor 5.5336×10⁻⁷. That is the rule's "non-contracting above the floor". Across all 24 control points, this is the only pair inside the tested band that `τ` links at `N = 40` alone (`tau_band.out`).
- **C3R/R4.** D's negative eigenvalue is -0.01596075 at all three cutoffs, to the seven digits printed. `n(D)`'s gray zone is read against ‖B‖, 576.141, 1,040.140 and 1,632.310, and its top, `10⁻⁵ ‖B‖`, is 0.00576, 0.01040 and 0.01632. It passes 0.01596075 at `N = 40` alone, by 2.3%.
- At both points the `N = 40` record reads Hyperbolic with (5, 1, 4), the recorded type and indices. The gate asks for a converged reading, and it was applied as the terms state. Both failures are at the controls' smallest amplitude, and neither feature moved with the cutoff (DERIVED from the records and the six reads).

**What could have seen it.** Neither crossing needed a sealed reading. The pair's gap is in the stored `N = 32` record, D's eigenvalue reads in 3 s at `N = 24`, and ‖A‖ and ‖B‖ at `N = 40` follow from the top level, about `N(N + 2) - λ`. No check of the frozen tolerances at `N = 40`'s norms was run before the filing.

**After the run.** `--check` finds no difference, kept as `../environment_after_run.out`, `37ff13a0681f43a7454612ddc5ea580af7723af9acb9b7afb705e1003497b0b7`, with the OS at 15.8.2. `../census_console.log` is copied byte for byte to `run/out/census_console.log`, `34547133730260cd8544c5f99c8747484b3ad561765d643a0b64e0c547eaae64`. `run/out/` is otherwise as the run left it.

**#688.** Merged at 2026-10-31T22:01:22Z, as `bdc8fae84c4f9e4a524388ac870096d1edb651cc`, with no maintainer edits: the merge's tree equals head `23393ced03ab519f73ecb6ab017b145919e8d78c`'s. The approval is kept verbatim as `../xrodz_approval_688_5725136193.md`, `fd89717757c6c3e9ca3fefe8a2ea0c856d043cc0408edbe3bc6d657a910d87c7`. It finds nothing and asks no change. It adds to the adjudication: `resume_check.py` and its arms are published with the record and read in full, and the run's log is read against the go, the written time and the pull request's opening. The launch was after that opening, 21:17:17Z, as its body says.

Nothing is committed, pushed or posted. What follows the record for the twelve is Blake's decision.

## 27. 2026-11-01T16:38:59Z: the record and the method note, drafted for the units; the tests reproduced after the run

**Blake's decision,** the bench's log, entry 152: M8.18 closes as registered, with the record, the method note and the adjudication; a short notice goes on #512 once the record is on MIT; the remaining values are computed on MIT's side, outside OpenWave's column. Nothing in this folder is repaired, and no record changes.

**The record.** `RECORD.md`, 5,409 words, `b993be28e8163c499ccfed4e8b538bcb8e53bda23cbbe1203e9a8aa4f5e39cdc`, built by `tools/build_record.py`, `ef05f6684adabb7405624d0b8054bb558202ce30608d714cd576684f6f1ff716`. The builder follows M8.17's. It recomputes the rows with the frozen `census_lib.assemble` and the gate with `lib.control_failures` and `lib.kernel_failures`, and refuses unless they equal `run/out/CENSUS.json` and `run/out/GATE.json`. Its --check reproduces the record. § 4 is the diagnostic of entry 26, marked as made after the run. § 7 gives each row's standing and reports three statements that bear on S6, without applying it.

**The arms.** `../record_arms/arms.py`, on a copy of this folder: 14 changes each make the builder refuse for its named reason, an edit to `RECORD.md` makes --check exit 1, and the restored copy reproduces. `../record_arms/arms.out`, `9653b387c9431b169668a0d3f9539e32f3293ae66485830d9364b71ca31e28db`, reads 0 failed.

**The tests after the run,** from copies of this folder, with nothing touching it. `run/test_constants.py`, `run/test_reader.py`, `run/test_locator.py`, `run/test_scope.py`, `run/test_freeze.py`, `launch/test_resume_check.py` and `run/test_gate.py` each exit 0 with nothing on stderr, and each rewrites its output equal to the one here, byte for byte. `test_gate.py` took 6,614 s. `test_reader.py` reads the same with the freeze's two files present and with them removed, so `REPRODUCE.md` carries no caveat for it, unlike M8.17's. `launch/test_launch_wrapper.py` was not rerun: it reads bench files that are not published, as `REPRODUCE.md` says.

**`REPRODUCE.md`,** post-run, `c1659afc56327ff2b18d65248765500b25c1ac5342c07b339776bcaf582f41a5`: the diff against `4bd8bbd` is `../REPRODUCE_postrun.diff`.

**The post-run files placed:** `launch/`, `prelaunch_checks_2026-10-31.txt`, `environment_postrun_2026-11-01.txt`, `run/out/census_console.log` and `dev/runs/019_gate_cause/`. `run/out/` is otherwise as the run left it. `SHA256SUMS` stays the pre-run inventory until the record's commit, where it is written fresh, last.

**The method note,** `../m8_18_note/m8_18_method_note.md`, 2,681 words, `da46e0a657b00fa12f6a09f773076102bfe8f66172085af536cd1758b098edc9`: 34 code links and 3 links to the record checked. The record's commit stays marked `⟨record-commit⟩`, and § 8, the audit record, waits for review.

**The notice,** `../notice_512_v1.md`, `bded12723e98ca04eac078b4c7ebb7b02df3ebcb28b7a0c415a50101ab2ec7af`: a draft for #512, for after the record is on MIT, asking nothing. Blake posts it.

Nothing is committed, pushed or posted.

**Next:** the units' review of `../m8_18_record_packet_v1.md`. Then, each on Blake's word: the MIT commit, with this log through the commit's entry and `SHA256SUMS` regenerated last; its push; the OpenWave branch filled with that commit; and Blake opens the pull request.

## 28. 2026-11-01T19:45:30Z: the units on the packet, adjudicated; P5's pair read at `N = 40`

**The verdicts.** UA: GO on items (a) to (d), and HOLD on one sentence of the notice. UB: HOLD for three FIXABLEs, none FATAL, with GO on (c) and (d). UB recomputed the gate, the kernel, the rows and Arm B from `run/out/` and found no number wrong, and UA checked all 78 logged output files against their SHA-256. Each finding was checked at source.

- **UB 1, S6 leaves out the twelve's own case: taken.** The census page's note of 2026-10-30 names two cases, no remedy admitted and a remedy that meets the same cause again. The twelve, and T4/R4's change across 4, are in neither: a remedy was admitted and ran, and its gate stopped before it read them. `RECORD.md` § 7 gains that fourth statement, § 11 carries it to the adjudication, and the note's § 5.3 follows. One addition to UB's text: the request of 2026-10-29 asked about "an admitted remedy ends without resolving its obstruction", and the answer reads "Yes, your reading of S6 holds". That bears on the same question, so the adjudication has both.
- **UB 2, the DERIVED grade held for C3R/R4 only: taken, by UB's better fix.** `dev/runs/019_gate_cause/pair_gap.py` reads P5 at `ε = 0.25` at all three cutoffs from the stored solutions, on a copy of this folder, and takes the eigenvalues before they are linked. Its output, `7bd6bcb9c1fb0766525504de0f7f1420f7bb61262ae6b4deb2fbe531413dbde4`: the gap is 1.1345×10⁻⁵ at each cutoff; the pair is one group at `N = 40` alone; from 32 to 40 its members move by 7.5×10⁻¹⁴ and 1.8×10⁻¹⁴; and the three reads reproduce the stored records. So DERIVED holds at both points, and § 4 and the note's § 5.1 say so. The builder now reads this output and refuses if it differs, with three new arms.
- **UB's NITs: taken.** "The twelve cases of `census_lib.RUN_ORDER`", and "On the recorded machine," before the reads in § 4.
- **UA, the notice's sentence on the corrections, and UB 3, its undertakings: taken together,** in `../notice_512_v2.md`, `a1506ea956b7ea55dd1d5150f42e4bf6eb36c7ac28f8952c4a5051c4e7fce1d5`. It names the instrument and the two tolerances, says the computation is a repaired one outside this thread and not an M8 outcome, says the method is stated before any MIT-side reading of the twelve and revises nothing here, says those values take no part in S6 on the census page, and replaces "This asks nothing of you" with UB's line on the comment of 2026-10-29. Its sentence that the sequel follows the census's close, S5 included, restates what was posted. Whether that stands is Blake's call.
- **UA's NIT on `REPRODUCE.md`: taken.** The tests write beside their scripts, most of them under `run/`.
- **UA's caution on the grade:** the DERIVED statement covers these two numerical mechanisms only, not the branches and not the twelve's causes. § 4 and the note already keep to that.

**After the edits:** `RECORD.md`, `d62d88fc7d6fab0fbaa5222b63ab2a8452265876d4a3b42cde3e2f4c4443c7f5`, built by `tools/build_record.py`, `873afd0127b6057a9d1d93e4fc50a8828b9b7de08c0250798c7075000d0da313`, and --check reproduces it. The note, `eecd931db2393d93f0650af6b9245b90135666ac7f67920e0310506dfd1d9b36`, is rebuilt with its links checked. `../record_arms/arms.out`, `286daeb9314fbba4a0bd897bcc487ac1861dfb44372baacedc68f3521224cdaa`: 17 changes refused, the edit to the record caught, 0 failed. No run file changed.

Nothing is committed, pushed or posted.

**Next:** Blake's call on the notice's S5 sentence, and `../m8_18_record_packet_v2.md`, for the units to confirm the holds. Then, each on Blake's word, the MIT commit and what follows it.

## 29. 2026-11-01T20:05:35Z: the units on packet v2, adjudicated

**The verdicts.** UA: GO on v2, with no further redlines. UB: the grade on the gate's cause and both NITs cleared, and `pair_gap.py` rerun, with the gap and the linking as stated. Two holds remain, each with its text given. Both units would keep the notice's S5 sentence, and Blake sent v2 with it as drafted, so it stays.

- **UB 1, the S6 quote: taken.** The phrase and the "Yes" quoted alone read as covering the twelve, whose remedy never met their cause. § 7 and the note's § 5.3 now give the request's question in full, its reading "through S6's first sentence where a remedy meets the same cause again", and the answer's two named cases. One change to UB's text: "read its own question" becomes "read the ruling of 2026-10-20 as covering these cases", which is what the request says. All the quotes were checked against `../posted_19277944.md` and `../ruling_2026-10-29_19278753.md`, byte for byte.
- **UB 2, the notice: taken,** in `../notice_512_v3.md`, `3267b6da46e81b9cdbdd9208cbfda655cd150935eb9487f6cc35b3c9a65c868c`.
  - `linear.record` applies `τ(λ)` inside each cutoff's record, before the rule compares anything across cutoffs, so the tolerance is now named as "the distance within which `linear.record` links two eigenvalues into one group". The lead-in reads "changes in how it treats the two tolerances", which holds whether the MIT-side method changes `τ` or only how the rule reads it.
  - The ruling's failure row has no scope, so the notice now quotes it, adds "Nothing under M8 is", and says that the MIT-side computation reads the twelve on this instrument again, so "your condition's words may reach it". UB's "reach" becomes "may reach", which fits a question.
  - The last paragraph takes UB's question: "does your condition reach a computation outside this thread?", with no MIT-side reading before the maintainer has had the chance to say. Whether the notice asks is Blake's call. The draft asks, and the plan of 2026-11-01 said it would ask nothing.
- **One change of my own.** UB's rerun gives P5's members moving by 8.0×10⁻¹⁵ and 6.2×10⁻¹⁵ from 32 to 40, against 7.5×10⁻¹⁴ and 1.8×10⁻¹⁴ here. Those digits are rounding, so `RECORD.md` § 4 and the note's § 5.1 now say "less than 10⁻¹³, the size of rounding". The builder and the note's builder refuse above that, with a new arm. `pair_gap.out` is unchanged.

**After the edits:** `RECORD.md`, `42112071d12b0c8d7e550eec04b1121f8ff4004c4e96d912dbb03121a0d4d73a`, built by `tools/build_record.py`, `41adab6241fbbf3ff0451c4ba458daf1be9ac9141b89d352ab7c58c78a30f392`, and --check reproduces it. The note, `0215cbbaaaad2194aa371902d1d53634acbab4872141571ebdebe7690ffb9b4c`, is rebuilt with its links checked. `../record_arms/arms.out`, `f6415d257fd99d6539ba4d6f061a7a6023d23abf30dd048cc29bf906855020f2`: 18 changes refused, the edit to the record caught, 0 failed. No run file changed.

No further review round: UB gave each replacement, and UA has no further redlines.

Nothing is committed, pushed or posted.

**Next:** Blake's call on whether the notice asks. Then, on Blake's word, the MIT commit, with this log through the commit's entry and `SHA256SUMS` regenerated last.

## 30. 2026-11-01T20:18:45Z: the units on v4: GO; the record's publication

Blake relayed both units and gave the word: "commit and push if good w/". Each verdict is read at source.
- **UB's check of the bytes:** GO. UB read v4 against v2: the record, the note and the notice changed as listed, `run/` is byte-identical to v1, and `dev/` to v2. `build_record.py --check` reproduces the record, its 18 checks end in "0 failed", and every quote matches its source. UB's text is improved at "read the ruling of 2026-10-20 as covering these cases", and "less than 10⁻¹³, the size of rounding" is fair: both machines' movements fall under it, and so does the eigensolver's error at `N = 40`, about 3.6×10⁻¹³.
- **UA:** GO on the record, the note and v4. Its ASK fell with Blake's statement that the answer would not decide the computation, and it reran the record's check.
- **Whether the notice asks.** Blake: "leave no stone untruned on the survivying ray so we can continue the M8 dynamics program." So a "yes, it reaches" would not stop the MIT-side computation, and `../notice_512_v4.md`, `0990696f05812f7c12ce791c4f4c532312394569de4cc5652d5d6e3dbd3939d4`, tells: it names the departure from the comment of 2026-10-29 and says we intend to proceed, before any of the twelve is read. It is posted once the record is on MIT and its links are filled in. Both units read the risk the same way: telling first establishes transparency, not agreement, and no audit is guaranteed.
- **The publication,** on MIT, in this folder, as § DEFINITION OF DONE states: the record, `REPRODUCE.md` and the run's outputs, with the post-run files, and this log through this entry. After this entry `tools/build_record.py --check` runs, and `../publish_checks.py --write` regenerates `SHA256SUMS` last, with its five checks. This entry cannot name its own commit, so the commit and its verification are recorded on the bench and in the program log.

**Next:** the method note, built with the record's commit and its audit record, on an OpenWave branch for Blake to open, on Blake's word; the notice; then the adjudication.

## 31. 2026-11-01T20:20:56Z: the record committed and pushed to MIT `main` (bench-only)

On Blake's word ("commit and push if good w/"), after entry 30:
- **Before the commit:** `tools/build_record.py --check` reproduced the record after entry 30. `../publish_checks.py --write` then regenerated `SHA256SUMS` last, `1614ab087d3c2cad58e63f66a52c71f80d667c5da117223e40974116869a346d`, and its five checks passed, with the generator first rebuilding `4bd8bbd`'s inventory byte for byte. The scan found no home-folder or scratch path and no email-shaped string.
- **The worktree** stood at MIT `origin/main`, `4bd8bbd8e3c60a387210c4464bf0c7915d10bdc3`, clean. This folder was copied in, equal to the bench byte for byte: 100 new files and 3 changed.
- **The commit,** `5241a2d50baae390f8b90a2c8ae0ba08366236d4`, parent `4bd8bbd8e3c60a387210c4464bf0c7915d10bdc3`: 103 files, all in this folder, in the MIT commit identity that `4bd8bbd` carries. Its message is `../commit_record.txt`.
- **Verified from its own tree:** the record reproduces, `shasum -a 256 -c SHA256SUMS` passes on all 285 files, the regenerated inventory equals `SHA256SUMS`, and the folder equals the bench's file for file.
- **The push:** a fast-forward. Read back through GitHub's API: `main` is the commit; the record, `SHA256SUMS`, `REPRODUCE.md`, this log, `run/out/CENSUS.json`, `GATE.json`, `RUNLOG.json`, `ARM_B.json`, `run/FROZEN.json`, `launch/resume_check.py`, `pair_gap.out` and the builder each equal the commit's blob; the folder holds 286 files; and the published log is this one through entry 30.

This entry, being after the commit, is on the bench only.

**Next:** the method note, built with the record's commit and its audit record, on an OpenWave branch for Blake to open, on Blake's word; then `../notice_512_v4.md`, with its links filled, posted by Blake; then the adjudication.

## 32. 2026-11-01T20:41:57Z: the method note on the fork; the pull request's text on Blake's clipboard (bench-only)

On Blake's word ("start the OpenWave filing"):
- **The audit record,** `../m8_18_note/audit.md`, `bd1749e2e8264268b20fb333d8888ab9f7d85f21adfc82ddecf30d510e3fc8ab`: the three rounds of checks before filing, what they led to and that no reading changed, with no review unit named.
- **The note,** `../m8_18_note/m8_18_method_note.md`, `782bc0f4a66d2e9cbecd2f4f750ceb54b1c29b3bcf2639cd69d5923ed2d42fab`, rebuilt with the record's commit, MIT `5241a2d`, and that audit record. From v4 only the three record links and § 8 change. The builder checked the 34 code links and the 3 record links against MIT's objects, and every OpenWave link at `upstream/main`. The record links resolve on GitHub at `5241a2d`.
- **Before branching:** OpenWave `main` at `82a470085a885f3430e59643dd5911d135cd3394`, with no M8 commit since #688's merge; no `findings/m8_18_method_note.md` upstream; no pull request open; the branch's name free.
- **The branch,** `m8-18-run-record-2026-11-01`, on `upstream/main`, as #676 carried M8.17's:
  - `findings/m8_18_method_note.md`, new: the note, byte for byte;
  - `m8_roadmap.md`: M8.18's BACKLOG row's gate, "the maintainers' adjudication of the run", linking the note.
- **The checks:** `check_roadmaps.py`, `check_models_md.py` and `check_no_local.py --require-files` on both files are clean.
- **The commit,** `6bdd908684729992c2ac3d9ed3191fdda92a9349`, signed off for the DCO in the clone's noreply identity, with the Co-Authored-By line. Its message is `../filing_drafts/commit_note.txt`. Pushed to the fork, the branch's head is the commit, the note and the roadmap read back byte for byte, and it is one commit ahead of `main` with two files.
- **The pull request's text:** the title in `../m8_18_note_pr_title_v1.txt`, and the body, `../m8_18_note_pr_body_v1.md`, `d030ada568436ff201469235bac2c038b296337ffc9b185ff9720e453ec00ddd`, in #676's form, with Blake's reviewer line. Its four links resolve, and GitHub's renderer gives 1 table, 3 rows and 12 list items. The body is on Blake's clipboard.
- **For the units, if Blake sends it:** `../m8_18_note_review_v1.zip`, since § 8 reports their checks and they have not read it.

**Next:** Blake opens the pull request; then `../notice_512_v4.md`, with its links filled, posted by Blake; then the maintainers' adjudication.

## 33. 2026-11-01T20:49:14Z: #692, the method note's pull request, opened by Blake; read back; the notice filled (bench-only)

Blake opened [#692](https://github.com/openwave-labs/openwave/pull/692) at 2026-11-01T20:47:29Z. Read back: the title and body as drafted, byte for byte; head `6bdd908684729992c2ac3d9ed3191fdda92a9349`, one commit, two files; the note equal to the bench's; DCO passes; mergeable.

**The notice,** `../notice_512_v5.md`, `86318a7fb089231899acf0a0df5e93afef3cd7d61157dbb33fd22f1b9f5ac25b`: v4 with the record's link, #692's link, and "@xrodz," at the start, as both earlier comments on the thread carry (`../notice_512_v4_to_v5.diff`). Its two links resolve, GitHub's renderer gives 2 list items and the mention, and it is on Blake's clipboard, one line per paragraph.

**Next:** Blake posts the notice on #512. Then the maintainers' adjudication of #692, and after any merge the merged tree is diffed against the head.

## 34. 2026-11-01T20:53:05Z: UA's NITs on the notice, taken (bench-only)

Blake relayed UA's three NITs, "if you want them", and all three are taken in `../notice_512_v6.md`, `1fd2dfbe105bc5d9013f3e4d5ddff7e831b5363c7f90d0d3b1e08f1488852d1d`:
- "completed without a global stop", since Arm A ended at its gate;
- "Neither tolerance issue required a sealed reading to anticipate", since "crossing" is the spectral word here;
- the audit sentence, which now says a separate audit, with "its own request".

The third differs from UA's text in two places. It keeps "its full suite of results". And "That would not resubmit the twelve points to M8" becomes "it would not reopen M8.18", since the earlier papers' audits were M8 tasks, and the sentence should not rule out an audit of the sequel there. Its two links resolve, and it is on Blake's clipboard.

## 35. 2026-11-01T23:07:59Z: #692 merged; the adjudication: M8.18 stands as recorded; the answer on #512; T5J (bench-only)

Blake: "both PR merged and #512 response". Read through GitHub's API.
- **The notice.** On #512 as comment 19338258, 2026-11-01T20:58:51Z, a reply under the comment of 2026-10-29, equal to `../notice_512_v6.md`. Kept: `../posted_19338258.md` `b6f8030c20d156194ca4bac85ed451269870a47875ea94e61f86e9ec11a06100`.
- **The merge.** xrodz approved [#692](https://github.com/openwave-labs/openwave/pull/692) (review 5730646319) at 22:50:22Z and merged it at 22:50:31Z as `1276adefda317ead27b1d41ccf21f7ccc59633bb`. The merged tree is the head's, `fc2ff6be2bb656f95b29c4ec6de7944b127967a4`, so there is no maintainer edit, as the approval says. The approval is kept verbatim: `../xrodz_approval_692_5730646319.md` `08ebd0edda33ce5fc1036df77ceee3c6610caceb9bf6ec37e0fff5861ba4f7e4`.
- **The adjudication:** "M8.18 stands as recorded, with no blocking finding and no maintainer edits."
  - T4/R5: Each change of type located, meeting an S4 completion condition, its identification with the genuine index crossing not claimed.
  - The kernel at `N = 40` passes on all seven controls. The control gate does not pass: P5 and C3R/R4 at `ε = 0.25` read Unresolved, and the other 22 of the 24 points pass.
  - The twelve: none solved or read at any cutoff, each keeping M8.17's cause, no type claimed. T1/R4, T4/R4, T1/R5 and T5/R2 are Not settled by this run, with 5, 6, 1 and 3 items open.
  - Every recomputation is the maintainer's own code over the published files at `5241a2d`. They ran no script of ours and no solve.
- **S6, ruled.** The two questions are answered, and the reading is a standing rule the census page applies:
  1. S6's first sentence does not reach these items: no instrument met their causes a second time.
  2. S6's last sentence does, as a ruling. The clause of 2026-10-20, "an admitted instrument that can no longer qualify, overall or for a row, is not an instrument that removes a cause", is extended to a remedy whose control gate stopped it before it read the item. Each item closes on the census page as instrument-limited, with no ruling per cause.
  3. The cause named for each of the twelve is M8.17's, as `run/out/CENSUS.json` keeps it, with the gate beside it.
  4. T4/R4's change across 4 closes with its point: not located.
  5. T5's row: S6 is applied now, since the premise that 45.25 would be read again no longer holds. 45.25 stands with the twelve, 128 and 132 stand as no remedy admitted, and no cause is claimed as shared with the finite-element instrument.

  Classified points keep their types, S5 still applies to their Elliptic stretches, and the approval does not rule on S5.
- **Two comment-tier items, no change asked:**
  1. "Where is M8?" and "What decides the program?" still read M8.18 as pending; they fit the close-out, with the Done row.
  2. `RECORD.md` § 1 and the note's §§ 3 and 8 say 57 jobs were each started once; the log has 56 `started` events and 57 `completed`, since `gate` logs only its completion. Verified at source: exactly that, and no other job. It is my wording in `tools/build_record.py`, line 400, and three rounds of checks passed it. M8.16.1's and M8.17's logs have no `started` events, and neither record carries the phrase. `RECORD.md` and the note are pinned in the approval, so neither is edited: the correction goes beside them in the close-out.
- **Three reading notes:** the gate stands as applied; § 5.1's missed check "holds on this side too", since neither the answer of 2026-10-30's replay nor #687's review computed the tolerances at `N = 40`; and the location rests on one designed midpoint, as foreseen.
- **The pins** equal ours, recomputed here: `RECORD.md`, `run/out/RUNLOG.json`, `run/out/CENSUS.json`, the note, the record's commit and the head. The quotations of the ruling of 2026-10-20 and of the review standards are exact.
- **The commitments.** The S6 reading binds the census page and the maintainers at this merge. The close-out is the author's to file and the maintainers' to review: the Done row, both status rows and the census page's dated note.
- **[#693](https://github.com/openwave-labs/openwave/pull/693),** the maintainer's, merged as `7fd5d46b`: one row in the review standards' lessons log on #692. Before a new input range freezes, evaluate each frozen tolerance at that range's scale against the stored quantities it separates. It is the same rule this project took from the failure.

**The answer on #512,** comment 19339563, 2026-11-01T22:50:40Z, kept: `../answer_2026-11-01_19339563.md` `7ed96596b320c643b431f43ae17c59561ed011e080effc557b7ff2e24479be3e`. The condition "binds M8's registrations and what the census counts under S6. It does not reach what you compute in your own repository." We told, and "there is nothing here to admit". It solicits nothing, authorizes nothing and creates no queue. It answers our closing question with how OpenWave's record will read the computation:
1. **A different instrument.** The changes take the code off M8.16.1's pin, `8cc2d7e2…`, so M8.16.1's qualification, the admission of 2026-10-15 and the adjudications of M8.17 and M8.18 do not carry to it. An audit would not read "the same harmonic Galerkin instrument" without that sentence.
2. **The design.** An audit would look in the dated note for whether the changes were chosen knowing M8.18's gate failure, the 24 control readings and M8.17's stored readings at the twelve, and for what the changed code was tested on before it read the twelve. "Readings already on record are not new evidence for the changed code."
3. **The census's accounting.** Our comment of 2026-10-29 fixes the S5 stretches from the classifications on record, so an MIT value at those points selects no stretch on OpenWave's record.
4. **The grades.** No M8 outcome, no `MODELS.md` cell, read as MIT's own.

**The audit:** nothing is accepted or pending. A request is reviewed on arrival under the conditions the platform sets then; "the platform reproduces computations to a frozen spec; it does not derive on request"; and a request would say which results rest on the changed code.

**A correction: the preview of the fix.** I told Blake on 2026-11-01 that candidates A and B change exactly the two failed readings, and that held on 163 readings. That set left out M8.16.1's rows: the folder's `reference/m8_16_1/` keeps only the controls. It was not "every saved reading". On all 262 stored readings (M8.18's 24, M8.16.1's 123, M8.17's 115), rerun for this entry, the as-built rule reproduces all 262 and the candidates change three: P5 and C3R/R4 at `ε = 0.25`, and T5J/R2 at `ε = 0.25`. No M8.17 reading or reason moves. `../mit_side_design/preview_fix.py` `1013ea8e82539df42651843685bb02bca537391c48bccceb4f31ea1ac9b41565`, `preview_fix_all.out` `1fc429763bf02b1bb6ed768c8e77596afe7c2946bf9109f17a82cdc5bc5e63fa`. The earlier statement was never published. None of this is in the record or the note.

**T5J (INFERRED).** T5J at `ε = 0.25` is the one reading behind T5's second member's "not qualified" on K5 in M8.16.1. Its reason, "partner set at 6.01511j (+1): non-contracting above the floor", is the same mechanism as P5's, at a lower rung. The pair is 8.78×10⁻⁶ apart at `N = 16` and 24, and one group of size 2 at `N = 32`; `τ` is 4.22×10⁻⁶, 8.27×10⁻⁶ and 1.13×10⁻⁵. So the tolerance passed the gap between 24 and 32, with the gap 1.06 `τ` at 24. The record's change of 4.8×10⁻⁶ from 24 to 32 is a member against the merged centre, half the gap and the mean's move, against 9.7×10⁻⁷ from 16 to 24. M8.16.1's `DEVLOG.md` recorded the merge in its review and nobody named the cause; I did not, and neither did the units or the maintainer. It stays INFERRED because the pair's gap at `N = 32`, before linking, is not stored: `run/out/` keeps a solution for P5 alone, so reading it needs a solve. `../mit_side_design/t5j_tau.py` `2ea74cfd665b9860e8aa8cb27f1162090fac6204ba33fea1b41931bad337abb4`, `t5j_tau.out` `ba730d5c795881b51dfc2fc45b84f4167fca9e1e7d8ba24d03f7cb0424049d68`. T5J at `ε = 2` reads Unresolved on a count change, and the candidates leave it Unresolved. M8.16.1's verdict stands as adjudicated, and a reading on record is not new evidence. What it adds is a third instance, and a reason to put T5J on MIT's list.

**What this changes in the MIT-side plan, decided:**
- The dated note states the code is off the pin, with the sentence on what does not carry, and says what the changes were chosen knowing: all of it, including M8.17's readings at the twelve, which the preview read. It names all three changed verdicts.
- Re-reading the controls is a regression test, not evidence. Before the twelve, the changed code reads fresh points that no record holds, at amplitudes nobody has solved, next to the failures, with the pass marks stated in the note first. That replaces "about an hour, no new solves": a few hours side by side, my estimate, from this run's control times (21 to 92 minutes for each control's `N = 40` path of four points).
- The folder carries a manifest pin before it runs, so a later request has a frozen spec to reproduce, and the sequel separates what rests on the changed code.
- T5J goes on MIT's list, not yet sized.
- No reply on #512: the dated note answers the four points.

**Next,** on Blake's word: the close-out, drafted for the units. It is the census page's dated note on MIT, with S6 applied per item as ruled and S5 open, and an OpenWave pull request with the Done row and both status rows. With the rows closed under S6, S5 is what stands before the census's close.

## 36. 2026-11-01T23:24:33Z: the close-out, drafted for the units

On Blake's word ("go"), as the terms' § DEFINITION OF DONE and #692's commitments ask, after M8.17's (MIT `2d4b697`, OpenWave #677). Nothing is committed, pushed or posted.
- **MIT, the census page,** `../closeout/mit/slot-dynamics-census.md` `82931a670213bf1894f093ee4012b9578eb404290fffd46e573db9c45b5709e6`, on `origin/main` `5241a2d5`:
  - a dated note in § V, step 5, after the adjudication: T4 in `R5` located; the reading at `N = 40` ended at its control gate; S6 applied per item as the approval rules it; what a closure says; and S5 open;
  - the catalog: T1 and T5 record the run, T4's row is split by slot since the two no longer share a status, T4 in `R5` closes under S4, and T1, T4 in `R4` and T5 read "instrument-limited under S6";
  - the Status line, dated 2026-11-01.

  Beyond the terms' list, for the units: the note's last bullet, on MIT's own computation; the Inputs line, § III's opening, the two label bullets, § IV's pointer and § VIII's line.
- **MIT, the working index's census row,** `../closeout/mit/README.md` `affcd998ea48b1913301ed286c8988c6f0fbb7018bb95f21e231ae8dad946e32`.
- **This folder's `REPRODUCE.md`,** `3dde1bed19ee756c7b7d172a2ce6003eb2ecea8b33bade90cbf875ea16338272`: its run line names the adjudication, a bullet corrects the job count, and the `SHA256SUMS` line names both regenerations. `tools/build_record.py --check` still reproduces `RECORD.md`.
- **OpenWave, on `upstream/main` `7fd5d46b`:**
  - the roadmap, `c8595947611bf24f9634cd45daf0adc235a681a083bb4a491920c94f69891a3c`: the Done row, 59 words by the checker's count; both status rows; the snapshot's date; the author's notes entry;
  - the task file, `a30e0113c203a503a8a9ee42e9f5ffc23d39b2e4d9e74964b99e3abe197de853`: a dated note after the terms, which stay the exact 44,825-byte prefix;
  - the briefing, `c4c7ef515e71dadb32bcc69542ab5b4cdb91601015d2cf0c418ed293e853a45f`: an M8.18 row.

  The method note and `RECORD.md` do not change: the approval pins both. The MIT close-out commit appears as markers until it exists.
- **The checks:** `../closeout/tools/check_closeout.py` `4e692b9d6c2888d18d831efe1ef6a76f7d988583bafc3fbbdc523ded39c80f51`, its output `a1794390d601c1b5880a688850685da385739ce1412e9289492c4aeb03e9b7d7`: every check passes, OpenWave's three checkers among them, with GitHub's renderer on both MIT pages. New against M8.17's: the note's open items against `run/out/CENSUS.json`, its quotations against their sources, the catalog's cell counts, and `RECORD.md` and the method note against the approval's pins. `arms_closeout.py` `9d9c8e239ec79f478c9da078f848fc3f911b3b28241d767f99490d0c0637e727`: ten arms, each failing as it must, its output `d2fca9eb281ba24af23c6c0b69d2bdc0e273740faef66843a6129449a23c4cfd`. The sibling's commit-does-not-exist arm could not have fired through a `git rev-parse` failure after entry 42's change there, so this checker tests the commit first and fails by name. The fill's dry run, `../closeout/fill_dryrun_standin.out`, fills everything and resolves every link, and fails four checks by design, since the record's commit stands in. The metadata lint has no failure or warning on the drafts, and the folder's scan has 0 hits.
- **The packet:** `../m8_18_closeout_packet_v1.md` `f4b185a965a2b534c213574ae1497b5577466dd7a1bbbdfdff3011c24b9b7a7f` and `../m8_18_closeout_review_v1.zip` `943d9050d10e160c277af82a0b9afe551de23e066b57d2dc25564c7fac37150d`, with the pull request's text, `../closeout/pr_title_v1.txt` and `../closeout/pr_body_v1.md` `8816e14ad124981bf48b1a972c21d6cdd14b1358beab97c4700fe757f8d1f8dd`, and both commit messages.

**Next:** the units' review. Then, each on Blake's word: the MIT commit, with this log through its entry and `SHA256SUMS` regenerated last, and its push; the OpenWave branch, filled with that commit; and Blake opens the pull request.

## 37. 2026-11-01T23:25:17Z: the packet rebuilt (bench-only)

The cover pointed to log entries the zip did not hold. The zip now holds them, as `folder/DEVLOG_31_to_36.md`, the cover says so and names the heads the checker reads, and no draft changed. These replace the two hashes in entry 36: `../m8_18_closeout_packet_v1.md` `b011e87739b57d6e286b1456483a506b7f8de630d08a612cb3474b2a990556fc` and `../m8_18_closeout_review_v1.zip` `05d11dc84656c9d9e6161a9a2b861a4b71f450c9187cd44d86b193c07f79fd67`.

## 38. 2026-11-02T00:01:26Z: the units on the close-out packet; the close-out, v2

Blake relayed both units: "feedback from the units". Each finding was read at source.
- **UA:** GO on (a) to (g), with no blocking redline. It compared each cause with the published `run/out/CENSUS.json`, and asks that the bullet on MIT's own computation stay.
- **UB:** HOLD on two FIXABLEs, with all seven items GO once they are made. It reran the checker on MIT `5241a2d` and OpenWave `7fd5d46b`, with its 36 local checks and `openwave.diff` matching, reran the arms, and reproduced `t5j_tau.py` and `preview_fix.py` byte for byte.
  1. **(e), taken.** The bullet lacked the answer's first point, which the answer calls the sentence an audit needs, and its second. It now says the code is off M8.16.1's pin, so its qualification, the admission of 2026-10-15 and both adjudications do not carry, and that the dated note will say what the change was chosen knowing and what the changed code was tested on. One word differs from UB's text: "The computation's code" for "Its code", since the sentence before it ends on the condition.
  2. **The task file's note, taken as worded.** The approval's commitments table limits the standing rule to an item whose admitted remedy stopped at its gate before reading it, and T5's 128 and 132 close under S6's last sentence directly. No other draft states the rule.
- **UB's three NITs, taken:**
  1. T5 at 132 gains "a record is unresolved", which `run/out/CENSUS.json` lists first;
  2. "set it to apply once 45.25 had been read again": the note of 2026-10-30 scheduled S6;
  3. `closeout/diffs/mit.diff` in v1's zip had `REPRODUCE.md`'s hunk on the wrong base. The cause was mine: the fill's dry run, with the record's commit standing in, reads the MIT bases at that commit's parent, `4bd8bbd`, and rewrote the diffs after the review run. The checker now writes the diffs on a review run alone. They are regenerated, and that hunk holds its 3 added lines.
- **(d), UB's optional form, taken** on the census page and the working index: "Next: S5, which stays open; its pre-registration carries the coherent row's ladder".
- **Added:** the checker reads M8.16.1's `run/MANIFEST_PIN` against the note's pin, with an arm.
- **For the MIT-side note,** UB's three points and the answer's four are gathered in `../mit_side_design/NOTES_for_the_dated_note.md` `b28855bca7a3c44589d153f4c74c23e92dd14f10e816b61ad496f55786803c63`. T5J stays out of the close-out, and UB could not break the reading: only the unlinked gap at `N = 32` is INFERRED.

**v2:** `../closeout/mit/slot-dynamics-census.md` `e8a68c9766048e10df57962eca128dbde614c4e0f4bad30a1544dbcfe99076b7`, `../closeout/mit/README.md` `ebc2c758d57e235d5ec6e58c7fee08427c35039380949cce74447f3c5c077364`, `../closeout/ow/m8_18_task_details.md` `0b0b4d88ded29411f6b15643065df5216a427a6f14abacc0f56d469bdb0b1e04`; every change against v1 is `../closeout/v1_to_v2.diff`. `check_closeout.py` `15785d506f928a9597b9fc9419fadcb899763dd3c126a45d3e818f1c7683b1c2`: 39 checks pass, `../closeout/check_closeout.out` `ea25ecf580c82460618e699607ae47846f7f677f21acf8bfcbcf3ebd4d1ecc16`. `arms_closeout.py` `e4d78eec53e6df132f70c6ff1aa202a41e5e8e975d207cef5c274c8abcf5ec43`: eleven arms fail as they must, `../closeout/arms_closeout.out` `7d63dc3f9ea6ff6bc16200b912fc3974068223dac3364e12c6d313b2c3342f2c`. No new packet: UB's GO rests on these edits, so they are made and this stops.

**Next,** each on Blake's word: the MIT commit, with this log through its entry and `SHA256SUMS` regenerated last, and its push; the OpenWave branch, filled with that commit; and Blake opens the pull request.

## 39. 2026-11-02T00:05:38Z: the close-out filed, on Blake's word: the census page's notes, with this folder rebuilt from the bench

On Blake's word ("commit and push"), after UA's GO on v1 and UB's GO on its fixes (entry 38).
- **The heads.** MIT `main` is still the record's commit, `5241a2d5`. OpenWave's upstream `main` is still #693's merge, `7fd5d46b`, with no pull request open.
- **The commit** changes five files:
  - the census page and the working index, as drafted in v2;
  - this folder, rebuilt from the bench: `REPRODUCE.md` names the adjudication, the job count's correction and this regeneration of `SHA256SUMS`, and this log runs through this entry. Entries 31 to 38 were written on the bench after the record's commit, and they publish here; 31 to 35 and 37 say so in their headings.
- `RECORD.md` is unchanged, as the approval pins it, and `tools/build_record.py --check` reproduces it after this entry. `SHA256SUMS` is written fresh after this entry, over the folder's files, itself excluded, by `../publish_checks.py --write`, with its five checks.

**Next:** the commit, verified from its own tree; the push; then the OpenWave branch, filled with that commit and checked against it.
