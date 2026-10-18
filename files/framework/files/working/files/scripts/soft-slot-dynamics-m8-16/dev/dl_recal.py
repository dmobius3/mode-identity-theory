#!/usr/bin/env python3
"""DL's recalibration claims: the record of DESIGN.md section 7 under the RECAL_PLAN.md calibration, on synthetic
Hamiltonian matrices. Case: synthetic. The production record throughout: margin = linear.margin(||A||, m), the gray zone
(margin/3, 3 margins), nonzero groups linked and typed within tau = max(margin, 10 sqrt(u ||A|| |lambda|)), and the leak
at most 200 u ||A|| / gap. DL's original claims (dl_linear.py) still run under the original calibration (UA).

The systems are dl_linear.py's: 2 x 2 blocks of L on (Re c_j, Im c_j) with the rotating frame's 2 omega J0, mixed by a
random unitary. A synthetic system has no branch amplitude, so m is stated. The synthetic phase chains split at about
0.26 sqrt(u ||A||) at omega = 1.3, like a control at m of about 21 (the controls' largest coefficient is 0.057); claims
on that family run at m = 72, where the synthetic cluster sits at least ten times below the gray zone, as the calibration
asks of the controls. The omega near 36 family splits at about 0.04 sqrt(u ||A||), and runs at m = 0.2, as UB ran it.
These cluster sizes were read in scratch runs before the claims were written, to set that precondition; the outcomes
below are derived from the constructions. Claims 5 and 7 were also seen in scratch runs first: claim 5 to check UB's
finding, claim 7 where the second limit was found.

Claims, each derived before the run, with arms that must turn red:
  1. Claim 3's system (two phase chains, Krein-positive oscillators, a quartet, the real pair diag(-5, 3)), omega 1.3,
     m = 72: V0 of dimension 4 with ranks [2, 0]; (n(L), n(D), K) = (4, 1, 3), k_r = 1, k_c = 1; Hyperbolic.
  1'. Claim 1 at m = 21, where the synthetic chains split like the controls' largest coefficient, over 40 mixings: as
     derived at every mixing, with the cluster at least ten times below the gray zone (UB). As first run it missed the
     headroom at 2 of 40 mixings, 9.59 and 9.94 times (DEVLOG 125, 126), and that FAIL stands (UA). The bar is a tail
     statistic of the mixings (UB): over 20,000 mixings every one classifies as derived and the headroom falls under
     ten at 1.6 percent (UB), at 3.1 percent over 5,000 here, and UA's rerun of these 40 read 10.4. So 1' stays as
     written and is reported, unscored, and the ten-fold requirement is read on the controls (11.7 times).
  1''. Claim 1 at m = 21, over the same 40 mixings: as derived at every mixing (UB). Scored.
  2. The margin's gray zone, below the margin: one phase block lifted to diag(-eta, 5), its zero pair at +-s with
     s^2 = eta 5 / (4 omega^2 + 5). (a) s = 8e-6, inside (margin/3, margin) and above the rank floor's square root: the
     separation is flagged, V0's ranks miss [2, 0], and the point is Unresolved, though the real pair is resolved;
     (b) s = 1e-7, below the gray zone and the rank floor: claim 1's counts and type. Arm: G = 1.0001 (no gray zone),
     where (a)'s separation is not flagged.
  3. The gray zone above the margin: claim 1's oscillators and the phase blocks, Elliptic, omega = 7, m = 72, with an
     oscillator diag(k, k), k = s^2 + 2 omega s, its slow pair at +-i s exactly, Krein-positive, its L eigenvalue k
     outside L's inertia gray zone. (a) s = 0.8 G margins: the separation is flagged, Unresolved; (b) s = 2 G margins:
     resolved, labelled imaginary and definite, (n(L), n(D), K) = (1, 1, 0), Elliptic. Arm: G = 1.0001, where (a) reads
     Elliptic.
  4. The leak bound. (a) linear.leak_bound refuses an infinite, zero or NaN gap and a bound above 1e-4, and returns
     200 u ||A|| / gap otherwise (UA); (b) claim 1's system with its symmetry directions turned off V0 by sin theta:
     ten times the bound is a V0 mismatch and Unresolved, a tenth of it matches; (c) a leak factor of 1e12, whose bound
     exceeds 1e-4: the point is Unresolved, never a pass. Arm: a fixed bound of 1, where (b)'s ten times passes.
  5. UB's collision: the block diag(-a, -2a), a = 35.7^2 / sqrt2, at omega^2 = (3 + 2 sqrt2) a / 4, has one Jordan
     2-chain at +-i 2^(1/4) sqrt(a) = +-35.7i of Krein signature (1, 1), with the phase blocks and Krein-positive
     oscillators, so nothing else leaves the axis; ||A|| about 1,800; 40 mixings at m = 0.2. Each reads Unresolved,
     the collision one mixed group and the only unresolved item, (n(L), n(D)) = (3, 1), K = 2. Arm: one margin for every
     role (kappa_d = 0), where at least one mixing reads Hyperbolic with k_c = 1 (UB: 6 of 40).
  6. Near the collision (UA): the same block at omega^2 = omega*^2 + delta, the exact separation d (delta > 0, two
     imaginary pairs of opposite Krein signs) or real part r (delta < 0, a quartet) at 50 digits; 10 mixings each.
     (a) d = 1e-5, below tau: Unresolved, one mixed group, never Elliptic; (b) d = 1e-3: two definite groups of
     opposite signs, K = 2, Elliptic; (c) r = 1e-5, below tau: Unresolved, never Hyperbolic or Elliptic; (d) r = 1e-3:
     the quartet, k_c = 1, Hyperbolic. Arm: kappa_d = 0, where (c) resolves the quartet below tau.
  7. The second limit, L's inertia, moved by Step 2's cut: claim 3's family at omega = 1.3 and m = 8 (margin about
     3.5e-6, gray zone up to 1.04e-5). A genuine slow pair needs an L eigenvalue near 2 omega s. Under the cut before
     Step 2 (1e-10 ||L||, gray zone to 1e-7 ||L||), the pair at s = 3e-5, its L eigenvalue about 4.6e-8 ||L||, read
     n(L) Unresolved (DEVLOG 116 to 132). Re-derived under Step 2's cut, 1000 u ||L|| with its gray zone to ten times
     it (UB): (a) s = 3e-5 and (b) s = 1e-4, each with its L eigenvalue above L's gray zone and outside A's, read
     Elliptic with nothing unresolved. Arm: the earlier cut, where (a) reads n(L) Unresolved. L's own gray zone is
     Step 3's G_L = 1 arm (UB).
  8. Missing tangents (UA): claim 7's Elliptic family at omega = 1.3 and m = 72. (a) With its phase chains' tangents:
     Elliptic, (n(L), n(D), K) = (1, 1, 0); (b) with an empty list, not declared free of symmetry directions: V0
     cannot be checked, an unresolved item, and the point is Unresolved, never Elliptic. Arm: the empty list read as
     declared (an implicit skip), where (b) reads Elliptic.
  9. L's zero count, alone (UB, 2026-10-17): ker A = ker L x {0}, so L's zero count equals V0's chain count. A slow
     pair near a crossing, diag(k1, K) with K = 1000 at omega = 14, its pair at s = 3e-6 from the exact quartic: its
     k1, about 43 u ||L||, is below L's cut, and the pair is about 5 margins out. The leak bound is held vacuous
     (leak_abs = 1, as claim 4's arm), so the check stands alone. Over 10 mixings at m = 0.2: the zero-count item at
     every mixing. Arm: the check dropped, where at least one mixing reads Elliptic with nothing unresolved (UB).
Reported, unscored (UA): every classification of DL's original claims that changes under the recalibration, each
construction built once and read under both calibrations (dl_changes). Where DL gave no symmetry directions, the
production reading declares none (symmetry_free), as DL ran them.
"""
import os
import sys
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import linear as ln, devtools  # noqa: E402

devtools.require('synthetic')
mp.mp.dps = 50
rng = np.random.default_rng(20261016)
U = np.finfo(float).eps
POS = [0.5, 1.0, 3.0, 10.0, 100.0, 700.0, 1700.0]
REAL_PAIR = np.diag([-5.0, 3.0])
TWO_CHAINS = dict(dim=4, ranks=[2, 0])
MIXED = 'a mixed imaginary group'
SEP = 'the zero cluster is not separated'
S_COLL = 35.7
A_COLL = S_COLL ** 2 / np.sqrt(2.0)
out = []


def say(s):
    print(s, flush=True)
    out.append(s)


def place(blocks):
    m = len(blocks)
    L = np.zeros((2 * m, 2 * m))
    for j, b in enumerate(blocks):
        idx = [j, m + j]
        L[np.ix_(idx, idx)] = b
    return L


def random_unitary_real(m):
    Z = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    Q, R = np.linalg.qr(Z)
    Q = Q * (np.diag(R) / np.abs(np.diag(R)))
    return np.block([[Q.real, -Q.imag], [Q.imag, Q.real]])


def system(blocks, omega, phase=(5.0, -2.0)):
    """A, B, W, L of the mixed system, and the exact phase-chain directions (T c of each phase block)."""
    m = len(blocks)
    R = random_unitary_real(m)
    L = R.T @ place(blocks) @ R
    A, B, W = ln.first_order(L, omega)
    E = np.eye(2 * m)
    sym = [np.concatenate([R.T @ E[j], np.zeros(2 * m)]) for j in range(len(phase))]
    return A, B, W, L, sym


def rec(A, B, W, L, m, sym, **kw):
    return ln.record(A, B, W, L, ln.margin(np.linalg.norm(A, 2), m), symmetry=sym, expected=TWO_CHAINS, **kw)


def claim3_blocks(extra=()):
    return [np.diag([0.0, 5.0]), np.diag([0.0, -2.0])] + [np.diag([k, k]) for k in POS + [-3.0]] + [REAL_PAIR] + list(extra)


def counts(r):
    return (r['nL'], r['nD'], r['K'])


def claim1():
    A, B, W, L, sym = system(claim3_blocks(), 1.3)
    r = rec(A, B, W, L, 72.0, sym)
    ok = (r['separated'] and r['v0_matches'] and r['sdim'] == 4 and r['jordan_ranks'] == [2, 0] and counts(r) == (4, 1, 3)
          and (r['kr'], r['kc'], r['ki']) == (1, 1, 0) and r['type'] == 'Hyperbolic' and not r['unresolved'])
    return ok, r


def claim1_prime(n=40):
    """Claims 1' (as first written, reported, unscored) and 1'' (scored), on the same mixings."""
    rows = []
    for _ in range(n):
        A, B, W, L, sym = system(claim3_blocks(), 1.3)
        r = rec(A, B, W, L, 21.0, sym)
        below = (r['margin'] / ln.GRAY) / r['cluster_max']
        derived = (r['separated'] and r['v0_matches'] and r['sdim'] == 4 and r['jordan_ranks'] == [2, 0]
                   and counts(r) == (4, 1, 3) and (r['kr'], r['kc'], r['ki']) == (1, 1, 0) and r['type'] == 'Hyperbolic'
                   and not r['unresolved'])
        rows.append((derived and below >= 10, below, r['type'], derived))
    return all(x[0] for x in rows), all(x[3] for x in rows), rows


def claim8(implicit=False):
    A, B, W, L, sym = system(elliptic_blocks(), 1.3)
    ra = rec(A, B, W, L, 72.0, sym)
    rb = ln.record(A, B, W, L, ln.margin(np.linalg.norm(A, 2), 72.0), symmetry=[], expected=TWO_CHAINS,
                   symmetry_free=implicit)
    a_ok = ra['type'] == 'Elliptic' and counts(ra) == (1, 1, 0) and not ra['unresolved']
    b_ok = (rb['type'] == 'Unresolved' and not rb['v0_matches']
            and any(u.startswith('V0 cannot be checked: no symmetry directions') for u in rb['unresolved']))
    return a_ok and b_ok, (ra, rb)


def claim9(zero_count=True, n=10):
    omega, s, K = 14.0, 3e-6, 1000.0
    x = -s * s
    k1 = -(x * x + (4 * omega ** 2 + K) * x) / (x + K)       # diag(k1, K): its slow pair at +-i s, exactly
    rows = []
    for _ in range(n):
        A, B, W, L, sym = system(elliptic_blocks([np.diag([k1, K])]), omega)
        r = rec(A, B, W, L, 0.2, sym, zero_count=zero_count, leak_abs=1.0)
        assert k1 / np.linalg.norm(L, 2) < ln.L_CUT and s >= ln.GRAY * r['margin']
        clean_elliptic = r['type'] == 'Elliptic' and not r['unresolved']
        item = any(u.startswith("n(L): L's zero count") for u in r['unresolved'])
        rows.append((item, clean_elliptic, r['dimkerL'], r['blocks'], k1 / np.linalg.norm(L, 2)))
    return all(x_[0] for x_ in rows), rows


def lifted(s, omega=1.3):
    eta = s * s * (4 * omega ** 2 + 5.0) / 5.0
    blocks = claim3_blocks()
    blocks[0] = np.diag([-eta, 5.0])
    return blocks


def claim2(gray=ln.GRAY):
    A, B, W, L, sym = system(lifted(8e-6), 1.3)
    ra = rec(A, B, W, L, 72.0, sym, gray=gray)
    a_ok = (any(u.startswith(SEP) for u in ra['unresolved']) and not ra['v0_matches'] and ra['type'] == 'Unresolved'
            and ra['margin'] / ln.GRAY < 8e-6 < ra['margin'])
    A, B, W, L, sym = system(lifted(1e-7), 1.3)
    rb = rec(A, B, W, L, 72.0, sym, gray=gray)
    b_ok = (rb['separated'] and rb['v0_matches'] and counts(rb) == (4, 1, 3) and rb['type'] == 'Hyperbolic'
            and not rb['unresolved'])
    return a_ok and b_ok, (ra, rb)


def elliptic_blocks(extra=()):
    return [np.diag([0.0, 5.0]), np.diag([0.0, -2.0])] + [np.diag([k, k]) for k in POS] + list(extra)


def slow_pair_system(s, omega, m):
    k = s * s + 2 * omega * s
    # the margin depends on ||A||, which the slow block barely moves: place s from a first build's margin
    return elliptic_blocks([np.diag([k, k])]), k


def claim3(gray=ln.GRAY):
    omega = 7.0
    A0, _, _, _, _ = system(elliptic_blocks([np.diag([1.0, 1.0])]), omega)
    mg = ln.margin(np.linalg.norm(A0, 2), 72.0)
    res = []
    for f, want in ((0.8, 'Unresolved'), (2.0, 'Elliptic')):
        s = f * ln.GRAY * mg
        blocks, k = slow_pair_system(s, omega, 72.0)
        A, B, W, L, sym = system(blocks, omega)
        r = rec(A, B, W, L, 72.0, sym, gray=gray)
        k_rel = k / np.linalg.norm(L, 2)
        near = np.abs(r['lam'] - 1j * s) < 1e-3 * s
        if want == 'Unresolved':
            good = any(u.startswith(SEP) for u in r['unresolved']) and r['type'] == 'Unresolved'
        else:
            good = (r['separated'] and r['type'] == 'Elliptic' and counts(r) == (1, 1, 0) and not r['unresolved']
                    and near.sum() == 1 and r['labels'][near][0] == 'imag'
                    and any(abs(g[0] - 1j * s) < 1e-3 * s and g[4] == 'definite' and g[2] == 0 for g in r['imag_groups']))
        res.append((f, s, k_rel, r, good, k_rel > 1e-7))
    return all(x[4] and x[5] for x in res), res


def turned(sym, V0, sin_t):
    """The symmetry directions turned off V0 by sin_t, along a unit vector orthogonal to V0."""
    outv = []
    for s in sym:
        n = rng.normal(size=s.shape)
        n -= V0 @ (V0.T @ n)
        n /= np.linalg.norm(n)
        sh = s / np.linalg.norm(s)
        outv.append(np.sqrt(1 - sin_t ** 2) * sh + sin_t * n)
    return outv


def claim4(leak_abs=None):
    pure = (np.isnan(ln.leak_bound(1700.0, np.inf)[0]) and ln.leak_bound(1700.0, np.inf)[1] is not None
            and ln.leak_bound(1700.0, 0.0)[1] is not None and ln.leak_bound(1700.0, np.nan)[1] is not None
            and ln.leak_bound(1700.0, 1e-9)[1] is not None
            and ln.leak_bound(1700.0, 0.2)[1] is None and abs(ln.leak_bound(1700.0, 0.2)[0] - 200 * U * 1700 / 0.2) < 1e-25)
    A, B, W, L, sym = system(claim3_blocks(), 1.3)
    r0 = rec(A, B, W, L, 72.0, sym)
    bound = r0['leak_bound']
    kw = {} if leak_abs is None else dict(leak_abs=leak_abs)
    r_hi = rec(A, B, W, L, 72.0, turned(sym, r0['V0'], 10 * bound), **kw)
    r_lo = rec(A, B, W, L, 72.0, turned(sym, r0['V0'], bound / 10), **kw)
    r_vac = rec(A, B, W, L, 72.0, sym, leak_kappa=1e12)
    sys_ok = (not r_hi['v0_matches'] and r_hi['type'] == 'Unresolved' and r_lo['v0_matches'] and r_lo['type'] == 'Hyperbolic'
              and not r_vac['v0_matches'] and r_vac['type'] == 'Unresolved'
              and any('too large to discriminate' in u for u in r_vac['unresolved']))
    return pure and sys_ok, (bound, r_hi, r_lo, r_vac, pure)


def collision_blocks(delta=mp.mpf(0)):
    w2 = (3 + 2 * mp.sqrt(2)) * mp.mpf(A_COLL) / 4 + delta
    return elliptic_blocks([np.diag([-A_COLL, -2 * A_COLL])]), float(mp.sqrt(w2)), w2


def coll_exact(w2):
    """(separation, largest |Re|) of the collision block's two roots in the upper half plane, at 50 digits."""
    a = mp.mpf(A_COLL)
    b = 4 * w2 - 3 * a
    disc = mp.sqrt(b * b - 8 * a * a)
    s = [mp.sqrt((-b + sg * disc) / 2) for sg in (1, -1)]
    s = [z if mp.im(z) > 0 else -z for z in s]
    return float(abs(mp.im(s[0]) - mp.im(s[1]))), float(max(abs(mp.re(z)) for z in s))


def coll_groups(r):
    return [g for g in r['imag_groups'] if abs(g[0].imag - S_COLL) < 0.1]


def claim5(kappa_d=ln.KAPPA_D, n=40):
    blocks, omega, w2 = collision_blocks()
    rows = []
    for _ in range(n):
        A, B, W, L, sym = system(blocks, omega)
        r = rec(A, B, W, L, 0.2, sym, kappa_d=kappa_d)
        cg = coll_groups(r)
        good = (r['type'] == 'Unresolved' and len(r['unresolved']) == 1 and r['unresolved'][0].startswith(MIXED)
                and len(cg) == 1 and cg[0][1] == 2 and cg[0][4] == 'mixed' and (r['nL'], r['nD']) == (3, 1) and r['K'] == 2)
        rows.append((r['type'], r['kc'], good, np.linalg.norm(A, 2), r['margin']))
    return all(x[2] for x in rows), rows, coll_exact(w2)


def delta_for(target, kind):
    """delta giving the exact separation (kind 'd', delta = x > 0) or real part (kind 'r', delta = -x < 0) target.
    Both grow with x, so x is bisected on a log scale."""
    w0 = (3 + 2 * mp.sqrt(2)) * mp.mpf(A_COLL) / 4
    sign, which = (1, 0) if kind == 'd' else (-1, 1)
    lo, hi = mp.mpf(-40), mp.mpf(2)                     # log10 x
    for _ in range(200):
        mid = (lo + hi) / 2
        if coll_exact(w0 + sign * mp.power(10, mid))[which] > target:
            hi = mid
        else:
            lo = mid
    return sign * mp.power(10, (lo + hi) / 2)


def claim6(kappa_d=ln.KAPPA_D, n=10):
    cases = [('a', 'd', 1e-5, 'Unresolved'), ('b', 'd', 1e-3, 'Elliptic'), ('c', 'r', 1e-5, 'Unresolved'),
             ('d', 'r', 1e-3, 'Hyperbolic')]
    res = []
    for tag, kind, target, want in cases:
        dl = delta_for(target, kind)
        blocks, omega, w2 = collision_blocks(dl)
        ex = coll_exact(w2)
        types, goods = [], []
        for _ in range(n):
            A, B, W, L, sym = system(blocks, omega)
            r = rec(A, B, W, L, 0.2, sym, kappa_d=kappa_d)
            cg = coll_groups(r)
            if want == 'Unresolved':
                good = (r['type'] == 'Unresolved' and len(cg) == 1 and cg[0][4] == 'mixed')
            elif want == 'Elliptic':
                good = (r['type'] == 'Elliptic' and len(cg) == 2 and all(g[4] == 'definite' for g in cg)
                        and sorted(g[2] for g in cg) == [0, 1] and r['K'] == 2 and r['balance'] and not r['unresolved'])
            else:
                good = r['type'] == 'Hyperbolic' and r['kc'] == 1 and not cg and r['K'] == 2 and r['balance']
            types.append(r['type'])
            goods.append(good)
        res.append((tag, kind, target, ex, want, types, all(goods)))
    return all(x[6] for x in res), res


def claim7(old_cut=False):
    omega = 1.3
    res = []
    kw = dict(zero_rel=1e-10, l_gray=1e3) if old_cut else {}
    for s in (3e-5, 1e-4):
        k = s * s + 2 * omega * s
        blocks = elliptic_blocks([np.diag([k, k])])
        A, B, W, L, sym = system(blocks, omega)
        r = rec(A, B, W, L, 8.0, sym, **kw)
        k_rel = k / np.linalg.norm(L, 2)
        outside_A = s >= ln.GRAY * r['margin']
        good = (outside_A and k_rel > ln.G_L * ln.L_CUT and r['type'] == 'Elliptic' and counts(r) == (1, 1, 0)
                and not r['unresolved'])
        res.append((s, k_rel, r['margin'], r['type'], [u.split(':')[0] for u in r['unresolved']], good))
    return all(x[5] for x in res), res


def dl_changes():
    """Unscored (UA): every classification of DL's original claims that changes under the recalibration. Each of
    dl_linear.py's constructions is built once and read under both calibrations: the original (its own margin,
    ln.ORIGINAL) and the production record (ln.margin at the construction's m: 0 for the free operator of claim 2, 72
    for the synthetic systems, as above). Claim 1 types nothing and is left out."""
    sys.path.insert(0, HERE)                     # under python3 -I the script's directory is not on the path (UB)
    import dl_linear as dl
    rows = []

    def both(label, A, B, W, L, sym=(), expected=dl.TWO_CHAINS, j=2, m=72.0, floor=None):
        mo = dl.margin_for(A, j) if floor is None else max(dl.margin_for(A, j), floor)
        ro = ln.record(A, B, W, L, mo, symmetry=sym, expected=expected, **ln.ORIGINAL)
        rp = ln.record(A, B, W, L, ln.margin(np.linalg.norm(A, 2), m), symmetry=sym, expected=expected,
                       symmetry_free=len(sym) == 0)
        rows.append((label, ro['type'], counts(ro), rp['type'], counts(rp), rp['unresolved']))

    for s in ('R2', 'R4', 'R5'):
        Bs = dl.basis.Basis(s, 16)
        Fn = dl.fn.Functional(Bs)
        levels = sorted(set(Bs.eig))
        lam = (levels[0] + levels[1]) / 2
        L = Fn.hess_dense(np.zeros(Bs.m, dtype=complex), lam)
        A, Bm, W = ln.first_order(L, np.sqrt(lam))
        both(f'claim 2, the free operator in {s}', A, Bm, W, L, expected=dl.NO_V0, j=1, m=0.0)
    A, B, W, L, V0x, _ = dl.mixed(dl.blocks_for(), dl.OMEGA3)
    both('claim 3', A, B, W, L, list(V0x.T[::2]))
    A, B, W, L, V0x, _ = dl.mixed(dl.blocks_for(extra=(dl.COLL,)), dl.OMEGA4)
    both('claim 4', A, B, W, L, list(V0x.T[::2]))
    E_ = (dl.NO_V0, dl.ONE_CHAIN)
    J = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    for t in (0.5, -0.5):
        Bm = t * np.eye(2)
        both(f'claim 5, case 1, t = {t:+}', *dl.two_dim(Bm), Bm, expected=E_[0], floor=1e-8)
        for bb in (1.0, -1.0):
            Bm = np.diag([t, bb])
            both(f'claim 5, case 2, B = diag(t, {bb:+.0f}), t = {t:+}', *dl.two_dim(Bm), Bm, expected=E_[0], floor=1e-8)
        Bm = np.diag([0.0, t])
        both(f'claim 5, case 3, t = {t:+}', *dl.two_dim(Bm), Bm, expected=E_[1], floor=1e-8)
    for t in (-0.1, 0.1):
        for lab, c0 in (('the degenerate family', 4), ('a regular control', 3)):
            Lm = np.diag([0.0, t - c0, t])
            both(f'claim 5, {lab}, t = {t:+}', *ln.first_order(Lm, None, G=2 * J), Lm, expected=E_[1], floor=1e-8)
    blocks = [np.diag([-2.1e-9, 5.0]), np.diag([0.0, -2.0])] + [np.diag([k, k]) for k in dl.KAPPAS] + [dl.REAL_PAIR]
    A, B, W = ln.first_order(dl.place(blocks), dl.OMEGA3)
    both('claim 6(a)', A, B, W, dl.place(blocks))
    blocks = dl.blocks_for(extra=(np.diag([1.7e-5, 1700.0]),))
    A, B, W = ln.first_order(dl.place(blocks), dl.OMEGA3)
    both('claim 6(b)', A, B, W, dl.place(blocks))
    for label, delta, typ, pattern in dl.CASES:
        blocks = [np.diag([0.0, k]) for k in (5.0, -2.0)] + [np.diag([k, k]) for k in dl.POS_KAPPAS] + [dl.COLL]
        A, B, W, L, V0x, _ = dl.mixed(blocks, float(mp.sqrt(dl.W2STAR + delta)))
        both(f'claim 7, {label}', A, B, W, L, list(V0x.T[::2]))
    blocks = [np.diag([0.0, 0.0])] + [np.diag([k, k]) for k in dl.POS_KAPPAS]
    A, B, W, L, _, R = dl.mixed(blocks, dl.OMEGA3, phase=())
    m_ = len(blocks)
    Ei = np.eye(2 * m_)
    kern = [np.concatenate([R.T @ Ei[0], np.zeros(2 * m_)]), np.concatenate([R.T @ Ei[m_], np.zeros(2 * m_)])]
    both('claim 8', A, B, W, L, kern, expected=dict(dim=2, ranks=[0]))
    L = np.diag([0.0, -100000.0])
    A, B, W = ln.first_order(L, np.sqrt(25001.0))
    both('claim 9', A, B, W, L, [np.array([1.0, 0.0, 0.0, 0.0])], expected=dl.ONE_CHAIN)
    blocks = [np.diag([-1.5e-7, 5.0]), np.diag([0.0, -2.0])] + [np.diag([k, k]) for k in dl.POS_KAPPAS]
    A, B, W, L, _, _ = dl.mixed(blocks, dl.OMEGA3)
    both('claim 10', A, B, W, L)
    return rows


def main():
    failed = 0
    say('DL recalibration claims, under RECAL_PLAN.md: margin = 2 sqrt(u ||A|| max(m, 0.2)), G = 3, kappa_d = 10,'
        ' kappa_L = 200')
    ok, r = claim1()
    failed += not ok
    say(f"1. claim 3's system, m = 72: {'PASS' if ok else 'FAIL'}  margin {r['margin']:.1e}, cluster max {r['cluster_max']:.1e};"
        f" V0 {r['sdim']} {r['jordan_ranks']}; (n(L), n(D), K) = {counts(r)}, k_r {r['kr']}, k_c {r['kc']}; {r['type']};"
        f" unresolved {r['unresolved']}")
    ok1p, ok, rows1 = claim1_prime()
    failed += not ok
    bl = [x[1] for x in rows1]
    say(f"1'. claim 1 at m = 21, {len(rows1)} mixings, as first written (reported, unscored; DEVLOG 125, 126):"
        f" {'PASS' if ok1p else 'FAIL'}  the cluster {min(bl):.2f} to {max(bl):.0f} times below the gray zone, under ten at"
        f" {sum(b < 10 for b in bl)}")
    say(f"1''. claim 1 at m = 21, the same mixings: {'PASS' if ok else 'FAIL'}  as derived at {sum(x[3] for x in rows1)} of"
        f" {len(rows1)}")
    ok, (ra, rb) = claim2()
    failed += not ok
    say(f"2. the gray zone below the margin: {'PASS' if ok else 'FAIL'}  (a) s 8e-6 in ({ra['margin'] / 3:.1e}, {ra['margin']:.1e}):"
        f" {ra['type']}, {[u.split(':')[0] for u in ra['unresolved']]}; (b) s 1e-7: {rb['type']} {counts(rb)}, unresolved"
        f" {rb['unresolved']}")
    ok, res = claim3()
    failed += not ok
    say(f"3. the gray zone above the margin: {'PASS' if ok else 'FAIL'}  " + '; '.join(
        f"s = {f:g} G margins ({s:.1e}), L's eigenvalue {kr:.1e} ||L||: {r['type']}"
        f"{' ' + str([u.split(':')[0] for u in r['unresolved']]) if r['unresolved'] else ''}" for f, s, kr, r, g, _ in res))
    ok, (bound, rh, rl, rv, pure) = claim4()
    failed += not ok
    say(f"4. the leak bound: {'PASS' if ok else 'FAIL'}  (a) refusals {pure}; (b) bound {bound:.1e}: ten times it {rh['type']},"
        f" a tenth {rl['type']}; (c) a factor of 1e12: {rv['type']}, {[u for u in rv['unresolved'] if 'leak' in u]}")
    ok, rows, ex = claim5()
    failed += not ok
    types = [x[0] for x in rows]
    say(f"5. UB's collision near 35.7i: {'PASS' if ok else 'FAIL'}  exact separation {ex[0]:.1e}, |Re| {ex[1]:.1e}; ||A||"
        f" {rows[0][3]:.0f}, margin {rows[0][4]:.1e}; {len(rows)} mixings: " + ', '.join(f'{t} {types.count(t)}' for t in sorted(set(types))))
    ok, res = claim6()
    failed += not ok
    say(f"6. near the collision: {'PASS' if ok else 'FAIL'}  " + '; '.join(
        f"({tag}) {'separation' if kind == 'd' else 'real part'} {ex[0] if kind == 'd' else ex[1]:.1e}: "
        + ', '.join(f'{t} {types.count(t)}' for t in sorted(set(types))) for tag, kind, tg, ex, want, types, g in res))
    ok, res = claim7()
    failed += not ok
    say(f"7. the second limit, L's inertia, under Step 2's cut: {'PASS' if ok else 'FAIL'}  " + '; '.join(
        f"s {s:.0e}, L's eigenvalue {kr:.1e} ||L||, margin {mg:.1e}: {t} {u}" for s, kr, mg, t, u, g in res))
    ok, (r8a, r8b) = claim8()
    failed += not ok
    say(f"8. missing tangents: {'PASS' if ok else 'FAIL'}  (a) with the tangents: {r8a['type']} {counts(r8a)}; (b) an empty"
        f" list, undeclared: {r8b['type']}, {[u for u in r8b['unresolved'] if u.startswith('V0 cannot')]}")
    ok, rows9 = claim9()
    failed += not ok
    say(f"9. L's zero count: {'PASS' if ok else 'FAIL'}  L's eigenvalue {rows9[0][4]:.1e} ||L||; zero count against chains"
        f" {sorted({(x[2], x[3]) for x in rows9})}; the item at {sum(x[0] for x in rows9)} of {len(rows9)}; clean Elliptic at"
        f" {sum(x[1] for x in rows9)}")
    rows9_off = claim9(zero_count=False)[1]
    say(f"   (claim 9 with the check dropped: clean Elliptic at {sum(x[1] for x in rows9_off)} of {len(rows9_off)})")
    res7_old = claim7(old_cut=True)[1]
    say(f"   (claim 7 under the cut before Step 2: {'; '.join(f'{x[0]:.0e} {x[3]} {x[4]}' for x in res7_old)})")
    arms = [('the cut before Step 2 (1e-10, gray zone to 1e-7): claim 7', not all(x[5] for x in res7_old)),
            ('the zero-count check dropped: claim 9', any(x[1] for x in rows9_off)),
            ('the empty tangent list read as declared (an implicit skip): claim 8', not claim8(implicit=True)[0]),
            ('no gray zone (G = 1.0001): claim 2', not claim2(gray=1.0001)[0]),
            ('no gray zone (G = 1.0001): claim 3', not claim3(gray=1.0001)[0]),
            ('a fixed leak bound of 1: claim 4', not claim4(leak_abs=1.0)[0]),
            ('one margin for every role (kappa_d = 0): claim 5', not claim5(kappa_d=0.0)[0]),
            ('one margin for every role (kappa_d = 0): claim 6', not claim6(kappa_d=0.0)[0])]
    c5_0 = claim5(kappa_d=0.0)[1]
    say(f"   (claim 5 under kappa_d = 0: Hyperbolic at {sum(x[0] == 'Hyperbolic' for x in c5_0)} of {len(c5_0)} mixings)")
    for label, red in arms:
        failed += not red
        say(f"   arm, {label}: {'red, as it must be' if red else 'NOT RED'}")
    rows = dl_changes()
    changed = [x for x in rows if (x[1], x[2]) != (x[3], x[4])]
    say(f"Unscored (UA): DL's original constructions under both calibrations, {len(rows)} readings; {len(changed)} change:")
    for label, to, co, tp, cp, up in rows:
        say(f"   {label}: original {to} {co}; recalibrated {tp} {cp}{'   <- changed' if (to, co) != (tp, cp) else ''}"
            f"{'; ' + str([u.split(':')[0] for u in up]) if (to, co) != (tp, cp) and up else ''}")
    say(f"{failed} failed")
    path = os.path.join(HERE, 'dl_recal.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f"DL's recalibration claims: {'PASS' if not failed else 'FAIL'}, 10 scored claims and 8 arms ({failed}"
                      " failed); claim 1' as first written is reported, unscored, and its FAIL in entries 125 and 126 stands.",
                      'The calibration as in RECAL_PLAN.md (provisional); each outcome derived before the run, the synthetic'
                      ' m chosen so the synthetic cluster sits ten times below the gray zone.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
