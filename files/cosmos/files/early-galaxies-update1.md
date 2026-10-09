<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Early Galaxies Update 1: MUSE-DARK III and the $`a_0(z)`$ direction

Tracking file for the epoch-dependent $`a_0`$ prediction between deposit and the formal $`z > 2`$ test. Update 1 logs MUSE-DARK III, the first robust intermediate-redshift measurement of the acceleration scale. The earlier low-$`z`$ measurement by Vărăşteanu et al. 2025, reaching $`z \sim 0.08`$, is taken up in §3. MUSE-DARK III appeared after the deposit and is not in the canonical paper. The picture it leaves is layered: the direction is corroborated, the rate is decomposition-dependent, the normalization is open, and the universality test, now runnable on the public per-galaxy data, proves structurally inapplicable. Each is recorded here alongside the paper's own intermediate-z tension so the whole stays visible.

**Measurement.** Ciocan, Bouché, Fensch, Krajnović, Freundlich, Desmond, Famaey & Techi (2026), *A&A* 709, L16; arXiv 2604.22613.

**Prediction (deposited).** Shatto, "Proposed Resolution of High-Redshift Galaxy Mass Anomalies via Epoch-Dependent Acceleration Scaling," Zenodo 10.5281/zenodo.18073340, 28 December 2025. Abstract: "the MOND acceleration scale a0 is not a universal constant but an epoch-dependent quantity scaling with the Hubble parameter H(z)," with a0(z=10) ≈ 20 × a0(0); §5 of the deposit pre-registers the *form*, "recovered a0 values larger than the local value, scaling approximately as H(z)/H0," with z > 2 named as the test. The prediction rests on Mode Identity Theory: Modal Realization from Nested Topology (Zenodo 10.5281/zenodo.18064856), the framework version the canonical paper cites.

**Mechanism (canonical).** Shatto, "Epoch-Dependent Acceleration Scale from Bounded Topology: Predictions for High-Redshift Galactic Dynamics," 13 June 2026; SSRN 6933958; Zenodo concept DOI 10.5281/zenodo.19980665.

**Timing.** The $`a_0 \propto H(z)`$ form was deposited 28 December 2025: after the first tentative low-$`z`$ observational hint of the same direction (Vărăşteanu et al. 2025, §3), but before the robust intermediate-$`z`$ MUSE-DARK III result. The deposit does not pre-register the direction, which was already weakly in print. What it states ahead of the robust data is the specific functional form, the locked exponent structure across five channels, and the mass- and aperture-independent universality (§6) that remains the discriminator. The framework reached $`a_0 \propto H(z)`$ as a consequence of the edge-mode structure, not as a fit to the rising-$`a_0`$ literature.

---

## 1. What MUSE-DARK III measures

79 star-forming galaxies at 0.33 < z < 1.44 (MUSE Hubble Ultra Deep Field). The RAR characteristic acceleration $`a_0`$ is fit per redshift bin (four quantile bins, ~20 galaxies each). $`a_0`$ increases systematically with redshift, ~1.99 (lowest bin) to ~2.71 (highest), in units of 10⁻¹⁰ m/s², significant at ~30σ against constant $`a_0`$. Global linear fit (dark-matter / DC14 decomposition): $`a_0(z) = 1.0 + 1.59\,z`$ (slope +0.11/−0.10).

## 2. What the framework predicted

$`a_0(z) = a_0(0)\,E(z)`$, with $`E(z) = H(z)/H_0`$. The canonical paper adopts the flat ΛCDM Friedmann form ($`\Omega_m = 0.315`$, $`\Omega_\Lambda = 0.685`$, $`H_0 = 67.4`$) as a transparency choice, for direct comparison with published data.

The ratio $`a_0/(cH) = C(13/120)/C(34/120) = 0.1845`$ follows from the phase-operator values at the Fibonacci wells 13 and 34 on the 120-domain, given one shared edge normalization; $`a_0`$ and $`H`$ are both edge modes ($`n = 1`$), so the ratio holds at every epoch. At $`z = 0`$, $`a_0(0) = 1.20`$ × 10⁻¹⁰ m/s² (SPARC), giving observed $`a_0/(cH_0) = 1.20/6.548 = 0.1833`$, a 0.7% match to that ratio.

The December deposit recorded the specific *form* ($`a_0 \propto H(z)`$) and named larger recovered $`a_0`$ values as the expected signature; the direction itself had already appeared weakly in the low-$`z`$ literature (§3), so what the timestamp establishes is the functional form, not the direction. The combinatorial fixing of the coefficient to 0.1845 above is the later canonical mechanism, not part of the timestamped prediction. Falsification (canonical paper, Table 5.1) sets two thresholds. A matched-systematics discrepancy at ≥2σ is a reportable tension. Formal falsification requires ≥3σ in one channel, or mutually consistent ≥2σ failures across independent bins or observables.

## 3. Direction: CORROBORATED (but non-discriminating)

The December deposit recorded the framework form, $`a_0(z) \propto H(z)`$, and expected recovered $`a_0`$ values larger than the local value. MUSE-DARK III measures $`a_0`$ rising at ~30σ over 0.33 < z < 1.44, the opposite of the falsification condition. The call was made in advance of the robust intermediate-$`z`$ result and came in on the right side, but the direction was already weakly in print.

The direction is not, however, a discriminator. The possibility that $`a_0`$ varies with cosmic time through its tie to $`H`$ is long-standing: Milgrom (1999) noted the $`a_0 \approx c H_0`$ coincidence, Limbach, Psaltis & Özel (2008) tested a Hubble- versus dark-energy-coupled $`a_0`$ against Tully–Fisher data to $`z = 1.2`$ and found the Hubble coupling disfavored at the precision then available, and Hossenfelder & Mistele (2018) derived a redshift-dependent $`a_0`$ in Covariant Emergent Gravity. ΛCDM is not exempt either: hydrodynamical simulations recover a rising best-fit $`a_0`$ (Mayer et al. 2023, Magneticum: ~3× from $`z = 0`$ to $`z = 2`$). There is also a direct observational precedent that predates the December deposit. Vărăşteanu et al. (2025, MIGHTEE-HI; arXiv:2504.20857) fit the RAR to $`z \sim 0.08`$ and reported the first tentative evidence for a rising acceleration scale, at roughly $`2.4\sigma`$. The direction was therefore already in print, weakly, before the framework's $`a_0(z)`$ deposit and before MUSE-DARK III. This sharpens rather than blunts the point: the framework's content is not that $`a_0`$ rises, but that it rises in a specific, locked, mass-independent way. So a climbing $`a_0`$ separates the framework from neither MOND-evolution proposals nor ΛCDM. The framework's distinct content is the mechanism (edge-mode phase wells, the locked exponent structure) and the specific functional form; the discriminating tests live in the form and the exponent lock at $`z > 2`$, not in the rise.

Scope: the formal falsification test names $`z > 2`$. MUSE-DARK III reaches $`z = 1.44`$, so this is corroboration in the predicted direction, with the formal test still owed.

## 4. Rate: measured to $`z = 1.44`$, and decomposition-dependent

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/muse_dark_iii_a0z_three_line.png/:/rs=w:1280,h:835" width="100%" alt="The framework curve a0(0)E(z) against the two MUSE-DARK III linear fits: the MOND-frame fit sits on the framework curve through the measured window, the dark-matter DC14 fit runs steeper, and both linear fits collapse to about 1.0 at z=0 against the SPARC anchor at 1.20.">

*The framework's convex $`a_0(0)\,E(z)`$ against the two MUSE-DARK III linear fits. In the MOND frame ($`a_0 = 1.03 + 1.20\,z`$) the data sit on the framework curve through the measured window; in the better-fitting dark-matter frame ($`a_0 = 1.0 + 1.59\,z`$) they run steeper. Both linear fits collapse toward 1.0 at $`z = 0`$ against the SPARC anchor at 1.20: that gap is the convex curve forced to a straight line, not a normalization mismatch. Solid where the data live (0.33 < z < 1.44), dashed out to $`z = 2`$.*

What is settled, and in every decomposition, is that the scale moves. The MUSE-DARK III masses are kinematic rather than photometric, and erasing the trend would demand stellar masses about 0.45 dex larger at high redshift, which the paper's own $`M/L_K`$ check against Drory rules out. So $`a_0`$ evolves as a matter of measurement, not merely as a rotation-curve modeling choice. That supports the framework's starting point, while leaving the discriminating claim, the locked form and universality, still open.

The *rate* of the climb depends on the decomposition. Under the dark-matter fit (DC14, the paper's headline) the trend runs as $`a_0 = 1.0 + 1.59\,z`$, faster than $`H(z)`$. Under the MOND decomposition, the natural frame for an acceleration scale that is only defined when the curve is read in MOND, it runs as $`a_0 = 1.03 + 1.20\,z`$, consistent with $`a_0(0)\,E(z)`$. The two frames are reconciled by a parameter-free postdiction: straight-line the convex curve $`a_0(0)\,E(z)`$ at $`a_0(0) = 1.2`$ across Ciocan's range and it returns an intercept near 0.97 and slope near 1.20, so forcing a line through the framework's own curve suppresses the zero-point from 1.2 to about 1.0 while holding the slope at 1.2. The MOND-frame fit, $`(1.03, 1.20)`$, sits on that artifact line; the DC14 slope of 1.59 lies well beyond anything an $`E(z)`$ curvature artifact produces. The honest register is *consistent with* $`a_0(0)\,E(z)`$, not *follows*: over this range a convex $`E(z)`$ and a plain line stay degenerate, so the matching intercept-slope pair explains the low MOND intercept without selecting $`E(z)`$ over other convex forms.

The steeper dark-matter frame fits marginally better, for more than 60% of the galaxies, but that is the decades-old result that a flexible halo fits an individual rotation curve at least as well as MOND's stiffer form (Rodrigues 2018 against McGaugh 2018), and the positive slope appears in both frames. So "the better-fitting frame says steeper" is real but weak.

The normalization stays open. The MUSE-to-SPARC scale is uncertain at tens of percent on both sides, and the larger lever is the omitted molecular gas the model carries as a flat profile: that term is z-dependent, climbing to a tens-of-percent baryon fraction by $`z \sim 1`$, and it is that z-dependence, not a uniform offset, that sits between the 1.20 and 1.59 slopes. On the framework side $`a_0(0) = 1.2`$ is fixed by SPARC (1.20 ± 0.26); the ratio 0.1845 reproduces it at $`H_0 = 67.4`$, a within-scheme echo at the weak weight the framework assigns that ratio elsewhere, not a second independent clamp.

## 5. The constraints bracket from both sides

MUSE-DARK III does not stand alone, and the surveys disagree in a telling way. The canonical paper's own intermediate-$`z`$ test is the Übler et al. KMOS3D Tully–Fisher comparison: a 2.9σ trend-shape tension under the most conservative systematics budget, the data non-monotonic against a monotonic prediction, held without retreat. It is a different observable (BTFR zero-point) from MUSE-DARK III's ($`a_0`$ via the RAR). Place the three side by side and they point opposite ways: Übler sits the framework too high near $`z = 2.3`$, Ciocan's dark-matter frame too low below $`z = 1.44`$, and Jeanneau 2026, accounting for the gas, finds the scale flat. Ciocan supplies the reason for the spread, that Übler's baryonic masses lean on scaling relations and drop the neutral gas. Opposite-pointing tensions are the fingerprint of cross-survey systematics, not a clean falsification. That sharpens the case for a matched-systematics arbiter, but it cuts only one way: it leaves the rate open, not vindicated. Survey disagreement rescues no particular value. Vărăşteanu et al. 2025 now serves as the low-$`z`$ anchor in the same direction, while MUSE-DARK III supplies the first robust intermediate-$`z`$ test; the remaining discriminator is not direction but functional form and universality.

## 6. Universality: the public test, run, and why it cannot settle the question

The framework's discriminator is whether one $`a_0`$ holds across galaxy mass. The MUSE-DARK release makes a per-galaxy test reachable: the posted DC14 fits give, for each galaxy, the dark-matter fraction within $`R_e`$ and the disk mass and size, which invert through the standard RAR relation to $`a_0 = g_{\rm bar}(R_e)/[\ln(1/f_{\rm DM})]^2`$. We ran it on all 126 galaxies; it cannot settle the question, for a structural reason. The fits hold $`f_{\rm DM}`$ flat with mass while $`g_{\rm bar}`$ rises, which makes $`a_0 \propto g_{\rm bar}`$, so the climb of $`a_0`$ with mass is the baryonic surface-density relation re-expressed rather than a property of $`a_0`$. A single $`a_0`$ instead requires $`f_{\rm DM}`$ to fall as $`g_{\rm bar}`$ rises; the flat $`f_{\rm DM}`$ the fits return is, for these dispersion-supported disks, more plausibly a galpak prior than a measurement, and a prior-flattened $`f_{\rm DM}`$ manufactures exactly this signal. The estimator is fragile on its own terms as well, carrying a pole as $`f_{\rm DM} \to 1`$: a seventh of the sample sits above 0.95, and across $`f_{\rm DM}`$ from 0.80 to 0.95 the inferred $`a_0`$ swings twentyfold from the estimator alone. The public DC14-frame data are therefore uninformative on $`a_0`$ universality in principle, leaving a degeneracy between a non-universal $`a_0`$ and a prior-driven $`f_{\rm DM}`$ that is exactly the stellar-M/L freedom an M/L-independent measurement removes. What the question needs is that M/L-independent measurement, and stacked galaxy–galaxy lensing at $`z \approx 0.5`$ to $`2`$ is the natural instrument for it. That route carries a condition. The framework supplies a Newtonian-equivalent dynamical prediction, not a relativistic lensing law, and outside general relativity the potential that deflects photons need not track the one that governs dynamics. Under a completion in which the lensing potential inherits the same $`E(z)`$ scaling, the forecast is a mass- and aperture-independent $`\sqrt{E(z)} = 1.74`$ at $`z = 2`$ against $`\Lambda`$CDM's mass-dependent 0.76 to 1.13. That completion is not yet supplied, so the number stands as a conditional forecast rather than a standing prediction, and the dynamical channels carry the falsifiable weight.

## 7. Methods and diligence

The per-galaxy test above ran on the public MUSE-DARK release (dark-matter.osu-lyon.fr), which posts the galpak DC14 fit for each galaxy: the dark-matter fraction $`f_{\rm DM}`$ within $`R_e`$, the disk mass and size, and the gas surface density, with SED stellar masses and redshifts in the photometry catalogue. For each galaxy the standard RAR interpolating function inverts at $`R_e`$ to $`a_0 = g_{\rm bar}(R_e)/[\ln(1/f_{\rm DM})]^2`$, with $`g_{\rm bar} = G\,M_{\rm bar}(<R_e)/R_e^2`$. Of the 126, two return 404 stubs and three lack a photometry-catalogue match or an in-range $`f_{\rm DM}`$, leaving 121 in the untrimmed sample. The MOND free-fit $`a_0`$ values, the clean frame, are not in the release; this is the DC14 frame.

**The apparent trend is not robust to the estimator's own pathology.** Trimming the $`f_{\rm DM} \to 1`$ tail drives the slope on both mass scales to the same significant positive value; the untrimmed "flat with dynamical mass" null (the reading an interim draft leaned on) is an artifact of that tail compounded by partial self-regression, since $`a_0`$ is built from the dynamical mass.

| f_DM cut | N | slope vs dynamical mass | slope vs SED mass |
|---|---|---|---|
| untrimmed | 121 | +0.085 ± 0.072 (t = 1.2) | +0.311 ± 0.070 (t = 4.5) |
| < 0.95 | 103 | +0.175 ± 0.062 (t = 2.8) | +0.221 ± 0.064 (t = 3.5) |
| < 0.90 | 87 | +0.198 ± 0.061 (t = 3.2) | +0.211 ± 0.066 (t = 3.2) |
| < 0.85 | 70 | +0.258 ± 0.069 (t = 3.7) | +0.244 ± 0.070 (t = 3.5) |

**The pole is why the per-galaxy scatter is meaningless.** At fixed $`g_{\rm bar}`$, a galaxy at f_DM = 0.95 inherits an $`a_0`$ nineteen times one at 0.80 from the estimator alone, and a seventh of the sample sits above 0.95. The reconstructed range (0.08 to 175, in 10⁻¹⁰ m/s²) is twentyfold wider than Ciocan's free-fit 0.13 to 9.6 for this reason.

| f_DM | [ln(1/f_DM)]² | a₀ relative to f_DM = 0.80 |
|---|---|---|
| 0.50 | 0.480 | 0.1 |
| 0.80 | 0.050 | 1.0 |
| 0.90 | 0.011 | 4.5 |
| 0.95 | 0.0026 | 18.9 |
| 0.98 | 0.0004 | 122 |
| 0.99 | 0.0001 | 493 |

**Validation.** Against Ciocan's own DC14 climb the one-point estimator matches only near $`z \approx 0.78`$, undershooting at the low end and oversteepening above $`z \approx 1`$ where $`f_{\rm DM}`$ runs highest and the pole bites: it is reliable only in a narrow mid-$`z`$ window, and its excursions on either side are propagated $`f_{\rm DM}`$ sensitivity, not physics.

| z bin | reconstructed median a₀ | Ciocan DC14 (1.0 + 1.59z) |
|---|---|---|
| ~0.49 | 0.86 | 1.79 |
| ~0.78 | 2.25 | 2.23 |
| ~1.00 | 4.65 | 2.59 |
| ~1.27 | 5.67 | 3.03 |

The reconstruction was checked by an internal adversarial review that reproduced the pipeline from the public files, confirmed the numbers, and corrected the interim interpretation: the dynamical-mass null cannot be cited as consistency with universality, and the trend is carried by $`g_{\rm bar}`$ (surface density), not by a stellar-M/L offset. The surviving bottom line is the structural one in §6.

## 8. Summary and disposition

| Claim | Status | Detail |
|---|---|---|
| $`a_0`$ evolves with $`z`$ (direction) | CORROBORATED, non-discriminating | Direction first measured tentatively at low $`z`$ by Vărăşteanu 2025 (~2.4σ), before the Dec 2025 deposit; MUSE-DARK III measures it robustly at intermediate $`z`$ (~30σ); also predicted by MOND-evolution models and ΛCDM simulations (Mayer 2023) |
| Rate, a₀(z) shape | DECOMPOSITION-DEPENDENT | MOND frame consistent with E(z) via the convex postdiction; DC14 frame steeper; Übler / Ciocan / Jeanneau bracket from both sides (systematics-limited) |
| a₀(0) normalization | OPEN | Tens of percent cross-calibration; SPARC fixes it, the 0.1845 ratio echoes it |
| a₀ universality (public ground test) | INAPPLICABLE | Flat f_DM forces a₀ ∝ g_bar; degenerate with a prior-driven f_DM; the clean test would be M/L-independent lensing, conditional on a relativistic completion (§6) |
| BTFR trend shape (Übler) | TENSION | 2.9σ, non-monotonic data vs monotonic prediction |
| Formal z > 2 test | NOT YET IDENTIFIED | Matched-systematics BTFR at $`z \approx 2.3`$ (JWST NIRSpec IFU or ground IFU); Euclid's slitless NISP delivers redshifts, not resolved rotation curves |

The disposition is unchanged in destination and sharper in reason. The direction is corroborated, the rate is open and decomposition-dependent, and the universality test is now demonstrated, on the public data and against my own initial lean, to be uninformative on its own terms: the ground-based inversion cannot separate a non-universal $`a_0`$ from a prior-driven $`f_{\rm DM}`$. What discriminates is universality, not the climb, and measuring it cleanly calls for an M/L-independent probe. Stacked galaxy–galaxy lensing at $`z = 0.5`$ to 2 would supply one, giving a mass- and aperture-independent $`M_\text{dyn}/M_b`$ enhancement of $`\sqrt{E(z)} = 1.74`$ at $`z = 2`$ against ΛCDM's mass-dependent 0.76 to 1.13, on the condition that a relativistic completion carries the $`E(z)`$ scaling into the lensing potential. That condition is open, which leaves the near-term weight on a matched-systematics BTFR comparison at $`z \approx 2.3`$.

---

*Update 1, drafted 2026-06-24. The per-galaxy reconstruction (§§6–7) runs on the public MUSE-DARK release; the MOND free-fit $`a_0`$ values remain unreleased, so the clean test waits on their release or on an M/L-independent probe.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
