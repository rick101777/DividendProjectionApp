from pandas import DataFrame

import plotly.express as px

from constants import YEARS_OF_REINVESTMENT


class ProjectionVisualizer:

    @staticmethod
    def __columns_to_plot():
        dividends_columns = []
        share_columns = []
        x_range = []
        for year in range(1, YEARS_OF_REINVESTMENT + 1):
            for quarter in range(1, 5):
                dividends_columns.append(f"Reinvested Y{year}Q{quarter} Dividends")
                share_columns.append(f"Reinvested Y{year}Q{quarter} Shares")
                x_range.append(f"Y{year}Q{quarter}")

        return dividends_columns, share_columns, x_range

    @staticmethod
    def generate_visualization(growth_df: DataFrame):
        dividend_columns, share_columns, x_range = ProjectionVisualizer.__columns_to_plot()
        plot = px.scatter(growth_df, x="Company Name", y=dividend_columns, color="Company Name",
                          title="Dividends Projection")
        plot2 = px.scatter(growth_df, x="Company Name", y=share_columns, color="Company Name",
                           title="Share Projections")
        plot.show()
        plot2.show()

    @staticmethod
    def view_single_stock_growth(growth_df: DataFrame, company_name: str):
        dividend_columns, share_columns, x_range = ProjectionVisualizer.__columns_to_plot()
        single_df = growth_df[growth_df["Company Name"] == company_name]
        data = single_df[dividend_columns].values.tolist()

        plot = px.scatter(x=x_range, y=data,
                          labels={
                              "x": "Time",
                              "value": "Dividend Return ($)",
                              "variable": company_name,
                              "wide_variable_0": "dividends in $"
                          },
                          title=f"{company_name} Dividend Returns Over Time")

        plot.show()
