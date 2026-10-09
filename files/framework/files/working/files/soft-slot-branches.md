<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Soft-Slot Branches

**Type:** Result
**State:** Closed
**Status (2026-10-06):** Derived. In the soft slots R2, R4 and R5, every critical orbit of the reduced quartic that is nondegenerate modulo the stationary symmetry group continues to a branch of standing waves at small amplitude (Lemma G). Along such a branch the small-amplitude linear spectrum is read off the reduced quartic (Theorem R). A slow eigenvalue off the imaginary axis makes the branch unstable. A nondegenerate minimum gives a branch that is spectrally stable and orbitally stable relative to its stationary family. A nondegenerate maximum gives a spectrally stable branch. An indefinite orbit gives one when its slow flow is elliptic with Krein-definite frequencies and its zero modes are accounted for exactly. Exact arithmetic, and interval arithmetic for one orbit, classifies M8.12's census in R4 and R5, one further orbit there, and R2's fixed-line points. Nothing is claimed at finite amplitude. The globality of R2's minimum, Proposition C2 of the Slot Ground States, stays OPEN.
**Summary:** Branch existence and the small-amplitude linear spectrum at the soft slots' critical orbits, with the orbits computed exactly.
**Inputs:** `slot-action.md` (§V, §VII, §IX), `slot-ground-states.md` (§I, §IV, Theorem D), OpenWave's M8.12 census record (the orbit list and representatives) at `344f416`, `scripts/soft-slot-branches/`
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
- Proposition C2, the globality of $`R_2`$'s minimum 144/143. The first two Hermitian lifts of $`Q - 144/143`$, with multipliers $`\lVert w\rVert^2`$ and $`\lVert w\rVert^4`$, are not positive semidefinite, so that route certifies nothing.
- The degenerate orbits, and the outside orbits not certified here.

## References

- T. Kato, *Perturbation Theory for Linear Operators*, Classics in Mathematics, Springer (1995), [doi:10.1007/978-3-642-66282-9](https://doi.org/10.1007/978-3-642-66282-9). Riesz projections, and the reduction of an isolated eigenvalue group.
- R. Krawczyk, Newton-Algorithmen zur Bestimmung von Nullstellen mit Fehlerschranken, *Computing* **4**, 187–201 (1969), [doi:10.1007/BF02234767](https://doi.org/10.1007/BF02234767).

## Files

In `scripts/soft-slot-branches/`:
- `branches_check.py`: the exact quartic in weighted coordinates, checked against the closed form; M8.12's ten census orbits in $`R_4`$ and $`R_5`$, and $`R_2`$'s weight states and line points; the $`Sp(1)`$ family test; the Krein certificate at the prism; the prism's isotropy; the interval certification of the third outside orbit; $`R_2`$'s constant lines; and the two lifts of $`Q - 144/143`$. Each claim has a mutation arm that turns it red. A few minutes.
- `branches_check.out`: its record.

In `scripts/soft-slot-dynamics/`, M8.15's solver, frozen before any target was run, with its control records and the run's record:
- `m8_15_solver/`: the finite-element solver, the branch driver and the control runs; `out/MANIFEST.json` holds the SHA-256 of every file the run executes, with the environment the controls ran in.
- `m8_15_math/`: the check that prints the third outside orbit's frozen frequencies and Krein signs from the certified point in `branches_check.py`, with its record.
- `REPRODUCE.md`: the reproduction route. `SHA256SUMS` pins every file.
- `RECORD.md`: M8.15's per-branch record, adjudicated on OpenWave #620. The branch records, run logs, persistence records and post-run diagnostics are in `m8_15_solver/out/`.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
