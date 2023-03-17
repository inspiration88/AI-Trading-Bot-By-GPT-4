import pandas as pd
import trading_environment as te
import train
import performance_metrics as pm
from tensorflow.keras.models import load_model
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy

def backtest_bot(leverage, csv_backtesting):
    backtest_data = pd.read_csv(csv_backtesting)
    total_episodes = 50
    successful_runs = 0
    initial_balance = train.INITIAL_BALANCE
    window_size = train.WINDOW_SIZE
    min_target_balance = initial_balance * 10

    portfolio_values = []

    # Load the trained model
    model_path = train.train_bot(...)  # Call the train_bot function with the required arguments
    trained_model = load_model(model_path)

    # Create a DQNAgent instance with the loaded model for backtesting
    memory = SequentialMemory(limit=5000, window_length=1)
    policy = EpsGreedyQPolicy(eps=0.1)
    dqn_agent = DQNAgent(model=trained_model, nb_actions=environment.action_space.n, memory=memory, nb_steps_warmup=500, target_model_update=1e-2, policy=policy)
    dqn_agent.compile(metrics=['mae'])

    for episode in range(total_episodes):
        environment = te.TradingEnvironment(data=backtest_data, window_size=window_size, initial_balance=initial_balance, leverage=leverage)
        state = environment.reset()
        done = False

        while not done:
            action = dqn_agent.forward(state)
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
