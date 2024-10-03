import yfinance as yf
import pandas_ta as ta
# import seaborn as sns
import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.svm import SVR
# from sklearn.preprocessing import StandardScaler

# Function to fetch historical data from Yahoo Finance
def fetch_historical_data(symbol, period="1y"):
    data = yf.download(tickers=symbol, period=period)
    return data

# Function to calculate the selected indicator
def calculate_indicator(data, indicator, length=14):
    if indicator == 'RSI':
        data = ta.rsi(data['Close'], length=length)
    elif indicator == 'MACD':
        data.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)

    return data
#
# # Function to plot the selected indicator
# def plot_indicator(data, indicator, model='linear'):
#     # Get the last 100 bars of the selected indicator
#     history = data[indicator].tail(100).reset_index()
#     history['index'] = history.index
#
#     # Create the regression model and fit it to the data
#     if model == 'linear':
#         reg = LinearRegression()
#     elif model == 'svr':
#         reg = SVR(kernel='rbf', C=1e3, gamma=0.1)
#         scaler = StandardScaler()
#         history[indicator] = scaler.fit_transform(history[[indicator]])
#     reg.fit(history[['index']], history[indicator])
#     history[f'{model}_pred'] = reg.predict(history[['index']])
#
#     # Plot the indicator and the regression line
#     sns.set(style="whitegrid")
#     plt.figure(figsize=(12, 6))
#     sns.lineplot(x='index', y=indicator, data=history)
#     sns.lineplot(x='index', y=f'{model}_pred', data=history, color='red', label=f'{model} regression')
#
#     # Set the plot title, axes labels, and tick labels
#     plt.title(f"{indicator} of EURUSD (5-minute interval) with {model.capitalize()} Regression")
#     plt.xlabel("Date and Time")
#     plt.ylabel(indicator)
#     plt.xticks(np.arange(0, len(history), 5), history['Datetime'].iloc[::5].dt.strftime('%a. %d %b %H:%M'), rotation=45)
#     plt.legend()
#     plt.show()

if __name__ == "__main__":
    # Set the symbol and indicator to be plotted
    symbol = "AAPL"
    indicator = 'RSI'

    # Fetch the historical data and calculate the selected indicator
    data = fetch_historical_data(symbol)
    indicator_data = calculate_indicator(data, indicator)

    print(indicator_data)

    plt.figure(figsize=(14, 7))
    plt.plot(indicator_data, label='RSI')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()
    plt.show()
    # Plot the indicator with support vector regression
    # plot_indicator(data, indicator, 'linear')