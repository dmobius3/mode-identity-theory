#!/usr/bin/env python3
"""DL: the linear record of DESIGN.md section 7, on synthetic Hamiltonian matrices, the instrument's own free operator
(no branch) and the Hamiltonian-Krein page's models. Case: synthetic. Before D6 (UA, UB).

The synthetic systems are built from 2 x 2 blocks of L on (Re c_j, Im c_j), with the gyroscopic term 2 omega J0 of
the rotating frame, and mixed by a random unitary U(m) (an orthogonal map that commutes with J0, so A is mixed by an
orthogonal similarity). Their counts are derived by hand, block by block:
  - a phase block diag(0, k): a zero 2-chain, x = (e_Re, 0), y = (-(2 omega/k) e_Im, e_Re), with B(y, y) = 1 + 4 omega^2/k,
    and the pair +-i sqrt(k + 4 omega^2), Krein-positive;
  - an oscillator diag(k, k): +-i(sqrt(omega^2 + k) +- omega), all Krein-positive for k > 0, and for omega^2 + k < 0 a
    quartet;
  - the real pair diag(-5, 3): s^4 + (4 omega^2 - 2) s^2 - 15 = 0, one real pair and one Krein-positive imaginary pair;
  - the collision diag(-1, -2): s^4 + (4 omega^2 - 3) s^2 + 2 = 0, double at omega*^2 = (3 + 2 sqrt2)/4, where
    s^2 + s G + L has rank one: one Jordan 2-chain at +-i 2^(1/4), of Krein signature (1, 1). At omega^2 = omega*^2 + delta
    it gives, for delta > 0, two imaginary pairs of opposite Krein signs about 2 sqrt(delta) apart, and for delta < 0 a
    quartet with real parts about sqrt(-delta) (exact values at 50 digits in claim 7);
  - a free complex dof diag(0, 0): a semisimple double zero, with D = 0 exactly on it, and the pair +-2 i omega,
    Krein-positive.

Claims, with arms that must turn red:
  1. The first-order form: A^T W = B, W skew and invertible, A^T W + W A = 0, and the spectrum closed under
     lambda -> -conj(lambda) and lambda -> conj(lambda), for random symmetric L and omega.
  2. The free operator (UB): at c = 0, lam between the two lowest levels, omega = sqrt(lam), in R2, R4 and R5 at N = 16,
     A's eigenvalues are +-i(sqrt(e) - omega) and +-i(sqrt(e) + omega) on each level, Krein-negative exactly on the
     levels below lam; V0 = {0}, n(D) = 0, K = n(L); typed Elliptic.
  3. Zero Jordan chains at ||A|| about 1,700: two phase blocks (k = 5, -2), eight oscillators (one a quartet) and the
     real pair, mixed. V0 (Schur) has dimension 4 and lies on the exact V0 = span(x_j, y_j); the Schur block's ranks
     give two chains of length 2; (n(L), n(D), K) = (4, 1, 3), with k_r = 1, k_c = 1, k_i = 0; the same counts as the
     unmixed blocks read one by one; typed Hyperbolic.
  4. A defective nonzero eigenvalue (UA, UB): claim 3's system with the collision block added, at its omega. V0
     (Schur) still lies on the exact V0; (n(L), n(D), K) = (6, 1, 5), with k_r = 1, k_c = 1, k_i = 1; the collision is
     one mixed group, its type the one item unresolved, and the Schur route alone gives its signature (1, 1); typed
     Hyperbolic, by the resolved real pair and quartet.
  5. Theorem K and the type on the page's two-dimensional models (cases 1, 2 and 3, t = +-0.5) and on its degenerate
     family and a regular control (t = +-0.1): each count and type as derived.
  6. Unresolved, not forced: (a) a zero pair moved into the cluster's gray zone by a perturbation below L's
     resolution flags the separation, and with it V0's mismatch with its expected two chains and the index, so the
     resolved real pair does not type the point; (b) an eigenvalue of L in its inertia gray zone flags only n(L), and
     the resolved real pair types the point Hyperbolic.
  7. The collision on both sides at ||A|| about 1,700 (UA, UB): phase blocks, Krein-positive oscillators and the
     collision block, mixed, so that nothing else leaves the axis. Typed Elliptic where the pairs are resolved on the
     axis (separations 2e-4 and 4e-5, above the margin); Unresolved where a mixed group is a collision within the margin
     (separation 2e-6, the collision itself, and quartets with real parts 3.16e-7 (UA) and 6e-6 (UB)); Unresolved with
     both members' Krein signatures degenerate at real part 1.2e-5 (UB); Hyperbolic at real parts 3e-5 and 1e-3. The
     unstable side is never typed Elliptic. (n(L), n(D)) = (3, 1) throughout, and K = 2 wherever K is resolved.
  8. n(D) at round-off: a free complex dof and Krein-positive oscillators, mixed. V0 is the semisimple double zero (one
     Schur rank of 0, two chains of length 1), D = 0 on it read as two zeros against ||B||, n(D) = 0, K = n(L) = 0;
     typed Elliptic.
  9. A failed index is not typed (UA): L = diag(0, -100000), omega^2 = 25001, so det = s^2 (s^2 + 4), one phase chain
     with partner energy 1 + 4 omega^2/k = -4e-5, below D's zero cut against ||B|| = 1e5. D's nullity 2 against one
     chain flags n(D), the balance K = 0 against n(L) - n(D) = 1 flags the index, and the point is Unresolved, not
     Elliptic.
 10. A kernel that misses its expectation is not typed (UB): the phase block diag(0, 5) perturbed to diag(-1.5e-7, 5),
     below L's resolution (8.8e-11 ||L||), lifts its zero pair to +-2.5e-4, a real pair outside the gray zone. With
     the expected two chains, V0's single chain is a mismatch, and the point is Unresolved, not Hyperbolic.
Every record() call here passes the original calibration, ln.ORIGINAL (the gray zone a decade on each side, one
margin for every role, the leak at most 1e-8), so these claims run exactly as they were derived. The section 7
recalibration's own claims are in dl_recal.py (UA, 2026-10-16).
Arms: W with the gyroscopic block's sign flipped (the identity fails); Krein signs from -B (claim 3 fails); the margin
at 1e-9, below the root scale (claim 3 fails); the replaced construction, the W-annihilator of the exact eigenvectors,
larger than V0 at claim 4's defect, though equal to it in claim 3; mixed groups typed as resolved (claim 7 fails);
Krein nondegeneracy read against the form's own largest value (claim 7 fails); n(D) read against D's own largest
eigenvalue (claim 8 fails); the balance and nullity checks dropped (claim 9 fails); the check against the expected V0
dropped (claim 10 fails). Reported beside them, unscored: the annihilator from the computed eigenvectors, as
identification_check.py takes them, and claim 7's real part 1.2e-5 with the Schur route also taken where the
eigenvectors span a group but B is degenerate on them (UB's c2 patch, as UB ran it).
"""
import os
import sys
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from instrument import basis, functional as fn, linear as ln, devtools  # noqa: E402

devtools.require('synthetic')
mp.mp.dps = 50
rng = np.random.default_rng(20261018)
out = []
U = np.finfo(float).eps
KAPPAS = [0.5, 1.0, 3.0, 10.0, 100.0, 700.0, 1700.0, -3.0]
POS_KAPPAS = KAPPAS[:-1]
REAL_PAIR = np.diag([-5.0, 3.0])
COLL = np.diag([-1.0, -2.0])
OMEGA3 = 1.3
OMEGA4 = np.sqrt((3 + 2 * np.sqrt(2)) / 4)
W2STAR = (mp.mpf(3) + 2 * mp.sqrt(2)) / 4
TAU = 2 ** 0.25
MIXED = 'a mixed imaginary group'
KREIN = 'the Krein signature of the group'
TWO_CHAINS = dict(dim=4, ranks=[2, 0])           # the two phase chains of the synthetic systems
NO_V0 = dict(dim=0, ranks=[])
ONE_CHAIN = dict(dim=2, ranks=[1, 0])


def say(s):
    print(s)
    out.append(s)


def place(blocks):
    """L on R^{2m} (Re coordinates, then Im), with a 2 x 2 block on (Re c_j, Im c_j) for each complex dof j."""
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


def margin_for(A, j=2, factor=30.0):
    return factor * (U * np.linalg.norm(A, 2)) ** (1.0 / j)


def blocks_for(phase=(5.0, -2.0), extra=()):
    return [np.diag([0.0, k]) for k in phase] + [np.diag([k, k]) for k in KAPPAS] + [REAL_PAIR] + list(extra)


def mixed(blocks, omega, phase=(5.0, -2.0)):
    """A, B, W of the mixed system, its L, and the exact V0 of the phase blocks (the first len(phase) blocks)."""
    m = len(blocks)
    R = random_unitary_real(m)
    L = R.T @ place(blocks) @ R
    A, B, W = ln.first_order(L, omega)
    E = np.eye(2 * m)
    cols = []
    for j, k in enumerate(phase):
        cols.append(np.concatenate([R.T @ E[j], np.zeros(2 * m)]))
        cols.append(np.concatenate([-(2 * omega / k) * (R.T @ E[m + j]), R.T @ E[j]]))
    return A, B, W, L, (np.column_stack(cols) if cols else np.zeros((4 * m, 0))), R


def block_totals(blocks, omega):
    tot = np.zeros(3, dtype=int)
    for b in blocks:
        A, B, W = ln.first_order(b, omega)
        r = ln.record(A, B, W, b, margin_for(A), **ln.ORIGINAL)
        tot += (r['nL'], r['nD'], r['K'])
    return tuple(int(v) for v in tot)


def claim1():
    worst, pair, inv = 0.0, 0.0, np.inf
    for _ in range(3):
        L = rng.normal(size=(12, 12))
        L = L + L.T
        A, B, W = ln.first_order(L, rng.uniform(0.3, 2.0))
        d = ln.symplectic_defects(A, B, W)
        worst = max(worst, d['energy'], d['skew'], d['hamiltonian'])
        inv = min(inv, d['invertible'])
        lam = np.linalg.eigvals(A)
        nA = np.linalg.norm(A, 2)
        for z in lam:
            pair = max(pair, np.abs(lam + np.conj(z)).min() / nA, np.abs(lam - np.conj(z)).min() / nA)
    return worst < 1e-14 and pair < 1e-10 and inv > 1e-3, (worst, pair)


def claim2():
    rows, ok = [], True
    for s in ('R2', 'R4', 'R5'):
        B = basis.Basis(s, 16)
        Fn = fn.Functional(B)
        levels = sorted(set(B.eig))
        lam = (levels[0] + levels[1]) / 2
        omega = np.sqrt(lam)
        L = Fn.hess_dense(np.zeros(B.m, dtype=complex), lam)
        A, Bm, W = ln.first_order(L, omega)
        nA = np.linalg.norm(A, 2)
        r = ln.record(A, Bm, W, L, margin_for(A, 1), expected=NO_V0, **ln.ORIGINAL)
        root = np.sqrt(B.eig)
        pred = np.sort(np.concatenate([root - omega, omega - root, root + omega, -root - omega]))
        ev = np.linalg.eigvals(A)
        err = np.abs(np.sort(ev.imag) - pred).max() / nA
        reals = np.abs(ev.real).max() / nA
        # each imaginary group: matched to its predicted frequencies, Krein-negative iff on a level below lam
        table = [(t, neg) for e in B.eig for t, neg in ((np.sqrt(e) + omega, False), (abs(np.sqrt(e) - omega), e < lam))]
        signs_ok = True
        for c, size, neg, _, status, _ in r['imag_groups']:
            hits = [n for t, n in table if abs(t - c.imag) < 1e-8 * nA]
            signs_ok &= (len(hits) == size and len(set(hits)) == 1 and neg == (size if hits[0] else 0)
                         and status == 'definite')
        below = int(np.sum(B.eig < lam))
        good = (err < 1e-12 and reals < 1e-12 and signs_ok and r['sdim'] == 0 and r['nD'] == 0
                and r['ki'] == below and r['nL'] == 2 * below and r['K'] == r['nL'] and r['balance']
                and not r['unresolved'] and r['type'] == 'Elliptic')
        ok &= good
        rows.append((s, B.m, levels[:2], err, signs_ok, r['ki'], below, r['nL'], r['K'], len(r['imag_groups']), r['type']))
    return ok, rows


def claim3(krein_sign=1.0, margin=None):
    blocks = blocks_for()
    A, B, W, L, V0x, _ = mixed(blocks, OMEGA3)
    mg = margin_for(A) if margin is None else margin
    r = ln.record(A, B, W, L, mg, symmetry=list(V0x.T[::2]), expected=TWO_CHAINS, krein_sign=krein_sign, **ln.ORIGINAL)
    angle = ln.principal_angle(r['V0'], V0x) if r['sdim'] == 4 else np.pi / 2
    tot = block_totals(blocks, OMEGA3)
    good = (r['separated'] and r['sdim'] == 4 and angle < 1e-8 and r['symmetry_leak'] < 1e-8
            and r['jordan_ranks'] == [2, 0] and r['blocks'] == 2 and r['longest_chain'] == 2
            and (r['nL'], r['nD'], r['K']) == (4, 1, 3) and (r['kr'], r['kc'], r['ki']) == (1, 1, 0)
            and tot == (4, 1, 3) and r['balance'] and not r['unresolved'] and r['type'] == 'Hyperbolic')
    return good, r, angle, tot, (A, W, mg, V0x)


def claim4():
    blocks = blocks_for(extra=(COLL,))
    A, B, W, L, V0x, _ = mixed(blocks, OMEGA4)
    mg = margin_for(A)
    r = ln.record(A, B, W, L, mg, symmetry=list(V0x.T[::2]), expected=TWO_CHAINS, **ln.ORIGINAL)
    angle = ln.principal_angle(r['V0'], V0x) if r['sdim'] == 4 else np.pi / 2
    tot = block_totals(blocks, OMEGA4)
    coll = [g for g in r['imag_groups'] if abs(g[0].imag - TAU) < 1e-3]
    lam = np.linalg.eigvals(A)
    pair = lam[np.abs(lam - 1j * TAU) < 1e-3]
    schur_only = ln._krein_schur(A, B, W, pair.mean(), np.abs(pair - pair.mean()).max() + mg / 2, 2, 1.0)
    good = (r['separated'] and r['sdim'] == 4 and angle < 1e-8 and r['symmetry_leak'] < 1e-8
            and (r['nL'], r['nD'], r['K']) == (6, 1, 5) and (r['kr'], r['kc'], r['ki']) == (1, 1, 1)
            and tot == (6, 1, 5) and len(coll) == 1 and coll[0][1] == 2 and coll[0][2] == 1 and coll[0][4] == 'mixed'
            and schur_only == (1, 1, True) and r['balance'] and r['K_resolved']
            and len(r['unresolved']) == 1 and r['unresolved'][0].startswith(MIXED) and r['type'] == 'Hyperbolic')
    return good, r, angle, tot, coll, pair, schur_only, (A, W, mg, V0x)


def two_dim(Bm):
    Om = np.array([[0.0, 1.0], [-1.0, 0.0]])
    return -np.linalg.inv(Om) @ Bm, Bm, Om


def claim5():
    rows, ok, models = [], True, []
    E_, H_ = 'Elliptic', 'Hyperbolic'
    for t in (0.5, -0.5):
        models.append((f'case 1, B = tI, t = {t:+}', two_dim(t * np.eye(2)), t * np.eye(2), (0, 0, 0) if t > 0 else (2, 0, 2), E_,
                       NO_V0))
        for bb in (1.0, -1.0):
            Bm = np.diag([t, bb])
            exp = {(1, 1): ((0, 0, 0), E_), (1, -1): ((1, 0, 1), H_), (-1, 1): ((1, 0, 1), H_),
                   (-1, -1): ((2, 0, 2), E_)}[(int(np.sign(t)), int(bb))]
            models.append((f'case 2, B = diag(t, {bb:+.0f}), t = {t:+}', two_dim(Bm), Bm) + exp + (NO_V0,))
        Bm = np.diag([0.0, t])
        models.append((f'case 3, B = diag(0, t), t = {t:+}', two_dim(Bm), Bm, (0, 0, 0) if t > 0 else (1, 1, 0), E_,
                       ONE_CHAIN))
    J = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    for t in (-0.1, 0.1):
        Lm = np.diag([0.0, t - 4, t])
        models.append((f'the degenerate family, L = diag(0, t - 4, t), t = {t:+}', ln.first_order(Lm, None, G=2 * J), Lm,
                       (2, 0, 2) if t < 0 else (1, 1, 0), H_ if t < 0 else E_, ONE_CHAIN))
        Lm = np.diag([0.0, t - 3, t])
        models.append((f'a regular control, L = diag(0, t - 3, t), t = {t:+}', ln.first_order(Lm, None, G=2 * J), Lm,
                       (2, 1, 1) if t < 0 else (1, 1, 0), H_ if t < 0 else E_, ONE_CHAIN))
    for name, (A, Bm, W), Lm, exp, typ, ev0 in models:
        r = ln.record(A, Bm, W, Lm, max(margin_for(A), 1e-8), expected=ev0, **ln.ORIGINAL)
        got = (r['nL'], r['nD'], r['K'])
        good = (got == exp and r['type'] == typ and r['balance'] and not r['unresolved']
                and ln.symplectic_defects(A, Bm, W)['energy'] < 1e-14)
        ok &= good
        rows.append((name, got, exp, r['type'], typ, good))
    return ok, rows


def claim6():
    # (a) the phase block diag(0, 5) perturbed to diag(-2.1e-9, 5): its zero pair moves to about +-3.0e-5, inside
    # the gray zone, while the perturbation is 1.2e-12 ||L||, below L's resolution 1e-10 ||L||
    blocks = [np.diag([-2.1e-9, 5.0]), np.diag([0.0, -2.0])] + [np.diag([k, k]) for k in KAPPAS] + [REAL_PAIR]
    A, B, W = ln.first_order(place(blocks), OMEGA3)
    ra = ln.record(A, B, W, place(blocks), margin_for(A), expected=TWO_CHAINS, **ln.ORIGINAL)
    moved = np.sort(np.abs(np.linalg.eigvals(A)))[2]
    # (b) a block diag(1.7e-5, 1700): an eigenvalue of L at 1e-8 ||L||, in its gray zone; its pair of A lies near
    # +-4.1e-3 i, outside the cluster's gray zone
    blocks = blocks_for(extra=(np.diag([1.7e-5, 1700.0]),))
    A, B, W = ln.first_order(place(blocks), OMEGA3)
    rb = ln.record(A, B, W, place(blocks), margin_for(A), expected=TWO_CHAINS, **ln.ORIGINAL)
    ua_ = ra['unresolved']
    ok = (len(ua_) == 3 and ua_[0] == 'the zero cluster is not separated: an eigenvalue lies in (margin/10, 10 margin)'
          and ua_[1].startswith('V0 does not match its expectation') and ua_[2].startswith('the index does not balance')
          and rb['unresolved'] == ['n(L): an eigenvalue of L lies in its gray zone'] and rb['separated']
          and ra['type'] == 'Unresolved' and rb['type'] == 'Hyperbolic')
    return ok, (ra['unresolved'], ra['margin'], moved, rb['unresolved'], ra['type'], rb['type'])


def collision_exact(w2):
    """The collision block's two eigenvalues with positive imaginary part, at 50 digits: (their separation along the
    axis, their largest |Re|)."""
    b = 4 * w2 - 3
    disc = mp.sqrt(mp.mpc(b * b - 8))
    s = [mp.sqrt((-b + sg * disc) / 2) for sg in (1, -1)]
    s = [z if mp.im(z) > 0 else -z for z in s]
    return float(abs(mp.im(s[0]) - mp.im(s[1]))), float(max(abs(mp.re(z)) for z in s))


CASES = [
    ('stable, separation 2e-4', mp.mpf('1e-8'), 'Elliptic', 'two definite'),
    ('stable, separation 4e-5', mp.mpf('4e-10'), 'Elliptic', 'two definite'),
    ('stable, separation 2e-6', mp.mpf('1e-12'), 'Unresolved', 'one mixed'),
    ('the collision', mp.mpf(0), 'Unresolved', 'one mixed'),
    ('unstable, real part 3.16e-7 (UA)', -mp.mpf('1e-13'), 'Unresolved', 'one mixed'),
    ('unstable, real part 6e-6 (UB)', -mp.mpf('6e-6') ** 2, 'Unresolved', 'one mixed'),
    ('unstable, real part 1.2e-5 (UB)', -mp.mpf('1.2e-5') ** 2, 'Unresolved', 'two degenerate'),
    ('unstable, real part 3e-5', -mp.mpf('3e-5') ** 2, 'Hyperbolic', 'none'),
    ('unstable, real part 1e-3', -mp.mpf('1e-3') ** 2, 'Hyperbolic', 'none'),
]


def collision_case(delta, arm=None):
    w2 = W2STAR + delta
    omega = float(mp.sqrt(w2))
    blocks = [np.diag([0.0, k]) for k in (5.0, -2.0)] + [np.diag([k, k]) for k in POS_KAPPAS] + [COLL]
    A, B, W, L, V0x, _ = mixed(blocks, omega)
    r = ln.record(A, B, W, L, margin_for(A), symmetry=list(V0x.T[::2]), expected=TWO_CHAINS, arm=arm, **ln.ORIGINAL)
    angle = ln.principal_angle(r['V0'], V0x) if r['sdim'] == 4 else np.pi / 2
    coll = [g for g in r['imag_groups'] if abs(g[0].imag - TAU) < 1e-3]
    return r, angle, coll, collision_exact(w2)


def case_ok(r, angle, coll, typ, pattern):
    base = (r['separated'] and r['sdim'] == 4 and angle < 1e-8 and (r['nL'], r['nD']) == (3, 1) and r['type'] == typ)
    if pattern == 'two definite':
        return (base and len(coll) == 2 and all(g[1] == 1 and g[4] == 'definite' for g in coll)
                and sorted(g[2] for g in coll) == [0, 1] and not r['unresolved'] and r['K'] == 2 and r['balance'])
    if pattern == 'one mixed':
        return (base and len(coll) == 1 and coll[0][1] == 2 and coll[0][2] == 1 and coll[0][4] == 'mixed'
                and len(r['unresolved']) == 1 and r['unresolved'][0].startswith(MIXED) and r['K_resolved']
                and r['K'] == 2 and r['balance'])
    if pattern == 'two degenerate':
        krein = [u for u in r['unresolved'] if u.startswith(KREIN)]
        rest = [u for u in r['unresolved'] if not u.startswith(KREIN)]
        return (base and len(coll) == 2 and all(g[1] == 1 and g[4] == 'degenerate' for g in coll)
                and len(krein) == 2 and all(u.startswith('the index does not balance') for u in rest)
                and not r['K_resolved'])
    return (base and not coll and (r['kc'], r['ki']) == (1, 0) and not r['unresolved'] and r['K'] == 2
            and r['balance'])


def claim7(arm=None):
    ok, rows, unstable_elliptic = True, [], []
    for label, delta, typ, pattern in CASES:
        r, angle, coll, (sep, re) = collision_case(delta, arm)
        good = case_ok(r, angle, coll, typ, pattern)
        ok &= good
        if delta < 0 and r['type'] == 'Elliptic':
            unstable_elliptic.append(label)
        rows.append((label, sep, re, r['margin'], r['type'], [(g[1], g[2], g[3], g[4], g[5]) for g in coll], r['kc'],
                     r['K'] if r['K_resolved'] else None, len(r['unresolved']), good))
    return ok and not unstable_elliptic, rows, unstable_elliptic


def claim8(arm=None):
    blocks = [np.diag([0.0, 0.0])] + [np.diag([k, k]) for k in POS_KAPPAS]
    A, B, W, L, _, R = mixed(blocks, OMEGA3, phase=())
    m = len(blocks)
    E = np.eye(2 * m)
    kern = [np.concatenate([R.T @ E[0], np.zeros(2 * m)]), np.concatenate([R.T @ E[m], np.zeros(2 * m)])]
    r = ln.record(A, B, W, L, margin_for(A), symmetry=kern, expected=dict(dim=2, ranks=[0]), arm=arm, **ln.ORIGINAL)
    good = (r['separated'] and r['sdim'] == 2 and r['symmetry_leak'] < 1e-8 and r['jordan_ranks'] == [0]
            and r['blocks'] == 2 and r['longest_chain'] == 1 and (r['nL'], r['dimkerL']) == (0, 2)
            and (r['nD'], r['dimkerD']) == (0, 2) and r['K'] == 0 and r['balance'] and not r['unresolved']
            and r['type'] == 'Elliptic')
    return good, r



def claim9(arm=None):
    L = np.diag([0.0, -100000.0])
    A, B, W = ln.first_order(L, np.sqrt(25001.0))
    r = ln.record(A, B, W, L, margin_for(A), symmetry=[np.array([1.0, 0.0, 0.0, 0.0])], expected=ONE_CHAIN, arm=arm, **ln.ORIGINAL)
    D = r['V0'].T @ B @ r['V0']
    dev = np.linalg.eigvalsh((D + D.T) / 2)
    u = r['unresolved']
    good = (r['nL'] == 1 and r['v0_matches'] and r['blocks'] == 1 and r['dimkerD'] == 2 and r['K'] == 0
            and not r['balance'] and len(u) == 2 and u[0].startswith("n(D): D's nullity 2")
            and u[1].startswith('the index does not balance') and r['type'] == 'Unresolved')
    return good, r, dev


def claim10(arm=None):
    blocks = [np.diag([-1.5e-7, 5.0]), np.diag([0.0, -2.0])] + [np.diag([k, k]) for k in POS_KAPPAS]
    A, B, W, L, _, _ = mixed(blocks, OMEGA3)
    r = ln.record(A, B, W, L, margin_for(A), expected=TWO_CHAINS, arm=arm, **ln.ORIGINAL)
    lam = np.linalg.eigvals(A)
    lifted = float(np.sort(np.abs(lam[np.abs(lam.imag) < 1e-12]))[-1]) if np.any(np.abs(lam.imag) < 1e-12) else 0.0
    good = (r['sdim'] == 2 and not r['v0_matches'] and r['kr'] == 1 and lifted > 10 * r['margin']
            and any(x.startswith('V0 does not match its expectation') for x in r['unresolved'])
            and r['type'] == 'Unresolved')
    return good, r, lifted


def main():
    failed, arms = 0, []
    ok, w = claim1()
    say(f"1. the first-order form: {'PASS' if ok else 'FAIL'}  identities {w[0]:.1e}, spectral pairing {w[1]:.1e}")
    failed += not ok
    ok, rows = claim2()
    say(f"2. the free operator at c = 0 (UB): {'PASS' if ok else 'FAIL'}")
    for s, m, lv, err, sg, ki, below, nL, K, ng, typ in rows:
        say(f"   {s}, N = 16, m = {m}, lam between {lv[0]:.0f} and {lv[1]:.0f}: eigenvalues against +-i(sqrt e -+ omega) {err:.1e};"
            f" {ng} imaginary groups, each definite, its Krein sign as predicted: {sg}; Krein-negative {ki} = the dofs below lam"
            f" ({below}); n(L) {nL}, K {K}, V0 = 0; {typ}")
    failed += not ok
    ok3, r3, ang3, tot3, (A3, W3, mg3, V0x3) = claim3()
    ex3 = ln.eigvec_annihilator(A3, W3, mg3)
    eg3 = ln.eigvec_annihilator(A3, W3, mg3, vectors='eig')
    say(f"3. zero chains at ||A|| = {r3['normA']:.0f}: {'PASS' if ok3 else 'FAIL'}  margin {r3['margin']:.1e} (root scale {np.sqrt(U * r3['normA']):.1e});"
        f" cluster max {r3['cluster_max']:.1e}, nearest outside {r3['outside_min']:.1e}; V0 dim {r3['sdim']}, angle to the exact V0 {ang3:.1e};"
        f" Schur ranks {r3['jordan_ranks']}, {r3['blocks']} chains, longest {r3['longest_chain']};"
        f" (n(L), n(D), K) = ({r3['nL']}, {r3['nD']}, {r3['K']}), (k_r, k_c, k_i) = ({r3['kr']}, {r3['kc']}, {r3['ki']});"
        f" the blocks one by one {tot3}; {r3['type']}")
    failed += not ok3
    ok4, r4, ang4, tot4, coll, pair, schur_only, (A4, W4, mg4, V0x4) = claim4()
    ex4 = ln.eigvec_annihilator(A4, W4, mg4)
    eg4 = ln.eigvec_annihilator(A4, W4, mg4, vectors='eig')
    say(f"4. a defective nonzero eigenvalue (a Krein collision): {'PASS' if ok4 else 'FAIL'}  the pair at i 2^(1/4) split by"
        f" {np.abs(pair[0] - pair[1]):.1e}, one group of {coll[0][1] if coll else 0}, {coll[0][4] if coll else '?'}, with"
        f" {coll[0][2] if coll else '?'} negative direction ({coll[0][3] if coll else '?'} route; the Schur route alone {schur_only});"
        f" V0 dim {r4['sdim']}, angle to the exact V0 {ang4:.1e}; (n(L), n(D), K) = ({r4['nL']}, {r4['nD']}, {r4['K']}),"
        f" (k_r, k_c, k_i) = ({r4['kr']}, {r4['kc']}, {r4['ki']}); the blocks one by one {tot4}; {r4['type']}, unresolved {r4['unresolved']}")
    failed += not ok4
    ok, rows = claim5()
    say(f"5. Theorem K and the type on the page's models: {'PASS' if ok else 'FAIL'}")
    for name, got, exp, typ, etyp, good in rows:
        say(f"   {name}: (n(L), n(D), K) = {got}, derived {exp}; {typ}, derived {etyp}  {'ok' if good else 'MISMATCH'}")
    failed += not ok
    ok, (ua, mga, moved, ub, ta, tb) = claim6()
    say(f"6. unresolved, not forced: {'PASS' if ok else 'FAIL'}  (a) a pair at {moved:.1e} against the margin {mga:.1e}: {ua}, {ta};"
        f" (b) {ub}, {tb}")
    failed += not ok
    ok7, rows7, ue7 = claim7()
    say(f"7. the collision on both sides at ||A|| about 1,700 (UA, UB): {'PASS' if ok7 else 'FAIL'}"
        f"  (n(L), n(D)) = (3, 1) throughout; the unstable side typed Elliptic: {ue7 or 'never'}")
    for label, sep, re, mg, typ, cg, kc, K, nu, good in rows7:
        say(f"   {label}: exact separation {sep:.2e}, exact |Re| {re:.2e}, margin {mg:.1e}; {typ}; collision groups"
            f" (size, negative, route, status, largest |Re|) {[(a, b, c, d, f'{e:.1e}') for a, b, c, d, e in cg]}; k_c {kc};"
            f" K {K if K is not None else 'unresolved'}; {nu} unresolved  {'ok' if good else 'MISMATCH'}")
    failed += not ok7
    ok8, r8 = claim8()
    say(f"8. n(D) at round-off: {'PASS' if ok8 else 'FAIL'}  V0 dim {r8['sdim']}, kernel leak {r8['symmetry_leak']:.1e}, Schur ranks"
        f" {r8['jordan_ranks']}, {r8['blocks']} chains of length {r8['longest_chain']}; n(L) {r8['nL']} with {r8['dimkerL']} zeros;"
        f" n(D) {r8['nD']} with {r8['dimkerD']} zeros against ||B||; K {r8['K']}; {r8['type']}")
    failed += not ok8
    ok9, r9, dev9 = claim9()
    say(f"9. a failed index is not typed (UA): {'PASS' if ok9 else 'FAIL'}  D's eigenvalues {[f'{x:+.3e}' for x in dev9]} against"
        f" ||B|| = 1e5; {r9['blocks']} chain, D's nullity {r9['dimkerD']}; n(L) {r9['nL']}, n(D) {r9['nD']}, K {r9['K']};"
        f" {r9['type']}, unresolved {r9['unresolved']}")
    failed += not ok9
    ok10, r10, lifted10 = claim10()
    say(f"10. a kernel that misses its expectation is not typed (UB): {'PASS' if ok10 else 'FAIL'}  the lifted real pair at"
        f" {lifted10:.2e}, ten margins {10 * r10['margin']:.2e}; V0 dim {r10['sdim']} against 4; k_r {r10['kr']}; {r10['type']},"
        f" unresolved {r10['unresolved']}")
    failed += not ok10
    # arms
    L = rng.normal(size=(8, 8))
    L = L + L.T
    A, B, W = ln.first_order(L, 0.9)
    Wbad = W.copy()
    Wbad[:8, :8] = -Wbad[:8, :8]                       # the whole gyroscopic block G, n = 8
    arms.append(("W's gyroscopic block with its sign flipped: the identity", ln.symplectic_defects(A, B, Wbad)['energy'] > 1e-6))
    arms.append(('Krein signs from -B: claim 3', not claim3(krein_sign=-1.0)[0]))
    arms.append(('the margin at 1e-9, below the root scale: claim 3', not claim3(margin=1e-9)[0]))
    arms.append(("the replaced construction at claim 4's defect: larger than V0", ex4.shape[1] > r4['sdim'] and ex3.shape[1] == r3['sdim']))
    ok_m, rows_m, ue_m = claim7(arm='mixed_resolved')
    arms.append(('mixed groups typed as resolved: claim 7', not ok_m))
    ok_k, rows_k, ue_k = claim7(arm='krein_own_scale')
    arms.append(("Krein nondegeneracy against the form's own largest value: claim 7", not ok_k))
    ok_d, r_d = claim8(arm='d_own_scale')
    arms.append(("n(D) against D's own largest eigenvalue: claim 8", not ok_d))
    ok_i, r_i, _ = claim9(arm='index_unguarded')
    arms.append(('the balance and nullity checks dropped: claim 9', not ok_i))
    ok_v, r_v, _ = claim10(arm='v0_unchecked')
    arms.append(('the check against the expected V0 dropped: claim 10', not ok_v))
    say('arms')
    for label, red in arms:
        say(f"   arm: {label:68s} {'RED' if red else 'green (FAIL)'}")
    failed += sum(not r for _, r in arms)
    say(f"   under the mixed-resolved arm, the unstable side typed Elliptic at: {ue_m or 'none'}")
    say(f"   under the own-scale Krein arm, the unstable side typed Elliptic at: {ue_k or 'none'}")
    say(f"   under the own-scale n(D) arm: n(D) {r_d['nD']} with {r_d['dimkerD']} zeros, balance {r_d['balance']}")
    say(f"   under the unguarded-index arm, claim 9's model: {r_i['type']}, unresolved {r_i['unresolved']}")
    say(f"   under the unchecked-V0 arm, claim 10's point: {r_v['type']}, unresolved {r_v['unresolved']}")
    a3 = ln.principal_angle(eg3, V0x3) if eg3.shape[1] == 4 else None
    a4 = ln.principal_angle(eg4, V0x4) if eg4.shape[1] == 4 else None
    say(f"   the exact-eigenvector annihilator: dimension {ex3.shape[1]} in claim 3, {ex4.shape[1]} at claim 4's defect (V0: 4)")
    say(f"   unscored, from the computed eigenvectors (identification_check.py's way): dimension {eg3.shape[1]} in claim 3"
        f"{'' if a3 is None else f', angle to V0 {a3:.1e}'}; {eg4.shape[1]} at the defect{'' if a4 is None else f', angle to V0 {a4:.1e}'}")
    r_u, _, coll_u, _ = collision_case(CASES[6][1], arm='schur_on_degenerate')
    say(f"   unscored, claim 7's real part 1.2e-5 with the Schur route also on degenerate spanning sets (UB's c2 patch as run):"
        f" {[(g[3], g[4]) for g in coll_u]}; {r_u['type']}; unresolved {r_u['unresolved']}")
    say(f"{failed} failed (claims and arms)")
    path = os.path.join(HERE, 'dl_linear.out')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     [f'DL, the linear record: PASS, 10 claims, 9 arms red.' if not failed else
                      f'DL, the linear record: FAIL, {failed} failures (claims and arms); see the output.',
                      'Tolerances: fixed before the run (1e-14 for the identities; 1e-10 and 1e-12 relative to ||A|| for the'
                      ' pairing and the free spectrum, 1e-8 ||A|| to match a group to its frequency; 1e-8 for the angle to the'
                      ' exact V0 and the kernel leak; the margin 30 (u ||A||)^(1/j), j = 2 with chains and 1 without, its gray zone'
                      ' a decade on each side, and the same margin for linking groups and typing their centres; Hyperbolic only'
                      ' from a group off the axis by more than the margin and outside the cluster gray zone; inertia gray zones'
                      ' 1e-10 to 1e-7 for L against ||L|| and 1e-8 to 1e-5 for D against ||B||; the nullity of D against the number of'
                      ' chains; V0 against its expected dimension and ranks, with the symmetry leak at most 1e-8; the rank floor 1e2 u ||A||; the'
                      ' eigenvector rank cut 1e-6; Krein nondegeneracy above 1e-8 |lambda| ||W|| in both routes; the round-off'
                      ' cut 1e-12 ||A|| for exact eigenvectors and 1e-10 for the annihilator null space). The run informed'
                      ' none.'], outputs=(path,))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
