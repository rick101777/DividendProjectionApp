import pandas as pd

from market.dividend_projection_app import DividendProjectionApp
from market.projection_visualizer import ProjectionVisualizer

pd.set_option("display.max_columns", 20)
pd.set_option("display.max_rows", 50)


def main():
    growth_df = DividendProjectionApp.run()
    # growth_df = DividendProjectionApp.local_run()

    ProjectionVisualizer.generate_visualization(growth_df)
    # ProjectionVisualizer.view_single_stock_growth(growth_df, "International Business Machines")
    # ProjectionVisualizer.view_single_stock_growth(growth_df, "Verizon Communications Inc.")


if __name__ == "__main__":
    main()
