import pandas as pd


def zscore(series, window=60):
    """
    Compute rolling z-score.
    """
    mean = series.rolling(window).mean()
    std = series.rolling(window).std()
    return (series - mean) / std
