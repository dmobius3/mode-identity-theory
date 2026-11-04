"""MIT's two changes to how a point is read, and nothing else. Neither touches a solve, and neither was chosen blind: both
were chosen knowing M8.18's gate failure, its 24 control readings and M8.17's stored readings at the twelve (DESIGN.md).

A, in instrument/convergence.py, the arm 'own_eigenvalues': a set is read by its eigenvalues, not by its groups' centres.
linear.group links two values within tau = max(margin, 10 sqrt(u ||A|| |lam|)), and ||A|| grows about as N^2, so at
N = 40 alone tau passed P5's stable pair at 0.25, and the rule read the link as motion. capture() keeps each linked
group's members at the record's own call, and with_members() hands them to the rule.

B, here: n(D)'s gray zone is (1e-8, 1e-7) ||B||, a factor D_GRAY = 10 above its cut, as L's is (linear.G_L), in place of
the inherited factor 1e3. ||B|| grows the same way, so at N = 40 alone the old top, 1e-5 ||B||, passed D's eigenvalue at
C3R/R4 at 0.25. The cut stays, so n(D) and D's nullity cannot move: B moves only the flag that says an eigenvalue of D
lies in the zone. ||B|| stays the scale, since D can be exactly 0 (UB's c2).

capture() reads B's flag at the record's own call, with D's and L's eigenvalues near zero and the linked groups' members
beside it, so instrument/linear.py stays M8.18's byte for byte and the as-built record comes out unchanged. reading() is
checks.reading on the changed summaries under the arm, and identity() is branch identity's record test with the records
as B types them, so each point can give both verdicts, and where they agree the point rests on no changed code.
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
    eigenvalues, checks.spectrum_of_L also gives L's eigenvalues nearest zero, and convergence.summarize also gives each
    linked group's members, by its indices. None of them changes what the record computes. Yields the dict they are
    written to."""
    held = {}
    inertia, spectrum, summarize = ln.inertia, ck.spectrum_of_L, cv.summarize

    def inertia_(M, zero_rel=1e-10, gray=1e3, scale=None):
        if scale is not None:
            held['b_resolved'] = bool(inertia(M, zero_rel, gray=D_GRAY, scale=scale)[2])
            held['d_eigs'] = [float(x) for x in np.linalg.eigvalsh((M + M.T) / 2)]
        return inertia(M, zero_rel, gray=gray, scale=scale)

    def spectrum_(L):
        mu = spectrum(L)
        held['l_near'] = [float(x) for x in mu[np.argsort(np.abs(mu))[:L_NEAR]]]
        return mu

    def summarize_(rec, A, W):
        held['members'] = [dict(idx=[int(i) for i in g['idx']],
                                z=[[float(z.real), float(z.imag)] for z in rec['lam'][g['idx']]])
                           for g in rec['groups'] if len(g['idx']) > 1 and cv._representative(g)]
        return summarize(rec, A, W)

    ln.inertia, ck.spectrum_of_L, cv.summarize = inertia_, spectrum_, summarize_
    try:
        yield held
    finally:
        ln.inertia, ck.spectrum_of_L, cv.summarize = inertia, spectrum, summarize


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


def with_members(summary, members):
    """One cutoff's summary with each linked group's members beside its centre, by its indices. A linked group with no
    members refuses, so the rule never falls back on a centre where a read should have kept them."""
    held = {tuple(m['idx']): m['z'] for m in members}
    s = dict(summary)
    s['groups'] = [dict(g, members=held[tuple(g['idx'])]) if g['size'] > 1 else g for g in summary['groups']]
    return s


def reading(sums, flags, eig_hi, lam_hi, margin_hi, n_lo, members=None):
    """checks.reading under A and B: sums, lowest cutoff first, with each cutoff's B flag and each cutoff's members. With
    no members, as on a stored summary, every group is read by its centre, so A acts on nothing."""
    band = cv.band_edge(eig_hi, n_lo, lam_hi)
    if not band / 2 > ln.GRAY * margin_hi:
        return dict(verdict='Unresolved', type=None, reasons=['the band edge lies within the gray zone (UA)'],
                    rows=[], band=float(band), rel_change_max=None, rel_change_ok=None)
    sums = [lifted(s, f) for s, f in zip(sums, flags)]
    if members is not None:
        sums = [with_members(s, m) for s, m in zip(sums, members)]
    res = cv.separation(sums, band=band, arms=('own_eigenvalues',))
    rel = [r['rel_change'] for r in res['rows'] if r.get('role') == 'tested' and 'rel_change' in r]
    return dict(verdict=res['verdict'], type=res['type'], reasons=list(res['reasons']), rows=res['rows'],
                band=float(band), rel_change_max=float(max(rel)) if rel else None,
                rel_change_ok=bool(rel) and max(rel) <= ck.FRACTION)


def identity(idn, pts, pair):
    """census.identity's test with the records as B types them: an Elliptic point whose flag fires at N = 40 alone keeps
    its branch under the changed reading, as it does not as built. pts: {N: point}."""
    if not idn or not all(pts.get(N) and 'record' in pts[N] for N in pair):
        return idn
    ra, rb = (lifted(pts[N]['record'], pts[N]['b_resolved']) for N in pair)
    same = all(ra[f] == rb[f] for f in ('type', 'nL', 'nD', 'K', 'krein', 'sdim', 'ranks'))
    return dict(idn, same_record=bool(same), kept=bool(idn['aligned_distance'] <= ck.IDENTITY and same))
