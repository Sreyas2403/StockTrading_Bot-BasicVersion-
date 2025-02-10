# -*- coding: utf-8 -*-
"""StockTrading_Bot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DE9oiBsTnxTZT_VB0e2vZZ9K5-0QAROu
"""

import pandas as pd
import yfinance as yf
import time
from datetime import datetime

# Stock symbol and strategy parameters
symbol = input() + ".NS" #Adding ".NS" suffix for Indian Stocks in yfinance
short_window = 10  # 10days window for Short-term moving average (can extend upto 50)
long_window = 50   # 50days window for Long-term moving average (can extend upto 200)
initial_balance = 10000  # Money in INR

# Portfolio tracking
portfolio = {'cash': initial_balance, 'shares': 0} #creating a dictionary of available cash and shares pair

def get_stock_data(symbol):
    "EQ series historical stock data from Yahoo Finance"""
    df = yf.download(symbol, period="3mo", interval="1d")
    df['SMA_Short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_Long'] = df['Close'].rolling(window=long_window).mean()
    return df

def trade_logic(df):
    #Buy when short SMA crosses above long SMA, sell when it crosses below"""
    if df['SMA_Short'].iloc[-1] > df['SMA_Long'].iloc[-1] and df['SMA_Short'].iloc[-2] < df['SMA_Long'].iloc[-2]:
        return "BUY"
    elif df['SMA_Short'].iloc[-1] < df['SMA_Long'].iloc[-1] and df['SMA_Short'].iloc[-2] > df['SMA_Long'].iloc[-2]:
        return "SELL"
    return "HOLD"

def execute_trade(action, symbol, current_price):
    #Simulated trade execution (updates portfolio balance money & number of shares)
    global portfolio
    if action == "BUY" and portfolio['cash'] >= current_price:
        shares_to_buy = int(portfolio['cash'] // current_price)  # Max shares we can buy
        portfolio['cash'] -= shares_to_buy * current_price
        portfolio['shares'] += shares_to_buy
        print(f"Buying {shares_to_buy} shares of {symbol} at {current_price:.2f} INR")

    elif action == "SELL" and portfolio['shares'] > 0:
        portfolio['cash'] += portfolio['shares'] * current_price
        print(f"Selling {portfolio['shares']} shares of {symbol} at {current_price:.2f} INR")
        portfolio['shares'] = 0  # Reset position after selling

    print(f"Portfolio - Cash: {portfolio['cash']:.2f} INR, Shares: {portfolio['shares']}")

#Trading Loop Simulation
for _ in range(10):  # Run for 10 iterations (simulating 10 hours)
    try:
        df = get_stock_data(symbol)
        action = trade_logic(df)
        current_price = float(df['Close'].iloc[-1])  # Get latest closing price and Convert to float
        execute_trade(action, symbol, current_price)
        print(f"{datetime.now()} - Action: {action} - Price: {current_price:.2f} INR")
        time.sleep(5)  # Wait 5 seconds (adjust for real-time simulation)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)  # Retry after 1 second