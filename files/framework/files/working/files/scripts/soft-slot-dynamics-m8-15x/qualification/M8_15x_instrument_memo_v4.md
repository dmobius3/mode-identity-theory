# M8.15.x: the instrument revision (scope memo v4, final for code, 2026-10-08)

> Landing copy, 2026-10-11. Apart from this note, the only change from the original is that its two-letter labels for the two independent reviews read Review A and Review B, at every occurrence. Reversing that gives back the original, whose SHA-256 is `28f35a938c94984fb7414f473303899474db78065a10a62f176e39a7da752d18`.

The aim is one qualified instrument that every M8.15 follow-up inherits. This is bench and instrument scope, not a target pre-registration. It is drafted against MIT `bec578d`: the solver frozen at `6058f95`, and the run's record at `28c8a76`. The adjudication it follows is OpenWave #620 (`f231bf04`).

v4 folds both units' reviews of v3. Both accepted § 8's two calls, and both rated the remaining fixes contract completion, so this version is frozen for code.

## Ground rules

1. **Repairs.** The instrument's existing behaviour changes only where one of these shows a defect or a contract mismatch:
   - M8.15's record;
   - #620;
   - a shipped bench check.
2. **Estimator upgrades.** A new estimator or bound enters only through controls built on orbits that are not targets. Its rules are frozen before any target runs, and it is never justified by M8.15's target outcomes. Three boundaries stay separate:
   - the ratified repair (§ 1a);
   - the unratified T1 diagnosis (§ 2);
   - any new estimator (§ 3, deferred).
3. **Controls.**
   - Every new control is an orbit that is not a target.
   - Its expected pass or fail is registered before it runs.
   - Running the solver on a target before the freeze is target output, and is not allowed.
4. **Disclosure.** The terms will state everything this follow-up has already seen:
   - every M8.15 target record, T1's 4.99% and 5.3% among them;
   - T4's post-run diagnostics, including the level-2 bench check at T4's slice-constrained point.

   No rule may be justified by reference to any of them.
5. **Regression.** Before the closing controls (C1, C2a, C2b, C3) are rerun, the memo lists every output field allowed to change and every field that must reproduce bit for bit.

Each section answers four questions: what failed, what changes, which armed control catches a regression, and what must pass before targets are legal.

## 1. Slices

### 1a. The stopping test: a ratified repair

**What failed.** The test leaves out the gauge multipliers. #620 ratified that mechanism.

**What changes.** The test includes every multiplier, and `μ` and `ν` are recorded.

**The armed control.**
- **1a.** A non-target slice control with nonzero phase overlap and nonzero slice force. The old test must stall on it, and the new one must pass.

### 1b. The slice-constrained point is not a standing wave (T4)

This finding comes from a shipped bench check; #620 did not ratify it.

**What failed.** At T4/R4's slice-constrained point at level 2, `|F₀|/|Mx| = 7.21×10⁻⁵`. It is the vector sum of a slice term of `7.28×10⁻⁵` and a phase term of `8.93×10⁻⁶`, and both units reproduced it. That point is not a discrete standing wave:
- the persistence reference is not exactly stationary;
- the linearization is taken about a point that is not critical.

The reference's drift is measured in qualification, on a control.

**What changes.**
- **Solve for the true discrete critical point on the lifted circle.** The rotation angle about the pinned axis becomes an unknown, and the slice force must vanish: `ν(θ) = 0`.
- **The selection rule (decision 1).**
  - The point that counts is the energy minimum on the discrete lifted circle, at fixed `N`.
  - It is found by a frozen grid in `θ` followed by a root-solve of `ν(θ) = 0`, by the same rule at both levels.
  - Minima related by a mesh symmetry count as one.
  - Inequivalent minima that fall within a frozen energy tolerance of each other are all recorded.
- **The angle is an unknown at every continuation step,** carried from the previous accepted point. The selected minimum is tracked continuously. If it stops being the energy minimum along the branch, that is recorded, never re-selected.
- **At such a point `μ = 0` too,** so even the old stopping test passes there. The critical point is what fixes T4. § 1a guards every other use of a slice.
- **Controls only, first.** The angle solve is developed and qualified on controls only, and T4 is first solved under the frozen terms.

**The armed control.**
- **1b.** A non-target control whose critical points on the circle are fixed by symmetry, with the solve started off the symmetric angle. At C3s's oriented seed `ν` is already `2×10⁻¹⁴`, so starting there would test nothing.

**What must pass first.**
- 1b's solve lands on the expected critical points, with `ν` at round-off.
- A level-2 reference run on 1b holds `d_ref ≤ η` over `T`.

## 2. The cluster classification (T1 and T4; Target 1 inherits it)

**The status.** The 0.9 overlap rule's treatment of T1's Krein-negative mode is unresolved. #620 confirmed the facts and did not ratify the claim.

**The rule.** A replacement becomes part of the instrument only if an armed non-target control (2a) shows the old rule failing.

**The evidence so far.** These are an independent review's continuum figures; its scripts ship as checkers.
- **T1:** `v₂`'s Krein-negative mode overlaps the rotations alone at 0.968, and the fibre and phase-partner directions at 0.000.
- **T4:** the third outside orbit's smallest mode overlaps the rotations alone at 0.996, and its next at 0.870.

**What changes.**
- **The candidate rule: decision 2, tracking anchored to the theorem.**
  - **The initial matching is frozen.** At a mode's first resolved point, a one-to-one assignment within each frozen Krein class matches the computed Hamiltonian blocks to the predicted multiset, by minimum total relative modulus.
  - **Every assigned block lies within 10%,** twice the 5% validity bar.
  - **An assignment that is not unique,** or whose separation from the next-best assignment falls below a frozen margin, is Unresolved.
  - **From then on the block, not any single eigenvector, is tracked** along `ε` by subspace continuity.
- **Candidate 3 is dropped.**
- **Refinement is a one-sided veto, never the primary test.** Both units tested a refinement-first rule and rejected it. Near a genuine zero crossing, a genuine mode's modulus legitimately changes with refinement: at T2/R4's `ε = 16` it shrinks 20% between levels. A refinement-first rule would pull that mode into `G`, so `n(B|G)` would absorb the index change that Target 1 is meant to locate.
- **The veto's calibration.** The control records give no single mesh-breaking rate. Between levels 2 and 3 the lifts shrink by:
  - 8.3 to 8.9 times (C2a, paired);
  - 58 times (C2b, paired);
  - 3.1 to 3.4 times (C3, radical).

  So the veto requires each nonzero lifted or rigid structural block in `G` to shrink by at least a frozen factor of 2 per level.
  - **Scope.** It applies only above the registered numerical-zero floor. The exact fibre and Jordan modes, which sit at round-off, are exempt.
  - **Why 2.** The factor sits below the radical rate: radical lifts shrink about 3.2 times per level, near the square root of the mesh splitting's 9.1 (terms line 169), and C3's 3.1 to 3.4 confirms it. A threshold at 3 would veto radical lifts shrinking exactly as theory says.
  - **What it still catches.** The factor sits above the convergence of genuine modes, which agree across levels to about 1% in the controls. So a genuine mode wrongly placed in `G` still trips it.
  - **Matching across levels.** Lifts are matched by sorted moduli within each kind, paired or radical.
  - **Failure** makes the point Unresolved.

**The paired-lift bound.** The current absolute `τ₀`, set from C1, C2a and C2b, stays for this revision unless an armed non-target control (2b) shows it inadequate. The reason for replacing it is T1/R4, which rule 4 forbids as justification.
- **The candidate replacement** is a separation test plus a refinement test:
  - below a frozen fraction of the smallest resolved predicted `|λ|` at that `ε`, as the radical bound does;
  - shrinking with refinement where both levels resolve the lift.
- **It enters only through 2b.** If no 2b qualifies it, T1 may remain blocked even with the classification repaired, and the memo says so openly.

**The armed controls.**
- **2a.** A genuine mode inside the structural span, on an orbit that is not a target.
  - **Rejected so far:**
    - T4's orbit is a target;
    - `v₀`, the coherent orbit and the octahedron have no genuine mode inside the span;
    - `v₁` is degenerate, so Theorem R gives it no known answer.
  - **The survey, before the memo freezes 2a:** the pyramid, the first two outside orbits and R2's orbits, in the continuum, using public spectra only.
- **2b.** A non-target orbit with a known paired structural lift, on which the candidate bound has a registered expected answer. It is needed only if the bound changes.

**What must pass first.**
- 2a's mode is classified genuine at every level where it is resolved.
- C1, C2a, C2b and C3 reproduce their classifications.
- 2b passes, if the bound changes.

**If 2a cannot be found or armed,** the new cluster rule does not qualify. The instrument then keeps the 0.9 rule, and T4 and T1 stay blocked. Target 1 can still run, because the review's continuum figures show:
- T3's genuine modes have zero overlap with the span;
- T2's slowest pair, the one that crosses zero, starts at 0.64.

So under the 0.9 rule, Target 1 records that pair's overlap at every bisection midpoint and guard offset, and any point where it reaches 0.9 is Unresolved.

## 3. Validity at `ε_min`: deferred

**The 5% bar stays for this revision:**
- #620 found no defect in it;
- the motivation for changing it was T1's outcome, which rule 4 forbids as justification;
- every valid M8.15 branch passed at 1.28% or better.

**Recorded for a later revision.** A convergence-based bar may enter only as an estimator upgrade under rule 2. It needs a non-target control that the 5% bar misjudges, and a ceiling: a mode whose estimated error exceeds a frozen cap is Unresolved, never valid. Review A's specification is kept for it:
- additive systematic bars, `E_tot = E_h + E_ε`, with `|λ̂ − λ_pred| ≤ 2 E_tot`;
- the spatial order frozen from controls, with Richardson extrapolation between levels 2 and 3;
- a frozen linear fit of `λ/ε` on the first three resolved ladder points;
- a planted under-resolved arm that must fail.

## 4. A record on every end

**What failed.** An empty level-3 ladder raised IndexError before the record was written.

**What changes.**
- **A branch end,** at the seed, a fold, a secant failure, a Newton failure or `ε_max`, writes the normal branch record with its end reason.
- **An instrument exception** writes a separate, machine-readable crash record: the last completed stage, a sanitized traceback with relative paths, and a nonzero exit status. It never poses as a scientific branch end.
- Both are written atomically.

**The armed control.**
- **4.** A forced seed failure on a control writes a branch record with its end reason, and a forced exception writes a crash record.

## 5. Observation times

**No change to the dynamics.** The terms state what the code does:
- observations come every `N_obs = round(1/dt)` steps;
- the run takes `N_step = round(T/dt)` steps, so it integrates to `T_int = N_step · dt`, the integer-step endpoint nearest `T`.

**What is recorded.**
- **The persistence summary** gains `N_obs`, `N_step` and `T_int`, listed under rule 5's allowed changes. It already carries `dt`.
- **The time series** already carry each observation time. They stay bit-identical, as regression evidence.

**The check.** A unit check of the recorded times against these formulas.

## 6. Qualification

1. **Register** the lists of changing and reproducing fields, and every new control's expected outcome.
2. **Rerun C1, C2a, C2b and C3.** Every gate passes, and everything outside the listed changes is bit-identical.
3. **Run 1a, 1b, 2a and 4,** plus 2b if the paired-lift bound changes, each against its registered outcome. Failing to find or arm 2a means the new cluster rule does not qualify (§ 2).
4. **The two self-tests also pass:**
   - § 5's observation-cadence unit test;
   - § 2's classifier tests: deterministic assignment, the ambiguity cases, and the refinement veto's self-test.
5. **Freeze as M8.15 did:** a manifest and `SHA256SUMS`, and the terms' hash on `main` before any target runs.

## 7. The targets, in order, after qualification

Every target inherits the whole qualified instrument.

### Target 1: locating the changes of type (T2/R4, T3/R5)

**The method.**
1. **Bisect at both levels.** At each midpoint, `n(L)` comes from the symmetric problem `L v = s M v`, and `n(B|G)` from the slow eigensolve and the cluster there.
2. **Find the crossing that counts.** Locate every relevant zero crossing of `L`, and use § 2's identity tracking to find the one that changes `n(L) − n(B|G)`. A difference of two integer indices does not supply a root by itself.
3. **Report the gap between the two levels' roots** as a cross-level shift, not as a discretization error, since § 3 is deferred.
4. **Confirm dynamically, which is mandatory.** Read the full Hamiltonian verdict at frozen guard offsets on each side, with the cross-level check.
5. **Name the result:**
   - If the verdict is Elliptic on one side and Hyperbolic on the other, it is a located change of type.
   - Otherwise: "an index crossing located; the change of type remains unresolved".

For the real-pair transitions M8.15 suggests, the candidate mechanism is a genuine zero crossing. Any quartet or nonzero-frequency collision found inside the bracket is recorded. Such a collision prevents the static crossing alone from being identified with the change of type.

**The brackets, from M8.15's record at level 3.** These readings are unscored, since `ε = 16` was Unresolved.

| Branch | Bracket in `ε` | `n(L)` | `n(B\|G)` | Genuine index `n(L) − n(B\|G)` |
|---|---|---|---|---|
| T2/R4 | 16 to 22.63 | 5 to 7 | 5 to 5 | 0 to 2 |
| T3/R5 | 11.31 to 16 | 12 to 9 | 6 to 5 | 6 to 4 |

**A secondary result, under its own label: an index jump inside the Hyperbolic range.**
- **Where:** T3/R5, between 22.63 and 32. Across it the genuine index falls from 4 to 3, with `k_i⁻` falling from 1 to 0 and `k_r` rising from 2 to 3. That endpoint bookkeeping is consistent with a Krein-negative imaginary pair crossing zero into a real pair. The locator tests whether the same tracked block makes that transition, and the stronger statement is made only if it does.
- **Method:** it is located the same way.
- **What it is not:** it carries no claim of a change of type or of persistence, and it cannot affect how the two primary results are scored.

### Target 2: T4

It needs §§ 1 and 2.

### Target 3: T1

It goes last, and its pre-registration has to face one fact openly. At `ε_min`, level 2 merges T1/R4's Krein-negative mode with the rotation lift into a quartet. So the classes disagree across levels under any classifier, and the lineage cannot start there.

## 8. Decisions

1. **Which critical point on T4's circle counts: the energy minimum on the circle at fixed `N`** (§ 1b). Both units accept this call, with Review A's earlier dissent answered as below. Two additions:
   - **The maximum's level-3 linear record** is registered as an unscored robustness diagnostic. It states in advance that a real lifted pair is expected there, and is not read as an instability of the branch.
   - **Minima related by a mesh symmetry count as one.** If two inequivalent minima fall within a frozen energy tolerance of each other, both are reported.

   **Review A dissents:** take the root nearest the registered oriented seed, by wrapped angle with a signed tie-break, with the extrema only as diagnostics. Review A's reason is that the minimum selects the orientation the artifact favours.

   **Why I side with Review B:**
   - the seed's angle about the axis comes from `orient()`'s convention, so the root nearest it is no less arbitrary;
   - the minimum is intrinsic to the mesh;
   - the artifact acts mainly along the lifted direction, which the count excludes;
   - the maximum's record measures any effect on the genuine modes, and that diagnostic is registered before the run.
2. **The cluster rule: tracking anchored to the theorem** (Review B's candidate 2, with Review A's frozen matching rule, § 2). Both units accept this call.
   - **The anchoring tolerance** is frozen at twice the validity bar, so the classification cannot force validity.
   - **The dimension and Ω-Gram checks** stay independent, so the dimension check keeps its power.
   - **Refinement** is the one-sided veto of § 2, and a merger or collision is Unresolved.

   **Review A dissents:** take a fixed-dimension Hamiltonian block by canonical overlap with the structural span, tracked in `ε`, with refinement as a cross-check. Review A's reason is that the theorem should stay outside the classification.

   **Why I side with Review B:** the blockwise rule would be Unresolved by construction at T4, whose smallest genuine mode overlaps the span at 0.996 against lifts near 1. The circularity concern is answered by the tolerance gap, by the independent checks, and by the terms' line 36: the run does not re-test the theorem.
3. **Validity:** deferred, keeping 5% (§ 3). Both units agree.
4. **Locating the changes of type:** as § 7 states. Both units agree.
5. **T3/R5 between 22.63 and 32:** included as a secondary result under its own label (§ 7). Both units agree.
6. **Observation times:** as § 5 states. Both units agree.
