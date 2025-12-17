import numpy as np
from statsmodels.tsa.stattools import adfuller


def compute_spread(log_x, log_y, beta):
    """
    Construct the cointegration spread.
    """
    return log_x - beta * log_y


def spread_half_life(spread):
    """
    Estimate mean-reversion half-life.
    """
    spread_lag = spread.shift(1)
    delta = spread - spread_lag
    spread_lag = spread_lag.dropna()
    delta = delta.dropna()

    beta = np.polyfit(spread_lag, delta, 1)[0]
    half_life = -np.log(2) / beta if beta < 0 else np.inf
    return half_life


def adf_test(spread):
    """
    Augmented Dickey-Fuller test for stationarity.
    """
    result = adfuller(spread)
    return result[1]  # p-value
