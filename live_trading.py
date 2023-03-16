import ccxt
import pandas as pd
import numpy as np
import time
from tensorflow.keras.models import load_model

def live_trade_bot(exchange, symbol, leverage, timeframe_to_trade, trained_model_path):
    # Load the trained model
    model = load_model(trained_model_path)

    # Set the leverage for the trading symbol
    exchange.fapiPrivate_post_leverage({'symbol': symbol.replace('/', ''), 'leverage': leverage})

    while True:
        # Get latest data
        ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe_to_trade, since=None, limit=500)
        data = pd.DataFrame(ohlcv_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['date'] = pd.to_datetime(data['timestamp'], unit='ms')
        data = data[['date', 'open', 'high', 'low', 'close', 'volume']]

        # Preprocess data
        state = data.iloc[-10:].copy()
        state['moving_average'] = state['close'].rolling(window=14).mean()
        state['rsi'] = calculate_rsi(state['close'], period=14)
        state['volume_pct_change'] = state['volume'].pct_change()

        # Predict the next action
        action = np.argmax(model.predict(state.values[np.newaxis]))

        # Execute the action
        execute_trade_action(exchange, symbol, action)

        # Wait for the next time frame
        time.sleep(300)  # 300 seconds for 5m timeframe

def execute_trade_action(exchange, symbol, action):
    # Check the current position
    positions = exchange.fapiPrivate_get_positionrisk()
    position = next((position for position in positions if position['symbol'] == symbol.replace('/', '')), None)

    if position is not None:
        entry_price = float(position['entryPrice'])
        position_size = float(position['positionAmt'])

    # Buy (Open Long Position)
    if action == 0:
        if position is None or position_size == 0:
            exchange.create_market_buy_order(symbol, 1)

    # Hold
    elif action == 1:
        pass

    # Sell Close Long Position
    elif action == 2:
        if position is not None and position_size > 0:
            exchange.create_market_sell_order(symbol, position_size)

    # Open Short Position
    elif action == 6:
        if position is None or position_size == 0:
            exchange.create_market_sell_order(symbol, 1)

    # Close Short Position
    elif action == 7:
        if position is not None and position_size < 0:
            exchange.create_market_buy_order(symbol, abs(position_size))

# RSI calculation
def calculate_rsi(series, period):
    delta = series.diff().dropna()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    avg_gain = gains.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = losses.ewm(com=period - 1, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

# Add this line at the end of the live_trading.py file
if __name__ == "__main__":
    from binance_config import exchange

    # Replace the following variables with your desired values
    symbol = "BTC/USDT"
    leverage = leverage
    timeframe_to_trade = timeframe_to_trade
    trained_model_path = "trained_model.h5"

    live_trade_bot(exchange, symbol, leverage, timeframe_to_trade, trained_model_path)

