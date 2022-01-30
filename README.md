# Patterns

Place for me to store my algorithms for detecting stock patterns

open anaconda prompt
activate doji for python 3.8

How to get recent chart data, run this in your terminal:
python getChartData.py [TICKER]

- only does one ticker at a time right now
- could probably modify to pass in a list of tickers we want data for

How to get patterns from data, run this in your terminal:
python patternRecognizer.py [TICKER]

# Server

Make sure you have pipenv: `pip install pipenv`.

Need Flask too: `pip install flask`.

To activate this project's virtualenv, run `pipenv shell`.

Inside of the shell, run `python server.py`.

# TODOS:

- Data collection
  - make list of S&P 500 Tickers
  - modify getChartData.py to loop through list and get all recent data from those companies
- Add more candlestick patterns to recognizer
- Create REST API endpoints. Should be returned in JSON format
  - _GET_ stock data for a ticker.
  - _GET_ run pattern for a ticker.
