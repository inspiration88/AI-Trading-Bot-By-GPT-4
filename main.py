import brain as te
import train
import backtesting
import live_trading
from fetch_data import fetch_binance_data
from binance_config import api_key, secret_key

# Set your main configs you want to use for training, backtesting, and live trading
symbol = 'BTC/USDT'
leverage = 20
timeframe_to_trade = '5m'
train_data_since = '2017-08-17T00:00:00Z'
train_data_until = '2020-01-01T00:00:00Z'
backtest_data_since = '2020-01-01T00:00:00Z'
backtest_data_until = '2023-01-01T00:00:00Z'
window_size = 20
initial_balance = 100

# Step 0: Create the Datasets to train and backtest with
csv_train = fetch_binance_data(api_key, secret_key, symbol, timeframe_to_trade, train_data_since, train_data_until, 'btcusdt_train.csv')
csv_backtesting = fetch_binance_data(api_key, secret_key, symbol, timeframe_to_trade, backtest_data_since, backtest_data_until, 'btcusdt_backtest.csv')

# Step 1: Train the trading bot
trained_model = train.train_bot(symbol, leverage, timeframe_to_trade, csv_train, window_size, initial_balance)

# Step 2: Backtest the trading bot
profitable = backtesting.backtest_bot(csv_backtesting, trained_model)

# Step 4: If the backtesting shows profitability, run the live trading bot
if profitable:
    live_trading.live_trade_bot(symbol, leverage, timeframe_to_trade, api_key, secret_key, trained_model)
else:
    print("The bot is not profitable based on backtesting. Retrain the bot before live trading.")
