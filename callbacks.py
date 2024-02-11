# callbacks.py

import pandas as pd
from dash.dependencies import Input, Output, State
# Ensure these functions are correctly defined in data_fetcher.py
from data_fetcher import get_raw_data, get_filtered_data


def register_callbacks(app):

    @app.callback(Output('raw_container', 'hidden'),
                  [Input('ticker_dropdown', 'value')])
    def cache_raw_data(ticker):
        # Ideally, use a more sophisticated caching mechanism instead of global
        global raw_data
        raw_data = get_raw_data(ticker)
        print('Loaded raw data')
        return 'loaded'

    @app.callback(Output('filtered_container', 'hidden'),
                  [Input('raw_container', 'hidden'),
                   Input('option_selector', 'value'),
                   Input('market_selector', 'value'),
                   Input('price_slider', 'value'),
                   Input('volume_slider', 'value'),
                   Input('iv_selector', 'value'),
                   Input('calendar_selector', 'value'),
                   Input('rf_input', 'value'),
                   Input('div_input', 'value')])
    def cache_filtered_data(hidden, call_or_put, market, above_below, volume_threshold,
                            calculate_iv, trading_calendar, rf_interest_rate, dividend_rate):
        if hidden == 'loaded':
            filtered_data = pd.DataFrame()
            print('Loaded filtered data')
            return 'loaded'

    @app.callback(Output('iv_surface', 'figure'),
                  [Input('filtered_container', 'hidden'),
                   Input('ticker_dropdown', 'value'),
                   Input('log_selector', 'value'),
                   Input('graph_toggles', 'values')],
                  [State('graph_toggles', 'values'),
                   State('iv_surface', 'relayoutData')])
    def make_surface_plot(hidden, ticker, log_selector, graph_toggles, graph_toggles_state, iv_surface_layout):
        figure = {}
        print('Updated IV Surface plot')
        return figure

    @app.callback(Output('iv_heatmap', 'figure'),
                  [Input('filtered_container', 'hidden'),
                   Input('ticker_dropdown', 'value'),
                   Input('graph_toggles', 'values')],
                  [State('graph_toggles', 'values'),
                   State('iv_heatmap', 'relayoutData')])
    def make_heatmap_plot(hidden, ticker, graph_toggles, graph_toggles_state, iv_heatmap_layout):
        figure = {}
        print('Updated IV Heatmap plot')
        return figure

    @app.callback(Output('iv_scatter', 'figure'),
                  [Input('filtered_container', 'hidden'),
                   Input('ticker_dropdown', 'value'),
                   Input('graph_toggles', 'values')],
                  [State('graph_toggles', 'values'),
                   State('iv_scatter', 'relayoutData')])
    def make_scatter_plot(hidden, ticker, graph_toggles, graph_toggles_state, iv_scatter_layout):
        figure = {}
        print('Updated IV Scatter plot')
        return figure
