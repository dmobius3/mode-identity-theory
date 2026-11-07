#!/usr/bin/env python3
"""Post-run: made after MIT's own computation read its last value. It builds RECORD.md from the run's logged files in
run/out and its machine's reading in run/ENVIRONMENT.json, the statements made before the reads in run/DESIGN.md and
run/TOP48.md, M8.17's stored records, the repository's commit history, and the outputs of dev/runs/011_row_readings/
and dev/runs/013_locator_reading/ where it cites them: each measured value is read from the files the run wrote, each
commit from the history, and each fit or extrapolation is labelled INFERRED. It follows M8.18's tools/build_record.py,
carried to this computation: its stages and custody, the fresh controls on both ladders, the twelve, the rows point by
point, T4/R4's locator, T5's top on both ladders, the statements made before the reads, and what stays open. A reason
the rule repeats, as it does for a set read once for each group it partners, is given once, and the reason on U with
its bar written out, as run/TOP48.md section 1 gives it.

Usage, from this folder: python3 -I -B tools/build_record.py MIT_REPO [--check]
  MIT_REPO  a clone of the repository that holds this folder: the commits that pinned and noted each stage, and
            M8.17's stored records of the twelve
  --check   build the record and compare it with RECORD.md, without writing; exit 1 on any difference

It refuses if a launch in run/out/RUNLOG.json failed or ran under a manifest no stage takes, if a job record's file
differs from its logged SHA-256, if a reading file's classification, as built or changed, differs from what census_lib
gives from that file, if a statement it sets a reading beside is not in run/DESIGN.md or run/TOP48.md as quoted, or if
a dev run's output it cites does not say what the record takes from it."""
import hashlib
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'run'))
from instrument import linear as ln  # noqa: E402
import census_lib as lib  # noqa: E402
import changed  # noqa: E402
import checks as ck  # noqa: E402
import fresh  # noqa: E402
import grid  # noqa: E402

OUT = os.path.join(ROOT, 'run', 'out')
REL = 'files/framework/files/working/files/scripts/soft-slot-dynamics-mit'
CENSUS = 'files/framework/files/working/files/slot-dynamics-census.md'
M817 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-17/run/out'
GH = 'https://github.com/dmobius3/mode-identity-theory/commit/'
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
ROWS = ('T1_R4', 'T4_R4', 'T1_R5', 'C2a_R5', 'T5_R2', 'T5J_R2')
NAME = dict(T1_R4='T1', T4_R4='T4', T1_R5='T1', C2a_R5='The coherent row', T5_R2='T5', T5J_R2="T5's second member")
TWELVE = {'T1_R4': [math.sqrt(2), 32, 32 * math.sqrt(2), 64, 72], 'T1_R5': [32],
          'T4_R4': [4, 8, 8 * math.sqrt(2), 64, 72], 'T5_R2': [32 * math.sqrt(2)]}      # dev/stored_readings.py
FRESH = {'fresh_P5': 'P5', 'fresh_C3R_R4': 'C3R/R4', 'fresh_C2b': 'C2b', 'fresh_C2a_R5': 'C2a/R5'}
STAGES = ((frozenset({'solves'}), 'The solves at `N = 24`, 32 and 40'),
          (frozenset({'reads', 'identities', 'readings', 'fresh'}), 'The reads at `N = 24`, 32 and 40, the fresh controls first'),
          (frozenset({'locate'}), "T4/R4's locator, M8.18's location of T4/R5 reproduced first"),
          (frozenset({'solves48'}), 'The solves at `N = 48`'),
          (frozenset({'rechecks48', 'reads48', 'identities48', 'readings48', 'fresh48', 'top48'}),
           'The reads at `N = 48`, the recheck and the fresh controls first'))
# each stage's launches in the order its terms set (run/DESIGN.md section 7, run/LOCATOR.md, run/TOP48.md section 7): the
# fresh controls and their pass before any row, the reproduction before T4/R4, the recheck and the fresh controls' pass
# at N = 48 before T5's reads there, and top48 last
ORDER = (['solves'], ['reads', 'identities', 'readings', 'fresh', 'reads', 'identities', 'readings'], ['locate', 'locate'],
         ['solves48'], ['rechecks48', 'reads48', 'identities48', 'readings48', 'fresh48', 'rechecks48', 'reads48',
                        'identities48', 'readings48', 'top48'])
CAUSE = {'link':'a new link at `N = 40` alone', 'flag': "D's flag at `N = 40` alone, B clearing it",
         'flag_40_48': "D's flag at `N = 40` and 48 alone, B clearing it", 'flag_48': "D's flag at `N = 48` alone, B clearing it"}
UNRES = {changed.ND_LINE: "D's flag"}
# the statements made before the reads, as run/DESIGN.md section 6 and run/TOP48.md section 5 make them
DESIGN_SAYS = ('**The twelve** should keep their stored type and indices at `N = 40`.',
               'The real part at 128 reads about 0.048 if it is geometric in `N`, 0.035 if algebraic, and 0.053 if its '
               'square is geometric', 'At 132: 0.127, 0.116, 0.136.',
               '**Every law keeps 132 off the axis,** and 128 is too close to call.',
               'the collision sits near 127 at `N = 40`, with a limit of 127.5 to 128',
               '**An Elliptic stretch with `K` = 4** should appear before the quartet',
               '**No new link at `N = 40` alone** at any stored point of the rows')
TOP48_SAYS = ('they gave at 128: 0.0481, 0.0346 and 0.0534 at `N = 40`, and 0.0288, −0.0015 and 0.0420 at 48',
              'At 132: 0.1272, 0.1161, 0.1359 at 40, and 0.1159, 0.0925, 0.1311 at 48',
              '127, 0.0643 to 0.0647; 128, 0.0909 to 0.0912; 129, 0.1112 to 0.1115; 130, 0.1282 to 0.1284; 132, 0.1565 to '
              '0.1567', 'Its step from 40 to 48 is about 1×10⁻⁴ to 7×10⁻⁴',
              '**The collision** at 125.98 at `N = 48`',
              '**The types at `N = 48`:** Elliptic (9, 3, 6) at 116 and 120; Elliptic (4, 0, 4) at 124; Hyperbolic (4, 0, 4) '
              'from 126, with the quartet within about 0.01 of the axis at 126, too close to call',
              '**Branch identity at (40, 48):** 5×10⁻⁴ to 9×10⁻⁴ at every target and in-row control',
              '**The tolerances at `N = 48`,** at every point it reads on T5: no gap falls between τ(40) and τ(48); K1\'s '
              'separation keeps A\'s smallest eigenvalue outside the cluster at least 200 times the top of its gray zone; L\'s '
              'gray zone stays at least 10⁷ times clear; and n(D)\'s inherited zone holds no eigenvalue',
              '**The branch:** T5\'s path at `N = 48` should reach 132 on the branch it holds at 32 and 40')
LAWS48 = {127: (0.0643, 0.0647), 128: (0.0909, 0.0912), 129: (0.1112, 0.1115), 130: (0.1282, 0.1284), 132: (0.1565, 0.1567)}
PINNED48 = {128: (0.0288, -0.0015, 0.0420), 132: (0.1159, 0.0925, 0.1311)}
LAWS40 = {128: (0.035, 0.053), 132: (0.116, 0.136)}


def stop(m):
    raise SystemExit(f'build_record: {m}')


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def J(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def fe(x):
    """An amplitude as the terms write it: 0.25, 0.354, 2.83, 22.63, 132."""
    x = float(x)
    if x == int(x):
        return str(int(x))
    return f'{x:.3f}'.rstrip('0') if x < 1 else f'{x:.2f}'


def sci(x, d=2):
    m, e = f'{x:.{d - 1}e}'.split('e')
    return f'{m}×10{str(int(e)).translate(SUP)}'


def num(x, d=2):
    """A positive number at d figures, in plain form from 10⁻³ to 10³ and as a power of ten outside."""
    if x == 0:
        return '0'
    if 1e-3 <= abs(x) < 1e3:
        return f'{x:.{max(d - 1 - math.floor(math.log10(abs(x))), 0)}f}'
    return sci(x, d)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, check=True).stdout


def first_with(repo, pin, path):
    """The first commit in the repository's history whose file at path gains the string pin."""
    out = git(repo, 'log', 'HEAD', '--reverse', '--format=%H', f'-S{pin}', '--', path).split()
    if not out:
        stop(f'no commit gives {path} the pin {pin[:8]}')
    return out[0]


def link(h):
    return f'[`{h[:8]}`]({GH}{h})'


def rec(r, krein=True):
    s = f"{r['type']} ({r['nL']}, {r['nD']}, {r['K']})"
    return s + (f"; {r['kr']}, {r['kc']}, {r['ki']}" if krein else '')


def cls(c):
    return f"{c['type']} ({c['nL']}, {c['nD']}, {c['K']})" if c['classified'] else 'not classified'


def point_rec(d, k, N, krein=True):
    p = d['cutoffs'][str(N)]['points'].get(k)
    if not p or 'record' not in p:
        return 'no record'
    r = p['record']
    s = rec(r, krein)
    if r['unresolved']:
        s += ', ' + ', '.join(UNRES.get(u, u) for u in r['unresolved'])
    if not ck.k1(p, d['case']):
        s += ', K1 fails'
    return s


def records(d, k, Ns, krein=True):
    """A point's records along a ladder: one entry if they agree at every cutoff, otherwise each, lowest first."""
    cells = [point_rec(d, k, N, krein) for N in Ns]
    return cells[0] if len(set(cells)) == 1 else ' / '.join(cells)


def spans(cells, Ns):
    """Records at cutoffs Ns as runs: 'X at 24; Y at 32 to 48'."""
    out, i = [], 0
    while i < len(cells):
        j = i
        while j + 1 < len(cells) and cells[j + 1] == cells[i]:
            j += 1
        at = f'{Ns[i]}' if i == j else f'{Ns[i]} and {Ns[j]}' if j == i + 1 else f'{Ns[i]} to {Ns[j]}'
        out.append(f'{cells[i]} at {at}')
        i = j + 1
    return '; '.join(out)


def uniq(xs):
    out = []
    for x in xs:
        if x not in out:
            out.append(x)
    return out


SET_RE = re.compile(r"^(tested|partner) (set|group) at \S+?( \(\+\d+\))?: (.*)$")


def short(cause):
    """One of census_lib.here's causes, shortened for a table: the rule's reasons each in a few words."""
    if cause.startswith('the rule reads it Unresolved: '):
        out = []
        for r in cause[len('the rule reads it Unresolved: '):].split('; '):
            m = SET_RE.match(r)
            if r == 'structure: the type, indices, V0 or Krein counts differ along the ladder':
                out.append('the structure differs along the ladder')
            elif r == 'structure: a record is unresolved':
                out.append('a record is unresolved')
            elif m and m.group(4) == "the set's count differs between cutoffs":
                out.append(f"a {m.group(1)} set's count changes")
            elif m and m.group(4) == 'non-contracting above the floor':
                out.append(f'a {m.group(1)} {m.group(2)} does not contract')
            elif m and m.group(4).startswith('U ') and 'above a tenth of its distance to ' in m.group(4):
                out.append(f"`U` above a tenth of the distance to {m.group(4).split('distance to ')[1].rsplit(',', 1)[0]}")
            elif m:
                out.append(f'a {m.group(1)} {m.group(2)}: {m.group(4)}')
            else:
                out.append(r)
        return '; '.join(uniq(out))
    m = re.match(r'branch identity fails between N = (\d+) and (\d+): aligned distance (\S+), the records (agree|differ)', cause)
    if m:
        return f'identity fails, {m.group(1)} to {m.group(2)}, the records {m.group(4)}'
    return cause


U_RE = re.compile(r'^U (\S+) above a tenth of its distance to the imaginary axis, (\S+)$')


def bar(reason):
    """The rule's reason on U with its bar written out, as run/TOP48.md section 1 gives it: the reading file's string gives
    U and the distance, not the tenth of the distance that U is held against."""
    m = SET_RE.match(reason)
    u = U_RE.match(m.group(4)) if m else None
    if not u:
        return reason
    U, dist = float(u.group(1)), float(u.group(2))
    if not U > dist / 10:
        stop(f'a reason on U whose U does not exceed a tenth of its distance: {reason}')
    return (f'{reason[:len(reason) - len(m.group(4))]}`U` = {sci(U, 3)} exceeds one tenth of its distance to the imaginary '
            f'axis, {sci(dist / 10, 3)} (distance {sci(dist, 3)})')


def full(causes):
    """census_lib.here's causes as the record gives them: each of the rule's reasons once, the one on U with its bar."""
    out = []
    for c in causes:
        if c.startswith('the rule reads it Unresolved: '):
            rs = [bar(r) for r in uniq(c[len('the rule reads it Unresolved: '):].split('; '))]
            out.append('the rule reads it Unresolved: ' + '; '.join(rs))
        else:
            out.append(c)
    return '; '.join(out)


def idn_cell(d, k, pairs):
    cells = []
    for a, b in pairs:
        i = d['identity'][k][f'{a}-{b}']
        cells.append(num(i['aligned_distance'], 3) + ('' if i['kept'] else ', fails') if i else 'none')
    return ' / '.join(cells)


def ran(t0, t1):
    """A stage's span: 'D t0 to t1' on one day, otherwise 'D0 t0 to D1 t1'."""
    if t0[:10] == t1[:10]:
        return f'{t0[:10]}, {t0[11:16]}Z to {t1[11:16]}Z'
    return f'{t0[:10]} {t0[11:16]}Z to {t1[:10]} {t1[11:16]}Z'


def listed(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ' and '.join(xs) if len(xs) == 2 else ', '.join(xs[:-1]) + ' and ' + xs[-1]


def tolerances48(d48, ks):
    """At each point, from its own records at N = 40 and 48, what run/TOP48.md section 5 forecast for N = 48 from the
    reads at 40 (dev/runs/014_top48_expectations/, E, with the actual margin and norms in place of the forecast ones): a
    gap between tested imaginary groups at 40 that falls between tau(40) and tau(48); A's smallest eigenvalue outside the
    cluster over the gray zone's top; L's smallest genuine eigenvalue over its gray zone's top; and n(D)'s flag."""
    links, a0s, lrs, flags = [], [], [], []
    for k in ks:
        p40, p48 = d48['cutoffs']['40']['points'][k], d48['cutoffs']['48']['points'][k]
        r40, r48 = p40['record'], p48['record']
        band = lib.band_value(d48['case']['slot'], p40['lam'])
        imag = sorted((g for g in p40['summary']['groups'] if g['cls'] == 'imag'), key=lambda g: g['c'][1])
        for g1, g2 in zip(imag, imag[1:]):
            lev = max(abs(g1['c'][1]), abs(g2['c'][1]))
            if not (lev < band / 2 or g1['neg'] or g2['neg']):
                continue
            gap = abs(g1['c'][1] - g2['c'][1])
            t40 = max(r40['margin'], ln.KAPPA_D * math.sqrt(ln.U * r40['normA'] * lev))
            t48 = max(r48['margin'], ln.KAPPA_D * math.sqrt(ln.U * r48['normA'] * lev))
            if t40 < gap <= t48:
                links.append((k, lev))
        a0s.append(r48['outside_min'] / (ln.GRAY * r48['margin']))
        g = p48.get('lkernel', {}).get('genuine')
        if g:
            lrs.append(g / (ln.L_CUT * ln.G_L))
        flags += [k for u in r48['unresolved'] if u == changed.ND_LINE]
    return dict(links=links, a0=min(a0s), l=min(lrs) if lrs else None, nl=len(lrs), flags=flags)


def recompute(res, lad, name):
    """Each point's classification, as built and changed, from the reading file alone, as run/jobs.py's ladder_reading
    computes it; refuses on any difference from the file's own."""
    for k, both in res['both'].items():
        e = float(k)
        if lib.key(e) != k:
            stop(f'{name}: the key {k} is not its amplitude\'s')
        a = lib.here(lib.at(res, e, lad), res['case'], lad)
        pb = lib.at(dict(res, readings=res['changed']), e, lad)
        pb['identity'] = {lib.pair_key(p): changed.identity(pb['identity'].get(lib.pair_key(p)), pb['points'], p)
                          for p in lad['pairs']}
        b = lib.here(pb, res['case'], lad)
        mine = json.loads(json.dumps(dict(as_built=a, changed=b, same=a == b)))
        if mine != both:
            stop(f'{name} at {k}: the classification recomputed from the file differs from the file\'s')
    return len(res['both'])


def off(p, kind='complex'):
    return [g for g in p['summary']['groups'] if g['cls'] == kind]


def collision(d, N, lo=64):
    """The collision law of run/DESIGN.md section 6, as dev/runs/011_row_readings/ applies it: the quartet's real part
    squared linear in eps over the Hyperbolic points above lo, its zero; with the records' bracket. INFERRED."""
    pts = d['cutoffs'][str(N)]['points']
    ks = sorted((k for k in pts if float(k) >= lo), key=float)
    hyp = [k for k in ks if pts[k]['record']['type'] == 'Hyperbolic']
    if [k for k in ks if float(k) > float(hyp[0]) and pts[k]['record']['type'] != 'Hyperbolic']:
        stop(f'T5 at N = {N}: a point above the first Hyperbolic one is not Hyperbolic')
    below = max((k for k in ks if float(k) < float(hyp[0])), key=float)
    xs = [float(k) for k in hyp]
    ys = []
    for k in hyp:
        q = off(pts[k])
        if len(q) != 1:
            stop(f'T5 at {k}, N = {N}: not one quartet')
        ys.append(q[0]['c'][0] ** 2)
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    a = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return dict(zero=mx - my / a, below=float(below), below_type=rec(pts[below]['record'], False), first=xs[0], n=len(xs))


def main():
    args = [a for a in sys.argv[1:] if a != '--check']
    check = '--check' in sys.argv[1:]
    if len(args) != 1:
        stop(__doc__)
    repo = args[0]
    design = open(os.path.join(ROOT, 'run', 'DESIGN.md'), encoding='utf-8').read()
    terms48 = open(os.path.join(ROOT, 'run', 'TOP48.md'), encoding='utf-8').read()
    for s in DESIGN_SAYS:
        if s not in design:
            stop(f'run/DESIGN.md does not say: {s}')
    for s in TOP48_SAYS:
        if s not in terms48:
            stop(f'run/TOP48.md does not say: {s}')

    # --- custody: the launches, by stage, and the job records ----------------------------------------------------
    ev = J(os.path.join(OUT, 'RUNLOG.json'))['events']
    launches = []
    for e in ev:
        if e['event'].startswith('launch: '):
            launches.append(dict(t=e['t'], kind=e['event'][8:].split(',')[0], manifest=e['manifest'], done=0, failed=0, end=None))
        elif not launches:
            stop(f'an event before any launch: {e}')
        elif e['event'].endswith(' completed'):
            launches[-1]['done'] += 1
            launches[-1]['failed'] += e.get('exit') != 0
        elif e['event'].startswith('launch ended'):
            if e['event'] != 'launch ended; 0 failed: []':
                stop(f"a launch ended with a failure: {e['event']}")
            launches[-1]['end'] = e['t']
    if any(x['failed'] or x['end'] is None for x in launches):
        stop('a launch failed or did not end')
    starts = {}
    for e in ev:
        if e['event'].endswith(' started'):
            j = e['event'][:-len(' started')]
            starts[j] = starts.get(j, 0) + 1
    resumed = sorted(j for j, n in starts.items() if n > 1)
    stages = []
    for x in launches:
        if stages and stages[-1]['manifest'] == x['manifest']:
            stages[-1]['launches'].append(x)
        else:
            stages.append(dict(manifest=x['manifest'], launches=[x]))
    if len(stages) != len(STAGES):
        stop(f'{len(stages)} stages in the log, where the record takes {len(STAGES)}')
    for s, (kinds, title), order in zip(stages, STAGES, ORDER):
        got = {x['kind'] for x in s['launches']}
        if not got <= kinds:
            stop(f'a stage of launches {sorted(got)} is not {title}')
        if [x['kind'] for x in s['launches']] != order:
            stop(f"{title}: the launches ran as {[x['kind'] for x in s['launches']]}, not in the order the terms set")
        s['title'] = title
        s['jobs'] = sum(x['done'] for x in s['launches'])
        s['t0'], s['t1'] = s['launches'][0]['t'], s['launches'][-1]['end']
        s['pinned'] = first_with(repo, s['manifest'], f'{REL}/run/MANIFEST_PIN')
        s['noted'] = first_with(repo, s['manifest'], CENSUS)
    jobs = [J(os.path.join(OUT, 'jobs', f)) for f in sorted(os.listdir(os.path.join(OUT, 'jobs'))) if f.endswith('.json')]
    pins = {s['manifest'] for s in stages}
    nfiles = 0
    for r in jobs:
        if r['manifest'] not in pins:
            stop(f"{r['job']} ran under a manifest no stage takes")
        for f, h in r['files'].items():
            nfiles += 1
            if sha(os.path.join(OUT, f)) != h:
                stop(f"{f} differs from the SHA-256 {r['job']} logged")
    if len(jobs) != sum(s['jobs'] for s in stages):
        stop(f'{len(jobs)} job records, where the log completes {sum(s["jobs"] for s in stages)} jobs')
    env = J(os.path.join(ROOT, 'run', 'ENVIRONMENT.json'))

    # --- the files ----------------------------------------------------------------------------------------------------
    rows = {t: J(os.path.join(OUT, f'{t}.json')) for t in ROWS}
    fr1 = {t: J(os.path.join(OUT, f'{t}.json')) for t in FRESH}
    fr2 = {t: J(os.path.join(OUT, f'{t}_L48.json')) for t in FRESH}
    t48 = J(os.path.join(OUT, 'T5_R2_L48.json'))
    top = J(os.path.join(OUT, 'TOP48.json'))
    pass1 = J(os.path.join(OUT, fresh.names()[1]))
    pass2 = J(os.path.join(OUT, fresh.names_48()[1]))
    loc = J(os.path.join(OUT, 'LOCATE_T4_R4.json'))
    repro = J(os.path.join(OUT, 'LOCATE_REPRO_T4_R5.json'))
    rechecks = [J(os.path.join(OUT, f)) for f in sorted(os.listdir(OUT)) if f.startswith('recheck48_') and f.endswith('.json')]
    stored = {t: J(os.path.join(repo, M817, f'{t}.json')) for t in TWELVE}
    n_re = sum(recompute(rows[t], lib.ARM_A, t) for t in ROWS) + sum(recompute(fr1[t], lib.ARM_A, t) for t in FRESH)
    n_re += recompute(t48, grid.LAD_48, 'T5_R2_L48') + sum(recompute(fr2[t], grid.LAD_48, t + '_L48') for t in FRESH)
    if not (pass1['passed'] and pass2['passed']) or any(pass1['results'].values()) or any(pass2['results'].values()):
        stop('a fresh control misses a mark')
    for f, h in list(pass1['files'].items()) + list(pass2['files'].items()):
        if sha(os.path.join(OUT, f)) != h:
            stop(f'{f} differs from the file its pass read')
    if not repro['passed'] or repro['differences'] or repro['unequal_arrays']:
        stop("the locator's reproduction did not pass")
    if not all(r['same'] for r in rechecks):
        stop('a recheck found a difference')
    n_rc = sum(len(r['differences']) for r in rechecks)

    L = []
    a = L.append
    s48 = stages[4]

    # --- the head -----------------------------------------------------------------------------------------------------
    a("# MIT's own computation: the record")
    a('')
    a("MIT's own computation of the census's open items, labelled as MIT's own and outside M8. Its values are no M8 outcome, "
      'take no part in S6, select no S5 stretch on OpenWave\'s record and move no `MODELS.md` cell, and they change no '
      'closure the census records; the census page says why, in its notes from 2026-11-01 on '
      '([§ V, step 5](../../slot-dynamics-census.md#v-the-program)). Its design is [`run/DESIGN.md`](run/DESIGN.md), with '
      "T4/R4's locator in [`run/LOCATOR.md`](run/LOCATOR.md) and T5's top at `N = 48` in [`run/TOP48.md`](run/TOP48.md). "
      f"It ran in {len(launches)} launches from {stages[0]['t0'][:10]} to {s48['t1'][:10]}, {len(jobs)} jobs in all, none "
      'failed. `tools/build_record.py` builds this record from the run\'s logged files in `run/out/` and its machine\'s '
      "reading in `run/ENVIRONMENT.json`, the statements made before the reads in `run/DESIGN.md` and `run/TOP48.md`, "
      "M8.17's stored records, the repository's commit history, and the outputs of `dev/runs/011_row_readings/` and "
      "`dev/runs/013_locator_reading/` where it cites them; its fits and extrapolations are labelled INFERRED. It also "
      f"recomputes each point's classification, as built and changed, from its reading file with `census_lib`, {n_re} "
      "points on the two ladders, and finds every one equal to the file's. The solutions come with this record, as "
      '`DEVLOG.md` entry 10 said. The read and reading files stay on the bench, each named by its SHA-256 in the job record '
      'that wrote it, and can be read again from the solutions on the pinned trees.')
    a('')

    # --- the chart ----------------------------------------------------------------------------------------------------
    a('**The chart,** on the ladder `N = 24`, 32 and 40, each cutoff on its own path from the seed. A point is classified '
      'when it is accepted with K1 at every cutoff, the rule reads it converged with a type, and branch identity holds on '
      'both pairs; the type is the rule\'s, with `N = 40`\'s indices `(n(L), n(D), K)`.')
    a('')
    a('| Row | Slot | Points | Classified, as built / changed | Wherever classified | Not classified |')
    a('|---|---|---|---|---|---|')
    chart = {}
    for t in ROWS:
        d = rows[t]
        ks = sorted(d['both'], key=float)
        nb = sum(d['both'][k]['as_built']['classified'] for k in ks)
        nc = sum(d['both'][k]['changed']['classified'] for k in ks)
        runs, opened = [], []
        for k in ks:
            b = d['both'][k]
            got = [b[arm] for arm in ('as_built', 'changed') if b[arm]['classified']]
            if len({cls(g) for g in got}) > 1:
                stop(f'{t} at {k}: the two verdicts classify different types')
            if got:
                c = cls(got[0])
                if runs and runs[-1][0] == c:
                    runs[-1][2] = k
                else:
                    runs.append([c, k, k])
            if not (b['as_built']['classified'] and b['changed']['classified']):
                opened.append((k, 'as built' if b['changed']['classified'] else ''))
        where = runs[0][0] if len(runs) == 1 else ', '.join(
            f'{c} ' + (f'from {fe(x)} to {fe(y)}' if x != y else f'at {fe(x)}') for c, x, y in runs)
        groups, i = [], 0
        while i < len(opened):
            j = i
            while j + 1 < len(opened) and ks.index(opened[j + 1][0]) == ks.index(opened[j][0]) + 1 and not opened[j + 1][1]:
                j += 1
            if j - i >= 2:
                groups.append(f'{fe(opened[i][0])} to {fe(opened[j][0])}')
                i = j + 1
            else:
                groups.append(fe(opened[i][0]) + (f' {opened[i][1]}' if opened[i][1] else ''))
                i += 1
        nots = ', '.join(groups) if groups else 'none'
        if t == 'T4_R4':
            nots += '; the change of type between 4 and 5.66 is not located (§ 5)'
        chart[t] = dict(nb=nb, nc=nc, n=len(ks), runs=runs, nots=nots)
        a(f"| {NAME[t]} | `{d['case']['slot']}` | {len(ks)}, {fe(ks[0])} to {fe(ks[-1])} | {nb} / {nc} | {where} | {nots} |")
    a('')
    tg = top['targets']
    raw = []
    for k in sorted(tg, key=float):
        r = tg[k]['on_48']['as_built']['reported']
        if tg[k]['on_48']['changed']['reported'] != r:
            stop(f'T5 at {k}: the two raw verdicts on the second ladder differ')
        txt = f"converged, {cls(r)}" if r['classified'] else 'Unresolved'
        if raw and raw[-1][0] == txt:
            raw[-1][1].append(k)
        else:
            raw.append([txt, [k]])
    raw_txt = '; '.join((fe(ks_[0]) if len(ks_) == 1 else f'{fe(ks_[0])} and {fe(ks_[1])}' if len(ks_) == 2
                         else f'{fe(ks_[0])} to {fe(ks_[-1])}') + f', {txt}' for txt, ks_ in raw)
    misses = sorted((k for k, v in top['in_row'].items() if v), key=float)
    a(f"**On a second ladder,** `N = 32`, 40 and 48, T5's top reads, as built and changed alike: {raw_txt}. None of it is "
      f"classified there, because the rule does not read the classified points below it, "
      f"{' and '.join(fe(k) for k in misses)}, converged on that ladder (§ 6).")
    a('')

    # --- 1. custody ---------------------------------------------------------------------------------------------------
    a('## 1. Custody')
    a('')
    a('Five stages, each on its own manifest pin. Each read refuses until it is given the commit of the note that names its '
      'pin (`run/jobs.py`, `note_gate`), and refuses a path whose job record names a manifest the solves did not run under, '
      'or whose files differ. A stage is pinned at the first commit that writes its pin into `run/MANIFEST_PIN`, and noted '
      'at the first whose census page names it.')
    a('')
    a('| Stage | Launches | Jobs | Ran | Manifest | Pinned at | Noted at |')
    a('|---|---|---|---|---|---|---|')
    for s in stages:
        a(f"| {s['title']} | {len(s['launches'])} | {s['jobs']} | {ran(s['t0'], s['t1'])} | `{s['manifest'][:8]}` | "
          f"{link(s['pinned'])} | {link(s['noted'])} |")
    a('')
    a(f"- **Every job completed,** none failed, and {'none was resumed' if not resumed else 'resumed: ' + ', '.join(resumed)}. "
      f'Each job record names the manifest it ran under, and the {nfiles} files the records logged match their SHA-256.')
    a('- **Before each note, the solves were checked at solve fields alone,** which hold no spectrum: '
      '`dev/runs/010_solve_checks/` before the note of 2026-11-04, and `dev/runs/015_solve_checks_48/` before the note of '
      "2026-11-07, which also sets each point's reached amplitude at `N = 48` beside its record at `N = 40`, deciding "
      'nothing.')
    a(f"- **The recheck.** Before any read at `N = 48`, the stored reads at `N = 32` and 40 at every point the second ladder "
      f"reads were read again on the run's machine, {sum(len(r['differences']) for r in rechecks)} point-reads, each equal "
      f'to its stored read field for field, value and type, timings aside: {sum(len(v) for r in rechecks for v in r["differences"].values())} differences.')
    a(f"- **The reproduction.** The locator's job first ran M8.18's location of T4 in `R5` again on this tree: "
      f"{len(repro['differences'])} differences from M8.18's record and {len(repro['unequal_arrays'])} of {repro['arrays']} "
      'arrays unequal, so T4 in `R4` was read.')
    a(f"- **The machine:** Python {env['interpreter']['version']}, NumPy {env['numpy']['version']} and SciPy "
      f"{env['scipy']['version']}, on Accelerate, under {env['os']['product']} {env['os']['version']} ({env['os']['build']}) on "
      f"one {env['machine']['cpu']}.")
    a('')
    if n_rc != 36:
        stop(f'{n_rc} point-reads rechecked, where the record takes 36')

    # --- 2. the fresh controls ----------------------------------------------------------------------------------------
    a('## 2. The fresh controls')
    a('')
    a('Six amplitudes no earlier record holds, next to M8.18\'s two failures, each with marks fixed before any read on its '
      'ladder: the case\'s own type and indices, K1 and branch identity at every cutoff, and the two verdicts below. No row '
      'was read until a pass for the first ladder\'s marks was on record, and no point of T5 at `N = 48` until a pass for '
      'the second\'s. Every point holds every mark on both ladders.')
    a('')
    for lad_name, frs, Ns, marks, pairs in (('`N = 24`, 32 and 40', fr1, grid.LADDER, pass1['marks'], ((24, 32), (32, 40))),
                                            ('`N = 32`, 40 and 48', fr2, grid.LADDER_48, pass2['marks'], ((32, 40), (40, 48)))):
        a(f'On {lad_name}:')
        a('')
        a('| Control | `ε` | Records, `(n(L), n(D), K)`; `k_r`, `k_c`, `k_i⁻` | As built | Changed | Marked, as built / changed '
          '| Identity, lower / upper pair |')
        a('|---|---|---|---|---|---|---|')
        for tag, e, mb, mc, cause in marks:
            d, k = frs[tag], lib.key(e)
            rb, rc = d['readings'][k], d['changed'][k]
            mark = (f'{mb}, by {CAUSE[cause]}' if cause else mb) if mb else 'reported, not marked'
            a(f"| {FRESH[tag]} | {e:.2f} | {records(d, k, Ns)} | {rb['verdict']} | {rc['verdict']} | {mark} / {mc} | "
              f'{idn_cell(d, k, pairs)} |')
        a('')

    # --- 3. the twelve ------------------------------------------------------------------------------------------------
    a('## 3. The twelve')
    a('')
    kept = 0
    lines = []
    for t, eps in TWELVE.items():
        d, s = rows[t], stored[t]
        for e in eps:
            k = lib.key(e)
            ks = [x for x in s['cutoffs']['32']['points'] if abs(float(x) - e) < 1e-9]
            if len(ks) != 1:
                stop(f"M8.17's {t} holds no record at {e}")
            was = []
            for N in ('16', '24', '32'):
                sm = s['cutoffs'][N]['points'][ks[0]]['summary']
                was.append(f"{sm['type']} ({sm['nL']}, {sm['nD']}, {sm['K']})")
            b = d['both'][k]
            now = [point_rec(d, k, N, False) for N in grid.LADDER]
            same = (b['as_built']['classified'] and b['changed']['classified'] and b['same']
                    and len(set(was + now)) == 1 and cls(b['as_built']) == now[-1])
            kept += same
            lines.append(f"| {NAME[t]} | `{d['case']['slot']}` | {fe(e)} | {was[0] if len(set(was)) == 1 else ' / '.join(was)} | "
                         f"{now[0] if len(set(now)) == 1 else ' / '.join(now)} | {cls(b['as_built'])} | {cls(b['changed'])} | "
                         f"{idn_cell(d, k, ((24, 32), (32, 40)))} |")
    a(f"The twelve points M8.18's remedy did not read, read here on the first ladder. {kept} of 12 keep M8.17's stored type "
      'and indices at every cutoff, classified both ways.')
    a('')
    a("| Row | Slot | `ε` | M8.17's records at `N = 16`, 24, 32 | Records at `N = 24`, 32, 40 | As built | Changed | "
      'Identity, 24 to 32 / 32 to 40 |')
    a('|---|---|---|---|---|---|---|---|')
    L.extend(lines)
    a('')

    # --- 4. the rows --------------------------------------------------------------------------------------------------
    a('## 4. The rows, point by point')
    a('')
    a('Each point\'s records at `N = 24`, 32 and 40, given once where they agree at all three, with `(n(L), n(D), K)` and the '
      'Krein counts `k_r`, `k_c`, `k_i⁻`; its classification as built and changed; and branch identity\'s aligned distance on '
      'both pairs, against the guard of 10⁻². Below each table, every point not classified, with the causes the run\'s '
      'code gives for it.')
    a('')
    for t in ROWS:
        d = rows[t]
        ks = sorted(d['both'], key=float)
        c = chart[t]
        a(f"### {NAME[t]} in `{d['case']['slot']}`")
        a('')
        a(f"{c['n']} points, {c['nb']} classified as built and {c['nc']} changed.")
        a('')
        a('| `ε` | Records at `N = 24`, 32, 40 | As built | Changed | Identity, 24 to 32 / 32 to 40 |')
        a('|---|---|---|---|---|')
        notes = []
        for k in ks:
            b = d['both'][k]
            a(f"| {fe(k)} | {records(d, k, grid.LADDER)} | {cls(b['as_built'])} | {cls(b['changed'])} | "
              f"{idn_cell(d, k, ((24, 32), (32, 40)))} |")
            for arm, label in (('as_built', 'as built'), ('changed', 'changed')):
                if not b[arm]['classified'] and (arm == 'as_built' or not b['same']):
                    notes.append(f"- **{fe(k)},** {label if not b['same'] or arm == 'changed' else 'both ways'}: "
                                 f"{full(b[arm]['causes'])}.")
        a('')
        if notes:
            L.extend(notes)
            a('')

    # --- 5. T4's change of type in R4 ---------------------------------------------------------------------------------
    a("## 5. T4's change of type in `R4`")
    a('')
    lo, hi = None, None
    for N, b in loc['bisection'].items():
        if lo is None:
            lo, hi = b['interval']
        elif b['interval'] != [lo, hi]:
            stop(f'the locator\'s interval differs at N = {N}')
    mids = {N: b['midpoints'] for N, b in loc['bisection'].items()}
    eps_mid = [m['eps'] for m in mids['24']]
    if any([m['eps'] for m in v] != eps_mid for v in mids.values()):
        stop("the locator's midpoints differ between cutoffs")
    refused = [i for i, m in enumerate(mids['24']) if not (m['from_lower']['k1'] and m['from_upper']['k1'])]
    if any([i for i, m in enumerate(v) if not (m['from_lower']['k1'] and m['from_upper']['k1'])] != refused for v in mids.values()):
        stop('K1 refuses different midpoints at different cutoffs')
    moved = [m['eps'] for m in mids['24'] if m.get('moved')]
    stops = {N: b['stop'] for N, b in loc['bisection'].items()}
    if loc['located'] or len(moved) != 1 or len(refused) != 2:
        stop('the locator\'s record is not the stop this section states')
    nl = loc['nL']
    a(f"The locator ran on ({fe(loc['bracket'][0])}, {fe(loc['bracket'][1])}), {loc['types'][0]} to {loc['types'][1]}, "
      f"with `n(L)` {nl['32'][0]} and {nl['32'][1]} at its ends, each midpoint solved from both ends of the current "
      'interval and read. The types below come from the records of the accepted midpoint solves, not from classified points. '
      f"**`n(L)` changes from {nl['32'][0]} to {nl['32'][1]} inside [{lo:.6f}, {hi:.6f}] at `N = 24`, 32 and 40; the change "
      f"of type is not located; K1 stopped the bisection at {mids['24'][refused[0]]['eps']:.6f} and at the moved point "
      f'{moved[0]:.6f}, at every cutoff.** The interval is not identified with the genuine index crossing. Its width, '
      f'{hi - lo:.6g}, is {(hi - lo) / lo:.3g} of its lower end, where completing asks below {lib.W_HALF:g}.')
    a('')
    a('| Midpoint | Records at `N = 24`, 32, 40, both solves | K1 | `n(L)` |')
    a('|---|---|---|---|')
    for i, e in enumerate(eps_mid):
        cells, k1s, nls = [], [], []
        for N in ('24', '32', '40'):
            m = mids[N][i]
            rs = {rec(m[s]['point']['record'], False) for s in ('from_lower', 'from_upper')}
            if len(rs) != 1:
                stop(f'the two solves at the midpoint {e} differ in their records at N = {N}')
            cells.append(rs.pop())
            k1s.append(m['from_lower']['k1'] and m['from_upper']['k1'])
            nls.append(m['from_lower']['nL'])
        a(f"| {e:.6f}{' (moved)' if mids['24'][i].get('moved') else ''} | "
          f"{cells[0] if len(set(cells)) == 1 else ' / '.join(cells)} | "
          f"{'holds' if all(k1s) else 'fails' if not any(k1s) else ' / '.join('holds' if x else 'fails' for x in k1s)} | "
          f"{nls[0] if len(set(nls)) == 1 else ' / '.join(map(str, nls))} |")
    a('')
    if set(stops.values()) != {'K1 fails'}:
        stop(f'the locator stopped otherwise than on K1: {stops}')
    o13 = open(os.path.join(ROOT, 'dev', 'runs', '013_locator_reading', 'locator_reading.out'), encoding='utf-8').read()
    zs = dict(re.findall(r'N = (\d+): the line through \d+ accepted midpoints, slope \S+, largest residual \S+; its zero (\S+);', o13))
    hs = re.findall(r"K1's neighbourhood, \|lambda\| < 3 margin with margin \S+: \|eps - zero\| < (\S+), twice that (\S+), "
                    r'where completion asks an interval below (\S+)', o13)
    offs = re.findall(r'the moved point (\S+) from it \(n\(L\) \d\), the midpoint (\S+) from it', o13)
    if sorted(zs) != ['24', '32', '40'] or len(hs) != 3 or len(offs) != 3 or len({h[2] for h in hs}) != 1:
        stop("dev/runs/013_locator_reading/ does not give the line's zero and K1's neighbourhood at each cutoff")
    if any(abs(float(x)) >= float(h[0]) for h, o in zip(hs, offs) for x in o):
        stop("a refused point lies outside K1's neighbourhood")
    a(f"Outside the locator's rule, and deciding nothing (`dev/runs/013_locator_reading/`, INFERRED): the eigenvalue of L "
      f"that changes sign, on a straight line through the accepted midpoints near the interval, crosses zero at "
      f"{float(zs['24']):.6f} at `N = 24` and {float(zs['32']):.6f} at 32 and 40. K1 cannot hold where A's eigenvalue on "
      f"that mode lies within three margins of zero, a neighbourhood {listed(sci(float(h[1])) for h in hs)} wide around "
      f"that zero at `N = 24`, 32 and 40, where a completed interval must be narrower than {sci(float(hs[0][2]))}. Both "
      'refused points lie inside it at every cutoff.')
    a('')

    # --- 6. T5's top --------------------------------------------------------------------------------------------------
    d1 = rows['T5_R2']
    top_ks = sorted([lib.key(e) for e in grid.TOP48['in_row'] + grid.TOP48['targets']], key=float)
    a("## 6. T5's top, on both ladders")
    a('')
    a("T5's points above 90.51 on the first ladder, `N = 24`, 32 and 40, and on the second, `N = 32`, 40 and 48, each "
      'cutoff on its own path from the seed. The second ladder reads the nine points the first leaves open and the three '
      'classified points below them, 100, 106 and 112, as controls in the row. The records at 32 and 40 are the same reads '
      'on both ladders, read again before any read at 48 and found equal. On the second ladder no target is classified, '
      'because the controls at 100 and 106 are not, so each target\'s reading there is its raw one.')
    a('')
    a("| `ε` | Records at `N = 24`, 32, 40, 48 | First ladder | Second ladder | The quartet's real part at 24 / 32 / 40 / 48 | "
      'Identity, 24 to 32 / 32 to 40 / 40 to 48 |')
    a('|---|---|---|---|---|---|')
    re_q = {}
    for k in top_ks:
        cells = [point_rec(d1, k, N, False) for N in grid.LADDER] + [point_rec(t48, k, 48, False)]
        if [point_rec(t48, k, N, False) for N in (32, 40)] != cells[1:3]:
            stop(f'T5 at {k}: the second ladder\'s records at 32 and 40 differ from the first\'s')
        qs = []
        for dd, N in ((d1, 24), (d1, 32), (d1, 40), (t48, 48)):
            q = off(dd['cutoffs'][str(N)]['points'][k])
            if len(q) > 1:
                stop(f'T5 at {k}, N = {N}: more than one quartet')
            qs.append(q[0]['c'][0] if q else None)
        re_q[k] = qs
        b1 = d1['both'][k]
        first_txt = cls(b1['as_built']) if b1['as_built']['classified'] else 'not classified: ' + '; '.join(
            uniq(short(c) for c in b1['as_built']['causes']))
        if b1['as_built'] != b1['changed']:
            stop(f'T5 at {k}: the two verdicts differ on the first ladder')
        b2 = t48['both'][k]
        if b2['as_built'] != b2['changed']:
            stop(f'T5 at {k}: the two verdicts differ on the second ladder')
        if k in tg:
            r = tg[k]['on_48']['as_built']['reported']
            second = (f'raw: converged, {cls(r)}' if r['classified'] else 'raw: ' + '; '.join(uniq(short(c) for c in r['causes'])))
        else:
            second = cls(b2['as_built']) if b2['as_built']['classified'] else 'not classified: ' + '; '.join(
                uniq(short(c) for c in b2['as_built']['causes']))
        idn = [d1['identity'][k]['24-32'], d1['identity'][k]['32-40'], t48['identity'][k]['40-48']]
        if t48['identity'][k]['32-40'] != idn[1]:
            stop(f'T5 at {k}: the identity between 32 and 40 differs between the ladders')
        a(f"| {fe(k)} | {spans(cells, (24, 32, 40, 48))} | {first_txt} | {second} | "
          f"{' / '.join('none' if x is None else f'{x:.4f}' for x in qs)} | "
          f"{' / '.join(num(i['aligned_distance'], 3) + ('' if i['kept'] else ', fails') for i in idn)} |")
    a('')
    rows_in = {}
    for k in misses:
        rr = [r for r in t48['readings'][k]['rows'] if r.get('why') == 'non-contracting above the floor']
        if len(rr) != 1 or rr != [r for r in t48['changed'][k]['rows'] if r.get('why') == 'non-contracting above the floor']:
            stop(f'T5 at {k}: not one non-contracting group, the same both ways')
        r = rr[0]
        if not (r['role'] == 'tested' and r['kind'] == 'group' and r['cls'] == 'imag' and r['neg'] == 1 and r['d2'] >= r['d1']):
            stop(f'T5 at {k}: the non-contracting group is not the one this section states')
        rows_in[k] = r
    held = [k for k, v in top['in_row'].items() if not v]
    g112 = [r for r in t48['readings'][held[0]]['rows'] if r['role'] == 'tested' and r['cls'] == 'imag' and r['neg'] == 1
            and abs(r['c'][1] - rows_in[misses[0]]['c'][1]) < 0.03]
    if len(held) != 1 or len(g112) != 1:
        stop('the held control is not one, or its group is not found')
    a('- **The controls in the row.** At ' + ' and '.join(fe(k) for k in misses) + ' the records keep Elliptic (9, 3, 6) at '
      '`N = 32`, 40 and 48, with nothing unresolved, K1 holds and branch identity holds on both pairs, but the rule reads '
      'each Unresolved, as built and changed alike, on one Krein-negative imaginary group, "non-contracting above the '
      'floor": ' + '; '.join(
          f"at {fe(k)}, the group at {r['c'][1]:.4f}i steps {sci(r['d1'], 3)} from 32 to 40 and {sci(r['d2'], 3)} from 40 to "
          f"48, above the floor of {sci(r['floor'], 3)}, and lies {r['d']:.3f} from the nearest event, {r['event']}"
          for k, r in rows_in.items())
      + f". With no shrinking step the rule shows no rate. At {fe(held[0])} the same group steps "
      f"{sci(g112[0]['d1'], 3)} and then {sci(g112[0]['d2'], 3)}, and the point is classified, Elliptic (9, 3, 6). On the "
      'first ladder all three were classified. Why the steps at ' + ' and '.join(fe(k) for k in misses)
      + ' stop shrinking is OPEN.')
    hyp1 = [k for k in top_ks if re_q[k][2] is not None]
    steps = {k: (re_q[k][1] - re_q[k][2], re_q[k][2] - re_q[k][3]) for k in top_ks if re_q[k][3] is not None}
    ratio = [s2 / s1 for s1, s2 in steps.values()]
    lim = {k: re_q[k][3] - (s2 * s2) / (s1 - s2) for k, (s1, s2) in steps.items()}
    if not hyp1 or any(not (re_q[k][0] > re_q[k][1] > re_q[k][2] > re_q[k][3]) for k in steps):
        stop("the quartet's real part does not fall at every step")
    a(f"- **The quartet.** From {fe(min(steps, key=float))} to {fe(max(steps, key=float))} its real part falls at every step "
      f"from `N = 24` to 48, its step from 40 to 48 {min(ratio):.3f} to {max(ratio):.3f} of its step from 32 to 40. On that "
      'ratio its limit would '
      'be about ' + ', '.join(f'{lim[k]:.4f} at {fe(k)}' for k in sorted(lim, key=float)) + ' (INFERRED: three cutoffs '
      'cannot show the rate).')
    zs = {N: collision(d1, N) for N in grid.LADDER}
    zs[48] = collision(t48, 48)
    zz = [zs[N]['zero'] for N in (32, 40, 48)]
    aitken = zz[2] - (zz[2] - zz[1]) ** 2 / ((zz[2] - zz[1]) - (zz[1] - zz[0]))
    a('- **The change of type.** By the records it lies ' + '; '.join(
        f"between {fe(z['below'])}, {z['below_type']}, and {fe(z['first'])} at `N = {N}`" for N, z in zs.items())
      + '. On the collision law, the real part squared linear in `ε` over the Hyperbolic points above 64, it sits at '
      + ', '.join(f"{z['zero']:.3f} at `N = {N}`" for N, z in zs.items())
      + f', with a limit of about {aitken:.2f} on the last three (INFERRED; the rate is not shown).')
    a('')

    # --- 7. stated before the reads -----------------------------------------------------------------------------------
    a('## 7. Stated before the reads, and what they found')
    a('')
    a('Each statement was made before any value it concerns was read, from known outcomes, all INFERRED and none a '
      'classification: `run/DESIGN.md` section 6 before the first ladder, `run/TOP48.md` section 5 before the second. Each '
      'stands as stated.')
    a('')
    a('| Where | Stated | Found | |')
    a('|---|---|---|---|')
    tw = f'{kept} of 12'
    q40 = {e: re_q[lib.key(e)][2] for e in (128, 132)}
    a(f"| `DESIGN.md` § 6 | The twelve keep their stored type and indices at `N = 40` | {tw} | {'held' if kept == 12 else 'missed'} |")
    a('| `DESIGN.md` § 6 | The quartet\'s real part at `N = 40`: 0.035 to 0.053 at 128, 0.116 to 0.136 at 132 | '
      f"{q40[128]:.4f} and {q40[132]:.4f}, above every law | "
      f"{'missed' if not any(LAWS40[e][0] <= q40[e] <= LAWS40[e][1] for e in q40) else 'held'} |")
    off128 = re_q[lib.key(128)][2] is not None
    a(f"| `DESIGN.md` § 6 | 132 off the axis at `N = 40`, 128 too close to call | 132 off the axis, and 128 off it too | "
      f"{'held' if re_q[lib.key(132)][2] is not None else 'missed'}{', 128 called' if off128 else ''} |")
    a(f"| `DESIGN.md` § 6 | The collision near 127 at `N = 40`, with a limit of 127.5 to 128 | between {fe(zs[40]['below'])} "
      f"and {fe(zs[40]['first'])}; {zs[40]['zero']:.2f} on the collision law (INFERRED) | missed |")
    k4 = {N: [fe(k) for k in sorted(d1['cutoffs'][str(N)]['points'], key=float)
              if d1['cutoffs'][str(N)]['points'][k]['record']['type'] == 'Elliptic' and d1['cutoffs'][str(N)]['points'][k]['record']['K'] == 4]
          for N in grid.LADDER}
    a('| `DESIGN.md` § 6 | An Elliptic stretch with `K` = 4 before the quartet | '
      + '; '.join(f"at {', '.join(v)} at `N = {N}`" for N, v in k4.items()) + f" | {'held' if all(k4.values()) else 'missed'} |")
    o11 = open(os.path.join(ROOT, 'dev', 'runs', '011_row_readings', 'row_readings.out'), encoding='utf-8').read()
    if ("a new link at N = 40 alone: 1 [('T5J_R2', 0.353553390593, False)]; at a stored point: 0" not in o11
            or 'a new link at N = 40 alone at a stored point of the rows: 0' not in o11):
        stop('dev/runs/011_row_readings/ does not give one new link at `N = 40` alone, at no stored point')
    a('| `DESIGN.md` § 6 | No new link at `N = 40` alone at a stored point of the rows | none at a stored point; the one '
      "new link at `N = 40` alone is T5's second member's at 0.354, which no record holds (`dev/runs/011_row_readings/`) | held |")
    v48 = {e: re_q[lib.key(e)][3] for e in LAWS48}
    a(f"| `TOP48.md` § 5 | The design's laws at `N = 48`, as pinned: 0.0288, −0.0015 and 0.0420 at 128, 0.1159, 0.0925 and "
      f"0.1311 at 132 | {v48[128]:.4f} and {v48[132]:.4f} | missed again, as stated |")
    a(f"| `TOP48.md` § 5 | The same laws on `N = 24`, 32 and 40: the real part at 48, "
      + '; '.join(f'{lo_:.4f} to {hi_:.4f} at {e}' for e, (lo_, hi_) in LAWS48.items()) + ' | '
      + ', '.join(f'{v48[e]:.4f}' for e in LAWS48)
      + f" | {'missed, each below its range' if all(v48[e] < LAWS48[e][0] for e in LAWS48) else 'mixed'} |")
    st48 = [s2 for s1, s2 in steps.values()]
    a(f"| `TOP48.md` § 5 | The real part's step from 40 to 48, about 1×10⁻⁴ to 7×10⁻⁴ | {sci(min(st48))} to {sci(max(st48))} | "
      'missed |')
    a(f"| `TOP48.md` § 5 | The collision at 125.98 at `N = 48` | between {fe(zs[48]['below'])} and {fe(zs[48]['first'])} by the "
      f"records; {zs[48]['zero']:.2f} on the collision law (INFERRED) | missed |")
    r126 = point_rec(t48, lib.key(126), 48, False)
    a('| `TOP48.md` § 5 | The types at `N = 48`: Elliptic (9, 3, 6) at 116 and 120, Elliptic (4, 0, 4) at 124, Hyperbolic '
      f'(4, 0, 4) from 126, 126 too close to call | as stated, but at 126, {r126} | held but at 126 |')
    i48 = [t48['identity'][k]['40-48']['aligned_distance'] for k in top_ks]
    lost = [k for k in top_ks if not t48['identity'][k]['40-48']['kept']]
    if lost != [lib.key(126)] or t48['identity'][lost[0]]['40-48']['same_record']:
        stop('branch identity at (40, 48) fails otherwise than at 126 by its change of type')
    a(f"| `TOP48.md` § 5 | Branch identity at (40, 48), 5×10⁻⁴ to 9×10⁻⁴ | {sci(min(i48))} to {sci(max(i48))}, kept but at 126, "
      'where the records differ | missed, under the range |')
    tol = tolerances48(t48, top_ks)
    a(f"| `TOP48.md` § 5 | The tolerances at `N = 48`: no gap between τ(40) and τ(48); A's smallest eigenvalue outside the "
      "cluster at least 200 times its gray zone's top; L's gray zone at least 10⁷ times clear; nothing in n(D)'s inherited "
      f"zone | {'no gap' if not tol['links'] else 'gaps at ' + ', '.join(fe(k) for k, _ in tol['links'])}; at least "
      f"{tol['a0']:.0f} times; " + (f"at least {sci(tol['l'])} times" if tol['l'] else 'no genuine eigenvalue of L recorded')
      + f"; {'nothing' if not tol['flags'] else 'a flag at ' + ', '.join(fe(k) for k in tol['flags'])}, from each point's "
      f"records at 40 and 48 | {'held' if not tol['links'] and tol['a0'] >= 200 and (tol['l'] or 0) >= 1e7 and not tol['flags'] else 'missed'} |")
    moved48 = [k for k in top_ks if point_rec(t48, k, 48, False) != point_rec(t48, k, 40, False)]
    if moved48 != lost:
        stop('the records at 48 change type or indices otherwise than where branch identity fails')
    a("| `TOP48.md` § 5 | The branch: T5's path at `N = 48` reaches 132 on the branch it holds at 32 and 40 | branch identity "
      f"at (40, 48) kept at every point but {listed(fe(k) for k in lost)}, where the record's type changes from `N = 40`'s | "
      f"held but at {listed(fe(k) for k in lost)} |")
    a('')

    # --- 8. what stays open -------------------------------------------------------------------------------------------
    a('## 8. What stays open')
    a('')
    a('Each with its values at every cutoff in the tables above, and its cause.')
    a('')
    a(f"- **T4's change of type in `R4`,** between 4 and 5.66: not located, the stop in § 5.")
    for t in ('T5_R2', 'T5J_R2'):
        d = rows[t]
        ks = [k for k in sorted(d['both'], key=float) if not (d['both'][k]['as_built']['classified'] and d['both'][k]['changed']['classified'])]
        if t == 'T5_R2':
            ks = [k for k in ks if k not in tg]
        one = [k for k in ks if d['both'][k]['changed']['classified']]
        if ks:
            a(f"- **{NAME[t]} at {listed(fe(k) for k in ks)}** on the first ladder (§ 4)"
              + (f", {listed(fe(k) for k in one)} as built alone." if one else '.'))
    a(f"- **T5's top, {fe(min(tg, key=float))} to {fe(max(tg, key=float))}:** not classified on the first ladder (§ 4), nor on "
      'the second, where the controls at ' + ' and '.join(fe(k) for k in misses) + ' are not classified (§ 6).')
    a('- **Why the steps at ' + ' and '.join(fe(k) for k in misses) + ' stop shrinking** on the second ladder: OPEN.')
    a('')

    # --- 9. deviations and looks --------------------------------------------------------------------------------------
    a('## 9. Deviations, and looks beyond the terms')
    a('')
    a('- **None in the runs.** Each stage ran from its pinned tree, in its terms\' order, and every job completed once.')
    a("- **Looks beyond the terms.** Between the two pins at `N = 48`, `run/TOP48.md` allows checks on each seed's check "
      "and each point's acceptance alone. `dev/runs/015_solve_checks_48/` also sets each point's reached amplitude against its "
      "record at `N = 40`, deciding nothing, and says so. After the reads, beyond the terms and deciding nothing: the "
      "quartet's limit on the ratio of its last two steps (§ 6), and the zero of L's sign-changing eigenvalue with K1's "
      'neighbourhood around it (§ 5), each INFERRED.')
    a('- **The statements in § 7** stand as stated, and their misses are kept.')
    a('')

    # --- 10. reproduction ---------------------------------------------------------------------------------------------
    a('## 10. Reproduction')
    a('')
    a('From a copy of this folder whose `run/out/` also holds the bench\'s read and reading files:')
    a('- `shasum -a 256 -c SHA256SUMS`, and the manifest against `run/MANIFEST_PIN`;')
    a('- `python3 -I -B tools/build_record.py MIT_REPO --check`, which rebuilds this record from the files and the '
      "repository's history, recomputes each point's classification, and reports any difference;")
    a('- `dev/runs/011_row_readings/`, `dev/runs/013_locator_reading/` and `dev/runs/015_solve_checks_48/`, each read from the '
      'same files.')
    a('')
    a('Bitwise agreement on another machine is not claimed: this run\'s own comparisons are bit for bit on the machine in § 1, '
      'and elsewhere they agree to round-off (`DEVLOG.md`, entry 17).')
    text = '\n'.join(L) + '\n'
    if '\u2014' in text or '\u2013' in text:
        stop('a dash in the record')
    path = os.path.join(ROOT, 'RECORD.md')
    if check:
        have = open(path, encoding='utf-8').read() if os.path.exists(path) else None
        if have != text:
            print('RECORD.md differs from the build')
            sys.exit(1)
        print('RECORD.md matches the build')
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'wrote RECORD.md: {len(L)} lines, {n_re} classifications recomputed, {nfiles} logged files matched')


if __name__ == '__main__':
    main()
