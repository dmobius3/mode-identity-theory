<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Stress-Tensor Bridge

**Type:** Program
**State:** Active
**Status (2026-09-15):** Open program page, first cycle complete: nothing derived (no X→g_eff, no X→T_eff, no action). The variational route is promoted to preferred for the construction step. The Molien P1 Bridge is folded in as C7 and R7: the spatial projection now carries its own route, beside R6 rather than under it, and every candidate must declare the fluctuation map it induces. R7's first calculation has run on the fluctuation half, classifying the admissible transfers shell by shell and stating exactly a sufficient axiom for the Q class.
**Summary:** The program page for the ledger's E(S): from the realized budget state to a stress tensor with a declared metric placement, the framework's one missing map.
**Gated by:** `gate:variational-independence-bar` (the variational route R6 only; R7 is not gated by it)
**Inputs:** `../../../../cosmos/files/cosmological-constant.md` §IV, `budget-map.md`, `friedmann-as-output.md`, `temporal-budget.md`, `molien-p1-bridge.md`, `../../bedrock/files/first-eigenvalue.md`

OPEN, program page; first cycle complete. Nothing on this page is derived: no $`X \to g_\text{eff}`$, no $`X \to T_\text{eff}`$, no action. What the first cycle did establish is recorded in §VI: the pilots have run against their registered expectations, the route that could not work is dead as a computed statement, and the target any future derivation must hit is analytically pinned, together with two newly named questions about what the effective metric even is. The page fixes the object, assembles the constraints any candidate must clear (all already in the corpus, gathered here for the first time), enumerates the candidate routes, and keeps the pilot definitions that were frozen before running. The object keeps its ledger name: $`E(S)`$, the amplitude-to-$`T_{\mu\nu}`$ dictionary. This page is its canonical program home; the [claim ledger](claim-ledger.md) keeps the count (one object, counted once), and the [Budget Map](budget-map.md) keeps the inventory role.

**Related:** the OpenWave M8 program's field-dynamics half is the same gap approached from the particle side (external; no Lagrangian survey is run on this page).

---

## I. The object

One map. Input: the framework's realized state, the budget variable $`S`$ and the standing-wave amplitudes the corpus already carries. Output: a stress tensor $`T_{\mu\nu}`$, together with a declared **placement**: a statement of which metric's Einstein equations it sources. The placement is part of the object, not a detail; §III is where it forks.

The same missing map currently carries four names in four places, and their consumers are different, which is why closing it pays four debts at once:

| Where | Name there | What that consumer needs from the map |
|---|---|---|
| [cosmological constant](../../../../cosmos/files/cosmological-constant.md) §IV | the stress tensor gating the Λ coefficient | decides whether $`\Lambda_\text{physical} = 3/R^2`$, the vacuum-reference value, survives contact with the domain's actual content |
| [claim ledger](claim-ledger.md) open problems | $`E(S)`$, the amplitude-to-$`T_{\mu\nu}`$ dictionary | the load-bearing open; the Ψ²→S² transfer needs a counterparty |
| [Friedmann as Output](friedmann-as-output.md) | the one dynamical import | the matter-scaling side of $`H(z)`$ currently borrows GR; a native source would let form be output |
| [Redshift and Cooling](redshift-and-cooling.md) §VI, [entropy](entropy-as-realization-budget.md) §VIII.2 | the cooling-energy accounting | where the phase-sampled photon energy goes |

Four names, one hole. A single theorem-shaped result discharges all four, and a single failure mode contaminates all four, which is why the constraints below are collected before any construction is attempted.

---

## II. The constraint set, already in hand

Every row below is established elsewhere in the corpus or was verified this cycle; nothing here is new. A candidate map that violates a row is dead on that row, not negotiable against the others.

| # | Constraint | Statement | Source |
|---|---|---|---|
| C1 | Static source | If the placement is the physical static metric with Einstein's equations unchanged, then $`G_{\mu\nu}`$ is time-independent, so $`T_{\mu\nu}`$ must be too. Instantaneously, not on average. | GR, given the static postulate |
| C2 | The coefficient gate | For a homogeneous isotropic perfect fluid on the static closed domain, $`\Lambda R^2 = (\rho+3p)/(\rho+p)`$. Given $`\rho + p > 0`$ (required for a real closed radius), the value 3 is attained exactly when $`\rho = 0`$, $`p > 0`$: a pure-pressure source, which violates the dominant energy condition. Dust gives 1, radiation 3/2. Outside the perfect-fluid class the question is open, and that is this page's question. | [cosmological constant](../../../../cosmos/files/cosmological-constant.md) §IV |
| C3 | The mechanism fence | The success bar of [Friedmann as Output](friedmann-as-output.md) admits GR only in the comparison to Friedmann form, never as the mechanism. Supplying a $`\rho(S)`$ and then using $`H^2 \propto \rho`$ to obtain $`H(S)`$ fails that bar regardless of where $`\rho(S)`$ came from. The bridge must respect this: a derived source is not the same as a derived evolution. | [claim ledger](claim-ledger.md), Friedmann tracker |
| C4 | The Killing ledger | A static metric carries a timelike Killing field, so total energy is exactly conserved in the physical description. This is sharper than ΛCDM, where the time-dependent metric makes energy non-conservation routine. The one pilot computation on record found no rising conserved counterparty for the realized side; a candidate map must either exhibit the counterparty or show why the Killing charge is not the right ledger. | [Budget Map](budget-map.md), Killing-charge pilot (recorded negative) |
| C5 | The fitted dictionary | The D+Λ phenomenology on SN+BAO, with $`\Omega_\Lambda = 0.685`$ held as the fiducial anchor (here $`\Omega_\Lambda`$ is the vacuum density fraction $`f_\Lambda`$ in the conventional ΛCDM sense, not the MIT hierarchy $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2`$), already sits essentially on ΛCDM. A derived source must reproduce that dictionary's constant term and matter-like term, or improve on them; it may not quietly break a fit the framework already owns. | [Temporal Budget](temporal-budget.md) |
| C6 | The coincidence fences | Any 3/2 or $`2/R^2`$ that surfaces in a candidate must clear the standing fences (the two-3/2s fence, the curvature-coincidence fence) before it counts. No new numerology enters through this page. | [Friedmann as Output](friedmann-as-output.md) discipline |
| C7 | The fluctuation-side declaration | A candidate $`g_\text{static} \to g_\text{eff}`$ must declare the fluctuation map it induces on the source shells, and classify what that map carries: the shells' spectral data alone, their $`A_5`$ directional covariance, or the quotient's identifications. The third is unavailable to any homogeneous flat law, so a candidate claiming a homogeneous flat law and the exact identifications together has contradicted itself. A candidate whose induced map is the Q-symbol transfer carries a further fingerprint: below $`N = 60`$ a definite icosahedral pattern of directional power, with zeros on the invariant forms' roots. | [The P1 Bridge](molien-p1-bridge.md) §II, §V |

**A structural observation, recorded as a hint and not a result.** With $`\Psi = \cos(t/2)`$ and $`S = \sin(t/2)`$ the budget identity is the harmonic energy identity: $`\dot\Psi = -S/2`$, so

```math
4\dot\Psi^2 + \Psi^2 = S^2 + \Psi^2 = 1.
```

A quadratic energy density of the standing wave is time-independent even though each share oscillates. So C1's staticity is natural for the energy density of any quadratic reading of the wave. It is not automatic for the pressure, which for a scalar reading is kinetic minus potential and oscillates with zero mean. Whether the physical $`T_{\mu\nu}`$ is such a quadratic reading is exactly the open dictionary; this observation constrains candidates, it does not select one.

---

## III. The placement fork

Three branches, mutually exclusive, each a legitimate outcome. The corpus is currently implicit on which branch it occupies; the translation-layer language of the budget pages leans (b) without saying so. Deciding the branch is part of closing the bridge, and each branch has stated consequences.

| Branch | Statement | What it requires | What it does downstream |
|---|---|---|---|
| (a) physical-static sourcing | Einstein's equations hold on the static physical metric with the mode content as source | a static $`T_{\mu\nu}`$ that is effectively vacuum: in the perfect-fluid class, $`\rho = 0`$, $`p > 0`$ (C2), or a principled exit from that class | if achieved, $`\Lambda_\text{physical} = 3/R^2`$ closes as identified; if the derived source is matter-like, the coefficient shifts and branch (c) is entered honestly |
| (b) effective-metric sourcing | Einstein's equations govern the effective metric $`g_\text{eff}(S)`$ of the distance-redshift dictionary; the static domain is substrate and is not required to solve them with matter | deriving the map $`g_\text{static} \to g_\text{eff}`$ and the source it implies, rather than assuming the FLRW form; C3 bars reading the answer off Friedmann | "Einstein imported unchanged" must be restated to name which metric; the Λ page's Stage 2 becomes the dictionary's normalization, which is what it already says |
| (c) shifted coefficient | The physical constant is not $`3/R^2`$; the vacuum-reference value is a reference only | owning the shift publicly: the Λ page §IV, the ledger gate row, and the MODELS.md Λ cell all update | the pre-registered Euclid falsifier $`\Lambda_\text{obs} R_\text{ind}^2 = 3`$ is then a test of the reference reading, and the framework must say what it predicts instead |

Branch (c) is a scientific outcome, not a defeat. This page exists to decide the branch, not to defend the number 3.

---

## IV. Candidate routes

The working table proper. Status vocabulary: OPEN (not yet attempted), PILOT-FROZEN (specified in §V, not yet run), RUN (executed against registered expectations, outcomes in §VI), DIAGNOSTIC (informative, cannot count as derivation), NEGATIVE (attempted, recorded), SPECULATIVE (no principled construction yet), PREFERRED (the form the construction step should take first, on methodological grounds, not evidence).

| Route | Construction | Branch served | Must clear | Status |
|---|---|---|---|---|
| R1 minimal scalar reading | Compute $`T_{\mu\nu}`$ of the standing wave read as a homogeneous scalar on the static $`S^3`$, quadratic density per §II | (a) | C1 instantaneously, then C2 | NEGATIVE (P1 run: dead as a computed statement, §VI) |
| R2 reverse diagnostic | Compute the $`T_\text{eff}`$ that makes $`g_\text{eff}(S)`$ Einstein, and compare its decomposition against the budget's fitted terms | (b) | C3: this READS the answer, so it can only locate the target, never derive it | RUN (P2, then flat variants P2b, P2c), DIAGNOSTIC: target located, §VI |
| R3 ALE-filling kinship | The postulate-bridge Tier-3 gravitational filling, a dictionary of the same general type for a different field | (a) or (b) | its own fence: formal kinship until an identity is shown | OPEN, fenced |
| R4 Killing counterparty | Identify the conserved charge that balances the realized side | any | C4; one computation found no rising counterparty | NEGATIVE (recorded), revisit only through a candidate map |
| R5 boundary or pure-pressure source | A principled origin for $`\rho = 0`$, $`p > 0`$ content (edge tension, Casimir-type reading of the Möbius boundary) | (a), preserving 3 | C2's DEC violation must be earned by a construction, not asserted to save the coefficient | SPECULATIVE |
| R6 variational route | Seek the action first, not the tensor: a map from the realized state to a coupled functional $`\mathcal{S}[g, \iota, \text{fields}]`$ per the [postulate-bridge](postulate-bridge.md) dynamical tiers, with the source obtained by variation, $`T_{\mu\nu} = -\tfrac{2}{\sqrt{-g}}\, \delta\mathcal{S}_\text{eff}/\delta g^{\mu\nu}`$. Tier 3 already names exactly this object: an effective action whose metric variation produces a stress tensor and whose embedding variation produces a force on the seam | any | the postulate-bridge independence gate: the functional must be motivated independently of the target, because a functional can always be built backward to make a chosen configuration critical; and no functional exists yet (Tier 2 is a recorded mood there, not a result) | OPEN, PREFERRED for the construction step |
| R7 spatial projection | Derive the spatial part of $`g_\text{static} \to g_\text{eff}`$ from the closed substrate: the curvature placement of §VI, together with the fluctuation map that placement induces on the shells; the Λ-dressing of the clock stays with the clock and action side | (b) | C7, and the curvature-placement half of §VI's two-part metric-definition problem; C3 bars reading the placement off the fitted dictionary, as it bars R2 | OPEN; first calculation run, the directional transfers classified shell by shell ([The Shell-to-Direction Transfers](directional-transfers.md)) |

**R7 is new to this cycle, and it fills a hole the first cycle left open.** §VII's success bar requires, on branch (b), the derived $`g_\text{static} \to g_\text{eff}`$ map, and no previously assigned row could produce it: R2 reads it off and C3 bars promoting that readout to a derivation, while R6 reaches metric variation only at the fifth of the six steps in its own expansion order. So the program could have completed every assigned route and still failed its own bar. R7 sits beside R6 rather than under it: R6 seeks the action and the tensor, R7 seeks the spatial placement. Both have to end in the same $`E(S)`$, and neither substitutes for the other, since a clock result does not settle $`k_\text{eff}`$ and a projection does not settle the lapse. R7 therefore takes the spatial part of that map, the curvature placement; the Λ-dressing of the clock is a lapse question and stays with the clock and action side.

What R7 gains from the fluctuation side is a constraint, not an answer. [The P1 Bridge](molien-p1-bridge.md) does not derive the projection and is not read here as doing so. It establishes what a projection's action on the source can be, as three named maps; it proves that one of the three, the quotient's own identifications, is unavailable to any homogeneous flat law; and it gives another, the Q-symbol transfer, an observable fingerprint on the shells below $`N = 60`$. That is why C7 requires a candidate to declare and classify its induced map rather than requiring it to be any particular one. The bridge reaches this program's boundary from the source side and records the same absence: neither program has a flattening at separations comparable to $`R`$.

**R7's first calculation has run**, on the fluctuation half only: [The Shell-to-Direction Transfers](directional-transfers.md). The positive SU(2)-covariant transfers from a shell covariance to a directional power form an $`(N+1)`$-parameter cone, so positivity and covariance select nothing, and P1's spectral transfer and the Q-symbol transfer are the barycenter and one vertex of its normalized simplex rather than two separate prescriptions. On a real field only the pair sums $`t_m + t_{-m}`$ act, which leaves an $`N/2`$-simplex in which Q and the antipodal Q are one vertex. Requiring a normalized transfer to preserve the nodal directions of *every* pure source on the shell selects Q, as a theorem, and on a real field the Q class; requiring it only for the shell's own invariant, which is the version that can be formulated from the realized source alone below $`N = 60`$, leaves the predicted directional pattern 2, 5 and 8 free parameters at $`N = 12, 20`$ and $`30`$, enough to reverse the sign of its leading icosahedral multipole, with an explicit second member exhibited at each. So C7's classification question is answered shell by shell, and the choice within it is not: a candidate projection must now say what it does to the radial label, which the calculation takes as given, and either supply the strong hypothesis, which is a statement about the map rather than about the source it acts on, or say which point of the simplex its construction induces.

R1's registered expectation was stated in the opening commit so it could not be adjusted later, and it landed exactly (§VI): "the mode content is not a minimally-read scalar field" is now a computed statement rather than a suspicion.

R6 was promoted to PREFERRED on methodological grounds, not evidence. It is the only route on the table where the stress tensor would have a principled origin instead of being chosen to fit, and it inverts the danger this page was built to avoid. The original hazard was "we know what $`T_{\mu\nu}`$ we want; can we find something that gives it." The protocol is now: derive the target independently (§VI, done), choose a candidate action independently (the gate above), obtain $`T_{\mu\nu}`$ by variation, then compare. A later independently motivated action either lands on the pinned fingerprint or it does not. Two structural properties come free with a legitimate action and cannot be had by guessing a tensor: diffeomorphism invariance yields $`\nabla_\mu T^{\mu\nu} = 0`$ as a consequence rather than a bolted-on property, and a static-geometry action carries a Noether energy, the first principled candidate for C4's missing counterparty since the recorded negative. That is machinery with which to own C4's problem, not a solution to it.

---

## V. Pilot checks, frozen before running

Both pilots are NON-EVIDENTIARY. Definitions were frozen in the opening commit; the computations have since landed and §VI records them, per the tick-lemma pattern. Each check states in advance what would count as pass, fail, and surprise, so it is able to fail. The definitions below are kept as frozen, for the record.

**P1, the minimal scalar reading (R1).** Metric: static round $`S^3(R)`$ with time, $`ds^2 = -dt^2 + R^2 d\Omega_3^2`$. Field: homogeneous $`\Psi(t) = \cos(\omega t)`$ with the budget normalization ($`\omega`$ matched to the Waltz phase so that $`S = \sin(\omega t)`$), quadratic density and pressure of the minimally coupled scalar. Outputs, each reported: $`\rho(t)`$, $`p(t)`$, the staticity residual $`\max_t \lvert p(t) - \bar p \rvert / \rho`$, the time-averaged $`w`$, and the coefficient $`\Lambda R^2`$ the static balance would assign to the averaged source. Expectations, registered: $`\rho`$ constant; $`p`$ oscillating with zero mean; averaged $`w = 0`$ (dust); assigned coefficient 1; staticity residual order unity. Surprise: any of those failing to hold.

**P2, the reverse diagnostic (R2).** Take $`g_\text{eff}`$ as the closed FLRW form with the budget's effective scale factor $`a_\text{eff} \propto S`$ in the distance-redshift dictionary. Compute $`G_{\mu\nu}[g_\text{eff}]`$ and read off the $`(\rho_\text{eff}(S), p_\text{eff}(S))`$ that Einstein's equations would require. Report their decomposition against the constant term and the matter-like term the fitted dictionary already carries. This is explicitly DIAGNOSTIC: it locates what a branch-(b) derivation must produce; producing it from the postulate side remains the open work, and C3 bars promoting this readout to a derivation.

---

## VI. First results: the pinned target

First cycle, run 2026-08-26. Every computation below is exact and symbolic, scored against expectations registered before execution; every registered expectation landed, and the two follow-on diagnostics (P2b, P2c) had their definitions and expectations registered before their runs as well. Notation throughout: $`S = \sin(t/2)`$, $`\Psi = \cos(t/2)`$, effective scale factor $`a_\text{eff} = a_\ast S`$, Waltz clock $`dt/d\tau = S^{-1/2}`$.

**P1: R1 is dead as a computed statement.** The minimal scalar reading fails C1 instantaneously: the pressure oscillates at full amplitude (staticity residual exactly 1), the time-averaged source is dust, and the static balance assigns the averaged source the Einstein-static coefficient $`\Lambda R^2 = 1`$, not 3. All five registered expectations landed. This kills R1, not branch (a).

**P2: the closed-placement fingerprint, and the sharp absence.** Reading the required source off the closed FLRW form with $`a_\text{eff} = a_\ast S`$ under the Waltz clock (self-checked against the corpus anchor $`H^2 = (1-S^2)/(4S^3)`$):

```math
8\pi G\, a_\ast^2\, \rho \;=\; \frac{3a_\ast^2}{4}\, S^{-3} \;+\; 3\, S^{-2} \;-\; \frac{3a_\ast^2}{4}\, S^{-1},
\qquad
8\pi G\, a_\ast^2\, p \;=\; -\,S^{-2} \;+\; \frac{a_\ast^2}{2}\, S^{-1}.
```

Three sectors with $`w = 0, -1/3, -2/3`$, each separately satisfying its own continuity equation (a non-interacting effective three-fluid), and **no constant term**: the effective-metric map alone does not generate a Λ-like piece. So even under branch (b), the constant must enter as its own object, which is exactly what the fitted dictionary does by anchoring $`\Omega_\Lambda`$.

**The fitted dictionary is one native term plus the anchor.** The [Temporal Budget](temporal-budget.md) fit's bracket collapses exactly under $`1+z = s_0/S`$: $`(1+z)^3 - s_0^2\,(1+z) = s_0^3\, \Psi^2/S^3`$. Its coefficient tie, $`\text{coeff}[(1+z)^1] = -s_0^2\; \text{coeff}[(1+z)^3]`$, is therefore not a fit target but a **structural identity**: a native derivation must produce the single object $`\Psi^2/S^3`$, never an independently normalized $`w = -2/3`$ component with its own amplitude. Relatedly, the negative-density reading of the $`S^{-1}`$ sector is decomposition-dependent: the native regrouping has $`\rho \ge 0`$, and the total source satisfies the null energy condition everywhere. Ontology hung on one decomposition would have to say why that decomposition is physical.

**The $`k_\text{eff}`$ question.** P2's frozen spec chose the closed form because the substrate is closed; the fitted dictionary is flat, with no $`(1+z)^2`$ term. Both cannot be the effective metric without a further statement, and a time-dependent scale factor changes the magnitude of spatial curvature, never its sign, so flatness cannot emerge from the closed form by rescaling. If the effective geometry is flat, the map $`g_\text{static} \to g_\text{eff}`$ must contain a genuine projection or coarse-graining that explains flat effective slices over a closed substrate; "the static $`S^3`$ looks like an expanding $`S^3`$" is not enough. The closed alternative is not excluded, but its curvature term being small against the matter term is necessary reasoning only, not acceptance: accepting a closed effective metric requires the SN+BAO comparison rerun with the nonflat distance relation. **(Pointer added 2026-09-15.)** This question's fluctuation-side counterpart landed after this cycle, in [The P1 Bridge](molien-p1-bridge.md) §V, which reaches the same boundary from the source side. It is carried forward as C7 and worked as R7; nothing this cycle computed changes.

**The Λ-clock consistency question.** The two frozen imports already force the geometric rate: $`a_\text{eff} = a_\ast S`$ and $`dt/d\tau = S^{-1/2}`$ give $`H^2 = \Psi^2/(4S^3)`$ exactly, with no freedom left to add a constant. The fitted form, written natively, is $`H^2 = \alpha\, \Psi^2/S^3 + \beta`$ with $`\alpha = H_0^2 (1-\Omega_\Lambda)\, s_0^3/(1-s_0^2)`$ and $`\beta = H_0^2\, \Omega_\Lambda`$. With $`\beta \neq 0`$ these are different functions: the fitted dictionary is a legitimate phenomenological $`H(z)`$, but it is **not** the geometric rate of that scale factor under that clock. The corpus carries this tension implicitly, split across two pages: [Temporal Budget](temporal-budget.md) derives the budget $`H^2`$ and then adds the anchored constant, while [Friedmann as Output](friedmann-as-output.md) states the one-exponent clock. The two statements need a bridge whenever the constant is real. If the fitted rate is to be geometric while $`a_\text{eff} = a_\ast S`$ is held, the clock must dress:

```math
\left(\frac{dt}{d\tau}\right)^2 \;=\; \frac{4\alpha}{S} \;+\; \frac{4\beta\, S^2}{\Psi^2}.
```

The first piece is the Waltz clock, recovered exactly when $`\beta = 0`$ and dominant early. The Λ piece crosses over exactly at the budget-Λ equality epoch, $`\alpha\, \Psi^2 = \beta\, S^3`$ (recorded without interpretation), and grows without bound as $`S \to 1`$. The alternative resolution dresses the translation layer $`a_\text{eff}(S)`$ instead, or distributes the dressing between the two; nothing here chooses. Consequence: $`k_\text{eff}`$ is not to be adjudicated in isolation. The missing $`X \to g_\text{eff}`$ theorem is a **two-part metric-definition problem**: spatial curvature placement, and Λ-dressing of the effective clock. And this sharpens "Λ is separate" rather than undermining it: the native machinery and the constant are demonstrably not both realized by one fixed metric under the original clock.

**P2b and P2c: the flat diagnostics.** P2b (flat slices, budget-only, original clock) reduces the source to exactly the fitted bracket, $`8\pi G a_\ast^2 \rho = \tfrac{3a_\ast^2}{4}(S^{-3} - S^{-1})`$ and $`8\pi G a_\ast^2 p = \tfrac{a_\ast^2}{2} S^{-1}`$, with the curvature rows gone and nothing else changed. It establishes the budget-only flat source target; it is not the full target, because its $`H^2`$ carries no Λ. P2c takes the full fitted $`H^2`$ on flat slices with $`a_\text{eff} = a_\ast S`$ held, and pins the full flat D+Λ target under that fixed placement:

```math
8\pi G\, \rho \;=\; 3\alpha\,(S^{-3} - S^{-1}) \;+\; 3\beta,
\qquad
8\pi G\, p \;=\; 2\alpha\, S^{-1} \;-\; 3\beta,
```

the tied pair with ratio exactly $`-1`$, plus a genuine $`w = -1`$ constant, no $`S^{-2}`$ sector, and the dressed lapse displayed above. This is one pinned member of the allowed family, not proved uniquely physical: if $`X \to g_\text{eff}`$ eventually derives $`a_\text{eff} = a_\ast F(S)`$ instead, the observational $`H(z)`$ can survive while the phase-to-proper-time map and the pressure reconstruction change.

**What the first cycle established, and nothing more:**

1. R1, the minimal scalar reading, is dead as a computed statement.
2. The original Waltz clock produces the budget sector but cannot accommodate an additive Λ while $`a_\text{eff} = a_\ast S`$ stays fixed.
3. For the flat D+Λ placement with $`a_\text{eff} = a_\ast S`$ held, the required source and the Λ-dressed lapse are analytically pinned.
4. Any native derivation now faces gates registered in advance of any construction: produce the tied $`\Psi^2/S^3`$ object as one term, produce a separate $`w = -1`$ constant, introduce no independently normalized $`w = -2/3`$ component, and close the metric/source triangle with Einstein's equations as the cross-check only (C3).

> **No $`X \to g_\text{eff}`$ has been derived. No $`X \to T_\text{eff}`$ has been derived. No action has been derived.** The route table says where construction stands; R6 is the preferred next direction, not an accomplishment.

---

## VII. Success and failure, stated in advance

Success is one map, stated once, that: (i) declares its branch; (ii) passes that branch's consistency row (C1 and C2 on (a); on (b), the derived $`g_\text{static} \to g_\text{eff}`$ map, now known from §VI to be a two-part job: curvature placement and clock dressing); (iii) exhibits the Killing counterparty or dissolves C4 with an argument; (iv) decides the Λ coefficient, in either direction; and (v) leaves the fitted dictionary of C5 intact or improved, with the comparison shown.

Failure is also an outcome worth recording, per route: R1 failing on its registered expectations is the expected result and still gets written down; R5 never finding a principled construction closes branch (a)'s coefficient-preserving arm; and if every route dies, the honest terminus is the Friedmann tracker's own alternative ending, "kinematics native, one dynamical import," now extended with "and the Λ coefficient rests on the vacuum reference."

What would falsify the whole program's premise rather than a route: a demonstration that no static-metric stress tensor and no $`g_\text{static} \to g_\text{eff}`$ map can reproduce the fitted dictionary at C5's level. That would be a result about the static architecture itself and would belong on the framework page, not here.

---

## VIII. What this page is not

Not a Lagrangian survey: that is the OpenWave M8 program's half, run under its own pre-registration discipline, and results cross between the two by citation, not by restatement. Not a rename: the object is the ledger's $`E(S)`$ and keeps that name and count. Not a license to import Friedmann as mechanism: C3 stands. And not evidence for a derivation: the pilots have run and §VI records what they established, but locating a target is not producing it; the diagnostics remain diagnostic, and the registered-expectation discipline is precisely what makes their outcomes mean something.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
