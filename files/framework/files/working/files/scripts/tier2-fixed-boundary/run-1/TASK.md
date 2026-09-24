# Task: the Dirichlet Jacobi spectrum of a minimal Möbius band in S³

Compute the quantities of §3 by the method of §4, and report them as §5 asks. Everything in §§1-2 is given and already verified. You may re-derive it, but do not change it.

## 1. Setting (given)

Let $S^3(R) \subset \mathbb R^4$ be the round sphere of radius $R$, with orthonormal basis $e_1, e_2, e_3, e_4$. Let $\gamma = S^3(R) \cap \mathrm{span}(e_3, e_4)$, a great circle.

The band $B$ is the image of
$$p(s,t) = R\big[\cos t\,(\cos s\, e_1 + \sin s\, e_2) + \sin t\,(\cos\tfrac{s}{2}\, e_3 + \sin\tfrac{s}{2}\, e_4)\big],\qquad (s,t) \in [0, 2\pi] \times [-\tfrac{\pi}{2}, \tfrac{\pi}{2}],$$
with $(2\pi, t)$ identified with $(0, -t)$.

Given facts:
- **Embedding.** $B$ is an embedded Möbius band, and its boundary is $\gamma$, traversed once.
- **Metric.** $g = R^2[f\,ds^2 + dt^2]$ with $f = 1 - \tfrac34\sin^2 t$, so $f \in [\tfrac14, 1]$.
- **Curvature.** $B$ is minimal: its mean curvature vanishes identically. The squared norm of its second fundamental form is $|A|^2 = 1/(2R^2 f^2)$.
- **Normal fields.** The orientation double cover of $B$ is the annulus $s \in \mathbb R/4\pi\mathbb Z$, $t \in [-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$, with deck map $\tau(s,t) = (s + 2\pi, -t)$. A unit normal $\nu$ of $B$ in $S^3(R)$ on the annulus satisfies $\nu \circ \tau = -\nu$. So normal fields on $B$ are exactly the $\tau$-odd functions on the annulus.
- **Symmetry.** $B$ is invariant under the one-parameter group $G$ that rotates the $(e_1, e_2)$-plane by $c$ and the $(e_3, e_4)$-plane by $c/2$. It acts by $s \mapsto s + c$.

## 2. The operator (given)

The Jacobi operator of $B$ is $J = -\Delta_g - |A|^2 - \mathrm{Ric}(\nu,\nu)$, with $\mathrm{Ric}(\nu,\nu) = 2/R^2$. It acts on $\tau$-odd functions $\psi$ on the annulus, with the Dirichlet condition $\psi = 0$ at $t = \pm\tfrac{\pi}{2}$. The spectrum in question is that of this self-adjoint problem.

**Sectors.** Writing $\psi = e^{ims/2}\varphi(t)$ with $m \in \mathbb Z$, the operator acts on $\varphi$ as
$$R^2 J_m \varphi = -\frac{1}{\sqrt f}\big(\sqrt f\, \varphi'\big)' + V_m \varphi,\qquad V_m = \frac{m^2}{4f} - \frac{1}{2f^2} - 2.$$
- **Parity.** $\tau$-oddness requires $\varphi$ odd in $t$ for even $m$, and even in $t$ for odd $m$. $V_m$ is even in $t$. Each sector is therefore the Sturm-Liouville problem on $[0, \tfrac{\pi}{2}]$ with $\varphi(0) = 0$ for even $m$ or $\varphi'(0) = 0$ for odd $m$, and with $\varphi(\tfrac{\pi}{2}) = 0$.
- **Pairing.** Sectors $m$ and $-m$ give the same problem.
- **Given, $m^2 \geq 16$.** $V_m > 0$ on the whole interval, so these sectors have no negative and no zero eigenvalue.
- **Given, $m = 0$.** Let $X_{12}(x) = (-x_2, x_1, 0, 0)$ be the rotation generator of the $(e_1, e_2)$-plane. Up to the sign of $\nu$, the function
$$\psi_X = \langle X_{12}, \nu\rangle = \frac{\sqrt2\, R\sin 2t}{2\sqrt{3\cos 2t + 5}}$$
  solves $J_0\psi_X = 0$. It vanishes at $t = 0$ and $t = \pm\tfrac{\pi}{2}$, and nowhere else. So sector $m = 0$ has no negative eigenvalue and exactly one zero eigenvalue, with eigenfunction $\psi_X$.

## 3. What to compute

For each of the sectors $m = 1, 2, 3$:
- the **index**, the number of negative eigenvalues of the Dirichlet problem of §2 in that sector;
- the **nullity**, the number of zero eigenvalues.

Then the totals $I$ (index) and $N$ (nullity) over all sectors. Each sector with $|m| \geq 1$ counts twice, for $e^{\pm ims/2}$, and $m = 0$ counts once.

## 4. Method (fixed: follow it exactly)

**4.1 Exact route, for $m = 1$ and $m = 3$.** For a Killing field $K$ of $S^3(R)$, the function $\langle K, \nu\rangle$ on $B$ solves $J\psi = 0$, because isometries carry minimal surfaces to minimal surfaces. Use the four rotation generators that mix the two planes, $X_{13}, X_{14}, X_{23}, X_{24}$, where $X_{ab}(x) = x_a e_b - x_b e_a$. $G$ acts on their span with frequencies $\pm\tfrac12$ and $\pm\tfrac32$, so suitable combinations of their normal components are sector-pure, in $|m| = 1$ and $|m| = 3$. For each of these two sectors:
- (a) Derive the sector-pure combination and its $t$-profile $\varphi_K(t)$.
- (b) Verify symbolically that $R^2 J_m \varphi_K = 0$.
- (c) Count its zeros. Being a normal field, $\varphi_K$ has the sector's parity, so it is the sector's solution of $J_m\varphi = 0$ satisfying the condition at $t = 0$. Locate its zeros in the open interval $(0, \tfrac{\pi}{2})$ from its closed form by symbolic root isolation, cross-checked against the sign changes of 4.2. By Sturm oscillation, the number of these zeros is the sector's index.
- (d) The sector's nullity is 1 if $\varphi_K(\tfrac{\pi}{2}) = 0$, checked symbolically, and 0 otherwise.

If a sector's combination vanishes identically, treat that sector by 4.2 alone.

**4.2 Numerical route**, for $m = 2$, and as a cross-check on $m = 1, 3$ and on $m = 0$ (control C1).
- **Sturm count.** Solve $\varphi'' + \tfrac{f'}{2f}\varphi' - V_m\varphi = 0$ on $[0, \tfrac{\pi}{2}]$ from $t = 0$. Take $\varphi(0) = 0, \varphi'(0) = 1$ for even $m$, and $\varphi(0) = 1, \varphi'(0) = 0$ for odd $m$. Use `scipy.integrate.solve_ivp`, method `DOP853`, with `rtol=1e-12`, `atol=1e-14` and dense output. A nontrivial solution of this regular linear equation has only simple zeros. So count interior zeros as sign changes of the dense output on a uniform grid of $10^5 + 1$ points on $[0, \tfrac{\pi}{2} - 10^{-6}]$, refining each bracket by Brent's method. Record the endpoint ratio $\rho = |\varphi(\tfrac{\pi}{2})| / \max|\varphi|$.
- **Eigenvalues.** Discretize $-\varphi'' - \tfrac{f'}{2f}\varphi' + V_m\varphi = \mu\varphi$, where $\mu = \lambda R^2$, by Chebyshev collocation on $[0, \tfrac{\pi}{2}]$. Impose the sector's condition at $0$ and the Dirichlet condition at $\tfrac{\pi}{2}$. Use two resolutions, 64 and 128 collocation points. Compare every eigenvalue up to and including the first with $\mu > 1$. The two resolutions must agree to $10^{-8}$ absolute in $\mu$.
- **Index and near-zero cases.** A sector's index is the number of eigenvalues with $\mu < -10^{-8}$, and its Sturm count must equal that number. An eigenvalue with $|\mu| \leq 10^{-8}$, or an endpoint ratio $\rho \leq 10^{-8}$, is a near-zero case. Resolve it only by 4.4.
- **Agreement.** The routes must agree on each sector's index, and on whether the sector has a near-zero case. Any disagreement is outcome O4 for that sector.

**4.3 Controls, each able to fail.**
- **C1.** Sector $m = 0$, run through 4.2, must give index 0 and exactly one near-zero case. 4.4 resolves that case as nullity, because $\psi_X$ is exhibited. The normalized numerical eigenfunction must match $\psi_X$ to $10^{-6}$ in the sup norm.
- **C2.** The functions $\varphi_K$ of 4.1 must satisfy their sector equations symbolically, and 4.1 and 4.2 must agree for $m = 1$ and $m = 3$.
- **C3.** Rerun C1 with a mutated operator, and it must fail. Run the two mutations separately: $\mathrm{Ric}(\nu,\nu) = 3/R^2$ in place of $2/R^2$; and $|A|^2$ dropped.

**4.4 Near zero.** A near-zero case counts as nullity only if an exact solution of $J_m\varphi = 0$ satisfying both boundary conditions is exhibited in that sector: $\psi_X$ for $m = 0$, or a combination from 4.1 vanishing at $t = \tfrac{\pi}{2}$ for $m = 1, 3$. A near-zero case without such an exhibited solution makes the sector O4, and its computed value is reported. No interval-arithmetic or other certification branch is used.

**4.5 Outcome classes.** Report which one applies.
- **O1:** $I = 0$ and $N = 1$.
- **O2:** $I \geq 1$. Report $I$ and the sectors carrying it.
- **O3:** $N \geq 2$. Report the sectors carrying the excess.
- **O4:** a control failed, the routes disagreed, or a near-zero case had no exhibited exact solution. Report which, and for which sector.

## 5. Reporting

Put everything in `RETURN.md` in this directory:
- **Per sector ($m = 0, 1, 2, 3$).** Give:
  - the index and nullity, and the route that decided each;
  - for $m = 1, 3$, the closed form of $\varphi_K$ and its zeros in $(0, \tfrac{\pi}{2})$;
  - the Sturm count and the endpoint ratio $\rho$;
  - every compared eigenvalue $\mu$ at both resolutions, as numbers.
- **Totals.** $I$, $N$, and the outcome class of 4.5.
- **Controls.** The result of each of C1, C2 and C3.
- **Method as run.** Any point where you could not follow §4 exactly, and what you did instead.
- **Files.** The scripts that produce every value, and their output records.
- **Consulted material.** A manifest of every file you read.
- **Underdetermined points.** Any point in this task you found underdetermined or ill-posed, with the reading you took.

Rules for the values:
- Report numbers as computed, without interpretation.
- Say, for each value, whether it was computed.
- Report a value your computation did not reach as missing, never as zero.
- "Unresolved" is always an allowed answer.
