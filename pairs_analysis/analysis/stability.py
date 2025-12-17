import pandas as pd
import statsmodels.api as sm


def rolling_hedge_ratio(log_x, log_y, window=60):
    """
    Compute rolling hedge ratio estimates.
    """
    betas = []

    for i in range(window, len(log_x)):
        X = sm.add_constant(log_y.iloc[i-window:i])
        y = log_x.iloc[i-window:i]
        beta = sm.OLS(y, X).fit().params[1]
        betas.append(beta)

    return pd.Series(betas, index=log_x.index[window:])
