<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The R Problem

**Type:** Map
**State:** Active
**Status (2026-09-17):** One best-conditioned determination of R, from the coupling route (R ≈ 6.1 Gpc, Λ_ref ~23% low), and an independent but much coarser cross-check from the mass spectrum (R ≈ 10.5-20 Gpc). The displaced values are compatible in magnitude with the mass route's known conditioning, but their origin is unresolved. Whether Λ_ref is the physical Λ is the Interface question. R is also not the only thing between the Molien gap and the sky: the spatial projection is a second, separate missing object.
**Summary:** The map of every route to an independent curvature radius R and where each stands; it surveys the routes and delegates the mass-route detail without owning it.

One best-conditioned determination, and one independent cross-check at lower resolution. The coupling (α) route pins Ω_Λ, hence R ≈ 6.1 Gpc, returning Λ_ref as a conditional output about 23% below the measured value; the mass-spectrum route spans R ≈ 10.5 to 20 Gpc depending on the assigned pair read. The mass route's displaced values are not resolved evidence either of a conflicting radius or of agreement: its inversion amplifies a few-percent mass-ratio residual by roughly the observed factor in Λ. That makes conditioning a quantitative candidate explanation for the split, not a verdict; the present machinery does not distinguish approximation error from structural mismatch. Whether the reference coefficient is the physical Λ remains the Interface question. This note tracks every route to an independent curvature radius R and where each stands; it sits above the detail in [r-from-mass-spectrum.md](r-from-mass-spectrum.md).

**Related:** [R from the mass spectrum](r-from-mass-spectrum.md), [Calibration Structure](calibration-structure.md), [Scaling Law Uniqueness](scaling-law-uniqueness.md).

---

## The goal

The spectral seed Λ_top = 2/R² is the surface result. The Gauss lift and the imported de Sitter vacuum normalization carry it to the reference value Λ_ref = 3/R². The seed is the content, not the coefficient, and whether that reference coefficient is the physical Λ of a static domain is open ([cosmological constant](../../../../cosmos/files/cosmological-constant.md) §IV). But it produces a number only with an independent R. Any route that reads R off Λ, or off a CMB scale that itself needs R, is circular, non-independent, or excluded. An R fixed from somewhere else turns Λ_ref from a tautology into a conditional output that can be checked against the measured value. That is the R problem.

## The routes

| Route | Chain | Verdict |
|---|---|---|
| de Sitter | R = √(3/Λ) | **Circular.** Reads R off Λ, feeds Λ back. |
| Molien gap (CMB) | low-ℓ feature → R ≈ 5.3 Gpc | **Not independent.** The old "sin-fold moves the first peak to ℓ ≈ 42, so R = 5.3 Gpc is excluded" was a coordinate error: the operative cosmology is flat FLRW and CMB-consistent. But the Molien gap still does not *determine* R on its own. |
| L-ratio (CMB) | ℓ_cut → L_fund → ×8 → L_strip = πR → R | **Dead.** The factor of 8 has no topological derivation: three clean kills, and the geometry gives W = πR/2, not the W = R/4 the 8 would require. |
| Coupling (α) | measured α → Ω_Λ → R ≈ 6.1 Gpc | **Live, best-conditioned.** α matched to ~0.44%, lever-amplified to Λ_ref at 23% below measured; the radius determination is independent of Λ, CMB, and the de Sitter back-read. |
| Particle mass spectrum | m_e, m_μ → R ≈ 20 Gpc (lepton-only cross-check); the corrected assigned-pair scan gives a tighter muon-top estimate, R ≈ 10.5 Gpc | **Cross-check, executed.** Order of magnitude, and not a single value at present precision. See [r-from-mass-spectrum.md](r-from-mass-spectrum.md). |

## The live routes

The coupling route inverts the fine-structure formula's Ω_Λ dependence: measured α fixes Ω_Λ, hence R ≈ 6.1 Gpc, and returns Λ_ref = 3/R² about 23% below the measured value. Against the canonical electron-muon cross-check both routes carry a 60-fold inversion, and the α route begins from the far smaller residual, so it is the better conditioned of the two; the tighter muon-top mass read uses Δd = 2, which halves its inversion to 30-fold. The radius determination is independent of measured Λ, the CMB, and the de Sitter back-read; converting that radius to Λ_ref then uses the Gauss/de Sitter reference relation, so the conversion is not independent of it.

The mass-spectrum route inverts the fermion mass formula's Ω_Λ dependence: electron and muon give R ≈ 20 Gpc and Λ_ref ≈ 8.1 × 10⁻⁵⁴ m⁻², about 13.4× (one order of magnitude) below measured. That lepton-only pair is the framework's canonical cross-check, but it is not the sector's tightest reading: on the corrected torsion table the muon-top pair lands within about 3.8×, an R near 10.5 Gpc, so the mass sector does not furnish a single R at its present precision. The radius determination is independent of measured Λ, the CMB, and the de Sitter back-read, so it genuinely breaks the circularity. The precision is capped by the McKay-lever amplification acting on the mass formula's current few-percent residual scatter, but pair choice matters through Δd: electron-muon carries Δd = 1 and a 60-fold inversion, while the corrected muon-top pair carries Δd = 2 and a 30-fold one, which is what makes it the tightest assigned-pair estimate. Full computation in [r-from-mass-spectrum.md](r-from-mass-spectrum.md).

## The shared engine

The L-ratio and the mass spectrum are not two problems. The candidate value of the factor of 8 is rank(E₈) = φ(30) = 8 (the eight integers coprime to the Coxeter number h(E₈) = 30, which are the Kostant exponents), and those same exponents and that same 30 drive C_geom and the dist/30 lever in the mass formula. So the L ratio and the mass-spectrum R are one problem at two scales, both projections of the 2I / E₈ representation ring scaled by R. If the factor of 8 is ever derived, it comes from the same structure the live route already uses.

## What survives from the L work, on its own

One piece of the L investigation stands independently of the dead factor of 8: the **Molien sparse-zone** explanation of the CMB low-ℓ deficit. Icosahedral filtering removes ~80% of scalar modes on S³/2I below N ≈ 10 (ℓ ≈ 28), with the surviving generators at degrees 12, 20, 30 (the Klein invariants; 30 = h(E₈) again), producing a gradual power deficit in the observed range. This is a cosmos-side CMB result, not a route to R, and it now has the home it was owed: [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §IV carries it, over [The Molien Shells](molien-shells.md). It uses the flat projection ℓ ≈ √(N(N+2))·χ\*/R − 1/2, the same estimate that page states, so it is consistent with the corrected flat-FLRW cosmology. The index here is the polynomial degree N, written j in an earlier draft; it is not the spin label of the even-spin descent, which is N/2.

## Where it stands

The coupling route is the best-conditioned determination; the mass route is an independent, lower-resolution cross-check. Their displacement is of the size the mass inversion's conditioning can produce, but that is not resolved evidence either of a conflicting radius or of agreement: the present machinery cannot distinguish conditioning from structural inconsistency. The coupling (α) route puts R near 6.1 Gpc; the canonical electron-muon mass pair puts it near 20, a factor of about 3.2 in R and 10.5 in Λ_ref, while the tighter muon-top pair puts it near 10.5 Gpc, about 1.7× in R and 2.9× in Λ_ref. The size of each route-to-measured miss is numerically compatible with the same steep inversion: the coupling formula's 0.44% α residual maps through the 60-power lever to the 23% Λ_ref miss, and the electron-muon pair's 4.5% mass-ratio residual maps to its ~13.4×, since (1.0044)^60 ≈ 1.30 and (1.045)^60 ≈ 14.0 against the 1.30 and 13.4 actually found. The coupling figure is reproduced within its quoted precision; the mass figure is reproduced to about 5% in the factor, a departure from the pure power law or another term in the chain that is not explained here. Neither carries an order-of-magnitude excess, but each is the same relation read in two directions rather than an independent confirmation. Both inversions are steep, and the decisive difference is input quality, 0.44% against 4.5%, which is why the mass route cannot resolve R sharply enough to compete. That arithmetic makes conditioning a candidate explanation, not a verdict. Nothing yet establishes those residuals as coherent systematics rather than a real disagreement between the routes, and the present machinery does not distinguish conditioning from structural inconsistency. One consequence is worth recording symmetrically with the mass route's ceiling: at the present formula residual, improving the experimental precision of α alone cannot remove the ~23% Λ_ref offset, since the 0.44% is the formula's residual and not the datum's, so sharpening this route requires reducing that residual. This is a property of the present calculation, not an intrinsic floor on the route. On the mass side, pair selection has already helped: re-seating the top on the corrected torsion table moved the achievable floor from electron-muon's 13.4× to muon-top's 3.8×, roughly half an order of magnitude, and what caps it there is the residual scatter times the best available lever rather than any further choice of pair. The α route remains the better conditioned of the two because its present formula residual is far smaller. The L ratio remains a downstream consistency check rather than a route; its factor of 8 is dead on geometric grounds (W = πR/2, not R/4), independent of how precisely R is now known.

One further thing belongs on a page that maps what R settles: R fixes the shell wavenumbers. It does not by itself fix where those modes appear on the sky; that takes a spatial projection from the static quotient to fields on flat effective space, which MIT does not derive and whose search through the existing geometry is closed ([The Spatial Carriers](spatial-carriers.md), [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §IV). Closing the split between these two routes would therefore leave the sky landing conditional on an object nobody has yet supplied.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
