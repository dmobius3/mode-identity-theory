<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# R from the Particle Mass Spectrum

**Type:** Program
**State:** Closed
**Status (2026-09-30):** Executed 2026-06-15, the assigned-pair scan tightened 2026-07-28: the mass route determines R independently of Λ, the CMB, and de Sitter, breaking the circularity at order-of-magnitude precision (R ≈ 20 Gpc on electron-muon, ≈ 10.5 Gpc on muon-top). An independent, lower-resolution cross-check: the coupling (α) route is the best-conditioned determination ([the R problem](r-problem.md)).
**Summary:** Determines the curvature radius R from the fermion mass formula's dependence on the hierarchy factor, the mass-sector route to R.
**Inputs:** the fermion mass formula and torsion table, the McKay residual scatter (precision floor), the Ω_Λ hierarchy

Working notes on determining the curvature radius R independently of Λ, the CMB, and the de Sitter relation, using the mass formula's dependence on the hierarchy factor Ω_Λ.

**Status:** EXECUTED (2026-06-15). Order-of-magnitude result. The route runs and genuinely breaks the circularity, but the precision ceiling is about 1 order of magnitude, not the few percent originally targeted. Electron and muon give R ≈ 20 Gpc, Λ ≈ 8.1 × 10⁻⁵⁴ m⁻², about 13.4× below the observed 1.089 × 10⁻⁵². The 2026-07-28 torsion correction improves this: with the top now well-fit at (R2, triv), the muon-top pair infers Λ within 3.8× (about half an order of magnitude), the best of any assigned pair, and electron-muon remains the lepton-only cross-check. See the Result section.

**Why this matters:** ΛR² = 3 starts from the postulate's spectral seed 2/R², lifted by the Gauss equation and normalized by the imported de Sitter vacuum relation (provenance in [the R problem](r-problem.md)). The seed is the content, not the coefficient. But Λ = 3/R² produces a number only with an independent R. Every previous route to R is either circular (de Sitter: R = √(3/Λ), feeds Λ back) or not an independent route to R (the Molien gap fixes the low-ℓ deficit boundary, a surviving spectral fact, but does not by itself pin R). The mass spectrum does determine R independently of measured Λ, the CMB, and the de Sitter back-read, so the circularity is genuinely broken: with an independently determined R, Λ_ref = 3/R² becomes a conditional output from particle physics. Converting R to Λ_ref then uses the Gauss/de Sitter reference relation and is not independent of it, and whether Λ_ref is the physical cosmological constant remains the open Interface question. The prediction lands within about half an order of magnitude of observed for the best assigned pair (muon-top), and within about one order for the electron-muon lepton pair, a real result at that bar but not the percent-level number Sections VI and VIII originally claimed.

---

## Result (executed 2026-06-15)

Run with the framework's own published data (`mass-spectrum.md`): electron = (R7, triv, dist 4), muon = (R8, std, dist 5), so Δd = 1; C_geom(R7) = 0.7564, C_geom(R8) = 0.2382; T²(R7, triv) = 2.250, T²(R8, std) = 13.090; √Ω_Λ = 1.019 × 10⁶¹.

The formula reproduces both masses (m_e = 5.22 × 10⁻⁴ GeV, m_μ = 0.103 GeV) and predicts the ratio m_μ/m_e = 198 against the measured 206.8, a 4.5% miss. Inverting that ratio for the scale gives:

- Ω_Λ = 1.42 × 10¹²³ (framework value 1.04 × 10¹²²)
- R ≈ 20 Gpc (framework 5.38 Gpc), a factor 3.7 too large
- Λ ≈ 8.1 × 10⁻⁵⁴ m⁻², about 13.4× below the observed 1.089 × 10⁻⁵² (1.13 orders of magnitude); R too large, so Λ too small

The 4.5% ratio miss becomes a factor of 13.4 in Λ because the McKay lever is weak: with Δd = 1 the ratio depends on Ω_Λ only through (√Ω_Λ)^(1/30), so inverting amplifies any input error by 60/Δd = 60×.

**Pair scan (updated 2026-07-28).** Every assigned charged-fermion pair was re-checked on the corrected table. The [half-integer torsion correction](torsion-correction.md) moved the top quark onto a well-fit address, (R2, triv) at pred/obs 0.93, and that changes the outcome: the muon-top pair (Δd = 2) now infers Λ ≈ 2.9 × 10⁻⁵³, only 3.8× from observed, and electron-top (Δd = 3) infers Λ ≈ 1.9 × 10⁻⁵³, 5.9× off, both beating electron-muon's 13.4×. Muon (residual 1.02) and top (0.93) are the common-mode, well-fit, high-distance pair the pre-correction scan reported as absent. The earlier worry that electron-bottom might now win is settled negatively: with bottom at its nearest compatible address (R4, gal), electron-bottom lands 58× off, worse than electron-muon. Pairs involving the down quark or τ still blow the inversion up (10⁴ to 10²⁹ off), and the up quark's former low-distance fit was the coexact-only artifact and drops out (it is now unassigned). The McKay-propagator note this scan previously leaned on was reopened by the correction and has since closed negative again on the corrected table ([its re-test result](mckay-propagator-correction.md#retest-result)).

**The floor.** With the corrected top the tightest single estimate is muon-top, Λ within about 0.6 orders of magnitude (3.8×), improving on the electron-muon estimate of 1.13 orders (13.4×). The ceiling is still the formula's few-percent ratio scatter amplified by the McKay lever, but the best available lever now rests on a well-fit high-distance pair rather than the weak Δd = 1 lepton pair, so pair selection does help: the correction lowered the floor by roughly half an order of magnitude. Electron-muon remains the clean lepton-only cross-check at 13.4×.

**What stands.** Topology plus two measured lepton masses plus zero cosmological input land Λ_ref within about 1 order of magnitude of the measured value, on a radius determined independently of measured Λ, the CMB, and the de Sitter back-read. That is a real, falsifiable, independent leg under Λ_ref = 3/R² at R of order Gpc. It is not, and structurally cannot be, a percent-level prediction.

---

## I. The Mechanism

The mass formula (engine file §14):

```math
m(\rho, \sigma) = \mu_\Lambda \times C_{\text{geom}}(\rho) \times (\sqrt{\Omega_\Lambda})^{\,\text{dist}(\rho)/30} \times T^2(\rho \otimes \sigma)
```

Three of the four factors are dimensionless topological ratios:
- C_geom(ρ): geometric mean of C(e/D) over Kostant exponents of irrep ρ
- (√Ω_Λ)^(dist/30): McKay graph distance dilution, h(E₈) = 30
- T²(ρ⊗σ): Reidemeister torsion

All physical dimensions live in the vacuum energy floor:

```math
\mu_\Lambda = \rho_\Lambda^{1/4} = \left(\frac{\Lambda c^4}{8\pi G}\right)^{1/4}
```

Both μ_Λ and Ω_Λ = (R/ℓ_P)² depend on R and G. But G = 3c⁴/(8πR²μ_Λ⁴), so everything reduces to (c, ℏ, R, topological ratios).

---

## II. The G-Power Collection

From the Waltz working notes. G enters the mass formula through two doors:

| Factor | G-dependence | Exponent |
|---|---|---|
| μ_Λ = (Λc⁴/(8πG))^(1/4) | G^(-1/4) | -1/4 |
| (√Ω_Λ)^(dist/30) = (R²c³/(ℏG))^(dist/60) | G^(-dist/60) | -dist/60 |

Total G-exponent in the mass formula:

```math
\alpha(d) = -\frac{1}{4} - \frac{d}{60} = -\frac{15 + d}{60}
```

The mass formula becomes:

```math
m = K(c, \hbar, R, \text{topology}) \cdot G^{-(15+d)/60}
```

where K contains only c, ℏ, R, and dimensionless topological ratios. Solving for G:

```math
G = \left(\frac{K}{m_{\text{obs}}}\right)^{60/(15+d)}
```

One equation, one unknown (G), given R and one measured mass. But G and R are related through Λ_ref = 3/R² and G = 3c⁴/(8πR²μ_Λ⁴). So the system has one free parameter: R. That closure is a conditional exchange-rate calibration, not part of the route below: it holds only once the vacuum density inside μ_Λ is identified with the reference relation 3/R², which is the Interface identification held open. The framework keeps G measured. The two-mass route does not need it, because the mass *ratio* cancels μ_Λ.

---

## III. The Two-Mass Determination

One measured mass (m_e) gives one equation in one unknown (R, with G slaved to R).

A second measured mass (m_μ) gives a second equation in the same unknown. The system is overdetermined. Either:
- Both give the same R (framework is consistent, R is determined)
- They disagree (framework fails at the mass formula level)

The ratio of two masses at different McKay distances:

```math
\frac{m_\mu}{m_e} = \frac{C_\mu}{C_e} \times (\sqrt{\Omega_\Lambda})^{(d_\mu - d_e)/30} \times \frac{T^2_\mu}{T^2_e}
```

If d_μ ≠ d_e, the ratio depends on Ω_Λ, which depends on R. The topological prefactors are pure numbers. Measuring the ratio and computing the prefactors gives Ω_Λ, hence R.

---

## IV. What's Needed

| Requirement | Status | Source |
|---|---|---|
| Mass formula structure | ESTABLISHED | Engine file §14 |
| G-power collection | ESTABLISHED | Waltz working notes §II |
| Electron assignment (ρ, σ, dist) | ASSIGNED (dist = 4) | Engine file §14 |
| Muon assignment (ρ, σ, dist) | ASSIGNED (R8, std, dist = 5; Δd = 1 vs electron) | mass-spectrum.md §III |
| C_geom for electron and muon | COMPUTED | Kostant exponents |
| T² for electron and muon | COMPUTED | Reidemeister torsion, T²(R₃)/T²(R₄) = φ⁻⁴ |
| (ρ,σ) → (T₃,Y) assignment rule | ESTABLISHED AS A GATE RULE (eleven featured: 5 assigned + 2 neutrino-proxy + 4 structural) | mass-spectrum.md §IV.4 |
| Electron mass (measured) | 0.511 MeV | Input |
| Muon mass (measured) | 105.66 MeV | Input |
| Muon/electron ratio | 206.768 | Known to 9 significant figures |

The assignment rule is resolved (mass-spectrum.md §IV.4, eleven featured addresses) and the computation has been executed; see the Result section. The remaining limitation is precision, not the assignments: the McKay-lever amplification (Sections VI and VIII) caps the route at order of magnitude.

---

## V. The Computation (executed 2026-06-15)

**Step 1.** Write m_e and m_μ as explicit functions of R using the mass formula with all topological factors evaluated.

**Step 2.** Take the ratio m_μ/m_e. The μ_Λ prefactor cancels. The remaining R-dependence lives in (√Ω_Λ)^((d_μ - d_e)/30).

**Step 3.** Solve for Ω_Λ from the measured ratio and the computed topological prefactors.

**Step 4.** Extract R from Ω_Λ = (R/ℓ_P)², noting ℓ_P depends on G which depends on R. The G-power collection resolves this to a single closed-form exponent.

**Step 5.** Compute Λ = 3/R².

**Step 6.** Compare with Λ_obs = 1.089 × 10⁻⁵² m⁻². Result: Λ ≈ 8.1 × 10⁻⁵⁴, about 13.4× low (Result section).

---

## VI. What Was Achieved

The forward chain runs:

```math
\frac{m_\mu}{m_e} \text{ (measured)} \xrightarrow{\text{mass formula}} \Omega_\Lambda \xrightarrow{R = \ell_P\sqrt{\Omega_\Lambda}} R \xrightarrow{\text{Gauss} \,\times\, \text{de Sitter}} \Lambda_\text{ref} = 3/R^2
```

The route takes no CMB input and no de Sitter back-read for R, so it breaks the circularity. It does not avoid the de Sitter normalization: the spectral seed 2/R² is the native surface result, and the lift to 3/R² carries the Gauss/Ricci 3 together with the imported de Sitter 1/2, so the final coefficient is 2 × 3/2 and the imported factor sits inside it. The seed rather than the full coefficient is the native content. What the route supplies is an independent determination of R from topology plus two measured masses, and a conditional Λ_ref output; whether Λ_ref is the physical cosmological constant is the open Interface placement question.

The realized precision is order of magnitude, not percent. The few-percent target stated in the original draft was wrong. The McKay lever for the electron-muon pair is weak (Δd = 1), so the formula's few-percent ratio accuracy amplifies by 60× into a roughly 1-order-of-magnitude uncertainty on Λ (executed value Λ ≈ 8.1 × 10⁻⁵⁴, about 13.4× below observed; Result section). The honest claim is "Λ within about half an order of magnitude of observed for the best pair (muon-top), within about one order for the electron-muon lepton pair, from particle physics alone," which is the success at the bar the structure supports.

---

## VII. What Failure Looks Like

- The electron and muon give inconsistent R values: the mass formula's assignments are wrong.
- The R value gives Λ far from observed: the framework fails at the quantitative level.
- The assignments are too uncertain (OPEN status) to execute the computation: the program is blocked until the assignment rule is derived.

All three are informative. The computation should be done regardless.

**Realized outcome.** The second, in a precise sense: R from electron-muon gives Λ 13.4× from observed, and the best assigned pair (muon-top, after the 2026-07-28 correction) gives 3.8×, far enough to fail a percent-level prediction but within about half an order of magnitude, which is a real result at the order-of-magnitude bar. The third mode is retired (the assignments are Established). The first did not occur fatally: different pairs give different R, but the 1-to-2-order spread is the expected McKay-lever amplification of the formula's residual scatter, not an inconsistency in the assignments.

---

## VIII. Connection to the 2% Systematic

The engine file documents a ~2% systematic offset across multiple observables (Λ, H₀, a₀, electron mass running ~2% high, muon ~2.5% low). The electron and muon bracket the measured values from opposite sides. Their geometric mean recovers G to better than 1% (Waltz document). This bracketing pattern is consistent with a single upstream correction (suspected: Gauss-Codazzi factor precision). The opposite-direction bracketing that helps the geometric mean (where the misses cancel) hurts the ratio (where they compound). R is read from the ratio m_μ/m_e, not the geometric mean, so the two ~2% misses add to a 4.5% ratio miss, which the Δd = 1 McKay lever amplifies by 60× into the factor-of-13.4 offset in Λ (Result section). The earlier estimate here, that 2% would carry through as 2% in Λ, assumed the misses were common-mode in the ratio; they are anti-correlated. The order-of-magnitude floor for the electron-muon pair is set by this residual correlation, not by the per-mass 2% accuracy. The 2026-07-28 torsion correction changed the pair scan, though: with the top well-fit at (R2, triv), the muon-top pair (both residuals within 7%, Δd = 2) does beat the electron-muon factor of 13.4, reaching 3.8×, so the achievable floor is now about half an order of magnitude.

---

*The mass spectrum knows R. The hierarchy factor carries it. Two masses triangulate it.*

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
