# M8.15.x step 1: the 2a survey, recorded (2026-10-08)

This is memo v4's § 2 survey, run before any control is frozen. It is continuum mathematics on public spectra, and no solver or target run is involved. The script is `continuum_overlap_survey.py`, and its output is `survey_v1.out`.

## Validation

The script is an independent implementation, and it reproduces every figure the review published:
- T1: 0.968 on the rotations and 0.000 on the fibre and partner directions;
- T2's slowest doubled pair: 0.641;
- T4: 0.996 and 0.870;
- `v₁`: 0.996.

One review unit also re-derived the pyramid's and the C3 ray's figures independently, from M8.12's census table. Two further checks:
- **The zero clusters** match the census zero multiplicities for every orbit, with a clean gap: the largest zero-cluster modulus is at most `1.5×10⁻⁷` of the maximum, and the smallest genuine one at least `0.0057` of it.
- **The normalization** matches the frozen spectra: at unit `u`, `v₂`'s smallest `τ` is `0.043512`, which is `56/1287`.

## Candidates for 2a

A candidate is an orbit that is neither a target nor an M8.15 control, is nondegenerate, and has a genuine slow mode inside the structural span.

| Orbit | Slot | In-span genuine mode | Overlap with `U` | Notes |
|---|---|---|---|---|
| **Pyramid** | R4 (R5) | imaginary, Krein − | 0.997, all on the rotations | Hyperbolic at small amplitude: a quartet sits at 1.19× the in-span mode's modulus |
| C3 ray | R4, R5 | a quartet | 0.981 | |
| Weight 3/2 | R2 | imaginary, Krein − | 0.994 | Elliptic only at the member with complex structure `i`, hyperbolic along its `Sp(1)` family; type (b), unstable members |
| Weight 5/2 | R2 | imaginary, Krein − | 0.965 | The same: elliptic only at the `i` member, hyperbolic along the family; type (b) |

Any R2 arm must name its member and register type (b), from the Result's § IV table.

Rejected:
- **`v₀`, the coherent orbit and the octahedron** have no genuine mode inside the span. The octahedron is M8.15's C3.
- **`v₁`** is degenerate.
- **The D2 ray's** real pairs overlap the span at 0.48 to 0.58.

**The two other outside orbits: closed, not surveyed.** The Result says they "are not certified, and nothing here uses them" (`soft-slot-branches.md` § IV). An armed control needs a known answer, so an uncertified orbit is ineligible for 2a without a Krawczyk certification first, which this memo does not scope. Their representatives also come from M8.12's census probe, not from its ten-orbit table. One review unit asked for them to be sourced, and the other to close the item; it is closed for that reason.

## The choice: the pyramid in R4

The pyramid in R4 is frozen as 2a's control. Weight 3/2 in R2 and the C3 ray are optional secondary arms, and are not needed to qualify the rule.

Three conditions are registered with it:
1. **It has T4's lift structure.** The pyramid has a nonzero `J` along its 5-fold axis, and rotation about that axis is not a phase on it. So that rotation is a continuous direction inside the fixed space, as at T4. Its standing waves therefore need § 1b's angle solve, and **2a qualifies after § 1b, not alongside it.**
   - The pyramid also serves as § 1's control, for both 1a and 1b. A bench check at level 2 settled this on 2026-10-08:
     - the slice's M-cosine with the phase direction is 0.1581;
     - at the oriented seed `ν ≈ 10⁻¹⁵`, so the seed angle is a symmetric critical point;
     - started off that angle, the slice carries a real force with that phase overlap.

     So the pyramid arms 1a off its critical angle, and 1b from there back to a critical point (`REGISTER_1.md`).
2. **Its expected outcome includes the quartet.** The pyramid is hyperbolic at small amplitude, with `k_c = 1`. The quartet lies at `τ = 0.07384` against the in-span mode's `0.06223`. The matching within each Krein class must keep them apart, and that is part of the registered answer.
3. **It is resolved at `ε_min` in R4.** Checked:
   - **R4:** `Q = 1.18462` and `|λ| = 2.37×10⁻⁴` at `ε = 0.25`, against `10 τ₀⁽³⁾ = 1.04×10⁻⁴`. That is resolved, with a margin of 2.3.
   - **R5:** the margin is only 1.4, which is why R4 is used.

## Code order

Revised from memo v4 by the lift-structure finding above:
1. § 4, a record on every end, with its armed controls;
2. § 1a, the stopping test, with control 1a;
3. § 1b, the angle solve, with control 1b, which may be the pyramid;
4. 2a on the pyramid;
5. the rest of § 2, then qualification (§ 6).
