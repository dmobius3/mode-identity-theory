# G4, the transfer onto the band's first positive mode: work order (drafted 2026-09-27; revised 2026-09-28 under the ruling; frozen 2026-09-28 on Blake's word)

*Revised 2026-09-28. The hold of 2026-09-27 is lifted: Blake ruled reading (A) on 2026-09-27 and decided 1a on 2026-09-28, and Lemma 1 is written out in projective-carrier.md §II. This revision takes F3's and F4's findings on the held version, which is kept as `FREEZE_2026-09-27.md` with its hold note and its Friedrichs note.*

**What landed first.** 9fca6ae on main records the reduction.
- The shared boundary mode reduces to the first-positive projection, given a simple first-positive eigenspace.
- Simplicity is a theorem for the pillar's twisted operator away from the critical width; any other band operator must
  be checked.
- For the pillar's operator, the projection is the one open premise.

This work order is the computation that tests whether the sampler's geometry supplies that projection by itself, on the
leading realization of the adopted placement, without selecting it.

## Rulings

**Scope round 2, carried.**
- The critical-width RP² claim is dropped.
- "One open premise" is scoped to operators with a known simple F_μ₁.
- The two signs are stated as projective-carrier.md §II states them: different objects, carried by one core loop, which
  agree on spinorial fields.
- Friedrichs and bridging columns are both run.
- Positives at finitely many samples are graded partial.

**Round 1 on the work order (F1 and F2, 2026-09-27), as carried.**
1. **Addition A.** Λ_l, the leakage, is the verdict quantity. In the twisted arm it does not depend on the extension:
   one Hilbert space, and F_μ₁ and ψ₁ are shared under Theorem 1.2. The untwisted arm is ruling 10's.
   - The complement of the first-positive eigenspace is everything outside it: the ground channel and the higher
     positive levels. It is not "the higher levels" alone.
   - The per-μ table gets an explicit ground row in every column.
2. **Withdrawn.** "No twisted descent" is no longer a block's verdict (rulings 8 and 9).
3. **Addition B's reduction, and the placement set is a probe.**
   - Conjugation by h ∈ 2I is L_h R_{h⁻¹}: L_h acts on each block by τ(h), a deck transformation, and R_{h⁻¹} acts
     unitarily. It fixes the real unit, so it rotates the imaginary S² by I. Any map x ↦ hxb that preserves that S² has
     b = ±h⁻¹, so nothing larger survives.
   - The residual space is SO(3)/A₅. The dependence on it is genuine: a block's output density on the S² is an
     I-invariant function, not a constant.
   - Finitely many placements cannot exhaust SO(3)/A₅, so the grading separates probes from a rule.
   - Where it is tractable, Λ_l is carried symbolically in the orientation too, a polynomial in the rotation's matrix
     entries.
4. **The widths.** Λ_l is symbolic in W, so the verdict covers every narrow width. The probe widths serve the per-μ
   table only.
5. **The bridging control.** Λ_l^F(W) = Λ_l^br(W) by construction in the twisted arm, and in the untwisted arm under
   the φ₀-transformed rule, which makes that arm isospectral with twisted bridging. The per-μ decomposition of the
   complement can redistribute. Under the same cone-trace matching the equality is not established (ruling 10).
6. **The channel readings are fixed before the numbers.**
   - Any leakage is a no-go for deriving the projection from that sampler's geometry, in that arm, on M(W). Condition 1
     returns to the projection as an explicit physical premise (scope round 2, ruling 6) only if every admissible sampler
     leaks, or if 1d selects one that does. It is not falsified.
   - Leakage confined to the ground channel speaks to the conic defect where the ground mode is a defect state: the
     twisted arm's φ₀ and bridging's bound state, and the untwisted arm's transformed bound state. The untwisted
     Friedrichs ground mode is the constant; leakage into it reads as a uniform component, with no defect reading.
   - Leakage into the positive levels speaks to the sampler's geometry.
7. **The norms are on the quotient.** The twisted arm is evaluated in L²(M(W), L; dA) and the untwisted arm in
   L²(M(W), dA): the rectangle [0, πR] × [−W, W] with dA = |cos(y/R)| dy dw. Upstairs integrals over the double lune
   are twice these.

**Round 2 on the work order (F3 and F4, 2026-09-28).**

8. **Both samplers are frozen, as two columns.** The value sampler O⁽⁰⁾ = Ψ̃|_M and the transverse sampler
   O⁽¹⁾ = ∂_ν Ψ̃. The sampler is open (1d), so neither column is primary. With one sampler frozen, a result favouring it
   would arrive with the choice still unmade.
9. **Two target arms in each sampler.**
   - A block's output under O⁽⁰⁾ is twisted exactly when τ(−I) = −id. Under O⁽¹⁾ it is twisted exactly when
     τ(−I) = +id, since the normal derivative lowers the degree by one.
   - Each output is graded against the first-positive eigenspace of its own arm's operator, in its own arm's norm.
   - No block is recorded as a known zero. That a block's output misses the other arm's target is bookkeeping, not a
     result.
   - Under Friedrichs the two arms are unitarily equivalent through multiplication by φ₀ (projective-carrier.md §II), so
     a block's arm moves no level and no intensity profile. It moves the target.
10. **The untwisted arm's operators.**
    - Friedrichs: the Neumann-lune problem on M(W). Its first positive level 2/R² is simple, spanned by φ₀u₀, the
      twisted mode u₀ = sin(y/R) with its sign flipped across the cone point. Its ground mode is the constant.
    - Bridging under two named policies, both run, so the run does not decide 1e:
      - **the φ₀-transformed rule** (δ₀ = R): isospectral with twisted bridging; the target is φ₀u₀ at 2/R², and
        ruling 5 extends;
      - **the same cone-trace matching** (δ₀ = R): φ₀u₀ leaves the domain. The column's first positive level and
        eigenspace are computed first, as a registered spectral step returning the level, its multiplicity and a basis.
        Leakage is graded only against that eigenspace. If it is degenerate, a zero grades as selection of the subspace
        only, and a grade for every narrow width needs the step for every narrow width. If the step is not completed in
        the run, the column records "not computed".
11. **The fork is decided, and a fence replaces it.** See the record below.
12. **The 2-fold placement's extra symmetry is disclosed in advance.**
    - Its core's axis, p × c = k, is itself a 2I axis. So ±k preserve the core under left multiplication, and the
      placement's image in S³/2I meets itself along the whole core at every width.
    - The pullback stays well defined, so the run is unaffected.
    - A zero at this placement is graded as a symmetric probe.
    - No non-central element preserves the core at the other three placements. The 2-fold pole's axis carries 2
      non-central elements, the 3-fold pole's 4 and the 5-fold pole's 8; the generic pole's none.
    - Checked in `tools/g4_terms.py` (T4).

## The frozen terms

- **Convention.**
  - 2I is the 120 unit icosians. That is the 24 Hurwitz units ±1, ±i, ±j, ±k and (±1 ± i ± j ± k)/2, plus the 96
    elements (0, ±1, ±φ⁻¹, ±φ)/2 under even permutations of the coordinates (1, i, j, k). Here φ = (1 + √5)/2.
  - The deck action is left multiplication.
  - The great S² is the unit imaginary quaternions, so its normal in S³ is the real unit.
  - The samplers are O⁽⁰⁾_M(Ψ) = Ψ̃|_M and O⁽¹⁾_M(Ψ) = ∂_ν Ψ̃, with ν = 1, the derivative along the real axis.
  - Checked in `tools/axes.py` (exact, sympy): 120 elements, 60 conjugation rotations, and the poles below are fixed
    axes of rotations of the stated orders. Checked in `tools/g4_terms.py`: the characters, the block levels, the
    arms and the placements' symmetries.
- **The band.**
  - M(W), the double lune modulo −I (Remark 2.1): the declared calculational realization of the adopted projective
    placement. It does not decide 1b.
  - For a pole p and azimuth c (orthonormal, imaginary) with d = p × c, the band point is
    P(y, w) = cos(y/R)(cos(w/R) c + sin(w/R) d_y) + sin(y/R) p on the rectangle [0, πR] × [−W, W], with d_y = d for
    y ≤ πR/2 and d_y = −d beyond. P is continuous at the pinch, where cos(y/R) = 0, and −I pairs (0, w) with (πR, −w),
    the pillar's seam, so the pillar's parity rules in w apply as written (`tools/g4_terms.py`, T5). The cone point is
    p.
- **Placements (pinned).**

  | Placement | Pole p | Azimuth c |
  |---|---|---|
  | generic | (i + 2j + 3k)/√14 | (2i − j)/√5 |
  | 2-fold | i | j |
  | 3-fold | (i + j + k)/√3 | (i − j)/√2 |
  | 5-fold | (φ⁻¹ i + j)/√(1 + φ⁻²) | k |

  The generic pole sits 15.62° from the nearest symmetry axis. The 2-fold placement's core is preserved by ±k
  (ruling 12).
- **Widths.**
  - Λ_l is symbolic in W on 0 < W < πR/2, and in the orientation where tractable. Otherwise it is symbolic in W at each
    pinned placement.
  - The per-μ table is computed at W/R ∈ {1/4, 1/2, 1, 7/5}.
- **Band operators.**
  - Twisted arm: the pillar's twisted Laplacian with Neumann arcs. Friedrichs is primary, with a bridging column at
    δ₀ = R (> 2R/e).
  - Untwisted arm: the Laplacian on functions on M(W) with Neumann arcs. Friedrichs is primary, with two bridging
    columns at δ₀ = R, the φ₀-transformed rule and the same cone-trace matching (ruling 10).
- **Blocks.** The first two occurring levels n ≥ 1 of every irreducible τ of 2I, computed from its character table
  before the run (`tools/g4_terms.py`, T2):

  | τ | 1 | 3 | 3′ | 4 | 5 | 2 | 2′ | 4′ | 6 |
  |---|---|---|---|---|---|---|---|---|---|
  | τ(−I) | + | + | + | + | + | − | − | − | − |
  | levels | 12, 20 | 2, 10 | 6, 10 | 6, 8 | 4, 8 | 1, 11 | 7, 13 | 3, 9 | 5, 7 |

  Level 0, the ambient constant, is run as a disclosed control and not graded: its eigenvalue is 0, so it carries no
  level for an observable to read. The value sampler sends it to the constant function in every column, which is the
  untwisted ground mode under Friedrichs; the transverse sampler annihilates it.
- **Bases.** Each block gets an orthonormal basis in the ambient L² norm on S³. The twisted target ψ₁ = sin(y/R) is taken
  in L²(M(W), L; dA) and the untwisted target φ₀u₀ in L²(M(W), dA). HS norms do not depend on the basis.
- **Outputs.**
  - Per block, sampler and extension column: ‖P_μ₁ O|‖²_HS and Λ_l against the block's own arm, in the symbolic forms
    above.
  - Per block, width, placement, sampler and column, the per-μ table: ‖P_μ O|‖²_HS and the rank. It covers the ground
    row and a fixed number of positive levels, with the remainder of Λ_l stated as a residual.
- **The zero rule.** Symbolic zeros where symmetry gives them; otherwise a relative tolerance of 10⁻¹² against
  ‖O|‖²_HS.
- **The grades,** read separately for each arm and each sampler column.
  1. Λ_l ≡ 0 symbolically for all W and all orientations, for every block the arm receives under that sampler: a
     selection rule. The projection is derived on M(W) for that arm and sampler.
  2. Λ_l = 0 at every pinned placement, symbolic in W: partial evidence only. No leakage was found at the registered
     placements; a zero at the 2-fold placement is a symmetric probe.
  3. Λ_l > 0 at any placement: a no-go instance for orientation-independent selection. It is read by channel, per
     ruling 6.
- **Guards.**
  - Which blocks land in which arm under each sampler is known in advance and gets no physical reading. In particular
    it is not to be read as the 60R projection, which needs its own adjudication.
  - §II's fence: the results get no spin-statistics reading. The spin sign is geometric on the carrier; the divide is
    set by −I.
  - Nothing here selects M(W) as the physical carrier (1b), a sampler (1d), an extension or untwisted policy (1e), or a
    layer (1f).
  - The run is blind: a fresh runner works from these terms alone, as the Tier 2 run was done.

## The record of decisions

This replaces the fork section of the held version, which is kept there with its options and grounds as history.
- **2026-09-27: reading (A).** Blake ruled that the vacuum carrier is unbent and realized through the projective layer:
  it lifts to and embeds in ℝP³ = S³/{±I}, with core −I (projective-carrier.md §XI).
- **2026-09-28: 1a's formula.** The postulate's formula names the layer, with the arrow on the band,
  S¹ = ∂(Möbius), Möbius ↪ ℝP³ = S³/{±I}, ∂S³ = ∅ (ee7b7f5).
- **Open:** 1a's second item (the anti-periodic condition's reach), 1b (whether the carrier is M(W)), 1c, 1d, 1e, 1f
  (the physical layer, and the pose if sampling reads through S³/2I) and 1g.
- **The fence.** G4 uses M(W) as the declared calculational realization of the adopted projective placement. It does
  not decide 1b, and its sampler and extension columns decide neither 1d nor 1e. The placements probe the carrier's pose
  relative to 2I; they decide nothing in 1f.
