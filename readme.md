# Great Wall AI Trading Bot Built with ChatGPT-4

Introducing the Great Wall AI Trading Bot, a cutting-edge solution that draws inspiration from the resilience and grandeur of the ancient Chinese Great Wall and the vast, enigmatic expanse of the Great GRB Wall in the cosmos. This innovative trading bot is designed to navigate the complexities of the financial markets, seeking to conquer the ever-changing landscape of opportunities and risks.

This ongoing project aims to explore ChatGPT-4's ability to develop a bot, apply AI, and ultimately achieve profitable automated trading.

This AI trading bot leverages deep reinforcement learning to trade cryptocurrencies. It is trained on historical data and can be used for both backtesting and live trading. The bot employs technical indicators and additional actions, such as stop loss, take profit, and position scaling, to make informed trading decisions.

## Contributors
No coding experience but eager to help us build a revolutionary AI Trading bot by ChatGPT-4? No problem! Just get a Plus subscription for ChatGPT-4 and start collaborating with us.

If you're a skilled coder, your expertise is invaluable! Join us and use ChatGPT-4 as a powerful tool to enhance our code and strengthen the project.

## Components

1. `main.py` - The main script that serves as the control command for the bot, where all variables are set.

2. `binance_config.py` - Contains the configuration for connecting to the Binance API, including the API key and secret. Upload the file as binance_configSAMPLE.py, add your Binance keys, and rename the file to binance_config.py.

3. `train.py` - Responsible for training the AI trading bot using historical data. It preprocesses data, creates and compiles the model, and trains the model using the trading environment.

4. `brain.py` - Contains the custom trading environment for the AI trading bot, based on OpenAI Gym. The environment defines the observation space, action space, and reward function. The reward function encourages the bot to make more trades when the account balance is closer to the initial balance and to focus on higher-quality trades as the balance increases.

5. `backtesting.py` - Used to backtest the trained model on historical data. It simulates trading with the trained model and provides success rates to evaluate the model's performance before deploying it for live trading.

6. `live_trading.py` - Responsible for executing live trades with the trained model using the Binance API. The bot retrieves the latest market data, preprocesses it, and uses the model to predict the next action. The chosen action is then executed on the Binance platform.

7. `performance_metrics.py` - Calculates various performance metrics, such as returns, Sharpe ratio, and drawdown, for the trading bot. These metrics can be used to evaluate the performance of the bot and make adjustments as needed.

8. 'fetch_data.py' - 

9. 'indicators.py' - 


## Planed updates

1. As the bot is built on ChatGPT-4, we encourage community contributions to modify the trading environment, enabling the training of the bot with various strategies.

2. We aim to enhance the bot's knowledge by teaching it to analyze crypto charts, empowering it to trade any coin profitably.

3. Add more connectors for other exchanges like Okx, Bybit, Kucoin, Kraken, etc.

4. Add the ability to trade any coin

5. Incorporate sentiment analysis of a specific altcoin's community to enhance the bot's decision-making process. For instance, if the goal is to accumulate a project like the ARB token (Arbitrum), the bot should monitor relevant news on Twitter, track exchange updates for potential ARB token listings, and gauge sentiment within the project's Discord and other significant social media platforms. By analyzing this information, the bot can identify congruence between the chart trends and current news, enabling it to make more informed trading decisions.

6. Introduce an Arbitrage Mining feature to the bot, enabling it to capitalize on price discrepancies across multiple exchanges. While the bot is in a trade, it can simultaneously open three positions in three different exchanges rather than a single large position in one exchange. When price fluctuations occur due to spikes, causing the price to be higher in one exchange compared to another, the bot can quickly rebalance the trade before other arbitrage bots have a chance to act. This is achieved by partially closing the trade in the higher-priced exchange and opening a new position in the lower-priced exchange, subsequently restoring equilibrium. By exploiting the liquidity adjustments in this manner, the bot can take advantage of arbitrage opportunities more effectively.

7. Add On-chain support to multiple blockchains for the arbitrage mining feature included crossed to CEX.

## Goal

Consistently 10x my trading account using high leverage

## Why I Started the Bot
Over the past 2 years, I've been immersing myself in the world of trading and experimenting with various ready-made bots. My primary objective was to develop effective trading strategies, identify a competitive edge, and ultimately achieve profitability through full automation and standalone trading. The creation of an advanced trading bot demands a deep understanding of coding, which prompted me to pursue this knowledge after mastering the art of trading.

Although I've gained some coding experience by making minor tweaks to existing bots (copy-pasting and modifying code snippets), my current skill set falls short of what's needed to create a bot from scratch, write complex functions in Python, or reach a level of coding proficiency and expertise.

On March 15th, ChatGPT underwent an update that unleashed its remarkable potential. After running a series of tests, I discovered that ChatGPT's capabilities could be harnessed to develop an AI trading bot. This realization sparked my inspiration for embarking on a journey to create an AI-powered trading bot, turning this ambitious vision into reality with the invaluable assistance of ChatGPT.