#!/usr/bin/env python3
"""Build m8_16_task_details.md from m8_16_task_details.src.md: every commit is read from git, the #512 boundary is
copied byte for byte from the ruling's record, and the resolution table, the band edges, T5's frequencies and the cost
table are computed here. No hash, commit, entry number or computed figure is typed into the source.

A drafting tool (UA, 2026-10-17). Its commits come from moving heads and its rates from the latest matching run files,
so the built text, not this script, is the artifact: once filed it is hashed after its last edit, and this script is
never rerun on it after the freeze. Each build prints its provenance, the commits and the run files with their SHA-256.

Usage: fill_terms.py MIT_REPO OPENWAVE_REPO [--write]
  MIT_REPO: a checkout of mode-identity-theory; its pages are read at origin/main, after a fetch.
  OPENWAVE_REPO: a checkout of openwave with the upstream remote; M8.15's filed terms are read at upstream/main, for
  the slot action's two commits as M8.15 cites them.
  --write: write m8_16_task_details.md; without it, report the values only.
  --base COMMIT: read MIT's pages at COMMIT, a commit in MIT_REPO, instead of origin/main, without a fetch, so a
  rebuild reads the base the terms were built from (UB on #637).
"""
import json
import math
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.dirname(HERE)
RULING = os.path.join(os.path.dirname(BENCH), 'census_step3_ruling', 'xrodz_reply_18955679.md')
RUNS = os.path.join(BENCH, 'dev', 'runs')
GH = 'https://github.com/dmobius3/mode-identity-theory/blob'
W = 'files/framework/files/working/files'
U = 2.220446049250313e-16
G = 3.0


REF = 'origin/main'           # MIT's pages are read here; --base moves it to a fixed commit


def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], check=True, capture_output=True, text=True).stdout


def last_commit(repo, path):
    sha = git(repo, 'log', '-1', '--format=%H', REF, '--', path).strip()
    assert re.fullmatch(r'[0-9a-f]{40}', sha), path
    return sha


def boundary():
    lines = [ln for ln in open(RULING, encoding='utf-8').read().splitlines() if ln.startswith('> Admitted on #512:')]
    assert len(lines) == 1
    return lines[0]


def m815_terms_commit(repo):
    """M8.15's governing terms commit on OpenWave, as M8.15's RECORD.md cites it."""
    rec = git(repo, 'show', f'{REF}:{W}/scripts/soft-slot-dynamics/RECORD.md')
    return re.search(r'governing terms \(OpenWave `([0-9a-f]{8})`', rec).group(1)


def slot_action_commits(ow):
    """The slot action's commits as M8.15's filed terms cite them: §§ I to VIII, and § IX's dated notes."""
    terms = git(ow, 'show', 'upstream/main:openwave/xperiments/m8_mit/research/tasks/m8_15_task_details.md')
    link = r'mode-identity-theory/blob/([0-9a-f]{40})/files/framework/files/working/files/slot-action\.md'
    frozen = [ln for ln in terms.splitlines() if ln.startswith('| MIT [`slot-action.md`]') and '§§ I to VIII' in ln]
    notes = [ln for ln in terms.splitlines() if ln.startswith("| the same page, § IX's dated notes")]
    assert len(frozen) == 1 and len(notes) == 1
    a, b = re.findall(link, frozen[0]), re.findall(link, notes[0])
    assert len(set(a)) == 1 and len(set(b)) == 1
    return a[0], b[0]


# the frozen values (this task's § FROZEN VALUES), for the resolution table
R4 = {
    'C2a': (Fr(1288, 1287), [28/143, 56/429, 140/99, 112/39, 896/1287]),
    'C3': (Fr(175, 143), [math.sqrt(250880/552123)]),
    'P5': (Fr(77, 65), [0.0622348691, abs(complex(0.0417352860, 0.0609168609)), 1.0951854883]),
    'T1': (Fr(147, 143), [56/1287, 112/143, 112/117, 224/143, 560/429]),
    'T2': (Fr(5831, 5031), [math.sqrt(5770240/7913763), math.sqrt(19066880/278420571)]),
    'T3': (Fr(1750, 1287), [math.sqrt(90160/61347), math.sqrt(501760/552123)]),
    'T4': (1.185203461338846, [1.01209160489, 0.310692742362, 0.139251832964, 0.00573685922309]),
}
R5Q = {'T1': Fr(581, 572), 'T2': Fr(609, 559), 'T3': Fr(2751, 2288), 'T4': 1.104176947003101}


def nu_roots(a, b, c):
    d = math.sqrt(b * b - 4 * a * c)
    return [(-b + d) / (2 * a), (-b - d) / (2 * a)]


T5_NU = nu_roots(418161601, 6989958976, 28677390336)      # nu = s^2, the Result's variable; both roots negative
assert all(x < 0 for x in T5_NU)
R2 = {'C2b': (Fr(144, 143), [112/143, 168/143, 336/143, 504/143, 560/143]),
      'T5': (Fr(22, 13), [math.sqrt(153664/20449)] + [math.sqrt(-x) for x in T5_NU])}


def slot_levels(nmax=30):
    """The levels n <= nmax at which R2 = 2', R4 = Sym^2(2') and R5 = 2 (x) 2' occur in V_n restricted to 2I, by
    characters over 2I's 120 unit quaternions, independent of the instrument's code."""
    import itertools
    phi = (1 + 5 ** 0.5) / 2
    pts = []
    for i in range(4):
        for sg in (1, -1):
            v = [0, 0, 0, 0]
            v[i] = sg
            pts.append(tuple(v))
    pts += list(itertools.product((0.5, -0.5), repeat=4))
    base = (0.5 * phi, 0.5, 0.5 / phi, 0.0)
    for p in itertools.permutations(range(4)):
        if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0:
            for s in itertools.product((1, -1), repeat=4):
                pts.append(tuple(base[p[k]] * s[k] for k in range(4)))
    grp = sorted(set(tuple(round(x, 12) for x in q) for q in pts))
    assert len(grp) == 120

    def chi_n(n, c):
        th = math.acos(max(-1.0, min(1.0, c)))
        if abs(math.sin(th)) < 1e-12:
            return (n + 1) * (1 if c > 0 else (-1) ** n)
        return math.sin((n + 1) * th) / math.sin(th)

    def galois(t):
        for a, b in ((phi, -1 / phi), (-1 / phi, phi), (1 / phi, -phi), (-phi, 1 / phi)):
            if abs(t - a) < 1e-9:
                return b
        return t
    chis = {'R2': lambda t: galois(t), 'R4': lambda t: galois(t) ** 2 - 1, 'R5': lambda t: t * galois(t)}
    return {s: [n for n in range(nmax + 1) if round(sum(chi_n(n, g[0]) * chi(2 * g[0]) for g in grp) / 120) > 0]
            for s, chi in chis.items()}


# the registration's highest read point in each slot: R4's and R5's window tops, and T5's last decided point
TOP_EPS = {'R4': 72.0, 'R5': 32.0, 'R2': 0.25 * 2 ** (17 / 2)}
LAM0 = {'R4': 48.0, 'R5': 48.0, 'R2': 63.0}
N_LO = 16


def bands():
    """n1, the first level above N_LO at which each slot occurs, and the band edge sqrt(n1 (n1 + 2)) - sqrt(lam) at the
    highest read point, as convergence.band_edge computes it; checked against the bands the saved control ladders
    carry at the same lam (C2a at eps 72 in R4, C2b at T5's last decided point in R2)."""
    lv = slot_levels()
    assert lv['R4'][:4] == [6, 10, 14, 16] and lv['R2'][:2] == [7, 13] and lv['R5'][:2] == [6, 8]
    n1 = {s: min(n for n in lv[s] if n > N_LO) for s in lv}
    band = {s: math.sqrt(n1[s] * (n1[s] + 2)) - math.sqrt(LAM0[s] + TOP_EPS[s]) for s in lv}
    import glob
    for c, s in (('C2a', 'R4'), ('C2b', 'R2')):
        J = json.load(open(sorted(glob.glob(os.path.join(RUNS, f'*_sep_controls_{c}_ladders.json')))[-1], encoding='utf-8'))
        saved = [v['band'] for k, v in J.items() if k.startswith('rule_eps') and abs(float(k[8:]) - TOP_EPS[s]) < 1e-9]
        assert len(saved) == 1 and abs(saved[0] - band[s]) < 1e-9, (c, saved, band[s])
    return n1, band


def resolution_rows():
    rows = []
    def one(name, slot, Q, taus, s):
        lam0 = 63.0 if slot == 'R2' else 48.0
        Qf = float(Q)
        kap = 1 / (8 * math.sqrt(lam0) * Qf)
        eps, N = 0.25, 32
        margin = 2 * math.sqrt(U * N * (N + 2) * max(eps / Qf, 0.2))
        small = min(eps * kap * s * t for t in taus)
        rows.append((name, slot, kap, small, margin, (small - G * margin) / margin))
    for k in ('C2a', 'C3', 'P5'):
        one(k, 'R4', *R4[k], 1.0)
    one('C2b', 'R2', *R2['C2b'], 1.0)
    for k in ('T1', 'T2', 'T3', 'T4'):
        one(k, 'R4', *R4[k], 1.0)
        one(k, 'R5', R5Q[k], R4[k][1], 9 / 16)
    one('T5', 'R2', *R2['T5'], 1.0)
    return rows


def sci(x):
    m, e = f'{x:.2e}'.split('e')
    return f'{m}×10{"⁻" if int(e) < 0 else ""}{str(abs(int(e))).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))}'


def resolution_table():
    rows = resolution_rows()
    out = ['| case | slot | `κ` | smallest predicted `\\|λ\\|` at `ε = 0.25` | margin at `N = 32` | margins outside the gray zone |',
           '| --- | --- | --- | --- | --- | --- |']
    for name, slot, kap, small, margin, n in rows:
        out.append(f'| {name} | `{slot}` | {kap:.5f} | {sci(small)} | {sci(margin)} | {n:.0f} |')
    t4r5 = [n for name, slot, _, _, _, n in rows if (name, slot) == ('T4', 'R5')][0]
    return '\n'.join(out), f'{t4r5:.0f}'


def mean_seconds(fname, Ns):
    J = json.load(open(os.path.join(RUNS, fname), encoding='utf-8'))
    per = {}
    for k, v in J.items():
        m = re.match(r'N(\d+)_eps', k)
        if m and isinstance(v, dict) and 'seconds' in v and int(m.group(1)) in Ns:
            per.setdefault(int(m.group(1)), []).append(v['seconds'])
    assert set(per) == set(Ns), (fname, sorted(per))
    return sum(sum(s) / len(s) for s in per.values())


def costs():
    """Seconds per point at N = 16, 24 and 32 together, from the logged runs: the samples (each cutoff from the germ)
    of entries' sep_controls runs, and the ladders' N = 24 and 32 from D7 with N = 16 from the separation ladders."""
    import glob
    import hashlib
    used = {}

    def find(pat):
        hits = sorted(glob.glob(os.path.join(RUNS, pat)))
        assert hits, pat
        name = os.path.basename(hits[-1])
        used[name] = hashlib.sha256(open(hits[-1], 'rb').read()).hexdigest()
        return name
    samp = {c: mean_seconds(find(f'*_sep_controls_{c}_sample.json'), (16, 24, 32)) for c in ('C2a', 'C2b', 'C3')}
    lad = {}
    for c in ('C2a', 'C2b', 'C3'):
        hi = mean_seconds(find(f'*_d7_ladders_{c}.json'), (24, 32))
        lo = mean_seconds(find(f'*_sep_controls_{c}_ladders.json'), (16,)) if c != 'C3' else \
            mean_seconds(find('*_sep_controls_C3_ladders.json'), (16,))
        lad[c] = hi + lo
    out = os.path.join(RUNS, find('*_d6_theoremD_N16_24_32_40.out'))
    secs = [float(x) for x in re.findall(r'; ([0-9.]+) s;', open(out, encoding='utf-8').read())]
    c1 = sum(secs)
    r4s = (samp['C2a'] + samp['C3']) / 2
    r4l = (lad['C2a'] + lad['C3']) / 2
    # R5, measured two ways (DEVLOG: step 2 and the dry run's rerun): its coherent branch's development sample against
    # R4's development samples, and the dry run's R5 control against the dry run's R4 controls, each per point at
    # N = 16, 24 and 32 together; the low and high ratios bound the R5 rows
    r5_dev = mean_seconds(find('*_r5_control.json'), (16, 24, 32)) / r4s
    dry = {}
    for c in ('C1', 'C2a', 'C2b', 'C3', 'C2a_R5'):
        with open(os.path.join(RUNS, find(f'*_dry_{c}.json')), encoding='utf-8') as f:
            dry[c] = json.load(f)['seconds']
    r5_dry = (dry['C2a_R5'] / 4) / ((dry['C2a'] + dry['C3']) / 8)
    lo, hi = sorted((r5_dev, r5_dry))
    rng = lambda x: (x * lo, x * hi)                                     # noqa: E731
    h = dict(
        H_CTRL=(c1 + 4 * (samp['C2a'] + samp['C2b'] + samp['C3'])) / 3600,
        H_R5C=rng(4 * r4s / 3600),
        H_P5=4 * r4s / 3600,
        H_S4=8 * r4s / 3600,
        H_S5=rng(8 * r4s / 3600),
        H_L4=36 * r4l / 3600,
        H_L5=rng(30 * r4l / 3600),
        H_L2=18 * lad['C2b'] / 3600,
    )
    h['H_TOT'] = (sum(v if not isinstance(v, tuple) else v[0] for v in h.values()),
                  sum(v if not isinstance(v, tuple) else v[1] for v in h.values()))
    h['DRY_CTRL'] = sum(dry.values()) / 3600
    return h, dict(samp=samp, lad=lad, c1=c1, r5_dev=r5_dev, r5_dry=r5_dry, dry=dry), used


def main():
    global REF
    repo, ow = sys.argv[1], sys.argv[2]
    if '--base' in sys.argv:
        REF = git(repo, 'rev-parse', '--verify', sys.argv[sys.argv.index('--base') + 1] + '^{commit}').strip()
        print('MIT read at', REF)
    else:
        git(repo, 'fetch', '-q', 'origin')
    git(ow, 'fetch', '-q', 'upstream')
    src = open(os.path.join(HERE, 'm8_16_task_details.src.md'), encoding='utf-8').read()
    pages = {'CEN': f'{W}/slot-dynamics-census.md', 'SSB': f'{W}/soft-slot-branches.md',
             'SGS': f'{W}/slot-ground-states.md', 'HKI': f'{W}/hamiltonian-krein-identification.md',
             'REC': f'{W}/scripts/soft-slot-dynamics/RECORD.md'}
    sub = {}
    for key, path in pages.items():
        sha = last_commit(repo, path)
        sub[key], sub[f'{key}_URL'] = sha[:7], f'{GH}/{sha}/{path}'
    qx = f'{W}/scripts/soft-slot-dynamics-m8-15x/qualification'
    sha = git(repo, 'log', '-1', '--format=%H', REF, '--', qx + '/RESULT_2.md', qx + '/REGISTER_2.md').strip()
    assert re.fullmatch(r'[0-9a-f]{40}', sha)
    sub['QX'], sub['QX_URL'] = sha[:7], f'{GH}/{sha}/{qx}'
    sa, sa9 = slot_action_commits(ow)
    sub['SA'], sub['SA_URL'], sub['SA9'] = sa[:7], f'{GH}/{sa}/{W}/slot-action.md', sa9[:7]
    sub['M815T'] = m815_terms_commit(repo)
    sub['BOUNDARY'] = boundary()
    table, t4r5 = resolution_table()
    sub['RESOLUTION_TABLE'], sub['T4R5_MARGINS'] = table, t4r5
    h, rates, used = costs()
    for k, v in h.items():
        sub[k] = f'{v[0]:.1f} to {v[1]:.1f}' if isinstance(v, tuple) else f'{v:.1f}'
    sub['R5_LO'], sub['R5_HI'] = (f'{x:.1f}' for x in sorted((rates['r5_dev'], rates['r5_dry'])))
    n1, band = bands()
    for s in ('R2', 'R4', 'R5'):
        sub[f'N1_{s}'], sub[f'BAND_{s}'] = str(n1[s]), f'{band[s]:.2f}'
    sub['HALF_MIN'] = f'{min(band.values()) / 2:.2f}'
    ta, tb = sorted(math.sqrt(-x) for x in T5_NU)
    sub['T5_TAU_A'], sub['T5_TAU_B'] = f'{ta:.4f}', f'{tb:.4f}'
    rates['run files'] = used
    return src, sub, rates


def fill(src, sub):
    text = src
    for k, v in sub.items():
        text = text.replace('{{' + k + '}}', v)
    return text


if __name__ == '__main__':
    src, sub, rates = main()
    used = rates.pop('run files')
    print('rates (s per point, N 16/24/32):', {k: (round(v, 2) if isinstance(v, float) else {a: round(b) for a, b in v.items()})
                                                for k, v in rates.items()})
    print('provenance, the run files read (SHA-256):')
    for name in sorted(used):
        print(f'   {name} {used[name]}')
    for k in sorted(sub):
        if k not in ('BOUNDARY', 'RESOLUTION_TABLE'):
            print(f'{k}: {sub[k]}')
    text = fill(src, dict(sub, WORDS='WORDS'))
    words = len(re.findall(r'\S+', text))
    sub['WORDS'] = f'{round(words, -2):,}'
    text = fill(src, sub)
    left = re.findall(r'\{\{[A-Z0-9_]+\}\}', text)
    assert not left, left
    print(f'words: {words}, stated as about {sub["WORDS"]}')
    if '--write' in sys.argv:
        out = os.path.join(HERE, 'm8_16_task_details.md')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(text)
        print('written:', out)
