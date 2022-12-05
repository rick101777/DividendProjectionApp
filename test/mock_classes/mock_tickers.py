from mock_classes.mock_ticker import MockTicker


class MockTickers:

    def __init__(self, ticker: str, mock_ticker: MockTicker):
        self.tickers = {ticker: mock_ticker}
