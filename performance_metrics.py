import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_returns(portfolio):
    portfolio['returns'] = portfolio['balance'].pct_change()
    return portfolio

def calculate_cumulative_returns(portfolio):
    portfolio['cumulative_returns'] = (portfolio['returns'] + 1).cumprod()
    return portfolio

def calculate_sharpe_ratio(portfolio, annualized_factor=252):
    sharpe_ratio = np.sqrt(annualized_factor) * (portfolio['returns'].mean() / portfolio['returns'].std())
    return sharpe_ratio

def calculate_max_drawdown(portfolio):
    portfolio['cumulative_max'] = portfolio['cumulative_returns'].cummax()
    portfolio['drawdown'] = (portfolio['cumulative_returns'] - portfolio['cumulative_max']) / portfolio['cumulative_max']
    max_drawdown = portfolio['drawdown'].min()
    return max_drawdown

def plot_cumulative_returns(portfolio):
    plt.plot(portfolio['cumulative_returns'])
    plt.xlabel('Time')
    plt.ylabel('Cumulative Returns')
    plt.title('Cumulative Returns Over Time')
    plt.show()
