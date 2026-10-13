"""The M8.15.2 terms' quoted numbers against their sources: recon_numbers.out, the locator v2's records, M8.15.1's run record,
the instrument's manifest and M8.15.1's terms file. Each number is recomputed and anchored to its own sentence.
Usage: check_terms_numbers.py TERMS RECON_OUT LOCATOR_FOLDER M815_1_RECORD MANIFEST M815_1_TERMS [--mutations]."""
import re, sys, json, os, hashlib, datetime


def grab(pattern, text, flags=re.S):
    m = re.search(pattern, text, flags)
    if not m:
        raise SystemExit(f'source pattern not found: {pattern}')
    return m.groups()


def needs(recon, loc, record, manifest, old_terms):
    n = []
    # what failed: ends and failing midpoints, level 3 and level 2
    for t in ('T2_R4', 'T3_R5'):
        e3 = grab(rf'== {t} level 3: ends ([\d.]+), ([\d.]+); fails at ([\d.]+)', recon)
        e2 = grab(rf'== {t} level 2: ends ([\d.]+), ([\d.]+); fails at ([\d.]+)', recon)
        h = grab(rf'== {t} level 3: .*?lo  [\d.]+: .*? h (\d+),.*?hi  [\d.]+: .*? h (\d+),', recon)
        tr = lambda x: x.rstrip('0') + '0' if x.endswith('.000000') else x
        row = f'| {t.replace("_", "/")} | {e3[0]}, {e3[1]}; {e3[2]} | {tr(e2[0])}, {tr(e2[1])}; {e2[2]} | {h[0]} → {h[1]} |'
        n.append((row, f'what failed, {t}'))
    widths = [grab(rf'== {t} level 3: .*?width at the failure ([\d.e+-]+) of the lower end', recon)[0] for t in ('T2_R4', 'T3_R5')]
    sup = lambda x: x.replace('e-03', '×10⁻³')
    n.append((f'at widths of `{sup(widths[0])}` (T2/R4) and `{sup(widths[1])}` (T3/R5) of the lower end', 'widths'))
    so = [grab(rf'== {t} level {lv}:.*?slowest pair overlap: [\d.]+ [\d.e+-]+, [\d.]+ ([\d.e+-]+),', recon)[0]
          for t, lv in (('T3_R5', 3), ('T3_R5', 2), ('T2_R4', 3), ('T2_R4', 2))]
    ok_small = all(float(x) < 1e-11 for x in so[2:])
    n.append((f'peaks at T3/R5\'s failing midpoints, {so[0]} at level 3 and {so[1]} at level 2, and is below `10⁻¹¹` at T2/R4\'s'
              if ok_small else '<T2/R4 overlap not below 1e-11>', 'slowest pair'))
    # the doublets at the failing midpoints: the overlaps strictly between 0.4 and 0.9 on the failing points' near-zero lines
    mids = []
    for t in ('T2_R4', 'T3_R5'):
        for lv in (3, 2):
            blk = grab(rf'(== {t} level {lv}:.*?)(?:\n==|\Z)', recon)[0]
            fail = grab(r'fails at ([\d.]+)', blk)[0]
            nz = re.findall(rf'near zero at {re.escape(fail)}[^\n]*?:([^\n]*)', blk) or re.findall(r'mid[^\n]*\n\s+near zero[^:]*:([^\n]*)', blk)
            for line in nz:
                mids += [float(x) for x in re.findall(r'\(([\d.]+)\)', line)]
    mid_ov = sorted(x for x in mids if 0.4 < x < 0.9)
    if mid_ov:
        n.append((f'both doublets\' overlaps with `P` sit at {mid_ov[0]:.2f} to {mid_ov[-1]:.2f}', 'doublets at the failing midpoints'))
    # stated before the run
    z = {t: [grab(rf'== {t} level {lv}:.*?interpolated zero ([\d.]+)', recon)[0] for lv in (3, 2)] for t in ('T2_R4', 'T3_R5')}
    n.append((f'| The crossing pair\'s interpolated zero, level 3 / level 2 | {z["T2_R4"][0]} / {z["T2_R4"][1]} | {z["T3_R5"][0]} / {z["T3_R5"][1]} |',
              'interpolated zeros'))
    ch = {(t, lv): grab(rf'== {t} level {lv}:.*?n\(L\) changes in (\([\d.]+, [\d.]+\])', recon)[0] for t in ('T2_R4', 'T3_R5') for lv in (3, 2)}
    n.append((f'| Where `n(L)` changes, level 3 | {ch[("T2_R4", 3)]} | {ch[("T3_R5", 3)]} |', 'n(L) change level 3'))
    n.append((f'| Where `n(L)` changes, level 2 | {ch[("T2_R4", 2)]} | {ch[("T3_R5", 2)]} |', 'n(L) change level 2'))
    ang = {(t, lv): grab(rf'== {t} level {lv}:.*?angle ([\d.]+) deg, cosine ([\d.]+)', recon) for t in ('T2_R4', 'T3_R5') for lv in (3, 2)}
    fa = lambda a: f'{a[0]}° ({a[1]})'
    n.append((f'| The two-level identity angle, level 3 / level 2 | {fa(ang[("T2_R4", 3)])} / {fa(ang[("T2_R4", 2)])} | '
              f'{fa(ang[("T3_R5", 3)])} / {fa(ang[("T3_R5", 2)])} |', 'identity angles'))
    t2c = sorted(float(ang[('T2_R4', lv)][1]) for lv in (3, 2))
    n.append((f'while T2/R4 passes at {t2c[0]:.2f}', 'identity prediction'))
    g2 = grab(r'== T2_R4 level 2:.*?gap [\d.e+-]+ to ([\d.e+-]+)', recon)[0]
    g5 = grab(r'== T3_R5 level 2:.*?gap [\d.e+-]+ to ([\d.e+-]+)', recon)[0]
    n.append((f'`n(L)` changes up to {100 * float(g2):.2f}% above the interpolated zero', 'T2/R4 level-2 gap'))
    n.append((f'On T3/R5 the change lies within {100 * float(g5):.2f}% of the zero', 'T3/R5 level-2 gap'))
    # the secondary
    sec = grab(r"local slopes from ([\d.]+) to ([\d.]+) are \+([\d.]+), \+[\d.]+, \+([\d.]+), and it crosses zero near ([\d.]+); "
               r"on the second path, over the (\d+) points the bisection evaluated between ([\d.]+) and ([\d.]+), it fits "
               r"(-[\d.]+)\(eps - ([\d.]+)\), residuals at most ([\d.e+-]+); the slope ratio (-[\d.]+) to (-[\d.]+)", recon)
    n.append((f'on the ladder\'s path from {sec[0]} to {sec[1]}, the critical eigenvalue\'s local slopes are +{sec[2]} to +{sec[3]}, '
              f'and it crosses zero near {sec[4]}', 'secondary slopes'))
    n.append((f'it fits `−{sec[8][1:]}(ε − {sec[9]})` over the {sec[5]} points the bisection evaluated between {sec[6]} and {sec[7]}, '
              f'with residuals at most `{sup(sec[10])}`', 'secondary fit'))
    n.append((f'The slope ratio, −{sec[11][1:]} to −{sec[12][1:]},', 'slope ratio'))
    # the two-level model and the bounds
    xl = grab(r'fails where \|g \+ delta\| < ([\d.]+) kappa, so above kappa/delta = ([\d.]+)', recon)
    n.append((f'fails where `|g + δ| < {xl[0]}κ`. Above `κ/δ = {xl[1]}`', 'exchanged-lift threshold'))
    w = grab(r'== v6, distinct genuine directions outside P:[^\n]*?agree outside P to at most ([\d.]+)', recon)[0]
    n.append((f'two different genuine directions agree outside `P` to at most {w}', 'Wielandt bound'))
    ua = grab(r"Unit A's counterexample: full cosine ([\d.]+); outside P ([\d.]+);", recon)
    n.append((f'agreeing outside `P` at {ua[1]} and in full at {ua[0]}', 'counterexample'))
    fit = grab(r'gives kappa/delta T2/R4 level 3 ([\d.]+); T2/R4 level 2 ([\d.]+); T3/R5 level 3 ([\d.]+); T3/R5 level 2 ([\d.]+); '
               r"T2/R4 level 2's next midpoints meet the clean interval ([\d.]+) to ([\d.]+) at ([\d.]+)", recon)
    n.append((f'gives `κ/δ` of {fit[0]} (T2/R4, level 3), {fit[1]} (T2/R4, level 2), {fit[2]} (T3/R5, level 3) and {fit[3]} (T3/R5, level 2)',
              'rough fit'))
    n.append((f'meet a clean interval from {fit[4]} to {fit[5]}, at {fit[6]}', 'clean interval'))
    # the tolerance
    tol = grab(r"controls' largest statistic is ([\d.]+)e-04 \((\w+), level (\d), at ([\d.]+)\); ten times it is ([\d.]+)e-03", recon)
    n.append((f'`τ_c = {tol[4]}×10⁻³`, is ten times the largest statistic over the control brackets\' pools, at both levels: '
              f'`{tol[0]}×10⁻⁴`, on {tol[1]} at level {tol[2]} at {tol[3]}', 'tolerance'))
    full = grab(r'full ladders, ([\d.]+) to ([\d.]+), the statistic reaches ([\d.]+)e-04 \((\w+), level (\d), at ([\d.]+)\)', recon)
    n.append((f'Over the controls\' full ladders, {full[0]} to {full[1]}, the statistic reaches `{full[2]}×10⁻⁴` ({full[3]}, level {full[4]}, at {full[5]})',
              'full ladders'))
    n.append((f'`τ_c = {tol[4]}×10⁻³`; duplicate targets', 'frozen tolerance'))
    r11 = grab(r"primaries at most ([\d.]+)e-04 \(T2/R4\) and ([\d.]+)e-04 \(T3/R5\), ([\d.]+) times the controls' largest; "
               r"the controls' steps at most ([\d.]+)e-06", recon)
    n.append((f'the primaries read at most `{r11[0]}×10⁻⁴` (T2/R4) and `{r11[1]}×10⁻⁴` (T3/R5), {r11[2]} times the controls\' largest, '
              f'and the controls\' steps at most `{r11[3]}×10⁻⁶`', 'rule 11 on M8.15.1'))
    sw = grab(r"level 3's starting interval [\d.]+ to [\d.]+, at [\d.]+ [\d.e+-]+, at ([\d.]+) ([\d.]+)e-03, at ([\d.]+) ([\d.]+); "
              r"level 2's, [\d.]+ to ([\d.]+), at [\d.]+ ([\d.]+);", recon)
    n.append((f'level 3\'s starting interval reads `{sw[1]}×10⁻³` at {sw[0]} and {sw[3]} at {sw[2]}, and level 2\'s reads {sw[5]} at {float(sw[4]):g}',
              'switches'))
    mult = grab(r'both switches stop\): ([\d.]+) to ([\d.]+)e\+04', recon)
    n.append((f'Every multiple from {mult[0]} to `{mult[1]}×10⁴` gives one outcome on these records', 'multiples'))
    # RESULT_5's records
    out = os.path.join(loc, 'out')
    syn = json.load(open(os.path.join(out, 'synthetic.json')))['results']
    arms = sum(len(t['arms']) for t in syn)
    ok = all(t['passed'] for t in syn) and all(a['caught'] for t in syn for a in t['arms'])
    n.append((f'{len(syn)} synthetic tests with {arms} arms' if ok else '<synthetic not all passing>', 'tests and arms'))
    real = json.load(open(os.path.join(out, 'real.json')))['results']
    d = {re.search(r'\((\d+) differences\)', c[0]).group(1) for c in real['RESULT_4 reproduced']['checks']}
    n.append((f'All five control records reproduce RESULT_4\'s with {d.pop()} differences' if len(d) == 1 else '<differences vary>',
              'reproduced'))
    lg = max(s['continuity']['largest'] for f in ('t1_C2a_R4_R1R4.json', 't1_C2a_R4_R3.json', 't1_C2a_R4_R3arm.json', 't1_C2a_R4_R1arm.json')
             for b in json.load(open(os.path.join(out, f)))['brackets'] for L in b['levels'].values() for s in L['steps'])
    n.append((f'the continuity statistic reads at most `{lg:.2e}`'.replace('e-06', '×10⁻⁶') + ' on their steps', 'control statistic'))
    # M8.15.1's run times, from its record
    rt = grab(r'T2/R4 ran from (\S+)Z to (\S+)Z, and T3/R5 from (\S+)Z to (\S+)Z', record)
    t = [datetime.datetime.strptime(x.strip('`'), '%Y-%m-%dT%H:%M:%S') for x in rt]
    h2, h5 = (t[1] - t[0]).total_seconds() / 3600, (t[3] - t[2]).total_seconds() / 3600
    n.append((f'M8.15.1\'s two runs took {h2 + h5:.1f} hours, {h5:.1f} of them on T3/R5', 'run times'))
    # hashes, computed from the files
    n.append((f'`{hashlib.sha256(open(manifest, "rb").read()).hexdigest()[:8]}…`, the instrument\'s `out/MANIFEST.json`', 'manifest pin'))
    n.append((f'SHA-256 `{hashlib.sha256(open(old_terms, "rb").read()).hexdigest()[:8]}…`, the prefix', "M8.15.1's terms hash"))
    def find(name):
        """A file beside this checker or one folder up: the bench keeps it in tools/, the frozen folder in scope/."""
        here = os.path.dirname(os.path.abspath(__file__))
        for d in (here, os.path.dirname(here)):
            if os.path.exists(os.path.join(d, name)):
                return os.path.join(d, name)
        raise SystemExit(f'{name} not found beside the checker or one folder up')
    reg = open(find('REGISTER_5.md')).read()
    stamp = grab(r'Registered at (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', reg)[0]
    n.append((f'(`REGISTER_5.md`, {stamp})', 'registration stamp'))
    # v2: the continuity check's two consequences for the targets (recon v6)
    fc = grab(r"T3/R5's guard region and primary bracket both start at ([\d.]+), the pool's lowest point at both levels, "
              r"so a step in its first cell, to ([\d.]+), would have a compared point with one predecessor; M8.15.1 has (\d+) "
              r"steps there\. T2/R4's guard region starts at ([\d.]+), below its bracket's.*?within ([\d.]+)e-16 of it, relative, "
              r"on the targets' brackets, and M8.15.1's primaries have (\d+) failing grid points", recon)
    n.append((f"T3/R5's guard region and primary bracket both start at {fc[0]}, the pool's lowest point at both levels. "
              f"So a step in its first cell, up to {fc[1]}, has a compared point with one point below it", 'first cell'))
    n.append((f'M8.15.1 had {fc[2]} steps there. T2/R4\'s guard region starts below its bracket, at {fc[3]}', 'first cell steps'))
    n.append((f'within `{fc[4]}×10⁻¹⁶` relative on the targets\' brackets', 'lone failing grid point'))
    n.append((f'M8.15.1\'s primaries had {fc[5]} failing grid points', 'failing grid points'))
    # v2: where the mixed-overlap rule fires on the mock, from the registered outcomes (plant_oracle.out's summary)
    orc = open(find('plant_oracle.out')).read()
    mixed = sorted(set(re.findall(r'^   (A1, slope sign [+-]1, kappa/delta [\d.]+|A2/A28, .*?kappa/delta [\d.]+), level \d: '
                                  r'.*?Unresolved \(mixed overlap\)', orc, flags=re.M))
                   | set(re.findall(r'^   (A2/A28, .*?kappa/delta [\d.]+): .*?Unresolved \(mixed overlap\)', orc, flags=re.M)))
    a1 = sorted({re.search(r'kappa/delta ([\d.]+)', m).group(1) for m in mixed if m.startswith('A1')})
    a1_signs = sorted({re.search(r'slope sign ([+-]1)', m).group(1) for m in mixed if m.startswith('A1')})
    a2 = sorted({re.search(r'kappa/delta ([\d.]+)', m).group(1) for m in mixed if m.startswith('A2')})
    if a1 == ['2'] and a1_signs == ['+1', '-1'] and a2 == ['2']:
        n.append(('the rule fires on the mock: A1 at `κ/δ = 2`, at both slopes, and A2 at `2δ`', 'mixed overlap fires'))
    else:
        n.append((f'<mixed overlap fires at A1 {a1} {a1_signs}, A2 {a2}>', 'mixed overlap fires'))
    return n


def check(text, need):
    return [f'{lab}: missing "{s}"' for s, lab in need if s not in text]


if __name__ == '__main__':
    terms, recon, loc, record, manifest, old_terms = sys.argv[1:7]
    text = open(terms).read()
    need = needs(open(recon).read(), loc, open(record).read(), manifest, old_terms)
    bad = check(text, need)
    print(f'terms: {len(need)} quoted numbers checked; mismatches: {len(bad)}')
    for b in bad:
        print('  ', b)
    if '--mutations' in sys.argv:
        plants = [('16.284772 |', '16.284773 |'), ('`3.18×10⁻³` (T2/R4)', '`3.19×10⁻³` (T2/R4)'), ('0.868 at level 3', '0.869 at level 3'),
                  ('15.8° (0.962)', '15.8° (0.963)'), ('2.95% above', '2.96% above'), ('+0.091 to +0.102', '+0.091 to +0.103'),
                  ('`|g + δ| < 1.580κ`', '`|g + δ| < 1.581κ`'), ('at most 0.105', 'at most 0.106'), ('3.08 (T2/R4, level 2)', '3.09 (T2/R4, level 2)'),
                  ('at 16.5178', 'at 16.5179'), ('`3.4601×10⁻⁴`, on C3', '`3.4602×10⁻⁴`, on C3'), ('`4.1580×10⁻⁴`', '`4.1581×10⁻⁴`'),
                  ('`7.5×10⁻⁴` (T3/R5)', '`7.6×10⁻⁴` (T3/R5)'), ('55.8 at 32', '55.9 at 32'), ('`2.4×10⁴` gives', '`2.5×10⁴` gives'),
                  ('52 synthetic tests', '51 synthetic tests'), ('with 0 differences', 'with 1 differences'), ('`2.63×10⁻⁶` on their', '`2.64×10⁻⁶` on their'),
                  ('took 6.5 hours', 'took 6.4 hours'), ('`2b9864ab…`', '`2b9864ac…`'), ('`fc566c04…`, the prefix', '`fc566c05…`, the prefix'),
                  ('2026-10-13T02:17:12Z)', '2026-10-13T02:17:13Z)'), ('sit at 0.49 to 0.87', 'sit at 0.49 to 0.88'),
                  ('up to 11.899495', 'up to 11.899496'), ('within `2.0×10⁻¹⁶`', 'within `2.1×10⁻¹⁶`'),
                  ('M8.15.1 had 0 steps there', 'M8.15.1 had 1 steps there'), ('had 0 failing grid points', 'had 1 failing grid points'),
                  ('A1 at `κ/δ = 2`, at both slopes', 'A1 at `κ/δ = 1`, at both slopes')]
        caught = 0
        for old, new in plants:
            if text.count(old) != 1:
                print(f'   plant anchor not unique ({text.count(old)}): {old}')
                continue
            caught += bool(check(text.replace(old, new), need))
        print(f'planted mutations caught: {caught} of {len(plants)}')
        bad = bad or ([] if caught == len(plants) else ['a planted mutation was not caught'])
    sys.exit(1 if bad else 0)
