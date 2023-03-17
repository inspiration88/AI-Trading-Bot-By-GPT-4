import numpy as np
import pandas as pd

def moving_average(data, window=14):
    return data.rolling(window=window).mean()

def calculate_rsi(data, period=14):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def volume_pct_change(data):
    return data.pct_change()

def support_resistance_levels(data, window=14, tolerance=0.02):
    pivot_highs = pd.Series(np.where(data['high'].rolling(window=window).max().shift(-window + 1) == data['high'], data['high'], np.nan), index=data.index)
    pivot_lows = pd.Series(np.where(data['low'].rolling(window=window).min().shift(-window + 1) == data['low'], data['low'], np.nan), index=data.index)

    pivot_highs = pivot_highs[pivot_highs.notnull()].copy()
    pivot_lows = pivot_lows[pivot_lows.notnull()].copy()

    for i, val in enumerate(pivot_highs):
        if i == 0:
            continue
        if val - pivot_highs[i - 1] <= pivot_highs[i - 1] * tolerance:
            pivot_highs.iloc[i] = np.nan

    for i, val in enumerate(pivot_lows):
        if i == 0:
            continue
        if pivot_lows[i - 1] - val <= val * tolerance:
            pivot_lows.iloc[i] = np.nan

    pivot_highs = pivot_highs[pivot_highs.notnull()]
    pivot_lows = pivot_lows[pivot_lows.notnull()]

    return pivot_highs, pivot_lows
