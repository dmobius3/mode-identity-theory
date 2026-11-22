"""The qualification's read, the part that does not touch the instrument: the one-step map fitted on the subspace the data
support, the mode fraction, the slow circle, mode admission against stored groups, the read's floor, the Krein test and
the convergence ratio of successive differences (the terms, § THE READ and § THE REFERENCES AND THE TOLERANCE).
Development code: nothing here is registered until the freeze.

A trajectory is an array of real observations, one column per observation, taken every dt. Every read below works on
the observations of all of a point's directions at once."""
import numpy as np

RANK_REL = 1e-8        # the fit's singular-value cutoff, relative to the largest (the prototype's rank6)
MODE_FRACTION = 1e-3   # the least share of a trajectory's projected data an admitted mode carries
SLOW_RADIUS = 1.0      # the slow circle: every stored slow group lies inside, every stored fast one outside
FLOOR_SHARE = 0.9      # the floor's refit uses the first nine tenths of the observations


class Fit:
    """The exact one-step map fitted at the data's numerical rank (exact DMD on the stacked snapshot pairs)."""

    def __init__(self, trajectories, dt, rank_rel=RANK_REL):
        X = np.hstack([t[:, :-1] for t in trajectories])
        Y = np.hstack([t[:, 1:] for t in trajectories])
        U, s, Vh = np.linalg.svd(X, full_matrices=False)
        r = int(np.sum(s > rank_rel * s[0]))
        self.rank, self.singular = r, s
        Ur, sr, Vr = U[:, :r], s[:r], Vh[:r].conj().T
        Atil = Ur.conj().T @ Y @ Vr / sr
        mu, Wt = np.linalg.eig(Atil)
        self.mu = mu
        self.modes = (Y @ Vr / sr) @ Wt / mu          # exact DMD modes, one column per eigenvalue
        self.lam = np.log(mu.astype(complex)) / dt
        # each trajectory's start expanded in the modes: its share in each mode
        Phi = self.modes
        self.share = np.zeros((len(trajectories), r))
        for i, t in enumerate(trajectories):
            b = np.linalg.lstsq(Phi, t[:, 0].astype(complex), rcond=None)[0]
            self.share[i] = np.abs(b) * np.linalg.norm(Phi, axis=0) / np.linalg.norm(t[:, 0])
        self.fraction = self.share.max(axis=0)

    def admitted(self, radius=SLOW_RADIUS, fraction=MODE_FRACTION):
        """Indices of the admitted slow eigenvalues: inside the circle, with a mode carrying at least `fraction`."""
        return [j for j in range(self.rank) if abs(self.lam[j]) < radius and self.fraction[j] >= fraction]


def representative(lam):
    """The member a group is read by: an imaginary pair by its member in the upper half plane, a quartet by its member
    in the first quadrant, a real pair by its positive member. Every eigenvalue of the real map folds to it."""
    return complex(abs(lam.real), abs(lam.imag))


PER_GROUP = {'imag': 2, 'real': 2, 'complex': 4}   # eigenvalues of the real map per pair or quartet


def admit(fit, stored, radius=SLOW_RADIUS, fraction=MODE_FRACTION):
    """Match the admitted slow eigenvalues to the stored groups, one to one with multiplicity.

    `stored` is a list of dicts with 'c' (the stored centre, complex, in its representative quadrant), 'cls' ('imag',
    'real' or 'complex') and 'size'. Every admitted eigenvalue is folded to its representative and goes to the nearest
    stored group. Where that group's class holds two or more stored groups, it must lie inside half the distance from
    the group's centre to the nearest other group of the class; where the class holds one group, class and multiplicity
    assign it, and (R1) judges the agreement. A group of size k needs exactly k pairs, or k quartets, of read
    eigenvalues. Returns (centres, members), the centre of each group the mean of its members' representatives, or
    raises Admission with the cause."""
    idx = fit.admitted(radius, fraction)
    want = sum(PER_GROUP[g['cls']] * g['size'] for g in stored)
    if len(idx) != want:
        raise Admission(f'rank: {len(idx)} admitted slow eigenvalues against {want} for the stored groups')
    members = {i: [] for i in range(len(stored))}
    for j in idx:
        z = representative(fit.lam[j])
        near = min(range(len(stored)), key=lambda i: abs(z - stored[i]['c']))
        same = [i for i, g in enumerate(stored) if g['cls'] == stored[near]['cls']]
        if len(same) > 1:
            gap = min(abs(stored[near]['c'] - stored[i]['c']) for i in same if i != near)
            if abs(z - stored[near]['c']) >= gap / 2:
                raise Admission(f'match: {z:.6g} lies outside half the gap of its nearest group')
        members[near].append(j)
    for i, g in enumerate(stored):
        if len(members[i]) != PER_GROUP[g['cls']] * g['size']:
            raise Admission(f'match: stored group {i}, {g["cls"]} of size {g["size"]}, matched by {len(members[i])} eigenvalues')
    centres = [complex(np.mean([representative(fit.lam[j]) for j in members[i]])) for i in range(len(stored))]
    return centres, members


class Admission(Exception):
    """The read's mode admission failed; the message names the rank or the match."""


def floor(trajectories, dt, stored, centres, share=FLOOR_SHARE, radius=SLOW_RADIUS):
    """The read's floor: the largest change of a matched centre when the fit uses the first `share` of the observations."""
    cut = [t[:, :max(3, int(share * t.shape[1]))] for t in trajectories]
    c2, _ = admit(Fit(cut, dt), stored, radius=radius)
    return [abs(a - b) for a, b in zip(centres, c2)]


def krein(form, fit, members):
    """The Krein test on a group's read eigenspace: the Hermitian restriction of the real symmetric form to the span of
    the group's read modes. Returns (sign, definite): +1 or -1 where the restriction is definite, with definite True."""
    V = fit.modes[:, members]
    Hm = V.conj().T @ form @ V
    w = np.linalg.eigvalsh(0.5 * (Hm + Hm.conj().T))
    if np.all(w > 0):
        return 1, True
    if np.all(w < 0):
        return -1, True
    return 0, False


def successive_ratio(l8, l16, l32):
    """|lambda(h0/8) - lambda(h0/16)| / |lambda(h0/16) - lambda(h0/32)|, which cancels a bias that does not depend on the step."""
    d1, d2 = abs(l8 - l16), abs(l16 - l32)
    return d1 / d2 if d2 > 0 else float('inf'), d1, d2


def tolerance(lead):
    """b_g = 10^-3 |L_g|, with L_g Theorem 4.2's leading order at the point."""
    return 1e-3 * abs(lead)
