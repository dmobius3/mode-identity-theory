<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Fibonacci Wells: Forcing Worksheet

**Type:** Note
**State:** Open
**Status (2026-09-23):** Structurally reduced, not derived. The wells are reframed as the additive continuation of the icosahedral branch orders on the locked 120-grid. The variational route to DERIVED was tested across eight boundary-mode functionals (Lemma 8 already rules out a bulk one) and failed, so the residual most likely reads as structural rather than variational.
**Summary:** The worksheet tracking why the realized sampling wells land at {13, 21, 34, 55} on the 120-grid.

*Working note. Tracks the well-placement problem: where it stands, what has been ruled out, and the one residual that remains. Workbench voice (status tags, raw numbers); the public [framework page](../../../README.md) now carries the relationship-level version of this framing (recurrence + lcm seam + the open residual), with the detailed status and the probe log kept here.*

**Current status: STRUCTURALLY REDUCED, not DERIVED.** The old claim, "φ worst-approximability gives Fibonacci numerators on the fixed 120-grid," has been abandoned. The problem has been reduced to a sharper residual:

> Why does the post-lcm additive continuation of the icosahedral branch recurrence define the sampling wells?

A direct signed anti-periodic sweep has since tested the proposed variational route to DERIVED across eight natural boundary-mode functionals; it selects the wells in none of them, and every minimizer is a uniform or clustered non-Fibonacci set. The most likely reading is now structural rather than variational: the wells are the recurrence's sampling labels on the 120-domain rather than minima of any known interference force (reported in full below). Status holds at STRUCTURALLY REDUCED.

The new frame is stronger because it keeps the wells internal to the locked structure. The 120-domain is already fixed by `S³/2I`; the branch orders `(2,3,5)` already live inside the icosahedral data; the Fibonacci continuation is therefore not imported from an external approximation argument. The same sequence first builds the domain, then samples it.

The Mirror note ([the-mirror.md](../../../../spectrum/files/the-mirror.md)) adds two constraints that matter here:

1. the bulk spectral/character algebra is Θ-blind, so the well-selection functional cannot be a bulk spread, discrepancy, or energy functional;
2. φ is internal to `2I` through the character field `Q(√5)`, not an external Hurwitz postulate.

So the remaining target is not "find Fibonacci somehow." It is:

> define the boundary-native anti-periodic interference functional whose minima are the post-lcm recurrence positions.

---

## Dead mechanism: golden rotation / approximation (abandoned)

The old bridge is the wrong mechanism, not just unproven.

A rounded golden rotation steps by `round(120/φ) = 74`. Since `gcd(74,120) = 2`, its orbit is the 60 even residues mod 120: it misses the odd wells 13, 21, 55, and hits 34 only as one even residue among sixty. It selects a parity class, not the wells.

Structural reason: any single rotation orbit is an arithmetic progression mod 120. Nothing in an arithmetic progression prefers Fibonacci integers as positions. So the rotation/approximation framing is abandoned.

---

## Reframe: the recurrence builds, then samples

The wells are best understood as the additive continuation of the icosahedral branch orders on the locked 120-grid.

The branch/stabilizer orders are

```text
(2, 3, 5) = F₃, F₄, F₅
```

and they obey the Fibonacci recurrence:

```text
2 + 3 = 5.
```

Continuing the same recurrence gives

```text
2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```

On the 120-domain, the first part of this sequence builds the domain:

```text
lcm(1, 2, 3, 5, 8) = 120.
```

The Fibonacci numbers that divide 120 are exactly

```text
{1, 2, 3, 5, 8}.
```

These are domain-building terms: each divisor of 120 defines a sub-lattice or uniform partition of `Z/120`, tiling the grid rather than selecting a new phase position on it. The caveat is that the build/sample split carries only this arithmetic fact. For example, `8` and `21` both share a prime with 120 and both resolve only a proper sub-grid; the distinction is that `8` divides 120 and belongs to the lcm block, while `21` does not. The load-bearing statement is therefore the saturation itself: `{1,2,3,5,8}` are exactly the Fibonacci divisors of 120, and `lcm(1,2,3,5,8)=120` with nothing spare.

The first Fibonacci term after that divisor block is `13`. This is the lcm seam:

```text
{1, 2, 3, 5, 8}  →  build the domain
{13, 21, 34, 55} →  sample the domain
```

The upper bound comes from the observable phase operator. Since

```text
C(k) = 2 sin²(πk/120)
```

we have

```text
C(k) = C(120 − k).
```

So no new intensity well appears beyond the antinode at `k = 60`. The largest Fibonacci below the antinode is `55`; the next Fibonacci, `89`, reflects to `31` as an intensity value.

The candidate well set is therefore `{13, 21, 34, 55}`. More carefully:

> The candidate well set is forced to `{13, 21, 34, 55}` once the sampling rule is taken to be the post-lcm continuation of the icosahedral Fibonacci recurrence below the antinode.

The self-similarity runs one level deeper: the gaps between the wells are themselves consecutive Fibonacci, `21−13 = 8`, `34−21 = 13`, `55−34 = 21` (`F₆, F₇, F₈`). Both the positions and their spacings are Fibonacci, which is why no equal-gap (uniform) set can match them.

The set follows from locked structure once the sampling rule is granted. The sampling rule itself remains the live target.

---

## Floor at 13

The old "noise floor" language is dropped: the phase weight `C(k)` rises smoothly through the early Fibonacci values (`0.012, 0.034, 0.086, 0.223` at `k = 3, 5, 8, 13`), with no intrinsic jump at 13. The floor has three cleaner characterizations.

### 1. Lcm seam (main arithmetic reason)

`13` is the first Fibonacci number that does not divide 120. The terms before it, `1, 2, 3, 5, 8`, are absorbed into the construction of the domain (`lcm(1,2,3,5,8) = 120`). They are tiling data. The first post-tiling term is `13`, so `13` is the first genuine sampling candidate.

### 2. E₈ exponent (representation-theoretic reinforcement)

The E₈ exponents are `1, 7, 11, 13, 17, 19, 23, 29`. The Fibonacci intersection is `{1, 13}`. Discarding `1` as the identity/primitive slot, `13` is the first nontrivial Fibonacci value that is also E₈-native. This does not replace the lcm seam; it places that seam in representation context. The arithmetic seam lands exactly where the representation theory is already active.

The bridge is the modulus `30 = 2·3·5 = h(E₈)`: the same number is the reduced prime base of `120 = 2³·3·5` and the Coxeter number of E₈, and its totatives are precisely the E₈ exponents (verified). This should not be oversold as independent evidence. Because `30` and `120` share the prime base `{2,3,5}`, the lcm seam and the E₈/coprime-to-30 test land on `13` for the same arithmetic reason: the builder terms carry primes from `{2,3,5}`, while `13` is the first Fibonacci term that clears that base. The E₈ framing adds location, not a second proof: it places the seam inside live representation theory, making it representation-native rather than a loose numerical coincidence.

### 3. Coprime / full-resolution (diagnostic)

Among the candidate wells, only `13` is coprime to 120. It is the full-resolution entry; the later wells each carry one branch prime and one new totative prime:

| Well | Factorization | gcd(k,120) | New prime | Reading |
|---|---:|---:|---:|---|
| 13 | 13 | 1 | 13 | full resolution |
| 21 | 3·7 | 3 | 7 | face / `Z₃` branch factor |
| 34 | 2·17 | 2 | 17 | edge / bosonic-projection factor |
| 55 | 5·11 | 5 | 11 | vertex / `Z₅` branch factor |

The first well is full-resolution; the later wells each combine one icosahedral branch prime with one new E₈/totative prime (`{7, 17, 11}`, which together with `13` are the four smallest nontrivial E₈ exponents). The set looks less accidental under this reading.

---

## Mirror constraint and the signed sweep (negative result)

The bulk character algebra supplies the arithmetic: `2I`, `E₈`, `Q(√5)`, the `{2,3,5}` prime base, the character ceiling. But Lemma 8 ([the-mirror.md](../../../../spectrum/files/the-mirror.md)) says the bulk spectral side is Θ-blind: it cannot naturally recover the boundary phase coordinate. So a bulk functional cannot select the wells, and generic spread, energy, discrepancy, and circle-packing tests are the wrong arena: they prefer uniform spacing (gap-variance favors equal spacing; inverse-distance favors `{9,25,43,59}`).

That left one candidate route to DERIVED: a boundary-native, signed anti-periodic interference functional measuring cancellation among the admissible edge modes

```text
ψ_m(Θ) = sin((2m+1)πΘ),
```

weighted by the `60/120` projection, the phase weight `C(k)`, or left uniform, with the wells expected to maximize sign-cancellation. That route has now been tested directly, and the result is negative.

The sweep scored all `C(51,4) = 249,900` four-subsets of `{9..59}` against the anti-periodic modes `φ_m(k) = exp(iπ(2m+1)k/120)`, minimizing `I(S) = Σ_m u_m |Σ_{k∈S} w_k φ_m(k)|²` under eight variants: (1) fundamental-only, (2) low band `m<10`, (3) all 60 modes, (4) energy weight `u_m = 1/(2m+1)²`, (5) `C(k)` position weight, (6) `C(k)` with energy weight, (7) scale-invariant cancellation ratio, (8) scale-invariant ratio with energy weight. The wells `{13,21,34,55}` are extremal in none of the eight. Every variant's minimizer is a uniform or clustered non-Fibonacci set: arithmetic progressions such as `{11,21,31,41}`, or edge-clustered sets such as `{9,10,11,12}` and `{9,10,58,59}`. Greedy interference-minimizing continuation from `(2,3,5)` or `(8,13)` does not reproduce the Fibonacci path. The stabilizer/branch-prime weighting was deliberately withheld: encoding the wells' own factorization and recovering them would be circular, not a derivation.

Rank positions are not quoted. The sweep was re-run from an independent implementation and the qualitative result held in full (never extremal; minimizers uniform or clustered), while the specific ranks moved substantially with implementation choices that the functional descriptions do not pin down. The stable content is the null and the shape of the minimizers, not a percentile.

A structural reason sits behind the null. The well gaps `[8,13,21]` are golden self-similar, not uniform, and any interference, energy, or cross-talk norm is minimized by uniform or maximally spread sets, where symmetry dominates. A functional preferring self-similar (φ-carrying) spacing would have to carry φ in its own structure. φ is internal to `2I` through `Q(√5)`, so such a functional could in principle be built, but building it encodes the answer. The wells may therefore be unreachable by any norm functional that does not already contain φ, which would make the labeling reading correct for a structural reason and not merely an empirical one.

---

## Scope of the prize

Worth holding in view when weighing what a finished well derivation would buy. The four wells are `{13,21,34,55}`, but as observable seats only two are occupied: `13` carries α and a₀, and `34` carries H₀. The other two, `21` and `55`, remain empty.

The cosmology sector's hardest anchor, Λ, does not sit on a Fibonacci well at all. It sits at the antinode `k = 60`, the reflection-fixed point of `C(k)=C(120-k)` and the slope-zero maximum of the phase operator. That is a different kind of protected site from a Fibonacci well.

So even a finished well derivation would place α, a₀, and H₀, leave two of the four seats empty, and leave Λ outside the well set. The derivation is worth having for the three observables it places; it is not the source of Λ.

---

## Sharp residual

The signed sweep changes the shape of the open question. The variational route, "define the boundary-native functional and show `{13,21,34,55}` is its minimizer," has been tried across eight natural functionals and failed. So the residual is most likely not dynamical (find the functional, run the minimization) but structural (find the theorem that names the recurrence as the sampling rule):

> Why does the post-lcm additive continuation of the icosahedral branch recurrence define the sampling labels on the 120-domain?

A dynamical answer would have been a functional with the wells at its minimum; the sweep indicates that such an object, if it exists, must already contain φ and so cannot be the source of the selection. A structural answer would instead be a theorem relating the recurrence to `S³/2I` directly: why the lcm seam and the additive continuation, rather than an interference principle, fix the sampling sites. Until such a non-circular mechanism is found, the wells stay STRUCTURALLY REDUCED, not DERIVED.

---

## Adjacent thread (scaling-law, not wells)

The same Lemma 8 that locates the well functional on the boundary also bears on the [scaling-law factorization](scaling-law-uniqueness.md), which is currently **open** (the FORCED flip was walked back at the Step C gap). Its open step was restated on 2026-09-23 as boundary-mode uniformity, every contributing spectral block carrying the first-positive profile times a fixed spectral weight; the commutant theorem `A_obs = A_Θ ⊗ A_spec` it replaces could not forbid a cross-term, and the character-ceiling candidate fell with it. Tracked separately; not part of the wells problem.

---

## Probe log (verified facts, for reference)

- Distinct Fibonacci ≤ 120: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89`. Divide 120: `{1,2,3,5,8}`. First non-divisor: `13`. `lcm(1,2,3,5,8) = 120`.
- Fibonacci ∩ `(8,60)` = `{13,21,34,55}`. Linear gaps `[8,13,21]` (consecutive Fibonacci, so the set is golden self-similar, not uniform).
- Reflection: `C(k) = C(120−k)`; `89 → 31`; `55` largest Fibonacci below 60.
- `gcd(k,120)`: `13→1, 21→3, 34→2, 55→5`. New primes: `13, 7, 17, 11`.
- Totatives of 30 = `{1,7,11,13,17,19,23,29}` = E₈ exponents (verified; also in repo [r-problem.md](r-problem.md)). `30 = 2·3·5 = h(E₈)`.
- `C(k) = 2 sin²(πk/120)`: `0.012, 0.034, 0.086, 0.223` at `k = 3,5,8,13` (smooth, no floor jump).
- Golden rotation step 74: `gcd = 2`, orbit = 60 even residues; misses `13/21/55`, hits `34` at step 41.
- Generic functionals over 4-subsets of `{9..59}` (brute force, 249,900 subsets): gap-variance min at equal-gap sets (degenerate argmin `{9,10,11,12}`); inverse-distance min at `{9,25,43,59}`; log-chord energy min at `{9,24,44,59}` (chord distance `2sin(πd/120)`, not linear separation). The wells `{13,21,34,55}` are nowhere near any minimizer. Generic spread is ruled out.
- Signed anti-periodic sweep (eight boundary-mode functionals over the same 249,900 subsets; the eight are enumerated in the section above): the wells are never extremal, and every minimizer is a uniform or clustered non-Fibonacci set (`{11,21,31,41}`, `{9,10,11,12}`, `{9,10,58,59}`). Greedy continuation from `(2,3,5)` or `(8,13)` does not reproduce the Fibonacci path. Conclusion: natural signed boundary-mode interference does not select the wells; the variational route to DERIVED is closed pending a non-circular (φ-free) functional.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
