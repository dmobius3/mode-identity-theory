<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Clock-Asymmetry Fit

**Type:** Test
**State:** Closed
**Verdict:** Inconclusive
**Status (2026-07-05):** Registered and executed same day (tag eps-family-v1.0, results 6e95fed). Row 3 fired: ε=0 excluded at 95% in both tiers (ε̂=−0.106), but the dial is contaminated as a P2 probe on this data, so it neither confirms nor cleanly refutes; the flip gate (row 1) did not fire.
**Summary:** The registered measurement track for P2: a continuous kernel-asymmetry fit scoring whether the observer clock exponent departs from the symmetric point.
**Inputs:** `tick-lemma.md`, `sampling-kernel-symmetry.md`, `temporal-budget.md`, the Λcos Model D+Λ pipeline
**Parent:** `tick-lemma.md`
**Frozen:** 2026-07-05 the registration, the slice table, the priors, and the verdict table (frozen before any run)

REGISTRATION, frozen before any run; EXECUTED same day from lambda-cos tag `eps-family-v1.0`, results commit `6e95fed`. **Verdict: row 3 of the frozen table fired: zero excluded at 95% in both tiers ($`\hat\epsilon = -0.106`$); P2 challenged; see Results.** The registered expectation failed and is recorded as such. This is the P2 measurement track of the [half-power clock](friedmann-as-output.md): one premise, one parameter, nothing else. The specification below is complete enough to execute mechanically in the Λcos pipeline at its next session; results land in a single commit filling the Results section, with no re-runs, no post-hoc priors, and no added parameters. This note cannot flip any label, and it contains no entropy, Molien, or model-building content by design.

**Related:** [The Tick Lemma](tick-lemma.md) (where the family arises as the residual of L1-L3), [The Sampling Kernel's Symmetry](sampling-kernel-symmetry.md) (the theorem track; independent, and not evidence about $`\epsilon`$'s value), [Temporal Budget](temporal-budget.md) (the baseline model and data), [The Half-Power Clock](friedmann-as-output.md).

---

## I. The Family, Once and Target-Free

The tick lemma's graded structure (L1-L3, with exchange symmetry removed) leaves exactly one family: the kernel-asymmetry family

```math
d\mu_\epsilon = w_1^{1/2-\epsilon}\, w_2^{1/2+\epsilon}, \qquad w_1 = S,\quad w_2 = S^2, \qquad\text{so}\qquad d\mu_\epsilon = S^{3/2+\epsilon}\,dt.
```

$`\epsilon = 0`$ **is P2's symmetric point**: exchange symmetry of the elementary sampling kernel. Wording guard, frozen with the spec: the fit measures the observable clock-asymmetry dial whose symmetric point is P2, including the cubic matter exponent that the symmetric point predicts; it does not observe microscopic kernel symmetry directly. Any eventual prose scores the dial, not the microphysics.

The observable form, which is what the pipeline fits, follows from the budget algebra exactly as in the validated Model D+Λ and is stated here so no convention enters the likelihood: with $`S = s_0/(1+z)`$ and $`\Omega_\Lambda = 0.685`$ held fixed as the fiducial vacuum-fraction anchor as in the baseline ($`\Omega_\Lambda`$ here is the vacuum density fraction $`f_\Lambda`$, not the MIT hierarchy $`\Omega_\Lambda = (R_\Lambda/\ell_P)^2`$),

```math
\frac{H^2(z)}{H_0^2} = \frac{1-\Omega_\Lambda}{1-s_0^2}\,(1+z)^{3+2\epsilon} \;-\; \frac{(1-\Omega_\Lambda)\,s_0^2}{1-s_0^2}\,(1+z)^{1+2\epsilon} \;+\; \Omega_\Lambda.
```

At $`\epsilon = 0`$ this is the published Model D+Λ identically. The asymmetry shifts both budget exponents rigidly by $`2\epsilon`$; it is not a $`w_0`$ clone and no template comparison is part of this registration. Convention guard: the family is defined by the tick measure and, equivalently, by this $`H^2(z)`$ formula; the labeling of intermediate times (which ladder rung is called proper or conformal) does not enter the likelihood and is not adjudicated here.

---

## II. The Slice Table (frozen; the family is not new)

The continuous family is the one-parameter closure of clocks already tested; it unifies the dead rows with the live one rather than being invented to rescue a result. Leading behavior of $`H`$ is $`(1+z)^{3/2+\epsilon}`$.

| $`\epsilon`$ | $`H`$ leading | Identity | Status |
|---|---|---|---|
| $`-3/2`$ | $`(1+z)^{0}`$ | Model C | dead, $`+7276.6`$ |
| $`-1/2`$ | $`(1+z)^{1}`$ | Model A | dead, $`+218.7`$ |
| $`0`$ | $`(1+z)^{3/2}`$ | Model D+Λ, the symmetric kernel | alive, $`+0.11`$ |
| $`+1/2`$ | $`(1+z)^{2}`$ | Model B | dead, $`+1821.9`$ |
| $`+1`$ | $`(1+z)^{5/2}`$ | the completing fit registered at gate (i) | expected dead |

The tabulated $`\Delta\chi^2`$ values are the budget page's; the Tier-1 run recomputes the full curve on the same data, so no cross-paper normalization is assumed. The run discharges the $`\epsilon = +1`$ registration as one of its slices; one session pays both debts.

---

## III. Data, Parameters, Priors (frozen)

Data and likelihood: identical to the published Λcos baseline (Pantheon+ 1701 SNe Ia with full covariance; DESI DR2 BAO, 13 points; same distance machinery and $`r_d`$ treatment). Parameters: $`(H_0, s_0, \epsilon)`$, with $`\Omega_\Lambda = 0.685`$ fixed exactly as the baseline fixed it; $`\Omega_\Lambda`$ variation is out of scope for this registration. Priors: $`H_0`$ and $`s_0`$ as in the baseline ($`s_0`$ flat on $`[0, 1)`$); $`\epsilon`$ flat on $`[-1.6,\ +1.1]`$, chosen once to cover every previously tested slice, with no alternate priors before or after the run.

**Two tiers, both frozen now.**

1. **Tier 1, diagnostic profile.** On a grid in $`\epsilon`$, profile the likelihood over $`(H_0, s_0)`$ and report the $`\Delta\chi^2(\epsilon)`$ curve, with 68% and 95% intervals read from it, plus the curve's values at the four dead slices.
2. **Tier 2, joint posterior.** Full MCMC over $`(H_0, s_0, \epsilon)`$ under the frozen priors; report the marginal $`\epsilon`$ posterior and the $`(s_0, \epsilon)`$ correlation structure. The strength criterion is pre-stated: $`\epsilon \approx 0`$ must survive marginalization over $`s_0`$. If $`\epsilon`$ is constrained only when $`s_0`$ is pinned by hand, the result is recorded as weaker, whatever the headline number. Expected identifiability, noted in advance: at $`s_0 \to 0`$ the model reduces to $`(1-\Omega_\Lambda)(1+z)^{3+2\epsilon} + \Omega_\Lambda`$, so $`\epsilon`$ remains constrained by the matter-exponent deformation even in the ΛCDM limit; degeneracy with $`s_0`$ is not expected to erase the measurement.

---

## IV. Registered Expectation and the Verdict Table (frozen)

**Expectation, stated before any run:** $`\epsilon`$ consistent with zero. Width forecast from quadratic interpolation of the walls: $`\sigma_+ \approx 0.5/\sqrt{1821.9} \approx 0.012`$ and $`\sigma_- \approx 0.5/\sqrt{218.7} \approx 0.034`$, so a 68% interval of order a few hundredths, asymmetric, tighter above than below.

**The bar, stated plainly: "zero allowed" is not enough.** A broad posterior that merely includes zero is non-falsification, not measurement. The meaningful-measurement bar is pre-set: both 68% half-widths at or below $`0.05`$.

| $`\epsilon`$ result | Verdict |
|---|---|
| zero inside the 68% interval AND both half-widths $`\leq 0.05`$ | P2 empirically supported as the observationally selected point of the registered family; proceed to the ledgered flip discussion |
| interval includes zero but a half-width exceeds $`0.05`$ | measurement inconclusive; no flip; recorded as such |
| zero excluded at 95% | P2 challenged; inspect R1 and R2 per [the chase note](sampling-kernel-symmetry.md), and downgrade the tick lemma per its own failure bar |
| $`\hat\epsilon`$ within $`0.1`$ of a dead slice, or a multimodal posterior | route failure or pipeline inconsistency; investigate before any physics claim |

---

## V. The Flip Precondition (restated, verbatim standard)

The budget page's label may change only to the ledgered form, only from the first verdict row, and only after review:

> DERIVED conditional on P1 and P2, with P1 definitional and P2 supported by the kernel-symmetry reduction plus the $`\epsilon`$-family constraint.

Not a bare word. This registration is the constraint's source; it is not the flip's authority.

---

## Results

**Executed 2026-07-05** from a clean checkout of the lambda-cos tag `eps-family-v1.0` (commit `351938c`), frozen sequence tier1 then tier2 uninterrupted, seed 12345, transcript and all outputs in the single results commit `6e95fed` on the `epsilon-family` branch. The gate binding held throughout (script sha256 and data md5 verified at each tier launch).

**Tier 1 (profile).** Minimum at $`\hat\epsilon = -0.106`$: $`\chi^2 = 1764.714`$, $`\Delta\chi^2_{\Lambda\text{CDM}} = -7.74`$, $`\Delta\chi^2_{\epsilon=0} = -7.85`$. Intervals: 68% $`[-0.139, -0.069]`$, 95% $`[-0.171, -0.031]`$; both 68% half-widths ($`0.033`$, $`0.037`$) inside the $`0.05`$ bar. The $`\epsilon = 0`$ point reproduces the published Model D exactly ($`+0.108`$). The profile has two regimes: for $`\epsilon \gtrsim -0.008`$ the profiled $`s_0`$ sits on the prior floor (the published ΛCDM-limit behavior), while at negative $`\epsilon`$ a degeneracy valley opens with $`s_0`$ climbing to $`0.467`$ at the minimum. The $`\epsilon = +1`$ slice lands at $`+6395.5`$: the completing fit registered at gate (i) is discharged, dead as expected.

**Tier 2 (joint posterior).** $`\epsilon`$ median $`-0.092`$, 68% $`[-0.131, -0.051]`$, 95% $`[-0.620, -0.019]`$, $`\mathrm{corr}(s_0, \epsilon) = -0.82`$; the posterior best point ($`s_0 = 0.467`$, $`\epsilon = -0.106`$) coincides with the Tier 1 minimum. Diagnostics (informational): acceptance $`0.469`$; $`\tau_\text{max} = 131`$, chain length $`\approx 38\tau`$, marginal; effective samples $`\approx 974`$; split-half $`\epsilon`$-quantile shift $`0.003`$, so the 68% region is stable and the deep negative 95% tail, which rides the $`s_0`$ valley, is the least-resolved feature.

**Verdict, scored strictly against the frozen table.** Row 1 does not fire (zero is outside the 68% interval). Row 2 does not fire (the interval does not include zero). Row 4 does not fire ($`\hat\epsilon`$ is $`0.394`$ from the nearest dead slice; the posterior is unimodal along a single valley). **Row 3 fires: zero is excluded at 95%, in both tiers.** As frozen: "P2 challenged; inspect R1 and R2 per [the chase note](sampling-kernel-symmetry.md), and downgrade the tick lemma per its own failure bar."

**The registered expectation was wrong, and that is part of the record.** The forecast ($`\epsilon`$ consistent with zero, half-widths $`\approx 0.012`$ and $`0.034`$ from quadratic interpolation of the walls) failed because the discrete slices bracketed but never probed the interior: the valley at $`\epsilon \approx -0.11`$ was invisible to the wall arithmetic.

**The wording guard governs the claim.** The measured statement is about the dial, not the microphysics: within the registered family, the data select a small negative clock asymmetry, at $`2.8\sigma`$ over the symmetric point ($`\Delta\chi^2 = 7.85`$, one parameter) and $`7.7`$ below ΛCDM at the cost of two. One structural observation is recorded without adjudication: the preferred valley sits along $`\mathrm{corr}(s_0, \epsilon) = -0.82`$ with $`s_0 \approx 0.47`$, which is the direction in which the known Pantheon+-versus-BAO pull on $`s_0`$ relaxes; whether the dial is measuring kernel physics or absorbing that data tension is exactly what the R1/R2 inspection and the queued $`\Omega_\Lambda`$ robustness check (robustness, not authority) must sort out.

**Consequences per the fired row.** The FORCED $`\to`$ DERIVED flip is off the table (row 1 did not fire). The tick lemma's conditional closure stands as mathematics (R1 $`\wedge`$ R2 $`\Rightarrow \epsilon = 0`$ is still a theorem), so by modus tollens the measurement challenges the premises: R1 or R2 is wrong somewhere, or the dial is contaminated, and the chase note says where to look. What is downgraded is exactly P2's empirical status, not the lemma.

**Two guards added at adjudication.** Model selection: the family improves $`\chi^2`$ relative to ΛCDM, but model-selection weight and robustness are not adjudicated by this registration. Exponent reading, under the wording guard: the selected tick measure within the family is $`S^{3/2+\epsilon}\,dt`$ with measured exponent $`\approx 1.39`$ to $`1.41`$ at 68%: close enough to $`3/2`$ for the symmetric theorem to stay structurally meaningful, too far for exact exchange symmetry to be promoted.

**Adjudicated diagnostic sequence (diagnosis, not repair; nothing below carries verdict authority).** (1) Results audit: recompute the summary numbers independently from the committed raw outputs. (2) $`\Omega_\Lambda`$-free scan: does the $`\epsilon`$ valley survive when $`\Omega_\Lambda`$ moves? Evaporation points to a fixed-$`\Omega_\Lambda`$ tension absorber; survival makes it a real family feature. (3) SN-only / BAO-only split: $`\epsilon_\text{SN}`$, $`\epsilon_\text{BAO}`$, $`\epsilon_\text{joint}`$; if the two datasets independently lean negative the result is harder to dismiss, if they disagree it is probably not tick physics. (4) R1/R2 inspection, only after the data diagnostics. (5) Tick-lemma status update. The two candidate diagnoses, recorded and deliberately not decided: $`\epsilon`$ absorbing the SN/BAO tension through the $`s_0`$ degeneracy (conservative), or the symmetric-kernel assumption genuinely too strong (interesting).

**Diagnostics executed (2026-07-05, lambda-cos commit `16094d7`; mechanical readings of the diagnostic questions posed at adjudication above (after the main fit, before their sub-runs, not part of the frozen registration); formal adjudication stays with review).**

*Audit:* all seven headline numbers recomputed from the committed raw outputs match exactly. The row-3 scoring stands on clean arithmetic.

*$`\Omega_\Lambda`$-free:* the valley survives in depth ($`-8.67`$ vs $`-7.85`$ at fixed $`\Omega_\Lambda`$) but **relocates off the tick layer**: at the free-$`\Omega_\Lambda`$ minimum ($`\epsilon \approx -0.08`$ to $`-0.10`$) the profiled $`s_0`$ sits on the prior floor with $`\Omega_\Lambda = 0.61`$ to $`0.63`$. At $`s_0 = 0`$ the family reduces to a pure matter-exponent deformation of ΛCDM, $`H^2 = \Omega_m (1+z)^{3+2\epsilon} + \Omega_\Lambda`$, in which the budget clock is inert: the data preference is for a softer matter exponent ($`\approx 2.84`$) with more matter ($`\approx 0.375`$), and it is expressed equally well with the tick structure switched off. The fixed-$`\Omega_\Lambda`$ valley ($`s_0 = 0.47`$) and the free-$`\Omega_\Lambda`$ minimum ($`s_0 = 0`$, $`\Omega_\Lambda = 0.625`$) are two corners of one degenerate ridge.

*Split:* $`\epsilon_\text{SN}`$ runs to the grid edge ($`-0.40`$, 68% region $`\epsilon \leq -0.23`$, unbounded below within the grid); $`\epsilon_\text{BAO} = -0.03`$ with 68% $`[-0.083, -0.011]`$. The two 68% regions are disjoint; the joint $`-0.106`$ is a compromise neither dataset wants. The adjudication-stage rule fires: disagreement, so probably not tick physics.

*What the mechanical readings imply, stated carefully.* Both data diagnostics point at the conservative branch: the $`\epsilon`$ preference is a generic background-shape pull in this data combination (softer matter exponent, the direction adjacent to the known DESI dynamic-dark-energy preference the Λcos paper's template-bias work already orbits), not a property of the tick layer, which the preference does not need. The adjudicated ledger line: **P2: supported by reduction; empirically unscored, channel contaminated.** The $`\epsilon`$ measurement channel is contaminated by background-shape and dataset-tension directions: the frozen row-3 result excludes $`\epsilon = 0`$ within the registered likelihood, but that exclusion is not a clean measurement of kernel asymmetry; P2 is neither empirically promoted nor empirically refuted, and the flip stays off. The headline scientific result of this registration is the specificity statement itself: **the observable $`\epsilon`$ dial is not specific enough to score P2 on current SN+BAO data.** The protocol protected the framework from overclaiming in both directions. The R1/R2 inspection is parked unless a discriminator independent of the $`\epsilon`$ dial appears.

*The exported thread.* The empirical preference the run exposed leaves this program under a new name, **the soft matter-exponent deformation**, because in the $`\Omega_\Lambda`$-free corner it is not measuring clock asymmetry. It becomes a Λcos-side follow-up, stripped of framework and tick language, with its question posed there: do Pantheon+ and DESI DR2 prefer a softened effective matter exponent in a one-parameter background deformation, and is that preference related to the same template-bias direction that produces apparent dynamical dark energy?

*External context (added 2026-07-05).* An independent late-time-only analysis (CC + DESI DR2 with Pantheon+, DES-Dovekie, and Union3; arXiv:2510.08339) finds the same qualitative direction: dataset-dependent preference for dynamical dark energy, strongest for Union3 and DES-Dovekie and below $`2\sigma`$ for Pantheon+, with flexible models drifting to $`\Omega_m \approx 0.35`$ to $`0.375`$, and explicit warnings that low-$`z`$ supernova subsets can drive the apparent preference. This supports treating the $`\epsilon`$ result as a background-shape diagnostic rather than a clean measurement of kernel symmetry. One caution carried with the citation: the correspondence is at the shape level (softened late-time growth, $`\omega_a < 0`$ slope, high-$`z`$ phantom side), not at the $`(\omega_0, \omega_a)`$ quadrant level; the effective-fluid image of the deformation sits phantom-side at $`z = 0`$ while their fits are quintom-B, and the exported note's template mapping is what adjudicates whether these are one data pull seen through two parameterizations.

---

*One premise, one parameter, one run. The family was always there; the fit reads the dial.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
