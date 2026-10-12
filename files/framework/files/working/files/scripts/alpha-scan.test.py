#!/usr/bin/env python3
"""
alpha-scan.test.py -- RECONSTRUCTION / REGRESSION artifact for the alpha identifiability
scan reported in spectrum/files/fine-structure.md SS IV.  (PF3, 2026-09-01)

This reconstructs the CURRENTLY PUBLISHED enumeration from first principles. It does not
recover the historical script that originally produced it; no such script was found.

Why it exists: the corpus carried two irreconcilable enumerations for these scans, the
source page's 24 restricted / 7,200 broad and claim-ledger row 5's 47 restricted /
3,527 broad. The 93-770% miss range attached to the latter was separately shown to be
unattainable and withdrawn. This script settles which enumeration is reproducible.

Formula under test:  alpha = C(Theta) * Omega_Lambda**(-1/d),  C(Theta) = 2 sin^2(pi Theta)

Run:  python3 alpha-scan.test.py     (stdlib only; exits non-zero if any check fails)
"""
import math, sys

OMEGA = 1.054e122   # canonical Planck-2018 hierarchy (framework, Inputs and Calibration)
ALPHA = 0.0072974   # CODATA low-energy fine-structure constant
TOL   = 0.005       # the "< 0.5%" hit window of SS IV

C   = lambda t: 2 * math.sin(math.pi * t) ** 2
val = lambda k, d: C(k / 120) * OMEGA ** (-1 / d)
hit = lambda v: abs(v / ALPHA - 1) < TOL

# --- the broad control -------------------------------------------------------------
# Positions run over the NON-REDUNDANT HALF-DOMAIN k = 1..60 only. C(Theta) = C(1-Theta),
# so every position above the antinode is a mirror of one below it and contributes no new
# value (framework, One Law: "no new intensity well appears beyond Theta = 1/2").
# Denominators run to the domain order, d = 1..120.
BROAD = [(k, d) for k in range(1, 61) for d in range(1, 121)]

# The same product 7,200 also factors as 120 positions x 60 denominators. That reading is
# WRONG and the hit count is what distinguishes them: it double-counts mirror pairs and
# returns 8 hits in four exact pairs, never the published 9. Kept as a regression guard
# because it is the piece of reasoning most easily lost.
BROAD_MIRRORED = [(k, d) for k in range(1, 121) for d in range(1, 61)]

# --- the restricted class ----------------------------------------------------------
# CANONICAL: the alpha formula's own three choice slots, well x grid x exponent depth.
WELLS, GRIDS, DEPTHS = [13, 21, 34, 55], [60, 120], [30, 60, 120]
RESTRICTED = [(w, N, d) for w in WELLS for N in GRIDS for d in DEPTHS]

# ROBUSTNESS CROSS-CHECK ONLY, deliberately not the primary definition: enumerating by
# Kostant exponents reaches the same count and the same unique selection, but it imports
# the Coxeter structure that belongs to the separate conjugate-pair comparison (ledger
# row 5a / fine-structure SS V). Keeping it secondary is what stops 5a and 5b re-fusing.
KOSTANT = [1, 7, 11, 13, 17, 19, 23, 29]
RESTRICTED_ALT = [(e, 60, d) for e in KOSTANT for d in DEPTHS]

sel = lambda cs: [(w, N, d) for w, N, d in cs if hit(C(w / N) * OMEGA ** (-1 / d))]


def local_density_baseline(half_width=0.10):
    """Expected hits in the +-0.5% window from the local density of scan values in log
    space. This is a density estimate, NOT a fitted null distribution: the candidates are
    structured and correlated through C(k/120) and the shared Omega**(-1/d), so the right
    reading is 'consistent with the baseline', not a sigma."""
    vals = [val(k, d) for k, d in BROAD if val(k, d) > 0]
    win  = math.log(1 + TOL) - math.log(1 - TOL)
    n    = sum(1 for v in vals if abs(math.log(v / ALPHA)) < half_width)
    return n / (2 * half_width) * win


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label:52} got {got!r:>10}  want {want!r}")
    return ok


if __name__ == "__main__":
    hits, base = sel([(k, 120, d) for k, d in BROAD]), local_density_baseline()
    ok = []
    print("BROAD CONTROL (k = 1..60 half-domain x d = 1..120)")
    ok.append(check("combinations", len(BROAD), 7200))
    ok.append(check("hits < 0.5%", len(hits), 9))
    ok.append(check("local-density baseline (1 dp)", round(base, 1), 7.6))
    best = min(hits, key=lambda r: abs(C(r[0] / 120) * OMEGA ** (-1 / r[2]) / ALPHA - 1))
    ok.append(check("best competitor position/denominator", (best[0], best[2]), (34, 55)))
    ok.append(check("best competitor error %, 2 dp",
                    round((C(34 / 120) * OMEGA ** (-1 / 55) / ALPHA - 1) * 100, 2), 0.06))

    print("\nWRONG FACTORIZATION GUARD (k = 1..120 x d = 1..60, same 7,200 product)")
    ok.append(check("combinations", len(BROAD_MIRRORED), 7200))
    ok.append(check("hits (mirror-doubled, never 9)",
                    len(sel([(k, 120, d) for k, d in BROAD_MIRRORED])), 8))

    print("\nRESTRICTED CLASS (canonical: wells x grids x depths)")
    ok.append(check("candidates", len(RESTRICTED), 24))
    ok.append(check("hits < 0.5%", len(sel(RESTRICTED)), 1))
    ok.append(check("unique selection", sel(RESTRICTED)[0], (13, 60, 60)))

    print("\nRESTRICTED CLASS (robustness cross-check: Kostant x depths)")
    ok.append(check("candidates", len(RESTRICTED_ALT), 24))
    ok.append(check("same unique selection", sel(RESTRICTED_ALT), [(13, 60, 60)]))

    print("\nWITHDRAWN LEDGER ENUMERATION (47 restricted / 3,527 broad)")
    print(f"  47 prime: {all(47 % i for i in range(2, 8))}   "
          f"3527 prime: {all(3527 % i for i in range(2, 60))}")
    print("  Neither is a positions x denominators product, so neither can arise from the")
    print("  family of enumerations that reproduces the source page. Deduplicating the")
    print(f"  7,200 broad set by value leaves "
          f"{len({round(val(k, d), 18) for k, d in BROAD})}, not 3,527, so it is not a")
    print("  dedupe of this space either. NOT RECONSTRUCTED, and not thereby disproved:")
    print("  a differently-filtered candidate set may have existed; its filter is unrecorded.")

    print(f"\n{sum(ok)}/{len(ok)} checks passed")
    sys.exit(0 if all(ok) else 1)
