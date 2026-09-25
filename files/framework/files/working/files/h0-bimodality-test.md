<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# H₀ Bimodality: Discrete-vs-Continuous Test of the Section V Fork

**Type:** Test
**State:** Closed
**Verdict:** Negative
**Status (2026-09-02):** The discrete two-cluster prediction is not supported (dip test fails to reject unimodality; GMM ΔBIC < 1.2). The V-A respecification against the three-valued lattice removed the specification defect and still returns no lattice-specific evidence: the middle component carries weight zero in all eight cells.
**Summary:** Tests whether published H₀ determinations cluster into the discrete states the hubble-tension §V fork predicts, or form a continuous spread.
**Inputs:** `../../../../cosmos/files/hubble-tension.md` (§V fork, §II lattice), the 18-determination compilation, `sparc-phase-field.md`
**Frozen:** 2026-05-19 the original 18-row data table and adjudication (the TRGB/CCHP row kept so the original run stays reproducible)

Analysis complete (2026-05-19). Exploratory, not pre-registered. The discrete two-cluster prediction is not supported; the Section V fork leans continuous.

**Related:** [hubble-tension.md](../../../../cosmos/files/hubble-tension.md), [sparc-phase-field.md](sparc-phase-field.md).

---

## The Question

The Hubble-tension note ([hubble-tension.md](../../../../cosmos/files/hubble-tension.md)) Section V states a discrete prediction: local H₀ should cluster at quantized values set by the lattice, not vary continuously between 67 and 73. The phase operator admits only the bare well ($`\Theta_0 = 34/120`$, H₀ ≈ 67) and the one-step shift ($`\Theta = 36/120`$, H₀ ≈ 73). Nothing in between.

This test asks one question: **do published H₀ measurements cluster into two discrete populations, or do they form a continuous spread?**

It is independent of the trigger mechanism. The SPARC test ([sparc-phase-field.md](sparc-phase-field.md)) falsified the specific coherence-scale trigger $`L_f = v_c^2/a_0`$. The trigger says *why* a shift would happen; the bimodality test asks *whether* the two-population structure exists at all. A discrete framework can survive a failed trigger; it cannot survive a continuous H₀ distribution.

This is a blind reanalysis of public data, not a pre-registered test. Every H₀ value used here was already published and widely known. The analysis choices (de-duplicated-subset membership, the statistical thresholds, the gap range) were fixed before the tests were run, but the data could not be blinded. The genuine forward test remains Euclid DR1.

---

## Result

**The discrete two-cluster prediction is not supported by current published H₀ data.**

The distribution is statistically consistent with a single continuous population. It does sort by calibration class (early-universe low, local-ladder high), but that stratification is the Hubble tension itself; it is not evidence of a discrete quantized step.

Three tests, run on a full 18-measurement set and a 13-row de-duplicated subset, with the model-dependent TDCOSMO value swapped between its two published determinations as a sensitivity check. All four configurations agree.

- **Hartigan dip test.** Fails to reject unimodality in every configuration. Primary config (de-duplicated subset, TDCOSMO = Shajib): p = 0.217 unweighted, median p = 0.469 with measurement uncertainties propagated by Monte Carlo, and only 5.3% of MC draws reach p < 0.05. No statistical signal of bimodality.
- **Gaussian mixture.** BIC does not cleanly separate 1- from 2-component fits: the de-duplicated subset weakly favours 2 components, the full set weakly favours 1, and every ΔBIC is far below the ≈ 2 threshold for even weak evidence. The models are effectively tied. Where a 2-component fit is the nominal pick, its means land near 68.4 and 73.5, not the lattice-predicted 67 and 73.
- **Gap test.** The predicted 69 to 71 gap is not empty. TRGB / CCHP (Freedman) at 69.8 ± 1.7 falls inside it, and JAGB / CCHP at 67.8 blurs the low edge.

By the Section V kill table, a failure to reject unimodality is evidence against the quantized-step picture.

---

## I. Data

Eighteen published H₀ determinations, one row per analysis, compiled 2026-05-19 from the primary literature. Units km/s/Mpc. The "Dedup." column marks membership in the de-duplicated subset (Section II).

| Method | Class | H₀ | σ | Reference | Dedup. |
|---|---|---|---|---|---|
| CMB, Planck 2018 | early-universe | 67.40 | 0.50 | Planck Collab. 2020 | Y |
| CMB, ACT DR6 | early-universe | 68.30 | 1.10 | Madhavacheril et al. 2024 | Y |
| CMB, SPT-3G | early-universe | 66.81 | 0.81 | SPT-3G / Camphuis 2025 | Y |
| BAO + BBN, DESI DR2 | early-universe | 68.52 | 0.62 | DESI Collab. 2025 | Y |
| Cepheid + SNIa, SH0ES (HST) | local-ladder | 73.04 | 1.04 | Riess et al. 2022 | Y |
| JWST Cepheids, CCHP | local-ladder | 72.05 | 3.62 | Freedman et al. 2025 | Y |
| JWST Cepheids, SH0ES | local-ladder | 72.60 | 2.00 | Riess et al. 2024 | N |
| TRGB, CCHP | local-ladder | 69.80 | 1.71 | Freedman et al. 2019/2021 | Y |
| TRGB, Anand 2022 | local-ladder | 71.50 | 1.80 | Anand et al. 2022 | N |
| JAGB, CCHP | local-ladder | 67.80 | 2.72 | Lee et al. 2024 | Y |
| Mira variables | local-ladder | 73.06 | 2.67 | cluster-Mira team 2025 | Y |
| Surface brightness fluctuations | local-ladder | 73.30 | 2.40 | Blakeslee et al. 2021 | N |
| Tully-Fisher relation | local-ladder | 73.30 | 4.08 | Boubel et al. 2024 | N |
| Megamasers, MCP | geometric | 73.90 | 3.00 | Pesce et al. 2020 | Y |
| Time-delay lensing, TDCOSMO | geometric | 74.20 | 1.60 | Shajib et al. 2023 | Y |
| Standard sirens, GW170817 | geometric | 70.00 | 10.00 | Abbott et al. 2017 | Y |
| Cepheids only, no SNe | local-ladder | 71.70 | 1.30 | Stiskalek et al. 2026 | N |
| Type II SNe, tailored EPM | independent | 74.90 | 1.90 | Vogl et al. 2025 | Y |

**Source audit (2026-07-30).** Every row was re-verified against its published source for the paper revision. No value or subset flag changed; the analysis is untouched. Three findings worth recording:

- **The σ convention is quadrature.** Where a source quotes separate statistical and systematic errors, this table's σ is their quadrature sum. Confirmed independently on two rows: JAGB, $`\sqrt{2.17^2 + 1.64^2} = 2.72`$; Tully-Fisher, $`\sqrt{2.1^2 + 3.5^2} = 4.08`$. The convention was applied consistently.
- **Both CMB rows need disambiguation, and neither is wrong.** ACT DR6 and SPT-3G each publish several $`H_0`$ values from different analyses of the same data, so a row labelled only by experiment is ambiguous even when its number is correct. ACT DR6's 68.30 ± 1.10 is the **lensing + BAO** constraint of Madhavacheril et al. 2024 (ApJ 962, 113), not the Louis et al. 2025 power-spectra determination. SPT-3G's 66.81 ± 0.81 is the **lensing / delensed-EE** result, not the SPT-3G D1 TT/TE/EE headline of 66.66 ± 0.60 (Camphuis et al. 2025). Both were flagged as suspected errors during the audit and both cleared on checking.
- **The Mira row is unsourced.** Its value 73.06 ± 2.67 could not be matched to any published Mira determination, and "cluster-Mira team 2025" is a collective label rather than a citation. Published Mira results found in the check were 72.7 ± 4.6, 73.3 ± 4.0, and 72.37 ± 2.97, none of which is the tabulated value. **This row needs a real source or removal.** It is retained for now because the frozen analysis was run with it included; the paper reports it as unresolved rather than dropping it silently. Note the row is inside the 13-row subset, so a correction would change the dip-test and GMM inputs.

Notes on individual rows. The Stiskalek et al. 2026 value is the MNRAS abstract figure 71.7 ± 1.3, the result under the paper's main stated selection assumption. GW170817 has an asymmetric interval (+12/−8); a symmetric σ ≈ 10 is used as a placeholder. The TDCOSMO row is model-dependent: Shajib et al. 2023 (parametrized mass profiles) gives 74.2 ± 1.6, Birrer et al. 2020 (maximally flexible mass models) gives 67.4 ± 3.7. Both are carried as a sensitivity check.

---

## II. Method

### De-duplicated subset

The 18 measurements are not 18 independent data points. Many share anchor galaxies, supernova samples, or calibration steps; correlated measurements inflate apparent bimodality. Five rows are dropped from the primary subset:

- **JWST Cepheids, SH0ES (Riess 2024)** is an explicit cross-check of Riess et al. 2022, same team, anchors, and supernova sample.
- **TRGB, Anand 2022** is a re-reduction of the same CCHP TRGB photometry with a different edge-detection method.
- **Cepheids only (Stiskalek 2026)** is a re-analysis of the SH0ES second-rung Cepheid data.
- **Surface brightness fluctuations** has a zero-point tied to the Cepheid scale; it inherits that calibration rather than measuring H₀ independently.
- **Tully-Fisher** has a zero-point calibrated on Cepheid and TRGB distances; same inheritance.

The 13-row de-duplicated subset is the primary set; the full 18-row set is reported as secondary. De-duplication removes the obvious re-analyses; it does not make the remainder statistically independent. Three retained rows come from the Carnegie-Chicago programme and share its lineage and calibration targets, and the retained ladder determinations are not mutually independent in a strict sense; a dependency matrix would be needed to support a stronger label. The four early-universe experiments are kept in but share sound-horizon physics, noted where relevant.

### Tests

1. **Hartigan dip test** for unimodality. Run unweighted on the central values, then in a Monte-Carlo variant: each iteration draws every measurement from $`\mathcal{N}(H_0, \sigma^2)`$ and runs the dip test on the pooled draw, so a wide measurement spreads its mass and contributes less to any apparent cluster (5000 draws). The dip test has no native weighting; this is the uncertainty-propagated equivalent.
2. **Gaussian mixture model**, 1 versus 2 components, compared by BIC.
3. **Gap test**: count of measurements in the predicted 69 to 71 gap, with GW170817 excluded because its σ ≈ 10 spans the whole range.

Each test is run on both sets and both TDCOSMO values.

---

## III. Findings

### By method

<p align="center"><img src="figures/h0-bimodality-fig1-by-method.png" alt="H₀ by method"></p>

Every measurement with its error bar, sorted by H₀ and coloured by class. The early-universe cluster (66.8 to 68.5) is tight. The local side is a smear from 71.5 to 74.9 with no obvious sub-peak. Two local-ladder methods sit inside or next to the predicted gap (grey band): JAGB at 67.8 and TRGB / CCHP at 69.8.

### Dip test

| Configuration | dip p (unweighted) | median p (MC) | MC fraction p < 0.05 |
|---|---|---|---|
| De-duplicated, TDCOSMO = Shajib (primary) | 0.217 | 0.469 | 5.3% |
| Full, TDCOSMO = Shajib | 0.722 | 0.606 | 2.3% |
| De-duplicated, TDCOSMO = Birrer | 0.661 | 0.648 | 2.9% |
| Full, TDCOSMO = Birrer | 0.308 | 0.620 | 1.9% |

The null hypothesis is unimodal. It is not rejected anywhere.

<p align="center"><img src="figures/h0-bimodality-fig2-histogram.png" alt="Histogram with dip test"></p>

The KDE shows a soft two-hump shape driven by the genuine class stratification, but the trough is too shallow for the dip test to flag.

### Gaussian mixture

BIC does not cleanly prefer two components. The de-duplicated subset weakly favours a 2-component fit (ΔBIC 0.47 with TDCOSMO = Shajib, 0.15 with Birrer); the full 18-row set weakly favours a single component (ΔBIC 0.73 and 0.30 the other way). Every margin is far below the ΔBIC ≈ 2 threshold for even weak evidence, so the 1- and 2-component models are statistically tied in all four configurations. Where a 2-component fit is the nominal pick (the de-duplicated subset), its means come out near 68.4 and 73.4 to 73.5: the low cluster is roughly one unit above the lattice value of 67.

<p align="center"><img src="figures/h0-bimodality-fig3-gmm.png" alt="GMM model selection"></p>

### Gap test

One retained local-ladder method falls in the predicted 69 to 71 gap: TRGB / CCHP (Freedman) at 69.8 ± 1.7. JAGB / CCHP at 67.8 blurs the low edge. The gap is populated, not clean.

### Class means

Inverse-variance weighted: early-universe 67.7 (n = 4, range 66.8 to 68.5); local-ladder 71.9 to 72.0; geometric 74.0; Type II SNe EPM 74.9. The class stratification is real. The discrete quantization is not.

---

## IV. Reading against the Section V kill table

| Pre-stated outcome | Observed | Implication |
|---|---|---|
| Continuous spread 67 to 73 | Dip test cannot reject unimodality | Falsifies quantized step |
| Two clusters at wrong values (e.g. 68 and 72) | GMM, where it picks 2 components, gives 68.4 / 73.5 | Quantized step wrong size |
| TRGB or JAGB land near 70 | TRGB / CCHP at 69.8, in the gap | Intermediate state; single-step picture fails |
| Local methods near 73, early-universe near 67 | Holds: see class means | Method-class stratification present |

The first three rows all register against the discrete picture. The fourth holds, but method-class stratification is just the Hubble tension restated; it is not evidence of a discrete quantized step.

---

## V. Caveats

- **Low statistical power.** With 13 to 18 measurements the dip test has limited power. "No evidence for bimodality" is not the same as a strong falsification. By the Section V kill table a failure to reject unimodality counts as evidence against the quantized picture, and that is the standard applied here.
- **The soft two-hump shape is real** but too shallow for the dip test to flag and too weak for the GMM to distinguish from a single broad population.
- **TDCOSMO model choice does not matter.** Swapping Shajib 2023 (74.2) for Birrer 2020 (67.4) changes no verdict.
- **SH0ES per-host H₀ not used.** Per-host distance moduli would add ~37 points, all local-ladder class; they probe intra-sample scatter rather than the bimodality fork and would not change this verdict. Available as an extension.

---

## V-A. Respecification against the three-valued lattice (2026-09-02)

*Added after the 2026-05-19 analysis. Nothing above is edited: the frozen table, the tests, the kill-table reading and the caveats all stand as run.*

**Why this exists, and when the motivation was found.** The analysis above tests a two-cluster prediction, and its Dependencies line names the bosonic step $`2/120`$. The hubble-tension page's §II, however, treats two steps as available and finds a local determination near each: $`2/120`$ gives $`67.4 \to 73.04`$, and $`1/120`$ gives $`67.4 \to 70.24`$. So the lattice that page describes has three values, and the middle one falls inside the 69 to 71 band this test treats as a predicted gap. The original test was therefore under-fitted to the framework's own prediction. **That was noticed on 2026-09-02, after the two-cluster version had returned its null.** Respecifying a test after it returns null is what pre-registration exists to prevent; it is admissible here only because this analysis states in its own Status line that it is exploratory and not pre-registered, and the ordering is recorded rather than presented as though the three-valued form had been the plan.

**Design, fixed before any fit was run.** Three models compared by BIC on identical rows, with each point entering as a Gaussian of its own $`\sigma_i`$ so that measurement error is carried rather than fitted:

| | model | free parameters |
|---|---|---|
| A | one Gaussian, free mean and width (the continuous alternative) | 2 |
| B | two Gaussians, **free** means, common intrinsic scatter | 4 |
| C | three Gaussians, centres **fixed** at 67.40 / 70.24 / 73.04, common intrinsic scatter | 3 |

C is the lattice hypothesis: its centres are predicted rather than fitted, which is why it can carry fewer parameters than B. The expectation recorded before running was that a second null was the likely outcome and would be the better one, since it would test the proposition the framework actually makes.

**Data.** This is a new analysis and runs on current values, so the CCHP TRGB row is entered at $`70.39 \pm 1.80`$ (Freedman et al. 2025, stat and sys in quadrature per this table's own convention) rather than the frozen $`69.80 \pm 1.71`$. That row is the one the respecification is about: it sits 0.15 from the middle lattice centre where the frozen value sat 0.44 from it. Both TDCOSMO configurations are carried, as the frozen analysis carried them. Both the 13-row de-duplicated subset and the full 18 rows are reported.

**The two TRGB values are both correct and neither should be reconciled to the other.** The table in section I keeps $`69.80 \pm 1.71`$ because that is the value the 2026-05-19 analysis ran on, and every statistic above it, the dip test, the mixture fits, the BIC margins, the gap test and the class means, is reproducible only against that row. This addendum runs on $`70.39 \pm 1.80`$ because it is a new analysis and current values are the right input for one. **Updating the frozen row to match this one would silently destroy the reproducibility of the original run**, which is the only thing that row is for. The difference between the two figures is the subject of this section, not an inconsistency in it.

**Result, all eight cells.** $`\Delta`$BIC is measured from the best model in each cell.

| TRGB | TDCOSMO | rows | $`\Delta`$BIC A | $`\Delta`$BIC B | $`\Delta`$BIC C | middle weight | $`\ln L`$ (B) $`-`$ $`\ln L`$ (C) |
|---|---|---|---|---|---|---|---|
| 69.80 | Shajib | 13 | 3.62 | 0.84 | 0.00 | 0.000 | +0.864 |
| 69.80 | Shajib | 18 | 2.70 | 1.19 | 0.00 | 0.000 | +0.852 |
| 69.80 | Birrer | 13 | 2.50 | 0.94 | 0.00 | 0.000 | +0.811 |
| 69.80 | Birrer | 18 | 1.09 | 0.64 | 0.00 | 0.000 | +1.128 |
| **70.39** | Shajib | 13 | 3.72 | 1.10 | 0.00 | **0.000** | +0.730 |
| **70.39** | Shajib | 18 | 3.08 | 1.29 | 0.00 | **0.000** | +0.800 |
| **70.39** | Birrer | 13 | 2.49 | 1.11 | 0.00 | **0.000** | +0.726 |
| **70.39** | Birrer | 18 | 1.41 | 0.70 | 0.00 | **0.000** | +1.097 |

**Three readings, and the first is the weakest.** C has the lowest nominal BIC in every cell. It is called nominal because a fitted mixture weight of exactly zero is a boundary solution, and ordinary BIC asymptotics are not clean for finite mixtures at a boundary.

Its margin over B is 0.64 to 1.29, which on the Kass-Raftery scale is not worth more than a bare mention, and the decomposition is worse than the margin suggests: the final column shows B fitting **better** in every cell, by 0.73 to 1.13 log units. C wins only because it spends one fewer parameter. Fixing the centres to the lattice does not describe these data better than fitting the centres freely; it describes them slightly worse and costs less. C's only real margin is over A, at 1.09 to 3.72, and A was never the framework's competitor: two populations separated by method class is the Hubble tension restated, which section III already says.

**The middle component carries zero weight in all eight cells**, including on the current TRGB value that sits 0.15 from that centre. The lattice state whose existence motivated this entire respecification draws no support from the data.

**Zero is the maximum-likelihood point, not an exclusion.** Forcing weight onto the 70.24 component, on the current compilation and the de-duplicated subset, costs

| forced middle weight | 0.05 | 0.10 | 0.20 | 1/3 |
|---|---|---|---|---|
| cost in $`\ln L`$ | 0.170 | 0.365 | 0.824 | 1.576 |

No conversion to $`\sigma`$ is quoted: a weight sitting at zero is on a boundary, where standard likelihood-ratio asymptotics do not apply cleanly. The plain statement is that the maximum-likelihood fit assigns the middle component nothing, and that this compilation does not strongly exclude a middle population of up to roughly a third.

**Verdict.** The three-valued respecification removes the specification defect in the original two-cluster test but does not produce lattice-specific evidence. The fixed-centre three-component model has the lowest nominal BIC on every configuration, yet its maximum-likelihood middle-component weight is zero and its advantage over a free two-component mixture is negligible and comes entirely from the parameter penalty. The data continue to support method-class structure without providing evidence that the lattice centres, or specifically the $`1/120`$ state at 70.24, organize that structure. A middle population is not excluded by a compilation this small. **The specification question raised on 2026-09-01 is closed; the answer did not change.**

---

## VI. Relation to the SPARC result

The two registered tests separate cleanly. SPARC ([sparc-phase-field.md](sparc-phase-field.md)) falsified the coherence-scale trigger $`L_f = v_c^2/a_0`$: the mechanism that would force ordinary disk galaxies to realize the phase shift. This test addresses the downstream observable: whether the shift, however triggered, leaves a discrete two-population fingerprint in H₀ data. It does not.

Both outcomes are negative for the testable phase-field predictions, and both leave the lattice arithmetic untouched. The 8.4% well sensitivity at $`\Theta_0 = 34/120`$ (hubble-tension.md Sections III and IV) is geometry, not a claim either test probes. What fails here is the empirical signature the discrete picture would produce: current H₀ data is consistent with a continuous distribution, sorted by calibration class but not quantized.

---

## References

- Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters. A&A, 641, A6.
- Madhavacheril, M. S., et al. (2024). The Atacama Cosmology Telescope: DR6 Gravitational Lensing. ApJ, 962, 113.
- SPT-3G Collaboration / Camphuis, E., et al. (2025). SPT-3G D1 TT/TE/EE. arXiv:2506.20707.
- DESI Collaboration (2025). DESI DR2 Results II. Phys. Rev. D, 112, 083515.
- Riess, A. G., et al. (2022). A Comprehensive Measurement of the Local Value of the Hubble Constant. ApJ, 934, L7.
- Riess, A. G., et al. (2024). JWST Observations Reject Unrecognized Crowding of Cepheid Photometry. ApJ, 962, L17.
- Freedman, W. L., et al. (2025). Status Report on the Chicago-Carnegie Hubble Program. ApJ, 985, 203.
- Freedman, W. L., et al. (2021). Calibration of the TRGB. ApJ, 919, 16.
- Anand, G. S., et al. (2022). Comparing TRGB Distances. ApJ, 932, 15.
- Lee, A. J., et al. (2024). The JAGB Method. arXiv:2408.03474.
- Pesce, D. W., et al. (2020). The Megamaser Cosmology Project XIII. ApJ, 891, L1.
- Shajib, A. J., et al. (2023). TDCOSMO XII. A&A, 673, A9.
- Birrer, S., et al. (2020). TDCOSMO IV. A&A, 643, A165.
- Abbott, B. P., et al. (2017). A gravitational-wave standard siren measurement of the Hubble constant. Nature, 551, 85.
- Vogl, C., et al. (2025). No rungs attached: a tailored EPM measurement of H₀. A&A, 702, A41.
- Blakeslee, J. P., et al. (2021). SBF Distances. ApJ, 911, 65.
- Boubel, P., Colless, M., Said, K., et al. (2024). An improved Tully-Fisher estimate of H₀. MNRAS, 533, 1550.
- Stiskalek, R., et al. (2026). A 1.8 per cent measurement of H₀ from Cepheids alone. MNRAS, 546, staf2260.
- Shatto, B. (2026). Mode Identity Theory engine file. github.com/dmobius3/mode-identity-theory

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
