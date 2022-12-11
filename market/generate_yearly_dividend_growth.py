from typing import Tuple

import pandas as pd
from pandas import DataFrame

from market.constants import YEARS_OF_REINVESTMENT


class GeneratedYearlyDividendGrowth:

    @staticmethod
    def growth_calculation(companies_df: DataFrame, dividends_df: DataFrame) -> DataFrame:
        # DividendReinvestedShares = RoundDown(AnnualDividendPayout/PricePerShare)
        # DividendPayoutDelta = ((DividendReinvestedShares+NumberOfShares)*AnnualPayout) - AnnualDividendPayout
        # TotalDividendsCollected = (DividendsPayoutDelta + AnnualDividendPayout)
        columns = ["Company Name", "Dividends Reinvested Shares", "Dividend Payout Delta", "Total Dividends Collected"]
        growth_df = pd.DataFrame([], columns=columns)
        growth_df["Company Name"] = dividends_df["Company Name"]
        growth_df["Dividends Reinvested Shares"] = dividends_df["Annual Dividend Payout"] / companies_df[
            "Price Per Share"]
        growth_df["Dividend Payout Delta"] = (growth_df["Dividends Reinvested Shares"] + dividends_df[
                                                 "Number of Shares"]) * \
                                             companies_df["Annual Payout"] - dividends_df["Annual Dividend Payout"]
        growth_df["Total Dividends Collected"] = (growth_df["Dividend Payout Delta"] +
                                                  dividends_df["Annual Dividend Payout"])

        return growth_df

    @staticmethod
    def yearly_growth_calculation_refined(dividend_df: DataFrame, years_of_reinvestment=None) -> DataFrame:
        for year in range(1, YEARS_OF_REINVESTMENT + 1):
            for quarter in range(1, 5):
                if year == 1 and quarter == 1:
                    dividend_df[f"Reinvested Y{year}Q{quarter} Shares"] = (
                            (dividend_df["Quarterly Dividends Payout"] / dividend_df["Price Per Share"]) +
                            dividend_df["Number of Shares"])

                    dividend_df[f"Reinvested Y{year}Q{quarter} Dividends"] = (
                            dividend_df[f"Reinvested Y{year}Q{quarter} Shares"] * dividend_df["Quarterly Payout"])
                else:
                    lyear, lquarter = GeneratedYearlyDividendGrowth.__look_back_one_quarter(year, quarter)
                    dividend_df[f"Reinvested Y{year}Q{quarter} Shares"] = (
                            dividend_df[f"Reinvested Y{lyear}Q{lquarter} Dividends"] / dividend_df["Price Per Share"] +
                            dividend_df[f"Reinvested Y{lyear}Q{lquarter} Shares"])
                    dividend_df[f"Reinvested Y{year}Q{quarter} Dividends"] = (
                            dividend_df[f"Reinvested Y{lyear}Q{lquarter} Shares"] * dividend_df["Quarterly Payout"]
                    )
        return dividend_df

    @staticmethod
    def __look_back_one_quarter(year: int, quarter: int) -> Tuple[int, int]:
        if quarter == 1:
            return year - 1, 4
        else:
            return year, quarter - 1

    @staticmethod
    def yearly_growth_calculation(dividend_df: DataFrame) -> DataFrame:

        def reinvestment(df: DataFrame, count: int = 1) -> DataFrame:
            if count >= YEARS_OF_REINVESTMENT:
                return df
            if count == 1:
                df[f"Reinvested Year {count} Shares"] = (
                        (df["Annual Dividend Payout"] / df["Price Per Share"]) +
                        df["Number of Shares"])

                df[f"Reinvested Year {count} Dividends"] = (
                        df[f"Reinvested Year {count} Shares"] * df["Annual Payout"])

                return reinvestment(df, count + 1)

            df[f"Reinvested Year {count} Shares"] = (
                    df[f"Reinvested Year {count - 1} Dividends"] / df["Price Per Share"] +
                    df[f"Reinvested Year {count - 1} Shares"])
            df[f"Reinvested Year {count} Dividends"] = (
                    df[f"Reinvested Year {count} Shares"] * df["Annual Payout"]
            )
            return reinvestment(df, count + 1)

        growth_df = reinvestment(dividend_df)

        return growth_df
