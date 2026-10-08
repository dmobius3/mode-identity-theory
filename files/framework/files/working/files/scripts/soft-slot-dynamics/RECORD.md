# M8.15 run record

The record of M8.15's target run, 2026-10-07 to 2026-10-08, under the governing terms (OpenWave `4b1177c8`, SHA-256 `e0c32d01ba374a2e…`) and the frozen solver (MIT `6058f95`). Every number below is read from the branch records in [`m8_15_solver/out/`](m8_15_solver/out/); paths are relative to `m8_15_solver/`. Terms lines are cited at `4b1177c8`. The record is per branch, with no aggregate verdict (terms lines 275 to 279), and adjudication is the maintainer's. The run is reproduced as in [`REPRODUCE.md`](REPRODUCE.md).

## 1. Custody

- The 23 files the frozen manifest pins match it: 19 scripts and 4 data files.
- `SHA256SUMS` passes 52 of 52. The controls-first rerun's outputs are filed in `out/controls_first_2026-10-07/`, and the frozen control records are back in `out/`. That rerun passed every gate; its records differ from the frozen ones only in timing, and in s2 by at most 1.05e-10 relative.
- `FROZEN.json` was written at 20:10:02 UTC on 2026-10-07, before any target computation. The driver refuses a target without it. Its terms hash is the SHA-256 of the terms at `4b1177c8`, and every target record's frozen block equals it.

## 2. The per-branch record

Ladders: R4 has 18 points from 0.25 to ε_max = 72, R5 has 15 to 32, R2 has 20 to 132. Every branch except T4 reached ε_max.

| Branch | Linear types (level 3, cross-checked at level 2) | Validity at ε_min |
|---|---|---|
| T1/R4 | Unresolved at all 18: cluster check (G_tol dimension 6, frozen 4) and a paired lifted mode above τ₀ | **INVALID** |
| T1/R5 | Unresolved at all 15, the same two reasons | **INVALID** |
| T2/R4 | Elliptic 0.25 to 11.31 (12 points); Unresolved at 16 and 22.63; **Hyperbolic at 32, 45.25, 64 and 72** | pass, 1.23% |
| T2/R5 | Elliptic at all 15 | pass, 0.29% |
| T3/R4 | Elliptic at 17; **Invalid at 32** (eigenpair residual) | pass, 0.38% |
| T3/R5 | Elliptic 0.25 to 11.31 (12 points); Unresolved at 16; **Hyperbolic at 22.63 and 32** | pass, 1.28% |
| T5/R2 | Elliptic at 17; Unresolved at 45.25, 128 and 132 | pass, 0.48% |
| T4/R4, T4/R5 | none: ended at the seed (item 3) | none |

**Persistence, at level 2.** The thresholds (lines 259 to 262), with η = 1e-3 and T = 1000:
- Persists if max d_⊥ ≤ 10η = 1e-2 over [0, T];
- Invalid (drift) if d_rot exceeds √η ≈ 3.2e-2 first;
- Fails if d_⊥ exceeds 100η first.

A scheduled test moves down to the last Elliptic point inside the slow lineage with r·T ≤ ln(1/(10η)) = 4.61 (lines 229 to 232 and 253). "Periods" is T|Im λ|/2π for the slowest genuine slow mode outside G_tol, at level 2, at the point where the test ran (line 263).

| Branch | Test: scheduled → ran at | max d_⊥ | max d_rot | Reference floor | Periods | Verdict |
|---|---|---|---|---|---|---|
| T1/R4 | 8 and 32 | | | | | Not reached, both |
| T1/R5 | 4 and 16 | | | | | Not reached, both |
| T2/R4 | 8 → 5.657, and 32 → 5.657 (run once) | 1.34e-3 | 8.9e-4 | 1.2e-10 | 2.66 | Persists |
| T2/R5 | 4 | 1.00e-3 | 5.2e-4 | 5.7e-12 | 1.53 | Persists |
| T2/R5 | 16 | 1.07e-3 | 4.6e-4 | 2.3e-11 | 5.62 | Persists |
| T3/R4 | 8 → 2.828, and 32 → 2.828 (run once) | 1.00e-3 | 2.5e-5 | 2.1e-10 | 5.75 | Persists |
| T3/R5 | 4 | 1.07e-3 | 1.2e-5 | 2.0e-11 | 4.06 | Persists |
| T3/R5 | 16 → 11.31 | 1.45e-3 | 7.3e-5 | 1.2e-10 | 5.98 | Persists |
| T5/R2 | 16 | 0.98e-3 | 1.5e-4 | 1.2e-12 | 45.8 | Persists |
| T5/R2 | 64 | 0.94e-3 | 3.1e-4 | 6.6e-14 | 64.2 | Persists |

Every test that ran spans more than 1.5 periods (the least is 1.526, T2/R5 at 4), so line 263's caveat about tests shorter than one period applies to none of them.

**Details.**
- **T1, both slots, INVALID.**
  - **The missing mode.** The resolved Krein-negative slow mode is absent from the genuine modes at ε_min: predicted |λ| = 1.909e-4 (R4) and 1.087e-4 (R5).
  - **Where it went.** The 0.9 overlap rule takes the mode itself into G_tol. The cluster's extra pair sits at 1.814e-4 and 1.145e-4, within 5.0% and 5.3% of the prediction, and no genuine mode lies near it: the nearest are at 3.44e-3 and 1.93e-3.
  - **The rest matches.** The four matched modes agree within 0.80% and 1.22%. The terms make the mismatch an instrument defect, never a counterexample to the theorems (line 274).
  - **Persistence.** No ladder point is Elliptic, so both persistence tests are Not reached (line 232). The slow lineage also fails at ε_min, with validity.
- **Unresolved reasons.**
  - T2/R4: at 16, the levels disagree (worst ratio to tolerance 9.29); at 22.63, they disagree (1.16) and level stability fails.
  - T3/R5 at 16: the levels disagree (2.48) and level stability fails.
  - T5/R2: at 45.25, the levels disagree (1.32); at 128 and 132, the class counts differ between levels and level stability fails.
- **Invalid point: T3/R4 at 32.** An eigenpair's backward error exceeds the 1e-10 residual bound (lines 160 and 273). The frozen code writes Unresolved (eigenpair residual), and neither label is scored. No other point in any branch carries this breach.
- **Hyperbolic points.**
  - T2/R4: level 3 has two real pairs (k_r = 2) at each Hyperbolic point, balanced and level-stable.
  - T3/R5: at 22.63, two real pairs and one Krein-negative pair (k_r = 2, k_i⁻ = 1); at 32, three real pairs.
  - T5/R2: level 3 at 128 and 132 shows one quartet (k_c = 1), but those points are Unresolved.
- **No bisection ran.** The frozen code bisects only between adjacent ladder points of different decided type. In T2/R4 and T3/R5 every step from Elliptic to Hyperbolic passes through an Unresolved point, and such steps are not declared changes of type, the reading recorded at the merge. The decided types bracket the change: 11.31 to 32 in T2/R4, and 11.31 to 22.63 in T3/R5.
- **Moved tests.**
  - T2/R4: r·T is 4.05 at 5.657 and 5.39 at 8.
  - T3/R4: r·T is 3.95 at 2.828 and 5.32 at 4.
  - T3/R5: 16 is Unresolved, so the test moved to 11.31 (r·T 4.00).
  - The terms' expected-coverage note (lines 255 to 258) named T4 as where real pairs may still appear; the margin also bound at T2/R4 and T3/R4.
- **Every test that ran is valid and Persists.** Max d_⊥ is between 0.94e-3 and 1.45e-3. The slow lineage, a level-2 check, holds at every ladder point of every valid branch, so at every persistence point that ran.

## 3. T4's record (both slots), reconstructed

A record file per slot, `out/branch_T4_R4_reconstructed.json` and `_R5`, labelled `"reconstructed": true`, with these fields:
- `end`: `["Newton failure at the seed", null]`;
- no ladder point, type, change or persistence entry;
- `sources`: the run log, `run_T4_R*.log` and the exact-replay logs.

Its note states the run's facts only: "Original run: no branch record was written. The level-3 ladder stayed empty, and the driver then raised IndexError before writing a branch record. An exact replay with the frozen bytes reproduced no accepted Newton solution and recovered `Branch.first`'s end reason, Newton failure at the seed. No linear verdict or persistence test exists, and there is no finite-amplitude verdict for this branch."

The post-run diagnosis stays outside the record, in [`out/post_run/`](m8_15_solver/out/post_run/) with its scripts and logs, and in the method note as post-run evidence:

"A post-run diagnosis attributes the failure to the instrument's stopping test. The frozen Newton solves T4's bordered equation to round-off. Its stopping test leaves out the phase multiplier's term, which is nonzero because T4's slice overlaps the phase direction and the slice force is nonzero; the slice control, C3s, had neither. R4: the test stalls at |μT|/|Mx| = 1.085e-6 at level 3 (M-cosine 0.1256). R5: 1.654e-5 at level 2 (M-cosine 0.1256); level 3 not run. The check, at level 2 for T4/R4, T4/R5 and C3s/R4 and at level 3 for T4/R4, was declared in the bench log before it ran, and it reproduces an independent review's earlier level-2 bench check. Under line 44, a defect claim is reproduced by the maintainer with independent code before it is ratified."

## 4. Deviations

1. **Controls-first stop, 2026-10-07 20:01 UTC.** The run's own byte check on `freeze_numbers.json` stopped it before any target. Every gate passed; s2 differed by at most 1.05e-10 relative, because the frozen spreads predate the one-thread pin. The run resumed on the author's go with the frozen values governing.
2. **All nine targets launched at once, 20:10 UTC.** An orchestration fault (a zsh quirk stored the literal `$!` as each pid) started all nine together. The seven later-wave processes were stopped after about 50 s, in setup, with empty logs. Their output was discarded, and they ran from the start in their planned waves from the same bytes. The orchestration lies outside the frozen set.
3. **The driver's IndexError on an empty ladder (T4/R4, T4/R5).** Recorded under the contingency in the author's plan of record, fixed before launch: the branch ends there, by an instrument failure, with no code change. The terms have no crash rule, and the maintainer adjudicates. The end reason is recovered by the exact replay.
4. **Post-run diagnostics, outside the record:** the exact replays, the post-hoc Newton trace, the gauge-term check, and an independent review's bench checks. None changed a record.
5. **The controls-first rerun wrote its records over the frozen control records in `out/`.** Those are restored from `6058f95`, and the rerun's records are filed in `out/controls_first_2026-10-07/`.
6. **Pre-flight smoke test, after the go and before launch.** C2b ran from the repo copy at bench test levels 2 and 1, to ε = 2, T = 10, in 19 s. Its output was moved out of the repo.

## 5. Follow-ups, outside M8.15

These are outside M8.15. Any scored rerun of T1 or T4 requires a new pre-registration under the then-current M8 rules. Instrument fixes and controls may be developed beforehand, but must be frozen and qualified under that new run.
- **T1:** separate the resolved Krein-negative slow mode from the lifted rotation pair robustly, with an armed control before any T1 rerun.
- **T4:**
  - a stopping test that includes every multiplier;
  - "the gauge multipliers vanish at a solution" restated for slice cases;
  - a slice control with a nonzero phase overlap and a nonzero slice force;
  - a driver that writes the record when the ladder is empty;
  - a check of the T1 overlap rule against the third outside orbit's smallest slow mode, which an independent review check found the same rule may also take (not verified in this record).
- **Physics:** locate the bracketed changes of type, T2/R4 between 11.31 and 32 and T3/R5 between 11.31 and 22.63. These terms leave them unlocated.
