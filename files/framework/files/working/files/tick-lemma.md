<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Tick Lemma

**Type:** Result
**State:** Closed
**Status (2026-07-05):** Gate (ii) of the half-power clock closes conditionally on the §VII premise ledger; the computation returns S^{3/2}dt. The ε measurement later diagnosed the dial contaminated (see clock-asymmetry-fit); P2 stands as supported-by-reduction, not derived.
**Summary:** Derives the interface tick measure as the geometric mean of the two ledger measures, fixing dμ_tick = S^{3/2}dt.
**Inputs:** `half-power-involution.md`, the regraded uniqueness lemma, the chronon, `entropy-as-realization-budget.md`
**Parent:** `friedmann-as-output.md`
**Frozen:** 2026-07-05 the tick definition, the disambiguation menu, and the verdict table (posted before computing)

Definition frozen in commit `2485b3d`; computation run in the following commit; premise ledger hardened by the review pass after that; the git history is the audit trail. This is gate (ii) of the [half-power clock](friedmann-as-output.md), the decider, and the computation returns the overlap density: gate (ii) CLOSES, conditionally on the premise ledger of §VII (one act two ledgers; no arrow in the kernel). The review pass regraded the uniqueness lemma onto the framework's own grading, dissolving its one hidden assumption, and gave P2 both a theorem path (the hermiticity chase) and a registered measurement path (the continuous $`\epsilon`$ fit; the discrete model table was its slice scan all along). The budget page's FORCED label is not flipped by this note; scoring moves to the armed channels and review. The definition in §II is built from primitives already in service elsewhere, and the target exponent appears nowhere in it.

**Measurement update (2026-07-05, post-run and post-diagnostics).** Gate (ii) remains conditionally closed as a theorem of the registered premises. The $`\epsilon`$ measurement channel is contaminated by background-shape and dataset-tension directions: the frozen row-3 result excludes $`\epsilon = 0`$ within the registered likelihood, but the diagnostics show that this exclusion is not a clean measurement of kernel asymmetry ([registration Results](clock-asymmetry-fit.md)). P2 therefore returns to the theorem-track status: **supported by reduction, not empirically promoted, not empirically refuted.** The half-power clock did not earn empirical promotion from its measurement track, and was not cleanly falsified by it either. The R1/R2 inspection is parked unless a discriminator independent of the $`\epsilon`$ dial appears.

**Related:** [The Half-Power Clock](friedmann-as-output.md) (the tracker), [The Level Exchange](half-power-involution.md) (gate i; supplies the level measures), [Temporal Budget](temporal-budget.md), [Entropy as Realization Budget](entropy-as-realization-budget.md) (the armed consequence channel; not touched here).

---

## I. The Question

Is a tick a joint-registration event? Everything else in the half-power program is closed, armed, or fenced: gate (i) gives the level-exchange structure, gate (iii)'s first consequence is pre-committed on the entropy page, and the fits eliminated the rungs and the skipped midpoint. What remains is whether the observer's elementary tick, once defined from the framework's own primitives, induces the overlap density of the two level measures or something else. A kill here is as valuable as a landing.

---

## II. Primitives and the Frozen Definition

Three primitives, each already in service, none introduced for this page:

1. **The chronon** $`\Delta t_{\min} = 4\pi/120`$: the smallest phase advance the domain registers. It supplies the tick's counting side and its units. Its measure-theoretic role here: the count-level measure $`dt`$ is the *base measure* against which the level densities are taken.
2. **The two ledgers**, fixed at gate (i) as the level measures relative to that base: the amplitude ledger $`d\mu_A = S\,dt`$ (section-level bookkeeping of realized content available to sample) and the intensity ledger $`d\mu_I = S^2\,dt`$ (function-level bookkeeping of registered results; the level of the measurement rule $`C(\Theta) = 2\sin^2(\pi\Theta)`$). These are stocks: the standing weight each level assigns to a phase interval. Flows (transfer rates like $`d(S^2) = S\Psi\,dt`$) are outputs of tick counting, not ledger weights; using a flow as a ledger weight is the already-dead R-REAL construction, named in Section IV so the stocks-versus-flows adjudication is visibly pre-committed.
3. **The sampling act**: the framework's elementary act of observation, registration of realized content. Per the sampling ontology the framework already carries: registration constitutively *draws on* realized content (amplitude level) and *deposits* a registered result (intensity level). The irreversibility of observation lives in the accumulation of such acts, not in the wave ([entropy page](entropy-as-realization-budget.md) §IX).

> **Definition (the tick; FROZEN).** An elementary tick is one sampling act at chronon resolution: a single event that draws on the amplitude ledger and deposits on the intensity ledger. One event, two ledger entries. The tick measure $`d\mu_{\text{tick}}`$ is the rate density of such events on the phase interval, taken relative to the count base $`dt`$; the chronon fixes its normalization (ticks are discrete, one per registered chronon), and the ledgers fix its $`S`$-dependence.

**Why the tick cannot live on one ledger (the necessity argument).** An amplitude-only event keeps the section-level $`4\pi`$ bookkeeping but is not registered: nothing is deposited, no observation occurred. An intensity-only event is registered but holonomy-blind: $`S^2`$ is $`2\pi`$-periodic, invariant under the lap sign flip, so a purely intensity-native tick cannot see the period it is supposed to keep. A tick must preserve the section-level temporal bookkeeping *and* produce a registered result, so it lives at the amplitude-intensity interface. (Caveat carried from gate (i): measures on the positive quadrant are sign-blind, so the holonomy half of this argument attaches to how the densities are built, not to their values; it is support for the definition, not a proof of the induced weight.)

One orientation guard, placed ahead of the premise it protects: the sampling act is oriented only once a state is supplied. Amplitude-to-intensity is the realized direction of use, not an intrinsic asymmetry of the elementary rule; Section VI returns to this as premise P2.

---

## III. The Interface-Measure Uniqueness Lemma (regraded)

Independent of the tick, a piece of elementary mathematics on the framework's own bookkeeping, stated conditionally: it says nothing about which reading the tick satisfies. The first draft of this lemma assumed covariance under independent rescaling of the two ledgers; review flagged that as its one hidden physical assumption (the ledger values are locked, intensity the square of amplitude, and under common rescaling alone the arithmetic and harmonic means survive). The regraded proof dispenses with it: every premise below is bookkeeping the framework already carries.

> **Lemma.** Let $`f(w_1, w_2)`$ be a local function of the two ledger densities relative to the count base, and assume: **(L1) definite grade**, under the amplitude grading $`S \to cS`$, which acts on the ledger pair with locked weights $`(w_1, w_2) \to (c\,w_1,\ c^2 w_2)`$: $`f(c\,w_1, c^2 w_2) = c^{\gamma} f(w_1, w_2)`$ for some grade $`\gamma`$; **(L2) degree one** under common rescaling of both densities (a change of count-base normalization): $`f(c\,w_1, c\,w_2) = c\,f(w_1, w_2)`$; **(L3) idempotence**: $`f(w, w) = w`$; **(L4) exchange symmetry**: $`f(w_1, w_2) = f(w_2, w_1)`$. Then $`f = \sqrt{w_1 w_2}`$, with grade $`\gamma = 3/2`$.

*Proof.* (L1) with $`c = 1/w_1`$ gives $`f(w_1, w_2) = w_1^{\gamma}\, g(w_2/w_1^2)`$ with $`g(x) := f(1, x)`$. Substituting into (L2): $`c^{\gamma} g(x/c) = c\, g(x)`$ for all $`c`$, so $`g(x) = g(1)\, x^{\gamma - 1}`$, and $`f = g(1)\, w_1^{2-\gamma} w_2^{\gamma - 1}`$: the pure-power family is forced, not assumed. (L3) fixes $`g(1) = 1`$. (L4) gives $`2 - \gamma = \gamma - 1`$, so $`\gamma = 3/2`$ and $`f = \sqrt{w_1 w_2}`$. $`\square`$

Three remarks. **Exclusions.** The arithmetic and harmonic means, and every power mean, satisfy (L2)-(L4) and fail (L1): no definite grade under the locked grading. Definite level, already doctrine, is what removes them; the earlier independent-rescaling axiom (what it actually required was separate bi-homogeneity) is superseded and carries no load. **The residual family is the asymmetry family.** (L1)-(L3) alone leave the one-parameter family $`w_1^{1/2-\epsilon} w_2^{1/2+\epsilon}`$ with grade $`\gamma = 3/2 + \epsilon`$; (L4) is exactly $`\epsilon = 0`$. The one physical premise, exchange symmetry, is therefore not decoration on the lemma: it is the single dial left, and Section VII gives it a measurement. **The grade is the exponent.** $`\gamma`$ is the tick's grade under the amplitude grading and equals the clock exponent through the degree-one structure: one object seen twice. This is the midpoint $`3/2`$ again, not a fourth one; the fence keeps its three posts. On the detailed-balance face, stated modestly: within the product-power class of local symmetric exchange kernels, balance and idempotence select the square root; the balance face and the overlap face are one selection viewed twice, coherence rather than double evidence.

---

## IV. The Disambiguation Menu (posted before computing)

"An event both bookkeepings register" has distinct formalizations with different induced weights. All four are named now, so the adjudication in Section VI is against a fixed menu:

| Reading | Structure | Induced weight | Note |
|---|---|---|---|
| Coincidence | two independent event streams, one per ledger; tick = both fire within one chronon | $`S^3\,dt`$ | product of densities; requires two stochastic streams |
| One-sided | tick counted on a single ledger | $`S\,dt`$ or $`S^2\,dt`$ | endpoints; both already eliminated as observer clocks by the fits |
| Flow-weighted | ledger entry taken as the transfer increment $`d(S^2) = S\Psi\,dt`$ | $`\propto S^{1/2}\Psi^{1/2}\,dt`$ or $`S\Psi\,dt`$ | level-mixed; the $`S\Psi`$ form is R-REAL, already dead analytically |
| Conversion | one event carried on two ledgers; tick measure is the interface measure of the stock pair | $`\sqrt{\mu_A\,\mu_I} = S^{3/2}\,dt`$ | requires the Lemma's premises, including kernel symmetry |

---

## V. The Verdict Table (posted before computing)

| Computation returns | Recorded outcome |
|---|---|
| $`S^{3/2}\,dt`$ | gate (ii) closes, with its premise ledger stated; scoring moves to the armed channels (entropy bound, registered fit) and review. The budget page's FORCED label is NOT flipped by this note. |
| $`S^3\,dt`$ or an endpoint | route dies; the tracker's failure bar activates; the program closes as kinematics native, one named dynamical import |
| off-ladder or level-mixed | route dies the same way, with the added note that the tick violates definite level |

If the tick cannot be shown to be a joint-registration event at all, the level-exchange structure remains elegant but non-derivational, and $`S^{3/2}\,dt`$ reverts to a motivated clock postulate. That sentence is the failure condition, registered before the attempt.

---

## VI. The Computation

**Step 1: adjudicate the reading against the frozen definition.** The coincidence reading requires two independent stochastic streams, one per ledger, firing separately; the frozen definition has one act with two entries, the draw and the deposit constitutive of the same sampling event, so coincidence does not describe it. The one-sided readings contradict the definition directly: a draw without a deposit is unregistered, a deposit without a draw has no content (the §II necessity argument). The flow-weighted reading uses transfer increments as ledger entries, but the frozen definition takes the ledgers as the gate-(i) stocks, with flows as outputs of tick counting, the pre-named R-REAL circle. One row survives the definition: conversion. The tick measure is the interface measure of the stock pair $`(\mu_A, \mu_I)`$.

**Step 2: check the Lemma's premises for that interface measure.** Locality (chronon-local event, rate density at $`t`$ depends only on the ledger densities at $`t`$), degree one (the tick density is a density relative to the same count base as the ledgers, so a common renormalization carries all three together), and idempotence (equal ledgers degenerate joint registration to registration) hold structurally. Definite grade is the definite-level doctrine: one event, one weight under the amplitude grading; a mixed-grade tick would change shape under $`S \to cS`$. That leaves exchange symmetry, the physical premise (P2): the elementary sampling kernel carries no arrow; direction lives in the state (the budget's $`\Psi(0) = +1`$ and the accumulation of samples), not in the rule. Two sentences resolve the tension a reader will name first. Each *instance* of the act is directed, a draw and a deposit; P2 is about the *rule* that sets the rate, which reads the same in both directions, with the arrow of net flow coming from what the ledgers hold: the standard split behind detailed balance, carried as a theorem by quantum transition rates whenever the generator equals its own adjoint. And the bridge from the framework's stated doctrine to P2 is one line: running a single tick backwards turns the draw into a deposit and the deposit into a draw, so time reversal of the elementary act implements the ledger swap, and the [entropy page](entropy-as-realization-budget.md) §IX doctrine (reversible wave; irreversibility by accumulated sampling) reaches P2 through an explicit chain. P2 is supported, not proved, and it is the single load-bearing premise: dropping it releases the asymmetry family $`w_1^{1/2-\epsilon} w_2^{1/2+\epsilon}`$ with no selection.

**Step 3: apply the Lemma.**

```math
d\mu_{\text{tick}} = \sqrt{\mu_A\,\mu_I} = \sqrt{(S\,dt)(S^2\,dt)} = S^{3/2}\,dt,
```

with the chronon fixing the normalization. This registered interface tick, $`d\mu_{\text{tick}} = S^{3/2}\,dt`$, is not a proper-time wristwatch: reading it as proper time would put $`H`$ on the dead $`S^{-5/2}`$ branch.

**Step 4: the chain to the clock exponent.** With the kinematic dictionary $`a = S`$ (ESTABLISHED), dividing the tick by the scale factor gives the Hubble clock the distance model runs on:

```math
d\tau_H = \frac{d\mu_{\text{tick}}}{a} = S^{1/2}\,dt, \qquad \frac{dt}{d\tau_H} = S^{-1/2}, \qquad H^2 \propto \frac{\Psi^2}{S^3} = \frac{1-S^2}{S^3}.
```

The exponent that the budget page carries as FORCED by $`S^3`$ dimensionality plus GR is returned here with GR absent from the chain. The computation lands on the first row of the pre-posted verdict table.

---

## VII. Premise Ledger and Verdict

| Premise | Content | Status |
|---|---|---|
| P0 | the gate-(i) level assignment: count base $`dt`$, amplitude stock $`S\,dt`$, intensity stock $`S^2\,dt`$; equivalently the locked grading $`(c, c^2)`$ under $`S \to cS`$ | carried from [The Level Exchange](half-power-involution.md); target-free, prior structure |
| P0b | ledgers are stock measures; flows (transfer increments like $`d(S^2) = S\Psi\,dt`$) are outputs of tick counting, not ledger weights | pre-committed in the frozen definition (§II); the stocks-versus-flows fence, doing real work in Step 1 |
| P1 | one act, two ledgers: the frozen definition, supported by the necessity argument (registration requires both a draw and a deposit) and the §II orientation guard | DEFINITIONAL with MOTIVATED support; rejecting it rejects the framework's sampling ontology, not a step of the computation |
| P2 | kernel exchange symmetry, equivalently $`\epsilon = 0`$ in the asymmetry family of §III: the elementary rule carries no arrow; direction lives in the state | SUPPORTED, reduced by [the chase](sampling-kernel-symmetry.md): P2 follows from R1 (magnitude-only registration, prior doctrine) and R2 (state-free rate rule, structural premise). **MEASURED, then DIAGNOSED, 2026-07-05: row 3 of the [registration](clock-asymmetry-fit.md) fired ($`\epsilon = 0`$ excluded at 95%, $`\hat\epsilon = -0.106`$), but the diagnostics mark the dial contaminated: the $`\Omega_\Lambda`$-free minimum sits at $`s_0 = 0`$ where the tick layer is inert, and the SN/BAO 68% regions are disjoint. Ledger line: SUPPORTED by reduction; empirically unscored, channel contaminated. R1/R2 inspection parked pending a discriminator independent of $`\epsilon`$.** |

Everything else in the chain is the regraded Lemma (proved from bookkeeping premises), the kinematic dictionary $`a = S`$ (established), and the native scale-factor map $`d\tau_H = d\mu_{\text{tick}}/a`$. Its formal resemblance to GR's proper/conformal relation is recorded as an open placement seam in [friedmann-as-output](friedmann-as-output.md); the identification of the native measures with GR's time variables is not claimed here. No other import enters, and GR enters nowhere.

**The theorem path for P2 (the hermiticity chase): RUN, verdict SUPPORTED by reduction ([The Sampling Kernel's Symmetry](sampling-kernel-symmetry.md)).** The adjoint-identity shape is realized concretely: the kernel is the realized-axis projector on the budget's own complex bookkeeping line, self-adjoint, with forward and reverse elementary magnitudes equal at $`S`$; the level stocks are recovered as the moment ladder of the one sampling element, partially deriving P0; and P2 reduces to R1 (magnitude-only registration, prior doctrine) plus R2 (state-free rate rule, a structural premise supported by source inventory: the state is the framework's only time-asymmetric object and its entry point is already counted). No intrinsic arrow was found; the FAILED row did not fire. DERIVED is withheld at two named blocks: the budget page's bookkeeping status for the complex form, and R2's premise status. The pillar fence held: its self-adjoint realizations modeled the discipline; no descent map was used or claimed.

**The measurement path for P2: MEASURED, then DIAGNOSED, 2026-07-05 ([The Clock-Asymmetry Fit](clock-asymmetry-fit.md)).** Give the kernel an asymmetry $`\epsilon`$: flux $`\propto w_1^{1/2-\epsilon} w_2^{1/2+\epsilon}`$, still degree one, grade $`3/2 + \epsilon`$; then $`d\mu_{\text{tick}} \propto S^{3/2+\epsilon}\,dt`$ and $`dt/d\tau = S^{-1/2-\epsilon}`$. The fit reads this observable dial; it does not observe microscopic kernel symmetry directly. Every clock model already run is an $`\epsilon`$ slice:

| $`\epsilon`$ | $`dt/d\tau`$ | Identity | Status |
|---|---|---|---|
| $`-3/2`$ | $`S^{+1}`$ | Model C | dead, $`+7276.6`$ |
| $`-1/2`$ | $`S^{0}`$ | Model A | dead, $`+218.7`$ |
| $`0`$ | $`S^{-1/2}`$ | Model D, the symmetric kernel | alive, $`+0.11`$ |
| $`+1/2`$ | $`S^{-1}`$ | Model B | dead, $`+1821.9`$ |
| $`+1`$ | $`S^{-3/2}`$ | the completing fit registered at gate (i) | dead, $`+6395.5`$ |

The discrete family was a kernel-asymmetry scan all along, and the walls at $`\epsilon = \pm 1/2`$ already bracket $`\epsilon`$ near zero. One continuous fit turns the bracket into a posterior. The full specification is now frozen as its own registration, [The Clock-Asymmetry Fit](clock-asymmetry-fit.md): data, priors, two tiers, the meaningful-measurement bar (a merely-includes-zero posterior is non-falsification, not measurement), the four-row verdict table, and the registered expectation ($`\epsilon`$ consistent with zero, forecast half-widths $`\approx 0.012`$ above and $`0.034`$ below). That fit has since run. Executed 2026-07-05 from the lambda-cos tag `eps-family-v1.0` with results in commit `6e95fed`, it discharged the registered $`S^{-3/2}`$ point as its $`\epsilon = +1`$ slice, one session paying both debts. Row 3 fired: $`\epsilon = 0`$ excluded at 95% in both tiers at $`\hat\epsilon = -0.106`$, P2 challenged, and the diagnostics then marked the dial contaminated; the §VII ledger line carries the resulting two-part status. One caution for later sweeps: the registration's own verdict table keeps $`\epsilon = +1`$ as *expected dead*, because that is the forecast frozen before execution, so that cell and the executed value in the table above are meant to differ.

**Flip protocol.** When the armed channels and review score this, the budget page's label should carry its ledger inline rather than a bare word: DERIVED (P1 definitional; P2 supported, bounded at $`\lvert\epsilon\rvert`$ below the fit width). A label that names its premises survives review.

**Verdict, per the pre-posted table.** The computation returns $`S^{3/2}\,dt`$: gate (ii) CLOSES, conditionally on the premise ledger above. As that table row states: scoring moves to the armed channels, the entropy-page bound and the registered $`S^{-3/2}`$ fit, and to review; the budget page's FORCED label is not flipped by this note. What changed epistemically: the two GR imports (matter dilution in three dimensions, the Friedmann square root) are replaced by two named, target-free, framework-native premises (P1, P2). What did not change: the numbers (the same $`H(z)`$, per the tracker's provenance paragraph), the pages (no relabels executed), and the parked items (Molien route, holonomy candidate, Λcos fit) stayed parked. The Λcos fit has since fired; see the measurement update above. The failure condition registered in Section V was not triggered and remains on the page: if P1 or P2 falls under review, $`S^{3/2}\,dt`$ reverts to a motivated clock postulate and the tracker's failure bar applies.

---

*One event, two ledgers, one base. The definition is frozen; the calculation decides.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
