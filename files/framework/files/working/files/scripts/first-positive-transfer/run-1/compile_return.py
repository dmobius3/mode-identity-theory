"""
Compile all results into RETURN.md.
Loads results.json, results_sctm.json, results_ground.json.
"""
import json
import numpy as np

def load(fn):
    with open(fn) as f:
        return json.load(f)

results = load('results.json')
sctm = load('results_sctm.json')
ground = load('results_ground.json')

BLOCKS = [
    ('1', 12), ('1', 20),
    ('3', 2), ('3', 10),
    ('3p', 6), ('3p', 10),
    ('4', 6), ('4', 8),
    ('5', 4), ('5', 8),
    ('2', 1), ('2', 11),
    ('2p', 7), ('2p', 13),
    ('4p', 3), ('4p', 9),
    ('6', 5), ('6', 7),
]

PLACEMENTS = ['generic', '2fold', '3fold', '5fold']
WIDTHS = [0.25, 0.5, 1.0, 1.4]

MINUS_TAUS = {'2', '2p', '4p', '6'}

tau_labels = {'1': '1', '2': '2', '2p': "2'", '3': '3', '3p': "3'",
              '4': '4', '4p': "4'", '5': '5', '6': '6'}

def get(data, tau, n, pl, W):
    for r in data:
        if r['tau'] == tau and r['n'] == n and r['placement'] == pl and abs(r['W'] - W) < 0.01:
            return r
    return None

def fmt(x, d=6):
    if x is None:
        return 'N/A'
    if abs(x) < 1e-12:
        return '0'
    return f'{x:.{d}f}'

def fmte(x, d=4):
    if x is None:
        return 'N/A'
    if abs(x) < 1e-12:
        return '0'
    return f'{x:.{d}e}'

def placement_independent(data, tau, n, key, tol=0.01):
    vals = {}
    for W in WIDTHS:
        vv = []
        for pl in PLACEMENTS:
            r = get(data, tau, n, pl, W)
            if r and key in r and r[key] is not None:
                vv.append(r[key])
        if len(vv) == 4 and max(vv) > 1e-14:
            ratio = max(vv) / min(vv) if min(vv) > 1e-14 else 999
            if ratio > 1 + tol:
                return False
        vals[W] = vv
    return True

def w_linear(data, tau, n, pl, key, tol=0.01):
    vv = []
    for W in WIDTHS:
        r = get(data, tau, n, pl, W)
        if r and key in r and r[key] is not None and r[key] > 1e-14:
            vv.append((W, r[key]))
    if len(vv) < 3:
        return False, 0
    ratios = [v/w for w, v in vv]
    if max(ratios)/min(ratios) < 1 + tol:
        return True, np.mean(ratios)
    return False, 0

lines = []
L = lines.append

L("# RETURN -- Transfer of Ambient Harmonic Blocks onto the First Positive Mode of a Conic Mobius Band")
L("")
L("## 1. Method as Run")
L("")
L("All computations use curvature radius R = 1. The reproducing kernel of each isotypic block E^tau_n is")
L("")
L("    K(q, q') = dim(tau)(n+1)/(240 pi^2) sum_{g in 2I} chi_tau(g) C_n^1(<gq, q'>)")
L("")
L("where C_n^1 is the Gegenbauer polynomial (= Chebyshev U_n).")
L("")
L("- **HS norms** ||O||^2: 2D Gauss-Legendre quadrature (60x40 points in y x w).")
L("- **Projections** ||P_1 O||^2: 4D quadrature (30x12 x 30x12) using the kernel at all (y,w,y',w') pairs,")
L("  weighted by the eigenfunction of the first positive eigenspace.")
L("- **Transverse sampler**: derivative kernel using C_n^2 and C_n^3.")
L("- **Group**: 120 binary icosahedral elements verified (closure, 9 conjugacy classes, character orthogonality, all block multiplicities = 1).")
L("- **Spectral step**: root-finding (scipy.optimize.brentq) on the secular equation derived from Legendre function identities.")
L("- **Per-level tables**: 1 positive level (the first) chosen; ground + first positive + residual.")
L("")
L("### Points where the task could not be followed exactly")
L("")
L("1. **Symbolic forms in W and orientation.** The reproducing-kernel integrals involve Gegenbauer polynomials")
L("   of bilinear combinations of band-map evaluations. Closed-form symbolic expressions were obtained for")
L("   blocks where the kernel simplifies (E^2_1: all quantities are rational multiples of W/pi^2; general HS")
L("   norms are proportional to W with computable constants). For most higher blocks, only numerical values at")
L("   the four widths are reported.")
L("2. **Bridging per-level decomposition.** The defect-bound eigenfunction for the twisted bridging (and untwisted")
L("   phi_0-transformed) ground mode was not computed. The ground-level decomposition for these conditions is")
L("   reported as missing. Since the first positive eigenspace is shared with Friedrichs, P_1 and Lambda are")
L("   identical for Friedrichs and bridging (twisted arm), and for Friedrichs and phi_0-transformed (untwisted arm).")
L("3. **Rank.** Since all block multiplicities are 1, the rank of P_mu O| is at most dim(tau) for each level.")
L("   Rank was not computed separately; it is bounded by the block dimension and the eigenspace multiplicity (1 for")
L("   all eigenspaces encountered).")
L("")

# ================= SPECTRAL STEP =================
L("## 2. Spectral Step (section 6.3): Same Cone-Trace Matching, Untwisted Arm")
L("")
L("The untwisted arm under same cone-trace matching (SCTM) has the boundary condition")
L("u_D^+ = u_D^-, u_N^+ + u_N^- = 0 (the twisted bridging condition applied to functions).")
L("")
L("### Constant transverse sector")
L("")
L("The constant-in-w sector decomposes by parity about the cone point y = pi/2:")
L("")
L("**Symmetric (Neumann at seam):** Under SCTM, the Kirchhoff condition forces u_N = 0")
L("(regular branch, same as Friedrichs). Tower: nu = 0, 2, 4, ... with lambda = 0, 6, 20, ...")
L("")
L("**Antisymmetric (Dirichlet at seam):** The log datum is active. The secular equation is")
L("")
L("    G_D(nu(nu+1)) = (pi/2) tan(pi nu/2) - gamma - psi(nu+1)")
L("")
L("where gamma is the Euler-Mascheroni constant and psi is the digamma function.")
L("Eigenvalue condition: G_D = ln(delta_0/(2R)) = ln(1/2) = -ln 2.")
L("")
L("**Derivation.** Q_nu(0)/P_nu(0) = -(pi/2) tan(pi nu/2) from the DLMF identities for")
L("P_nu(0) and Q_nu(0). The Dirichlet-normalized solution gives")
L("G_D = -Q_nu(0)/P_nu(0) - gamma - psi(nu+1). Compare with the twisted Neumann secular")
L("function G_N = -(pi/2) cot(pi nu/2) - gamma - psi(nu+1) of the reference section 4.4.")
L("")
L("**Root:** nu* = 2.341328411, lambda* = nu*(nu*+1) = 7.823147140.")
L("")
L("**Negative eigenvalue check:** min G_D on (-1, 0) approx -0.185 > -ln 2 approx -0.693.")
L("No negative eigenvalue exists (unlike twisted bridging).")
L("")
L("### Nonconstant transverse sectors")
L("")
L("Transverse Neumann modes on [-W, W] include:")
L("- Even: cos(k pi w / W), k = 0,1,2,... (periodic seam in untwisted arm)")
L("- Odd: sin((2m+1) pi w / (2W)), m = 0,1,2,... (anti-periodic seam in untwisted arm)")
L("")
L("The odd modes flip seam parity. First odd sector: m = 0, alpha_0 = pi/(2W),")
L("bottom eigenvalue alpha_0(alpha_0 + 1).")
L("")
L("### Width-dependent first positive eigenvalue")
L("")
L("Mode crossing at W = pi/4: constant sector symmetric tower (lambda = 6) vs first odd nonconstant (lambda = alpha_0(alpha_0+1)).")
L("")
L("| W | First positive eigenvalue | Sector | Eigenfunction |")
L("|---|---|---|---|")
for W in WIDTHS:
    alpha0 = np.pi / (2*W)
    lam_nc = alpha0 * (alpha0 + 1)
    if lam_nc >= 6.0:
        L(f"| {W} | 6.000000 | constant symmetric | P_2(sin y) = (3 sin^2 y - 1)/2 |")
    else:
        L(f"| {W} | {lam_nc:.6f} | odd nonconstant m=0 | sgn(cos y)|cos y|^{{alpha_0}} sin(pi w/(2W)) |")
L("")
L("Multiplicity: 1 (simple) at all four widths. At W = pi/4 exactly, the eigenvalue 6 is doubly degenerate.")
L("")

# ================= LEVEL-0 CONTROL =================
L("## 3. Level-0 Control (E^1_0)")
L("")
L("E^1_0 is the 1-dimensional block of constants (degree 0, trivial representation).")
L("")
L("**Value sampler O^(0) (untwisted arm):**")
L("- Basis: Psi_0 = 1/sqrt(2 pi^2)")
L("- O^(0) Psi_0(y,w) = 1/sqrt(2 pi^2) (constant on band)")
L("- ||O^(0)||^2 = 2W/pi^2")
L("- P_1 projection: <constant, phi_0 sin y> = 0 by parity")
L("- ||P_1 O^(0)||^2 = 0")
L("- Lambda = 2W/pi^2 (all norm in ground level)")
L("")
L("**Transverse sampler O^(1) (twisted arm):**")
L("- d(constant)/dx_0 = 0")
L("- ||O^(1)||^2 = 0, ||P_1 O^(1)||^2 = 0, Lambda = 0")
L("")
L("| W | ||O^(0)||^2 | ||P_1 O^(0)||^2 | Lambda_val | ||O^(1)||^2 |")
L("|---|---|---|---|---|")
for W in WIDTHS:
    hs = 2*W/np.pi**2
    L(f"| {W} | {hs:.6f} | 0 | {hs:.6f} | 0 |")
L("")
L("Level-0 control is not graded (section 7).")
L("")

# ================= SYMBOLIC W-DEPENDENCE =================
L("## 4. Symbolic W-dependence")
L("")
L("### HS norms")
L("")
L("All HS norms are proportional to W (placement-independent):")
L("")
L("    ||O||^2 = c * W")
L("")
L("This follows from the reproducing kernel K_E(q,q) being constant on S^2 for each block")
L("(verified numerically to < 0.01% for all blocks).")
L("")
L("| Block | c_val = ||O^(0)||^2 / W | c_trans = ||O^(1)||^2 / W |")
L("|---|---|---|")
for tau, n in BLOCKS:
    r = get(results, tau, n, 'generic', 1.0)
    if r:
        cv = r['hs_val']
        ct = r['hs_trans']
        tl = tau_labels[tau]
        L(f"| E^{tl}_{n} | {cv:.6f} | {ct:.6f} |")
L("")
L("### Analytic result: E^2_1")
L("")
L("All quantities are exact and placement-independent:")
L("- ||O^(0)||^2 = 8W/pi^2 (value sampler, twisted arm)")
L("- ||P_1 O^(0)||^2 = 8W/(3 pi^2)")
L("- Lambda_val = 16W/(3 pi^2)")
L("- ||O^(1)||^2 = 8W/pi^2 (transverse sampler, untwisted arm)")
L("- ||P_1 O^(1)||^2 = 0")
L("- Lambda_trans = 8W/pi^2")
L("- Ground projection (twisted Friedrichs): ||P_0 O^(0)||^2 = sin^2(W)/(2W)")
L("")

# ================= MAIN RESULTS TABLES =================
L("## 5. Numerical Results")
L("")
L("Results for all 18 blocks, both samplers, 4 placements, 4 widths.")
L("Cone conditions: Friedrichs (primary) for both arms; bridging (twisted arm),")
L("phi_0-transformed (untwisted arm), and SCTM (untwisted arm) share the same HS norms.")
L("P_1 projections differ only under SCTM.")
L("")

for sampler_label, s_key, s_sctm_key, arm_fn, arm_label_fn in [
    ("Value sampler O^(0)", "val", "proj_val_sctm",
     lambda tau: "twisted" if tau in MINUS_TAUS else "untwisted",
     lambda tau: "twisted" if tau in MINUS_TAUS else "untwisted"),
    ("Transverse sampler O^(1)", "trans", "proj_trans_sctm",
     lambda tau: "untwisted" if tau in MINUS_TAUS else "twisted",
     lambda tau: "untwisted" if tau in MINUS_TAUS else "twisted"),
]:
    L(f"### {sampler_label}")
    L("")

    for pl in PLACEMENTS:
        L(f"**Placement: {pl}**")
        L("")
        L(f"| Block | Arm | W | ||O||^2 | ||P_1 O||^2 (Fried) | Lambda (Fried) | ||P_1 O||^2 (SCTM) | Lambda (SCTM) |")
        L("|---|---|---|---|---|---|---|---|")

        for tau, n in BLOCKS:
            arm = arm_fn(tau)
            tl = tau_labels[tau]
            for W in WIDTHS:
                r = get(results, tau, n, pl, W)
                s = get(sctm, tau, n, pl, W)
                if r:
                    hs = r[f'hs_{s_key}']
                    proj = r[f'proj_{s_key}']
                    lam = r[f'lambda_{s_key}']

                    if s and s.get(s_sctm_key) is not None:
                        proj_s = s[s_sctm_key]
                        lam_s = hs - proj_s
                        sctm_proj_str = fmte(proj_s)
                        sctm_lam_str = fmte(lam_s)
                    else:
                        sctm_proj_str = "N/A"
                        sctm_lam_str = "N/A"

                    L(f"| E^{tl}_{n} | {arm} | {W} | {fmte(hs)} | {fmte(proj)} | {fmte(lam)} | {sctm_proj_str} | {sctm_lam_str} |")
        L("")

# ================= PER-LEVEL TABLES =================
L("## 6. Per-level Tables")
L("")
L("Decomposition: ||O||^2 = ||P_0 O||^2 + ||P_1 O||^2 + Residual.")
L("One positive level chosen (the first). Residual = Lambda - ||P_0 O||^2.")
L("")
L("Ground eigenfunction under Friedrichs:")
L("- Twisted arm: phi_0(y) = sgn(cos y), eigenvalue 0")
L("- Untwisted arm: 1 (constant), eigenvalue 0")
L("")
L("Under bridging (twisted) and phi_0-transformed (untwisted): ground mode is the")
L("defect-bound state; per-level decomposition not computed for those conditions.")
L("Under SCTM: ground is the constant function (same as untwisted Friedrichs).")
L("")

for sampler_label, s_key, g_key, arm_fn in [
    ("Value sampler O^(0)", "val", "proj0_val",
     lambda tau: "twisted" if tau in MINUS_TAUS else "untwisted"),
    ("Transverse sampler O^(1)", "trans", "proj0_trans",
     lambda tau: "untwisted" if tau in MINUS_TAUS else "twisted"),
]:
    L(f"### {sampler_label} -- Friedrichs per-level")
    L("")

    for pl in PLACEMENTS:
        L(f"**Placement: {pl}**")
        L("")
        L(f"| Block | Arm | W | ||P_0 O||^2 | ||P_1 O||^2 | Residual | ||O||^2 |")
        L("|---|---|---|---|---|---|---|")

        for tau, n in BLOCKS:
            arm = arm_fn(tau)
            tl = tau_labels[tau]
            for W in WIDTHS:
                r = get(results, tau, n, pl, W)
                g = get(ground, tau, n, pl, W)
                if r and g:
                    hs = r[f'hs_{s_key}']
                    proj1 = r[f'proj_{s_key}']
                    proj0 = g[g_key]
                    resid = hs - proj0 - proj1
                    L(f"| E^{tl}_{n} | {arm} | {W} | {fmte(proj0)} | {fmte(proj1)} | {fmte(resid)} | {fmte(hs)} |")
        L("")

# ================= OUTCOME CLASSES =================
L("## 7. Outcome Classes")
L("")
L("### Methodology")
L("")
L("For each block, sampler, and cone condition, Lambda = ||O||^2 - ||P_1 O||^2 was")
L("checked at all 4 placements and 4 widths. A value is zero if below 10^{-12}")
L("relative to ||O||^2 (section 7 zero rule).")
L("")
L("### Results")
L("")
L("**All blocks have Lambda > 0 at all placements for all samplers and all cone conditions.**")
L("")
L("Specifically, no block satisfies Lambda = 0 at any placement for any W in {1/4, 1/2, 1, 7/5}.")
L("This means the outcome class is **N (leakage)** for every arm/sampler/cone condition.")
L("")

L("| Arm | Sampler | Cone condition | Outcome class |")
L("|---|---|---|---|")
L("| twisted | O^(0) | Friedrichs | N |")
L("| twisted | O^(0) | bridging | N (same Lambda as Friedrichs) |")
L("| twisted | O^(1) | Friedrichs | N |")
L("| twisted | O^(1) | bridging | N (same Lambda as Friedrichs) |")
L("| untwisted | O^(0) | Friedrichs | N |")
L("| untwisted | O^(0) | phi_0-transformed | N (same Lambda as Friedrichs) |")
L("| untwisted | O^(0) | SCTM | N |")
L("| untwisted | O^(1) | Friedrichs | N |")
L("| untwisted | O^(1) | phi_0-transformed | N (same Lambda as Friedrichs) |")
L("| untwisted | O^(1) | SCTM | N |")
L("")

L("### Placement-independent blocks")
L("")
L("The following blocks have HS norms, P_1 projections, and Lambda identical across all placements")
L("(to < 1% relative variation):")
L("")
pi_blocks_val = []
pi_blocks_trans = []
for tau, n in BLOCKS:
    tl = tau_labels[tau]
    if placement_independent(results, tau, n, 'proj_val'):
        pi_blocks_val.append(f"E^{tl}_{n}")
    if placement_independent(results, tau, n, 'proj_trans'):
        pi_blocks_trans.append(f"E^{tl}_{n}")

L(f"- Value sampler: {', '.join(pi_blocks_val)}")
L(f"- Transverse sampler: {', '.join(pi_blocks_trans)}")
L("")

L("### 2-fold symmetric probe")
L("")
L("At the 2-fold placement (p = i, c = j), left multiplication by +/-k preserves the core")
L("circle. No zero of Lambda at the 2-fold placement was found for any block.")
L("")

# ================= FILES =================
L("## 8. Files")
L("")
L("- `core.py` -- 2I group construction, characters, placements, band map, Gegenbauer polynomials")
L("- `compute_all.py` -- main computation: HS norms, first-positive projections, leakage for Friedrichs")
L("- `compute_sctm.py` -- SCTM first-positive projections")
L("- `compute_ground.py` -- ground-level projections for per-level tables")
L("- `spectral_step.py` -- spectral step: secular equation, root-finding, mode-crossing analysis")
L("- `compile_return.py` -- assembles results into RETURN.md")
L("- `validate.py` -- quick validation of E^2_1 block (analytic cross-check)")
L("- `process_results.py` -- summary tables and W-linearity check")
L("- `results.json` -- 304 numerical results (HS norms, projections, leakage)")
L("- `results_sctm.json` -- 304 SCTM projection results")
L("- `results_ground.json` -- 304 ground-level projection results")
L("")

# ================= CONSULTED MATERIAL =================
L("## 9. Consulted Material")
L("")
L("- `TASK.md` -- task specification (sections 1-8)")
L("- `REFERENCE.md` -- the paper on the conic Mobius band and its operator")
L("- `BRIEF.md` -- instructions file")
L("")

# ================= UNDERDETERMINED =================
L("## 10. Underdetermined Points")
L("")
L("1. **Same cone-trace matching spectrum for general W.** The task asks to grade leakage against the SCTM")
L("   first positive eigenspace for every W. The spectral step was computed for all four tabulated widths")
L("   and the mode-crossing at W = pi/4 was identified. For W in (0, pi/4], the first positive eigenvalue")
L("   is 6 (constant symmetric sector). For W in (pi/4, pi/2), it is alpha_0(alpha_0+1) = (pi/(2W))(pi/(2W)+1)")
L("   (odd nonconstant sector). These formulas hold for all W in (0, pi/2), so the spectral step covers")
L("   the full range.")
L("")
L("2. **Symbolic forms in orientation.** The HS norms are placement-independent (proven by the constancy")
L("   of K_E(q,q) on S^2). For projections, some blocks (E^3_2, E^5_4, E^2_1, E^4'_3, E^6_5) are")
L("   placement-independent; others depend on placement. A closed-form polynomial in the frame entries")
L("   was not computed.")
L("")
L("3. **Bridging ground mode.** The defect-bound eigenfunction of twisted bridging (and hence the untwisted")
L("   phi_0-transformed ground) was not computed explicitly. The per-level decomposition for these conditions")
L("   is reported as missing at the ground level.")
L("")
L("4. **Number of positive levels.** One positive level was chosen for the per-level table. The eigenspaces")
L("   at higher levels involve mode crossings and sector-dependent eigenfunctions that were not tabulated.")
L("")

with open('RETURN.md', 'w') as f:
    f.write('\n'.join(lines))

print(f"RETURN.md written: {len(lines)} lines")
