import json, numpy as np

r = json.load(open('results.json'))
s = json.load(open('results_sctm.json'))
g = json.load(open('results_ground.json'))

rv = [x for x in r if x['tau']=='2' and x['n']==1 and x['placement']=='generic' and abs(x['W']-1.0)<0.01][0]
gv = [x for x in g if x['tau']=='2' and x['n']==1 and x['placement']=='generic' and abs(x['W']-1.0)<0.01][0]

print('=== E^2_1, W=1.0, generic ===')
print(f'hs_val = {rv["hs_val"]:.8f}  exact = {8/np.pi**2:.8f}')
print(f'proj_val = {rv["proj_val"]:.8f}  exact = {8/(3*np.pi**2):.8f}')
print(f'lambda_val = {rv["lambda_val"]:.8f}  exact = {16/(3*np.pi**2):.8f}')
print(f'proj0_val = {gv["proj0_val"]:.8f}  exact = {np.sin(1.0)**2/2:.8f}')
print(f'hs_trans = {rv["hs_trans"]:.8f}  exact = {8/np.pi**2:.8f}')
print(f'proj_trans = {rv["proj_trans"]:.10f}  (should be ~0)')
print(f'proj0_trans = {gv["proj0_trans"]:.8f}  exact = {8/np.pi**2:.8f}')

rv0 = [x for x in r if x['tau']=='1' and x['n']==0 and x['placement']=='generic' and abs(x['W']-1.0)<0.01][0]
gv0 = [x for x in g if x['tau']=='1' and x['n']==0 and x['placement']=='generic' and abs(x['W']-1.0)<0.01][0]
print()
print('=== E^1_0, W=1.0, generic ===')
print(f'hs_val = {rv0["hs_val"]:.8f}  exact = {2/np.pi**2:.8f}')
print(f'proj0_val = {gv0["proj0_val"]:.8f}  exact = {2/np.pi**2:.8f}')
print(f'proj_val = {rv0["proj_val"]:.10f}  (should be 0)')

all_pos = True
for x in r:
    if x['tau'] == '1' and x['n'] == 0:
        continue
    hs_v = x['hs_val']
    lam_v = x['lambda_val']
    if hs_v > 1e-14 and lam_v / hs_v < 1e-12:
        print(f'ZERO Lambda_val: {x["tau"]}_{x["n"]} {x["placement"]} W={x["W"]}')
        all_pos = False
    hs_t = x['hs_trans']
    lam_t = x['lambda_trans']
    if hs_t > 1e-14 and lam_t / hs_t < 1e-12:
        print(f'ZERO Lambda_trans: {x["tau"]}_{x["n"]} {x["placement"]} W={x["W"]}')
        all_pos = False
print()
print(f'All Lambda > 0 for all graded blocks: {all_pos}')

for tau, n in [('3',2), ('5',4), ('2',1), ('4p',3), ('6',5)]:
    vals = []
    for pl in ['generic','2fold','3fold','5fold']:
        x = [x for x in r if x['tau']==tau and x['n']==n and x['placement']==pl and abs(x['W']-1.0)<0.01][0]
        vals.append(x['proj_val'])
    ratio = max(vals)/min(vals) if min(vals)>1e-14 else 999
    print(f'E^{tau}_{n} proj_val ratio: {ratio:.6f} (1.0 = independent)')
