import pandas as pd

from pandas import DataFrame
from yfinance import Tickers


class Company:

    @staticmethod
    def build_companies_table(tickers: Tickers) -> DataFrame:
        columns = ["Company Name", "Ticker", "Price Per Share", "Number of Dividend Payouts", "Annual Dividend Yield",
                   "Quarterly Payout", "Annual Payout"]
        data = []
        for ticker, obj in tickers.tickers.items():
            print(obj.dividends[-1])
            temp = [obj.info['shortName'], ticker, obj.info['currentPrice'], obj.info["dividendRate"],
                    obj.info['fiveYearAvgDividendYield'], obj.dividends[-1], obj.dividends[-1] * 4]
            data.append(temp)
        df = pd.DataFrame(data, columns=columns)

        return df
