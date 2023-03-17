import gym
import numpy as np
import pandas as pd
from indicators import moving_average, calculate_rsi, volume_pct_change, support_resistance_levels

class TradingEnvironment(gym.Env):
    def __init__(self, data, window_size, initial_balance, leverage):
        super(TradingEnvironment, self).__init__()

        self.data = data
        self.window_size = window_size
        self.initial_balance = initial_balance
        self.leverage = leverage

        self.action_space = gym.spaces.Discrete(8)  # Increased from 6 to 8 actions
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(window_size, 10), dtype=np.float32)

        # Calculate indicators
        self.data['ma'] = moving_average(self.data['close'])
        self.data['rsi'] = calculate_rsi(self.data['close'])
        self.data['volume_pct_change'] = volume_pct_change(self.data['volume'])
        self.data['resistance'], self.data['support'] = support_resistance_levels(self.data)

        self.reset()


    def reset(self):
        self.balance = self.initial_balance
        self.position = None
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        self.current_step = self.window_size
        self.balance_history = []

        state = self.data.iloc[self.current_step - self.window_size : self.current_step].copy()
        state['moving_average'] = moving_average(state['close'], window=14)
        state['rsi'] = calculate_rsi(state['close'], period=14)
        state['volume_pct_change'] = volume_pct_change(state['volume'])
        state['resistance'], state['support'] = support_resistance_levels(self.data)

        return state.values


    def step(self, action):
        self.current_step += 1
        reward = 0
        done = False

        current_price = self.data.iloc[self.current_step]['close']

        # Buy (Open Long Position)
        if action == 0:
            if self.position is None:
                self.entry_price = current_price
                self.position = self.entry_price
                self.stop_loss = self.entry_price * (1 - (0.05 / self.leverage))
                self.take_profit = self.entry_price * 1.05
                reward += self.initial_balance / (self.balance + 1)  # Add a dynamic reward for opening a long position

        # Hold
        elif action == 1:
            if self.position is not None:
                reward = -2  # Small penalty for holding a position


        # Close Long Position
        elif action == 2:
            if self.position is not None and self.position > 0:  # Check if there's a long position
                sell_price = current_price
                reward = (sell_price - self.position) * self.leverage
                self.balance += reward
                self.position = None
                self.entry_price = None
                self.stop_loss = None
                self.take_profit = None
                self.balance_history.append(self.balance)

        # Scale Up
        elif action == 3:
            if self.position is not None:
                profit = current_price - self.entry_price
                if profit > 0:
                    self.entry_price = current_price
                    self.stop_loss = self.entry_price * (1 - (0.05 / self.leverage))

        # Adjust Stop Loss
        elif action == 4:
            if self.position is not None:
                self.stop_loss = current_price * (1 - (0.05 / self.leverage))

        # Adjust Take Profit
        elif action == 5:
            if self.position is not None:
                self.take_profit = current_price * 1.05

        # Open Short Position
        elif action == 6:
            if self.position is None:
                self.entry_price = current_price
                self.position = -self.entry_price  # Short position represented by a negative value
                self.stop_loss = self.entry_price * (1 + (0.05 / self.leverage))
                self.take_profit = self.entry_price * 0.95
                reward += self.initial_balance / (self.balance + 1)  # Add a dynamic reward for opening a short position

        # Close Short Position
        elif action == 7:
            if self.position is not None and self.position < 0:  # Check if there's a short position
                buy_price = current_price
                reward = (self.entry_price - buy_price) * self.leverage
                self.balance += reward
                self.position = None
                self.entry_price = None
                self.stop_loss = None
                self.take_profit = None
                self.balance_history.append(self.balance)

        if self.position is not None:
            if (self.position > 0 and (current_price <= self.stop_loss or current_price >= self.take_profit)) or \
               (self.position < 0 and (current_price >= self.stop_loss or current_price <= self.take_profit)):
                if self.position > 0:
                    sell_price = current_price
                    reward = (sell_price - self.position) * self.leverage
                else:
                    buy_price = current_price
                    reward = (self.entry_price - buy_price) * self.leverage
                self.balance += reward
                self.position = None
                self.entry_price = None
                self.stop_loss = None
                self.take_profit = None
                self.balance_history.append(self.balance)
        
        if self.balance <= 0:
            reward = -1000  # You can adjust the penalty value based on your preferences
            done = True
        # Calculate the reward as the change in account balance
        if len(self.balance_history) > 0:
            reward = self.balance - self.balance_history[-1]
        else:
            reward = 0

        state = self.data.iloc[self.current_step - self.window_size : self.current_step].copy()
        state['moving_average'] = moving_average(state['close'], window=14)
        state['rsi'] = calculate_rsi(state['close'], period=14)
        state['volume_pct_change'] = volume_pct_change(state['volume'])
        state['resistance'], state['support'] = support_resistance_levels(self.data)

        return state.values, reward, done, dict()




