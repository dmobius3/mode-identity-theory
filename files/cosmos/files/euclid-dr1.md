<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🔮 Euclid DR1 Showdown

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/dr1%20banner.png?raw=true" width="100%" alt="Euclid DR1">

The Euclid Data Release 1 arrives in two stages. DR1-Foundation, in November 2026, carries the raw data and calibrated images, catalogues and spectra over about 1900 deg², with no cosmology-derived products. The full DR1, in mid 2027, adds the higher-level science products for galaxy clustering and weak lensing. ESA states that these dates are tentative and will have to be confirmed. Five Mode Identity Theory predictions are registered here, before the data, against four named contenders: flat ΛCDM, w<sub>0</sub>w<sub>a</sub>CDM (CPL), early dark energy (EDE), and MOND / relativistic MOND. Each row is a head-to-head with a stated falsification threshold for MIT. Row IV, the high-<i>z</i> stellar mass function, was the one row expected at the Foundation stage; the other four read cosmology-derived products and wait for the full release. Results will be added in later commits as each stage lands. Row I was given its scoring rule on 2026-09-21, before any DR1 data (§I). Row IV was given its scoring rule on 2026-09-23, made exact on 2026-09-24, also before any DR1 data: it is scored against the ceiling Boylan-Kolchin (2023) derives, on the first Euclid measurement that meets its rules, from DR1-Foundation or a later release. The JWST measurements examined in §IV lie inside that ceiling.

---

## :lock: Pre-Registration

| Field | Value |
|---|---|
| First deposited | 2026-06-05 |
| Reference | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20563047.svg)](https://doi.org/10.5281/zenodo.20563047) |
| Expected Euclid DR1 release | DR1-Foundation: November 2026. Full DR1: mid 2027. ESA states that data release dates are tentative and will have to be confirmed. *(Schedule field updated 2026-07-18 from ESA's published timeline; on 2026-06-05 it read October 2026.)* |
| Data products in scope | Cosmology release: spectroscopic BAO (<i>z</i> = 0.9–1.8), photometric weak lensing, high-<i>z</i> stellar mass function. Quick-look products are not bound by this card. |

**How the card is scored.**

- Each row is scored against the latest version of this card deposited on Zenodo before the first data capable of scoring that row appear.
- Post-DR1 results enter via the Winner(s) row of the Scoreboard and the per-observable DR1 outcome lines on a clearly dated later commit. Earlier content is not edited at that time.
- Contender predictions cite either a published canonical source or the best-fit posterior from the most recent public data release of that framework. Where a contender is silent on an observable, the cell reads "no prediction" and that silence counts as data.
- The card adjudicates the five rows independently. A single falsification falsifies that row; the framework as a whole stands or falls on the collective pattern.

*Clarification added 2026-07-18.* **The three data products named in scope no longer arrive together.** ESA has split DR1, its stated reason being that additional time is needed to process and validate the higher-level science products across this survey area. The high-<i>z</i> stellar mass function rides the photometric source catalogue and spectra in DR1-Foundation (November 2026); spectroscopic BAO and photometric weak lensing are higher-level products held for the full DR1 (mid 2027). The scope of the card is unchanged: the same three product classes bind it, delivered in two releases rather than one. This means two dated scoring commits rather than one, the first covering Row IV after DR1-Foundation and the second covering Rows I, II, III and V after the full release. Earlier content is not edited at either point. *For Row IV this schedule is superseded by its scoring rule of 2026-09-23 (§IV): that row scores on the first measurement that qualifies, from DR1-Foundation or later.*

---

## :crystal_ball: Prediction Summary

| # | Observable | MIT prediction | Euclid DR1 channel | Falsifies MIT if |
|---|---|---|---|---|
| I | $`\Lambda`$ epoch-independence | $`\Lambda_\text{obs} = 3/R^2`$ is topologically fixed; $`\Omega_\text{DE}(z)`$ flat across all DR1 redshift bins | Spectroscopic BAO across four $`z`$ bins + photometric weak lensing (3×2pt); $`\Omega_\text{DE}(z)`$ reconstruction and CPL fit | Reconstructed $`\Omega_\text{DE}(z)`$ varies at $`\geq 2\sigma`$ across DR1 bins in a model-independent (binned or non-parametric) reconstruction |
| II | $`a_0(z)`$ evolution | $`a_0(z) = a_0(0) \cdot H(z)/H_0`$; $`a_0(z{=}1.5) \approx 2.4\times`$ local | Galaxy-galaxy weak lensing stellar-mass-halo-mass relation; photometric/spectroscopic galaxy samples for high-<i>z</i> scaling relations | Euclid DR1 galaxy-galaxy lensing and stellar-mass-halo-mass scaling show no enhancement consistent with the predicted $`a_0(z)`$ evolution, while external $`z \approx 1`$–1.5 kinematic follow-up rules out the predicted $`a_0(z)`$ evolution at $`\geq 2\sigma`$, with $`a_0(z{=}1.5)`$ consistent with the constant $`a_0(0)`$ |
| III | $`w_\text{eff}(z)`$ trajectory | $`w_\text{eff}(z) > -1`$ at all $`z`$ (fiducial split, proven) | Spectroscopic BAO ($`z = 0.9`$–1.8, four bins) combined with photometric weak lensing; CPL parameter posterior | Fiducial split gives $`w_\text{eff}(z) < -1`$ at $`\geq 2\sigma`$ |
| IV | Stellar mass function at $`z \gtrsim 10`$ | JWST-style massive galaxies persist in Euclid wide-area statistics; reachable with $`\varepsilon_\text{SF} \lesssim 1`$ under $`a_0(z{=}10) \approx 20.5\times`$ | Wide-area photometric source catalog with high-<i>z</i> selection; NISP/ancillary spectroscopic confirmation where available | Abundance of $`M_{*} \sim 10^{10}\ M_\odot`$ galaxies at $`z > 10`$ falls within Boylan-Kolchin (2023) ΛCDM SMF forecast at $`\geq 2\sigma`$ |
| V | $`(1+z)^1`$ coefficient in $`H^2(z)`$ | Negative, magnitude $`\lvert\beta\rvert < 0.012`$ tied to $`s_0`$ | Spectroscopic BAO precision across $`z = 0.9`$–1.8 (forecast 1–2% per bin); coefficient extracted from the $`H^2(z)`$ form | Coefficient positive at $`\geq 2\sigma`$, or magnitude inconsistent with fitted $`s_0`$ |

*Clarification added 2026-06-26.* **Rows II, III, and V are correlated channels, not independent bets.** All three read the same phase-clock relation: $`a_0(z)`$ through $`H(z)`$, and $`w_\text{eff}(z)`$ plus the $`(1+z)^1`$ coefficient through the same $`H^2(z; s_0)`$ background form. A DR1 outcome in one row therefore informs the interpretation of the others. Passing II, III, and V together would confirm one underlying relation through three observational channels, not three independent framework successes. The rows are still adjudicated separately, and their collective pattern is what carries the evidence. See [dark energy](dark-energy.md) and [early galaxies](early-galaxies.md).

---

## I. $`\Lambda`$ Epoch-Independence

This is the framework's deepest claim. $`\Lambda`$ is not a free parameter fit to the cosmological redshift–distance data; its spectral seed is the first positive eigenvalue of the Möbius surface embedded in $`S^3`$, $`\lambda_1 = 2/R^2`$, lifted by the Gauss equation to $`6/R^2`$ and then normalized by the imported de Sitter vacuum relation to the reference coefficient $`\Lambda_\text{ref} = 3/R^2`$. The topology fixes the seed, not the imported $`\tfrac{1}{2}`$, and whether that reference coefficient is the physical constant of a static domain is open (see [cosmological constant](cosmological-constant.md) §IV); the numerical value additionally needs the curvature radius $`R`$ (the open R problem, see [cosmological constant](cosmological-constant.md)), so the 122-order Planck agreement ($`\Lambda_\text{obs} \cdot \ell_P^2 \approx 2.90 \times 10^{-122}`$) is a surface-sector consistency check read back from $`\Lambda_\text{obs}`$, not an independent value prediction. What Euclid DR1 adjudicates is whether $`\Lambda`$ stays constant across cosmic time, or whether the dark-energy density evolves.

*Dataset-convention note added 2026-09-01.* **The $`2.90 \times 10^{-122}`$ benchmark above is the Planck 2018 +BAO combination this card carried when first deposited**. The live framework now names TT,TE,EE+lowE+lensing as its Λ-anchored default, giving $`\Lambda\,\ell_P^2 = 2.845 \times 10^{-122}`$ ([Inputs and Calibration](../../framework/README.md#inputs-and-calibration)). The figure is left as first deposited, and Row I's prediction cell carries no numeric value in any case. The same applies to notation: the prose above now writes the computed $`3/R^2`$ as $`\Lambda_\text{ref}`$, matching the live framework, while three cells keep the earlier form: Row I's Prediction Summary cell, the MIT row of the contender table in this section, and the Scoreboard. Those also carry "is topologically fixed", which the prose above states more precisely, and $`\Lambda_\text{obs}`$ elsewhere in this section means the observed value $`R`$ was back-read from, which is the point of that sentence.

| Framework | Prediction | Source |
|---|---|---|
| **MIT** | $`\Lambda_\text{obs}`$ is topologically fixed; $`\Omega_\text{DE}(z)`$ is flat at every DR1 redshift bin | [cosmological-constant](cosmological-constant.md), [first-eigenvalue](../../framework/files/bedrock/files/first-eigenvalue.md) |
| **ΛCDM** | $`\Lambda`$ constant by construction | Standard Friedmann cosmology |
| **w<sub>0</sub>w<sub>a</sub>CDM** | DESI DR2 best fit: $`(w_0, w_a) = (-0.42 \pm 0.21,\; -1.75 \pm 0.58)`$ (BAO+CMB), implying time-varying dark energy density; $`\Omega_\text{DE}(z)`$ not flat | DESI DR2 BAO+CMB combined fit |
| **EDE** | Early dark energy component active near $`z \sim 3000`$; at low $`z`$, $`\Omega_\text{DE}(z)`$ approximately flat | Poulin, Smith, Karwal class |
| **MOND / RelMOND** | No prediction | Standard MOND has no cosmology |

> 🎯 *Outcome to be recorded after the full DR1 release, mid 2027. This row reads spectroscopic BAO and the weak-lensing 3×2pt combination, higher-level products the November 2026 DR1-Foundation release does not carry.*

*Added 2026-09-21, before any Euclid DR1 data.* **Row I's scoring rule.** The row as first written left one choice open, how matter is treated in the reconstruction, and this entry supplies it. DR1 adjudicates Row I under this rule, and its result will be reported as the outcome of a test set on 2026-09-21.

**Why the row as first written does not determine a result.** A reconstruction of $`\Omega_\text{DE}(z)`$, the dark-energy density in the sense the w<sub>0</sub>w<sub>a</sub>CDM cell above uses it ("time-varying dark energy density; $`\Omega_\text{DE}(z)`$ not flat"), first subtracts a matter term from $`E^2(z) = A(1+z)^3 - \beta(1+z) + \Omega_\Lambda`$, with $`A = \Omega_m/(1-s_0^2)`$ and $`\beta = \Omega_m s_0^2/(1-s_0^2)`$. For $`s_0 > 0`$ no constant matter coefficient leaves an exactly flat residual, because a $`(1+z)^1`$ term cannot be absorbed into a $`(1+z)^3`$ one, so different treatments draw different histories from the same $`H(z)`$. Holding matter at the fiducial fraction, the split Row III names, leaves a residual that rises toward the past by $`\beta[(1+z)^3 - (1+z)]`$: relative to today, 1.3% at $`z = 0.9`$ and 5.1% at $`z = 1.8`$ at the SN+BAO posterior median $`s_0 = 0.076`$, and 8.5% and 33.0% at the 95% bound $`s_0 = 0.19`$. Subtracting the dressed matter term $`A(1+z)^3`$ leaves $`-\beta(1+z)`$ ([dark energy](dark-energy.md) §III).

**The registered rule.** Row I is scored on two binned reconstructions in the DR1 BAO bins, one holding matter at the fiducial fraction and one fitting it with the bins, and it fails if either varies at $`\geq 2\sigma`$ across the bins. Other reconstructions are reported alongside and do not score. With two looks, the chance that noise alone fails the row is higher than for a single 2σ test, up to twice as high. The card gives the row no deferral provision.

**Row I as a joint test.** "Flat" means flat to within 2σ at Euclid's precision, and the framework's own background predicts a rise in the fiducial arm. Row I can therefore fail on an evolving vacuum term, and it can also fail on the framework's own phase if $`s_0`$ sits near the upper end of its allowed range. It reads the same $`H^2(z; s_0)`$ background as Rows II, III and V, so the accounting of the 2026-06-26 note extends to it: passing Rows I, II, III and V together would confirm one relation through four channels, not four independent successes.

---

## II. $`a_0(z)`$ Evolution

MIT predicts $`a_0`$ scales with $`H(z)`$; standard MOND predicts $`a_0`$ is universal and constant; ΛCDM has no acceleration scale at all. This is the sharpest three-way split on the card. The $`z = 10`$ extrapolation ($`\approx 20.5\times`$ local) is for JWST and ELT; Euclid DR1's contribution comes through galaxy-galaxy weak lensing and the stellar-mass-halo-mass relation at $`z \approx 1`$–1.5.

| Framework | Prediction | Source |
|---|---|---|
| **MIT** | $`a_0(z) = a_0(0) \cdot H(z)/H_0`$; $`a_0(z{=}2) \approx 3\times`$ local, $`a_0(z{=}10) \approx 20.5\times`$ | [early-galaxies](early-galaxies.md) |
| **ΛCDM** | No acceleration scale; rotation curves explained by dark matter halos of mass-dependent profile | Navarro-Frenk-White, standard structure formation |
| **w<sub>0</sub>w<sub>a</sub>CDM** | No acceleration scale | Same as ΛCDM |
| **EDE** | No acceleration scale | Same as ΛCDM |
| **MOND / RelMOND** | a<sub>0</sub> = const ≈ 1.2 × 10<sup>−10</sup> m/s² at all <i>z</i> | Milgrom (1983); AeST in cosmological regime |

> ⚠️ *Euclid DR1 galaxy-galaxy lensing constrains the stellar-mass-halo-mass relation but does not directly measure $`a_0(z)`$. If DR1 lensing data lack the sensitivity to distinguish the predicted enhancement from standard halo-mass scatter, this row is deferred to DR2 and external kinematic follow-up and is not counted in the row-by-row tally.*

> 🎯 *Outcome to be recorded after the full DR1 release, mid 2027. Galaxy-galaxy weak lensing is a higher-level product held for the full release.*

*Note added 2026-07-18.*

**The row II lensing channel is conditional on a relativistic completion the framework has not supplied.** The framework gives a Newtonian-equivalent dynamical prediction, not a lensing law: outside general relativity the potential that deflects photons need not track the one governing dynamics, which is why relativistic completions were developed for MOND itself. A DR1 lensing result therefore bears on $`a_0(z)`$ only under a completion in which the lensing potential inherits the $`E(z)`$ scaling.

Because the lensing conjunct carries no derived expectation, an apparent DR1 enhancement arising from noise or an unrelated systematic would leave the falsification condition unmet even where the kinematic conjunct is satisfied.

The sensitivity provision above therefore applies, for a different cause: an absent theoretical connection rather than insufficient data. Absent a completion, the row defers to DR2 and external kinematic follow-up and is not counted in the tally. This note changes no cell.

**[Update 1 (June 2026): MUSE-DARK III](early-galaxies-update1.md)** 

The first robust intermediate-redshift measurement of the acceleration scale arrived after this prediction was deposited. MUSE-DARK III (Ciocan et al., *A&A* 709) fits $`a_0`$ in four redshift bins from 79 galaxies in the MUSE Hubble Ultra Deep Field and finds it rising with redshift at ~30σ over 0.33 < z < 1.44, the predicted direction, against the standard-MOND constant.

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/muse_dark_iii_a0z_three_line.png/:/rs=w:1280,h:835" width="100%" alt="The framework curve a0(0)E(z) against the two MUSE-DARK III linear fits: the MOND-frame fit sits on the framework curve through the measured window, the dark-matter DC14 fit runs steeper, and both linear fits dip toward 1.0 at z=0 against the SPARC anchor at 1.20.">

> The framework's convex $`a_0(0)\,E(z)`$ against the two MUSE-DARK III fits. In the MOND frame the data sit on the curve; in the better-fitting dark-matter frame they run steeper. Both linear fits dip toward 1.0 at $`z = 0`$ against the SPARC anchor at 1.20, the convex curve forced to a straight line. The frames disagree, so the rate is open.

**Direction: corroborated, not yet a discriminator.** The framework's $`a_0 \propto H(z)`$ form was deposited before this robust result, and the climb came in on the right side. But the same direction was already measured weakly at low redshift before the deposit (Vărăşteanu et al. 2025), and a rising $`a_0`$ also follows from other evolving-acceleration models and from ΛCDM simulations, so the climb alone does not single out the framework.

**Rate: decomposition-dependent.** How fast $`a_0`$ climbs depends on how the rotation curve is split. In the MOND frame the data sit on the framework's $`a_0(0)\,E(z)`$ curve; in the better-fitting dark-matter frame they run steeper than $`H(z)`$. Other surveys bracket the framework from both sides, so the rate is open and systematics-limited, not settled.

**Normalization: open.** The anchor $`a_0(0) = 1.2`$ is fixed by SPARC and echoed by the locked ratio; the comparison is limited by the tens-of-percent cross-calibration between MUSE and SPARC and by the redshift-dependent gas the model omits, not by the framework.

**Universality: the ground test is uninformative on its own terms.** The per-galaxy test of whether a single $`a_0`$ holds across mass is now runnable on the public data, and it proves structurally inapplicable: the fitted dark-matter fractions stay flat with mass, which turns any apparent $`a_0`$ trend into a surface-density artifact degenerate with a fitting prior. What the question needs is a measurement free of the stellar mass-to-light scale, which stacked lensing would supply mass- and aperture-independently, on the condition recorded in the note above. Absent that completion, the near-term weight sits on matched-systematics kinematics.

This sits alongside the companion paper's standing 2.9σ trend-shape tension with the Übler KMOS3D Tully–Fisher data: the intermediate-redshift record is direction confirmed, details contested, clean test pending.

---

## III. $`w_\text{eff}(z)`$ Trajectory

The full Euclid DR1 release, mid 2027, will deliver spectroscopic BAO in four redshift bins between <i>z</i> = 0.9 and 1.8, combined with photometric weak lensing; the November 2026 DR1-Foundation release carries no cosmology-derived products. The headline cosmology result will be reported in the w<sub>0</sub>w<sub>a</sub>CDM (CPL) parameterization. This row carries a single core claim: the underlying $`H(z)`$ introduces no independent phantom fluid. The Waltz-clock distance-redshift relation satisfies $`w_\text{eff}(z) > -1`$ for all $`z \geq 0`$ in the fiducial-matter split (proven analytically). Restricted two-parameter bases (CPL, BA, JBP) can nevertheless manufacture an apparent crossing from that relation; MIT treats template projection as a candidate explanation of such crossings, not as an established explanation of the DESI signal. The specific location of such an artifact depends on the template basis, the dataset, and the covariance structure; MIT does not predict a crossing redshift, since on this reading the crossing is not physical.

*Clarification added 2026-09-02.* **The scope of this row's claims.** The companion analysis scopes $`w_\text{eff}(z) > -1`$ to the fiducial matter split and notes that a different valid split reads $`w_\text{eff} < -1`$ at high $`z`$, so there is no decomposition-independent statement about $`w(z)`$ to make; the decomposition-independent claim is that the underlying $`H(z)`$ introduces no independent phantom fluid, as the prose above states. The same analysis states that its template exercise establishes the mechanism rather than showing DESI's signal to be primarily template bias, so the prose treats template projection as a candidate explanation, matching the callout below. **This leaves the same asymmetry the 2026-09-01 note records for $`\Lambda`$.** The Scoreboard's "$`w > -1`$ at all $`z`$; any apparent crossing is template artifact" is the card's only unscoped statement of either claim, as Row I's cell is its only untyped $`\Lambda`$.

| Framework | Prediction | Source |
|---|---|---|
| **MIT** | $`w_\text{eff}(z) > -1`$ at all $`z`$ in the fiducial-matter split; no real crossing | [dark-energy](dark-energy.md) §III (proof) |
| **ΛCDM** | $`w(z) = -1`$ exactly, no crossing possible | Standard Friedmann cosmology |
| **w<sub>0</sub>w<sub>a</sub>CDM** | Parameterization permits crossing; DESI DR2 best fit $`(w_0, w_a) \approx (-0.4,\; -1.8)`$ implies a crossing near <i>z</i> ≈ 0.4–0.5 | DESI DR2 BAO+CMB combined fit |
| **EDE** | $`w(z) \approx -1`$ at Euclid DR1 redshifts; the EDE component is active near $`z \sim 3000`$ | Poulin, Smith, Karwal class |
| **MOND / RelMOND** | No prediction | Standard MOND has no cosmology; AeST does not constrain $`w(z)`$ at this precision |

> ⚠️ **If a crossing is detected.** *MIT's position is that any CPL crossing is a template-projection artifact of a non-phantom truth; the framework does not predict a specific crossing redshift. The diagnostic is reconstruction-basis dependence: crossings that appear in two-parameter bases (CPL, BA, JBP) but vanish in non-parametric reconstructions are template artifacts; a crossing that persists across reconstruction methods would constitute evidence against that interpretation.*
>
> *Other contenders: ΛCDM predicts no crossing. w<sub>0</sub>w<sub>a</sub>CDM best fit puts the crossing near <i>z</i> ≈ 0.4–0.5. EDE and MOND give no late-time crossing.*

> 🎯 *Outcome to be recorded after the full DR1 release, mid 2027. The BAO and weak-lensing inputs, and the CPL posterior read off them, are higher-level products held for the full release.*

---

## IV. Stellar Mass Function at $`z \gtrsim 10`$

Euclid's wide-area photometric survey will dramatically extend the JWST-discovered population of high-redshift massive galaxies, replacing small-area surprise with cosmologically significant statistics. The question this row asks is whether the abundance of $`M_{*} \sim 10^{10}\ M_\odot`$ galaxies at $`z \gtrsim 10`$ is what standard structure formation expects or what JWST already suggests it is not. MIT and EDE both predict enhanced high-redshift abundance relative to ΛCDM, by different mechanisms (epoch-dependent $`a_0`$ vs. shifted matter-radiation equality). This row discriminates MIT from ΛCDM and w<sub>0</sub>w<sub>a</sub>CDM; the MIT-vs-EDE tiebreaker is Row II ($`a_0(z)`$ evolution).

| Framework | Prediction | Source |
|---|---|---|
| **MIT** | Wide-area statistics confirm JWST-class abundance; reachable under standard $`\varepsilon_\text{SF} \lesssim 1`$ with $`a_0(z{=}10) \approx 20.5\times`$ local | [early-galaxies](early-galaxies.md) |
| **ΛCDM** | Stellar mass function at $`z \gtrsim 10`$ within standard halo-abundance forecasts; the JWST tension is anomalous and resolves with better selection / dust corrections | Boylan-Kolchin (2023) SMF forecast; standard structure formation |
| **w<sub>0</sub>w<sub>a</sub>CDM** | Same as ΛCDM (dark energy modifications do not change early structure growth) | Standard structure formation |
| **EDE** | Enhanced early structure from shifted matter-radiation equality; consistent with JWST UV luminosity functions at $`z \sim 4`$–16 with moderate $`\varepsilon_\text{SF}`$; quantitative SMF at $`z > 10`$ TBD | Klypin et al. (2021); Shen, Vogelsberger, Boylan-Kolchin (2024) |
| **MOND / RelMOND** | Enhanced gravity at low accelerations qualitatively eases early structure formation; no clean quantitative mass-function prediction available | Sanders, McGaugh review |

> ⚠️ *Euclid DR1 wide-area photometry at z > 10 may yield a catalog too sparse or selection-dominated to distinguish the MIT and ΛCDM mass-function forecasts at the stated threshold. If DR1 uncertainties or selection systematics are too large to determine whether the abundance of M<sub>*</sub> ~ 10<sup>10</sup> M<sub>☉</sub> galaxies at z > 10 lies above or within the Boylan-Kolchin (2023) ΛCDM forecast at the stated 2σ threshold, this row is deferred to DR2 / JWST cross-calibration and is not counted in the row-by-row tally.*

> 🎯 *Outcome to be recorded after DR1-Foundation, November 2026. The wide-area photometric source catalogue and the spectra ship at that stage, which puts this row roughly half a year ahead of the other four.* *(Superseded on 2026-09-23 by the rule below: the outcome is recorded when the first qualifying measurement appears, at the Foundation stage or later.)*

*Added 2026-09-23, before any Euclid DR1 data; the power rule made exact on 2026-09-24.* **Row IV's scoring rule.** The row as first written left open what its comparison is, which statistic and which measurement score, how its 2σ is computed, and when it scores. This entry fixes them. Its scope does not change: the row reads Euclid-based wide-area measurements, as its cells say, from DR1 or a later release; quick-look products stay outside the card, as its scope field says.

**What the comparison is.** The cells call [Boylan-Kolchin (2023)](https://doi.org/10.1038/s41550-023-01937-7) a ΛCDM stellar-mass-function forecast, and it is not one. The paper bounds the abundance of galaxies above a stellar mass $`M_*`$ by the halo mass function, taking every baryon in every halo massive enough to host them to have become stars: $`n(>M_*) \leq n_\text{halo}(>M_*/f_b)`$ and $`\rho_*(>M_*) \leq f_b\,\rho_m(>M_*/f_b)`$, with $`f_b = 0.156`$. These are ceilings at full conversion efficiency, with no central value and no error band of their own. They hold at any redshift, and the paper draws them from $`z = 5`$ to 20, but it states numbers only for its candidates at $`z \approx 7.5`$ and 9.1. The numbers Row IV needs are computed here by the paper's method, the Planck 2018 parameters it quotes and the [Sheth and Tormen (1999)](https://doi.org/10.1046/j.1365-8711.1999.02692.x) mass function, and registered: for $`M_* \geq 10^{10}\,M_\odot`$ at $`z = 10`$, $`n_\text{ceil} = 10^{-4.57}\ \text{Mpc}^{-3}`$ and $`\rho_\text{ceil} = 10^{5.60}\,M_\odot\ \text{Mpc}^{-3}`$, falling to $`10^{-5.85}`$ and $`10^{4.29}`$ at $`z = 12`$. A measured abundance averages over its redshift window, so the row compares it with the ceiling averaged over the same window, weighted by comoving volume; over $`10 < z < 11`$ that average is $`10^{-4.84}`$ and $`10^{5.33}`$. The computation reproduces the paper's stated numbers on both statistics: for its $`z \approx 9.1`$ candidate, peak heights to within 0.15 and halo number densities to within 0.3 dex; for the stellar-mass densities of its two most massive candidates, taken from the paper's own data, the conversion efficiencies they imply, 0.99 at $`z \approx 9.1`$ and 0.84 at $`z \approx 7.5`$, and 0.57 at the lower 1σ edge, to within 0.05. Both err toward the higher ceiling ([bk23_ceiling.py](../../framework/files/working/files/scripts/euclid-row-iv/bk23_ceiling.py)).

**The registered rule.**

- The threshold keeps June's words, read literally against the ceiling: the row fails if the abundance falls within the ceiling at ≥ 2σ, that is, if the one-sided 2σ upper bound of the measured abundance lies below the ceiling. It is scored on both statistics above $`M_* = 10^{10}\,M_\odot`$, the cumulative number density and the cumulative stellar-mass density, and it fails if either one falls within its ceiling that way, as Row I fails on either reconstruction. The 2σ is per statistic. With two correlated looks, the chance that noise alone fails the row is higher than for a single 2σ test, up to twice as high.
- The window is the measurement's own redshift bin above $`z = 10`$; if it reports several, the row reads the lowest one whose lower edge is at or above $`z = 10`$. Each ceiling is averaged over that bin, weighted by comoving volume, as the measured abundance is.
- Stellar masses are taken as the measurement reports them on a [Chabrier (2003)](https://doi.org/10.1086/376392) initial mass function, or through the measurement's own stated conversion to it. A measurement that supplies neither does not qualify, and no conversion is chosen at scoring time.
- The 2σ bound is the measurement's own. It must publish the cumulative number and stellar-mass densities with their joint uncertainty (Poisson counts, sample variance, stellar-mass and redshift posteriors, completeness and contamination), or release enough to reproduce that uncertainty uniquely; no way of combining them is chosen at scoring time. Where the measurement states a range for a completeness or contamination correction, the end that lowers the abundance is used.
- The Sheth and Tormen mass function stays. The paper notes that it over-predicts massive halos by 20 to 50% at the redshifts it studies, $`z \approx 7`$ to 10; keeping the same form above $`z = 10`$ keeps the ceiling generous.
- A statistic is powered when, by the measurement's own published uncertainty, an abundance at half its ceiling would register as a 2σ deficit. For a count, that uncertainty takes its Poisson part at the expected count of a population at half the ceiling, over the measurement's own volume and completeness, never at the count observed, and its other components as the measurement publishes them, so whether a measurement qualifies does not depend on the outcome it is about to score. A measurement qualifies only if at least one statistic is powered. A qualifying measurement fails the row if either statistic falls within its ceiling as above, powered or not, and passes it only if both statistics are powered and neither does; with one powered and neither within its ceiling, it does not score, and the next qualifying version does. Weak data cannot pass the row.

**What the rule tests.** The ΛCDM cell and this section's opening speak of what standard structure formation expects; the source that cell and the threshold name bounds the abundance instead, and the MIT cell makes its claim against that bound. It cites [early-galaxies](early-galaxies.md), which in its last version before the card was first deposited ([bf6bcfa](https://github.com/dmobius3/mode-identity-theory/blob/bf6bcfa90a8937ae5115134e9eb8194b4eca5550/files/cosmos/files/early-galaxies.md), 2026-05-29) described the JWST masses near $`z \approx 10`$ as ones that "approach or exceed the maximal baryon abundance permitted in standard dark matter halos under ΛCDM" and added: "Under standard assumptions (constant $`a_0`$, ΛCDM collapse timescales), the implied star formation efficiency $`\varepsilon_\text{SF}`$ exceeds unity". The cell's "reachable with $`\varepsilon_\text{SF} \lesssim 1`$" is a claim only against that ceiling. The ΛCDM cell predicts the opposite, that the tension "resolves with better selection / dust corrections". The literal threshold scores that contrast: an abundance at or above the ceiling within 2σ is the population the MIT cell names, and passes; an abundance clearly inside it is the outcome the ΛCDM cell predicts, and fails. A failure would record that ΛCDM reaches the measured abundance below full efficiency. It would not record that massive galaxies are absent above $`z = 10`$.

**Other readings.** Failing the row unless the abundance clears the ceiling by 2σ would fail it even if the galaxies turned up as MIT's cell predicts. The paper places the most extreme JWST densities at $`z \approx 9`$ at the ceiling, not above it, and galaxies persisting at that level would fail a must-clear test. The same holds for taking the ceiling at the lower edge of the window, where it is largest: over $`10 < z < 12`$ a population at the ceiling at every redshift would measure 0.46 dex below that value, and any measurement precise enough to qualify would fail it. It holds too for failing the row whenever any qualifying measurement fails: with no limit on how many analyses appear, noise alone would in time fail a true claim, so the first qualifying version scores instead. Until a version scores, each qualifying version that does not score is another look at the fail condition. June's words are read against the ceiling, which sits well above a realistic-efficiency forecast.

**Which measurement scores, and when.** The row is scored by the earliest public version of a measurement that itself satisfies every rule above, whenever it appears: on DR1-Foundation data, the full DR1, DR2, or through JWST cross-calibration of Euclid samples as the June provision names. Its date is that version's posting, on arXiv or in a journal; if two qualifying versions appear on the same day, the one covering the larger comoving volume scores. That version's reported values and uncertainties are the ones scored. A formal erratum to it replaces its values, and a retraction voids the score and passes the row to the next version to qualify; ordinary revised estimates in later versions change nothing. Later measurements are reported beside the score and do not change it, so once a version has scored, the number of analyses published adds no looks. Each candidate's qualification is recorded in a dated commit when it appears, naming the clause it meets or fails, and a disqualification that rests only on the clause about reproducing the uncertainty is marked as such. Each scoring commit records whether a qualifying version has appeared; until one has, the row is deferred under its June provision. Whether DR1-Foundation supplies one is not predicted here. The Q1 photometric-redshift pipeline reported redshifts from 0 to 6, extended to 10 only for sources seen in the near-infrared alone, and its authors plan improvements to that configuration for DR1 ([Euclid Collaboration: Tucci et al. 2025](https://arxiv.org/abs/2503.15306)); a Euclid Collaboration study finds that Euclid imaging can detect galaxies to $`z = 13`$, with Spitzer data helping to recover those beyond $`z = 10`$ ([Euclid Collaboration: Allen et al. 2025](https://arxiv.org/abs/2511.02926)). Euclid's reddest band, NISP $`H_\text{E}`$, cuts off at 2021.4 nm ([Euclid Collaboration: Schirmer et al. 2022](https://doi.org/10.1051/0004-6361/202142897)), rest-frame 1840 Å at $`z = 10`$, so a stellar mass from Euclid photometry alone rests on the rest-frame ultraviolet, and that uncertainty enters the power rule above.

**The existing evidence.** No measurement in the row's scope exists yet, but its question has been looked at with JWST, and each measurement examined here lies inside the ceiling averaged over its own window ([bk23_ceiling.py](../../framework/files/working/files/scripts/euclid-row-iv/bk23_ceiling.py), context section). [Casey et al. (2024)](https://doi.org/10.3847/1538-4357/ad2075), in the first 0.28 deg² of JWST's COSMOS-Web survey, report candidates at $`10 \lesssim z \lesssim 14`$ with volume densities of about $`10^{-6}\ \text{Mpc}^{-3}`$ for $`M_* \sim 10^{10}\,M_\odot`$, some 0.7 dex inside the ceiling, and their most massive candidates imply a conversion efficiency of 0.2 to 0.5. [Shuntov et al. (2025)](https://doi.org/10.1051/0004-6361/202452570), over the whole survey, select 27 candidates at $`10 < z < 12`$, and their published mass function at those redshifts ([data](https://doi.org/10.5281/zenodo.14712538)) has no occupied bin above $`10^{10}\,M_\odot`$; at 2σ that null count lies 1.06 dex inside the ceiling for a complete sample and stays inside it down to 9% completeness, and the authors, who call the measurement tentative and likely incomplete, find no tension with ΛCDM's limits. [Harvey et al. (2025)](https://doi.org/10.3847/1538-4357/ad8c29), over 187 arcmin² of deep fields, find no galaxy above $`10^{10}\,M_\odot`$ at $`9.5 < z < 11.5`$, a null count inside the ceiling unless their sample is less than 34% complete. None of these is Row IV's score: they come from JWST fields, the largest about half a square degree, and the row asks whether such galaxies persist in Euclid's wide-area statistics. Row IV remains unscored because no qualifying Euclid wide-area measurement exists yet. Scoring COSMOS-Web or PRIMER would be a separate test, registered after those data, with no claim on this one.

---

## V. $`(1+z)^1`$ Coefficient in $`H^2(z)`$

This is the distinctive signature row. The phase-clock $`H^2(z)`$ form contains a $`(1+z)^1`$ term that is absent from every canonical FLRW component (radiation, matter, curvature, $`\Lambda`$). The coefficient is strictly negative for $`s_0 > 0`$ and tied to the fitted phase parameter. No other model on this card predicts this term at all.

| Framework | Prediction | Source |
|---|---|---|
| **MIT** | Negative coefficient $`-\beta`$ with $`\lvert\beta\rvert < 0.012`$ at 95% CL from current data; magnitude tied to $`s_0`$ | [dark-energy](dark-energy.md) §II, §VI |
| **ΛCDM** | Exactly zero (Friedmann has no $`(1+z)^1`$ component) | Standard Friedmann cosmology |
| **w<sub>0</sub>w<sub>a</sub>CDM** | Approximately zero; CPL has no isolated linear-in-<i>z</i> coefficient in $`H^2`$ | Linder (2003) parameterization |
| **EDE** | Approximately zero at Euclid DR1 redshifts | Poulin et al. class |
| **MOND / RelMOND** | No prediction | Same as above |

> ⚠️ *DR1 BAO precision (forecast 1–2% per bin) is marginal for direct detection of this term at the current $`s_0`$ bound; a null result here is consistent with the MIT prediction and a stronger DR2 test.* **A null DR1 result on this row is not counted in the row-by-row tally.**

> 🎯 *Outcome to be recorded after the full DR1 release, mid 2027. The coefficient is extracted from spectroscopic BAO precision, a higher-level product held for the full release.*

*Cosmographic-translation note added 2026-09-03.* **The same term has a standard cosmographic face.** For $`E^2(z) = A(1+z)^3 - \beta(1+z) + \Omega_\Lambda`$ the present jerk is $`j_0 = 1 + \beta`$, so this row's negative $`(1+z)^1`$ coefficient is the statement $`j_0 > 1`$, against $`j_0 = 1`$ exactly for ΛCDM. It is a translation for the cosmography literature, not a second test and not a second bet: the row's own bound $`\lvert\beta\rvert < 0.012`$ puts $`\lvert j_0 - 1\rvert`$ far inside the uncertainty of current $`j_0`$ determinations, which is of order unity. Nothing is scored on it.

---

## :musical_score: Scoreboard

|  | Λ | a₀(z) | w(z) | SMF z ≳ 10 | (1+z)¹ in H² |
|---|---|---|---|---|---|
| **MIT** | $`\Lambda = 3/R^2`$, fixed by topology | $`a_0 \propto H(z)`$; ≈ 3× at $`z = 2`$ | $`w > -1`$ at all $`z`$; any apparent crossing is template artifact | abundance matches JWST under $`a_0(z{=}10) \approx 20.5\times`$ | negative; \|β\| < 0.012 tied to $`s_0`$ |
| **ΛCDM** | fixed by construction | no $`a_0`$ | $`w = -1`$ exact | predicted SMF below JWST (tension) | coefficient = 0 (term absent from Friedmann) |
| **w<sub>0</sub>w<sub>a</sub>CDM** | $`\Omega_\text{DE}(z)`$ varies | no $`a_0`$ | crossing near $`z`$ ≈ 0.4–0.5 | same tension as ΛCDM | no tied standalone (1+z)¹ coefficient |
| **EDE** | fixed at low $`z`$, EDE component at $`z \sim 3000`$ | no $`a_0`$ | $`w \approx -1`$ at DR1 $`z`$ | consistent with JWST UVLFs; quantitative SMF at $`z > 10`$ TBD | coefficient ≈ 0 at DR1 $`z`$ |
| **MOND** | no prediction | $`a_0`$ fixed ≈ 1.2 × 10<sup>−10</sup> m/s² | no prediction | enhanced gravity qualitatively helps; no quantitative SMF | no prediction |
| 🎯 **DR1 outcome** |  |  |  |  |  |
| 🏆 **Winner(s)** |  |  |  |  |  |

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
