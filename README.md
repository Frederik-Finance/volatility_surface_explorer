
# Volatility Surface Explorer

## Project Description
The Volatility Surface Explorer is an interactive web application designed to visualize the implied volatility surface for equity options. Targeted at financial analysts, quantitative researchers, and options traders, this tool aims to provide insights into the volatility characteristics of options across different strikes and maturities, facilitating better trading and hedging decisions.

## Features
- **Dynamic 3D Visualization**: Interactive 3D surface plots of implied volatility, enabling users to explore volatility dynamics across strikes and maturities.
- **Real-Time Data**: Fetches real-time options data from Yahoo Finance, ensuring up-to-date analysis.
- **Customizable Settings**: Users can select between different equities, option types (calls and puts), and visualization modes (3D surface, heatmap, and scatter plot).

## Installation

### Prerequisites
- Python 3.8 or later
- pip and virtualenv

### Installing
1. Clone the repository:
   ```sh
   git clone [Link to your GitHub repo]
   cd volatility_surface_explorer
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To run the application:
```sh
python app.py
```
Navigate to `http://127.0.0.1:8050/` in your web browser to view the app.

## Running the Tests
Ensure your development environment is active, and run:
```sh
pytest
```

## Deployment
This app can be deployed on platforms like Heroku, AWS Elastic Beanstalk, or your own server. Ensure you set environment variables as needed for production environments.

## Built With
- [Dash](https://dash.plotly.com/) - Interactive web application framework
- [Pandas](https://pandas.pydata.org/) - Data analysis and manipulation library
- [Plotly](https://plotly.com/python/) - Graphing library for interactive plots

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

