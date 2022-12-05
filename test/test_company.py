from typing import Dict, Any
from unittest.mock import Mock

import pytest

from test.mock_classes.mock_ticker import MockTicker
from market.company import Company
from test.mock_classes.mock_tickers import MockTickers


class TestCompany:
    # index, name, ticker, stock price, annual dividend yield, quarterly payout, annual payout
    # 18,"Best Buy Co., Inc.",BBY,84.745,2.63,0.88,3.52

    @pytest.fixture
    def best_buy_ticker(self):
        mock_ticker = MockTicker("BBY")
        mock_ticker.info = {
            "shortName": "Best Buy Co., Inc.",
            "currentPrice": 84.745,
            "fiveYearAvgDividendYield": 2.63
        }
        mock_ticker.dividends = [0.88]
        mock_tickers = MockTickers("BBY", mock_ticker)
        return mock_tickers

    def test_fetch_ticker(self, best_buy_ticker):
        Company.fetch_tickers = Mock()
        Company.fetch_tickers.return_value = best_buy_ticker

        tickers: MockTicker = Company.fetch_tickers(["BBY"])

        stock: Dict[str, Dict[Any]] = tickers.tickers
        print(stock["BBY"])

        assert list(stock.keys()) == ["BBY"]
        assert stock["BBY"].info["shortName"] == "Best Buy Co., Inc."
        assert stock["BBY"].info["currentPrice"] == 84.745
        assert stock["BBY"].info["fiveYearAvgDividendYield"] == 2.63
        assert stock["BBY"].dividends == [0.88]
        assert Company.fetch_tickers.called
        assert Company.fetch_tickers.call_count == 1

    def test_build_companies_table(self, best_buy_ticker):
        df = Company.build_companies_table(best_buy_ticker)

        assert df.columns.tolist() == ["Company Name", "Ticker", "Price Per Share", "Annual Dividend Yield",
                                       "Quarterly Payout", "Annual Payout"]
        assert df["Company Name"].values[0] == "Best Buy Co., Inc."
        assert df["Ticker"].values[0] == "BBY"
        assert df["Price Per Share"].values[0] == 84.745
        assert df["Annual Dividend Yield"].values[0] == 2.63
        assert df["Quarterly Payout"].values[0] == 0.88
        assert df["Annual Payout"].values[0] == 3.52
