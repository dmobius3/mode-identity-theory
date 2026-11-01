# M8.18 run record

The record of M8.18's registered run, the census's two remedies, from 2026-10-31T21:51:23Z to 2026-11-01T13:17:32Z. It ran under the governing terms, `run/m8_16_task_details.md` (SHA-256 `924e7ee363a756a8…`), merged in OpenWave [#687](https://github.com/openwave-labs/openwave/pull/687) as `a81d50c9`, and the code frozen at MIT `4bd8bbd` with its manifest pin, `6d244f4af56b71d6…`. The maintainer's go is [#687's comment](https://github.com/openwave-labs/openwave/pull/687#issuecomment-6548866246), and the freeze block is OpenWave's `research/m8_18/freeze_block.md`, merged in [#688](https://github.com/openwave-labs/openwave/pull/688). Every number below is read from the run's files in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them, except § 4, which also reads a diagnostic made after the run. `run/out/ARM_B.json` holds the bracket's recomputed path, bisections and guard readings; `run/out/GATE.json` holds the kernel and the control gate; the case files hold each control's readings at each cutoff; `run/out/CENSUS.json` holds Arm B's outcome, the gate and every row. This record gives what the terms' § DEFINITION OF DONE asks: the kernel check and each control's reading on the ladder; each of the twelve with its cause; every bracket, with its location or the condition it failed; each of the five rows' standing; and each stop. Adjudication is the maintainers'.

**The outcome.** The run completed in one launch, with no stop and no job left unfinished. **Arm B located T4/R5's change of type:** with the moved midpoint at 8.720990, `N = 24` and 32 both complete on [8.720990, 8.724874], `n(L)` changing by −1, between the guard readings, Elliptic at 8.633781 and Hyperbolic at 9.161117. T4/R5's row now ends Each change of type located. **Arm A ended at the control gate.** The kernel at `N = 40` passed on all seven controls, and 22 of the 24 control points read converged, but P5 and C3R/R4 at `ε = 0.25` read Unresolved. So none of Arm A's targets was solved or read, at any cutoff, and the twelve stay unclassified, each keeping M8.17's cause. T1/R4, T4/R4, T1/R5 and T5/R2 end not settled by this run, with 5, 6, 1 and 3 items open.

**The rows:**

| Row | Slot | Outcome | Meets an S4 completion condition | Classified | Not classified | Of those, the twelve |
|---|---|---|---|---|---|---|
| T1/R4 | `R4` | Not settled by this run | no | 13 of 18 | 5 | 5 |
| T4/R4 | `R4` | Not settled by this run | no | 13 of 18 | 5 | 5 |
| T1/R5 | `R5` | Not settled by this run | no | 14 of 15 | 1 | 1 |
| T4/R5 | `R5` | Each change of type located | yes | 15 of 15 | 0 | 0 |
| T5/R2 | `R2` | Not settled by this run | no | 17 of 20 | 3 | 1 |

## 1. Custody

- **The freeze.** `run/FROZEN.json` was written once, at 2026-10-31T21:13:28Z, by `run/write_guard.py`, after the go. It holds the allowlist and the order, the twelve cases of `census_lib.RUN_ORDER`; each case with its registered path; the census values; what M8.18 inherits from M8.16.1; the terms' and the manifest's SHA-256; the go; and 22 targets, every reference file at its SHA-256 with `reference/SOURCES.json` among them. Its own SHA-256 is `run/FROZEN_PIN`, `b5902494f927ec5d…`.
- **The freeze block,** built by the pinned `run/freeze_block.py`, carries `FROZEN.json` in full. Its pull request, [#688](https://github.com/openwave-labs/openwave/pull/688), was opened at 2026-10-31T21:17:17Z, before the run started, and merged at 2026-10-31T22:01:22Z as `bdc8fae8`, after it started, as its body says it may. The maintainer's approval rebuilt the block byte for byte from MIT's git objects with its own script, and records that the adjudication reads `resume_check.py` in full and reads the run's log against the go, the written time and the pull request's opening. All three are below.
- **Before the launch,** read-only, by `launch/prelaunch_checks.py` with #688's number, at the bench beside this folder: 17 checks, all clean, its output kept as `prelaunch_checks_2026-10-31.txt`. Among them: both admissions, `devtools.frozen()` and `census.frozen()`; the manifest and the freeze pin; `run/record_environment.py --check`, with no difference from `run/ENVIRONMENT.json`; no `run/out/`, so no solve had run at `N = 40`; no census run in progress; no file newer than the freeze pin but `DEVLOG.md`; the resume check at its reviewed SHA-256, and passing; mains power; and #688 open, its one file the block, equal at its head, with DCO passing.
- **The launch.** One launch, on the author's word, by the command `DEVLOG.md` entry 21 records, run unchanged from this folder as a background task, under `caffeinate` on its shell, on mains power:

  ```
  set -o pipefail; caffeinate -i -m -s -w $$ & { printf '%s  %s\n' 9405929a8518f5f5df68b0206c71d64fce90d4ea4921b01cebd4f1f4caae0971 ../resume_check/resume_check.py | shasum -a 256 -c - && python3 -I -B ../resume_check/resume_check.py . && python3 -I -B run/record_environment.py --check | tail -1 && python3 -I -B -u run/census.py; } 2>&1 | tee -a ../census_console.log
  ```

  It checks the resume check's bytes against `9405929a8518f5f5…`, runs the check, runs `--check`, and only then `run/census.py`. Its console log, `run/out/census_console.log`, opens with the hash check's `OK`, the check's `PASS` with `run/out/` not yet existing, and `differences: none`, and then holds the run's transcript, `run/out/census.out`, line for line. The resume check sat outside the pinned tree, at `../resume_check/`, as the freeze block's pull request states; `launch/resume_check.py` is that file, byte for byte, published with its 21 arms, `launch/test_resume_check.py`, and their output. It refuses on seven checks: a stop in the log; the run's record in the log; a `STOP.json` under `run/out/`; a JSON file carrying a stop; a completed job's file missing or off its logged SHA-256; `run/out/` holding files but no `RUNLOG.json`; the log or a completed job's file that does not parse.
- **The run.** It started at 2026-10-31T21:51:23Z and wrote its record at 2026-11-01T13:17:32Z, 55569 s later, against 55569 s by its own clock, after the go, the freeze's written time and #688's opening, in the recorded environment: Python 3.13.13, NumPy 2.5.0 and SciPy 1.18.0, on Accelerate's BLAS and LAPACK as each reports them, under macOS 15.8.2 (24H232) on one Apple M3. Its log, `run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, equal to `run/MANIFEST_PIN`; one start, and so no resume; each of 57 jobs, each started once and completed, with its files' SHA-256, its time and the process's peak resident size, at most 3,702,833,152 bytes; no stop and no job ended; and the record and the transcript, each with its SHA-256.
- **After the run:** every output equals the SHA-256 the log recorded; both admissions pass; the tree still equals the manifest pin; and the environment, read again, equals `run/ENVIRONMENT.json` (`environment_postrun_2026-11-01.txt`). The resume check then refuses a relaunch, since the run has completed.
- **Post-run files.** These files were made or placed after the run, and are not records from it:
  - `prelaunch_checks_2026-10-31.txt`, the checks before the launch, read just before it;
  - `environment_postrun_2026-11-01.txt`, `run/record_environment.py --check`, read after the run, with no difference;
  - `launch/`, each file byte for byte as it ran from the bench beside this folder: the resume check and its arms; `prelaunch_checks.py`; and `test_launch_wrapper.py` with its output, the launch command's form run on stubs;
  - `run/out/census_console.log`, the run's console output, copied byte for byte from beside this folder once the run had ended;
  - `dev/runs/019_gate_cause/`, the diagnostic § 4 reads, made after the run on a copy of this folder;
  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference;
  - `SHA256SUMS`, regenerated over the published folder at the record's commit, one line per file but itself. The pre-run inventory stays at MIT `4bd8bbd`.

  | File | SHA-256 |
  |---|---|
  | `run/out/ARM_B.json` | `7ea461b2ec8624189c1517296b716f55d4a21bb7ff4a1f5e6bfef0f20e6b8d92` |
  | `run/out/arm_b_solutions.npz` | `9eea9ab8e0028beed22477270ac8f11576739cd219461f71ae6746e5ee8c1042` |
  | `run/out/C2a_N24.npz` | `76fd3114142c9079c071b281581149d7545621056f99935a69bc3b1b05a74920` |
  | `run/out/C2a_N24.json` | `b048f59fc9d6eaf60c2211db8a7af9bf787b89443abacbb2816dff3e03169ff6` |
  | `run/out/C2a_N24_read.json` | `ba8b33798cd9d4cd6d22b9cfbbc05fd5ea97a333c9b532026a625e5f6a861760` |
  | `run/out/C2a_N32.npz` | `59f1382d9f4b5f1a2213cb7ffa6a35b283ec75226c4e9dce41d3dd96174ed4c2` |
  | `run/out/C2a_N32.json` | `8673daac65c720f8f15cc176de92b8536139f072f7dad053866f13b50e48821e` |
  | `run/out/C2a_N32_read.json` | `94ad3d1e8f6d07e15e982623f35235d4672cf1877a75ce7d44d200032cd83a80` |
  | `run/out/C2a_identity_24_32.json` | `ab107e3f41ca38572cc74ee969bc0e1d88a6e635a6e416391be0cc643b594d20` |
  | `run/out/C2b_N24.npz` | `54e5cdafe82d4bcfedc16cd4681691812c0c3baf74eaea11ae52dcd722c23f99` |
  | `run/out/C2b_N24.json` | `c50945430bbdeafd82470873cb0f979747719730f4f666a803ca43a225875dbf` |
  | `run/out/C2b_N24_read.json` | `17e9739c42e321acd8ca75229123115bc835b884f640c452b6f15c160d1f4b4d` |
  | `run/out/C2b_N32.npz` | `adf80ba5aec34e68998b4344605405d0ca0c25023592addbf754f5434f28d22e` |
  | `run/out/C2b_N32.json` | `2f060828c042626ec13418c649135d5386c2082f60d77c0ef054bdf457f717a5` |
  | `run/out/C2b_N32_read.json` | `4dc40a74ac3de7d613bfc02a0b0f12d062ad68be0e946c759a7e94e92e451c7a` |
  | `run/out/C2b_identity_24_32.json` | `eb9086aa0ffd4290a4e6e127dd0a95cbdd293e80b3db9b9e555d51b69872d994` |
  | `run/out/C3_N24.npz` | `0c0ae80f9ae091a387036c621426cea6fd63fc9191090e2c6a80fd66e84575a0` |
  | `run/out/C3_N24.json` | `0c3af20e71215d39334d396993cb0b44fe19c7c4eb3a481046e1d6928381b20c` |
  | `run/out/C3_N24_read.json` | `c6d49ce5a3215e25d5374816c10bc8ca20081dd3a9c526232357e3f4cf084177` |
  | `run/out/C3_N32.npz` | `b3b877438930fe5969bc36b374752b4210b5a2e0f56b81fd895f581c12594003` |
  | `run/out/C3_N32.json` | `2db0521c8864b116dda2cddbf7676cbae08d34ea9b05ac01a759d605d9ece371` |
  | `run/out/C3_N32_read.json` | `d36c5378faffca2dd24f96aa8c446cb1a8569dd5cd2d986435fbcf74020c1536` |
  | `run/out/C3_identity_24_32.json` | `3812f06848540dda6a3cc80a4980a400f6a7db34f368b268d15b9b74a6400b1b` |
  | `run/out/C2a_R5_N24.npz` | `ab2c281be33061a01ae88c2869e4a3eeace803793d1b993a07c9e5505b1c33bf` |
  | `run/out/C2a_R5_N24.json` | `b85a41f29c5a03c48e24bc4f9655fcbf588f996fa9fbc0f71f04223e39051b49` |
  | `run/out/C2a_R5_N24_read.json` | `cfe111d8f4804bc6b69cf1c4453a6c8254f8a96885f9f99a6b911e50edefd919` |
  | `run/out/C2a_R5_N32.npz` | `c57bf255595f3d4fbac0bb8ec312ae426a37230e2164cab3371d623a7dcf65c8` |
  | `run/out/C2a_R5_N32.json` | `bee2b39502ab2651a112d988688ea01ec62a487fe385ecf2d5c66a584794177b` |
  | `run/out/C2a_R5_N32_read.json` | `c04080a7332c0da8c068e5fec31b94b61e7c7568b2ce17f0c06f6629ab5ebbbd` |
  | `run/out/C2a_R5_identity_24_32.json` | `c17cf7f23c4b4f1289f231657ba16601f937f452e3fb0deca04b0a681dc75f3b` |
  | `run/out/P5_N24.npz` | `156deaadfc6c2579322c5678341b76b427a5fc40813a9c841e02341a0617a1cc` |
  | `run/out/P5_N24.json` | `4567ef0905f0c99b6f98a02fdb1787e8a483672e090f02d3087a5968d6b9c4a0` |
  | `run/out/P5_N24_read.json` | `3127feac54f2fb59f1fa39c26534430ca9a121f240410218c8d9fb624ddb7ef2` |
  | `run/out/P5_N32.npz` | `a2034530714eb8a83c91d51cccf33792549abf735ebd7a653ba032fcebf292bd` |
  | `run/out/P5_N32.json` | `a57446bb598b4ef6871f9c73c93d84bc0d09836c98528f30e8b70a75dfc70a23` |
  | `run/out/P5_N32_read.json` | `dd48757ed276ecb24909338785f7260a4dd9f6a40a47f3e2f021100e9cb40d56` |
  | `run/out/P5_identity_24_32.json` | `1c2521fa8e3c5d6ae96c0a1d5e0c08b2263058d97506d0dd2458a0e9dfaf6ec3` |
  | `run/out/C3R_R4_N24.npz` | `99e6349df1de74108c7acd25884c5ef55931711b3015e4e298dfb07423267891` |
  | `run/out/C3R_R4_N24.json` | `24ad0d87de8f6cd50edd8df412d987d7e83767af8bf6221f120720b6de3e1bb7` |
  | `run/out/C3R_R4_N24_read.json` | `90cf07e9fa599581b4cc8744e90916f2907f14c8a9657f78f15cfca5de9f6e3a` |
  | `run/out/C3R_R4_N32.npz` | `e3a089fdd25f66aa3178c219ec731cdfa4457037a966ef8cddc6cea25cd097c4` |
  | `run/out/C3R_R4_N32.json` | `7166b89e0068450d9790de0ec8f988e5f50d7c6538f9918ddf6b878bb70e1119` |
  | `run/out/C3R_R4_N32_read.json` | `abfbcbd7dcda3b1c7361edd4edd1617f78b0a27e5b3b589cf10b4fb76f3d401c` |
  | `run/out/C3R_R4_identity_24_32.json` | `fb8fd13ede86a029dc662e82427e0b570bafe420f8e3ea9f7eafb4c838db82c9` |
  | `run/out/C1.json` | `556bb88ae71f3dbe14b63d6313c69120be14a5d4eef2136008e6441983cd3cd6` |
  | `run/out/C2a_N40.npz` | `a96b460a584389e0f85e3e14375ee5a44ab1259d3181fac4cb3d09cd1e9edd5d` |
  | `run/out/C2a_N40.json` | `82b3979e4aa966f9647d374f307a1b54f18736054ec53d020342c65984d62849` |
  | `run/out/C2a_N40_read.json` | `3c879da4257a64b45b9ff093b026506f42c843a1159290521b819d7a86338a6c` |
  | `run/out/C2a_identity_32_40.json` | `ab814a930c8570ce2e20e8952230a3ce00d78c588e38eadd0281b5e28dc78d65` |
  | `run/out/C2b_N40.npz` | `6c1991af8f85f9bd9c1b7ca186369a755b04c049ac651af2a0fdb1b1198c8065` |
  | `run/out/C2b_N40.json` | `5800dcd343875f1717faf8df89710d2a82d1fb6ef4dcf49a33f522f7c29dc453` |
  | `run/out/C2b_N40_read.json` | `d7416c7109fc808835ecefef7ab77b7c32b779ec1de672190d8c03b3c31ddf8f` |
  | `run/out/C2b_identity_32_40.json` | `3ee845b7ca1c112f69e58b4d71e2619925f678e4afa001a8299042bf6735d5f2` |
  | `run/out/C3_N40.npz` | `43cc2b64d54826ac0b07329615623e8e8b3ae5a90294dacf43127730bbab6927` |
  | `run/out/C3_N40.json` | `f8145d25d74ec97875ce9ce846357f6193d2a75fd92b18ae4fb009ca7940a60e` |
  | `run/out/C3_N40_read.json` | `f7fdb40cadb81249f20d339b41fe8646ff63b19061935d45ba26cfde075f9668` |
  | `run/out/C3_identity_32_40.json` | `e974af06613560ae5302107f7dddb46401c4a4d73750365dfaa1c38f2087db74` |
  | `run/out/C2a_R5_N40.npz` | `10b748592ccc69c8ab9e06505a9cf986a81e5ee76172f4844787e1e7558d5155` |
  | `run/out/C2a_R5_N40.json` | `837568ea15560bc2521128c755fcee0b9d240c47e54b20dc11ea41431c5966a8` |
  | `run/out/C2a_R5_N40_read.json` | `2dfdb2255dad12a646730164693c8f2b8a3e78bc2f5ee05903fd42bf01644747` |
  | `run/out/C2a_R5_identity_32_40.json` | `95c6424449f960615d30f5aaa817ae8e4525600ca1f8bb22009d0467a871b9e4` |
  | `run/out/P5_N40.npz` | `dbb0ce96106424d41797fef4fbc552d6e4874f4069160d5d6c44f261912523c1` |
  | `run/out/P5_N40.json` | `951801777ed55f90ee1cb5d62c3dd47183dd20137194134d4278ca88c3a7e8fb` |
  | `run/out/P5_N40_read.json` | `d1b5d1823d7bccb4da47259364ee30d2acf5168b58ffebdcd90037127e422e09` |
  | `run/out/P5_identity_32_40.json` | `4972d024b9e587e440c7ca6cfe218f6825072a957d39259b9b81754fe80fa5a1` |
  | `run/out/C3R_R4_N40.npz` | `79421341caf09a51e975eb621a25e3abff5c27803ff0a33130c221806779ec0d` |
  | `run/out/C3R_R4_N40.json` | `05691eafd9d536e0f329ad79433d6a8eeb5f39b69ca536af511fdd245edab3d3` |
  | `run/out/C3R_R4_N40_read.json` | `e4ded70fef8ee3e1c34254bab5c26a5a18c2a04a20ab9f444eeece3100cc1212` |
  | `run/out/C3R_R4_identity_32_40.json` | `e2122145d76a6f9001960eed219f3427a21ac518916ed44e92d5214af058a26d` |
  | `run/out/C2a.json` | `fdb00c97e0ef0e3b54652031e14720fb45839e6392ec45b373d56ef930a80f00` |
  | `run/out/C2b.json` | `157850aae578a2ce355190454a9364757619e355790aa664a3537de45e9a08f3` |
  | `run/out/C3.json` | `f844f0d013302e05ff62061aab6d1a4fe6b77a1989495399095877353057b461` |
  | `run/out/C2a_R5.json` | `e16b5e319cbcf925eaed5b75666069c9ce70166ca2f1b8459aa4fc7fa931c4d0` |
  | `run/out/P5.json` | `456181b8b5535dad71bbc470dfeff8d23402463d3d5a9e697cb4509987d4213c` |
  | `run/out/C3R_R4.json` | `c4407f91a2bd554663e7694e6e57a7653fc101ee5809fba94e985444a6edd271` |
  | `run/out/GATE.json` | `a4f439313e70b8b9ab0766403d940c875fd8655c5536ab5deb3898f0bb21c244` |
  | `run/out/CENSUS.json` | `fbfcb28123e18735f7351fbdfbdf13d593249eac8b6b343f4a706a7f698c2947` |
  | `run/out/census.out` | `55f5327234f2c667eade2815918a72621fc96647692d02d26e4bb75ac41371dd` |
  | `run/out/RUNLOG.json` | `dca2c1b3fd0a74352cb7eab51b19524295e231b652fee7b74302e8a1f4301860` |
  | `run/FROZEN.json` | `b5902494f927ec5daee1562fdf3d64bf3f402eb2cc9cac777de7a29aaa7c32d5` |

  The post-run files:

  | File | SHA-256 |
  |---|---|
  | `prelaunch_checks_2026-10-31.txt` | `820dc69ed28b0f1d1c626475a7172afa1aead21f351580135955028e548be236` |
  | `environment_postrun_2026-11-01.txt` | `37ff13a0681f43a7454612ddc5ea580af7723af9acb9b7afb705e1003497b0b7` |
  | `launch/resume_check.py` | `9405929a8518f5f5df68b0206c71d64fce90d4ea4921b01cebd4f1f4caae0971` |
  | `launch/test_resume_check.py` | `dfad45fa8de64c84e8bc1a6ba2ce3c7b182f457537e8efe233cb6af6a29a4072` |
  | `launch/test_resume_check.out` | `ce5bb76190b7d42f12184e8e8d45705ce7715cf545f513722d1bfdd244717cb7` |
  | `launch/test_launch_wrapper.py` | `ef7a9dc99983aaeca27b1b16ae62f5f4f5196075fce130a0b7a440dd1b2d97f5` |
  | `launch/test_launch_wrapper.out` | `865b915f3df0356188b0ebf0b84846d8aed75aad23b0a248bede37fa3b52800b` |
  | `launch/prelaunch_checks.py` | `d49147d7a89d9079bd3c143d95119d31aca1910e124c8e90226679bc7c86b23c` |
  | `run/out/census_console.log` | `34547133730260cd8544c5f99c8747484b3ad561765d643a0b64e0c547eaae64` |
  | `dev/runs/019_gate_cause/diag_nd.py` | `41e028851032b79ab644e791dcfbb1207f0f0c9de5776855153ffc15e6c7378d` |
  | `dev/runs/019_gate_cause/diag_nd.out` | `b750024b8911fa470c77d9e10dd57eb7b9b89cb63a8a73bc9e4be2467073240b` |
  | `dev/runs/019_gate_cause/tau_check.py` | `c81845053e68eaed4290dac0bf4c9f1e61a3c56e00a1e25e7c0a63e79becf2bb` |
  | `dev/runs/019_gate_cause/tau_check.out` | `f9de08532cd1a3b19c4bb71c36d303548ca4b42ad75a8f207e5024e493b30061` |
  | `dev/runs/019_gate_cause/tau_band.py` | `1b04d4472aeb7bb4190ff98c3e35d8767da1339fde906212f5b87106a36a02d6` |
  | `dev/runs/019_gate_cause/tau_band.out` | `65cd5650ba4cf9f6d1932610a69963802bb714f6ce2b55ca4cc8654e5fce9ba8` |
  | `dev/runs/019_gate_cause/pair_gap.py` | `d37fc6827dd25b8d100e566ee89a4c5ee035fc631d13cc1e8c0e3b323a474133` |
  | `dev/runs/019_gate_cause/pair_gap.out` | `7bd6bcb9c1fb0766525504de0f7f1420f7bb61262ae6b4deb2fbe531413dbde4` |
  | `tools/build_record.py` | `41adab6241fbbf3ff0451c4ba458daf1be9ac9141b89d352ab7c58c78a30f392`, as it built this record |

## 2. Arm B: the revised locator on T4/R5

Arm B ran first, and its record was written 19217 s after the start, before any solve at `N = 40`.

- **The bracket** is T4/R5's (8, 11.31): Elliptic, (7, 1, 6), 3, and Hyperbolic, (6, 1, 5), 2, at every cutoff, an index bracket. The signed change `Δn(L)` is −1 at `N = 24`, −1 at 32, and −1 at 16, which is reported and does not decide.
- **The path.** Each cutoff's path was recomputed from its seed to the bracket's upper end, 12 points, every one equal to its record in M8.17's outputs, timings aside.
- **M8.17's midpoints.** Each of them, at each cutoff, equals its stored record, timings aside. The run compares them as it goes, and a difference stops it; it did not stop.
- **The bisections:**
  - `N = 16`: 10 midpoints, the interval [8.851079, 8.854315], 3.7×10⁻⁴ of its lower end, complete. It is reported, and does not decide.
  - `N = 24`: 11 midpoints, the interval [8.720990, 8.724874], 4.5×10⁻⁴ of its lower end, complete.
  - `N = 32`: 11 midpoints, the interval [8.720990, 8.724874], 4.5×10⁻⁴ of its lower end, complete.
- **The moved midpoint.** At each deciding cutoff, K1 refused M8.17's last midpoint on both of its solutions, and that midpoint stays in the record and decides nothing. One move, to the point 0.4 of the current interval above its lower end, as the terms fix it. The terms' interpolation (INFERRED) put the nearest eigenvalue there at about 1.16×10⁻⁵ and 1.26×10⁻⁵, and the run reads:
  - `N = 24`: K1 fails at `ε = 8.721638`: "the zero cluster is not separated: an eigenvalue lies in (margin/3, 3 margin)", with `outside_min` 3.69×10⁻⁶ and 3.70×10⁻⁶ against `margin` 2.03×10⁻⁶; and "V0 does not match its expectation", with a symmetry leak of 9.4×10⁻⁶ and 8.2×10⁻⁶. At the moved point, `ε = 8.720990`, K1 holds on both solutions, with `outside_min` 1.16×10⁻⁵ against `margin` 2.03×10⁻⁶; `n(L)` reads 7 on both, and the two solutions lie 1.12×10⁻⁸ apart. The midpoint before the refused one, `ε = 8.718402`, held K1 with `outside_min` 2.48×10⁻⁵.
  - `N = 32`: K1 fails at `ε = 8.721638`: "the zero cluster is not separated: an eigenvalue lies in (margin/3, 3 margin)", with `outside_min` 6.12×10⁻⁶ on both solutions against `margin` 2.72×10⁻⁶. `V₀` matches there. At the moved point, `ε = 8.720990`, K1 holds on both solutions, with `outside_min` 1.26×10⁻⁵ against `margin` 2.72×10⁻⁶; `n(L)` reads 7 on both, and the two solutions lie 1.12×10⁻⁸ apart. The midpoint before the refused one, `ε = 8.718402`, held K1 with `outside_min` 2.53×10⁻⁵.
- **The location.** The interval at `N = 24` and 32 is [8.720990, 8.724874], 4.5×10⁻⁴ of its lower end, narrower than the `w/2` that completes a bisection, and the union is that same interval, narrower than `w = 10⁻³`. The `n(L)` change at `N = 16` lies above both, as M8.17's record has it.
- **The guards.** Each is read at all three cutoffs at one `ε`, classified by the rule, and solved from its end of the bracket. The stored band is the one the reading used; Arm B's guards are outside the run's own band test, so this table gives each one against `R5`'s frozen level, 18, for the third note of #687's approval:

  | Side | `δ` | `ε` | `n(L)` at 16, 24, 32 | Type at 16, 24, 32 | The rule | Branch identity, 24 to 32 | Stored band | Level 18 at `λ` |
  |---|---|---|---|---|---|---|---|---|
  | lower | 0.01 | 8.633781 | 7, 7, 7 | Elliptic, Elliptic, Elliptic | converged: Elliptic | kept, 5.31×10⁻⁵ | 11.448124093 | 11.448124093 |
  | upper | 0.01 | 8.812122 | 7, 6, 6 | Elliptic, Hyperbolic, Hyperbolic | Unresolved | kept, 5.52×10⁻⁵ | 11.436284289 | 11.436284289 |
  | upper | 0.05 | 9.161117 | 6, 6, 6 | Hyperbolic, Hyperbolic, Hyperbolic | converged: Hyperbolic | kept, 5.95×10⁻⁵ | 11.413168793 | 11.413168793 |

  The upper guard at `δ = 0.01` lies below `N = 16`'s change, so `N = 16` reads `n(L) = 7` there against 6 at `N = 24` and 32, and the rule's structure condition leaves it Unresolved, as § The guards inferred: "the rule reads it Unresolved: structure: the type, indices, V0 or Krein counts differ along the ladder; tested group at 0.000131694+0j: no candidate of its class and Krein sign at a lower cutoff". The retry at `δ = 0.05` lies above it, and counts.
- **What is located.** The run names it: "a change of type located between the guard readings, with n(L) changing by -1 inside the interval at N = 24 and 32". Its resolution is an `n(L)` interval and two guard readings, not a crossing point. Its identification with the genuine index crossing is not claimed, and Corollary I is not applied.

## 3. Arm A's gates

- **The paths at `N = 24` and 32.** Each of the six controls' paths was solved and read at each registered point, and reproduced M8.16.1's record, with branch identity between them. The run compares them as it goes, and a difference stops it; it did not stop.
- **The kernel at `N = 40` passed** on all seven controls, against K1 as M8.16.1's terms freeze it, with its calibration constants unchanged. C1, at its four cutoffs, passes `checks.check_c1`, and its record, `N = 40` included, equals M8.16.1's: the first `N = 40` reproduced on this OS.

| Control | Slot | Seed | Points accepted at `N = 40` | K1 at `N = 40` | Path at `N = 40`, s |
|---|---|---|---|---|---|
| C2a | `R4` | ok | 4 of 4 | holds at 4 of 4 | 3381 |
| C2b | `R2` | ok | 4 of 4 | holds at 4 of 4 | 1244 |
| C3 | `R4` | ok | 4 of 4 | holds at 4 of 4 | 4673 |
| C2a/R5 | `R5` | ok | 4 of 4 | holds at 4 of 4 | 5485 |
| P5 | `R4` | ok | 4 of 4 | holds at 4 of 4 | 5229 |
| C3R/R4 | `R4` | ok | 4 of 4 | holds at 4 of 4 | 5351 |

- **The control gate did not pass.** Each control but C1 was read on `N = 24`, 32 and 40 at its registered points, on the band above `N = 16`. Each point must read converged with the type and indices on its record, and branch identity must hold on both pairs. All six were read and recorded before the gate decided. Branch identity held on both pairs at all 24 points. The reading beside the rule, on the band above `N = 24`, is unscored.

| Control | `ε` | The rule | Type; `(n(L), n(D), K)`, `k_i⁻` at `N = 40` | On record | Aligned distance, 24 to 32 | 32 to 40 | Beside, unscored | Gate |
|---|---|---|---|---|---|---|---|---|
| C2a | 0.25 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 3.57×10⁻¹⁰ | 1.05×10⁻¹⁴ | converged | passes |
| C2a | 0.5 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 1.42×10⁻⁹ | 8.32×10⁻¹⁴ | converged | passes |
| C2a | 1 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 5.59×10⁻⁹ | 6.51×10⁻¹³ | converged | passes |
| C2a | 2 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 2.18×10⁻⁸ | 4.99×10⁻¹² | converged | passes |
| C2b | 0.25 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 3.34×10⁻⁹ | 4.86×10⁻¹³ | converged | passes |
| C2b | 0.5 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 1.33×10⁻⁸ | 3.85×10⁻¹² | converged | passes |
| C2b | 1 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 5.24×10⁻⁸ | 3.01×10⁻¹¹ | converged | passes |
| C2b | 2 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 2.04×10⁻⁷ | 2.31×10⁻¹⁰ | converged | passes |
| C3 | 0.25 | converged | Hyperbolic; (6, 3, 3), 0 | Hyperbolic; (6, 3, 3) | 8.54×10⁻⁸ | 3.57×10⁻¹¹ | converged | passes |
| C3 | 0.5 | converged | Hyperbolic; (6, 3, 3), 0 | Hyperbolic; (6, 3, 3) | 3.41×10⁻⁷ | 2.85×10⁻¹⁰ | converged | passes |
| C3 | 1 | converged | Hyperbolic; (6, 3, 3), 0 | Hyperbolic; (6, 3, 3) | 1.36×10⁻⁶ | 2.27×10⁻⁹ | converged | passes |
| C3 | 2 | converged | Hyperbolic; (6, 3, 3), 0 | Hyperbolic; (6, 3, 3) | 5.39×10⁻⁶ | 1.79×10⁻⁸ | converged | passes |
| C2a/R5 | 0.25 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 1.70×10⁻¹⁰ | 6.33×10⁻¹⁵ | converged | passes |
| C2a/R5 | 0.5 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 6.74×10⁻¹⁰ | 4.88×10⁻¹⁴ | Unresolved | passes |
| C2a/R5 | 1 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 2.66×10⁻⁹ | 3.81×10⁻¹³ | converged | passes |
| C2a/R5 | 2 | converged | Elliptic; (0, 0, 0), 0 | Elliptic; (0, 0, 0) | 1.03×10⁻⁸ | 2.92×10⁻¹² | Unresolved | passes |
| P5 | 0.25 | Unresolved | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 8.63×10⁻⁸ | 5.42×10⁻¹¹ | Unresolved | **fails** |
| P5 | 0.5 | converged | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 3.43×10⁻⁷ | 4.29×10⁻¹⁰ | converged | passes |
| P5 | 1 | converged | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 1.35×10⁻⁶ | 3.37×10⁻⁹ | converged | passes |
| P5 | 2 | converged | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 5.27×10⁻⁶ | 2.59×10⁻⁸ | converged | passes |
| C3R/R4 | 0.25 | Unresolved | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 8.07×10⁻⁸ | 4.37×10⁻¹¹ | Unresolved | **fails** |
| C3R/R4 | 0.5 | converged | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 3.20×10⁻⁷ | 3.45×10⁻¹⁰ | converged | passes |
| C3R/R4 | 1 | converged | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 1.26×10⁻⁶ | 2.68×10⁻⁹ | converged | passes |
| C3R/R4 | 2 | converged | Hyperbolic; (5, 1, 4), 1 | Hyperbolic; (5, 1, 4) | 4.89×10⁻⁶ | 2.01×10⁻⁸ | converged | passes |

The two failures, as `run/out/GATE.json` states them:

- **P5:** "eps = 0.25: Unresolved, None: tested set at 8.67568e-16+4.02029j (+1): non-contracting above the floor".
- **C3R/R4:** "eps = 0.25: Unresolved, None: structure: a record is unresolved".

C3R/R4's record at `N = 40` carries "n(D): an eigenvalue of D lies in its gray zone"; its records at `N = 24` and 32 carry nothing. The record of the gate names P5, the first failure: "the control gate: P5: eps = 0.25: Unresolved, None: tested set at 8.67568e-16+4.02029j (+1): non-contracting above the floor".

**What followed, as the terms state:** "A failure inside Arm A's gates ends Arm A. The twelve stay unclassified, and the record is written." No other level was tried, and the run went on to its record. The log holds no job of any target, at any cutoff.

**The reading beside the rule** reads C2a/R5 at 0.5, C2a/R5 at 2, P5 at 0.25 and C3R/R4 at 0.25 Unresolved. It decides nothing here.

## 4. Why the gate failed: a diagnostic made after the run

This section is not a record from the run. It rests on the stored records and on `dev/runs/019_gate_cause/`, a diagnostic made after the run on a copy of this folder. It scores nothing, changes no record, and moves no verdict: the gate stands as § 3 states it. On the recorded machine, the diagnostic's reads of stored solutions, six in `diag_nd.py` and three in `pair_gap.py`, reproduce the stored `type`, `nL`, `nD`, `K`, `margin`, `unresolved` and `normA`. The cause the census applies is the one the adjudication names.

In both cases a tolerance that grows with the cutoff reaches a value that does not move (DERIVED from the records and those reads).

- **P5 at `ε = 0.25`.** Two Krein-positive eigenvalues near 4.0203 lie 1.1345×10⁻⁵ apart at all three cutoffs, read before they are linked. `linear.record` links eigenvalues within `τ(λ) = max(margin, 10 sqrt(u ‖A‖ |λ|))`, and ‖A‖ grows with the cutoff: 576, 1,040 and 1,632. So `τ` is 7.173×10⁻⁶, 9.636×10⁻⁶ and 1.207×10⁻⁵, and it passes the gap at `N = 40` alone, by 6.4%. There the pair is stored as one group of size 2 at its mean. The rule then compares that one centre with the two below it, and the set's change from `N = 32` is half the gap, 5.673×10⁻⁶, against 5.390×10⁻¹¹ from 24 to 32 and the floor 5.534×10⁻⁷: "non-contracting above the floor". The pair's mean is 4.020290064009, 4.020290063996 and 4.020290063996, changing by 5×10⁻¹⁴ from 32 to 40, and its members, read before they are linked, move by less than 10⁻¹³, the size of rounding. Across all 24 control points, it is the only pair inside the tested band that `τ` links at `N = 40` alone.
- **C3R/R4 at `ε = 0.25`.** D's negative eigenvalue is -0.01596075 at all three cutoffs, to the seven digits printed. `n(D)`'s gray zone is read against ‖B‖, 576.141, 1,040.140 and 1,632.310, and its top, `10⁻⁵ ‖B‖`, is 0.00576, 0.01040 and 0.01632. It passes 0.01596075 at `N = 40` alone, by 2.3%. D's zero eigenvalues read below 10⁻¹⁷ of ‖B‖ there.
- **At both points** the `N = 40` record reads Hyperbolic with (5, 1, 4), the recorded type and indices, and both failures are at the controls' smallest amplitude. The gate asks for a converged reading, and it was applied as the terms state.
- **What could have seen it.** Neither crossing needed a sealed reading: the pair's gap is in the stored `N = 32` record, D's eigenvalue can be read at `N = 24`, and ‖A‖ and ‖B‖ at `N = 40` follow from the top level, about `N(N + 2) - λ`. No check of the frozen tolerances at `N = 40`'s norms was run before the filing.

## 5. The twelve

None of the twelve was solved or read at any cutoff. Each is not classified, and each keeps M8.17's cause as M8.17 recorded it, with the gate named beside it in `run/out/CENSUS.json`. As the terms state, "that is not a second outcome with that cause". No band read them, so the two readings § DEFINITION OF DONE asks for, and the Krein-negative distance, do not apply. No type is claimed.

- **T1/R4, `ε = 1.41`:** the rule reads it Unresolved: tested set at 9.47465e-16+4.02388j (+1): the set's count differs between cutoffs.
- **T1/R4, `ε = 32`:** the rule reads it Unresolved: tested set at 3.01235e-15+0.342541j (+2): the set's count differs between cutoffs; tested set at 3.71208e-16+3.6807j (+1): the set's count differs between cutoffs; tested set at -7.11106e-16+3.92415j (+1): the set's count differs between cutoffs.
- **T1/R4, `ε = 45.25`:** the rule reads it Unresolved: tested set at 4.94519e-16+3.56238j (+1): the set's count differs between cutoffs; tested set at 2.24587e-16+3.86997j (+1): the set's count differs between cutoffs.
- **T1/R4, `ε = 64`:** the rule reads it Unresolved: tested set at 4.81427e-16+3.4127j (+1): the set's count differs between cutoffs; tested set at 4.38554e-17+3.79165j (+1): the set's count differs between cutoffs.
- **T1/R4, `ε = 72`:** the rule reads it Unresolved: tested set at -9.30127e-16+3.35419j (+1): the set's count differs between cutoffs; tested set at 2.16492e-16+3.75837j (+1): the set's count differs between cutoffs.
- **T4/R4, `ε = 4`:** the rule reads it Unresolved: tested set at -9.98233e-16+4.00991j (+1): the set's count differs between cutoffs.
- **T4/R4, `ε = 8`:** the rule reads it Unresolved: tested set at 7.8458e-16+3.98968j (+1): the set's count differs between cutoffs; tested set at -1.00202e-15+3.88085j (+1): the set's count differs between cutoffs.
- **T4/R4, `ε = 11.31`:** the rule reads it Unresolved: tested set at -2.54393e-15+3.97075j (+1): the set's count differs between cutoffs; tested set at -9.63062e-16+3.83191j (+1): the set's count differs between cutoffs.
- **T4/R4, `ε = 64`:** the rule reads it Unresolved: tested group at 3.39649e-15+3.0127j: non-contracting above the floor.
- **T4/R4, `ε = 72`:** the rule reads it Unresolved: tested group at 2.15032e-15+2.93462j: non-contracting above the floor; tested set at 1.11333e-15+3.29749j (+2): the set's count differs between cutoffs.
- **T1/R5, `ε = 32`:** the rule reads it Unresolved: tested set at 9.90708e-16+0.301797j (+1): the set's count differs between cutoffs.
- **T5/R2, `ε = 45.25`:** the rule reads it Unresolved: tested set at -6.21607e-16+0.592227j (+2): the set's count differs between cutoffs; partner set at -3.45032e-16+4.53231j (+1): the set's count differs between cutoffs; partner set at -3.45032e-16+4.53231j (+1): the set's count differs between cutoffs; partner set at -3.45032e-16+4.53231j (+1): the set's count differs between cutoffs; M8.15 left it Unresolved.

## 6. The brackets

- **T4/R4, (2.83, 5.66),** Elliptic to Hyperbolic, across the unclassified grid point 4: no type bracket, and not located. The point was not read, so no new bracket exists and the locator did not run.
- **T4/R5, (8, 11.31),** Elliptic to Hyperbolic: located, § 2.

## 7. The row outcomes

Each row's run outcome under § THE ROW OUTCOMES, and, separately, whether it meets an S4 completion condition. M8.17's outcomes stand as adjudicated, and these state where each row stands after this run.

| Row | M8.17's outcome | This run's | Meets an S4 completion condition | Open |
|---|---|---|---|---|
| T1/R4 | Not settled by this run | Not settled by this run | no | 1.41, 32, 45.25, 64, 72 |
| T4/R4 | Not settled by this run | Not settled by this run | no | 4, 8, 11.31, 64, 72, (2.83, 5.66) |
| T1/R5 | Not settled by this run | Not settled by this run | no | 32 |
| T4/R5 | Not settled by this run | Each change of type located | yes | none |
| T5/R2 | Not settled by this run | Not settled by this run | no | 45.25, 128, 132 |

This record does not apply S6: the census page applies it to each item after the adjudication, with the cause the adjudication names. Four statements bear on that step, and this record only reports them:
- the sentence quoted in § 5 keeps the gate's stop from being a second outcome with M8.17's causes, which is S6's first sentence;
- S6's last sentence closes as instrument-limited the rows a root cause blocks, where the maintainer admits no instrument that removes it, and the answer of 2026-10-29 leaves a point this run does not classify not offered to this instrument again;
- that answer applies S6 to T5's row when its point at 45.25 has been read again, and this run did not read it;
- the twelve, and T4/R4's change across 4, are in neither case the census page's note of 2026-10-30 names: a remedy was admitted for them and ran, and its gate stopped before it read them. The request of 2026-10-29 asked: "if only one remedy is admitted, or an admitted remedy ends without resolving its obstruction, may the remaining items close the same way, or does each cause need its own ruling?", and read the ruling of 2026-10-20 as covering these cases, "through S6's first sentence where a remedy meets the same cause again". The answer reads "Yes, your reading of S6 holds", and names two cases: no remedy admitted for an item, and a remedy that meets the same cause again.

## 8. What is new

The new evidence the terms name (§ Known outcomes, and what is new), as it fell:
- **At `N = 40`:** the 24 readings on the six controls, and the kernel on all seven. C1's `N = 40` record is M8.16.1's, reproduced. None of the twelve.
- **T4/R5's moved midpoint,** at `N = 24` and 32, each solved from both ends.
- **The guard readings:** 3, each at three cutoffs.
- **A new bracket's midpoints, and the new record at a bracket's end outside the twelve:** none, since no target was read.

## 9. Deviations

- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above, once, with no resume and no stop. It started after #688's opening and before its merge, as #688's body says.

## 10. Corrections and reading notes

- **No correction.**
- **#687's approval, its four notes.** The first: `--check` read before the launch, by the launch itself and after the run, with no difference (§ 1). The second, a global stop: none happened. The third, the stored band of Arm B's guards: § 2. The fourth, closure per item: read here only, in § 7.
- **#688's approval, its two notes.** The first: the environment record already carries macOS 15.8.2, so the comparison that tests the OS move is the run's own, with M8.16.1's and M8.17's records, and it found no difference. The second: `launch/resume_check.py` is published at the SHA-256 that approval pins, with its arms.

## 11. Follow-ups, outside M8.18

- **The catalog.** After the adjudication, the census page's dated note gives each row's ending and catalog status, with S6 applied per item, and S5's obligation stated as open (the terms, § DEFINITION OF DONE).
- **T5's row, the twelve and T4/R4's change across 4.** The third and fourth statements in § 7 are questions for the adjudication.
- **The location's identification.** T4/R5's location is an `n(L)` interval with two guard readings, not a crossing point; its identification with the genuine index crossing is not established (the terms, § ARM B).
- **The twelve.** The terms do not offer them to this instrument again. Anything MIT computes at these points after this run is outside this registration and is not part of this record.

## 12. Reproduction

`REPRODUCE.md` gives every command. For the run, from a copy of this folder:
- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and `python3 -I -B run/record_environment.py --check`;
- **the registered run:** the launch command above, from a copy without `run/out/`, beside a copy of `launch/` at `../resume_check/`. In a copy that keeps this `run/out/`, the resume check refuses, since the run has completed;
- `python3 -I -B tools/build_record.py --check`, which rebuilds this record from the files, recomputes the gate and every row with `census_lib`, and reports any difference.

Bitwise agreement on another machine is not claimed: the reproduction rules compare bit for bit on the recorded environment, which the readings before and after the run equal.
