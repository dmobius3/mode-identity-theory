<a id="top"></a>
| **[`<back`](/files/framework/files/working/)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |

---

# The SN-BAO Consistency Test

**Type:** Test
**State:** Closed
**Verdict:** Mixed
**Status (2026-11-18):** Run once from the design commit `e3ef4e5`. Verdict Mixed, as registered: the all row MILD TENSION (graded $`p`$ 0.0166) and the cut row CONSISTENT (0.4127), so the pull is sensitive to including the light curves below $`z = 0.01`$; the rows are nested, and their difference is not itself tested. Under the cut the supernovae alone prefer $`s_0 = 0.239`$.
**Summary:** Whether one common $`s_0`$ in Model D+Λ describes both the Pantheon+ supernovae and DESI DR2 BAO: the parameter goodness-of-fit $`T`$, graded by a sampled approximation to the largest $`p`$ over the BAO data's own confidence set, plus the set's miss probability, on all 1701 light curves and on the 1590 with $`z_\text{HD} > 0.01`$.
**Inputs:** `temporal-budget.md`, `clock-asymmetry-fit.md`, `nonflat-distance-comparison.md`, `dark-energy.md`, the Λcos Model D+Λ pipeline
**Parent:** `temporal-budget.md`
**Frozen:** 2026-11-18 this contract, its gate table and tolerances, the frozen thresholds and the pins (frozen before any run)

REGISTRATION, frozen 2026-11-18 before any run. This page registers the test [the Temporal Budget](temporal-budget.md)'s §X asks for: "Pantheon+ alone accommodates $`s_0 \sim 0.4`$; BAO pulls toward zero. Whether this reflects a real tension (different aspects of the $`H(z)`$ trajectory constraining $`s_0`$ differently) or simply the expected tightening from complementary data needs investigation." The instrument runs in the Λcos pipeline, from the design commit `e3ef4e5` of the branch `sn-bao-consistency`. This page holds the registration and, after the run, its record. The run happens once, and its results land in one Λcos results commit and in this page's Results.

**Related:** [Temporal Budget](temporal-budget.md) §III (the fit) and §X (the question), [The Clock-Asymmetry Fit](clock-asymmetry-fit.md) (the supernovae's pull on $`s_0`$), [The Nonflat Distance Comparison](nonflat-distance-comparison.md) (the pattern this registration follows), [Dark Energy](../../../../cosmos/files/dark-energy.md) (the joint fit under the $`z > 0.01`$ cut).

---

## 0. What the test assumes

The test scores one declared model against two datasets. It does not test $`s_0 > 0`$, the clock exponent, or MIT as a whole (§8).

**The model** is [the Temporal Budget](temporal-budget.md)'s Model D+Λ, with $`\Omega_\Lambda = 0.685`$ fixed as the published Λcos fit fixes it, and $`s_0`$ on $`[0.001, 0.99]`$:

```math
E^2(z; s_0) = \frac{1-\Omega_\Lambda}{1-s_0^2}\,(1+z)^3 - \frac{(1-\Omega_\Lambda)\,s_0^2}{1-s_0^2}\,(1+z) + \Omega_\Lambda, \qquad I(z; s_0) = \int_0^z \frac{dz'}{E(z'; s_0)}.
```

**The likelihoods** are the published fit's.
- $`\chi^2_\text{SN}(s_0)`$ is $`(m - M - \mu)^\top C^{-1}(m - M - \mu)`$ minimized over the offset $`M`$ on $`[-20, -18]`$, with $`\mu = 5\log_{10}[(1+z)(c/70)\,I] + 25`$ and $`C`$ the row's block of the supernova covariance.
- $`\chi^2_\text{BAO}(s_0)`$ is the 13-point DESI DR2 form minimized over $`H_0 r_d`$ on $`[8000, 12000]`$ km/s, the predictions being $`c/(H_0 r_d)`$ times $`I`$, $`1/E`$ and $`(z I^2/E)^{1/3}`$.
- Both nuisances are profiled analytically, each clipped to its box.

**The numerics** are `fit_lcos.py`'s own: $`E`$ on 4000 points from $`z = 0`$ to 2.5, $`I`$ by the cumulative trapezoid with linear interpolation to the data's redshifts, and the supernova covariance read from its upper triangle, as `fit_lcos.py`'s Cholesky factorization reads it. The file is not exactly symmetric: 778 of its 2 893 401 entries differ from their transposes, by $`3 \times 10^{-8}`$ at most. Every minimum over $`s_0`$, for the data and for every mock, is taken on a uniform grid of 1961 points in $`u = s_0^2`$, a step of about $`5 \times 10^{-4}`$, then by the three-point parabola about the best grid point, kept between its neighbours and inside the box.

On these numerics the all row's $`T`$ is 5.8866. The committed outputs cited below were computed on another $`z`$ grid and from the covariance's other triangle, and give 5.8867.

## 1. The question

Do Pantheon+ and DESI DR2 BAO admit one common $`s_0`$ in the model's range? [The Temporal Budget](temporal-budget.md)'s §III records the split: the supernovae alone prefer $`s_0 = 0.389`$, while BAO alone and the joint fit sit on the floor.

**The statistic** is the parameter goodness-of-fit of Maltoni and Schwetz, with $`s_0`$ the one parameter the two datasets share:

```math
T = \min_{s_0}\big[\chi^2_\text{SN}(s_0) + \chi^2_\text{BAO}(s_0)\big] - \min_{s_0}\chi^2_\text{SN}(s_0) - \min_{s_0}\chi^2_\text{BAO}(s_0).
```

$`T`$ is zero when the two datasets' minima coincide, and positive otherwise.

**The rows.**

| row | light curves | role |
|---|---|---|
| all | the 1701 of the published fit | graded |
| cut | the 1590 with $`z_\text{HD} > 0.01`$, with the covariance's block | graded |
| stress | the 960 with $`z_\text{HD} > 0.1`$ | reported, not graded |

- **Neither graded row is preferred.** The first is the published fit's baseline; the second applies the cut the supernova analyses themselves apply. The rows are nested, so equal grades are not independent confirmations.
- **The cut.** Brout et al. give 0.01 as the nominal minimum redshift for Pantheon+ cosmology fits without SH0ES (the caption of their Figure 16). The data file carries $`z_\text{HD}`$ alone, so the cut is on it, as in the Λcos repo's robustness check; which redshift the paper's minimum applies to is OPEN. No light curve sits at $`z_\text{HD} = 0.01`$ itself, so either reading of the boundary keeps the same 1590.

## 2. Frozen inputs

**The files,** pinned by SHA-256. The first five are in the Λcos repo at the base commit `8558124`. The other four are in the design commit: the generator, written apart from the instrument and not imported by it, wrote the synthetic sets and the forecast; the coverage record holds BAO mocks the generator drew and the instrument evaluated (§3).

| file | contents | SHA-256 |
|---|---|---|
| `data/pantheon_plus.csv` | Pantheon+, 1701 light curves (`zHD`, `m_b_corr`) | `46a9334d15f7115435f662038692061a06fa36ba87e61e85bc17f5ac86c439a8` |
| `data/pantheon_plus_cov.npy` | its covariance, read from its upper triangle | `5c1b855c02e6a96ca8aa651e5e645af2db3b5f15f0c3647ca93c10ca27f8197e` |
| `data/desi_dr2_bao.csv` | DESI DR2 BAO, 13 points: one $`D_V/r_d`$, and six pairs of $`D_M/r_d`$ and $`D_H/r_d`$ | `c746badffdef7f5e6b475d075f55a4de12173e991c94cb3a00eb498b9b5c254a` |
| `data/desi_dr2_bao_cov.npy` | its covariance | `4d6ce177d7e96fb63199af88c2688a926dbb166acd61dc9f75dc0da7b4825c03` |
| `results/lcos_summary.json` | the published joint best fit, whose $`M_B`$ the mocks use | `b234fd104fedce1f333ec9b058448694ed945ea8ff1f86cdb11ef488fc2ac2bd` |
| `data/sn_bao_synthetic.json` | the generator's synthetic sets: a null set at the published joint best fit, and four with the supernovae at one $`s_0`$ and BAO at another, both at 0.3 in one of them | `95b65237bf0f4237b41da1e19c48eaa53424c14d0ca77c7f21b1c8616a3a2717` |
| `data/sn_bao_forecast.json` | the generator's null distributions at every truth and midpoint of §3, on both graded rows | `3638aa06b790086395d324a61520315deb9859610be3f1f5708da461b63ffe6b` |
| `data/sn_bao_coverage.json` | the coverage record of $`J`$, which G6 reads back | `c3eeb225d3a9ce5a8f34dc523f1638570901e1ee7bd8b698f3230791e4905f28` |
| `scripts/sn_bao_generator.py` | the generator; G6 recomputes the thresholds and the graded $`p`$ with its code | `bf093cb30e6f0e16878611fb79c3e444610426ca88b8e9bba3ef6cf9e6d68e34` |

**The parameters.** $`s_0`$ on $`[0.001, 0.99]`$, $`H_0 r_d`$ on $`[8000, 12000]`$ km/s and $`M_B`$ on $`[-20, -18]`$: the box of `fit_lcos.py`, profiled and not sampled.

**The code** is `scripts/sn_bao_consistency.py` in the Λcos repo, on the branch `sn-bao-consistency`, at the design commit `e3ef4e5`. Its SHA-256 is, as at qualification, `13967fa9df0491829d801095baa4f3a14e08e2ab0ca3f5eb02ada5463551c460`. Its seed is 20261117, and it draws 100 000 mocks per truth and row. The environment is Λcos's own (Python 3.9.6, numpy 2.0.2, scipy 1.13.1, pandas 2.3.3), and checking it is the script's first act. Until the run is authorized, its guard lets the cut and stress rows' supernovae be evaluated only where the answer is already committed: in flat ΛCDM, and in Model D+Λ at the floor.

### Pins

The run reads this table. It requires the checkout to sit at the design commit and to be clean, and the script and every file to match their SHA-256.

| pin | value |
|---|---|
| design commit | `e3ef4e5d414e107be6d73e56f8e1e0db6836c636` |
| script | `13967fa9df0491829d801095baa4f3a14e08e2ab0ca3f5eb02ada5463551c460` |
| data/pantheon_plus.csv | `46a9334d15f7115435f662038692061a06fa36ba87e61e85bc17f5ac86c439a8` |
| data/pantheon_plus_cov.npy | `5c1b855c02e6a96ca8aa651e5e645af2db3b5f15f0c3647ca93c10ca27f8197e` |
| data/desi_dr2_bao.csv | `c746badffdef7f5e6b475d075f55a4de12173e991c94cb3a00eb498b9b5c254a` |
| data/desi_dr2_bao_cov.npy | `4d6ce177d7e96fb63199af88c2688a926dbb166acd61dc9f75dc0da7b4825c03` |
| results/lcos_summary.json | `b234fd104fedce1f333ec9b058448694ed945ea8ff1f86cdb11ef488fc2ac2bd` |
| data/sn_bao_synthetic.json | `95b65237bf0f4237b41da1e19c48eaa53424c14d0ca77c7f21b1c8616a3a2717` |
| data/sn_bao_forecast.json | `3638aa06b790086395d324a61520315deb9859610be3f1f5708da461b63ffe6b` |
| data/sn_bao_coverage.json | `c3eeb225d3a9ce5a8f34dc523f1638570901e1ee7bd8b698f3230791e4905f28` |
| scripts/sn_bao_generator.py | `bf093cb30e6f0e16878611fb79c3e444610426ca88b8e9bba3ef6cf9e6d68e34` |

## 3. The calibration

The null hypothesis is that one point $`(s_0, H_0 r_d, M)`$ of the box generated both datasets. It is composite: $`T`$'s distribution depends on $`s_0`$ and, weakly, on $`H_0 r_d`$. The model's range ends at the floor, where BAO alone and the joint fit sit, and a parameter on the boundary of its range changes a likelihood ratio's distribution (Chernoff; Self and Liang): at the floor about a quarter of the mocks give $`T = 0`$. So $`T`$ is not read as a $`\chi^2`$ with one degree of freedom, and the grade is calibrated by mocks. The graded $`p`$ is the largest upper-tail probability of the observed $`T`$ over a confidence set for $`s_0`$ and $`H_0 r_d`$, plus the probability that the set misses them. The construction is Berger and Boos's; the argument is given in full below.

**The set.** It is built from the BAO data alone, and no supernova:

```math
J = \big\lbrace (s_0, H_0 r_d) \text{ in the box} : \chi^2_\text{BAO}(s_0, H_0 r_d) \le q \big\rbrace,
```

with $`\chi^2_\text{BAO}`$ not profiled, and $`q`$ the $`1-\beta`$ quantile of a $`\chi^2`$ with 13 degrees of freedom, one per BAO point. Here $`\beta = 10^{-5}`$, so $`q = 46.912`$. If the null holds at a point of the box, the BAO residuals at that point are thirteen Gaussians with the stated covariance, so $`\chi^2_\text{BAO}`$ there has exactly that distribution, and $`J`$ misses the point with probability exactly $`\beta`$ (DERIVED). In BAO mocks at five truths, four million each, $`J`$ missed the truth 184 times against an expected 200 ± 14.

**What is proven.** Write $`p(\theta)`$ for the upper-tail probability of the observed $`T`$ when the truth is $`\theta`$, and $`p_g`$ for the largest $`p(\theta)`$ over all of $`J`$, plus $`\beta`$. Under any null truth $`\theta_0`$, either $`J`$ misses $`\theta_0`$, which has probability $`\beta`$, or $`p_g \ge p(\theta_0) + \beta`$. A $`p`$-value at the truth is at or below $`\alpha - \beta`$ with probability at most $`\alpha - \beta`$. So $`p_g`$ is at or below $`\alpha`$ with probability at most $`\alpha`$, for every $`\alpha`$ and every $`\theta_0`$ (DERIVED). $`J`$ and $`T`$ share the BAO data; the argument does not need them independent.

**What is sampled.** That proof is for the largest $`p`$ over all of $`J`$, which is a continuous set. The lattice below, its one refinement and its Monte Carlo allowance approximate that largest $`p`$. It has not been proven that the approximation holds over all of $`J`$: that rests on the mocks (INFERRED; see the truths, below). So the grade as computed is not proven valid at every null truth, and this page does not say it is.

**For these data,** $`J`$'s $`s_0`$ values run from the floor to 0.3544. Its $`H_0 r_d`$ interval is [9868, 10188] km/s at the floor and closes to 9769 at the top; its lowest value is 9735, at $`s_0 = 0.33`$. Everywhere on $`J`$ the nuisance is more than 1700 km/s inside its box, and both codes resolve the likelihood there, by about fifty grid steps at the least. $`J`$ is not empty: the BAO $`\chi^2`$ at the floor is 13.5331.

**The truths.** The lattice in $`s_0`$ runs from the floor through the first value past $`J`$: 0.001, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35 and 0.40. At each value inside $`J`$, $`H_0 r_d`$ takes three values: the BAO data's own profiled value, and the two ends of $`J`$'s interval at that $`s_0`$. At 0.40 it takes the profiled value.
- **At the baseline's $`T`$ the largest sampled $`p`$ is at the last truth,** in both codes, and the last truth lies past $`J`$ both ways: its $`s_0`$, 0.40, is above $`J`$'s 0.3544, and its $`H_0 r_d`$, 9691.7, is below $`J`$'s lowest, 9735.
- **On the mocks $`p`$ rises with $`s_0`$ along the lattice, and as $`H_0 r_d`$ falls.** The second is the weaker: summed over 36 pairs of ends, the low end's $`p`$ exceeds the high end's at two standard errors. If $`p`$ is monotone in both throughout, the last truth bounds the largest $`p`$ over $`J`$ from above (INFERRED: an empirical check on a lattice, not a proven bound over the continuous set).
- **The refinement tests the $`s_0`$ direction.** In $`H_0 r_d`$, three sampled values do not exclude a maximum inside $`J`$'s interval; the whole movement across that interval is a percent or two of $`p`$, against what the bound adds, 5% of $`p`$ at the baseline's $`T`$ and 3% at the first bar.

**The mocks.** At each truth, for each graded row, 100 000 mock pairs are drawn from the model through the row's own covariances, the supernovae and BAO independent, on a stream fixed by the seed, the row and the truth. $`T`$ is computed for each exactly as for the data. The $`p`$-value at a truth is $`(1 + n)/(1 + N)`$, where $`n`$ counts the mocks at or above the observed $`T`$ and $`N`$ is their number.

**The offset M.** Two statements, kept apart.
- **The first is exact.** On any data whose offset, profiled with $`M`$ unbounded, lies inside its box at the minima of the supernova and joint profiles, both taken with $`M`$ unbounded, $`T`$ equals its value with $`M`$ unbounded, which a constant added to every magnitude does not change (DERIVED). The BAO profile carries no offset. Where that condition fails, a boxed minimum can sit at another $`s_0`$, and a shift can then change $`T`$.
- **The second is that such realizations are a negligible tail.** The data's own profiled offset at the floor, which the guard allows, is −19.354 on the all row and −19.356 on the cut row; its standard error is at most 0.00377; along $`J`$ its expectation moves by 0.011 at most. The nearer edge of its box is 0.643 away, over 170 standard errors.
- **So the offset joins the confidence set.** Write $`\hat M`$ for the data's offset at the floor, profiled with $`M`$ unbounded. At a truth $`(s_0, H_0 r_d, M)`$ it is $`M + \delta(s_0) + \epsilon`$, where $`\delta(s_0) = \mathbf{1}^\top C^{-1}[\mu(s_0) - \mu(0.001)]\,/\,\mathbf{1}^\top C^{-1}\mathbf{1}`$ is the shift the model fixes and $`\epsilon`$ is Gaussian with standard error $`\sigma_M = (\mathbf{1}^\top C^{-1}\mathbf{1})^{-1/2}`$. So with each point of $`J`$ the set takes the $`M`$ with $`\lvert \hat M - \delta(s_0) - M \rvert \le 8\,\sigma_M`$. At any null truth it misses $`M`$ with probability under $`1.3 \times 10^{-15}`$, the tail beyond eight standard errors (DERIVED). With $`J`$'s own miss probability, the paired set over all three parameters misses a null truth with probability at most $`\beta`$ plus $`1.3 \times 10^{-15}`$ (DERIVED), and it is the set the argument above applies to. Along $`J`$ the shift's size is at most 0.011, so every $`M`$ in the set lies within 0.05 of $`\hat M`$, and for each the box's nearer edge is still over 150 standard errors off.
- **A minimum can fall anywhere in the box,** and there the model moves the offset's expectation by at most 1.131, at $`s_0 = 0.99`$, toward the farther edge, at least 1.354 away. So for every $`M`$ in the set, at every minimum the unbounded offset sits over 45 standard errors inside its box, and a mock reaches the box with a probability far smaller again.
- **The miss probability the grade carries** is then $`\beta`$ plus less than $`1.3 \times 10^{-15}`$, the same number at every digit shown. A gate checks, mock by mock, that the unbounded offset lies inside its box at every grid point, and so at the supernova and joint minima (§4).

**The bound.** A $`p`$ from $`N`$ mocks has the Monte Carlo standard error $`\mathrm{SE}(p) = \sqrt{p(1-p)/N}`$. Let $`p_1`$ be the largest $`p`$ over the truths. One refinement is fixed in advance: the $`s_0`$ midway between that truth's and each neighbouring lattice value is added, with the same rule for $`H_0 r_d`$, and the largest is taken again, $`p_2 \ge p_1`$. If $`p_2 - p_1 > 3\,\mathrm{SE}(p_1)`$, the calibration is not bounded and the row's grade is Uninformative. Otherwise the graded $`p`$ is $`\min\big(1,\; p_2 + 2\,\mathrm{SE}(p_2) + \beta\big)`$.

**The bars as thresholds on T.** Each bar $`b`$ is equivalently a threshold: the $`T`$ above which the graded $`p`$ is below $`b`$. At one truth it is the $`(c+1)`$-th largest mock $`T`$, where $`c`$ is the largest count with $`p_c + 2\,\mathrm{SE}(p_c) + \beta < b`$ and $`p_c = (1+c)/(1+N)`$; the row's threshold is the largest over the truths. At $`N = 100\,000`$ and $`\beta = 10^{-5}`$ the counts are 4862 and 237. The thresholds use the redshifts, the covariances, the BAO data and published parameters only. No supernova residual enters, so they are fixed at qualification (§4), before the cut row is evaluated. The refinement can only raise the graded $`p`$. The grade is read from the graded $`p`$, and the thresholds are its equivalent whenever the refinement leaves the largest in place.

**Reported, not graded:** the $`p`$-values at the floor and at each row's 95% profile limit (0.177 on the all row, 0.149 on the cut row), and the $`\chi^2`$ value with one degree of freedom.

## 4. Qualification and the gates

**Qualification, before the freeze,** ran on the candidate files: the environment check; G1 to G5 and G7, with the pin check's rehearsal; the calibration and G6; then R; then every arm, each after its parent passed, at the same tolerances. Each deterministic tolerance was set beforehand from its floor, measured on a dry run, and qualification measured every floor again. The measured data met only what the guard allows before the freeze: the all row, and the cut row in flat ΛCDM and at the floor. Every other evaluation was on mocks, on the generator's pinned synthetic sets, and on the BAO data.

| gate | passes when | tolerance | arm that must turn it red |
|---|---|---|---|
| G1, parity | the instrument's $`E`$, $`\chi^2_\text{SN}`$, $`\chi^2_\text{BAO}`$ and BAO predictions equal `fit_lcos.py`'s at fixed points | $`10^{-9}`$ relative | $`\Omega_\Lambda = 0.686`$; separately, $`D_V`$'s exponent set to 1/2 |
| G2, anchors | the committed results at the base commit, on the numerics they were computed with: on the all row each profile's minimum and its $`s_0`$, $`T`$, and the joint profile at $`s_0 = 0.39`$; on the cut row the flat ΛCDM fits and Model D+Λ's joint value at the floor | $`10^{-5}`$ in $`\chi^2`$ and $`T`$; $`10^{-5}`$ in $`s_0`$ | a BAO point dropped; separately, the cut applied to the data with the covariance's leading block kept |
| G3, null | $`T = 0`$ on the two synthetic sets where both datasets share one $`s_0`$, on both graded rows | $`10^{-7}`$ | a planted set given as a null set |
| G4, planted tension | $`T`$ on the planted synthetic sets equals the generator's | $`10^{-2}`$ | $`D_V`$'s exponent set to 1/2 |
| G5, grids | $`T`$ moves little on a $`u`$ grid ten times finer: on every synthetic set at qualification, and on each graded row at the run | $`10^{-6}`$ | the registered grid made ten times coarser |
| G6, calibration | the ten parts below | as listed | twelve arms, below |
| G7, pins | every pinned file, and `fit_lcos.py` up to its MCMC section, match their SHA-256; at qualification exactly the design commit's new files are untracked, and at the run the checkout is clean; the commit and the script's SHA-256 are recorded | exact | one byte changed in a pinned file; in a scratch clone, the run's pin check refusing a registration that names the base commit, a wrong script hash, and a stray file in the checkout |
| R, rehearsal | the run's analysis on the planted set with the supernovae at $`s_0 = 0.389`$ and BAO at the floor, in place of the measured data, gives the grades and Verdict that the generator's $`T`$ and thresholds give, with $`T`$ within G4's tolerance; and the run's closing steps run on it: G5 on its graded rows, which a moved stress row cannot fail, and the Verdict's Uninformative flag | as G4 and G5 | the null set given as the rehearsal's data; separately, a graded row's finer-grid $`T`$ moved |

**G6, part by part.** Each part has its own arm.

| part | passes when | tolerance | arm |
|---|---|---|---|
| design | $`J`$'s top, its lattice, its truths and midpoints, and their $`H_0 r_d`$ values equal the generator's | $`10^{-5}`$ in $`s_0`$; 0.01 km/s | the lattice cut down to the floor alone |
| q | $`q`$'s upper tail is $`\beta`$ under a $`\chi^2`$ with as many degrees of freedom as BAO points, by the instrument's own closed form and by the generator's | $`10^{-12}`$ | $`q`$ taken with 12 degrees of freedom |
| coverage | the coverage record, read back: $`J`$ missed the truth at the rate $`\beta`$ | 3 standard errors | the record's misses doubled |
| halves | at every calibrated set and bar, the two halves of the mocks put the same share above the set's threshold | 4 standard errors | each second half taken from the next set |
| generator | at every set and bar, the instrument's count of mocks at or above the generator's threshold agrees with the generator's own | 4 standard errors | the truths mislabeled by one lattice step |
| recompute | each row's thresholds and graded $`p`$, recomputed by the generator's code from the tails and counts the instrument saves, equal the instrument's; and where every mock is at or above the observed $`T`$, both codes give a graded $`p`$ of exactly 1 | exact | $`\beta`$'s term dropped; separately, a threshold moved; separately, the cap at 1 removed |
| noise | at every set, the whitened noise's mean squared norm is the number of points, for the supernovae and for BAO | 5 standard errors | a mock drawn with the wrong block |
| offsets | in every mock, the offset profiled with $`M`$ unbounded lies inside its box at every grid point, and so at the supernova and joint minima | inside | the box narrowed to 0.005 about the reference offset |
| M | mocks with the truth's offset moved by 0.1 either way, on the same stream, give the same $`T`$, at the floor and at $`s_0 = 0.30`$ on both rows | $`10^{-9}`$ | the offset held at the reference, not profiled |
| refinement | the bound's one refinement runs: every midpoint beside the largest $`p`$ is calibrated, and at qualification the all row's graded $`p`$ is bounded | runs | the midpoints left out |

**The qualification record** (2026-11-18, on the candidate files at Λcos `8558124`) is [`qualification.json`](scripts/sn-bao-consistency/qualification.json), SHA-256 `67dc3ec787e6b8869fb7c7e89864ef16d0d4c295b9936527f14f17f33f6eb3a9`.
- The environment check passed and every gate passed. Each of the 22 arms turned its gate red after its parent passed, and so did the three arms of the pin check's rehearsal, in a scratch clone.
- Two full runs agree in every field but the time taken.
- G6's statistical parts stood inside their limits: the largest departure between the halves was 2.59 standard errors, between the two codes 2.69, and in the noise 2.82. Over every grid point of every mock, the closest the unbounded offset came to its box's edge was 0.21.

Each deterministic tolerance sits at least ten times above its measured floor:

| gate | quantity | measured floor | tolerance |
|---|---|---|---|
| G1 | worst relative departure from `fit_lcos.py` | $`4.7 \times 10^{-15}`$ | $`10^{-9}`$ |
| G2 | $`\chi^2`$ and $`T`$ against the committed anchors | $`1.1 \times 10^{-7}`$ | $`10^{-5}`$ |
| G2 | $`s_0`$ at the committed minima | $`2.9 \times 10^{-7}`$ | $`10^{-5}`$ |
| G3 | $`T`$ on the null sets | $`5.3 \times 10^{-9}`$ | $`10^{-7}`$ |
| G4 | $`T`$ on the planted sets, against the generator's | $`3.2 \times 10^{-4}`$ | $`10^{-2}`$ |
| G5 | $`T`$'s move on the finer grid | $`5.3 \times 10^{-8}`$ | $`10^{-6}`$ |
| G6 | $`J`$'s top against the generator's | $`1.1 \times 10^{-7}`$ | $`10^{-5}`$ |
| G6 | $`H_0 r_d`$ at the truths against the generator's, km/s | $`4.7 \times 10^{-4}`$ | $`10^{-2}`$ |
| G6 | $`q`$'s upper tail against $`\beta`$ | $`2.2 \times 10^{-20}`$ | $`10^{-12}`$ |
| G6 | $`T`$'s move when the offset moves | $`1.8 \times 10^{-12}`$ | $`10^{-9}`$ |
| R | the rehearsal's $`T`$ against the generator's | $`3.2 \times 10^{-4}`$ | $`10^{-2}`$ |

**The frozen thresholds** are the instrument's, from qualification's own calibration, whose streams the run repeats. Each is set by the truth at $`s_0 = 0.40`$. Its Monte Carlo error is half the spread of the order statistics one binomial standard error either side.

| row | at $`p = 0.05`$ | at $`p = 0.0027`$ |
|---|---|---|
| all | 3.953 ± 0.022 | 9.074 ± 0.106 |
| cut | 3.921 ± 0.022 | 9.140 ± 0.088 |

**A gate that fails.**
- **Before the freeze,** the instrument goes back for repair, and qualification runs again in full.
- **After the freeze,** a failed environment or pin check stops the run before any gate, and a gate that fails ends it as Uninformative. A repair returns only through a reviewed version of this page.

**The run, once:**
1. The environment check, then the registration's pins (§2).
2. G1 to G5 and G7 again, at the frozen tolerances.
3. The calibration, on both graded rows, at every truth and midpoint of §3 and at the two 95% profile limits.
4. Each row's $`T`$, its parts and the reported rows of §6; then each graded row's graded $`p`$ and grade, and the Verdict.
5. G6 on the run's own calibration, recomputed at each graded row's measured $`T`$, and G5 on each graded row. If either fails, the Verdict is Uninformative. The stress row's G5 move is reported beside that row.

## 5. Grades and the Verdict

| graded $`p`$ | grade |
|---|---|
| $`p \ge 0.05`$ | CONSISTENT |
| $`0.0027 \le p < 0.05`$ | MILD TENSION |
| $`p < 0.0027`$ | TENSION |

| the two rows | Verdict |
|---|---|
| both CONSISTENT | Positive: no detectable inconsistency on a common $`s_0`$ within the model's range, $`s_0 \ge 0`$, under the registered test; BAO's cost at the floor is reported beside it |
| both TENSION | Negative: evidence against a common $`s_0`$ under the specified model and likelihood |
| both MILD TENSION | Inconclusive |
| the grades differ | Mixed: sample-dependent, both grades recorded |
| a gate fails, or a row's calibration is not bounded | Uninformative |

With the BAO-only and the joint minima both on the floor, $`T`$ counts only the supernovae's pull upward. BAO's own optimum lies below $`s_0 = 0`$, where the model does not go, and what that costs BAO is outside $`T`$ (§10).

## 6. Reported, not graded

- Each row's supernova-only and BAO-only best $`s_0`$, with the region within 1 of its minimum.
- Each row's supernova and BAO $`\chi^2`$ at the floor, beside flat ΛCDM's own minima.
- The same $`T`$ in flat ΛCDM with $`\Omega_m`$ shared, on each row, as the reference for what the data do in the standard model.
- The $`p`$-values at the floor and at the 95% profile limits (§3).
- The stress row, $`z_\text{HD} > 0.1`$ (960 light curves), as the Λcos repo's matter-exponent gate and robustness check carried it, with its $`T`$'s move on the finer grid of G5.
- $`T`$ at the Λcos paper's other anchors, $`\Omega_\Lambda = 0.68`$, 0.69, 0.70 and 0.715.
- $`J`$'s $`s_0`$ range and $`q`$ (§3).
- Beside each graded row's $`T`$, both rules' thresholds: the registered ones, and the largest quantiles over the fifteen truths of the rule this calibration replaced, without the bound that rule's graded $`p`$ carried (3.899 and 9.405 on the all row, 3.867 and 9.228 on the cut row). If a row's $`T`$ lies between the two rules' thresholds at either bar, the Results say so beside the grade.

## 7. Moves that do not count

- Changing the model, $`\Omega_\Lambda`$, the rows, the statistic, the bars, $`\beta`$, the lattice of truths, the bound, the seed or $`N`$ after the freeze, or before it except through a reviewed version of this page.
- Evaluating Model D+Λ on the cut or stress row's supernovae away from the floor before the run, directly or by subtracting a BAO profile from the committed joint profile.
- Adding a cut, a sample or a statistic after the fact.
- Settling a difference between the rows by preferring one.
- Reading $`s_0 > 0`$, or its absence, off any outcome.
- Choosing any term for its expected outcome.

## 8. After the run

The result is recorded whatever it is, in one results commit in Λcos and in this page's Results. The Results carry the Verdict, each graded row's $`T`$, graded $`p`$ and grade, and the reported rows of §6.

What each outcome means is fixed now, by §5's table and by these limits on reading it:
- **No outcome tests** $`s_0 > 0`$, the clock exponent, or MIT as a whole.
- **None says which light curves carry the pull,** only whether it is sensitive to including those below $`z = 0.01`$, and that only if the rows differ.
- **CONSISTENT** means agreement within $`s_0 \ge 0`$, not that the two datasets agree.
- **Mixed** records a grade that depends on the sample, with both grades standing. The rows are nested, and the difference between them is not itself tested.

The result lands in three places: the Results here, a dated pointer on [the Temporal Budget](temporal-budget.md)'s §X row, and the working index. The Temporal Budget's §III table, §IV, §V and §XI's ledger are not changed by this result: they carry $`s_0 = 0.389`$ until a separate ruling. The Euclid card is not touched.

## 9. What the test leaves out

- $`\Omega_\Lambda`$ free, and the CMB.
- Union3 and DES Y5, for which DESI reports 2.1σ and 2.9σ in ΛCDM.
- Which individual light curves carry the pull.
- Model selection against ΛCDM.
- The continuation to $`s_0^2 < 0`$, which the model does not have.

## 10. Expectation and caveats

**What is known before the freeze.**
- **The all row's T,** 5.8867 (5.8866 on the registered numerics). Because BAO alone and the joint fit both sit on the floor, it is exactly what the supernovae pay to be moved from 0.389 to the floor: 1772.5637 − 1753.1439 − 13.5331. Read as a $`\chi^2`$ with one degree of freedom, its $`p`$ is 0.0153.
- **Its grade, in effect.** On mocks the all row's graded $`p`$ at that $`T`$ is 0.0166 in the instrument and 0.0160 in the generator, between the bars, so MILD TENSION.
- **The thresholds** (§4).
- **The cut row's references.** In flat ΛCDM with $`\Omega_m`$ shared, its $`T`$ is 1416.6561 − 1403.7046 − 10.3615 = 2.590, 1.61σ, close to DESI's own 1.7σ for Pantheon+ against DR2 BAO in ΛCDM, so the committed pipeline reproduces the literature there. For Model D+Λ the joint fit and BAO alone sit on the floor again, so the cut sample's $`\chi^2`$ at the floor is 1417.9925 − 13.5331 = 1404.4594.
- **The floor's cost to BAO.** BAO alone reach 13.5331 at the floor against 10.3615 in flat ΛCDM with $`\Omega_m`$ free, a cost of 3.17 that $`T`$ does not count, since BAO's own optimum ($`u \approx -0.063`$, INFERRED) lies below $`s_0 = 0`$.
- **The reachable Verdicts.** The run repeats qualification's streams, so the all row stays at MILD TENSION, and Positive and Negative are out of reach. The outcome is Mixed or Inconclusive, set by the cut row, or Uninformative if a gate fails or the cut row's calibration is not bounded.
- **A sample dependence on record.** The Λcos repo's matter-exponent gate found its preference, in $`\Delta\chi^2`$, fall from −8.75 on all the light curves to −2.97 under the cut.
- **The grading rule's history.** Three rules, each set with the all row's $`T`$ known.
  - The first graded on the larger $`p`$ of two truths, the floor and the 95% limit: 0.0070 for the baseline, by a no-data forecast.
  - The second took the largest $`p`$ over fifteen truths spanning the box: 0.0177 on mocks. Mocks then found two things at the top of the box: the supernova likelihood as narrow as one grid step, where the instrument and the generator disagreed, and, above $`s_0 = 0.80`$, the BAO nuisance outside its box. The second rule's largest $`p`$ was set there.
  - This one stops that lattice at 0.40 and adds $`\beta`$: 0.0166. The plain $`\chi^2`$ reading is 0.0153.
  - $`\beta`$ and the lattice's last value were chosen with a table of alternatives in hand, and every one of them grades the baseline MILD TENSION, between 2.37σ and 2.43σ.

**The expectation, registered.**
- **All row:** MILD TENSION, with a graded $`p`$ of 0.0166, and the floor's own calibration near 0.004.
- **Cut row:** CONSISTENT if Model D+Λ fits the cut sample no better than flat ΛCDM does, since then $`T`$ is at most 1404.4594 − 1403.7046 = 0.755 and the graded $`p`$ is at least 0.38.
- **Verdict:** Mixed.
- **The supernova-only $`s_0`$ under the cut:** OPEN.

**Caveats.**
- **Retrospective, not blind.** The data, the published fits and this calibration are known before the freeze. The freeze prevents tuning, not prior contact. Registering does not make the baseline's result prospective; what the freeze protects is the cut row.
- **The grade samples a supremum.** The proof of §3 covers the largest $`p`$ over all of $`J`$, and the grade samples it on a lattice. That the lattice stands in for the whole rests on the mocks (INFERRED).
- **The cut's redshift** is $`z_\text{HD}`$ (§1).

## 11. The freeze

What remains, in order:

1. Built: the Λcos instrument, its generator and their files, on the branch `sn-bao-consistency`, in the design commit `e3ef4e5`.
2. Qualified (2026-11-18), in the order of §4; the record is in §4.
3. Review of this page, the instrument and the generator, and the go to freeze (2026-11-18).
4. The freeze (2026-11-18). The design commit `e3ef4e5` is pushed to the Λcos branch, holding the instrument and the four new files of §2, and nothing runs there. Then this page is committed to MIT main, its Pins table naming that commit and the script's SHA-256. The run starts only after both.
5. The run, once (§4), from a clean checkout of the design commit. Its one results commit follows on the branch.
6. Review of the results; then, on its own go, the record is entered here. After that, on a further go, the branch is merged into Λcos main.

## Results

**Executed 2026-11-18, once,** from the Λcos design commit `e3ef4e5` of the branch `sn-bao-consistency`, in a clean checkout, against this registration as it sat on MIT main (`b6f15db4`, page SHA-256 `5942e831ba57e5ad38d6ff5136d2d053da69e184967a3376988f32413dd65968`). The single results commit is `00fcf21`, on the branch. The design commit also reached Λcos main ahead of §11's step 6, through pull request #3 (merge `f518592`, 2026-11-18, after the freeze and before the run, with the design commit's tree unchanged); the results commit is on the branch alone. The run's whole record is `results/sn_bao_consistency/run.json` there, with `g6_counts.json`, the mock counts at each graded row's measured $`T`$; the saved tails behind them are qualification's, array for array.
- The environment check passed, and every pin held: the design commit, a clean checkout, the script and all nine files.
- G1 to G5 and G7 passed again at the frozen tolerances. G6 passed on the run's own calibration, and G5 on both graded rows.
- The calibration repeated qualification's streams: each graded row's thresholds are the frozen ones of §4, to the last digit.
- The all row's $`T`$ is 5.88664, its value on the registered numerics (§0).

| row | $`T`$ | graded $`p`$ | grade |
|---|---|---|---|
| all, the 1701 light curves | 5.887 | 0.0166 | MILD TENSION |
| cut, the 1590 with $`z_\text{HD} > 0.01`$ | 0.689 | 0.4127 | CONSISTENT |

**Verdict: Mixed.** The grades differ (§5).

**What it means, as §8 fixed it:**
- **Mixed** records a grade that depends on the sample, with both grades standing. The rows are nested, and the difference between them is not itself tested.
- **The pull is sensitive to including the 111 light curves below $`z = 0.01`$.** The test does not say which of them carry it.
- **CONSISTENT on the cut row** means agreement within $`s_0 \ge 0`$, not that the two datasets agree: BAO's own optimum lies below $`s_0 = 0`$, and what that costs BAO is outside $`T`$.
- **No outcome tests** $`s_0 > 0`$, the clock exponent, or MIT as a whole.

**The calibration, row by row.**
- **All row.** The largest sampled $`p`$, 0.0158, is at the last truth, $`s_0 = 0.40`$, with $`H_0 r_d`$ profiled, and the refinement leaves it there. The calibration is bounded, and the graded $`p`$ is 0.0166.
- **Cut row.** The largest sampled $`p`$, 0.4094, is at $`s_0 = 0.35`$, with $`H_0 r_d`$ at the low end of $`J`$'s interval. The refinement moves it to the midpoint $`s_0 = 0.325`$, with $`H_0 r_d`$ at the low end of $`J`$'s interval, where it is 0.4096: a move within $`3\,\mathrm{SE}`$, so the calibration is bounded, and the graded $`p`$ is 0.4127.
- **Neither row's $`T`$ lies between the two rules' thresholds** (§6). The registered ones are 3.953 and 9.074 on the all row and 3.921 and 9.140 on the cut row; those of the rule this calibration replaced, without its bound, are 3.899 and 9.405 on the all row and 3.867 and 9.228 on the cut row.

**Reported, not graded (§6).**

| | all | cut | stress |
|---|---|---|---|
| supernova-only best $`s_0`$, and the region within 1 of its minimum | 0.389, from 0.306 to 0.451 | 0.239, from the floor to 0.345 | 0.260, from the floor to 0.384 |
| BAO-only best $`s_0`$, and the region within 1 of its minimum; joint best $`s_0`$ | the floor, from the floor to 0.090; the floor | the floor, from the floor to 0.090; the floor | the floor, from the floor to 0.090; the floor |
| supernova and BAO $`\chi^2`$ at the floor | 1759.032; 13.533 | 1404.459; 13.533 | 834.858; 13.533 |
| flat ΛCDM's supernova-only and BAO-only minima | 1752.514; 10.362 | 1403.704; 10.362 | 834.285; 10.362 |
| $`T`$ in flat ΛCDM, $`\Omega_m`$ shared | 9.580 | 2.590 | 1.841 |
| $`T`$ in Model D+Λ | 5.887 | 0.689 | 0.567 |
| $`p`$ at the floor; at the row's 95% profile limit | 0.0042; 0.0065 | 0.2191; 0.3058 | |
| the $`\chi^2`$ reading, one degree of freedom | 0.0153 | 0.4064 | |
| $`T`$ at $`\Omega_\Lambda = 0.68`$, 0.69, 0.70 and 0.715 | 4.589, 7.356, 9.652, 10.696 | 0.303, 1.237, 2.644, 3.223 | 0.301, 0.921, 1.865, 2.205 |
| $`T`$'s move on G5's finer grid | $`-4.4 \times 10^{-9}`$ | $`1.9 \times 10^{-9}`$ | $`-9.7 \times 10^{-9}`$, reported |

$`J`$'s $`s_0`$ range runs from the floor to 0.3544, at $`q = 46.912`$, as at qualification.

**Against the registered expectation (§10).**
- **All row:** registered MILD TENSION, with a graded $`p`$ of 0.0166 and the floor's own calibration near 0.004. The run gives MILD TENSION, 0.0166, and 0.0042 at the floor.
- **Cut row:** registered CONSISTENT if Model D+Λ fits the cut sample no better than flat ΛCDM. It fits no better, by 0.066 (1403.7701 against 1403.7044), so $`T`$ is at most 0.755. It is 0.689, and the graded $`p`$ is 0.4127, above the registered 0.38.
- **Verdict:** registered Mixed; the run gives Mixed.
- **The supernova-only $`s_0`$ under the cut,** registered OPEN, is 0.239. The region within 1 of its minimum runs from the floor to 0.345.

## Sources

- D. Brout et al., "The Pantheon+ Analysis: Cosmological Constraints", Astrophys. J. 938, 110 (2022), [doi:10.3847/1538-4357/ac8e04](https://doi.org/10.3847/1538-4357/ac8e04), [arXiv:2202.04077](https://arxiv.org/abs/2202.04077).
- DESI Collaboration, "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints", Phys. Rev. D 112, 083515 (2025), [doi:10.1103/tr6y-kpc6](https://doi.org/10.1103/tr6y-kpc6), [arXiv:2503.14738](https://arxiv.org/abs/2503.14738).
- M. Maltoni and T. Schwetz, "Testing the statistical compatibility of independent data sets", Phys. Rev. D 68, 033020 (2003), [doi:10.1103/PhysRevD.68.033020](https://doi.org/10.1103/PhysRevD.68.033020), [arXiv:hep-ph/0304176](https://arxiv.org/abs/hep-ph/0304176).
- R. L. Berger and D. D. Boos, "P Values Maximized Over a Confidence Set for the Nuisance Parameter", J. Am. Stat. Assoc. 89, 1012 (1994), [doi:10.1080/01621459.1994.10476836](https://doi.org/10.1080/01621459.1994.10476836).
- H. Chernoff, "On the Distribution of the Likelihood Ratio", Ann. Math. Statist. 25, 573 (1954), [doi:10.1214/aoms/1177728725](https://doi.org/10.1214/aoms/1177728725).
- S. G. Self and K.-Y. Liang, "Asymptotic Properties of Maximum Likelihood Estimators and Likelihood Ratio Tests under Nonstandard Conditions", J. Am. Stat. Assoc. 82, 605 (1987), [doi:10.1080/01621459.1987.10478472](https://doi.org/10.1080/01621459.1987.10478472).

---

| **[`<back`](/files/framework/files/working/)** | **[`↑top`](#top)** | **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** | **[`framework`](/files/framework/)** | **[`bedrock`](/files/framework/files/bedrock/)** | **[`dynamics`](/files/framework/files/dynamics/)** | **[`working`](/files/framework/files/working/)** | **[`cosmos`](/files/cosmos/)** | **[`spectrum`](/files/spectrum/)** | **[`tools`](/files/tools/)** |
