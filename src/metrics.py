import numpy as np
import pandas as pd


POSITION_METRIC_CONFIG = {
    "Forward": {
        "name": "ATT",
        "cols": ["Goals", "Assists"],
    },
    "Midfielder": {
        "name": "MID",
        "cols": ["Assists", "Big chances created", "Through balls"],
    },
    "Defender": {
        "name": "DEF",
        "cols": [
            "Tackles",
            "Interceptions",
            "Blocked shots",
            "Clearances",
            "Headed Clearance",
        ],
    },
    "Goalkeeper": {
        "name": "GK",
        "cols": ["Saves"],
    },
}


def position_ceiling_floor_stats(
    df_season: pd.DataFrame,
    position_label: str,
    appearances_min: int = 10,
) -> dict:
    """
    Compute ceiling and floor metrics for a given position within one league-season.

    Parameters
    ----------
    df_season : pd.DataFrame
        Player-season data for a single league-season.
    position_label : str
        One of 'Forward', 'Midfielder', 'Defender', 'Goalkeeper'.
    appearances_min : int
        Minimum appearances to be considered a regular player.

    Returns
    -------
    dict
        Dictionary with ceiling/floor metrics and some diagnostics.
    """
    if position_label not in POSITION_METRIC_CONFIG:
        raise ValueError(f"Unknown position_label: {position_label}")

    cfg = POSITION_METRIC_CONFIG[position_label]
    metric_cols = cfg["cols"]

    df_pos = df_season[df_season["Position"] == position_label].copy()

    if df_pos.empty:
        return {
            "position_label": position_label,
            "position_group": cfg["name"],
            "n_players": 0,
            "n_players_reg": 0,
            "z_ceiling": np.nan,
            "z_floor": np.nan,
        }

    numeric_cols = list(metric_cols) + ["Appearances"]
    for col in numeric_cols:
        if col in df_pos.columns:
            df_pos[col] = pd.to_numeric(df_pos[col], errors="coerce").fillna(0)
        else:
            df_pos[col] = 0

    n_all = len(df_pos)

    df_pos = df_pos[df_pos["Appearances"] >= appearances_min].copy()

    if df_pos.empty:
        return {
            "position_label": position_label,
            "position_group": cfg["name"],
            "n_players": n_all,
            "n_players_reg": 0,
            "z_ceiling": np.nan,
            "z_floor": np.nan,
        }

    df_pos["impact_metric"] = df_pos[metric_cols].sum(axis=1)

    n_reg = len(df_pos)

    mean_val = df_pos["impact_metric"].mean()
    std_val = df_pos["impact_metric"].std(ddof=0)

    if std_val == 0:
        return {
            "position_label": position_label,
            "position_group": cfg["name"],
            "n_players": n_all,
            "n_players_reg": n_reg,
            "metric_cols": ",".join(metric_cols),
            "mean_metric": mean_val,
            "std_metric": std_val,
            "q1_metric": np.nan,
            "top_player_name": None,
            "top_player_metric": None,
            "z_ceiling": np.nan,
            "z_floor": np.nan,
        }

    top_idx = df_pos["impact_metric"].idxmax()
    top_row = df_pos.loc[top_idx]

    top_name = top_row["Name"]
    top_metric = top_row["impact_metric"]

    q1_val = df_pos["impact_metric"].quantile(0.25)

    z_ceiling = (top_metric - mean_val) / std_val
    z_floor = (q1_val - mean_val) / std_val

    return {
        "position_label": position_label,
        "position_group": cfg["name"],
        "n_players": n_all,
        "n_players_reg": n_reg,
        "metric_cols": ",".join(metric_cols),
        "mean_metric": mean_val,
        "std_metric": std_val,
        "q1_metric": q1_val,
        "top_player_name": top_name,
        "top_player_metric": top_metric,
        "z_ceiling": z_ceiling,
        "z_floor": z_floor,
    }
