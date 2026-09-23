# Work item 4b: the full isotropy of the three outside orbits, and [KU]'s table (packet, frozen for the run, 2026-09-22)

Work item 4 (`work_item_4_packet.md`, frozen at `458de644…`, run log `b0f15831…`) stands as PASS for
what it asked: three certified critical orbits, `T1`, `T2`, `T3`, with certified `SO(3)` stabilisers
`C₂`, `{1}`, `C₂`. **Dated note, 2026-09-22:** its pre-registered [KU] inference used the wrong notion
of stabiliser. [KU]'s group `G` contains time reversal (`symmetry.tex` line 163), so the question
their procedure turns on is the isotropy in `U(1) × SO(3) × {1, Θ}`, antiunitary elements included.
That frozen packet is not amended; this one asks the question it substituted away (F1).

## Part 1: the full projective isotropy, certified

For the three targets and three controls (pyramid, prism, D2 ray), certify the group of all
`g ∈ U(1) × SO(3) × {1, Θ}` that fix the ray.

- **Upper bound.** From the full-sphere certified box (work item 4's system, rerun here), every
  isotropy element permutes the six stars preserving all distances: a unitary one with determinant
  `+1`, an antiunitary one (time reversal composed with a rotation, an improper map of the
  constellation) with determinant `−1`. So the group has at most as many elements as there are
  surviving permutations of both kinds, all 720 enumerated with the determinant enclosure deciding
  each.
- **Convention gate** (F1). In these coordinates, `Θ ∘ D(R_y(π))` must act as `w ↦ −w̄`,
  coefficientwise conjugation up to sign, checked on random states before anything else. Then the
  rays fixed by that antiunitary element are exactly the real rays.
- **Lower bound.** Rotate the representative so that its principal rotation axis, if any, is `z` and a
  mirror normal is `y`, and certify the critical orbit inside the joint fixed set: the character
  subspace of the unitary generators intersected with the real vectors. Slices only for continuous
  symmetries preserving that set (rotations about `y` when there is no unitary part; none
  otherwise). Every point of the set is fixed by the generated group, which is `2 ×` its unitary
  part. If that order equals the upper bound, the isotropy is exactly that group.
- **Identification.** The joint-set certificate and the full-sphere one are separate proofs; they are
  matched by overlapping enclosures of `924 r̂₆`, `|f|²`, `‖B₀‖²` and `Tr𝒩²`, a cross-check, not a
  proof of identity, as in work item 4.
- **Phase lifts** (F1). For each generator the phase with which it fixes the certified real
  representative is printed: `χ` for the unitary ones, and `Θ D(R_y(π)) w = −w` for the antiunitary
  one on a real `w`.

Controls: pyramid, prism and D2 ray must certify with isotropy of order 10, 12 and 8 (their five,
six and four rotations, each with as many antiunitary elements). Arm: the displaced pyramid of work
item 4 has no antiunitary survivor, so it must find no mirror (its antiunitary defect stays above
`10⁻¹⁴` at every normal).

## Part 2: [KU]'s Table II at the point

At `(c_γ, c_α, c_β) = (1, −32, −12)`, evaluate exactly the parameters of [KU]'s states G, R and J
(`symmetry.tex` Table II): a state whose amplitudes need the square root of a negative number does not
exist there. State C is given by [KU] only numerically, on real `(a, 0, b, 0, c, 0, d)` with isotropy
`{e^{iπ}C₂z, C₂ₓΘ}`; compare it with the certified groups by isotropy class. Record whether any row of
the table has an isotropy group with no nontrivial unitary element.

**Two questions kept apart** (F2), for § 7.2:

1. *Does [KU]'s procedure return the orbit?* Their procedure minimises the energy on each subgroup's
   fixed set. If an orbit's isotropy is exactly `H`, and `H`'s fixed set contains the coherent state
   and the hexagon, the extremes of `r̂₆` (Section 7.3), then at `g = 1` the procedure returns the
   coherent state and at `g = −1` the hexagon from that subgroup, and returns the orbit at neither
   sign, since its value lies strictly between them. This is checked by verifying that `v₃` and the
   hexagon lie in each certified fixed set.
2. *Does some [KU] stationary-state formula, evaluated at the point, coincide with the orbit?* A
   search question, answered row by row from part 2, with "not located" wording where nothing
   matches.

## Outcomes, and what § 7.2 may then say

| outcome | § 7.2 |
| --- | --- |
| `T2`'s isotropy certified as exactly `{1, Θ R(π)}` | a certified critical orbit whose only symmetry is antiunitary; [KU]'s table has no row of that isotropy type, and their procedure would not return it at either sign |
| `T1`, `T3` certified as exactly [KU]'s C type | two certified critical orbits of [KU]'s state-C isotropy type, neither the extreme on that fixed set, so not returned by the procedure at either sign; [KU] compute C only numerically, as a minimum |
| a certificate fails | stated as not certified, with the diagnostic; the § 7.2 sentence is restricted to what did certify |

`T2`'s value is worded "agrees with `28800/121` to 59 digits"; its exact form is not attempted in this
run (F1, F2: third, bounded, and only if the table hands it over).

## Mechanics

`sources/certify_isotropy.py` executes the definitions of `certify_outside_orbits.py` verbatim (so the
model is the certified one), then parts 1 and 2, controls first. Its log, its hash and this packet's
travel in the report. Nothing is filed anywhere.
