import csv

class TickerService:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_tickers(self):
        with open(self.file_name) as f:
            reader = csv.DictReader(f)
            tickers = list(reader)

            return tickers
