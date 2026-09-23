# Work item 4: the three orbits outside the census's class (packet, frozen for the run, 2026-09-22)

This file fixes the target, the standing each check can earn, the controls and what each outcome
lets § 7.2 say, before the script meets the targets. It follows F1's scoping and F2's conditions
from the plan redline, and the packet redline from both units (round 2): the two-object critical
system, projective root isolation, the permutation certificate for the stabiliser, both sectors,
the failure diagnostics and the stated limitation.

## Target

For each of the three critical orbits that the 2026-09-05 exploratory census found outside M8.12's
class, at `924 r̂₆ ≈ 215.775792502`, `238.016528926` and `238.356854743`:

1. whether it is a genuine critical orbit of `r̂₆` on `ℙ(V₃)`, **certified**;
2. its projective stabiliser in `SO(3)`, **certified**, with the weight on proving or refuting a
   trivial stabiliser for the orbit at `238.016528926`.

Not in scope: exact closed forms, and the three orbits' Morse indices. Numerical signatures are
reported as reconnaissance only.

## Inputs, pinned

| file (local, exploratory) | SHA-256 | what it holds |
| --- | --- | --- |
| `OpenWave/M8_DYNAMICS/out/pencil_census_r4.npz` | `01e27b734c7a0ca7ec73b360fc20d6ce5d131652b37371ff2b00526e1f85b698` | twelve orbits, `orb00` to `orb11`, as 7-vectors in the order `v₃ … v₋₃` (index 0 is `m = 3`), read as fibre vectors |
| `OpenWave/M8_DYNAMICS/out/pencil_census_r5.npz` | `6da7f6ca4e48703866a5d96edb69ee2979725ab850c54fc7f84de38e92d05450` | the same for the other sector (the label trap: `r4` is `3′`, `r5` is `4`) |
| `OpenWave/M8_S/identify_census_states.py` | `5743a5a0157cdd49951b52127a4408b57fe8875cc2652ec2558a392eceaf64ec` | the reconnaissance: an axis search for `C_k`, `k = 2 … 6`, at tolerance `10⁻¹⁰` |
| `OpenWave/M8_S/identify_census_states_log.txt` | `dbb5f7806a31745e6e871e915020152f063a06c57a575914f8137beffed21b17` | its labels: `C₂`, none found, `C₂`, the same in both sectors |

Each sector holds nine of the ten census orbits (`v₁` is missing) and the same three outside ones.
The two sectors are two seeds for one ambient quartic, since `r̂₆` does not depend on the sector.
The reconnaissance labels are leads, not results.

## Coordinates

The computation runs in the coefficients `w₀, …, w₆` of the binary sextic `P_u` of Section 7.3
(`w_k` on `x^k y^{6−k}`). There the Bombieri norm, `r(u) = ‖ρ₆(u)‖² = [P_u P_Θu]²` (Lemma 7.3), the
time reversal `P_Θu(x, y) = −P̄_u(y, −x)` and the rotation generators `x∂_y`, `y∂_x` and
`(x∂_x − y∂_y)/2` all have rational coefficients, so interval evaluation is exact up to outward
rounding. Inner products are the real part of the Bombieri inner product throughout.

## The standings, named before the run

**Certified critical orbit.** In interval arithmetic (`mpmath.iv`, 60 digits), the Krawczyk
operator proves that the following system has exactly one zero in a stated box around a refined
centre. Two different objects enter it (F1): fixed slice vectors `s₀ = i w₀` and `s_μ = i F_μ w₀`,
evaluated once at the seed `w₀`, and the orbit tangents at the moving point,
`τ₀(w) = i w` and `τ_μ(w) = i F_μ w`. In the unknowns `w ∈ ℝ¹⁴`, `μ` and `ν₀, …, ν₃`:

```text
∇r(w) − 2μ w − Σ_k ν_k τ_k(w) = 0      (14)
‖w‖² − 1 = 0                            (1)
⟨s_k, w − w₀⟩ = 0,  k = 0, …, 3         (4)
```

Because `r` is invariant under phase and rotations, `∇r(w)` is orthogonal to every `τ_k(w)`, and so
is `w`; pairing the first line with each `τ_j(w)` gives `Gram(τ) ν = 0`, so `ν = 0` whenever the
stabiliser is finite. A certified zero is therefore a genuine critical point on the whole sphere,
not only a stationary point of the slice. Krawczyk's theorem also makes every Jacobian in a
certified box nonsingular, so a degenerate orbit cannot certify; the degenerate arm below checks the
implementation, and soundness does not rest on it (F2). The value `924 r̂₆` is enclosed over the box;
the three targets' enclosures must be disjoint from each other and from the census values, in
particular from `237.6`, the pyramid and C3 ray.

**Certified Majorana constellation.** The six stars are found projectively (F1, F2). Each root of
the sextic is isolated in the chart where it is bounded, `z` with `|z| ≤ 1` or `ζ = 1/z`, as a
two-variable real Krawczyk box with the polynomial's coefficients enclosed from the critical box.
The six boxes must be disjoint on the sphere, which with degree six accounts for every root, each
simple. The boxes are mapped to the sphere and the fifteen squared chordal distances enclosed.

**Certified stabiliser.** The projective stabiliser of `[w]` is the symmetry group of its
constellation. Every symmetry induces a permutation of the six stars that preserves all fifteen
distances.

- *Upper bound* (F1): enumerate all 720 permutations. A permutation is excluded when some pair of
  corresponding distance enclosures is disjoint. Each survivor fixes an orthogonal map; one whose
  determinant enclosure excludes `+1` is a reflection and is excluded too. The stabiliser has at most
  as many elements as there are surviving rotations. The comparison is sort-free throughout; the
  per-star sums of distances, a symmetric function, serve as a quick pre-check (F2).
- *Trivial:* if only the identity survives, the stabiliser is `{1}`.
- *A named group `G`, lower bound:* rotate the representative so that `G` is in standard position and
  certify the critical point inside the character-fixed subspace
  `{w : D(g) w = χ(g) w for g ∈ G}` (F1), where every point has `G` in its stabiliser, with slices
  only for the continuous symmetries that preserve the subspace. By symmetric criticality it is
  critical on the whole sphere. If the number of surviving rotations equals `|G|`, the stabiliser is
  exactly `G`.

The full-sphere certificate and the fixed-subspace certificate are two separate proofs. That they
reach the same orbit is shown by overlapping enclosures of `924 r̂₆`, `|f|²`, `‖B₀‖²` and `Tr𝒩²`,
which is a cross-check, not a proof of identity, and is reported as such.

If a certificate does not close, the result is *not certified*, never *not critical* or *no
symmetry*. The report then gives the smallest singular value of the Jacobian at the centre and the
box radii tried (F2): near zero points to a degenerate orbit, a structural finding, and a
well-conditioned Jacobian that fails to contract points to the box size.

## Both sectors (F1, F2)

Each target is certified from both seeds. The two certified orbits must have overlapping
enclosures of `924 r̂₆`, `|f|²`, `‖B₀‖²` and `Tr𝒩²`, or the discrepancy stops the run.

## Controls, run before the targets

1. **Known groups** (F1): the census's pentagonal pyramid (`C₅`), trigonal prism (`D₃`) and D2 ray
   (`D₂`), from the same files, must certify as critical on the full sphere, certify in their
   character-fixed subspaces, and return exactly those groups.
2. **The two `C₂` leads** must return `C₂` exactly, or the discrepancy is reported.
3. **Perturbation arm** (F1): the pyramid, displaced by `10⁻⁶` in a generic direction and not
   re-solved, must return a trivial permutation certificate, showing that the test detects a broken
   symmetry. Refined from that displaced start, the full-sphere certificate must still certify the
   pyramid, showing the certificate does not need an exact input.
4. **Non-critical arm:** a random unit state, not refined, must fail to certify.
5. **Degenerate arm:** `v₀`, whose stabiliser is continuous, must fail under three rotation slices.

Each arm runs only after its unperturbed control passes.

**A limitation, stated in advance (F2).** No known critical point has a trivial stabiliser, so the
trivial path is never tested whole. Its two halves are tested separately: the full-sphere Krawczyk
certificate on symmetric critical points, and the permutation test on the displaced pyramid.

## Outcomes, and what § 7.2 may then say

| outcome for `238.0165` | § 7.2 |
| --- | --- |
| certified critical, stabiliser `{1}` | a certified critical orbit with trivial stabiliser, which [KU]'s symmetry-classification procedure cannot contain by construction; not located in the sources read |
| certified critical, stabiliser `G ≠ {1}` | stated with `G`; the "outside [KU]'s procedure" framing is dropped |
| not certified | a numerical critical point (gradient about `10⁻¹⁰`), not certified, with the diagnostic; the census's ceiling unchanged |

The two `C₂` orbits are reported the same way, with their certified value and group. Whatever the
outcome, M8.12's ten-orbit result stays exactly as scoped, and the three orbits mark its ceiling.

## Mechanics

One local script, `sources/certify_outside_orbits.py`, with its log beside it: controls and arms
first, then the targets. Its hash, the log's and this packet's travel in the report, with the inputs
re-hashed at run time. Nothing is filed anywhere.
