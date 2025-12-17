import numpy as np 
from data.loader import load_prices
from analysis.correlation import rank_pairs_by_correlation
from analysis.cointegration import engle_granger_test, estimate_hedge_ratio
from analysis.spread import compute_spread, spread_half_life, adf_test
from analysis.stability import rolling_hedge_ratio
from utils.stats import zscore
from visualization.plots import plot_spread

# Asset universe
tickers = ["MSFT", "AAPL", "GOOGL", "META", "AMZN"]

# Load data
prices = load_prices(tickers, start="2018-01-01", end="2024-01-01")
log_prices = np.log(prices)

# Pair screening
pairs = rank_pairs_by_correlation(log_prices, min_corr=0.8)
asset_x, asset_y, corr = pairs[0]

print(f"Top pair: {asset_x}, {asset_y} | Corr: {corr:.2f}")

# Cointegration analysis
pvalue = engle_granger_test(log_prices[asset_x], log_prices[asset_y])
beta = estimate_hedge_ratio(log_prices[asset_x], log_prices[asset_y])

print(f"Cointegration p-value: {pvalue:.4f}")
print(f"Hedge ratio (beta): {beta:.3f}")

# Spread diagnostics
spread = compute_spread(log_prices[asset_x], log_prices[asset_y], beta)
half_life = spread_half_life(spread)
adf_pvalue = adf_test(spread)

print(f"Half-life: {half_life:.2f} days")
print(f"ADF p-value: {adf_pvalue:.4f}")

# Z-score and plots
z = zscore(spread)
plot_spread(spread, z)
