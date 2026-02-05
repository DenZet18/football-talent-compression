# Football Talent Compression in the Premier League
Has elite football experienced talent distribution compressed over time, with a rising floor and a narrowing ceiling?

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Status](https://img.shields.io/badge/status-v1.0%20complete-brightgreen)
![Scope](https://img.shields.io/badge/scope-EPL%202015--2024-orange)
## Abstract
Over the past decade, elite football has undergone significant tactical, physical, and organizational change. While contemporary players benefit from improved coaching, conditioning, and tactical structure, there is growing debate over whether modern football produces fewer truly dominant individuals than previous eras.

This project investigates whether the English Premier League has experienced talent distribution compression, a phenomenon characterized by a rising baseline standard of performance (the “floor”) alongside reduced or more volatile separation between the league’s most dominant players and the positional average (the “ceiling”).

Using player-season data from the Premier League spanning the 2015–16 to 2023–24 seasons, the analysis measures talent distribution at the individual level across four position groups (forwards, midfielders, defenders, and goalkeepers). Position-specific performance metrics are standardized within each season to estimate ceiling dominance (top individual z-scores) and floor strength (25th-percentile performance among regular players).

Rather than assessing absolute quality, the study focuses on distributional change: how the spread of individual performance within positions has evolved over time. The project is implemented as a reproducible and modular analysis pipeline, designed to generalize to other leagues and competitions in future work.

By reframing player quality as a distribution rather than a ranking, this project provides a framework for understanding why modern football may appear simultaneously more competitive and less individually dominant, even as overall performance standards continue to rise.

## Project Scope

### Current Implementation
- League: English Premier League (EPL)
- Seasons: 2015–16 to 2023–24
- Unit of analysis: Individual player-season
- Positions analyzed: Forwards, Midfielders, Defenders, Goalkeepers
- Focus: Talent distribution dynamics (floor vs ceiling) within positions
- Output:
  - Reproducible analysis pipeline
  - Processed metrics dataset
  - Position-specific visualizations
  - Long-form analytical write-up

### Planned Extensions
- Replication across other top European leagues (La Liga, Serie A, Bundesliga, Ligue 1)
- Expansion to leagues with structural parity mechanisms (e.g., MLS)
- Alternative dominance metrics (e.g., WAR-style composite impact models)


## Pipeline Overview
1. Ingest player-season data by league and season
2. Assign players to standardized position groups
3. Compute role-specific impact metrics
4. Estimate ceiling dominance and floor strength using within-season standardization
5. Aggregate results across seasons
6. Visualize talent distribution trends over time

## Key Findings

- **Forwards (ATT):**  
  The Premier League exhibits clear signs of attacking talent compression. While elite goal-scoring seasons still occur, the attacking ceiling is volatile rather than structurally dominant. In contrast, the attacking floor remains consistently close to the positional mean, indicating that weaker-but-regular forwards now provide more reliable output than in earlier periods.

- **Midfielders (MID):**  
  Midfield performance shows pronounced elite spikes without corresponding floor deterioration. While certain seasons feature extreme creative outliers, the lower quartile of midfielders remains remarkably stable, reflecting rising baseline technical and tactical competence driven by modern positional demands.

- **Defenders (DEF):**  
  Defensive talent displays one of the strongest compression patterns. The defensive ceiling remains relatively flat, while the floor has tightened across seasons, suggesting a decline in exploitable weak defenders. This aligns with the increased importance of pressing resistance, build-up ability, and positional discipline in modern defensive roles.

- **Goalkeepers (GK):**  
  Goalkeepers show the most pronounced floor stabilization of all positions. Although elite shot-stopping seasons still emerge, the positional floor remains consistently close to the league average, indicating a narrowing gap between starting-level goalkeepers. Advances in goalkeeper coaching and recruitment likely contribute to this trend.

## Conclusion

Across all positions, the Premier League shows strong evidence of talent distribution compression over the 2015–16 to 2023–24 period. While exceptional individual seasons continue to occur, elite dominance has become more volatile rather than structurally persistent. At the same time, the baseline level of performance among regular players has risen or stabilized across every position group.

These findings suggest that modern football has not necessarily produced worse players at the top, but rather a more competitive and standardized environment in which extreme separation is harder to sustain. Tactical sophistication, improved coaching infrastructure, and stricter performance thresholds appear to have raised the league-wide floor, reducing the presence of exploitable weaknesses.

By framing player quality as a distribution rather than a ranking, this project provides a lens for understanding why contemporary football may feel both more competitive and less individually expressive. The methodology is designed to generalize to other leagues and competitive structures, offering a foundation for future comparative and cross-league analysis.

### Quantitative Summary (EPL 2015–2024)

Across all positions, the average performance of lower-quartile regular players remained within approximately one standard deviation of the positional mean (mean floor ranging from −0.65 to −0.81). This indicates a consistently high baseline level of competence across the league.

Ceiling dominance varied substantially by position. Midfielders exhibited the highest average ceiling (mean z = 5.41), while defenders and goalkeepers showed much smaller and more stable ceilings. Trend analysis suggests that midfield talent experienced the clearest compression over time, driven by a decline in extreme elite dominance alongside a stable floor. In contrast, attacking ceilings remained volatile but did not show sustained growth or collapse, while defensive and goalkeeping roles displayed the narrowest and most stable performance distributions.

Together, these results support the interpretation that modern Premier League talent compression is primarily driven by rising and stabilized floors, with position-dependent changes in elite dominance rather than a universal decline in top-end quality.
