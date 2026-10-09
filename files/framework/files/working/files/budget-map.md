<a id="top"></a>
/ **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /

---

# The Budget Map

**Type:** Map
**State:** Active
**Status (2026-08-26):** The one-budget-two-readings taxonomy is settled; the inventory's highest-leverage open row is E(S), the realized-sector energy, routed to the stress-tensor-bridge program.
**Summary:** The inventory of what is a budget and what is read off one: a single conserved temporal budget, with temperature and entropy as readings of its state S and the Waltz clock as a phase-to-time map, not budgets of their own.

One conserved budget in this sector, the temporal $`\Psi^2 + S^2 = 1`$, with the spatial $`u_0^2 + J^2 = 1`$ as its twin. Temperature and entropy are two readings of the budget's single state variable $`S`$, not budgets of their own; the Waltz clock is a map from phase to time, not a budget. This note is the inventory the detail pages point back to.

**Related:** [The Temporal Budget Identity](temporal-budget.md), [Redshift and Cooling](redshift-and-cooling.md), [Energy as Resolution Amplitude](energy-as-resolution-amplitude.md), [Entropy as Realization Budget](entropy-as-realization-budget.md), [The Waltz](../../../../spectrum/files/the-waltz.md), [Cosmological Constant](../../../../cosmos/files/cosmological-constant.md) (spatial budget).

---

## The point

The budget, the things read off it, and the clock that times it are spread across several notes, and from a distance they read as three or four parallel budgets. There is one budget in this sector, with a twin in the spatial sector. Temperature and entropy are not budgets; they are two readings of the budget's single state variable $`S`$. The Waltz clock is not a budget either; it is the map from phase to time. Keeping these straight is not housekeeping: treating entropy as its own primitive budget is exactly what produced the scale error the [entropy note](entropy-as-realization-budget.md) had to fix, counting modes where it should count configurations. This map is the inventory.

## The inventory

| Object | Identity or law | Kind | Conserved | What it fixes |
|---|---|---|---|---|
| Temporal budget | $`\Psi^2 + S^2 = 1`$ | budget | yes | the state $`S`$; the realization partition |
| Spatial budget | $`u_0^2 + J^2 = 1`$ | budget (twin) | yes | the reference value $`\Lambda_\text{ref} = 3/R^2`$, through the 3/2 conversion (3 the Gauss/Ricci lift, 1/2 the de Sitter vacuum normalization, imported from general relativity) |
| Temperature | $`T \propto 1/S`$ | reading of $`S`$ | no | per-mode energy; cooling and the thermal redshift law |
| Entropy | $`\Sigma = k_B \ln W_\text{micro}(S)`$ | reading of $`S`$ | no, grows | configurations over realized modes; the rising trend |
| Waltz clock | $`dt/d\tau = S^{-1/2}`$ | map | not applicable | $`H(z)`$, distances, redshift kinematics |

## The one budget, and its twin

$`\Psi^2 + S^2 = 1`$, with $`\Psi = \cos(t/2)`$ the unresolved standing wave and $`S = \sin(t/2)`$ the realized-mode content. It is conserved by construction and has one state variable, $`S`$. Everything thermodynamic on this page is a function of that one number. The spatial budget $`u_0^2 + J^2 = 1`$ is its structural twin on the Möbius wavefunction, fixing the reference value $`\Lambda_\text{ref} = 3/R^2`$ through the 3/2 conversion (3 the Gauss/Ricci lift, 1/2 the de Sitter vacuum normalization, imported from general relativity) that the clock's exponent numerically matches (a correspondence still open). The relation is derived given $`R`$; the reference value is not independently predicted while $`R`$ is calibration-dependent, and its identification with the observed $`\Lambda`$ is gated on the stress tensor ([Cosmological Constant](../../../../cosmos/files/cosmological-constant.md#vi-test-and-scope) §VI). The spatial budget is the only other genuine budget in the framework.

## The two readings

Temperature and entropy are the intensity and the spread of the same budget state. As the budget transfers $`\Psi^2 \to S^2`$, the energy moves from few realized modes into many: per-mode intensity falls ($`T \propto 1/S`$, the cooling) while the configuration count climbs ($`\Sigma = k_B \ln W_\text{micro}`$, the rising trend; the arrow proper is the sampling, see the [entropy note](entropy-as-realization-budget.md) §III). They move in opposite directions because they are conjugate faces of one transfer, the first law showing through, not two ledgers disagreeing.

The anti-circularity lesson lives here. Entropy is a reading of $`S`$, computed as the microstate count over the phase space $`S`$ sets, not a relabeling of $`S`$ itself. Read it the second way and the entropy collapses to the definition, and to the wrong scale (the [entropy note](entropy-as-realization-budget.md) walks the failure). The budget supplies the state; the readings are computed over it.

## The clock, not a budget

$`dt/d\tau = S^{-1/2}`$ maps the budget's phase to the Hubble-clock time $`\tau`$, the time the distance fits use; whether that is observers' proper time is the open placement seam of [Friedmann as Output](friedmann-as-output.md). It is what turns $`S`$ into observable cosmology: $`H(z)`$, distances, and the redshift kinematics that fit Pantheon+ and DESI BAO ([temporal budget §II-III](temporal-budget.md)). It is a map, not a conserved sum, so it is not a budget; it rides on the same $`S`$.

## Out of scope

One entropy ledger sits outside the budget: the gravitational one (Weyl curvature, clumping, black holes), which is Penrose's low-entropy-past puzzle and the dominant share of the universe's entropy. The realization reading accounts for the arrow in its own sector and leaves the gravitational ledger open ([entropy note §V](entropy-as-realization-budget.md)). This map covers the realization sector; it does not annex the gravitational one.

## Where it stands

| Piece | Status |
|---|---|
| Temporal budget identity $`\Psi^2 + S^2 = 1`$ | PROPOSED; consistent with data |
| Cooling, $`T \propto 1/S`$ | ESTABLISHED; derivation and status in [redshift and cooling](redshift-and-cooling.md) §II |
| Waltz clock and the $`H(z)`$ fit | ESTABLISHED at model level; the SN+BAO fit is in [temporal budget](temporal-budget.md) |
| Entropy reading | MOTIVATED; rests on the unwalked shell-unlock map $`S \mapsto N_\text{max}(S)`$ that sets $`W_\text{modes}`$ |
| Realized-sector energy $`E(S)`$ | OPEN, highest-leverage: the amplitude-to-$`T_{\mu\nu}`$ dictionary (program page: [stress-tensor-bridge](stress-tensor-bridge.md)) that would make the $`\Psi^2 \to S^2`$ transfer a counterparty and pin the entropy map (redshift and cooling §VI, entropy note §VIII) |
| Spatial budget and $`\Lambda`$ | DERIVED as a conditional relation: the reference relation $`\Lambda_\text{ref} = 3/R^2`$ from the surface eigenvalue, with the de Sitter normalization imported; the value is not independently predicted while $`R`$ is calibration-dependent, and its identification with the observed $`\Lambda`$ is gated on the stress tensor ([cosmological constant](../../../../cosmos/files/cosmological-constant.md)) |
| Clock from the postulate, $`t_\text{now}`$ from topology, Friedmann as output | OPEN |

---

/ **[`↑top`](#top)** / **[`main`](https://github.com/dmobius3/mode-identity-theory/tree/main/)** / **[`framework`](/files/framework/)** / **[`bedrock`](/files/framework/files/bedrock/)** / **[`dynamics`](/files/framework/files/dynamics/)** / **[`working`](/files/framework/files/working/)** / **[`cosmos`](/files/cosmos/)** / **[`spectrum`](/files/spectrum/)** / **[`tools`](/files/tools/)** /
