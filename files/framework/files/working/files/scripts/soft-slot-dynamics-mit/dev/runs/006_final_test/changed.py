"""MIT's two changes to how a point is read, and nothing else. Neither touches a solve, and neither was chosen blind: both
were chosen knowing M8.18's gate failure, its 24 control readings and M8.17's stored readings at the twelve (DESIGN.md).

A, in instrument/convergence.py, the arm 'same_resolution': a set's members are compared at the top cutoff's linking
distance at every cutoff. linear.group links two values within tau = max(margin, 10 sqrt(u ||A|| |lam|)), and ||A|| grows
about as N^2, so at N = 40 alone tau passed P5's stable pair at 0.25.

B, here: n(D)'s gray zone is (1e-8, 1e-7) ||B||, a factor D_GRAY = 10 above its cut, as L's is (linear.G_L), in place of
the inherited factor 1e3. ||B|| grows the same way, so at N = 40 alone the old top, 1e-5 ||B||, passed D's eigenvalue at
C3R/R4 at 0.25. The cut stays, so n(D) and D's nullity cannot move: B moves only the flag that says an eigenvalue of D
lies in the zone. ||B|| stays the scale, since D can be exactly 0 (UB's c2).

capture() reads B's flag at the record's own call, with D's and L's eigenvalues near zero beside it, so instrument/linear.py
stays M8.18's byte for byte and the as-built record comes out unchanged. reading() is checks.reading on the changed
summaries under the arm, so each point can give both verdicts, and where they agree the point rests on no changed code.
"""
import contextlib
import copy
import numpy as np

from instrument import convergence as cv, linear as ln
import checks as ck

D_GRAY = 10.0                  # n(D)'s gray zone's factor, as linear.G_L is L's; the record's call uses inertia's 1e3
ND_LINE = 'n(D): an eigenvalue of D lies in its gray zone'
L_NEAR = 24                    # how many of L's eigenvalues nearest zero a read keeps


@contextlib.contextmanager
def capture():
    """While a point is read: linear.inertia's call for n(D), the only one with a scale, also gives B's flag and D's
    eigenvalues, and checks.spectrum_of_L also gives L's eigenvalues nearest zero. Neither changes what the record
    computes. Yields the dict they are written to."""
    held = {}
    inertia, spectrum = ln.inertia, ck.spectrum_of_L

    def inertia_(M, zero_rel=1e-10, gray=1e3, scale=None):
        if scale is not None:
            held['b_resolved'] = bool(inertia(M, zero_rel, gray=D_GRAY, scale=scale)[2])
            held['d_eigs'] = [float(x) for x in np.linalg.eigvalsh((M + M.T) / 2)]
        return inertia(M, zero_rel, gray=gray, scale=scale)

    def spectrum_(L):
        mu = spectrum(L)
        held['l_near'] = [float(x) for x in mu[np.argsort(np.abs(mu))[:L_NEAR]]]
        return mu

    ln.inertia, ck.spectrum_of_L = inertia_, spectrum_
    try:
        yield held
    finally:
        ln.inertia, ck.spectrum_of_L = inertia, spectrum


def lifted(summary, b_resolved):
    """One cutoff's summary under B: n(D)'s line goes where B's flag clears it. A record that holds no other unresolved
    item and read Unresolved only for it is Elliptic, as linear.record types it, since its off-axis count is zero."""
    if ND_LINE not in summary['unresolved'] or not b_resolved:
        return summary
    s = copy.copy(summary)
    s['unresolved'] = [u for u in summary['unresolved'] if u != ND_LINE]
    if s['type'] == 'Unresolved' and not s['unresolved']:
        s['type'] = 'Elliptic'
    return s


def reading(sums, flags, eig_hi, lam_hi, margin_hi, n_lo):
    """checks.reading under A and B: sums, lowest cutoff first, with each cutoff's B flag."""
    band = cv.band_edge(eig_hi, n_lo, lam_hi)
    if not band / 2 > ln.GRAY * margin_hi:
        return dict(verdict='Unresolved', type=None, reasons=['the band edge lies within the gray zone (UA)'],
                    rows=[], band=float(band), rel_change_max=None, rel_change_ok=None)
    res = cv.separation([lifted(s, f) for s, f in zip(sums, flags)], band=band, arms=('same_resolution',))
    rel = [r['rel_change'] for r in res['rows'] if r.get('role') == 'tested' and 'rel_change' in r]
    return dict(verdict=res['verdict'], type=res['type'], reasons=list(res['reasons']), rows=res['rows'],
                band=float(band), rel_change_max=float(max(rel)) if rel else None,
                rel_change_ok=bool(rel) and max(rel) <= ck.FRACTION)
