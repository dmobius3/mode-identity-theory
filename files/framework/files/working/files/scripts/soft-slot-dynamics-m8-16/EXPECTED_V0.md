# M8.16: each control's expected generalized kernel (2026-10-15)

Stated before any control runs (UB's (e); UA's GO). Each row is the `expected` input that §7's record takes at a point of that control: V₀'s dimension and the ranks of A's powers on it. A mismatch, or a symmetry leak above 10⁻⁸, is an unresolved item, and then the point is not typed. The rows are derived from MIT's pages. M8.15's frozen algebraic dimensions, `FROZEN_DIM` in `m815_common.py` (C1 6, C2a 4, C2b 6, C3 8, each k + r_u), serve only as the cross-check (UA).

## The rule (DERIVED, from the pages cited)

At a point of a branch from Lemma G at small amplitude, or of Theorem D's rigid family at any amplitude:
- **The kernel.** ker A consists of the static vectors (ζ, 0) with Lζ = 0. That is the tangent space of the stationary family, of dimension k. Sources: the Soft-Slot Branches §III, "Its kernel"; and the Slot Ground States, Theorem D.
- **The partners.** Each vector of the σ-radical of the kernel, of dimension r_u, has a partner, with σ(x, y) = Re⟨x, iy⟩ and the radical always containing iφ. So V₀ has dimension at least k + r_u (the Soft-Slot Branches, Theorem R(e), "Partners", with Lemma S).
- **No more zeros.** By Theorem R(a), A has exactly as many eigenvalues within o(ε) of 0 as Ŝ_u has zeros. That number is the slow space's real dimension, 2 dim_C E₀, less two for each nonzero slow pair. At each control below it equals k + r_u.
- **So,** V₀ has dimension exactly k + r_u. It carries r_u chains of length 2 and k − r_u chains of length 1. A's ranks on it are [r_u, 0], and the number of chains, `blocks`, is k. No chain is longer than 2, so the margin's root scale is j = 2 (UB).

## The controls

| Control | Slot, state | E₀ (level, real dimension) | k, r_u | Nonzero slow pairs | Zero multiplicity | M8.15 | `expected` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 (D6) | R3, Theorem D's member φ = π₂(x)v | 2, 6 | 5, 1 | (exact spectrum, Theorem D) | 6 | 6 | dim 6, ranks [1, 0] |
| C2a (D7) | R4, coherent v₃ | 6, 14 | 3, 1 | 5: τ = 28/143, 56/429, 140/99, 112/39, 896/1287 | 14 − 10 = 4 | 4 | dim 4, ranks [1, 0] |
| C2b (D7) | R2, weight 7/2, v₇/₂, complex structure i | 7, 16 | 5, 1 | 5: τ = 112/143, 168/143, 336/143, 504/143, 560/143 | 16 − 10 = 6 | 6 | dim 6, ranks [1, 0] |
| C3 (D7) | R4, octahedron v₂ + v₋₂ | 6, 14 | 4, 4 | 3: the real pair at ν = 250880/552123, three times | 14 − 6 = 8 | 8 | dim 8, ranks [4, 0] |

- **C1.** The Slot Ground States, Theorem D, item 2, with n = dist(R₃) = 2: on E₀ the zero has algebraic multiplicity 2n + 2 = 6 and geometric 2n + 1 = 5. The kernel is the tangent space of the sphere |v′| = |v| in E₀, of real dimension 5. The one generalized vector is the family's derivative in the charge. So k = 5 and r_u = 1. The σ-radical of that tangent space is the line of iv, since iq is normal to the sphere only along iv. Theorem D is exact, so the row holds at every amplitude.
- **C2a, C2b and C3.** (k, r_u) are the Soft-Slot Branches §IV's rows: coherent v₃ (3, 1), octahedron (4, 4) and weight 7/2 (5, 1). The nonzero slow pairs are that section's frequency lists. E₀'s dimension is (n₀ + 1) complex at the lowest level n₀, where each slot occurs once, by 2I's characters (D1).

## Why the rows hold at the sample points (DERIVED where marked, INFERRED otherwise)

- **The radical along the branch (DERIVED).** σ(X_aφ, X_bφ) = −½ ε_abc J_c(φ) for the rotation generators, and the phase direction pairs with none of them (the Soft-Slot Branches §IV, "Hypothesis (Z)").
  - **C2a and C2b.** J(u) ≠ 0, since the state is a weight vector of nonzero weight. So J(φ_ε) ≠ 0 for small ε, and the radical keeps dimension 1. In R2 the Sp(1) directions Jφ and iJφ lie in the kernel and pair with each other, σ(Jφ, iJφ) = −‖Jφ‖², so they add nothing to it.
  - **C3.** The isotropy contains the octahedral rotations, each with its fibre phase. An O-invariant vector of ℝ³ is 0, so J(φ_ε) = 0 along the branch, and the radical is all of the kernel throughout.
  - **C1.** The radical is the line of iv at every member.
- **The kernel's dimension (DERIVED for small ε).** Lemma G gives φ_ε isotropy exactly Γ_u, so the family's dimension k is constant. The coherent and weight-7/2 isotropies contain the rotations about z composed with a phase, so T_zφ is a multiple of iφ. That gives k = 3 in R4 (Γ of dimension 4) and k = 5 in R2 (Γ of dimension 6).
- **No genuine crossing at ε ∈ {0.5, 1, 2} (INFERRED).** Theorem R holds for 0 < ε < ε₁, and ε₁ is not computed. `soft-slot-dynamics-m8-15x-target1/REGISTER_4.md` §5 records, from M8.15's qualification, that none of the non-target controls has a genuine crossing: "C2a, C2b, C3 and the pyramid each keep their genuine index along their ladders", and "C2a's and C2b's changes in `n(L)` are structural", the finite-element lift. A crossing at a sample point, or a partner whose energy vanished there and lengthened its chain, would show in §7's record as a mismatch, reported as unresolved and never as a type.

## The symmetry directions for the leak

- T_aφ for a = 1, 2, 3, the right generators (`functional.right_generators`), and iφ, at every control.
- In R2 (C2b), also Jφ and iJφ, from the fibre structure K (`functional.fibre_structure_matrix`).
- In C1 the kernel is larger than the symmetry orbit: it is the whole sphere of the rigid family. The leak covers the symmetry directions, and the dimension and the ranks cover the rest.
