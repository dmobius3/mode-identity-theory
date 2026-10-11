<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Nonflat Distance Comparison

**Type:** Test
**State:** Closed
**Verdict:** Negative
**Status (2026-10-11):** Run once from the tag. Verdict Negative: A (6.13 Gpc) EXCLUDED, C (10.5 Gpc) DISFAVORED and B (19.7 Gpc) NOT EXCLUDED, each the same in both scale rows. The data's own region is $`\Omega_0 R \ge 15.2`$ Gpc at the anchor's $`H_0`$ (14.0 at SH0ES's), and closure is not preferred.
**Summary:** The SN+BAO comparison the stress-tensor bridge owes a closed effective metric: the fitted D+Λ rate with the closed transverse distance $`D_M = R\sin(\chi/R)`$, scored against Pantheon+ and DESI DR2 BAO at the radius readings on record.
**Inputs:** `propagation-theorem.md`, `r-problem.md`, `claim-ledger.md`, `r-from-mass-spectrum.md`, `molien-step-two.md`, `temporal-budget.md`, `redshift-and-cooling.md`, the Λcos Model D+Λ pipeline
**Parent:** `stress-tensor-bridge.md`
**Frozen:** 2026-10-11 this contract, its gate table and tolerances, the forecast and the pins (frozen before any run)

REGISTRATION, frozen 2026-10-11 before any run. This page registers the comparison [the stress-tensor bridge](stress-tensor-bridge.md)'s §VI asks for: "accepting a closed effective metric would require the SN+BAO comparison rerun with the nonflat distance relation". It tests the closed alternative that [the propagation theorem](propagation-theorem.md) derives for one case, not the framework's adopted flat dictionary. The instrument runs in the Λcos pipeline, from the tag `closed-distance-v1.0`. This page holds the registration, the adjudication and the record (ruled 2026-10-10). The run happens once, and its results land in one Λcos results commit and in this page's Results.

**Related:** [The Propagation Theorem](propagation-theorem.md) (where the closed case comes from), [The Stress-Tensor Bridge](stress-tensor-bridge.md) §VI (where the comparison is owed), [The R Problem](r-problem.md) (the readings), [Temporal Budget](temporal-budget.md) §III (the rate), [The Clock-Asymmetry Fit](clock-asymmetry-fit.md) (the split between MIT and Λcos that this follows).

---

## 0. What the test assumes

The closed relation is an alternative under test, not the framework's cosmology. The framework adopts flat effective slices, "a commitment, not a derivation" ([the bridge](stress-tensor-bridge.md) §VI). The test scores what follows from five declarations.

1. **The case.** The declared carrier of light and standard rulers lies in the class of [the propagation theorem](propagation-theorem.md), and the effective metric is required to metricize its cone with the domain's symmetry. Under these declarations the theorem gives closed, round slices (§V).
2. **The representative.** $`g_\text{eff} = \Omega(t)^2\,[-c(t)\,dt^2 + h]`$, with $`h`$ the round metric of radius $`R`$ (the theorem's §III), and its conformal factor proportional to the realization amplitude, $`\Omega \propto S`$.
   - Its scale factor is then the bridge's frozen import $`a_\text{eff} = a_\ast S`$ (§VI).
   - Under the rate of item 4, its clock is the dressed one of §VI's Λ-clock question, not the frozen $`dt/d\tau = S^{-1/2}`$.
   - $`1 + z = \Omega_0/\Omega(t_\text{emit}) = S(t_\text{obs})/S(t_\text{emit})`$, the phase ratio of [Redshift and Cooling](redshift-and-cooling.md) §I.
3. **The identification (ruled 2026-10-10).** $`\Omega_0 = 1`$, declared as the primary diagnostic identification, not derived: the effective slice's curvature radius today equals the static $`R`$. Fixing $`\Omega`$ needs a declared standard (the theorem's §III). Another $`\Omega_0`$ only changes the radius the data see, since $`D_M = \Omega_0 R\sin\big((c\int dz/H)/(\Omega_0 R)\big)`$. So the data constrain $`\Omega_0 R`$, and cannot separate $`\Omega_0`$ from $`R`$.
4. **The rate.** $`H(z)`$ is the fitted D+Λ dictionary's ([Temporal Budget](temporal-budget.md) §III), unchanged, with no curvature term. With one, the test would score a different model: nonflat ΛCDM puts $`\Omega_k(1+z)^2`$ into $`E^2`$.
5. **Images.** Each image inherits the cover's transverse factor (the theorem's §III), so the relation holds image by image, beyond the injectivity radius $`\pi R/10`$ too.

The model, with $`\Omega_\Lambda = 0.685`$ fixed as the dictionary fixes it:

```math
E^2(z) = \frac{1-\Omega_\Lambda}{1-s_0^2}\left[(1+z)^3 - s_0^2(1+z)\right] + \Omega_\Lambda, \qquad I(z) = \int_0^z \frac{dz'}{E(z')}, \qquad \zeta = \frac{R H_0}{c},
```

```math
D_M = \frac{c}{H_0}\,\zeta\,\sin\frac{I(z)}{\zeta}, \qquad D_H = \frac{c}{H_0\,E(z)}, \qquad D_V = \left(z\,D_M^2\,D_H\right)^{1/3}, \qquad D_L = (1+z)\,D_M.
```

The closed factor replaces the transverse distance wherever it appears: in $`D_L`$ for the supernovae, and in $`D_M`$ and $`D_V`$ for BAO. $`D_H`$ is unchanged. The flat limit $`\zeta \to \infty`$ is the published Λcos model.

## 1. The question

Under the declarations of §0, do Pantheon+ and DESI DR2 BAO allow the closed effective metric at the radius readings on record? And what lower bound do they put on today's effective curvature radius, $`\Omega_0 R`$? The pre-freeze expectation (§8) is that the coupling-route radius fails decisively, the muon-top radius falls between the bars, and the electron-muon radius is out of reach.

## 2. Frozen inputs

**The readings.** Each is scored under its own label, with no scan.

| reading | $`R`$ | route | as pinned by | role |
|---|---|---|---|---|
| A | 6.13 Gpc | coupling | [the Claim Ledger](claim-ledger.md) | sets the Verdict |
| B | 19.7 Gpc | mass, electron-muon | [The Molien Shells, Step Two](molien-step-two.md) | its own label |
| C | 10.5 Gpc | mass, muon-top | the Claim Ledger | its own label |

[The R Problem](r-problem.md) rounds A to 6.1 and calls its route best-conditioned. Step two derived B from the route's executed $`\Lambda_\text{ref} \approx 8.1 \times 10^{-54}`$ m⁻² through $`\Lambda_\text{ref} = 3/R^2`$, and the route pages round it to 20. The mass route's precision is an order of magnitude, and the mass sector gives no single $`R`$ ([R from the Particle Mass Spectrum](r-from-mass-spectrum.md)). So B and C fix values rather than claim them, and neither replaces A.

**The scale (ruled 2026-10-10).** Each reading converts to $`\zeta = RH_0/c`$, with $`c = 299\,792.458`$ km/s, in two rows run on identical data, profiling and bars.

| reading | $`\zeta`$, primary row ($`H_0 = 67.36`$) | $`\zeta`$, robustness row ($`H_0 = 73.04`$) |
|---|---|---|
| A | 1.3773 | 1.4935 |
| C | 2.3592 | 2.5582 |
| B | 4.4264 | 4.7996 |

- **The primary row** is [the engine](../../../README.md)'s named anchor (Three readings of one hierarchy), a flat base-ΛCDM CMB inference.
- **The robustness row** is the SH0ES value, an alternative calibration, not a term in the likelihood. Its Hubble-flow supernovae lie at $`0.0233 < z < 0.15`$ (its §5), where the closed correction to distances is under 0.2% even at A. So this row does not presuppose the flatness under test.

**The files,** pinned by SHA-256.
- The first five come from the Λcos repo at `975bda0`.
- The last two sit in the candidate commit. [`forecast_registered.py`](scripts/nonflat-distance-comparison/forecast_registered.py), pinned in the table, generated both once, on 20 001 points, independently of the instrument: the synthetic sets in the published magnitude convention, and the forecast of §8. Their bytes repeat run to run.

| file | contents | SHA-256 |
|---|---|---|
| `data/pantheon_plus.csv` | Pantheon+, 1701 SNe Ia (`zHD`, `m_b_corr`) | `46a9334d15f7115435f662038692061a06fa36ba87e61e85bc17f5ac86c439a8` |
| `data/pantheon_plus_cov.npy` | its covariance | `5c1b855c02e6a96ca8aa651e5e645af2db3b5f15f0c3647ca93c10ca27f8197e` |
| `data/desi_dr2_bao.csv` | DESI DR2 BAO, 13 points: one $`D_V/r_d`$, and six pairs of $`D_M/r_d`$ and $`D_H/r_d`$ | `c746badffdef7f5e6b475d075f55a4de12173e991c94cb3a00eb498b9b5c254a` |
| `data/desi_dr2_bao_cov.npy` | its covariance | `4d6ce177d7e96fb63199af88c2688a926dbb166acd61dc9f75dc0da7b4825c03` |
| `results/lcos_summary.json` | the published flat best fit: $`\chi^2 = 1772.565`$ at $`s_0 = 0.001`$, $`H_0 r_d = 10025.4`$ km/s, $`M_B = -19.354`$ | `b234fd104fedce1f333ec9b058448694ed945ea8ff1f86cdb11ef488fc2ac2bd` |
| `data/closed_distance_synthetic.json` | one flat set, equal to the published fit's predictions; and the closed model at each reading's $`\zeta`$ in both rows, at $`s_0 = 0.001`$ and $`0.1`$ | `80c4f32c43accefa2992abfdea72dc5030ac8df53d6fa74ff16389583b12c68d` |
| `data/closed_distance_forecast.json` | §8's forecast, which G3 checks against | `2e16bd4f9a92232e8b0e82f1151408d2a29a3aaa05ace4adcd43ff8235a9e5ef` |
| `forecast_registered.py` | the generator of the two files above, in this page's packet | `e29babf71f378c1c6177aaf951eaa5fe3b1d409a54f368bd0ba42de63f563b6b` |

**The parameters.** $`s_0`$ on $`[0.001, 0.99]`$, $`H_0 r_d`$ on $`[8000, 12000]`$ km/s and $`M_B`$ on $`[-20, -18]`$: the box of `fit_lcos.py`, with its strict bounds closed as a numerical convention. They are profiled, not sampled.
- $`M_B`$ enters as an additive offset, and $`c/(H_0 r_d)`$ as a multiplicative amplitude. Both are profiled analytically, with the fitted parameters clipped to the box.
- $`s_0`$ is profiled on a fixed grid, 0.001, then 0.01 to 0.98 in steps of 0.01, then 0.99. It is refined to $`10^{-6}`$ by bounded minimization between the best grid point's neighbors.

**The numerics** are `fit_lcos.py`'s own:
- $`E`$ on 4000 points from $`z = 0`$ to 2.5;
- $`I`$ by the cumulative trapezoid, with linear interpolation to the data's redshifts;
- the supernova modulus as it writes it, $`5\log_{10}[(1+z)(c/70)\,\zeta\sin(I/\zeta)] + 25`$, with $`H_0 = 70`$ absorbed by $`M_B`$.

**The code** is `scripts/fit_lcos_closed.py` in the Λcos repo, at candidate commit `32d9d1a449f4b3d53b7fa316ae3a3f239be4f163` on the branch `closed-distance`. It is written in that repo's own terms: a closed transverse distance at a fixed radius, with $`H(z)`$ unchanged.
- Its SHA-256 is `627e2620453c451eebfa9b8d2e5512243c49897b1c67c279e2c42b8a14b3e341`.
- The environment is Λcos's own, recorded at the freeze (Python 3.9.6, numpy 2.0.2, scipy 1.13.1, pandas 2.3.3). Checking it is the script's first act.

## 3. Qualification and the gates

**Qualification, before the freeze,** runs on the candidate instrument in this order:
1. Measure the floors, and set each tolerance above its floor.
2. Check the environment, then run G1 to G5, R and G6a at those tolerances, in order, so that a failure has one location.
3. Run every arm, after its parent passes, at the same tolerances.

Until the tag, the measured data are evaluated only in the flat limit (G1 and G2). Every closed evaluation is on the fixed synthetic sets. Qualification set the tolerances below; the record under the table gives each one's measured floor.

| gate | passes when | tolerance | arm that must turn it red |
|---|---|---|---|
| G1, parity | the published code agrees with the new script's flat limit (below) | $`10^{-9}`$ relative | $`\Omega_\Lambda = 0.686`$ in the new script; separately, $`D_V`$'s exponent set to 1/2 |
| G2, the published fit | the flat profile on the measured data reproduces `lcos_summary.json` | $`\chi^2`$ and its parts 0.01; $`s_0^2`$, $`10^{-5}`$ from the published value; $`H_0 r_d`$ 1 km/s; $`M_B`$ $`10^{-3}`$ | the $`D_V`$ point dropped, leaving a working 12-point likelihood |
| G3, flat | on the flat set, the profile is minimized at $`u = 0`$, and each reading's $`\Delta\chi^2`$ matches §8 | no grid point lower by $`10^{-6}`$; 0.5% | a closed signal at $`\zeta = 3`$ in a copy of the flat set |
| G4, closed | on the twelve closed sets, the refined minimum recovers $`\zeta`$ and $`s_0^2`$, with $`\chi^2`$ near zero | $`\zeta`$, $`10^{-4}`$ relative; $`s_0^2`$, $`10^{-5}`$; $`\chi^2`$, $`10^{-6}`$ | $`\sin`$ replaced by $`\sinh`$; separately, $`\Omega_k(1+z)^2`$ added to $`E^2`$ |
| G5, floor | G3's and G4's outputs barely move with the instrument on 20 001 points | 0.01 in $`\Delta\chi^2`$; $`10^{-3}`$ relative in $`\zeta`$; $`10^{-5}`$ in $`s_0^2`$ | the instrument's grid cut to 400 points |
| R, rehearsal | the run's analysis, on the flat set, gives §8's grades and bound and no preference; on the C@67.36 closed set, it recovers $`\zeta`$ inside its region and prefers closure | bound, $`10^{-3}`$ relative to §8; $`\zeta`$, $`10^{-4}`$ relative | the region's level moved to 3.84 |
| G6a, pins before the freeze | the files and the executed span match their SHA-256, the script's SHA-256 is recorded, and the candidate commit is clean | exact | one byte changed in a data file's copy |
| G6b, pins after the freeze | the tag `closed-distance-v1.0` resolves to the checkout, and G6a's pins hold; the registration, fetched afresh, sits on MIT main at its commit, has its SHA-256, and names the candidate commit, the script's SHA-256 and the tag | exact | a tag on another commit; a registration off main; a wrong registration hash; a registration naming another commit |

**The qualification record** (2026-10-11, candidate `32d9d1a`), [`qualification.json`](scripts/nonflat-distance-comparison/qualification.json). Three repairs came before it (Record and errata). The environment check passed, every gate passed, and every arm turned its gate red after its parent passed. G6b, probed on temporary local tags and throwaway registrations, passed its parent and failed all four arms. Each provisional tolerance sat at least ten times above its measured floor and was kept:

| gate | quantity | measured floor | tolerance |
|---|---|---|---|
| G1 | worst relative deviation from the published code | 4.7 × 10⁻¹⁵ relative | 10⁻⁹ relative |
| G2 | $`\chi^2`$, worst of the total and its parts | 8.9 × 10⁻⁸ | 10⁻² |
| G2 | $`s_0^2`$ | 10⁻¹³ | 10⁻⁵ |
| G2 | $`H_0 r_d`$ | 7.2 × 10⁻³ km/s | 1 km/s |
| G2 | $`M_B`$ | 5.3 × 10⁻⁷ | 10⁻³ |
| G3 | $`\chi^2`$ of the flat set at $`u = 0`$; no grid point lies below it | 9.3 × 10⁻⁸ | 10⁻⁶ |
| G3 | worst relative difference from §8's forecast | 3.8 × 10⁻⁵ relative | 5 × 10⁻³ relative |
| G4 | worst $`\zeta`$ error | 6.6 × 10⁻⁶ relative | 10⁻⁴ relative |
| G4 | worst $`s_0^2`$ error | 9.8 × 10⁻⁷ | 10⁻⁵ |
| G4 | largest $`\chi^2`$ at the refined minimum | 9.4 × 10⁻⁸ | 10⁻⁶ |
| G5 | largest move in $`\Delta\chi^2`$ | 4.5 × 10⁻⁴ | 10⁻² |
| G5 | largest move in $`\zeta`$ | 6.6 × 10⁻⁶ relative | 10⁻³ relative |
| G5 | largest move in $`s_0^2`$ | 9.8 × 10⁻⁷ | 10⁻⁵ |
| R | the flat set's bound against §8's | 1.8 × 10⁻⁶ relative | 10⁻³ relative |
| R | the C@67.36 closed set's recovered $`\zeta`$ | 1.8 × 10⁻⁶ relative | 10⁻⁴ relative |

**G1 in detail.**
- **What runs.** Execute `fit_lcos.py` from its first line to the line before its MCMC marker (L1 to L101 at `975bda0`), with `sys.argv` pinned to the script's name, so that $`\Omega_\Lambda = 0.685`$, and with its own directory as the working directory.
- **The pin.** The span's SHA-256, over those lines as UTF-8 text each ending in a newline, is `75d1089fb20328245a1ea1122b3844ac834af0e8e2d1f6cfa35b48870c788e5d`.
- **The comparison,** against the new script's flat limit:
  - $`E`$ on the grid, at $`s_0 \in \{0.001, 0.05, 0.1, 0.2, 0.4\}`$;
  - `sn_chi2` on those values of $`s_0`$ by $`M_B \in \{-19.40, -19.354, -19.30\}`$;
  - `bao_chi2` on those values of $`s_0`$ by $`H_0 r_d \in \{9900, 10025.43, 10150\}`$;
  - each of the 13 BAO predictions at the same points, read out of the published `bao_chi2` by setting its namespace's data vector to zero and its inverse covariance to each unit projector in turn.
- **The sign.** Each readout is the prediction squared. Its positive square root, a distance, is compared with the new script's signed prediction, so a sign error in the new script fails.

**A gate that fails.**
- **Before the freeze,** the instrument goes back for repair. This page's terms change only through a reviewed version.
- **After the freeze,** a gate that fails ends the run as Uninformative. A repaired instrument returns only through a reviewed version of this page, with a dated erratum, a new candidate commit and script hash, a new versioned tag, and qualification again in full. The frozen scientific terms do not change.

**The run, once, from the tag:**
1. The environment check, G6b, then G1 to G5 again at the frozen tolerances. R runs at qualification only: the analysis it rehearses follows, on the measured data.
2. Each reading's profiled $`\Delta\chi^2`$, in both rows.
3. The free-$`\zeta`$ profile, on $`u = 1/\zeta^2`$ from 0 to 1 in steps of 0.001, with its minimum refined by bounded minimization between the best grid point's neighbors.
4. The region and the bound.
5. The preference.

## 4. Grades and the Verdict

- **The statistic.** $`\Delta\chi^2(R) = \min \chi^2_\text{closed}(\zeta(R)) - \min \chi^2_\text{flat}`$. Both are minimized identically over $`(s_0, H_0 r_d, M_B)`$, with the supernovae and BAO summed.
- **The bars.** These are decision conventions on $`\Delta\chi^2`$, not calibrated significances: flat sits on the boundary of the closed family, and no reference distribution is calibrated here.
  - EXCLUDED: $`\Delta\chi^2 \ge 25`$;
  - DISFAVORED: $`9 \le \Delta\chi^2 < 25`$;
  - NOT EXCLUDED: $`\Delta\chi^2 < 9`$.
- **The rows.** Each reading is graded in each row. Where the two grades differ, the reading is SCALE-DEPENDENT, with both grades recorded and neither row preferred.

**The Verdict** is set by A, as A set it in [step two](molien-step-two.md). B and C carry their own labels beside A's, never in its place.

| A's grade | Verdict |
|---|---|
| EXCLUDED | Negative |
| NOT EXCLUDED | Positive |
| DISFAVORED, or SCALE-DEPENDENT | Inconclusive |
| a gate fails | Uninformative |

**The data's own region** is reported, not graded.
- **The region.** The level is 2.71 above the refined minimum. The region is every $`u`$ where the profile lies below that level. It is reported in full, as intervals in $`u`$, in $`\zeta`$, and in $`\Omega_0 R`$ (in Gpc, in both rows), together with the profile itself.
- **The bound.** $`\zeta_{95}`$ is the region's smallest $`\zeta`$, reported as $`\Omega_0 R_{95} = \zeta_{95}\,c/H_0`$ in both rows. With flat on the boundary $`u = 0`$, it is the nominal one-sided 95% lower bound; its coverage is not calibrated here.
- **Three cases, registered now:**
  - if the region reaches $`u = 1`$, no bound is set within $`\zeta \ge 1`$;
  - if the region has several intervals, all are reported, and $`\zeta_{95}`$ is the smallest $`\zeta`$ among them;
  - if the minimum is interior, lying more than $`10^{-6}`$ below the flat value, its $`u`$ is reported, along with whether flat lies in the region. The region is then nominally a two-sided 90% interval, and only its smallest-$`\zeta`$ end is read as the bound.

**Closure preferred.** If $`\chi^2_\text{flat} - \min_\zeta \chi^2(\zeta) \ge 9`$, these data prefer closure at that level. The value is reported whatever it is.

## 5. Moves that do not count

- Changing any of the following after the freeze, or before it except through a reviewed version of this page:
  - the model, the representative or the identification;
  - $`\Omega_\Lambda`$, the readings or the scale rows;
  - the data, the synthetic sets, the profiling or the numerics;
  - the statistic, a gate, a tolerance, the bars or the region's convention.
- Setting a tolerance other than from a floor measured at qualification.
- Choosing any of the above for its expected outcome.
- Adding a statistic or a sample cut after the fact.
- Evaluating a finite $`\zeta`$ on the measured data before the tag.
- Putting B or C in place of A.
- Settling a disagreement between the rows by preferring one.
- Putting a curvature term into $`H`$.
- Reading $`R`$ off the result, which would make it a distance-derived $`R`$.

## 6. After the run

The result is recorded whatever it is, in one results commit in Λcos and in this page's Results. The Results carry the Verdict and report A, B and C in both rows side by side, each with its $`\Delta\chi^2`$, grade and profiled parameters, along with the free-$`\zeta`$ profile, the region, the bound and the preference.

What each outcome means is fixed now:
- **EXCLUDED at a reading.** At that radius, with $`\Omega_0 = 1`$, SN+BAO exclude the closed effective metric the theorem gives.
  - A metric effective description then needs one of four routes: a carrier outside the class; a representative that gives up the domain's symmetry on an open patch; giving up the metricization; or a scale standard other than $`\Omega_0 = 1`$, which the bound limits.
  - The flat dictionary is untouched, and the reading itself is not tested; it was an input.
- **DISFAVORED.** A tension at that radius, recorded; no route is forced.
- **NOT EXCLUDED.** This meets the bridge's §VI condition at that radius. It is necessary, not sufficient: branch (b) still owes the derived map $`g_\text{static} \to g_\text{eff}`$ and an independently derived effective source ([the bridge](stress-tensor-bridge.md) §VII).
- **SCALE-DEPENDENT.** Both grades stand, and the reading waits on the scale.
- **Closure preferred.** This counts against the adopted flat slices on these data, and the bridge's §VI records it.

No outcome tests MIT as a whole. None reinstates the earlier CMB argument, which was withdrawn as a coordinate error ([CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §V, [The R Problem](r-problem.md)).

The result lands in three places: the Results here, a dated pointer under the bridge's §VI question on $`k_\text{eff}`$, and the working index. [The R Problem](r-problem.md) is not changed, since the readings are inputs here.

## 7. What the test leaves out

- **The CMB.** With $`\chi_\ast`$ near 14 Gpc, $`\chi_\ast/R`$ runs from about 0.7 to 2.3 across the readings, so the acoustic scale would reach all three. But the fitted $`H(z)`$ has no radiation term, and the acoustic scale needs its own early-universe computation.
- **The z > 0.01 sample.** Below $`z = 0.01`$ the closed correction is under $`10^{-5}`$ at every reading. The cut would still change the calibration and the statistical weighting, so the published all-1701 sample remains primary.
- **Model selection** beyond the statistic of §4, such as information criteria or evidence.

## 8. Expectation and caveats

**What is expected.** This was computed before any closed evaluation on the measured data, by `forecast_registered.py`, which is carried into the frozen packet.
- **Inputs:** the flat synthetic set, with the closed model profiled over $`(s_0, H_0 r_d, M_B)`$ on 20 001 points.
- **What it uses:** the published best fit, and the data's redshifts and covariances. No measured residual vector enters.
- **$`s_0`$:** profiling leaves it at the floor at every reading.

| reading | $`\Delta\chi^2`$ at 67.36 | $`\Delta\chi^2`$ at 73.04 | expected grade |
|---|---|---|---|
| A, 6.13 Gpc | 143.6 | 104.1 | EXCLUDED |
| C, 10.5 Gpc | 16.8 | 12.2 | DISFAVORED |
| B, 19.7 Gpc | 1.36 | 0.98 | NOT EXCLUDED |

**The spread.** In the fixed-template Gaussian approximation, the fluctuation of $`\Delta\chi^2`$ on real data has standard deviation $`2\sqrt{\Delta\chi^2}`$ (8.2 and 7.0 at C). Profiling can change this distribution, so the grade probabilities below are indicative, not calibrated.
- At A and B, the expected grade holds in both rows with probability above 0.99.
- At C, the chances of each grade at the two rows are:
  - EXCLUDED: 0.16 and 0.03;
  - DISFAVORED: 0.67 and 0.64;
  - NOT EXCLUDED: 0.17 and 0.33.

**The bound.** The expected bound is $`\zeta_{95} \approx 3.72`$, so $`\Omega_0 R_{95} \approx 16.6`$ Gpc at 67.36 and 15.3 Gpc at 73.04.

The square roots of these $`\Delta\chi^2`$ are Gaussian-equivalent sensitivities, not calibrated significances.

**Caveats.**
- **Retrospective, not blind.** The data, the published flat fit and this forecast are known before the freeze, which prevents tuning but not prior contact.
- **The primary scale is a flat base-ΛCDM CMB inference.** That is why the second row exists, and why no verdict rests on one row.
- **The rate is the dictionary's by declaration (§0).** A closed effective metric with dynamics of its own could carry a different one.

## 9. The freeze

What remains, in order:

1. Built: the Λcos instrument, on the branch `closed-distance`, at candidate commit `32d9d1a`.
2. Qualified (2026-10-11), in the order of §3; the record is in §3.
3. Both units' final green, and Blake's go (2026-10-11).
4. The freeze (2026-10-11). This page is committed to MIT main, with the tolerances, pinning the Λcos candidate commit and the script's SHA-256. Then the tag `closed-distance-v1.0` is cut on that commit.
5. The run, once, from the tag (§3). Its one results commit records this page's SHA-256 at the freeze, so the candidate commit never changes. Then Λcos main is brought up to it by a merge that keeps its own history, and the record is entered here.

## Results

**Executed 2026-10-11, once,** from the Λcos tag `closed-distance-v1.0` (commit `32d9d1a`), in a clean checkout. The single results commit is `51f7144`, merged into Λcos main as `00ff986`, and the run's whole record is `results/closed_distance/run.json` there.
- The environment check passed.
- G6b passed against this registration: MIT `a9a97c9`, page SHA-256 `7afde5e5dca55f2be6fa55b4ea0c6e14eab5106021fab5b8d0f6a9f5035d91bb`.
- G1 to G5 passed again at the frozen tolerances, with floors identical to qualification.

| reading | $`\Delta\chi^2`$ at 67.36 | grade | $`\Delta\chi^2`$ at 73.04 | grade | the reading's grade |
|---|---|---|---|---|---|
| A, 6.13 Gpc | 135.6 | EXCLUDED | 97.3 | EXCLUDED | EXCLUDED |
| C, 10.5 Gpc | 14.2 | DISFAVORED | 9.93 | DISFAVORED | DISFAVORED |
| B, 19.7 Gpc | 0.62 | NOT EXCLUDED | 0.36 | NOT EXCLUDED | NOT EXCLUDED |

**Verdict: Negative.** A is EXCLUDED in both rows (§4).

**What each grade means, as §6 fixed it:**
- **A, EXCLUDED.** At 6.13 Gpc, with $`\Omega_0 = 1`$, SN+BAO exclude the closed effective metric the theorem gives. A metric effective description at that radius then needs one of four routes: a carrier outside the class; a representative that gives up the domain's symmetry on an open patch; giving up the metricization; or a scale standard other than $`\Omega_0 = 1`$, which the region below limits. The flat dictionary is untouched, and the reading itself was an input, not tested.
- **C, DISFAVORED.** A tension at 10.5 Gpc, recorded; no route is forced. At 73.04 it cleared the bar by 0.93.
- **B, NOT EXCLUDED.** At 19.7 Gpc the closed effective metric meets the bridge's §VI condition. That is necessary, not sufficient: branch (b) still owes the derived map $`g_\text{static} \to g_\text{eff}`$ and an independently derived effective source.

**The data's own region.**
- **The minimum.** The profile's refined minimum lies at $`u = 0.0137`$ ($`\zeta = 8.53`$), 0.098 below the flat value. That is interior by the $`10^{-6}`$ cut, so the region reads as nominally two-sided, and only its smallest-$`\zeta`$ end as the bound.
- **The region.** It is one interval, $`u \le 0.0860`$, with flat inside it: $`\zeta \ge 3.410`$. So $`\Omega_0 R \ge 15.2`$ Gpc at the anchor's $`H_0`$, and $`\ge 14.0`$ Gpc at SH0ES's.
- **Closure is not preferred.** $`\chi^2_\text{flat} - \min_\zeta \chi^2 = 0.098`$, against the bar of 9.

**Against the registered expectation.** All three grades fell as expected.
- **The Δχ² values.** Each sits below its expectation by about a third of the forecast's indicative standard deviation:

  | reading | at 67.36 | at 73.04 |
  |---|---|---|
  | A | 135.6 against 143.6 (spread 24.0) | 97.3 against 104.1 (spread 20.4) |
  | C | 14.2 against 16.8 (spread 8.2) | 9.9 against 12.2 (spread 7.0) |
  | B | 0.62 against 1.36 (spread 2.33) | 0.36 against 0.98 (spread 1.98) |

- **The bound.** It came out at 3.41, looser than the expected 3.72. This is the same small lean toward closure that puts the minimum inside.

## Sources

- D. Brout et al., "The Pantheon+ Analysis: Cosmological Constraints", Astrophys. J. 938, 110 (2022), [doi:10.3847/1538-4357/ac8e04](https://doi.org/10.3847/1538-4357/ac8e04).
- DESI Collaboration, "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints", [arXiv:2503.14738](https://arxiv.org/abs/2503.14738) (2025).
- A. G. Riess et al., "A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team", [arXiv:2112.04510](https://arxiv.org/abs/2112.04510). The Hubble-flow range is from its §5.
- Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", Astron. Astrophys. 641, A6 (2020), [arXiv:1807.06209](https://arxiv.org/abs/1807.06209).

## Record and errata

Before the freeze, 2026-10-11, four qualification runs:
1. **On `1e9ba21`: stopped.** In G4's curvature arm, with the curvature term in the rate, $`E^2`$ turned negative at high $`z`$ for large $`u`$, and the solve received NaNs. `5a92106` gives such a model $`\chi^2 = 10^{30}`$, so the arm fails on its criterion instead of crashing.
2. **On `5a92106`: every gate and all eight arms passed.** Mapping this contract's terms to the code then found three with no code path: the environment check, the region's intervals in $`\zeta`$ and $`\Omega_0 R`$, and any exercise of the run's analysis. `6d4d43c` adds them, the last as gate R.
3. **On `6d4d43c`: every gate and all nine arms passed;** this was the freeze candidate the units reviewed. Unit A found that G6b took the commit and the script's hash from the caller, so a local tag could have opened the measured data with no registration frozen. `32d9d1a` binds G6b to the tag and to the committed registration, with four arms.
4. **On `32d9d1a`: the record** (§3).

No term of this contract changed in any repair. `1e9ba21` also reached Λcos main through `fe8c61c` (pull request #2, merged 2026-10-10) before qualification. Main's copy of the script is not the candidate, and the run is from the tag only. Its guard, present in every version, kept any finite $`\zeta`$ off the measured data.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
