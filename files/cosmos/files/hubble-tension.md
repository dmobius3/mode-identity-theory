<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🛰️ Hubble Tension

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/hubble%20tension%20banner.png?raw=true" width="100%" alt="Hubble Tension">

Measurements of the Hubble constant have split into two persistent camps: the cosmic microwave background gives 67.4 km/s/Mpc, local distance ladders give 73.04. The discrepancy has survived a decade of systematic checks. Mode Identity Theory, referred to below as the framework, reads the pair as one Fibonacci well sampled at two positions on the 120-domain.

**What matched.** One lattice step at the $`H_0`$ well carries 67.4 to 73.04 km/s/Mpc. The 8.4% size of that step follows once four choices are fixed, all imported rather than derived (§VI): a retrospective match, not a prediction.

**What failed.** The galactic mechanism proposed to realize the step, pre-registered and falsified against SPARC. And, in a separate, weaker exploratory check, no support for the two-population signature that mechanism predicted.

**What remains.** An unexplained numerical correspondence. Not a solution to the Hubble tension.

**Summary**

| Quantity | Status |
|---|---|
| Phase shift required | $`\Theta_f = 2/120`$ |
| $`\Delta C/C`$ at $`H_0`$ well | 8.4%, unchanged by either test |
| Shifted value if realized | $`67.4 \times 1.0837 = 73.04`$ km/s/Mpc |
| $`\Delta C/C`$ at $`\Lambda`$ under the same step | $`-0.27\%`$, stationary to first order but not zero |
| Displacement direction | not fixed by the lattice; an imported choice |
| Proposed trigger | $`L_f = v_c^2/a_0`$, falsified by SPARC |
| Predicted two-cluster structure ($`2/120`$) | not detected |

## I. The Tension

The Planck CMB measurement gives $`H_0 = 67.4 \pm 0.5`$ km/s/Mpc at $`z \approx 1100`$. The SH0ES collaboration measures $`H_0 = 73.04 \pm 1.04`$ km/s/Mpc from Cepheid-calibrated Type Ia supernovae at $`z \approx 0`$. The gap is 8.4%.

The two-camp description is accurate for those two anchors and is not an accurate description of the full literature. Tip-of-the-red-giant-branch and J-region asymptotic-giant-branch calibrations from the Carnegie-Chicago programme fall well below SH0ES, and time-delay cosmography spans a wide range depending on how the lens mass profile is treated. That untidiness matters for §V and is not incidental.

The framework's own phase-clock fit to Pantheon+ and DESI DR2 BAO prefers the low, Planck-side value, with $`H_0`$ entering as the fitted edge anchor rather than a derived output. It therefore sits on the CMB side of the pair and treats the local excess as the quantity requiring explanation.

In that reading, the two values are one Fibonacci well ($`\Theta_0 = 34/120`$) sampled at two positions. The CMB is taken to record a phase epoch predating local structure and therefore to sample the bare well; the local value corresponds to a one-step displacement. What the lattice fixes is the size of that step (§II). What it does not fix is why any observable would move, or in which direction.

## II. The Lattice Calculation

Independent of any galactic trigger, the lattice asks what one bosonic step would do at the $`H_0`$ well.

The phase operator $`C(\Theta) = 2\sin^2(\pi\Theta)`$ (the anti-periodic first-positive mode intensity, normalized to unit mean) has a logarithmic slope that differs at each well:

```math
\frac{d\ln C}{d\Theta} = 2\pi\cot(\pi\Theta)
```

| Well | Θ | Slope | Finite change at $`\Delta\Theta = +2/120`$ | Character |
|---|---|---|---|---|
| $`a_0`$ | 13/120 | 17.74 | $`+31.4\%`$ | steepest of the three |
| $`H_0`$ | 34/120 | 5.09 | $`+8.4\%`$ | measured through the field |
| $`\Lambda`$ | 60/120 | 0 | $`-0.27\%`$ | stationary to first order at the antinode |

The displacement column applies the same upward step at every well for comparison. Whether that step is the allowed one at $`a_0`$ is not settled here, since the framework treats $`a_0`$ as a dynamical rather than a bosonic observable.

$`\Lambda`$ sits at the antinode where the derivative vanishes identically, so it is stationary to first order in $`\Theta`$. It is not invariant under a finite step:

```math
\frac{C(62/120)}{C(60/120)} = \cos^2\!\left(\frac{\pi}{60}\right) = 0.99726
```

a change of $`-0.27\%`$. The same step moves $`H_0`$ by 8.4%, a factor of about thirty larger. That differential, rather than any protection, is the sense in which the framework can move $`H_0`$ while holding $`\Lambda`$ nearly fixed.

$`a_0`$ at slope 17.74 marks a steep, sensitive well. The derivative alone says nothing about the character of the MOND transition: a large derivative produces a sensitive continuous response, not a threshold. The binary mechanism that would have discretized it is the one §III reports as falsified.

### The 8.4% displacement

<p align="center"><img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/ht-well-steps.png?raw=true" width="80%" alt="The phase operator C(Theta) near the H0 well at 34/120, with the even positions of the bosonic sublattice filled and the odd positions open: one bosonic step up carries 67.4 to 73.04 (+8.4%), one step down carries it to 61.6 (-8.6%), and the odd step carries it to 70.24 (+4.2%)"></p>

At the bare well $`\Theta_0 = 34/120`$, and at the adjacent bosonic position $`\Theta = 36/120`$:

```math
C(34/120) = 1.2079, \qquad C(36/120) = 1.3090, \qquad \frac{C(36/120)}{C(34/120)} = 1.0837
```

Applied to the bare value:

```math
67.4 \times 1.0837 = 73.04 \;\text{km/s/Mpc}
```

which is the SH0ES scale. No galactic physics enters this calculation.

### What the step size assumes

Geometric observables are taken to access the 60-position bosonic sublattice, the even positions $`k/120 = j/60`$. That assignment is a framework selection rule, not a derivation, and it is the load-bearing assumption of this section. The stakes are direct: a displacement of $`1/120`$ would give $`C(35/120)/C(34/120) = 1.0421`$, a 4.2% shift rather than 8.4%.

Both available steps have a published local determination close to them. Against the same 67.4 baseline, SH0ES implies $`+8.4\%`$ and matches the $`2/120`$ step, while the Carnegie-Chicago tip-of-the-red-giant-branch value of 70.39 $`\pm`$ 1.22 (stat) $`\pm`$ 1.33 (sys) (Freedman et al. 2025, combined HST and JWST, 24 SN Ia calibrators) implies $`+4.4\%`$, close to the 4.2% of the $`1/120`$ step. The uncertainties do separate SH0ES from the $`1/120`$ endpoint, at two to three standard deviations. They do not separate the two local determinations from each other. The same programme's JWST-only figures, 68.81 and 67.80, imply offsets near 2.1% and 0.6% and match no lattice step at all.

Which step the framework calls correct is therefore not independent of which local determination is treated as canonical.

### The lattice does not fix the direction

The well at $`34/120`$ has two nearest bosonic neighbours, and they respond in opposite directions:

```math
\frac{C(32/120)}{C(34/120)} = 0.9144, \qquad \frac{C(36/120)}{C(34/120)} = 1.0837
```

a change of $`-8.6\%`$ or $`+8.4\%`$. The lattice fixes the magnitude of a nearest-neighbour response at this well to roughly 8.5%, but not its sign. The upward branch lands on the SH0ES scale; the downward branch would carry 67.4 to 61.6. Orientation was supplied by the positive indicator in the trigger of §III, and with that trigger retired, nothing tested here selects the sign. It is a fourth imported choice alongside the phase operator, the well assignment, and the sublattice assignment.

## III. The Trigger Hypothesis and Its Falsification

The lattice fixes the size of the displacement but not whether anything realizes it. The mechanism proposed for that role was a binary threshold on galactic environment, with a coherence scale set by the radius at which the gravitational field falls to the MOND acceleration:

```math
L_f = \frac{v_c^2}{a_0} \approx 13\;\text{kpc for the Milky Way}
```

Every calibrator inside that radius was to share one phase shift, and the response was binary: one bosonic grid step or nothing, $`\Theta_f = (2/120)\cdot\mathbf{1}(\mathcal{T} \geq \mathcal{T}_c)`$. The appeal was closure. For a flat rotation curve both the trigger index and its critical value scale as $`v_c^2`$, so their ratio is galaxy-independent and every flat-curve disk crosses the threshold by the same factor. The full specification, the geometry factor, and the registered predictions are in the [SPARC working note](/files/framework/files/working/files/sparc-phase-field.md).

Neither the scale nor the architecture was new. For a flat curve $`v_c^4 = GMa_0`$, so $`v_c^2/a_0 = \sqrt{GM/a_0}`$, the standard MOND transition radius. Applying an environmental gravitational threshold to distance-ladder calibrators and carrying the split into $`H_0`$ has a prior refereed instance in Desmond, Jain and Sakstein (2019). What the framework added was the proposal that the MOND radius also bounds a phase domain, and the quantized binary response.

### SPARC result

The trigger was tested against 123 quality-filtered SPARC rotation curves in a frozen, pre-registered pipeline ([dmobius3/phase-field](https://github.com/dmobius3/phase-field), archived at DOI [10.5281/zenodo.20271702](https://doi.org/10.5281/zenodo.20271702)), locked before data contact and executed once.

| Registered prediction | Criterion | Observed | Verdict |
|---|---|---|---|
| Transition radius tracks $`L_f`$ | OLS slope in [0.7, 1.3] | slope $`\approx 0.23`$ | Fail |
| Flat-onset radius tracks $`L_f`$ | ratio in [0.75, 1.25] | median 1.26 ($`n = 56`$) | Fail (near-miss) |
| Closure identity holds | $`\leq 5\%`$ of flat-curve galaxies below threshold | 53.7% below (66/123) | Fail |
| Trigger index predicts curve morphology | AUC separating flat from rising | no rising-curve galaxies pass cuts | Untestable |

Three of the four registered predictions returned a verdict and all three failed. The fourth returned none: no rising-curve galaxy survived the sample cuts, so the test that would have discriminated most sharply between the mechanism and ordinary galactic scaling was never evaluated. Verdicts are stable across the registered 27-cell sensitivity grid.

The direction of the failure is legible. Real rotation curves are not flat over $`[0, L_f]`$: for most disks the interval reaches inward across the rising part of the curve, so the mean-square velocity falls below the threshold, with typical suppression near 0.41 against $`\xi \approx 0.46`$. That last comparison is indicative rather than quantitative, because the two quantities were computed on different radial geometries and the mismatch biases it toward the failure it illustrates; the [working note](/files/framework/files/working/files/sparc-phase-field.md) carries the detail. The registered verdicts do not depend on it.

Post-hoc checks find that the transition radius correlates more tightly with baryonic mass than with $`L_f`$ at every plausible mass-to-light ratio, so the residual correlation is consistent with ordinary galactic size scaling rather than a phase-coherence effect. The threshold derivations built on $`L_f`$, namely the halo-profile geometry factor, the threshold hierarchy over the prime factors of 120, and the epoch-onset argument, are downstream of the trigger and are retired with it.

No replacement coherence scale is introduced here.

## IV. Propagation, Stated Conditionally

The propagation logic is separable from the trigger: it describes how a displacement would reach an inferred $`H_0`$, given that something produced one. With the trigger falsified, this section is conditional throughout.

Local distance ladders anchor their absolute scale to calibrators inside a putative coherence domain, so under that hypothesis every rung would inherit the full displacement. The ruler itself is shifted.

Geometric methods integrate $`1/H(z)`$ along the line of sight, so a locally confined displacement enters only through the coherent fraction of the path. A 13 kpc domain on a baseline of order 1 Gpc gives a fraction near $`10^{-5}`$, falling to $`3 \times 10^{-6}`$ at the Hubble radius. Applied to the 8.4% step, that leaves a direct path-averaging displacement of about one part per million.

This corrects the first version of this note, which treated phase-domain averaging as producing partial, intermediate $`H_0`$ values for geometric methods. The averaging channel is numerically irrelevant, and that prediction does not follow from it.

The correction leaves an unexplained observation rather than a repaired one. Megamasers and one standard treatment of time-delay lensing both return values near 74, where the corrected model no longer predicts anything intermediate. Explaining them would require an additional calibration-coupling mechanism that is not derived here.

## V. Test Outcomes

Two tests have been run. They carry different evidential weight and are reported separately for that reason.

### [Trigger: falsified](/files/framework/files/working/files/sparc-phase-field.md)

Pre-registered, locked before data contact, run once. The coherence scale $`L_f = v_c^2/a_0`$ does not behave as a coherence radius in observed galaxies. This is the heavier of the two results.

### [Discrete H₀ structure: not detected](/files/framework/files/working/files/h0-bimodality-test.md)

The original prediction was that $`H_0`$ should cluster at two quantized values with a clean gap between them. An exploratory compilation of 18 published determinations, of which 13 form a de-duplicated sensitivity subset, was tested against it.

| Pre-stated outcome | Observed |
|---|---|
| Continuous or intermediate spread rather than clean clusters | dip test cannot reject unimodality ($`p = 0.217`$ unweighted); intermediate values present |
| Two clusters at wrong values | GMM gives 68.4 / 73.5 where it picks two components; BIC margins are a statistical tie |
| TRGB or JAGB land near 70 | TRGB/CCHP at 69.8, inside the gap the $`2/120`$ picture predicts |
| Local methods near 73, early-universe near 67 | holds: class stratification is real |

The first three rows register against the original $`2/120`$ two-cluster picture. The fourth holds, but method-class stratification is the Hubble tension restated, not evidence of a quantized step.

This test is exploratory rather than pre-registered, so it carries less weight than the SPARC result. It is a compilation by method class rather than the environment-binned histogram originally nominated, making it a close relative of the registered falsifier rather than that falsifier exactly. With 18 determinations the dip test has limited power, so failing to reject unimodality is not positive evidence for a single population. The subset is de-duplicated, not statistically independent: three retained rows share Carnegie-Chicago lineage and calibration targets. Several rows carry disclosed provenance defects, documented in the working note, which further reduce the weight the result can bear. It also tested one step only: the companion note names the $`2/120`$ bosonic shift as its dependency, so the $`1/120`$ alternative of §II, which displaces $`67.4`$ to $`70.24`$, was never among the hypotheses under test. Whether a three-valued lattice fares better needed a new specification and a rerun rather than a rereading of this one; that respecification was run on 2026-09-02 and is recorded in the [companion note](/files/framework/files/working/files/h0-bimodality-test.md). It returned no lattice-specific evidence: the fixed-centre model's maximum-likelihood weight on the $`1/120`$ value is zero, and its advantage over a free two-component fit comes entirely from spending one fewer parameter.

### What the tests leave standing

The arithmetic of §II remains true, and neither test probes it. That is a weaker statement than it sounds. An identity survives a test it was never exposed to, but it gains nothing from surviving, and without a mechanism that selects it the correspondence carries little evidential weight. What the tests removed is not the number. It is the reason to think the number means anything physical.

## VI. What Survives

The correspondence: a one-step bosonic displacement from $`\Theta_0 = 34/120`$ to $`\Theta = 36/120`$ carries 67.4 km/s/Mpc to 73.04 through the phase-operator ratio, against $`-0.27\%`$ at $`\Lambda`$ under the same step.

It is fixed once four choices are stipulated: the phase operator, the well assignment, the bosonic-sublattice assignment, and the displacement orientation. All four are imported rather than derived here, $`H_0`$ is itself the framework's calibration anchor, and a domain carrying 120 positions carries many neighbouring ratios. The match is a retrospective structural correspondence, not an out-of-sample prediction and not statistical evidence.

What failed is the galactic mechanism that would force ordinary disk galaxies to realize the displacement, and the discrete two-population structure that realization would have produced.

What the failures leave is a specification. A replacement mechanism would have to select the bosonic sector and the direction on its own rather than inheriting them; run on a coherence scale other than $`v_c^2/a_0`$, while accounting for an acceleration transition observed near $`0.38\,L_f`$; work for rising inner rotation curves rather than assuming flatness; and not predict the clean bimodality that is already absent. It would also have to be derived independently rather than fitted to the data that falsified its predecessor.

*The discrepancy between the principal CMB and distance-ladder determinations is real. The lattice fixes a possible displacement scale. The physical operator that selects and realizes it remains unknown.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
