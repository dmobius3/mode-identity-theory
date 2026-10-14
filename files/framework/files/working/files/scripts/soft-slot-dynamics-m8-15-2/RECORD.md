# M8.15.2 run record

The record of M8.15.2's target run on 2026-10-13, under the governing terms (OpenWave `1e8a6e2b`, SHA-256 `c6da782b43bc13d2…`), a delta on M8.15.1's, and the frozen locator v2 in this folder (MIT `851b2ad`). The locator v2 reads the M8.15.x instrument (MIT `97a8c08`) unchanged and leaves M8.15.1's locator (MIT `324fde3`) unchanged. Every number below is read from the target records in [`out/`](out/). The record is per branch and per bracket, with no aggregate verdict. Adjudication is the maintainer's.

## 1. Custody

- **Before the run.** The 13 checks in `out/prerun_check.json` passed at 2026-10-13T14:28:09Z:
  - the instrument's 17 `.py` files and `out/freeze_numbers.json` against its manifest, and the manifest's SHA-256 against the driver's pin and this folder's record of it;
  - both `SHA256SUMS`, 53 of 53 here and 196 of 196 in the instrument's folder;
  - the commits `851b2ad`, `9eab674`, `97a8c08` and `324fde3` on MIT `main`, and this folder equal to its tree at `851b2ad`, with no change and no untracked file;
  - the terms file, equal to the task document merged in OpenWave `1e8a6e2b`;
  - the instrument's `FROZEN.json`, which a target run reads (§ 6): its SHA-256 the one M8.15.1's record gives it, and its values those of `freeze_numbers.json`;
  - the environment, against the instrument manifest's, and no guard file yet;
  - the guard written by `write_guard.py` on a scratch copy of this folder, and passed by the driver's check before any solve.
- **The guard file,** `out/FROZEN.json`, was written once at 2026-10-13T14:28:09Z, before any target computation, by `write_guard.py`, called from the orchestration `out/run_m8_15_2.py`, which also wrote `out/prerun_check.json`. It carries `freeze_numbers.json`'s values unchanged, `frozen` true, the terms' SHA-256, the go ([#630](https://github.com/openwave-labs/openwave/pull/630#issuecomment-6147458225)), the instrument manifest's SHA-256 and the SHA-256 of `locate.py` and `t1_branch.py`. The driver checked it before any solve, and refuses a target without it.
- **Each target record** carries the terms' SHA-256, the SHA-256 of `locate.py` and `t1_branch.py` (equal to this folder's manifest and to the guard's), of the instrument's manifest and of the extracted `decide`. Its frozen block equals `freeze_numbers.json` at `97a8c08`, with `s₂` for its slot.
- **After the run.** Both `SHA256SUMS` pass, 53 of 53 and 196 of 196, and the guard file and the instrument's `FROZEN.json` are unchanged (`out/target_chain.log`).
- **Post-run files.** Four files beside this record were made after the run and are not records from it:
  - `tools/check_target_records.out`: `tools/check_target_records.py`, ALL PASS. It checks the custody above from the files, and the regression of § 4, with seven mutation arms, each caught.
  - `record_frozen_check_postrun_2026-10-13.out`: M8.15.1's `record_frozen_check.py` (MIT `324fde3`), run on a copy of this folder over its seven driver records (the qualification's five control records and the two target records), ALL PASS. It reads 215 points, 208 "not needed" and 7 "skipped". The skipped points are the points that do not balance: 2 in the control record `out/t1_C2a_R4_R1R4.json`, and the 5 of T3/R5's level 3 in § 3. Each point carries its own frozen record, and the fast-spectrum search ran at none.
  - `environment_postrun_2026-10-13.txt`: Python, numpy, scipy, platform and machine, read after the run, each equal to the instrument manifest's.
  - `adjudicate_targets_postrun_2026-10-13.out`: `adjudicate.py`'s reading of both target records, run on a copy of this folder (§ 3).
- **The run's files.** The last row is the instrument's `SHA256SUMS` as it stood during the run, unchanged since MIT `a261c7a`.

  | File | SHA-256 |
  |---|---|
  | `out/t1_T2_R4.json` | `6923448aee62093923d8604a7174229536e105e18a6bde06cf227ffa5699ed7d` |
  | `out/t1_T3_R5.json` | `04753279b48e38cd88c2ecc1013828e5006f5a9ca2d80c17d0f04a62c975039f` |
  | `out/run_T2_R4.log` | `5ffe332afc8e0106f745ea82c5799591fd8849fddb3dd31ca3532d0cd3532336` |
  | `out/run_T3_R5.log` | `2de66818d8344154c7dc2e0cc173e7dd60a9c48c319d51b3b076382ff1c80c8c` |
  | `out/target_chain.log` | `9e927e778d6b6dc066dc3cc9d25908d4629ca2e75f5225d0e57d3b8386fe2966` |
  | `out/prerun_check.json` | `f600f37613a67589ee6ac3a890e133afc81079b820c9b81a31b26048b884a4bf` |
  | `out/FROZEN.json` | `cb3a021f0bc02271cc39f26b61d10841e45405f71ba212423271f7af5d6eff92` |
  | `out/run_m8_15_2.py` | `7601c1ea8ae74ef7a0c4dc7fdcfb1dfcd964066668ca6df877f7d8f016c0cb51` |
  | `../soft-slot-dynamics-m8-15x/m8_15x_solver/out/FROZEN.json`, M8.15.1's guard | `ad40abbeaf2ea3561e783f7d86030cf53963741863e5491c8d558951637690e7` |
  | `../soft-slot-dynamics-m8-15x/SHA256SUMS` | `aad9af224605f95fd2c8d8ab3ee70c899129a4b45e44bfe1af93c7a704d6e1a7` |

  The post-run files:

  | File | SHA-256 |
  |---|---|
  | `tools/check_target_records.py` | `97ae81dacd92775beccebbb91749151d454abed6634dc48660abe4b108a7c0b2` |
  | `tools/check_target_records.out` | `4fd0f10d6bb27be25331d87d653933fd14c4bc063b54100a9c0280e6694cf697` |
  | `record_frozen_check_postrun_2026-10-13.out` | `d8acc0ed82a1bf2a1bfe85fb9f29a37a025362735329380dbd4ee0d00ebc723e` |
  | `environment_postrun_2026-10-13.txt` | `9c90f188125fb104e4c4539c80a06706cf6995be08fd3a397dff8880eb928a0c` |
  | `adjudicate_targets_postrun_2026-10-13.out` | `b35b2e65117edddf6ea0aacea57c62f71dad3ed91303ad098936cd4dfeacfc8d` |

T2/R4 ran from 2026-10-13T14:28:09Z to 2026-10-13T15:52:36Z, and T3/R5 from 2026-10-13T15:52:37Z to 2026-10-13T20:10:52Z. Both exited normally, and there is no crash record.

## 2. The ladder reruns

Both reproduce M8.15's ladder: each record's own comparison with M8.15's ran and found no difference (§ 4).

- **T2/R4:** Elliptic from 0.25 to 11.31 (12 points); Unresolved at 16 (cross-level disagreement); Unresolved at 22.63 (cross-level disagreement, level stability); Hyperbolic at 32.
- **T3/R5:** Elliptic from 0.25 to 11.31 (12 points); Unresolved at 16 (cross-level disagreement, level stability); Hyperbolic at 22.63, where this run's ladder ends.

## 3. The brackets

The target records carry every item of the terms' § REPORTED: each failing and exchanged-lift point's checks, counts and near-zero spectrum, and every continuity comparison with its three points, its two steps, its miss and its statistic. What follows reads them. In a branch step the clean ends are the step's ends and its name's location interval, and `n(L)` changes within its `n(L)` ends. A classified step's root is its crossing pair's interpolated zero: each crossing eigenvalue's zero, interpolated linearly between the reading ends and averaged over the crossing set, an estimate with no `10⁻³` guarantee. It is not where `n(L)` changes, which the `n(L)` ends bracket. Counts are `(n(L), n_S, n(B|G_tol), h)`.

### T2/R4, primary (16 to 22.6274)

| Level | Step | Clean ends | `n(L)` ends | Counts at the clean ends | Reading interval | Interpolated root | Branch step |
|---|---|---|---|---|---|---|---|
| 3 | genuine | 16.2589 to 16.2977 | 16.2848 to 16.2977 | (5, 2, 5, 0) to (7, 2, 5, 2) | 16.2589 to 16.2977 | 16.2807 | yes |
| 2 | Unresolved (index bookkeeping) | 16 to 16.5307 | 16.5178 to 16.5307 | (5, 2, 5, 0) to (7, 2, 7, 0) | 16 to 16.5307 | none | yes |

Both steps started on the grid cell 16 to 16.8284.

- **The points passed on `n(L)`:**
  - level 3 at `ε = 16.2848`: fails the structural subspace check; counts (5, 0, 5, 0);
  - level 2 at `ε = 16.4142`: fails the structural subspace check; counts (5, 0, 5, 0);
  - level 2 at `ε = 16.5178`: an exchanged lift, with the lower side's `n(L)` and `n_S = 0`, below that side's clean end's 2; counts (5, 0, 5, 0).

  Each lies inside its step's reading interval, so both steps are branch steps. Their near-zero spectra are in the record.
- **Level 3's crossings.** Two genuine eigenvalues change sign, from positive to negative, between the reading ends, and `Δn(L) = Δh = 2` with `Δn_S = 0`. Their interpolated zero, 16.2807, lies below the `n(L)` ends, 16.2848 to 16.2977, which bracket where `n(L)` changes. Their identity cosines between the clean ends are 0.9314 in full and 0.999999 outside `P`.
- **Level 2's bookkeeping.** Two crossings are classed genuine, with identity cosines 0.8924 in full and 0.999963 outside `P`. But `h` reads 0 at both clean ends: at 16.5307, `n(B|G_tol)` reads 7 where it reads 5 at 16. So `Δh = 0` against a signed genuine count of 2, and the step is Unresolved (index bookkeeping). The record's root field holds the clean ends' midpoint, 16.2654; an Unresolved step has no crossing root.
- **Points that do not balance:** none.
- **Solution continuity:** each step passes, with 8 comparisons (7 along the span and 1 across the step), no degenerate comparison and no duplicate target. The largest statistic is 3.75×10⁻⁴ at level 3 and 3.72×10⁻⁴ at level 2, against `τ_c = 3.4601×10⁻³`.
- **No genuine step is matched across levels,** so no guard was evaluated.
- **The record's names:** "no genuine crossing detected at level 2"; "an Unresolved step (index bookkeeping)", at level 2, 16 to 16.5307; "an index crossing located; the change of type remains unresolved" (cross-level disagreement).

### T3/R5, primary (11.3137 to 16)

| Level | Step | Clean ends | `n(L)` ends | Counts at the clean ends | Reading interval | Interpolated root | Branch step |
|---|---|---|---|---|---|---|---|
| 3 | structural | 13.1534 to 13.1626 | 13.1534 to 13.1626 | (12, 3, 5, 7) to (11, 2, 4, 7) | 13.0711 to 13.364 | 13.1609 | no |
| 3 | genuine | 15.7803 to 15.7986 | 15.7803 to 15.7895 | (11, 2, 5, 6) to (9, 2, 5, 4) | 15.7803 to 15.7986 | 15.7935 | yes |
| 2 | genuine | 15.7437 to 16 | 15.7437 to 15.7529 | (11, 2, 5, 6) to (9, 2, 5, 4) | 15.7437 to 16 | 15.8335 | yes |

The structural step started on the grid cell 13.0711 to 13.6569, and both genuine steps on 15.4142 to 16.

- **The points passed on `n(L)`,** each failing the structural subspace check, with counts (9, 0, 1, 8): level 3 at `ε = 15.7895`; level 2 at `ε = 15.8536`, 15.7803, 15.762 and 15.7529. Each lies inside its step's reading interval, so both genuine steps are branch steps. Their near-zero spectra are in the record.
- **The crossings.** At each level two genuine eigenvalues change sign, from negative to positive, between the reading ends, with `Δn(L) = Δh = −2` and `Δn_S = 0`. Their interpolated zeros, 15.7935 at level 3 and 15.8335 at level 2, lie above the `n(L)` ends, 15.7803 to 15.7895 and 15.7437 to 15.7529, which bracket where `n(L)` changes. Their identity cosines between the clean ends are 0.8042 in full and 0.999992 outside `P` at level 3, and 0.8242 and 0.999898 at level 2.
- **The structural step** at level 3 has one structural crossing, with `Δn(L) = Δn_S = −1` and `Δh = 0`.
- **Points that do not balance:** level 3: 5 points, from `ε = 13.1443` to `13.2175`, inside the structural step's reading interval, its threshold window. Level 2: none.
- **Solution continuity:** each of the three steps passes, with 8 comparisons (7 along the span and 1 across the step), no degenerate comparison and no duplicate target. The largest statistic is 7.55×10⁻⁴ for the structural step, and 6.79×10⁻⁴ for each genuine step, against `τ_c = 3.4601×10⁻³`.
- **The match and the guards.** The genuine steps match across levels, so every guard was read, in the terms' order. Each counts, and each of its points balances. No collision lies between the readings, and no point there fails to balance.

  | Side | Guard | `ε` at level 3 | `ε` at level 2 | Verdict | Decided | Same-`ε` diagnostic |
  |---|---|---|---|---|---|---|
  | lower | `d = 0.01` | 15.6356 | 15.6752 | Elliptic | yes | Unresolved (cross-level disagreement) |
  | lower | `d = 0.02` | 15.4777 | 15.5168 | Elliptic | yes | Unresolved (cross-level disagreement) |
  | lower | `d = 0.05` | 15.0039 | 15.0418 | Elliptic | yes | Unresolved (cross-level disagreement) |
  | lower | `d = 0.10` | 14.2142 | 14.2502 | Elliptic | yes | Elliptic |
  | lower | `d = 0.20` | 12.6348 | 12.6668 | Elliptic | yes | Elliptic |
  | lower | region end | 11.3137 | 11.3137 | Elliptic | yes | not read |
  | upper | `d = 0.01` | 15.9515 | 15.9918 | Unresolved (cross-level disagreement, level stability) | no | Unresolved (cross-level disagreement, level stability) |
  | upper | `d = 0.02` | 16.1094 | 16.1502 | Unresolved (cross-level disagreement, level stability) | no | Unresolved (cross-level disagreement, level stability) |
  | upper | `d = 0.05` | 16.5832 | 16.6252 | Hyperbolic | yes | Unresolved (cross-level disagreement, level stability) |
  | upper | `d = 0.10` | 17.3729 | 17.4169 | Hyperbolic | yes | Hyperbolic |
  | upper | `d = 0.20` | 18.9522 | 19.0002 | Hyperbolic | yes | Hyperbolic |
  | upper | region end | 22.6274 | 22.6274 | Hyperbolic | yes | not read |

- **The readings,** each side's nearest decided guard: Elliptic at `d = 0.01` below, and Hyperbolic at `d = 0.05` above. Neither side is mixed, and neither reading is a region end.
- **The record's names:** "a structural step", at level 3, with its interpolated root, 13.1609; "a located change of type", with the location and the readings above. The record carries clause 3's trigger, true.

### What follows under the terms

- **T2/R4: no change of type is located.** Level 3's genuine step has no genuine match at level 2, whose step is Unresolved. So the levels disagree, no guard is read, and the ceiling has nothing to restrict. `adjudicate.py` prints no line for this bracket (§ 6), and the record's names stand.
- **T3/R5: a change of type is located, under clause 3's qualifier.** The record names the matched genuine steps "a located change of type". The ceiling (the terms' § NAMING), read by `adjudicate.py`:
  - clause 1 does not hold: the four points of the two readings all balance;
  - clause 2 does not hold: every point between the readings balances, at both levels; level 3's five unbalanced points lie below the readings, inside the structural step's reading interval;
  - clause 3 holds: the genuine step is a branch step at both levels.

  The adjudicated name, in the terms' words: "A change of type is located between the registered guard readings. Its identification with the genuine index crossing at this step is not established: the crossing subspaces agree after removal of the structural directions, and the full spectral crossing identity remains unresolved. The step's classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count fell below its side's, by a rule whose changed branch has synthetic controls only."

  Beside it, as the terms require wherever it is reported: "The solution-continuity check does not certify which solution branch the step lies on, least of all where two branches share `m`."

  The record's own name beside both: "a located change of type".
- **Where it is confirmed.** The change of type is confirmed between the readings: Elliptic at 15.6356 at level 3 and 15.6752 at level 2, and Hyperbolic at 16.5832 and 16.6252. Their evidence does not place it at the interpolated zeros.
- **The name's location** gives the genuine-classed crossing pairs' interpolated zeros: 15.7935 at level 3, between the clean ends 15.7803 and 15.7986, and 15.8335 at level 2, between 15.7437 and 16, a cross-level shift of 2.53×10⁻³. They are estimates. `n(L)` changes within 15.7803 to 15.7895 at level 3 and 15.7437 to 15.7529 at level 2, and neither zero lies inside its level's `n(L)` ends.
- **What the matched reading does not establish** (M8.15.1's terms, § THE CONFIRMATION): that the two levels have the same type at one identical amplitude. The same-`ε` diagnostic, which is never a reading, is Unresolved at every offset up to 0.05 on both sides.
- **The structural step** at level 3, 13.1609, is reported as such, and is never a change of type.
- **The names** are the locator's automatic names, as frozen.

## 4. The regression

The terms (§ THE FREEZE, THE GUARD AND THE RUN, item 4) ask two things of the targets. `tools/check_target_records.py` checks both from the files.

- **The ladder reproduces M8.15's,** to 32 on T2/R4 and to 22.63 on T3/R5: each record's own comparison with M8.15's ladder ran (`compared` true) and found no difference.
- **M8.15.1's points reproduce, value for value.** Against M8.15.1's two target records, as committed at MIT `b13e0f4`:
  - every ladder entry M8.15.1 recorded up to this run's last target, at level 3, at level 2, its type and its cross-level check: 15, 15, 15 and 7 entries on T2/R4, and 14, 14, 14 and 6 on T3/R5, all equal;
  - every point of M8.15.1's primary bracket: on T2/R4, 16 of 16 at level 3 and 12 of 12 at level 2; on T3/R5, 22 of 22 and 12 of 12. Each is evaluated here at the same `ε`, and equals M8.15.1's record field for field.

  The records list a bracket's points by `ε`, not in the order evaluated, so the order itself is not checked.
- **No difference was found.** Under the approval of #630, a difference is reported and changes no name, and a comparison that did not run is not a pass.

## 5. Deviations

None in the target run. The orchestration, `out/run_m8_15_2.py`, lies outside the frozen set, and is filed here with its SHA-256. It ran the pre-run checks, wrote the guard file through `write_guard.py`, launched T2/R4 and then T3/R5, and ran the post-run checks. The machine was held awake for the run's length, on mains power.

## 6. Corrections

- **A target run reads the instrument's own `FROZEN.json`.** The terms say of M8.15.2's guard, in § THE FREEZE, THE GUARD AND THE RUN, item 3: "It never reads the instrument's own `FROZEN.json`." The maintainer's approval of #630 records that this is wrong for the target path. The driver takes `r_f` at both levels, `δ_lev` and `s₂` for its slot from that file, through the instrument's `frozen_numbers` (`t1_branch.py`, line 152), which also refuses a target without it.
  - The same statement stands in `REGISTER_5.md` (§ 1), in the docstring of `t1_branch.py`'s `validate_guard`, and in the freeze block on OpenWave.
  - Nothing in the run moved with it. The pre-run check pinned the file to the SHA-256 M8.15.1's record gives it, and its values to `freeze_numbers.json`. The post-run check found it unchanged, and each record's frozen block equals `freeze_numbers.json`.
  - The task document takes a dated note after the verdict, as the approval asks.
- **What `adjudicate.py` prints.** Its docstring and `REPRODUCE.md` say it prints "each bracket's adjudicated names". It prints one line per genuine step matched across levels, as the tests' `ceiling` returns them, and nothing for a bracket without one. T2/R4's primary has none, so its reading is empty and the record's own names stand. No name rests on the wording.

## 7. Follow-ups, outside M8.15.2

Any scored rerun needs a new pre-registration under the then-current M8 rules.
- **T2/R4's levels disagree.** Level 3 classifies its step genuine. Level 2's step, over the wider clean window 16 to 16.5307, fails the bookkeeping because `n(B|G_tol)` reads 7 at its upper clean end. Whether level 2's cluster count takes in the crossing pair there is open.
- **Lifting clause 3 on T3/R5** needs a real-solver control, registered in advance, whose genuine crossing is classified through a structural-subspace failure. No such control exists: the changed branch has synthetic controls only.

## 8. Reproduction

`REPRODUCE.md` gives every command. For the targets, from a copy of the scripts folder, since each run writes into `out/`:
- **The route this run took:** `out/run_m8_15_2.py --dry`, then `--go`, which writes the guard file, so it needs a copy without `out/FROZEN.json`. Its constants name this machine's paths.
- **By hand, with the committed guard file:**
  - `shasum -a 256 -c SHA256SUMS`, here and in `../soft-slot-dynamics-m8-15x/`;
  - the guard file stands as committed: `python3 write_guard.py TERMS GO` wrote it once and refuses now that it exists, and the driver checks it as it is;
  - `python3 -B t1_branch.py T2 4 --terms TERMS`, then `python3 -B t1_branch.py T3 5 --terms TERMS`, with `TERMS` the task document as merged in OpenWave `1e8a6e2b`;
  - `python3 -B adjudicate.py out/t1_T2_R4.json`, and the same for T3/R5;
  - `python3 -B tools/check_target_records.py`;
  - `python3 -B tools/check_record.py TERMS --mutations`, which recomputes this record's rows, numbers and hashes from the files.

## Post-adjudication note (2026-10-14)

Everything above this heading is the record as committed at MIT `f1ebda7`, unchanged. This note records the adjudication, and one comparison that the record's own does not make, and keeps every entry, number and hash as the locator returned them.

**The adjudication.** The maintainer adjudicated the run on OpenWave [#632](https://github.com/openwave-labs/openwave/pull/632#pullrequestreview-5511519208) and merged the method note unedited, at OpenWave `2a2d16ba`.

| Bracket | Adjudicated | The record's names, beside it |
|---|---|---|
| T2/R4, primary | No change of type is located. Level 3's genuine step, 16.2589 to 16.2977, has no genuine match at level 2, so no guard is read and the ceiling has nothing to restrict | "no genuine crossing detected at level 2"; "an Unresolved step (index bookkeeping)", at level 2, 16 to 16.5307; "an index crossing located; the change of type remains unresolved" (cross-level disagreement) |
| T3/R5, primary | A structural step at level 3, interpolated root 13.1609, never a change of type; and a change of type located, under clause 3's qualifier, with the name below | "a structural step"; "a located change of type" |

The name on T3/R5, in the terms' words: "A change of type is located between the registered guard readings. Its identification with the genuine index crossing at this step is not established: the crossing subspaces agree after removal of the structural directions, and the full spectral crossing identity remains unresolved. The step's classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count fell below its side's, by a rule whose changed branch has synthetic controls only."

Beside it: "The solution-continuity check does not certify which solution branch the step lies on, least of all where two branches share `m`."

**The ladder against M8.15, at both levels.** The record's own comparison, `compare_m815` in `t1_branch.py`, reads the type at every ladder point both runs reached, and `n(L)` and `n(B|G_tol)` at level 3's points only. § 2 and § 4 report that comparison. The adjudication compared both levels with M8.15's branch records, as at MIT `28c8a76`, and a recomputation from the records agrees:
- at the 15 shared points on T2/R4 and the 14 on T3/R5, every type, `n(L)`, `n(B|G_tol)`, Krein count and balance flag is equal at both levels;
- only the Newton residual differs, by at most 2.7% of the smaller value, on residuals between `5×10⁻¹³` and `8×10⁻¹²`;
- M8.15.1's ladder, which this run's equals value for value (§ 4), differs from M8.15's in the same way.

Under the approval of #630, a difference is reported and changes no name.
