<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# 🧮 The Hamiltonian–Krein Identification

**Type:** Result
**State:** Closed
**Status (2026-10-15):** Derived. On a branch of standing waves of the slot action with its symmetry exact, the number of unstable and Krein-negative eigenvalues, k_r + 2k_c + 2k_i⁻, equals n(L) − n(D): the stationary operator's negative index less the energy's negative index on the generalized kernel (Theorem K). M8.15's instrument reads that number as its genuine index h wherever its structural cluster spans the generalized kernel, and the number changes only where eigenvalues of the linearization pass through zero. At a transversal genuine crossing of the stationary operator, where the family's own Jordan structure stays regular, the symplectic form on the whole kernel sorts the crossing directions three ways (Theorem C): an Ω-nondegenerate pair passes through zero imaginary and reverses its Krein sign; a radical direction reaching into the crossing moves a pair between real and imaginary there; a direction paired with the family's own radical moves no eigenvalue, while n(L) and n(D) change together. So the census's step 2 holds in its first sentence, on that reading of h, and its second needs a qualifier: such a crossing moves a pair between real and imaginary only through the second case. Checked on two-dimensional models and on a perturbed model at R2's degenerate point, where the three cases occur at different members of its family. The pitchfork at a crossing, and the identification of T3/R5's located change, stay open.
**Summary:** The Hamiltonian–Krein count on the slot fields' standing-wave branches with exact symmetry, where it can move, and which genuine crossings of the stationary operator change the type there.
**Inputs:** `soft-slot-branches.md` (§III, Theorem R′), `slot-dynamics-census.md` (§V), M8.15's verdict module and M8.15.1's REGISTER_4 (the instrument's h), `scripts/hamiltonian-krein-identification/`
**Parent:** `slot-dynamics-census.md`

---

RESULT, a derivation with no pre-committed pass condition. [The Slot Dynamics Census](slot-dynamics-census.md) asks, as its step 2, for the argument that ties a change of type to a genuine zero crossing of the stationary operator once the symmetry is exact. This page proves the count that argument rests on, shows that a genuine crossing, where the family's own Jordan structure stays regular, changes the type in only one of three cases, and states the test that tells them apart. It gives no verdict on any run: the finite-element records stay as adjudicated.

**Related:** [The Soft-Slot Branches](soft-slot-branches.md), [The Slot Dynamics Census](slot-dynamics-census.md).

## I. The Setting

Take a branch of standing waves $`e^{i\omega_\varepsilon T}\varphi_\varepsilon`$ of the slot action, for $`\varepsilon`$ in an interval and at any amplitude, with its stationary symmetry group $`\Gamma`$ acting exactly. Its linearization is Theorem R's first-order system ([The Soft-Slot Branches, §III](soft-slot-branches.md#iii-the-small-amplitude-spectrum)), whose form, energy and symplectic form need no smallness: $`\dot x = A_\varepsilon x`$ for $`x = (\zeta, \partial_T\zeta)`$, Hamiltonian for $`\Omega`$, with

```math
B(x, x) = \lVert\partial_T\zeta\rVert^2/c^2 + \langle L_\varepsilon\zeta, \zeta\rangle, \qquad \Omega(A_\varepsilon x, y) = B(x, y).
```

The setting is the energy space $`\mathcal H = H^1 \times L^2`$. There $`B`$ and $`\Omega`$ are bounded forms, and $`\Omega`$ is only weakly nondegenerate: it does not map $`\mathcal H`$ onto its dual. $`A_\varepsilon`$ is closed and densely defined, with domain $`H^2 \times H^1`$, which $`\mathcal H`$ contains compactly, so $`A_\varepsilon`$ has compact resolvent. The potential of $`L_\varepsilon`$ is bounded, since $`\varphi_\varepsilon \in H^2 \subset L^\infty`$, so $`L_\varepsilon \ge -C`$ for some constant $`C`$; with its compact resolvent, $`L_\varepsilon`$ has finitely many negative eigenvalues and a finite-dimensional kernel. Second-order-in-time problems can also be treated as quadratic pencils [SS12]; the first-order form needs no restriction on the number of negative eigenvalues. Write:
- $`n(L_\varepsilon)`$ for the number of negative eigenvalues of $`L_\varepsilon`$; $`n(B) = n(L_\varepsilon)`$, since the kinetic term is positive and decoupled;
- $`V_0`$ for the generalized kernel of $`A_\varepsilon`$. Its kernel is the static vectors $`(\zeta, 0)`$ with $`L_\varepsilon\zeta = 0`$; at a regular point that is the tangent space $`T_\varepsilon`$ of the stationary family, which in $`R_2`$ includes the $`Sp(1)`$ directions, static solutions though not symmetries of the rotating frame;
- $`D`$ for the form $`B`$ on $`V_0`$, and $`n(D)`$ for its number of negative directions. It vanishes against $`\ker A_\varepsilon`$, since $`B(x, y) = \Omega(A_\varepsilon x, y)`$. Taking all of $`V_0`$ covers Jordan chains of any length, and those through the static $`Sp(1)`$ directions;
- $`K = k_r + 2k_c + 2k_i^-`$, where $`k_r`$ counts the positive real eigenvalues of $`A_\varepsilon`$, $`k_c`$ those with positive real and imaginary parts, and $`k_i^-`$ the negative directions of the Hermitian form $`B(\bar v, w)`$ on the generalized eigenspaces of the eigenvalues $`i\tau`$ with $`\tau > 0`$, all with multiplicity.

In $`R_2`$ each member of an orbit's $`Sp(1)`$ family has its own complex structure ("Families in $`R_2`$", there), and so its own $`A_\varepsilon`$, $`\Omega`$, $`V_0`$ and $`D`$, while its $`L_\varepsilon`$ is the same up to conjugation.

## II. The Count

**Theorem K.** At every $`\varepsilon`$,

```math
k_r + 2k_c + 2k_i^- = n(L_\varepsilon) - n(D).
```

*Proof.* A finite-dimensional reduction, with its complement controlled.
- *Large eigenvalues are imaginary and Krein-positive.* If $`A_\varepsilon x = \lambda x`$, then $`x = (\zeta, \lambda\zeta)`$ and $`B(\bar x, x) = (\lvert\lambda\rvert^2/c^2)\lVert\zeta\rVert^2 + \langle L_\varepsilon\zeta, \zeta\rangle \ge (\lvert\lambda\rvert^2/c^2 - C)\lVert\zeta\rVert^2`$. $`A_\varepsilon`$ is skew for $`B`$, $`B(A_\varepsilon x, y) = -B(x, A_\varepsilon y)`$, so generalized eigenspaces of $`\lambda`$ and $`\mu`$ are $`B`$-orthogonal unless $`\lambda + \bar\mu = 0`$: $`B(\bar x, x) = 0`$ when $`\mathrm{Re}\,\lambda \ne 0`$, and also for an eigenvector that heads a Jordan chain. So every eigenvalue with $`\lvert\lambda\rvert^2 > c^2C`$ is imaginary, semisimple and Krein-positive.
- *The split.* Take a radius $`r_0 > c\sqrt C`$ with no eigenvalue on its circle. The spectral subspace $`X_f`$ of the eigenvalues inside it is finite-dimensional, by the compact resolvent, and holds every eigenvalue off the imaginary axis, every Krein-negative direction, and $`V_0`$. The spectral subspace $`X_\infty`$ of the rest is invariant, and $`B`$- and $`\Omega`$-orthogonal to $`X_f`$, since no eigenvalue $`\lambda`$ inside and $`\mu`$ outside satisfy $`\lambda + \bar\mu = 0`$.
- *The complement is positive.* $`B`$ has finitely many negative squares and is coercive off finitely many directions, and its kernel, $`\ker A_\varepsilon`$, lies in $`X_f`$, so $`X_\infty`$ with $`B`$ is a Pontryagin space. If $`B`$ had a negative direction there, Pontryagin's theorem [IKL82, ch. II], applied to the bounded resolvent $`(A_\varepsilon - \zeta)^{-1}`$ on $`X_\infty`$ for an imaginary $`\zeta`$ off the spectrum, a scalar multiple of which is self-adjoint for $`B`$, would give a nonzero invariant subspace on which $`B \le 0`$, and in it an eigenvector with $`B(\bar x, x) \le 0`$, which the first step excludes.
- *The finite part.* On $`X_f`$, $`\Omega`$ is nondegenerate, being weakly nondegenerate on $`\mathcal H`$ and $`\Omega`$-orthogonal to $`X_\infty`$, and $`A_\varepsilon`$ is a Hamiltonian matrix. $`B`$ adds over its generalized eigenspaces, grouped by $`\lambda + \bar\mu = 0`$: each real pair contributes one, each quartet two, each imaginary pair twice its negative Krein directions, and $`V_0`$ contributes $`n(D)`$. So $`n(B\vert X_f) = n(D) + K`$, and $`n(L_\varepsilon) = n(B) = n(B\vert X_f) + n(B\vert X_\infty) = n(D) + K`$.

The identity is the Hamiltonian–Krein index theorem [KKS04, Pel05; KP13, ch. 7], here in the energy space of the slot action. The decomposition is $`B`$-orthogonal at every $`\varepsilon`$, so the identity holds where $`D`$ is degenerate too.

- *The instrument's genuine index.* M8.15's verdict module tracks a structural cluster $`G_{\mathrm{tol}}`$, chosen by structure and a tolerance with a frozen algebraic dimension $`k + r_u`$: the fibre vectors with the phase's Jordan partner, and the lifted rotation modes with their partners. It checks the count against $`n(L) - n(B\vert G_{\mathrm{tol}})`$, which M8.15.1's register calls the genuine index $`h`$ ([REGISTER_4](scripts/soft-slot-dynamics-m8-15x-target1/REGISTER_4.md)). In an instrument with the symmetry exact, at a regular point where the cluster is verified to span $`V_0`$, $`n(B\vert G_{\mathrm{tol}}) = n(D)`$ and $`h = K`$. A matching dimension, with no other eigenvalue within the cluster's tolerance, does not by itself establish the span, which must be checked. At a crossing $`V_0`$ is larger than the structural cluster, so $`h`$ is read on either side of it, not at the point. Where the cluster spans $`V_0`$, the genuine index is the count, and taking $`n(D)`$ from it again would remove the structure twice.
- *Where it moves.* $`K`$ counts the eigenvalues in the open right half-plane, plus twice the negative Krein directions on the imaginary axis. A Krein collision at nonzero frequency trades a Krein-negative imaginary pair for a quartet, and a collision on the real axis trades a quartet for two real pairs; neither changes $`K`$. So $`K`$ changes only where eigenvalues of $`A_\varepsilon`$ pass through zero: at a genuine crossing of $`L_\varepsilon`$ (§III, cases 1 and 2), or where the family's own Jordan structure degenerates, as in the Vakhitov–Kolokolov mechanism, with or without a crossing at the same point; this page does not analyse that, and Theorem C excludes it at its crossing. With $`h`$ read where its cluster spans $`V_0`$, this proves the census's step 2 first sentence. At a crossing of §III's case 3, $`n(L_\varepsilon)`$ and $`n(D)`$ change together and $`K`$ does not.

## III. The Crossing

**Theorem C (a transversal genuine crossing).** Suppose that $`\varepsilon \mapsto \varphi_\varepsilon`$ is $`C^2`$ into $`H^2`$, so that $`A_\varepsilon`$ is a $`C^2`$ family of bounded perturbations of one closed operator, and that at $`\varepsilon_*`$:
- $`\ker L_{\varepsilon_*} = T_* \oplus Z`$, with $`T_*`$ the stationary family's tangent space, of constant dimension near $`\varepsilon_*`$, and $`Z`$ of dimension $`d \ge 1`$, while for $`\varepsilon \ne \varepsilon_*`$ near it the kernel of $`L_\varepsilon`$ is the family's tangent;
- the crossing form $`L' = P_Z(\partial_\varepsilon L_\varepsilon)P_Z`$ at $`\varepsilon_*`$ is definite on $`Z`$, so the $`d`$ eigenvalues through zero cross in one direction.

Let $`\sigma`$ be $`\Omega`$ on static vectors, $`R_T`$ the $`\sigma`$-radical of $`T_*`$, $`\mathrm{Rad}`$ the $`\sigma`$-radical of $`T_* \oplus Z`$, and $`R_3`$ a complement of $`R_T \cap \mathrm{Rad}`$ in $`R_T`$. Each $`s \in R_T \cap \mathrm{Rad}`$ has a partner $`p_s`$ with $`A_{\varepsilon_*}p_s = (s, 0)`$, in the family's own Jordan blocks. Suppose the family's Jordan structure is regular through $`\varepsilon_*`$:
- $`\sigma`$ has constant rank on the family's tangent spaces near $`\varepsilon_*`$;
- the matrix $`\Pi_T`$ of the energies of the partners $`p_s`$ is nondegenerate.

This excludes a degeneracy of the family's own blocks at the crossing, and makes the family's block, its tangent space less $`R_3`$ with the partners $`p_s`$, $`\Omega`$-nondegenerate (see the proof). $`Z`$ is fixed only up to vectors of $`T_*`$, so choose it in the block's $`\Omega`$-complement, split as $`Z = Z_1 \oplus Z_2 \oplus Z_3`$, with:
- $`Z_3`$ paired nondegenerately with $`R_3`$ by $`\sigma`$; its dimension $`d_3`$ is the rank of $`\sigma`$ between $`R_T`$ and $`Z`$;
- $`Z_2`$ inside $`\mathrm{Rad}`$, of dimension $`d_2 = \dim\mathrm{Rad} - \dim(\mathrm{Rad} \cap T_*)`$;
- $`Z_1`$ the rest, $`\sigma`$-orthogonal to $`T_*`$, $`Z_2`$ and $`Z_3`$, of dimension $`d_1 = d - d_2 - d_3`$; $`\sigma`$ is nondegenerate on it.

Each $`z \in Z_2`$ has a partner $`p`$ with $`A_{\varepsilon_*}p = (z, 0)`$, which can be taken in the same complement. Suppose the matrix $`\Pi`$ of these partners' energies is nondegenerate, and write $`W`$ for the pairing $`\Omega(z, p)`$. Then, for $`\delta = \varepsilon - \varepsilon_*`$ small, the eigenvalues of $`A_\varepsilon`$ near zero are the family's, which stay at zero, and:
- **Case 1, a Krein flip.** $`d_1`$ eigenvalues $`\delta\mu + O(\delta^2)`$, for simple $`\mu`$, imaginary on both sides, with $`\mu`$ the eigenvalues of the Hamiltonian matrix, relative to $`\sigma`$, of the Schur complement of $`L'`$ on $`Z_1 \oplus Z_2`$ onto $`Z_1`$. Their Krein signs reverse at $`\varepsilon_*`$, and $`K`$ changes by $`\pm d_1`$.
- **Case 2, a change between real and imaginary.** $`d_2`$ pairs with $`\lambda^2 = \delta\nu + O(\delta^{3/2})`$, for simple $`\nu`$, with $`\nu`$ the eigenvalues, real and nonzero, of $`-L'`$ on $`Z_2`$ relative to the form $`W\Pi^{-1}W^{\mathsf T}`$. Each pair is real on the side where $`\delta\nu > 0`$, and imaginary on the other with the Krein sign of its partner's energy, and each changes $`K`$ by $`\pm 1`$.
- **Case 3, absorbed by the family.** No eigenvalue from $`Z_3`$ leaves zero. Its directions change $`n(L_\varepsilon)`$ and $`n(D)`$ by $`d_3`$ each, as the partners of $`R_3`$ grow like $`1/\delta`$ and their energies change sign, so they leave $`K`$ unchanged.

*Proof.*
- *The reduction.* Near $`\varepsilon_*`$ the Riesz projection onto the eigenvalues of $`A_\varepsilon`$ in a small disc about zero is $`C^2`$ in $`\varepsilon`$ [Kato], and its range is invariant, of fixed dimension and $`\Omega`$-nondegenerate (Lemma S's argument, there). Transported to a fixed space, the problem is exactly a $`C^2`$ family of Hamiltonian matrices of fixed size: the eigenvalues of $`A_\varepsilon`$ near zero are theirs, with nothing truncated.
- *The family's block.* The tangent space less $`R_3`$, with the partners $`p_s`$, is invariant, with only zero eigenvalues. $`\sigma`$ is nondegenerate on $`T_*`$ modulo $`R_T`$, and $`\Omega`$ pairs $`R_T \cap \mathrm{Rad}`$ with the partners through $`\Pi_T`$, since $`\Omega(s, p_{s'}) = \Omega(A_{\varepsilon_*}p_s, p_{s'}) = B(p_s, p_{s'})`$; so the block is $`\Omega`$-nondegenerate exactly when $`\Pi_T`$ is. Near $`\varepsilon_*`$, by the first half of the regularity hypothesis, $`R_T \cap \mathrm{Rad}`$ continues with constant dimension. Its partners continue with bounded components along $`Z`$, since $`\sigma`$ vanishes between $`R_T \cap \mathrm{Rad}`$ and $`Z`$, and a kernel component leaves their pairing with $`R_T \cap \mathrm{Rad}`$ unchanged, so $`\Pi_T`$ is continuous. By the second half the block then stays $`\Omega`$-nondegenerate, of constant dimension, and it splits off $`\Omega`$-orthogonally, with an invariant complement. Its eigenvalues stay at zero.
- *The crossing directions.* A static kernel vector pairs with the block only through $`\sigma`$ on $`T_*`$ modulo $`R_T`$ and through $`\Omega`$ against the partners $`p_s`$. Adding vectors of $`T_*`$ cancels both, the second because $`\Pi_T`$ is nondegenerate, so $`Z`$ and $`R_3`$ can be taken in the complement. The split of $`Z`$ is possible because $`\sigma`$ is nondegenerate on $`T_*`$ modulo $`R_T`$ and pairs $`Z_3`$ with $`R_3`$ nondegenerately. Each partner of $`Z_2`$ can be taken in the complement, which is invariant, and, being fixed there only up to the kernel, $`\Omega`$-orthogonal to $`Z_1`$ and to $`R_3`$. For a nonzero eigenvalue the eigenvector is $`\Omega`$-orthogonal to $`\ker A_\varepsilon`$, as in Lemma S, so the row of each $`t \in R_3`$ reads $`\sigma(t, z)x_z = O(\delta)\,x`$, which puts the components along $`Z_3`$ at higher order in both cases.
- *Case 3.* For $`t \in R_3`$ paired with $`z \in Z_3`$, the energy on $`\mathrm{span}\lbrace t, z\rbrace`$ is $`\mathrm{diag}(0, \delta L'(z, z))`$ to leading order, so $`A_\varepsilon`$ is nilpotent there, with $`A_\varepsilon z`$ a multiple of $`t`$, and no eigenvalue moves. The partner of $`t`$ is $`z\,\Omega(t, z)/(\delta L'(z, z))`$ up to sign, with energy $`\Omega(t, z)^2/(\delta L'(z, z))`$, which changes sign with $`\delta`$, as the eigenvalue of $`L_\varepsilon`$ along $`z`$ does.
- *Case 2.* For $`\lambda`$ of order $`\delta^{1/2}`$, the partners' rows give $`x_p = \lambda\Pi^{-1}W^{\mathsf T}x_{Z_2}`$ to leading order, the rows of $`Z_1`$ give $`x_{Z_1}`$ of order $`\delta^{1/2}x_{Z_2}`$, and the rows of $`Z_2`$ then give $`(\delta L'_{Z_2} + \lambda^2 W\Pi^{-1}W^{\mathsf T})x_{Z_2} = 0`$. The pencil has a definite form, so $`\nu`$ is real. On the imaginary side the energy on the pair's invariant plane is definite, with the sign of the partner's energy.
- *Case 1.* For $`\lambda`$ of order $`\delta`$, the rows of $`Z_2`$ give $`x_{Z_2} = -(L'_{Z_2})^{-1}L'_{Z_2 Z_1}x_{Z_1} + O(\delta)`$, and the rows of $`Z_1`$ then give $`(\delta S_1 + \lambda\,\sigma_{Z_1})x_{Z_1} = 0`$, with $`S_1`$ the Schur complement. $`S_1`$ is definite, so the eigenvalues are imaginary, and replacing $`\delta`$ by $`-\delta`$ reverses the energy, and with it the Krein signs.
- *The remainders.* Substituting $`\lambda = \delta\mu`$ in case 1, and $`\lambda = \delta^{1/2}\rho`$ in case 2, and dividing the reduced characteristic polynomial by the power of $`\delta`$ it carries, leaves $`\det(S_1 + \mu\,\sigma_{Z_1}) + O(\delta)`$ and $`\det(L'_{Z_2} + \rho^2 W\Pi^{-1}W^{\mathsf T}) + O(\delta^{1/2})`$. Simple roots persist with those errors, by the implicit function theorem, which gives the stated bounds.
- *The counts.* Across $`\varepsilon_*`$, $`n(L_\varepsilon)`$ changes by $`d`$, and $`n(D)`$ by $`d_3`$, since the family's part of $`D`$ keeps its inertia, $`\Pi_T`$ being continuous and nondegenerate. So $`K`$ changes by $`d_1 + d_2`$, all with the sign of the crossing, which is Theorem K on both sides.

**An indefinite crossing form.** If $`L'`$ is indefinite on $`Z`$, the same reduction applies with the Schur complements as they come: case 1's eigenvalues keep their type across $`\varepsilon_*`$, with their Krein signs reversed, but need not be imaginary, and case 2's $`\nu`$ need not be real. This page claims and checks only the definite case.

**A degenerate family.** Each half of the regularity hypothesis is needed. In $`\ddot z + 2J\dot z + L(t)z = 0`$ on $`\mathbb R^3`$, with energy $`\lvert\dot z\rvert^2 + \langle Lz, z\rangle`$, $`Je_1 = e_2`$, $`Je_2 = -e_1`$, $`Je_3 = 0`$ and $`L(t) = \mathrm{diag}(0, t - 4, t)`$, the family's tangent is the line of $`e_1`$, and $`e_3`$ crosses at $`t = 0`$ with $`L' = 1`$, in case 2 with $`d_2 = 1`$. But the partner of $`e_1`$ has energy $`t/(t - 4)`$, which vanishes at $`t = 0`$, and $`\det(\lambda^2 + 2\lambda J + L(t)) = \lambda^2(\lambda^2 + t)^2`$: two pairs change between real and imaginary there, not one. With $`2tJ`$ in place of $`2J`$ and $`L(t) = \mathrm{diag}(0, 0, t)`$, the family's tangent is the plane of $`e_1`$ and $`e_2`$ and $`\Pi_T`$ is nondegenerate, but $`\sigma`$ drops rank on it at $`t = 0`$, and a pair $`\pm 2it`$ passes through zero there besides case 2's.

## IV. The Identification

**Corollary I.** Suppose a bracket of $`\varepsilon`$ holds one crossing as in Theorem C and no other point where eigenvalues of $`A_\varepsilon`$ pass through zero. Then:
- the pairs that change between real and imaginary through zero inside the bracket are case 2's $`d_2`$ pairs, all at $`\varepsilon_*`$, on the sides Theorem C gives;
- if $`d_2 = 0`$, no pair changes between real and imaginary at $`\varepsilon_*`$, and a change of type inside the bracket comes from a Krein collision or a collision on the real axis, away from zero;
- if $`d_2 > 0`$ and the rest of the spectrum is elliptic on the imaginary side of those pairs, the crossing is a change of type at $`\varepsilon_*`$.

So the census's step 2 holds in its first sentence, with $`h`$ read as §II says, and its second, as written, does not follow. A genuine crossing with $`\Delta h = \pm 2`$ can be a case 1 Krein flip, with no change of type, and a Krein collision elsewhere in the same bracket then gives a change of type with $`\Delta h = \pm 2`$ that does not sit at the crossing. What holds is Corollary I: a genuine crossing as in Theorem C moves a pair between real and imaginary at the crossing only through case 2, which is a change of type when the rest of the spectrum is elliptic.

- *The test.* For an instrument with the symmetry exact, the identification test is Theorem C's decomposition at the crossing: $`\Omega`$ on the whole kernel, the family's directions included, with the signs of $`L'`$ and of the partners' energies, and the regularity of the family's Jordan structure. It is not the identity of the crossing vectors at two ends, which M8.15.2 compared. Restricting $`\Omega`$ to the crossing directions alone mistakes case 3 for case 2 (§V).
- *What it does not decide.* It does not identify T3/R5's located change. That needs the decomposition at its crossing, which the finite-element instrument, with the symmetry broken, cannot give. Its counts, Elliptic below and Hyperbolic above with $`h`$ falling from 6 to 4, fit case 2 for a doublet whose partners have negative energy, where Krein-negative pairs turn real as $`n(L)`$ falls. Its near-zero spectra point the same way. Fitted on the three clean points nearest the crossing on each side, at level 3 the doublet's $`\lvert\lambda\rvert^2`$ is linear in $`\varepsilon`$ on both sides, with slopes $`4.82\times10^{-4}`$ and $`4.83\times10^{-4}`$ and zeros at 15.7955 and 15.7929, imaginary and Krein-negative below and real above, and the record finds no quartet between the readings. A case 1 flip keeps its pair imaginary on both sides, so its real doublet would need a quartet that no evaluated point shows. The same fit puts the zeros above each level's $`n(L)`$ ends, by 0.003 to 0.006 at level 3 and 0.06 to 0.11 at level 2, which is why the identification stays open (INFERRED, from the finite-element spectra with the symmetry broken).

## V. The Checks

[`identification_check.py`](scripts/hamiltonian-krein-identification/identification_check.py), in floating point at 50 digits:
- **Two-dimensional models.** $`B = tI`$ (case 1), $`B = \mathrm{diag}(t, \pm 1)`$ (case 2) and $`B = \mathrm{diag}(0, t)`$ with its first direction a family radical (case 3): the sizes, $`\lvert t\rvert`$ and $`\lvert t\rvert^{1/2}`$, the sides, the Krein signs, the pole $`1/t`$ of case 3's partner energy, and Theorem K at every point.
- **$`R_2`$'s degenerate point.** A perturbed model, not a crossing observed along a branch. The Hessian of the reduced function at the germ, with kernel $`K_u \oplus K'`$, the symplectic forms and the family are $`R_2`$'s, from The Soft-Slot Branches, and the energy of $`K'`$ is moved through zero by hand: $`B_t = \mathrm{Hess}\,\tilde f(y_0) + tP_{K'}`$, where $`t`$ plays the part of $`\varepsilon\gamma_u`$ (Theorem R′).
  - At four members of the family, by their complex structures, the decomposition is $`(d_1, d_2, d_3) = (2, 1, 0)`$ at $`i`$, $`(2, 0, 1)`$ at $`(i + 2j + 3k)/\sqrt{14}`$, and $`(0, 2, 1)`$ at $`j`$ and at $`(i + j + k)/\sqrt 3`$.
  - At $`t = \pm 10^{-6}`$ and $`\pm 10^{-8}`$, $`d_1/2`$ pairs scale like $`\lvert t\rvert`$ and reverse their Krein signs, and $`d_2`$ pairs scale like $`\lvert t\rvert^{1/2}`$, imaginary with Krein sign + for $`t > 0`$ and real for $`t < 0`$, the partners' energies being positive there. $`n(L)`$ goes from 0 to 3 and $`n(D)`$ from 0 to $`d_3`$, and Theorem K holds at every point.
  - So all three cases occur on $`R_2`$'s own kernel, forms and family, with the crossing imposed. At the generic member, where the $`\sigma`$-radical line of $`K'`$ pairs with the family's radical, the crossing is not a change of type, while at $`i`$ it is.
- **Arms.** The crossing classified by $`\Omega`$ on $`K'`$ alone predicts, at the generic member, a real pair the spectrum does not have. $`n(D)`$ taken off twice, as the instrument's $`h`$ less $`n(D)`$, breaks the count where $`d_3 = 1`$. Krein signs read from $`-B`$ break it in case 1. The exit status is 1 if a claim fails or an arm stays green.

## VI. What It Earns, and What It Does Not

**What it earns.**
- The count for the slot action's branches with the symmetry exact, in its energy space, and what the instrument's genuine index reads where its structural cluster spans the generalized kernel.
- Where the count can move: only where eigenvalues pass through zero.
- The three cases of a transversal genuine crossing where the family's own Jordan structure stays regular, and with them the test that identifies a change of type with a crossing, for the census's step 3 instrument.
- The qualifier on the census's step 2 sentence.

**What it does not give.**
- Branching at a crossing: whether a new branch bifurcates there, and which symmetry it breaks, the pitchfork question of OpenWave #625 and M8.15.1's second path. Case 3, a crossing paired with the family's radical, is where relative equilibria with momentum can branch off.
- The identification of any located change in the finite-element records, T3/R5's included.
- Crossings with an indefinite crossing form, tangential crossings, and points where the family's own Jordan structure degenerates, with or without a crossing, beyond §III's remarks and §II's naming of the Vakhitov–Kolokolov mechanism.
- The existence of branches at finite amplitude; a branch is assumed here.

## VII. What Stays Open

- The pitchfork at a genuine crossing.
- T3/R5's identification, which needs an instrument with the symmetry exact (the census's step 3).
- The indefinite and degenerate crossings of §VI.

## References

- **[KKS04]** T. Kapitula, P. G. Kevrekidis and B. Sandstede, Counting eigenvalues via the Krein signature in infinite-dimensional Hamiltonian systems, *Physica D* **195**, 263–282 (2004), [doi:10.1016/j.physd.2004.03.018](https://doi.org/10.1016/j.physd.2004.03.018), with a note under the same title, *Physica D* **201**, 199–201 (2005), [doi:10.1016/j.physd.2004.11.015](https://doi.org/10.1016/j.physd.2004.11.015).
- **[Pel05]** D. E. Pelinovsky, Inertia law for spectral stability of solitary waves in coupled nonlinear Schrödinger equations, *Proc. R. Soc. A* **461**, 783–812 (2005), [doi:10.1098/rspa.2004.1345](https://doi.org/10.1098/rspa.2004.1345).
- **[KP13]** T. Kapitula and K. Promislow, *Spectral and Dynamical Stability of Nonlinear Waves*, Applied Mathematical Sciences, Springer (2013), [doi:10.1007/978-1-4614-6995-7](https://doi.org/10.1007/978-1-4614-6995-7); ch. 7, Point Spectrum: Linear Hamiltonian Systems.
- **[SS12]** M. Stanislavova and A. Stefanov, Linear stability analysis for travelling waves of second order in time PDE's, *Nonlinearity* **25**, 2625–2654 (2012), [doi:10.1088/0951-7715/25/9/2625](https://doi.org/10.1088/0951-7715/25/9/2625). Second-order problems as quadratic pencils, for an operator with one simple negative eigenvalue.
- **[IKL82]** I. S. Iohvidov, M. G. Krein and H. Langer, *Introduction to the Spectral Theory of Operators in Spaces with an Indefinite Metric*, De Gruyter (1982), [doi:10.1515/9783112735992](https://doi.org/10.1515/9783112735992); ch. II, Isometric and Hermitian operators in a space $`\Pi_N`$.
- **[Kato]** T. Kato, *Perturbation Theory for Linear Operators*, Classics in Mathematics, Springer (1995), [doi:10.1007/978-3-642-66282-9](https://doi.org/10.1007/978-3-642-66282-9). Riesz projections.

## Files

In `scripts/hamiltonian-krein-identification/`:
- `identification_check.py`: the checks of §V; it imports `second_order_check.py` from `scripts/soft-slot-branches/`, unchanged. Each claim has a mutation arm that turns it red, and the exit status is 1 if a claim fails or an arm stays green. Under a minute.
- `identification_check.out`: its record.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
