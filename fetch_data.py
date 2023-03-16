import ccxt
import pandas as pd
import time

def fetch_binance_data(api_key, secret_key, symbol, timeframe, since, until, filename):
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': secret_key,
        'rateLimit': 1200,
        'enableRateLimit': True,
    })

    def get_ohlcv_data(symbol, timeframe, since, until):
        all_candles = []
        until = exchange.parse8601(until)
        while since:
            candles = exchange.fetch_ohlcv(symbol, timeframe, since)
            if not candles:
                break
            since = candles[-1][0] + 1
            if since >= until:
                break
            all_candles += candles
            time.sleep(exchange.rateLimit / 1000)
        return all_candles

    ohlcv_data = get_ohlcv_data(symbol, timeframe, since, until)

    df = pd.DataFrame(ohlcv_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]

    df.to_csv(filename, index=False)
