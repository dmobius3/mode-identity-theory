<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Entropy as Realization Budget

**Type:** Program
**State:** Active
**Status (2026-07-07):** MOTIVATED, not derived. The cooling half is established; the entropy half rests on the one unwalked shell-unlock map S↦N_max(S).
**Summary:** A candidate account of the thermodynamic arrow in a static universe: entropy as the spread of the resolution-amplitude budget over realized modes.
**Inputs:** `temporal-budget.md`, `redshift-and-cooling.md`, the 2I Molien shell spectrum, the chronon and the 120-domain

A candidate MIT account of the thermodynamic arrow in a static universe, scoped to the realization sector. The temporal budget already cools the universe without an exterior; this note asks where the entropy increase comes from, and answers it only where it can.

**Related:** [The Budget Map](budget-map.md), [The Temporal Budget Identity](temporal-budget.md), [Energy as Resolution Amplitude](energy-as-resolution-amplitude.md), [The Half-Power Clock](friedmann-as-output.md) (posted cross-constraint on the mode-count map, §IV), [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) (the same Molien shells), [The Waltz](../../../../spectrum/files/the-waltz.md).

**Notation.** $`S = \sin(t/2)`$ is the realization amplitude, kept from the temporal budget. Entropy is written $`\Sigma`$ to avoid collision with it; the accessible-mode count is $`W_\text{modes}`$, the microstate count over it $`W_\text{micro}`$, with $`\Sigma = k_B \ln W_\text{micro}`$. The action $`\mathcal{S}`$ is unaffected.

---

## I. The question

A static space at fixed volume has no exterior to radiate into and no growing volume to dilute into. Cooling is already answered: budget weight transfers $`\Psi^2 \to S^2`$ as the phase advances, photon energies scale by $`S(\text{emit})/S(\text{obs}) = 1/(1+z)`$, every wavelength by the same factor, so a blackbody stays a blackbody at $`T \propto 1/S`$ ([Redshift and Cooling](redshift-and-cooling.md)). That is the temperature half, and it is settled.

A temperature law is not an entropy law: cooling fixes $`T \propto 1/S`$ but says nothing about the configuration count. This note is the gameplan for the entropy, and it claims only the realization sector: the arrow of time as the budget resolves, not the gravitational arrow that Penrose's puzzle is about (§V).

---

## II. Energy, realization, entropy

The reframe is inherited, not invented here. [Energy as Resolution Amplitude](energy-as-resolution-amplitude.md) reads energy not as a substance an object carries but as the amplitude of the wave resolved at an observer's sampling coordinates. Carry that into the budget and entropy has a natural home.

$`S = \sin(t/2)`$ is the realized-mode content of the wave, the fraction expressed as resolvable modes at phase $`t`$. If energy is resolution amplitude, then the realized modes are where energy lives, and **entropy is how that energy is spread across them**. A budget concentrated in a few modes is ordered; the same budget spread across many is not.

| Question | Standard (FLRW) reading | MIT realization reading |
|---|---|---|
| What cools the bath | growing volume; comoving photon entropy conserved | budget spreads $`\Psi^2 \to S^2`$; per-mode amplitude falls |
| Why the low-entropy past | unexplained boundary condition (Penrose) | realization sector: forced by $`\Psi(0) = +1`$, $`S(0) = 0`$ |
| Where the arrow comes from | initial conditions, external | the sampling (irreversible), not the reversible wave |

---

## III. The second law as budget transfer

At early phase ($`t \to 0`$): $`\Psi^2 \approx 1`$, $`S^2 \approx 0`$. The budget sits concentrated in the unresolved standing wave, the formal hot dense limit of the unit-circle table. Few realized modes, the amplitude piled into them: low realization-entropy, high $`T`$.

As the phase advances the budget flows $`\Psi^2 \to S^2`$, out of the concentrated reservoir and into distributed realized modes. Per-mode amplitude falls (this is $`T \propto 1/S`$, the cooling), while the budget spreads over more modes. **The realization entropy climbs, and its increase is the same transfer that does the cooling.** This gives a monotone entropy trend through the observable quarter, anchored to the low-entropy start at $`S(0) = 0`$ where the wave begins. The flow is not itself the arrow: the budget transfer is reversible and unwinds past $`t = \pi`$ (§VI). The irreversibility proper belongs to the sampling, the observer reads the wave at $`\sqrt{\Omega}`$ and cannot un-sample, and that accumulated sampling history is what carries the arrow ([Energy as Resolution Amplitude](energy-as-resolution-amplitude.md)).

**The crux, stated honestly.** A naive photon gas in a fixed volume with $`T \propto 1/S`$ has entropy $`\propto V T^3 \propto 1/S^3`$, which falls as $`S`$ grows: the wrong direction. In the FLRW picture the growing volume rescues it; a static domain has no such term. So this account cannot rest on $`T^3`$ box entropy. What rises is the count of configurations the budget can take over the realized modes (§IV), not $`T^3`$: per-mode energy falls while the accessible modes multiply, so the configurations multiply with them and the entropy climbs. This is ordinary thermalization, a few hot modes giving way to many cool ones at fixed total budget. Stating it any other way puts the second law backward.

---

## IV. The mode-count map and the microstate count

The entropy needs a count, and two counts enter. Keeping them distinct is what makes the page both right in scale and safe from circularity: the structure must fix the count, not a relabeling of $`S`$. Write $`\Sigma = S`$ by hand and the second law is the definition read back, assumed rather than derived.

**The accessible modes set the phase space.** The realization $`S`$ governs how many modes the budget can occupy. The structure offers a concrete candidate: the accessible modes are the $`2I`$-invariant harmonics on $`S^3/2I`$, graded by degree into the Molien shells $`N = 0, 12, 20, 24, 30, \ldots`$ (the same shells that set the low-ℓ CMB gap; see [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md)). The accessible-mode count up to the highest shell realized at $`S`$ is

```math
W_\text{modes}(S) = \sum_{N \le N_\text{max}(S)} d_N,
```

with $`d_N`$ the $`2I`$-invariant degeneracy of shell $`N`$. **The load-bearing, unwalked step is the link $`S \mapsto N_\text{max}(S)`$:** how much realization unlocks which shell. Until it is derived from the 120-domain or the McKay grading (a second candidate ties $`N_\text{max}`$ to phase resolution through the chronon $`\pi/30`$), the growth of the phase space is a candidate, not a theorem. This map is the physics of the page: the structure sets the phase space, which is what keeps the entropy from being a relabeling of $`S`$.

**The entropy counts microstates over that phase space.** Thermodynamic entropy is not the log of the mode count; it is the log of the number of ways the budget's quanta occupy the accessible modes:

```math
\Sigma(S) = k_B \ln W_\text{micro},
```

where $`W_\text{micro}`$ is the number of microstates, the configurations of the budget's quanta across the $`W_\text{modes}(S)`$ accessible modes. The distinction is a scale test the page must pass. A CMB-scale photon gas occupies of order $`10^{89}`$ modes, so $`k_B \ln W_\text{modes} \approx k_B \ln(10^{89})`$ is only a few hundred $`k_B`$, short of the observed $`\sim 10^{89}\,k_B`$ (§VII) by some eighty orders of magnitude. The microstate count carries the scale: $`\ln W_\text{micro}`$ grows with the number of quanta, which is what reaches $`10^{89}`$. Counting modes misses §VII by itself; counting configurations meets it.

The entropy still rises for the reason in §III, more accessible modes meaning more configurations, and the low end is unchanged: at $`S \to 0`$ a single mode is realized, one configuration exists, $`W_\text{micro} = 1`$, and $`\Sigma = 0`$, a Boltzmann ground state forced by the boundary condition. The wave starts ordered because it starts as one mode.

```math
\begin{aligned}
\text{energy} = \text{resolution amplitude} & \quad \text{[IMPORTED, MOTIVATED]} \\
\Psi^2 + S^2 = 1,\; S = \sin(t/2) & \quad \text{[temporal budget]} \\
S \mapsto N_\text{max}(S) \text{ from } S^3/2I & \quad \text{[OPEN; load-bearing; anti-circularity]} \\
W_\text{modes}(S) = \textstyle\sum_{N \le N_\text{max}} d_N & \quad \text{[phase space; FOLLOWS once the map is fixed]} \\
\Sigma = k_B \ln W_\text{micro} \text{ over } W_\text{modes} & \quad \text{[Gibbs / microcanonical; scales with the quanta]} \\
d\Sigma/dt > 0 \text{ on } 0 < t < \pi & \quad \text{[THEOREM if } W_\text{modes} \text{ monotone; OPEN until the map is fixed]}
\end{aligned}
```

**Cross-constraint from the half-power clock (posted 2026-07-05, before the map is drawn).** The [half-power clock program](friedmann-as-output.md) fixes the counting face of the observer's tick ([The Level Exchange](half-power-involution.md), gate iii): each tick is one realized conversion, and the registered interface tick measure is $`S^{3/2}\,dt`$. The cumulative realized count must therefore obey

```math
dR \propto S^{3/2}\,dt, \qquad R(S) \propto \int_0^S \frac{u^{3/2}}{\sqrt{1-u^2}}\,du,
```

with early-phase index $`d\ln R/d\ln S \to 5/2`$ and a square-root approach to its finite total at $`S = 1`$. This is registered here before $`S \mapsto N_\text{max}(S)`$ is derived, and it cuts both ways. Hard bound: realized cannot exceed accessible, $`R(S) \le W_\text{modes}(S)`$ up to the shell staircase's envelope, so any candidate map whose accessible count grows more slowly than $`S^{5/2}`$ at early phase (early exponent above $`5/2`$) is dead on arrival. Strong fusion: if realization saturates access, ticks filling shells as they unlock, then $`W_\text{modes} \propto R`$ with the exact profile above, and one structure answers this page's load-bearing step and the clock program's second-consequence gate at once. A derived map that violates the bound kills the fusion candidate; one that meets the strong form is the clock program's second consequence landing. The comparison reads on the staircase envelope; shell discreteness is expected structure, not a violation. No conformal-seat fallback is registered.

---

## V. Scope: two entropy ledgers

The reframe accounts for the arrow in one sector and leaves Penrose's puzzle to the gravitational ledger, where that puzzle lives.

| | Realization entropy (this note) | Gravitational entropy (Penrose's subject) |
|---|---|---|
| What it counts | budget spread over realized modes | Weyl curvature, clumping, black holes |
| Early state | low: the wave concentrated at $`S = 0`$ | low: the early universe smooth |
| Why the low past | forced by $`\Psi(0) = +1`$ | the open puzzle |
| Through turnaround | peaks at full realization, then falls | keeps rising; black holes stay formed |
| Share of the total | subdominant | dominant |

The honest claim is the left column: realization entropy starts low because the wave starts at $`S = 0`$, a genuine account of the arrow in that sector. The right column is Penrose's, and this note leaves it open. The realization budget gives the thermodynamic arrow of the radiation and mode sector; it does not explain the smoothness of the gravitational initial state, and it should not be advertised as if it does.

---

## VI. The turnaround is a sub-budget feature

$`S = \sin(t/2)`$ peaks at $`t = \pi`$ and returns to $`0`$ at the $`t = 2\pi`$ turnaround, so the realization entropy $`\Sigma(S)`$ rises to a maximum at full realization and then falls. This is a reversal of the realization sub-budget, not of the second law. The dominant ledger is gravitational, and gravitational entropy rides straight through the turnaround: black holes stay formed, clumping does not un-clump, so total entropy keeps climbing. The reversal is a real and unusual prediction about the realization sector alone, and it costs nothing observationally: the present sits at $`t_\text{now} < 0.38`$ rad, far inside the rising branch ($`S \approx 0.19`$, about a fifth of the way to full realization).

---

## VII. Observational anchors

The thermal history is a phase ladder, every epoch a value of $`S = S_\text{now}/(1+z)`$: recombination at $`S \approx 1.7 \times 10^{-4}`$, BBN near $`S \sim 10^{-10}`$, the pure-wave limit at $`S \to 0`$. The temperature law $`T \propto 1/S`$ reproduces these as the FLRW history does, kinematically ([Redshift and Cooling](redshift-and-cooling.md)).

For the entropy the bar should sit where it can be cleared. **The honest target is that the entropy must stay consistent with the observed values:** the photon-to-baryon ratio $`\eta \approx 6 \times 10^{-10}`$ and the absolute CMB entropy ($`\sim 10^{89}\,k_B`$). Reproducing $`\eta`$ from harmonic counting would be a baryogenesis number falling out of group theory, which is upside, not the pass condition; it is unlikely to come out cleanly and the page should not stake itself on it. Consistency is the pass; prediction is the bonus.

---

## VIII. What needs to be derived

1. **The map $`S \mapsto N_\text{max}(S)`$.** Load-bearing and anti-circularity, per §IV. Without it the second law here is assumed, not derived. The half-power clock cross-constraint (§IV) now bounds the answer in advance: early growth no slower than $`S^{5/2}`$ (early exponent at most $`5/2`$), with the strong-fusion profile as the target.
2. **The realized-sector energy $`E(S)`$, and the thermodynamic route to $`\Sigma`$.** The energy accounting lives in [Redshift and Cooling](redshift-and-cooling.md) §VI: radiation carries the conformal conserved charge $`\rho\, a_\text{eff}^4 = \text{const}`$, and turning the budget transfer $`\Psi^2 \to S^2`$ into a stress-energy $`E(S)`$ needs an amplitude-to-$`T_{\mu\nu}`$ dictionary that is not yet written. Until it is, the thermodynamic route is conditional: given a candidate $`E(S)`$ and the established $`T \propto 1/S`$, the first law $`d\Sigma = dE/T`$ fixes $`\Sigma(S)`$ (for the candidate $`E \propto S^2`$, $`\Sigma \propto S^3`$, a 3D mode-volume scaling), which cross-checks the microstate count rather than substituting for the map of item 1. Highest-leverage: the dictionary would decide whether the realization sector carries a genuine energy counterparty, and it feeds this reading.
3. **The microstate count $`W_\text{micro}`$.** Carry out the Gibbs or microcanonical count of the budget's configurations over the accessible phase space $`W_\text{modes}(S)`$, and confirm $`\ln W_\text{micro}`$ scales with the quanta as §IV requires, not as a relabeling of $`S`$.
4. **Consistency with $`\eta`$ and the CMB entropy** (§VII), as a floor; clean reproduction as upside.
5. **Reconciliation with the cooling reading.** The entropy account must agree with the established kinematic $`T \propto 1/S`$ ([Redshift and Cooling](redshift-and-cooling.md)) wherever the FLRW thermal history agrees.
6. **The boundary of scope held explicitly:** realization sector in, gravitational ledger out (§V).

---

## IX. What this is not

A solution to Penrose's low-entropy past. That is the gravitational ledger, and it stays open (§V).

A claim that total entropy reverses at turnaround. Only the realization sub-budget peaks and falls; gravitational entropy carries the total monotonically through (§VI).

A second law read off the wave. The standing wave is reversible and periodic, so the realization entropy is a monotone trend over the observable quarter, not an arrow derived from the wave evolution. Irreversibility enters through the sampling: the observer cannot un-sample ([Energy as Resolution Amplitude](energy-as-resolution-amplitude.md)).

Tired light. The redshift here is a uniform phase-ratio rescaling that preserves the Planck spectrum, not a scattering loss that would smear it ([Redshift and Cooling](redshift-and-cooling.md)).

A derived result. The reframe is consistent and framework-native, and it rests on one unwalked map. Until that map is drawn from the structure, this is MOTIVATED.

---

*Cooling is the budget spreading. Entropy is the spread, counted.*

*The wave starts ordered because it starts as one mode.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
