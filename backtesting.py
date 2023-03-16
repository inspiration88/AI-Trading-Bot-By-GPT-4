import pandas as pd
import trading_environment as te
import train
import performance_metrics as pm

def backtest_bot(symbol, leverage, timeframe_to_trade, csv_backtesting):
    backtest_data = pd.read_csv(csv_backtesting)
    window_size = train.WINDOW_SIZE
    initial_balance = train.INITIAL_BALANCE
    total_episodes = 50
    successful_runs = 0
    min_target_balance = initial_balance * 10

    portfolio_values = []

    for episode in range(total_episodes):
        environment = te.TradingEnvironment(data=backtest_data, window_size=window_size, initial_balance=initial_balance, leverage=leverage)
        state = environment.reset()
        done = False

        while not done:
            action = train.model.act(state)
            state, reward, done, _ = environment.step(action)
            portfolio_values.append(environment.balance)

        final_balance = environment.balance

        if final_balance >= min_target_balance:
            successful_runs += 1

    success_rate = (successful_runs / total_episodes) * 100

    if success_rate >= 50:
        print(f"Backtesting successful. Success rate: {success_rate:.2f}%")
        result = True
    else:
        print(f"Backtesting failed. Success rate: {success_rate:.2f}%")
        result = False

    # Calculate and print performance metrics
    portfolio = pd.DataFrame(portfolio_values, columns=["balance"])
    portfolio = pm.calculate_returns(portfolio)
    portfolio = pm.calculate_cumulative_returns(portfolio)
    sharpe_ratio = pm.calculate_sharpe_ratio(portfolio)
    max_drawdown = pm.calculate_max_drawdown(portfolio)

    print(f"Sharpe Ratio: {sharpe_ratio}")
    print(f"Max Drawdown: {max_drawdown}")

    # Plot cumulative returns
    pm.plot_cumulative_returns(portfolio)

    return result
