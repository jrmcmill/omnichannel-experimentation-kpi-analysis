# 🧪 Omnichannel Fulfillment Experimentation & KPI Optimization

## Overview
This project simulates and analyzes controlled omnichannel fulfillment experiments to evaluate tradeoffs between delivery speed, operational cost, and guest experience.

Using a fully synthetic but realistic dataset, the project designs A/B experiments across fulfillment strategies (ship-from-store vs ship-from-DC, routing logic, carrier selection), measures causal impact using statistical methods, and frames results for executive decision-making.

The end-to-end workflow mirrors how experimentation and decision science teams at large retailers evaluate operational changes before national rollout.

---

## Key Business Questions
- Which fulfillment strategy improves on-time delivery without increasing cost?
- What is the causal impact of routing or carrier changes?
- How do experiment results translate into national-scale cost and SLA outcomes?
- How should leadership decide whether to roll out a test variant?

---

## Data
All data is **synthetically generated** (100% free, no external dependencies):

- Omnichannel orders with:
  - Fulfillment origin (store vs DC)
  - Delivery speed tiers
  - Cost structures
  - Delivery outcomes
- Experiment assignment (control vs treatment)
- Regional and time-based attributes

Synthetic data enables full reproducibility while preserving realistic operational patterns.

---

## Methods

### Experiment Design
- Randomized A/B testing framework
- Experiment groups simulate:
  - Different fulfillment origins
  - Routing rule changes
  - Carrier assignment strategies
- Balanced assignment across regions and time

### Statistical Analysis
- Difference-in-means estimation
- Confidence intervals for treatment effects
- Regression adjustment for variance reduction
- KPI-level causal attribution

### KPIs
- On-time delivery rate
- Average delivery cost
- Late delivery rate
- Guest-impact proxy metrics
- Incremental cost vs SLA tradeoffs

### Decision Framing
- Executive-style rollup metrics
- “If rolled out nationally…” scenario analysis
- Cost savings vs SLA impact summaries

---

## Results
- Quantified lift in on-time delivery from experimental treatments
- Identified fulfillment strategies that reduced cost without SLA degradation
- Produced decision-ready outputs suitable for leadership review
- Demonstrated end-to-end experimentation lifecycle from design to decision

---

## Tech Stack
- Python
- pandas, NumPy
- scikit-learn
- statsmodels
- Matplotlib, Seaborn
- SQL (logical modeling)
- Tableau-ready output datasets

All tools and libraries used are free and open-source.

---

## Repository Structure
```text
omnichannel-experimentation/
│
├── data/
│   ├── raw/
│   │   └── synthetic_orders.csv
│   ├── processed/
│   │   ├── experiment_dataset.csv
│   │   ├── kpi_summary.csv
│   │   └── exec_rollup.csv
│
├── notebooks/
│   ├── 01_data_generation.ipynb
│   ├── 02_experiment_design.ipynb
│   ├── 03_experiment_analysis.ipynb
│   └── 04_exec_decision_view.ipynb
│
├── src/
│   ├── data_generation.py
│   ├── experimentation.py
│   ├── analysis.py
│   └── kpis.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

-----

## How to Run

Install dependencies:
```bash
pip install -r requirements.txt
```

Launch Jupyter:
```bash
jupyter lab
```

Run notebooks in order:
```bash
01_data_generation.ipynb
02_experiment_design.ipynb
03_experiment_analysis.ipynb
04_exec_decision_view.ipynb
```

-----

## Business Relevance

This project reflects how modern retail experimentation and decision science teams operate:
- Controlled A/B experimentation for operational changes
- Causal measurement of fulfillment strategy impact
- KPI-driven decision-making across speed, cost, and guest experience
- Executive-ready outputs to support national rollout decisions

The workflow mirrors real-world omnichannel analytics used by large retailers, marketplaces, and logistics organizations, where experiments inform high-stakes operational decisions before scaling.
