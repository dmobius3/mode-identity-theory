# M8.15.x: qualification (§ 6), results (run finished 2026-10-09T19:44Z)

**Status:** v3. v2 folded both review units' review of v1. v3 folds their NITs on v2, and both gave GO for the freeze.
- **The verdict.** The instrument is qualified as registered: every registered comparison passes, and there was no regression deviation.
- **One correction.** A sentence of § 3's rationale was wrong, though its rule held (see "The residual").
- **The fixes.**
  - `REGISTER_3.md`'s amendment of 20:24Z: § 1's `pinned.py` row, § 3's reading and the gauge-norm premise, and § 8's sequence and checks.
  - The corrections on this page. They include one to v1's own wording: only the linear records carry iteration counts.
- **What follows.** Nothing reruns. The freeze waits for the maintainer's go.

**The registration** is `REGISTER_3.md` v2, registered at 2026-10-09T14:33:42Z, with its amendment of 14:35:39Z on the branch floors. Notes followed the run at 19:51Z, 20:24Z and 20:53Z. The run started at 14:39:23Z and finished at 19:44:03Z: 5 h 5 min, against the estimate of 10 to 11 h.

**The code:**
- `qual_run.py`, the orchestrator;
- `qual_compare.py`, the comparator. Its self-test passed 21 of 21 arms on M8.15's baseline before the run.

**The instrument's bytes.** The SHA-256 of the solver folder's 18 files was recorded at the start, in `QUALIFICATION.json`. It matches the files after the run, so every job ran on the same bytes. The 18 include `cluster_rule.py`, which § 8 leaves out of the freeze.

**The records** are in `qual_2026-10-09/`:
- `QUALIFICATION.json`, `.log` and `.progress`, and `ENVIRONMENT.json`;
- the job logs in `logs/`, the controls' records in `controls/`, and the baselines in `baseline/`.

The rerun records are in `solver/m8_15_solver/out/`. The bench's earlier `out/` was archived to `solver/m8_15_solver/out_pre_qual_2026-10-09/`.

## The verdict: qualified as registered

| Register | Test | Outcome |
|---|---|---|
| § 2.1 | the environment, field by field against `MANIFEST.json` | identical, no differences |
| § 2.2 | the frozen-bytes arm: 19 files against `6058f95`, then `spreads` bit for bit | pass |
| § 2.3 | the static inputs, by SHA-256 against the repo | 3 of 3 |
| § 6 | control 4, 1a, 1b, the carry, the ν-sign kind | all pass |
| § 3 | `linear 3`, `linear 2` (932 values each) | within tolerance: only the 10 residuals moved in each |
| § 3 | `theoremD 3` | passes the frozen gate; `theoremD_rel = 1.217×10⁻¹³` |
| § 3 | `spreads` | bit-identical |
| § 3 | `dynamics` C1, C2a, C2b, C3 and `rate` | bit-identical, `.npy` series included |
| § 3 | `summarize` | only `s2` differs, by the recorded amounts: `1.054×10⁻¹⁰` (R4), `2.23×10⁻¹¹` (R5), `2.00×10⁻¹¹` (R2); the rest bit-identical; the governing file restored |
| § 4 | the unit check, on all five dynamics records | pass |
| § 5 | the C3 branch (1956 values) | bit-identical apart from its 36 residuals; no floor used |
| § 5 | the C2a branch (2108 values) | bit-identical apart from its 36 residuals; no floor used |

**Newton iteration counts.** Only the two linear records carry them, 10 each.
- None moved, so § 3's straddle rule was never needed.
- The branch and dynamics records carry none. v1 said "in any record", which overstated it.
- § 5's branch rule does not read iteration counts.

**§ 6's controls,** on the final bytes, ran from 14:39Z to 14:49Z:
- **Control 4.** Arm a wrote a full branch record ending "Newton failure at the seed", exit 0. Arm b wrote a crash record with stage `level 2`, its traceback and the frozen block, exit 1.
- **1a.** Its seven checks and the amendment's seven pass, and every mutation arm is caught.
- **1b.** Checks 1 to 5 pass. The selected solution is bit-identical to the earlier run's, so check 6 carries forward.
- **The carry and the ν-sign kind.** Their ten and seven checks pass, and every mutation arm is caught.

**Theorem D at level 3.** The rerun passes the frozen gate. Its value, `1.2170940212688522×10⁻¹³`, rounds to the recorded `1.2×10⁻¹³`.
- **M8.15's own record** was filed with its frozen solver in `6058f95` (`m8_15_solver/out/theoremD_L3.json`), and the rerun is byte-identical to it.
  - § 3 had stated that it was filed nowhere in the repo; the note of 20:53Z corrects that.
  - The comparison ran as registered and passed. Against the filed record it also matches bit for bit.
- The qualification's record is filed with the freeze (amendment of 20:24Z), so that the next qualification has a baseline on record.

**The branches.** Apart from the residuals, both are bit-identical to the committed baselines: every categorical result, eigenvalue, Krein value, persistence diagnostic and schedule entry. No floor was used.
- § 5 recorded that it was not known whether these baselines predate the one-thread pin.
- They reproduce bit for bit under it. That does not date them.

## The residual: what moved, and a correction to § 3's rationale

**What moved.** The four records with Newton solves hold 92 residuals: 10 in each linear record, and 36 in each branch (18 points at each level).
- All 92 moved, and all are within the registered rule.
- Both values are at or below `10⁻¹¹`; the largest is `6.1×10⁻¹²`.
- `|new − old|` is at most 0.60 of its bound, `Σ|μ| + 10⁻¹³`. The largest move is `6.10×10⁻¹⁴`.

**The correction.** § 3 says the new test "adds exactly the μ terms", so a move should stay within `Σ|μ|`. It did not.
- 86 of the 92 moves exceed `Σ|μ|`. The largest `Σ|μ|` is `1.18×10⁻¹⁴`, and the largest excess over it `5.96×10⁻¹⁴`.
- The rule's `10⁻¹³` term carried them. That term was a registered numerical allowance, not a proved bound on the changed evaluation, and it is not read as one.

**The mechanism, measured at level 2** (`diag_residual.py` and `.out`, a diagnostic, not a registered check).
- **The two tests code the physical residual differently.**
  - The frozen test calls `standing.residual`, which applies `K` and `M` as complex matrices to `Φ`.
  - The bench's test reads Newton's own inline `F`, which applies their real forms `Kr` and `Mr` to `x`.
  - The two are equal in exact arithmetic but round differently. On a random vector the products differ by `2.7×10⁻¹⁶` (`K`) and `2.3×10⁻¹⁶` (`M`) relative, and neither is bit-identical.
- **At a converged iterate the residual is at its evaluation floor.** At the level-2 seed solves of C3 and C2a:
  - the two codings' residual vectors differ by 0.51 and 0.59 of their own norm;
  - their norms differ by `6.8×10⁻¹⁵` and `4.4×10⁻¹⁶`;
  - the μ terms move the norm by only `1.8×10⁻¹⁸` and `5.7×10⁻¹⁷`.
- **So at level 2 the moves are the coding's round-off, not the μ terms.**

**At level 3, by elimination.**
- **The iterates are unchanged.**
  - Newton's update is untouched by the diff. Only the stopping test's value changed.
  - At the 10 level-3 linear points this follows from the recorded iteration counts.
  - At the branches' 36 level-3 points it follows from the bit-identical records: one Newton step more or fewer at convergence would have changed their bits.
- **The bound.** At the same iterate, `|new − old| ≤ Σ_k |μ_k| ‖T_k‖/‖M x‖ + (the recoding's move)`.
  - § 3 took `‖T_k‖ = ‖M x‖`. In fact each `T_k` is built at the solve's starting point.
  - At the two traced level-2 seeds the ratio is 0.999988 and 0.999724 (`diag_residual.out`, a line added after the review; the reviewed lines reproduce unchanged).
- **The result.** Every level-3 move is at least 2.66 times `Σ|μ|`, with one gauge per solve, so the recoding moved all 46.
  - Its one premise is that `‖T‖/‖M x‖` stays below 2.66 at those points. It is not recorded there.
  - **Why the premise is safe.** `Branch.newton` scales the start to the norm `m`, and the solve holds that norm, so the start and the converged iterate share their M-norm. The ratio departs from 1 only through the change of shape within one solve. It is disclosed, not measured, at level 3.
- **What stays INFERRED at level 3** is that the residual there is dominated by round-off, as at level 2. The vectors' difference was measured only at level 2.
- **The sizes agree.** The relative moves are the same size at both levels: 0.06% to 3.3% at level 2, and 0.3% to 2.3% at level 3, over 46 residuals each.

**What it changes.** The verdict stands: the rule is the registered one, and it passed.
- If the largest move had been 1.7 times larger, the rule would have failed, although no solution changed.
- The recoding is sound in itself. The test now measures the residual that Newton's own update drives down.
- `REGISTER_3.md`'s sentence stands as written. The dated notes at its foot correct its rationale and § 1's row.

## For Target 1's registration

**The margin is thinner than these controls show.** M8.15's committed records on `main`:
- **A control.** C2b/R2 at level 2, `ε = 11.31`, reaches `9.22×10⁻¹²`, only 1.08 times below the tolerance.
- **Inside Target 1's brackets.** T2/R4 at level 3, `ε = 16`, the lower end of its bracket: `8.04×10⁻¹²`, a factor of 1.24.
- **Elsewhere among the targets:**
  - T5/R2 at level 3, `ε = 5.66`: `9.72×10⁻¹²`, a factor of 1.03;
  - T2/R5 at level 2, `ε = 22.63`: `8.99×10⁻¹²`, a factor of 1.11.
- **What they may support.** The control's figure can ground Target 1's rule. The target figures only locate where the margin bites, because target records never justify a rule.

**What a floor-caused failure does now.** A bisection midpoint whose solve cannot get below `10⁻¹¹` returns no state. `bisect` in `m815_branch.py` then records "continuation failed inside the bracket" and stops. That end is visible, but it ends the location.

**Target 1's registration chooses one of these before it runs:**
1. **A reading rule.** A solve that stalls at the floor is reported as Unresolved (residual floor), with its residual history.
2. **A stopping test scaled to the residual's own size:** `‖Kr x‖ + σ‖Mr x‖` plus the nonlinear term. That is an instrument change, and it would need its own qualification.

Either rests on control evidence: `diag_residual` and C2b/R2. A review unit prefers the first: the qualified stopping test, with explicit Unresolved reporting.

**Fixed for Target 1, whichever it picks:**
- a failed solve is recorded as unresolved continuation or bisection, and never turned into a claimed change of type;
- the tolerance is never relaxed on the strength of a target's records.

**Not covered here** (§ 5):
- the bisection's change-of-type logic and the guard offsets;
- a crash in a full run.

Target 1 needs pre-registered, armed non-target or synthetic tests for these before it runs. The branch reruns still count: they establish that the inherited driver reproduces its frozen outputs.

## Ahead of the freeze

- **The imports, checked on a copy of the solver folder without `cluster_rule.py`.**
  - All 17 modules import cleanly.
  - `cluster_rule` is never loaded, and nothing loads from outside the copy.
  - No file in the solver folder names `cluster_rule`. Only control 2a's harnesses do.
  - The registered check repeats this in the frozen folder.
- **The hashes.** The 18 files match `QUALIFICATION.json` now. The registered check repeats this against the new manifest.

## Next

1. **On the maintainer's go, the freeze of § 8, as amended.**
   - The revised solver goes in a folder of its own, with its own manifest and `SHA256SUMS`: `angle.py` in, `cluster_rule.py` out, and `theoremD_L3.json` filed with it.
   - Both checks run there: the hashes against `QUALIFICATION.json`, and the imports without `cluster_rule.py`.
   - M8.15's folder stays as it is.
2. **Then Target 1's pre-registration,** carrying the items above.
3. **Then the revised solver's guard file,** once Target 1's terms are frozen on `main` and their SHA-256 recorded, before any target run.

*v1 written 2026-10-09T19:50Z, after the run; v2 2026-10-09T20:26Z; v3 2026-10-09T20:55Z.*
