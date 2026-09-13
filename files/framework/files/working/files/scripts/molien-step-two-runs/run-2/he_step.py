"""Post-verdict diagnosis of the ionization history (no spectrum, no likelihood): the step CAMB leaves in x_e at the start
of helium's second reionization, for CAMB 2.0.4's helium defaults, each E1 helium value alone, and E1's pair. CAMB adds
the second-helium term only below its start redshift, so the start leaves a step of about f_He (1 + tanh(-n)) / 2 in x_e,
where n is the number of widths between z_He and the start.
Usage: CLIPY_NOJAX=1 PYTHONDONTWRITEBYTECODE=1 .venv/bin/python he_step.py <packet dir> <planck dir>
"""
import math, os, sys
pk, data = sys.argv[1], sys.argv[2]
sys.path.insert(0, pk)
import numpy as np
import camb
import step_two_run as R

p, _ = R.read_minimum(os.path.join(data, R.BASELINE_FIT + ".minimum"))
CONFIGS = [("CAMB 2.0.4 defaults (run 1)", 0.4, 5.5), ("width 0.5 alone", 0.5, 5.5), ("start 5.0 alone", 0.4, 5.0),
           ("E1's pair (the 2017 values)", 0.5, 5.0)]
print("configuration                  width  start  widths out  x_e just below  x_e just above  step in x_e   "
      "f_He (1 + tanh(-n)) / 2")
for name, dz, start in CONFIGS:
    pars = R.camb_params(p, for_g1b=True)
    pars.Reion.helium_delta_redshift, pars.Reion.helium_redshiftstart = dz, start
    res = camb.get_background(pars)
    eps = 1e-4
    xe = res.get_background_redshift_evolution(np.array([start - eps, start + eps]), ["x_e"], format="array")[:, 0]
    n = (start - pars.Reion.helium_redshift) / dz
    f_he = pars.YHe / (R_MASS := 3.9715) / (1 - pars.YHe)
    print(f"{name:30} {dz:5.2f}  {start:5.2f}  {n:10.2f}  {xe[0]:14.8f}  {xe[1]:14.8f}  {xe[0] - xe[1]:11.3e}   "
          f"{f_he * (1 + math.tanh(-n)) / 2:11.3e}")
