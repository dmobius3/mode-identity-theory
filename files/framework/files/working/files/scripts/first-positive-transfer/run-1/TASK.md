# Task: the transfer of ambient harmonic blocks onto the first positive mode of a conic Möbius band

Compute the quantities of §6, grade them as §7 says, and report them as §8 asks. Everything in §§1-5 is given; the facts marked "given" are already verified. You may re-derive any of them, but do not change them. `REFERENCE.md` in this directory is a paper on the band and its operator; this task cites it as "the reference".

Units: the curvature radius is 1 throughout.

## 1. Setting (given)

**The sphere and the group.**
- S³ is the unit sphere in ℝ⁴, written as unit quaternions q = x₀ + x₁i + x₂j + x₃k.
- 2I is the group of the 120 unit icosians: the 24 elements ±1, ±i, ±j, ±k and (±1 ± i ± j ± k)/2, and the 96 elements whose coordinates (x₀, x₁, x₂, x₃) are an even permutation of (0, ±1, ±φ⁻¹, ±φ)/2 with all sign choices, where φ = (1 + √5)/2.
- 2I acts on S³ by left multiplication, q ↦ gq, and on functions by (g·Ψ)(q) = Ψ(g⁻¹q). Its central element −1 acts on S³ as the antipodal map.
- The great sphere S² = S³ ∩ {x₀ = 0} is the set of unit imaginary quaternions. Its unit normal in S³ is the real unit 1, the direction of x₀.

**The band.**
- Fix a pole p and an azimuth c, orthonormal unit imaginary quaternions, and let d = p × c (the cross product of their imaginary parts).
- For 0 < W < π/2, the band map on the rectangle [0, π] × [−W, W] is
  P(y, w) = cos y · (cos w · c + sin w · d_y) + sin y · p,
  with d_y = d for y ≤ π/2 and d_y = −d for y > π/2. P is continuous at y = π/2, where cos y = 0, and it lies in the great sphere S².
- **Seam.** P(π, −w) = −P(0, w) for every w. So the antipodal map identifies (0, w) with (π, −w).
- **Cone point.** The fiber y = π/2 maps to the single point p.
- **The intrinsic band.** The metric pulled back by P is dy² + cos²y dw², with area element dA = |cos y| dy dw. With the seam identification (0, w) ∼ (π, −w) this is the reference's band M(W) (its §2), and P realizes the reference's Remark 2.1: the double lune in S², modulo the antipodal map.

## 2. Ambient blocks (given)

**Characters.** For g ∈ 2I let χ₂(g) = 2·Re(g), and χ₂′(g) = 2·σ(Re(g)), where σ is the Galois conjugation φ ↦ 1 − φ on the real parts that occur (so σ fixes 0, ±1, ±1/2 and exchanges φ/2 with −φ⁻¹/2, and −φ/2 with φ⁻¹/2). The nine irreducible characters of 2I are
1 = 1, 2 = χ₂, 2′ = χ₂′, 3 = χ₂² − 1, 3′ = χ₂′² − 1, 4 = χ₂χ₂′, 4′ = χ₂³ − 2χ₂, 5 = χ₂⁴ − 3χ₂² + 1, 6 = χ₂⁵ − 4χ₂³ + 3χ₂.
The central element −1 acts as −id exactly in 2, 2′, 4′ and 6.

**Blocks.** For an irreducible τ and a degree n, the block E^τ_n is the τ-isotypic component, under the left action above, of the degree-n harmonic polynomials on ℝ⁴ restricted to S³. Each block gets an orthonormal basis in L²(S³) with the round volume measure. The blocks to run are the first two degrees n ≥ 1 at which each τ occurs:

| τ | 1 | 3 | 3′ | 4 | 5 | 2 | 2′ | 4′ | 6 |
|---|---|---|---|---|---|---|---|---|---|
| −1 acts as | + | + | + | + | + | − | − | − | − |
| degrees | 12, 20 | 2, 10 | 6, 10 | 6, 8 | 4, 8 | 1, 11 | 7, 13 | 3, 9 | 5, 7 |

**Level 0.** The block E¹₀ (the constants) is run as a control and is not graded (§7).

## 3. Samplers (given)

For a function Ψ on S³, extended to ℝ⁴ as its harmonic polynomial:
- the **value sampler** is O⁽⁰⁾Ψ(y, w) = Ψ(P(y, w));
- the **transverse sampler** is O⁽¹⁾Ψ(y, w) = (∂Ψ/∂x₀)(P(y, w)), the derivative along the normal of S².

**Arms.** A sampled output f satisfies f(π, −w) = ±f(0, w).
- Sign −1: f is a section of the band's orientation line bundle, the reference's twisted setting. This is the **twisted arm**.
- Sign +1: f is a function on M(W). This is the **untwisted arm**.
- Given: under O⁽⁰⁾ a block's output is in the twisted arm exactly when −1 acts as −id in τ; under O⁽¹⁾, exactly when −1 acts as +id. Every block is run under both samplers, each output in its own arm.

## 4. The target operators (given)

In both arms the operator is the Laplacian of dy² + cos²y dw² on the rectangle, with the arm's seam condition from §3, the Neumann condition on the arcs w = ±W, and, at the cone point, the regular branch in every nonconstant transverse sector (the reference's Definition 3.5). The constant transverse sector takes one of the cone conditions below, in the reference's trace coordinates (u_D^±, u_N^±) of its §3.5. The "+" side is y > π/2 and the "−" side is y < π/2, and ũ_D denotes the value renormalized at length δ₀ as in the reference.

**Twisted arm.**
- *Friedrichs (primary):* u_N^+ = u_N^- = 0.
- *Bridging, δ₀ = 1:* ũ_D^+ = ũ_D^-, u_N^+ + u_N^- = 0.
- Given: for 0 < W < π/2 both have first positive eigenvalue 2, simple, spanned by ψ₁ = sin y (the reference's Theorem 1.2 and Corollary 6.3; δ₀ = 1 > 2/e). The Friedrichs ground mode is φ₀, equal to +1 for y < π/2 and −1 for y > π/2, with eigenvalue 0. The bridging ground mode is the defect-bound state of the reference's §4.4.

**Untwisted arm.**
- *Friedrichs (primary):* u_N^+ = u_N^- = 0.
- *The φ₀-transformed rule, δ₀ = 1:* ũ_D^+ = −ũ_D^-, u_N^+ = u_N^-. This is the twisted bridging domain multiplied by φ₀.
- *The same cone-trace matching, δ₀ = 1:* ũ_D^+ = ũ_D^-, u_N^+ + u_N^- = 0, the twisted bridging condition applied to functions.
- Given: multiplication by φ₀ maps the twisted arm unitarily onto the untwisted arm and carries the twisted Friedrichs and bridging conditions onto the untwisted Friedrichs and φ₀-transformed conditions (the reference's Proposition 4.2 for Friedrichs). So under those two conditions, the untwisted first positive eigenvalue is 2, simple, spanned by φ₀ψ₁ = φ₀ sin y. The untwisted Friedrichs ground mode is the constant function.
- *Under the same cone-trace matching* φ₀ sin y is not in the domain, and nothing about the spectrum is given. First compute this operator's first positive eigenvalue, its multiplicity and a basis of its eigenspace. That is a spectral step. Grade leakage only against that eigenspace (§7).

## 5. Placements and widths (given)

| Placement | Pole p | Azimuth c |
|---|---|---|
| generic | (i + 2j + 3k)/√14 | (2i − j)/√5 |
| 2-fold | i | j |
| 3-fold | (i + j + k)/√3 | (i − j)/√2 |
| 5-fold | (φ⁻¹ i + j)/√(1 + φ⁻²) | k |

- Disclosed in advance: at the 2-fold placement the core circle {P(y, 0)} has axis p × c = k, and left multiplication by ±k preserves that circle. At the other three placements no element of 2I other than ±1 preserves the core circle.
- Widths: the leakage of §6 is computed symbolically in W on 0 < W < π/2, and also in the orientation of (p, c) where that is tractable (for example as a polynomial in the entries of the rotation taking a reference frame to (p, c, d)); otherwise symbolically in W at each placement. The per-level tables of §6 are computed at W ∈ {1/4, 1/2, 1, 7/5}.

## 6. What to compute

For a block E = E^τ_n with orthonormal basis Ψ₁, …, Ψ_D, a sampler O, and a cone condition of the output's arm, all norms are in L² of the rectangle with dA = |cos y| dy dw:
- ‖O|‖² = Σ_k ‖O Ψ_k‖², the Hilbert-Schmidt norm of O restricted to E;
- ‖P₁O|‖² = Σ_k ‖P₁ O Ψ_k‖², where P₁ is the orthogonal projection onto the arm's first positive eigenspace for that cone condition;
- the leakage Λ = ‖O|‖² − ‖P₁O|‖².

Compute:
1. For every block of §2, both samplers, and every cone condition of the output's arm: ‖O|‖², ‖P₁O|‖² and Λ, in the symbolic forms of §5.
2. Per block, width, placement, sampler and cone condition, the per-level table: ‖P_μ O|‖² and the rank of P_μ O|, for the ground level and for a fixed number of positive levels that you choose and state, with the rest of Λ reported as a residual.
3. The spectral step of §4 for the same cone-trace matching.
4. The level-0 control, under both samplers.

## 7. Zero rule and outcome classes

**Zero rule.** A value is zero if it vanishes symbolically where a symmetry gives the vanishing; otherwise if it is below 10⁻¹² relative to ‖O|‖².

**Outcome classes,** reported separately for each arm, each sampler and each cone condition:
- **S (selection):** Λ = 0 symbolically for every W in (0, π/2) and every orientation, for every graded block that the arm receives under that sampler.
- **P (partial):** Λ = 0 at every placement of §5, symbolically in W. Report a zero at the 2-fold placement as a symmetric probe.
- **N (leakage):** Λ > 0 at some placement. Report where, and its per-level decomposition from §6.2.

For the same cone-trace matching:
- if the spectral step finds the first positive eigenspace degenerate, Λ = 0 counts only as selection of that subspace;
- a class claimed for every W needs the spectral step for every W;
- if the spectral step is not completed, report the condition as "not computed".

Two relations hold by construction and are not outcomes:
- In the twisted arm, and in the untwisted arm under the φ₀-transformed rule, Λ is the same under Friedrichs and bridging (the target is shared), though the per-level decomposition may differ.
- The level-0 control is not graded.

## 8. Reporting

Put everything in `RETURN.md` in this directory:
- **Results.** For every block, sampler, arm and cone condition: ‖O|‖², ‖P₁O|‖² and Λ, in symbolic form where computed and numerically at the four widths.
- **Per-level tables,** as §6.2 asks, with the number of positive levels you chose.
- **The spectral step:** the level, its multiplicity, a basis and the method, or "not computed".
- **The level-0 control.**
- **Outcome classes** of §7, one per arm, sampler and cone condition.
- **Method as run.** Any point where you could not follow this task exactly, and what you did instead.
- **Files.** The scripts that produce every value, and their output records.
- **Consulted material.** A manifest of every file you read.
- **Underdetermined points.** Any point in this task you found underdetermined or ill-posed, with the reading you took.

Rules for the values:
- Report numbers as computed, without interpretation.
- Say for each value whether it was computed.
- Report a value your computation did not reach as missing, never as zero.
- "Unresolved" is always an allowed answer.
