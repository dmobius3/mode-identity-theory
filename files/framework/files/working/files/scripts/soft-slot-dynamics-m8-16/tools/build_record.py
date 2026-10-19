#!/usr/bin/env python3
"""Post-run: made after M8.16's registered run. It builds RECORD.md from the run's files, so that every number and hash
in the record is read from the bytes it names.

Usage, from this folder: python3 -I -B tools/build_record.py MIT_REPO [--check]
  MIT_REPO: a clone of mode-identity-theory whose HEAD holds this folder's frozen commit; the instrument's commit is
            read there as the last one that wrote run/MANIFEST_PIN.
  --check:  build the record and compare it with RECORD.md, without writing; exit 1 on any difference.

It refuses if an output differs from the SHA-256 the run's log recorded, or if the freeze does not validate."""
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

FOLDER = 'files/framework/files/working/files/scripts/soft-slot-dynamics-m8-16'
OUT = os.path.join(ROOT, 'run', 'out')
OW = 'https://github.com/openwave-labs/openwave'
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
CASES = ('C1', 'C2a', 'C2b', 'C3', 'C2a/R5', 'P5')
EPS = (0.25, 0.5, 1.0, 2.0)
POSTRUN = ('environment_postrun_2026-10-18.txt', 'tools/p5_extrapolation.py', 'tools/p5_extrapolation.out',
           'tools/build_record.py')


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


def main():
    if len(sys.argv) < 2:
        stop(__doc__)
    repo, check = sys.argv[1], '--check' in sys.argv[2:]

    def git(*a):
        return subprocess.run(['git', '-C', repo, *a], check=True, capture_output=True, text=True).stdout.strip()
    instr = git('log', '-1', '--format=%H', 'HEAD', '--', f'{FOLDER}/run/MANIFEST_PIN')
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
    if log['manifest_sha256'] != mpin:
        stop('the run log does not record the manifest pin')
    terms = sha(os.path.join(ROOT, 'run', 'm8_16_task_details.md'))
    with open(os.path.join(OUT, 'driver.log'), 'rb') as a, open(os.path.join(OUT, 'driver.out'), 'rb') as b:
        same_transcript = a.read() == b.read()
    if not same_transcript:
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
    t0 = log['events'][0]['t']
    t1 = log['verdict']['written']
    wall = (datetime.datetime.fromisoformat(t1.replace('Z', '+00:00'))
            - datetime.datetime.fromisoformat(t0.replace('Z', '+00:00'))).total_seconds()
    order = re.search(r"cases \[(.*)\]", log['events'][0]['event']).group(1).replace("'", '').split(', ')
    ran = list(log['completed'])
    if tuple(ran) != CASES or order[:len(ran)] != ran:
        stop(f'the run ran {ran}')
    rows_not_run = order[len(ran):]
    seconds_total = int(re.search(r'; (\d+) s$', open(os.path.join(OUT, 'driver.log'), encoding='utf-8').read().strip()).group(1))
    if not (verdict['verdict'] == 'NOT QUALIFIED' and verdict['failed'] == ['P5: K3', 'P5: K4'] and not verdict['rows']):
        stop(f'the verdict is {verdict}')

    R = {n: J(os.path.join(OUT, n.replace('/', '_') + '.json')) for n in CASES}

    # the calibration's fitted range (the terms, § STATED LIMITS): every point's max(m, m0), from its margin
    tt = open(os.path.join(ROOT, 'run', 'm8_16_task_details.md'), encoding='utf-8').read()
    FIT = 'in `R2`, `R3` and `R4`, with `m` from 0.204 to 132 and `N` from 16 to 40. Outside that range it is an extrapolation, flagged in the record wherever it applies. `R5` lies outside the slots it was fitted on.'
    if FIT not in tt:
        stop('the terms do not state the calibration range as this record reads it')
    fit_slots, m_lo, m_hi = ('R2', 'R3', 'R4'), 0.204, 132.0
    meff = {n: [(c['record']['margin'] / ln.KAPPA) ** 2 / (ln.U * c['record']['normA']) for cut in R[n]['cutoffs'].values()
                for c in cut['points'].values()] for n in CASES}
    m_all = [x for v in meff.values() for x in v]
    outside_m = [n for n in CASES if any(not (m_lo <= x <= m_hi) for x in meff[n])]
    outside_slot = [n for n in CASES if R[n]['case']['slot'] not in fit_slots]
    if outside_m:
        stop(f'points outside the fitted range of m in {outside_m}: the record must flag them')
    # the power, as read at the launch: DEVLOG's launch entry, by heading
    dl0 = open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8').read()
    h0 = [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^## (\d+)\. (.*)$', dl0, re.M)]
    n_launch = [k for k, h in h0 if h.split(': ', 1)[1].startswith("the registered run, launched on Blake's go")]
    if len(n_launch) != 1:
        stop('no single launch entry in DEVLOG.md')
    n_launch = n_launch[0]
    e_launch = re.search(rf'^## {n_launch}\. .*?(?=^## {n_launch + 1}\. |\Z)', dl0, re.S | re.M).group(0)
    pw = re.search(r"\*\*The power,\*\* read at (\S+): \"Now drawing from 'AC Power'\"", e_launch)
    if not pw:
        stop('the launch entry does not record mains power')
    power_read = pw.group(1)

    # the seeds
    seed_q, seed_c, seeds = 0.0, 0.0, 0
    for n in CASES:
        qx = ck.num(R[n]['case']['Q'])
        for cut in R[n]['cutoffs'].values():
            s = cut['seed']
            if not s['ok']:
                stop(f'{n}: a seed failed')
            seeds += 1
            seed_q, seed_c = max(seed_q, abs(s['Q'] - qx) / qx), max(seed_c, s['crit'])

    # C1
    c1 = R['C1']
    c1pts = [p for cut in c1['cutoffs'].values() for p in cut['points'].values()]
    c1case = c1['case']
    if not all(p['accepted'] and p['d6_ok'] and p['record']['type'] == 'Elliptic' and
               [p['record'][x] for x in ('nL', 'nD', 'K')] == [0, 0, 0] and p['record']['v0_matches'] for p in c1pts):
        stop('C1 does not read as recorded here')
    c1_res = max(p['residual_rel'] for p in c1pts)
    c1_off = max(p['off_level'] for p in c1pts)
    c1_low = max(max(p['lowest_errors']) for p in c1pts)

    # the soft-slot controls and the pyramid, per point
    def bounds(n):
        pts = [p for cut in R[n]['cutoffs'].values() for p in cut['points'].values()]
        return dict(floor=max(p['floor_rel'] for p in pts),
                    tangent=max(p['kernel']['tangent'] for p in pts) / ln.U,
                    cluster=max(p['record']['cluster_max'] / p['record']['margin'] for p in pts),
                    rel=max(R[n]['readings'][ck.key(e)]['rel_change_max'] for e in EPS),
                    rel_over=[e for e in EPS if not R[n]['readings'][ck.key(e)]['rel_change_ok']],
                    aligned=max(R[n]['identity'][ck.key(e)]['aligned_distance'] for e in EPS),
                    npts=len(pts))
    soft = ('C2a', 'C2b', 'C3', 'C2a/R5')
    table = []
    for n in soft:
        case = R[n]['case']
        for e in EPS:
            types, devs = set(), []
            for N in ('16', '24', '32'):
                p = R[n]['cutoffs'][N]['points'][ck.key(e)]
                if not (p['accepted'] and ck.k1(p, case)):
                    stop(f'{n} at N = {N}, eps = {e}: not accepted, or K1 fails')
                r = p['record']
                types.add(f"{r['type']}; ({r['nL']}, {r['nD']}, {r['K']})")
                devs.append(ck.leading(p, case, e)[1])
            rd, idn = R[n]['readings'][ck.key(e)], R[n]['identity'][ck.key(e)]
            if len(types) != 1 or rd['verdict'] != 'converged' or not idn['kept']:
                stop(f'{n} at eps = {e}: not one reading, not converged or identity not kept')
            table.append(f"| {n} | `{case['slot']}` | {e:g} | {types.pop()} | {', '.join(pct(d) for d in devs)} | "
                         f"converged | {sci(idn['aligned_distance'])} |")
    ctl = {n: gate['cases'][n] for n in soft}
    ctl_lines = []
    for n in soft:
        g, b = ctl[n], bounds(n)
        k2 = f", K2 {'passes' if g.get('K2') else 'fails'}" if 'K2' in g else ''
        d = g['deviations']
        ctl_lines.append(
            f"- **{n}** (`{R[n]['case']['slot']}`, {round(R[n]['seconds'])} s): K1 {'passes' if g['K1'] else 'fails'}{k2}, "
            f"and K4 {'passes' if g['K4'] else 'fails'}. The largest deviation from leading order is "
            f"{', '.join(pct(d[N][0]) for N in ('16', '24', '32'))} at `ε = 0.25` and "
            f"{', '.join(pct(d[N][1]) for N in ('16', '24', '32'))} at `ε = 2`, at `N = 16, 24` and 32. "
            f"Every floor is below {p10(b['floor'])}, every tangent residual below {up1(b['tangent'])} u, and every "
            f"zero cluster below {up1(b['cluster'])} of its margin. Beside the rule, unscored, the largest relative change "
            f"between the two highest cutoffs is at most {upsci(b['rel'])}"
            + (f", within the retired fraction `10⁻⁶`." if not b['rel_over'] else f", above the retired fraction `10⁻⁶` at `ε = "
               + ', '.join(f'{e:g}' for e in b['rel_over']) + '`.')
            + (f" Its margin is an extrapolation: `{R[n]['case']['slot']}` lies outside the slots the calibration was fitted on "
               f"(the terms, § STATED LIMITS)." if n in outside_slot else ''))

    # the pyramid
    p5, case5 = R['P5'], R['P5']['case']
    g5 = gate['cases']['P5']
    k3 = g5['K3']
    NEG, QUA, POS = ('imag', -1), ('complex', None), ('imag', 1)
    p5rows, dev5, ptype = [], {}, {}
    for e in EPS:
        types, cells = set(), {NEG: [], QUA: [], POS: []}
        for N in ('16', '24', '32'):
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
        p5rows.append(f"| {e:g} | {'scored' if e == 0.25 else 'reported, unscored'} | {ptype[e]} | "
                      + ' | '.join(', '.join(pct(v) for v in cells[k]) for k in (NEG, QUA, POS)) + f" | {sci(idn['aligned_distance'])} |")
    q = [dev5[(0.25, N, QUA)] for N in ('16', '24', '32')]
    if not (all(v > ck.BAR for v in q) and all(dev5[(0.25, N, k)] <= ck.BAR for N in ('16', '24', '32') for k in (NEG, POS))):
        stop('the pyramid does not read as recorded here')
    b5 = bounds('P5')
    k3rows = []
    for N in ('16', '24', '32'):
        v, p = k3['per_N'][N], p5['cutoffs'][N]['points'][ck.key(0.25)]
        kern, kk = p['kernel'], ck.kernel_exact(p, case5)
        tro = ck.theorem_r_outside(p, case5, 0.25)
        if v['a'] or not kk or tro or not (v['b'] and v['c'] and v['d']):
            stop(f'K3 at N = {N} does not read as recorded here')
        ov = v['overlaps']
        k3rows.append(f"| {N} | holds: tangent residual below {up1(kern['tangent'] / ln.U)} u, `L`'s zero count "
                      f"{kern['dimkerL']} = the chains, gray zone empty | fails: the quartet {pct(dev5[(0.25, N, QUA)])} | "
                      f"holds: {pct(dev5[(0.25, N, NEG)])} | holds: {ov['xy']:.4f} and below {p10(ov['z'])}; axis fraction {ov['axis']:.3f} | holds |")
    drow = k3['d_row']
    ext = open(os.path.join(ROOT, 'tools', 'p5_extrapolation.out'), encoding='utf-8').read()
    blk = ext.split('N = 32\n', 1)[1]
    ext_rows = []
    for name, label in (('the in-span pair, imaginary and Krein-negative', 'the in-span pair'),
                        ('the quartet', 'the quartet'), ('the Krein-positive pair', 'the Krein-positive pair')):
        m = re.search(re.escape(name) + r': at eps = 0\.25: ([\d.]+%).*\n\s+extrapolated to eps -> 0: first order removed '
                      r'([\d.]+%); second order removed ([\d.]+%)', blk)
        ext_rows.append(f'| {label} | {m.group(1)} | {m.group(2)} | {m.group(3)} |')

    # the targets and the post-run files
    tgt = [(t['file'], t['sha256']) for t in F['targets']]
    for f, h in tgt:
        if sha(os.path.join(ROOT, f)) != h:
            stop(f'{f} differs from FROZEN.json')
    post = [(p, sha(os.path.join(ROOT, p))) for p in POSTRUN]

    # the seed check's entry, by heading, for § 6
    dl = open(os.path.join(ROOT, 'DEVLOG.md'), encoding='utf-8').read()
    heads = [(int(m.group(1)), m.group(2)) for m in re.finditer(r'^## (\d+)\. (.*)$', dl, re.M)]
    n269 = max(k for k, h in heads if 'run `dev/seed_check.py`' in h)
    gl = open(os.path.join(ROOT, 'instrument', 'linear.py'), encoding='utf-8').read().splitlines()
    ln_d = 1 + next(i for i, l in enumerate(gl) if 'inertia(Dm, 1e-8' in l)
    cl = open(os.path.join(ROOT, 'run', 'checks.py'), encoding='utf-8').read().splitlines()
    ln_axis = 1 + next(i for i, l in enumerate(cl) if l.startswith('AXIS_MIN = 1e-6'))

    run_files = [(f'run/out/{f}', h) for f, h in files.items()]
    run_files += [(f"run/out/{log['gate']['file']}", log['gate']['sha256']), (f"run/out/{log['verdict']['file']}", log['verdict']['sha256']),
                  (f"run/out/{log['transcript']['file']}", log['transcript']['sha256']),
                  ('run/out/driver.log', sha(os.path.join(OUT, 'driver.log'))), ('run/out/RUNLOG.json', sha(os.path.join(OUT, 'RUNLOG.json'))),
                  ('run/FROZEN.json', fpin)] + tgt

    T = []
    a = T.append
    a('# M8.16 run record')
    a('')
    a(f"The record of M8.16's registered run on 2026-10-18, under the governing terms, `run/m8_16_task_details.md` (SHA-256 "
      f"`{terms[:16]}…`), merged in OpenWave [#637]({OW}/pull/637), and the instrument frozen at MIT `{instr[:7]}` with its "
      f"manifest pin, `{mpin[:16]}…`. The maintainer's go is [#637's comment]({F['go']}), and the freeze block is OpenWave's "
      f"`research/m8_16/freeze_block.md`, merged in [#639]({OW}/pull/639). Every number below is read from the run's files "
      f"in [`run/out/`](run/out/), and `tools/build_record.py` builds this record from them. The case files hold every "
      f"point's full readings at every cutoff; this record gives each point's type, indices and deviations from leading "
      f"order, and every check. The verdict is the one the "
      f"driver wrote under the terms' verdict rule. Adjudication is the maintainer's.")
    a('')
    a(f"**The outcome.** NOT QUALIFIED, failing K3 and K4, both on the pyramid, P5. The five controls passed every check. "
      f"The pyramid's quartet lies {pct(q[0])}, {pct(q[1])} and {pct(q[2])} from Theorem R's leading order at `ε = 0.25`, "
      f"at `N = 16, 24` and 32, over the bar of 5%, and that one reading fails both K4 and K3's part (a). The run stopped "
      f"at the pyramid, as the terms require, and no census row ran.")
    a('')
    a('## 1. Custody')
    a('')
    a(f"- **The freeze.** `run/FROZEN.json` was written once, at {F['written']}, by `run/write_guard.py`, after the go. It "
      f"holds the allowlist of {len(F['allowlist'])} cases, the frozen values, the terms' SHA-256, the manifest's SHA-256 "
      f"and the go, and the SHA-256 of M8.15's {len(tgt)} target records, which it copied into `reference/m815_targets/` "
      f"after each blob id matched the one named before the freeze. Its own SHA-256 is `run/FROZEN_PIN`. The freeze block "
      f"carries it in full.")
    a('- **Before the run,** read-only: `devtools.frozen()` validated the freeze, the tree against the manifest pin, the '
      'terms and the target records; `run/record_environment.py --check` found no difference from `run/ENVIRONMENT.json`; '
      'and `run/out/` did not exist.')
    a(f"- **The run.** `python3 -I -B -u run/driver.py`, from this folder, its output to `run/out/driver.log`, on mains "
      f"power at its launch (read at {power_read}, `DEVLOG.md` entry {n_launch}), with sleep held off for its length, "
      f"in the recorded environment: {envtext}. It started at {t0} and wrote its verdict at {t1}, {int(wall)} s later"
      + (', equal to its own clock' if int(wall) == seconds_total else f", against {seconds_total} s by its own clock") + f". Its log, `run/out/RUNLOG.json`, records the manifest's SHA-256 at the start, "
      f"equal to `run/MANIFEST_PIN`, and each completed case's outputs with their SHA-256.")
    a('- **After the run:** every output equals the SHA-256 the log recorded; `devtools.frozen()` validates; and the '
      'environment, read again, equals `run/ENVIRONMENT.json`.')
    a('- **Post-run files.** These files beside this record were made after the run, and are not records from it:')
    a('  - `environment_postrun_2026-10-18.txt`: `run/record_environment.py --check`, read after the run, with no difference;')
    a('  - `tools/p5_extrapolation.py` and its output, `tools/p5_extrapolation.out`: the pyramid\'s slow eigenvalues '
      'extrapolated to zero amplitude, unscored (§ 3);')
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
    a(f"Each control ran every point and cutoff the terms set, each cutoff from its own seed. All {seeds} seeds of the run "
      f"passed their check: every `Q(u)` within {upsci(seed_q)} of its exact value, relative, and every criticality at "
      f"most {upsci(seed_c)}, against `10⁻¹²`, and every `(k, r_u)` the Result's. Quantities at the round-off level are given "
      f"as bounds. Every point's `m = ‖φ‖²` lies inside the range the calibration was fitted on, `{m_lo}` to `{m_hi:g}`: "
      f"from {min(m_all):.4f} to {max(m_all):.4f}, read from each point's margin.")
    a('')
    a(f"**C1, Theorem D at the rigid slot `{c1case['slot']}`** ({round(c1['seconds'])} s). The exact branch, `c = √ε v`, "
      f"`λ = λ₀ + ‖c‖²`, with no solve, at `ε ∈ {{0.5, 1, 2}}` and `N = 16, 24, 32` and 40. At all {len(c1pts)} points the "
      f"residual is at most {upsci(c1_res)} of the size, against `10⁻¹⁵`; the cubic's part off the lowest level at most "
      f"{upsci(c1_off)}, against `10⁻¹⁴`; and the lowest level's spectrum Theorem D's to {upsci(c1_low)} relative, "
      f"against `10⁻¹⁰`. Every point is Elliptic, `(n(L), n(D), K) = (0, 0, 0)`, with `V₀` as expected, and the type, `n(L)`, `K` "
      f"and those eigenvalues are unchanged in `N` to `10⁻¹²`. K1 and K4 pass.")
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
    a(f"P5 is `{case5['slot']}`'s pyramid, the first sealed case in the order ({round(p5['seconds'])} s). Every point is "
      f"accepted, at every cutoff, and K1 and K2 hold at every point: the slow band holds exactly the three predicted "
      f"groups. Each group's deviation from Theorem R's leading order is given at `N = 16, 24` and 32.")
    a('')
    a('| `ε` | Under K4 | Type; `(n(L), n(D), K)` | The in-span pair | The quartet | The Krein-positive pair | Aligned distance |')
    a('|---|---|---|---|---|---|---|')
    T.extend(p5rows)
    a('')
    rel5 = {e: p5['readings'][ck.key(e)]['rel_change_max'] for e in EPS}
    a(f"Every floor is below {p10(b5['floor'])}, every tangent residual below {up1(b5['tangent'])} u, every zero cluster "
      f"below {up1(b5['cluster'])} of its margin, and every `ε` converged. Beside the rule, unscored, the largest relative "
      f"change between the two highest cutoffs is at most " + ', '.join(upsci(rel5[e]) for e in EPS) + " at `ε = 0.25, 0.5, 1` and 2"
      + ('' if not b5['rel_over'] else ', above the retired fraction `10⁻⁶` at `ε = ' + ', '.join(f'{e:g}' for e in b5['rel_over']) + '`')
      + '.')
    a('')
    a('**K3 at `ε = 0.25`,** at every cutoff:')
    a('')
    a("| `N` | (a) the kernel, by `L`'s certificate | (a) the slow band outside the in-span class | (b) the in-span pair | (c) the static overlaps, XY and Z | (d) |")
    a('|---|---|---|---|---|---|')
    T.extend(k3rows)
    a('')
    a(f"- **(a) fails at every cutoff,** on the quartet alone. K3's outcome is therefore \"{k3['outcome']}\": the terms list "
      f"\"the slow band departs from Theorem R outside the in-span pair\" under the instrument failure.")
    VR = 'If K3 fails with the kernel exact, the record says that the diagnosis is wrong.'
    K3LIST = '**Instrument failure:** (a) fails: a point is not accepted, a seed fails its check, the kernel is not exact, or the slow band departs from Theorem R outside the in-span pair. The diagnosis is untested.'
    if VR not in tt or K3LIST not in tt or '**Not resolved, with the kernel exact:** (a) passes and (b), (c) or (d) fails' not in tt:
        stop('the terms do not carry the K3 texts this record quotes')
    a(f"- **The verdict rule's K3 sentence.** § THE VERDICT RULE says: \"{VR}\" Read alone, it would fit P5, whose "
      f"kernel certificate holds while K3 fails. K3's own list defines that outcome as \"(a) passes and (b), (c) or (d) "
      f"fails\", and lists a slow band that departs from Theorem R outside the in-span pair under the instrument "
      f"failure. The driver follows K3's list, and so does this record; the sentence is noted here for the adjudication.")
    a(f"- **(b), (c) and (d) hold at every cutoff,** and decide nothing once (a) fails. (d) reads the group (b) finds at "
      f"`N = 32`: converged, its distance to the nearest event, {drow['event']}, {drow['ratio']:.0f} times its uncertainty.")
    a(f"- **K4 fails:** converged, {ptype[0.25].replace('; (', ' with `(').replace(')', ')`')} at every cutoff, and every seed "
      f"passed, but the quartet is over the bar at every cutoff. The Krein-positive pair is within it, at "
      f"{', '.join(pct(dev5[(0.25, N, POS)]) for N in ('16', '24', '32'))}.")
    a('')
    a("**Post-run, unscored** (`tools/p5_extrapolation.out`). Each group's eigenvalue over `ε`, extrapolated to `ε → 0` from "
      "the registered points, against Theorem R's `κsτ`, at `N = 32`:")
    a('')
    a('| Group | At `ε = 0.25` | First order removed | Second order removed |')
    a('|---|---|---|---|')
    T.extend(ext_rows)
    a('')
    a('## 4. The gate record and the verdict')
    a('')
    a(f"- **`run/out/GATE.json`,** written at {gate['written']}: the stop \"{gate['stop']}\"; the controls and the pyramid "
      f"complete; the instrument not qualified; the `R5` gate passed.")
    a(f"- **`run/out/VERDICT.json`:** {verdict['verdict']}, failing {' and '.join(verdict['failing'])}, both the "
      f"pyramid's, with K3's outcome as above.")
    a(f"- **The rows did not run:** {', '.join(rows_not_run)}. The row gate refuses a row until the gate record shows K1 "
      f"to K4 passed, so K5 and K6 have no outcome.")
    a('- **A resume is refused:** the gate record names a stop.')
    a('')
    a('## 5. Deviations')
    a('')
    a(f"- **`FROZEN.json`'s values.** § FIXED AT THE FREEZE says `FROZEN.json` holds \"the cutoffs and every frozen value "
      f"above\". Its values omit two items of § FROZEN VALUES: `D`'s cut `10⁻⁸ ‖B‖`, the literal at "
      f"`instrument/linear.py:{ln_d}`, and K3's axis guard `10⁻⁶`, `AXIS_MIN` at `run/checks.py:{ln_axis}`. The maintainer's "
      f"approval of [#639]({OW}/pull/639) records it. Neither could move: the run reads its constants from the pinned "
      f"code and never reads the values, and `devtools.frozen()` refuses a tree that differs from the manifest pin "
      f"`FROZEN.json` carries. `FROZEN.json` is written once and stands as written. At adjudication the two values are "
      f"read from the pinned code, as the approval says.")
    a('- **None in the run.** It ran in the order the terms set, from the pinned tree, by the one command above.')
    a('')
    a('## 6. Corrections')
    a('')
    a(f"- **The freeze block's seeds line.** It says that the instrument files `dev/seed_check.py` reads, seven named, are "
      f"unchanged in the pinned tree. The seed check imports eleven: those seven and `__init__.py`, `devtools.py`, "
      f"`newton.py` and `linear.py`. The maintainer's approval of [#639]({OW}/pull/639) records it. Against the hashes "
      f"`DEVLOG.md` entry {n269} logged at the seed check, ten of the twelve instrument files are unchanged at MIT "
      f"`{instr[:7]}`. Of the eleven read, only `linear.py` changed, by one line in `record()` that adds `l_resolved` to "
      f"its output. The seed values never reach `record()`: the seed check's claim 5 makes it raise throughout the seed "
      f"evaluation, and no sentinel fired. The seed values stand on the pinned code.")
    a('')
    a('## 7. Follow-ups, outside M8.16')
    a('')
    a('- **A revised instrument, or another qualification run,** is a new pre-registration under a new ID, as the terms\' '
      'verdict rule requires.')
    a('- **The census rows** did not run. The census run runs only rows that a qualification qualifies.')
    a('- **The quartet at `ε = 0.25`.** The post-run reading of § 3 is unscored. How a bar at the smallest amplitude '
      'allows for a mode\'s next-order term is for a later pre-registration to settle.')
    a('')
    a('## 8. Reproduction')
    a('')
    a('`REPRODUCE.md` gives every command. For the run, from a copy of this folder:')
    a('- `shasum -a 256 -c SHA256SUMS`, the manifest against `run/MANIFEST_PIN`, and '
      '`python3 -I -B run/record_environment.py --check`;')
    a('- **the registered run:** `python3 -I -B -u run/driver.py`, in a copy without `run/out/`. It validates the committed '
      'freeze, `run/FROZEN.json` against `run/FROZEN_PIN`, and refuses a tree that differs from the manifest pin. In a '
      'copy that keeps this `run/out/`, it reads the log and refuses to resume, since the gate record names a stop;')
    a('- `python3 -I -B tools/p5_extrapolation.py`, which re-reads the pyramid\'s outputs;')
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
