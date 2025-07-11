#write the code
#optimize the code

#Import all the packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

#JPM: JP Morgan
# MS: Morgan Stanley
# BAC:Bank of America

#Download Stock Data from Python

tickers = ['JPM','MS','BAC']
start_date = '2024-01-01'
end_date = '2025-01-01'

data1 = yf.download(tickers, start  = start_date, end = end_date)['Close']
print(data1)

#Visualize our Stocks Data

#Individual
line1 = px.line(data1, x=data1.index , y= data1['MS'] ,  title = 'Closing Price of MS, BAC, & JPM', color_discrete_sequence=["blue"]).show()
line2 = px.line(data1, x=data1.index , y= data1['BAC'] ,  title = 'Closing Price of MS, BAC, & JPM', color_discrete_sequence=["red"]).show()
line3 = px.line(data1, x=data1.index , y= data1['JPM'] ,  title = 'Closing Price of MS, BAC, & JPM', color_discrete_sequence=["green"]).show()



#Comparison on one chart

line4 = px.line(data1, title = 'Closing Price of MS, BAC, & JPM').show()

#Get Porfolio Simple Returns, Simple Returns & Log Returns from Jupyter Notebook


#Simple and Log Returns
simple_returns = data1.pct_change().dropna()
print(simple_returns)


log_returns = np.log(data1/data1.shift(1)).dropna()
print(log_returns)


#Portfolio Returns (Log & simple)
weights = np.array([1/3,1/3,1/3])
portfolio_simple_returns = simple_returns.dot(weights)
print(portfolio_simple_returns)


weights = np.array([1/3,1/3,1/3])
portfolio_log_returns = log_returns.dot(weights)
print(portfolio_log_returns)


#Annualize the return of our portfolio - Simple Return -> (1+AVG(Returns))^252 - 1

annualized_simple_return = ((1+portfolio_simple_returns.mean())**252)-1
print(annualized_simple_return)

#Annualize the return of our portfolio - Log Return -> Avg Returns * 252

annualized_log_return = portfolio_log_returns.mean()*252
print(annualized_log_return)


#Volatility 
daily_volatility = np.std(portfolio_simple_returns)
annual_volatility = daily_volatility*np.sqrt(252)
print(annual_volatility)


#Alpha and Beta (SPY Data)

#Calulate S&P Simple Return
start_date = '2024-01-01'
end_date = '2025-01-01'
benchmark = yf.download('^GSPC', start = start_date, end = end_date)['Close']
benchmark_returns = benchmark.pct_change()
benchmark_returns = benchmark_returns.dropna()
print(benchmark_returns)

#Calulate Beta -> Use variance and covariance, Beta = covariance(portfolio, market)/variance(market)
#Variance is std squared or volatility squares
#Covariance: How 2 Variables (Portfolio, Market) are moving togther

portfolio_returns = portfolio_simple_returns.to_numpy().flatten()
print(portfolio_returns)
benchmark_returns = benchmark_returns.to_numpy().flatten()
print(benchmark_returns)

cov_matrix = np.cov(portfolio_returns, benchmark_returns)
print(cov_matrix)

beta1 = (cov_matrix[0,1])/(cov_matrix[1,1])

print(beta1)

#Beta = 0.90 < 1 => Our Portfolio is less volatile than the market
#For every 1% Change in the market, our portfolio tend to change by ~0.90% in the same direction

#Calculate Alpha - Used the CAPM formula to calculate Alpha
risk_free_rate = 0.07
alpha = (np.mean(portfolio_simple_returns) - risk_free_rate/252) - beta1*(np.mean(benchmark_returns) - risk_free_rate/252)

alpha = alpha*252
print(alpha)

#Alpha represents the excess return of a portfolio relative to its benchmark
#Portfolio outperformed the benchmark by 14.45%

#Calculate the ratios & then optimize -> 27:57 & 25 minutes video left, finish entireproject by tonight

#Calculate the negative returns to find the Sortino Ratio
negative_returns = portfolio_simple_returns[portfolio_simple_returns<0]
downside_deviation = np.std(negative_returns) #Daily Downside Standard Deviation
downside_deviation = downside_deviation* np.sqrt(252) #Annualized Downside Std Dev
print(downside_deviation)

#Sortino Ratio = (Rp - Rf)/sigma(d)
sortino_ratio = (annualized_simple_return - risk_free_rate)/downside_deviation
print(sortino_ratio)

#For every unit of downside risk, the portfolio is generating 2.58 units of excess return 
#Sortino Ratio of 2.58 is considered to be very good

#Sharpe Ratio -> (Rp - Rf)/sigma

sharpe_ratio = (annualized_simple_return - risk_free_rate)/annual_volatility
print(annual_volatility)

#For every 1 unit of risk, the portfolio is generating 1.64 units of excess return
#This sharpe ratio is considered to be very good


#Calmar Ratio = Rp/Max Drawdown
#Max Drawdown => Cumulative return

cumulative_simple_returns = (1+portfolio_simple_returns).cumprod()
maximum_drawdown = ((cumulative_simple_returns.cummax() - cumulative_simple_returns)/cumulative_simple_returns.cummax()).max()
print(cumulative_simple_returns)
print(maximum_drawdown)

#Maximum drawdown of 13% => It shows the worst historical loss from peak to its lowest point in this period

#Explaination of max drawdown calculation
#cumulative_simple_returns = (1+portfolio_simple_returns).cumprod()
#running_max = cumulative_simple_returns.cummax()
#drawdown = (running_max - cumulative_simple_returns)/running_max
#maximum_drawdown = drawdown.max(), This is also the same thing with more steps

#Calmar Ratio
calmar_ratio = annualized_simple_return/maximum_drawdown
print(calmar_ratio)


#Treynor Ratio -> (Rp - Rf)/Beta

treynor_ratio = (annualized_simple_return - risk_free_rate)/beta1
print(treynor_ratio)

#Value at Risk (Historical Method)
#Calculate VaR for the 90th Percentile
portfolio_value = 1000000
var_90 = np.percentile(portfolio_simple_returns,10)*portfolio_value
var_95 = np.percentile(portfolio_simple_returns, 5)*portfolio_value
var_99 = np.percentile(portfolio_simple_returns, 1)*portfolio_value

#Explaination of VaR
#round(len(portfolio_simple_returns)*10/100), then with 5, then with 1
#Then find it in the portfolio array which is arranged in ascending order
#This value is that percentage of return which is the 10th, 5th or 1st percentile of the returns in a day, 
#multiplies by portfolio value gives you the maximum value at risk on any given day fro this portfolio

print(var_90)
print(var_95)
print(var_99)

#Conditional VaR / Expected Shortfall => E[Loss/Loss>VaR], sign becomes opposit since we are dealing with losses (negative numbers)
#This is with a 95th percentile calculation

c_var95 = portfolio_simple_returns[portfolio_simple_returns <= np.percentile(portfolio_simple_returns, 5)].mean()
c_var95 = c_var95*portfolio_value
print(c_var95)


