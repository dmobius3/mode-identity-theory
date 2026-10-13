"""RECORD.md's numbers, recomputed from the files they come from: the target records, the run's logs, the pre-run record,
the post-run files and the terms. Each table row is rebuilt from the records and must stand in RECORD.md as a line; each
number in the prose is rebuilt and must stand there as written; each hash in the file tables must be its file's.

  python3 check_record.py TERMS [--mutations]     TERMS: M8.15.2's terms file, as merged in OpenWave 1e8a6e2b

With --mutations, each arm edits a copy of RECORD.md's text and must fail; the parent must pass first. Prints the outcome,
writes check_record.out beside this script, and exits 1 on any failure."""
import os, sys, json, re, ast, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
LOC = os.path.dirname(HERE)
OUT = os.path.join(LOC, 'out')
sys.path.insert(0, os.path.join(LOC, 'tests'))
sys.path.insert(0, LOC)
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
SUP = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')


def f4(x):
    """A value as the record writes it: four decimals, trailing zeros dropped."""
    return f'{x:.4f}'.rstrip('0').rstrip('.')


def lab(x):
    """A ladder point as the record names it: four significant figures."""
    return f'{x:.4g}'


def sci(x, n=2):
    m, e = f'{x:.{n}e}'.split('e')
    return f'{m}×10{str(int(e)).translate(SUP)}'


def counts(p):
    return f'({p["nL"]}, {p["nS"]}, {p["nB"]}, {p["h"]})'


def verdict(v, why):
    return v + (f' ({", ".join(why)})' if why else '')


def expected(terms_path):
    """Every line and phrase RECORD.md must hold, as (what, text, kind), kind 'line' or 'phrase'."""
    E = []
    add = lambda what, text, kind='phrase': E.append((what, text, kind))
    recs = {t: json.load(open(os.path.join(OUT, f't1_{t}.json'))) for t in ('T2_R4', 'T3_R5')}
    sides = {}
    for t, r in recs.items():
        case = t.replace('_', '/')
        add(f'{case} start and finish', f'{r["started"]} to {r["finished"]}')
        # the ladder's types, run-length grouped as the record writes them
        parts, i, ty = [], 0, r['types']
        while i < len(ty):
            j = i
            while j + 1 < len(ty) and ty[j + 1]['type'] == ty[i]['type'] == 'Elliptic' and not ty[j + 1]['why']:
                j += 1
            if j > i:
                parts.append(f'Elliptic from {lab(ty[i]["eps"])} to {lab(ty[j]["eps"])} ({j - i + 1} points)')
            else:
                parts.append(f'{ty[i]["type"]} at {lab(ty[i]["eps"])}' + (f' ({", ".join(ty[i]["why"])})' if ty[i]['why'] else ''))
            i = j + 1
        add(f'{case} ladder types', '; '.join(parts))
        b = r['brackets'][0]
        add(f'{case} bracket heading', f'### {case}, primary ({f4(b["brackets"]["3"][0])} to {f4(b["brackets"]["3"][1])})', 'line')
        for lv in ('3', '2'):
            pts = {p['eps']: p for p in b['points'][lv]}
            for s in b['levels'][lv]['steps']:
                st = s['status'] + (f' ({s["reason"]})' if s.get('reason') else '')
                ce, ne, rd = s['clean_ends'], s['nL_ends'], s['reading']
                root = f4(s['root']) if s['status'] in ('genuine', 'structural') else 'none'
                add(f'{case} L{lv} {st} row',
                    f'| {lv} | {st} | {f4(ce[0])} to {f4(ce[1])} | {f4(ne[0])} to {f4(ne[1])} | {counts(pts[ce[0]])} to '
                    f'{counts(pts[ce[1]])} | {f4(rd[0])} to {f4(rd[1])} | {root} | {"yes" if s["branch_step"] else "no"} |', 'line')
                c = s['continuity']
                kinds = [x['kind'] for x in c['comparisons']]
                assert c['verdict'] == 'passes' and not c['duplicates'] and not any(x.get('degenerate') for x in c['comparisons'])
                add(f'{case} L{lv} {st} continuity count',
                    f'{len(kinds)} comparisons ({kinds.count("along the span")} along the span and {kinds.count("across the step")} across the step)')
                add(f'{case} L{lv} {st} continuity largest', sci(c['largest']))
                if s['status'] == 'genuine':
                    side = 'below' if s['root'] < s['nL_ends'][0] else ('above' if s['root'] > s['nL_ends'][1] else 'inside')
                    sides.setdefault(case, []).append((lv, s['root'], side, s['nL_ends']))
                if s.get('identity_cosines_genuine'):
                    ic = s['identity_cosines_genuine']
                    assert max(ic['full']) - min(ic['full']) < 5e-5 and max(ic['outside_P']) - min(ic['outside_P']) < 5e-7
                    add(f'{case} L{lv} identity cosine, in full', f'{min(ic["full"]):.4f}')
                    add(f'{case} L{lv} identity cosine, outside P', f'{min(ic["outside_P"]):.6f}')
                for m in s.get('midpoints', []):
                    add(f'{case} L{lv} passed point {f4(m["eps"])}', f4(m['eps']))
                    add(f'{case} L{lv} passed point counts', counts(pts[m['eps']]))
                if s['status'] == 'Unresolved':
                    add(f'{case} L{lv} root field midpoint', f'midpoint, {f4((ce[0] + ce[1]) / 2)}')
            unb = sorted(e for e, p in pts.items() if not p['balanced'])
            if unb:
                add(f'{case} L{lv} unbalanced', f'{len(unb)} points, from `ε = {f4(unb[0])}` to `{f4(unb[-1])}`')
        for sn in b['steps_named']:
            for g in sn['guards']:
                d = f'`d = {g["d"]:.2f}`' if g['kind'] == 'offset' else 'region end'
                se = verdict(g['same_eps']['verdict'], g['same_eps']['why']) if 'same_eps' in g else 'not read'
                add(f'{case} guard {g["side"]} {d}',
                    f'  | {g["side"]} | {d} | {f4(g["eps3"])} | {f4(g["eps2"])} | {verdict(g["verdict"], g["why"])} | '
                    f'{"yes" if g["decided"] else "no"} | {se} |', 'line')
                assert g['counting']
                if g['kind'] == 'offset':
                    assert g['point3']['balanced'] and g['point2']['balanced']
            assert not sn['collisions'] and not sn['unbalanced_between'] and sn['clause3_trigger'] is True
            nm = sn['name']
            lo, up = nm['readings']['lower'], nm['readings']['upper']
            add(f'{case} readings', f'{lo["verdict"]} at {f4(lo["eps3"])} at level 3 and {f4(lo["eps2"])} at level 2, and '
                f'{up["verdict"]} at {f4(up["eps3"])} and {f4(up["eps2"])}')
            add(f'{case} reading offsets', f'{lo["verdict"]} at `d = {lo["d"]:.2f}` below, and {up["verdict"]} at `d = {up["d"]:.2f}` above')
            loc = nm['location']
            add(f'{case} location', f'{f4(loc["root3"])} at level 3, between the clean ends {f4(loc["interval3"][0])} and '
                f'{f4(loc["interval3"][1])}, and {f4(loc["root2"])} at level 2, between {f4(loc["interval2"][0])} and '
                f'{f4(loc["interval2"][1])}, a cross-level shift of {sci(loc["shift"])}')
            n3, n2 = sn['step3']['nL_ends'], sn['step2']['nL_ends']
            assert not (n3[0] <= loc['root3'] <= n3[1]) and not (n2[0] <= loc['root2'] <= n2[1])
            add(f'{case} the n(L) ends against the zeros', f'`n(L)` changes within {f4(n3[0])} to {f4(n3[1])} at level 3 and '
                f'{f4(n2[0])} to {f4(n2[1])} at level 2, and neither zero lies inside its level\'s `n(L)` ends')
        for n in b['names']:
            add(f'{case} name', f'"{n["name"]}"')
        sd = sides.get(case, [])
        if len(sd) == 1:
            lv, z, side, ne = sd[0]
            add(f'{case} the zero against the n(L) ends', f'Their interpolated zero, {f4(z)}, lies {side} the `n(L)` ends, '
                f'{f4(ne[0])} to {f4(ne[1])}, which bracket where `n(L)` changes')
        elif len(sd) == 2:
            (l3, z3, s3, e3), (l2, z2, s2_, e2) = sd
            assert s3 == s2_ and (l3, l2) == ('3', '2')
            add(f'{case} the zeros against the n(L) ends', f'Their interpolated zeros, {f4(z3)} at level 3 and {f4(z2)} at level 2, '
                f'lie {s3} the `n(L)` ends, {f4(e3[0])} to {f4(e3[1])} and {f4(e2[0])} to {f4(e2[1])}, which bracket where `n(L)` changes')
    # the adjudicated name and the continuity sentence
    adj = open(os.path.join(LOC, 'adjudicate_targets_postrun_2026-10-13.out')).read()
    q = re.search(r'^primary: (.*?)  \[the record: a located change of type\]$', adj, re.M).group(1)
    add('the adjudicated name, as adjudicate.py prints it', f'"{q}"')
    terms = open(terms_path).read()
    assert sha(terms_path) == json.load(open(os.path.join(OUT, 'FROZEN.json')))['terms_sha256'], 'the terms file is not the guard\'s'
    cs = re.search(r'this sentence stands wherever the name is reported: "([^"]+)"', terms).group(1)
    add("the continuity check's limit, in the terms' words", f'"{cs}"')
    # custody numbers
    pre = json.load(open(os.path.join(OUT, 'prerun_check.json')))
    assert all(c['ok'] for c in pre['checks'])
    add('the pre-run checks', f'The {len(pre["checks"])} checks in `out/prerun_check.json` passed at {pre["stamp"]}')
    chain = open(os.path.join(OUT, 'target_chain.log')).read()
    for who in ('locator v2', 'instrument folder'):
        n_ok, n = re.search(rf'post-run: {who} SHA256SUMS passes \((\d+) of (\d+)\)', chain).groups()
        add(f'post-run {who} SHA256SUMS', f'{n_ok} of {n}')
    assert 'unchanged: True; the instrument\'s FROZEN.json unchanged: True' in chain
    rfc = open(os.path.join(LOC, 'record_frozen_check_postrun_2026-10-13.out')).read()
    n_pts, st = re.search(r'points: (\d+); by fast-spectrum state: (\{.*\})', rfc).groups()
    st = ast.literal_eval(st)
    assert set(st) == {'not needed', 'skipped'} and 'record check: ALL PASS' in rfc
    add('the frozen-record check', f'It reads {n_pts} points, {st["not needed"]} "not needed" and {st["skipped"]} "skipped"')
    ctr = open(os.path.join(HERE, 'check_target_records.out')).read()
    assert ctr.rstrip().endswith('ALL PASS')
    n_arms = ctr.count('  arm: ')
    assert n_arms == ctr.count(': caught by')
    add('the regression arms', f'with {["no", "one", "two", "three", "four", "five", "six", "seven", "eight"][n_arms]} mutation arms, each caught')
    ent = {t: re.findall(rf"PASS  {re.escape(t)}: the ladder's [^:]+: (\d+) of M8\.15\.1's (\d+) entries", ctr) for t in ('T2/R4', 'T3/R5')}
    for t, rows in ent.items():
        assert all(a == b_ for a, b_ in rows) and len(rows) == 4
    add('the ladder regression counts', f'{", ".join(a for a, _ in ent["T2/R4"][:3])} and {ent["T2/R4"][3][0]} entries on T2/R4, and '
        f'{", ".join(a for a, _ in ent["T3/R5"][:3])} and {ent["T3/R5"][3][0]} on T3/R5, all equal')
    br = {t: re.findall(rf"PASS  {re.escape(t)}: the primary bracket, level \d: (\d+) of M8\.15\.1's (\d+) points", ctr) for t in ('T2/R4', 'T3/R5')}
    add('the bracket regression counts', f'on T2/R4, {br["T2/R4"][0][0]} of {br["T2/R4"][0][1]} at level 3 and {br["T2/R4"][1][0]} of '
        f'{br["T2/R4"][1][1]} at level 2; on T3/R5, {br["T3/R5"][0][0]} of {br["T3/R5"][0][1]} and {br["T3/R5"][1][0]} of {br["T3/R5"][1][1]}')
    return E


def hash_rows(text):
    """Each file table row's hash against its file's: (path, ok)."""
    out = []
    for path, h in re.findall(r'^  \| `([^`]+)`(?:[^|]*)\| `([0-9a-f]{64})` \|$', text, re.M):
        p = os.path.normpath(os.path.join(LOC, path))
        out.append((path, os.path.exists(p) and sha(p) == h))
    return out


def check(text, terms_path):
    res = []
    lines = set(text.splitlines())
    for what, t, kind in expected(terms_path):
        ok = (t in lines) if kind == 'line' else (t in text)
        res.append((f'{what}: {t[:90]}', ok))
    hr = hash_rows(text)
    res.append((f'the file tables: {sum(ok for _, ok in hr)} of {len(hr)} hashes are their files\'', bool(hr) and all(ok for _, ok in hr) and len(hr) == 15))
    res.append(('no em-dash', '—' not in text))
    return res


def arms():
    return [
        ('a root off in its last digit', lambda t: t.replace('| 16.2807 |', '| 16.2808 |', 1)),
        ('a guard verdict changed', lambda t: t.replace('| upper | `d = 0.05` | 16.5832 | 16.6252 | Hyperbolic |', '| upper | `d = 0.05` | 16.5832 | 16.6252 | Elliptic |', 1)),
        ('a continuity statistic transposed', lambda t: t.replace('3.75×10⁻⁴', '3.57×10⁻⁴', 1)),
        ('a hash changed', lambda t: re.sub(r'(\| `out/t1_T3_R5\.json` \| `)([0-9a-f])', lambda m: m.group(1) + ('0' if m.group(2) != '0' else '1'), t, count=1)),
        ('the point count changed', lambda t: t.replace('It reads 215 points', 'It reads 216 points', 1)),
        ("the continuity check's limit dropped", lambda t: t.replace('least of all where two branches share `m`.', 'least of all where two branches meet.', 1)),
        ('a count at a clean end changed', lambda t: t.replace('(5, 2, 5, 0) to (7, 2, 7, 0)', '(5, 2, 5, 0) to (7, 2, 5, 0)', 1)),
        ('an identity cosine changed', lambda t: t.replace('0.8042 in full', '0.8024 in full', 1)),
        ('an interpolated zero put inside its n(L) ends', lambda t: t.replace('lies below the `n(L)` ends, 16.2848', 'lies inside the `n(L)` ends, 16.2848', 1)),
    ]


def main():
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    terms = sys.argv[1]
    text = open(os.path.join(LOC, 'RECORD.md')).read()
    res = check(text, terms)
    out = ['check_record.py: RECORD.md against the files']
    out += [f'  {"PASS" if ok else "FAIL"}  {w}' for w, ok in res]
    parent = all(ok for _, ok in res)
    out.append(f'{len(res)} checks; the parent: {"ALL PASS" if parent else "FAILED"}')
    caught = []
    if len(sys.argv) == 3 and sys.argv[2] == '--mutations' and parent:
        for name, edit in arms():
            t2 = edit(text)
            assert t2 != text, name
            c = not all(ok for _, ok in check(t2, terms))
            caught.append(c)
            out.append(f'  arm: {name}: {"caught" if c else "NOT CAUGHT"}')
    ok = parent and (all(caught) if len(sys.argv) == 3 else True)
    out.append('ALL PASS' if ok else 'FAIL')
    text_out = '\n'.join(out) + '\n'
    open(os.path.join(HERE, 'check_record.out'), 'w').write(text_out)
    print(text_out, end='')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
