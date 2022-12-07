import pandas as pd
import pytest

from market.generate_dividends import GenerateDividends


class TestGenerateDividends:

    @pytest.fixture
    def company_df(self):
        # 18, "Best Buy Co., Inc.", BBY, 84.745, 2.63, 0.88, 3.52
        data = {
            "Company Name": ["Best Buy Co., Inc."],
            "Ticker": ["BBY"],
            "Price Per Share": [84.745],
            "Annual Dividend Yield": [2.63],
            "Quarterly Payout": [0.88],
            "Annual Payout": [3.52]
        }
        return pd.DataFrame(data)

    def test_dividend_calculation(self, company_df):
        dividends_df = GenerateDividends.dividend_calculation(company_df, total_liquid_assets=20000)

        assert dividends_df["Price Per Share"].values[0] == 84.745
        assert dividends_df["Quarterly Payout"].values[0] == 0.88
        assert dividends_df["Annual Payout"].values[0] == 3.52
        # 20000 (total liquid assets) / 84.745 (price per share) = 236.00212401911617 (number of shares)
        assert dividends_df["Number of Shares"].values[0] == 236.00212401911617
        # 236.00212401911617 (number of shares) * 0.88 (Quarterly Payout) = 207.68186913682223 (Quarterly Dividend
        # Payout)
        assert dividends_df["Quarterly Dividends Payout"].values[0] == 207.68186913682223
        # 236.00212401911617 (number of shares) * 3.52 (Annual Payout) = 830.7274765472889 (Annual Dividend Payout)
        assert dividends_df["Annual Dividend Payout"].values[0] == 830.7274765472889
