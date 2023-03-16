# AI Cryptocurrency Trading Bot Fully Built with ChatGPT-4

First and foremost, I'd like to mention that my coding experience is limited to minor tweaks in bots, and I lack the skills to create a bot, write functions in Python, or achieve this level of coding quality, proficiency, and expertise. This ongoing project aims to explore ChatGPT-4's ability to develop a bot, apply AI, and ultimately achieve profitable automated trading.

This AI trading bot leverages deep reinforcement learning to trade cryptocurrencies. It is trained on historical data and can be used for both backtesting and live trading. The bot employs technical indicators and additional actions, such as stop loss, take profit, and position scaling, to make informed trading decisions.

Any donations would be appreciated for keep working on this project and share public to make achieve its goal. Donations wallet: 0x570a977847a1b98a2e23cc4CB05E71046d1234DE

Date of start: 03/15/2023

## Components

1. `main.py` - The main script that serves as the control command for the bot, where all variables are set.

2. `binance_config.py` - Contains the configuration for connecting to the Binance API, including the API key and secret. Upload the file as binance_configSAMPLE.py, add your Binance keys, and rename the file to binance_config.py.

3. `train.py` - Responsible for training the AI trading bot using historical data. It preprocesses data, creates and compiles the model, and trains the model using the trading environment.

4. `trading_environment.py` - Contains the custom trading environment for the AI trading bot, based on OpenAI Gym. The environment defines the observation space, action space, and reward function. The reward function encourages the bot to make more trades when the account balance is closer to the initial balance and to focus on higher-quality trades as the balance increases.

5. `backtesting.py` - Used to backtest the trained model on historical data. It simulates trading with the trained model and provides success rates to evaluate the model's performance before deploying it for live trading.

6. `live_trading.py` - Responsible for executing live trades with the trained model using the Binance API. The bot retrieves the latest market data, preprocesses it, and uses the model to predict the next action. The chosen action is then executed on the Binance platform.

7. `performance_metrics.py` - Calculates various performance metrics, such as returns, Sharpe ratio, and drawdown, for the trading bot. These metrics can be used to evaluate the performance of the bot and make adjustments as needed.


## Planed shortterm updates

1. Based that is built on ChatGPT-4 i would leave open the possibility for people to edit the trading enviroment to train the bot into different strategies

2. I would like to reinforce its knowledge by making it learn crypto charts so its being capable of trade any coin with profit

## Goal

Consistently 10x my trading account using high leverage