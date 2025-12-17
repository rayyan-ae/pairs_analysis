import statsmodels.api as sm
from statsmodels.tsa.stattools import coint


def engle_granger_test(series_x, series_y):
    """
    Run Engle-Granger cointegration test.
    """
    score, pvalue, _ = coint(series_x, series_y)
    return pvalue


def estimate_hedge_ratio(series_x, series_y):
    """
    Estimate hedge ratio using OLS.
    """
    X = sm.add_constant(series_y)
    model = sm.OLS(series_x, X).fit()
    beta = model.params[1]
    return beta
