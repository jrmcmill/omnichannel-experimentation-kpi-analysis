import pandas as pd
import numpy as np
from scipy import stats


def ab_test(df, metric):
    """
    Perform a two-sample A/B test comparing control vs treatment
    for a given metric.

    Parameters
    ----------
    df : pandas.DataFrame
        Experiment dataset containing an 'experiment_group' column
        with values ['control', 'treatment'].
    metric : str
        Name of the metric column to test (e.g., 'on_time', 'fulfillment_cost').

    Returns
    -------
    dict
        Dictionary containing group means, absolute lift, and p-value.
    """

    # Split data into control and treatment groups
    control = df[df["experiment_group"] == "control"][metric]
    treatment = df[df["experiment_group"] == "treatment"][metric]

    # Compute absolute lift (treatment - control)
    lift = treatment.mean() - control.mean()

    # Welch’s t-test (does not assume equal variance)
    # This is standard for real-world experiments
    t_stat, p_value = stats.ttest_ind(
        treatment,
        control,
        equal_var=False
    )

    return {
        "control_mean": control.mean(),
        "treatment_mean": treatment.mean(),
        "lift": lift,
        "p_value": p_value
    }
