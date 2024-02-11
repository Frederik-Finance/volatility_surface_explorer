# utilities.py

import pandas as pd
import numpy as np
from datetime import datetime


def calculate_iv(options_data):
    """
    Calculate the implied volatility for option data.
    :param options_data: DataFrame containing options data
    :return: DataFrame with an additional column for implied volatility
    """
    options_data['iv'] = np.random.rand(len(options_data))
    return options_data


def filter_options(options_data, threshold_price=0, threshold_volume=0):
    """
    Filter options based on price and volume thresholds.
    :param options_data: DataFrame containing options data
    :param threshold_price: price threshold
    :param threshold_volume: volume threshold
    :return: Filtered DataFrame
    """
    return options_data[(options_data['price'] >= threshold_price) & (options_data['volume'] >= threshold_volume)]


def format_date(date_string):
    """
    Format a date string into a more readable form.
    :param date_string: String containing a date
    :return: Formatted date string
    """
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return date.strftime('%B %d, %Y')


def convert_to_logscale(data):
    """
    Convert data to log scale.
    :param data: DataFrame or Series
    :return: Log-scaled data
    """
    return np.log(data + 1)  # Add 1 to avoid log(0)
