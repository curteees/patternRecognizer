from flask import Flask, jsonify
from flask_cors import cross_origin
from tickerService import TickerService

# Initialize Flask
app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello_world():
  return jsonify({'Hello': 'World'})

# This can be improved by getting different kinds of stock or tickers from different
# parts of the market. For now, it defaults to S&P 500
@app.route("/api/v1/tickers", methods=['GET'])
@cross_origin()
def get_tickers():
  ticker_service = TickerService('Data/sp500.csv')
  tickers = ticker_service.get_tickers()
  json_array = []

  for i in range(1, len(tickers)):
    json_array.append({
      "symbol": tickers[i]['Symbol'],
      "companyName": tickers[i]['Name'],
      "sector": tickers[i]['Sector']
    })

  return jsonify(json_array)


if __name__ == '__main__':
    app.run(debug=True)
