from typing import List

import pandas as pd
import yfinance as yf

from pandas import DataFrame
from yfinance import Tickers


class Company:

    @staticmethod
    def fetch_tickers(ticker_names: List[str]) -> Tickers:
        return yf.Tickers(" ".join(ticker_names))

    @staticmethod
    def build_companies_table(tickers: Tickers) -> DataFrame:
        columns = ["Company Name", "Ticker", "Price Per Share", "Annual Dividend Yield", "Quarterly Payout",
                   "Annual Payout"]
        data = []
        for ticker, obj in tickers.tickers.items():
            temp = [obj.info['shortName'], ticker, obj.info['currentPrice'],
                    obj.info['fiveYearAvgDividendYield'], obj.dividends[-1], obj.dividends[-1] * 4]
            data.append(temp)
        df = pd.DataFrame(data, columns=columns)

        return df
