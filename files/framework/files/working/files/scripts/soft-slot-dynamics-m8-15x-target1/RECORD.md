# M8.15.1 run record

The record of M8.15.1's target run on 2026-10-12, under the governing terms (OpenWave `dcc63851`, SHA-256 `fc566c0406fef33d…`) and the frozen locator in this folder (MIT `324fde3`), which reads the M8.15.x instrument (MIT `97a8c08`). Every number below is read from the target records in [`out/`](out/). The record is per branch and per bracket, with no aggregate verdict. Adjudication is the maintainer's.

## 1. Custody

- **Before the run.** The ten checks in `out/prerun_check.json` passed at 2026-10-12T02:53:20Z:
  - the instrument's 17 files and `out/freeze_numbers.json` against its manifest;
  - both `SHA256SUMS`, 83 of 83 here and 196 of 196 in the instrument's folder;
  - the locator's and the instrument's commits on `main`;
  - the terms file, equal to the merged task document;
  - the guard on the real instrument, and the freeze check with the guard file present.
- **The guard file,** `../soft-slot-dynamics-m8-15x/m8_15x_solver/out/FROZEN.json`, was written at 2026-10-12T02:53:20Z, before any target computation, by the orchestration `out/run_m8_15_1.py`, which also wrote `out/prerun_check.json`. It carries `freeze_numbers.json`'s values unchanged, the terms' SHA-256, the go ([#624](https://github.com/openwave-labs/openwave/pull/624#issuecomment-6116132742)) and the two commits. The locator refuses a target without it.
- **Each target record** carries the terms' SHA-256, the SHA-256 of the locator's code (equal to this folder's manifest), of the instrument's manifest and of the extracted `decide`. Its frozen block equals `freeze_numbers.json` at `97a8c08`, with `s₂` for its slot.
- **After the run.** The instrument's `SHA256SUMS` passes 196 of 196, and `FROZEN.json` is unchanged. `record_frozen_check.py` passes over all seven driver records: the five committed control records (93 points) and the two target records (96 points: 80 "not needed" and 16 "skipped"). The 16 skipped points are the points § 3 lists as not balancing. Each point carries its own frozen record, with a search result exactly where the search ran.
- **The environment.** Checked after the run: the machine's Python, numpy, scipy and platform equal the instrument manifest's.
- **The run's files.** The last row is the instrument's `SHA256SUMS` as it stood during the run. A later commit adds a dated note to the instrument's `REPRODUCE.md` and rewrites that file, so its hash after that commit is not the run's.

  | File | SHA-256 |
  |---|---|
  | `out/t1_T2_R4.json` | `f7640113fe33d399f548d8599db26ff135fd18ffd8cea7f4e5d1479f0e86d325` |
  | `out/t1_T3_R5.json` | `224096451ce0bf5b2579ced6032904b4beb92c985358b79786d7172b4756dfdf` |
  | `out/run_T2_R4.log` | `6edd99da3d08d2c11b213504a7ce224654825bfd1b369fe0ac739d54c785ec52` |
  | `out/run_T3_R5.log` | `22feed55fc5e25392c4f39bcc04a68796bc666991cf680773b3daf055a155454` |
  | `out/target_chain.log` | `bbed64548d8a290b919a7f4f2d4293f6eed0a4b774726a8239da08f01d138401` |
  | `out/prerun_check.json` | `528f9f4eec81afed64f1c7bcca4e4a99a4848da8fba356b3524dd5e0ee44b2e8` |
  | `out/run_m8_15_1.py` | `33338e2d27b6626a59ba167c464b405f051ed104b2bb8e6006081b4ddf411f45` |
  | `../soft-slot-dynamics-m8-15x/m8_15x_solver/out/FROZEN.json` | `ad40abbeaf2ea3561e783f7d86030cf53963741863e5491c8d558951637690e7` |
  | `../soft-slot-dynamics-m8-15x/SHA256SUMS`, as it stood during the run (MIT `ae3ad04`) | `200759a28ed01588c0df79c254f0653462baa70f7f87e5f6aa63af39ce46a8e4` |

T2/R4 ran from 2026-10-12T02:53:21Z to 2026-10-12T04:13:52Z, and T3/R5 from 2026-10-12T04:13:52Z to 2026-10-12T09:21:13Z. Both exited normally, and there is no crash record.

## 2. The ladder reruns

Both reproduce M8.15's ladder: every type, `n(L)` and `n(B|G_tol)` at every point both reached.

- **T2/R4:** Elliptic from 0.25 to 11.31 (12 points); Unresolved at 16 (cross-level disagreement); Unresolved at 22.63 (cross-level disagreement, level stability); Hyperbolic at 32.
- **T3/R5:** Elliptic from 0.25 to 11.31 (12 points); Unresolved at 16 (cross-level disagreement, level stability); Hyperbolic from 22.63 to 32 (2 points).

## 3. The brackets

### T2/R4, primary (16 to 22.6274)

| Level | Step | Final interval | Counts at its ends, `(n(L), n_S, n(B\|G_tol), h)` | Reading interval | Root |
|---|---|---|---|---|---|
| 3 | Unresolved (structural subspace) | 16.2589 to 16.3107 | (5, 2, 5, 0) to (7, 2, 5, 2) | none | none |
| 2 | Unresolved (structural subspace) | 16 to 16.8284 | (5, 2, 5, 0) to (7, 2, 5, 2) | none | none |

- **Points that fail a check:**
  - level 3 at `ε = 16.2848`: structural subspace; 2 structural eigenvectors of the 4 required; counts (5, 0, 5, 0);
  - level 2 at `ε = 16.4142`: structural subspace; 2 structural eigenvectors of the 4 required; counts (5, 0, 5, 0);
- **Points that do not balance:** none.
- **The record's names:** "no genuine crossing detected at level 3"; "an Unresolved step (structural subspace), at level 3"; "no genuine crossing detected at level 2"; "an Unresolved step (structural subspace), at level 2".

### T3/R5, primary (11.3137 to 16)

| Level | Step | Final interval | Counts at its ends, `(n(L), n_S, n(B\|G_tol), h)` | Reading interval | Root |
|---|---|---|---|---|---|
| 3 | structural | 13.1534 to 13.1626 | (12, 3, 5, 7) to (11, 2, 4, 7) | 13.0711 to 13.364 | 13.1609 |
| 3 | Unresolved (structural subspace) | 15.7803 to 15.7986 | (11, 2, 5, 6) to (9, 2, 5, 4) | none | none |
| 2 | Unresolved (structural subspace) | 15.7071 to 16 | (11, 2, 5, 6) to (9, 2, 5, 4) | none | none |

- **Points that fail a check:**
  - level 3 at `ε = 15.7895`: structural subspace; 2 structural eigenvectors of the 4 required; counts (9, 0, 1, 8);
  - level 2 at `ε = 15.8536`: structural subspace; 2 structural eigenvectors of the 4 required; counts (9, 0, 1, 8);
- **Points that do not balance:** level 3: 5 points, from `ε = 13.1443` to `13.2175`. Level 3's lie inside its structural step's reading interval, its threshold window.
- **The record's names:** "no genuine crossing detected at level 3"; "a structural step, at level 3"; "an Unresolved step (structural subspace), at level 3"; "no genuine crossing detected at level 2"; "an Unresolved step (structural subspace), at level 2".

### T3/R5, secondary (22.6274 to 32)

| Level | Step | Final interval | Counts at its ends, `(n(L), n_S, n(B\|G_tol), h)` | Reading interval | Root |
|---|---|---|---|---|---|
| 3 | Unresolved (no balanced reading end) | 28.0276 to 28.0459 | (9, 2, 4, 5) to (10, 3, 5, 5) | none | none |
| 3 | Unresolved (no balanced reading end) | 28.467 to 28.4853 | (10, 3, 6, 4) to (8, 2, 5, 3) | none | none |
| 2 | genuine | 31.9817 to 32 | (9, 2, 5, 4) to (8, 2, 5, 3) | 31.9817 to 32 | 31.9934 |

- **Points that fail a check:** none.
- **Points that do not balance:** level 3: 10 points, from `ε = 27.8995` to `28.467`; level 2: 1 point, at `ε = 28.4853`.
- **`n_S` reads 3** at level 3 from `ε = 28.0459` to `28.467` (6 points), and 2 elsewhere in the bracket.
- **The record's names:** "no genuine crossing detected at level 3"; "an Unresolved step (no balanced reading end), at level 3"; "an Unresolved step (no balanced reading end), at level 3"; "an index crossing located; the change of type remains unresolved (cross-level disagreement)". The secondary makes no type claim in any case.

### What follows under the terms

- **No genuine step matched across levels in any bracket.** So no guard was read, and no change of type is located.
- **The ceiling has no positive result to restrict.** The fast-spectrum search did not run in either target run: every ladder point balanced, the bracket points were "not needed" or "skipped", and no guard was evaluated.
- **What the brackets detected.** Each registered bracket detected an index change within the final intervals reported above. An Unresolved step has no certified crossing identity and no eigenvalue root.
- **The names** are the locator's automatic names, as frozen. "No genuine crossing detected at level 3" means that no step qualified as genuine under the registered tests. It does not exclude a genuine crossing.

## 4. What the failed checks show

This section reports data the record carries. It is not part of any verdict.

- **The failing points.** At each primary unresolved candidate crossing, the bisection's last midpoint, inside the final interval, fails the structural subspace check at both levels. It has two structural eigenvectors where four are required, and `n_S = 0` where both ends of the final interval have 2.
- **The consequence.** A point that fails that check cannot end a bisection (§ THE LOCATOR, step 2), so the step is Unresolved.
- **The counts at the final interval's ends** differ by `Δn(L) = ±2`, `Δn_S = 0` and `Δh = ±2`, matching the registered index arithmetic. The analysis stopped before it formed the crossing set, so the class of the crossing eigenvectors is the open question.
- **"The slowest genuine pair"** is the slowest pair of the slow spectrum outside the frozen cluster, the slow modes M8.15 sets aside. That classification is separate from the locator's own structural and genuine split of the eigenvectors of `L`. Its static overlap with the rotations, `span{X_aΦ}`, is recorded at every point.

**T3/R5, level 3, around the crossing:**

| `ε` | `n(L)`, `n_S`, `n(B\|G_tol)`, `h` | balances | the slowest genuine pair | its overlap with the rotations |
|---|---|---|---|---|
| 15.7071 | 11, 2, 5, 6 | yes | imaginary, 0.00653 | 0.045 |
| 15.7803 | 11, 2, 5, 6 | yes | imaginary, 0.0027 | 0.282 |
| 15.7895 (fails the structural subspace check) | 9, 0, 1, 8 | yes | real, 0.000512 | 0.868 |
| 15.7986 | 9, 2, 5, 4 | yes | real, 0.0017 | 0.455 |
| 15.8169 | 9, 2, 5, 4 | yes | real, 0.00337 | 0.154 |
| 15.8536 | 9, 2, 5, 4 | yes | real, 0.00542 | 0.063 |
| 16 | 9, 2, 5, 4 | yes | real, 0.0101 | 0.019 |

**T3/R5, level 2:**

| `ε` | `n(L)`, `n_S`, `n(B\|G_tol)`, `h` | balances | the slowest genuine pair | its overlap with the rotations |
|---|---|---|---|---|
| 15.7071 | 11, 2, 5, 6 | yes | imaginary, 0.00809 | 0.380 |
| 15.8536 (fails the structural subspace check) | 9, 0, 1, 8 | yes | imaginary, 0.00471 | 0.892 |
| 16 | 9, 2, 5, 4 | yes | real, 0.00954 | 0.220 |

**T2/R4, level 3:**

| `ε` | `n(L)`, `n_S`, `n(B\|G_tol)`, `h` | balances | the slowest genuine pair | its overlap with the rotations |
|---|---|---|---|---|
| 16 | 5, 2, 5, 0 | yes | imaginary, 0.0066 | 0.768 |
| 16.2071 | 5, 2, 5, 0 | yes | imaginary, 0.00352 | 0.752 |
| 16.2589 | 5, 2, 5, 0 | yes | imaginary, 0.00209 | 0.684 |
| 16.2848 (fails the structural subspace check) | 5, 0, 5, 0 | yes | imaginary, 0.171 | 0.000 |
| 16.3107 | 7, 2, 5, 2 | yes | real, 0.00189 | 0.822 |
| 16.4142 | 7, 2, 5, 2 | yes | real, 0.00447 | 0.785 |
| 16.8284 | 7, 2, 5, 2 | yes | real, 0.00941 | 0.774 |

**T2/R4, level 2:**

| `ε` | `n(L)`, `n_S`, `n(B\|G_tol)`, `h` | balances | the slowest genuine pair | its overlap with the rotations |
|---|---|---|---|---|
| 16 | 5, 2, 5, 0 | yes | imaginary, 0.00827 | 0.655 |
| 16.4142 (fails the structural subspace check) | 5, 0, 5, 0 | yes | imaginary, 0.172 | 0.000 |
| 16.8284 | 7, 2, 5, 2 | yes | real, 0.00759 | 0.832 |

- **At T3/R5's failing points,** `n(B|G_tol)` falls from 5 to 1 while the Krein count still balances. So the overlap there may come from structural directions leaving the cluster, as well as from the crossing mode.
- **At T2/R4's failing points,** the slowest genuine pair is a different and much faster mode, with overlap 0. At level 2's failing `ε`, 16.4142, level 3 reads 0.785. The record leaves open why.
- **A reading, not established here:** where the crossing eigenvalue of `L` passes zero, the crossing mode and two structural directions are close to degenerate, so the static classification does not separate them at that point.

## 5. Deviations

None in the target run. The orchestration, `out/run_m8_15_1.py`, lies outside the frozen set, and is filed here with its SHA-256. It ran the pre-run checks, wrote the guard file, launched T2/R4 and then T3/R5, and ran the post-run checks. The machine was held awake for the run's length.

## 6. Corrections

- **Where the fast-spectrum search has run.** The maintainer's approval of [#624](https://github.com/openwave-labs/openwave/pull/624#pullrequestreview-5485856574) records one qualification point that ran it: P5 in `../soft-slot-dynamics-m8-15x/qualification/regress_verdict_before.json` (level 2, `ε = 0.25`; 83 eigenvalues found, counts `[0, 0, 0]`, still unbalanced).
  - Three places say otherwise: the terms' § Standing, the instrument's `REPRODUCE.md` note of 2026-10-11, and `RESULT_4.md` in this folder.
  - A sweep of every JSON record in the soft-slot folders finds that point and no other.
  - The approval calls P5 "the refactor's regression gate, not a target or a control", and no rule, threshold or verdict rests on the statement.
  - The commit after this record adds a dated note to the instrument's `REPRODUCE.md`, and the task document will take one after the verdict.

## 7. Follow-ups, outside M8.15.1

Any scored rerun needs a new pre-registration under the then-current M8 rules.
- **Classifying the primary index changes** needs a rule that separates the crossing mode from the structural directions through their near-degeneracy. Any such rule stands on controls, with these records disclosed under the memo's rule 4, since they motivated it.
- **The secondary's levels place its change far apart:** near 28.0 to 28.5 at level 3, and at 31.98 at level 2. A cross-level comparison there needs the memo's § 3.
