import pandas as pd
from pandas import DataFrame

from constants import TOTAL_LIQUID_ASSETS


class GenerateDividends:

    @staticmethod
    def dividend_calculation(companies_df: DataFrame) -> DataFrame:
        # NumberOfShares = RoundDown(TOTAL_LIQUID_ASSETS/SharePrice)
        # Quarterly Dividends Payout = RoundDown(NumberOfShares * QuarterlyDividendPayout)
        # Annual Dividend Payout = RoundDown(NumberOfShares * AnnualDividendPayout
        columns = ["Company Name", "Price Per Share", "Number of Shares", "Quarterly Dividends Payout",
                   "Annual Dividend Payout"]
        dividends_df = pd.DataFrame([], columns=columns)
        dividends_df["Company Name"] = companies_df["Company Name"]
        dividends_df["Price Per Share"] = companies_df["Price Per Share"]
        dividends_df["Annual Payout"] = companies_df["Annual Payout"]
        dividends_df["Quarterly Payout"] = companies_df["Annual Payout"] / 4
        dividends_df["Number of Shares"] = TOTAL_LIQUID_ASSETS / companies_df["Price Per Share"]
        dividends_df["Quarterly Dividends Payout"] = dividends_df["Number of Shares"] * companies_df["Quarterly Payout"]
        dividends_df["Annual Dividend Payout"] = dividends_df["Number of Shares"] * companies_df["Annual Payout"]

        return dividends_df
