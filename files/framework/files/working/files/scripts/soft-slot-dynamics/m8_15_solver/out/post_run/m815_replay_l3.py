"""Post-run diagnostic, not part of the frozen run: an exact replay of one target's level-3 continuation, to recover the
end reason that the frozen driver's crash on an empty ladder swallowed. It imports the frozen modules from the repo
copy and calls them as m815_branch.run_branch does, with the same case, slot, ladder and inputs. The one difference is
the continuation's existing log parameter, which prints each accepted point and the end. No frozen file is changed.
If the replay reaches any ladder point, it does not reproduce the run, and nothing from it may stand in for the run.

  python3 m815_replay_l3.py <case> <slot>          (run from anywhere; it changes into the repo copy)"""
import os
for _k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import sys, time
SOLVER = ('/Users/blake/mode-identity-theory/.claude/worktrees/confident-varahamihira-0572e1/'
          'files/framework/files/working/files/scripts/soft-slot-dynamics/m8_15_solver')
sys.path.insert(0, SOLVER)
os.chdir(SOLVER)
from m815_common import LevelCase, ladder, EPS_MAX
import m815_branch          # the run's full import closure; nothing runs on import
name, slot = sys.argv[1], int(sys.argv[2])
t0 = time.time()
targets = ladder(0.25, EPS_MAX[slot])
print(f'replay {name}/R{slot} level 3: ladder {len(targets)} points from {targets[0]} to {targets[-1]}', flush=True)
lc3 = LevelCase(3, name, slot)
reached = []
br3 = lc3.branch(targets, lambda k, e, rec: reached.append(e), log=lambda s: print(s, flush=True))
print(f'end: {br3.end}; ladder points reached: {len(reached)}; accepted Newton solutions: {len(br3.accepted)}; '
      f'{time.time() - t0:.0f} s', flush=True)
