"""The candidate cluster rule (M8.15.x control 2a; REGISTER_2.md, registered 2026-10-09T01:21:48Z): decision 2,
tracking anchored to the theorem. The functions act on abstract blocks, so the synthetic tests and the solver share
them.

  block:     dict(cls, lam = the first-quadrant representative (complex), basis = real columns orthonormal in the
             inner product used, idx = the slow eigenvalues it covers, kre = the Krein value)
  multiplet: dict(label, cls, mult); its reference value is passed separately (the theorem's at level 3, level 3's
             tracked value at level 2)
  track:     dict(label, cls, mult, basis, lam, alive, why)

The anchor is a single attempt at a multiplet's first resolved point: within each class, the computed blocks not
already tracked are matched to the newly resolved multiplets, each to `mult` blocks as a set, at cost
|lam_c - lam_ref| / |lam_ref|; every block within WINDOW, and the best mean cost per predicted block beating the
next-best distinct assignment by MARGIN. The tracking carries each live track to the computed block (or, for a
multiplet, the `mult` blocks) with smallest principal cosine >= TRACK_COS against it and |lam| within a factor BAND of
the tracked |lam| times the ladder step; its own class first, another only if none qualifies there (a tracked class
change); none, two in the searched class, or a block taken twice is Unresolved, and a lost track is never re-anchored."""
import itertools
import numpy as np

WINDOW = 0.10
MARGIN = 0.05
TRACK_COS = 0.9
BAND = 2.0


def orth(V, inner, rel=1e-8):
    """An orthonormal basis of span(V) in the inner product."""
    if V.shape[1] == 0:
        return V
    C = inner(V, V)
    C = (C + C.T) / 2
    ev, U = np.linalg.eigh(C)
    keep = ev > rel ** 2 * ev.max()
    return V @ (U[:, keep] / np.sqrt(ev[keep]))


def orth_top(V, inner, d):
    """An orthonormal basis of the d leading directions of span(V): a block's registered dimension (two for a pair,
    four for a quartet), so that round-off in its members' eigenvectors adds no spurious direction."""
    C = inner(V, V)
    C = (C + C.T) / 2
    ev, U = np.linalg.eigh(C)
    top = np.argsort(ev)[::-1][:d]
    return V @ (U[:, top] / np.sqrt(ev[top]))


def pcos_min(A, B, inner):
    """The smallest principal cosine between span(A) and span(B), both orthonormal in the inner product; for unequal
    dimensions, that of the smaller inside the larger."""
    C = inner(A, B)
    if C.size == 0:
        return 0.0
    return float(np.linalg.svd(np.atleast_2d(C), compute_uv=False).min())


def cost(lc, lref):
    return float(abs(lc - lref) / abs(lref))


def anchor(blocks, multiplets, refs, taken=()):
    """The single-attempt anchor. multiplets: the newly resolved ones; refs[label]: the reference value (complex).
    Returns {label: dict(ok, blocks, errors, mean_cost, margin, why, nearest)}; nearest is each multiplet's smallest
    error over every candidate in its class, recorded whatever the outcome."""
    out = {}
    taken = set(taken)
    for cls in sorted(set(m['cls'] for m in multiplets)):
        ms = [m for m in multiplets if m['cls'] == cls]
        cand = [i for i, b in enumerate(blocks) if b['cls'] == cls and i not in taken]
        nearest = {m['label']: (min(cost(blocks[c]['lam'], refs[m['label']]) for c in cand) if cand else None) for m in ms}
        valid = []

        def rec(k, used, chosen):
            if k == len(ms):
                valid.append(list(chosen))
                return
            m = ms[k]
            for combo in itertools.combinations([c for c in cand if c not in used], m['mult']):
                errs = [cost(blocks[c]['lam'], refs[m['label']]) for c in combo]
                if max(errs) <= WINDOW:
                    chosen.append((m['label'], combo, errs))
                    rec(k + 1, used | set(combo), chosen)
                    chosen.pop()
        rec(0, set(), [])
        n_pred = sum(m['mult'] for m in ms)
        scored = sorted(((sum(sum(e) for _, _, e in a) / n_pred, a) for a in valid), key=lambda t: t[0])
        if not scored:
            for m in ms:
                out[m['label']] = dict(ok=False, why='no assignment inside the window', nearest=nearest[m['label']])
            continue
        best_c, best = scored[0]
        margin = (scored[1][0] - best_c) if len(scored) > 1 else None
        if margin is not None and margin < MARGIN:
            for m in ms:
                out[m['label']] = dict(ok=False, why=f'not unique: the next-best mean cost lies {margin:.4f} above',
                                       nearest=nearest[m['label']], margin=margin)
            continue
        for label, combo, errs in best:
            out[label] = dict(ok=True, blocks=list(combo), errors=[float(e) for e in errs], mean_cost=float(best_c),
                              margin=margin, nearest=nearest[label])
    return out


def track(tracks, blocks, scale, inner):
    """One tracking step for every live track. scale = eps_new / eps_old. Returns {label: dict(ok, blocks, change,
    overlap, runner_up, why)}; the candidates are fixed for every track before any conflict is checked."""
    res = {}
    for t in tracks:
        if not t['alive']:
            continue
        target = abs(t['lam']) * scale
        inband = lambda b: target / BAND <= abs(b['lam']) <= target * BAND
        ov = [pcos_min(t['basis'], b['basis'], inner) for b in blocks]
        order = sorted(range(len(blocks)), key=lambda i: -ov[i])
        qual = [i for i in range(len(blocks)) if ov[i] >= TRACK_COS and inband(blocks[i])]
        own = [i for i in qual if blocks[i]['cls'] == t['cls']]
        other = [i for i in qual if blocks[i]['cls'] != t['cls']]
        r = dict(ok=False, blocks=None, change=False, why=None)
        if t['mult'] == 1:
            if len(own) == 1:
                r.update(ok=True, blocks=own)
            elif len(own) > 1:
                r['why'] = 'two candidates in its own class'
            elif len(other) == 1:
                r.update(ok=True, blocks=other, change=True)
            elif len(other) > 1:
                r['why'] = 'two candidates in another class'
            else:
                r['why'] = 'no candidate'
        else:
            if len(own) == t['mult']:
                U = orth_top(np.column_stack([blocks[i]['basis'] for i in own]), inner,
                             sum(blocks[i]['basis'].shape[1] for i in own))
                if pcos_min(t['basis'], U, inner) >= TRACK_COS:
                    r.update(ok=True, blocks=own)
                else:
                    r['why'] = 'the union fails the overlap'
            else:
                r['why'] = f'{len(own)} candidates for a multiplet of {t["mult"]}'
        picked = set(r['blocks'] or [])
        rest = [i for i in order if i not in picked]
        r['overlap'] = [float(ov[i]) for i in (r['blocks'] or [])]
        r['runner_up'] = float(ov[rest[0]]) if rest else None
        res[t['label']] = r
    used = {}
    for lab, r in res.items():
        for i in r['blocks'] or []:
            used.setdefault(i, []).append(lab)
    for i, labs in used.items():
        if len(labs) > 1:
            for lab in labs:
                res[lab].update(ok=False, why='two tracks take the same block', blocks=None)
    return res


def advance(tracks, res, blocks, inner):
    """Apply a tracking step's results: carry the live tracks to their blocks, end the lost ones."""
    for t in tracks:
        if not t['alive']:
            continue
        r = res[t['label']]
        if not r['ok']:
            t.update(alive=False, why=r['why'])
            continue
        bs = [blocks[i] for i in r['blocks']]
        t['basis'] = bs[0]['basis'] if len(bs) == 1 else orth_top(np.column_stack([b['basis'] for b in bs]), inner,
                                                                   sum(b['basis'].shape[1] for b in bs))
        t['lam'] = complex(np.mean([b['lam'] for b in bs]))
        if r['change']:
            t['cls'] = bs[0]['cls']
        t['blocks'] = list(r['blocks'])


def start_tracks(tracks, anchored, blocks, inner):
    """New tracks from an anchor's successful multiplets; a failed anchor leaves its label unanchored (dead)."""
    for label, a in anchored.items():
        t = dict(label=label, alive=bool(a['ok']), why=None if a['ok'] else a['why'], mult=None, cls=None)
        if a['ok']:
            bs = [blocks[i] for i in a['blocks']]
            t.update(cls=bs[0]['cls'], mult=len(bs), blocks=list(a['blocks']), lam=complex(np.mean([b['lam'] for b in bs])),
                     basis=bs[0]['basis'] if len(bs) == 1 else orth_top(np.column_stack([b['basis'] for b in bs]), inner,
                                                                         sum(b['basis'].shape[1] for b in bs)))
        tracks.append(t)


# --- blocks from a verdict's slow eigenpairs ------------------------------------------------------------------------
def classify(lam, krein, tau_re):
    if lam.real > tau_re and abs(lam.imag) <= tau_re:
        return 'real'
    if lam.real > tau_re:
        return 'quartet'
    return 'imag+' if krein > 0 else 'imag-'


def blocks_from_verdict(v, tau_re, cls_old):
    """The computed slow blocks outside the exact fibre vectors (the 0.9 rule's 'fibre' label marks those), each with
    its partners: a pair's conjugate, a real pair's negative, a quartet's three others. Basis: the real span of the
    members' eigenvectors, orthonormal in the phase-space inner product."""
    vals, vecs = v.vals, v.vecs
    lin, n2 = v.lin, v.n2
    Mr, c = lin.Mr, lin.c
    inner = v.ps.inner
    kre = [float(np.real(np.vdot(x, np.concatenate([lin.L @ x[:n2], (Mr @ x[n2:]) / c ** 2])))) for x in vecs.T]
    used = {i for i in range(len(vals)) if cls_old[i] == 'fibre'}
    tol = lambda lam: 1e-6 * abs(lam) + 1e-7
    blocks, loose = [], []
    for i in sorted(range(len(vals)), key=lambda k: abs(vals[k])):
        if i in used:
            continue
        lam = vals[i]
        if not (lam.real >= -tau_re and lam.imag >= -tau_re):
            continue
        cl = classify(lam, kre[i], tau_re)
        targets = {'imag+': [np.conj(lam)], 'imag-': [np.conj(lam)], 'real': [-lam],
                   'quartet': [np.conj(lam), -lam, -np.conj(lam)]}[cl]
        members = [i]
        for tg in targets:
            free = [k for k in range(len(vals)) if k not in used and k not in members]
            if not free:
                break
            j = min(free, key=lambda k: abs(vals[k] - tg))
            if abs(vals[j] - tg) <= tol(lam):
                members.append(j)
        used.update(members)
        V = np.column_stack([np.real(vecs[:, members]), np.imag(vecs[:, members])])
        blocks.append(dict(cls=cl, lam=complex(lam), kre=kre[i], idx=members, basis=orth_top(V, inner, 4 if cl == 'quartet' else 2),
                           complete=len(members) == 1 + len(targets)))
    loose = [i for i in range(len(vals)) if i not in used]
    return blocks, loose, kre
