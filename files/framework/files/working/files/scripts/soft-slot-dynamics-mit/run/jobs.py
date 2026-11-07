#!/usr/bin/env python3
"""One job of MIT's own computation, in a process of its own (DESIGN.md); run/runner.py starts them side by side.

Usage: jobs.py OUT path TAG N                         a path at one cutoff, solved and read nowhere
       jobs.py OUT read TAG N --note COMMIT --repo R  its records, from the stored solutions
       jobs.py OUT identity TAG N1 N2 --note ...      branch identity between two cutoffs, from the records
       jobs.py OUT reading TAG --note ...             the rule on the ladder: both verdicts at every point
       jobs.py OUT fresh --note ...                   the fresh controls against their marks, the pass the rows need
       jobs.py OUT reread TAG N SOURCE                M8.18's stored solutions read again, against its records
       jobs.py OUT locate_repro SOURCE --note ...     M8.18's Arm B run again, against its record (run/locate.py)
       jobs.py OUT locate --note ...                  T4/R4's locator, once the reproduction has passed
       jobs.py OUT recheck48 TAG N --note ...         T5's top at N = 48 (run/TOP48.md): the stored reads at N = 32
                                                      or 40, at the points the new ladder reads, read again
       jobs.py OUT read48 TAG --note ...              its records at N = 48, once its recheck has passed
       jobs.py OUT identity48 TAG --note ...          branch identity between N = 40 and 48
       jobs.py OUT reading48 TAG --note ...           the rule on N = 32, 40 and 48: both verdicts at every point
       jobs.py OUT fresh48 --note ...                 the fresh controls against their marks on the new ladder
       jobs.py OUT top48 --note ...                   T5's in-row controls against their marks, and each target

A job is one file set, in OUT, with a record in OUT/jobs/ holding each file's SHA-256, its time and its peak resident
size. A path is written point by point, so a killed job resumes at its next point and loses only the one under way. A
stored solution is used only through its hash and its lam, as M8.18's solve-state gate does, and only from a path solved
under a manifest in SOLVE_PINS (stored). The solve is census.Cutoff's, and so runs inside checks.withheld, where every
record path refuses.

No read of this computation's own solutions runs before the dated note: note_gate wants a commit on the repository's
origin/main whose census page names this tree's manifest pin. No row is read before the fresh controls pass: fresh.refusal
wants the record of a pass. reread alone needs no note: it refuses any tag but M8.18's controls and any source but M8.18's
published files, by M8.18's SHA256SUMS, pinned here, so it reads only points whose records are on file.

T5's top at N = 48 (run/TOP48.md) reads only after its recheck has passed, and T5 itself only after the fresh controls
have passed on the new ladder (fresh.refusal_48). Its paths at N = 48 are path jobs like any other, solved under their
own pin, which a later tree adds to SOLVE_PINS.
"""
import json
import os
import resource
import subprocess
import sys
import time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from instrument import devtools  # noqa: E402
import checks as ck  # noqa: E402
import driver as dr  # noqa: E402
import census_lib as lib  # noqa: E402
import census  # noqa: E402
import changed  # noqa: E402
import fresh  # noqa: E402
import grid  # noqa: E402

NOTE_PAGE = 'files/framework/files/working/files/slot-dynamics-census.md'
NEW_FIELDS = frozenset(('b_resolved', 'd_eigs', 'l_near', 'members'))        # what a read here adds to M8.18's point
M818_SUMS = '69b88f8c8bacb5722510b1f9110199ac9b6a8cc24112a1aedb8a3a3c594a80b7'   # M8.18's SHA256SUMS, which lists its run/out
# the manifests the paths were solved under
SOLVE_PINS = frozenset(('391b097fa6164e502c341b384381d19207d943f5692bb67f43a1cb2c28d49c65',
                        '80df072cca091ce8722ba593b79580e4132b37db0e9a62a31bc324c445f9ebcf'))


def say(s):
    print(s, flush=True)


def note_gate(commit, repo):
    """Refuses unless commit is on repo's origin/main and the census page at it names this tree's manifest pin."""
    if not commit or not repo:
        raise PermissionError('no read of this computation before the dated note: no commit given')
    with open(os.path.join(ROOT, 'run', 'MANIFEST_PIN'), encoding='utf-8') as f:
        pin = f.read().strip()
    if devtools.manifest()[1] != pin:
        raise PermissionError('the running tree differs from run/MANIFEST_PIN')
    git = lambda *a: subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True)  # noqa: E731
    if git('merge-base', '--is-ancestor', commit, 'origin/main').returncode != 0:
        raise PermissionError(f'the note commit {commit} is not on origin/main')
    page = git('show', f'{commit}:{NOTE_PAGE}')
    if page.returncode != 0 or pin not in page.stdout:
        raise PermissionError(f'the census page at {commit} does not name the manifest pin {pin}')


def atomic(path, write):
    """Write through a temporary name, so a kill leaves the last whole file."""
    tmp = path + '.tmp'
    with open(tmp, 'wb') as f:
        write(f)
    os.replace(tmp, path)


def write_json(path, obj):
    atomic(path, lambda f: f.write(json.dumps(dr.jsonable(obj), indent=1).encode('utf-8')))


def write_path(stem, seed, sols, seconds):
    """A path's two files, in M8.18's layout: the solutions, and the seed and solve fields of every point."""
    done = {k: s for k, s in sols.items() if s['state'] is not None}
    arrays = {f'c{i}': s['state'][0] for i, s in enumerate(done.values())}
    arrays.update(keys=np.array(list(done) or ['']), lam=np.array([float(s['state'][1]) for s in done.values()]),
                  slope=np.array([float(s['state'][2]) for s in done.values()]))
    atomic(stem + '.npz', lambda f: np.savez(f, **arrays))
    write_json(stem + '.json', dict(seed=seed, points={k: s['point'] for k, s in sols.items()}, setup_seconds=seconds))


def load_path(stem):
    """(seed, sols) from a path's two files, or None where they are absent. A kill between the two files leaves the
    solutions a point ahead of the fields, or behind: only points both hold are kept."""
    if not (os.path.exists(stem + '.npz') and os.path.exists(stem + '.json')):
        return None
    meta = lib.load_json(stem + '.json')
    with np.load(stem + '.npz', allow_pickle=False) as z:
        arrays = {k: z[k] for k in z.files}
    sols = {}
    for k, p in meta['points'].items():
        sols[k] = dict(ok=False, why=p.get('reason'), eps=None, state=None, c=None, k1=False, nL=None, point=p)
    for i, k in enumerate(str(x) for x in arrays['keys'] if str(x)):
        if k not in meta['points']:
            continue
        lam, slope, c = float(arrays['lam'][i]), float(arrays['slope'][i]), arrays[f'c{i}']
        if lam != meta['points'][k]['lam']:
            raise RuntimeError(f'the stored lam of {stem} at {k} differs from its solve fields')
        sols[k] = dict(sols[k], ok=bool(meta['points'][k]['accepted']), state=(c, lam, slope), c=c, eps=float(k))
    return meta['seed'], sols


class Cut(census.Cutoff):
    """census.Cutoff, solved a point at a time into a checkpoint, and read with changed.capture beside the record."""

    def __init__(self, name, case, N):
        super().__init__(name, case, N, lambda: True)

    def solved(self, stem):
        """Cutoff.solves over the case's points: from the last point the checkpoint holds, or from the seed, as
        Cutoff.solves starts. A path ends where a step fails. The state and the slope are stored at full precision, so
        a resumed path is the path run through."""
        grid_ = [p['eps'] for p in self.case['points']]
        held = load_path(stem + '.partial')
        sols = dict(held[1]) if held else {}
        for k in list(sols):
            if sols[k]['state'] is None:          # a failed last point is solved again
                del sols[k]
        done = [e for e in grid_ if lib.key(e) in sols]
        if [lib.key(e) for e in grid_[:len(done)]] != list(sols):
            raise RuntimeError(f'the checkpoint {stem} is not a prefix of the path')
        if done:
            last = sols[lib.key(done[-1])]
            state, acc = last['state'], True
            say(f'   resuming at {done[-1]:g}, {len(done)} of {len(grid_)} points held')
        else:
            state, acc = (np.sqrt(grid_[0] / self.chk['Q']) * self.u, self.case['lam0'] + grid_[0], 1 / self.chk['Q']), False
        t0 = time.perf_counter()
        for e in grid_[len(done):]:
            s = self.solve(state, e, prev_accepted=acc)
            sols[lib.key(e)] = s
            write_path(stem + '.partial', self.seed(), sols, time.perf_counter() - t0)
            say(f"   {lib.key(e)}: {'accepted' if s['ok'] else s['why']}; {s['point'].get('seconds', 0):.0f} s")
            if s['state'] is None:
                break
            state, acc = s['state'], True
        return sols, time.perf_counter() - t0

    def read(self, s, eps, why='mit'):
        with changed.capture() as held:
            point, _, _ = dr.read_point(self.Fn, self.K, s['c'], s['point']['lam'], self.case, eps, False)
        point.update(s['point'])
        point.update(held)
        return dict(s, k1=bool(s['ok'] and ck.k1(point, self.case)), nL=lib.nl_at(point), point=point)


class Job:
    """One job's outputs and its record."""

    def __init__(self, out, job):
        self.out, self.job, self.t0 = out, job, time.perf_counter()
        os.makedirs(os.path.join(out, 'jobs'), exist_ok=True)

    def at(self, f):
        return os.path.join(self.out, f)

    def done(self):
        return os.path.exists(self.at(os.path.join('jobs', self.job + '.json')))

    def complete(self, files):
        write_json(self.at(os.path.join('jobs', self.job + '.json')),
                   dict(job=self.job, files={f: dr.sha(self.at(f)) for f in files}, t=dr.now(),
                        seconds=time.perf_counter() - self.t0, manifest=devtools.manifest()[1],
                        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        say(f'{self.job}: complete, {time.perf_counter() - self.t0:.0f} s')


def record_of(out, job):
    """A completed job's record, with each file's SHA-256 checked."""
    path = os.path.join(out, 'jobs', job + '.json')
    if not os.path.exists(path):
        raise PermissionError(f'no completed job {job}')
    rec = lib.load_json(path)
    for f, h in rec['files'].items():
        if dr.sha(os.path.join(out, f)) != h:
            raise PermissionError(f'{f} differs from the SHA-256 its job logged')
    return rec


def stored(out, tag, N):
    """A path's solutions through the solve-state gate, from a path solved under a solve pin: (seed, sols)."""
    rec = record_of(out, f'path_{tag}_N{N}')
    if rec['manifest'] not in SOLVE_PINS:
        raise PermissionError(f"{tag} at N = {N} was solved under {rec['manifest']}, not a solve pin")
    held = load_path(os.path.join(out, f'{tag}_N{N}'))
    if held is None:
        raise PermissionError(f'no stored path for {tag} at N = {N}')
    return held


def path(out, tag, N):
    if N > 48 or (N == 48 and tag not in grid.PATHS_48):
        raise PermissionError(f'no path for {tag} at N = {N}: N = 48 solves grid.PATHS_48 alone (run/TOP48.md)')
    job = Job(out, f'path_{tag}_N{N}')
    if job.done():
        return
    name, eps, case = grid.entry(tag)
    devtools.require(case['admission'])
    stem = job.at(f'{tag}_N{N}')
    cu = Cut(name, case, N)
    sols, seconds = cu.solved(stem) if cu.seed_ok else ({}, 0.0)
    write_path(stem, cu.seed(), sols, seconds)
    for ext in ('.npz', '.json'):
        if os.path.exists(stem + '.partial' + ext):
            os.remove(stem + '.partial' + ext)
    job.complete([f'{tag}_N{N}.npz', f'{tag}_N{N}.json'])
    say(f"   {sum(s['state'] is not None for s in sols.values())} of {len(eps)} points solved")


def read(out, tag, N):
    job = Job(out, f'read_{tag}_N{N}')
    if job.done():
        return
    name, eps, case = grid.entry(tag)
    if N == 48:
        eps = points_48(tag)
    devtools.require(case['admission'])
    seed, sols = stored(out, tag, N)
    fname = f'{tag}_N{N}_read.json'
    held = job.at(fname + '.partial')
    pts = lib.load_json(held) if os.path.exists(held) else {}
    cu = Cut(name, case, N)
    for e in eps:
        k, s = lib.key(e), sols.get(lib.key(e))
        if k in pts or not s:
            continue
        pts[k] = cu.read(s, e)['point'] if s['ok'] else s['point']
        write_json(held, pts)
        say(f"   {k}: read, {pts[k].get('seconds_record', 0):.0f} s")
    write_json(job.at(fname), dict(seed=seed, points=pts))
    os.remove(held)
    job.complete([fname])


def identity(out, tag, Na, Nb):
    job = Job(out, f'identity_{tag}_{Na}_{Nb}')
    if job.done():
        return
    name, eps, case = grid.entry(tag)
    if 48 in (Na, Nb):
        eps = points_48(tag)
    devtools.require(case['admission'])
    cuts = {N: Cut(name, case, N) for N in (Na, Nb)}
    st = {N: stored(out, tag, N)[1] for N in (Na, Nb)}
    recs = {N: lib.load_json(job.at(f'{tag}_N{N}_read.json'))['points'] for N in (Na, Nb)}
    res = {}
    for e in eps:
        k, sols = lib.key(e), {}
        for N in (Na, Nb):
            s = st[N].get(k)
            sols[N] = dict(s, point=recs[N][k]) if s and s['c'] is not None and k in recs[N] else None
        res[k] = census.identity(cuts, sols, (Na, Nb))
    fname = f'{tag}_identity_{Na}_{Nb}.json'
    write_json(job.at(fname), res)
    job.complete([fname])


def rule(pts):
    """Both verdicts at one point, each on the band above N = 16, with the as-built reading on the band above N = 24
    beside it: (as built, beside, changed)."""
    built, beside = census.rule(pts)
    if built.get('reasons') == ['a cutoff is missing']:
        return built, beside, built
    hi = pts[-1]
    return built, beside, changed.reading([q['summary'] for q in pts], [q['b_resolved'] for q in pts], hi['eig'], hi['lam'],
                                          hi['record']['margin'], lib.BAND_N, [q['members'] for q in pts])


def ladder_reading(out, tag, ladder, lad, eps=None):
    """The rule on one ladder at an entry's points, or at eps: both verdicts at every point. On the first ladder it is
    the reading every row's file holds; on the new one, run/TOP48.md's."""
    name, all_eps, case = grid.entry(tag)
    eps = all_eps if eps is None else eps
    recs = {N: lib.load_json(os.path.join(out, f'{tag}_N{N}_read.json')) for N in ladder}
    pairs = list(zip(ladder, ladder[1:]))
    ids = {lib.pair_key(p): lib.load_json(os.path.join(out, f'{tag}_identity_{p[0]}_{p[1]}.json')) for p in pairs}
    res = dict(case=dict(case, cutoffs=list(ladder)), cutoffs={str(N): recs[N] for N in ladder}, readings={}, beside={},
               changed={}, identity={}, both={})
    for e in eps:
        k = lib.key(e)
        pts = [recs[N]['points'].get(k) for N in ladder]
        res['readings'][k], res['beside'][k], res['changed'][k] = rule(pts)
        res['identity'][k] = {pk: v.get(k) for pk, v in ids.items()}
    res = census.roundtrip(res)
    for e in eps:
        k = lib.key(e)
        a = lib.here(lib.at(res, e, lad), res['case'], lad)
        pb = lib.at(dict(res, readings=res['changed']), e, lad)
        pb['identity'] = {lib.pair_key(p): changed.identity(pb['identity'].get(lib.pair_key(p)), pb['points'], p)
                          for p in lad['pairs']}
        b = lib.here(pb, res['case'], lad)
        res['both'][k] = dict(as_built=a, changed=b, same=a == b)
    return res


def reading(out, tag):
    job = Job(out, f'reading_{tag}')
    if job.done():
        return
    res = ladder_reading(out, tag, grid.LADDER, lib.ARM_A)
    fname = f'{tag}.json'
    write_json(job.at(fname), res)
    job.complete([fname])


# --- T5's top at N = 48 (run/TOP48.md) --------------------------------------------------------------------------------
def points_48(tag):
    """The amplitudes the new ladder reads on one entry: T5's targets and in-row controls, or a fresh control's every
    point. Any other entry refuses."""
    name, eps, case = grid.entry(tag)
    if tag == grid.TOP48['row']:
        want = {lib.key(e) for e in grid.TOP48['targets'] + grid.TOP48['in_row']}
        got = [e for e in eps if lib.key(e) in want]
        if len(got) != len(want):
            raise RuntimeError("T5's grid does not hold every point the new ladder reads")
        return got
    if tag in grid.FRESH:
        return list(eps)
    raise PermissionError(f'the new ladder reads T5 and the fresh controls alone, not {tag}')


def recheck48(out, tag, N):
    """The stored solutions at N = 32 or 40, at the points the new ladder reads, read again by this tree, each against
    its stored read field for field, timings aside (run/TOP48.md, section 4). Nothing new is read."""
    if N not in grid.LADDER_48[:2]:
        raise PermissionError(f'the recheck reads N = 32 and 40 alone, not {N}')
    job = Job(out, f'recheck48_{tag}_N{N}')
    if job.done():
        return
    name, eps, case = grid.entry(tag)
    devtools.require(case['admission'])
    seed, sols = stored(out, tag, N)
    record_of(out, f'read_{tag}_N{N}')
    theirs = lib.load_json(job.at(f'{tag}_N{N}_read.json'))['points']
    cu = Cut(name, case, N)
    res = {}
    for e in points_48(tag):
        k, s = lib.key(e), sols[lib.key(e)]
        mine = census.roundtrip(cu.read(s, e)['point'] if s['ok'] else s['point'])
        res[k] = lib.differences(mine, theirs[k])
        say(f'   {k}: {len(res[k])} differences')
    fname = f'recheck48_{tag}_N{N}.json'
    write_json(job.at(fname), dict(differences=res, same=not any(res.values())))
    job.complete([fname])


def recheck_refusal(out, tag):
    """Why the new ladder may not read tag at N = 48 yet, or None once its recheck has passed at N = 32 and 40."""
    for N in grid.LADDER_48[:2]:
        job = f'recheck48_{tag}_N{N}'
        try:
            record_of(out, job)
        except PermissionError as e:
            return str(e)
        if not lib.load_json(os.path.join(out, job + '.json'))['same']:
            return f'{job} found a difference from the stored read'
    return None


def reading48(out, tag):
    """The rule on N = 32, 40 and 48 at the points the new ladder reads, both verdicts at each, from files checked
    against the jobs that wrote them."""
    job = Job(out, f'reading48_{tag}')
    if job.done():
        return
    for N in grid.LADDER_48:
        record_of(out, f'read_{tag}_N{N}')
    for a, b in grid.LAD_48['pairs']:
        record_of(out, f'identity_{tag}_{a}_{b}')
    res = ladder_reading(out, tag, grid.LADDER_48, grid.LAD_48, points_48(tag))
    fname = f'{tag}_L48.json'
    write_json(job.at(fname), res)
    job.complete([fname])


def fresh48_job(out):
    """The fresh controls against their marks on the new ladder: the record fresh.refusal_48 reads."""
    name, pass_file = fresh.names_48()
    job = Job(out, name)
    if job.done():
        return
    for tag in sorted({t for t, _ in grid.PASS_MARKS_48}):
        record_of(out, f'reading48_{tag}')
    res = fresh.evaluate_48(out)
    write_json(job.at(pass_file), res)
    job.complete([pass_file])
    say(f"   {sum(not v for v in res['results'].values())} of {len(res['results'])} points hold their marks")


def top48(out):
    """T5's top on the new ladder (run/TOP48.md, section 6): each in-row control against its marks, then each target's
    readings both ways, beside its reading on the first ladder. If an in-row control misses, no target is classified on
    the new ladder, and each target's reading there is kept as reported."""
    job = Job(out, 'top48')
    if job.done():
        return
    tag = grid.TOP48['row']
    record_of(out, f'reading48_{tag}')
    record_of(out, f'reading_{tag}')
    new = lib.load_json(os.path.join(out, f'{tag}_L48.json'))
    first = lib.load_json(os.path.join(out, f'{tag}.json'))
    marks = grid.TOP48['in_row_marks']
    controls = {}
    for e in grid.TOP48['in_row']:
        k, miss = lib.key(e), []
        for arm, c in new['both'][k].items():
            if arm == 'same':
                continue
            if not c['classified']:
                miss.append(f"{arm}: not classified: {'; '.join(c['causes'])}")
            elif any(c[f] != v for f, v in marks.items()):
                miss.append(f"{arm}: {c['type']} ({c['nL']}, {c['nD']}, {c['K']}), marked {marks}")
        controls[k] = miss
    held = not any(controls.values())
    targets = {}
    for e in grid.TOP48['targets']:
        k, b = lib.key(e), new['both'][lib.key(e)]
        on_48 = {arm: b[arm] if held else dict(classified=False, causes=['an in-row control missed its marks'],
                                               reported=b[arm]) for arm in ('as_built', 'changed')}
        targets[k] = dict(on_48=on_48, same=b['same'], on_first=first['both'][k])
    res = dict(ladder=list(grid.LADDER_48), first_ladder=list(grid.LADDER), in_row=controls, in_row_held=held,
               targets=targets)
    write_json(job.at('TOP48.json'), res)
    job.complete(['TOP48.json'])
    say(f"   in-row controls held: {held}; classified on the new ladder, as built: "
        f"{[k for k, t in targets.items() if t['on_48']['as_built']['classified']]}")


def fresh_job(out):
    """The fresh controls against their marks: the record fresh.refusal reads, named by the marks it tests."""
    name, pass_file = fresh.names()
    job = Job(out, name)
    if job.done():
        return
    res = fresh.evaluate(out)
    write_json(job.at(pass_file), res)
    job.complete([pass_file])
    say(f"   {sum(not v for v in res['results'].values())} of {len(res['results'])} points hold their marks")


def m818_files(source, tag, N):
    """Refuses unless tag is one of M8.18's controls and source is M8.18's run/out, its files by M8.18's SHA256SUMS."""
    if tag not in grid.CONTROLS:
        raise PermissionError(f'reread reads M8.18 controls alone, not {tag}')
    sums = os.path.join(source, os.pardir, os.pardir, 'SHA256SUMS')
    if not os.path.exists(sums) or dr.sha(sums) != M818_SUMS:
        raise PermissionError(f"{source} is not M8.18's published output: its SHA256SUMS is not the pinned one")
    with open(sums, encoding='utf-8') as f:
        held = {line.split(None, 1)[1].strip(): line.split()[0] for line in f}
    base = f'{dr.safe(grid.CONTROLS[tag])}_N{N}'
    for f in (base + '.npz', base + '.json', base + '_read.json'):
        p = os.path.join(source, f)
        if not os.path.exists(p) or dr.sha(p) != held.get(f'run/out/{f}'):
            raise PermissionError(f"{f} differs from M8.18's SHA256SUMS")


def reread(out, tag, N, source):
    """M8.18's solutions at one cutoff read again by this tree's code, every field against M8.18's record, timings and
    the new fields aside. Nothing new is read: every point here has a record on file."""
    m818_files(source, tag, N)
    job = Job(out, f'reread_{tag}_N{N}')
    if job.done():
        return
    name, eps, case = grid.entry(tag)
    devtools.require(case['admission'])
    base = os.path.join(source, f'{dr.safe(name)}_N{N}')
    theirs = lib.load_json(base + '_read.json')
    seed, sols = load_path(base)
    cu = Cut(name, case, N)
    res, pts = {}, {}
    for e in eps:
        k = lib.key(e)
        s = dict(sols[k], point={x: theirs['points'][k][x] for x in ('accepted', 'eps_reached', 'lam', 'm', 'evaluations',
                                                                     'floor_rel', 'seconds')})
        pts[k] = census.roundtrip(cu.read(s, e)['point'])
        d = lib.differences(pts[k], theirs['points'][k], ignore=lib.TIMINGS | NEW_FIELDS | lib.NOT_COMPUTED)
        res[k] = dict(differences=d, b_resolved=pts[k]['b_resolved'], d_eigs=pts[k]['d_eigs'], l_near=pts[k]['l_near'],
                      unresolved=pts[k]['record']['unresolved'])
        say(f'   {k}: {len(d)} differences; b_resolved {pts[k]["b_resolved"]}')
    fname, read_file = f'reread_{tag}_N{N}.json', f'{tag}_N{N}_read.json'
    write_json(job.at(fname), res)
    write_json(job.at(read_file), dict(seed=seed, points=pts))
    Job(out, f'read_{tag}_N{N}').complete([read_file])
    job.complete([fname])


def main():
    argv = sys.argv[1:]
    if not __debug__:
        raise SystemExit('refused under python -O, which removes asserts')
    note = repo = None
    if '--note' in argv:
        i = argv.index('--note')
        note, repo = argv[i + 1], argv[argv.index('--repo') + 1]
        argv = argv[:i]
    out, kind, args = argv[0], argv[1], argv[2:]
    os.makedirs(out, exist_ok=True)
    if kind == 'path':
        path(out, args[0], int(args[1]))
    elif kind == 'reread':
        reread(out, args[0], int(args[1]), args[2])
    elif kind in ('locate_repro', 'locate'):
        note_gate(note, repo)
        import locate                   # here, since run/locate.py imports this module
        if kind == 'locate_repro':
            locate.repro(out, args[0])
            why = locate.refusal(out)
            if why:                     # on record and failed: exit nonzero, so the runner reports the job failed
                raise SystemExit(f'{why}; its record stands, and T4/R4 is not read')
            return
        why = fresh.refusal(out)
        if why:
            raise PermissionError(f'no row is read before the fresh controls pass: {why}')
        locate.locate(out)
    elif kind in ('recheck48', 'read48', 'identity48', 'reading48', 'fresh48', 'top48'):
        note_gate(note, repo)
        if kind == 'fresh48':
            fresh48_job(out)
            return
        tag = grid.TOP48['row'] if kind == 'top48' else args[0]
        why = fresh.refusal(out) if tag in grid.ROWS else None
        if not why and tag in grid.ROWS and kind != 'recheck48':
            why = fresh.refusal_48(out)
        if why:
            raise PermissionError(f"no read of T5's top at N = 48 before the fresh controls pass: {why}")
        if kind == 'top48':
            top48(out)
            return
        if kind == 'recheck48':
            recheck48(out, tag, int(args[1]))
            return
        why = recheck_refusal(out, tag)
        if why:
            raise PermissionError(f'no read at N = 48 before the recheck passes: {why}')
        if kind == 'read48':
            read(out, tag, 48)
        elif kind == 'identity48':
            identity(out, tag, 40, 48)
        else:
            reading48(out, tag)
    elif kind in ('read', 'identity', 'reading', 'fresh'):
        note_gate(note, repo)
        if kind == 'fresh':
            fresh_job(out)
            return
        if kind in ('read', 'identity') and 48 in [int(x) for x in args[1:]]:
            raise PermissionError('N = 48 is read by read48 and identity48 alone, behind their gates (run/TOP48.md)')
        why = fresh.refusal(out) if args[0] in grid.ROWS else None
        if why:
            raise PermissionError(f'no row is read before the fresh controls pass: {why}')
        if kind == 'read':
            read(out, args[0], int(args[1]))
        elif kind == 'identity':
            identity(out, args[0], int(args[1]), int(args[2]))
        else:
            reading(out, args[0])
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
