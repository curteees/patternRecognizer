import sys
import urllib

ticker = sys.argv[1]
print("Ticker = " + ticker)

def make_filename(ticker):
    output_path = "Data/" + ticker + ".csv"
    return output_path

# base_url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1607470781&period2=1639006781&interval=1d&events=history&includeAdjustedClose=true"
def make_url(ticker):
    ticker_url = "https://query1.finance.yahoo.com/v7/finance/download/" + ticker + "?period1=1607470781&period2=1639006781&interval=1d&events=history&includeAdjustedClose=true"
    return ticker_url
print(make_url(ticker))

def pull_historical_data(ticker):
    try:
        urllib.urlretrieve(make_url(ticker), make_filename(ticker))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker), "w")
        outfile.write(e.content)
        outfile.close()

pull_historical_data(ticker)