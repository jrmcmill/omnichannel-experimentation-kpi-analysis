def compute_exec_kpis(df):
    """
    Compute executive-level KPIs for an experiment group.

    Intended for:
    - GroupBy apply (control vs treatment)
    - Dashboard rollups
    - Decision framing

    Parameters
    ----------
    df : pandas.DataFrame
        Subset of experiment data (one experiment group).

    Returns
    -------
    dict
        Aggregated KPI metrics.
    """

    return {
        # SLA performance
        "on_time_rate": df["on_time"].mean(),

        # Cost efficiency
        "avg_cost": df["fulfillment_cost"].mean(),

        # Guest experience proxy
        "avg_satisfaction": df["guest_satisfaction"].mean(),

        # Volume context
        "orders": len(df)
    }
