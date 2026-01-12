import pandas as pd
import numpy as np


def assign_experiment_groups(df, seed=42):
    """
    Randomly assign orders to control and treatment groups
    and simulate treatment effects.

    Treatment assumptions:
    - Faster delivery times
    - Slightly lower fulfillment cost
    - Improved on-time rate

    Parameters
    ----------
    df : pandas.DataFrame
        Omnichannel orders dataset.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        Dataset with experiment_group and updated outcomes.
    """

    np.random.seed(seed)

    # Work on a copy to avoid mutating upstream data
    df = df.copy()

    # Random assignment (50/50 split)
    df["experiment_group"] = np.random.choice(
        ["control", "treatment"],
        size=len(df)
    )

    # Identify treatment rows
    mask = df["experiment_group"] == "treatment"

    # Simulated treatment effects:
    # - 5% faster delivery
    # - 3% lower cost
    df.loc[mask, "actual_days"] *= 0.95
    df.loc[mask, "fulfillment_cost"] *= 0.97

    # Recompute SLA outcome after treatment
    df["on_time"] = (
        df["actual_days"] <= df["promised_days"]
    ).astype(int)

    return df
