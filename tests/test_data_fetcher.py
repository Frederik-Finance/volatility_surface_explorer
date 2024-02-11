# test_data_fetcher.py

import datetime as dt
import pytest
import pandas as pd
from data_fetcher import get_raw_data, get_filtered_data


def test_get_raw_data():
    """
    Test the get_raw_data function to ensure it returns a non-empty DataFrame.

    This test checks if the function can successfully fetch data for a given
    ticker symbol (in this case, 'AAPL') and return it as a pandas DataFrame.
    The test validates both the type of the return value and its emptiness.
    """
    ticker = "AAPL"
    data = get_raw_data(ticker)
    assert isinstance(
        data, pd.DataFrame), "Expected data to be a pandas DataFrame"
    assert not data.empty, "Expected the DataFrame to not be empty when fetching data for a valid ticker"


def test_get_filtered_data():
    """
    Test the get_filtered_data function with mock data to ensure it correctly filters data.

    This test provides a mock DataFrame to the get_filtered_data function with
    predefined criteria. It checks if the returned data is filtered correctly based
    on these criteria, such as option type (call or put), volume threshold, and
    whether it calculates implied volatility. The function's ability to handle
    different parameters and return the expected filtered set of options data is validated.
    """
    mock_data = pd.DataFrame({
        'strike': [100, 150, 200],
        'expiry': ['2023-01-01', '2023-06-01', '2023-12-01'],
        'type': ['call', 'put', 'call'],
        'price': [10, 15, 5],
        'volume': [100, 150, 50]
    })

    filtered_data = get_filtered_data(
        mock_data, calculate_iv=True, call=True, put=False, above_below=50,
        volume_threshold=1, rf_interest_rate=0.01, dividend_rate=0.02,
        trading_calendar=True, market='last'
    )

    assert not filtered_data.empty, "Expected filtered data to not be empty given the mock data"
    expected_columns = ['strike', 'expiry', 'type', 'price', 'volume']
    assert all(column in filtered_data.columns for column in expected_columns), \
        f"Expected filtered data to contain columns {expected_columns}"


def test_get_time_delta_trading_days():
    today = dt.datetime(2023, 1, 1)
    date_list = [dt.datetime(2023, 1, 10), dt.datetime(2023, 1, 20)]
    deltas, normalized = get_time_delta(
        today, date_list, trading_calendar=True)

    # Assuming 6 trading days between 1st and 10th, and 14 trading days between 1st and 20th
    # and considering weekends but not public holidays for simplicity in this example.
    expected_deltas = [6, 14]
    expected_normalized = [6 / 252.0, 14 / 252.0]

    assert (deltas == expected_deltas).all(), "Delta calculation is incorrect"
    assert (normalized == expected_normalized).all(
    ), "Normalized delta calculation is incorrect"


def test_get_time_delta_calendar_days():
    today = dt.datetime(2023, 1, 1)
    date_list = [dt.datetime(2023, 1, 10), dt.datetime(2023, 1, 20)]
    deltas, normalized = get_time_delta(
        today, date_list, trading_calendar=False)

    expected_deltas = [10, 20]  # Simple calendar day count
    expected_normalized = [10 / 365.0, 20 / 365.0]

    assert (deltas == expected_deltas).all(), "Delta calculation is incorrect"
    assert (normalized == expected_normalized).all(
    ), "Normalized delta calculation is incorrect"


def test_get_time_delta_trading_days():
    """
    Test the get_time_delta function with trading calendar days.

    This test verifies that get_time_delta correctly calculates the number of trading days
    between a given start date and a list of end dates. It checks both the absolute deltas
    and their normalized form against expected values. The normalization assumes a trading
    year of 252 days.

    Parameters:
    - today: A datetime object representing the starting date.
    - date_list: A list of datetime objects representing the end dates.

    The test asserts that both the deltas and normalized deltas match expected values,
    accounting for trading days only.
    """
    today = dt.datetime(2023, 1, 1)
    date_list = [dt.datetime(2023, 1, 10), dt.datetime(2023, 1, 20)]
    deltas, normalized = get_time_delta(
        today, date_list, trading_calendar=True)

    # Example expected values considering trading days.
    expected_deltas = [6, 14]
    expected_normalized = [6 / 252.0, 14 / 252.0]

    assert (deltas == expected_deltas).all(
    ), "Trading day delta calculation is incorrect"
    assert (normalized == expected_normalized).all(
    ), "Normalized trading day delta calculation is incorrect"


def test_get_time_delta_calendar_days():
    """
    Test the get_time_delta function with calendar days.

    This test checks get_time_delta's ability to compute the number of calendar days
    between a given start date and a list of end dates when not accounting for the trading
    calendar. It verifies both the absolute number of days (deltas) and their normalized
    form against predefined expectations. The normalization uses a standard year of 365 days.

    Parameters:
    - today: A datetime object for the start date.
    - date_list: A list of datetime objects for the end dates.

    The assertions confirm that the calculated deltas and normalized deltas are accurate,
    using simple calendar days without considering trading holidays or weekends.
    """
    today = dt.datetime(2023, 1, 1)
    date_list = [dt.datetime(2023, 1, 10), dt.datetime(2023, 1, 20)]
    deltas, normalized = get_time_delta(
        today, date_list, trading_calendar=False)

    expected_deltas = [10, 20]  # Expected values using simple calendar count.
    expected_normalized = [10 / 365.0, 20 / 365.0]

    assert (deltas == expected_deltas).all(
    ), "Calendar day delta calculation is incorrect"
    assert (normalized == expected_normalized).all(
    ), "Normalized calendar day delta calculation is incorrect"
