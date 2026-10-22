# T5's second member is not symmetry-equivalent to the registered one

*UB, 2026-10-20, against MIT `54f3d7c`, with UA's two wording fixes of the same day. A draft for M8.16.1's terms, answering the condition of #512 (comment 19076863, § 3): "the terms show, DERIVED, that no symmetry of the frozen action or of the truncation carries it to the member with complex structure `i`". For the code unit to land with its check.*

## The member

In $`R_2`$, at level 7 and $`j = 7/2`$, T5's registered member is $`u = \sqrt{3/10}\,v_{7/2} + \sqrt{7/10}\,v_{-3/2}`$, read with complex structure $`i`$ (M8.16's terms, § THE CASES). $`Sp(1)`$ acts on $`E_0`$ by right multiplication, with $`i`$ the complex structure and $`j`$ acting as $`\Theta`$ (the Soft-Slot Branches, § I). The second member is $`u_2 = u\,p_0`$, with $`p_0 = (1 + k)/\sqrt 2`$, so that $`p_0\,i\,p_0^{-1} = j`$:

```math
u_2 = \sqrt{3/20}\,v_{7/2} + i\sqrt{7/20}\,v_{3/2} + \sqrt{7/20}\,v_{-3/2} - i\sqrt{3/20}\,v_{-7/2} = (u - i\Theta u)/\sqrt 2.
```

The other sign convention for $`k`$ gives $`(u + i\Theta u)/\sqrt 2`$, and everything below holds for it unchanged (claim B of the check).

**The symmetry group.** The frozen action's symmetries are $`\Gamma`$, right SU(2) times $`Sp(1)`$, with time translations and time reversal. Every complete-level truncation keeps $`\Gamma`$ exactly (M8.16's method note, § 1.2).

## The statement

**Proposition (DERIVED).**
- **(a)** No element of that group carries the standing wave through $`u_2`$, read with $`i`$, to the registered member's standing wave, read with $`i`$, allowing a phase, a time translation and time reversal. The two stationary states do lie on one $`Sp(1)`$ orbit, since $`u_2 = u\,p_0`$; the claim is about the standing waves. Nor does any element carry the standing wave of $`u_2`$'s germ to the registered member's at an $`\varepsilon`$ where the registered germ's isotropy group is $`\Gamma_u`$, which by Lemma G is every small $`\varepsilon`$.
- **(b)** For sufficiently small positive $`\varepsilon`$, the two members' linearizations $`A_\varepsilon`$, formed with complex structure $`i`$ as the instrument forms them, have disjoint nonzero slow spectra; both keep their exact structural zeros. So no linear map conjugates one into the other, and the second member's readings are not a transform of the registered member's.

*Proof.*
1. *The fibre part.* Write the fibre action on the right. Let $`(g, q) \in \Gamma`$, with a time shift $`T_0`$ and $`\sigma = \pm 1`$ ($`\sigma = -1`$ with time reversal), carry the standing wave $`\varphi_2 e^{i\omega T}`$ to $`\varphi_1 e^{i\omega(\sigma T + T_0)}`$. Then $`(g\cdot\varphi_2 q)\,e^{(q^{-1}iq)\omega T} = \varphi_1 e^{i\omega(\sigma T + T_0)}`$ for all $`T`$, and at $`T = 0`$, $`g\cdot\varphi_2 q = \varphi_1 e^{i\omega T_0}`$. Right multiplication by a quaternion is injective on a nonzero fibre vector, so $`q^{-1}iq = \sigma i`$. The frequency, and with it $`\varepsilon`$, is preserved.
2. *Conjugacy.* So the element commutes with $`i`$ ($`\sigma = 1`$) or anticommutes with it ($`\sigma = -1`$). With $`C`$ its action times $`e^{-i\omega T_0}`$, the rotating-frame perturbations satisfy $`\zeta_1(\sigma T + T_0) = C\zeta_2(T)`$. So $`A_\varepsilon`$ at the first member is $`\sigma D A_\varepsilon D^{-1}`$ at the second, with $`D = \mathrm{diag}(C, \sigma C)`$. The spectra agree, since each is symmetric under $`\lambda \mapsto -\lambda`$.
3. *Leading order.* Both members lie on T5's orbit, nondegenerate with signature (9, 0, 0). By Theorem R(a) the slow eigenvalues of each are $`\varepsilon(\kappa s + o(1))`$, with the same $`\kappa`$, since $`Q = 22/13`$ at both, and $`s`$ over the eigenvalues of its slow matrix. For $`u_2`$ read with $`i`$, that matrix is similar to $`\Theta\widehat M_u`$ (§ III, "Families in $`R_2`$": $`S_{up}`$ is similar to $`R_{pip^{-1}}M_u`$).
4. *The polynomials,* exact ([`t5_member_check.py`](t5_member_check.py)), in $`\nu = s^2`$ for unit $`u`$:
   - the registered member: $`P_1 = (20449\nu + 153664)(418161601\nu^2 + 6989958976\nu + 28677390336)/8550986578849`$, the terms' frozen T5 spectrum, with $`\tau`$ = 2.6886, 2.7413 and 3.0802;
   - the second member: $`P_2 = (1859\nu + 15680)(418161601\nu^2 + 6605190592\nu + 25491013632)/777362416259`$, with $`\tau`$ = 2.5899, 2.9042 and 3.0147.

   Their resultant is nonzero, so they share no root.
5. *(b).* By 3 and 4 the nonzero slow spectra of the two $`A_\varepsilon`$ are disjoint for sufficiently small positive $`\varepsilon`$, and similar operators have equal spectra.
6. *(a) at the seed.* An element carrying the standing wave through $`u_2`$ to that through $`u e^{i\theta}`$ has $`q^{-1}iq = \pm i`$, by 1. It conjugates $`\widehat M_{u_2}`$ to $`\widehat M_{ue^{i\theta}}`$, which is similar to $`\widehat M_u`$, and $`i`$ to $`\pm i`$. So the two slow matrices are similar up to sign, and $`P_1 = P_2`$, which 4 excludes.
7. *(a) along the germ.* Lemma G's germ is $`\Gamma`$-equivariant, so the germ through $`u_2`$ is the registered germ times $`p_0`$. If $`(g, q)`$ carried it to $`\varphi_\varepsilon e^{i\theta}`$ at some $`\varepsilon`$, then $`(g, p_0 q e^{-i\theta})`$ would fix $`\varphi_\varepsilon`$. Where $`\varphi_\varepsilon`$'s isotropy group is exactly $`\Gamma_u`$, that element fixes $`u`$, so $`(g, q)`$ carries the standing wave through $`u_2`$ to that through $`u e^{i\theta}`$, which 6 excludes.

## Its values at the seed

From claim A, and Theorems R(d) and K:
- $`Q = 22/13`$ and signature (9, 0, 0);
- $`(k, r_u) = (6, 4)`$, and $`V_0`$ of dimension 10;
- elliptic, with every slow pair Krein-negative, since $`n_+ = 0`$;
- $`(n(L), n(D), K) = (9, 3, 6)`$.

These are the registered member's. Only the frequencies differ, as in 4.

## What it does not give

- Anything where the isotropy group of a branch grows beyond $`\Gamma_u`$, or along a continuation past Lemma G's range.
- A symmetry of a truncation outside $`\Gamma`$ is not excluded as a symmetry of the equation. (b) shows that no such map relates the two members' linearizations, which is what makes the second member's outcome new evidence.
- Which equatorial member to take. The leading slow spectrum is the same at $`j`$ and $`k`$ exactly, and at nine more azimuths on the equator in floating point (INFERRED), so the choice of $`p_0`$ there changes no leading frequency. The member's next-order coefficients come from the pinned script at the stated seed.

## The check

`t5_member_check.py`, run from this folder with MIT's `scripts/soft-slot-branches/` at `54f3d7c` as its argument, imports `branches_check.py`'s exact quartic, metric and structures unchanged. In those weighted coordinates $`u`$ and $`u_2`$ are rational, so every polynomial is exact.
- Claim A: both members' values at the seed.
- Claim B: $`u_2`$ read with $`i`$ has the polynomial of $`u`$ read with $`\Theta`$, and so does the other sign.
- Claim C: $`P_1`$ is the terms' frozen T5 spectrum, $`P_1 \ne P_2`$, and the resultant is nonzero.
- One mutation arm, $`u`$ in place of $`u_2`$, turns claim C red.

Its record is `t5_member_check.out`.
