<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Molien Shells: The P1 Bridge

**Type:** Result
**State:** Closed
**Status (2026-09-17):** Complete as a geometric derivation, checked by three scripts. The source domain S³/2I is homogeneous with isotropy group A5 at every point. A construction that keeps only the shells' spectrum gives an isotropic law, P1's counterpart; the quotient's own law carries P2's identifications, and no homogeneous flat law can keep them. The flat limit sends both canonical laws to P1, so their fork is localized to the low shells, while from N = 60 a non-scalar source shape can carry an anisotropy to high N. Below N = 60 the symmetry fixes the source's shape, so a Q-symbol flattening would give a definite icosahedral pattern of directional power, up to the shell amplitudes and one orientation. What MIT does not yet supply is a reason its flattening would act that way; a derivation of that map would be recorded on the effective-metric side, such as the Stress-Tensor Bridge, citing this page, rather than by reopening it.
**Summary:** What the Molien-shell source needs from MIT to reach the sky: the symmetry of S³/2I and what it forces on a source and a sky, which constructions shed the quotient's identifications and what each keeps of its A5 anisotropy, and what flattening onto flat slices carries.
**Inputs:** `molien-shells.md`, `molien-step-two.md`, `molien-ratio-table.md`, `stress-tensor-bridge.md`, `postulate-bridge.md`, `friedmann-as-output.md`, `redshift-and-cooling.md`, `entropy-as-realization-budget.md`, `../../../../cosmos/files/cmb-anomalies.md` §III to §VI, `scripts/molien-p1-bridge/isotropy_check.py`, `scripts/molien-p1-bridge/quotient_half_check.py`, `scripts/molien-p1-bridge/flattening_check.py`
**Parent:** `molien-shells.md`

---

## I. The question

[The Molien Shells, Step Two](molien-step-two.md) carried the surviving shells of S³/2I to the sky by an explicit prescription, P1: each shell keeps its wavenumber and its variance, spread isotropically, and nothing else. [The full-transfer ratio table](molien-ratio-table.md) computed what P1 gives at MIT's two radii. P1 was always a prescription, not a consequence of MIT. This page asks what MIT would have to supply for the shells to reach the sky as P1, or as something else, and answers the geometric part of that question.

- **The source domain is homogeneous and anisotropic.** Its isotropy group at every point is the icosahedral rotation group A5, finite rather than SO(3). Symmetry forces the source's covariance shell by shell, and on the sky, under any map that preserves A5, it forces the quadrupole to be isotropic and uncorrelated with the octupole (§II).
- **Three objects, not two.** Between P1 and P2, the quotient taken as the space the photons cross, sits a middle object that keeps the shells' A5 anisotropy but not their identifications (§III).
- **A spectrum alone is isotropic.** A construction that keeps only the levels and multiplicities, and commutes with the isometries, gives an isotropic law, P1's counterpart. Keeping A5 takes orientation data, and on the sphere the laws that keep it form a family the geometry does not choose from (§IV).
- **Flattening.** The flat limit carries a shell law to its coherent-state symbol and sends both canonical laws to P1; no homogeneous flat law keeps the identifications. The canonical fork between flattenings is localized to the low shells, while a source shape that is open from N = 60 can carry an anisotropy to high N (§V).
- **What remains.** On the shells below N = 60, a Q-symbol flattening would turn the symmetry-fixed source into a definite icosahedral pattern of directional power. Whether MIT's flattening acts that way is the one missing statement (§VI).

## II. The symmetry of the source domain

Take S³ = SU(2) as the unit quaternions, with 2I acting on the left, so that a point of M = S³/2I is a coset [x] = 2I·x.

1. **Homogeneous.** Right multiplication, R_b: [x] ↦ [xb], is well defined on cosets, since 2I(xb) = (2I·x)b, and transitive, since R_{x⁻¹} takes [x] to [1]. It supplies a transitive copy of SU(2)/{±1} ≅ SO(3) inside M's isometry group. With two imported facts, the chirality theorem of [CMB Anomalies](../../../../cosmos/files/cmb-anomalies.md) §III (no orientation-reversing isometry) and the standard fact that 2I is its own normalizer in SU(2), it is the whole isometry group. Nothing below uses that last step: the Schur arguments need only the transitive right action and its stabilizer.
2. **Isotropy group A5 at every point.** R_b fixes [1] exactly when b ∈ 2I, and −1 acts trivially. For b ∈ 2I and a tangent vector v at [1], the representative of [exp(v) b] nearest 1 is b⁻¹ exp(v) b = exp(Ad(b⁻¹)v), so b rotates the tangent space by Ad(b⁻¹). The image of 2I in SO(3) is the icosahedral rotation group A5, 60 rotations, and by homogeneity every point carries a conjugate copy.

The same result follows from a second presentation. Since −1 ∈ 2I, M = (S³/{±1})/(2I/{±1}) = A5\SO(3), on which right multiplication by SO(3) is transitive with stabilizer A5 at the identity coset. The volumes agree: 2π²/120 from the unit S³ and π²/60 from SO(3), whose volume is π².

**What symmetry forces on the source.** Each shell is H_N^{2I} ≅ (Sym^N)^{2I} ⊗ Sym^N, the second factor irreducible under the right SU(2) and inequivalent for different N. So a Gaussian covariance invariant under M's isometries is, by Schur,

    ⟨a_{Nαm} a*_{N′βm′}⟩ = δ_{NN′} Σ^(N)_{αβ} δ_{mm′},

with Σ^(N) a positive m_N × m_N matrix on the multiplicity space (Sym^N)^{2I}. Below N = 60, m_N ≤ 1 and Σ^(N) is one number, P_N: equal power across a shell's N + 1 states is forced, not chosen. At N = 60, where m_N = 2 for the first time, Σ^(N) becomes a matrix that symmetry leaves open.

**What symmetry forces on the sky.** Suppose the map from source to sky respects the observer's A5, as a map built from the quotient's own structure would. Then the sky covariance commutes with A5 on every spin-ℓ space, and Schur applies again: a spin whose A5 content is a single irreducible has an isotropic covariance, and two spins can be correlated only through a constituent they share.

| ℓ | A5 content | covariance |
|---|---|---|
| 1 | 3 | forced isotropic |
| 2 | 5 | forced isotropic |
| 3 | 3′ + 4 | anisotropy allowed |
| 4 | 4 + 5 | anisotropy allowed |
| 5 | 3 + 3′ + 5 | anisotropy allowed |
| 6 | 1 + 3 + 4 + 5 | anisotropy allowed |

Between spins the covariance is forced to zero for (1, 2), (1, 3), (1, 4) and (2, 3), and allowed for every other pair up to ℓ = 6. The number of A5 invariants at spin ℓ equals the Molien count m_{2ℓ}, which ties the table to [step one](molien-shells.md).

**A corollary, conditional on that supposition.** For a Gaussian source carried to the sky by a map that preserves the observer's A5, the quadrupole is statistically isotropic and uncorrelated with the octupole, and therefore independent of it; an isotropic quadrupole independent of the octupole leaves their relative orientation uniform. So such a source produces no quadrupole-octupole alignment beyond what full isotropy gives. A non-Gaussian source, or a map that breaks the observer's A5, is not covered. The corollary says nothing about parity: A5 contains no inversion, and the per-ℓ variances are left free.

[`isotropy_check.py`](scripts/molien-p1-bridge/isotropy_check.py) checks the group steps: 2I as 120 unit quaternions closed under multiplication; right multiplication well defined and transitive; the stabilizer of [1] equal to 2I; the tangent action equal to Ad(b⁻¹) to 2 × 10⁻¹⁶; the 60 rotations permuting the icosahedron's 12 vertices, in rotation-angle classes 0, 2π/5, 4π/5, 2π/3 and π of sizes 1, 12, 12, 20 and 15; the A5 content of each spin and which pairs may couple; and the invariant counts against m_{2ℓ} for ℓ up to 40. It does not check the two imported facts.

## III. Three objects, and where the map is missing

| | spectral selection | A5 anisotropy from ℓ = 3 | identifications, hence matched circles |
|---|---|---|---|
| P1 | kept | dropped | dropped |
| the middle object | kept | kept | dropped |
| P2 | kept | kept | kept |

**P2** takes the source domain to be the space the photons cross. At MIT's radii its inscribed radius, πR/10, is 1.9 to 6.3 Gpc, under half of χ*, so it gives matched circles: the known miss recorded on [Step Two](molien-step-two.md). **The middle object** is a statistically homogeneous effective field in flat space whose covariance keeps the quotient's spectral selection and its A5 symmetry, but not its identifications. Circles come from a field being periodic under the holonomy, which a covariance constraint does not impose. **P1** drops the A5 anisotropy as well. All three agree at ℓ ≤ 2 on isotropy and on the absence of a (2, 3) coupling. P1 and the middle object first differ at ℓ = 3, and then only in how each multipole's power is spread over m: with the same angle-averaged shell weights their power per multipole is the same (§VII).

The pages that translate MIT's static S³ into an effective cosmology do not contain the map these objects need. [The Half-Power Clock](friedmann-as-output.md) and [Redshift and Cooling](redshift-and-cooling.md) are a time-sector dictionary: S plays the role of a scale factor for redshift, temperature and distance, and nothing says how points, modes or fields of S³/2I correspond to those of a flat effective space. [The Postulate Bridge](postulate-bridge.md)'s sampler maps a surface into the quotient and samples the 2I-periodic field through its lift, so it carries the identifications rather than shedding them. [The Stress-Tensor Bridge](stress-tensor-bridge.md) names the background version of the missing map as open: if the effective slices are flat, the map from the static metric "must contain a genuine projection or coarse-graining that explains flat effective slices over a closed substrate".

So the map from source to sky has two parts. Shedding the identifications is quotient-specific: S³/2I and S³ are locally the same, with the same curvature, so the quotient is visible only in the fluctuations (§IV). Flattening S³ at radius R onto flat slices is shared with the Stress-Tensor Bridge (§V).

## IV. Shedding the identifications

Work on the covering sphere S³ at radius R, with the observer at the point 1 and the right action of SU(2) as the homogeneity that descends to the quotient. Shell N of the sphere is spanned by the matrix coefficients of Sym^N, whose character is the Chebyshev polynomial U_N(Re g). A Gaussian law on the shell that is homogeneous under the right action has covariance K_A(x, y) = Tr(A ρ_N(x y⁻¹)), with A a positive operator on Sym^N, by Schur. Below N = 60, where symmetry forces its covariance to be one number, the quotient's own shell is, up to P_N, A = Π_N, the projector onto the 2I-invariants, Π_N = (1/120) Σ_g ρ_N(g); from N = 60 its shape is open (§V). Written out,

    K_Π(x, y) = (1/120) Σ_g U_N((g x)·y),

a sum of the isotropic shell kernel centred on the 120 images of x, where (g x)·y is the four-dimensional dot product.

**One sum, three readings.** Everything §III's three objects sort is a reading of this sum.

1. At coincident points it is the selection: K_Π(x, x) = m_N. The central pair ±1 contributes (N + 1)/60 at every even N, and the 118 other images supply the rest. At every empty even shell up to N = 18 they cancel the central pair exactly, and at N = 12 they add 0.7833 to its 0.2167. The spectral selection is interference among the images.
2. Near the observer it is the A5 anisotropy: the central terms are isotropic, and all of the direction dependence comes from the other images, in the A5-invariant degrees only (6, 10, 12, 16, …).
3. At the images it is the identifications: K_Π(x, g x) = m_N = K_Π(x, x) for all 120 elements g, so f(g x) = f(x).

So nothing that uses the quotient's shell as it is can keep one reading and drop another. The pullbacks, through the cover or through the exponential map at the observer, carry K_Π itself and keep all three.

**The spectrum alone is isotropic.** Suppose a construction takes the deck group to a law, commutes with the isometries, and uses only the levels N and the multiplicities m_N. A conjugate h 2I h⁻¹ has the same spectrum as 2I, so the construction gives it the same law, which is also the rotation of 2I's law by h. So the law is invariant under every rotation about the observer, whatever the construction's target. On the sphere the canonical such law is the whole shell, A = (m_N/(N + 1))·I, with the quotient's variance m_N at each point and a total of m_N(N + 1) over the shell, the factor P1's shell weights carry. Averaging P2's law over the observer's orientation gives the same covariance, by Schur, but it is a mixture whose realizations stay periodic under rotated copies of 2I, so it keeps the identifications and is not Gaussian.

**A5 needs orientation data, and on the sphere it comes as a family.** A law keeps the observer's A5 when A commutes with ρ_N(2I). These laws form the commutant, whose dimension is the number of A5-invariant harmonics of degree at most N: 4, 8, 11 and 17 at N = 12, 20, 24 and 30. For a real field the count is that of the even-degree ones. A law's correlation between a point and its image under g is Tr(A ρ_N(g⁻¹))/Tr A, the same at every point, and an isotropic law gives U_N(Re g)/(N + 1), the baseline. The image correlations depend on A only through its traces on the isotypic components: they are the average of the normalized characters χ_ρ(g)/d_ρ weighted by those traces, and at the nearest images they span −1/4 to 1. Hence:

- all the weight on the invariants makes the law periodic, which is P2;
- equal weights put every image correlation on the baseline, and since the constituents' characters are independent on 2I, no other weighting does;
- every other law in the family is neither periodic nor on the baseline.

The laws in the commutant's center are the character-weighted image sums (1/120) Σ_g w(g) U_N((g x)·y), and each is anisotropic exactly when it departs from the baseline at some image. At N = 20 the law on every sector except the invariants puts correlation 0 at the nearest images, where the baseline is 0.048. Outside the center, where a constituent repeats, parts acting on its multiplicity space with trace zero add A5 anisotropy with no change to any image correlation. Among the Molien shells that happens from N = 20 on and never at N = 12, whose Sym^12 is 1 + 3 + 4 + 5; the five irreducibles of A5 have dimensions summing to 16, so a constituent repeats at every even N from 16.

So on the sphere, laws with the selection, the observer's A5 and no periodicity exist on every Molien shell from N = 12, and those with every image correlation on the baseline need a repeated constituent. The geometry fixes the family, not the member. Near and far are also tied: a shell's kernel K_A(1, z) is a polynomial on S³, so its behaviour near the observer fixes it everywhere, the image correlations included.

[`quotient_half_check.py`](scripts/molien-p1-bridge/quotient_half_check.py) checks these statements: the Molien counts as character averages, split between the central pair and the other images; the image sum's invariance and its values at coincident points and images, to 2 × 10⁻¹⁴; the near field's A5-invariant degrees; the commutant's dimension, by rank and by harmonic count; the center's theorem, against 100 random weightings; the non-central laws at N = 20, 24 and 30; and the image correlations as weighted averages of normalized characters, with the nearest-image range from −1/4 to 1. Its record writes Π as P.

## V. Flattening

Two covariances have to be kept apart. The source's is Σ^(N) on (Sym^N)^{2I}. Writing Σ^(N) = P_N Σ̂^(N) with Tr Σ̂^(N) = m_N makes P_N the amplitude at every N and Σ̂^(N) the shape, which is 1 below N = 60. Coherent states live on the whole of Sym^N, so the source is embedded there: with ι_N the inclusion of the invariants into Sym^N, Σ̃_N = ι_N Σ^(N) ι_N† and Π_N = ι_N ι_N†. Below N = 60 the source is Σ̃_N = P_N Π_N = P_N |ψ_N⟩⟨ψ_N|, with ψ_N the shell's unique invariant. The effective shell's covariance is A_N^eff, its directional covariance once the identifications are shed.

| map | spectral support | A5 | periodicity, image correlations | homogeneous | positive | source to A_N^eff |
|---|---|---|---|---|---|---|
| pullback by the exponential map at the observer | not a flat shell | kept | kept, at the image vectors | no | yes | carries the whole source law |
| any homogeneous flat law with the identifications | none exists | | | | | |
| flat limit, N → ∞ at fixed k_N r | a shell at k_N | through the symbol | dropped: the images recede | yes | yes | to its symbol, for regular families, in the limit |
| spectral transfer at every N (P1's prescription) | a shell at k_N | dropped | dropped | yes | yes | the trace alone |
| symbol transfer at every N | a shell at k_N | kept, through the symbol | dropped | yes | yes, with the Q-symbol | to its Q-symbol |
| spectral filters on the sphere (heat kernel, smoothing) | reweights the shells | unchanged | unchanged | on the sphere only | yes | none: it acts on traces |

Here k_N = √(N(N+2))/R, as in the ratio table, and r is the separation.

**The flat limit carries a regular family to its symbol.** With spin coherent states |m⟩ on the factor 2I acts on, ⟨m|ρ_N(z)|m⟩ = ⟨m|U_z|m⟩^N, with U_z the 2 × 2 matrix of z. At a displacement of c/k_N in a direction w, taken in the Bloch frame,

    ⟨m|U|m⟩^N = (cos(c/k_N) − i sin(c/k_N) w·m)^N → exp(−i c w·m).

So for a coherent-state family A = ∫ f(m)|m⟩⟨m| dm, with f fixed as N grows, the correlation tends to the flat shell kernel ∫ f(m) exp(−i c w·m) dm / ∫ f(m) dm, and the Bloch sphere of the factor 2I acts on becomes the sphere of local wave-vector directions. The same holds, with f the limit of the symbol, for families regular in N; an arbitrary sequence need not have such a limit. By Bochner's theorem the flat kernel is a covariance exactly when its weight is nonnegative. [`flattening_check.py`](scripts/molien-p1-bridge/flattening_check.py) shows, at c = 6:

- the whole-shell law meets the flat shell kernel j0(c) to 2.7 × 10⁻³ at N = 12 and 3.1 × 10⁻⁷ at N = 1200;
- a law with a smooth anisotropic A5 symbol meets the flat kernel of its symbol to 6.2 × 10⁻⁴ at N = 1200, and keeps its anisotropy;
- the invariant-projector law Π_N loses its anisotropy near the observer, from 0.18 of the variance at N = 12 to 1.5 × 10⁻³ at N = 1200, about 2/N: the central pair contributes two terms of order N, each of the other 118 images a term of order one;
- Π_N's symbol, Q_Π(m) = (1/120) Σ_g ⟨m|U_g|m⟩^N, has mean m_N/(N + 1), and at N = 600 and 1200, both multiples of 60, it equals k/60 on each k-fold axis to within 0.1%: uniform apart from spikes on the 62 axis directions, whose low-degree content falls like 2/N;
- a source with a non-scalar shape can keep its anisotropy: a rank-two shape, onto the invariant parts of the coherent states at a generic direction and at its antipode, holds an rms of 6.2 × 10⁻² at N = 1200, tending to the flat kernel of its orbit's measure, while Π_N's falls to 1.6 × 10⁻³ on the same directions.

**No homogeneous flat law keeps the identifications.** Suppose a homogeneous flat law correlated f(x) and f(x + u) perfectly for each image vector u, the displacement at which the pullback puts a point's image. Then f(x + u) = f(x) for every u in the group those vectors generate. That group contains the Z-span of the 12 nearest-image vectors, which point along the icosahedron's vertex directions and span a module of rank 6, so it is not discrete, and its closure contains a nonzero A5-invariant subspace, which is all of R³ because A5 acts irreducibly. A field with a continuous covariance that is periodic under a dense group of translations is constant. So P2 has no homogeneous realization on flat slices: the pullback realizes it inhomogeneously, and the conventional Poincaré space realizes it on curved slices.

**Where the fork lives.** For the canonical laws the three flattenings, spectral, symbol and pullback, agree with each other and with P1 in the flat limit, and part on the low shells. At N = 12, Π_N's kernel on the sphere and its symbol transfer differ by up to 0.35 at c = 6, a separation of 0.46R, short of the nearest images at 0.63R; at N = 1200 they agree to 6.8 × 10⁻⁵. The difference comes from the other images' terms, since the central pair's part is flat to 2.7 × 10⁻³. The full covariance fork need not be confined to the low shells. From N = 60 a non-scalar shape can retain a directional structure through the flat limit, which the pullback and the symbol transfer carry and the spectral transfer discards, at every N; a shape whose anisotropy moves to ever finer angles as N grows need not. What is localized is the finite-curvature ambiguity of flattening, not an anisotropy in the source.

Every shell that lands inside the ratio table's band, ℓ = 2 to 29, has a unique invariant, so its shape is forced. With the ratio table's recorded χ* = 13,860 Mpc, at B (R = 19700 Mpc) those are the shells from N = 12 to 40; at A (R = 6130 Mpc) the first shell, N = 12, lands at k_N χ* = 29.3, the band's top edge, and every other shell lands above it. The first shell with an open shape, N = 60, lands at k_N χ* = 42.9 at B and 137.9 at A. Shells also feed the multipoles below where they land, and the ratio table's record gives only the first shell's share, so how much of the band's power comes from N ≥ 60 is not recorded here.

The Stress-Tensor Bridge meets the same boundary from the background side. The flat limit supplies local flatness at separations far below R for free, as it would over any closed substrate; flat effective slices at separations comparable to R, which the flat fitted dictionary needs, are what its projection or coarse-graining has to supply. Neither program has a flattening at that scale.

## VI. What remains

**The symbol transfer.** Carry each shell's source to a flat shell at k_N whose power over directions is the Q-symbol of the embedded source covariance, A_N^eff(k̂) = ⟨k̂|Σ̃_N|k̂⟩, at every N rather than only in the limit.

- **It yields a covariance.** ⟨m|A|m⟩ ≥ 0 for positive A, so the flat weight is nonnegative, which Bochner requires. The other standard symbols do not guarantee it. A nonnegative Glauber–Sudarshan symbol, the weight f in A = ∫ f(m)|m⟩⟨m| dm, would write a state as a mixture of coherent states, which a pure state other than a coherent one cannot be; and for spin 1/2 already, the Stratonovich–Weyl symbol of a pure state is negative opposite its Bloch vector. Among the standard symbols considered here positivity singles out Q, but it does not derive Q, since other positive covariant transforms can be built. The transfer is homogeneous, has no images, and on regular families agrees with the flat limit as N grows.
- **On the whole-shell law it gives P1.**
- **Below N = 60 it gives a definite pattern.** There A_N^eff(k̂) = P_N |⟨k̂|ψ_N⟩|²: the dynamical amplitude times a pattern the symmetry fixes. The pattern's zeros are exactly ψ_N's Majorana constellation, the roots of the invariant form f12^a f20^b f30^c: the 12 vertex directions when a > 0, the 20 face centres when b > 0 and the 30 edge midpoints when c > 0. This is an identity, and the record confirms it on all 14 shells from N = 12 to 56. So the pattern changes shell by shell with the invariant's factors: zeros on the vertices at N = 12, 24, 36 and 48, on the faces at 20 and 40, on the edges at 30, on vertices and faces at 32, 44, 52 and 56, on vertices and edges at 42 and 54, and on faces and edges at 50. Its angle average is the whole shell's with the same amplitude, so its power per multipole equals P1's with the same shell weights (§VII).
- **At N = 60 the zeros go.** There m_N = 2, and the symbol of Π_60 is a sum of two squares, which vanishes only at common zeros; the degree-60 invariants have none, since f12 and f20 share no roots, and the record's smallest value is 0.53 of the mean. This boundary, a repeated trivial constituent, is not §IV's boundary for laws with baseline image correlations, which needs any repeated constituent and starts at N = 16, or N = 20 among the Molien shells.
- **From N = 60 it carries whatever the source supplies.** There A_N^eff(k̂) = P_N ⟨k̂|ι_N Σ̂^(N) ι_N†|k̂⟩, with Σ̂^(N) = 1 giving Π_N.
- **The orientation is a nuisance parameter, not a modelling choice.** The identification of the observer's tangent space with the Bloch sphere is canonical. What the geometry leaves free is how the observer's isotropy group sits relative to external axes: three angles that any anisotropic law carries.

**The fork, restated.** Two choices come in sequence. The source dynamics chooses the amplitudes P_N and, from N = 60, the shapes Σ̂^(N); the flattening chooses what of the covariance Σ̃_N survives. With the quotient as the source on every branch:

- a spectral transfer keeps the trace alone and gives P1;
- a symbol transfer gives A_N^eff(k̂) = ⟨k̂|Σ̃_N|k̂⟩, which is P_N |⟨k̂|ψ_N⟩|² below N = 60;
- a pullback gives P2, inhomogeneous on flat slices.

Below N = 60 the symbol transfer is therefore a prediction up to the amplitudes and the orientation; above, it carries source dynamics that nothing here supplies. Its observable difference from P1 is a frame: P1 has none, while the symbol transfer's power carries the icosahedral frame of the observer's isotropy group.

What stays open has two parts. Which flattening MIT performs matters on the low shells for every source, since even the canonical laws tell the three apart there; that is a question for the effective-metric side, at the scale where the Stress-Tensor Bridge's projection is also missing. From N = 60 it can matter at every N, for a source whose non-scalar shape keeps a low-degree directional structure, which the spectral transfer discards and the other two keep; whether the source has one is a question for its dynamics. On the unique-invariant shells, which are the low shells, the geometry fixes the directional shape if the rule is the symbol transfer. On the shells with more than one invariant it fixes only the invariant subspace, and the source dynamics can carry an anisotropy that the flat limit does not erase. The missing physics is then one statement: why MIT's projection from the static S³ to flat slices, at the scale R, should act on the source as the Q-symbol map, or as any other of these.

## VII. Bearing on other pages

- **CMB Anomalies.** [The page](../../../../cosmos/files/cmb-anomalies.md) said parity and the quadrupole-octupole alignment stay open to this topology through the eigenmode covariance. §II's corollary closes the alignment half conditionally, for a Gaussian source carried to the sky by a map that preserves the observer's A5, and every map on this page does. It leaves parity as it was. That update has since run (2026-09-15), as a sweep of every place the claim appeared: the CMB page's thesis, its §III, its falsification table and its close; the [cosmos index](../../../../cosmos/README.md) and the [framework index](../../../README.md); [the temporal budget](temporal-budget.md), whose §G footnote had also credited the closure to chirality; [the Oort Cloud project](oort-cloud-project.md), whose Piece E keeps its local-sampling reading and now carries A5-breaking as that reading's load-bearing requirement; and, as appended notes rather than repairs, the frozen contracts of [step two](molien-step-two.md) and [the ratio table](molien-ratio-table.md). The [claim ledger](claim-ledger.md) carries §II's corollary beside the chirality theorem.
- **The ratio table is unaffected.** It tabulates power per multipole, the sum of the variances over m. For a statistically homogeneous field with direction-dependent power P_N(k̂), that sum depends only on the angle average of the power at each wavenumber, since Σ_m |Y_ℓm(k̂)|² = (2ℓ+1)/4π in every direction. So the middle object and the symbol transfer, normalized to P1's angle-averaged shell weights, have the same table; telling them apart takes an anisotropy or covariance observable, not C_ℓ. The equivalence stops at the mean: unequal variances across a spin's constituents lower its effective number of degrees of freedom, so the scatter of a measured C_ℓ differs from P1's at ℓ ≥ 3.
- **Step one.** [The Molien Shells](molien-shells.md) calls the shared Majorana constellation "representation-space source structure, not yet a spatial or sky pattern". It is still not a sky pattern. In the flat limit, though, the Bloch sphere of the factor 2I acts on becomes the sphere of local wave-vector directions (§V), so under a symbol transfer the constellation would become the zeros of the power over wave-vector directions.
- **Step two.** P1 rests on the statement "The translation to the sky keeps spectrum, not pattern." The symbol transfer is the corresponding statement that keeps the pattern as well, as a pattern of power over wave-vector directions, while still discarding the images. Under it, as under P1, no points are identified, and the matched-circle observable is N/A.
- **The shell-unlock map** of [Entropy as Realization Budget](entropy-as-realization-budget.md), S ↦ N_max(S), decides which source modes are available, not how available modes become effective fluctuations, so it does not decide the map this page is about.

## VIII. Checks

The three scripts in [`scripts/molien-p1-bridge/`](scripts/molien-p1-bridge/) are pure computation, needing only numpy and scipy, and each record beside them reproduces byte for byte from its script: [`isotropy_check.out`](scripts/molien-p1-bridge/isotropy_check.out), [`quotient_half_check.out`](scripts/molien-p1-bridge/quotient_half_check.out) and [`flattening_check.out`](scripts/molien-p1-bridge/flattening_check.out). The last two write the invariant projector Π as P. Not computed: the flat-limit asymptotics, which the checks show numerically; Bochner's theorem, the density argument of §V and the spin-1/2 symbol, which are standard; and anything on the sky.
