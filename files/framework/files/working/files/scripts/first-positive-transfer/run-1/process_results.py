"""
Process results from compute_all.py and produce tables for RETURN.md.
"""
import json
import numpy as np


def load_results(filename='results.json'):
    with open(filename) as f:
        return json.load(f)


def format_sci(x, digits=4):
    if x is None:
        return "N/A"
    if abs(x) < 1e-14:
        return "0"
    return f"{x:.{digits}e}"


def format_dec(x, digits=6):
    if x is None:
        return "N/A"
    if abs(x) < 1e-14:
        return "0"
    return f"{x:.{digits}f}"


def outcome_class(results, tau, sampler, arm):
    """Determine outcome class for a given arm/sampler/cone condition.
    S: Λ = 0 for all W, all placements
    P: Λ = 0 at all placements, symbolically in W
    N: Λ > 0 at some placement
    """
    threshold_rel = 1e-12

    for r in results:
        if r['tau'] != tau:
            continue
        key = f'lambda_{sampler}'
        hs_key = f'hs_{sampler}'
        lam = r[key]
        hs = r[hs_key]
        if hs > 0 and abs(lam)/hs > threshold_rel:
            return 'N'
    return 'S or P'


def print_block_table(results, widths=[0.25, 0.5, 1.0, 1.4]):
    """Print a summary table of results."""
    from core import BLOCKS, minus1_acts_as_minus

    print("\n=== VALUE SAMPLER (O^(0)) ===")
    print(f"{'Block':>8} | {'arm':>8} | {'placement':>8} | ", end="")
    for W in widths:
        print(f"{'||O||^2':>12} {'||P1O||^2':>12} {'Lambda':>12} | ", end="")
    print()

    for tau, n in BLOCKS:
        is_minus = minus1_acts_as_minus(tau)
        arm = 'twisted' if is_minus else 'untwisted'
        for pname in ['generic', '2fold', '3fold', '5fold']:
            row_data = []
            for W in widths:
                r = next((x for x in results
                         if x['tau'] == tau and x['n'] == n
                         and x['placement'] == pname and abs(x['W'] - W) < 0.01), None)
                if r:
                    row_data.append((r['hs_val'], r['proj_val'], r['lambda_val']))
                else:
                    row_data.append((None, None, None))

            if pname == 'generic':
                print(f"E^{tau}_{n:>2} | {arm:>8} | {pname:>8} | ", end="")
            else:
                print(f"{'':>8} | {'':>8} | {pname:>8} | ", end="")
            for hs, proj, lam in row_data:
                print(f"{format_sci(hs):>12} {format_sci(proj):>12} {format_sci(lam):>12} | ", end="")
            print()

    print("\n=== TRANSVERSE SAMPLER (O^(1)) ===")
    for tau, n in BLOCKS:
        is_minus = minus1_acts_as_minus(tau)
        arm = 'untwisted' if is_minus else 'twisted'
        for pname in ['generic', '2fold', '3fold', '5fold']:
            row_data = []
            for W in widths:
                r = next((x for x in results
                         if x['tau'] == tau and x['n'] == n
                         and x['placement'] == pname and abs(x['W'] - W) < 0.01), None)
                if r:
                    row_data.append((r['hs_trans'], r['proj_trans'], r['lambda_trans']))
                else:
                    row_data.append((None, None, None))

            if pname == 'generic':
                print(f"E^{tau}_{n:>2} | {arm:>8} | {pname:>8} | ", end="")
            else:
                print(f"{'':>8} | {'':>8} | {pname:>8} | ", end="")
            for hs, proj, lam in row_data:
                print(f"{format_sci(hs):>12} {format_sci(proj):>12} {format_sci(lam):>12} | ", end="")
            print()


def check_W_linearity(results):
    """Check if quantities are linear in W."""
    from core import BLOCKS
    widths = [0.25, 0.5, 1.0, 1.4]

    print("\n=== W-dependence check ===")
    for tau, n in BLOCKS:
        for pname in ['generic']:
            vals_hs = []
            vals_proj = []
            for W in widths:
                r = next((x for x in results
                         if x['tau'] == tau and x['n'] == n
                         and x['placement'] == pname and abs(x['W'] - W) < 0.01), None)
                if r:
                    vals_hs.append(r['hs_val'])
                    vals_proj.append(r['proj_val'])

            if len(vals_hs) == 4:
                ratios_hs = [v/W for v, W in zip(vals_hs, widths)]
                is_linear_hs = max(ratios_hs)/min(ratios_hs) < 1.01 if min(ratios_hs) > 0 else False

                ratios_proj = [v/W for v, W in zip(vals_proj, widths)]
                is_linear_proj = (max(ratios_proj)/min(ratios_proj) < 1.01
                                 if min(ratios_proj) > 1e-15 else False)

                if is_linear_hs:
                    print(f"  E^{tau}_{n}: hs_val ∝ W (ratio ≈ {np.mean(ratios_hs):.6f})")
                if is_linear_proj:
                    print(f"  E^{tau}_{n}: proj_val ∝ W (ratio ≈ {np.mean(ratios_proj):.6f})")


def generate_markdown_tables(results, widths=[0.25, 0.5, 1.0, 1.4]):
    """Generate markdown tables for RETURN.md."""
    from core import BLOCKS, minus1_acts_as_minus

    lines = []

    lines.append("### Numerical Results: Friedrichs / Bridging")
    lines.append("")

    for sampler_label, s_key, arm_fn in [
        ("Value sampler O^(0)", "val", lambda tau: "twisted" if minus1_acts_as_minus(tau) else "untwisted"),
        ("Transverse sampler O^(1)", "trans", lambda tau: "untwisted" if minus1_acts_as_minus(tau) else "twisted"),
    ]:
        lines.append(f"#### {sampler_label}")
        lines.append("")

        for pname in ['generic', '2fold', '3fold', '5fold']:
            lines.append(f"**Placement: {pname}**")
            lines.append("")
            lines.append(f"| Block | Arm | " + " | ".join(f"W={W}" for W in widths) + " |")
            lines.append(f"|---|---|" + "|".join(["---"] * len(widths)) + "|")

            for tau, n in BLOCKS:
                arm = arm_fn(tau)
                row = f"| E^{tau}\\_{n} | {arm} |"
                for W in widths:
                    r = next((x for x in results
                             if x['tau'] == tau and x['n'] == n
                             and x['placement'] == pname and abs(x['W'] - W) < 0.01), None)
                    if r:
                        hs = r[f'hs_{s_key}']
                        proj = r[f'proj_{s_key}']
                        lam = r[f'lambda_{s_key}']
                        cell = f"Λ={format_sci(lam, 3)}"
                    else:
                        cell = "missing"
                    row += f" {cell} |"
                lines.append(row)
            lines.append("")

    return "\n".join(lines)


if __name__ == '__main__':
    try:
        results = load_results()
        print(f"Loaded {len(results)} results")
        print_block_table(results)
        check_W_linearity(results)

        md = generate_markdown_tables(results)
        with open('tables.md', 'w') as f:
            f.write(md)
        print("\nMarkdown tables written to tables.md")
    except FileNotFoundError:
        print("results.json not found. Run compute_all.py first.")
