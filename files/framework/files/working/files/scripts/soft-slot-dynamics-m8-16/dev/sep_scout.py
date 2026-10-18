#!/usr/bin/env python3
"""The separation scout: synthetic ladders in N for DESIGN.md section 10.2's separation rule, under today's record (the
section 7 calibration and L's cut). Case: synthetic. Reported, unscored: it informs SEPARATION_PLAN.md. The rule itself is
not implemented here and no verdict of it is read from a record; its expected verdicts are derived from each family's
exact eigenvalues, which this script prints beside the records' readings.

A ladder is four cutoffs, N = 16, 24, 32 and 40 (j = 0 to 3), with one parameter p_j converging as j grows, and its limit
j -> infinity. Each family is dl_recal.py's Elliptic family (the phase chains diag(0, 5) and diag(0, -2), Krein-positive
oscillators up to 1,700) with one block added, mixed by one random unitary for the whole ladder, at m = 0.2:
  P, a converged control: S1+ diag(k, k) at s_j = 1e-3 (1 + 1e-3 4^-j), Elliptic in the limit;
  P', a converged control: S1r diag(-k1, 1.66 k1), its real pair at s_j = 1e-3 (1 + 1e-3 4^-j), Hyperbolic;
  PK, a converged control near a Krein collision: UB's block diag(-a, -2a) at omega^2 = omega*^2 + delta_j, its two
      imaginary pairs of opposite Krein sign separated by 9e-3 (1 + 0.1 4^-j), Elliptic;
  Z, through zero: a soft-soft block diag(k1_j, 4e-4) whose slow root lambda^2 = -sigma_j, sigma_j = sigma_inf + c 4^-j,
      from an imaginary pair at 1e-5 (j = 3) to a real pair at 3e-6 in the limit (sigma_inf < 0): Elliptic at every
      cutoff, Hyperbolic in the limit;
  K, a Krein collision: UB's block at delta_j = delta_inf + c 4^-j, separation 1e-3 at j = 3, a quartet with real part
      1e-3 in the limit: Elliptic at every cutoff, Hyperbolic in the limit;
  X, the axis: the same block from a quartet with real part 1e-3 at j = 3 to two imaginary pairs separated by 1e-3 in
      the limit: Hyperbolic at every cutoff, Elliptic in the limit;
  R, a slow rate: the same block with its separation stepped geometrically, sep_j = S_inf + c 0.95^j, 1e-3 at j = 3,
      S_inf = -5e-4, so a quartet with real part 2.5e-4 in the limit: Elliptic at every cutoff, Hyperbolic in the limit;
  F, two rates: the soft-soft block with sigma_j = sigma_inf + a 4^-j + b 0.999^j, its pair at 5 margins at j = 3, the
      last change mostly the fast part (0.03 margins), and a slow part that carries it through zero to a real pair at 4
      margins in the limit: Elliptic at every cutoff, Hyperbolic in the limit.
For each family the scout prints, from the exact roots: the tracked eigenvalue of the binding pair at each cutoff and in
the limit; its last two changes d1 and d2; the geometric remaining error d2^2 / (d1 - d2) where d2 < d1 (else
non-contracting); the margin floor; its distance at j = 3 to the nearest type-changing event (the top of A's gray zone,
the imaginary axis, or the nearest imaginary eigenvalue of opposite Krein sign); and the ratio of that distance to the
uncertainty, max(geometric, floor). Then, over 3 mixings, the record's type at each cutoff, against the limit's.
"""
import os
import sys
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from instrument import linear as ln, devtools  # noqa: E402
import dl_recal as d  # noqa: E402

devtools.require('synthetic')
d.rng = np.random.default_rng(20261024)
mp.mp.dps = 50
OMEGA, M, N_MIX = 7.0, 0.2, 3
NS = (16, 24, 32, 40)
A_C = mp.mpf(d.A_COLL)
W2S = (3 + 2 * mp.sqrt(2)) * A_C / 4
out = []


def say(s=''):
    print(s, flush=True)
    out.append(s)


def coll_roots(delta):
    """The collision block's two roots in the upper half plane at omega^2 = omega*^2 + delta (50 digits)."""
    b = 4 * (W2S + delta) - 3 * A_C
    disc = mp.sqrt(b * b - 8 * A_C * A_C)
    z = [mp.sqrt((-b + sg * disc) / 2) for sg in (1, -1)]
    return sorted((t if mp.im(t) > 0 else -t for t in z), key=lambda t: (mp.re(t), mp.im(t)))


def coll_sep(delta):
    z = coll_roots(delta)
    return abs(mp.im(z[0]) - mp.im(z[1]))


def coll_re(delta):
    return max(abs(mp.re(t)) for t in coll_roots(delta))


def bisect(f, lo, hi):
    for _ in range(200):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == (f(hi) > 0):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def delta_for_sep(sep):
    return bisect(lambda x: coll_sep(x) - sep, mp.mpf('1e-14'), mp.mpf(10))


def delta_for_re(re_):
    return -bisect(lambda x: coll_re(-x) - re_, mp.mpf('1e-14'), mp.mpf(10))


def soft_block(x, k2):
    """diag(k1, k2) at OMEGA with its slow root lambda^2 = x exactly."""
    k1 = -(x * x + (4 * OMEGA ** 2 + k2) * x) / (x + k2)
    return np.diag([float(k1), float(k2)])


def s1r_block(s, r):
    x = s * s
    k = ((r - 1) * x + np.sqrt((r - 1) ** 2 * x * x + 4 * r * (x * x + 4 * OMEGA ** 2 * x))) / (2 * r)
    return np.diag([-k, r * k])


def exact_margin(blocks, omega):
    """The record's margin at m = 0.2 from the unmixed system's ||A||, which the mixing does not move."""
    return ln.margin(np.linalg.norm(ln.first_order(d.place(blocks), omega)[0], 2), M)


MG = exact_margin(d.elliptic_blocks([np.diag([1e-3, 1e-3])]), OMEGA)


def family(name):
    """dict: the system (blocks, omega) at j = 0..3 and in the limit; the binding pair's exact eigenvalue at each (the
    upper root, or the first-quadrant one); its kind; the type at the cutoffs and in the limit; the collision's deltas."""
    J = [0, 1, 2, 3]
    if name in ('P', "P'"):
        s = [1e-3 * (1 + 1e-3 * 4.0 ** -j) for j in J] + [1e-3]
        if name == 'P':
            sysm = [(d.elliptic_blocks([np.diag([v * v + 2 * OMEGA * v] * 2)]), OMEGA) for v in s]
            return dict(sys=sysm, lam=[mp.mpc(0, v) for v in s], kind='imaginary, Krein +', fin='Elliptic', lim='Elliptic')
        sysm = [(d.elliptic_blocks([s1r_block(v, 1.66)]), OMEGA) for v in s]
        return dict(sys=sysm, lam=[mp.mpf(v) for v in s], kind='real', fin='Hyperbolic', lim='Hyperbolic')
    if name in ('Z', 'F'):
        if name == 'Z':
            s3, s_inf, k2 = mp.mpf('1e-5'), mp.mpf('3e-6'), mp.mpf('4e-4')
            sig_inf = -s_inf ** 2
            c = (s3 ** 2 - sig_inf) * 4 ** 3
            sig = [sig_inf + c * mp.mpf(4) ** -j for j in J] + [sig_inf]
        else:
            m_ = mp.mpf(MG)
            s3, s_inf = 5 * m_, 4 * m_
            k2 = 2 * OMEGA * s3
            sig_inf = -s_inf ** 2
            r1, r2 = mp.mpf(1) / 4, mp.mpf('0.999')
            a = 2 * s3 * mp.mpf('0.03') * m_ / (r1 ** 2 * (1 - r1))       # the fast part's last change, in sigma
            b = (s3 ** 2 - sig_inf - a * r1 ** 3) / r2 ** 3
            sig = [sig_inf + a * r1 ** j + b * r2 ** j for j in J] + [sig_inf]
        sysm = [(d.elliptic_blocks([soft_block(-x, k2)]), OMEGA) for x in sig]
        lam = [mp.mpc(0, mp.sqrt(x)) if x > 0 else mp.sqrt(-x) for x in sig]
        return dict(sys=sysm, lam=lam, kind='imaginary, Krein +', fin='Elliptic', lim='Hyperbolic')
    if name == 'PK':
        seps = [mp.mpf('9e-3') * (1 + mp.mpf('0.1') * mp.mpf(4) ** -j) for j in J] + [mp.mpf('9e-3')]
        dl = [delta_for_sep(x) for x in seps]
    elif name == 'R':
        s3, s_inf, rho = mp.mpf('1e-3'), mp.mpf('-5e-4'), mp.mpf('0.95')
        c = (s3 - s_inf) / rho ** 3
        dl = [delta_for_sep(s_inf + c * rho ** j) for j in J] + [delta_for_re(-s_inf / 2)]
    else:
        dk, dx = delta_for_sep(mp.mpf('1e-3')), delta_for_re(mp.mpf('1e-3'))
        d_inf, d3 = (dx, dk) if name == 'K' else (dk, dx)
        c = (d3 - d_inf) * 4 ** 3
        dl = [d_inf + c * mp.mpf(4) ** -j for j in J] + [d_inf]
    sysm = [(d.elliptic_blocks([np.diag([-float(A_C), -2 * float(A_C)])]), float(mp.sqrt(W2S + x))) for x in dl]
    fin, lim = ('Hyperbolic', 'Elliptic') if name == 'X' else ('Elliptic', 'Elliptic' if name == 'PK' else 'Hyperbolic')
    kind = 'a quartet' if name == 'X' else 'imaginary, opposite Krein signs'
    return dict(sys=sysm, lam=[coll_roots(x)[-1] for x in dl], kind=kind, fin=fin, lim=lim, dl=dl)


def distance(name, f, mg):
    """The binding pair's distance at j = 3 to its nearest type-changing event, and the event."""
    lam3 = f['lam'][3]
    gray = abs(lam3) - ln.GRAY * mg
    if name in ('P', 'Z', 'F', "P'"):
        return gray, "A's gray zone"
    if name == 'X':
        return min(gray, coll_re(f['dl'][3])), 'the imaginary axis'
    return min(gray, coll_sep(f['dl'][3])), 'the opposite Krein sign'


def main():
    say(f"The separation scout (reported, unscored): ladders N = {NS}, m = {M}; the rule's expected verdicts derived from"
        " exact roots: separated where the distance is at least ten times max(geometric, floor).")
    for name in ('P', "P'", 'PK', 'Z', 'K', 'X', 'R', 'F'):
        f = family(name)
        lam = f['lam']
        mg = max(exact_margin(*f['sys'][j]) for j in (2, 3))
        d1, d2 = abs(lam[2] - lam[1]), abs(lam[3] - lam[2])
        geo = d2 * d2 / (d1 - d2) if d2 < d1 else mp.inf
        dist, event = distance(name, f, mg)
        ratio = dist / max(geo, mp.mpf(mg))
        say(f"{name:3s} ({f['kind']}): the pair at j = 0..3 {[mp.nstr(z, 6) for z in lam[:4]]}, limit {mp.nstr(lam[4], 6)}")
        say(f"     d1 {mp.nstr(d1, 3)}, d2 {mp.nstr(d2, 3)}, geometric {mp.nstr(geo, 3)}, floor {mg:.2e}; distance to {event}"
            f" {mp.nstr(dist, 3)}; ratio {mp.nstr(ratio, 3)}: {'separated' if ratio >= 10 else 'NOT separated'}; the type at"
            f" the cutoffs {f['fin']}, in the limit {f['lim']}")
        reads = []
        m_ = len(f['sys'][0][0])
        for _ in range(N_MIX):
            R = d.random_unitary_real(m_)
            row = []
            for j in range(4):
                bl, w = f['sys'][j]
                L = R.T @ d.place(bl) @ R
                A, B, W = ln.first_order(L, w)
                E = np.eye(2 * m_)
                sym = [np.concatenate([R.T @ E[i], np.zeros(2 * m_)]) for i in range(2)]
                r = ln.record(A, B, W, L, ln.margin(np.linalg.norm(A, 2), M), symmetry=sym, expected=d.TWO_CHAINS)
                row.append(r['type'] + ('' if not r['unresolved'] else ' ' + str(sorted({u.split(':')[0] for u in r['unresolved']}))))
            reads.append(row)
        same = sum(all(x == f['fin'] for x in row) for row in reads)
        say(f"     records, {N_MIX} mixings: {f['fin']} at all four cutoffs in {same}" + ('' if same == N_MIX else
            '; ' + '; '.join(' | '.join(row) for row in reads)))
    path = os.path.join(HERE, 'sep_scout.out')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    devtools.log_run(os.path.abspath(__file__), 'synthetic',
                     ['The separation scout: reported, unscored; it informs SEPARATION_PLAN.md. The rule is not implemented'
                      ' here; its expected verdicts are derived from exact roots.'], outputs=(path,))


if __name__ == '__main__':
    main()
