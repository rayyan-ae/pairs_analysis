import pandas as pd
import itertools


def correlation_matrix(prices):
    """
    Compute Pearson correlation matrix.
    """
    return prices.corr()


def rank_pairs_by_correlation(prices, min_corr=0.7):
    """
    Rank asset pairs by absolute correlation.
    """
    corr = prices.corr()
    pairs = []

    for i, j in itertools.combinations(corr.columns, 2):
        value = corr.loc[i, j]
        if abs(value) >= min_corr:
            pairs.append((i, j, value))

    return sorted(pairs, key=lambda x: abs(x[2]), reverse=True)
