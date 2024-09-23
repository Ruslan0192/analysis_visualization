# Цель:
# Реализовать функцию calculate_and_display_average_price(data), которая вычисляет и выводит среднюю цену закрытия акций за заданный период.
#
# Реализация:
# Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'. Результат будет выводиться в консоль.
#
#
import numpy
import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    data_close = data['Close']
    values = data_close.values
    avr_close = round(numpy.average(values), 13)
    print(f'Средняя цена закрытия акций за заданный период {avr_close}')
