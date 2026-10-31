#!/usr/bin/env python3
"""The census's two remedies (M8.18's terms: TWO ARMS, ONE REGISTRATION; ARM A; ARM B; THE ROW OUTCOMES; and THE FREEZE,
THE GUARD AND THE RUN). It is M8.17's census.py, with solving and reading made separate operations and the run cut into
jobs.

Usage: census.py        the registered run, refused unless devtools.frozen() validates run/FROZEN.json

The order:
  1. Arm B: T4/R5's bracket, each cutoff's path recomputed from its seed to 11.31, every recomputed point and each of
     M8.17's midpoints equal to its record, a midpoint where K1 fails moved once, then the location and the guards. Its
     record is written before any solve at N = 40, which the Cutoff refuses until then.
  2. Arm A's gates: the six controls' paths at N = 24 and 32, each reproducing M8.16.1's record; C1 by run_c1, whose
     check holds at N = 40 and which reproduces M8.16.1's record at its four cutoffs; each of the six at N = 40, K1
     read control by control, the first failure ending Arm A; then the rule on all six and both identities. GATE.json
     records the outcome.
  3. Arm A's targets, in census_lib.TARGETS' order, only on a GATE.json that passed: each path at N = 24 and 32, every
     point read and reproducing M8.17's record, with the identity between them; then N = 40, solved at every grid
     point and read at the row's twelve alone, with the identity between 32 and 40; then the rule on the three.
  4. Each row's points and changes of type; the locator on each type bracket, from the ends' stored solutions.
  5. The band's test on every scored reading, and the record: run/out/CENSUS.json.

A job is one file set: a path at one cutoff, its read, an identity, a case's reading, the gate, a location. A path's
solutions are written and hashed before anything reads them, and a stored solution is used only through the solve-state
gate (Run.stored). A reproduction failure raises StopRun and stops the run, and a stop is global. So does a scored
reading off the frozen band, or a read refused at N = 40, each a defect in the code, and so does any other exception,
on its first launch. Every record already written is kept, and no reading of Arm A is classified. Arm B's record, if
written, stands.

A job that runs out of memory, or that census_lib.ATTEMPTS launches start and leave unfinished, ends only the part of
the run it belongs to, with the cause named: a control's N = 40 job or C1 fails the kernel check, and Arm A ends; a
target's row stays unread, and the run goes on to the next row; a location's bracket is not located; Arm B ends, and Arm
A goes on; any other job stops the run. The system can end a process with nothing raised, so a job's start is logged
before it solves, and the next launch counts those entries: a job started that many times and not completed starts no
more, and takes its route (Run.begin). Those two causes alone take a route, each caught by name at its route.

Outputs go to run/out/. RUNLOG.json records the manifest at the start, each job's start, each completed job's files
with their SHA-256, its time and the process's peak resident size so far, in bytes on macOS, and a stop; a resume refuses another tree's manifest, a stopped run and a completed job whose file differs, moves any
other output to interrupted/, and restarts at the first incomplete job (M8.16.1's rules, applied to each job). A
completed job's checks are read again on a resume, so a stop that a job recorded is not passed over.
"""
import glob
import json
import os
import resource
import shutil
import sys
import time
import traceback
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
KEEP = ('RUNLOG.json', 'CENSUS.json', 'STOP.json')
say = dr.say


def roundtrip(o):
    return json.loads(json.dumps(dr.jsonable(o)))


def sources(root=ROOT):
    return lib.load_json(os.path.join(root, 'reference', 'SOURCES.json'))


class StopRun(Exception):
    """A reproducibility failure: the run stops (TWO ARMS, ONE REGISTRATION, What stops what)."""

    def __init__(self, why, detail=None):
        super().__init__(why)
        self.why, self.detail = why, detail


class Unfinished(StopRun):
    """A job that census_lib.ATTEMPTS launches started and left unfinished. It stops the run unless its route catches it
    first (TWO ARMS, ONE REGISTRATION, What stops what)."""


# --- the freeze ----------------------------------------------------------------------------------------------------
def frozen():
    """The freeze, validated: devtools.frozen() (the pin, the manifest, the terms, each target's SHA-256) and
    driver.load's representatives; then FROZEN.json's cases are M8.16.1's, serialized, with this task's points and
    ladders, its census values are census_lib's, and its targets hold every reference file SOURCES.json names, at its
    SHA-256."""
    order, cases, F = dr.load(False)
    if order != lib.RUN_ORDER or sorted(F['allowlist']) != sorted(lib.RUN_ORDER):
        raise PermissionError("FROZEN.json's order or allowlist is not this run's")
    for name in lib.RUN_ORDER:
        want = roundtrip(cs.serialize(name, dict(cs.CASES[name], points=lib.path_points(name),
                                                 cutoffs=lib.cutoffs_of(name))))
        if cases[name] != want:
            raise PermissionError(f"FROZEN.json's case {name} differs from M8.16.1's with this task's points and ladder")
    if F.get('census') != roundtrip(lib.frozen_values()):
        raise PermissionError("FROZEN.json's census values differ from census_lib's")
    held = {t['file']: t['sha256'] for t in F['targets']}
    for s in sources()['files']:
        if s['file'].startswith('reference/') and held.get(s['file']) != s['sha256']:
            raise PermissionError(f"FROZEN.json does not pin {s['file']} at its source's SHA-256")
    return F


# --- the instrument's side ---------------------------------------------------------------------------------------
class Cutoff:
    """One cutoff's basis, functional and fibre structure, and its seed, checked as run_case checks it. Solving and
    reading are separate operations (ARM A, Solving and reading). opened() says whether Arm B's record is written, and
    no solve at N = 40 starts before it. bracket: a location's (lo, hi), while one is open, for the read's scope. kept:
    the solutions of a location's midpoints and guards."""

    def __init__(self, name, case, N, opened=lambda: True):
        self.name, self.N, self.case, self.opened, self.bracket, self.kept = name, N, case, opened, None, []
        self.B = basis.Basis(case['slot'], N)
        self.Fn = fn.Functional(self.B)
        self.K = fn.fibre_structure_matrix(self.Fn)[1] if case['slot'] == 'R2' else None
        self.u = sd.seed_state(sd.base(name), self.B)
        self.chk = br.orbit_checks(self.Fn, self.u, self.K)
        Qx = ck.num(case['Q'])
        self.seed_ok = bool(abs(self.chk['Q'] - Qx) / Qx < 1e-12 and self.chk['crit'] <= 1e-12
                            and (self.chk['k'], self.chk['r']) == (case['k'], case['r']))

    def seed(self):
        return dict(Q=self.chk['Q'], crit=self.chk['crit'], k=self.chk['k'], r=self.chk['r'], ok=self.seed_ok)

    def solve(self, state, eps, prev_accepted=True):
        """A continuation to eps from state (c, lam, slope), its acceptance check, and no linear-spectrum record: it runs
        inside checks.withheld, where every record path refuses. Nothing it computes depends on a read."""
        if self.N == lib.TOP and not self.opened():
            raise PermissionError(f"a solve at N = {lib.TOP} before Arm B's record is written")
        c0, lam0, slope = state
        t1 = time.perf_counter()
        with ck.withheld(f'{self.name} N = {self.N} eps {eps:g}'):
            res = br.continue_to(self.Fn, self.case['lam0'], eps, c0, lam0, slope, K=self.K, prev_accepted=prev_accepted)
        n_eval = sum(s_['evaluations'] for s_ in res['steps'])
        if not res['ok']:
            return dict(ok=False, why=res['reason'], eps=eps, state=None, c=None, k1=False, nL=None,
                        point=dict(accepted=False, reason=res['reason']))
        c, lam = res['c'], res['lam']
        accepted = abs(res['eps'] - eps) <= 1e-6 and all(s_['accepted'] for s_ in res['steps'])
        point = dict(accepted=bool(accepted), eps_reached=float(res['eps']), lam=float(lam), m=float(res['m']),
                     evaluations=n_eval, floor_rel=float(res['info']['floor_rel']), seconds=time.perf_counter() - t1)
        return dict(ok=bool(accepted), why=None if accepted else 'not accepted', eps=eps, state=(c, lam, res['slope']), c=c,
                    k1=False, nL=None, point=point)

    def read(self, s, eps, why):
        """The record of a solved point, as run_case records a read point, with K1 and n(L) by inertia (None where
        unresolved). why names its place in the read's frozen scope, and a read outside it is refused."""
        if not lib.in_scope(self.name, self.N, eps, why, self.bracket):
            raise lib.OutOfScope(f'{self.name}: a read at N = {self.N}, eps = {eps:g}, as {why}, is outside the scope')
        point, _, _ = dr.read_point(self.Fn, self.K, s['c'], s['point']['lam'], self.case, eps, False)
        point.update(s['point'])
        return dict(s, k1=bool(s['ok'] and ck.k1(point, self.case)), nL=lib.nl_at(point), point=point)

    def step(self, state, eps, prev_accepted=True):
        """A solve and a read: a location's midpoint or guard, whose solution is kept."""
        s = self.solve(state, eps, prev_accepted)
        if s['state'] is None:
            return s
        self.kept.append((eps, s['state']))
        return self.read(s, eps, 'location')

    def solves(self, upto=None):
        """The registered path from the seed along the case's points to upto, as run_case takes it: from
        c = sqrt(eps_0 / Q) u at lam0 + eps_0 with slope 1/Q, each point solved and none read. It ends where a step
        fails."""
        grid = [p['eps'] for p in self.case['points'] if upto is None or p['eps'] <= upto * (1 + 1e-12)]
        state = (np.sqrt(grid[0] / self.chk['Q']) * self.u, self.case['lam0'] + grid[0], 1 / self.chk['Q'])
        out, acc = {}, False
        for e in grid:
            s = self.solve(state, e, prev_accepted=acc)
            out[lib.key(e)] = s
            if s['state'] is None:
                break
            state, acc = s['state'], True
        return out

    def path(self, upto):
        """Arm B's path: every point solved and then read, as M8.17's path reads it."""
        return {k: (self.read(s, s['eps'], 'path') if s['state'] is not None else s) for k, s in self.solves(upto).items()}


def aligned(Fn, K, c_ref, c):
    """The distance from c to c_ref, relative to c_ref's norm, once the orbit tangents at c_ref are removed: run_case's
    branch identity, at one cutoff."""
    Qb, _, _ = newton.tangent_borders(br.tangent_vectors(Fn, c_ref, K))
    dx = fn.to_real(c) - fn.to_real(c_ref)
    return float(np.linalg.norm(dx - Qb @ (Qb.T @ dx)) / np.linalg.norm(fn.to_real(c_ref)))


def identity(cuts, sols, pair):
    """Branch identity on one pair, as run_case computes it between its two highest cutoffs: None unless both cutoffs
    hold a solution with a record."""
    Na, Nb = pair
    sa, sb = sols.get(Na), sols.get(Nb)
    if not (sa and sa['c'] is not None and 'record' in sa['point'] and sb and sb['c'] is not None and 'record' in sb['point']):
        return None
    dr.embeds(cuts[Na].B, cuts[Nb].B)
    ca = np.concatenate([sa['c'], np.zeros(cuts[Nb].B.m - cuts[Na].B.m, dtype=complex)])
    d_al = aligned(cuts[Nb].Fn, cuts[Nb].K, ca, sb['c'])
    ra, rb = sa['point']['record'], sb['point']['record']
    same = all(ra[f] == rb[f] for f in ('type', 'nL', 'nD', 'K', 'krein', 'sdim', 'ranks'))
    return dict(aligned_distance=d_al, same_record=bool(same), kept=bool(d_al <= ck.IDENTITY and same))


def rule(pts):
    """The convergence rule on one point's records, lowest cutoff first, with the band above N = 16, and the reading
    beside it on the band above N = 24: (scored, beside)."""
    if not all(q and 'summary' in q for q in pts):
        miss = dict(verdict='Unresolved', type=None, reasons=['a cutoff is missing'], rows=[])
        return miss, miss
    hi = pts[-1]
    args = ([q['summary'] for q in pts], hi['eig'], hi['lam'], hi['record']['margin'])
    return ck.reading(*args, lib.BAND_N), ck.reading(*args, lib.BESIDE_N)


def readings_of(cuts, sols, lad, read_rule=True):
    """One point's records from each cutoff's step: its points, the rule's reading and the reading beside it, and branch
    identity on every pair. read_rule=False leaves the rule out: a bracket's end outside the twelve, which it does not
    read."""
    pts = [sols[N]['point'] if sols.get(N) else None for N in lad['cutoffs']]
    reading, beside = rule(pts) if read_rule else (None, None)
    return dict(points={N: roundtrip(q) for N, q in zip(lad['cutoffs'], pts)}, reading=roundtrip(reading),
                beside=roundtrip(beside) if lad['beside'] else None,
                identity={lib.pair_key(p): roundtrip(identity(cuts, sols, p)) for p in lad['pairs']})


# --- the run --------------------------------------------------------------------------------------------------------
class Run:
    """One registered run: its frozen values, its outputs and its log. make(name, case, N, opened) builds a cutoff."""

    def __init__(self, F, out=OUT, make=Cutoff):
        self.F, self.out, self.make, self.cuts, self.job = F, out, make, {}, None
        self.log = dr.load_log(out)

    def at(self, fname):
        return os.path.join(self.out, fname)

    def done(self, job):
        return job in self.log['completed']

    def opened(self):
        return self.done('arm_b')

    def cutoff(self, name, N):
        if (name, N) not in self.cuts:
            devtools.require(self.F['cases'][name]['admission'])
            self.cuts[(name, N)] = self.make(name, self.F['cases'][name], N, self.opened)
        return self.cuts[(name, N)]

    def begin(self, job):
        """A job's start, in the log before it solves. A job started lib.ATTEMPTS times and not completed, or one that
        ran out of memory, starts no more, on this launch or a later one: its route takes it from here. The count is the
        job's own, read from the log on every launch."""
        ended, started = self.log.setdefault('ended', {}), f'{job} started'
        if job not in ended and sum(e['event'] == started for e in self.log['events']) >= lib.ATTEMPTS:
            ended[job] = f'{job}: {lib.UNFINISHED}'
            dr.save_log(self.out, self.log)
        if job in ended:
            raise Unfinished(ended[job], job)
        self.job = job
        self.log['events'].append(dict(t=dr.now(), event=started))
        dr.save_log(self.out, self.log)

    def cause(self, e):
        """What ended a job, for its route: out of memory, held in the log against the job under way, or the job left
        unfinished."""
        if isinstance(e, MemoryError):
            self.log.setdefault('ended', {})[self.job] = lib.NO_MEMORY
            dr.save_log(self.out, self.log)
        why = lib.NO_MEMORY if isinstance(e, MemoryError) else e.why
        say(f'   ended: {why}')
        return why

    def complete(self, job, files):
        self.log['completed'][job] = dict(files={f: dr.sha(self.at(f)) for f in files}, t=dr.now(),
                                          peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        self.log['events'].append(dict(t=dr.now(), event=f'{job} completed'))
        dr.save_log(self.out, self.log)

    def write(self, job, fname, obj, also=()):
        with open(self.at(fname), 'w', encoding='utf-8') as f:
            json.dump(dr.jsonable(obj), f, indent=1)
        self.complete(job, [fname, *also])
        return lib.load_json(self.at(fname))

    def stop(self, why, detail):
        path = self.at('STOP.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(dr.jsonable(dict(why=why, detail=detail, t=dr.now())), f, indent=1)
        self.log['stop'] = dict(file='STOP.json', sha256=dr.sha(path), why=why)
        self.log['events'].append(dict(t=dr.now(), event=f'STOP: {why}'))
        dr.save_log(self.out, self.log)
        say(f'STOP: {why}')

    # --- one path ---------------------------------------------------------------------------------------------------
    def path_job(self, name, N):
        """A path at one cutoff, solved and read nowhere: the solutions and the solve fields, written and hashed."""
        job = f'path:{name}:{N}'
        if self.done(job):
            return
        self.begin(job)
        base = f'{dr.safe(name)}_N{N}'
        cu = self.cutoff(name, N)
        t0 = time.perf_counter()
        sols = cu.solves() if cu.seed_ok else {}
        done = {k: s for k, s in sols.items() if s['state'] is not None}
        arrays = {f'c{i}': s['state'][0] for i, s in enumerate(done.values())}
        arrays.update(keys=np.array(list(done) or ['']), lam=np.array([float(s['state'][1]) for s in done.values()]),
                      slope=np.array([float(s['state'][2]) for s in done.values()]))
        np.savez(self.at(base + '.npz'), **arrays)
        with open(self.at(base + '.json'), 'w', encoding='utf-8') as f:
            json.dump(dr.jsonable(dict(seed=cu.seed(), points={k: s['point'] for k, s in sols.items()},
                                       setup_seconds=time.perf_counter() - t0)), f, indent=1)
        self.complete(job, [base + '.npz', base + '.json'])
        say(f"   {name} N = {N}: {len(done)} of {len(self.F['cases'][name]['points'])} points solved; "
            f"{time.perf_counter() - t0:.0f} s")

    def stored(self, name, N):
        """A path's solutions through the solve-state gate: its files have the SHA-256 the log recorded when the job
        completed, and each stored lam equals the job's record. Anything else stops the run."""
        base = f'{dr.safe(name)}_N{N}'
        job = f'path:{name}:{N}'
        if not self.done(job):
            raise StopRun(f'reproducibility failure: no logged path job for {name} at N = {N}', job)
        for fname, h in self.log['completed'][job]['files'].items():
            if dr.sha(self.at(fname)) != h:
                raise StopRun(f'reproducibility failure: {fname} differs from the SHA-256 the log recorded', fname)
        rec = lib.load_json(self.at(base + '.json'))
        with np.load(self.at(base + '.npz'), allow_pickle=False) as z:
            arrays = {k: z[k] for k in z.files}
        sols = {}
        for k, p in rec['points'].items():
            sols[k] = dict(ok=False, why=p.get('reason'), eps=None, state=None, c=None, k1=False, nL=None, point=p)
        for i, k in enumerate(str(x) for x in arrays['keys'] if str(x)):
            lam, slope, c = float(arrays['lam'][i]), float(arrays['slope'][i]), arrays[f'c{i}']
            if lam != rec['points'][k]['lam']:
                raise StopRun(f'reproducibility failure: the stored lam of {name} at N = {N}, {k}, differs from the job', k)
            sols[k] = dict(sols[k], ok=bool(rec['points'][k]['accepted']), state=(c, lam, slope), c=c, eps=float(k))
        return dict(seed=rec['seed'], sols=sols)

    def read_job(self, name, N, where, why):
        """The records of a path at one cutoff, read from its stored solutions at where."""
        job, fname = f'read:{name}:{N}', f'{dr.safe(name)}_N{N}_read.json'
        if self.done(job):
            return lib.load_json(self.at(fname))
        self.begin(job)
        st, cu = self.stored(name, N), self.cutoff(name, N)
        pts = {k: s['point'] for k, s in st['sols'].items()}
        for e in where:
            s = st['sols'].get(lib.key(e))
            if s and s['ok']:
                pts[lib.key(e)] = cu.read(s, e, why)['point']
        return self.write(job, fname, dict(seed=st['seed'], points=pts))

    def reproduce(self, name, N, rec, theirs):
        """A path at N = 24 or 32 against its record: the first difference stops the run."""
        eps = [p['eps'] for p in self.F['cases'][name]['points']]
        fails = lib.gate_cutoff(rec, theirs['cutoffs'][str(N)], eps)
        if fails:
            raise StopRun(f'reproducibility failure: {name} at N = {N}: {fails[0]}', fails)

    def identity_job(self, name, pair, where, recs):
        """Branch identity on one pair, at where, from the stored solutions and the records."""
        job, fname = f'identity:{name}:{lib.pair_key(pair)}', f'{dr.safe(name)}_identity_{pair[0]}_{pair[1]}.json'
        if self.done(job):
            return lib.load_json(self.at(fname))
        self.begin(job)
        st = {N: self.stored(name, N) for N in pair}
        cuts = {N: self.cutoff(name, N) for N in pair}
        out = {}
        for e in where:
            k = lib.key(e)
            sols = {}
            for N in pair:
                s = st[N]['sols'].get(k)
                sols[N] = dict(s, point=recs[N]['points'][k]) if s and s['c'] is not None else None
            out[k] = {lib.pair_key(pair): identity(cuts, sols, pair)}
        return self.write(job, fname, out)

    def case_job(self, name, recs, ids, where):
        """A case's reading on Arm A's ladder, with no solve: the rule and the reading beside it at where."""
        job, fname = f'case:{name}', dr.safe(name) + '.json'
        if self.done(job):
            return lib.load_json(self.at(fname))
        self.begin(job)
        lad = lib.ARM_A
        out = dict(case=self.F['cases'][name], cutoffs={str(N): recs[N] for N in lad['cutoffs']}, readings={}, beside={},
                   identity={})
        for part in ids:
            for k, v in part.items():
                out['identity'].setdefault(k, {}).update(v)
        for e in where:
            k = lib.key(e)
            out['readings'][k], out['beside'][k] = rule([recs[N]['points'].get(k) for N in lad['cutoffs']])
        return self.write(job, fname, out)

    def lower(self, name, where):
        """A case's paths at N = 24 and 32, each read at every point and reproducing its record, and the identity
        between them. Returns (records, identity)."""
        theirs = lib.theirs(name, ROOT)
        recs = {}
        pair = lib.ARM_A['pairs'][0]
        for N in pair:
            self.path_job(name, N)
            recs[N] = self.read_job(name, N, where, 'path')
            self.reproduce(name, N, recs[N], theirs)
        ids = self.identity_job(name, pair, where, recs)
        fails = lib.gate_identity(ids, theirs['identity'], where)
        if fails:
            raise StopRun(f'reproducibility failure: {name}, the identity between N = 24 and 32: {fails[0]}', fails)
        return recs, ids

    # --- Arm B ------------------------------------------------------------------------------------------------------
    def arm_b(self):
        """Arm B, to its record (ARM B). It stops the run only if a recomputed point or a midpoint does not reproduce."""
        job, fname = 'arm_b', 'ARM_B.json'
        if self.done(job):
            rec = lib.load_json(self.at(fname))
        else:
            row, lad = lib.ARM_B_ROW, lib.ARM_B
            case = self.F['cases'][row]
            ch = next(dict(c) for c in lib.m817_file('CENSUS.json', ROOT)['rows'][row]['changes'] if c['kind'] == 'type')
            if (lib.key(ch['lo']), lib.key(ch['hi'])) != tuple(map(lib.key, lib.BRACKET_B)):
                raise StopRun(f"reproducibility failure in Arm B: M8.17's bracket ({ch['lo']:g}, {ch['hi']:g}) is not the frozen one")
            cuts = {}
            try:
                self.begin(job)
                cuts = {N: self.cutoff(row, N) for N in lad['cutoffs']}
                theirs, known = lib.theirs(row, ROOT), lib.m817_file(lib.LOCATED_B, ROOT)
                say(f"Arm B, {row} on ({ch['lo']:g}, {ch['hi']:g}):")
                rec, _ = lib.locate(ch, lib.WINDOWS[case['slot']], case, cuts, lambda sols: readings_of(cuts, sols, lad),
                                    lambda cu, s1, s2: aligned(cu.Fn, cu.K, s1['c'], s2['c']),
                                    lambda e: lib.at(theirs, e, lad), lad, moved=lib.MOVED,
                                    gate_mids=lambda N, mids: lib.gate_midpoints(roundtrip(mids), known['bisection'][str(N)]['midpoints']),
                                    say=say)
            except (MemoryError, Unfinished) as e:
                rec, cuts = lib.not_located(ch, self.cause(e)), {}
            rec.update(row=row, moved=dict(fraction=lib.MOVED, end='lower'))
            rec = self.write(job, fname, rec, [self.keep_located('arm_b', cuts)])
            self.cuts.clear()
        if rec.get('stop'):
            raise StopRun(f"reproducibility failure in Arm B: {rec['stop']}", rec.get('path'))
        say(f"Arm B: {rec.get('kind')}; located: {rec.get('located')}; {rec.get('why')}")
        return rec

    def keep_located(self, tag, cuts):
        """A location's midpoints and guards: their solutions, in a file of their own."""
        arrays = {}
        for N, cu in cuts.items():
            for i, (e, st) in enumerate(cu.kept):
                arrays[f'N{N}_{i}_c'], arrays[f'N{N}_{i}_ls'] = st[0], np.array([e, float(st[1]), float(st[2])])
            cu.kept = []
        fname = dr.safe(tag) + '_solutions.npz'
        np.savez(self.at(fname), **arrays)
        return fname

    # --- Arm A's gates ----------------------------------------------------------------------------------------------
    def gates(self):
        """The kernel at N = 40, then the control gate (ARM A). Returns GATE.json's content."""
        if self.done('gate'):
            return lib.load_json(self.at('GATE.json'))
        cases = self.F['cases']
        lows = {}
        for name in lib.READ_CONTROLS:
            where = [p['eps'] for p in cases[name]['points']]
            say(f'{name}: N = 24 and 32')
            lows[name] = (where, *self.lower(name, where))
            self.cuts.clear()
        gate = dict(kernel={}, control={}, passed=False, stopped=None)
        try:
            c1 = self.c1()
        except (MemoryError, Unfinished) as e:
            c1 = [self.cause(e)]
        gate['kernel']['C1'] = c1
        if c1:
            gate['stopped'] = f"the kernel at N = {lib.TOP}: C1: {c1[0]}"
            return self.write('gate', 'GATE.json', gate)
        tops, ids40 = {}, {}
        for name in lib.READ_CONTROLS:
            where, recs, _ = lows[name]
            say(f'{name}: N = {lib.TOP}')
            try:
                self.path_job(name, lib.TOP)
                tops[name] = {**recs, lib.TOP: self.read_job(name, lib.TOP, where, 'control')}
                gate['kernel'][name] = lib.kernel_failures(tops[name][lib.TOP], cases[name], where)
                if not gate['kernel'][name]:
                    ids40[name] = self.identity_job(name, lib.ARM_A['pairs'][1], where, tops[name])
            except (MemoryError, Unfinished) as e:
                gate['kernel'][name] = [self.cause(e)]
            self.cuts.clear()
            if gate['kernel'][name]:
                gate['stopped'] = f"the kernel at N = {lib.TOP}: {name}: {gate['kernel'][name][0]}"
                return self.write('gate', 'GATE.json', gate)
        for name in lib.READ_CONTROLS:
            where, _, ids = lows[name]
            out = self.case_job(name, tops[name], [ids, ids40[name]], where)
            gate['control'][name] = lib.control_failures(out, cases[name])
        bad = [n for n, f in gate['control'].items() if f]
        gate['passed'] = not bad
        if bad:
            gate['stopped'] = f"the control gate: {bad[0]}: {gate['control'][bad[0]][0]}"
        return self.write('gate', 'GATE.json', gate)

    def c1(self):
        """C1 by M8.16.1's run_c1, at its four cutoffs: Theorem D's check, and its record reproduced."""
        job, fname = 'C1', 'C1.json'
        if self.done(job):
            out = lib.load_json(self.at(fname))
        else:
            if not self.opened():
                raise PermissionError(f"a solve at N = {lib.TOP} before Arm B's record is written")
            self.begin(job)
            case = dict(self.F['cases']['C1'])
            devtools.require(case['admission'])
            say('C1, at its four cutoffs:')
            out, _ = dr.run_c1(case)
            out['checks'], out['case'] = ck.check_c1(out, case), case
            out = self.write(job, fname, out)
        fails = lib.differences(out['cutoffs'], lib.m8161_file('C1.json', ROOT)['cutoffs'], '/cutoffs')
        if fails:
            raise StopRun(f'reproducibility failure: C1: {fails[0]}', fails)
        return [] if out['checks'].get('K1') and out['checks'].get('K4') else ['K1 or K4 fails']

    # --- Arm A's targets --------------------------------------------------------------------------------------------
    def target(self, row):
        """One row: its paths at N = 24 and 32, then N = 40, then the rule on the twelve (ARM A)."""
        gate = lib.load_json(self.at('GATE.json'))
        if not (self.done('gate') and dr.sha(self.at('GATE.json')) == self.log['completed']['gate']['files']['GATE.json']
                and gate['passed']):
            raise PermissionError('no target is read before the gate record shows the controls passed')
        twelve, where = lib.TWELVE[row], [p['eps'] for p in self.F['cases'][row]['points']]
        say(f'{row}: N = 24 and 32')
        recs, ids = self.lower(row, where)
        say(f'{row}: N = {lib.TOP}')
        self.path_job(row, lib.TOP)
        recs = {**recs, lib.TOP: self.read_job(row, lib.TOP, twelve, 'twelve')}
        ids40 = self.identity_job(row, lib.ARM_A['pairs'][1], twelve, recs)
        out = self.case_job(row, recs, [ids, ids40], twelve)
        self.cuts.clear()
        return out

    def locate(self, row, ch, cls, res):
        """One bracket of Arm A's, from its ends' stored solutions: an end outside the twelve is read at N = 40 and must
        be admissible; then census_lib.settle. cls: each end's classification, by key."""
        lo, hi = ch['lo'], ch['hi']
        job = f'locate:{row}:{lib.key(lo)}:{lib.key(hi)}'
        fname = dr.safe(job) + '.json'
        if self.done(job):
            return lib.load_json(self.at(fname))
        self.begin(job)
        lad, case = lib.ARM_A, res['case']
        cuts = {N: self.cutoff(row, N) for N in lad['cutoffs']}
        st = {N: self.stored(row, N) for N in lad['cutoffs']}
        for cu in cuts.values():
            cu.bracket, cu.kept = (lo, hi), []
        rec = dict(bracket=[lo, hi], types=[ch['lo_type'], ch['hi_type']], seeds={N: cu.seed_ok for N, cu in cuts.items()},
                   path={}, ends={}, row=row)
        fails = []
        for e in (lo, hi):
            k = lib.key(e)
            if lib.on(e, lib.TWELVE[row]):
                rec['ends'][k] = lib.at(res, e, lad)
                continue
            sols = {}
            for N in lad['cutoffs']:
                s = st[N]['sols'].get(k)
                if s and N == lib.TOP and s['ok']:
                    sols[N] = cuts[N].read(s, e, 'end')
                elif s and s['c'] is not None:
                    sols[N] = dict(s, point=res['cutoffs'][str(N)]['points'][k])
            rec['ends'][k] = readings_of(cuts, sols, lad, read_rule=False)
            fails += [f'the end at {e:g}: {x}' for x in lib.admissible(rec['ends'][k], cls[k], case, lad, lib.on(e, lib.PATHS[row]))]
        if fails:
            rec.update(located=False, kind='inadmissible', failures=fails, why='; '.join(fails))
            say(f'   {job}: not located: {fails[0]}')
        else:
            states = {N: (st[N]['sols'][lib.key(lo)]['state'], st[N]['sols'][lib.key(hi)]['state']) for N in cuts}
            rec, _ = lib.settle(rec, ch, lib.WINDOWS[case['slot']], case, cuts, lambda sols: readings_of(cuts, sols, lad),
                                lambda cu, s1, s2: aligned(cu.Fn, cu.K, s1['c'], s2['c']), lad, states, say=say)
        for cu in cuts.values():
            cu.bracket = None
        return self.write(job, fname, rec, [self.keep_located(job, cuts)])

    # --- the order --------------------------------------------------------------------------------------------------
    def resume(self):
        """M8.16.1's resume rules (driver.resume), for this run's jobs."""
        log = self.log
        if log['completed'] or log['events']:
            if log.get('manifest_sha256') != devtools.manifest()[1]:
                raise PermissionError('the run does not resume: its log records '
                                      + ('no manifest' if 'manifest_sha256' not in log else "another tree's manifest"))
            if log.get('stop'):
                raise PermissionError(f"the run stopped ({log['stop']['why']}): a stopped run does not resume")
        for name, rec in log['completed'].items():
            for fname, h in rec['files'].items():
                if dr.sha(self.at(fname)) != h:
                    raise PermissionError(f'the completed job {name}: {fname} differs from the SHA-256 the run logged')
        done = {f for rec in log['completed'].values() for f in rec['files']}
        partial = [f for pat in ('*.json', '*.npz') for f in glob.glob(self.at(pat))
                   if os.path.basename(f) not in done | set(KEEP)]
        if partial:
            dest = self.at(os.path.join('interrupted', dr.now().replace(':', '')))
            os.makedirs(dest, exist_ok=True)
            for f_ in partial:
                shutil.move(f_, dest)
            log['events'].append(dict(t=dr.now(), event=f'partial outputs moved to {os.path.relpath(dest, self.out)}'))

    def go(self):
        """The registered order, to the record. Returns CENSUS.json's content."""
        os.makedirs(self.out, exist_ok=True)
        self.resume()
        if 'manifest_sha256' not in self.log:
            self.log['manifest_sha256'] = devtools.manifest()[1]
        self.log['events'].append(dict(t=dr.now(), event=f'run started; order {lib.RUN_ORDER}'))
        dr.save_log(self.out, self.log)
        results, located, left = {}, {}, {}
        census = dict(stop=None, arm_b=None, gate=None, rows={}, bands=None, left=left)
        try:
            rec_b = self.arm_b()
            census['arm_b'] = {k: rec_b[k] for k in ('bracket', 'kind', 'nL', 'delta', 'union', 'span', 'located', 'why',
                                                     'failures', 'moved', 'reproduced') if k in rec_b}
            located[(lib.ARM_B_ROW, lib.key(rec_b['bracket'][0]), lib.key(rec_b['bracket'][1]))] = rec_b
            gate = self.gates()
            census['gate'] = gate
            m817 = lib.m817_file('CENSUS.json', ROOT)
            if gate['passed']:
                for row in lib.TARGETS:
                    try:
                        results[row] = self.target(row)
                    except (MemoryError, Unfinished) as e:
                        left[row] = self.cause(e)
                        self.cuts.clear()
                state = lib.classify_rows(results, m817, None, left)
                for row, ch in lib.jobs(state):
                    cls = {lib.key(e): c for e, c in state[row]['points']}
                    bracket = (row, lib.key(ch['lo']), lib.key(ch['hi']))
                    try:
                        located[bracket] = self.locate(row, ch, cls, results[row])
                    except (MemoryError, Unfinished) as e:
                        located[bracket] = lib.not_located(ch, self.cause(e))
                        self.cuts.clear()
            bands = lib.band_failures(results, self.scored_controls(gate), located, self.F['cases'])
            census['bands'] = dict(failures=bands)
            if bands:
                raise StopRun(f'the band: {bands[0]}', bands)
            rows = lib.assemble(lib.classify_rows(results, m817, gate['stopped'], left), located)
            for row, r in rows.items():
                say(f"{row}: {r['outcome']}" + (f"; open: {len(r['open'])}" if r['open'] else ''))
            census['rows'] = rows
        except StopRun as s:
            self.stop(s.why, s.detail)
        except MemoryError:
            self.stop(lib.NO_MEMORY, self.job)
        except Exception as e:
            self.stop(f'a defect in the code: {type(e).__name__}: {e}', traceback.format_exc())
        census['stop'] = self.log.get('stop')
        path = self.at('CENSUS.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(dr.jsonable(census), f, indent=1)
        self.log['census'] = dict(file='CENSUS.json', sha256=dr.sha(path), written=dr.now())
        self.log['events'].append(dict(t=dr.now(), event='record written'))
        dr.save_log(self.out, self.log)
        return census

    def scored_controls(self, gate):
        """The controls' case outputs, where the gate read them."""
        return {n: lib.load_json(self.at(dr.safe(n) + '.json')) for n in lib.READ_CONTROLS if self.done(f'case:{n}')}


def main():
    if len(sys.argv) != 1:
        raise SystemExit(__doc__)
    if not __debug__:
        raise SystemExit('refused under python -O, which removes asserts')
    F = frozen()
    t0 = time.perf_counter()
    say(f'M8.18, the census\'s two remedies; outputs in {os.path.relpath(OUT, ROOT)}')
    run = Run(F)
    run.go()
    say(f'{time.perf_counter() - t0:.0f} s')
    tpath = os.path.join(OUT, 'census.out')
    with open(tpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(dr.out_lines) + '\n')
    run.log['transcript'] = dict(file='census.out', sha256=dr.sha(tpath), written=dr.now())
    dr.save_log(OUT, run.log)


if __name__ == '__main__':
    main()
