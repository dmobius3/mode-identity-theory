#!/usr/bin/env python3
"""The census run (M8.17's terms: THE POINTS, CLASSIFYING A POINT, LOCATING A CHANGE OF TYPE, THE ROW OUTCOMES, and
THE FREEZE, THE GUARD AND THE RUN).

Usage: census.py        the registered run, refused unless devtools.frozen() validates run/FROZEN.json

The order:
  1. Each row's path, in census_lib.RUN_ORDER, by M8.16.1's driver.run_case, byte for byte: each cutoff from its own
     seed along its own path, every point read, then the rule's readings and branch identity. After each row the
     reproduction rules are applied to every point of its path that M8.16.1 solved. A point that does not reproduce
     stops the run: run_case returns a whole row, so the stop falls at the row's end. A stop is global. Every completed
     job's records are kept, the stopped row's and any locator job's among them, and no reading of this run is
     classified: the record names each completed job's files, and a row's first-time points (census_lib.stopped).
  2. Each point of the nine rows' windows is classified, from this run's records where it computed them and M8.16.1's
     and M8.15's otherwise, and each row's changes of type are read.
  3. The locator, on each index bracket, and on T2/R4's (22.63, 32) wherever it is a type bracket, the path going on to
     32: each cutoff's registered path is recomputed from its seed to the bracket's upper end, every point read as
     run_case reads it, and every recomputed point must equal its record, this run's or M8.16.1's, field for field;
     then the index evidence, the bisection at each cutoff, the location and the guard readings.
  4. The record: run/out/CENSUS.json, each row's points, changes and ending.
Outputs go to run/out/. RUNLOG.json records the manifest at the start, each completed case's file with its SHA-256,
and a stop; a resume refuses another tree's manifest, a stopped run and a completed case whose file differs, and moves
any other case file to interrupted/ (M8.16.1's rules, as driver.resume applies them).
"""
import glob
import json
import os
import shutil
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import basis, functional as fn, branches as br, newton, devtools  # noqa: E402
import cases as cs  # noqa: E402
import checks as ck  # noqa: E402
import seeds as sd  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402

OUT = os.path.join(HERE, 'out')
KEEP = ('RUNLOG.json', 'CENSUS.json')
say = dr.say


def roundtrip(o):
    return json.loads(json.dumps(dr.jsonable(o)))


def sources(root=ROOT):
    return lib.load_json(os.path.join(root, 'reference', 'SOURCES.json'))


# --- the freeze ----------------------------------------------------------------------------------------------------
def frozen():
    """The freeze, validated: devtools.frozen() (the pin, the manifest, the terms, each target's SHA-256) and
    driver.load's representatives; then FROZEN.json's cases are M8.16.1's, serialized, with this task's paths, its
    census values are census_lib's, and its targets hold every reference file SOURCES.json names, at its SHA-256."""
    order, cases, F = dr.load(False)
    if order != lib.RUN_ORDER or sorted(F['allowlist']) != sorted(lib.RUN_ORDER):
        raise PermissionError("FROZEN.json's order or allowlist is not the census run's")
    for row in lib.RUN_ORDER:
        if cases[row] != roundtrip(cs.serialize(row, dict(cs.CASES[row], points=lib.path_points(row)))):
            raise PermissionError(f"FROZEN.json's case {row} differs from M8.16.1's with this task's path")
    if F.get('census') != roundtrip(lib.frozen_values(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))):
        raise PermissionError("FROZEN.json's census values differ from census_lib's")
    held = {t['file']: t['sha256'] for t in F['targets']}
    for s in sources()['files']:
        if s['file'].startswith('reference/') and held.get(s['file']) != s['sha256']:
            raise PermissionError(f"FROZEN.json does not pin {s['file']} at its source's SHA-256")
    return F


# --- the instrument's side ---------------------------------------------------------------------------------------
class Cutoff:
    """One cutoff's basis, functional and fibre structure, and its seed, checked as run_case checks it."""

    def __init__(self, row, case, N):
        self.N, self.case = N, case
        self.B = basis.Basis(case['slot'], N)
        self.Fn = fn.Functional(self.B)
        self.K = fn.fibre_structure_matrix(self.Fn)[1] if case['slot'] == 'R2' else None
        self.u = sd.seed_state(sd.base(row), self.B)
        self.chk = br.orbit_checks(self.Fn, self.u, self.K)
        Qx = ck.num(case['Q'])
        self.seed_ok = bool(abs(self.chk['Q'] - Qx) / Qx < 1e-12 and self.chk['crit'] <= 1e-12
                            and (self.chk['k'], self.chk['r']) == (case['k'], case['r']))

    def step(self, state, eps, prev_accepted=True):
        """A continuation to eps from state (c, lam, slope), the point recorded as run_case records a read point, with
        K1 and n(L) by inertia (None where unresolved)."""
        c0, lam0, slope = state
        t1 = time.perf_counter()
        res = br.continue_to(self.Fn, self.case['lam0'], eps, c0, lam0, slope, K=self.K, prev_accepted=prev_accepted)
        n_eval = sum(s_['evaluations'] for s_ in res['steps'])
        if not res['ok']:
            return dict(ok=False, why=res['reason'], state=None, c=None, k1=False, nL=None,
                        point=dict(accepted=False, reason=res['reason']))
        c, lam = res['c'], res['lam']
        accepted = abs(res['eps'] - eps) <= 1e-6 and all(s_['accepted'] for s_ in res['steps'])
        point, _, _ = dr.read_point(self.Fn, self.K, c, lam, self.case, eps, False)
        point.update(accepted=bool(accepted), eps_reached=float(res['eps']), lam=float(lam), m=float(res['m']),
                     evaluations=n_eval, floor_rel=float(res['info']['floor_rel']), seconds=time.perf_counter() - t1)
        return dict(ok=bool(accepted), why=None if accepted else 'not accepted', state=(c, lam, res['slope']), c=c,
                    k1=bool(accepted and ck.k1(point, self.case)), nL=lib.nl_at(point), point=point)

    def path(self, upto):
        """The registered path from the seed along the window's grid to upto, as run_case takes it: from
        c = sqrt(eps_0 / Q) u at lam0 + eps_0 with slope 1/Q, each point read. It ends where a step fails."""
        grid = [e for e in lib.WINDOWS[self.case['slot']] if e <= upto * (1 + 1e-12)]
        state = (np.sqrt(grid[0] / self.chk['Q']) * self.u, self.case['lam0'] + grid[0], 1 / self.chk['Q'])
        out, acc = {}, False
        for e in grid:
            s = self.step(state, e, prev_accepted=acc)
            out[lib.key(e)] = s
            if s['state'] is None:
                break
            state, acc = s['state'], True
        return out


def aligned(Fn, K, c_ref, c):
    """The distance from c to c_ref, relative to c_ref's norm, once the orbit tangents at c_ref are removed: run_case's
    branch identity, at one cutoff."""
    Qb, _, _ = newton.tangent_borders(br.tangent_vectors(Fn, c_ref, K))
    dx = fn.to_real(c) - fn.to_real(c_ref)
    return float(np.linalg.norm(dx - Qb @ (Qb.T @ dx)) / np.linalg.norm(fn.to_real(c_ref)))


def readings_of(cuts, sols):
    """One point's records from each cutoff's step: its points, the rule's reading and branch identity, as run_case
    computes them."""
    pts = [sols[N]['point'] if sols.get(N) else None for N in lib.CUTOFFS]
    if not all(q and 'summary' in q for q in pts):
        reading = dict(verdict='Unresolved', type=None, reasons=['a cutoff is missing'], rows=[])
    else:
        hi = pts[-1]
        reading = ck.reading([q['summary'] for q in pts], hi['eig'], hi['lam'], hi['record']['margin'], lib.CUTOFFS[0])
    Na, Nb = lib.CUTOFFS[-2], lib.CUTOFFS[-1]
    ident = None
    if sols.get(Na) and sols[Na]['c'] is not None and sols.get(Nb) and sols[Nb]['c'] is not None:
        dr.embeds(cuts[Na].B, cuts[Nb].B)
        c24 = np.concatenate([sols[Na]['c'], np.zeros(cuts[Nb].B.m - cuts[Na].B.m, dtype=complex)])
        d_al = aligned(cuts[Nb].Fn, cuts[Nb].K, c24, sols[Nb]['c'])
        r24, r32 = pts[-2]['record'], pts[-1]['record']
        same = all(r24[f] == r32[f] for f in ('type', 'nL', 'nD', 'K', 'krein', 'sdim', 'ranks'))
        ident = dict(aligned_distance=d_al, same_record=bool(same), kept=bool(d_al <= ck.IDENTITY and same))
    return dict(points={N: roundtrip(q) for N, q in zip(lib.CUTOFFS, pts)}, reading=roundtrip(reading),
                identity=roundtrip(ident))


# --- the run's log -------------------------------------------------------------------------------------------------
def resume(log):
    """M8.16.1's resume rules (driver.resume), for this run's cases."""
    if log['completed'] or log['events']:
        if log.get('manifest_sha256') != devtools.manifest()[1]:
            raise PermissionError('the run does not resume: its log records '
                                  + ('no manifest' if 'manifest_sha256' not in log else "another tree's manifest"))
        if log.get('stop'):
            raise PermissionError(f"the run stopped ({log['stop']['why']}): a stopped run does not resume")
    for name, rec in log['completed'].items():
        for fname, h in rec['files'].items():
            if dr.sha(os.path.join(OUT, fname)) != h:
                raise PermissionError(f'the completed case {name}: {fname} differs from the SHA-256 the run logged')
    done = {f for rec in log['completed'].values() for f in rec['files']}
    partial = [f for f in glob.glob(os.path.join(OUT, '*.json')) if os.path.basename(f) not in done | set(KEEP)]
    if partial:
        dest = os.path.join(OUT, 'interrupted', dr.now().replace(':', ''))
        os.makedirs(dest, exist_ok=True)
        for f_ in partial:
            shutil.move(f_, dest)
        log['events'].append(dict(t=dr.now(), event=f'partial outputs moved to {os.path.relpath(dest, OUT)}'))


def complete(log, name, fname, obj):
    path = os.path.join(OUT, fname)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dr.jsonable(obj), f, indent=1)
    log['completed'][name] = dict(files={fname: dr.sha(path)}, t=dr.now())
    log['events'].append(dict(t=dr.now(), event=f'{name} completed'))
    dr.save_log(OUT, log)
    return lib.load_json(path)


def stop_run(log, why, detail):
    path = os.path.join(OUT, 'STOP.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dr.jsonable(dict(why=why, detail=detail, t=dr.now())), f, indent=1)
    log['stop'] = dict(file='STOP.json', sha256=dr.sha(path), why=why)
    log['events'].append(dict(t=dr.now(), event=f'STOP: {why}'))
    dr.save_log(OUT, log)
    say(f'STOP: {why}')


# --- the reproduction rules ---------------------------------------------------------------------------------------
def gate_row(row, mine, theirs):
    """The three rules on every point of the row's path that M8.16.1 solved."""
    rows = []
    for e in lib.PATHS[row]:
        rule = lib.rule_for(row, e, theirs)
        if rule is None:
            continue
        fails = lib.GATES[rule](lib.at(mine, e), lib.at(theirs, e))
        rows.append(dict(eps=e, rule=rule, ok=not fails, failures=fails))
    return dict(points=rows, failed=[r['eps'] for r in rows if not r['ok']])


def ref_for(row, e, results, theirs):
    """A recomputed path point's record: this run's, on its row's path, or M8.16.1's, read on the same steps."""
    if lib.on_path(row, e):
        return lib.at(results[row], e)
    tp = theirs[row]['case']['points']
    read = {lib.key(p['eps']): p['read'] for p in tp}
    if read.get(lib.key(e)) and lib.same_steps([p['eps'] for p in tp], lib.WINDOWS[lib.SLOT[row]], e):
        return lib.at(theirs[row], e)
    return None


# --- the locator ---------------------------------------------------------------------------------------------------
def locate(row, case, ch, results, theirs):
    """One bracket, by census_lib.locate on the instrument: each cutoff's Cutoff, its path and steps; the rule's reading
    and branch identity from the steps (readings_of); the two-ends distance (aligned); and the record each recomputed
    point must equal (ref_for)."""
    cuts = {N: Cutoff(row, case, N) for N in lib.CUTOFFS}
    rec, stop = lib.locate(ch, lib.WINDOWS[case['slot']], case, cuts, lambda sols: readings_of(cuts, sols),
                           lambda cu, s1, s2: aligned(cu.Fn, cu.K, s1['c'], s2['c']),
                           lambda e: ref_for(row, e, results, theirs), say=say)
    rec['row'] = row
    return rec, stop


# --- the run -------------------------------------------------------------------------------------------------------
def main():
    if len(sys.argv) != 1:
        raise SystemExit(__doc__)
    if not __debug__:
        raise SystemExit('refused under python -O, which removes asserts')
    F = frozen()
    os.makedirs(OUT, exist_ok=True)
    log = dr.load_log(OUT)
    resume(log)
    if 'manifest_sha256' not in log:
        log['manifest_sha256'] = devtools.manifest()[1]
    log['events'].append(dict(t=dr.now(), event=f'run started; rows {lib.RUN_ORDER}'))
    dr.save_log(OUT, log)
    t_all = time.perf_counter()
    theirs, m815 = lib.theirs_records(), lib.m815_records()
    loc = lib.known_location(lib.load_json(os.path.join(ROOT, *lib.M8152_FILE)))
    say(f'M8.17, the census run: {len(lib.RUN_ORDER)} rows; outputs in {os.path.relpath(OUT, ROOT)}')
    results = {}
    for row in lib.RUN_ORDER:
        fname = dr.safe(row) + '.json'
        if row in log['completed']:
            results[row] = lib.load_json(os.path.join(OUT, fname))
            say(f'{row}: completed earlier, its output checked against the log')
        else:
            case = dict(F['cases'][row])
            devtools.require(case['admission'])
            t0 = time.perf_counter()
            say(f"{row} ({case['slot']}): {len(case['points'])} points")
            out, _ = dr.run_case(row, case, False)
            out['case'], out['seconds'] = case, time.perf_counter() - t0
            out['gate'] = gate_row(row, roundtrip(out), theirs[row])
            results[row] = complete(log, row, fname, out)
            say(f"   {row}: {out['seconds']:.0f} s; reproduction: {len(out['gate']['points'])} points compared, "
                f"{len(out['gate']['failed'])} failed")
        if results[row]['gate']['failed']:
            stop_run(log, f"reproducibility failure: {row} at eps = {results[row]['gate']['failed'][0]:g}",
                     results[row]['gate'])
            break
    extra, located = {}, {}
    if not log.get('stop'):
        for row, ch in lib.jobs(lib.classify_rows(results, extra, theirs, m815, loc), results, extra, theirs):
            name = f"locate:{row}:{lib.key(ch['lo'])}:{lib.key(ch['hi'])}"
            fname = dr.safe(name) + '.json'
            if name in log['completed']:
                rec = lib.load_json(os.path.join(OUT, fname))
                say(f'{name}: completed earlier, its output checked against the log')
            else:
                t0 = time.perf_counter()
                say(f'{name}:')
                rec, stop = locate(row, results[row]['case'], ch, results, theirs)
                rec['seconds'] = time.perf_counter() - t0
                rec = complete(log, name, fname, rec)
                say(f"   {name}: {rec.get('kind', 'stopped')}; located: {rec.get('located')}; {rec['seconds']:.0f} s")
                if stop:
                    stop_run(log, f'reproducibility failure in {name}: {stop}', rec['path'])
                    break
            for k, v in rec['ends'].items():
                extra[(row, k)] = lib.pt_from_json(v)
            located[(row, lib.key(ch['lo']), lib.key(ch['hi']))] = rec
    census = dict(stop=log.get('stop'), rows={}, unclassified=lib.stopped(log))
    if not log.get('stop'):
        census['rows'] = lib.assemble(results, extra, located, theirs, m815, loc)
        for row, r in census['rows'].items():
            say(f"{row}: {r['outcome']}" + (f"; open: {len(r['open'])}" if r['open'] else ''))
    path = os.path.join(OUT, 'CENSUS.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dr.jsonable(census), f, indent=1)
    tpath = os.path.join(OUT, 'census.out')
    say(f'{time.perf_counter() - t_all:.0f} s')
    with open(tpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(dr.out_lines) + '\n')
    log['census'] = dict(file='CENSUS.json', sha256=dr.sha(path), written=dr.now())
    log['transcript'] = dict(file='census.out', sha256=dr.sha(tpath), written=dr.now())
    log['events'].append(dict(t=dr.now(), event='record and transcript written'))
    dr.save_log(OUT, log)


if __name__ == '__main__':
    main()
