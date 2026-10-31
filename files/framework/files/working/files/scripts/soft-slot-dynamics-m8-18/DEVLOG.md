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
