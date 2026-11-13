# The figures of Paper 2

The page is [`standing-wave-branches.md`](../../standing-wave-branches.md). Its four figures are drawn here, each by a script that reads committed sources at a pinned commit and checks them before it draws. `SHA256SUMS` lists every other file in this folder; `shasum -a 256 -c SHA256SUMS` checks them.

## Figures 1 to 3: the slots, the shape of the spectrum, and the orbits with their types

`fig_theory.py` draws them in TikZ, in the style of the repository's other figures, from the page itself at MIT commit `b0e50ae3` and the Surviving Ray's certificate file, `sr_v2_certificates.json`, at `1d11a877`:
- Figure 1, in section 2.1: the slots on the affine E8 graph of 2I, rigid and soft, from Table 1 and section 2.1;
- Figure 2, in section 4.1: the shape of the small-amplitude spectrum, a schematic of Theorem R(a), with the three kinds of slow flow that Table 4 lists;
- Figure 3, in section 4.1: the thirteen critical orbits in R4 and R5 as Majorana constellations, in rows by their small-amplitude type, from Tables 2 and 4, the three orbits outside the census's class at the centres of their certified boxes.

Before it draws, it checks that the graph is the McKay graph of 2I with Table 1's dimensions and that its distances from R0 are Table 1's lowest levels; that each closed-form representative's 924 r6 is Table 2's value, exactly; that each certified orbit's agrees with the digits Table 2 prints; and that Tables 2 and 4 give each orbit the same signature. It stops on any difference. `theory.json` holds what it read, with each orbit's Majorana points, and `fig_theory_log.txt` is the run's log. Each figure is in `figures/` as its TikZ source, a PDF and a PNG at 300 dpi; the PDFs carry no dates, so a rerun gives the same bytes. Rerun from this folder, in a clone of MIT that has both commits in its history, with pdflatex and pdftocairo installed:

    python3 fig_theory.py

## Figure 4: OpenWave's adjudicated census at its close on 2026-11-10

`fig_census.py` draws the figure from the committed records alone, read at MIT commit `c7e3f46e`:
- every registered point of the nine branches, with its classification and the instrument that supplies it, from
  M8.17's record, § 3;
- the prism's located interval in R4 and its guards, from the same record, § 4;
- the location of O3's change of type in R5 and its guards, from M8.18's record;
- the hexagon's two mesh-level n(L) steps in R5 and its guards, from M8.15.2's record, its T3/R5 section.

Before it draws, it checks each row against the census's close as the draft's Table 6 states it (window, counts, open
points, endings), and it stops on any difference. `census.json` holds what it read, with each value's record.
`figures/figure1-census.pdf` and `.png` are the figure, which the page links by absolute URL; its file name is from when it was the page's only figure. `fig_census_log.txt` is the run's log.

Rerun from this folder, in a clone of MIT that has `c7e3f46e` in its history; the script reads the records
from that commit, whatever is checked out:

    python3 fig_census.py

