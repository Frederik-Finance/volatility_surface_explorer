# test_utilities.py

import pytest
import pandas as pd
from utilities import calculate_iv, filter_options


def test_calculate_iv():
    """
    Test the calculate_iv function to ensure it correctly adds an 'iv' column.

    This test provides a mock DataFrame containing option strike prices and premiums
    (prices) to the calculate_iv function. It verifies that the function processes
    this data to add a new column ('iv' for implied volatility) to the DataFrame.

    The test checks the presence of the 'iv' column in the resulting DataFrame to
    ensure that implied volatility calculations are integrated as expected.
    """
    mock_data = pd.DataFrame({
        'strike': [100, 150, 200],
        'price': [10, 15, 5]
    })

    result = calculate_iv(mock_data)
    assert 'iv' in result.columns, "Expected 'iv' column to be added to the DataFrame after calculating implied volatility"


def test_filter_options():
    """
    Test the filter_options function for its ability to filter data based on price and volume thresholds.

    This test provides a mock DataFrame simulating options data with strike prices,
    premiums, and trading volumes. It applies the filter_options function with specific
    price and volume thresholds to test its filtering logic.

    The function is expected to return options that meet or exceed both the price and
    volume thresholds. This test verifies that the returned DataFrame matches the expected
    filtered data, ensuring the filter_options function operates correctly.
    """
    mock_data = pd.DataFrame({
        'strike': [100, 150, 200],
        'price': [10, 15, 5],
        'volume': [100, 50, 10]
    })

    filtered_data = filter_options(
        mock_data, threshold_price=10, threshold_volume=50)

    expected_filtered_data = pd.DataFrame({
        'strike': [100, 150],
        'price': [10, 15],
        'volume': [100, 50]
    }, index=[0, 1])  # Reset index for direct comparison

    pd.testing.assert_frame_equal(filtered_data.reset_index(
        drop=True), expected_filtered_data, "The filter_options function did not return the expected filtered data")
