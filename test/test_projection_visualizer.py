import pytest

import pandas as pd
from pandas import RangeIndex

from market.projection_visualizer import ProjectionVisualizer


class TestProjectionVisualizer:

    # TODO Implement Tests
    @pytest.fixture
    def years_of_reinvestment(self):
        return 10

    @pytest.fixture
    def growth_df(self, years_of_reinvestment):
        columns = ["Company Name", "Price Per Share", "Number of Shares", "Quarterly Dividends Payout",
                   "Annual Dividend Payout", "Annual Payout", "Quarterly Payout"]
        for y in range(1, years_of_reinvestment + 1):
            for q in range(1, 5):
                columns.append("Reinvested Y{y}Q{q} Shares")
                columns.append("Reinvested Y{y}Q{q} Dividends")

        data = [[
            "Best Buy Co., Inc.", 84.745, 236.00212401911617, 207.68186913682223, 830.7274765472889, 3.52, 0.88,
            238.45279213094366, 209.83845707523042, 240.92890820947608, 209.83845707523042, 243.4050242880085,
            212.01743922433894, 245.9068525873104, 214.19642137344746, 248.43439310738177, 216.39803027683314,
            250.98791284632605, 218.62226593449594, 253.56767880224672, 220.86936330476692, 256.17396074578045,
            223.13955734597712, 258.80703122009726, 225.4330854562868, 261.46716556969056, 227.7501874736856,
            264.15464196916764, 230.0911057013277, 266.86974145233864, 232.45608493286753, 269.6127479416049,
            234.845372478058, 272.383948277649, 237.2592181886123, 275.18363224943033, 239.6978744843311,
            278.0120926244888, 242.1615963794987, 280.8696251795599, 244.65064150955013, 283.75652873150455,
            247.1652701580127, 286.673105168557, 249.705745283724, 289.6196594818938, 252.27233254833018,
            292.5964997975269, 254.86530034406653, 295.6039374085254, 257.48491982182367, 298.6422868075675,
            260.1314649195023, 301.7118657198278, 262.8052123906594, 304.81299513620235, 265.5064418334485,
            307.94599934687494, 268.23543571985806, 311.1112059752289, 270.99247942524994, 314.3089460121072,
            273.7778612582015, 317.5395538504245, 276.59187249065434, 320.80336732013546, 279.4348073883736,
            324.10072772356193, 282.3069632417192, 327.43197987108357, 285.2086403967345, 330.79747211719524,
            288.14014228655356, 334.1975563969351, 291.1017754631318, 337.63258826268685, 294.0938496293029,
            341.10292692136056, 297.11667767116444, 344.60893527195543, 300.1705756907973, 348.1509799435089,
            303.2558630393208, 351.7294313334354, 306.37286235028785, 355.3446636462596, 309.5218995734231
        ]]

        return pd.DataFrame(data=data, columns=columns, index=RangeIndex(start=0, stop=len(data[0])))

    def test_placeholder(self):
        df = pd.read_csv("resources/results/growth.csv")
        print(df.index)

    # def test_view_single_stock_growth(self, growth_df):
    #     # TODO: Fixing dataframe indexing
    #     print(growth_df, growth_df.columns, growth_df.index)
    #
    #     plot = ProjectionVisualizer.view_single_stock_growth(growth_df, "Best Buy Co., Inc.")

