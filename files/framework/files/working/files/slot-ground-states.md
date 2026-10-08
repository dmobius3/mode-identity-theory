<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Slot Ground States

**Type:** Result
**State:** Closed
**Status (2026-10-08):** Derived. Under the frozen slot action, every slot has energy minimizers at each fixed nonzero charge; each is a standing wave, and the set of them is orbitally stable (Theorem A). In R4 and R5 at small charge, the ground states concentrate on the lowest level, and each set is the stationary family of the small-amplitude branch through the coherent orbit, so there the sets form a branch (Proposition C3); beyond small charge, and in R2, whether they form branches remains open. In the five rigid slots and the control the minimizers are the exact lowest-level family, which the slot action's §VI item 6 records for the five slots and which in the control is the constant sections. It is orbitally stable as a set at every nonzero charge (Theorem B), and about every member the linearization's whole spectrum lies on the imaginary axis, with kernel exactly the family's tangent at fixed charge (Theorem D). Together these supply both parts of §VII's stability protocol for those branches, under M8.4's persistence label; on OpenWave, the rung is a filing's to adjudicate. In R4 and R5 no ground state lies entirely in the lowest free eigenspace; in R2 the same question is whether a spin-6 multipole can vanish, and it stays open. The soft blocks' reduced quartic is derived in closed form, which gives OpenWave's D7 weights and R2's coefficients. The stability mechanism is generic; what is specific to 2I is which slots are rigid, the coherent orbit that minimizes the reduced quartic in R4 and R5, and the closed form.
**Summary:** Whether the frozen slot action carries orbitally stable nonlinear states without a run: energy minimizers at fixed charge in every slot, the rigid slots' exact branches, and the soft blocks' reduced quartic in closed form.
**Inputs:** `slot-action.md` (§V, §VI item 6, §VII, §IX), `soft-slot-branches.md` (§I, §IV, Lemma G, the proof of Theorem R(d)), OpenWave's M8.12 record (the bridge from the block quartic to r̂₆, and G1) at `344f416`, `scripts/slot-ground-states/`
**Parent:** `slot-action.md`

---

RESULT, a derivation with no pre-committed pass condition. [The slot action](slot-action.md) froze one law for the eight slot fields and recorded what it decides without a run (§VI); the stability of its nonlinear branches it left to a linear record together with a pre-registered persistence test or an orbital-stability theorem (§VII). This page proves that theorem by minimizing the energy at fixed charge, both for the rigid slots' exact branches, at every nonzero charge, and for the ground-state sets of every slot. It records the linear spectrum about every rigid branch, and it derives the soft blocks' reduced quartic in closed form. Nothing here is a run, and nothing here bears on the slot relation, which stays OPEN.

**Related:** [The Slot Action](slot-action.md), [The Slot Relation](slot-relation.md), [The Surviving Ray](../../bedrock/files/surviving-ray.md).

## I. The Setting

For each sector $`\rho`$, the control $`R_0`$ and the slots $`R_1`$ to $`R_8`$, the fields are the slot action's sections $`\psi`$ of $`E_\rho`$ over $`X = S^3/2I`$, of volume $`V = 2\pi^2R^3/120`$. The phase space is $`\mathcal{H} = H^1(X; E_\rho) \times L^2(X; E_\rho)`$, with points $`(\psi, \pi)`$, $`\pi = \partial_T\psi`$. The energy and charge of §V are

```math
E = \int_X dV \left[ \frac{1}{2c^2}\lvert\pi\rvert^2 + \frac{1}{2}\lvert\nabla\psi\rvert^2 + \frac{g}{4}\lvert\psi\rvert^4 \right],
\qquad
N = \frac{1}{c^2}\int_X dV\; \mathrm{Im}\left(\psi^{\dagger}\pi\right),
```

with $`g = g_4 > 0`$. The lowest eigenvalue of $`-\Delta`$ on $`E_\rho`$ is $`\lambda_0 = n(n+2)/R^2`$ with $`n = \mathrm{dist}(\rho)`$: a slot's first occurrence is its bundle's lowest level, and $`\lambda_0 = 0`$ for $`R_0`$.

**Well-posedness.** In three dimensions $`H^1 \subset L^6`$, so $`\psi \mapsto \lvert\psi\rvert^2\psi`$ is locally Lipschitz from $`H^1`$ to $`L^2`$, and Picard iteration on the linear Klein–Gordon group gives local solutions in $`\mathcal{H}`$ that conserve $`E`$ and $`N`$. The energy bounds $`\lVert\nabla\psi\rVert^2`$ and $`\lVert\pi\rVert^2`$, and by Lemma 1(c) also $`\lVert\psi\rVert^2`$, so solutions are global.

## II. Three Lemmas

**Lemma 1 (the lower bound).** For $`(\psi, \pi) \in \mathcal{H}`$ with $`m = \int_X \lvert\psi\rvert^2 dV > 0`$,

```math
E \;\ge\; F(m; N) = \frac{c^2N^2}{2m} + \frac{\lambda_0 m}{2} + \frac{g\,m^2}{4V},
```

each term from one inequality, with its equality case:
- (a) Cauchy–Schwarz on the charge, $`c^2\lvert N\rvert \le \lVert\psi\rVert\,\lVert\pi\rVert`$: equality if and only if $`\pi = i\alpha\psi`$ with $`\alpha`$ real;
- (b) the spectral bound $`\int \lvert\nabla\psi\rvert^2 \ge \lambda_0 m`$: equality if and only if $`\psi`$ lies in the lowest eigenspace;
- (c) Jensen, $`\int \lvert\psi\rvert^4 \ge m^2/V`$: equality if and only if $`\lvert\psi\rvert`$ is constant on X.

So equality in $`E \ge F`$ holds exactly when (a), (b) and (c) hold together.

**Lemma 2 (precompactness of minimizing sequences).** Fix $`N_0 \ne 0`$, let $`e(N_0)`$ be the infimum of $`E`$ over $`\lbrace N = N_0 \rbrace`$, and let $`(\psi_k, \pi_k)`$ satisfy $`N = N_0`$ and $`E \to e(N_0)`$. Then a subsequence converges strongly in $`\mathcal{H}`$ to a minimizer.
- *Bounded.* $`F(m; N_0) \to \infty`$ as $`m \to 0`$ and as $`m \to \infty`$, so by Lemma 1 the $`m_k`$ stay in a compact interval of $`(0, \infty)`$, and $`E`$ bounds $`\lVert\nabla\psi_k\rVert^2`$ and $`\lVert\pi_k\rVert^2`$.
- *A minimizing limit.* On a compact 3-manifold $`H^1`$ embeds compactly in $`L^2`$ and $`L^4`$ (Rellich–Kondrachov), so a subsequence has $`\psi_k \to \psi`$ strongly in $`L^2`$ and $`L^4`$, $`\nabla\psi_k \rightharpoonup \nabla\psi`$ and $`\pi_k \rightharpoonup \pi`$. The charge passes to the limit under strong-times-weak convergence, so $`N(\psi, \pi) = N_0`$, and $`m > 0`$. The energy is weakly lower semicontinuous, so $`(\psi, \pi)`$ is a minimizer.
- *Strong convergence.* The quartic term converges, the energy converges to $`E(\psi, \pi)`$, and each of $`\lVert\nabla\psi_k\rVert^2`$ and $`\lVert\pi_k\rVert^2`$ is weakly lower semicontinuous, so each converges to its limit's norm. Weak convergence with convergence of norms is strong convergence.

**Lemma 3 (lowest-level standing waves).** Let $`\psi \ne 0`$ lie in the lowest eigenspace. Then $`e^{i\omega T}\psi`$ solves the field equation if and only if $`\lvert\psi\rvert`$ is constant, and then $`\omega^2 = c^2(\lambda_0 + g\lvert\psi\rvert^2)`$. The equation reduces to $`(\lambda_0 - \omega^2/c^2)\psi + g\lvert\psi\rvert^2\psi = 0`$, so $`\lvert\psi\rvert^2 = (\omega^2/c^2 - \lambda_0)/g`$ wherever $`\psi \ne 0`$; a nonzero eigensection is real-analytic, so its zero set has empty interior, and by continuity $`\lvert\psi\rvert`$ is constant everywhere. The converse is substitution.

## III. The Theorems

**Theorem A (ground states, every sector).** Fix a sector and $`N_0 \ne 0`$.
1. The infimum $`e(N_0)`$ is attained.
2. Every minimizer has $`\pi = i\omega\psi`$ for a real $`\omega`$, and $`(-\Delta - \omega^2/c^2)\psi + g\lvert\psi\rvert^2\psi = 0`$: it is a standing wave $`e^{i\omega T}\psi`$, a ground state.
3. The set $`G(N_0)`$ of minimizers is orbitally stable in $`\mathcal{H}`$: for every $`\varepsilon > 0`$ there is $`\delta > 0`$ such that data within $`\delta`$ of $`G(N_0)`$ stay within $`\varepsilon`$ of it for all time.

*Proof.* Item 1 is Lemma 2. For item 2, $`N_0 \ne 0`$ makes $`dN \ne 0`$ at a minimizer, so a Lagrange multiplier $`\omega`$ exists; varying $`\pi`$ gives $`\pi = i\omega\psi`$, and varying $`\psi`$ gives $`-\Delta\psi + g\lvert\psi\rvert^2\psi = (\omega/c^2)(-i\pi) = (\omega^2/c^2)\psi`$. Item 3 follows the constrained-minimization contradiction of Cazenave and Lions, written for the Schrödinger equation on $`\mathbb{R}^N`$; for Klein–Gordon standing waves that minimize the energy at fixed charge see Shatah. The Klein–Gordon phase-space and charge steps are supplied here. If item 3 failed, there would be data converging to $`G(N_0)`$ and times $`T_k`$ at which the solutions, which are global by §I, sit at distance at least $`\varepsilon`$ from it. Conservation and continuity give $`E \to e(N_0)`$ and $`N \to N_0`$ along the sequence at the $`T_k`$; rescaling $`\pi_k`$ by $`N_0/N_k`$ restores the constraint and changes $`E`$ by $`o(1)`$; by Lemma 2 a subsequence converges strongly to a point of $`G(N_0)`$, a contradiction.

**Theorem B (the rigid sectors).** Take $`R_0, R_1, R_3, R_6, R_7`$ or $`R_8`$, where $`\rho = \pi_n`$ restricted to 2I with $`n = \mathrm{dist}(\rho) \le 5`$. For $`N_0 \ne 0`$ let $`m`$ be the unique positive root of $`c^2N_0^2/m^2 = \lambda_0 + g\,m/V`$. Then

```math
G(N_0) = \left\lbrace \big(\pi_n(x)\,v,\ i\omega\,\pi_n(x)\,v\big) \;:\; \lvert v\rvert^2 = m/V \right\rbrace,
\qquad
\omega = \frac{c^2N_0}{m},\qquad \omega^2 = c^2\left(\lambda_0 + g\lvert v\rvert^2\right),
```

the exact lowest-level family at that frequency: the family of the slot action's §VI item 6 in the five slots, and the constant sections in the control, where $`\pi_0`$ is trivial. It is orbitally stable as a set, at every nonzero charge, and along each direction of $`v`$ it is a branch continuous in the charge.

*Proof.* In these sectors every lowest-level section is $`\pi_n(x)v`$, and $`\lvert\pi_n(x)v\rvert = \lvert v\rvert`$ is constant. So all three equalities of Lemma 1 hold for $`(\pi_n(x)v, i\alpha\,\pi_n(x)v)`$, and $`E = F(m; N)`$. $`F`$ is strictly convex in $`m`$, so it has one minimizing $`m`$, the stated root, which depends continuously on $`N_0`$; equality in $`E \ge F(m) \ge F(m^*)`$ picks out exactly the stated set, and stationarity of $`F`$ there gives $`\omega^2 = c^2(\lambda_0 + g\lvert v\rvert^2)`$. Orbital stability is Theorem A.3.

With each member $`\pi_n(x)v`$ the family contains every $`\pi_n(x)v'`$ with $`\lvert v'\rvert = \lvert v\rvert`$, among them the profiles that the phase, right translations and the fibre symmetry produce from it, so the claim is about the family as a set, as the slot action's §IX asks. No spectral or nondegeneracy analysis enters; the linear spectrum is Theorem D.

## IV. The Soft Slots

**The reduced quartic in closed form.** For a lowest-level section $`\psi_w`$ of a soft slot, write $`Q(w) = V\int\lvert\psi_w\rvert^4/(\int\lvert\psi_w\rvert^2)^2`$, the Jensen ratio of Lemma 1(c), which is 1 exactly at constant norm. The soft slots are $`R_4`$ and $`R_5`$ at level 6 and $`R_2`$ at level 7. Among the spins 0 to 7, 2I has invariant vectors only at 0 and 6, so a 2I-invariant operator on the block has spin components only at those two spins. The slot projector is therefore $`P = (r/d)\,\mathrm{Id} + P_6`$ with $`\lVert P_6\rVert^2 = r - r^2/d`$, where $`d = \mathrm{dist} + 1`$ is the block's dimension and $`r = \dim\rho`$. Schur orthogonality on the spin-6 representation then gives

```math
Q(w) = 1 + \beta_\rho\,\frac{\lVert (w w^{\dagger})_6 \rVert^2}{\lVert w\rVert^4},
\qquad
\beta_\rho = \frac{d\,(d-r)}{13\,r},
```

with $`(ww^{\dagger})_6`$ the spin-6 component of $`ww^{\dagger}`$ under conjugation, in the Hilbert–Schmidt norm. For spin 3 the last factor is M8.12's $`\hat r_6`$.

| slot | d | r | $`\beta_\rho`$ |
| --- | --- | --- | --- |
| $`R_4`$ ($`3'`$) | 7 | 3 | 28/39, OpenWave's D7 value |
| $`R_5`$ ($`4`$) | 7 | 4 | 21/52, OpenWave's D7 value |
| $`R_2`$ ($`2'`$) | 8 | 2 | 24/13 |

Recoupled to the pairing channels, $`Q = \sum_J q_J f_J`$, where the channel fractions $`f_J = \lVert[w\otimes w]_J\rVert^2/\lVert w\rVert^4`$ sum to 1 and, with $`j = (d-1)/2`$ the block's spin,

```math
q_J = 1 + 13\,\beta_\rho\begin{Bmatrix} j & j & 6 \\ j & j & J \end{Bmatrix},
```

which for $`R_2`$ gives $`(q_7, q_5, q_3, q_1) = (144/143,\ 196/143,\ 28/11,\ 0)`$.

**Proposition C.**
1. *In $`R_4`$ and $`R_5`$, no ground state lies entirely in the lowest free eigenspace, at any nonzero charge.* Every symmetric-channel coefficient exceeds 1: $`(1288/1287, 35/33, 14/9, 7/3)`$ in $`R_4`$ and $`(2289/2288, 91/88, 21/16, 7/4)`$ in $`R_5`$, at $`F = (6, 4, 2, 0)`$. So $`Q > 1`$, no lowest-level section has constant norm, and Lemma 3 excludes a lowest-level ground state. This does not exclude a ground state lying in one higher free eigenspace with constant norm; whether such sections exist is not examined, and at large charge the quartic term, which grows as $`m^2`$, can outweigh the level term, which grows as $`m`$.
2. *In $`R_2`$ the same holds if and only if no unit vector of the block has $`(ww^{\dagger})_6 = 0`$.* Whether one does is OPEN; the smallest $`Q`$ found numerically is 144/143.
3. *At small charge in $`R_4`$ and $`R_5`$, the ground states concentrate on the lowest level, and the direction of their lowest-level part tends to the coherent orbit, modulo the phase and the right translations.* The coherent orbit is the unique minimizer of $`Q`$ on the lowest block: $`q_6`$ is the strictly smallest coefficient, and $`f_6 = 1`$ exactly on coherent states. Write $`E_0`$ for the lowest eigenspace, on which the right translations act in spin 3; $`v_k`$, $`k = 3, \ldots, -3`$, for a weight basis of $`E_0`$ with $`v_3`$ coherent; $`\mathcal{M}`$ for the coherent orbit, the unit vectors of $`E_0`$ at which $`Q = q_6`$, a single orbit of the phase and the right translations; and $`\lambda_1`$ for the next eigenvalue of $`-\Delta`$ on $`E_\rho`$. For a section $`\phi`$, $`\phi_0`$ is its orthogonal projection on $`E_0`$ and $`\phi_\perp = \phi - \phi_0`$. For $`(\psi, \pi) \in G(N_0)`$, let $`m = \int_X\lvert\psi\rvert^2 dV`$ and $`\varepsilon = \omega^2/c^2 - \lambda_0`$. There are $`N_* > 0`$ and $`C`$, depending only on the slot, $`g`$, $`c`$ and $`R`$, such that for $`0 < \lvert N_0\rvert \le N_*`$ every member of $`G(N_0)`$ satisfies:
   - *(a) Mass and frequency.* $`\omega`$ has the sign of $`N_0`$, and $`g\,m/V \le \varepsilon \le q_6\,g\,m/V`$, with $`\varepsilon = q_6\,g\,m/V + O(m^2)`$. So $`\omega = \mathrm{sgn}(N_0)\,c\sqrt{\lambda_0}\,\bigl(1 + q_6\,g\,c\,\lvert N_0\rvert/(2V\lambda_0^{3/2}) + O(N_0^2)\bigr)`$ and $`m = (c\lvert N_0\rvert/\sqrt{\lambda_0})\,\bigl(1 - q_6\,g\,c\,\lvert N_0\rvert/(2V\lambda_0^{3/2}) + O(N_0^2)\bigr)`$: the mass vanishes linearly in the charge, and the frequency tends to the lowest free frequency $`c\sqrt{\lambda_0}`$, with the sign of the charge.
   - *(b) Off the lowest level.* $`\lVert(-\Delta)^{s/2}\psi_\perp\rVert \le C\lvert N_0\rvert\,\lVert(-\Delta)^{s/2}\psi\rVert`$ for $`s = 0, 1, 2`$, and $`\sup_X\lvert\psi_\perp\rvert \le C\lvert N_0\rvert\,\sup_X\lvert\psi\rvert`$; since $`\pi = i\omega\psi`$, the same holds for $`(\psi_\perp, \pi_\perp)`$ in $`\mathcal{H}`$. The order is exact: $`\lVert\psi_\perp\rVert \ge C^{-1}\lvert N_0\rvert\,\lVert\psi\rVert`$.
   - *(c) The direction.* $`\mathrm{dist}(\psi_0/\lVert\psi_0\rVert,\ \mathcal{M}) \le C\lvert N_0\rvert`$ in $`E_0`$: a phase and a right translation carry $`\psi_0/\lVert\psi_0\rVert`$ to within $`C\lvert N_0\rvert`$ of $`v_3`$. The quotient cannot be dropped, since $`G(N_0)`$ is invariant under both; charge conjugation maps $`\mathcal{M}`$ to itself and adds nothing.
   - *(d) The coherent branch.* For $`0 < \lvert N_0\rvert \le N_*`$, $`G(N_0)`$ is the set of $`(\gamma\varphi_\varepsilon,\ i\omega\,\gamma\varphi_\varepsilon)`$ with $`\gamma`$ in the stationary symmetry group $`\Gamma`$ of [The Soft-Slot Branches](soft-slot-branches.md), where $`\varphi_\varepsilon`$ is the branch its Lemma G gives through the coherent orbit, $`\omega^2 = c^2(\lambda_0 + \varepsilon)`$ with $`\omega`$ of the sign of $`N_0`$, and $`\varepsilon`$ is the small solution of $`c^{-1}(\lambda_0 + \varepsilon)^{1/2}\lVert\varphi_\varepsilon\rVert^2 = \lvert N_0\rvert`$. So at small charge each ground-state set is one orbit of $`\Gamma`$, the sets form a branch continuous in the charge, and the direction of every ground state's lowest-level part lies on the coherent orbit exactly.

In item 3, the bracket in (a) holds at every charge, and the rest of (a) and the upper bound in (b) hold once $`\lvert N_0\rvert \le V\sqrt{\lambda_0}\,(\lambda_1 - \lambda_0)/(2cgq_6)`$; the lower bound in (b), (c) and (d) use a compactness step, so $`N_*`$ is not explicit.

*Proof of 3.* Let $`(\psi, \pi) \in G(N_0)`$. By Theorem A.2, $`\pi = i\omega\psi`$ with $`\omega`$ real, and $`(-\Delta - \omega^2/c^2)\psi + g\lvert\psi\rvert^2\psi = 0`$. Then $`N_0 = \omega m/c^2`$, so $`\omega`$ has the sign of $`N_0`$ and $`c^2N_0^2/m^2 = \lambda_0 + \varepsilon`$. Write $`\hat\psi = \psi/\sqrt{m}`$; $`\delta = \lVert\nabla\hat\psi\rVert^2 - \lambda_0`$, which is at least 0 by Lemma 1(b); and $`Q(\phi) = V\int_X\lvert\phi\rvert^4 dV/\lVert\phi\rVert^4`$ for any section $`\phi \ne 0`$, the Jensen ratio of §IV, which is at least 1 by Lemma 1(c). In $`R_4`$ and $`R_5`$, $`\lambda_0 = 48/R^2 > 0`$. $`C`$ stands for a constant of the kind in the statement, not the same at each use.

*The comparison.* Lemma 1(a) holds with equality at $`\pi = i\omega\psi`$, so $`E(\psi, \pi) = F(m; N_0) + m\delta/2 + g\,m^2\,(Q(\hat\psi) - 1)/4V`$. For $`e \in \mathcal{M}`$, the pair $`(\sqrt{m}\,e,\ i(c^2N_0/m)\sqrt{m}\,e)`$ has charge $`N_0`$; Lemma 1(a) and (b) hold for it with equality and $`Q(e) = q_6`$, so its energy is $`F(m; N_0) + g\,m^2\,(q_6 - 1)/4V`$. The ground state's energy is at most that, so

```math
\frac{2V}{g\,m}\,\delta + Q(\hat\psi) \;\le\; q_6 .
```

No smallness enters, so this holds at every $`N_0 \ne 0`$.

*Mass and frequency.* Pairing the field equation with $`\psi`$ gives $`\varepsilon = \delta + g\,m\,Q(\hat\psi)/V`$. With $`\delta \ge 0`$ and $`Q \ge 1`$, $`\varepsilon \ge g\,m/V`$. The comparison gives $`Q(\hat\psi) \le q_6`$ and $`\delta \le g\,m\,(q_6 - Q(\hat\psi))/2V`$, so $`\varepsilon \le g\,m\,(q_6 + Q(\hat\psi))/2V \le q_6\,g\,m/V`$. That is the bracket in (a), at every charge. With $`c^2N_0^2/m^2 = \lambda_0 + \varepsilon \ge \lambda_0`$ it gives $`m \le c\lvert N_0\rvert/\sqrt{\lambda_0}`$.

*Off the lowest level.* Let $`\lvert N_0\rvert \le V\sqrt{\lambda_0}\,(\lambda_1 - \lambda_0)/(2cgq_6)`$, so that the bracket gives $`\omega^2/c^2 \le (\lambda_0 + \lambda_1)/2`$. Pairing the field equation with an eigensection of $`-\Delta`$ of eigenvalue $`\lambda \ge \lambda_1`$ gives $`(\lambda - \omega^2/c^2)\,\psi_\lambda = -g\,(\lvert\psi\rvert^2\psi)_\lambda`$ for the components in that eigenspace, and $`\lambda/(\lambda - \omega^2/c^2) \le 2\lambda/(\lambda - \lambda_0) \le 2\lambda_1/(\lambda_1 - \lambda_0)`$. Summing over the eigenspaces,

```math
\lVert\Delta\psi_\perp\rVert \;\le\; \frac{2\lambda_1}{\lambda_1 - \lambda_0}\; g\,\lVert\psi\rVert_{L^6}^3 \;\le\; C\,m^{3/2},
```

by §I's embedding $`H^1 \subset L^6`$, which with $`-\Delta \ge \lambda_0 > 0`$ gives $`\lVert\phi\rVert_{L^6} \le C\lVert\nabla\phi\rVert`$, and by $`\lVert\nabla\psi\rVert^2 = m(\lambda_0 + \delta) \le C\,m`$. Since $`-\Delta \ge \lambda_1`$ off $`E_0`$ and $`-\Delta \ge \lambda_0`$ everywhere, $`\lVert(-\Delta)^{s/2}\psi_\perp\rVert \le \lambda_1^{s/2 - 1}\lVert\Delta\psi_\perp\rVert`$ and $`\lVert(-\Delta)^{s/2}\psi\rVert \ge \lambda_0^{s/2}\sqrt{m}`$; with $`m \le c\lvert N_0\rvert/\sqrt{\lambda_0}`$ this is the bound in (b). The uniform bound follows from $`H^2 \subset C^0`$ in three dimensions and $`\sup_X\lvert\psi\rvert \ge \sqrt{m/V}`$. In particular $`\lVert\nabla\hat\psi_\perp\rVert \le C\,m`$, and since the cross terms vanish, $`\delta = \lVert\nabla\hat\psi_\perp\rVert^2 - \lambda_0\lVert\hat\psi_\perp\rVert^2 \le C\,m^2`$.

*The Jensen ratio.* Let $`w = \psi_0/\lVert\psi_0\rVert`$. The gap gives $`(\lambda_1 - \lambda_0)\lVert\hat\psi_\perp\rVert^2 \le \delta`$ and the comparison gives $`\delta \le g\,m\,(q_6 - 1)/2V`$, so on the range above $`\lVert\hat\psi_\perp\rVert^2 \le (q_6 - 1)/4q_6`$, and $`\lVert\psi_0\rVert^2 = m\,(1 - \lVert\hat\psi_\perp\rVert^2) \ge m/2`$. Since $`\bigl\lvert\lVert a\rVert_{L^4}^4 - \lVert b\rVert_{L^4}^4\bigr\rvert \le 4\max(\lVert a\rVert_{L^4}, \lVert b\rVert_{L^4})^3\,\lVert a - b\rVert_{L^4}`$ and $`\lVert\phi\rVert_{L^4} \le C\lVert\nabla\phi\rVert`$, $`\lvert Q(\hat\psi) - Q(w)\rvert \le C\,m`$. With the comparison and §IV, $`q_6 \le Q(w) \le q_6 + C\,m`$ and $`\lvert Q(\hat\psi) - q_6\rvert \le C\,m`$. With $`\delta \le C\,m^2`$, $`\varepsilon = \delta + g\,m\,Q(\hat\psi)/V`$ then gives $`\varepsilon = q_6\,g\,m/V + O(m^2)`$, and the expansions of $`\omega`$ and $`m`$ follow from $`c^2N_0^2/m^2 = \lambda_0 + \varepsilon`$. The unit sphere of $`E_0`$ is compact, and $`Q = q_6`$ on it exactly at $`\mathcal{M}`$, so $`\mathrm{dist}(w, \mathcal{M}) \to 0`$ as $`N_0 \to 0`$, uniformly over $`G(N_0)`$.

*Nondegeneracy.* Since $`J_+v_3 = 0`$ and $`J_-v_3`$ is a multiple of $`v_2`$, the tangent to $`\mathcal{M}`$ at $`v_3`$ is spanned by $`iv_3`$, $`v_2`$ and $`iv_2`$, so a unit vector normal to $`\mathcal{M}`$ there is $`v = \sum_{k \le 1}a_kv_k`$. Here and below $`J`$ runs over the symmetric channels 6, 4, 2 and 0, the only ones $`w\otimes w`$ meets. Along $`\cos t\,v_3 + \sin t\,v`$, $`f_J = 4t^2\lVert[v_3\otimes v]_J\rVert^2 + O(t^3)`$ for $`J < 6`$, since $`[v_3\otimes v_3]_J = 0`$ there, while $`\sum_J f_J = 1`$; so

```math
\frac{d^2Q}{dt^2}\bigg\rvert_{t=0} \;=\; 8\sum_{J<6}\,(q_J - q_6)\,\lVert[v_3\otimes v]_J\rVert^2 \;\ge\; 8\,(q_4 - q_6)\left(\tfrac{1}{2} - \lVert[v_3\otimes v]_6\rVert^2\right) \;\ge\; \tfrac{24}{11}\,(q_4 - q_6) \;=\; \tau_* .
```

The symmetric channels carry half of $`\lVert v_3\otimes v\rVert^2 = 1`$; $`q_4`$ is the least coefficient after $`q_6`$ (item 1); and $`\lVert[v_3\otimes v_k]_6\rVert^2 = \binom{6}{3-k}\big/\binom{12}{3-k} \le 5/22`$ for $`k \le 1`$, the squared Clebsch–Gordan coefficient that applying $`J_-^{3-k}`$ to $`v_3\otimes v_3`$ gives, with the $`[v_3\otimes v_k]_6`$ mutually orthogonal. So $`\mathcal{M}`$ is a nondegenerate minimum, with normal Hessian at least $`\tau_* = 56/429`$ in $`R_4`$ and $`21/286`$ in $`R_5`$, attained along $`v_1`$; this is the least of the slow frequencies [The Soft-Slot Branches](soft-slot-branches.md) lists for the coherent orbit (§IV), computed there in exact arithmetic. By invariance the bound holds at every point of $`\mathcal{M}`$, so a Taylor expansion of the gradient about the nearest point of $`\mathcal{M}`$ gives $`\lVert\mathrm{grad}\,Q(w)\rVert \ge (\tau_*/2)\,\mathrm{dist}(w, \mathcal{M})`$ for $`w`$ near $`\mathcal{M}`$.

*The rate.* Projecting the field equation on $`E_0`$ gives $`g\,(\lvert\psi\rvert^2\psi)_0 = \varepsilon\,\psi_0`$. Pointwise, $`\bigl\lvert\lvert\psi\rvert^2\psi - \lvert\psi_0\rvert^2\psi_0\bigr\rvert \le \tfrac{3}{2}\bigl(\lvert\psi\rvert^2 + \lvert\psi_0\rvert^2\bigr)\lvert\psi_\perp\rvert`$, so by Hölder and §I the $`L^2`$ norm of the difference is at most $`C\,m\,\lVert\nabla\psi_\perp\rVert \le C\,m^{5/2}`$. Dividing by $`\lVert\psi_0\rVert^3`$, $`(\lvert w\rvert^2w)_0 = \mu w + r`$ with $`\mu`$ real and $`\lVert r\rVert \le C\,m`$. On the unit sphere of $`E_0`$, $`\mathrm{grad}\,Q(w) = 4V\bigl((\lvert w\rvert^2w)_0 - \mathrm{Re}\langle(\lvert w\rvert^2w)_0, w\rangle\,w\bigr) = 4V\bigl(r - \mathrm{Re}\langle r, w\rangle\,w\bigr)`$, of norm at most $`C\,m`$. Once $`w`$ is near $`\mathcal{M}`$, nondegeneracy gives $`\mathrm{dist}(w, \mathcal{M}) \le 2C\,m/\tau_* \le C\lvert N_0\rvert`$, which is (c).

*The exact order.* Let $`R_\sigma`$ be the inverse of $`-\Delta - \sigma`$ off $`E_0`$, so that the step off the lowest level reads $`\psi_\perp = -g\,R_{\omega^2/c^2}(\lvert\psi\rvert^2\psi)_\perp`$. Since $`R_{\omega^2/c^2} - R_{\lambda_0} = \varepsilon\,R_{\omega^2/c^2}R_{\lambda_0}`$ with $`\varepsilon \le C\,m`$, and the cubic difference above is at most $`C\,m^{5/2}`$, $`\psi_\perp = -g\,\lVert\psi_0\rVert^3R_{\lambda_0}(\lvert w\rvert^2w)_\perp + O(m^{5/2})`$ in $`L^2`$. The map $`w \mapsto R_{\lambda_0}(\lvert w\rvert^2w)_\perp`$ is continuous on the unit sphere of $`E_0`$, and its norm is the same at every point of $`\mathcal{M}`$, since the phase and the right translations commute with $`\Delta`$ and with the cubic. That norm is not 0: at $`w \in \mathcal{M}`$, criticality gives $`(\lvert w\rvert^2w)_0 = (Q(w)/V)\,w`$, so if $`(\lvert w\rvert^2w)_\perp`$ vanished, then $`\lvert w\rvert^2 = Q(w)/V`$ wherever $`w \ne 0`$, and $`\lvert w\rvert`$ would be constant by Lemma 3's argument, against $`Q(w) = q_6 > 1`$. So for $`\lvert N_0\rvert \le N_*`$ the leading term has norm at least $`C^{-1}m^{3/2}`$, and $`\lVert\psi_\perp\rVert \ge C^{-1}\lvert N_0\rvert\,\lVert\psi\rVert`$.

*Proof of (d).* By (a) to (c), $`\psi`$ is small in $`H^2`$, $`\varepsilon > 0`$ is small, and $`y = (g/\varepsilon)^{1/2}\psi_0`$ has $`\lVert y\rVert^2 = (V/q_6)(1 + O(m))`$ and $`y/\lVert y\rVert = w`$ near $`\mathcal{M}`$. For a unit coherent $`u`$, Lemma G's $`\kappa_u = 2H(u)`$ is $`q_6/V`$, so $`y`$ is near the orbit of $`y_0 = \kappa_u^{-1/2}u`$. Lemma G's complementary equation has a unique small solution, so $`\psi_\perp = v(\psi_0, \lambda_0 + \varepsilon)`$, and $`y`$ is a critical point of $`\tilde f(\cdot, \varepsilon)`$ near that orbit; Lemma G's slice step then puts $`\psi`$ in the stationary family $`\Gamma\varphi_\varepsilon`$. Along the branch the charge is $`\mathcal{N}(\varepsilon) = c^{-1}(\lambda_0 + \varepsilon)^{1/2}\lVert\varphi_\varepsilon\rVert^2`$, and $`\mathcal{N}'(\varepsilon) = c\,\Omega(\theta, \xi)\big/\bigl(2(\lambda_0 + \varepsilon)^{1/2}\bigr) > 0`$ by the computation in that page's proof of Theorem R(d), which uses Lemma G alone; so $`\varepsilon`$ is fixed by $`\lvert N_0\rvert`$. Every $`\gamma \in \Gamma`$ preserves $`\lVert\cdot\rVert`$, $`\lVert\nabla\cdot\rVert`$ and $`\int\lvert\cdot\rvert^4`$, so every member of the family has the ground state's energy and charge, and $`G(N_0)`$ is the whole family. Finally, the isotropy group of $`\varphi_\varepsilon`$ is $`\Gamma_u`$; for $`u = v_3`$ it contains each rotation about the axis of $`v_3`$ composed with the phase that undoes it on $`v_3`$, which multiplies $`v_k`$ by $`e^{i(k-3)\theta}`$. On $`E_0`$ these fix only the multiples of $`v_3`$, so $`(\varphi_\varepsilon)_0`$ is one, and the direction of every ground state's lowest-level part lies on the coherent orbit.

## V. The Linear Spectrum

The slot action's §VII asks first for a linear record: in the frame rotating with a branch's phase, its linearization has no eigenvalue with positive real part. About the rigid families this holds at every member, with the whole spectrum on the imaginary axis.

**Theorem D (the linear spectrum, rigid sectors).** Take $`R_0, R_1, R_3, R_6, R_7`$ or $`R_8`$, with $`n = \mathrm{dist}(\rho)`$, and a member $`e^{i\omega T}\varphi`$ of the family of Theorem B, $`\varphi = \pi_n(x)\,v`$ with $`v \ne 0`$. Write $`\psi = e^{i\omega T}(\varphi + \zeta)`$, linearize the field equation in $`\zeta`$, and let $`E_0`$ be the lowest eigenspace of $`-\Delta`$ on $`E_\rho`$. Then the whole spectrum of the linearization lies on the imaginary axis:
1. The linearization preserves the splitting $`\zeta = \zeta_0 + \zeta_\perp`$, with $`\zeta_0 \in E_0`$ and $`\zeta_\perp`$ orthogonal to $`E_0`$.
2. On $`E_0`$ the eigenvalues are 0, with algebraic multiplicity $`2n+2`$ and geometric multiplicity $`2n+1`$; $`\pm 2i\omega`$, each $`n`$ times, from the complex directions orthogonal to $`v`$; and $`\pm i\left(4\omega^2 + 2gc^2\lvert v\rvert^2\right)^{1/2}`$, from the direction of $`v`$.
3. Off $`E_0`$ the conserved quadratic form is positive definite, so the spectrum there consists of imaginary eigenvalues, none of them 0.

The kernel is exactly the tangent space at $`v`$ to the sphere $`\lvert v'\rvert = \lvert v\rvert`$, whose points are the members of the family at the same charge; it contains the directions of the phase, of right translations and of the fibre symmetry acting on the profile. The zero eigenvalue has one more direction, a generalized eigenvector: the family's derivative in the charge. So no kernel is left unexplained, as the slot action's §IX asks. In the quaternionic slots the fibre symmetry's generators beyond the phase anticommute with $`i`$, so their action on phase space moves the standing wave along a $`\pm 2i\omega`$ mode, not along the kernel. The zero eigenvalue is not semisimple: in a fixed rotating frame the charge direction drifts linearly. The claim is spectral stability, not bounded linearized evolution about one member at a fixed frequency; the nonlinear stability of the family is Theorem B's.

*Proof.* With $`\lvert\varphi\rvert = \lvert v\rvert`$ constant and $`\omega^2/c^2 = \lambda_0 + g\lvert v\rvert^2`$, the linearized equation is

```math
\frac{1}{c^2}\left(\partial_T^2\zeta + 2i\omega\,\partial_T\zeta\right) + (-\Delta - \lambda_0)\,\zeta + 2g\,\mathrm{Re}\left(\varphi^{\dagger}\zeta\right)\varphi = 0,
```

with $`\varphi^{\dagger}\zeta`$ the pointwise fibre product. It is real-linear, so its spectrum is taken on its complexification. It conserves the second variation of $`E - \omega N`$ at the standing wave,

```math
H_2 = \int_X dV \left[ \frac{1}{2c^2}\lvert\partial_T\zeta\rvert^2 + \frac{1}{2}\left(\lvert\nabla\zeta\rvert^2 - \lambda_0\lvert\zeta\rvert^2\right) + g\left(\mathrm{Re}\,\varphi^{\dagger}\zeta\right)^2 \right]:
```

once the equation is used in $`dH_2/dT`$, the gyroscopic term contributes a multiple of $`\mathrm{Re}\left(i\lvert\partial_T\zeta\rvert^2\right) = 0`$, and the other terms cancel in pairs.

*The splitting.* $`E_0`$ is the set of sections $`\pi_n(x)u`$ with $`u \in \mathrm{Sym}^n\mathbb{C}^2`$, and $`\pi_n(x)`$ is unitary. For $`\zeta_0 = \pi_n(x)u`$ the product $`\varphi^{\dagger}\zeta_0 = v^{\dagger}u`$ is constant, so the coupling term lies in $`E_0`$. For $`\zeta_\perp`$ orthogonal to $`E_0`$, the coupling term's $`L^2`$ product with $`\pi_n(x)u`$ is $`(u^{\dagger}v)\,\mathrm{Re}\langle\varphi, \zeta_\perp\rangle = 0`$, since $`\varphi \in E_0`$. The Laplacian and the time derivatives preserve both parts, and the cross terms of $`H_2`$ vanish for the same reasons.

*Above the lowest level.* On the complement of $`E_0`$, $`-\Delta \ge \lambda_1`$, the next eigenvalue of $`-\Delta`$ on $`E_\rho`$. The slot occurs at level $`K`$ as often as 2I has invariants in $`\mathrm{Sym}^n\mathbb{C}^2 \otimes \mathrm{Sym}^K\mathbb{C}^2`$, the sum of the levels $`\lvert K-n\rvert`$ to $`K+n`$ in steps of 2. Below level 12 the only invariants are the constants, at level 0, which needs $`K = n`$; level 12 first enters at $`K = 12 - n`$. So

```math
\lambda_1 - \lambda_0 = \frac{(12-n)(14-n) - n(n+2)}{R^2} = \frac{28\,(6-n)}{R^2} > 0 .
```

With $`g > 0`$ the coupling term is nonnegative, so on the complement $`H_2`$ is at least $`\lVert\partial_T\zeta_\perp\rVert^2/2c^2 + (1 - \lambda_0/\lambda_1)\lVert\nabla\zeta_\perp\rVert^2/2`$, and at least $`(\lambda_1 - \lambda_0)\lVert\zeta_\perp\rVert^2/2`$: it is the square of a norm equivalent to that of $`H^1 \times L^2`$. The linearized flow preserves it, so, complexified, the flow is a unitary group for the Hermitian extension of $`H_2`$ and its generator is skew-adjoint; the spectrum there lies on the imaginary axis. The generator has compact resolvent, since its domain $`H^2 \times H^1`$ embeds compactly in $`H^1 \times L^2`$, so that spectrum consists of eigenvalues. Pairing a static solution with itself shows that twice the potential part of $`H_2`$ vanishes, which forces $`\zeta_\perp = 0`$, so none of the eigenvalues is 0.

*On the lowest level.* With $`\zeta_0 = \pi_n(x)u`$ the equation is $`\partial_T^2 u + 2i\omega\,\partial_T u + 2gc^2\,\mathrm{Re}(v^{\dagger}u)\,v = 0`$. For $`u`$ orthogonal to $`v`$ the coupling vanishes and $`u = u_1 + u_2\,e^{-2i\omega T}`$, so each of the $`n`$ complex directions orthogonal to $`v`$ gives the eigenvalues 0, 0 and $`\pm 2i\omega`$. Along $`v`$, with $`u = (a + ib)\,v/\lvert v\rvert`$,

```math
\partial_T^2 a - 2\omega\,\partial_T b + 2gc^2\lvert v\rvert^2 a = 0, \qquad \partial_T^2 b + 2\omega\,\partial_T a = 0,
```

with characteristic polynomial $`\mu^2\left(\mu^2 + 4\omega^2 + 2gc^2\lvert v\rvert^2\right)`$. The static solutions are exactly the $`u`$ with $`\mathrm{Re}(v^{\dagger}u) = 0`$, of real dimension $`2n+1`$. The remaining zero belongs to $`a`$ constant with $`b = (gc^2\lvert v\rvert^2/\omega)\,aT`$: the change of $`\lvert v\rvert`$, and so of $`\omega`$, along the family.

## VI. What It Earns, and What It Does Not

**What it earns.** Theorem B gives the rigid slots' exact branches an orbital-stability theorem at every nonzero charge, and Theorem D gives every member of them the linear record. Together they supply both parts of the slot action's §VII stability protocol for those branches, the linear record and an orbital-stability theorem in place of a persistence test, under M8.4's label "nonlinear persistence of the installed free structure", since their shape never changes; on OpenWave, the rung is a filing's to adjudicate. Theorem A gives every slot, at every nonzero charge, an orbitally stable set of standing-wave ground states. In $`R_4`$ and $`R_5`$ at small charge those sets form a branch continuous in the charge (Proposition C3). Beyond that, in the soft slots, Theorem A gives a stable set at each charge, not a branch shown continuous in the charge, and M8.2's literal rung asks for "stable nonlinear branches / defects", so there a filing must also adjudicate whether sets suffice, unless that continuity is proved.

**The stability mechanism is generic.** Theorem A holds for a defocusing quartic on any compact manifold of dimension at most three. Theorem B applies wherever the whole lowest eigenspace consists of constant-norm sections, and 2I's representation theory decides that this happens here exactly in the control and in $`R_1, R_3, R_6, R_7`$ and $`R_8`$, the slots §VI item 6 of the slot action names. Theorem D needs that property and nothing more: by polarization, constant norms on all of $`E_0`$ make every pointwise product of two of its sections constant, which is all the splitting uses, and on a compact manifold the next eigenvalue lies above the lowest. 2I sets the size of that gap, $`28(6-n)/R^2`$. What is specific to 2I is which slots are rigid, the coherent orbit that minimizes the reduced quartic in $`R_4`$ and $`R_5`$ and carries their small-charge ground states (Proposition C3), and the closed form of §IV. The common structure across the eight slots meets the letter of M8.4's "common finite-amplitude branch or stability structure across the eight under one action", not its intent, and must not be presented as earning more than persistence.

**What it does not give.** It does not give:
- the stability of non-minimizing branches;
- the linear spectrum about the soft-slot ground states beyond small charge in $`R_4`$ and $`R_5`$, and at every charge in $`R_2`$;
- whether a ground-state set is a single orbit, beyond small charge in $`R_4`$ and $`R_5`$ and at every charge in $`R_2`$;
- smooth dependence on the charge in the soft slots;
- $`R_2`$'s constant-norm question;
- any relation among slot energies (the slot relation is OPEN);
- any physical particle state.

## VII. What Stays Open

- The soft-slot ground states beyond small charge in $`R_4`$ and $`R_5`$, and at every charge in $`R_2`$: their shape, whether each set is one orbit, and whether they form branches.
- Proposition C2.
- Non-minimizing branches: the maximum and the saddles of the reduced quartic.
- The linear spectrum about the soft-slot ground states beyond small charge in $`R_4`$ and $`R_5`$, and at every charge in $`R_2`$.

**Note (2026-10-06), on the soft branches.** [The Soft-Slot Branches](soft-slot-branches.md) proves that every critical orbit of the reduced quartic that is nondegenerate modulo the stationary symmetry group carries a branch of standing waves at small amplitude, and decides that branch's small-amplitude linear spectrum. Through a nondegenerate minimum of $`Q`$, the coherent orbit in $`R_4`$ and $`R_5`$ and the weight-7/2 orbit in $`R_2`$, a strict local minimum, the branch is spectrally and orbitally stable relative to its stationary family; at the definite maxima and the elliptic saddles listed there it is spectrally stable. Whether those branches are the ground-state sets is Proposition C3's limit, INFERRED, and Proposition C2 and everything at finite amplitude stay open.

**Note (2026-10-08), on Proposition C3.** Proposition C3 is now derived (§IV). As the charge tends to 0 in $`R_4`$ and $`R_5`$, every ground state concentrates on the lowest level, with its part off that level of relative order $`\lvert N_0\rvert`$, and its frequency tends to the lowest free frequency. With Lemma G of [The Soft-Slot Branches](soft-slot-branches.md), each ground-state set at small charge is the stationary family of the branch through the coherent orbit, and the direction of every ground state's lowest-level part lies on that orbit. So in $`R_4`$ and $`R_5`$ the minimizing branches of the note above are the ground-state sets at small charge, and the small-amplitude spectral and orbital stability stated there holds for those ground states. Proposition C2, the ground states of $`R_2`$, and everything beyond small charge stay open.

## References

- T. Cazenave and P.-L. Lions, "Orbital stability of standing waves for some nonlinear Schrödinger equations", *Commun. Math. Phys.* **85** (1982) 549–561, doi:[10.1007/BF01403504](https://doi.org/10.1007/BF01403504).
- J. Shatah, "Stable standing waves of nonlinear Klein-Gordon equations", *Commun. Math. Phys.* **91** (1983) 313–327, doi:[10.1007/BF01208779](https://doi.org/10.1007/BF01208779).
- OpenWave M8.12, the bridge $`Q_\sigma = 1 + w_6(\sigma)\,\hat r_6`$ ([method note §1.5](https://github.com/openwave-labs/openwave/blob/344f4162eb2bc256728c240c31382db277f399b1/openwave/xperiments/m8_mit/research/findings/m8_12_method_note.md#L84)) and G1 ([task](https://github.com/openwave-labs/openwave/blob/344f4162eb2bc256728c240c31382db277f399b1/openwave/xperiments/m8_mit/research/tasks/m8_12_task_details.md#L151)).

## Files

In [`scripts/slot-ground-states/`](scripts/slot-ground-states/), with the SHA-256 of every other file in `SHA256SUMS`:
- `soft_quartic.py`: the group, its characters and McKay distances; each soft slot's projector and its spin content; the closed form of §IV against the group-sum quartic on random states, with a 1% error in $`\beta_\rho`$ as the control; the exact coefficients, with a spin-4 control; and Proposition C1's inequalities. Self-contained, a few seconds.
- `soft_quartic.out`: its output.
- `linear_spectrum.py`: Theorem D's checks. The occurrences of each rigid slot at levels $`n`$ and $`12-n`$, from the characters, with the reducible level 6 as the control; the lowest-level spectrum and its multiplicities on random members, with the coupling and the gyroscopic term each mutated as controls; and, on finite models built from the frames $`\pi_n(x)`$, the splitting, the conservation and positivity of $`H_2`$, an imaginary spectrum and the kernel's dimensions, with a profile of non-constant norm, a wrong coupling weight in $`H_2`$ and an operator below $`-\omega^2/c^2`$ as controls. Self-contained, about a second.
- `linear_spectrum.out`: its output.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
