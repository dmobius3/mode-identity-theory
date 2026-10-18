# M8.16: the separation rule's tests, a plan (2026-10-17)

`DESIGN.md` §10.2 states the rule: a point's classification is converged only if its eigenvalues' uncertainty sits at most a tenth of their distance to the nearest type-changing event. It also requires the rule and its factor to be "tested on the disclosed controls and on synthetic counterexamples, with mutation arms that must fail it, before the qualification's criteria freeze (UA)". It is the last test of the instrument still open on entry 113's pre-freeze list (entry 148). Blake's decision (2026-10-17): it comes before the registration draft.

Before this plan, no code applied the rule. D7's closure read it as an analysis, on the recorded changes and margins (entry 113).

**Status (2026-10-17): closed.** Both units confirmed the set rule and its tests on the v3 packet, and the separation gate is closed (DEVLOG 180). UB's wording on when a set forms is folded (entry 179).

## The rule as written (§10.2)

- **Structure.** The type, n(L), K, V₀ and each imaginary group's negative-sign count are unchanged between the two highest N, and the same along the ladder.
- **Which eigenvalues.** Each eigenvalue the record types: the slow band, and any mode of the next level near zero at a window's top. Each is matched across the two highest N.
- **Its uncertainty,** the largest of:
  - its change, read as the remaining error from the geometric rate where three cutoffs exist, and as the last change otherwise;
  - the larger margin of the two compared records;
  - a greater uncertainty implied by numerical residuals or spectral sensitivity. Where that cannot be adequately controlled, the comparison is Unresolved (UA).
- **The events:** the cluster's gray zone; the imaginary axis, for an eigenvalue off it; the nearest imaginary eigenvalue of opposite Krein sign, for an imaginary one.
- **The test:** the uncertainty at most a tenth of the distance to the nearest event. Where the separation cannot be shown or computed, the point is Unresolved. Each eigenvalue's estimate is reported beside it, unscored.

## The rule as an algorithm (proposed; four choices flagged)

1. **Structure first,** as D7 ran it.
2. **The tested groups (choice 1).** Every group the record types (real, imaginary or complex, outside the gray zone) with |λ| below half the band edge, Λ = √(n₁(n₁ + 2)) − √λ. Here n₁ is the slot's lowest level above the lower of the two compared cutoffs.
   - Below Λ every free mode at the higher cutoff has one at the lower, so each group there can be matched. This takes in the slow band and the next level's mode near zero, which §10.2 names.
   - Every Krein-negative imaginary group, and every off-axis group, is tested wherever it lies, since these carry the type. A Krein-positive group above Λ/2, far from zero, can change the type only by meeting a Krein-negative one. So the nearest opposite-sign group of every tested imaginary group is tested too, wherever it lies, against the same distance; if it cannot be matched, the point is Unresolved (UB).
   - On a synthetic ladder, whose size does not change with N, every typed group is tested.
3. **Matching.** Each tested group is matched to the nearest group of its class at the lower cutoff: real; imaginary of the same Krein sign; complex. With three cutoffs, that one is matched again to the cutoff below it. A match counts only if the next nearest is at least twice as far. A tested group without one makes the point Unresolved.
4. **The uncertainty U,** the largest of:
   - **the remaining error:** with three cutoffs, d₂²/(d₁ − d₂) where d₂ < d₁ (d₁ and d₂ the last two changes); with two, the last change d₂;
   - **non-contracting (choice 2):** where d₂ ≥ d₁ and d₂ exceeds the floor, no rate is shown, and the point is Unresolved. At or below the floor, the floor stands;
   - **the floor:** the larger margin of the two highest cutoffs;
   - **the numerical estimate (choice 3):** ‖P_g‖ max(‖R_g‖, u‖A‖) at each of the two highest cutoffs, with P_g the group's spectral projector and R_g its residual. It needs no second eigendecomposition. Since AᵀW = −WA, W x at −λ̄ is a left eigenvector at λ, so P_g comes from the record's own right eigenvectors (DERIVED).
5. **The distance d,** at the highest cutoff: the smallest of |λ| − G margins (the gray zone's top); |Re λ| for an off-axis group (the imaginary axis); and, for an imaginary group, the distance to the nearest imaginary group of opposite Krein sign.
6. **The verdict.** Separated if U ≤ d/10 for every tested group, and converged if, besides, the structure holds. Otherwise Unresolved, naming the failing group, its U, its d and its event. Each tested group's U and d are reported beside it.

## The controls: the survey (`dev/sep_survey.py`; an analysis of records, no run)

The rule's record-only terms, on D7's sample and ladders, at §7's calibration:
- **65 points** (9 in the sample, 56 on the ladders), every one separated. The smallest ratio of distance to uncertainty is 1.21×10³ (C2a, ε = 0.25, N = 24 and 32), where the floor binds.
- **The change binds at 8 mid-ladder points,** the smallest at 1.4×10³ (C3, ε = 32). No three-cutoff sequence is non-contracting.
- **No Krein-negative imaginary group** appears in C2a's or C2b's records. So their only event is the gray zone, and C3's real pairs meet the gray zone before the axis.
- **So the factor of a tenth has about two decades of headroom** on the controls' slow bands. D7's closure read 30.5 at C2a's smallest point against the margin before §7's recalibration.
- **Not in the records,** so not read:
  - the residuals and sensitivities (entry 113's limitation 7);
  - the next level's near-zero modes at the ladders' tops (its limitation 2).

## The synthetic counterexamples: the scout (`dev/sep_scout.py`, entry 149; reported, unscored)

Each family is a ladder in N: four cutoffs, N = 16 to 40, with one parameter converging as N grows, and its limit. It is built on `dl_recal.py`'s Elliptic family with one block added, at m = 0.2. Each counterexample reads its finite-N type at all four cutoffs, at all 3 mixings, so no single cutoff can see it. The ratios are derived from exact roots.

| Family | What converges | At the cutoffs | In the limit | Binding event | Ratio |
|---|---|---|---|---|---|
| P | an S1+ pair near 10⁻³ | Elliptic | Elliptic | the gray zone | 1.82×10³ |
| P′ | an S1r real pair near 10⁻³ | Hyperbolic | Hyperbolic | the gray zone | 1.82×10³ |
| PK | UB's collision block, its pairs 9×10⁻³ apart | Elliptic | Elliptic | the opposite sign | 1.28×10³ |
| Z | a soft-soft pair, through zero | Elliptic | Hyperbolic | the gray zone | 0.758 |
| K | the collision block, into a quartet | Elliptic | Hyperbolic | the opposite sign | 0.382 |
| X | the collision block, out of a quartet | Hyperbolic | Elliptic | the axis | 0.78 |
| R | K at a slow geometric rate, 0.95 a step | Elliptic | Hyperbolic | the opposite sign | 1.33 |
| F | Z with a slow second rate under a fast one | Elliptic | Hyperbolic | the gray zone | 2 |

- **P, P′ and PK** are converged controls: separated, with the right type.
- **Z, K, X, R and F** read a type at every cutoff that their limit does not have. The rule must leave each Unresolved, never converged with that type.
- **What each one isolates:**
  - R's last change, 3.95×10⁻⁵, is under a tenth of its distance, 10⁻³, while its remaining error, 7.5×10⁻⁴, is not. Only the geometric reading catches it.
  - F's remaining error, 7.23×10⁻⁹, is far under the floor, 5.5×10⁻⁷. Only the floor catches it.
  - R and F sit between 1 and 10, so a factor of 1 passes both.
  - F is caught by the floor because its pair sits within ten floors of the gray zone; at 15 margins the same family reads converged with its finite-N type, and R does too with only two cutoffs. A slow rate under a faster one is beyond any reading of a few cutoffs: the rule rests on the leading rate dominating at the highest cutoffs. The controls' measured rates, at most 0.033 over the 39 three-cutoff sequences at the ladders' tops, place the instrument's systems far from that regime, and the two-cutoff reading is safe there (UB; the count as checked here, flagged to UB).

## The scored test (Step 2, after your review)

- **`instrument/convergence.py`:** the rule as above, with each arm as a parameter. The record also returns its eigenvectors and groups; no reading changes.
- **`dev/sep_claims.py`,** synthetic, 10 mixings a family, each outcome derived before the run from exact roots:
  - P, P′ and PK converged, with their types;
  - Z, K, X, R and F Unresolved, each naming its event;
  - the arms, each red:
    - (a) a factor of 1, where R and F read converged with the wrong type;
    - (b) the last change in place of the remaining error: R;
    - (c) no floor: F;
    - (d) no gray-zone event: Z and F;
    - (e) no axis event: X;
    - (f) no Krein event: K and R;
    - (g) no numerical estimate: `convergence.py` on constructed group data, a converged sequence whose ‖P_g‖ u‖A‖ is set above a tenth of its distance. With the estimate, Unresolved; without it, converged. No natural system makes the estimate bind first, so the logic is tested at the module (UB).
- **The controls:**
  - the survey's 65 points, as above;
  - one cheap run with the rule in full (choice 4): D7's sample at N = 16 and 24, the regression set, about 4 minutes; or with N = 32 too, for three cutoffs, about 35 minutes. It is your call and Blake's on cost; no ladder is rerun.

## What the plan does not do

- No reading of the record changes, nor §7's calibration, nor the drivers' scoring. The rule is a new module, which the qualification's driver calls once the registration is reviewed.
- The factor is not tuned on these results. The controls' headroom and the counterexamples' ratios are reported, and it stays a tenth unless you rule otherwise.
- No pyramid, no census target, no qualification run and no filing. Nothing sealed is touched.

## Questions for you

1. **The tested groups (choice 1):** as proposed, or §10.2's narrower slow band and next level, with another operational definition.
2. **Non-contracting sequences above the floor (choice 2):** Unresolved, as proposed, or read by the last change.
3. **The numerical estimate (choice 3),** through the Hamiltonian pairing. Its arm can be wiring only: no natural construction made it bind. In a scratch check, an ill-conditioned congruence (condition 10² to 10⁵) drove the record Unresolved through its own Krein, V₀ and margin checks first. On the instrument's systems, ‖P_g‖ u‖A‖ stays far below the floor.
4. **The controls' run (choice 4):** N = 16 and 24, or with N = 32, or the records only.
5. **Anything missing** from the families or the arms.

## The units' rulings on the plan (2026-10-17)

- **Both units CONFIRM the survey and the scout.** UA reran both byte-identical, with the hashes matching DEVLOG 149 and 150; UB reproduced them under python3 -I. The factor stays a tenth, an operational adequacy test, not a rigorous bound on every spectral error (UA).
- **UA: a conditional GO to Step 2,** with three bounded requirements:
  - **Matching, one to one:** a unique, bidirectional match, with compatible size and Krein signature. Missing, duplicated or ambiguous partners read Unresolved. The band edge is a matching domain only: a required group that cannot be matched reads Unresolved, never omitted.
  - **A non-contracting counterexample:** d₂ ≥ d₁ above the floor, with a misleading finite-cutoff type. The rule reads it Unresolved, and an arm that ignores non-contraction accepts it.
  - **The projector validated:** the pairing, the normalization and the residual verified, and Unresolved where the projector is singular or unusable. One small analytic projector test. No claim that the control survey validates the sensitivity.
  - **The control run:** D7's sample at N = 16, 24 and 32, about 35 minutes. Once the cheap tests and this run pass review, the separation gate closes and the registration draft follows. This is the last instrument-development check unless it exposes a concrete defect.
- **UB: KEEP the algorithm,** with three changes, folded above:
  - the partner tested too (choice 1), with a new family, K′;
  - arm (g) made red at the module;
  - the rule's rate assumption stated, with F at 15 margins reported.
  - The events are complete: every route to a type change passes through the gray zone, the axis or an opposite-sign meeting, and n(L) and n(D) change only through an eigenvalue of A crossing zero (UB).
  - The control run: D7's sample and the ladders at N = 16 and 24, the ladders read at their tops for the next level's mode near zero, and not N = 32.
- **Checked here.**
  - UB's pairing derivation agrees with the plan's.
  - UB's rates: at the ladders' tops, ρ = d₂/d₁ is at most 0.0331 over 39 three-cutoff sequences. In the sample, N = 16 to 32 gives at most 5.9×10⁻⁵, and the N = 24 to 40 changes sit at round-off: the largest ρ there, 0.067, is a change of 1.5×10⁻¹⁵. UB counted 64 sequences; the sentence folded above carries the count checked here, flagged to UB.
- **The control run, Blake's decision (2026-10-17):** both, about an hour, after the synthetic claims pass: UA's sample at N = 16, 24 and 32, and UB's ladders at N = 16 and 24 to their tops. Each covers a case the other does not; flagged to both units.

## Step 2 as built (2026-10-17)

- **`instrument/convergence.py`:** the rule, with each arm as a parameter: `factor_one`, `last_change`, `contract_ignored`, `no_floor`, `no_numerical`, `no_gray`, `no_axis`, `no_krein` and `no_partner`.
  - `projector()` reads ‖P_g‖ from the record's right eigenvectors through the pairing. It is usable only if the group's eigenvectors span it, by the record's own test (no singular value below 10⁻⁶ of the largest), the left vectors' residual is at round-off, Yᴴ X is well conditioned, and M is inverted to working accuracy (P X = X, which holds by construction, read numerically); the left residual is what verifies the pairing (UB).
  - An unlogged check on a near-collision (δ = 10⁻¹⁴) found that Yᴴ X's conditioning alone does not flag a defective group: it read 1.0000003. The span test was added before any scored run.
  - `match()` is UA's one-to-one rule; `separation()` the rest, with UB's partner.
- **`instrument/linear.py`:** the record also returns its eigenvectors and its groups. No reading changes; DL and `dl_recal.py` rerun to show it.
- **`dev/sep_claims.py`:** the scored synthetic claims, derived from exact roots and printed before any record is read:
  - 1, the analytic projector (UA), and a projector that is not usable reading Unresolved;
  - 2 and 3, the eight families of the scout, with N (UA) and K′ (UB) added, F15 and R2 reported;
  - 4, nine arms, (a) to (i), each red.
  - **K′ is two modes joined by a weak conjugate coupling,** c = 10⁻⁴. A single block cannot hold one root while its partner meets it: holding a root fixed makes the meeting a tangency, with no quartet. Its ladder steps by 3, which keeps each match unique against the oscillator at 0.0357; at steps of 4, an unlogged off-grid check found the partner's lowest match ambiguous, which the rule correctly refused.
- **`dev/sep_controls.py`:** the control run, `--sample` (N = 16, 24 and 32) and `--ladders` (N = 16 and 24 to the tops). On one off-sample point (C2a, N = 16, ε = 0.75; unlogged), all 98 typed groups' projectors were usable, ‖P_g‖ from 1.0 to 7.1, and the numerical estimate stayed five decades under the margin.

## Step 2's results (2026-10-17, DEVLOG 152 to 164; for the units)

**The synthetic claims pass (entry 158), after one correction.**
- **Entry 154 failed one item,** arm (c), and that FAIL stands. As coded, the arm took away both of the floor's jobs: the smallest uncertainty, and the threshold below which a non-contracting sequence is round-off. Its derivation took away only the first. With the threshold at zero, about half of a converged point's unchanged groups read non-contracting at round-off. The arm now drops the floor from U only (entry 155), and the rule is unchanged. So the threshold is needed, which bears out choice 2.
- **Entry 158:**
  - the analytic projector to round-off, with the defective group at UB's exact collision not usable;
  - P, P′ and PK converged at 10 of 10;
  - Z, K, X, R, F, N and K′ Unresolved at 10 of 10;
  - all nine arms red, each at 10 of 10;
  - F15 and R2 converged with their finite-N types: the rule's stated limit.
- **No reading of the record changed.** DL is byte-identical to entry 93's (152 and 156), and `dl_recal.py`'s output identical to entry 145's (153 and 157).
- **The numerical estimate reached 5.6×10⁻⁷** on K's near-collision pairs, whose ‖P_g‖ is 1.4×10⁶ at a separation of 10⁻³. That is as large as the floor, but it did not bind, since a tenth of their distance is 10⁻⁴.

**The controls (entries 159 to 164, about 78 minutes on battery).**
- **The sample** (N = 16, 24 and 32; UA): C2b and C3 converged at 3 of 3. **C2a FAILS: converged at 2 of 3,** and that FAIL stands.
  - At ε = 2, two tested Krein-positive groups near 4.039, 2.4×10⁻⁴ apart, have no unique, bidirectional match at the lower cutoffs, so the point reads Unresolved.
  - Its slow band clears there at a ratio of 3.3×10³. The sample claim's derivation read only the slow band, from D7's records.
- **The ladders** (N = 16 and 24, to the tops; UB): no point converges with a wrong type, for all three (the claim). Reported: C2a converges at 6 of 18 points, C2b at 10 of 20, C3 at 15 of 18.
  - **Matching** makes C2a Unresolved from ε = 2 and C2b from ε = 8: Krein-positive groups too close together for their change between N = 16 and 24.
  - **Separation** fails at the tops, C2a at ε = 64 and 72, and C2b and C3 from 45. There the change between N = 16 and 24 is several percent of the eigenvalue, so the ratios fall to 5 to 10. At the registered cutoffs, 24, 32 and 40, D7's records give ratios of about 3×10⁴ at the same tops (the survey).
  - **The tested group nearest zero at each top was read:** at C2a, 0.045 to 0.051, separated at ratios 43 to 55; at C2b and C3, 0.25 to 0.39, at 5.6 to 8.8. The driver does not identify which group, if any, is the next level's mode, so these values are not claimed as it.
- **The numerical estimate on the controls** stayed at 1.1×10⁻¹³ to 1.2×10⁻¹², five or more decades under the floor. This is a measurement of the term's size on these operators, not a validation of the sensitivity (UA).

**The finding, for your ruling.**
- One-to-one matching (UA) makes a converged control read Unresolved wherever groups of one class and one Krein sign sit closer than their change across N. Such groups cannot change the type among themselves: Krein-positive imaginary groups that meet stay on the axis, and real or complex groups that meet stay off it, with K unchanged.
- **A proposal, not implemented:** where a tested group's match is ambiguous only among groups of its own class and sign, match that set as a whole, by its count, and test its extent against its events. Any ambiguity across class or sign, any missing partner, and any count that differs between cutoffs stays Unresolved.
- Until you rule, the rule stands as built, and the C2a FAIL stands.

## The units' rulings on Step 2, and the set rule (2026-10-17)

- **Both units CONFIRM** the implementation, the claims, entry 154's FAIL with its correction (the arm's scope, not the rule), and the control runs as reported. C2a's FAIL stands as the strictness of the rule as built. UA and UB each reran `sep_claims.py` under python3 -I: 0 failed.
- **UB's 64 sequences, reconciled:** 39 at the ladders' tops (ρ at most 0.0331), plus 25 in the sample at N = 24, 32 and 40 whose change from 24 to 32 sits above 10⁻¹¹, the noise in those records (ρ at most 5×10⁻⁴). The folded sentence stands as accurate (UB).
- **UB's wording fix,** folded above and in `projector()`: P X = X holds by construction; the left residual verifies the pairing.
- **The set rule, adopted by both (UA's four properties, UB's definition), merged here:**
  - **When:** a tested group's one-to-one match fails, and it has candidates of its own class and Krein sign, of any size. Its set is the group and its competitors, within twice the nearest candidate's distance, closed under that test at every cutoff used, its count taken with multiplicity (UB's wording, after the v3 review).
  - **Counts:** the set matches only if its total count agrees at every cutoff. A missing candidate, or a changed count, is Unresolved; no member is dropped.
  - **Change:** the bottleneck distance between the sets of centres, the least over one-to-one assignments of the largest displacement (UA). It is never smaller than the Hausdorff distance (UB's measure), so UB's argument holds: distance to an event is 1-Lipschitz in the set, so a set that clears its events has no member that can reach one. Read by the group rule: remaining error, floor, non-contraction.
  - **Distance:** the nearest member's, to each event (UA, UB). The partner rule applies to that member's opposite-sign neighbour (UB).
  - **Numerical estimate:** the largest member's, every member's projector usable; otherwise Unresolved (UA).
  - **The bottleneck is UA's measure,** chosen over UB's Hausdorff distance because it keeps multiplicity. Flagged to UB.
- **The new tests,** derived before the run:
  - **M,** the harmless permutation (UA, UB): two Krein-positive pairs that exchange order between cutoffs, converging far from every event. Converged.
  - **M′,** the dangerous approach (UA, UB): two Krein-positive pairs about a fixed centre, the lower converging onto a Krein-negative pair. Unresolved.
  - **Arm (j),** the set's change read at its centroid (UB): M′ reads converged with its finite-N type.
  - Each S1+ block's fast pair sits at exactly 2ω + f, so in M and M′ the fast pairs form a mirror set with the same steps. An unlogged off-grid check showed it.
  - **All nine original arms are rerun,** and must stay red (UA).
- **The control rerun, Blake's decision (2026-10-17):** targeted, about 33 minutes: C2a's sample and the C2a and C2b ladders. These are every reading that failed on unique matching, and so every reading the set rule can change. The C2b and C3 samples and C3's ladders matched uniquely everywhere, so their readings cannot change. UA asked for C2a's sample only, and UB for all six runs; flagged to both. Each run saves its summaries (UB).
  - **C2a at ε = 2, derived:** its two groups near 4.039 form one Krein-positive set. C2a has no Krein-negative group, so the set's only event is the gray zone, about 4.04 away; it converges if the set's uncertainty is under 0.40 (UB).
- **To keep in the registration (UA):**
  - the two-cutoff limitation and F15's false confidence: a slow rate hidden under a faster one is beyond any reading of a few cutoffs;
  - the upper-window runs did not identify every next-level near-zero mode. The qualification's coverage and Unresolved rules must not omit a required mode; every group below half the band edge is tested (UB).
- **The gate closes (UA, UB)** when the set rule passes M, M′ and arm (j), all nine original arms stay red, C2a's sample no longer reads Unresolved only for same-sign exchange, and the ladders keep no wrong type. If C2a fails for a genuine separation reason, that FAIL stands, with no further recalibration (UA).

## The set rule's results (2026-10-17, DEVLOG 166 to 172; for the units)

**The synthetic claims pass (entry 169), 0 failed.**
- The analytic projector, as before.
- P, P′, PK and M converged at 10 of 10. M's set, two Krein-positive pairs that exchange order, has U = 10⁻³ against a distance of 0.149.
- Z, K, X, R, F, N, K′ and M′ Unresolved at 10 of 10. M′'s sets do not contract.
- All ten arms red, each at 10 of 10: the nine original and (j), the set's change at its centroid, where M′ reads converged with its finite-N type.
- DL is byte-identical to entry 93's (167), and `dl_recal.py`'s output identical to entry 145's (168).

**The targeted control rerun (entries 170 to 172), about 33 minutes.**
- **C2a's sample: PASS, converged at 3 of 3.** At ε = 2, the two Krein-positive groups near 4.039 form one set. Its change falls from 1.6×10⁻⁴ to 1.7×10⁻¹⁰ across the cutoffs, so its uncertainty is the floor, 1.4×10⁻⁶, against the gray zone 4.04 away: a ratio of 3×10⁶, as derived (under 0.40). The original FAIL, entry 159, stays on record.
- **The ladders keep no wrong type** (the claim, PASS for both). C2a converges at 12 of 18 points (6 before), and C2b at 14 of 20 (10 before).
- **What still reads Unresolved:**
  - **a set whose count differs between N = 16 and 24** (C2a at ε = 4, 5.66, 32 and 45; C2b at 16, 90.5, 128 and 132): another group joins the competitors at one cutoff. Both units required a changed count to read Unresolved;
  - **separation at the tops,** where the change between N = 16 and 24 gives ratios below 10, as before.
- **Not rerun, since their readings cannot change:** the C2b and C3 samples (3 of 3 each) and C3's ladders (no wrong type), entries 160, 161 and 164. They matched uniquely everywhere.
- **Saved this time:** each point's summary and the basis's levels, so the rule can be read again without a solve (UB).

**The gate's conditions (UA, UB), all met:**
- the set rule passes M, M′ and arm (j);
- all nine original arms stay red;
- C2a's sample no longer reads Unresolved for same-sign exchange;
- the ladders keep no wrong type.

The gate closes on your review (UA).

## The units' rulings on the set rule: the gate is closed (2026-10-17)

- **Both units CONFIRM** the set rule as built, its claims, the targeted rerun and its scope, and `DESIGN.md` v2.16. The separation gate is closed (DEVLOG 180).
- **UA:**
  - reran `sep_claims.py`, byte-identical, with 0 failed, and checked the bottleneck matcher against an exhaustive search over assignments in small cases;
  - confirms the four properties, M, M′, the nine original arms and arm (j), C2a's sample at 3 of 3, and the ladders' safety. Entry 159's FAIL and the remaining upper-window Unresolved readings stay on record;
  - keeps the limits explicit for the registration: a hidden slow rate can defeat a few-cutoff estimate, and the upper-window runs did not establish coverage of every next-level mode near zero. The scored qualification must enforce the declared coverage and Unresolved rules;
  - gives a GO to draft the M8.16 qualification registration. Every sealed case HOLDs until the registration is reviewed, frozen and filed. The registration review settles the Newton acceptance and frozen-allowlist contracts, as documentation and enforcement, not a new development campaign. The #512 admission restriction is unchanged, and no pyramid, census target or scored qualification run is authorized.
- **UB:**
  - re-read all 41 control verdicts from the saved summaries, each as shipped, and finds the targeted scope complete;
  - confirms the bottleneck merge: never smaller than the Hausdorff distance, with multiplicity kept;
  - asked for one wording change, folded (DEVLOG 179): a set forms whenever a group's one-to-one match fails and it has candidates of its own class and Krein sign, of any size.
- **Checked here:** the re-read is logged (DEVLOG 177 and 178): 41 of 41 verdicts as shipped, under `convergence.py` as it now is.
