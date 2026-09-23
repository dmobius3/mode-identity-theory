# Work item 4c: certified inertia at the three outside orbits (packet, frozen for the run, 2026-09-22)

F2's hinge on 4b: a fixed set that contains the coherent state and the hexagon rules an orbit out only
as the *global* minimiser of the energy on that set. A numerical minimisation started nearby can stop
at a *local* minimum, and [KU] computed state C numerically, over complex `(a, 0, b, 0, c, 0, d)`
(`symmetry.tex` line 1020). The robust statement needs each orbit's signature restricted to its fixed
sets. The same computation certifies the full transverse splits `(n₋, n₊)` that work item 4 left
numerical (its `n₀ = 0` is certified already).

## Targets

For `T1`, `T2`, `T3`, certified inertia `(n₋, n₀, n₊)` of the second variation of `r̂₆`:

1. on the full transverse space, of real dimension 9;
2. restricted to the fixed set of the orbit's full isotropy group (real odd `m` for `T1` and `T3`, the
   real locus for `T2`, in the aligned frames of work item 4b), modulo its continuous symmetries;
3. for `T1` and `T3`, restricted to the fixed set of their unitary `C₂` alone, complex odd `m`: the
   domain [KU] minimised over for state C.

## Method

At a critical point on the unit sphere, with `H_L = Hess r − 2μG` and `B` the constraint gradients
(the sphere and the slices), the bordered-Hessian theorem gives
`In [[H_L, B], [Bᵀ, 0]] = In(H_L restricted to ker Bᵀ) + (m, 0, m)` when `B` has full column rank `m`,
and `H_L` restricted to `ker Bᵀ` carries the transverse signature. The bordered matrix is formed over
the certified box in interval arithmetic, congruent by the approximate eigenvectors of its centre
(Sylvester: any nonsingular congruence keeps the inertia), and each eigenvalue is placed by a
Gershgorin disc. If every disc excludes zero, the inertia holds for every matrix in the box, the true
one included, and `M` is nonsingular, which gives the full rank. The restricted versions use the same
construction in the fixed set's coordinates.

Reading at the two signs: at `g = 1` an orbit is a local minimum of the energy on a set exactly when the
restricted `n₋` is 0; at `g = −1`, exactly when the restricted `n₊` is 0.

## Controls and arm

The six finite-stabiliser census orbits must reproduce M8.12's exact signatures, from
`research/scripts/m8_12_author/s1_control_log.txt` on OpenWave's main: octahedron `(6, 0, 3)`,
hexagon `(9, 0, 0)`, pyramid `(5, 0, 4)`, prism `(3, 0, 6)`, C3 ray `(5, 0, 4)`, D2 ray `(5, 0, 4)`.
Arm: dropping the `−2μG` term must change the hexagon's certified signature.

Added before the run, each able to fail:

- a second arm at the hexagon, and a third at `T1` in its complex `C₂` subspace: without the slice
  columns the orbit directions are null, so no signature may be certified;
- each target's certified full split must agree with work item 4's reconnaissance split;
- each restricted certificate must carry the full certificate's fingerprint (same orbit), and its
  signature must sum to the restricted transverse dimension;
- block diagonality: the isotropy group fixes the point, so the second variation splits across a fixed
  set and its complement; the counts must nest (isotropy fixed set ≤ complex `C₂` subspace ≤ full,
  for `n₋` and `n₊` separately).

## Outcomes, and what § 7.2 may then say

| outcome | § 7.2 |
| --- | --- |
| every restricted `n₋ ≥ 1` and `n₊ ≥ 1` | no minimisation on those fixed sets stops at the three orbits, at either sign: the line-maxima mechanism, generalised |
| some restricted count is 0 | that orbit is a local minimum of the energy on that set at that sign, so a local numerical minimisation there, [KU]'s for state C included, can return it; the "not returned" claim then holds only in the literal reading of [KU]'s procedure (the minimum, line 243), stated with the line cited |

The full splits, once certified, replace the numerical ones, and the comparison of `T3` with the
octahedron is stated between a certified and an exact signature.

## Mechanics

`sources/certify_inertia.py` executes the definitions of `certify_isotropy.py` verbatim (and through
them those of `certify_outside_orbits.py`). Controls and arm first. Its log, its hash and this
packet's travel in the report.
