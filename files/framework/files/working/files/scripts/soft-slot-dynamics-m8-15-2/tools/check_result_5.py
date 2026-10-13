"""RESULT_5's quoted numbers against the records, each recomputed and anchored to its own sentence.
Usage: check_result_5.py RESULT_5 LOCATOR_FOLDER PATCH COMPARE_OUT [--mutations]. Exit 1 on any mismatch.
With --mutations, each planted change to a copy of the page must be caught."""
import os, re, sys, json, glob


def expected(loc, patch, compare_out):
    out = os.path.join(loc, 'out')
    rec = lambda n: json.load(open(os.path.join(out, n)))
    syn = rec('synthetic.json')['results']
    s_tests = [t for t in syn if t['test'].startswith('S')]
    n_arms = sum(len(t['arms']) for t in syn)
    all_ok = all(t['passed'] for t in syn) and all(a['caught'] for t in syn for a in t['arms'])
    tier = [a for a in [t for t in syn if t['test'] == 'A1'][0]['arms'] if a['label'] == "v4's tiered names restored"][0]
    tier_cases = sorted({b.split(':')[0] for b in tier['failed_checks']})
    words = {7: 'seven', 6: 'six', 8: 'eight', 5: 'five'}
    c2a = rec('t1_C2a_R4_R1R4.json')['brackets'][0]['levels']
    s3, s2 = c2a['3']['steps'][0], c2a['2']['steps'][0]
    r3 = rec('t1_C2a_R4_R3.json')['brackets'][0]['levels']['2']['steps'][0]
    c3 = rec('t1_C3_R4_R2R4.json')['brackets'][0]
    c3_n = sorted({len(c3['points'][lv]) for lv in c3['points']})
    c3_nl = sorted({p['nL'] for lv in c3['points'] for p in c3['points'][lv]})
    real = json.load(open(os.path.join(out, 'real.json')))['results']
    diffs = [re.search(r'\((\d+) differences\)', c[0]).group(1) for c in real['RESULT_4 reproduced']['checks']]
    chain = open(os.path.join(out, 'chain.log')).read()
    t0 = re.search(r'chain start \d{4}-\d\d-\d\dT(\d\d:\d\d):\d\dZ', chain).group(1)
    t1 = re.search(r'chain done \d{4}-\d\d-\d\dT(\d\d:\d\d:\d\d)Z', chain).group(1)
    stat = re.findall(r'^diff --git ', open(patch).read(), flags=re.M)
    plus = sum(1 for ln in open(patch) if ln.startswith('+') and not ln.startswith('+++'))
    minus = sum(1 for ln in open(patch) if ln.startswith('-') and not ln.startswith('---'))
    new_files = re.findall(r'^new file mode', open(patch).read(), flags=re.M)
    cmp_ = open(compare_out).read()
    eq = re.search(r'equal outside the new fields: (\d+); differing: (\[.*?\])', cmp_)
    r5 = rec('r5.json')
    refused = [c for c in r5['cases'] if c['expected'] == 'refused' and c['ok']]
    reg = [c for c in refused if c['case'] != "the instrument's manifest not the pinned one"]
    f3 = lambda x: f'{x:.3f}'
    need = [
        (f'run finished 2026-10-13T{t1[:5]}Z', 'title time'),
        (f'from {t0}Z to {t1[:5]}Z', 'status window'),
        (f'52 tests, with A7 and A11 counted by their plants (three and two), and {n_arms} arms', 'test and arm counts')
        if len(syn) == 52 and all_ok else ('<synthetic not all passing>', 'synthetic'),
        (f'| S1 to S18c | {sum(t["passed"] for t in s_tests)} of {len(s_tests)} pass', 'S count'),
        (f'6 files, {plus} lines added and {minus} removed, one of them new', 'diff stat') if len(stat) == 6 and len(new_files) == 1
        else ('<patch shape changed>', 'diff stat'),
        (f'fails at the {words[len(tier_cases)]} cases whose full cosine reaches 0.9 at every branch step, +1, 0.3 among them',
         'tiered arm') if '+1, 0.3' in tier_cases else ('<tiered arm misses +1, 0.3>', 'tiered arm'),
        (f'at level 3 the final interval {f3(s3["lo"])} to {f3(s3["hi"])}, read to {f3(s3["reading"][1])}, root {f3(s3["root"])}',
         'R1 level 3'),
        (f'at level 2 the final interval {f3(s2["lo"])} to {f3(s2["hi"])}, root {f3(s2["root"])}', 'R1 level 2'),
        (f'`n(L) = {c3_nl[0]}` at all {c3_n[0]} points per level', 'R2') if len(c3_n) == 1 and len(c3_nl) == 1
        else ('<C3 points vary>', 'R2'),
        (f'`ε = {f3(r3["failed_at"])}`, is recorded with its three failed attempts', 'R3 point')
        if len(r3['history']) == 3 else ('<R3 attempts not three>', 'R3 point'),
        ('residuals ' + ', '.join(f'`{float(f"{a[-1]["res"]:.1e}"):.1e}`'.replace('e-03', '×10⁻³') for a in r3['history'][:2])
         + f' and `{r3["history"][2][-1]["res"]:.1e}`'.replace('e-03', '×10⁻³'), 'R3 residuals'),
        (f'reported over `[{f3(r3["lo"])}, {f3(r3["hi"])}]`', 'R3 interval'),
        (f'the statistic reaches `{s3["continuity"]["largest"]:.2e}`'.replace('e-06', '×10⁻⁶') + ' (level 3) and '
         + f'`{s2["continuity"]["largest"]:.2e}`'.replace('e-06', '×10⁻⁶') + ' (level 2)', 'rule 11 values'),
        (f'value for value once § 4\'s fields are set aside: {diffs[0]} differences in each', 'RESULT_4 reproduced')
        if len(set(diffs)) == 1 and len(diffs) == 5 else ('<differences vary>', 'RESULT_4 reproduced'),
        (f'refuses a target in each of its {words[len(reg)]} registered cases, and in one more', 'R5 cases')
        if len(refused) == len(reg) + 1 else ('<R5 refusals changed>', 'R5 cases'),
        (f'Nineteen of the twenty are equal; S10 differs' if eq and eq.group(1) == '19' and eq.group(2) == "['S10']"
         else '<compare changed>', 'bench check'),
    ]
    return need, dict(r5_passed=r5['passed'], arms=[a['caught'] for a in r5['arms']], real_all=all(v['passed'] for v in real.values()))


def check(text, need, facts):
    bad = [f'{lab}: missing "{n}"' for n, lab in need if n not in text]
    if not (facts['r5_passed'] and all(facts['arms']) and facts['real_all']):
        bad.append(f'records: {facts}')
    return bad


if __name__ == '__main__':
    page, loc, patch, cmp_ = sys.argv[1:5]
    text = open(page).read()
    need, facts = expected(loc, patch, cmp_)
    bad = check(text, need, facts)
    print(f'RESULT_5: {len(need)} quoted numbers checked; mismatches: {len(bad)}')
    for b in bad:
        print('  ', b)
    if '--mutations' in sys.argv:
        plants = [('1369 lines added', '1368 lines added'), ('`2.63×10⁻⁶` (level 2)', '`2.64×10⁻⁶` (level 2)'),
                  ('`ε = 14.536`', '`ε = 14.535`'), ('the seven cases', 'the six cases'), ('root 34.042', 'root 34.043'),
                  ('at all 9 points', 'at all 8 points'), ('`3.2×10⁻³`', '`3.1×10⁻³`'), ('0 differences in each', '1 differences in each'),
                  ('its eight registered cases', 'its seven registered cases'), ('Nineteen of the twenty', 'Eighteen of the twenty'),
                  ('and 55 arms', 'and 54 arms'), ('from 03:08Z', 'from 03:09Z'), ('`[14.243, 14.828]`', '`[14.243, 14.829]`')]
        caught = 0
        for old, new in plants:
            assert text.count(old) == 1, f'plant anchor not unique: {old}'
            caught += bool(check(text.replace(old, new), need, facts))
        print(f'planted mutations caught: {caught} of {len(plants)}')
        bad = bad or ([] if caught == len(plants) else ['a planted mutation was not caught'])
    sys.exit(1 if bad else 0)
