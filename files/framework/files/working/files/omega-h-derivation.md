<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# Ω_Ψ(Θ): Frozen Derivation Question

**Type:** Program
**State:** Blocked
**Status (2026-07-16):** OPEN, frozen before any attempt: derive Ω_Ψ(Θ) for a specified observer congruence. Blocked on the congruence choice: the static channel gives p=2, a freely-falling one p=4 or a nonzero constant, so the black-hole compound limit is underdetermined until the clock field is specified.
**Summary:** The frozen question of deriving Ω_Ψ(Θ) near a horizon, whose value gates whether the black-hole double-zero limit is determinate.
**Inputs:** `../../../../cosmos/files/black-hole.md` §II (where the question originates), §VIII.1 (the Φ→Θ mapping)

> Do not assume that the compound scaling-law limit vanishes.

**Notation update (2026-09-04).** The phase-gradient hierarchy previously written $`\Omega_H`$ on this page is now written $`\Omega_\Psi`$, reserving $`\Omega_H`$ for the cosmological rate hierarchy $`(c/H\ell_P)^2`$. Notation only: the frozen question, its equations, hypotheses, stop conditions and adjudication are unchanged, and the pre-migration text is in git. One result of the split sharpens this page's own question rather than altering it: for any lapse $`d\tau = N\,dt`$ the factor $`N`$ cancels from the ratio of the two logarithmic gradients, and $`\Omega_\Psi/\Omega_H = (\Psi/S)^4`$, so a congruence reconciling the two ledgers must produce exactly $`d\tau/d\tau_H = (S/\Psi)^2`$. A channel differing by any other power of $`S/\Psi`$ is not closing that gap.

OPEN. This is a research question, not a derivation in progress. It is frozen here, before any attempt, specifically so a later attempt cannot be shaped by wanting to recover [Black Double Zero's](../../../../cosmos/files/black-hole.md)'s title mechanism. A negative or inconclusive result is as valid an outcome as a positive one and does not require another retreat from that page; the page has already been corrected independent of how this resolves. §V records a partial result: the exterior static channel gives $`p=2`$ for any stationary clock field with a fixed Killing frequency; the free-fall channel is underdetermined, since the framework has no field equation fixing the clock's extension into the geometry. This does not select a preferred $`\Omega_\Psi`$ and is not written back to that page (per §IV below).

---

## I. The Frozen Question

For a specified observer congruence or invariant phase-gradient definition, derive $`\Omega_\Psi(\Theta)`$ near a Schwarzschild horizon and determine the asymptotic exponent $`p`$ in $`\Omega_\Psi \sim \Theta^p`$. Do not assume the compound scaling-law limit $`C(\Theta) \cdot \Omega_\Psi^{-n/2}`$ vanishes; determine what it actually does.

## II. The Chain, and What Must Be Decided Before Calculating

```math
\Psi(t) \;\longrightarrow\; \Psi\bigl(t(\tau,r)\bigr) \;\longrightarrow\; \kappa_\text{phase} = \left|\frac{d\ln\Psi}{d\tau}\right| \;\longrightarrow\; \Omega_\Psi(r) \;\longrightarrow\; \Omega_\Psi(\Theta)
```

Before any of this can be calculated, $`\tau`$ has to mean something specific. The candidates are physically inequivalent, and the answer can depend on which is chosen:

1. Proper time of static exterior observers ($`d\tau = \sqrt{1-r_s/r}\,dt`$; diverges in the relevant sense as $`r\to r_s`$, and no static observer exists at the horizon itself to evaluate the limit on).
2. Proper time of freely falling observers (regular at the horizon; may not show any collapse at all).
3. An invariant norm, e.g. $`\sqrt{\lvert\nabla_\mu\ln\Psi\,\nabla^\mu\ln\Psi\rvert}`$, avoiding a choice of worldline entirely.
4. A preferred MIT clock distinct from either GR observer family, if one can be motivated independently.

If the zero exists only for the static congruence, $`\Omega_\Psi\to0`$ describes exterior redshifted observation, not an observer-independent collapse of the local hierarchy, and the "second zero" framing in [Black Double Zero's](../../../../cosmos/files/black-hole.md) §II would need to say so explicitly rather than presenting $`\Omega_\Psi`$ as if it stood on the same footing as $`\Theta`$.

## III. The Gate

Suppose, near the node, $`C(\Theta) \sim \Theta^2`$ (established) and $`\Omega_\Psi(\Theta) \sim \Theta^p`$ (to be derived). The scaling-law output is

```math
C(\Theta) \cdot \Omega_\Psi^{-n/2} \sim \Theta^{\,2 - pn/2}
```

- $`p < 4/n`$: the compound output vanishes.
- $`p = 4/n`$: finite, nonzero limit.
- $`p > 4/n`$: the compound output diverges.

Deriving merely "$`\Omega_\Psi \to 0`$" is not sufficient; the exponent $`p`$ is the actual gate. Whichever value of $`n`$ is appropriate near a horizon (the manifold-index table elsewhere in the framework uses $`n=1`$ for edge-type observables) should be stated explicitly alongside $`p`$, since the gate's outcome depends on both.

## IV. What Would Count as an Answer

A completed answer states: which $`\tau`$ (§II) was used and why; the derived $`p`$; and which regime of the gate (§III) the horizon falls into, for the stated $`n`$.

A negative or null result, no natural $`\tau`$ produces a clean power law, or the exponent depends on the choice of $`\tau`$ in a way that can't be resolved, is a complete and useful answer. It would mean the "double zero" stays exactly what [Black Double Zero's](../../../../cosmos/files/black-hole.md) now says it is: a conjectured mechanism, not a derived one.

A positive result, a specific $`\tau`$, a derived $`p`$, and a determinate gate outcome, would be the first thing that could restore the title mechanism on merit, and should be written back into that page's §II only at that point, not before.

---

## V. Static Channel Resolved; General Question Underdetermined

**Status:** The exterior stationary construction gives $`p=2`$ for a finite nonzero asymptotic clock rate. No observer-independent $`\Omega_\Psi`$ is selected, because the framework supplies no covariant evolution or transport law for the clock field this section isolates, $`T(x)`$. Not written back to black-hole.md §II: per §IV above, that update is reserved for a positive, determinate result, and this is not one.

### V.1 The missing object is the clock field, not a new complex phase

The framework's standing wave is real: $`\Psi = \cos(t/2)`$, with $`S=\sin(t/2)`$ its budget partner, $`\Psi^2+S^2=1`$ ([temporal-budget](temporal-budget.md) §I). The bookkeeping identity $`\Psi+iS = e^{it/2}`$ is explicitly *not* an independent complex field, $`\Psi`$ is its real part, $`S`$ its imaginary part, two real budget components, not a phase and an amplitude. A calculation for $`\kappa_\text{phase}`$ built on an independently posited $`\Psi=|\Psi|e^{-i\phi}`$ would be computing a different object than the framework's own $`\Psi`$, however suggestively named.

Keep $`\Psi`$ real and promote its argument to a spacetime scalar, $`\Psi(x) = \cos(T(x)/2)`$, where $`T`$ reduces to the cosmological phase $`t`$ far from any mass. Then

```math
\nabla_\mu\ln|\Psi| = -\frac{1}{2}\tan\left(\frac{T}{2}\right)\nabla_\mu T
```

and the covariant, observer-measured rate is

```math
\kappa_\Psi(u) \equiv \left|u^\mu\nabla_\mu\ln|\Psi|\right| = \frac{1}{2}\left|\tan\left(\frac{T}{2}\right)\right|\,\left|u^\mu\nabla_\mu T\right|
```

This is exactly §II's original definition, $`|u^\mu\nabla_\mu\ln\Psi|`$, applied to the framework's actual $`\Psi`$, with no new field introduced. The underdetermined object is now visible on its own: $`K_\mu \equiv \nabla_\mu T`$, the extension of the cosmological clock into the Schwarzschild geometry, paired with the observer $`u^\mu`$. This is the same pair as $`(k_\mu, u^\mu)`$ below, without displacing $`\Psi`$.

The prefactor $`\frac{1}{2}|\tan(T/2)|`$ vanishes at temporal antinodes ($`T=0`$) and diverges at temporal nodes ($`T=\pi`$). Everything below assumes the cosmological clock sits at a phase where this prefactor is finite and nonzero; that is a hypothesis of the calculation, not a free pass, and it does not affect the exponent $`p`$ derived next, which comes entirely from $`u^\mu\nabla_\mu T`$.

### V.2 Static result

Write $`\kappa_\infty \equiv |\partial_t\ln|\Psi||_\infty`$ for the finite, nonzero asymptotic rate implicit in $`\Omega_\Psi\to\Omega_\infty\equiv\Omega_\Lambda`$ far from masses. For $`T=t`$ and $`u_\text{stat}^\mu = x^{-1/2}\partial_t`$ (with $`x\equiv1-r_s/r`$, matching black-hole.md §VIII.1):

```math
\kappa_\Psi(u_\text{stat}) = \frac{\kappa_\infty}{\sqrt x}, \qquad \Omega_\Psi = \Omega_\infty\, x
```

the standard static-observer blueshift of a fixed Killing-time rate, conditional only on the hypothesis above, not on any complex-field ansatz. Using the minimal identity $`C/C_0=x`$ (black-hole.md §VIII.1), exact at every $`r`$ under that page's minimal extension, not merely a near-horizon limit:

```math
C\cdot\Omega_\Psi^{-n/2} = C_0\,x\cdot(\Omega_\infty\,x)^{-n/2} = C_0\,\Omega_\infty^{-n/2}\,x^{\,1-n/2}
```

Near the horizon $`x\propto\Theta^2`$ (from $`C\approx2\pi^2\Theta^2`$ combined with $`C/C_0=x`$), giving $`p=2`$ and $`x^{1-n/2}\sim\Theta^{2-n}`$, matching §III's gate:

| $`n`$ | Behavior | Reading |
|---|---|---|
| 1 (edge) | $`\to 0`$ | Vanishes, and more weakly than $`C`$ alone: a single zero of reduced order, not a "double zero" |
| 2 (surface) | $`= C_0/\Omega_\infty`$ exactly, at every $`r`$, under the minimal identity | Exact cancellation of the near-horizon powers, a finite nonzero coefficient |
| 3 (volume) | $`\to\infty`$ | Diverges |

The $`n=2`$ coefficient is $`C_0/\Omega_\infty \approx 1.2/10^{122}\approx10^{-122}`$: mathematically nonzero, but suppressed by the same order of magnitude the definition of $`\Omega_\Psi`$ already carries. The power-law cancellation is real; it does not produce an order-one horizon output. $`n`$ is not a dial the framework gets to set to make the horizon come out clean: it labels which class of observable (edge/surface/volume-indexed) is being scaled, and the static congruence gives a different limit for each. Any claim about "the" horizon output has to first name the observable.

**A stronger, invariant form of the static result.** Let $`\xi^\mu=(\partial_t)^\mu`$ be the Schwarzschild Killing field, and let $`K_\mu`$ be *any* stationary clock gradient with fixed Killing frequency $`\kappa_\infty = -\xi^\mu K_\mu`$, regardless of its radial component. Since $`u_\text{stat}^\mu = \xi^\mu/\sqrt x`$ has no radial part, $`u_\text{stat}^\mu K_\mu = (\xi^\mu K_\mu)/\sqrt x = -\kappa_\infty/\sqrt x`$ identically. So $`p=2`$ is not a property of the coordinate choice $`T=t`$ specifically; it holds for *any* stationary fixed-Killing-frequency clock field, including ones with ingoing or outgoing radial structure, precisely because the static congruence is blind to the radial component of $`K_\mu`$. The static result is robust in this sense; it is the free-fall congruence, which does have a radial component and so is not blind to $`K_\mu`$'s radial part, where the answer stops being unique.

### V.3 Free fall has no unique result, because it is not blind to $`K_\mu`$'s radial part

"Free-fall proper time is regular at the horizon" does not by itself mean $`\Omega_\Psi`$ cannot collapse there: $`T=t`$ is still built on Schwarzschild $`t`$, the coordinate that is singular at the horizon, not the underlying geometry. For radial infall from rest at infinity ($`dt/d\tau=1/x`$, $`dr/d\tau=-\sqrt{1-x}`$), three extensions of the same asymptotic clock into the Schwarzschild geometry, agreeing far away, give inequivalent horizon behavior:

| Clock field | $`u^\mu\nabla_\mu T / \kappa_\infty`$ as $`x\to0`$ | $`\kappa_\Psi`$ | $`\Omega_\Psi`$ |
|---|---|---|---|
| $`T=t`$ (Killing/Schwarzschild time) | $`1/x`$ | diverges | $`\propto x^2\propto\Theta^4`$: vanishes, $`p=4`$ |
| $`T=v=t+r_*`$ (ingoing, future-horizon-regular) | $`\to 1/2`$ | finite, nonzero | approaches a nonzero constant: no collapse |
| $`T=u=t-r_*`$ (outgoing retarded) | $`\to 2/x`$ | diverges | $`\propto x^2\propto\Theta^4`$: vanishes, $`p=4`$, same exponent as $`T=t`$ |

($`r_*`$ the tortoise coordinate.) $`T=t`$ and $`T=u`$ give the *same* $`\Omega_\Psi`$ exponent, $`p=4`$: both $`\kappa_\Psi`$ divergences are $`\propto x^{-1}`$, so both $`\Omega_\Psi\propto x^2`$. The distinction between them is horizon regularity of the clock field itself, not a different $`\Omega_\Psi`$ branch: $`T=u`$ is additionally singular exactly on the future horizon, the coordinate pathology that Eddington-Finkelstein coordinates are built to cure only on the ingoing side. So free fall does not yield "$`p=4`$, no collapse, or a divergence" as three different $`\Omega_\Psi`$ outcomes; it yields $`\Omega_\Psi\to0`$ (twice, by the same power) or $`\Omega_\Psi\to`$ const, and one of the two vanishing branches is additionally ill-defined as a coordinate object right at the horizon. Either way, asymptotic agreement of $`T=t,v,u`$ far from the mass does not fix which of them correctly extends into the geometry, which is exactly the point: asymptotic normalization alone does not determine $`T(x)`$.

This also weakens candidate 3 (§II) as a way to sidestep the choice. For $`T=t`$, the invariant norm $`\sqrt{|K_\mu K^\mu|}=\kappa_\infty/\sqrt x`$ coincides exactly with the static-observer answer, since the static four-velocity is parallel to $`\partial_t`$; it adds nothing new for that clock field. For $`T=v`$ or $`T=u`$, $`v`$ and $`u`$ are null coordinates and $`K_\mu K^\mu\equiv0`$ identically: the invariant norm is degenerate exactly for the clock choices most natural for a wave (an eikonal along a null congruence), and cannot discriminate ingoing from outgoing there. Candidate 3 does not resolve the choice; it is blind in the case that matters most.

### V.4 Verdict

The exterior static channel gives a robust conditional result, $`p=2`$, holding for any stationary clock field with a fixed Killing frequency, not merely $`T=t`$. A freely falling channel has no unique result: the same congruence gives $`\Omega_\Psi\to0`$ at $`p=4`$ or $`\Omega_\Psi\to`$ a nonzero constant, depending on which horizon-extension of the asymptotic clock is chosen, a choice asymptotic agreement cannot make. The ambiguity is not removed by covariant notation alone, and the invariant norm (candidate 3) is degenerate for exactly the null clock fields that matter. This is more than "still open": it is a demonstrated underdetermination. No observer-independent $`\Omega_\Psi`$ exists until the framework supplies a preferred spacetime clock field $`T(x)`$, or a transport equation for one.

```math
\boxed{\text{What framework principle or field equation determines } T(x)\text{?}}
```

Until such an equation exists, further choices among $`t`$, $`v`$, $`u`$, or another preferred clock extension would be selection by desired outcome. $`p=2`$ stays scoped to the exterior stationary channel; it is not written back into black-hole.md as the second zero.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
