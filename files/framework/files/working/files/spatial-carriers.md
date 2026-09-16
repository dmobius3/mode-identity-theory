<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Spatial Carriers

**Type:** Result
**State:** Closed
**Status (2026-09-15):** Complete as a theorem with a classification, checked by one script. Run under a work order frozen before it, this asks what form the missing spatial projection can take rather than whether MIT supplies one. A deterministic linear map from one Molien shell's fields to fields on flat space, whose contribution to the flat field is separately homogeneous, has a finitely atomic spectrum with at most m_N(N+1) atoms, and the bound is attained. P1's uniform angular measure is not atomic, so no such map induces it at finite N. Full rotation equivariance leaves only the zero map at every tested shell. At the tested shells N = 12, 20 and 30, a nonzero A5-equivariant carrier is a single icosahedral orbit, and which orbits a shell admits is decided by representation content, not by counting: at N = 12 none is admissible once locality is imposed, at N = 20 the twelve five-fold directions, at N = 30 those or the twenty three-fold directions. Where a carrier exists it reproduces the ratio table's contribution to that shell's C_ℓ exactly, since the angle-integrated power agrees. Those carriers do not assemble: an object owes every shell its power, so the first shell's obstruction leaves no admissible A5-equivariant lift across the tested shells, and no replacement for the table is produced.
**Summary:** What any deterministic field-level linear lift of a Molien shell to flat space can be under separate shell homogeneity, the representation test that decides which icosahedral spectra a shell admits, and why the shells that admit one still do not assemble into an object.
**Inputs:** `effective-metric-floors.md` §III, §V, `missing-spatial-projection.md` §IV, `stress-tensor-bridge.md` C7-C10, `directional-transfers.md` §II, `radial-transfers.md` §II-III, `molien-p1-bridge.md` §II, §IV, `molien-ratio-table.md`, `scripts/spatial-carriers/carrier_check.py`
**Parent:** `stress-tensor-bridge.md`

---

## I. The question, and the class it is asked in

[The Effective-Metric Floors](effective-metric-floors.md) closed the admissibility question at E0: MIT supplies four floors on the missing spatial projection and nothing that says what it is. This page asks a different question, about form rather than motivation, and a work order frozen before it fixed the class.

> What form must any object satisfying the landed requirements have?

The theorem restricts the candidate to one shell at a time. For a Molien shell $`N`$, let $`V_N`$ be its real fields on the domain, of dimension $`d_N = m_N(N+1)`$: 13 at $`N = 12`$, 21 at $`N = 20`$, 31 at $`N = 30`$. Requirement 2 forbids building the map through the shell decomposition, so what is studied here is the restriction $`F_N = F|_{V_N}`$ of one prospective spatial map, not an independent map per shell:

> $`F_N`$, from $`V_N`$ to fields on $`\mathbb{R}^3`$, deterministic, linear at the field level, continuous, with distribution-valued outputs allowed.

**The level is the content.** [The Missing Spatial Projection](missing-spatial-projection.md) §IV's second requirement fixes the object as a map from fields to fields. This theorem studies the deterministic linear field-level subclass fixed by its frozen work order, and the covariance transfer that subclass induces is what §IV's third requirement, linearity and positivity, scores. The two classification pages work at that covariance level, on the maps from a shell covariance to a flat power, and P1 is defined there. Nothing on this page says what is definable at the covariance level.

**Premises, marked.** Each shell's contribution to the flat field is taken to be separately homogeneous. That is carried over from the landed shellwise classification, not inherited from the source, and every result below is conditional on it. The source covariance is fixed by the domain's homogeneity ([The P1 Bridge](molien-p1-bridge.md) §II). The four floors of the Floors page §III apply, and locality is the one that bites here.

**Escapes, named in advance.** A map whose homogeneity appears only after two or more shells are combined; a covariance-level or stochastic channel, P1 included; failure of separate shell homogeneity; a nonlinear map. Nothing below touches those.

## II. The theorem

**Finite shell, linear field lift, separate stationarity: the spectrum is finitely atomic, with at most $`d_N`$ atoms.**

Write $`u_i = F_N(e_i)`$ on a basis of $`V_N`$. The output covariance is the distribution $`K = \sum_{ij} C_{ij}\, u_i \otimes u_j`$, with $`C`$ the source covariance, so as a quadratic form on test functions it has rank at most $`d_N`$. Stationarity and positive-definiteness give, by Bochner and Schwartz, a positive tempered measure $`\mu`$ with $`K(\varphi, \varphi) = \int |\hat\varphi|^2 d\mu`$. Test functions have dense Fourier image in $`L^2(\mu)`$, so $`\dim L^2(\mu)`$ is at most the rank, hence at most $`d_N`$. A measure whose $`L^2`$ is finite-dimensional is finitely atomic with at most that many atoms, since $`d+1`$ disjoint sets of positive measure would give $`d+1`$ independent indicators. Reality makes $`\mu`$ even, so the support is antipodally closed.

The bound is attained: at $`N = 12`$, six arbitrary axes and the zero mode give thirteen atoms, stationary and of rank exactly 13, while fourteen atoms need rank 14, which a thirteen-dimensional shell cannot supply. That witness shows sharpness only. With a zero atom carrying weight its mean squared wavenumber falls below $`\lambda_N`$, so locality excludes it.

## III. What that does to P1

The uniform angular measure on the sphere of radius $`k_N`$ is not atomic, so no $`F_N`$ at finite $`N`$ induces it. The record measures the same thing as a kernel of rank 30 over 30 sample points, against $`d_N = 13`$.

The ratio table remains the exact result of the frozen P1 prescription, and its numbers stand conditional on P1. What fails is P1's derivation as a deterministic field-level spatial map at finite shell dimension, under the separate-homogeneity premise. [The ratio table](molien-ratio-table.md) is unchanged by this page.

## IV. Full rotation equivariance leaves nothing

If the output is rotation invariant with finite support, the support is a finite union of rotation orbits, and the orbit of any nonzero wave vector is a whole sphere. So the support is the origin, the output is constant, and the image lies in the constants, where rotations act trivially. $`V_N`$ carries $`m_N`$ copies of the spin-$`N/2`$ irreducible of the domain's right action, which has no invariant vector for $`N > 0`$: the record finds invariant dimension 0 at $`N = 12, 20`$ and $`30`$. An equivariant map into a trivial target is zero, so full rotation equivariance leaves $`F_N = 0`$ at every tested shell, and so does declaring that the domain's rotations act trivially on the target.

## V. Under A5: fit is not containment

An $`A_5`$-equivariant carrier puts equal weight on each point of a transitive orbit, so the carrier has full rank on that orbit's module, which forces the module to sit inside the shell. Counting is not enough. The shell content, by character and cross-checked against the commutant, and the orbit modules, computed twice over, as permutation modules on the directions and as the real plane-wave spaces they carry:

| | shell content | orbit of 12 | orbit of 20 | orbit of 30 |
|---|---|---|---|---|
| module | | $`1 + 3a + 3b + 5`$ | $`1 + 3a + 3b + 4^2 + 5`$ | $`1 + 3a + 3b + 4^2 + 5^3`$ |
| $`N = 12`$, $`d = 13`$ | $`1 + 3a + 4 + 5`$ | fits, not contained | does not fit | does not fit |
| $`N = 20`$, $`d = 21`$ | $`1 + 3a + 3b + 4 + 5^2`$ | fits, contained | fits, not contained | does not fit |
| $`N = 30`$, $`d = 31`$ | $`1 + 3a^2 + 3b^2 + 4^2 + 5^2`$ | fits, contained | fits, contained | fits, not contained |

The sharpest disagreement is $`N = 12`$ on the twelve five-fold directions, where the dimension fits exactly, twelve atoms and the zero atom against thirteen, and containment fails because the orbit module needs the second three-dimensional irreducible and the shell has none. Where containment fails the maximal equivariant rank falls short: 9 of 12 at $`N = 12`$, 16 of 20 at $`N = 20`$, 25 of 30 at $`N = 30`$.

**One component per shell.** Each tested shell has one trivial summand, $`m_N = 1`$, and each orbit module has one, carrying the equal-weight vector; a zero atom's image is a further invariant. A nonzero orbit and a zero atom would need two invariants in the shell, and there is one. So a shell's spectrum is one orbit, or the zero atom, never both and never two orbits.

## VI. The carriers, and why they do not assemble

Containment is also sufficient. For each irreducible it lets an equivariant isometry carry the orbit module's copies inside the shell's, and their sum is equivariant with $`F F^{T}`$ proportional to the identity, which on a source covariance proportional to the identity is equal weights and no cross-correlation, that is, stationarity. The record establishes this by construction at each containment case, by polar normalization of a full-rank equivariant map, and verifies equivariance under all 60 rotations.

Tightness fixes the weights and not the scale. Power conservation fixes the scale: the orbit must carry the shell's whole power, which is what an $`A_5`$ declaration owes under C10. In the convention where the source covariance is the identity on an orthonormal basis, so the shell's variance at a point is $`d_N`$, the tight covariance $`F F^{T}`$ is rescaled by $`\gamma = 2 d_N / s`$ for an orbit of $`s`$ directions, which is 3.500 at $`N = 20`$ and 5.167 and 3.100 at $`N = 30`$; equivalently $`F`$ itself is rescaled by $`\sqrt{\gamma}`$. That number is the spectral mass per axis, counting a cosine and a sine together, and the mass per direction is half of it.

What a shell admits is a spectrum, not a unique map: the field-level lifts realizing one carrier need not be unique, since a shell can hold more copies of an irreducible than the orbit needs.

With locality fixing the radius at $`k_N`$:

- **$`N = 12`$: no admissible carrier.** The constant is the only $`A_5`$-equivariant stationary carrier the shell admits, and locality, which asks for mean squared wavenumber $`\lambda_N`$, excludes it.
- **$`N = 20`$: one admissible spectral carrier.** The twelve five-fold directions at $`k_{20}`$, equal weights.
- **$`N = 30`$: two.** The twelve five-fold or the twenty three-fold directions at $`k_{30}`$, equal weights, with nothing in the premises selecting between them.

**What a carrier predicts, shell by shell.** A carrier puts a shell's whole power on one orbit at radius $`k_N`$. Its angular measure is not P1's, which spreads the shell over the sphere, but the angle-integrated power is the same at the same radius, and the expected $`C_\ell`$ reads only that (the Floors page §V). So a shell with a carrier contributes exactly what the ratio table has it contribute, and the two carriers at $`N = 30`$ are indistinguishable in $`C_\ell`$.

**They do not assemble.** An object owes every shell its power, by C10's conservation clause and by locality in its primary form, H2's requirement that the effective field reproduce the correlations near the observer ([The Effective-Metric Floors](effective-metric-floors.md) §III). A map that sends the first Molien shell to zero does neither: that shell's power is not carried, and its correlations are not reproduced. It is that primary form doing the work, not the second-moment condition [the radial page](radial-transfers.md) §III derives from it, which is vacuous on a shell carried to zero for want of a measure to take a moment of.

**One declaration, not one per shell.** The escape this invites is to declare $`A_5`$ where a carrier exists and nothing where none does, giving $`N = 12`$ six arbitrary axes while $`N = 20`$ and $`N = 30`$ take orbits. C10 asks how the domain's isometries act on the flat target's rotations, which is one answer for the map, so a shell-by-shell answer is not a declaration at all. So the carriers at $`N = 20`$ and $`N = 30`$ are shellwise results rather than pieces of an admissible whole, and across the tested shells there is no admissible $`A_5`$-equivariant field-level lift at all. The obstruction sits at a tested shell, so untested shells cannot remove it; they could only add more. No replacement for the ratio table is produced here.

As a counterfactual diagnostic, and not as a prediction: if the first shell were deleted anyway, against locality and shell-power conservation, [The Shell-to-Radius Transfers](radial-transfers.md) §IV prices what would go, below that shell's landing. The first shell's share of $`C_\ell`$ runs from 1.0% at $`\ell = 13`$ to 82% at $`\ell = 22`$ at route A, and from 1.7% at $`\ell = 5`$ to 84% at $`\ell = 7`$ at route B.

Each nonzero shellwise carrier is statistically anisotropic, since twelve or twenty directions are not a sphere, and that is where the two carriers at $`N = 30`$ differ. The shape of the anisotropy is not free: [The P1 Bridge](molien-p1-bridge.md) §II needs only $`A_5`$, so it applies here unchanged and the quadrupole stays isotropic and uncorrelated with the octupole. Nothing further about the anisotropy is computed here.

## VII. What this leaves

C10 now has a test rather than a warning. A candidate that declares the full rotation group has no field-level lift at these shells; one that declares $`A_5`$ can be scored shell by shell, by asking whether the shell contains an orbit module, and at the tested shells that scoring already fails at the first one; and one that declares the domain's rotations act trivially has no lift either. If no rotational equivariance condition is imposed at all, the control branch, nonzero carriers exist but their axes are unconstrained, since six arbitrary antipodal pairs at $`k_N`$ already give a stationary carrier meeting locality; that branch therefore fails C10 as a candidate declaration rather than answering it.

Collecting the sweep: within the field-level class tested here, every declaration that would yield a directional prediction yields no object, and the only branch that yields objects yields no prediction. That is where this line ends, not merely that C10 can now be scored.

The requirement this page holds to, that the object is a map from fields to fields, is the second requirement of [The Missing Spatial Projection](missing-spatial-projection.md) §IV, where the reading and its consequence are recorded. Under it P1 keeps its numbers and loses its claim to be the projection itself, and no admissible $`A_5`$-equivariant field-level lift stands in its place at the shells tested here.

Not computed: the untested shells, $`N = 24`$ and above, whose representation content has not been checked here, though none of them can lift the obstruction at $`N = 12`$; the four escapes named in §I; the anisotropy beyond the quadrupole; and what an object could do at the first shell that a shellwise carrier cannot.

## VIII. Checks

[`carrier_check.py`](scripts/spatial-carriers/carrier_check.py) needs numpy and scipy, and its record [`carrier_check.out`](scripts/spatial-carriers/carrier_check.out) reproduces all nine checks and all nine controls from it. Quantities at the roundoff level print as bounds, so differences in roundoff between machines do not reach the record. It checks $`2I`$ and the real spin representations; each shell's content twice over; each orbit module twice over; the fit and the containment tests; the carriers where they exist, with equivariance and tightness, and the maximal rank where they do not; the scalar power conservation fixes; the absence of an invariant vector; the thirteen-atom sharpness witness with its fourteen-atom control; and the uniform measure's rank. Nine controls come out the other way.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
