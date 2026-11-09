"""M8.19's gates, stretches and references (the terms: THE GATES, The stretches, THE COHERENT ROW IN R5), as functions of
numbers a job has already computed. Nothing here solves or reads a state, so the gates' mutation arms run on stored
points. The frozen instrument supplies `classify` (m815_common), imported by the caller's sys.path.

A point's input is a dict:
  eps; reached3, reached2 (gate 2); L3, L2: dict(cluster_ok, tau_re, genuine=[[[re, im], krein], ...]) with the frozen
  Point.genuine representatives; ref: dict(source='harmonic', lam, sign, count) or dict(source='level3');
  share (gate 5, computed by the job at the level-2 mode this module identifies); r and log_bound (gate 7: the largest
  real part among level 2's lifted or rigid eigenvalues, and np.log(1 / (10 eta)) as persistence.margin_ok takes it);
  harmonic: whether gate 4 reads the harmonic reference (the duration control's gates are 3, 5, 6 and 7)."""
import json
import math

ETA = 1e-3
BAND = 0.05                  # gate 4's 5%; also the band gate 3 counts candidates in (DESIGN.md, reading 1)
SHARE_MIN = 0.01             # gate 5
T_MIN, T_STEP = 1000.0, 250.0   # gate 6
LONG_T = 2750.0              # C2a/R4's duration control; a longer test waits for the longest control
REF_FLOOR = 1e-9             # the reference's slowest imag row above 1e-9, as tools/periods.py reads it
KEY_TOL = 1e-9               # a record's eps key matched to a ladder value, relative
GATES = (2, 3, 4, 5, 6, 7)


def C(z):
    return complex(z[0], z[1])


def mag(v):
    return abs(complex(v[0], v[1])) if isinstance(v, (list, tuple)) else abs(v)


# --- the references ------------------------------------------------------------------------------------------------
def load_readings(path):
    """A harmonic record's readings (M8.17's rows, M8.16.1's controls): {eps key: reading}."""
    with open(path, encoding='utf-8') as f:
        return json.load(f)['readings']


def match_key(key, ladder):
    """The ladder value a record's eps key names, or None."""
    e = float(key)
    hits = [x for x in ladder if abs(x - e) <= KEY_TOL * x]
    return hits[0] if len(hits) == 1 else None


def reference_mode(reading):
    """The reading's slowest imag row above REF_FLOOR at its top cutoff: (|lambda|, Krein sign, count)."""
    rows = sorted((mag(x['c'][-1]), -1 if x.get('neg', 0) else +1, int(x.get('count', 1))) for x in reading['rows']
                  if x.get('cls') == 'imag' and mag(x['c'][-1]) > REF_FLOOR)
    return rows[0] if rows else None


def references(readings, ladder):
    """{ladder eps: dict(source='harmonic', lam, sign, count, type, verdict)} for every reading the ladder names."""
    out = {}
    for key, r in readings.items():
        e = match_key(key, ladder)
        if e is None:
            raise ValueError(f'reading {key} is on no ladder point')
        m = reference_mode(r) if r.get('type') == 'Elliptic' and r.get('verdict') == 'converged' else None
        out[e] = dict(source='harmonic', type=r.get('type'), verdict=r.get('verdict'),
                      lam=(m[0] if m else None), sign=(m[1] if m else None), count=(m[2] if m else None))
    return out


def stretches(refs):
    """The record's Elliptic stretches: maximal runs of the record's own consecutive points, each Elliptic and
    converged; any other point splits a stretch (the terms: The stretches)."""
    out, cur = [], []
    for e in sorted(refs):
        if refs[e]['type'] == 'Elliptic' and refs[e]['verdict'] == 'converged':
            cur.append(e)
        else:
            if cur:
                out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


# --- gate 3: the mode -----------------------------------------------------------------------------------------------
def candidates(level, sign, classify):
    """The level's genuine representatives classed imag+ (sign > 0) or imag- (sign < 0) at its tau_Re, by modulus."""
    want = 'imag+' if sign > 0 else 'imag-'
    out = [(abs(C(l)), C(l), float(k)) for l, k in level['genuine'] if classify(C(l), float(k), level['tau_re']) == want]
    return sorted(out, key=lambda t: t[0])


def identify(level, sign, count, classify):
    """The slowest candidate of the given Krein sign, with the candidates within BAND of its modulus counted; identified
    when that count is the reference's multiplicity (DESIGN.md, reading 1). A count that differs leaves the mode not
    identified, recorded with the count and the candidates' moduli; it says nothing of the modes' own multiplicity.
    Returns (dict(lam, krein, multiplicity), None) or (None, why)."""
    c = candidates(level, sign, classify)
    s = '+' if sign > 0 else '-'
    if not c:
        return None, f'no genuine imaginary mode with Krein sign {s}'
    lead = c[0]
    band = [x[0] for x in c if abs(x[0] - lead[0]) <= BAND * lead[0]]
    if len(band) != count:
        n, mods = len(band), ', '.join(f'{m:.6g}' for m in band)
        return None, (f'the mode is not identified: {n} candidate{"s" if n > 1 else ""} of Krein sign {s} within '
                      f'{BAND:.0%} of the slowest ({"moduli" if n > 1 else "modulus"} {mods}), where the reference\'s '
                      f'multiplicity is {count}')
    return dict(lam=[lead[1].real, lead[1].imag], krein=lead[2], multiplicity=len(band)), None


def level3_reference(level, classify):
    """On the coherent row above 2 the reference is level 3 alone: its slowest genuine imaginary mode, of either Krein
    sign, which must be found once there."""
    allc = sorted(candidates(level, +1, classify) + candidates(level, -1, classify), key=lambda t: t[0])
    if not allc:
        return None, 'no genuine imaginary mode at level 3'
    sign = +1 if allc[0][2] > 0 else -1
    return dict(source='level3', sign=sign, count=1), None


# --- gates 6 and 7 --------------------------------------------------------------------------------------------------
def test_T(lam2):
    """Gate 6: T = max(1000, P) rounded up to a multiple of 250, P = 2 pi / |lambda| at level 2."""
    P = 2 * math.pi / abs(C(lam2))
    return max(T_MIN, T_STEP * math.ceil(P / T_STEP)), P


def margin(r, T, log_bound):
    """Gate 7, with persistence.margin_ok's arithmetic: r T <= log(1 / (10 eta))."""
    return bool(r * T <= log_bound)


# --- one point ------------------------------------------------------------------------------------------------------
def mode_at(pt, classify):
    """Gate 3's identification at both levels: (reference, mode at level 3, mode at level 2, reasons it failed)."""
    why, m3, m2 = [], None, None
    ref = pt['ref']
    if ref['source'] == 'level3':
        ref, w = level3_reference(pt['L3'], classify)
        if ref is None:
            return None, None, None, [w]
    m3, w3 = identify(pt['L3'], ref['sign'], ref['count'], classify)
    m2, w2 = identify(pt['L2'], ref['sign'], ref['count'], classify)
    if m3 is None:
        why.append('level 3: ' + w3)
    if m2 is None:
        why.append('level 2: ' + w2)
    return ref, m3, m2, why


def evaluate(pt, classify):
    """The gates a point reads (pt['read'], default 2 to 7), in order, each read only while every earlier one passed;
    the first that failed is the point's recorded cause. A target reads all six; C2a/R4's duration control reads 2, 3,
    5, 6 and 7 (the terms: THE CONTROLS)."""
    read = tuple(pt.get('read', GATES))
    g, state = {}, {}

    def fail(n, why, **kw):
        g[n] = dict(passed=False, why=why, **kw)

    def ok(n, **kw):
        g[n] = dict(passed=True, **kw)

    for n in GATES:
        if n not in read:
            continue
        if any(not g[k]['passed'] for k in g):
            break
        if n == 2:
            if pt['reached3'] and pt['reached2']:
                ok(2)
            else:
                fail(2, 'no accepted solution at level ' +
                     ' and '.join(str(h) for h, r in ((3, pt['reached3']), (2, pt['reached2'])) if not r))
        elif n == 3:
            why = [f'level {h} cluster check' for h in (3, 2) if not pt[f'L{h}']['cluster_ok']]
            ref, m3, m2, w = mode_at(pt, classify)
            why += w
            state.update(ref=ref, m3=m3, m2=m2)
            if why:
                fail(3, '; '.join(why))
            else:
                ok(3, sign=ref['sign'], count=ref['count'], reference=ref['source'], mode3=m3, mode2=m2)
        elif n == 4:
            l3, l2 = C(state['m3']['lam']), C(state['m2']['lam'])
            rel = abs(l2 - l3) / max(abs(l2), abs(l3))
            why = [] if rel <= BAND else [f'levels 2 and 3 differ by {rel:.3%}']
            reading = dict(levels=rel)
            if pt['ref']['source'] == 'harmonic':
                lam = pt['ref']['lam']
                for h, l in ((3, l3), (2, l2)):
                    d = abs(abs(l) - lam) / lam
                    reading[f'harmonic_{h}'] = d
                    if d > BAND:
                        why.append(f'level {h} differs from the harmonic reading by {d:.3%}')
            if why:
                fail(4, '; '.join(why), **reading)
            else:
                ok(4, **reading)
        elif n == 5:
            s = pt['share']
            if s >= SHARE_MIN:
                ok(5, share=s)
            else:
                fail(5, f'the slow half carries {s:.3%} on the mode', share=s)
        elif n == 6:
            T, P = test_T(state['m2']['lam'])
            state['T'] = T
            ok(6, T=T, P=P)
        elif n == 7:
            T = state['T']
            if margin(pt['r'], T, pt['log_bound']):
                ok(7, r=pt['r'], rT=pt['r'] * T)
            else:
                fail(7, f'r T = {pt["r"] * T:.3g} exceeds ln(1/(10 eta))', r=pt['r'], rT=pt['r'] * T)
    first = next((n for n in read if n in g and not g[n]['passed']), None)
    return dict(eps=pt['eps'], read=list(read), gates={str(n): g[n] for n in GATES if n in g}, first_failed=first,
                passed=(first is None and all(n in g for n in read)), T=state.get('T'))


def search(evaluated):
    """The stretch's test point: its highest point at which gates 2 to 7 all pass (the walk down from the top)."""
    good = [p for p in evaluated if p['passed']]
    return max(good, key=lambda p: p['eps']) if good else None


def coherent_stretch(types, ladder_pts, record_pts, established):
    """The coherent row's stretch: if its ladder is established, the run of consecutive Elliptic ladder points that
    contains 2 (DESIGN.md, reading 3); otherwise the record's points."""
    if not established:
        return list(record_pts), 'record'
    top = max(record_pts)
    run, best = [], None
    for e in ladder_pts:
        if types.get(e) == 'Elliptic':
            run.append(e)
        else:
            if top in run:
                best = run
            run = []
    if top in run:
        best = run
    return (best or list(record_pts)), ('ladder' if best else 'record')


def other_elliptic_runs(types, ladder_pts, stretch, established):
    """The coherent row's other Elliptic runs (DESIGN.md, reading 3): on an established ladder, each run of consecutive
    Elliptic ladder points that shares no point with the stretch, which the record names as a newly identified Elliptic
    stretch with no test fixed; on a ladder not established, none, since its types establish nothing."""
    if not established:
        return []
    runs, cur = [], []
    for e in ladder_pts:
        if types.get(e) == 'Elliptic':
            cur.append(e)
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return [r for r in runs if not set(r) & set(stretch)]
