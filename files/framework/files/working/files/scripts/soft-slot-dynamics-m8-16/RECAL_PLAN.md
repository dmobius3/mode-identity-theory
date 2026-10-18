# M8.16: §7's recalibration (2026-10-16; the units' conditions folded, and implemented)

`DESIGN.md` §7 asks for this before the freeze. The zero cluster's margin, its gray zone and the symmetry-leak bound are recalibrated on the controls' measured clusters and gaps. The record must resolve a slow pair below 1.04×10⁻⁵ at N = 40, M8.15's level-3 cluster tolerance, with the controls' largest cluster eigenvalue, at comparable amplitude, at least ten times below its gray zone. The margin scales with amplitude if needed. The leak is read against u‖A‖/gap. DL gains an arm at each (UB).

The proposal is built from the shipped records only: `dev/recal_survey.py` reads every recorded control point and solves nothing, and its output is `dev/recal_survey.out`. Both units confirmed the survey, and gave a provisional GO to κ, m₀, G and κ_L. Two changes are folded below: a scale-aware tolerance for nonzero groups (UB), and the drivers and DL reading the production classifier (UA). Both units then accepted the constants as the development calibration: UA as the pre-freeze baseline, and UB as provisional until the slow-pair demonstration (DEVLOG 126). Claim 1′, UB's check at m = 21, missed the ten-fold headroom UB first set for it at 2 of 40 mixings, though every mixing classified as derived. Both units keep κ = 2 and read that headroom on the controls. Claim 1′ stays as written and as failed, reported unscored, and claim 1″ scores the classification (below). `DESIGN.md` §7 carries the constants, from v2.12.

## What the records show

169 control points: D6's C1 (12), D7's sample (36) and D7's ladders (121), at N = 16 to 40, with m = ‖φ‖² from 0.204 to 132.

- **Today the record cannot meet §7's requirement.**
  - The margin is 30 √(u‖A‖), from 5.2×10⁻⁶ to 1.9×10⁻⁵, and the gray zone is (margin/10, 10 margins).
  - The smallest slow pair it can resolve is 10 margins: 1.8×10⁻⁴ to 1.9×10⁻⁴ at N = 40.
  - So a pair below 1.04×10⁻⁵ lies in the gray zone at every point, and is Unresolved.
- **The cluster scales with amplitude.**
  - Against √(u‖A‖), the cluster's largest eigenvalue spans 0.0028 to 0.625, a spread of 226x.
  - Against √(u‖A‖ m), it spans 0.0020 to 0.0568, a spread of 29x.
  - Along each ladder the cluster grows about as m^0.5 to m^0.7, while √(u‖A‖) stays flat.
  - MOTIVATED, not derived: a Jordan chain of length two split by a perturbation δ opens as √(δ b), where b is the chain's coupling, which grows with the amplitude.
- **The leak tracks u‖A‖/gap,** at 0.08 to 19.2 times it, where the gap is the smallest |λ| outside the cluster (5.8×10⁻⁴ to 6.3). The fixed bound of 10⁻⁸ is the wrong shape for the census's hard cases: at the controls' largest ratio, it would fail any gap below 7.4×10⁻⁴.

## The proposal

- **The margin:** κ √(u‖A‖ max(m, m₀)), with κ = 2 and m₀ = 0.2, the controls' smallest m. It sets the zero cluster and its gray zone. Nonzero groups are linked, and typed off the axis, against max(margin, κ_d √(u‖A‖ |λ|)), with κ_d = 10: a defective eigenvalue splits on the scale √(u‖A‖ |λ|), measured at 0.14 to 0.68 of it at a collision near 36i, so a single small margin would let an exact Krein collision read as a quartet (UB's text, verbatim; reproduced in `dl_recal.py`'s claim 5).
  - κ is the smallest round value that keeps the cluster at least ten times below the gray zone's lower edge at every control point.
  - That needs κ/G ≥ 10 × 0.0568, the largest coefficient, so κ ≥ 1.70.
- **The gray zone:** (margin/G, G margins), with G = 3, UB's feasibility figure, in place of 10.
  - The record's other factor-10 thresholds move with it: the off-axis count's |c| ≥ 10 margins becomes G margins.
- **The leak bound:** at most κ_L u‖A‖/gap, with κ_L = 200: ten times the controls' largest ratio, 19.2, rounded up. It replaces the fixed 10⁻⁸.
  - A gap that is not finite and positive, or a bound above 10⁻⁴, too large to discriminate, is an unresolved item, never a pass (UA).
  - The leak is checked only where symmetry directions are given. A system without them must be declared free of them (`symmetry_free`). An empty list not so declared is an unresolved item, so a driver that loses its tangents cannot read Elliptic (UA, UB).
  - The cap of 10⁻⁴ is mine, flagged. At any gap outside the gray zone, the bound stays below it for ‖A‖ up to about 8.1×10³.

## What it gives, on all 169 control points

- **(a) The cluster** sits 11.7 to 341 times below the gray zone's lower edge, at least ten at 169 of 169 points.
- **(b) Every control's spectrum outside the cluster** stays outside the gray zone: the gap is at least 406 times its upper edge.
- **(c) The leak** is at least 10 times below its bound.
- **(d) The smallest resolvable slow pair,** G margins:
  - N = 40: 1.7×10⁻⁶ at the smallest amplitudes. It reaches 1.04×10⁻⁵ at m = 7.8 to 8.8, and 4.3×10⁻⁵ at m = 132.
  - N = 24 and 32: 1.04×10⁻⁵ is reached at m = 12.2 to 26.4.
- **G = 10 does not meet the requirement.** With G = 10 the cluster condition needs κ ≥ 5.7, and at N = 40 a pair at 1.04×10⁻⁵ is then resolvable only up to m = 0.087, below the ladders' first point.

## What it does not give

- **The requirement holds only up to a moderate amplitude.** At N = 40, a pair below 1.04×10⁻⁵ is resolved only to m ≈ 8; above that, the floor rises with √m. That is reported as the recalibration's limit, not a pass.
- **The √m law is fitted on the controls only:** slots R2, R3 and R4, m from 0.204 to 132, and N = 16 to 40. Outside that range the margin is an extrapolation, and is flagged as one. For a target, the formula is fixed before the run; it is never tuned to a target's eigenvalues.
- **The resolution is not demonstrated here.** UA's synthetic demonstration of a genuine slow pair below 1.04×10⁻⁵ is the next pre-freeze item, at this margin, with its own arms.

## A second limit: L's inertia

- **A genuine slow pair at s needs an eigenvalue of L near 2ωs,** for a slow mode the gyroscopic term dominates (MOTIVATED).
- **L's inertia reads its zero cut at 10⁻¹⁰ ‖L‖,** with a gray zone up to 10⁻⁷ ‖L‖. A pair whose L eigenvalue falls there reads n(L) Unresolved, whatever the margin.
- **On the synthetic family** (`dl_recal.py`'s claim 7: ω = 1.3, m = 8), a pair at 3×10⁻⁵ clears A's gray zone, but its L eigenvalue, 4.6×10⁻⁸ ‖L‖, sits in L's, so n(L) reads Unresolved. At 10⁻⁴ the pair reads Elliptic.
- **At the controls' ‖A‖ and ω at N = 40,** the cut bounds the resolvable pair at about 10⁻⁷ ‖L‖/(2ω): 6.0×10⁻⁶ to 1.2×10⁻⁵, taking ‖L‖ ≈ ‖A‖ (INFERRED). That is the same size as the 1.04×10⁻⁵ requirement.
- **§7 does not list L's zero cut,** and the requirement needs it too. Its recalibration needs the controls' L-kernel lift, which the records do not carry.
- **The units' text, verbatim (UB; UA concurring):** "L's inertia cut is part of the same requirement: a genuine slow pair at s needs an L eigenvalue near 2ωs, so the current cut, 10⁻¹⁰ to 10⁻⁷ ‖L‖, bounds the resolvable pair near 10⁻⁵ at N = 40 (claim 7). The slow-pair demonstration recalibrates it on the controls' measured L kernel, and §7's requirement is met only when that demonstration passes."
- **UA's condition:** that demonstration must exercise both the spectral classifier and n(L). If the present cut prevents resolving the pair below 1.04×10⁻⁵, the gate fails and needs its own bounded, documented correction, never a forced classification.

## Risks, and what guards them

- **A defective nonzero group.** With one small margin, a Krein collision among the fast modes could split past it and read as a quartet, with nothing flagged (UB). The scale-aware tolerance links such a group and types it as one mixed group, which is Unresolved. `dl_recal.py`'s claim 5 shows it, at a collision near 35.7i over 40 mixings, with one margin for every role as its arm.
- **A cluster eigenvalue the model underestimates** could escape the cluster and be typed. The narrower gray zone makes that possible between G and 10 margins. Two checks catch it: V₀'s dimension against its expectation, and Theorem K's balance. Both report Unresolved; neither is new.
- **The choice was made after seeing the controls,** which §7 asks for. κ, G, κ_d and κ_L are provisional until the units review the implementation, its tests and the synthetic demonstration (UA).

## The implementation

- **The code** (`instrument/linear.py`):
  - `margin(normA, m)`, and the constants KAPPA, M0, GRAY, KAPPA_D, KAPPA_L and LEAK_CAP;
  - `record()` takes G, κ_d and the leak's factor; it links and types nonzero groups against τ(λ) = max(margin, κ_d √(u‖A‖ |λ|)), and labels each eigenvalue for the drivers;
  - `leak_bound()` refuses an undefined gap, or a bound above the cap;
  - no other threshold changes: the Jordan rank floor stays at 10² u‖A‖, and L's inertia cut at 10⁻¹⁰ ‖L‖.
- **The drivers** (`d6_theoremD.py`, `d7_controls.py`, `d7_ladders.py`) take the margin from `margin(‖A‖, ‖c‖²)`. They read the slow eigenvalues from the record's own labels, not from their own ten-margin filters (UA).
- **DL's original claims** (`dl_linear.py`) run under the original calibration, `ORIGINAL`, and reproduce their last output byte for byte (UA).
- **The recalibration's claims** (`dl_recal.py`), each outcome derived before the run:
  1. claim 3's system under the production record;
  1′. claim 1 at m = 21 over 40 mixings, as first written: as derived, with the cluster at least ten times below the gray zone at every mixing (UB).
     - It missed the headroom at 2 of 40, 9.59 and 9.94 times (DEVLOG 125, 126), and that FAIL stands (UA).
     - The bar is a tail statistic of the mixings. Over UB's 20,000 mixings every one classifies as derived; the headroom is at least 7.3, and under ten at 1.6 percent. Over 5,000 here it is at least 6.96, and under ten at 3.1 percent. UA's rerun of the same 40 read 10.4.
     - So 1′ is reported, unscored, and the ten-fold requirement is read on the controls: 11.7 times at their largest coefficient;
  1″. claim 1 at m = 21 over the same 40 mixings: as derived at every mixing (UB). Scored;
  2. the gray zone below the margin, with no gray zone as its arm;
  3. the gray zone above the margin, with the same arm;
  4. the leak bound and its refusals, with a vacuous fixed bound as its arm;
  5. UB's collision near 35.7i over 40 mixings, with one margin for every role as its arm;
  6. near the collision, at separations and real parts of 10⁻⁵ and 10⁻³ (UA), with the same arm;
  7. the second limit, L's inertia (above);
  8. missing tangents: an empty list not declared free of symmetry directions reads Unresolved, never Elliptic, with the empty list read as declared as its arm (UA).

  Reported beside them, unscored: every classification of DL's original claims that changes under the recalibration (UA). Read as DL ran them, declaring no symmetry where DL gave none, one of 31 changes: the quartet at real part 1.2×10⁻⁵, from Unresolved to Hyperbolic.
- **The synthetic m.** A synthetic system has no branch amplitude, so m is stated: 72 for the ω = 1.3 family, whose phase chains split like a control's at m of about 21, and 0.2 for the collision family, as UB ran it.
- **The regression,** on Blake's approval of its cost: DL, `dl_recal.py`, D6 at N = 16 to 40, D7's trial, and D7's sample at N = 16 and 24.

## Note (2026-10-17), after the slow-pair demonstration's Step 2

The text above stands as the recalibration closed (DEVLOG.md, entry 128). Since then, L's inertia cut is 1000 u ‖L‖, with its own gray zone up to G_L = 10 times it (`SLOWPAIR_PLAN.md`, Step 2; UB). Under it, `dl_recal.py`'s claim 7 reads its pair at 3×10⁻⁵ Elliptic, with the earlier cut as its arm, and claim 9 is rebuilt so the zero-count check stands alone: 10 scored claims and 8 arms pass (DEVLOG.md, entries 142 to 145). The change report reads 3 of 31, with two further count changes inside readings that stay Unresolved.
