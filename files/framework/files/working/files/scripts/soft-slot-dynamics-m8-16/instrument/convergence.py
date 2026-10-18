"""The separation rule (DESIGN.md section 10.2), as SEPARATION_PLAN.md makes it an algorithm, with the units' rulings of
2026-10-17 folded (UA, UB). A point's classification is converged when its structure holds along its ladder in N and
every tested group's uncertainty is at most FACTOR, a tenth, of its distance to the nearest type-changing event.

summarize(rec, A, W) keeps from one linear.record what the rule needs: the record's structure, its margin, and every
typed group outside the gray zone, as the first-quadrant member of its orbit {lam, conj lam, -lam, -conj lam}, with the
group's numerical estimate from projector().

separation(sums, band=None, arms=()) reads a point's summaries at the cutoffs of its ladder, lowest first:
  1. the structure: the type, n(L), n(D), K, V0 (its dimension, ranks and match) and the imaginary groups' negative
     Krein counts are the same at every cutoff, with nothing unresolved at any; otherwise Unresolved;
  2. the tested groups, at the highest cutoff: every group with |lam| below band/2, band being the free frequency of the
     slot's lowest level above the lowest cutoff used (every group when band is None); every Krein-negative imaginary
     group and every off-axis group, wherever it lies; and, for each tested imaginary group, its nearest imaginary group
     of opposite Krein sign, wherever it lies, tested against the same distance (UB);
  3. matching: each tested group is matched, at each lower cutoff used, to a group of its class, size and Krein count;
     the match must be unique (the next candidate at least twice as far) and bidirectional (UA). Where its one-to-one
     match fails and it has candidates of its own class and Krein sign, of any size, it and those competitors form a
     set, closed under the same test at every cutoff used, its count taken with multiplicity (UA, UB, 2026-10-17).
     Closures that share a group are one set, their union, which is closed under the same test, so a set is the same
     whichever of its groups is read first. Every group to be read is read, none passed over for lying in a set
     already read, and a tested set's partner joins the groups to be read before any is read (DEVLOG 219). Each
     closure read alone, in stored order, with the groups already read passed over, made a control's verdict turn on
     the eigensolver's output order (DEVLOG 218); a link read from either group's side joined sets, through the
     higher cutoff's unmatched groups, whose nearest candidate is far, to the whole spectrum (DEVLOG 219). The
     set matches when its total count agrees at every cutoff. Its change between two cutoffs is the bottleneck distance
     between their centres, the least over one-to-one assignments of the largest displacement (UA; it is at least the
     Hausdorff distance, UB's measure). The set is then read as one group, with its distance to each event its nearest
     member's, and its numerical estimate its largest member's, every member's projector usable. A tested group with no
     candidate of its class and sign, or a set whose count changes, makes the point Unresolved; none is omitted. Members
     of one class and sign cannot change the type among themselves, since distance to an event is 1-Lipschitz in the set
     (UB);
  4. its uncertainty U, the largest of: the remaining error, d2^2 / (d1 - d2) from three cutoffs where d2 < d1, and the
     last change d2 from two; where d2 >= d1 and d2 exceeds the floor, no rate is shown and the point is Unresolved (UA,
     UB); the floor, the larger margin of the two highest cutoffs; and the numerical estimate, ||P_g|| max(||R_g||,
     u ||A||) at the two highest cutoffs, from a projector that must be usable, or the point is Unresolved (UA);
  5. its distance d at the highest cutoff, the smallest of: |lam| - G margins (the gray zone's top); |Re lam| for an
     off-axis group (the imaginary axis); and, for an imaginary group, the distance to the nearest imaginary group of
     opposite Krein sign;
  6. the verdict: converged when the structure holds and U <= FACTOR d for every tested group and partner; otherwise
     Unresolved, naming each failure. Every tested group's U and d are reported.
The rule rests on the leading rate dominating at the highest cutoffs: a slow rate hidden under a faster one is beyond
any reading of a few cutoffs, and the floor catches one only within ten floors of an event (UB; SEPARATION_PLAN.md).
The arms, each a mutation that must let a counterexample through: 'factor_one', 'last_change', 'contract_ignored',
'no_floor', 'no_numerical', 'no_gray', 'no_axis', 'no_krein', 'no_partner', 'set_centroid', which reads a set's
change at its centroid (UB), and 'one_way_set', the sets as built before DEVLOG 218 (each closure alone, the
groups read in stored order, those already read passed over), whose counterexample is a verdict that turns on the
order of the groups. 'no_floor' drops the floor from U only: the
margin stays the threshold below which a non-contracting sequence is round-off, without which about half of a
converged point's unchanged groups read non-contracting and every point reads Unresolved (DEVLOG 154).
"""
import numpy as np
from scipy.optimize import linear_sum_assignment

U = np.finfo(float).eps
FACTOR = 0.1
ARMS = ('factor_one', 'last_change', 'contract_ignored', 'no_floor', 'no_numerical', 'no_gray', 'no_axis', 'no_krein',
        'no_partner', 'set_centroid', 'one_way_set')
COND_MAX = 1e-2 / U        # Y^H X conditioning beyond which the projector is not usable
LEFT_MAX = 1e4 * U         # the left vectors' residual, relative to ||A||, beyond which the pairing is not verified
IDEM_MAX = 1e-6            # ||P X - X|| / ||X||, beyond which the projector is not normalized
SPAN_MIN = 1e-6            # the record's own test that a group's eigenvectors span it (linear.record)


def projector(A, W, lam, V, idx, pidx, normA=None):
    """The spectral projector of the group idx of A's eigenvalues lam (right eigenvectors V, unit columns), from right
    eigenvectors alone: A^T W = -W A, so for A x = nu x, y = W conj(x) satisfies y^H A = -nu y^H. Taking x at -conj(lam),
    its partners pidx, gives y = W x_(-conj lam), a left eigenvector at lam. Returns ||P_g||, computed as
    ||R_X M^-1 R_Y^H|| with X = Q_X R_X, Y = Q_Y R_Y and M = Y^H X; the group's largest residual ||A x - lam x||; and the
    checks that make it usable (UA): the eigenvectors span the group, by the record's own test (no singular value below
    1e-6 of the largest; a defective group's do not); the left vectors' residual ||A^H y + nu y||, which is what verifies
    the pairing; M's conditioning; and M inverted to working accuracy (P X = X, which holds by construction, read
    numerically) (UB)."""
    nA = np.linalg.norm(A, 2) if normA is None else normA
    X, Xp = V[:, idx], V[:, pidx]
    Y = W @ Xp
    resid = float(np.max(np.linalg.norm(A @ X - X * lam[idx], axis=0) / np.linalg.norm(X, axis=0)))
    left = float(np.max(np.linalg.norm(A.conj().T @ Y + Y * lam[pidx], axis=0) / np.linalg.norm(Y, axis=0)) / nA)
    M = Y.conj().T @ X
    cond = float(np.linalg.cond(M)) if np.all(np.isfinite(M)) else np.inf
    out = dict(resid=resid, left=left, cond=cond, pnorm=np.inf, idem=np.nan, ok=False, why=None)
    for Z in (X, Xp):
        sv = np.linalg.svd(Z, compute_uv=False)
        if sv.min() < SPAN_MIN * sv.max():
            out['why'] = "the group's eigenvectors do not span it (a defective group)"
            return out
    if not np.isfinite(cond) or cond > COND_MAX:
        out['why'] = f'Y^H X singular to working precision (condition {cond:.1e})'
        return out
    Minv = np.linalg.inv(M)
    _, Rx = np.linalg.qr(X)
    _, Ry = np.linalg.qr(Y)
    out['pnorm'] = float(np.linalg.norm(Rx @ Minv @ Ry.conj().T, 2))
    out['idem'] = float(np.linalg.norm(X @ (Minv @ M) - X) / np.linalg.norm(X))
    if left > LEFT_MAX:
        out['why'] = f'the pairing is not verified (left residual {left:.1e} ||A||)'
    elif out['idem'] > IDEM_MAX:
        out['why'] = f'the projector is not normalized (P X - X {out["idem"]:.1e})'
    else:
        out['ok'] = True
    return out


def _representative(g):
    c = g['centre']
    if g['cls'] == 'imag':
        return c.imag > 0
    if g['cls'] == 'real':
        return c.real > 0
    return c.real > 0 and c.imag > 0


def summarize(rec, A, W):
    """What the rule needs from one record (module docstring), JSON-able."""
    lam, V, nA = rec['lam'], rec['V'], rec['normA']
    top = rec['gray'] * rec['margin']
    groups = []
    for g in rec['groups']:
        c = g['centre']
        if not _representative(g) or abs(c) < top:
            continue
        if g['cls'] == 'imag':
            pidx = g['idx']                                   # -conj(lam) = lam on the axis: the group is its own partner
        else:
            tau = max(rec['margin'], rec['kappa_d'] * np.sqrt(U * nA * abs(c)))
            cand = [h for h in rec['groups'] if h['cls'] == g['cls'] and len(h['idx']) == len(g['idx'])]
            p = min(cand, key=lambda h: abs(h['centre'] + np.conj(c)))
            pidx = p['idx'] if abs(p['centre'] + np.conj(c)) <= tau else None
        if pidx is None:
            sens = dict(resid=np.nan, left=np.nan, cond=np.inf, pnorm=np.inf, idem=np.nan, ok=False,
                        why='no partner group at -conj(lambda)')
        else:
            sens = projector(A, W, lam, V, g['idx'], pidx, nA)
        groups.append(dict(c=[c.real, c.imag], cls=g['cls'], size=len(g['idx']), neg=g['neg'], status=g['status'], **sens))
    return dict(type=rec['type'], nL=int(rec['nL']), nD=int(rec['nD']), K=int(rec['K']), sdim=int(rec['sdim']),
                ranks=list(rec['jordan_ranks']), v0=bool(rec['v0_matches']), unresolved=list(rec['unresolved']),
                margin=float(rec['margin']), gray=float(rec['gray']), normA=float(nA),
                krein=sorted(int(g[2]) for g in rec['imag_groups'] if g[2] > 0), groups=groups)


def _structure(s):
    return (s['type'], s['nL'], s['nD'], s['K'], s['sdim'], tuple(s['ranks']), s['v0'], tuple(s['krein']))


def _same(g, h):
    return g['cls'] == h['cls'] and g['size'] == h['size'] and g['neg'] == h['neg']


def _c(g):
    return complex(g['c'][0], g['c'][1])


def match(ga, i, gb):
    """The index in gb of the group matched to ga[i]: the nearest of the same class, size and Krein count, unique (the
    next candidate at least twice as far) and bidirectional (ga[i] the same way nearest to it); None otherwise (UA)."""
    c = _c(ga[i])
    cand = sorted((abs(_c(h) - c), j) for j, h in enumerate(gb) if _same(h, ga[i]))
    if not cand or (len(cand) > 1 and cand[1][0] < 2 * cand[0][0]):
        return None
    j = cand[0][1]
    back = sorted((abs(_c(h) - _c(gb[j])), k) for k, h in enumerate(ga) if _same(h, gb[j]))
    if back[0][1] != i or (len(back) > 1 and back[1][0] < 2 * back[0][0]):
        return None
    return j


def _opposite(gs, i):
    """The nearest imaginary group of opposite Krein sign to the imaginary group gs[i], or None."""
    g = gs[i]
    neg = bool(g['neg'])
    cand = [(abs(_c(h) - _c(g)), j) for j, h in enumerate(gs) if h['cls'] == 'imag' and bool(h['neg']) != neg]
    return min(cand)[1] if cand else None


def _key(g):
    """A group's class and, for an imaginary group, its Krein sign: what a set's members share."""
    return (g['cls'], bool(g['neg']) if g['cls'] == 'imag' else None)


def bottleneck(P, Q):
    """The bottleneck distance between two equal multisets of points: the least, over one-to-one assignments, of the
    largest displacement (UA)."""
    P, Q = np.asarray(P), np.asarray(Q)
    D = np.abs(np.subtract.outer(P, Q))
    vals = np.unique(D)
    lo, hi = 0, len(vals) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        cost = (D > vals[mid]).astype(float)
        r, c = linear_sum_assignment(cost)
        if cost[r, c].sum() == 0:
            hi = mid
        else:
            lo = mid + 1
    return float(vals[lo])


def closure(levels, i):
    """The ruled set of the group levels[0][i] (levels highest first), from that seed alone: every group of its class
    and Krein sign within twice the nearest candidate's distance of a member, at an adjacent cutoff, added until none
    is left out. One index set per cutoff; None where some member's adjacent cutoff has no group of its class and
    sign."""
    key = _key(levels[0][i])
    S = [set() for _ in levels]
    S[0].add(i)
    changed = True
    while changed:
        changed = False
        for a in range(len(levels) - 1):
            for x, y in ((a, a + 1), (a + 1, a)):
                for k in list(S[x]):
                    c = _c(levels[x][k])
                    cand = sorted((abs(_c(h) - c), j) for j, h in enumerate(levels[y]) if _key(h) == key)
                    if not cand:
                        return None
                    for dist, j in cand:
                        if (dist < 2 * cand[0][0] or dist == cand[0][0]) and j not in S[y]:
                            S[y].add(j)
                            changed = True
    return S


def merged_sets(levels, seeds):
    """{seed: its set}: the union of the closures of every seed whose closure shares a group with its own, transitively,
    so a set is the same whichever of its seeds is read first (module docstring, item 3); None where the seed's own
    closure is None."""
    clo = {s: closure(levels, s) for s in seeds}
    valid = [s for s in seeds if clo[s] is not None]
    root = {s: s for s in valid}

    def find(x):
        while root[x] != x:
            x = root[x]
        return x
    for a, s in enumerate(valid):
        for t in valid[a + 1:]:
            if find(s) != find(t) and any(clo[s][l] & clo[t][l] for l in range(len(levels))):
                root[find(s)] = find(t)
    union = {}
    for s in valid:
        u = union.setdefault(find(s), [set() for _ in levels])
        for l in range(len(levels)):
            u[l] |= clo[s][l]
    return {s: union[find(s)] if clo[s] is not None else None for s in seeds}


def _chain(levels, i):
    """The one-to-one matches of levels[0][i] down the cutoffs, or None where one fails."""
    js = [i]
    for a in range(1, len(levels)):
        j = match(levels[a - 1], js[-1], levels[a])
        if j is None:
            return None
        js.append(j)
    return js


def _nearest_opposite(G, top):
    """(distance, index) of the nearest imaginary group of opposite Krein sign to any of the groups `top` of G, or
    None."""
    opp = [(abs(_c(G[j]) - _c(G[jj])), j) for jj in top for j in [_opposite(G, jj)] if j is not None]
    return min(opp) if opp else None


def separation(sums, band=None, arms=()):
    """The rule (module docstring) on a point's summaries, lowest cutoff first."""
    arms = set(arms)
    assert arms <= set(ARMS), arms
    factor = 1.0 if 'factor_one' in arms else FACTOR
    one_way = 'one_way_set' in arms                               # the arm: the sets as built before DEVLOG 218
    use = sums[-3:]
    levels = [s['groups'] for s in reversed(use)]                 # highest first
    hi, mid = use[-1], use[-2]
    reasons, rows = [], []
    st = [_structure(s) for s in sums]
    if any(s['unresolved'] for s in sums):
        reasons.append('structure: a record is unresolved')
    if len(set(st)) > 1:
        reasons.append('structure: the type, indices, V0 or Krein counts differ along the ladder')
    G = levels[0]
    tested = [i for i, g in enumerate(G) if band is None or abs(_c(g)) < band / 2 or g['cls'] != 'imag' or g['neg']]
    pending = [(i, 'tested', None) for i in tested]
    if 'no_partner' not in arms:
        for i in tested:
            if G[i]['cls'] == 'imag':
                j = _opposite(G, i)
                if j is not None and j not in tested:
                    pending.append((j, 'partner', [_c(G[i])]))
    seen = {i for i, _, _ in pending}
    chains, sets = {}, {}
    while not one_way:              # the groups to be read, to a fixpoint: a tested set's partner joins them (UB)
        for i, _, _ in pending:
            if i not in chains:
                chains[i] = _chain(levels, i)
        sets = merged_sets(levels, sorted({i for i, _, _ in pending if chains[i] is None}))
        new = []
        if 'no_partner' not in arms and 'no_krein' not in arms:
            for i, role, _ in pending:
                S = sets.get(i)
                if role != 'tested' or S is None or G[i]['cls'] != 'imag':
                    continue
                near = _nearest_opposite(G, sorted(S[0]))
                if near is not None and near[1] not in seen:
                    new.append((near[1], 'partner', [_c(G[j]) for j in sorted(S[0]) for _ in range(G[j]['size'])]))
                    seen.add(near[1])
        if not new:
            break
        pending += new
    noise = max(hi['margin'], mid['margin'])                      # the floor, and the non-contraction threshold
    floor = 0.0 if 'no_floor' in arms else noise
    done, read = set(), set()
    k = 0
    while k < len(pending):
        i, role, ref = pending[k]
        k += 1
        if one_way and i in done:
            continue
        js = _chain(levels, i) if one_way else chains[i]
        if js is not None:
            members = [[(js[a], levels[a][js[a]])] for a in range(len(levels))]
            kind = 'group'
        else:
            S = closure(levels, i) if one_way else sets[i]
            if S is None:
                done.add(i)
                if (role, tuple(ref or ()), i) in read:
                    continue
                read.add((role, tuple(ref or ()), i))
                c = _c(G[i])
                rows.append(dict(c=[c.real, c.imag], cls=G[i]['cls'], neg=G[i]['neg'], role=role, kind='group', ok=False,
                                 why='no candidate of its class and Krein sign at a lower cutoff'))
                reasons.append(f"{role} group at {c:.6g}: no candidate of its class and Krein sign at a lower cutoff")
                continue
            members = [[(j, levels[a][j]) for j in sorted(S[a])] for a in range(len(levels))]
            kind = 'set'
        done |= {j for j, _ in members[0]}
        ident = (role, tuple(ref or ()), tuple(tuple(j for j, _ in lev) for lev in members))
        if ident in read:                                         # the same set, read for another of its groups
            continue
        read.add(ident)
        hi_members = [g for _, g in members[0]]
        cls, neg = hi_members[0]['cls'], hi_members[0]['neg']
        pts = [[_c(g) for _, g in lev for _ in range(g['size'])] for lev in members]
        row = dict(c=[[z.real, z.imag] for z in pts[0]] if kind == 'set' else [pts[0][0].real, pts[0][0].imag],
                   cls=cls, neg=neg, role=role, kind=kind, count=len(pts[0]))
        name = f"{role} {'set' if kind == 'set' else 'group'} at {pts[0][0]:.6g}" + (f" (+{len(pts[0]) - 1})" if kind == 'set' else '')
        if len({len(p) for p in pts}) > 1:
            row.update(ok=False, why="the set's count differs between cutoffs")
            rows.append(row)
            reasons.append(f"{name}: the set's count differs between cutoffs")
            continue
        if kind == 'set' and 'set_centroid' in arms:
            cen = [np.mean(p) for p in pts]
            steps = [abs(cen[a] - cen[a + 1]) for a in range(len(pts) - 1)]
        else:
            steps = [bottleneck(pts[a], pts[a + 1]) for a in range(len(pts) - 1)]
        d2 = steps[0]
        rem, why = d2, None
        if len(pts) == 3 and 'last_change' not in arms:
            d1 = steps[1]
            if d2 < d1:
                rem = d2 * d2 / (d1 - d2)
            elif d2 > noise and 'contract_ignored' not in arms:
                rem, why = np.inf, 'non-contracting above the floor'
            row['d1'] = d1
        num = 0.0
        if 'no_numerical' not in arms:
            two = [g for _, g in members[0]] + [g for _, g in members[1]]
            bad = [g for g in two if not g['ok']]
            if bad:
                why = why or f"the numerical estimate is not usable: {bad[0]['why']}"
                num = np.inf
            else:
                num = max([g['pnorm'] * max(g['resid'], U * hi['normA']) for _, g in members[0]] +
                          [g['pnorm'] * max(g['resid'], U * mid['normA']) for _, g in members[1]])
        Ug = max(rem, floor, num)
        dist = {}
        if role == 'partner':
            dist['the opposite Krein sign'] = min(abs(z - r) for z in pts[0] for r in ref)
        else:
            if 'no_gray' not in arms:
                dist["A's gray zone"] = min(abs(z) for z in pts[0]) - hi['gray'] * hi['margin']
            if cls != 'imag' and 'no_axis' not in arms:
                dist['the imaginary axis'] = min(abs(z.real) for z in pts[0])
            if cls == 'imag' and 'no_krein' not in arms:
                near = _nearest_opposite(G, [j for j, _ in members[0]])
                if near is not None:
                    dk, jk = near
                    dist['the opposite Krein sign'] = dk
                    if one_way and kind == 'set' and 'no_partner' not in arms and jk not in done and jk not in seen:
                        pending.append((jk, 'partner', pts[0]))               # UB: the nearest member's neighbour
                        seen.add(jk)
        event, dmin = min(dist.items(), key=lambda kv: kv[1]) if dist else (None, np.inf)
        ok = why is None and Ug <= factor * dmin
        row.update(d2=d2, rem=rem, floor=floor, num=num, U=Ug, d=dmin, event=event,
                   ratio=dmin / Ug if Ug > 0 else np.inf, ok=ok, why=why)
        rows.append(row)
        if not ok:
            reasons.append(f"{name}: " + (why if why else f"U {Ug:.2e} above a {'tenth' if factor == FACTOR else 'factor ' + format(factor, 'g')} of its distance to {event}, {dmin:.2e}"))
    verdict = 'converged' if not reasons else 'Unresolved'
    return dict(verdict=verdict, type=hi['type'] if verdict == 'converged' else None, reasons=reasons, rows=rows,
                cutoffs=len(use))


def row_centre(row):
    """A row's place: the group's centre, or a set's first member."""
    c = row['c']
    return complex(*c[0]) if isinstance(c[0], (list, tuple)) else complex(*c)


def band_edge(eig_hi, N_lo, lam):
    """The free frequency of the slot's lowest level above the cutoff N_lo, at lam: every free mode below it at the
    higher cutoff has a counterpart at N_lo. eig_hi: the higher basis's level energies n (n + 2)."""
    above = [e for e in set(np.round(np.asarray(eig_hi, dtype=float), 6)) if e > N_lo * (N_lo + 2) + 0.5]
    return np.sqrt(min(above)) - np.sqrt(lam) if above else np.inf
