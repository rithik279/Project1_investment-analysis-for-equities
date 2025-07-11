# 📊 Project1: Investment Analysis for Equities

A beginner-friendly quant finance project focused on analyzing equity performance using Python. This project lays the foundation for building more advanced financial models and backtests in future iterations.

## 🧠 Project Goals

- Collect and clean equity price data
- Perform basic risk-return analysis
- Visualize key indicators (returns, volatility, drawdowns)
- Lay the groundwork for strategy backtesting

## 🗂️ Project Structure

quant-finance-project/
│
├── data/ # Raw or processed datasets (e.g., CSVs)
│ └── .gitkeep
├── notebooks/ # Jupyter notebooks for EDA and visualization
│ └── .gitkeep
├── src/ # Core Python code (functions, logic)
│ └── main.py
├── README.md # Project overview
├── requirements.txt # List of Python packages used
└── .gitignore # Files/folders excluded from Git tracking

markdown
Copy
Edit


## 🔧 Technologies

- Python
- pandas
- numpy
- pyplot
- yfinance

## Project Summary

- Downloaded Data From Yahoo Finance
- Visualized the Stock/Portfolio
- Calculated:
    - Daily Simple Returns
    - Daily Log Returns
    - Annualized Simple Returns
    - Annualized Log Returns
    - Daily & Annualized Portfolio Returns (Simple & Log)
    - Daily Volatility & Annualized Volatility
    - Benchmark Returns
    - Alpha
    - Beta
    - Sortino Ratio (Using Downside Deviation)
    - Sharpe Ratio
    - Maximum Drawdown (Using Cumulative Simple Returns)
    - Calmar Ratio (Using Max. Drawdown)
    - Treynor Ratio
    - Value At Risk Using Historical Method For 90th, 95th & 99th Percentile
    - Conditional Value At Risk For 95th Percentile

## Next Steps

-Take input from user for 3 stocks
- Ask the user for their investing goals and tailor the reponse too that
- Present each value as a dashbioard and explain the signifcance of each value with respect to the ticker that it is derived from.
- Make recommendations based on the performance of these three stocks
- Even more advanced: Make a recommendation for the weighting of each stock in the portfolio based on return, risk etc.
- Can implement these ideas using openai api integration to make this an interactive stock analyzing AI Agent.







