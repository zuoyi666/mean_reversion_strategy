import numpy as np
import pandas as pd

def sharpe_ratio(returns: pd.Series, periods: int = 252) -> float:
    """
    Calculate the annualized Sharpe Ratio of a return series.
    Assumes risk-free rate = 0.

    :param returns: pd.Series of periodic returns
    :param periods: number of periods per year (252 for daily data)
    :return: Sharpe Ratio
    """
    # Annualized return
    mean_return = returns.mean() * periods
    # Annualized volatility
    vol = returns.std() * np.sqrt(periods)
    if vol == 0:
        return np.nan
    return mean_return / vol

def max_drawdown(equity_curve: pd.Series) -> float:
    """
    Calculate the maximum drawdown of an equity curve.

    :param equity_curve: pd.Series of cumulative returns (e.g., (1 + returns).cumprod())
    :return: Maximum drawdown as a negative float (e.g., -0.2 means -20%)
    """
    # Running maximum of the equity curve
    roll_max = equity_curve.cummax()
    # Drawdown series: current value relative to running max
    drawdown = equity_curve / roll_max - 1
    # Return the worst drawdown
    return drawdown.min()

__all__ = ['sharpe_ratio', 'max_drawdown']
