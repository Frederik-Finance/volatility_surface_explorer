# app.py

# Import required libraries
import os
from dash import Dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Volatility Surface Explorer"
server = app.server

# Setup app external CSS and JavaScript
external_css = [
    "https://fonts.googleapis.com/css?family=Overpass:300,300i",
    "https://cdn.rawgit.com/plotly/dash-app-stylesheets/dab6f937fd5548cebf4c6dc7e93a10ac438f5efb/dash-technical-charting.css"
]

for css in external_css:
    app.css.append_css({"external_url": css})

if 'DYNO' in os.environ:
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })

# Set the app layout
app.layout = create_layout(app)

# Register the callbacks
register_callbacks(app)

# Main
if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
