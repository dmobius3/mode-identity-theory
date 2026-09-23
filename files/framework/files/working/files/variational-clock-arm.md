<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Variational Clock Arm

**Type:** Result
**State:** Closed
**Status (2026-09-23):** Run and scored against the parent's pre-registered terms. In the class the parent's §11 names, a quadratic kinetic term with the lapse equation a genuine constraint, the lapse exponent is half the level difference between the kinetic and potential terms, and the standing wave solves the constrained variation at every potential level, so the variation selects nothing. Independent route: FAIL, since the Rayleigh oscillator's own potential gives N = 1. Operator realization of R-HALF: obtained with the amplitude-level potential, but it does not satisfy the promotion bar, and gate (iii) is not met on any of the three pre-named second consequences.
**Summary:** The variational program's first clock arm, run in the reparametrization-invariant class with a quadratic kinetic term: what the lapse variation decides, and what it leaves to the choice of levels.
**Inputs:** `variational-score-to-sample.md` §4, §7, §11, §14, `friedmann-as-output.md` §II, §III, `tick-lemma.md` §III, `half-power-involution.md`, `clock-asymmetry-fit.md`, `scripts/variational-clock-arm/clock_arm_check.py`
**Parent:** `variational-score-to-sample.md`

---

RESULT. Variational mechanics supplies the mean; MIT still has to supply the level pair. Within the minimal reparametrization-invariant class, with a quadratic kinetic term, the lapse exponent is half the level difference between the kinetic and potential terms, and the equations admit the standing wave for every potential level, so they do not select the half power. The native Rayleigh oscillator gives $`N = 1`$. $`N = S^{1/2}`$ occurs only when the potential is independently assigned the amplitude level, $`W \propto S`$, and with that assignment the on-shell action automatically carries the $`S^{3/2}`$ tick weight. That makes the arm an operator realization of R-HALF, not an independent derivation. It is scored against the [parent's](variational-score-to-sample.md) terms, pre-registered on 2026-09-02; §VII records why it was computed rather than frozen first.

---

## I. The class

The parent's §11 names the class this arm runs in, where $`\delta\mathcal{S}/\delta N = 0`$ is a genuine Hamiltonian constraint: a kinetic term $`T`$ quadratic in the velocities and a velocity-free term $`W`$, with the lapse entering as

```math
\mathcal{S} = \int \left( \frac{T}{N} + N\,W \right) dt ,
```

the overall sign fixed by the action convention. The lapse equation gives

```math
N^2 = \frac{T}{W},
```

and eliminating $`N`$ leaves $`2\sqrt{TW}`$: the arithmetic-geometric mean bound $`T/N + NW \geq 2\sqrt{TW}`$, attained. Reparametrization invariance fixes the lapse powers. Under a change of parameter, $`(T/N + NW)\,dt`$ is invariant, while $`(T/N^a + N^b W)\,dt`$ is invariant only at $`a = b = 1`$; unequal powers would eliminate to a weighted mean $`T^{b/(a+b)} W^{a/(a+b)}`$. Inside the class the mean is symmetric. The parameter is gauge, and the parent fixes the gauge: the corpus phase $`t`$ stays fundamental, and [Lemma 0.1](friedmann-as-output.md) makes $`t/2`$ the lap coordinate. With the gauge fixed, the lapse equation determines $`N`$. The half that follows belongs to the quadratic kinetic term. For a kinetic term homogeneous of degree $`p`$ in the velocities, invariance forces $`T/N^{p-1} + NW`$, the lapse equation gives $`N^p = (p-1)\,T/W`$, and the lapse exponent becomes the level difference over $`p`$; every natural kinetic term in the corpus is quadratic, so $`p = 2`$ throughout.

## II. The kinetic term

The parent's §4 names the Rayleigh form as the existing variational foothold and prescribes the first arm as that sector plus the lapse and the budget constraint. So $`T = \Psi'^2`$. On the standing wave the realized share is twice the wave's rate, $`S = -2\Psi'`$, so

```math
T = \Psi'^2 = \tfrac{1}{4}\,S^2 ,
```

which sits at the intensity level. The budget identity is this oscillator's energy integral: $`\Psi'' = -\Psi/4`$ conserves $`\Psi'^2 + \Psi^2/4 = 1/4`$, which is $`\Psi^2 + S^2 = 1`$.

## III. The potential's level sets the lapse

With $`T`$ at the intensity level and a potential $`W = c\,S^w`$ at level $`w`$,

```math
N = \frac{S^{(2-w)/2}}{2\sqrt{c}}, \qquad 2\sqrt{TW} = \sqrt{c}\; S^{(2+w)/2} .
```

For a kinetic term at level $`k`$ the exponents are $`(k-w)/2`$ and $`(k+w)/2`$: the lapse exponent is half the level difference, and the on-shell action sits at the midpoint of the two levels. On the three native levels, with $`c = 1/4`$:

| Potential level | Source | Lapse $`N`$ | $`dt/d\tau`$ | Route menu |
|---|---|---|---|---|
| $`w = 2`$, intensity | the Rayleigh oscillator's own potential at the budget energy, $`W = 1/4 - \Psi^2/4 = S^2/4`$ | $`1`$ | $`S^0`$ | R-PHASE, Model A: dead |
| $`w = 1`$, amplitude | the tick lemma's amplitude ledger | $`S^{1/2}`$ | $`S^{-1/2}`$ | R-HALF's clock; the on-shell action is $`S^{3/2}/2`$, the tick weight |
| $`w = 0`$, count | a constant | $`S`$ | $`S^{-1}`$ | R-INT, Model B: dead |

The other natural kinetic term, the budget metric $`\Psi'^2 + S'^2 = 1/4`$, sits at the count level; with it the half power needs $`W = 1/(4S)`$, level $`-1`$, off the native ladder.

## IV. The constrained variation selects no level

The arm varies $`N`$, $`S`$, $`\Psi`$ and a multiplier $`\lambda`$, with the budget entering only as the multiplier's constraint and nothing substituted early:

```math
\mathcal{L} = \frac{\Psi'^2}{N} + N\,c\,S^w + \lambda\,(\Psi^2 + S^2 - 1).
```

The $`S`$ equation gives $`\lambda = -\tfrac{1}{2} N c\, w\, S^{w-2}`$, and the $`\Psi`$ equation, $`(2\Psi'/N)' = 2\lambda\Psi`$, is solved by $`\Psi = \cos(t/2)`$, $`S = \sin(t/2)`$ with the lapse of §III, for every $`w`$ and $`c`$, wherever $`S > 0`$. The equations of motion therefore select no level: the level sets the lapse and nothing else. The multiplier does real work here: without it, the $`\Psi`$ equation fails at the amplitude level.

## V. Scoring against the parent's terms

The parent pre-registered its PASS and FAIL conditions, the dressed-lapse scoring, the three second consequences and the stop conditions on 2026-09-02 (complete at `c7006d8`), before any functional existed. Scored against them:

- **Independent route: FAIL.** The parent's own first arm, the Rayleigh sector plus the lapse and the budget and nothing else, is the level-2 row. It returns $`N = 1`$, the phase clock: outside the dressed family, and dead on data.
- **Operator realization of R-HALF: obtained, but it does not satisfy the promotion bar.** With the amplitude-level potential the arm returns $`N = S^{1/2}`$, the undressed limit $`\beta = 0`$, and the on-shell action carries the tick weight. It realizes arithmetic R-HALF already had, at the operator level. It does not say why those are the two levels.
- **Gate (iii), across all three named second consequences: not met.** The tick measure appears as the on-shell action, but $`2\sqrt{TW} = 2NW`$ with $`T \propto S^2`$ and $`W \propto S`$ is welded to the choice that set the lapse; it is not a consequence beyond the design target. The realization-rate candidate carries the same $`S^{3/2}`$ weight, but this arm produces no independent $`R`$ equation; identifying the on-shell action with $`dR`$ would be an additional interpretation, so it supplies no second consequence. The $`\Lambda`$ piece of the dressed lapse does not appear: this arm has no vacuum term, and its lapse is undressed.

The parent's stop conditions (§14) then hold the program at MOTIVATED: the route returns $`N = S^{1/2}`$ and nothing independent of it, and only the data select its level from the native three.

## VI. What the arm changes

**Gain.** Reparametrization invariance supplies the geometric-mean structure once the two levels are chosen; it does not select the levels or independently prove the tick lemma's exchange-symmetry premise, L4. In the tick lemma the square root of the ledger product is the output of four premises; here, given the two levels, it is the lapse variation.

**Exposure.** The same fact raises the stakes. In the tick lemma, L4 is a premise, and a clean $`\epsilon \neq 0`$ would cost that premise and nothing else. In this class the mean is not adjustable. Action times lapse is fixed at $`2T`$ here, while in the fit's $`\epsilon`$ family tick measure over lapse is fixed at $`a \propto S`$. Moving the potential to $`w = 1 - 2\epsilon`$ reaches the fit's clock, $`N = S^{1/2+\epsilon}`$, but makes the class's action $`S^{3/2-\epsilon}`$ while the family's tick is $`S^{3/2+\epsilon}`$. They move in opposite directions, so the class and the family share exactly one member, $`\epsilon = 0`$; the only other road to $`\epsilon \neq 0`$ leaves the class, with unequal lapse powers. The arm turns an adjustable premise into a hard consequence of the class and its levels. The one channel that measures it, the [clock-asymmetry fit](clock-asymmetry-fit.md), excluded $`\epsilon = 0`$ at 95% in both tiers at $`\hat\epsilon = -0.106`$. The [Half-Power Clock](friedmann-as-output.md) grades that dial contaminated as a P2 probe on this data, so a contaminated dial cannot cleanly refute the symmetric kernel, and nothing is refuted today. But the only measurement points away from zero, and a clean nonzero value would therefore cost the class or the native-level assignment, rather than merely adjusting L4 inside the fixed amplitude-intensity realization.

**Consistency, not gain.** The action over the lapse is $`2W \propto S`$: the existing identity $`d\mu_{\text{tick}} = a\,d\tau_H`$ with $`a \propto S`$, read from the action side.

## VII. What was known when

The parent's §11 published on 2026-09-02 the potential each natural kinetic term needs for $`N^2 = S`$. With that table public, no freeze of a functional could have been blind, and in this class the pre-named second consequence is arithmetic too. This arm was computed while it was being designed, on 2026-09-23, and it is recorded as a Result scored against the parent's pre-registered terms, not as a Test with a frozen functional. The pre-registration held where it could: the PASS and FAIL conditions, the dressed-lapse scoring, the three second consequences and the stop conditions were all fixed before any functional existed.

## VIII. What could change the verdict

The R-VAR level-selection residue is now the whole clock-arm problem: why should the variational potential carry amplitude weight, $`W \propto S`$? It is the same level-selection issue the gate-(i) qualification exposed, that reciprocity does not select the pair; gate (i) stays closed. Inside the class there is nothing further for the variation to decide: with pure-power terms the lapse is $`S^{(k-w)/2}`$ for whatever levels are chosen, and the table covers the native ones.

Two things could change the verdict: new structural input that selects $`W \propto S`$, or a later arm of the parent's §13 (embedding, sampler, connections, metric) that yields a consequence the mean does not already fix. The scaling law's [boundary-mode uniformity](scaling-law-uniqueness.md#proof-the-schur-separation) marks one place to look, posed as a question: a coupling that keeps every block's boundary profile proportional to $`C(\Theta)`$ leaves the scaling law intact, and one that breaks it would predict sector-dependent shifts of $`C`$ at the wells, which nothing in this arm could produce.

[`clock_arm_check.py`](scripts/variational-clock-arm/clock_arm_check.py) needs sympy, and its record [`clock_arm_check.out`](scripts/variational-clock-arm/clock_arm_check.out) reproduces all eight checks, each against a control that must come out the other way; every quantity is exact.

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
