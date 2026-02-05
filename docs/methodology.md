## Research Question

This project examines whether the English Premier League has experienced talent distribution compression over time — a phenomenon characterized by rising baseline performance among regular players (the “floor”) alongside reduced or more volatile separation between the most dominant individuals and their positional peers (the “ceiling”).

The analysis focuses on individual player performance within position groups rather than aggregate team outcomes, emphasizing distributional change over absolute quality.

---

## Metric Definitions

### Individual Ceiling

The individual ceiling is defined as the degree of relative dominance achieved by the top-performing player within a given position group and league-season.

For each season and position group, role-specific performance metrics are standardized using z-scores. The ceiling is measured as the maximum standardized score within the positional distribution, capturing how far the most dominant individual separates from their peers in that season.

---

### Individual Floor

The individual floor represents the baseline competence level of weaker but regularly utilized players.

For each position group and season, players are first filtered to include only regular contributors, defined as those meeting a minimum appearances threshold. The floor is then measured as the 25th percentile of the standardized positional performance distribution, reflecting the lower bound of sustained, rotation-level quality rather than fringe participation.

---

### Compression

Talent distribution compression is evaluated through joint analysis of ceiling and floor dynamics over time.

Compression is inferred when:
- floor values rise or stabilize closer to the positional mean, and/or
- ceiling dominance becomes less structurally persistent and more volatile across seasons.

Rather than testing for statistical significance, the analysis emphasizes descriptive trends supported by time-series visualization and summary statistics.

---

## Planned Extensions

Future work will extend this framework in several directions, including:
- replication across other top European leagues and Major League Soccer,
- alternative floor definitions using different percentile thresholds,
- and position-weighted, WAR-style composite impact metrics for seasons where richer event-level data is available.

---

## Notes

The current implementation focuses on the English Premier League (2015–16 to 2023–24) as a case study. The methodology is designed to generalize to other leagues with comparable player-season data and positional role definitions.
