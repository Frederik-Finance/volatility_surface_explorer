# layout.py

import dash_core_components as dcc
import dash_html_components as html
from tickers import tickers  # Make sure to have this module for your tickers data


def create_layout(app):
    # Tickers
    ticker_options = [dict(label=str(ticker), value=str(ticker))
                      for ticker in tickers]

    return html.Div(
        [
            # Add header with images and app title
            html.Div([
                html.Img(
                    src="https://datashop.cboe.com/Themes/Livevol/Content/images/logo.png",
                    className='two columns',
                    style={
                        'height': '60',
                        'width': '160',
                        'float': 'left',
                        'position': 'relative',
                    },
                ),
                html.H1(
                    'Volatility Surface Explorer',
                    className='eight columns',
                    style={'text-align': 'center'}
                ),
                html.Img(
                    src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
                    className='two columns',
                    style={
                        'height': '60',
                        'width': '135',
                        'float': 'right',
                        'position': 'relative',
                    },
                ),
            ],
                className='row'
            ),

            # Add horizontal line and other components
            html.Hr(style={'margin': '0', 'margin-bottom': '5'}),
            html.Div([

            ]),



            # Temporary hack for live dataframe caching
            # 'hidden' set to 'loaded' triggers next callback
            html.P(
                hidden='',
                id='raw_container',
                style={'display': 'none'}
            ),
            html.P(
                hidden='',
                id='filtered_container',
                style={'display': 'none'}
            )
        ],
        style={
            'width': '85%',
            'max-width': '1200',
            'margin-left': 'auto',
            'margin-right': 'auto',
            'font-family': 'overpass',
            'background-color': '#F3F3F3',
            'padding': '40',
            'padding-top': '20',
            'padding-bottom': '20',
        },
    )
