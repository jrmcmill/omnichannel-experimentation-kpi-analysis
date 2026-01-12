import numpy as np
import pandas as pd


def generate_omnichannel_orders(
    n_orders=50000,
    seed=42
):
    """
    Generate a synthetic omnichannel fulfillment dataset.

    The dataset simulates:
    - Store vs DC fulfillment
    - Delivery speed tiers
    - Fulfillment costs
    - Delivery performance and guest satisfaction

    Parameters
    ----------
    n_orders : int
        Number of synthetic orders to generate.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        Synthetic omnichannel order-level dataset.
    """

    np.random.seed(seed)

    # High-level business dimensions
    regions = ["Northeast", "Midwest", "South", "West"]
    fulfillment_types = ["store", "dc"]
    carriers = ["Carrier_A", "Carrier_B"]

    # Mapping speed tier to promised delivery days
    speed_tiers = {
        "same_day": 1,
        "next_day": 2,
        "two_day": 3
    }

    data = []

    for i in range(n_orders):

        # Fulfillment origin choice
        # Stores are slightly more common than DCs
        fulfillment = np.random.choice(
            fulfillment_types,
            p=[0.55, 0.45]
        )

        # Delivery speed mix
        speed = np.random.choice(
            list(speed_tiers.keys()),
            p=[0.2, 0.5, 0.3]
        )

        promised_days = speed_tiers[speed]

        # Base delivery delay (noise around SLA)
        base_delay = np.random.normal(0.3, 0.5)

        # Store fulfillment is slightly faster on average
        if fulfillment == "store":
            base_delay -= 0.2

        # Actual delivery time (bounded to avoid negative values)
        actual_days = max(
            0.5,
            promised_days + base_delay
        )

        # SLA indicator
        on_time = actual_days <= promised_days

        # Cost structure:
        # - Store is more expensive per order
        # - Faster speeds cost more
        fulfillment_cost = (
            6 if fulfillment == "store" else 4
        ) + promised_days * 1.2

        # Guest satisfaction proxy:
        # Penalized for lateness
        guest_satisfaction = (
            5
            - (actual_days - promised_days)
            - (0.3 if not on_time else 0)
        )

        data.append({
            "order_id": f"O{i}",
            "region": np.random.choice(regions),
            "fulfillment_type": fulfillment,
            "carrier": np.random.choice(carriers),
            "speed_tier": speed,
            "promised_days": promised_days,
            "actual_days": round(actual_days, 2),
            "on_time": int(on_time),
            "fulfillment_cost": round(fulfillment_cost, 2),
            "guest_satisfaction": round(guest_satisfaction, 2)
        })

    return pd.DataFrame(data)
