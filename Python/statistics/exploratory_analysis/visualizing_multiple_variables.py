import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_conditional_zip_code(
    data: pd.DataFrame, zip_codes: list = [98188, 98105, 98108, 98126]
):
    kc_tax_zip = data.loc[data.ZipCode.isin(zip_codes), :]

    def hexbin(x, y, color, **kwargs):
        color_map = sns.light_palette(color, as_cmap=True)
        plt.hexbin(x, y, gridsize=25, cmap=color_map, **kwargs)

    graph = sns.FacetGrid(kc_tax_zip, col="ZipCode", col_wrap=2)
    graph.map(hexbin, "SqFtTotLiving", "TaxAssessedValue")
    plt.show()


if __name__ == "__main__":
    file = "../../data/statistics/kc_tax.csv"
    data = pd.read_csv(file)
    kc_tax = data.loc[
        (data.TaxAssessedValue < 750000)
        & (data.SqFtTotLiving < 3500)
        & (data.SqFtTotLiving > 100)
    ]

    plot_conditional_zip_code(kc_tax)
    plot_conditional_zip_code(data)  # with outliers
