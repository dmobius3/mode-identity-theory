# M8.17 run record

The record of M8.17's registered run, the census run on the nine rows M8.16.1 qualified, from 2026-10-27T19:50:47Z to 2026-10-28T16:18:02Z. It ran under the governing terms, `run/m8_16_task_details.md` (SHA-256 `667159c3db993396…`), merged in OpenWave [#662](https://github.com/openwave-labs/openwave/pull/662) as `a4c7a270`, and the census run's code frozen at MIT `338b873` with its manifest pin, `2deed9aa564a6ccb…`. The maintainer's go is [#662's comment](https://github.com/openwave-labs/openwave/pull/662#issuecomment-6443460379), and the freeze block is OpenWave's `research/m8_17/freeze_block.md`, merged in [#673](https://github.com/openwave-labs/openwave/pull/673). Every number below is read from the run's files in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them. `run/out/CENSUS.json` holds every point's classification, its instrument and, where it is not classified, its causes; the case files hold every point's readings at every cutoff; the locator's files hold each bracket's recomputed path, bisections and guard readings. This record gives what the terms' § DEFINITION OF DONE asks: every point of the nine rows' windows with its classification, its instrument and, on this instrument, the convergence rule's reading; every point not classified, with its cause; every bracket, with its location or the condition it failed; and each row's ending. Adjudication is the maintainers'.

**The outcome.** The run completed, with no stop. Every point on the seven computed paths was accepted at all three cutoffs, the reproduction gate held at all 63 known points it compared, and both of the locator's recomputed paths reproduced. Of the 56 first-time readings, 42 are classified and 14 are not. Four rows meet an S4 completion condition: T2/R4 and T3/R5, with each change of type located, and T2/R5 and T3/R4, Elliptic throughout. Five rows end not settled by this run: T1/R4, T4/R4, T1/R5, T4/R5 and T5/R2, with 5, 6, 1, 1 and 3 items open (§ 5). The locator located T2/R4's change of type, and did not locate T4/R5's (§ 4).

**The rows:**

| Row | Slot | Outcome | Meets an S4 completion condition | Classified | Not classified | Brackets |
|---|---|---|---|---|---|---|
| T1/R4 | `R4` | Not settled by this run | no | 13 of 18 | 5 | 0 |
| T4/R4 | `R4` | Not settled by this run | no | 13 of 18 | 5 | 1 |
| T1/R5 | `R5` | Not settled by this run | no | 14 of 15 | 1 | 0 |
| T4/R5 | `R5` | Not settled by this run | no | 15 of 15 | 0 | 1 |
| T2/R4 | `R4` | Each change of type located | yes | 18 of 18 | 0 | 1 |
| T2/R5 | `R5` | Elliptic throughout | yes | 15 of 15 | 0 | 0 |
| T3/R4 | `R4` | Elliptic throughout | yes | 18 of 18 | 0 | 0 |
| T3/R5 | `R5` | Each change of type located | yes | 14 of 15 | 1, accounted for by its location | 1 |
| T5/R2 | `R2` | Not settled by this run | no | 17 of 20 | 3 | 0 |

## 1. Custody

- **The freeze.** `run/FROZEN.json` was written once, at 2026-10-27T15:20:25Z, by `run/write_guard.py`, after the go. It holds the allowlist and the order, the seven rows of `census_lib.RUN_ORDER`; each row's case with its registered path; the census values; what M8.17 inherits from M8.16.1; the terms' and the manifest's SHA-256; the go; and 34 targets, every reference file at its SHA-256 with `reference/SOURCES.json` among them. Its own SHA-256 is `run/FROZEN_PIN`, `bea8d27a537198b3…`.
- **The freeze block,** built by the pinned `run/freeze_block.py`, carries `FROZEN.json` in full. Its pull request, [#673](https://github.com/openwave-labs/openwave/pull/673), was opened at 2026-10-27T16:41:23Z and merged at 2026-10-27T18:59:56Z as `c21d2f8c`, before the run started. The maintainer's approval rebuilt the block byte for byte from MIT's git objects with its own script, and records two reading notes: the adjudication reads #662's approval note 1 from the run's own environment readings at its start and its end, and checks the published resume check against the SHA-256 the pull request names. Both are below.
- **Before the launch,** read-only, by `launch/prelaunch_checks.py` with #673's number, at the bench beside this folder: 15 checks, all clean, its output kept as `prelaunch_checks_2026-10-27.txt`. Among them: both admissions, `devtools.frozen()` and `census.frozen()`; the manifest and the freeze pin; `run/record_environment.py --check`, with no difference from `run/ENVIRONMENT.json`; no `run/out/`; no census run in progress; the resume check at its reviewed SHA-256, and passing; mains power; and #673 merged, its one file the block, equal at its head and on OpenWave `main`, with DCO passing.
- **The launch.** One launch, on the author's word, by the command `DEVLOG.md` entry 26 records, run unchanged from this folder as a background task, under `caffeinate` on its shell, on mains power:

  ```
  set -o pipefail; caffeinate -i -m -s -w $$ & { printf '%s  %s\n' 2c4762ef369f84218992e3ec30d29e78b6d07d798bc596edce41f6cfd5b9f87f ../resume_check/resume_check.py | shasum -a 256 -c - && python3 -I -B ../resume_check/resume_check.py . && python3 -I -B -u run/census.py; } 2>&1 | tee -a ../census_console.log
  ```

  It checks the resume check's bytes against `2c4762ef369f8421…`, runs the check, and only then `run/census.py`. Its console log, `run/out/census_console.log`, opens with the hash check's `OK` and the check's `PASS`, `run/out/` not yet existing, and then holds the run's transcript, `run/out/census.out`, line for line. The resume check sat outside the pinned tree, at `../resume_check/`, as the freeze block's pull request states; `launch/resume_check.py` is that file, byte for byte, published with its 22 arms, `launch/test_resume_check.py`, and their output. It refuses on eight checks: a stop in the log; the run's record in the log; a `STOP.json` under `run/out/`; a JSON file carrying a stop; a failed reproduction gate; a completed job's file missing or off its logged SHA-256; `run/out/` holding files but no `RUNLOG.json`; the log or a completed job's file that does not parse.
- **The run.** It started at 2026-10-27T19:50:47Z and wrote its record at 2026-10-28T16:18:02Z, 73635 s later, against 73635 s by its own clock, in the recorded environment: Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK as each reports them, under macOS 15.8 (24H23) on one Apple M3. Its log, `run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, equal to `run/MANIFEST_PIN`; one start, and so no resume; each completed job with its file's SHA-256, the seven rows in their registered order and then the locator's two brackets; no stop; and the record and the transcript, each with its SHA-256.
- **After the run:** every output equals the SHA-256 the log recorded; both admissions pass; the tree still equals the manifest pin; and the environment, read again, equals `run/ENVIRONMENT.json` (`environment_postrun_2026-10-28.txt`). The resume check then refuses a relaunch, since the run has completed.
- **Post-run files.** These files were made or placed after the run, and are not records from it:
  - `prelaunch_checks_2026-10-27.txt`, the checks before the launch, read just before it;
  - `environment_postrun_2026-10-28.txt`, `run/record_environment.py --check`, read after the run, with no difference;
  - `launch/`, each file byte for byte as it ran from the bench beside this folder: the resume check and its arms; `prelaunch_checks.py`; and `test_launch_wrapper.py` with its output, the launch command's form run on stubs, as `DEVLOG.md` entry 26 records it. Its first check reads the command from `FILING_PLAN.md`'s step 3, which stays on the bench, so it reruns only beside that plan;
  - `run/out/census_console.log`, the run's console output, copied byte for byte from beside this folder once the run had ended;
  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference;
  - `SHA256SUMS`, regenerated over the published folder at the record's commit, one line per file but itself. The pre-run inventory stays at MIT `338b873`.

  | File | SHA-256 |
  |---|---|
  | `run/out/T2_R4.json` | `6240d252b790a8dc403d0efd1bfa252151c6f5997c8a9c557ba4c7e615874ccc` |
  | `run/out/T3_R4.json` | `02a953d33b7844d332456e6127873cacffc6e9e86eba1c6763250ba3da6f377b` |
  | `run/out/T5_R2.json` | `fb185a91edcf7099950e4e7529d125136537769992d8bddb9cb18edf0d632bec` |
  | `run/out/T1_R4.json` | `06e51a090e310a2accf6bab21fdee693ab2806ff6115bb8a7f10b54aae96bcc9` |
  | `run/out/T4_R4.json` | `2955bc02cb2c653deb28f13bcdf53229b21541521681900661183a632823e512` |
  | `run/out/T1_R5.json` | `e8ecd65f3754e6bd047e0d6c34964d59aaa44bd05bb522a71a884118926d3678` |
  | `run/out/T4_R5.json` | `167ddab0d696d2758581a8f7063d0d74283c13bbe2500fb60c91665e1a2ce95c` |
  | `run/out/locate_T2_R4_16_22.627416998.json` | `ea1b9937ed82b9049e7faa50ea0bc0a22d92c4f08bc3e38de96fa6ed10570924` |
  | `run/out/locate_T4_R5_8_11.313708499.json` | `517aa9f62a45255ec4a76690e95069935d32265e532a7858e58d8709cf10af55` |
  | `run/out/CENSUS.json` | `d010db400a6bdef2ad64ce1bfd0e085995c49e62ba1982325ff6234f8d233aac` |
  | `run/out/census.out` | `50fac723ceaa77c778ba2a3b20011559d87ac51259b6b939f776cf699f883352` |
  | `run/out/RUNLOG.json` | `7d761506f8bfb05cee50ddc6cbf29b0a97fb20c7d9242d57c6765cff8114196a` |
  | `run/FROZEN.json` | `bea8d27a537198b3f3a840f9af2b2e4aba8c70d7982e512766c71bd1093375b6` |

  The post-run files:

  | File | SHA-256 |
  |---|---|
  | `prelaunch_checks_2026-10-27.txt` | `ba2bcef3d772cf26580714ba3a18680bfa8d341f4a8f8ef8bbbefd8af6e97db0` |
  | `environment_postrun_2026-10-28.txt` | `5e12e201d9fa970e9ccc7db1ad32778c5f50d4a6014ba45bf6e42a0be7554390` |
  | `launch/resume_check.py` | `2c4762ef369f84218992e3ec30d29e78b6d07d798bc596edce41f6cfd5b9f87f` |
  | `launch/test_resume_check.py` | `88538e8cc72ae2022e4e09b316ae9c884e1faa19550fc8b4f443ce94560e3b63` |
  | `launch/test_resume_check.out` | `d9b9c6b8e30bc979af69c0e989a1d744e1a21659c105cf053429f48f04d79de4` |
  | `launch/test_launch_wrapper.py` | `8211659cc99026efe3d640b794a6fd46ab131bd564fed96e2be343ce3025b5a9` |
  | `launch/test_launch_wrapper.out` | `00296c908d33f9a28c4866a04c30e31dc8df990ce0a10855f840702d8061fae1` |
  | `launch/prelaunch_checks.py` | `2b5061e9578f4d8df5a89ed580228cec1d1acf1c7b3f72a8116735bd774c65c3` |
  | `run/out/census_console.log` | `41f13f667bffdf05cf20327ee2430417775d1224607df5ede8fc084061761476` |
  | `tools/build_record.py` | `fcee4a2d2b8a927509e867f35479ca8d66fccc32ff8745f3e0dfedce9ecd1c30`, as it built this record |

## 2. The reproduction gate

The terms' three rules (§ THE FREEZE, THE GUARD AND THE RUN), applied when each row's `run_case` returned, to every point of its path that M8.16.1 solved: rule 1, full equality with M8.16.1's record, timings aside, at a point M8.16.1 read and reached by its own steps; rule 2, the solve and acceptance fields at a point M8.16.1 withheld; rule 3, type, indices, `V₀`'s dimension and ranks, chains, Krein counts and the rule's verdict, at T1's and T4's 0.5, 1 and 2. Every compared point passed.

| Row | Rule 1 | Rule 2 | Rule 3 | Failed | Path | s |
|---|---|---|---|---|---|---|
| T2/R4 | 12 | 16, 22.63 | none | 0 | 14 points, to 22.63 | 4650 |
| T3/R4 | 14 | 32 | none | 0 | 15 points, to 32 | 5271 |
| T5/R2 | 17 | 45.25 | none | 0 | 20 points, to 132 | 3205 |
| T1/R4 | 1 | none | 0.5, 1, 2 | 0 | 18 points, to 72 | 6043 |
| T4/R4 | 1 | none | 0.5, 1, 2 | 0 | 18 points, to 72 | 6759 |
| T1/R5 | 1 | none | 0.5, 1, 2 | 0 | 15 points, to 32 | 9912 |
| T4/R5 | 1 | none | 0.5, 1, 2 | 0 | 15 points, to 32 | 10150 |

- **T2/R4's bracket (16, 22.63):** each cutoff's path recomputed from its seed to the bracket's upper end, 14 points, every one equal to its record, field for field, before the bisection began.
- **T4/R5's bracket (8, 11.31):** each cutoff's path recomputed from its seed to the bracket's upper end, 12 points, every one equal to its record, field for field, before the bisection began.

## 3. The points, row by row

Each row's window, every point with its classification, the instrument that supplies it, this instrument's reading and M8.15's. A point is classified on this instrument when it is accepted and K1 holds at every cutoff, the convergence rule reads it converged, and branch identity holds between `N = 24` and 32; the type is the rule's, with `(n(L), n(D), K)` and `k_i⁻` from the highest cutoff. On M8.15's, a point is classified where M8.15 decided it. "Both" means each instrument classifies it, and they agree. The source is this run's computation, or, beyond this run's paths, M8.16.1's and M8.15's records. The aligned distance is branch identity's, between `N = 24` and 32.

### T1/R4, `R4`: Not settled by this run

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.20×10⁻⁸ |
| 0.354 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.40×10⁻⁸ |
| 0.5 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 4.77×10⁻⁸ |
| 0.707 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 9.46×10⁻⁸ |
| 1 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.87×10⁻⁷ |
| 1.41 | not classified | none | Unresolved | no record | this run | 3.68×10⁻⁷ |
| 2 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 7.20×10⁻⁷ |
| 2.83 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.40×10⁻⁶ |
| 4 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.67×10⁻⁶ |
| 5.66 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 5.03×10⁻⁶ |
| 8 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 9.27×10⁻⁶ |
| 11.31 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.66×10⁻⁵ |
| 16 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.87×10⁻⁵ |
| 22.63 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 4.74×10⁻⁵ |
| 32 | not classified | none | Unresolved | no record | this run | 7.43×10⁻⁵ |
| 45.25 | not classified | none | Unresolved | no record | this run | 1.10×10⁻⁴ |
| 64 | not classified | none | Unresolved | no record | this run | 1.54×10⁻⁴ |
| 72 | not classified | none | Unresolved | no record | this run | 1.71×10⁻⁴ |

**This instrument's causes,** at each point it does not classify, as the run's record states them:

- **`ε = 1.41`:** the rule reads it Unresolved: tested set at 9.47465e-16+4.02388j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 32`:** the rule reads it Unresolved: tested set at 3.01235e-15+0.342541j (+2): the set's count differs between cutoffs; tested set at 3.71208e-16+3.6807j (+1): the set's count differs between cutoffs; tested set at -7.11106e-16+3.92415j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 45.25`:** the rule reads it Unresolved: tested set at 4.94519e-16+3.56238j (+1): the set's count differs between cutoffs; tested set at 2.24587e-16+3.86997j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 64`:** the rule reads it Unresolved: tested set at 4.81427e-16+3.4127j (+1): the set's count differs between cutoffs; tested set at 4.38554e-17+3.79165j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 72`:** the rule reads it Unresolved: tested set at -9.30127e-16+3.35419j (+1): the set's count differs between cutoffs; tested set at 2.16492e-16+3.75837j (+1): the set's count differs between cutoffs. Not classified.

### T4/R4, `R4`: Not settled by this run

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 7.91×10⁻⁸ |
| 0.354 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 1.58×10⁻⁷ |
| 0.5 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 3.14×10⁻⁷ |
| 0.707 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 6.23×10⁻⁷ |
| 1 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 1.23×10⁻⁶ |
| 1.41 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 2.43×10⁻⁶ |
| 2 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 4.78×10⁻⁶ |
| 2.83 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 9.30×10⁻⁶ |
| 4 | not classified | none | Unresolved | no record | this run | 1.79×10⁻⁵ |
| 5.66 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 3.42×10⁻⁵ |
| 8 | not classified | none | Unresolved | no record | this run | 6.43×10⁻⁵ |
| 11.31 | not classified | none | Unresolved | no record | this run | 1.20×10⁻⁴ |
| 16 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 2.21×10⁻⁴ |
| 22.63 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 4.07×10⁻⁴ |
| 32 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 7.38×10⁻⁴ |
| 45.25 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 1.31×10⁻³ |
| 64 | not classified | none | Unresolved | no record | this run | 2.26×10⁻³ |
| 72 | not classified | none | Unresolved | no record | this run | 2.70×10⁻³ |

**This instrument's causes,** at each point it does not classify, as the run's record states them:

- **`ε = 4`:** the rule reads it Unresolved: tested set at -9.98233e-16+4.00991j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 8`:** the rule reads it Unresolved: tested set at 7.8458e-16+3.98968j (+1): the set's count differs between cutoffs; tested set at -1.00202e-15+3.88085j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 11.31`:** the rule reads it Unresolved: tested set at -2.54393e-15+3.97075j (+1): the set's count differs between cutoffs; tested set at -9.63062e-16+3.83191j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 64`:** the rule reads it Unresolved: tested group at 3.39649e-15+3.0127j: non-contracting above the floor. Not classified.
- **`ε = 72`:** the rule reads it Unresolved: tested group at 2.15032e-15+2.93462j: non-contracting above the floor; tested set at 1.11333e-15+3.29749j (+2): the set's count differs between cutoffs. Not classified.

### T1/R5, `R5`: Not settled by this run

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 7.17×10⁻⁹ |
| 0.354 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.43×10⁻⁸ |
| 0.5 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.84×10⁻⁸ |
| 0.707 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 5.63×10⁻⁸ |
| 1 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.11×10⁻⁷ |
| 1.41 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.19×10⁻⁷ |
| 2 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 4.27×10⁻⁷ |
| 2.83 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 8.26×10⁻⁷ |
| 4 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.58×10⁻⁶ |
| 5.66 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.95×10⁻⁶ |
| 8 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 5.40×10⁻⁶ |
| 11.31 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 9.56×10⁻⁶ |
| 16 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 1.62×10⁻⁵ |
| 22.63 | Elliptic | this instrument | converged: Elliptic; (2, 0, 2), 1 | no record | this run | 2.62×10⁻⁵ |
| 32 | not classified | none | Unresolved | no record | this run | 3.99×10⁻⁵ |

**This instrument's causes,** at each point it does not classify, as the run's record states them:

- **`ε = 32`:** the rule reads it Unresolved: tested set at 9.90708e-16+0.301797j (+1): the set's count differs between cutoffs. Not classified.

### T4/R5, `R5`: Not settled by this run

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 4.83×10⁻⁸ |
| 0.354 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 9.65×10⁻⁸ |
| 0.5 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 1.93×10⁻⁷ |
| 0.707 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 3.85×10⁻⁷ |
| 1 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 7.67×10⁻⁷ |
| 1.41 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 1.53×10⁻⁶ |
| 2 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 3.04×10⁻⁶ |
| 2.83 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 6.03×10⁻⁶ |
| 4 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 1.19×10⁻⁵ |
| 5.66 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 2.34×10⁻⁵ |
| 8 | Elliptic | this instrument | converged: Elliptic; (7, 1, 6), 3 | no record | this run | 4.59×10⁻⁵ |
| 11.31 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 8.89×10⁻⁵ |
| 16 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 1.70×10⁻⁴ |
| 22.63 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 2 | no record | this run | 3.21×10⁻⁴ |
| 32 | Hyperbolic | this instrument | converged: Hyperbolic; (6, 1, 5), 1 | no record | this run | 5.97×10⁻⁴ |

### T2/R4, `R4`: Each change of type located

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 6.02×10⁻⁸ |
| 0.354 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 1.20×10⁻⁷ |
| 0.5 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 2.40×10⁻⁷ |
| 0.707 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 4.79×10⁻⁷ |
| 1 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 9.54×10⁻⁷ |
| 1.41 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 1.90×10⁻⁶ |
| 2 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 3.76×10⁻⁶ |
| 2.83 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 7.44×10⁻⁶ |
| 4 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 1.47×10⁻⁵ |
| 5.66 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 2.87×10⁻⁵ |
| 8 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 5.55×10⁻⁵ |
| 11.31 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | this run | 1.06×10⁻⁴ |
| 16 | Elliptic | this instrument | converged: Elliptic; (3, 3, 0), 0 | undecided | this run | 1.99×10⁻⁴ |
| 22.63 | Hyperbolic | this instrument | converged: Hyperbolic; (5, 3, 2), 0 | undecided | this run | 3.62×10⁻⁴ |
| 32 | Hyperbolic | both | converged: Hyperbolic; (5, 3, 2), 0 | Hyperbolic | M8.16.1's and M8.15's records | 6.35×10⁻⁴ |
| 45.25 | Hyperbolic | both | converged: Hyperbolic; (5, 3, 2), 0 | Hyperbolic | M8.16.1's and M8.15's records | 1.06×10⁻³ |
| 64 | Hyperbolic | both | converged: Hyperbolic; (5, 3, 2), 0 | Hyperbolic | M8.16.1's and M8.15's records | 1.65×10⁻³ |
| 72 | Hyperbolic | both | converged: Hyperbolic; (5, 3, 2), 0 | Hyperbolic | M8.16.1's and M8.15's records | 1.89×10⁻³ |

### T2/R5, `R5`: Elliptic throughout

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 3.50×10⁻⁸ |
| 0.354 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 6.98×10⁻⁸ |
| 0.5 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 1.39×10⁻⁷ |
| 0.707 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 2.76×10⁻⁷ |
| 1 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 5.47×10⁻⁷ |
| 1.41 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 1.08×10⁻⁶ |
| 2 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 2.12×10⁻⁶ |
| 2.83 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 4.14×10⁻⁶ |
| 4 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 7.98×10⁻⁶ |
| 5.66 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 1.52×10⁻⁵ |
| 8 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 2.83×10⁻⁵ |
| 11.31 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 5.12×10⁻⁵ |
| 16 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 8.93×10⁻⁵ |
| 22.63 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 1.48×10⁻⁴ |
| 32 | Elliptic | both | converged: Elliptic; (3, 3, 0), 0 | Elliptic | M8.16.1's and M8.15's records | 2.32×10⁻⁴ |

### T3/R4, `R4`: Elliptic throughout

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 7.00×10⁻⁸ |
| 0.354 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 1.40×10⁻⁷ |
| 0.5 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 2.79×10⁻⁷ |
| 0.707 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 5.57×10⁻⁷ |
| 1 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 1.11×10⁻⁶ |
| 1.41 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 2.21×10⁻⁶ |
| 2 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 4.40×10⁻⁶ |
| 2.83 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 8.74×10⁻⁶ |
| 4 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 1.73×10⁻⁵ |
| 5.66 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 3.41×10⁻⁵ |
| 8 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 6.67×10⁻⁵ |
| 11.31 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 1.30×10⁻⁴ |
| 16 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 2.49×10⁻⁴ |
| 22.63 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 4.73×10⁻⁴ |
| 32 | Elliptic | this instrument | converged: Elliptic; (9, 3, 6), 3 | undecided | this run | 8.82×10⁻⁴ |
| 45.25 | Elliptic | M8.15's | Unresolved | Elliptic | M8.16.1's and M8.15's records | 1.60×10⁻³ |
| 64 | Elliptic | M8.15's | Unresolved | Elliptic | M8.16.1's and M8.15's records | 2.83×10⁻³ |
| 72 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 3.40×10⁻³ |

**This instrument's causes,** at each point it does not classify, as the run's record states them:

- **`ε = 16`:** the rule reads it Unresolved: tested set at 2.79122e-15+3.51578j (+3): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 45.25`:** the rule reads it Unresolved: tested set at -7.05549e-16+3.23787j (+5): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 64`:** the rule reads it Unresolved: tested set at -2.67583e-15+3.03461j (+5): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.

### T3/R5, `R5`: Each change of type located

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 4.93×10⁻⁸ |
| 0.354 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 9.84×10⁻⁸ |
| 0.5 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 1.96×10⁻⁷ |
| 0.707 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 3.90×10⁻⁷ |
| 1 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 7.75×10⁻⁷ |
| 1.41 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 1.53×10⁻⁶ |
| 2 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 3.02×10⁻⁶ |
| 2.83 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 5.92×10⁻⁶ |
| 4 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 1.15×10⁻⁵ |
| 5.66 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 2.20×10⁻⁵ |
| 8 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 4.14×10⁻⁵ |
| 11.31 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | M8.16.1's and M8.15's records | 7.59×10⁻⁵ |
| 16 | not classified; accounted for by M8.15.2's location | none | not computed | undecided | none |  |
| 22.63 | Hyperbolic | both | converged: Hyperbolic; (7, 3, 4), 1 | Hyperbolic | M8.16.1's and M8.15's records | 2.24×10⁻⁴ |
| 32 | Hyperbolic | both | converged: Hyperbolic; (6, 3, 3), 0 | Hyperbolic | M8.16.1's and M8.15's records | 3.51×10⁻⁴ |

**This instrument's causes,** at each point it does not classify, as the run's record states them:

- **`ε = 16`:** T3/R5 at eps = 16 is a withheld point; not computed here. It lies between M8.15.2's guard readings, 15.6356 and 16.5832, which account for it.

### T5/R2, `R2`: Not settled by this run

| `ε` | Classification | Instrument | This instrument: the rule's reading; `(n(L), n(D), K)`, `k_i⁻` | M8.15 | Source | Aligned distance |
|---|---|---|---|---|---|---|
| 0.25 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 2.56×10⁻⁷ |
| 0.354 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 5.11×10⁻⁷ |
| 0.5 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 1.02×10⁻⁶ |
| 0.707 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 2.03×10⁻⁶ |
| 1 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 4.03×10⁻⁶ |
| 1.41 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 8.00×10⁻⁶ |
| 2 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 1.58×10⁻⁵ |
| 2.83 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 3.11×10⁻⁵ |
| 4 | Elliptic | both | converged: Elliptic; (9, 3, 6), 3 | Elliptic | this run | 6.07×10⁻⁵ |
| 5.66 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 1.17×10⁻⁴ |
| 8 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 2.24×10⁻⁴ |
| 11.31 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 4.20×10⁻⁴ |
| 16 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 7.67×10⁻⁴ |
| 22.63 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 1.35×10⁻³ |
| 32 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 2.28×10⁻³ |
| 45.25 | not classified | none | Unresolved | undecided | this run | 3.63×10⁻³ |
| 64 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 5.45×10⁻³ |
| 90.51 | Elliptic | M8.15's | Unresolved | Elliptic | this run | 7.69×10⁻³ |
| 128 | not classified | none | branch identity fails: aligned distance 0.0104, the records agree; Unresolved | undecided | this run | 1.04×10⁻² |
| 132 | not classified | none | K1 fails at N = 16; branch identity fails: aligned distance 0.0106, the records agree; Unresolved | undecided | this run | 1.06×10⁻² |

**This instrument's causes,** at each point it does not classify, as the run's record states them:

- **`ε = 5.66`:** the rule reads it Unresolved: partner set at 3.20878e-15+5.77121j (+1): the set's count differs between cutoffs; partner set at 3.20878e-15+5.77121j (+1): the set's count differs between cutoffs; partner set at 3.20878e-15+5.77121j (+1): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 8`:** the rule reads it Unresolved: partner set at 2.66246e-15+5.67184j (+1): the set's count differs between cutoffs; partner set at 2.66246e-15+5.67184j (+1): the set's count differs between cutoffs; partner set at 2.66246e-15+5.67184j (+1): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 11.31`:** the rule reads it Unresolved: partner set at -2.07388e-15+5.53882j (+1): the set's count differs between cutoffs; partner set at -2.07388e-15+5.53882j (+1): the set's count differs between cutoffs; partner set at -2.07388e-15+5.53882j (+1): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 16`:** the rule reads it Unresolved: partner set at -1.84007e-15+5.36336j (+1): non-contracting above the floor; partner set at -1.84007e-15+5.36336j (+1): non-contracting above the floor; partner set at -1.84007e-15+5.36336j (+1): non-contracting above the floor. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 22.63`:** the rule reads it Unresolved: partner set at 1.67077e-16+5.13822j (+1): non-contracting above the floor; partner set at 1.67077e-16+5.13822j (+1): non-contracting above the floor; partner set at 1.67077e-16+5.13822j (+1): non-contracting above the floor. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 32`:** the rule reads it Unresolved: tested set at 8.02228e-16+0.436471j (+1): the set's count differs between cutoffs; partner set at 2.26776e-15+4.85989j (+1): non-contracting above the floor; partner set at 2.26776e-15+4.85989j (+1): non-contracting above the floor; partner set at 2.26776e-15+4.85989j (+1): non-contracting above the floor. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 45.25`:** the rule reads it Unresolved: tested set at -6.21607e-16+0.592227j (+2): the set's count differs between cutoffs; partner set at -3.45032e-16+4.53231j (+1): the set's count differs between cutoffs; partner set at -3.45032e-16+4.53231j (+1): the set's count differs between cutoffs; partner set at -3.45032e-16+4.53231j (+1): the set's count differs between cutoffs. Not classified.
- **`ε = 64`:** the rule reads it Unresolved: tested set at -2.20149e-15+0.606222j (+2): the set's count differs between cutoffs; tested group at -2.15883e-15+0.481689j: non-contracting above the floor; tested group at 1.05424e-15+0.39386j: non-contracting above the floor. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 90.51`:** the rule reads it Unresolved: structure: the type, indices, V0 or Krein counts differ along the ladder; tested set at -1.03234e-14+0.527107j (+2): the set's count differs between cutoffs; tested group at 2.8818e-15+0.263559j: non-contracting above the floor; partner set at 1.34931e-15+3.80019j (+1): the set's count differs between cutoffs; partner set at 1.34931e-15+3.80019j (+1): the set's count differs between cutoffs; partner set at 1.34931e-15+3.80019j (+1): the set's count differs between cutoffs. Classified Elliptic by M8.15's adjudicated reading.
- **`ε = 128`:** the rule reads it Unresolved: tested group at 0.0964772+0.154937j: U 8.03e-02 above a tenth of its distance to the imaginary axis, 9.65e-02; partner set at -6.33775e-16+3.45647j (+1): the set's count differs between cutoffs; branch identity fails: aligned distance 0.0104, the records agree. Not classified.
- **`ε = 132`:** K1 fails at N = 16; the rule reads it Unresolved: structure: a record is unresolved; structure: the type, indices, V0 or Krein counts differ along the ladder; tested group at 0.160267+0.156776j: U 5.03e-02 above a tenth of its distance to the imaginary axis, 1.60e-01; partner set at 1.00578e-15+3.46832j (+1): non-contracting above the floor; branch identity fails: aligned distance 0.0106, the records agree. Not classified.

## 4. The brackets

A type bracket is two consecutive registered grid points of a row, both classified, whose types differ; an index bracket is one whose ends' `n(L)` is resolved at `N = 24` and 32 and different between them at both. A change across an unclassified grid point has no type bracket and is not located. The locator ran on each index bracket (§ LOCATING A CHANGE OF TYPE).

- **T4/R4, (2.83, 5.66),** Elliptic to Hyperbolic, across the unclassified grid point 4: no type bracket, and not located.
- **T4/R5, (8, 11.31),** Elliptic to Hyperbolic: an index bracket, `n(L)` 7 to 6 at both `N = 24` and 32; the signed change `Δn(L)` is −1 at `N = 24`, −1 at 32, and −1 at 16, the diagnostic. **Not located:** the bisections at `N = 24` and 32 each made an unsuccessful stop, K1 failing.
  - `N = 16`: 10 midpoints, the interval [8.851079, 8.854315], 3.7×10⁻⁴ of its lower end, complete. It is reported, and does not decide.
  - `N = 24`: 10 midpoints, the interval [8.718402, 8.724874], 7.4×10⁻⁴ of its lower end, not complete. It stopped at the midpoint `ε = 8.721638`, where K1 fails on both of its solutions, from the lower end and from the upper end, as the run's record states it: "the zero cluster is not separated: an eigenvalue lies in (margin/3, 3 margin)", with `outside_min` 3.69×10⁻⁶ and 3.70×10⁻⁶ against `margin` 2.03×10⁻⁶; and "V0 does not match its expectation", with a symmetry leak of 9.4×10⁻⁶ and 8.2×10⁻⁶. At the midpoint before, `ε = 8.718402`, K1 held, with `outside_min` 2.48×10⁻⁵.
  - `N = 32`: 10 midpoints, the interval [8.718402, 8.724874], 7.4×10⁻⁴ of its lower end, not complete. It stopped at the midpoint `ε = 8.721638`, where K1 fails on both of its solutions, from the lower end and from the upper end, as the run's record states it: "the zero cluster is not separated: an eigenvalue lies in (margin/3, 3 margin)", with `outside_min` 6.12×10⁻⁶ on both solutions against `margin` 2.72×10⁻⁶. `V₀` matches there. At the midpoint before, `ε = 8.718402`, K1 held, with `outside_min` 2.53×10⁻⁵.
- **T2/R4, (16, 22.63),** Elliptic to Hyperbolic: an index bracket, `n(L)` 3 to 5 at both `N = 24` and 32; the signed change `Δn(L)` is +2 at `N = 24`, +2 at 32, and +2 at 16, the diagnostic. **Located:** a change of type located between the guard readings, with `n(L)` changing by +2 inside the interval at `N = 24` and 32.
  - `N = 16`: 10 midpoints, the interval [16.194163, 16.200635], 4.0×10⁻⁴ of its lower end, complete. It is reported, and does not decide.
  - `N = 24`: 10 midpoints, the interval [16.271828, 16.278300], 4.0×10⁻⁴ of its lower end, complete.
  - `N = 32`: 10 midpoints, the interval [16.271828, 16.278300], 4.0×10⁻⁴ of its lower end, complete.
  - The union at `N = 24` and 32: [16.271828, 16.278300], 4.0×10⁻⁴ of its lower end, narrower than `w = 10⁻³`.
  - The lower guard, `δ = 0.01`, at `ε = 16.109109`, solved from the bracket's lower end: Elliptic; (3, 3, 0), 0, classified on this instrument.
  - The upper guard, `δ = 0.01`, at `ε = 16.441083`, solved from the bracket's upper end: Hyperbolic; (5, 3, 2), 0, classified on this instrument.
- **T3/R5, (11.31, 22.63),** Elliptic to Hyperbolic, across the grid point 16: accounted for by M8.15.2's location (#632), level 3, between its guard readings, Elliptic at 15.6356 and Hyperbolic at 16.5832. The locator does not rerun it.

## 5. The row outcomes

Each row's run outcome under § THE ROW OUTCOMES, and, separately, whether it meets an S4 completion condition. A row not settled by this run is not declared closed under S6 here: S6's condition is for the census page to establish, after the adjudication. Under the ruling of 2026-10-20, a point this run does not classify is not offered to this instrument again without a ruling on #512.

| Row | Outcome | Meets an S4 completion condition | Open |
|---|---|---|---|
| T1/R4 | Not settled by this run | no | 1.41, 32, 45.25, 64, 72 |
| T4/R4 | Not settled by this run | no | 4, 8, 11.31, 64, 72, (2.83, 5.66) |
| T1/R5 | Not settled by this run | no | 32 |
| T4/R5 | Not settled by this run | no | (8, 11.31) |
| T2/R4 | Each change of type located | yes | none |
| T2/R5 | Elliptic throughout | yes | none |
| T3/R4 | Elliptic throughout | yes | none |
| T3/R5 | Each change of type located | yes | none |
| T5/R2 | Not settled by this run | no | 45.25, 128, 132 |

- **T1/R4:** five points not classified, at `ε` = 1.41, 32, 45.25, 64, 72. Each point's cause is in § 3. No type is claimed there.
- **T4/R4:** five points not classified, at `ε` = 4, 8, 11.31, 64, 72; and its change of type in (2.83, 5.66) not located, across the unclassified grid point 4, with no type bracket. Each point's cause is in § 3, and the bracket's in § 4. No type is claimed there.
- **T1/R5:** one point not classified, at `ε` = 32. Each point's cause is in § 3. No type is claimed there.
- **T4/R5:** every point classified; its change of type in (8, 11.31) not located, its bisections at `N = 24` and 32 stopped by K1. The bracket's cause is in § 4. No type is claimed there.
- **T5/R2:** three points not classified, at `ε` = 45.25, 128, 132. Each point's cause is in § 3. No type is claimed there.

## 6. What is new

The new evidence the terms name (§ Known outcomes, and what is new): the points beyond T1's and T4's samples, the four points M8.16.1 solved without a linear record, T5/R2 at 128 and 132, and the locator's points.

| Row | First-time readings | Classified | Not classified |
|---|---|---|---|
| T1/R4 | 14 | 9 | 1.41, 32, 45.25, 64, 72 |
| T4/R4 | 14 | 9 | 4, 8, 11.31, 64, 72 |
| T1/R5 | 11 | 10 | 32 |
| T4/R5 | 11 | 11 | none |
| T2/R4 | 2 | 2 | none |
| T3/R4 | 1 | 1 | none |
| T5/R2 | 3 | 0 | 45.25, 128, 132 |
| all | 56 | 42 | 14 |

- **The four points M8.16.1 withheld,** their spectral records computed here for the first time: T2/R4 at 16, Elliptic; (3, 3, 0), 0; T2/R4 at 22.63, Hyperbolic; (5, 3, 2), 0; T3/R4 at 32, Elliptic; (9, 3, 6), 3; T5/R2 at 45.25, not classified.
- **The locator's points:** on T2/R4's bracket, 30 midpoints across the three cutoffs, each solved from both ends, and 6 guard solves; on T4/R5's bracket, 30 midpoints across the three cutoffs, each solved from both ends, and no guard solves.

## 7. Deviations

- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above, once, with no resume and no stop.

## 8. Corrections

- **None.** The two reading notes in #673's approval need no change to the run; § 1 gives the readings they name.

## 9. Follow-ups, outside M8.17

- **The catalog.** After the adjudication, the census page's dated note gives each row's ending and catalog status, any S6 question this record raises, and S5's obligation as open (the terms, § DEFINITION OF DONE).
- **The S6 questions this record raises,** for the census page: the points § 5 leaves open, each with its cause in § 3; T4/R4's change of type across its unclassified point; and T4/R5's bracket, where K1 stopped the bisections at `N = 24` and 32. Whether any of them is instrument-limited is the census page's to establish, not this record's.
- **S5.** The persistence tests for the Elliptic stretches this run classifies on T1 and T4 stay open, under a pre-registration of their own (the terms, § What this task is not).
- **The location's identification.** T2/R4's location is an `n(L)` interval with two guard readings, not a crossing point; its identification with the genuine index crossing is not established (the terms, § STATED LIMITS: WHAT IS ADDED).

## 10. Reproduction

`REPRODUCE.md` gives every command. For the run, from a copy of this folder:
- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and `python3 -I -B run/record_environment.py --check`;
- **the registered run:** the launch command above, from a copy without `run/out/`, beside a copy of `launch/` at `../resume_check/`. In a copy that keeps this `run/out/`, the resume check refuses, since the run has completed;
- `python3 -I -B tools/build_record.py --check`, which rebuilds this record from the files, recomputes every row's record with `census_lib.assemble`, and reports any difference.

Bitwise agreement on another machine is not claimed: the reproduction rules compare bit for bit on the recorded environment, which the readings before and after the run equal.
