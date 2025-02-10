# StockTrading_Bot-BasicVersion-
This is a stock trading bot that uses a Simple Moving Average (SMA) crossover strategy to decide when to BUY, SELL, or HOLD a stock. The bot fetches stock price data from Yahoo Finance and simulates trades without needing real money or API keys.
Building a simple agent/bot for real time stock trading simulation using 'yfinance' library , "shortSMA" and "longSMA" for the trade logic. Stock Trading Bots are AI-powered software programs that automate buying and selling of stocks based on predefined algorithms.
We import libraries such as yfinance for real-time stock data dowmloading, pandas for data manuplation, datetime for days and date, time for hourly time intervals
Then in the program The bot will:
Download stock data for the last 3 months using yfinance taking a stock as input.
Afterwads, we Calculate SMA indicators (Short SMA & Long SMA).
We build trade logic using Short SMA & Long SMA and Decide trade actions:
📈 BUY when Short SMA crosses above Long SMA.
📉 SELL when Short SMA crosses below Long SMA.
➖ HOLD if no crossover occurs.
A dictionary is created with balance and shares as key-value pair
Balance is the available cash in the tarder's portfolio and shares are the number of shares available in the profolio
If the action is buy and balance is higher than stock's closing price and it buys maximum number of shares of that particular stock for the balance
Then the deducts the money from the balance using (closing price * max shares), and increases the shares value in the dictionary to the max shares the bot buys 
If the action is sell and shares are greater than 0 and sells all available shares of that particular stock
Then it increases the money in the balance value in dictionary using (clsoing price* shares) logic and sets shares value to '0' in the dictionary
At the end it prints "action" and the dictionary of balance-share pair
 


