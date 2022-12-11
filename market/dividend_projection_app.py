import pandas as pd
import yfinance as yf
from pandas import DataFrame

from market.generate_dividends import GenerateDividends
from market.generate_yearly_dividend_growth import GeneratedYearlyDividendGrowth
from market.company import Company
from market.constants import companies


class DividendProjectionApp:
    # TODO:
    #   Update Dividend Project App to do:
    #       - Differentiate methods of providing parameters
    #       - Implement Caching
    #       -

    @staticmethod
    def local_run() -> DataFrame:
        """
        Info: Uses pre-calculate data stored locally to reduce network calls, should only be used in testing.
        """
        companies_df = pd.read_csv("resources/results/companies.csv")
        dividend_df = GenerateDividends.dividend_calculation(companies_df)
        refined_growth_df = GeneratedYearlyDividendGrowth.yearly_growth_calculation_refined(dividend_df)
        # growth_df = GeneratedYearlyDividendGrowth.yearly_growth_calculation(dividend_df)
        return refined_growth_df

    @staticmethod
    def run() -> DataFrame:
        """
        Info: Uses network calls to Yahoo Finance to pull company information like name, stock price, dividend payouts
            and more ....
        :return:
        """
        tickers = yf.Tickers(" ".join(companies.values()))
        companies_df = Company.build_companies_table(tickers)
        companies_df.to_csv("./resources/results/companies.csv")
        dividend_df = GenerateDividends.dividend_calculation(companies_df)
        dividend_df.to_csv("./resources/results/dividend.csv")
        growth_df = GeneratedYearlyDividendGrowth.yearly_growth_calculation_refined(dividend_df)
        growth_df.to_csv("./resources/results/growth.csv")

        return growth_df
