# Figure 1 of Paper 2: OpenWave's adjudicated census at its close on 2026-11-10

`fig_census.py` draws the figure from the committed records alone, read at MIT commit `c7e3f46e`:
- every registered point of the nine branches, with its classification and the instrument that supplies it, from
  M8.17's record, § 3;
- the prism's located interval in R4 and its guards, from the same record, § 4;
- the location of O3's change of type in R5 and its guards, from M8.18's record;
- the hexagon's two mesh-level n(L) steps in R5 and its guards, from M8.15.2's record, its T3/R5 section.

Before it draws, it checks each row against the census's close as the draft's Table 6 states it (window, counts, open
points, endings), and it stops on any difference. `census.json` holds what it read, with each value's record.
`figures/figure1-census.pdf` and `.png` are the figure, which the page links by absolute URL; `fig_census_log.txt` is the run's log.

Rerun from this folder, in a clone of MIT that has `c7e3f46e` in its history; the script reads the records
from that commit, whatever is checked out:

    python3 fig_census.py

The page is [`standing-wave-branches.md`](../../standing-wave-branches.md), Figure 1 in its section 5.
