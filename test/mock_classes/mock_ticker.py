

class MockTicker:

    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.info = None
        self.dividends = None
