<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Variational Score-to-Sample Program

**Type:** Program
**State:** Open
**Status (2026-09-23):** WORKING / MOTIVATED, parked. The first clock arm has run, recorded at `variational-clock-arm.md`: in the class of §11 the lapse equation is solved and the variation selects no level, since the potential's level sets the lapse, so the independent route fails and the half power returns only as R-HALF's operator realization, below the promotion bar. The program is parked on what that leaves, why the potential carries amplitude weight (§16): no search is run, the §13 arms stay closed behind the clock gate, and a standing admission bar governs any later proposal. The pre-registered PASS/FAIL stands unchanged.
**Summary:** Frames the dynamics problem as a variational principle for the global score-to-sample relation; the program page for the variational reading, which works the exponent derivation rather than waiting on it.
**Inputs:** `postulate-bridge.md`, `temporal-budget.md`, `friedmann-as-output.md`, `stress-tensor-bridge.md`, the engine (chronon, sign flip, Hubble clock)

WORKING / MOTIVATED. Ledger effect: none. Engine effect: none. The first clock arm has run, recorded at [The Variational Clock Arm](variational-clock-arm.md): in the class of §11 the lapse equation is solved and the variation selects no level, so the independent route fails and the half power returns only as R-HALF's operator realization. The program is parked on the question that leaves, why the potential carries amplitude weight, under a standing admission bar (§16). No functional outside that class is fixed. The page fixes the corpus conventions any candidate must respect, states the two-level action architecture, names the one bounded computation, and pre-registered its PASS and FAIL conditions before the run. This is the working program behind the variational reading recorded on the [postulate bridge](postulate-bridge.md).

**Primary promotion gate:** derive the observer lapse $`N = S^{1/2}`$ from the native global functional, without inserting the exponent by hand.

**Related:** [The Waltz](../../../../spectrum/files/the-waltz.md) (the eight-functional well sweep, the recorded null this program must not repeat), [Sampler first test](sampler-first-test.md), [The Tick Lemma](tick-lemma.md), [The Level Exchange](half-power-involution.md).

---

## 1. Purpose

MIT already carries a global wave/history structure. The open problem is to select and descend the relation among the global wave, the embedding, the sampler, the connections, and the observer chart.

The program target is a native global functional coupling:

- the wave / budget fields;
- the embedding $`i`$;
- the sampler $`\mathcal O_M`$;
- the relevant flat and matter connections;
- and, at Tier 3, the metric response.

The observer-chart action is downstream:

```math
\mathcal{S}_{\text{MIT}}
\longrightarrow
\text{sampled local state}
\longrightarrow
\mathcal{S}_{\text{eff}}[g,\text{sampled fields}]
\longrightarrow
\text{Einstein field equations}.
```

$`\mathcal{S}_{\text{eff}}`$ descends from $`\mathcal{S}_{\text{MIT}}`$.

## 2. Fixed corpus conventions

Use the corpus symbols:

```math
\Psi=\cos(t/2), \qquad S=\sin(t/2)
```

for the existing on-shell budget solution.

$`t`$ is the native phase parameter.

The observer Hubble-clock variable is $`\tau_H`$, with general lapse

```math
d\tau_H=N(t)\,dt.
```

The currently used clock is

```math
N(t)=S(t)^{1/2}.
```

That exponent is not unclaimed ground. It is labelled FORCED on the [budget page](temporal-budget.md) §VII, forced by $`S^3`$ dimensionality plus GR, and [The Half-Power Clock](friedmann-as-output.md) has already landed it natively along its route R-HALF, conditionally on that route's premise ledger. This program is a second route to the same number.

Two prerequisites are inherited with the symbol, and neither is discharged here. First, §7 varies $`N`$, which gives it the role of a metric lapse against the phase metric, $`g_{tt} = -N^2`$; that is the Half-Power Clock's gate (iii) perturbation-sector candidate, which stands named but uncommitted until its EFE-unchanged constraint is unpacked. Second, the [placement seam](friedmann-as-output.md) recorded 2026-09-01 leaves the semantic identification open: whether $`d\tau_H`$ is observer proper time in the effective metric, and whether the native pair $`(d\mu_\text{tick}, d\tau_H)`$ maps onto GR's proper/conformal pair at all. So the variational lapse and the fitted Hubble clock share a name and a law before they are shown to share an object. The first bounded computation must keep them distinguishable rather than assume the identification.

The descriptive chain is

```math
t \longrightarrow \tau_H(t) \longrightarrow q(\tau_H).
```

Time is phase advance; motion is change of resolved state under it.

## 3. Phase domain and Möbius sign

The one-lap phase interval has length $`2\pi`$ and carries the sign flip

```math
\Psi(t+2\pi)=-\Psi(t).
```

The closed edge traverses two laps, has phase length $`4\pi`$, and returns the field to itself:

```math
\Psi(t+4\pi)=\Psi(t).
```

Quadratic quantities satisfy

```math
\lvert\Psi(t+2\pi)\rvert^2=\lvert\Psi(t)\rvert^2,
```

so a quadratic functional on the closed $`4\pi`$ edge descends to the single $`2\pi`$ lap.

This descent forgets the Möbius orientation sign.

That $`\mathbb{Z}_2`$ is distinct from the central $`-I`$ of $`2I`$, whose parity on integer- and half-integer-spin representations separates the 120 and 60R resolutions in the matter-side representation structure. Squaring erases both signs by the same algebraic operation but does not choose the grid; the two $`\mathbb{Z}_2`$ structures are different objects.

A term that must retain Möbius orientation information must therefore retain data erased by $`\Psi \to -\Psi`$.

## 4. Existing variational foothold

The anti-periodic temporal sector already contains a variational statement.

On the one-lap problem with anti-periodic boundary condition,

```math
\Psi(t+2\pi)=-\Psi(t),
```

the functions

```math
\cos(t/2), \qquad \sin(t/2)
```

span the Rayleigh-quotient ground space of the quadratic form

```math
Q[\Psi]=\int \lvert\Psi'(t)\rvert^2\,dt.
```

The phase condition

```math
\Psi(0)=+1
```

selects the physical phase convention.

The program therefore starts from an existing quadratic variational structure rather than from nothing. The Rayleigh form is the wave sector alone: it contains no $`N`$ and no independent $`S`$, and its ground space is a fact about one eigenproblem on one lap. The first arm adds the lapse and the budget constraint to that sector and nothing else. Whether any coupling to $`i`$, $`\mathcal O_M`$ or $`A`$ survives is the open content of the later arms, and it is open against recorded negatives rather than against blank space: the postulate bridge's Steps 1 through 4 and the [sampler first test](sampler-first-test.md) both closed negative on those couplings. Continuity from this quadratic form to a functional over sampler, embedding and connection data is a claim the program owes, not a starting asset.

## 5. Two-level action architecture

The intended architecture is

```math
\mathcal{S}_{\text{MIT}}
\;\longrightarrow\;
\mathcal{S}_{\text{eff}}.
```

The global functional carries the topology, phase, sampler, embedding, and connection data.

The effective observer-chart action carries the sampled matter and metric degrees of freedom.

This is the existing Tier-3 descent reading: sampled / twisted degrees of freedom are integrated out or descended into $`\mathcal{S}_{\text{eff}}`$.

The global and effective actions are therefore two levels of one program, rather than two independent postulates.

## 6. Candidate global functional

Keep the first functional schematic:

```math
\mathcal{S}_{\text{MIT}}
=
\mathcal{S}_{\text{MIT}}[\Psi,S,N,\lambda;\,i,\mathcal O_M,A,g,\ldots],
```

where:

- $`\Psi`$ is the complementary wave share;
- $`S`$ is the realized-mode share;
- $`N`$ is the observer lapse defined by $`d\tau_H = N\,dt`$;
- $`\lambda`$ is an optional multiplier enforcing a native budget constraint;
- $`i`$ is the embedding;
- $`\mathcal O_M`$ is the sampler / readout map;
- $`A`$ denotes the relevant flat and matter connections;
- $`g`$ enters when the Tier-3 metric-response arm is activated.

The minimal clock arm should contain only the structure required to test the lapse equation. Couplings to $`i`$, $`\mathcal O_M`$, $`A`$, and $`g`$ remain frozen during that first computation.

## 7. Jacobi precedent and the clock slot

The useful precedent is Jacobi's principle.

Jacobi replaces an externally driven time evolution with a geometric variational problem whose constraint supplies the physical clock along the extremal.

MIT already has a preferred phase parameter fixed by topology:

- one lap: $`2\pi`$;
- closed edge: $`4\pi`$;
- chronon: $`\pi/30`$.

The role of the global functional is therefore to convert the preferred phase parameter into the observer clock, rather than erase the preferred parameter.

Write

```math
d\tau_H=N(t)\,dt.
```

The promotion question is whether the lapse equation

```math
\frac{\delta \mathcal{S}_{\text{MIT}}}{\delta N}=0
```

forces

```math
N=S^{1/2}.
```

The identity

```math
\Psi^2+S^2=1
```

may appear as an on-shell constraint equation only. $`S`$ must remain a varied realized-mode share during the derivation, rather than being replaced at the start by $`\sin(t/2)`$.

The gate is not this page's to score. The half-power exponent is owned by [The Half-Power Clock](friedmann-as-output.md), which carries the route menu, the success and failure bars, the three-gate argument for the landing route R-HALF, and the prior discipline that governs any new route: the half power is the lowest-complexity value outside the integer family, and any framework carrying both amplitudes and intensities has a square root sitting between the two levels, so a route landing on $`-1/2`$ is expected under the null. The landing is not the evidence; the operator gates are. This program enters that menu as R-VAR, inherits those terms, and its verdict is recorded there. The owner page's failure bar already reserves this slot, listing "no tick functional returning $`N^2 = S`$" and "no geometric functional landing the half power" as separate exhaustion conditions.

The candidate functional must therefore declare, before it is run, which of two things it is: an independent route, whose lapse equation reaches the exponent with no reference to the tick measure, or the operator-level realization of R-HALF, in which the tick lemma's overlap density falls out of a variation rather than being defined. The second is not a lesser outcome. By the owner page's own doctrine the landing is not the evidence and the operator gates are, so supplying R-HALF with an operator-level derivation would be a result in its own right. What is not admissible is leaving the relation undeclared until after the exponent appears.

### PASS

A preregistered native functional and its constraint structure determine

```math
N=S^{1/2}
```

without inserting the exponent as an input, with GR appearing only in the comparison to Friedmann form, and with the functional returning a second consequence beyond its design target.

### PASS by stabilizer route

If the exponent is obtained through one of the currently unmerged numerical $`3/2`$ structures, the result promotes only together with the operator-level bridge that identifies the relevant structures.

This applies in particular to any route using a stabilizer ratio to reach the clock exponent.

### PASS by non-stabilizer route

A derivation of $`N=S^{1/2}`$ from a route independent of the unmerged $`3/2`$ structures stands on its own.

**Scoring the dressed lapse, pre-registered.** "Another clock" is not by itself a failure, and the distinction is fixed here rather than after the run. [The stress-tensor bridge](stress-tensor-bridge.md) records that holding $`a_\text{eff} = a_\ast S`$ while the fitted rate carries its constant forces the clock to dress, $`(dt/d\tau)^2 = 4\alpha/S + 4\beta S^2/\Psi^2`$, whose first piece is the Waltz clock recovered exactly at $`\beta = 0`$. A functional returning that dressed lapse is therefore returning the object §9 relocates the open question to, not a wrong answer. The pre-registered target is the $`\beta \to 0`$ limit: a lapse whose budget piece reduces to $`S^{1/2}`$ passes the clock gate, and its $`\Lambda`$ piece is then a second consequence, feeding the bridge's two-part metric-definition problem. This is also what makes the second-consequence requirement preregisterable rather than an after-the-fact quality judgment: the consequence is named now, before any functional exists.

The undressed outcome is named with it, so that neither case is scored after the run. If the functional returns $`N = S^{1/2}`$ exactly then $`\beta = 0`$, there is no $`\Lambda`$ piece, and the second consequence is instead the tick measure $`d\mu_\text{tick} = S^{3/2}\,dt`$ falling out of the same variation rather than being defined, which is the operator-realization outcome of the declaration above; or, failing that, gate (iii)'s realization-rate law $`dR \propto S^{3/2}\,dt`$ on the [entropy page](entropy-as-realization-budget.md). Which of the two is claimed is declared with the route type, before the run.

### FAIL

The minimal functional leaves $`N`$ underdetermined, returns a clock outside the dressed family fixed above, or requires $`S^{1/2}`$ to be inserted into the action or constraint by construction.

## 8. Relation to the unmerged 3/2 triple

The corpus keeps three numerically equal $`3/2`$ appearances fenced apart, and that fence is owned elsewhere: the [framework page](../../../README.md)'s One Identity section states its three posts, and [Friedmann as Output](friedmann-as-output.md)'s R-STAB row carries the hazard gate. Neither is restated here.

The one hook specific to this program: the Hubble-clock exponent $`1/2`$ reaches the tick exponent $`3/2`$ only through the existing import $`a_\text{eff} = a_\ast S`$, so a functional that lands the clock by way of a $`3/2`$ structure has crossed the fence and owes the operator-level bridge. That requirement is scored in §7 under PASS by stabilizer route, not here.

## 9. Relation to the stress-tensor bridge

The existing stress-tensor result remains unchanged.

With

```math
a_\text{eff}=a_\ast S
```

and

```math
d\tau_H=S^{1/2}\,dt,
```

the current bridge gives

```math
H^2=\frac{\Psi^2}{4S^3},
```

with the constant term excluded.

The variational program relocates the open question to the descent

```math
\mathcal{S}_{\text{MIT}}\longrightarrow \mathcal{S}_{\text{eff}}.
```

A successful global functional must explain why the observer-chart descent carries the required clock and stress-energy structure.

## 10. Tier relation and metric response

This program lies over the existing tiers.

Tier 2 remains the embedding-selection problem:

```math
\delta\mathcal{S}/\delta i.
```

Tier 3 remains the metric-response problem:

```math
\delta\mathcal{S}/\delta g.
```

For a diffeomorphism-invariant $`\mathcal{S}_{\text{eff}}`$ with sampled fields on shell, stress-energy conservation follows from the symmetry structure.

The load-bearing Tier-3 gate is the Einstein equation with the required coefficient structure:

```math
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
8\pi G\,T_{\mu\nu}.
```

The specific $`\Lambda`$ coefficient remains part of the coefficient gate.

## 11. First bounded computation

The first computation tests only the observer clock.

### Varied

Vary:

- $`N(t)`$, the observer lapse;
- $`S(t)`$, the realized-mode share;
- $`\Psi(t)`$, when required by the chosen minimal functional;
- $`\lambda(t)`$, when a multiplier is used to impose the native budget constraint.

### Held fixed

Hold fixed:

- the Möbius topology;
- the one-lap $`2\pi`$ anti-periodic boundary condition;
- the closed-edge $`4\pi`$ periodicity;
- the phase convention $`\Psi(0)=+1`$;
- the chronon $`\pi/30`$;
- the embedding $`i`$;
- the sampler $`\mathcal O_M`$;
- the flat and matter connections $`A`$;
- the metric $`g`$.

The first arm therefore asks only whether the native phase/budget variational structure determines the lapse.

### Constraint handling

If the functional uses

```math
\Psi^2+S^2=1,
```

treat it as a constraint equation arising from variation or multiplier enforcement.

The on-shell substitutions

```math
\Psi=\cos(t/2),
\qquad
S=\sin(t/2)
```

belong after the constraint equations are obtained.

### Frozen before the run: the kinetic term and the potential

The lapse equation is only a gate if what it varies is fixed in advance. In the one class where $`\delta\mathcal{S}/\delta N = 0`$ is a genuine Hamiltonian constraint, the parametrized form $`\mathcal{S} = \int (T/N - N\,V)\,dt`$ with $`T`$ quadratic in the velocities, the lapse equation returns $`N^2`$ from the kinetic-to-potential ratio, with the overall sign fixed by the action convention. The whole exponent then rests on the $`S`$-power of $`V`$, which the sign does not touch, and the two natural kinetic choices already split it:

| Kinetic term | Value on shell | $`V`$ required for $`N^2 = S`$ |
|---|---|---|
| the Rayleigh form $`\lvert\Psi'\rvert^2`$ of §4 | $`S^2/4`$ | $`V \propto S`$ |
| the budget metric $`\lvert\Psi'\rvert^2 + \lvert S'\rvert^2`$ | $`1/4`$, constant | $`V \propto 1/S`$ |

Both rows are arithmetic, not results. Their point is that a $`V`$ chosen after the target is known is exactly the inserted-by-construction FAIL, so the requirement is procedural: the kinetic term and the potential must each be read from a named corpus object (the Rayleigh form, the budget identity, the tick measure) and frozen in a commit before the run, with the $`S`$-power of $`V`$ recorded as the pre-registered prediction rather than reported as the output. This is the owner page's prior discipline made mechanical.

### Primary observable

Read off the lapse law returned by the $`N`$ equation.

Promotion requires

```math
N(t)=S(t)^{1/2}
```

with the exponent fixed by the native functional.

*Run 2026-09-23 and recorded at [The Variational Clock Arm](variational-clock-arm.md). The registration above is unchanged. With its kinetic-and-potential table public, no freeze of a functional could have been blind, so the arm is recorded as a Result scored against these terms.*

## 12. Existing negative evidence

The eight-functional well-selection sweep remains a caution against low-complexity extremization narratives.

That sweep addressed a different search space: selection among discrete wells.

The present program concerns a functional over phase, lapse, and eventually embedding / sampler / connection data.

The candidate functional should still be preregistered before its observable consequences are inspected.

## 13. Expansion order after the clock gate

If the clock gate passes, arm the open objects in this order:

1. Couple the embedding $`i`$.
2. Couple the sampler $`\mathcal O_M`$.
3. Couple the relevant flat / matter connections.
4. Derive the sampled local state.
5. Activate metric variation and the Tier-3 descent.
6. Compare the resulting $`\mathcal{S}_{\text{eff}}`$ against the stress-tensor and coefficient gates.

Each arm should retain an independent stop condition and a predeclared observable.

## 14. Stop conditions

Stop and retain MOTIVATED status if:

- the lapse exponent is inserted rather than derived;
- the lapse equation leaves $`N`$ freely specifiable;
- the result depends on an arbitrary normalization that changes the exponent;
- the preferred topological phase parameter is erased;
- a stabilizer-based derivation merges the unbridged $`3/2`$ structures without the required operator map;
- the on-shell trigonometric forms are substituted before the constraint variation and thereby make the clock gate tautological;
- the route returns only $`N = S^{1/2}`$ and nothing else, which is decoration rather than derivation;
- the desired clock appears only after observable-dependent tuning.

A failed clock arm may motivate a new preregistered functional, but it does not repair the failed arm.

## 15. Promotion rule

This program remains MOTIVATED until the bounded lapse computation passes.

Promotion occurs only when a native variational constraint fixes

```math
N=S^{1/2}
```

without importing the exponent, with any stabilizer-based route carrying its operator-level bridge.

At that point the score-to-sample reframing becomes a derivational result rather than program architecture.

## 16. Parked

*Added 2026-09-23, after the first clock arm.* The first clock arm leaves one question: why should the variational potential carry amplitude weight, $`W \propto S`$? The level the clock needs is already known, so a search run now would be run knowing what it has to find, and whatever it turned up would carry little evidence. Its likely result, that nothing in the corpus qualifies, is what the [clock arm's residue](variational-clock-arm.md#viii-what-could-change-the-verdict) already records. The program is therefore parked: no search is run, and no next arm is named.

**The standing admission bar.** An object proposed later as the potential $`W \propto S`$ counts only if all four conditions hold:

1. it was introduced for a reason unrelated to the clock: it existed before the first clock arm's result of 2026-09-23, or it was built later for another stated purpose, fixed in a dated record that names, before its weight in $`S`$ is checked, both that purpose and the consequence it offers under condition 4;
2. its $`S^1`$ weight follows from its own construction, not from the wish for $`N = S^{1/2}`$;
3. it is eligible to enter an action as the potential $`W`$, rather than being merely another quantity proportional to $`S`$;
4. using it produces a consequence besides the half power, and for a construction built after 2026-09-23 that consequence is the one its dated record named.

The fourth is §7's second-consequence requirement, with §7's rule that the consequence be named in advance carried over to later constructions, and §14's stop against decoration, applied to the input rather than to the output.

**What stays closed.** §13 opens its arms only after the clock gate passes, and it has not, so the embedding, sampler and connection arms stay closed; none is opened to rescue the clock. The fixed-boundary area branch that the [postulate bridge](postulate-bridge.md) recorded on 2026-07-13 as its Tier 2 ground floor is a separate problem: it runs there, with no clock target, and anything it returns reaches this program only through the bar above.

**What reopens it.** A construction motivated for its own reasons that meets all four conditions. The likeliest place for one is the independently motivated action both bridges wait on, coupling the wave and budget sector to the matter degrees of freedom, with the clock as a downstream check rather than its target. For such an action two things are fixed now. Its lapse variation, $`\delta\mathcal{S}_\text{MIT}/\delta N = 0`$, should return $`N = S^{1/2}`$ without the level being chosen. And whether its couplings keep every block's boundary profile proportional to $`C(\Theta)`$, the scaling law's open [uniformity condition](scaling-law-uniqueness.md#proof-the-schur-separation), is scored either way: if they do, the factored scaling law gains a derivation for single-position observables; if they do not, the shifts of $`C`$ they predict at the wells are a consequence under condition 4, tested rather than grounds for rejecting the action. Until then `gate:variational-independence-bar` stays Open with no worker, and the postulate bridge and the stress-tensor bridge's route R6 wait on it.

---

*The exponent is labelled FORCED and has landed once, conditionally, on another route's premise ledger. This program is a second route to it, and it promotes only on the Half-Power Clock's terms.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
