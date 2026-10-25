#!/usr/bin/env python3
"""Post-run: made after M8.16.1's registered run. It builds RECORD.md from the run's files, so that every number and
hash in the record is read from the bytes it names. It is M8.16's tools/build_record.py, carried to M8.16.1's cases
and checks: the next-order bar, the C3 ray, the rows and T5's second member.

Usage, from this folder: python3 -I -B tools/build_record.py MIT_REPO [--check]
  MIT_REPO: a clone of mode-identity-theory whose HEAD holds this folder's frozen commit. The instrument's commit is
            read there as the last one that wrote run/MANIFEST_PIN, and the calibration's fitted range from M8.16's
            terms at that commit.
  --check:  build the record and compare it with RECORD.md, without writing; exit 1 on any difference.

It refuses if an output differs from the SHA-256 the run's log recorded, if the freeze does not validate, or if a
reading differs from the one the record states."""
import datetime
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
import checks as ck  # noqa: E402
from instrument import devtools, linear as ln  # noqa: E402

FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16-1'
M816 = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
OUT = os.path.join(ROOT, 'run', 'out')
OW = 'https://github.com/openwave-labs/openwave'
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
NS = ('16', '24', '32')
EPS4 = (0.25, 0.5, 1.0, 2.0)
CONTROLS = ('C2a', 'C2b', 'C3', 'C2a/R5')
SAMPLES = ('T1/R4', 'T1/R5', 'T4/R4', 'T4/R5')
LADDERS = ('T2/R4', 'T2/R5', 'T3/R4', 'T3/R5', 'T5/R2')
MEMBER, RAY = 'T5J/R2', 'C3R/R4'
BAR_CASES = ('P5', RAY) + SAMPLES + (MEMBER,) + LADDERS
POSTRUN = ('environment_postrun_2026-10-25.txt', 'tools/build_record.py')


def stop(m):
    raise SystemExit(f'STOPPED: {m}')


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def J(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def p10(x):
    """The smallest power of ten above x, written 10ⁿ: a bound for a quantity at the round-off level."""
    if x <= 0:
        return '0'
    k = math.floor(math.log10(x)) + 1
    return f'10{str(k).translate(SUP)}'


def sci(x, d=2):
    """x in d significant figures, as a×10ⁿ."""
    if x == 0:
        return '0'
    k = math.floor(math.log10(abs(x)))
    a = round(x / 10 ** k, d - 1)
    if abs(a) >= 10:
        a, k = a / 10, k + 1
    return f'{a:.{d - 1}f}×10{str(k).translate(SUP)}'


def up1(x):
    """x rounded up to one significant figure: a bound."""
    k = math.floor(math.log10(x))
    v = math.ceil(x / 10 ** k - 1e-12) * 10 ** k
    return f'{v:.{max(0, -k)}f}'


def upsci(x):
    """x rounded up to one significant figure, as a×10ⁿ: a bound."""
    k = math.floor(math.log10(x))
    a = math.ceil(x / 10 ** k - 1e-12)
    if a == 10:
        a, k = 1, k + 1
    return f'{a}×10{str(k).translate(SUP)}'


def pct(x, d=2):
    return f'{100 * x:.{d}f}%'


def bnd(x, up, sig=3):
    """x in sig significant figures, rounded outward for a stated bound: up for 'at most', down for 'at least';
    as a decimal between 10⁻³ and 10⁴, otherwise as a×10ⁿ."""
    k = math.floor(math.log10(abs(x))) - sig + 1
    v = (math.ceil if up else math.floor)(x / 10 ** k * (1 - 1e-12 if up else 1 + 1e-12)) * 10 ** k
    if 1e-3 <= abs(v) < 1e4:
        return f'{v:.{max(0, -k)}f}'
    e = math.floor(math.log10(abs(v)))
    return f'{v / 10 ** e:.{sig - 1}f}×10{str(e).translate(SUP)}'


def cz(v):
    """A complex value as the files store it: a pair, [re, im], of numbers or decimal strings."""
    return complex(float(v[0]), float(v[1])) if isinstance(v, (list, tuple)) else complex(v)


def sg(x, d=6):
    """x signed, in d significant figures, with the minus sign the terms use."""
    return ('+' if x >= 0 else '−') + f'{abs(x):.{d}g}'


def ratio_text(z):
    """c_g/(κs_g) as the terms' table writes it: real for a real or imaginary group, complex for a quartet."""
    if abs(z.imag) <= 1e-9 * max(1.0, abs(z.real)):
        return sg(z.real)
    return f"{sg(z.real)} {'+' if z.imag >= 0 else '−'} {abs(z.imag):.6g} i"


def ef(e):
    return f'{e:.3g}'


def g2(x):
    """A ratio in two significant figures; below 10⁻³, as a×10ⁿ."""
    if x == 0:
        return '0'
    return sci(x) if x < 1e-3 else f'{x:#.2g}'.rstrip('.')


def main():
    if len(sys.argv) < 2:
        stop(__doc__)
    repo, check = sys.argv[1], '--check' in sys.argv[2:]

    def git(*a):
        return subprocess.run(['git', '-C', repo, *a], check=True, capture_output=True, text=True).stdout

    instr = git('log', '-1', '--format=%H', 'HEAD', '--', f'{FOLDER}/run/MANIFEST_PIN').strip()
    if not instr:
        stop('no commit in MIT_REPO wrote run/MANIFEST_PIN')

    # custody
    log, gate, verdict = J(os.path.join(OUT, 'RUNLOG.json')), J(os.path.join(OUT, 'GATE.json')), J(os.path.join(OUT, 'VERDICT.json'))
    files = {f: h for rec in log['completed'].values() for f, h in rec['files'].items()}
    for f, h in files.items():
        if sha(os.path.join(OUT, f)) != h:
            stop(f'run/out/{f} differs from the SHA-256 the run log recorded')
    for k in ('gate', 'verdict', 'transcript'):
        if sha(os.path.join(OUT, log[k]['file'])) != log[k]['sha256']:
            stop(f"run/out/{log[k]['file']} differs from the SHA-256 the run log recorded")
    F = devtools.frozen(ROOT)
    mpin = open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8').read().strip()
    fpin = open(os.path.join(ROOT, 'run', 'FROZEN_PIN'), encoding='utf-8').read().strip()
    if log['manifest_sha256'] != mpin or F['manifest_sha256'] != mpin:
        stop('the run log or the freeze does not record the manifest pin')
    terms = sha(os.path.join(ROOT, 'run', 'm8_16_task_details.md'))
    if terms != F['terms_sha256']:
        stop('the terms in run/ differ from the SHA-256 the freeze records')
    with open(os.path.join(OUT, 'driver.log'), 'rb') as a, open(os.path.join(OUT, 'driver.out'), 'rb') as b:
        if a.read() != b.read():
            stop('run/out/driver.log differs from run/out/driver.out')
    env = open(os.path.join(ROOT, POSTRUN[0]), encoding='utf-8').read()
    if not env.rstrip().endswith('differences: none'):
        stop('the post-run environment differs from run/ENVIRONMENT.json')
    E = J(os.path.join(ROOT, 'run', 'ENVIRONMENT.json'))
    envtext = (f"Python {E['interpreter']['version']}, NumPy {E['numpy']['version']} and SciPy {E['scipy']['version']}, on "
               f"Accelerate's BLAS and LAPACK as each reports them, under {E['os']['product']} {E['os']['version']} "
               f"({E['os']['build']}) on one {E['machine']['cpu']}")
    if not (E['numpy']['blas']['name'] == E['numpy']['lapack']['name'] == 'accelerate'):
        stop('the recorded BLAS is not Accelerate')
    t0, t1 = log['events'][0]['t'], log['verdict']['written']
    wall = (datetime.datetime.fromisoformat(t1.replace('Z', '+00:00'))
            - datetime.datetime.fromisoformat(t0.replace('Z', '+00:00'))).total_seconds()
    order = re.search(r"cases \[(.*)\]", log['events'][0]['event']).group(1).replace("'", '').split(', ')
    ran = list(log['completed'])
    if not (ran == order == F['order'] and len(ran) == 17):
        stop(f'the run ran {ran}')
    seconds_total = int(re.search(r'; (\d+) s$', open(os.path.join(OUT, 'driver.log'), encoding='utf-8').read().strip()).group(1))
    rows_all = SAMPLES + LADDERS
    if not (verdict['verdict'] == 'QUALIFIED' and verdict['instrument'] and verdict['k3'] == 'resolved'
            and verdict['r5_gate'] and not verdict['failing'] and not verdict['failed']
            and verdict['rows'] == {n: True for n in rows_all} and verdict['members'] == {MEMBER: False}
            and verdict['c3_ray'] == {RAY: 'passed'} and verdict['qualified'] == list(rows_all)):
        stop(f'the verdict is {verdict}')
    if not (gate['stop'] is None and gate['complete'] and gate['instrument_ok'] and gate['r5_gate'] and not gate['absent']):
        stop(f'the gate record is {gate}')

    R = {n: J(os.path.join(OUT, n.replace('/', '_') + '.json')) for n in order}
    sec = {n: round(R[n]['seconds']) for n in order}

    # the calibration's fitted range (M8.16's terms, § STATED LIMITS, which M8.16.1's carry)
    tt = open(os.path.join(ROOT, 'run', 'm8_16_task_details.md'), encoding='utf-8').read()
    tt16 = git('show', f'{instr}:{M816}/run/m8_16_task_details.md')
    FIT = ('in `R2`, `R3` and `R4`, with `m` from 0.204 to 132 and `N` from 16 to 40. Outside that range it is an '
           'extrapolation, flagged in the record wherever it applies. `R5` lies outside the slots it was fitted on.')
    if FIT not in tt16:
        stop("M8.16's terms do not state the calibration range as this record reads it")
    fit_slots, m_lo, m_hi = ('R2', 'R3', 'R4'), 0.204, 132.0

    def mval(p):
        """A point's m = ‖φ‖², as the run recorded it; at C1, which records none, read from its margin, as M8.16's
        record read every point."""
        if 'm' in p:
            return p['m']
        return (p['record']['margin'] / ln.KAPPA) ** 2 / (ln.U * p['record']['normA'])
    m_pts = {n: [(N, float(e), mval(p)) for N, cut in R[n]['cutoffs'].items() for e, p in cut['points'].items()
                 if 'record' in p] for n in order}
    m_all = [x for v in m_pts.values() for _, _, x in v]
    low = {n: sorted({e for _, e, x in v if x < m_lo}) for n, v in m_pts.items()}
    low = {n: v for n, v in low.items() if v}
    if any(x > m_hi for x in m_all):
        stop('a point lies above the fitted range of m: the record must flag it')
    low_min = {n: min(x for _, e, x in m_pts[n] if x < m_lo) for n in low}
    outside_slot = [n for n in order if R[n]['case']['slot'] not in fit_slots]
    # the margin's headroom (M8.16's terms, § STATED LIMITS): the cluster coefficient κ cluster/margin against the controls'
    # largest, and the cluster against its gray zone's lower edge, margin/G; with L's kernel against its cut
    COEF_FIT = 0.0568
    if ('their largest cluster coefficient, 0.0568 over 169 points' not in tt16
            or 'The ten-fold headroom holds on the controls' not in tt16):
        stop("M8.16's terms do not state the margin's fit and headroom as this record reads them")
    hd, gap_min, lift_max, gen_min = [], math.inf, 0.0, math.inf
    for n in order:
        for N, cut in R[n]['cutoffs'].items():
            for e, p in cut['points'].items():
                if 'record' not in p:
                    continue
                r = p['record']
                if not r['separated'] or r['gray_count']:
                    stop(f'{n} at N = {N}, eps = {e}: the cluster is not separated, or its gray zone is occupied')
                head = r['margin'] / (ln.GRAY * r['cluster_max']) if r['cluster_max'] > 0 else math.inf
                hd.append((n, N, float(e), ln.KAPPA * r['cluster_max'] / r['margin'], head))
                if r.get('outside_min') is not None:
                    gap_min = min(gap_min, r['outside_min'] / (ln.GRAY * r['margin']))
                if isinstance(p.get('lkernel'), dict):
                    lift_max = max(lift_max, p['lkernel']['lift'] / ln.U)
                    gen_min = min(gen_min, p['lkernel']['genuine'] / ln.U)
    over = [x for x in hd if x[3] > COEF_FIT]
    under = [x for x in hd if x[4] < 10]
    over_cases = sorted({x[0] for x in over}, key=order.index)
    under_cases = sorted({x[0] for x in under}, key=order.index)
    worst = min(under, key=lambda x: x[4])
    scored_under = sorted({x[0] for x in under if any(abs(x[2] - e) < 1e-9 for e in ck.NEXT_EPS)}, key=order.index)
    if not (gap_min >= 10 and lift_max * 10 <= ln.L_CUT / ln.U and gen_min >= 10 * ln.G_L * ln.L_CUT / ln.U):
        stop('the spectrum outside the cluster, or L\'s kernel, does not read as recorded here')

    # the launch, the freeze block and the power: DEVLOG's entries, by heading
    dl = open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8').read()
    heads = [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^## (\d+)\. (.*)$', dl, re.M)]

    def entry(k):
        return re.search(rf'^## {k}\. .*?(?=^## {k + 1}\. |\Z)', dl, re.S | re.M).group(0)
    n_launch = [k for k, h in heads if h.split(': ', 1)[1].startswith("the registered run, launched on Blake's go")]
    n_open = [k for k, h in heads if "#652, the freeze block's pull request, opened by Blake" in h]
    n_end = [k for k, h in heads if h.split(': ', 1)[1].startswith('the registered run: QUALIFIED')]
    if not (len(n_launch) == len(n_open) == len(n_end) == 1):
        stop('no single launch, freeze-block or closing entry in DEVLOG.md')
    e_launch, e_open, e_end = entry(n_launch[0]), entry(n_open[0]), entry(n_end[0])
    pw = re.search(r"\*\*The power,\*\* read at (\S+): \"Now drawing from 'AC Power'\"", e_launch)
    if not pw or 'through `tee`' not in e_launch:
        stop('the launch entry does not record mains power and the command as this record states them')
    power_read = pw.group(1)
    opened = re.search(r'\(\[#652\]\([^)]*\), opened (\S+)\):', e_open)
    merged = re.search(r'#652, was approved and merged by the maintainer at (\S+), during the run', e_end)
    if not (opened and merged and opened.group(1) < t0):
        stop('the freeze block was not open before the run, as the entries record it')

    # the seed check's bytes, which the approval of #652's reading note leaves to the log
    e19 = [k for k, _ in heads if '`dev/runs/011_*`' in entry(k)]
    e23 = [k for k, _ in heads if '`dev/runs/014_*`' in entry(k)]
    sc = sha(os.path.join(ROOT, 'dev', 'seed_check.json'))
    if not (len(e19) == len(e23) == 1 and sc == sha(os.path.join(ROOT, 'dev', 'runs', '011_seed_check.json'))
            == sha(os.path.join(ROOT, 'dev', 'runs', '014_seed_check.json'))):
        stop("dev/seed_check.json is not the record kept from the seed check's runs")
    seeds_23 = re.findall(r'`run/seeds\.py` `([0-9a-f]{64})`', entry(e23[0]))
    if not seeds_23 or sha(os.path.join(ROOT, 'run', 'seeds.py')) != seeds_23[-1]:
        stop('run/seeds.py differs from the SHA-256 entry 23 records after its changes')
    inst_files = sorted(f for f in os.listdir(os.path.join(ROOT, 'instrument')) if f.endswith('.py'))
    for f in inst_files:
        theirs = subprocess.run(['git', '-C', repo, 'show', f'{instr}:{M816}/instrument/{f}'], check=True,
                                capture_output=True).stdout
        if hashlib.sha256(theirs).hexdigest() != sha(os.path.join(ROOT, 'instrument', f)):
            stop(f"instrument/{f} differs from M8.16's")

    # the seeds
    seed_q, seed_c, seeds = 0.0, 0.0, 0
    for n in order:
        qx = ck.num(R[n]['case']['Q'])
        for cut in R[n]['cutoffs'].values():
            s = cut['seed']
            if not s['ok'] or (s['k'], s['r']) != (R[n]['case']['k'], R[n]['case']['r']):
                stop(f'{n}: a seed failed, or its (k, r_u) is not the frozen case\'s')
            seeds += 1
            seed_q, seed_c = max(seed_q, abs(s['Q'] - qx) / qx), max(seed_c, s['crit'])

    # C1
    c1 = R['C1']
    c1pts = [p for cut in c1['cutoffs'].values() for p in cut['points'].values()]
    if not all(p['accepted'] and p['d6_ok'] and p['record']['type'] == 'Elliptic' and
               [p['record'][x] for x in ('nL', 'nD', 'K')] == [0, 0, 0] and p['record']['v0_matches'] for p in c1pts):
        stop('C1 does not read as recorded here')
    c1_res = max(p['residual_rel'] for p in c1pts)
    c1_off = max(p['off_level'] for p in c1pts)
    c1_low = max(max(p['lowest_errors']) for p in c1pts)

    def bounds(n):
        pts = [p for cut in R[n]['cutoffs'].values() for p in cut['points'].values() if 'record' in p]
        eps_all = [p['eps'] for p in R[n]['case']['points']]
        rds = [R[n]['readings'][ck.key(e)] for e in eps_all if ck.key(e) in R[n]['readings']]
        return dict(floor=max(p['floor_rel'] for p in pts),
                    tangent=max(p['kernel']['tangent'] for p in pts) / ln.U,
                    cluster=max(p['record']['cluster_max'] / p['record']['margin'] for p in pts),
                    rel=max(r['rel_change_max'] for r in rds),
                    rel_over=[e for e in eps_all if not R[n]['readings'][ck.key(e)]['rel_change_ok']],
                    npts=len(pts))

    def point_rows(n):
        """One row per ε of the case's four points: the type and indices at every cutoff, or the rule's Unresolved;
        the largest deviation from leading order at each cutoff; the reading; the aligned distance."""
        case, out = R[n]['case'], []
        for e in EPS4:
            types, devs = set(), []
            for N in NS:
                p = R[n]['cutoffs'][N]['points'][ck.key(e)]
                if not (p['accepted'] and ck.k1(p, case)):
                    stop(f'{n} at N = {N}, eps = {e}: not accepted, or K1 fails')
                r = p['record']
                types.add(f"{r['type']}; ({r['nL']}, {r['nD']}, {r['K']})")
                devs.append(ck.leading(p, case, e)[1])
            rd, idn = R[n]['readings'][ck.key(e)], R[n]['identity'][ck.key(e)]
            if len(types) != 1 or not idn['kept']:
                stop(f'{n} at eps = {e}: not one record type, or the identity not kept')
            t = types.pop()
            if rd['verdict'] == 'converged':
                if rd['type'] != t.split(';')[0]:
                    stop(f'{n} at eps = {e}: the rule reads another type')
                cell, conv = t, 'converged'
            else:
                cell, conv = 'not labelled', rd['verdict']
            out.append(f"| {n} | `{case['slot']}` | {e:g} | {cell} | {', '.join(pct(d) for d in devs)} | {conv} | "
                       f"{sci(idn['aligned_distance'])} |")
        return out

    # the controls
    table = [r for n in CONTROLS for r in point_rows(n)]
    ctl_lines = []
    for n in CONTROLS:
        g, b = gate['cases'][n], bounds(n)
        if not (g['K1'] and g['K4'] and g['converged'] and g['bar'] and g['trend'] and g.get('K2', True)):
            stop(f'{n} does not read as recorded here')
        k2 = f", K2 {'passes' if g.get('K2') else 'fails'}" if 'K2' in g else ''
        d = g['deviations']
        ctl_lines.append(
            f"- **{n}** (`{R[n]['case']['slot']}`, {sec[n]} s): K1 passes{k2}, and K4 passes. The largest deviation from "
            f"leading order is {', '.join(pct(d[N][0]) for N in NS)} at `ε = 0.25` and "
            f"{', '.join(pct(d[N][1]) for N in NS)} at `ε = 2`, at `N = 16, 24` and 32. "
            f"Every floor is below {p10(b['floor'])}, every tangent residual below {up1(b['tangent'])} u, and every "
            f"zero cluster below {up1(b['cluster'])} of its margin. Beside the rule, unscored, the largest relative change "
            f"between the two highest cutoffs is at most {upsci(b['rel'])}"
            + (", within the retired fraction `10⁻⁶`." if not b['rel_over'] else ", above the retired fraction `10⁻⁶` at `ε = "
               + ', '.join(f'{e:g}' for e in b['rel_over']) + '`.')
            + (f" Its margin is an extrapolation: `{R[n]['case']['slot']}` lies outside the slots the calibration was fitted on "
               f"(M8.16's terms, § STATED LIMITS)." if n in outside_slot else ''))

    # the next-order bar, every group at every cutoff
    def groups_of(n):
        case = R[n]['case']
        top = [g for g in case['next_order']['32']]
        return [(gi, g) for gi, g in enumerate(top) if g['under_bar']]

    def label(n, gi):
        g = R[n]['case']['next_order']['32'][gi]
        kr = {'+': ', Krein-positive', '-': ', Krein-negative'}.get(g['krein'], '')
        mult = ', double' if g['mult'] == 2 else ''
        return {'complex': 'quartet', 'imag': 'imaginary pair', 'real': 'real pair'}[g['cls']] + kr + mult

    def gratio(n, gi, N):
        g = R[n]['case']['next_order'][N][gi]
        return cz(g['c_g']) / cz(g['kappa_s'])

    bar_tables, bar_counts = {}, {}
    for n in BAR_CASES:
        nb = R[n]['checks']['next_order']
        gs = groups_of(n)
        if sorted(int(k) for k in nb) != [gi for gi, _ in gs]:
            stop(f'{n}: the bar read groups other than the frozen ones')
        rows, reads = [], []
        for k, (gi, g) in enumerate(gs, 1):
            r = nb[str(gi)]
            reads.append(r['reading'])
            for N in NS:
                x = r['per_N'][N]
                ks = cz(R[n]['case']['next_order'][N][gi]['kappa_s'])
                ceil = g2(x['ceiling'] / abs(ks))
                if x['c1'] and x['c2'] and x['c3'] is not None:
                    cg, c3h = cz(x['c_g']), cz(x['c3hat'])
                    tol = max(x['spread'], ck.FLOOR * x['ceiling'])
                    vals = '; '.join(ratio_text(v / ks) for v in (cg, cz(x['c2hat']), c3h))
                    cell1 = 'holds'
                    cell2 = f"{g2(x['E_c'] / (ck.RESOLUTION * x['ceiling']))}, holds"
                    cell3 = f"{g2(x['spread'] / x['ceiling'])}, {'holds' if x['c3'] else 'fails'}"
                    cell4 = f"{g2(abs(cg - c3h) / tol)}, {'holds' if x['c4'] else 'fails'}"
                    two = pct(x['two_term'], 4 if x['two_term'] < 1e-4 else 2)
                    devs = ', '.join(pct(d) for d in x['deviation'])
                else:
                    vals = ratio_text(gratio(n, gi, N)) + '; not read'
                    cell1 = 'holds' if x['c1'] else 'fails at ' + ', '.join(
                        f"`ε = {w.split('eps = ')[1]}`" for w in x['why'] if w.startswith('check 1'))
                    cell2 = ('holds' if x['c2'] else 'fails') if x['c1'] else 'not read'
                    cell3 = cell4 = two = devs = 'not read'
                rows.append(f"| {k}: {label(n, gi)} | {N} | {vals} | {ceil} | {cell1} | {cell2} | {cell3} | {cell4} | {two} | "
                            f"{devs} | {r['reading'] if N == '16' else ''} |")
        bar_tables[n], bar_counts[n] = rows, reads
    # what the record states of the bar
    for n in BAR_CASES:
        if n == MEMBER:
            if bar_counts[n] != ['Unresolved'] * len(bar_counts[n]):
                stop('the member does not read as recorded here')
        elif bar_counts[n] != ['pass'] * len(bar_counts[n]):
            stop(f'{n}: a group does not pass')

    # the pyramid
    p5, case5 = R['P5'], R['P5']['case']
    g5 = gate['cases']['P5']
    k3 = g5['K3']
    NEG, QUA, POS = ('imag', -1), ('complex', None), ('imag', 1)
    p5rows, dev5, ptype = [], {}, {}
    for e in EPS4:
        types, cells = set(), {NEG: [], QUA: [], POS: []}
        for N in NS:
            p = p5['cutoffs'][N]['points'][ck.key(e)]
            if not (p['accepted'] and ck.k1(p, case5) and ck.k2(p, case5, e)):
                stop(f'P5 at N = {N}, eps = {e}: not accepted, or K1 or K2 fails')
            r = p['record']
            types.add(f"{r['type']}; ({r['nL']}, {r['nD']}, {r['K']})")
            for cls, sign, pr, c, dv in ck.leading(p, case5, e)[2]:
                cells[(cls, sign)].append(dv)
                dev5[(e, N, (cls, sign))] = dv
        rd, idn = p5['readings'][ck.key(e)], p5['identity'][ck.key(e)]
        if len(types) != 1 or rd['verdict'] != 'converged' or not idn['kept']:
            stop(f'P5 at eps = {e}: not one reading, not converged or identity not kept')
        ptype[e] = types.pop()
        p5rows.append(f"| {e:g} | {ptype[e]} | " + ' | '.join(', '.join(pct(v) for v in cells[k]) for k in (NEG, QUA, POS))
                      + f" | {sci(idn['aligned_distance'])} |")
    if not (g5['K1'] and g5['K2'] and g5['K4'] and g5['converged'] and g5['bar'] and g5['seeds'] and k3['outcome'] == 'resolved'):
        stop('the pyramid does not read as recorded here')
    # the known outcome, measured: this run's controls and pyramid against M8.16's record, at its commit as the terms cite it
    rec16s = set(re.findall(r'mode-identity-theory/blob/([0-9a-f]{40})/' + re.escape(M816) + r'/RECORD\.md', tt))
    if len(rec16s) != 1:
        stop("the terms do not cite M8.16's record at one commit")
    rec16 = rec16s.pop()
    log16 = json.loads(git('show', f'{rec16}:{M816}/run/out/RUNLOG.json'))
    h16 = {f: h for r_ in log16['completed'].values() for f, h in r_['files'].items()}
    repro = 0
    for n in ('C1',) + CONTROLS + ('P5',):
        f16 = n.replace('/', '_') + '.json'
        raw = subprocess.run(['git', '-C', repo, 'show', f'{rec16}:{M816}/run/out/{f16}'], check=True, capture_output=True).stdout
        if hashlib.sha256(raw).hexdigest() != h16.get(f16):
            stop(f"M8.16's {f16} differs from its run log")
        old16 = json.loads(raw)
        for N, cut in R[n]['cutoffs'].items():
            for e, p in cut['points'].items():
                if [g['c'] for g in p['groups']] != [g['c'] for g in old16['cutoffs'][N]['points'][e]['groups']]:
                    stop(f'{n} at N = {N}, eps = {e}: the group centres differ from M8.16\'s')
                repro += 1
    b5 = bounds('P5')
    k3rows = []
    for N in NS:
        v, p = k3['per_N'][N], p5['cutoffs'][N]['points'][ck.key(0.25)]
        kern = p['kernel']
        if not (v['a'] and v['b'] and v['c'] and v['d'] and ck.kernel_exact(p, case5)):
            stop(f'K3 at N = {N} does not read as recorded here')
        ov = v['overlaps']
        k3rows.append(f"| {N} | holds: tangent residual below {up1(kern['tangent'] / ln.U)} u, `L`'s zero count "
                      f"{kern['dimkerL']} = the chains, gray zone empty; the quartet and the Krein-positive pair pass the bar "
                      f"| holds: {pct(dev5[(0.25, N, NEG)])} | holds: {ov['xy']:.4f} and below {p10(ov['z'])}; axis "
                      f"fraction {ov['axis']:.3f} | holds |")
    k3a = k3['next_order']
    if [r['reading'] for r in k3a.values()] != ['pass'] * len(k3a):
        stop("K3(a)'s bar does not read as recorded here")
    drow = k3['d_row']
    nb5 = p5['checks']['next_order']
    p5bar = []
    for gi, g in groups_of('P5'):
        r = nb5[str(gi)]
        name = {'complex': 'the quartet', 'imag': 'the Krein-positive pair'}[g['cls']]
        sp = [r['per_N'][N]['spread'] / r['per_N'][N]['ceiling'] for N in NS]
        c4 = [abs(cz(r['per_N'][N]['c_g']) - cz(r['per_N'][N]['c3hat'])) / max(r['per_N'][N]['spread'], ck.FLOOR * r['per_N'][N]['ceiling']) for N in NS]
        tt2 = [r['per_N'][N]['two_term'] for N in NS]
        p5bar.append(f"| {name} | {ratio_text(gratio('P5', gi, '32'))} | {', '.join(g2(x) for x in sp)} | "
                     f"{', '.join(g2(x) for x in c4)} | {', '.join(pct(x, 4 if x < 1e-4 else 2) for x in tt2)} |")
    q = [dev5[(0.25, N, QUA)] for N in NS]

    # the C3 ray
    ray, case_r = R[RAY], R[RAY]['case']
    rc = ray['checks']
    if not (rc['K1'] and rc['K2'] and rc['bar'] and rc['discrimination'] and rc['outcome'] == 'passed'):
        stop('the ray does not read as recorded here')
    drows = rc['discrimination_rows']
    if not (drows and all(d['fails_check_4'] for d in drows)):
        stop("the ray's discrimination does not read as recorded here")
    disc = {}
    for d in drows:
        disc.setdefault(d['group'], {})[d['N']] = d['distance'] / d['tolerance']
    ray_disc = [f"| {k}: {label(RAY, gi)} | " + ', '.join(f'{disc[gi][N]:.0f}' for N in NS) + ' |'
                for k, (gi, _) in enumerate(groups_of(RAY), 1)]
    dmin = min(x for v in disc.values() for x in v.values())

    # the samples, the member and the ray, point by point
    ray_rows = point_rows(RAY)
    sample_rows = [r for n in SAMPLES + (MEMBER,) for r in point_rows(n)]

    def k5_line(n):
        c, case = R[n]['checks'], R[n]['case']
        k1s = all(ck.k1(R[n]['cutoffs'][N]['points'][ck.key(0.25)], case) for N in NS)
        conv = ck.converged(R[n], 0.25, case)
        ng = len(c['next_order'])
        if not (c['K5'] and c['bar'] and k1s and conv and ck.seeds_ok(R[n])):
            stop(f'{n}: K5 does not read as recorded here')
        return (f"- **{n}** (`{case['slot']}`, {sec[n]} s): K5 holds. Every seed is checked, K1 holds at `ε = 0.25` at "
                f"every cutoff, the point converges there, {case['type']} with `(n(L), n(D), K) = "
                f"({', '.join(str(i) for i in case['idx'])})` as expected, and its {ng} groups under the bar pass.")

    # the ladders
    lad = {}
    for n in LADDERS:
        c, case = R[n]['checks'], R[n]['case']
        if not (c['K5'] and c['K6'] and c['accepted'] and c['seeds'] and c['disagree'] == 0 and c['low_ok']):
            stop(f'{n}: K6 does not read as recorded here')
        rows, unres = [], []
        for x in c['rows']:
            mine, th = x['mine'], x['m815']
            here = f"{mine['type']}; {mine['K']}; {mine['ki']}" if x['status'] != 'unresolved' else 'not labelled'
            why = ''
            if x['status'] == 'unresolved':
                rs = sorted(set(x['reasons']))
                why = '; '.join(rs)
                unres.append(x['eps'])
            idn = x['identity'] or {}
            ad = sci(idn['aligned_distance']) if idn.get('aligned_distance') is not None else 'none'
            rows.append(f"| {ef(x['eps'])} | {here} | {th['type']}; {th['K']}; {th['ki']} | {x['status']} | {ad} | {why} |")
        unread = [p['eps'] for p in case['points'] if not p['read']]
        above = [x for x in c['rows'] if x['eps'] > 2 + 1e-12]
        lad[n] = dict(rows=rows, unres=unres, unread=unread, above=len(above), agree=c['agree_above_2'],
                      npts=len(case['points']), nread=len(c['rows']))
        if sum(x['status'] == 'agrees' for x in above) != c['agree_above_2'] or any(x['status'] == 'disagrees' for x in c['rows']):
            stop(f'{n}: K6 does not read as recorded here')

    # the measured margin behind check 1 (the approval of #650's reading note): T5/R2 at the point nearest ε = 1
    t5r, deps = R['T5/R2'], []
    for gi, r in t5r['checks']['next_order'].items():
        for N, x in r['per_N'].items():
            gN = t5r['case']['next_order'][N][int(gi)]
            e1, lam1 = x['x'][-1], x['lam'][-1]
            lamc = complex(*lam1) if isinstance(lam1, (list, tuple)) else complex(lam1)
            deps.append(abs(lamc - e1 * cz(gN['kappa_s']) - e1 ** 2 * cz(gN['c_g'])) / x['ceiling'])
    dep_max = max(deps)
    e44 = [k for k, _ in heads if 'at 4.5 each every group passes' in entry(k) and 'at 5.5 the two read fail' in entry(k)]
    if len(e44) != 1 or len(deps) != 9:
        stop("the log does not record the exchange's margin once, or T5/R2 does not read as recorded here")

    # the member
    mem, case_m = R[MEMBER], R[MEMBER]['case']
    cm = mem['checks']
    r25, r2 = mem['readings'][ck.key(0.25)], mem['readings'][ck.key(2.0)]
    why25, why2 = sorted(set(r25['reasons'])), sorted(set(r2['reasons']))
    m_ok = (not cm['K5'] and not cm['bar'] and r25['verdict'] == 'Unresolved' and len(why25) == 1 and len(why2) == 1
            and all(ck.k1(mem['cutoffs'][N]['points'][ck.key(0.25)], case_m) for N in NS)
            and all(mem['cutoffs'][N]['points'][ck.key(0.25)]['accepted'] for N in NS)
            and all(ck.mode_values(mem['cutoffs'][N]['points'][ck.key(0.25)], case_m, 0.25, g['spectrum_index'], int(N))[0]
                    for N in NS for _, g in groups_of(MEMBER))
            and not ck.converged(mem, 0.25, case_m) and ck.converged(mem, 0.5, case_m) and ck.converged(mem, 1.0, case_m)
            and all(w.startswith('check 1 at N = ') and w.endswith('eps = 0.25') for r in cm['next_order'].values() for w in r['why']))
    if not m_ok:
        stop('the member does not read as recorded here')
    slow_rel = max(x['rel_change'] for x in r25['rows'] if x.get('role') == 'tested')
    part25 = complex(why25[0].split('partner set at ')[1].split(' ')[0])
    # one reading at ε = 0.25, from the three cutoffs; each slow group's partner, the same set, read once per group
    prts = [x for x in r25['rows'] if x.get('role') == 'partner']
    tested = [x for x in r25['rows'] if x.get('role') == 'tested']
    prt = prts[0] if prts else None
    if not (prt and len(tested) == len(prts) == len(r25['reasons']) == 3
            and all((x['c'], x['d1'], x['d2'], x['floor']) == (prt['c'], prt['d1'], prt['d2'], prt['floor']) for x in prts)
            and prt['neg'] == 0 and prt['d2'] > prt['d1'] and prt['d2'] > prt['floor']):
        stop("the member's partner set does not read as recorded here")
    if '### Known outcomes' not in tt or '**The diagnosis at the rows,** reported, unscored.' not in tt:
        stop('the terms do not carry the sections this record cites')

    # the targets and the post-run files
    tgt = [(t['file'], t['sha256']) for t in F['targets']]
    for f, h in tgt:
        if sha(os.path.join(ROOT, f)) != h:
            stop(f'{f} differs from FROZEN.json')
    post = [(p, sha(os.path.join(ROOT, p))) for p in POSTRUN]
    run_files = [(f'run/out/{f}', h) for f, h in files.items()]
    run_files += [(f"run/out/{log['gate']['file']}", log['gate']['sha256']), (f"run/out/{log['verdict']['file']}", log['verdict']['sha256']),
                  (f"run/out/{log['transcript']['file']}", log['transcript']['sha256']),
                  ('run/out/driver.log', sha(os.path.join(OUT, 'driver.log'))), ('run/out/RUNLOG.json', sha(os.path.join(OUT, 'RUNLOG.json'))),
                  ('run/FROZEN.json', fpin)] + tgt

    # the order as run
    def summary(n):
        """The case's checks as the terms name them; K6's clauses (acceptance, the seeds, agreement through ε = 2) are
        K6's, and K4's are the controls' and the pyramid's, as M8.16's record listed them."""
        k = R[n]['checks']
        role = R[n]['case']['role']
        names = {'row': ('K5', 'bar', 'K6'), 'member': ('K5', 'bar'), 'ray': ('K1', 'K2', 'bar', 'discrimination')}.get(role)
        keys = [x for x, v in k.items() if isinstance(v, bool) and (names is None or x in names)]
        p = [x for x in keys if k[x]] + (['K3'] if n == 'P5' and k['K3']['outcome'] == 'resolved' else [])
        f = [x for x in keys if not k[x]]
        rs = bar_counts.get(n)
        under = (', '.join(f'{rs.count(x)} {x}' for x in sorted(set(rs)))) if rs else 'none'
        return f"| {n} | {role} | `{R[n]['case']['slot']}` | {', '.join(p) or 'none'} | {', '.join(f) or 'none'} | {under} | {sec[n]} |"

    T = []
    a = T.append
    a('# M8.16.1 run record')
    a('')
    a(f"The record of M8.16.1's registered run on {t0[:10]}, under the governing terms, `run/m8_16_task_details.md` (SHA-256 "
      f"`{terms[:16]}…`), merged in OpenWave [#650]({OW}/pull/650), and the instrument frozen at MIT `{instr[:7]}` with its "
      f"manifest pin, `{mpin[:16]}…`. The maintainer's go is [#650's comment]({F['go']}), and the freeze block is OpenWave's "
      f"`research/m8_16_1/freeze_block.md`, merged in [#652]({OW}/pull/652). Every number below is read from the run's files "
      f"in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them. The case files hold every "
      f"point's full readings at every cutoff. This record gives each point's type and indices, or the convergence rule's "
      f"Unresolved; each case's deviations from leading order; every group's next-order reading at every cutoff (§ 11); and "
      f"every check. The verdict is the one the driver wrote under the terms' verdict rule. Adjudication is the maintainers'.")
    a('')
    a(f"**The outcome.** QUALIFIED. The instrument qualifies: the five controls passed every check, and the pyramid passed "
      f"K1 to K4, with K3 resolved. Its quartet lies {pct(q[0])}, {pct(q[1])} and {pct(q[2])} from Theorem R's leading "
      f"order at `ε = 0.25`, at `N = 16, 24` and 32, as M8.16 read it, and passes the next-order bar at every cutoff. All "
      f"nine rows qualify: {', '.join(rows_all)}. T5's second member, {MEMBER}, is not qualified: its three groups read "
      f"Unresolved by check 1 at `ε = 0.25`, where the convergence rule reads the point Unresolved (§ 6). The C3 ray passed, "
      f"its discrimination holding.")
    a('')
    a('**The cases, in the order run,** every case at its three cutoffs (C1 at four):')
    a('')
    a('| Case | Role | Slot | Passed | Failed | Groups under the next-order bar | s |')
    a('|---|---|---|---|---|---|---|')
    for n in order:
        a(summary(n))
    a('')
    a('## 1. Custody')
    a('')
    a(f"- **The freeze.** `run/FROZEN.json` was written once, at {F['written']}, by `run/write_guard.py`, after the go. It "
      f"holds the allowlist of {len(F['allowlist'])} cases, the frozen values with the next-order coefficients by case, "
      f"group and cutoff, the terms' SHA-256, the manifest's SHA-256 and the go, and the SHA-256 of M8.15's {len(tgt)} "
      f"target records, which it copied into `reference/m815_targets/` after each blob id matched the one named before the "
      f"freeze. Its own SHA-256 is `run/FROZEN_PIN`.")
    a(f"- **The freeze block,** built by the pinned `run/freeze_block.py`, carries `FROZEN.json` in full. Its pull request, "
      f"[#652]({OW}/pull/652), was opened at {opened.group(1)}, before the run started, and merged at {merged.group(1)}, "
      f"during it. The maintainer's approval rebuilt the block byte for byte from the pinned code, and records one reading "
      f"note: the column \"equals its manifest line\" in the seeds' file table compares each file with a manifest built from "
      f"the same tree, so it shows only that the seed check loaded manifest files. That the seed check ran on these bytes "
      f"stands on the log: `dev/seed_check.json` is byte for byte the record kept from its runs in `DEVLOG.md` entries "
      f"{e19[0]} and {e23[0]}; `run/seeds.py` has the SHA-256 entry {e23[0]} records after that step's changes; and the "
      f"{len(inst_files)} files of `instrument/` are M8.16's, byte for byte.")
    a('- **Before the run,** read-only: `devtools.frozen()` validated the freeze, the tree against the manifest pin and the '
      'terms; `run/record_environment.py --check` found no difference from `run/ENVIRONMENT.json`; and `run/out/` did not '
      'exist.')
    a(f"- **The run.** `python3 -I -B -u run/driver.py`, from this folder, its output to `run/out/driver.log` through `tee`, "
      f"on mains power at its launch (read at {power_read}, `DEVLOG.md` entry {n_launch[0]}), with sleep held off for its "
      f"length, in the recorded environment: {envtext}. It started at {t0} and wrote its verdict at {t1}, {int(wall)} s "
      f"later" + (', equal to its own clock' if int(wall) == seconds_total else f", against {seconds_total} s by its own clock")
      + f". The cases' run times sum to {round(sum(R[n]['seconds'] for n in order))} s. Its log, `run/out/RUNLOG.json`, "
      f"records the manifest's SHA-256 at the start, equal to `run/MANIFEST_PIN`, and each completed case's outputs with "
      f"their SHA-256.")
    a('- **After the run:** every output equals the SHA-256 the log recorded; `devtools.frozen()` validates; and the '
      'environment, read again, equals `run/ENVIRONMENT.json`.')
    a('- **Post-run files.** These files beside this record were made after the run, and are not records from it:')
    a(f'  - `{POSTRUN[0]}`: `run/record_environment.py --check`, read after the run, with no difference;')
    a('  - `tools/build_record.py`, which builds this record from the files and, with `--check`, reports any difference.')
    a("- **The run's files.** `run/out/driver.log` is the run's standard output and error, and equals `run/out/driver.out`, "
      "the transcript the driver wrote. The target records are M8.15's, copied at the freeze.")
    a('')
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for f, h in run_files:
        a(f'  | `{f}` | `{h}` |')
    a('')
    a('  The post-run files:')
    a('')
    a('  | File | SHA-256 |')
    a('  |---|---|')
    for f, h in post:
        a(f'  | `{f}` | `{h}` |' if f != 'tools/build_record.py' else f'  | `{f}` | `{h}`, as it built this record |')
    a('')
    a('## 2. The controls')
    a('')
    a(f"Every case ran every point and cutoff the terms set, each cutoff from its own seed. All {seeds} seeds of the run "
      f"passed their check: every `Q(u)` within {upsci(seed_q)} of its exact value, relative, every criticality at most "
      f"{upsci(seed_c)}, against `10⁻¹²`, and every `(k, r_u)` the frozen case's. Quantities at the round-off level are given "
      f"as bounds. Points' `m = ‖φ‖²` run from {min(m_all):.4f} to {max(m_all):.2f}; the calibration was fitted on `{m_lo}` "
      f"to `{m_hi:g}` in `R2`, `R3` and `R4` (M8.16's terms, § STATED LIMITS). Below that range lie the points at "
      + '; '.join(f"`ε = {', '.join(ef(e) for e in v)}` of {n}, `m` down to {low_min[n]:.3f}" for n, v in low.items())
      + ". There the margin reads `max(m, m₀)` with `m₀ = " + f"{ln.M0:g}" + "`, an extrapolation, flagged. "
      + "`R5`, the slot of " + ', '.join(outside_slot) + ", lies outside the slots it was fitted on, so the margin there is an "
      "extrapolation too.")
    a('')
    a(f"**The margin's headroom.** M8.16's terms fit the margin on the controls' largest cluster coefficient, {COEF_FIT}, and "
      f"state that its ten-fold headroom holds on the controls (§ STATED LIMITS). Over this run's {len(hd)} points the "
      f"coefficient exceeds {COEF_FIT} at {len(over)}, in {len(over_cases)} cases, and the zero cluster lies less than ten "
      f"times below its gray zone's lower edge at {len(under)}, in {len(under_cases)} cases: {', '.join(under_cases)}. The least "
      f"headroom is {worst[4]:.1f} times, at {worst[0]}, `N = {worst[1]}`, `ε = {ef(worst[2])}`. Points the bar scores are "
      f"among them, in {', '.join(scored_under)}. Every cluster stays separated, as K1 asks, and no eigenvalue outside it "
      f"enters its gray zone: the nearest lies at least {bnd(gap_min, False)} times above the zone's upper edge. On `L`, the "
      f"kernel's lift is at most {bnd(lift_max, True)} u‖L‖, against the cut of {ln.L_CUT / ln.U:g} u‖L‖, and the smallest "
      f"genuine eigenvalue at least {bnd(gen_min, False)} u‖L‖, against the cut's gray zone, which ends at {ln.G_L * ln.L_CUT / ln.U:g} "
      f"u‖L‖. No constant moves: the calibration is fixed with the instrument.")
    a('')
    a(f"**C1, Theorem D at the rigid slot `{c1['case']['slot']}`** ({sec['C1']} s). The exact branch, `c = √ε v`, "
      f"`λ = λ₀ + ‖c‖²`, with no solve, at `ε ∈ {{0.5, 1, 2}}` and `N = 16, 24, 32` and 40. At all {len(c1pts)} points the "
      f"residual is at most {upsci(c1_res)} of the size, against `10⁻¹⁵`; the cubic's part off the lowest level at most "
      f"{upsci(c1_off)}, against `10⁻¹⁴`; and the lowest level's spectrum Theorem D's to {upsci(c1_low)} relative, "
      f"against `10⁻¹⁰`. Every point is Elliptic, `(n(L), n(D), K) = (0, 0, 0)`, with `V₀` as expected. K1 and K4 pass.")
    a('')
    a('**C2a, C2b, C3 and C2a/R5,** at every point and at `N = 16, 24` and 32. The last column is the branch identity\'s '
      'aligned distance between `N = 24` and 32, against `10⁻²`.')
    a('')
    a('| Case | Slot | `ε` | Type; `(n(L), n(D), K)` | Largest deviation from leading order, `N = 16, 24, 32` | Convergence | Aligned distance |')
    a('|---|---|---|---|---|---|---|')
    T.extend(table)
    a('')
    T.extend(ctl_lines)
    a('')
    a('## 3. The pyramid, P5')
    a('')
    a(f"P5 is `{case5['slot']}`'s pyramid ({sec['P5']} s). Every point is accepted, at every cutoff, and K1 and K2 hold at "
      f"every point: the slow band holds exactly the three predicted groups. Each group's deviation from Theorem R's leading "
      f"order, reported and unscored, is given at `N = 16, 24` and 32.")
    a('')
    a('| `ε` | Type; `(n(L), n(D), K)` | The in-span pair | The quartet | The Krein-positive pair | Aligned distance |')
    a('|---|---|---|---|---|---|')
    T.extend(p5rows)
    a('')
    rel5 = {e: p5['readings'][ck.key(e)]['rel_change_max'] for e in EPS4}
    a(f"Every floor is below {p10(b5['floor'])}, every tangent residual below {up1(b5['tangent'])} u, every zero cluster "
      f"below {up1(b5['cluster'])} of its margin, and every `ε` converged. Beside the rule, unscored, the largest relative "
      f"change between the two highest cutoffs is at most " + ', '.join(upsci(rel5[e]) for e in EPS4) + " at `ε = 0.25, 0.5, 1` and 2"
      + ('' if not b5['rel_over'] else ', above the retired fraction `10⁻⁶` at `ε = ' + ', '.join(f'{e:g}' for e in b5['rel_over']) + '`')
      + '.')
    a('')
    a("**The next-order bar,** on the quartet and the Krein-positive pair, at `ε = 0.25, 0.5` and 1. Both pass checks 1 to 4 "
      "at every cutoff. The columns give, at `N = 16, 24` and 32: check 3's spread over the ceiling `C_g(N)`; check 4's "
      "distance `|c_g(N) − ĉ₃|` over its tolerance, `max(spread, 0.1 C_g(N))`; and, reported and unscored, the two-term "
      "residual at `ε = 0.25`, relative to leading order (§ 11 gives every check).")
    a('')
    a('| Group | `c_g/(κs_g)`, `N = 32` | Spread over `C_g(N)` | Check 4: distance over tolerance | Two-term residual at 0.25 |')
    a('|---|---|---|---|---|')
    T.extend(p5bar)
    a('')
    a(f"M8.16 read the quartet {pct(q[0])} to {pct(q[2])} from leading order at `ε = 0.25`, over its bar of 5%, and stopped "
      f"there. This run reproduces M8.16's: at every point of the pyramid and the five controls, {repro} points in all, its "
      f"group centres equal those of M8.16's record at MIT `{rec16[:7]}`, bit for bit, each of those files checked against "
      f"M8.16's run log. Read against the next-order prediction `εκs_g + ε²c_g(N)`, the same readings pass. That is a known outcome on "
      f"M8.16's record, read as INFERRED, not a check of Proposition N passed (the terms, § Known outcomes; the reading note "
      f"of [#650's first review]({OW}/pull/650#pullrequestreview-5631395680)).")
    a('')
    a('**K3 at `ε = 0.25`,** at every cutoff:')
    a('')
    a("| `N` | (a) the kernel, by `L`'s certificate, and the slow band outside the in-span class | (b) the in-span pair | (c) the static overlaps, XY and Z | (d) |")
    a('|---|---|---|---|---|')
    T.extend(k3rows)
    a('')
    a(f"- **K3 is resolved:** (a) to (d) hold at every cutoff. (a)'s slow band is read by the next-order bar, check 1 as "
      f"K3(a) reads it. (d) reads the group (b) finds at `N = 32`: converged, its distance to the nearest event, "
      f"{drow['event']}, {drow['ratio']:.0f} times its uncertainty.")
    a(f"- **K4 passes:** converged at `ε = 0.25`, {ptype[0.25].replace('; (', ' with `(').replace(')', ')`')} at every cutoff, "
      f"every seed passed, and both groups under the bar pass.")
    a('')
    a('## 4. The C3 ray, C3R/R4')
    a('')
    a(f"The ray in `{case_r['slot']}`, a control that gates nothing ({sec[RAY]} s). K1 and K2 hold at its four points, and "
      f"its {len(groups_of(RAY))} groups pass the next-order bar at every cutoff (§ 11). Its points, at `N = 16, 24` and 32, "
      f"with the aligned distance between `N = 24` and 32:")
    a('')
    a('| Case | Slot | `ε` | Type; `(n(L), n(D), K)` | Largest deviation from leading order, `N = 16, 24, 32` | Convergence | Aligned distance |')
    a('|---|---|---|---|---|---|---|')
    T.extend(ray_rows)
    a('')
    a("**The discrimination holds:** wherever checks 1 and 2 hold, the prediction with the off-ray part left out, `c_g°(N)`, "
      "fails check 4 at `c_g`'s tolerance. Its distance from `ĉ₃`, over that tolerance, at `N = 16, 24` and 32:")
    a('')
    a('| Group | `|c_g°(N) − ĉ₃|` over the tolerance |')
    a('|---|---|')
    T.extend(ray_disc)
    a('')
    a(f"The smallest is {dmin:.0f}. The ray's outcome is \"{rc['outcome']}\", as the driver wrote it.")
    a('')
    a('## 5. The rows')
    a('')
    a('**The points of the samples and the member,** at `N = 16, 24` and 32. A point the convergence rule leaves '
      'Unresolved is not labelled with a type (the terms, § STATED LIMITS: WHAT IS ADDED). The last column is the aligned '
      'distance between `N = 24` and 32.')
    a('')
    a('| Case | Slot | `ε` | Type; `(n(L), n(D), K)` | Largest deviation from leading order, `N = 16, 24, 32` | Convergence | Aligned distance |')
    a('|---|---|---|---|---|---|---|')
    T.extend(sample_rows)
    a('')
    a('**K5,** at the samples and the ladders:')
    a('')
    for n in SAMPLES + LADDERS:
        a(k5_line(n))
    a('')
    a("**The diagnosis,** reported, unscored (the terms, § THE VERDICT RULE: WHAT CHANGES): at T1 and T4, in both slots, "
      "K5 holds, with the kernel exact and the slow band matched under the bar, which is what the diagnosis predicts there. "
      "The record claims nothing beyond that.")
    a('')
    a("**K6, at the ladders.** At every read point, the reading here against M8.15's record: its type, `K = n(B) − "
      "n(B|G_tol)` and `k_i⁻`, with the branch identity between `N = 24` and 32. Scored: every point accepted at every cutoff, "
      "no disagreement, and agreement at every read point with `ε ≤ 2`. An Unresolved point above `ε = 2` fails no row. "
      "M8.15's tracked slow eigenvalues against the nearest here, reported beside each and unscored, are in the case files. "
      "The rule's reasons are quoted as it writes them, with `j` for the imaginary unit.")
    a('')
    for n in LADDERS:
        L_ = lad[n]
        a(f"**{n}** (`{R[n]['case']['slot']}`, {sec[n]} s): K6 holds. {L_['npts']} points ran at every cutoff, all accepted, "
          f"and {L_['nread']} are read"
          + (f"; `ε = {', '.join(ef(e) for e in L_['unread'])}` ran unread, as registered" if L_['unread'] else '')
          + f". Every read point with `ε ≤ 2` agrees; above 2, {L_['agree']} of {L_['above']} agree"
          + (f", and {len(L_['unres'])} read Unresolved." if L_['unres'] else '.'))
        a('')
        a("| `ε` | Here: type; `K`; `k_i⁻` | M8.15: type; `K`; `k_i⁻` | K6 | Aligned distance | The rule's reason |")
        a('|---|---|---|---|---|---|')
        T.extend(L_['rows'])
        a('')
    a(f"## 6. T5's second member, {MEMBER}")
    a('')
    a(f"Scored for that member alone ({sec[MEMBER]} s). Each of its three groups under the bar reads Unresolved by check 1 "
      f"at `ε = 0.25`, at `N = 16, 24` and 32 (§ 11).")
    a(f"- **At that point** the seed is checked, the point accepted, K1 holds and each group is matched. The convergence "
      f"rule, which reads the point once from its three cutoffs, reads it {r25['verdict']}: \"{why25[0]}\". That "
      f"Krein-positive set is each slow group's partner, its nearest imaginary group of opposite Krein sign, which the rule "
      f"reads wherever it lies; the reason stands once for each of the three groups. Its change from `N = 24` to 32, "
      f"{sci(prt['d2'])}, exceeds both its change from 16 to 24, {sci(prt['d1'])}, and the floor, {sci(prt['floor'])}. The "
      f"slow groups' own rows in that reading converge, their relative change {bnd(slow_rel, True)} at most.")
    a("- **K5 fails** on the same reading: convergence at `ε = 0.25` is its own clause.")
    a(f"- **At `ε = 0.5` and 1** the point converges, {case_m['type']} with `(n(L), n(D), K) = "
      f"({', '.join(str(i) for i in case_m['idx'])})` as expected, and K1 holds.")
    a(f"- **Reported, unscored:** at `ε = 2` the rule reads {r2['verdict']} again: \"{why2[0]}\".")
    a(f"- **Its `ε = 0.25` points** lie below the calibration's fitted range of `m` (§ 2), as T5/R2's do, which converge there.")
    a("- **Its outcome is its own** (the terms, § T5'S SECOND MEMBER). It stops nothing, and it neither carries nor takes the "
      "verdict on T5's registered member, which qualified.")
    a('')
    a('## 7. The gate record and the verdict')
    a('')
    a(f"- **`run/out/GATE.json`,** written at {gate['written']}: no stop; the controls and the pyramid complete; the "
      f"instrument qualified; the `R5` gate passed.")
    a(f"- **`run/out/VERDICT.json`:** {verdict['verdict']}, with K3's outcome \"{verdict['k3']}\". The rows it qualifies: "
      f"{', '.join(verdict['qualified'])}. The member not qualified: {MEMBER}. The C3 ray: {verdict['c3_ray'][RAY]}.")
    a('')
    a('## 8. Deviations')
    a('')
    a('- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above.')
    a('')
    a('## 9. Corrections')
    a('')
    a("- **None.** The reading note in the maintainer's approval of the freeze block (§ 1) needs no change to it.")
    a('')
    a('## 10. Follow-ups, outside M8.16.1')
    a('')
    a('- **The census run,** under its own pre-registration, runs only the nine rows qualified here (the terms, '
      '§ DEFINITION OF DONE). Its adequacy tests still apply at the Unresolved points of § 5 (the terms, § STATED LIMITS: '
      'WHAT IS ADDED).')
    a(f"- **T5's second member** is not offered to this instrument again (the terms, § THE VERDICT RULE: WHAT CHANGES). "
      f"Why the partner set near `{part25.imag:.4g}i` does not contract at `ε = 0.25` is OPEN.")
    a('- **The margin behind check 1** is measured, not certified: a reading note of the approval of '
      f'[#650]({OW}/pull/650), with no stronger rule asked. On this run T5/R2\'s three groups depart from '
      f'`εκs_g + ε²c_g(N)` at `ε = 1` by at most {bnd(dep_max, True)} of a ceiling, where an exchange of its two lowest needs '
      f'`ε³` terms toward each other of 4.5 to 5.5 ceilings each (`DEVLOG.md` entry {e44[0]}), at least '
      f'{math.floor(4.5 / float(bnd(dep_max, True)))} times more.')
    a('')
    a('## 11. The next-order readings, every group at every cutoff')
    a('')
    a("Each case's groups under the bar, by ascending `|s_g|`, as the terms' table orders them. At each cutoff: `c_g(N)`, and, "
      "where check 1 holds, `ĉ₂` and `ĉ₃`, all three over `κs_g`; the ceiling `C_g(N) = max(0.1 |c_g(N)|, 10⁻³ |κs_g|)` over "
      "`|κs_g|`; the four checks; and, reported and unscored as § THE NEXT-ORDER BAR asks, the two-term residual at "
      "`ε = 0.25`, `|λ_g − εκs_g − ε²c_g| / (ε|κs_g|)`, beside 1%, and the deviation from leading order at `ε = 0.25, 0.5` "
      "and 1. Check 1: each point accepted, its seed checked, K1, converged, and K2's matching against `εκs_g + ε²c_g(N)`. "
      "Check 2: the association, and `E_c` over `C_g(N)/10`, at most 1. Check 3: the spread `|ĉ₃ − ĉ₂|` over `C_g(N)`, at "
      "most 1. Check 4: `|c_g(N) − ĉ₃|` over `max(spread, 0.1 C_g(N))`, at most 1. A group passes when checks 1 to 4 hold at "
      "every cutoff.")
    a('')
    for n in BAR_CASES:
        a(f"**{n}**")
        a('')
        a('| Group | `N` | `c_g`; `ĉ₂`; `ĉ₃`, over `κs_g` | `C_g(N)` over `|κs_g|` | Check 1 | Check 2 | Check 3 | Check 4 '
          '| Two-term residual | Deviation from leading order | Reading |')
        a('|---|---|---|---|---|---|---|---|---|---|---|')
        T.extend(bar_tables[n])
        a('')
    a('## 12. Reproduction')
    a('')
    a('`REPRODUCE.md` gives every command. For the run, from a copy of this folder:')
    a('- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and '
      '`python3 -I -B run/record_environment.py --check`;')
    a('- **the registered run:** `python3 -I -B -u run/driver.py`, in a copy without `run/out/`. It validates the committed '
      'freeze, `run/FROZEN.json` against `run/FROZEN_PIN`, and refuses a tree that differs from the manifest pin. In a '
      "copy that keeps this `run/out/`, it checks every case's outputs against the SHA-256 the log recorded and solves "
      'nothing; it writes the same verdict, with a new transcript and log;')
    a('- `python3 -I -B tools/build_record.py MIT_REPO --check`, which rebuilds this record from the files and reports any '
      'difference.')
    a('')
    a('Bitwise agreement on another machine is not claimed: the terms read every scored quantity against margins far above '
      'round-off.')
    text = '\n'.join(T) + '\n'
    for bad in ('—', '–', '/Users/', 'Desktop', 'm8_carry_home'):
        if bad in text:
            stop(f'the record holds {bad!r}')
    path = os.path.join(ROOT, 'RECORD.md')
    if check:
        old = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if old != text:
            print('RECORD.md differs from the record these files build')
            raise SystemExit(1)
        print(f'RECORD.md equals the record these files build: {len(text.split())} words')
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'written RECORD.md: {len(text.splitlines())} lines, {len(text.split())} words')


if __name__ == '__main__':
    main()
