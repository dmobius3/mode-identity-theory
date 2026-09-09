<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🔮 Euclid DR1 Showdown

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/dr1%20banner.png?raw=true" width="100%" alt="Euclid DR1">

The Euclid Data Release 1 arrives in two stages. DR1-Foundation, in November 2026, carries the raw data and calibrated images, catalogues and spectra over about 1900 deg², with no cosmology-derived products. The full DR1, in mid 2027, adds the higher-level science products for galaxy clustering and weak lensing. ESA states that these dates are tentative and will have to be confirmed. Five Mode Identity Theory predictions are locked here, before the data, against four named contenders: flat ΛCDM, w<sub>0</sub>w<sub>a</sub>CDM (CPL), early dark energy (EDE), and MOND / relativistic MOND. Each row is a head-to-head with a stated falsification threshold for MIT. Only Row IV, the high-<i>z</i> stellar mass function, is reachable at the Foundation stage; the other four read cosmology-derived products and wait for the full release. Results will be added in later commits as each stage lands.

---

## :lock: Pre-Registration

| Field | Value |
|---|---|
| Freeze date | 2026-06-05 |
| Reference | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20563048.svg)](https://doi.org/10.5281/zenodo.20563048) |
| Expected Euclid DR1 release | DR1-Foundation: November 2026. Full DR1: mid 2027. ESA states that data release dates are tentative and will have to be confirmed. *(Schedule field updated 2026-07-18 from ESA's published timeline; at freeze it read October 2026.)* |
| Data products in scope | Cosmology release: spectroscopic BAO (<i>z</i> = 0.9–1.8), photometric weak lensing, high-<i>z</i> stellar mass function. Quick-look products are not bound by this card. |

**Ground rules.**

1. MIT prediction cells, contender prediction cells, and falsification thresholds are immutable after the tagged release. Any edit voids the pre-registration for that row.
2. Post-DR1 results enter via the Winner(s) row of the Scoreboard and the per-observable DR1 outcome lines on a clearly dated later commit. Earlier content is not edited at that time.
3. Contender predictions cite either a published canonical source or the best-fit posterior from the most recent public data release of that framework. Where a contender is silent on an observable, the cell reads "no prediction" and that silence counts as data.
4. The card adjudicates the five rows independently. A single falsification falsifies that row; the framework as a whole stands or falls on the collective pattern.

*Clarification added 2026-07-18, post-freeze; no prediction cell, contender cell, or falsification threshold is edited.* **The three data products named in scope no longer arrive together.** ESA has split DR1, its stated reason being that additional time is needed to process and validate the higher-level science products across this survey area. The high-<i>z</i> stellar mass function rides the photometric source catalogue and spectra in DR1-Foundation (November 2026); spectroscopic BAO and photometric weak lensing are higher-level products held for the full DR1 (mid 2027). The scope of the card is unchanged: the same three product classes bind it, delivered in two releases rather than one. Under ground rule #2 this means two dated scoring commits rather than one, the first covering Row IV after DR1-Foundation and the second covering Rows I, II, III and V after the full release. Earlier content is not edited at either point.

---

## :crystal_ball: Prediction Summary

| # | Observable | MIT prediction | Euclid DR1 channel | Falsifies MIT if |
|---|---|---|---|---|
| I | $`\Lambda`$ epoch-independence | $`\Lambda_\text{obs} = 3/R^2`$ is topologically fixed; $`\Omega_\text{DE}(z)`$ flat across all DR1 redshift bins | Spectroscopic BAO across four $`z`$ bins + photometric weak lensing (3×2pt); $`\Omega_\text{DE}(z)`$ reconstruction and CPL fit | Reconstructed $`\Omega_\text{DE}(z)`$ varies at $`\geq 2\sigma`$ across DR1 bins in a model-independent (binned or non-parametric) reconstruction |
| II | $`a_0(z)`$ evolution | $`a_0(z) = a_0(0) \cdot H(z)/H_0`$; $`a_0(z{=}1.5) \approx 2.4\times`$ local | Galaxy-galaxy weak lensing stellar-mass-halo-mass relation; photometric/spectroscopic galaxy samples for high-<i>z</i> scaling relations | Euclid DR1 galaxy-galaxy lensing and stellar-mass-halo-mass scaling show no enhancement consistent with the predicted $`a_0(z)`$ evolution, while external $`z \approx 1`$–1.5 kinematic follow-up rules out the predicted $`a_0(z)`$ evolution at $`\geq 2\sigma`$, with $`a_0(z{=}1.5)`$ consistent with the constant $`a_0(0)`$ |
| III | $`w_\text{eff}(z)`$ trajectory | $`w_\text{eff}(z) > -1`$ at all $`z`$ (fiducial split, proven) | Spectroscopic BAO ($`z = 0.9`$–1.8, four bins) combined with photometric weak lensing; CPL parameter posterior | Fiducial split gives $`w_\text{eff}(z) < -1`$ at $`\geq 2\sigma`$ |
| IV | Stellar mass function at $`z \gtrsim 10`$ | JWST-style massive galaxies persist in Euclid wide-area statistics; reachable with $`\varepsilon_\text{SF} \lesssim 1`$ under $`a_0(z{=}10) \approx 20.5\times`$ | Wide-area photometric source catalog with high-<i>z</i> selection; NISP/ancillary spectroscopic confirmation where available | Abundance of $`M_{*} \sim 10^{10}\ M_\odot`$ galaxies at $`z > 10`$ falls within Boylan-Kolchin (2023) ΛCDM SMF forecast at $`\geq 2\sigma`$ |
| V | $`(1+z)^1`$ coefficient in $`H^2(z)`$ | Negative, magnitude $`\lvert\beta\rvert < 0.012`$ tied to $`s_0`$ | Spectroscopic BAO precision across $`z = 0.9`$–1.8 (forecast 1–2% per bin); coefficient extracted from the $`H^2(z)`$ form | Coefficient positive at $`\geq 2\sigma`$, or magnitude inconsistent with fitted $`s_0`$ |

*Clarification added 2026-06-26, post-freeze; no prediction, threshold, or scoring rule is changed.* **Rows II, III, and V are correlated channels, not independent bets.** All three read the same phase-clock relation: $`a_0(z)`$ through $`H(z)`$, and $`w_\text{eff}(z)`$ plus the $`(1+z)^1`$ coefficient through the same $`H^2(z; s_0)`$ background form. A DR1 outcome in one row therefore informs the interpretation of the others. Passing II, III, and V together would confirm one underlying relation through three observational channels, not three independent framework successes. Ground rule #4 still holds: the rows are adjudicated separately, and their collective pattern is what carries the evidence. See [dark energy](dark-energy.md) and [early galaxies](early-galaxies.md).

---

## I. $`\Lambda`$ Epoch-Independence

This is the framework's deepest claim. $`\Lambda`$ is not a free parameter fit to the cosmological redshift–distance data; its spectral seed is the first positive eigenvalue of the Möbius surface embedded in $`S^3`$, $`\lambda_1 = 2/R^2`$, lifted by the Gauss equation to $`6/R^2`$ and then normalized by the imported de Sitter vacuum relation to the reference coefficient $`\Lambda_\text{ref} = 3/R^2`$. The topology fixes the seed, not the imported $`\tfrac{1}{2}`$, and whether that reference coefficient is the physical constant of a static domain is open (see [cosmological constant](cosmological-constant.md) §IV); the numerical value additionally needs the curvature radius $`R`$ (the open R problem, see [cosmological constant](cosmological-constant.md)), so the 122-order Planck agreement ($`\Lambda_\text{obs} \cdot \ell_P^2 \approx 2.90 \times 10^{-122}`$) is a surface-sector consistency check read back from $`\Lambda_\text{obs}`$, not an independent value prediction. What Euclid DR1 adjudicates is whether $`\Lambda`$ stays constant across cosmic time, or whether the dark-energy density evolves.

*Dataset-convention note added 2026-09-01, post-freeze; no prediction cell, contender cell, or falsification threshold is edited.* **The $`2.90 \times 10^{-122}`$ benchmark above is the Planck 2018 +BAO combination this card carried at freeze**. The live framework now names TT,TE,EE+lowE+lensing as its Λ-anchored default, giving $`\Lambda\,\ell_P^2 = 2.845 \times 10^{-122}`$ ([Inputs and Calibration](../../framework/README.md#inputs-and-calibration)). The frozen figure is left as deposited; this clarification changes no prediction, threshold, or scoring rule, and Row I's prediction cell carries no numeric value in any case. The same applies to notation: the prose above now writes the computed $`3/R^2`$ as $`\Lambda_\text{ref}`$, matching the live framework, while three immutable cells keep the deposited form: Row I's Prediction Summary cell, the MIT row of the contender table in this section, and the Scoreboard. Those also carry "is topologically fixed", which the prose above now states more precisely; they are prediction cells under ground rule #1 and cannot be edited, which is why the correction lives in the prose rather than in them. The split is permanent by design, and $`\Lambda_\text{obs}`$ elsewhere in this section means the observed value $`R`$ was back-read from, which is the point of that sentence.**

| Framework | Prediction | Source |
|---|---|---|
| **MIT** | $`\Lambda_\text{obs}`$ is topologically fixed; $`\Omega_\text{DE}(z)`$ is flat at every DR1 redshift bin | [cosmological-constant](cosmological-constant.md), [first-eigenvalue](../../framework/files/bedrock/files/first-eigenvalue.md) |
| **ΛCDM** | $`\Lambda`$ constant by construction | Standard Friedmann cosmology |
| **w<sub>0</sub>w<sub>a</sub>CDM** | DESI DR2 best fit: $`(w_0, w_a) = (-0.42 \pm 0.21,\; -1.75 \pm 0.58)`$ (BAO+CMB), implying time-varying dark energy density; $`\Omega_\text{DE}(z)`$ not flat | DESI DR2 BAO+CMB combined fit |
| **EDE** | Early dark energy component active near $`z \sim 3000`$; at low $`z`$, $`\Omega_\text{DE}(z)`$ approximately flat | Poulin, Smith, Karwal class |
| **MOND / RelMOND** | No prediction | Standard MOND has no cosmology |

> 🎯 *Outcome to be recorded after the full DR1 release, mid 2027. This row reads spectroscopic BAO and the weak-lensing 3×2pt combination, higher-level products the November 2026 DR1-Foundation release does not carry.*

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

*Note added 2026-07-18, post-freeze. No prediction cell and no falsification threshold is edited. This note invokes the row's existing deferral provision under a cause that provision was not written for, and states the stretch rather than leaving it implicit.*

**The row II lensing channel is conditional on a relativistic completion the framework has not supplied.** The framework gives a Newtonian-equivalent dynamical prediction, not a lensing law: outside general relativity the potential that deflects photons need not track the one governing dynamics, which is why relativistic completions were developed for MOND itself. A DR1 lensing result therefore bears on $`a_0(z)`$ only under a completion in which the lensing potential inherits the $`E(z)`$ scaling.

The adverse direction is worth stating plainly. Because the lensing conjunct carries no derived expectation, an apparent DR1 enhancement arising from noise or an unrelated systematic would leave the falsification condition unmet even where the kinematic conjunct is satisfied, shielding this row from a falsification the channel that does the work had already delivered.

The remedy is the one the sensitivity provision above specifies, applied to a different cause: not insufficient data, but an absent theoretical connection. Absent a completion, the row defers to DR2 and external kinematic follow-up and is not counted in the tally. The deposited cells stand as written.

**[Update 1 (June 2026): MUSE-DARK III](early-galaxies-update1.md)** 

The first robust intermediate-redshift measurement of the acceleration scale arrived after this prediction was deposited. MUSE-DARK III (Ciocan et al., *A&A* 709) fits $`a_0`$ in four redshift bins from 79 galaxies in the MUSE Hubble Ultra Deep Field and finds it rising with redshift at ~30σ over 0.33 < z < 1.44, the predicted direction, against the standard-MOND constant.

<img src="https://img1.wsimg.com/isteam/ip/21cc2ac0-6dc4-4b19-93ef-6a7079ac9d3c/muse_dark_iii_a0z_three_line.png/:/rs=w:1280,h:835" width="100%" alt="The framework curve a0(0)E(z) against the two MUSE-DARK III linear fits: the MOND-frame fit sits on the framework curve through the measured window, the dark-matter DC14 fit runs steeper, and both linear fits dip toward 1.0 at z=0 against the SPARC anchor at 1.20.">

> The framework's convex $`a_0(0)\,E(z)`$ against the two MUSE-DARK III fits. In the MOND frame the data sit on the curve; in the better-fitting dark-matter frame they run steeper. Both linear fits dip toward 1.0 at $`z = 0`$ against the SPARC anchor at 1.20, the convex curve forced to a straight line. The frames disagree, so the rate is open.

**Direction: corroborated, not yet a discriminator.** The framework's $`a_0 \propto H(z)`$ form was deposited before this robust result, and the climb came in on the right side. But the same direction was already measured weakly at low redshift before the deposit (Vărăşteanu et al. 2025), and a rising $`a_0`$ also follows from other evolving-acceleration models and from ΛCDM simulations, so the climb alone does not single out the framework.

**Rate: decomposition-dependent.** How fast $`a_0`$ climbs depends on how the rotation curve is split. In the MOND frame the data sit on the framework's $`a_0(0)\,E(z)`$ curve; in the better-fitting dark-matter frame they run steeper than $`H(z)`$. Other surveys bracket the framework from both sides, so the rate is open and systematics-limited, not settled.

**Normalization: open.** The anchor $`a_0(0) = 1.2`$ is fixed by SPARC and echoed by the locked ratio; the comparison is limited by the tens-of-percent cross-calibration between MUSE and SPARC and by the redshift-dependent gas the model omits, not by the framework.

**Universality: the ground test is uninformative on its own terms.** The per-galaxy test of whether a single $`a_0`$ holds across mass is now runnable on the public data, and it proves structurally inapplicable: the fitted dark-matter fractions stay flat with mass, which turns any apparent $`a_0`$ trend into a surface-density artifact degenerate with a fitting prior. What the question needs is a measurement free of the stellar mass-to-light scale, which stacked lensing would supply mass- and aperture-independently, on the condition recorded in the note above. Absent that completion, the near-term weight sits on matched-systematics kinematics.

This sits alongside the companion paper's standing 2.9σ trend-shape tension with the Übler KMOS3D Tully–Fisher data: the honest intermediate-redshift record is direction confirmed, details contested, clean test pending.

---

## III. $`w_\text{eff}(z)`$ Trajectory

The full Euclid DR1 release, mid 2027, will deliver spectroscopic BAO in four redshift bins between <i>z</i> = 0.9 and 1.8, combined with photometric weak lensing; the November 2026 DR1-Foundation release carries no cosmology-derived products. The headline cosmology result will be reported in the w<sub>0</sub>w<sub>a</sub>CDM (CPL) parameterization. This row carries a single core claim: the underlying $`H(z)`$ introduces no independent phantom fluid. The Waltz-clock distance-redshift relation satisfies $`w_\text{eff}(z) > -1`$ for all $`z \geq 0`$ in the fiducial-matter split (proven analytically). Restricted two-parameter bases (CPL, BA, JBP) can nevertheless manufacture an apparent crossing from that relation; MIT treats template projection as a candidate explanation of such crossings, not as an established explanation of the DESI signal. The specific location of such an artifact depends on the template basis, the dataset, and the covariance structure; MIT does not predict a crossing redshift, since on this reading the crossing is not physical.

*Clarification added 2026-09-02, post-freeze; no prediction cell, contender cell, Scoreboard cell, or falsification threshold is edited.* **The prose above stated this row's core claim unscoped, then scoped it in the next sentence.** The companion analysis scopes $`w_\text{eff}(z) > -1`$ to the fiducial matter split and notes that a different valid split reads $`w_\text{eff} < -1`$ at high $`z`$, so there is no decomposition-independent statement about $`w(z)`$ to make; the decomposition-independent claim is that the underlying $`H(z)`$ introduces no independent phantom fluid, and the prose now says that. The same analysis states that its template exercise establishes the mechanism rather than showing DESI's signal to be primarily template bias, so the prose now treats template projection as a candidate explanation, matching the callout below rather than overrunning it. **This leaves the same asymmetry the 2026-09-01 note records for $`\Lambda`$.** The Scoreboard's "$`w > -1`$ at all $`z`$; any apparent crossing is template artifact" is now the card's only unscoped statement of either claim, as Row I's cell is its only untyped $`\Lambda`$, and it stays for the same reason: a pre-registration is worth what it committed to, not what it would commit to now.

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

> 🎯 *Outcome to be recorded after DR1-Foundation, November 2026. The wide-area photometric source catalogue and the spectra ship at that stage, which puts this row roughly half a year ahead of the other four.*

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

*Cosmographic-translation note added 2026-09-03, post-freeze; no prediction cell, contender cell, or falsification threshold is edited.* **The same term has a standard cosmographic face.** For $`E^2(z) = A(1+z)^3 - \beta(1+z) + \Omega_\Lambda`$ the present jerk is $`j_0 = 1 + \beta`$, so this row's negative $`(1+z)^1`$ coefficient is the statement $`j_0 > 1`$, against $`j_0 = 1`$ exactly for ΛCDM. It is a translation for the cosmography literature, not a second test and not a second bet: the row's own bound $`\lvert\beta\rvert < 0.012`$ puts $`\lvert j_0 - 1\rvert`$ far inside the uncertainty of current $`j_0`$ determinations, which is of order unity. Nothing is scored on it.

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
