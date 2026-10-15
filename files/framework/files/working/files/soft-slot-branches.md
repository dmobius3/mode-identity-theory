<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🎋 The Soft-Slot Branches

<img src="https://github.com/dmobius3/mode-identity-theory/blob/main/files/assets/Soft-Slot_Wave_Branch_Stability.png?raw=true" width="100%" alt="Bedrock">

**Type:** Result
**State:** Closed
**Status (2026-10-14):** Derived. In the soft slots R2, R4 and R5, every critical orbit of the reduced quartic that is nondegenerate modulo the stationary symmetry group continues to a branch of standing waves at small amplitude (Lemma G). Along such a branch the small-amplitude linear spectrum is read off the reduced quartic (Theorem R). A slow eigenvalue off the imaginary axis makes the branch unstable. A nondegenerate minimum gives a branch that is spectrally stable and orbitally stable relative to its stationary family. A nondegenerate maximum gives a spectrally stable branch. An indefinite orbit gives one when its slow flow is elliptic with Krein-definite frequencies and its zero modes are accounted for exactly. Exact arithmetic, and interval arithmetic for three orbits, classifies M8.12's census in R4 and R5, the three orbits certified outside its class there, and R2's fixed-line points; two of the outside orbits, added on 2026-10-14, are born hyperbolic. At R2's degenerate line point, Lemma G in the fixed space of its octahedral isotropy gives a germ, pinned by the symmetry. At second order, a closed form for the reduced function's first correction decides both degenerate orbits: R2's point is spectrally and orbitally stable along its family, and v1 is spectrally stable in R4 and R5. Nothing is claimed at finite amplitude. The globality of R2's minimum, Proposition C2 of the Slot Ground States, stays OPEN.
**Summary:** Branch existence and the small-amplitude linear spectrum at the soft slots' critical orbits, with the orbits computed exactly.
**Inputs:** `slot-action.md` (§V, §VII, §IX), `slot-ground-states.md` (§I, §IV, Theorem D), OpenWave's M8.12 census record (the orbit list and representatives) at `344f416`, `scripts/soft-slot-branches/`, and since 2026-10-14 the Surviving Ray's §7.2 certificates and, as a check of Lemma F, OpenWave M8.10's frozen values
**Parent:** `slot-ground-states.md`

---

RESULT, a derivation with no pre-committed pass condition. [The Slot Ground States](slot-ground-states.md) proved that every slot has orbitally stable sets of ground states and derived the soft blocks' reduced quartic in closed form. It left open the non-minimizing branches and the linear spectrum about the soft slots' states (§VII). This page proves that the soft blocks' nondegenerate critical orbits carry branches at small amplitude, decides their small-amplitude linear spectrum from the reduced quartic, and computes the orbits that decide it. Finite amplitude is not decided here; nothing here is a run, and nothing here bears on the slot relation, which stays OPEN.

**Related:** [The Slot Action](slot-action.md), [The Slot Ground States](slot-ground-states.md).

## I. The Setting

The soft slots are $`R_4`$ and $`R_5`$ at level 6 and $`R_2`$ at level 7, with $`\lambda_0 = K(K+2)/R^2`$ at level $`K`$. Their lowest eigenspace $`E_0`$ of $`-\Delta`$ on $`E_\rho`$ has complex dimension $`d = K + 1`$, and right translations act on it as the spin $`j = K/2`$ representation: $`E_0 \cong V_j`$ isometrically, $`w \mapsto \psi_w`$. With the Jensen ratio $`Q`$ of the Slot Ground States, §IV, the reduced quartic is

```math
H(w) = \frac{1}{2}\int_X \lvert\psi_w\rvert^4\, dV = \frac{Q(w)\,\lVert w\rVert^4}{2V}.
```

**The stationary symmetry group** $`\Gamma`$ is right SU(2) together with the fibre group of the slot action's §IX note: the phase and charge conjugation in $`R_4`$ and $`R_5`$, and $`Sp(1)`$ in $`R_2`$. In $`R_2`$, $`\mathrm{Hom}_{2I}(V_{7/2}, V_{2'})`$ is one-dimensional, so the fibre's quaternionic $`j`$ acts on $`E_0`$ as the quaternionic structure $`\Theta`$ of $`V_{7/2}`$, $`\Theta\lvert j, m\rangle = (-1)^{j-m}\lvert j, -m\rangle`$ extended antilinearly, up to a phase. $`\Gamma`$ is compact and acts orthogonally on $`E_0`$, and $`H`$ is $`\Gamma`$-invariant.

**At a critical orbit.** Let $`u`$, with $`\lVert u\rVert = 1`$, be critical for $`H`$ on the unit sphere, so $`\nabla H(u) = 4H(u)\,u`$. Write:
- $`K_u`$ for the tangent space of the orbit $`\Gamma u`$, of dimension $`k`$; it contains $`iu`$;
- $`M_u = \mathrm{Hess}\,H(u) - 4H(u)`$, a symmetric real-linear map of $`E_0`$, with $`M_u u = 8H(u)\,u`$ and $`M_u K_u = 0`$;
- $`N_u`$ for the orthogonal complement of $`u`$ and $`K_u`$, which $`M_u`$ preserves;
- $`(n_-, n_0, n_+)`$ for the signature of $`M_u`$ on $`N_u`$. The orbit is **nondegenerate** if $`n_0 = 0`$.

**The slow matrix** is $`S_u = iM_u`$, Hamiltonian for $`\sigma(x, y) = \mathrm{Re}\langle x, iy\rangle`$. Let $`r_u`$ be the dimension of the $`\sigma`$-radical of $`K_u`$, which always contains $`iu`$. At a nondegenerate orbit, $`\ker S_u = K_u`$ and every radical vector $`y`$ has a partner, $`S_u x = y`$, because $`-iy \perp K_u`$. So the zero eigenvalue of $`S_u`$ has multiplicity at least $`k + r_u`$. A nonzero frequency cluster $`\pm i\tau`$ of $`S_u`$ is **Krein-definite** if $`M_u`$ is definite on its real invariant subspace $`\ker(S_u^2 + \tau^2)`$; a simple pair always is. Theorem R and §IV use the same objects for $`h = Q\lVert w\rVert^4 = 2VH`$: $`\widehat M_u = 2V M_u`$ and $`\widehat S_u = i\widehat M_u`$.

## II. The Germs

**Lemma G.** Let $`\Gamma u`$ be a nondegenerate critical orbit and $`\kappa_u = 2H(u)`$. For small $`\varepsilon > 0`$ there are sections $`\varphi_\varepsilon \in H^2`$, smooth in $`\varepsilon`$, with $`\varphi_\varepsilon = (\varepsilon/g\kappa_u)^{1/2}\,(u + O(\varepsilon))`$, such that $`e^{i\omega T}\varphi_\varepsilon`$ with $`\omega^2 = c^2(\lambda_0 + \varepsilon)`$ solves the field equation. Moreover:
- $`\varphi_\varepsilon`$ has isotropy group exactly $`\Gamma_u`$, so the stationary family $`\Gamma\varphi_\varepsilon`$ has dimension $`k`$;
- near $`\Gamma u`$, the small solutions at that frequency are exactly the members of $`\Gamma\varphi_\varepsilon`$;
- the stationary operator $`L_\varepsilon = -\Delta - \omega^2/c^2 + g\left(\lvert\varphi_\varepsilon\rvert^2 + 2\varphi_\varepsilon\mathrm{Re}(\varphi_\varepsilon^{\dagger}\,\cdot\,)\right)`$ on $`H^2`$ has kernel exactly the tangent space of $`\Gamma\varphi_\varepsilon`$.

*Proof.*
- *The stationary map.* With $`\sigma = \omega^2/c^2`$, the map $`\mathcal{F}(\varphi, \sigma) = (-\Delta - \sigma)\varphi + g\lvert\varphi\rvert^2\varphi`$ is smooth from $`H^2 \times \mathbb{R}`$ to $`L^2`$, because $`H^2`$ is an algebra contained in $`L^\infty`$ in three dimensions. It is $`\Gamma`$-equivariant, and it is the $`L^2`$-gradient of $`E_\sigma(\varphi) = \frac{1}{2}\int(\lvert\nabla\varphi\rvert^2 - \sigma\lvert\varphi\rvert^2) + \frac{g}{4}\int\lvert\varphi\rvert^4`$.
- *Lyapunov–Schmidt.* Write $`\varphi = w + v`$ with $`w \in E_0`$ and $`v \perp E_0`$. For $`\sigma`$ near $`\lambda_0`$, $`-\Delta - \sigma`$ maps the complement of $`E_0`$ in $`H^2`$ onto its complement in $`L^2`$ with bounded inverse. So by the implicit function theorem the complementary equation has a unique small solution $`v(w, \sigma)`$, smooth, $`\Gamma`$-equivariant and odd in $`w`$, with $`\lVert v\rVert_{H^2} = O(\lVert w\rVert^3)`$. The small solutions are the critical points of the reduced function $`f(w, \sigma) = E_\sigma(w + v(w, \sigma))`$, since $`\nabla_w f = P_0\mathcal{F}(w + v, \sigma)`$. $`f`$ is $`\Gamma`$-invariant and even, equal to $`\frac{1}{2}(\lambda_0 - \sigma)\lVert w\rVert^2 + \frac{g}{2}H(w) + O(\lVert w\rVert^6)`$.
- *Scaling.* With $`\sigma = \lambda_0 + \varepsilon`$ and $`w = (\varepsilon/g)^{1/2}y`$, $`f = (\varepsilon^2/2g)\,\tilde f(y, \varepsilon)`$, where $`\tilde f(y, \varepsilon) = H(y) - \lVert y\rVert^2 + \varepsilon\,\tilde R(y, \varepsilon)`$ and $`\tilde R`$ is smooth, since $`f`$ is even. The critical points of $`\tilde f(\cdot, 0)`$ near the orbit are $`\Gamma y_0`$ with $`y_0 = \kappa_u^{-1/2}u`$, where its Hessian is $`\kappa_u^{-1}M_u`$, nondegenerate on the normal space $`\mathbb{R}u \oplus N_u`$.
- *The slice.* $`\Gamma`$ is compact and acts orthogonally, so by the slice theorem a neighbourhood of $`\Gamma y_0`$ is $`\Gamma \times_{\Gamma_u} \Sigma`$, with $`\Sigma`$ a small ball about $`y_0`$ in $`y_0 + (\mathbb{R}u \oplus N_u)`$. Every orbit near $`\Gamma y_0`$ meets $`\Sigma`$, and at each $`y \in \Sigma`$ the orbit tangent and $`\mathbb{R}u \oplus N_u`$ together span $`E_0`$. The differential of a $`\Gamma`$-invariant function vanishes on orbit tangents, so its critical orbits near $`\Gamma y_0`$ are the orbits of the critical points of its restriction to $`\Sigma`$. $`\tilde f(\cdot, 0)`$ restricted to $`\Sigma`$ has a nondegenerate critical point at $`y_0`$, so by the implicit function theorem $`\tilde f(\cdot, \varepsilon)`$ restricted to $`\Sigma`$ has a unique critical point $`y_\varepsilon`$ near $`y_0`$, smooth in $`\varepsilon`$. $`\Gamma_u`$ preserves $`\Sigma`$ and $`\tilde f`$, so uniqueness makes $`y_\varepsilon`$ $`\Gamma_u`$-fixed, and equivariance of $`v`$ carries this to $`\varphi_\varepsilon = w + v(w, \lambda_0 + \varepsilon)`$ with $`w = (\varepsilon/g)^{1/2}y_\varepsilon`$.
- *Isotropy.* The isotropy group of $`y_\varepsilon`$ contains $`\Gamma_u`$, and by the slice theorem it lies in $`\Gamma_u`$, so it is $`\Gamma_u`$.
- *The kernel.* Differentiating the complementary equation shows that $`L_\varepsilon\zeta = 0`$ forces the complementary part of $`\zeta`$ to be $`D_wv\,\zeta_0`$, with $`\zeta_0`$ its $`E_0`$ part, and then $`P_0L_\varepsilon\zeta = \mathrm{Hess}_w f\,\zeta_0`$. So $`\ker L_\varepsilon`$ corresponds to the kernel of the reduced Hessian. That Hessian is a small perturbation of $`\kappa_u^{-1}M_u`$, nondegenerate on $`\mathbb{R}u \oplus N_u`$, and it vanishes on the orbit tangent at $`y_\varepsilon`$, which has dimension $`k`$.

**Lemma G′, in a fixed space (added 2026-10-14).** Lemma G run in the fixed space of a point's isotropy, the slot action's analogue of the Surviving Ray's §8.3 theorem, written for $`R_2`$'s degenerate point and graded as a new derivation. Let $`u`$, with $`\lVert u\rVert = 1`$, be critical for $`H`$ on the unit sphere, $`\Gamma_u`$ its isotropy group in $`\Gamma`$, $`X^u`$ the closed subspace of sections that $`\Gamma_u`$ fixes, $`E_0^u = E_0 \cap X^u`$, a real subspace, and $`\Gamma^u`$ the closed subgroup of $`\Gamma`$ that preserves $`X^u`$. Let $`N_u^u`$ be the orthogonal complement in $`E_0^u`$ of $`u`$ and the tangent space of $`\Gamma^u u`$. If $`M_u`$ is nondegenerate on $`N_u^u`$, in particular if $`N_u^u = 0`$, then for small $`\varepsilon > 0`$ there are sections $`\varphi_\varepsilon \in X^u \cap H^2`$, smooth in $`\varepsilon`$, with $`\varphi_\varepsilon = (\varepsilon/g\kappa_u)^{1/2}\,(u + O(\varepsilon))`$, such that $`e^{i\omega T}\varphi_\varepsilon`$ with $`\omega^2 = c^2(\lambda_0 + \varepsilon)`$ solves the field equation. Moreover:
- $`\varphi_\varepsilon`$ has isotropy group exactly $`\Gamma_u`$;
- near $`u`$, the small solutions in $`X^u`$ at that frequency are exactly the members of $`\Gamma^u\varphi_\varepsilon`$.

It claims nothing about solutions outside $`X^u`$, about the kernel of $`L_\varepsilon`$, or about stability.

*Proof.* Lemma G's proof, run in $`X^u`$.
- *The fixed space.* $`\mathcal F`$ is $`\Gamma`$-equivariant, so it maps $`X^u \cap H^2`$ into $`X^u`$, and $`-\Delta - \sigma`$ preserves $`X^u`$. For $`w \in E_0^u`$ the complementary solution $`v(w, \sigma)`$ is $`\Gamma_u`$-fixed, by its uniqueness and equivariance, and so is $`\nabla_w f`$. So $`\nabla_w f`$ lies in $`E_0^u`$ there, and the critical points of $`f`$ restricted to $`E_0^u`$ are critical points of $`f`$.
- *Scaling.* As in Lemma G, on $`E_0^u`$: $`\tilde f(\cdot, 0)`$ has the critical point $`y_0 = \kappa_u^{-1/2}u`$, with Hessian $`\kappa_u^{-1}M_u`$ on $`\mathbb{R}u \oplus N_u^u`$. It is nondegenerate there, on $`\mathbb{R}u`$ because $`M_u u = 8H(u)\,u`$ and on $`N_u^u`$ by hypothesis.
- *The slice.* $`\Gamma^u`$ is compact and acts orthogonally on $`E_0^u`$, so a neighbourhood of $`\Gamma^u y_0`$ there is $`\Gamma^u \times_{\Gamma_u} \Sigma^u`$, with $`\Sigma^u`$ a small ball about $`y_0`$ in $`y_0 + (\mathbb{R}u \oplus N_u^u)`$. The implicit function theorem gives $`\tilde f(\cdot, \varepsilon)`$ a unique critical point $`y_\varepsilon`$ on $`\Sigma^u`$ near $`y_0`$, smooth in $`\varepsilon`$, and with it $`\varphi_\varepsilon`$.
- *Isotropy.* $`y_\varepsilon`$ is $`\Gamma_u`$-fixed. The $`\Gamma_u`$-fixed part of the orbit tangent $`K_u`$ is the tangent of $`\Gamma^u u`$, and its other isotypic components are orthogonal to $`E_0^u`$. So $`N_u^u`$ lies in $`N_u`$, and $`\Sigma^u`$ in the slice $`\Sigma`$ of Lemma G's proof, whose points have isotropy inside $`\Gamma_u`$.

**At $`R_2`$'s degenerate point** ([`germ_check.py`](scripts/soft-slot-branches/germ_check.py), exact over $`\mathbb{Q}(\sqrt 2, i)`$). The interior critical point of the cyclic line {5/2, −3/2} (§IV), $`\sqrt{3/4}\,v_{5/2} + \sqrt{1/4}\,v_{-3/2}`$ with $`Q = 161/143`$, has $`k = 6 = \dim\Gamma`$ and signature (0, 3, 6). It is degenerate, so Lemma G does not apply, and its isotropy group is finite.
- *The isotropy.* $`\Gamma_u`$ contains the quarter-turn about $`z`$ with the fibre phase $`e^{5\pi i/4}`$, and the half-turn about $`y`$ with the fibre element $`-j`$. Turned by $`\pi/4`$ about $`z`$, the point becomes $`\sqrt{3/4}\,v_{5/2} - \sqrt{1/4}\,v_{-3/2}`$ up to a fibre phase, which the quarter-turn about $`x`$ with the fibre element $`(-1 + k)/\sqrt 2`$ also fixes. The two quarter-turns generate the octahedral group, which no finite subgroup of SO(3) properly contains, so the rotation part of $`\Gamma_u`$ is $`O`$.
- *The fixed space.* $`E_0^u`$ is the real line through the point. So $`N_u^u = 0`$: the slice is a point and the symmetry pins the germ, as at the Surviving Ray's four symmetry-pinned rays (§8.3 there). Lemma G′ gives a branch with isotropy exactly $`\Gamma_u`$, unique in $`X^u`$ near the point.
- *A cross-check on a subgroup.* The quarter-turn about $`z`$ and the half-turn about $`y`$ generate a dihedral group, which fixes the real plane of the coefficients of $`v_{5/2}`$ and $`v_{-3/2}`$. No infinitesimal symmetry preserves that plane, its direction orthogonal to the point lies in $`N_u`$, and $`M_u`$ is positive there, $`168/143`$ relative to the metric for unit $`u`$ in the $`h`$ normalization. So Lemma G′'s argument, run with that subgroup in place of $`\Gamma_u`$, uses the Hessian condition and finds the same germ, unique in the larger fixed space near the point.
- *The kernel.* The three-dimensional kernel of $`M_u`$ on $`N_u`$ meets neither fixed space. It is why Theorem R does not apply here: the branch's small-amplitude type needs the slow spectrum at order $`\varepsilon^2`$ (§VI).

## III. The Small-Amplitude Spectrum

Fix a branch from Lemma G, with $`\omega_\varepsilon = c(\lambda_0 + \varepsilon)^{1/2}`$. Writing $`\psi = e^{i\omega_\varepsilon T}(\varphi_\varepsilon + \zeta)`$, the linearized equation

```math
\frac{1}{c^2}\left(\partial_T^2\zeta + 2i\omega_\varepsilon\,\partial_T\zeta\right) + L_\varepsilon\zeta = 0
```

is a real-linear system $`\dot x = A_\varepsilon x`$ on $`\mathcal{H}`$, with $`x = (\zeta, \partial_T\zeta)`$.
- *Its conserved form.* $`A_\varepsilon`$ conserves $`H_2(x) = \lVert\partial_T\zeta\rVert^2/2c^2 + \frac{1}{2}\langle L_\varepsilon\zeta, \zeta\rangle`$, the second variation of $`E - \omega_\varepsilon N`$ at the standing wave.
- *Its symplectic form.* $`A_\varepsilon`$ is Hamiltonian, $`\Omega(A_\varepsilon x, y) = B(x, y)`$ with $`H_2(x) = \frac{1}{2}B(x, x)`$, for $`\Omega(x_1, x_2) = c^{-2}\,\mathrm{Re}\left(\langle\zeta_1, \dot\zeta_2\rangle - \langle\dot\zeta_1, \zeta_2\rangle + 2\omega_\varepsilon\langle\zeta_1, i\zeta_2\rangle\right)`$. On static vectors, $`\Omega((y, 0), (z, 0)) = (2\omega_\varepsilon/c^2)\,\sigma(y, z)`$.
- *Its kernel.* $`\ker A_\varepsilon = \ker B`$ consists of the static vectors $`(\zeta, 0)`$ with $`L_\varepsilon\zeta = 0`$: by Lemma G, the tangent space of the stationary family, of dimension $`k`$. In $`R_2`$ this includes the $`Sp(1)`$ directions, which are static solutions though not symmetries of the rotating frame, the distinction the Slot Ground States' Theorem D draws.

**Lemma S (the slow symplectic space).** For small $`\varepsilon`$, let $`\mathcal{H}_s(\varepsilon)`$ be the spectral subspace of $`A_\varepsilon`$ inside a fixed small circle about 0 (Theorem R(a)). $`\Omega`$ is nondegenerate on it. For the complex-bilinear extension of $`\Omega`$, generalized eigenspaces of $`A_\varepsilon`$ for eigenvalues $`\lambda`$ and $`\mu`$ with $`\lambda + \mu \ne 0`$ are $`\Omega`$-orthogonal. So the generalized kernel, and the sum of the generalized eigenspaces of each nonzero cluster $`\lbrace\pm\lambda, \pm\bar\lambda\rbrace`$, are each $`\Omega`$-nondegenerate.

*Proof.* The fast subspace is $`\Omega`$-orthogonal to $`\mathcal{H}_s(\varepsilon)`$, and $`\Omega`$ is weakly nondegenerate on $`\mathcal{H}`$, so a vector of $`\mathcal{H}_s(\varepsilon)`$ that pairs to zero with all of it is zero. On the complexification, $`\Omega(A x, y) = -\Omega(x, A y)`$ gives $`(\lambda + \mu)\,\Omega(x, y) = 0`$ for eigenvectors, and induction along Jordan chains extends this to generalized eigenvectors. A subspace orthogonal to its complement in a nondegenerate space is itself nondegenerate.

**Theorem R.** Let $`\Gamma u`$ be a nondegenerate critical orbit with branch $`\varphi_\varepsilon`$. There is $`\varepsilon_1 > 0`$ such that for $`0 < \varepsilon < \varepsilon_1`$:
- **(a) Splitting.** The spectrum of $`A_\varepsilon`$ consists of a slow part, $`2d`$ eigenvalues $`\varepsilon(\kappa s + o(1))`$ with $`s`$ running over the eigenvalues of $`\widehat S_u`$ and $`\kappa = c^2/(8\omega_0 Q(u)) > 0`$, and a fast part on the imaginary axis, bounded away from 0.
- **(b) Hyperbolic.** If $`\widehat S_u`$ has an eigenvalue with positive real part, so does $`A_\varepsilon`$: the branch is spectrally unstable.
- **(c) Minimum.** If $`n_- = 0`$, then $`H_2 \ge 0`$ with kernel exactly the stationary family's tangent space. The spectrum of $`A_\varepsilon`$ is imaginary, and the family is orbitally stable: data near it stay near it, as a set, for all time.
- **(d) Maximum.** If $`n_+ = 0`$, the spectrum of $`A_\varepsilon`$ is imaginary.
- **(e) Indefinite.** Suppose the nonzero eigenvalues of $`\widehat S_u`$ are imaginary and Krein-definite, and (Z) the zero eigenvalue of $`\widehat S_u`$ has multiplicity exactly $`k + r_u`$ and the $`\Omega`$-radical of $`\ker A_\varepsilon`$ has dimension $`r_u`$. Then the spectrum of $`A_\varepsilon`$ is imaginary.

In (c) to (e) the claim is spectral stability at small amplitude; only (c) also gives orbital stability.

*Proof.*
- **At $`\varepsilon = 0`$.** On $`E_0 \times E_0`$, $`A_0(\zeta, \eta) = (\eta, -2i\omega_0\eta)`$: the eigenvalue 0 is semisimple with eigenspace $`E_0 \times \lbrace 0\rbrace`$, and the rest of this block is the eigenvalue $`-2i\omega_0`$ and its conjugate. Each higher level contributes a nonzero imaginary pair. $`A_0`$ has compact resolvent, and $`H_2 \ge 0`$ with kernel $`E_0 \times \lbrace 0\rbrace`$. On the spectral complement of that kernel it is coercive: there it is $`\lVert\dot\zeta\rVert^2/2c^2`$ on the $`E_0`$ block, and at least $`(\lambda_1 - \lambda_0)\lVert\zeta\rVert^2/2`$ plus the kinetic term above it.
- **(a) Splitting.** $`A_\varepsilon - A_0`$ is bounded on $`\mathcal{H}`$, of size $`O(\varepsilon)`$ and differentiable at 0. For a circle $`\lvert\lambda\rvert = \delta`$ inside the gap, the Riesz projection $`P_\varepsilon`$ is continuous and has rank $`2d`$ (Kato). The slow and fast subspaces $`\mathcal{H}_s(\varepsilon)`$ and $`\mathcal{H}_f(\varepsilon)`$ are $`A_\varepsilon`$-invariant and orthogonal for both $`B`$ and $`\Omega`$, since their spectral sets are disjoint and each symmetric under $`\lambda \mapsto -\lambda`$.
  - *Fast part.* $`H_2`$ stays coercive on $`\mathcal{H}_f(\varepsilon)`$, so the group it generates there is bounded and its spectrum is imaginary.
  - *Slow part.* For the semisimple eigenvalue 0, Kato's first-order reduction transports $`A_\varepsilon`$ on $`\mathcal{H}_s(\varepsilon)`$ to $`\varepsilon P_0A'P_0 + o(\varepsilon)`$ on $`E_0 \times \lbrace 0\rbrace`$. With $`P_0(\zeta, \eta) = (\zeta - (i/2\omega_0)\eta, 0)`$ on the $`E_0`$ block and $`\varphi_\varepsilon \approx (\varepsilon/g\kappa_u)^{1/2}u`$, a direct computation gives $`P_0A'P_0 = \kappa\widehat S_u`$. In the same transport $`B`$ becomes $`(\varepsilon/4Q(u))\langle\widehat M_u\cdot, \cdot\rangle + o(\varepsilon)`$, because $`B_0`$ vanishes on $`E_0 \times \lbrace 0\rbrace`$ together with its cross terms.
- **(b)** follows from (a), by continuity of the eigenvalues of the transported slow matrix.
- **(c)** $`\widehat M_u \ge 0`$ with kernel $`K_u`$. On $`\mathcal{H}_s(\varepsilon)`$, $`B`$ is $`\varepsilon(\widehat M_u/4Q(u) + o(1))`$, and the $`k`$ static directions of the stationary family are exact null vectors with vanishing cross terms. So $`B \ge 0`$ there with kernel exactly those directions, and with $`\mathcal{H}_f(\varepsilon)`$, $`B \ge 0`$ on $`\mathcal{H}`$ with that kernel.
  - *Spectrum.* The kernel is $`A_\varepsilon`$-invariant, and on the quotient $`H_2`$ is a conserved norm, so the spectrum is imaginary.
  - *Orbital stability.* The family is a compact nondegenerate critical manifold of the conserved functional $`E - \omega_\varepsilon N`$, with Hessian coercive on its normal bundle, so it is Lyapunov stable as a set. Solutions are global by the Slot Ground States, §I.
  - *In $`R_2`$,* $`E - \omega_\varepsilon N`$ is not $`Sp(1)`$-invariant, because $`N`$ uses the complex structure $`i`$. The family is still a critical manifold on which it is constant: each member $`e^{i\omega_\varepsilon T}(\varphi_\varepsilon p)`$ is a standing wave of frequency $`\omega_\varepsilon`$ with $`\lvert\varphi_\varepsilon p\rvert = \lvert\varphi_\varepsilon\rvert`$, and the normal Hessian is coercive at each member through the similarity under "Families in $`R_2`$".
- **(d)** Let $`\theta = (i\varphi_\varepsilon, 0)`$, the phase mode, and $`\xi = ((2\omega_\varepsilon/c^2)\partial_\varepsilon\varphi_\varepsilon,\ i\varphi_\varepsilon)`$.
  - *The phase pair.* Differentiating the stationary equation in $`\varepsilon`$ gives $`L_\varepsilon\partial_\varepsilon\varphi_\varepsilon = \varphi_\varepsilon`$, and with it $`A_\varepsilon\xi = \theta`$. By Lemma G, $`\lVert\varphi_\varepsilon\rVert^2 = (\varepsilon/g\kappa_u)(1 + O(\varepsilon))`$, so $`\Omega(\theta, \xi) = c^{-2}\left(\lVert\varphi_\varepsilon\rVert^2 + (2\omega_\varepsilon^2/c^2)\,\partial_\varepsilon\lVert\varphi_\varepsilon\rVert^2\right) > 0`$. So $`\mathrm{span}\lbrace\theta, \xi\rbrace`$ is invariant and symplectic.
  - *The complement.* Its $`\Omega`$-complement $`\mathcal{H}_s'(\varepsilon)`$ in $`\mathcal{H}_s(\varepsilon)`$ is invariant and tends to the $`\sigma`$-complement of $`\lbrace u, iu\rbrace`$ in $`E_0`$, which is $`N_u`$ plus $`K_u`$ minus the phase direction. There $`-\widehat M_u \ge 0`$ with kernel exactly the non-phase part of $`K_u`$.
  - *The kernel.* $`\ker A_\varepsilon \cap \mathcal{H}_s'(\varepsilon)`$ has dimension $`k - 1`$: each static direction $`y`$, corrected by a multiple of $`\theta`$, lies in it, since $`\Omega(y, \theta) = -\Omega(A_\varepsilon y, \xi) = 0`$.
  - *Conclusion.* As in (c), $`-B \ge 0`$ on $`\mathcal{H}_s'(\varepsilon)`$ with kernel the static directions, so the spectrum there is imaginary. $`\mathrm{span}\lbrace\theta, \xi\rbrace`$ carries the eigenvalue 0, and $`\mathcal{H}_f(\varepsilon)`$ is imaginary by (a).
- **(e)**
  - *Partners.* $`\ker A_\varepsilon`$ lies in $`\mathcal{H}_s(\varepsilon)`$, where $`\Omega`$ is nondegenerate (Lemma S) and $`A_\varepsilon`$ is $`\Omega`$-skew, so there the range of $`A_\varepsilon`$ is the $`\Omega`$-annihilator of its kernel. Each vector of the $`\Omega`$-radical of $`\ker A_\varepsilon`$ therefore has a partner, and the generalized kernel has dimension at least $`k + r_u`$.
  - *Exact zeros.* By (a), $`A_\varepsilon`$ has exactly as many eigenvalues within $`o(\varepsilon)`$ of 0 as $`\widehat S_u`$ has zeros, $`k + r_u`$ by (Z). So all of them are 0.
  - *Nonzero clusters.* By Lemma S, the sum of the generalized eigenspaces near each cluster $`\pm i\varepsilon\kappa\tau`$ is $`\Omega`$-nondegenerate, invariant, and tends to $`\ker(\widehat S_u^2 + \tau^2)`$. On it $`B`$ is $`\varepsilon(\widehat M_u/4Q(u) + o(1))`$, definite by Krein-definiteness. A conserved definite form keeps those eigenvalues imaginary.

**Families in $`R_2`$.** An orbit in $`R_2`$ contains its $`Sp(1)`$ family $`\lbrace u\,p\rbrace`$ of distinct standing waves. Theorem R applies at each member: $`M_{up}`$ is $`M_u`$ conjugated by right multiplication by $`p`$, so $`S_{up}`$ is similar to $`R_{pip^{-1}}M_u`$, the slow matrix of $`u`$ for the complex structure $`pip^{-1}`$. Definiteness, and with it (c) and (d), holds along the whole family, uniformly by compactness. The type of an indefinite orbit can change along it, which the slot action's §IX note requires to be assessed point by point.

**Second order at the degenerate orbits (added 2026-10-14).** At a degenerate orbit Theorem R leaves the kernel of $`M_u`$ on $`N_u`$ undecided at order $`\varepsilon`$. Lemma F carries the reduced function one order further, in closed form for the soft slots, and Theorem R′ reads the type from it where the germ comes from Lemma G′. Both are graded as new derivations. [`second_order_check.py`](scripts/soft-slot-branches/second_order_check.py) checks them in exact arithmetic, apart from a floating-point cross-check of one projector and a floating-point model of the slow problem.

**Lemma F (the first correction).** In Lemma G's scaling, $`\tilde R(y, 0) = \tilde R_0(y)`$, with

```math
\tilde R_0(y) = -\big\langle L_0^{-1}P_\perp N(\psi_y),\ P_\perp N(\psi_y)\big\rangle, \qquad N(\psi) = \lvert\psi\rvert^2\psi,
```

where $`L_0 = -\Delta - \lambda_0`$ is inverted on the complement of $`E_0`$. In the soft slots, at level $`K`$ and spin $`j = K/2`$,

```math
\tilde R_0(y) = -\frac{R^2}{s^3V^2}\sum_{J \ne j}\frac{t_J}{(2J+1)\,\mu_J}\,\big\lVert[Y_6(y)\otimes y]_J\big\rVert^2,
```

with:
- $`s = \dim\rho/(2j+1)`$: 3/7 in $`R_4`$, 4/7 in $`R_5`$ and 1/4 in $`R_2`$;
- $`Y_6(y)`$ the spin-6 part of $`yy^\dagger`$, in the orthonormal basis of `branches_check.py`'s claim A, where $`h = \lVert w\rVert^4 + \beta\lVert Y_6(w)\rVert^2`$, and $`[\,\cdot\,]_J`$ the spin-$`J`$ part of $`V_6\otimes V_j`$, for $`\lvert 6 - j\rvert \le J \le 6 + j`$;
- $`\mu_J = 2J(2J+2) - K(K+2)`$, the gap of level $`2J`$ over level $`K`$;
- $`t_J = (2j+1)\,s(1-s)\big(s(2J+1)/13 + \kappa_J(1-2s)\big)`$, with $`\kappa_J = \sum_m \langle 6\,0;\, j\,m\,\vert\, J\,m\rangle^2\,(T_0)_{mm}\big/\sum_m (T_0)_{mm}^3`$ for $`T_0`$ the spin-6 operator of weight 0 on $`V_j`$, of unit Hilbert–Schmidt norm.

The nonzero $`t_J`$ fall at levels 10, 14, 16 and 18 in $`R_4`$, at 8, 12, 14, 16 and 18 in $`R_5`$, and at 13, 17 and 19 in $`R_2`$.

*Proof.*
- *The correction.* In Lemma G's proof, $`v(w, \sigma) = -gL_\sigma^{-1}P_\perp N(w) + O(\lVert w\rVert^5)`$, with $`L_\sigma`$ the restriction of $`-\Delta - \sigma`$ to the complement, $`L_0 + O(\varepsilon)`$. Substituting into $`E_\sigma(w + v)`$ gives the sixth-order part $`-\frac{g^2}{2}\langle L_0^{-1}P_\perp N(w), P_\perp N(w)\rangle`$, and the scaling gives $`\tilde R_0`$.
- *The density.* Write $`\psi_y(x) = AD^j(x)\,y`$, with $`A`$ intertwining $`2I`$ and $`A^\dagger A = P_\rho/(sV)`$, where $`P_\rho`$ projects $`V_j`$ onto its $`\rho`$-part. For $`1 \le L \le 7`$, $`V_L`$ has $`2I`$-invariants only at $`L = 6`$, so $`P_\rho = s + P_6`$ with $`P_6`$ of spin 6, and $`\lvert\psi_y\rvert^2 = \lVert y\rVert^2/V + \langle P_6, D^6(x)Y_6(y)\rangle/(sV)`$. The constant part keeps $`N`$ in $`E_0`$. The spin-6 part puts the level-$`2J`$ part of $`N`$ at $`A_JD^J(x)[Y_6(y)\otimes y]_J`$, with $`A_J`$ the coupling of $`P_6`$ and $`A`$ to spin $`J`$, and Schur orthogonality gives its squared norm, $`t_J\lVert[Y_6(y)\otimes y]_J\rVert^2/\big((2J+1)s^3V^2\big)`$.
- *The constants.* $`t_J`$ is the trace of $`\lvert P_6\rangle\langle P_6\rvert\otimes P_\rho`$ on the spin-$`J`$ part of $`V_6\otimes V_j`$, with $`P_6`$ read as a vector of $`V_6`$. From $`P_\rho^2 = P_\rho`$, $`\lVert P_6\rVert^2 = (2j+1)s(1-s)`$ and $`\mathrm{tr}\,P_6^3 = (1-2s)\lVert P_6\rVert^2`$. The part $`s`$ of $`P_\rho`$ contributes $`s(2J+1)\lVert P_6\rVert^2/13`$, by Schur. The part $`P_6`$ contributes a cubic rotation invariant of a real spin-6 vector; those form a line, so it is $`\kappa_J\,\mathrm{tr}\,P_6^3`$, with $`\kappa_J`$ read off at $`T_0`$.
- *Checks.* In $`R_4`$ and $`R_5`$ the closed form reproduces OpenWave M8.10's frozen values exactly [M8.10]: its 36 level norms, its eight values of $`\lambda_4/g^2`$, and its level sets. In $`R_2`$, binary-icosahedral characters put $`2'`$ at levels 13, 17 and 19 above the bottom, and the projector onto $`2'`$, summed over the 120 elements of $`2I`$, has spin parts 0 and 6 only and returns the same $`t_J`$.

**Theorem R′ (second order).** Let $`u`$ be a degenerate critical point whose germ $`\varphi_\varepsilon`$ comes from Lemma G′, with $`E_0^u \subset \mathbb{C}u`$, and let $`K' = \ker M_u \cap N_u`$. Write

```math
\gamma_u = \kappa_u^{-2}\big(\mathrm{Hess}\,\tilde R_0(u) - 6\tilde R_0(u)\big)\big|_{K'},
```

a symmetric form on $`K'`$, taken relative to the metric.
- **(a) The Hessian at the germ.** $`\mathrm{Hess}_y\tilde f(y_\varepsilon, \varepsilon) = \kappa_u^{-1}M_u + \varepsilon D + O(\varepsilon^2)`$, where $`D`$ annihilates $`K_u`$ and is $`\gamma_u`$ on $`K'`$.
- **(b) A definite second order.** If $`n_- = 0`$ and $`\gamma_u`$ is positive definite, then for small $`\varepsilon > 0`$, $`L_\varepsilon \ge 0`$ with kernel exactly the tangent space of $`\Gamma\varphi_\varepsilon`$. Theorem R(c)'s conclusions follow: the spectrum of $`A_\varepsilon`$ is imaginary, and the family is orbitally stable, in $`R_2`$ along the family.
- **(c) A decoupled sector.** Suppose $`\Gamma_u`$ contains a circle acting complex-linearly, and $`K'`$ is a whole isotypic component of it in $`E_0`$, of dimension 2 and nonzero weight. Then $`\gamma_u`$ is a multiple of the metric, and the part of the slow space of that weight is invariant, $`\Omega`$-nondegenerate and two-dimensional. Its pair is imaginary for every small $`\varepsilon`$, at $`\pm i\varepsilon^2(c^2/4\omega_0)\,\gamma_u(1 + O(\varepsilon))`$ when $`\gamma_u \ne 0`$. If Theorem R(e)'s hypotheses hold for $`\widehat S_u`$ on the other components, the spectrum of $`A_\varepsilon`$ is imaginary.

As in Theorem R, the claims are at small amplitude, and only (b) gives orbital stability.

*Proof.*
- **(a)** By Lemma G′ and the phase symmetry, $`y_\varepsilon = \rho_\varepsilon u`$. The critical equation on $`\mathbb{R}u`$ is $`\kappa_u\rho^2 - 1 + 3\varepsilon\tilde R_0(u)\rho^4 = 0`$, so $`\kappa_u\rho_\varepsilon^2 = 1 - 3\varepsilon\kappa_u^{-2}\tilde R_0(u) + O(\varepsilon^2)`$. On $`\ker M_u`$, $`\mathrm{Hess}\,H(u) = 2\kappa_u`$, so there $`\mathrm{Hess}\,H(y_\varepsilon) - 2 = 2(\kappa_u\rho_\varepsilon^2 - 1)`$, and the correction adds $`\varepsilon\rho_\varepsilon^4\,\mathrm{Hess}\,\tilde R_0(u)`$: together $`\varepsilon\kappa_u^{-2}(\mathrm{Hess}\,\tilde R_0(u) - 6\tilde R_0(u)) + O(\varepsilon^2)`$. Since $`y_\varepsilon`$ is a multiple of $`u`$, the orbit tangent there is $`K_u`$ itself, which the Hessian annihilates at every $`\varepsilon`$, so $`D`$ annihilates $`K_u`$.
- **(b)** By (a), the Hessian is positive on the normal space at $`y_\varepsilon`$: on the range of $`M_u`$ at order 1, and on $`K'`$ at order $`\varepsilon`$, since the cross terms are $`O(\varepsilon)`$ and change the block of $`K'`$ at order $`\varepsilon^2`$. By the kernel step of Lemma G's proof, $`L_\varepsilon`$ is positive on the complement of $`E_0`$ for small $`\varepsilon`$, and its Schur complement on $`E_0`$ is $`\mathrm{Hess}_wf = \frac{\varepsilon}{2}\mathrm{Hess}_y\tilde f`$. So $`L_\varepsilon \ge 0`$ with kernel the orbit tangent, and $`H_2 \ge 0`$ with kernel exactly the stationary family's tangent space. From there Theorem R(c)'s proof applies as written, with coercivity of order $`\varepsilon^2`$ on $`K'`$, and in $`R_2`$ through the similarity under "Families in $`R_2`$".
- **(c)** By Lemma G′ the circle lies in the germ's isotropy, and it commutes with $`i`$, so it commutes with $`A_\varepsilon`$ and preserves $`\Omega`$. Its isotypic parts of the slow space are invariant and $`\Omega`$-orthogonal, so each is $`\Omega`$-nondegenerate (Lemma S), and since the Riesz projection commutes with the circle, the part of the weight of $`K'`$ has dimension 2. On it $`A_\varepsilon`$ commutes with the circle's rotations, so it is $`a + bX`$, with $`X`$ the generator, and $`\Omega`$-skewness gives $`a = 0`$: its eigenvalues are $`\pm ib`$. Reducing $`(L_\varepsilon + \lambda^2/c^2 + 2\omega_\varepsilon\lambda i/c^2)\zeta = 0`$ to $`E_0`$, as in Lemma G's proof, gives $`[\mathrm{Hess}_wf + 2\omega_\varepsilon\lambda i/c^2 + O(\lambda^2 + \varepsilon^2\lvert\lambda\rvert)]\zeta_0 = 0`$, and with (a) on $`K'`$ this gives $`b = \varepsilon^2(c^2/4\omega_0)\,\gamma_u(1 + O(\varepsilon))`$. Off that component $`M_u`$ has no kernel on $`N_u`$, since its kernel there is $`K'`$; so by (a) and the kernel step of Lemma G's proof, the kernel of $`L_\varepsilon`$ off the component is exactly the orbit tangent, and Theorem R(e)'s proof applies as written.

**At $`R_2`$'s degenerate point** (§II), the interior critical point of the line {5/2, −3/2}:
- *The kernel and its group.* $`K'`$ has dimension 3, and $`\Gamma_u`$, of order 24, acts on it absolutely irreducibly, so $`\gamma_u`$ is a multiple of the metric, by Schur, and the same along the family. Only 8 of the 24 elements respect $`i`$, 4 commuting with it and 4 reversing it, and under those 8 $`K'`$ is reducible. The slow matrix sees that dihedral subgroup, the energy sees the whole group, and the type is read from the energy.
- *The value.* Lemma F's sum runs over levels 13, 17 and 19, with $`t_J = 147/136,\ 1323/1976,\ 180/323`$. At each level the gradient of $`\lVert[Y_6(y)\otimes y]_J\rVert^2`$ vanishes on $`K'`$, and its spherical Hessian there is a multiple of the metric: $`-17955/82654`$, $`10125/120802`$ and $`2205/60401`$. So $`\gamma_u = (115020/20333173)\,R^2`$, positive.
- *The type.* $`n_- = 0`$ (§IV), so Theorem R′(b) applies: the branch is spectrally and orbitally stable at small amplitude, along its family.
- *The leading orders.* By (b), the full linearization's slow spectrum is imaginary at small amplitude. $`\widehat S_u`$ has its zero of multiplicity 12, and the stationary family supplies $`k + r_u = 8`$ of it, which stay zero for $`A_\varepsilon`$. $`\sigma`$ on $`\ker M_u`$ has rank 6 and a radical of dimension 3: two directions in $`K_u`$, and one reaching into $`K'`$, whose partner has positive energy. In the script's finite-dimensional model of the slow problem, the other four eigenvalues leave zero at two orders:
  - a pair at $`\pm i\varepsilon^2(c^2/4\omega_0)\,a_2`$, from the plane of $`K'`$ orthogonal to the radical direction;
  - a pair at $`\pm i\varepsilon^{3/2}(c^2/4\omega_0)\,a_{3/2}`$, from the radical direction and its partner, a Jordan pair at order $`\varepsilon`$.

  Both are imaginary and Krein-positive there, with $`a_2 = 0.0038986\,R^2`$ and $`a_{3/2} = 0.05823\,R`$ in floating point. These rates and coefficients are diagnostics of the model, not derived here as asymptotics of the full linearization, and the type does not rest on them.

**At $`v_1`$**, in $`R_4`$ and $`R_5`$:
- *The germ.* $`\Gamma_u`$ contains the circle $`R_z(\theta)e^{i\theta}`$, which fixes $`v_1`$ and acts on $`v_m`$ with weight $`1 - m`$, and the half-turn about $`y`$ with charge conjugation, which fixes $`v_1`$ too. So $`E_0^u = \mathbb{R}v_1`$ and $`N_u^u = 0`$, and Lemma G′ gives the germ, with the circle in its isotropy; the Surviving Ray's §8.3 gives the same germ.
- *The decoupled sector.* The component of weight 4 is $`\mathbb{C}v_{-3}`$, which is $`K'`$, and the circle commutes with $`M_u`$ and $`i`$. So Theorem R′(c) applies, and that pair is imaginary for every small $`\varepsilon`$. Its $`\gamma_u`$ is $`-(19919/6697728)\,R^2`$ in $`R_4`$, Krein-negative, and $`(224487/41628563)\,R^2`$ in $`R_5`$, Krein-positive.
- *The other components.* There $`\widehat S_u`$ has its zero of multiplicity exactly $`4 = k + r_u`$ and the four simple negative roots of $`v_1`$'s slow polynomial in §IV, and $`J(v_1) \ne 0`$ keeps $`r_u = 1`$ along the branch. So Theorem R(e)'s hypotheses hold there, and the branch is spectrally stable at small amplitude in $`R_4`$ and $`R_5`$.

## IV. The Orbits

**Method.** The computations run in exact arithmetic, in weighted coordinates $`p_m = w_m/\sqrt{(j+m)!\,(j-m)!}`$, where the quartic, the metric, the generators and $`\Theta`$ are rational. For each orbit:
- criticality is checked exactly;
- the signature comes from the characteristic polynomial of $`\widehat M_u`$, by exact root counts;
- the type comes from the characteristic polynomial of $`\widehat S_u`$ in $`\nu = s^2`$: elliptic if and only if all its roots are negative reals;
- Krein-definiteness comes from the eigenvalues of $`\widehat M_u`$ on each cluster's invariant subspace, relative to the metric.

The representatives are written in orthonormal Condon–Shortley components $`v_m = \lvert j, m\rangle`$, unnormalized as in M8.12. $`R_5`$ is $`R_4`$ with $`q_J - 1`$ scaled by 9/16 (OpenWave's D7), so its signatures and types are $`R_4`$'s, with every slow eigenvalue scaled by exactly 9/16.

**$`R_4`$ and $`R_5`$, level 6.** The first ten rows are M8.12's census, which the computation reproduces in value and signature.

| orbit | representative | $`924\hat r_6`$ | $`(n_-, n_0, n_+)`$ | $`k, r_u`$ | slow flow | Theorem R |
| --- | --- | --- | --- | --- | --- | --- |
| coherent $`v_3`$ | $`v_3`$ | 1 | (0, 0, 10) | 3, 1 | elliptic, simple; Krein + | (c): spectrally and orbitally stable |
| $`v_2`$ | $`v_2`$ | 36 | (2, 0, 8) | 3, 1 | elliptic, simple; Krein 4+, 1− | (e): spectrally stable |
| prism | $`v_3 + \sqrt{23/10}\,v_0 + v_{-3}`$ | 8800/43 | (3, 0, 6) | 4, 4 | elliptic, one double frequency; Krein + | (e): spectrally stable |
| $`v_1`$ | $`v_1`$ | 225 | (4, 2, 4) | degenerate | not decided | none |
| D2 ray | $`v_2 + i\sqrt{6/5}\,v_0 + v_{-2}`$ | 225 | (5, 0, 4) | 4, 4 | hyperbolic, real pairs | (b): unstable |
| C3 ray | $`v_2 + 2v_{-1}`$ | 1188/5 | (5, 0, 4) | 4, 2 | hyperbolic, a complex quartet | (b): unstable |
| pyramid | $`\sqrt{12}\,v_3 + \sqrt{13}\,v_{-2}`$ | 1188/5 | (5, 0, 4) | 4, 2 | hyperbolic, a complex quartet | (b): unstable |
| octahedron | $`v_2 + v_{-2}`$ | 288 | (6, 0, 3) | 4, 4 | hyperbolic, real pairs | (b): unstable |
| zonal $`v_0`$ | $`v_0`$ | 400 | (8, 0, 2) | 3, 3 | hyperbolic, real pairs | (b): unstable |
| hexagon | $`v_3 + v_{-3}`$ | 463 | (9, 0, 0) | 4, 4 | elliptic, one double frequency; Krein − | (d): spectrally stable |
| third outside orbit | interval-certified | 238.35685474309527034553212338375… | (7, 0, 2) | 4, 2 | elliptic, simple | (e): spectrally stable |

- **Hypothesis (Z) where (e) is used.**
  - *Multiplicity.* The zero multiplicity of $`\widehat S_u`$ is $`k + r_u`$ at all three orbits: 4, 8 and 6.
  - *The radical along the branch.* By the formula for $`\Omega`$ on static vectors, the $`\Omega`$-radical of $`\ker A_\varepsilon`$ is the $`\sigma`$-radical of the orbit tangent at $`\varphi_\varepsilon`$. There $`\sigma(X_a\varphi, X_b\varphi) = -\frac{1}{2}\epsilon_{abc}J_c(\varphi)`$ for the rotation generators, and the phase direction pairs with none of them.
  - *At $`v_2`$ and the third outside orbit,* $`J(u) \ne 0`$, so $`J(\varphi_\varepsilon) \ne 0`$ for small $`\varepsilon`$ and the radical keeps its dimension.
  - *At the prism,* the isotropy contains the 3-fold rotation about $`z`$ and, with the phase $`-1`$, the half-turn about $`x`$, so $`J(\varphi_\varepsilon) = 0`$ along the branch by Lemma G, and the radical is all of $`\ker A_\varepsilon`$ throughout.
- **Krein at the prism.** On the double cluster, $`\tau^2 = 19066880/278420571`$, the invariant subspace is four-dimensional with an exact rational basis. The eigenvalues of $`\widehat M_u`$ on it, relative to the metric, are $`8895040/79001793`$ and $`1216/5031`$, each twice: definite, positive. On the simple pair, $`\tau^2 = 5770240/7913763`$, they are $`224/429`$ and $`25760/18447`$.
- **The slow frequencies** of the targets and controls, for unit $`u`$ in the $`h`$ normalization, given as $`\tau`$ where rational and as $`\tau^2`$ otherwise:
  - coherent $`v_3`$: $`\tau = 28/143,\ 56/429,\ 140/99,\ 112/39,\ 896/1287`$;
  - $`v_2`$: $`\tau = 56/1287`$ (Krein −), and $`112/143,\ 112/117,\ 224/143,\ 560/429`$ (Krein +);
  - prism: $`\tau^2 = 5770240/7913763`$, and $`19066880/278420571`$ twice;
  - hexagon: $`\tau^2 = 90160/61347`$, and $`501760/552123`$ twice;
  - octahedron: $`\nu = +250880/552123`$, three times;
  - zonal $`v_0`$: $`\nu = +250880/552123`$ twice, and $`\tau^2 = 62720/61347`$ twice.
- **The third outside orbit,** found numerically in M8.12's census probe, is certified. A Krawczyk box of radius $`10^{-60}`$ about an 80-digit point, on the system $`\nabla h = \lambda G p`$ with $`p^TGp = 1`$ and a slice normal to the orbit, contains exactly one critical point. Interval characteristic polynomials then fix:
  - the signature (7, 0, 2), from a nonzero coefficient of $`\mu^4`$ and Descartes' rule on real-rooted polynomials;
  - an orbit of dimension 4, from a nonzero minor;
  - $`\lVert J(u)\rVert^2 \in [0.0759489135688902862814, 0.0759489135688902862815]`$, so $`J(u) \ne 0`$ and $`r_u = 2`$;
  - a zero of $`\widehat S_u`$ of multiplicity exactly 6;
  - four simple negative roots in $`\nu`$, from certified sign changes.
- **The other two outside orbits** of the census probe are not certified, and nothing here uses them.
- **At $`v_1`$** (added 2026-10-14), the degenerate row is decided at second order: spectrally stable at small amplitude in $`R_4`$ and $`R_5`$, by Theorem R′(c) with Theorem R(e) off the component of weight 4 (§III). The pair of that component is imaginary for every small $`\varepsilon`$, Krein-negative in $`R_4`$ and Krein-positive in $`R_5`$.

**The other two outside orbits, added 2026-10-14.** The Surviving Ray certified both on 2026-09-23 ([§7.2](../../bedrock/files/surviving-ray.md)), each at one point inside the fixed set of its full isotropy: its $`\mathcal O_1`$ and $`\mathcal O_2`$. [`outside_orbits_check.py`](scripts/soft-slot-branches/outside_orbits_check.py) recertifies each on the full system, as the bullet above does for the third:
- the certificate's box centre in weighted coordinates, through $`w_k = \sqrt{720}\,p_{k-3}`$ for the certificate's binary-sextic coefficients $`w_k`$, two Newton steps on the slice system, and a Krawczyk box of radius $`10^{-60}`$;
- the value inside the certificate's enclosure, and the signature equal to §7.2's;
- the slow polynomial in $`\nu`$, with all four roots certified real and simple by sign changes.

| orbit | representative | $`924\hat r_6`$ | $`(n_-, n_0, n_+)`$ | $`k, r_u`$ | slow flow | Theorem R |
| --- | --- | --- | --- | --- | --- | --- |
| $`\mathcal O_1`$ | interval-certified | 215.77579250166841349523233893587… | (4, 0, 5) | 4, 2 | hyperbolic, one real pair | (b): spectrally unstable |
| $`\mathcal O_2`$ | interval-certified | 238.01652892561983471074380165289… | (6, 0, 3) | 4, 2 | hyperbolic, one real pair | (b): spectrally unstable |

- *What (b) rests on.* At each orbit, $`n_0 = 0`$, from the signature step's four zero eigenvalues of $`\widehat M_u`$ together with $`k = 4`$ from the Gram determinant, and a sign change of $`\det(\mu - \widehat S_u)`$ across the real pair, at $`\mu = \pm 0.2419314538\ldots`$ for $`\mathcal O_1`$ and $`\pm 0.03074313532\ldots`$ for $`\mathcal O_2`$, for unit $`u`$ in the $`h`$ normalization. It uses neither the zero multiplicity, 6, nor $`r_u = 2`$, which follows from $`J(u) \ne 0`$; those enter only (e).
- *The slow frequencies,* as in the list above: at $`\mathcal O_1`$, $`\nu = +0.05853082836\ldots`$ and $`\tau^2 = 0.9108404275\ldots,\ 0.05525518896\ldots,\ 0.001662568255\ldots`$; at $`\mathcal O_2`$, $`\nu = +0.0009451403698\ldots`$ and $`\tau^2 = 1.072108997\ldots,\ 0.09874229398\ldots,\ 0.001181574087\ldots`$.
- *The other slot.* In $`R_5`$ the types are the same, and each root in $`\nu`$ is $`R_4`$'s times 81/256.
- *The control.* The third outside orbit, rerun from its own certificate, reproduces claim I's row: its value, its signature, $`\lVert J(u)\rVert^2`$ and its four roots.

**$`R_2`$, level 7.** The points are the weight states and the interior critical points of the cyclic fixed lines, each line spanned by two weights alone. Three of the seven lines, $`\lbrace 5/2, -5/2\rbrace`$, $`\lbrace 7/2, -7/2\rbrace`$ and $`\lbrace 3/2, -3/2\rbrace`$, are $`Sp(1)`$ orbits of weight states, on which $`Q`$ is constant. The column "along the family" uses the members whose complex structure is $`j`$, $`k`$, $`(i + j)/\sqrt 2`$ or $`(i + k)/\sqrt 2`$.

| orbit | representative | $`Q`$ | $`(n_-, n_0, n_+)`$ | $`k, r_u`$ | slow flow at the point | along the family | Theorem R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| weight 7/2 | $`v_{7/2}`$ | 144/143 | (0, 0, 10) | 5, 1 | elliptic, simple; Krein + | definite | (c): spectrally and orbitally stable, along the family |
| weight 5/2 | $`v_{5/2}`$ | 168/143 | (4, 0, 6) | 5, 1 | elliptic | hyperbolic | (b): unstable members |
| weight 3/2 | $`v_{3/2}`$ | 224/143 | (8, 0, 2) | 5, 1 | elliptic | hyperbolic | (b): unstable members |
| weight 1/2 | $`v_{1/2}`$ | 168/143 | (4, 0, 6) | 5, 1 | hyperbolic | | (b): unstable |
| line {7/2, −5/2} | $`\sqrt{17/38}\,v_{7/2} + \sqrt{21/38}\,v_{-5/2}`$ | 369/247 | (6, 0, 3) | 6, 2 | hyperbolic | | (b): unstable |
| line {7/2, −3/2} | $`\sqrt{3/10}\,v_{7/2} + \sqrt{7/10}\,v_{-3/2}`$ | 22/13 | (9, 0, 0) | 6, 4 | elliptic; Krein − | definite | (d): spectrally stable along the family |
| line {7/2, −1/2} | $`\sqrt{5/12}\,v_{7/2} + \sqrt{7/12}\,v_{-1/2}`$ | 193/143 | (5, 0, 4) | 6, 2 | hyperbolic | | (b): unstable |
| line {5/2, −3/2} | $`\sqrt{3/4}\,v_{5/2} + \sqrt{1/4}\,v_{-3/2}`$ | 161/143 | (0, 3, 6) | degenerate | not decided | | none |

- **The weight-7/2 orbit is a strict local minimum** modulo its symmetry family, and $`\tau = 112/143,\ 168/143,\ 336/143,\ 504/143,\ 560/143`$.
- **At the {5/2, −3/2} point** (added 2026-10-14), the germ exists, pinned by its octahedral isotropy (Lemma G′, §II); its type is not decided.
- **Its type, at second order** (added 2026-10-14): $`\gamma_u = (115020/20333173)\,R^2 > 0`$ on its kernel, so the branch is spectrally and orbitally stable at small amplitude, along its family, by Theorem R′(b) (§III).
- **At the {7/2, −3/2} point,** $`J(u) = 0`$; one squared frequency is $`\tau^2 = 153664/20449`$, and the other two are the roots of $`418161601\,\nu^2 + 6989958976\,\nu + 28677390336`$, all Krein-negative.
- **The minimizer, on its own line.** In $`R_4`$ and $`R_5`$ the coherent orbit is the unique minimizer of $`Q`$, derived in the Slot Ground States, §IV, Proposition C3: $`q_6`$ is the strictly smallest coefficient, and $`f_6 = 1`$ exactly on coherent states. That proposition's small-charge limit identifies this branch with the ground states at small charge; nothing above uses it.

## V. What It Earns, and What It Does Not

**What it earns.**
- *Branches in the soft slots.* Lemma G with Theorem R(c) gives each soft slot a branch at small amplitude through a nondegenerate minimum of $`Q`$: the coherent orbit in $`R_4`$ and $`R_5`$, $`Q`$'s unique minimizer there, and the weight-7/2 orbit in $`R_2`$, a strict local minimum whose globality is Proposition C2, OPEN. Each branch is continuous in the frequency and orbitally stable relative to its stationary family, so both parts of the slot action's §VII protocol hold for it at small amplitude.
- *With Theorem B.* Every slot then carries an orbitally stable nonlinear branch, the five rigid slots and the control at every amplitude and the three soft slots at small amplitude. The label is M8.4's "nonlinear persistence of the installed free structure"; on OpenWave, the rung is a filing's to adjudicate.
- *The other orbits.* Every nondegenerate orbit in the tables has its germ and its small-amplitude spectral type.

**What it does not give.**
- Anything at finite amplitude: where a branch goes, whether ellipticity is lost, the spectrum along it, or its nonlinear persistence.
- The orbital stability of the maxima and saddles, for which (d) and (e) give spectral stability only.
- That the minimizing branches are the ground-state sets, which the Slot Ground States derives in $`R_4`$ and $`R_5`$ at small charge (Proposition C3) and which stays open in $`R_2`$.
- The degenerate orbits $`v_1`$ and $`R_2`$'s level 161/143.
- Completeness of either critical set.
- Any slot relation or physical particle state.

## VI. What Stays Open

- Finite amplitude, for every branch above. M8.15, a continuation and persistence run on these branches filed with OpenWave, froze its terms on 2026-10-07, before any target was run: SHA-256 `b21eed1a487dea27431ecc3336417fa558df3b9b848fcce6ba3def7dafcbe5e4`. They were first hashed the same day as `c079f2a06da86c73f5cbd79e732da725539bc91e6f517ff32a9603c0c3febc17`; the second hash escapes four pipes in one table row so that it renders, and changes no term. At the maintainer's request on OpenWave #618, the filed terms were revised on 2026-10-07, before the go and before any target was run, and re-hashed as `e0c32d01ba374a2efd758ab33466fcdc89836f17989baa8b401ef70f1012cca8`, which governs. Its solver and control records are pinned in `scripts/soft-slot-dynamics/`.
- **Note (2026-10-08), on M8.15's verdict.** The run was adjudicated on OpenWave [#620](https://github.com/openwave-labs/openwave/pull/620), per branch, with no aggregate verdict. Its record is [`RECORD.md`](https://github.com/dmobius3/mode-identity-theory/blob/28c8a7648a88c9234d32be753cbbe3563ea2eec3/files/framework/files/working/files/scripts/soft-slot-dynamics/RECORD.md) at MIT `28c8a76`. On the pinned finite-element mesh, under the frozen slot action:
  - **Elliptic:**
    - the prism in $`R_5`$ (T2/R5) at all 15 ladder points to $`\varepsilon = 32`$;
    - the hexagon in $`R_4`$ (T3/R4) at 17 of 18 to $`\varepsilon = 72`$;
    - the member of $`R_2`$'s orbit named in the terms (T5/R2), for that member only, at 17 of 20 to $`\varepsilon = 132`$.
  - **Hyperbolic:** the prism in $`R_4`$ (T2/R4) from $`\varepsilon = 32`$, and the hexagon in $`R_5`$ (T3/R5) from $`\varepsilon = 22.63`$. Each change lies in a bracket that passes through Unresolved points, between 11.31 and 32 and between 11.31 and 22.63, and is not located.
  - **Persistence:** all eight tests that ran Persist, each for its one registered direction.
  - **Instrument outcomes, with no finite-amplitude verdict:**
    - $`v_2`$ (T1) is INVALID at $`\varepsilon_{\min}`$ in both slots; in $`R_4`$ this rests on the instrument's 0.9 overlap classification alone;
    - the third outside orbit (T4) reached no ladder point in either slot.

  The record keeps the label "nonlinear persistence of the installed free structure", at the row 6 ceiling. These are the instrument's verdicts on one pinned mesh, so the first bullet's finite-amplitude question stays open as mathematics for every branch. M8.15 gives no verdict for $`v_2`$ or the third outside orbit, and the two changes of type stay unlocated.
- **Note (2026-10-11), on M8.15.1's terms.** M8.15.1, filed with OpenWave, locates the index changes on T2/R4 and T3/R5 inside M8.15's brackets and asks whether each is a change of type. It froze its terms on 2026-10-11, before any target was run: SHA-256 `fc566c0406fef33d0f2a4ef2540fc6ce841191d292e5767de28d13b617156dbf`. They are the locator's `TARGET1_TERMS.md` v7, as reshaped for filing. Its instrument, the M8.15.x solver, is frozen in `scripts/soft-slot-dynamics-m8-15x/`, and its locator in `scripts/soft-slot-dynamics-m8-15x-target1/`.
- **Note (2026-10-12), on M8.15.1's verdict.** The run was adjudicated on OpenWave [#625](https://github.com/openwave-labs/openwave/pull/625#pullrequestreview-5492753760). Its record is [`RECORD.md`](scripts/soft-slot-dynamics-m8-15x-target1/RECORD.md), committed at MIT `c4e2f7f`, with a post-adjudication note at its foot. No change of type is located.
  - **The prism in $`R_4`$ (T2/R4) and the hexagon in $`R_5`$ (T3/R5).** Each primary bracket holds a change of the genuine index by two inside its final interval at both levels: 16.2589 to 16.3107 and 16 to 16.8284 for the prism, 15.7803 to 15.7986 and 15.7071 to 16 for the hexagon. Neither is classified. The bisection's last midpoint fails the structural subspace check, so each reads "no genuine crossing detected", the frozen name for a bracket with no classified genuine step, which does not exclude a genuine crossing. The hexagon's level 3 also holds a structural step, at 13.1609.
  - **The hexagon's secondary bracket, 22.63 to 32.** Not located: the run's steps there join two solution paths, so it locates no index change along the branch.

  So the two changes of type M8.15 bracketed stay unlocated, and the first bullet's finite-amplitude question stays open.
- **Note (2026-10-13), on M8.15.2's terms.** M8.15.2, filed with OpenWave, asks whether the two primary index changes M8.15.1 left unclassified can be located through the structural-subspace failure that stopped their bisections: bracketed by `n(L)`, classified between clean ends, checked for solution continuity, and confirmed at the guard offsets. Its terms, a delta on M8.15.1's, froze on 2026-10-13, before any target was run: SHA-256 `c6da782b43bc13d256f445d822d6c1456d71b42a4b5771b054d0c6b344dd4e4d`. Its locator v2 is frozen in `scripts/soft-slot-dynamics-m8-15-2/`, at MIT `851b2ad`.
- **Note (2026-10-14), on M8.15.2's verdict.** The run was adjudicated on OpenWave [#632](https://github.com/openwave-labs/openwave/pull/632#pullrequestreview-5511519208). Its record is [`RECORD.md`](scripts/soft-slot-dynamics-m8-15-2/RECORD.md), committed at MIT `f1ebda7`, with a post-adjudication note at its foot. On the pinned finite-element mesh, at both levels:
  - **The hexagon in $`R_5`$ (T3/R5).** A change of type is located, between Elliptic at the 1% guard offset, 15.6356 at level 3 and 15.6752 at level 2, and Hyperbolic at the 5% offset, 16.5832 and 16.6252. The adjudicated name, in the terms' words: "A change of type is located between the registered guard readings. Its identification with the genuine index crossing at this step is not established: the crossing subspaces agree after removal of the structural directions, and the full spectral crossing identity remains unresolved. The step's classification crossed a structural-subspace or slowest-pair failure, or a point whose structural count fell below its side's, by a rule whose changed branch has synthetic controls only." Beside it: "The solution-continuity check does not certify which solution branch the step lies on, least of all where two branches share `m`."
  - **The prism in $`R_4`$ (T2/R4).** No change of type is located. Level 3 classifies a genuine step, 16.2589 to 16.2977, and level 2's step is Unresolved (index bookkeeping), so the levels disagree.

  So the hexagon's change of type, which M8.15 bracketed, is located on the pinned mesh, and its identification with the genuine crossing stays open; the prism's stays unlocated. The first bullet's finite-amplitude question stays open as mathematics.
- **Note (2026-10-14), on the outside orbits.** §IV says that the other two outside orbits of the census probe are not certified, and this section's last bullet lists the outside orbits not certified here. The Surviving Ray had certified all three on 2026-09-23 ([§7.2](../../bedrock/files/surviving-ray.md)): its $`\mathcal O_1`$ and $`\mathcal O_2`$, with signatures (4, 0, 5) and (6, 0, 3), and its $`\mathcal O_3`$, the third outside orbit of §IV. The small-amplitude type of $`\mathcal O_1`$ and $`\mathcal O_2`$, Theorem R at their certified points, is not computed here. [The Slot Dynamics Census](slot-dynamics-census.md) carries them as open rows.
- **Note (2026-10-14), on $`\mathcal O_1`$ and $`\mathcal O_2`$.** §IV's addition of the same day computes the type the note above leaves open: both are born hyperbolic in $`R_4`$ and $`R_5`$, Theorem R(b). Every outside orbit the Surviving Ray certified now has its type here, so the last bullet's second clause names none, and [The Slot Dynamics Census](slot-dynamics-census.md) closes their row.
- **Note (2026-10-14), on $`R_2`$'s level 161/143.** §II's Lemma G′, added the same day, gives that degenerate orbit a germ, pinned by its octahedral isotropy. §V's list and the last bullet still hold for its small-amplitude type, which needs the slow spectrum at order $`\varepsilon^2`$.
- **Note (2026-10-14), on the degenerate orbits at second order.** §III's Theorem R′, added the same day, decides both at small amplitude: $`v_1`$ is spectrally stable in $`R_4`$ and $`R_5`$, and $`R_2`$'s level 161/143 is spectrally and orbitally stable along its family, a second orbitally stable branch of $`R_2`$ at small amplitude, beside the weight-7/2 minimum. For both, §V's list and this section's last bullet now concern finite amplitude only.
- Proposition C2, the globality of $`R_2`$'s minimum 144/143. The first two Hermitian lifts of $`Q - 144/143`$, with multipliers $`\lVert w\rVert^2`$ and $`\lVert w\rVert^4`$, are not positive semidefinite, so that route certifies nothing.
- The degenerate orbits, and the outside orbits not certified here.

## References

- T. Kato, *Perturbation Theory for Linear Operators*, Classics in Mathematics, Springer (1995), [doi:10.1007/978-3-642-66282-9](https://doi.org/10.1007/978-3-642-66282-9). Riesz projections, and the reduction of an isolated eigenvalue group.
- R. Krawczyk, Newton-Algorithmen zur Bestimmung von Nullstellen mit Fehlerschranken, *Computing* **4**, 187–201 (1969), [doi:10.1007/BF02234767](https://doi.org/10.1007/BF02234767).
- **[M8.10]** OpenWave M8 track, M8.10: first correction at the level-6 critical rays. The [task record](https://github.com/openwave-labs/openwave/blob/b0b078678ca75ad31b8813806d6b61a0a386d1e0/openwave/xperiments/m8_mit/research/tasks/m8_10_task_details.md), with its frozen claims B1, B2 and C1, 2026.

## Files

In `scripts/soft-slot-branches/`:
- `branches_check.py`: the exact quartic in weighted coordinates, checked against the closed form; M8.12's ten census orbits in $`R_4`$ and $`R_5`$, and $`R_2`$'s weight states and line points; the $`Sp(1)`$ family test; the Krein certificate at the prism; the prism's isotropy; the interval certification of the third outside orbit; $`R_2`$'s constant lines; and the two lifts of $`Q - 144/143`$. Each claim has a mutation arm that turns it red. A few minutes.
- `branches_check.out`: its record.
- `outside_orbits_check.py` (added 2026-10-14): the other two outside orbits, and the third as the control, from the Surviving Ray's §7.2 certificates, with the certificate file checked against its folder's `SHA256SUMS`; Krawczyk on the slice system, then Theorem R by interval characteristic polynomials in $`R_4`$ and $`R_5`$. Each claim has a mutation arm that turns it red, and the exit status is 1 if a claim fails or an arm stays green. Under a minute.
- `outside_orbits_check.out`: its record.
- `germ_check.py` (added 2026-10-14): $`R_2`$'s degenerate line point in exact arithmetic over $`\mathbb{Q}(\sqrt 2, i)`$: its degeneracy, its octahedral isotropy, its one-dimensional fixed space, and the dihedral cross-check with its slice value 168/143. Each claim has a mutation arm that turns it red, and the exit status is 1 if a claim fails or an arm stays green. About ten seconds.
- `germ_check.out`: its record.
- `second_order_check.py` (added 2026-10-14): Lemma F's constants and levels, against binary-icosahedral characters, the projector onto $`2'`$ and OpenWave M8.10's frozen values; $`R_2`$'s degenerate point, its kernel, its isotropy group and $`\gamma_u`$; $`v_1`$'s circle and its $`\gamma_u`$ in $`R_4`$ and $`R_5`$; and a floating-point model of the slow problem, with its effective problem on the generalized kernel. Each claim has a mutation arm that turns it red, and the exit status is 1 if a claim fails or an arm stays green. Under a minute.
- `second_order_check.out`: its record.

In `scripts/soft-slot-dynamics/`, M8.15's solver, frozen before any target was run, with its control records and the run's record:
- `m8_15_solver/`: the finite-element solver, the branch driver and the control runs; `out/MANIFEST.json` holds the SHA-256 of every file the run executes, with the environment the controls ran in.
- `m8_15_math/`: the check that prints the third outside orbit's frozen frequencies and Krein signs from the certified point in `branches_check.py`, with its record.
- `REPRODUCE.md`: the reproduction route. `SHA256SUMS` pins every file of the freeze; the guard file and the run's records, added with the record, are not in it.
- `RECORD.md`: M8.15's per-branch record, adjudicated on OpenWave #620. The branch records, run logs, persistence records and post-run diagnostics are in `m8_15_solver/out/`.

In `scripts/soft-slot-dynamics-m8-15x/`, the M8.15.x solver: M8.15's solver revised, and qualified before any of its targets ran.
- `m8_15x_solver/`: the solver; `out/MANIFEST.json` holds the SHA-256 of every file it runs.
- `qualification/`: the qualification's record, with its README.
- `REPRODUCE.md`: the reproduction route. `SHA256SUMS` pins every file of the freeze. The guard file `m8_15x_solver/out/FROZEN.json`, written before M8.15.1's run, is outside it, and M8.15.1's `RECORD.md` gives its SHA-256.

In `scripts/soft-slot-dynamics-m8-15x-target1/`, M8.15.1's locator, frozen after its tests and before any target was run: its code and tests, its registration `REGISTER_4.md`, its results `RESULT_4.md` and their records. `REPRODUCE.md` is the reproduction route, and `SHA256SUMS` pins every file frozen before the run. The run's files came after:
- `RECORD.md`: M8.15.1's record, adjudicated on OpenWave #625, with a post-adjudication note at its foot. It lists the target records, run logs and pre-run record in `out/` with their SHA-256.
- `record_frozen_check_postrun_2026-10-12.out` and `environment_postrun_2026-10-12.txt`: the two dated post-run verifications the note describes.

In `scripts/soft-slot-dynamics-m8-15-2/`, M8.15.2's locator v2, frozen after its tests and before any target was run: its code and tests, its registration `REGISTER_5.md`, its results `RESULT_5.md` and their records, the adjudication reading `adjudicate.py`, and in `scope/` the scope memo with its numbers. `REPRODUCE.md` is the reproduction route, and `SHA256SUMS` pins every file frozen before the run. The run's files came after:
- `RECORD.md`: M8.15.2's record, adjudicated on OpenWave #632, with a post-adjudication note at its foot. It lists the target records, run logs, pre-run record and guard file in `out/` with their SHA-256.
- `tools/check_target_records.py` and `tools/check_record.py`, with their outputs, and three dated post-run files: the checks the record describes.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
