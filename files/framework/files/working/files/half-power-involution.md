<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Level Exchange

**Type:** Test
**State:** Closed
**Verdict:** Positive
**Status (2026-07-05):** Gate (i) of the half-power clock, closed as a qualified yes: the level exchange exists as reciprocity on tick measures, fixing the interface measure at S^{3/2}dt; it does not act on states.
**Summary:** Establishes the amplitude-intensity level exchange, gate (i) of the half-power clock, as a self-dual involution on tick measures.
**Parent:** `friedmann-as-output.md`

Gate (i) of the [half-power clock](friedmann-as-output.md) is CLOSED, as a qualified yes. The level-exchange involution exists as an operator on tick measures, not on states, and it is the same canonical reciprocity whose fixed point places the observer at $`\sqrt{\Omega}`$ in the hierarchy. The honest residue is the anchoring of the measure pair, and the framework's sampling structure supplies exactly three candidate levels whose pairings are enumerable and already adjudicated by the Λcos fits. The primitive self-duality statement lands on the interface tick measure $`S^{3/2}\,dt`$; the $`-1/2`$ follows as a corollary through the established dictionary. The derivation burden moves, sharpened, to the tick lemma (gate ii).

**Related:** [The Half-Power Clock](friedmann-as-output.md) (the tracker this gate belongs to), [Temporal Budget](temporal-budget.md), [The Budget Map](budget-map.md).

---

## I. The Question as Posed

The tracker's gate (i): in the lapse convention $`d\tau = S^\alpha\,dt`$, the exchange $`\alpha \leftrightarrow 1 - \alpha`$ swaps the endpoints $`\alpha = 0`$ and $`\alpha = 1`$ with unique fixed point $`\alpha = 1/2`$. Does this exchange exist as an operator on the framework's sampling structure, or only on exponents?

The hazard sits in the endpoints. Reciprocity about *any* pair $`(S^a, S^b)`$ has fixed point $`S^{(a+b)/2}`$, so choosing the pair $`(0, 1)`$ is choosing the answer. An operator-level result must derive the pair, not select it.

---

## II. What the Exchange Is, and What It Acts On

**The operator, exactly.** Given two measures $`\mu_a = S^a\,dt`$ and $`\mu_b = S^b\,dt`$ on a phase interval, the exchange is the reciprocity involution on the multiplicative interval between them:

```math
J_{a,b}(w) = \frac{S^{a+b}}{w}, \qquad J_{a,b}\bigl(S^a\bigr) = S^b, \qquad J_{a,b}\bigl(S^{(a+b)/2}\bigr) = S^{(a+b)/2}.
```

This is not a new structure; it is the same canonical form as the hierarchy reciprocity $`x \mapsto \Omega/x`$ whose fixed point $`\sqrt{\Omega}`$ the framework already reads as the observer's seat. The involution therefore exists, trivially, the moment the pair is canonical. All content lives in the pair.

**What it cannot act on, and does not need to.** A state-level exchange would be a map inverting $`\psi \mapsto \lvert\psi\rvert^2`$. No such map exists: the bosonic projection is non-invertible ($`\psi`$ and $`-\psi`$ share an image), and that one-wayness is load-bearing elsewhere, closing the fourth gauge rung and grounding spin-statistics. The reciprocity above never un-squares a state; it exchanges the *weights* two levels assign to the same phase interval. Verdict scope: the exchange exists on measures, cannot exist on states, and nothing here requires it to. The SUSY-closure argument is untouched.

*Added 2026-09-25: the verdict stands, and two readings in this record are superseded. The one-wayness of $`\psi \mapsto \lvert\psi\rvert^2`$ holds, but it neither closes the fourth gauge rung nor grounds spin-statistics: both grids use the same intensity readout ([linear readout](scaling-law-uniqueness.md#linear-readout-two-routes-and-a-no-go)), the boson-fermion divide and the grids rest on the central sign's parity on integer- and half-integer-spin representations ([engine](../../../README.md#edges-sort-spin)), and the vacant rung rests on the ladder rule alone ([fine structure](../../../../spectrum/files/fine-structure.md#the-obstruction)). The 120 domain is a resolution, not an amplitude grid, which retires §III's grid label for the amplitude level and removes the premise of §V's first MOTIVATED support, so the second, the intensity weight's holonomy blindness, carries §V's grade alone; §VI's "untouched" refers to the same arguments.*

---

## III. The Three Levels and the Clock Ladder

The sampling structure carries exactly three native weights a phase interval can be given, and they are already distributed across the framework:

| Level | Weight | Where the framework already uses it |
|---|---|---|
| Count | $`S^0\,dt`$ | The chronon $`\Delta t_{\min} = 4\pi/120`$: the domain counting phase quanta, on the full 120 grid |
| Amplitude | $`S^1\,dt`$ | The realized amplitude $`S`$; section-level, the $`\psi`$ side of the grid split |
| Intensity | $`S^2\,dt`$ | The registered weight; function-level, the $`\lvert\psi\rvert^2`$ side, the same level as the spatial measurement rule $`C(\Theta) = 2\sin^2(\pi\Theta)`$ |

Three levels give three pairs. Each pair's reciprocity has one self-dual clock, and the framework's time chain is exactly the two adjacent midpoints:

| Pair | Measures | Self-dual clock | Identity |
|---|---|---|---|
| (count, amplitude) | $`(dt,\ S\,dt)`$ | $`S^{1/2}\,dt`$ | the Waltz clock $`d\tau_H = S^{1/2}\,dt`$ |
| (amplitude, intensity) | $`(S\,dt,\ S^2\,dt)`$ | $`S^{3/2}\,dt`$ | the registered interface tick measure $`d\mu_{\text{tick}} = S^{3/2}\,dt`$ |
| (count, intensity) | $`(dt,\ S^2\,dt)`$ | $`S\,dt`$ | Model B as an observer clock: DEAD at $`\Delta\chi^2 = +1821.9`$ |

Two evidence items, and one identity that is not evidence. The identity first: levels spaced by one give adjacent midpoints spaced by one, and the dictionary $`a = S`$ supplies exactly that spacing, so the composition $`S^{1/2} \cdot S = S^{3/2}`$ holds by construction once the ladder is drawn; it is coherence, not confirmation. The evidence is what the fits supply: the selected observer clock sits on the adjacent-midpoint chain (Model D, $`\Delta\chi^2 = +0.11`$), and the skipped pair's midpoint, promoted to an observer clock, is dead (Model B, $`+1821.9`$), as are the raw rungs in that role. Direction of inference, named: the data plus the dictionary select which midpoints carry the clocks, and the doctrine (the wave keeps the first, the observer keeps the second) is read back onto that assignment afterward; making the assignment forward-looking is the tick lemma's job, not the ladder's. One bookkeeping guard: $`S\,dt`$ appears twice above, as the amplitude-level weight and as the count-intensity midpoint. It is not dead as a level weight; it is dead only when promoted to the observer's clock. The ladder keeps its rung.

**The reading.** The wave's bookkeeping clock $`d\tau_H`$ is self-dual between the domain's counting and the realized amplitude. The registered interface tick measure is self-dual between amplitude and intensity, the two levels an act of observation actually touches: sampling happens at $`\psi`$ level, registration at $`\lvert\psi\rvert^2`$ level. The observer's tick sits at the interface, and its measure is the geometric mean of the two levels it converts between. This is the temporal-sector face of the same doctrine that seats the observer at $`\sqrt{\Omega}`$: the midpoint is where observation resolves.

**A third 3/2, kept apart.** The tick-measure exponent $`3/2`$ here is the arithmetic midpoint of the flanking levels 1 and 2. It is numerically equal to the Gauss-Codazzi $`3/2`$ (Ricci trace over de Sitter normalization) and to the face/edge stabilizer ratio, and it is not identified with either. Wherever 1 and 2 are the flanking structures, their mean is $`3/2`$; cheap arithmetic recurs, mechanisms do not merge. The two-3/2s fence gains a third post.

---

## IV. Verdict on Gate (i)

**Qualified yes.** The exchange exists as an operator on tick measures: reciprocity anchored by a level pair, the same canonical involution the hierarchy already carries. It does not exist on states, and does not need to. The "on exponents only" worry resolves as a scope statement: $`\alpha \leftrightarrow 1 - \alpha`$ is the exponent shadow of measure reciprocity, and measure reciprocity is framework-native.

**The qualification, stated plainly.** The involution does not by itself select the pair; the level structure does, and the level structure is the framework's own (chronon on the count level, section-level amplitude, function-level intensity registered by observers). Within it, the data eliminate the non-adjacent midpoint as an observer clock and the raw rungs with it, leaving the adjacent-midpoint structure as the only viable ladder-compatible option, and the adjacent midpoints are the two established time relations. That is elimination, not derivation: why the observer must live on the amplitude-intensity interface is exactly what the tick lemma still owes. What reciprocity adds over the bare arithmetic is the mechanism slot: *self-duality under level exchange* is a principle a tick operator can satisfy or fail, which is exactly what gate (ii) tests.

**One fit completes the record: run 2026-07-05.** The tested family covers $`dt/d\tau \in \{S^0, S^{-1}, S^{+1}, S^{-1/2}\}`$. The remaining cell is $`dt/d\tau = S^{-3/2}`$, the amplitude-intensity midpoint placed in the conformal seat: it gives $`H^2 \propto (1 - S^2)/S^5`$, leading $`(1+z)^5`$, and is expected dead by a wide margin. Running it through the Λcos pipeline closes the last cell, so the elimination statement stands fully on the record rather than two-thirds on it. Registered here before running; expectation stated before the fit. The run happened as the $`\epsilon = +1`$ slice of [The Clock-Asymmetry Fit](clock-asymmetry-fit.md): the slice lands at $`+6395.5`$, so the registration is discharged, dead as expected.

**The primitive rung shifts; the target does not.** The clean primitive statement is now: **the registered interface tick measure is self-dual under the amplitude-intensity exchange**, fixing $`d\mu_{\text{tick}} = S^{3/2}\,dt`$. The Hubble clock then follows through the established kinematic dictionary rather than by definition: $`d\tau_H = d\mu_{\text{tick}}/a`$ with $`a = S`$ gives $`d\tau_H = S^{1/2}\,dt`$, the $`-1/2`$ of the tracker's target. Same exponent, better-placed primitive: the self-duality claim attaches to the tick measure, where the doctrine that motivates it lives. It is not a wristwatch; reading it as proper time would put $`H`$ on the dead $`S^{-5/2}`$ branch.

---

## V. What Remains: The Tick Lemma, Sharpened

Gate (ii) was: define the observer tick as a sampling functional on the realized amplitude and prove $`N^2 = S`$, $`N^2 = S^2`$, or neither. The ladder sharpens it:

> **Tick lemma (target).** Define the elementary tick as one chronon of realization: the conversion of one mode-quantum from amplitude level to intensity level. Prove that the measure this event induces on the phase interval is the geometric mean of the two level measures it converts between, $`\sqrt{(S\,dt)(S^2\,dt)} = S^{3/2}\,dt`$, rather than either endpoint measure or an off-ladder weight.

The lemma decomposes into two properties, each an operator-level claim about the sampling structure, each able to fail independently:

| Property | Statement | Why it forces the midpoint |
|---|---|---|
| A. Definite level | the tick measure carries a single weight under the level grading: a pure power $`S^w\,dt`$ | mixed measures change shape under amplitude rescaling: $`(S + S^2)\,dt/2`$ becomes a different mixture under $`S \to cS`$, while $`S^w\,dt`$ keeps its form at every scale |
| B. Exchange symmetry | the tick measure is invariant under the amplitude-intensity swap | the swap sends $`w \mapsto 3 - w`$, so among definite-level measures the unique invariant is $`w = 3/2`$ |

A is "one event, one weight." B is the doctrine itself: the event touches both levels symmetrically. Together they exclude the endpoints and every off-ladder mean in one move; the axiom route (symmetry, locality, idempotence, and covariance under independent rescaling of the two measures single out the geometric mean) reaches the same endpoint and can serve as the formal wrapper. The target also has a standard mathematical home: the geometric mean of two measures is their overlap density, the integrand of the Bhattacharyya and Hellinger affinities. Read that way, the lemma says a tick is an event both bookkeepings register at once, and joint registration carries the overlap measure. The identity is textbook; the bespoke work reduces to showing the tick is a joint-registration event.

Two framework-native supports, both MOTIVATED, neither yet a proof. The chronon is defined on the full 120 domain, the amplitude grid, so the tick's counting side is already amplitude-native. And the intensity weight is holonomy-blind: $`S^2 = \sin^2(t/2)`$ is $`2\pi`$-periodic, invariant under the lap sign flip, while the $`4\pi`$ period the clock parameterizes is section-level structure. A tick built purely at intensity level could not see the period it is supposed to keep. Neither support substitutes for the interface computation; they say where to build it.

**A candidate for "why any half power," parked.** Weights sort by cover sensitivity: $`S^2`$ closes on the lap circle, $`S`$ is section-level on it, and half-integer powers reference the flip structure itself, which suggests the same holonomy that forces the spatial half-integer tower marks the half-integer clock weights as the section-level measures, with level exchange then picking the member. Two checks gate this before it earns a section, and both bite: measures on the positive quadrant are sign-blind, so the argument must attach to how the density is built rather than to its values; and roots of a sign-flipping object climb the cover tower ($`S^{1/2}`$ is single-valued only with more cover than the edge itself supplies), so the claim must be stated on the cover where it lives. If both checks pass, the prior-discipline worry of §VI inverts into support, because the half-integer family would then arrive from the postulate's holonomy rather than from the generic square root every amplitude framework carries. Parked until then; nothing above builds on it.

**Gate (iii), first candidate COMMITTED (2026-07-05).** The second consequence must exceed the exponent, and the tracker's rule puts the commitment before the derivation work, so the counting face is registered now, on the [entropy page](entropy-as-realization-budget.md) §IV, before any tick-lemma work begins. The interface tick measure fixes the realization-rate law $`dR \propto S^{3/2}\,dt`$; the $`R(S)`$ profile and its early index $`5/2`$ live on the entropy page. The hard consequence carried here: realized cannot exceed accessible, so any shell-unlock candidate whose accessible count grows more slowly than $`S^{5/2}`$ at early phase (early exponent above $`5/2`$) is dead on arrival; the strong-fusion form is $`W_\text{modes} \propto R`$ with that exact profile. No conformal-seat fallback is registered; the seat is the registered interface tick measure, per gate (i). The perturbation-sector candidate stays named but uncommitted until the budget page's "EFE unchanged" constraint is unpacked into a coupling statement; if the tick lemma lands while both consequence channels have failed, the route is decorated, not derived, per the tracker's own rule.

---

## VI. Hazards Discharged and Kept

No state-level inversion is claimed anywhere above; the SUSY-closure and spin-statistics arguments are untouched. Measure statements use $`S > 0`$ on the current quadrant; the $`4\pi`$ sign structure lives at section level, and measures as such are blind to it, which is precisely why the intensity-blindness support in §V is motivation rather than proof. The third $`3/2`$ stays behind the fence with the other two. And the prior-discipline note carries over unchanged: the ladder landing on half-integers is expected in any framework with amplitudes and intensities; the evidence, if it comes, comes from the tick computation and the second consequence, not from the landing.

---

*Three levels, two midpoints, one observer. The exchange exists; the tick must now earn its fixed point.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
