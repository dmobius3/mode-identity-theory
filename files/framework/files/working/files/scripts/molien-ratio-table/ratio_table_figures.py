#!/usr/bin/env python3
"""Two figures drawn from the ratio table's result file (contract section 4): the spectra, and the ratios beside the two
pre-freeze estimates. They present the recorded table and add nothing to it: no data, no likelihood value, no
cosmic-variance band. Standard library only: plain SVG, with a light palette and a dark one chosen by the viewer's scheme.
Usage: python ratio_table_figures.py <result.json> <output folder outside the packet>
"""
import json, math, os, sys
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
LMIN, LMAX = 2, 29
XTICKS = (2, 5, 10, 15, 20, 25, 29)
# The charting skill's validated reference palette: categorical slots 1 and 2 for the two routes, ink for LambdaCDM.
LIGHT = {"surface": "#fcfcfb", "ink": "#0b0b0b", "ink2": "#52514e", "muted": "#898781", "grid": "#e1e0d9", "axis": "#c3c2b7",
         "band": "#f0efec", "a": "#2a78d6", "b": "#eb6834"}
DARK = {"surface": "#1a1a19", "ink": "#ffffff", "ink2": "#c3c2b7", "muted": "#898781", "grid": "#2c2c2a", "axis": "#383835",
        "band": "#383835", "a": "#3987e5", "b": "#d95926"}
LINE = "fill: none; stroke-width: 2; stroke-linejoin: round; stroke-linecap: round"
CLASSES = {   # class: (colour properties as (property, token), fixed properties)
    "bg": ((("fill", "surface"),), ""),
    "grid": ((("stroke", "grid"),), "stroke-width: 1; shape-rendering: crispEdges"),
    "axis": ((("stroke", "axis"),), "stroke-width: 1; shape-rendering: crispEdges"),
    "band": ((("fill", "grid"),), ""),
    "t1": ((("fill", "ink"),), "font-size: 15px; font-weight: 600"),
    "t2": ((("fill", "ink2"),), "font-size: 12px"),
    "tm": ((("fill", "muted"),), "font-size: 11px; font-variant-numeric: tabular-nums"),
    "l-lcdm": ((("stroke", "ink2"),), LINE), "l-A": ((("stroke", "a"),), LINE), "l-B": ((("stroke", "b"),), LINE),
    "m-lcdm": ((("fill", "ink2"), ("stroke", "surface")), "stroke-width: 2"),
    "m-A": ((("fill", "a"), ("stroke", "surface")), "stroke-width: 2"),
    "m-B": ((("fill", "b"), ("stroke", "surface")), "stroke-width: 2"),
    "o-A": ((("fill", "surface"), ("stroke", "a")), "stroke-width: 1.5"),
    "o-B": ((("fill", "surface"), ("stroke", "b")), "stroke-width: 1.5"),
    "k-line": ((("stroke", "ink2"),), LINE),
    "k-dot": ((("fill", "ink2"), ("stroke", "surface")), "stroke-width: 2"),
    "k-open": ((("fill", "surface"), ("stroke", "ink2")), "stroke-width: 1.5"),
}
ROUTES = {"A": ("a", "Route A, R = 6130 Mpc"), "B": ("b", "Route B, R = 19700 Mpc")}


def style():
    rules = ["svg { " + "; ".join(f"--{k}: {v}" for k, v in LIGHT.items()) + "; font-family: system-ui, -apple-system, 'Segoe UI', sans-serif }",
             "@media (prefers-color-scheme: dark) { svg { " + "; ".join(f"--{k}: {v}" for k, v in DARK.items()) + " } }"]
    for cls, (colours, fixed) in CLASSES.items():
        decl = "; ".join(f"{p}: {LIGHT[t]}; {p}: var(--{t})" for p, t in colours)
        rules.append(f".{cls} {{ {decl}" + (f"; {fixed}" if fixed else "") + " }")
    return "<style>\n" + "\n".join(rules) + "\n</style>"


def header(w, h, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">'
            f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>')


class Panel:
    """A log-y plot region over l = 2..29."""

    def __init__(self, x0, y0, w, h, lo, hi):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.a, self.b = math.log10(lo), math.log10(hi)

    def x(self, l):
        return self.x0 + (l - LMIN) / (LMAX - LMIN) * self.w

    def y(self, v):
        return self.y0 + self.h - (math.log10(v) - self.a) / (self.b - self.a) * self.h


def decade_bounds(values):
    return 10.0 ** math.floor(math.log10(min(values))), 10.0 ** math.ceil(math.log10(max(values)))


def tick_text(v):
    return f"{v:,.0f}" if v >= 1 else f"{v:g}"


def axes(pn, lo, hi, unit=None, y_labels=True):
    out, e = [], round(math.log10(lo))
    while 10.0 ** e <= hi * 1.0001:
        yy = pn.y(10.0 ** e)
        out.append(f'<line class="grid" x1="{pn.x0:.1f}" x2="{pn.x0 + pn.w:.1f}" y1="{yy:.1f}" y2="{yy:.1f}"/>')
        if y_labels:
            out.append(f'<text class="tm" x="{pn.x0 - 8:.1f}" y="{yy + 4:.1f}" text-anchor="end">{tick_text(10.0 ** e)}</text>')
        e += 1
    base = pn.y0 + pn.h
    out.append(f'<line class="axis" x1="{pn.x0:.1f}" x2="{pn.x0 + pn.w:.1f}" y1="{base:.1f}" y2="{base:.1f}"/>')
    out += [f'<text class="tm" x="{pn.x(l):.1f}" y="{base + 18:.1f}" text-anchor="middle">{l}</text>' for l in XTICKS]
    out.append(f'<text class="tm" x="{pn.x0 + pn.w / 2:.1f}" y="{base + 36:.1f}" text-anchor="middle">multipole ℓ</text>')
    if unit:
        out.append(f'<text class="tm" x="{pn.x0 - 8:.1f}" y="{pn.y0 - 12:.1f}" text-anchor="end">{escape(unit)}</text>')
    return out


def dots(pn, values, line_cls, mark_cls, name, ls=None):
    ls = list(ls or range(LMIN, LMAX + 1))
    pts = [(pn.x(l), pn.y(v)) for l, v in zip(ls, values)]
    out = [f'<path class="{line_cls}" d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '"/>'] if line_cls else []
    for (x, y), l, v in zip(pts, ls, values):
        out.append(f'<circle class="{mark_cls}" cx="{x:.1f}" cy="{y:.1f}" r="4" data-l="{l}" data-v="{v!r}">'
                   f'<title>{escape(name)}, ℓ = {l}: {v:.4g}</title></circle>')
    return out


def triangles(pn, values, cls, name, ls):
    out = []
    for l, v in zip(ls, values):
        x, y = pn.x(l), pn.y(v)
        out.append(f'<path class="{cls}" d="M{x:.1f},{y - 5:.1f} L{x + 4.6:.1f},{y + 3:.1f} L{x - 4.6:.1f},{y + 3:.1f} Z" '
                   f'data-l="{l}" data-v="{v!r}"><title>{escape(name)}, ℓ = {l}: {v:.4g}</title></path>')
    return out


def legend(x, y, items):
    """items: (kind, classes, label); kind is 'line' (a line and a dot), 'open', 'triangle' or 'band'."""
    out = []
    for kind, cls, label in items:
        if kind == "line":
            out += [f'<line class="{cls[0]}" x1="{x}" x2="{x + 22}" y1="{y}" y2="{y}"/>', f'<circle class="{cls[1]}" cx="{x + 11}" cy="{y}" r="4"/>']
            x0 = x + 30
        elif kind == "open":
            out.append(f'<circle class="{cls[0]}" cx="{x + 5}" cy="{y}" r="4"/>')
            x0 = x + 16
        elif kind == "triangle":
            out.append(f'<path class="{cls[0]}" d="M{x + 5},{y - 5} L{x + 9.6},{y + 3} L{x + 0.4},{y + 3} Z"/>')
            x0 = x + 16
        else:
            out.append(f'<rect class="{cls[0]}" x="{x}" y="{y - 6}" width="18" height="12"/>')
            x0 = x + 26
        out.append(f'<text class="t2" x="{x0}" y="{y + 4}">{escape(label)}</text>')
        x = x0 + 6.4 * len(label) + 22
    return out


def spectra_svg(result):
    W, H = 760, 470
    lc, a, b = result["LCDM_D_l_uK2"]["frozen"], result["A"]["frozen"]["D_l_P1_uK2"], result["B"]["frozen"]["D_l_P1_uK2"]
    lo, hi = decade_bounds(lc + a + b)
    pn = Panel(72, 112, W - 72 - 124, H - 112 - 58, lo, hi)
    title = "P1's low-ℓ temperature spectrum at MIT's two radii"
    out = [header(W, H, title, "D_l for LambdaCDM and for P1 at routes A and B, l = 2 to 29, from the ratio table's frozen computation; theory only, no data."),
           style(), f'<rect class="bg" width="{W}" height="{H}"/>',
           f'<text class="t1" x="24" y="32">{escape(title)}</text>',
           f'<text class="t2" x="24" y="52">{escape("D_ℓ = ℓ(ℓ+1)C_ℓ/2π, unlensed, from CAMB 2.0.4 transfer functions; theory only, no data")}</text>']
    out += legend(24, 80, [("line", ("l-lcdm", "m-lcdm"), "ΛCDM"), ("line", ("l-A", "m-A"), "P1, route A"), ("line", ("l-B", "m-B"), "P1, route B")])
    out += axes(pn, lo, hi, "μK²")
    out += dots(pn, lc, "l-lcdm", "m-lcdm", "ΛCDM") + dots(pn, a, "l-A", "m-A", "P1, route A") + dots(pn, b, "l-B", "m-B", "P1, route B")
    ends = sorted([(pn.y(lc[-1]), "ΛCDM"), (pn.y(a[-1]), "route A"), (pn.y(b[-1]), "route B")])
    if all(e2[0] - e1[0] >= 14 for e1, e2 in zip(ends, ends[1:])):      # direct labels only where they do not collide
        out += [f'<text class="t2" x="{pn.x(LMAX) + 10:.1f}" y="{y + 4:.1f}">{escape(t)}</text>' for y, t in ends]
    return "\n".join(out + ["</svg>"]) + "\n"


def ratios_svg(result):
    W, H = 920, 500
    vals = [0.9, 1.1]
    for name in ROUTES:
        vals += result[name]["frozen"]["ratio"] + result[name]["estimates"]["sachs_wolfe"] + result[name]["estimates"]["with_isw_to_l10"]
    lo, hi = decade_bounds(vals)
    pw = (W - 72 - 40 - 64) / 2
    title = "P1's ratio to ΛCDM at MIT's two radii"
    out = [header(W, H, title, "R_l = C_l(P1)/C_l(LambdaCDM) at routes A and B from the frozen computation, beside the two estimates recorded "
                  "before v1's freeze; the band marks R_l within 10 percent of 1. Theory only, no data."),
           style(), f'<rect class="bg" width="{W}" height="{H}"/>',
           f'<text class="t1" x="24" y="32">{escape(title)}</text>',
           f'<text class="t2" x="24" y="52">{escape("R_ℓ = C_ℓ(P1)/C_ℓ(ΛCDM) from one transfer run, beside the two estimates made before v1’s freeze; theory only, no data")}</text>']
    out += legend(24, 80, [("line", ("k-line", "k-dot"), "full transfer"), ("open", ("k-open",), "Sachs-Wolfe estimate"),
                           ("triangle", ("k-open",), "with the integrated term, ℓ ≤ 10"), ("band", ("band",), "within 10% of ΛCDM")])
    for i, (name, (tok, label)) in enumerate(ROUTES.items()):
        pn = Panel(72 + i * (pw + 64), 136, pw, H - 136 - 58, lo, hi)
        out.append(f'<text class="t1" x="{pn.x0:.1f}" y="{pn.y0 - 24:.1f}">{escape(label)}</text>')
        out.append(f'<rect class="band" x="{pn.x0:.1f}" y="{pn.y(1.1):.1f}" width="{pn.w:.1f}" height="{pn.y(0.9) - pn.y(1.1):.1f}"/>')
        out += axes(pn, lo, hi, "R_ℓ" if i == 0 else None)
        out.append(f'<line class="axis" x1="{pn.x0:.1f}" x2="{pn.x0 + pn.w:.1f}" y1="{pn.y(1):.1f}" y2="{pn.y(1):.1f}"/>')
        est = result[name]["estimates"]
        out += dots(pn, est["sachs_wolfe"], None, f"o-{name}", f"Sachs-Wolfe estimate, route {name}")
        out += triangles(pn, est["with_isw_to_l10"], f"o-{name}", f"estimate with the integrated term, route {name}", range(LMIN, 11))
        out += dots(pn, result[name]["frozen"]["ratio"], f"l-{name}", f"m-{name}", f"full transfer, route {name}")
    return "\n".join(out + ["</svg>"]) + "\n"


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip().split("\n")[-1])
        return 2
    res = json.load(open(argv[1], encoding="utf-8"))
    if res.get("status") != "Complete":
        print("the result is not Complete, so no figures are drawn")
        return 1
    out = os.path.abspath(argv[2])
    if os.path.commonpath([out, HERE]) == HERE:
        print("the output folder lies inside the packet, which would break the freeze; no figures are drawn")
        return 2
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "ratio_table_spectra.svg"), "w", encoding="utf-8").write(spectra_svg(res))
    open(os.path.join(out, "ratio_table_ratios.svg"), "w", encoding="utf-8").write(ratios_svg(res))
    print("figures written: ratio_table_spectra.svg, ratio_table_ratios.svg")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
