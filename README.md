# pairs_analysis
Overview

This project is a research-focused statistical arbitrage analysis framework designed to identify, evaluate, and monitor long-run relationships between financial assets. Rather than implementing a trading strategy, the tool provides diagnostics and stability analysis commonly used in quantitative research to assess whether asset pairs exhibit meaningful mean-reverting behavior.

The framework answers four core questions:

Which assets move together?

Is the relationship statistically meaningful or coincidental?

How stable is the relationship over time?

How unusual is the current deviation from equilibrium?

Key Concepts (Intuition)

Correlation: Measures whether two prices move together in the short run.

Cointegration: Tests whether two prices share a stable long-term relationship.

Hedge Ratio: Quantifies how strongly one asset moves relative to another.

Spread: A constructed series measuring the distance between two related prices.

Mean Reversion: Whether deviations from equilibrium tend to decay over time.

Stability Analysis: Evaluates whether the relationship deteriorates or remains consistent.

This framework mirrors how quantitative researchers evaluate statistical arbitrage opportunities before any trading rules are considered.

Project Structure
pairs_analysis/
│
├── data/
│   └── loader.py          # Price data acquisition and preprocessing
│
├── analysis/
│   ├── correlation.py    # Pair screening using correlation
│   ├── cointegration.py  # Engle–Granger tests and hedge ratio estimation
│   ├── spread.py         # Spread construction and mean reversion diagnostics
│   └── stability.py      # Rolling hedge ratio stability analysis
│
├── utils/
│   └── stats.py          # Rolling z-score computation
│
├── visualization/
│   └── plots.py          # Diagnostic plots
│
└── main.py               # End-to-end research demonstration

Methodology
1. Data Collection

Historical adjusted price data is downloaded from Yahoo Finance using yfinance.

Prices are adjusted for dividends and splits.

Log-prices are used for statistical consistency.

2. Pair Screening

All asset pairs are evaluated using Pearson correlation.

Only highly correlated pairs are retained for further analysis.

3. Cointegration Testing

The Engle–Granger two-step method is applied.

Low p-values indicate a statistically significant long-run relationship.

4. Hedge Ratio Estimation

Ordinary Least Squares (OLS) regression estimates the relative movement between assets.

The hedge ratio is used to construct the spread.

5. Spread Diagnostics

Spread stationarity is tested using the Augmented Dickey-Fuller test.

Mean reversion speed is quantified via half-life estimation.

6. Stability & Deviation Analysis

Rolling hedge ratios monitor parameter stability.

Rolling z-scores measure the extremeness of current deviations.

Example Output

Running main.py produces:

Identification of the strongest correlated asset pair

Cointegration p-values and hedge ratio estimates

Mean-reversion half-life estimates

Diagnostic plots showing:

Spread behavior

Deviation z-scores over time
