import numpy
import pandas as pd
import yfinance as yf
import pandas_ta as ta

def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval="5m")
    return data

def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    data_close = data['Close']
    values = data_close.values
    avr_close = round(numpy.average(values), 13)
    print(f'Средняя цена закрытия акций за заданный период {avr_close}')


def notify_if_strong_fluctuations(data, threshold):
    data_close = data['Close']
    values = data_close.values

    min_value = values[0]
    max_value = values[0]
    # анализ на максимальное и минимальное значения
    for value in values:
        if value <  min_value:

            min_value = value
        elif value > max_value:
            max_value = value

    value_threshold = float(max_value-min_value)
    if  value_threshold > threshold:
        print(f'Разница цен закрытия акций за заданный период превышает порог! И составляет {value_threshold}')

def export_data_to_csv(data, filename):
    data.to_csv(f'{filename}.csv', index=False)

def add_calculate_indicator(data, length=2):
    # расчет индикаторов торгов
    data['RSI'] = ta.rsi(data['Close'], length=length)
    data['MACD'], data['MACD_Signal'], data['MACD_Hist'] = data.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
    return data