from pandas import DataFrame

import plotly.express as px

from constants import YEARS_OF_REINVESTMENT


class ProjectionVisualizer:

    @staticmethod
    def __columns_to_plot():
        dividends_columns = []
        share_columns = []
        for year in range(1, YEARS_OF_REINVESTMENT + 1):
            for quarter in range(1, 5):
                dividends_columns.append(f"Reinvested Y{year}Q{quarter} Dividends")
                share_columns.append(f"Reinvested Y{year}Q{quarter} Shares")

        return dividends_columns, share_columns

    @staticmethod
    def generate_visualization(growth_df: DataFrame):
        dividend_columns, share_columns = ProjectionVisualizer.__columns_to_plot()
        plot = px.scatter(growth_df, x="Company Name", y=dividend_columns, color="Company Name",
                          title="Dividends Projection")
        plot2 = px.scatter(growth_df, x="Company Name", y=share_columns, color="Company Name",
                           title="Share Projections")
        plot.show()
        plot2.show()
