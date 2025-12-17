import yfinance as yf
import pandas as pd
import numpy as np


def load_prices(tickers, start, end):
    """
    Download adjusted close prices and align dates.
    Explicitly use auto_adjust=True and Close prices.
    """
    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True,   # prices are already adjusted
        progress=False
    )["Close"]

    data = data.dropna()
    return data


def log_prices(prices):
    """
    Convert prices to log-prices.
    """
    return np.log(prices)
