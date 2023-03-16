#Edit the file name to binance_config.py then edit your api_key and secret_key from Binance API

import ccxt

api_key = 'INSERT API KEY'
secret_key = 'INSERT SECRET'

def create_binance_future_client():
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future'
        }
    })
    return exchange

