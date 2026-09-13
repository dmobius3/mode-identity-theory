"""G1b's CAMB configuration beside the Planck fit's own derived background quantities: the gate's own computation, no
variant. Run against the freeze runner it reproduces run 1's g1b_background.out; against the E1 runner, run 2's.
Usage: CLIPY_NOJAX=1 PYTHONDONTWRITEBYTECODE=1 .venv/bin/python g1b_background.py <packet dir> <planck dir>
"""
import os, sys
pk, data = sys.argv[1], sys.argv[2]
sys.path.insert(0, pk)
import camb
import step_two_run as R
p, _ = R.read_minimum(os.path.join(data, R.BASELINE_FIT + ".minimum"))
pars = R.camb_params(p, for_g1b=True)
res = camb.get_results(pars)
der = res.get_derived_params()
rows = [("H0", res.Params.H0, p["H0"]), ("Y_P used", res.Params.YHe, p["yheused"]), ("z_re", res.Params.Reion.redshift, p["zrei"]),
        ("z_star", der["zstar"], p["zstar"]), ("100 theta_star", der["thetastar"], p["thetastar"])]
print("quantity         CAMB 2.0.4      Planck 2018 fit   relative difference")
for name, mine, theirs in rows:
    print(f"{name:15} {mine:13.6f}   {theirs:13.6f}     {mine / theirs - 1:+.2e}")
