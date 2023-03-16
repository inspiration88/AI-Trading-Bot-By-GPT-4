# AI Cryptocurrency Trading Bot Fully Built with ChatGPT-4

Prior to all i would like to comment that i don't have any experience in coding just a minor coding tweaks in bots but i am unable to even start the bot, write it, or even write functions in Python noneless reach this coding quality, proficiency and expertise. The current bot is an ongoing project to see if ChatGPT-4 has the capable to code a bot and being an AI apply AI on it and finally achieve profitability to automatize trading.

This AI trading bot is designed to trade cryptocurrencies using deep reinforcement learning. The bot is trained on historical data, and it can be used for backtesting and live trading. The bot uses technical indicators and additional actions like stop loss, take profit, and position scaling to make its trading decisions.

Any donations would be appreciated for keep working on this project and share public to make achieve its goal. Donations wallet: 0x570a977847a1b98a2e23cc4CB05E71046d1234DE

Date of start: 03/15/2023

## Components

0. 'main.py' - This file is the main execution tree script as control command for the bot where all variables would be set

1. `binance_config.py` - This file contains the configuration for connecting to the Binance API, including the API key and secret. The file uploaded is binance_configSAMPLE.py, add your binance keys and edit the filename to binance_config.py

2. `train.py` - This script is responsible for training the AI trading bot using historical data. It preprocesses the data, creates and compiles the model, and trains the model using the trading environment.

3. `trading_environment.py` - This file contains the custom trading environment for the AI trading bot, based on OpenAI Gym. The environment defines the observation space, action space, and the reward function. The reward function is designed to encourage the bot to make more trades when the account balance is closer to the initial balance, and focus on higher quality trades as the balance grows.

4. `backtesting.py` - This script is used to backtest the trained model on historical data. It simulates trading with the trained model and provides success rates, which can be used to evaluate the performance of the model before deploying it for live trading.

5. `live_trading.py` - This script is responsible for executing live trades with the trained model using the Binance API. The bot retrieves the latest market data, preprocesses it, and uses the model to predict the next action. The chosen action is then executed on the Binance platform.

6. `performance_metrics.py` - This script calculates various performance metrics, such as returns, Sharpe ratio, and drawdown, for the trading bot. These metrics can be used to evaluate the performance of the bot and make adjustments as needed.

7. `README.md` - This file provides an overview of the AI trading bot and its components.

## Planed shortterm updates

1. Based that is built on ChatGPT-4 i would leave open the possibility for people to edit the trading enviroment to train the bot into different strategies

2. I would like to reinforce its knowledge by making it learn crypto charts so its being capable of trade any coin with profit

## Goal

Consistently 10x my trading account using high leverage