import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    file = "../../data/statistics/kc_tax.csv"
    data = pd.read_csv(file)
    kc_tax = data.loc[
        (data.TaxAssessedValue < 750000)
        & (data.SqFtTotLiving < 3500)
        & (data.SqFtTotLiving > 100)
    ]

    print(kc_tax.shape)

    # hexagonal binding plot
    ax = kc_tax.plot.hexbin(
        x="SqFtTotLiving",
        y="TaxAssessedValue",
        gridsize=60,
        sharex=False,
        figsize=(10, 6),
        cmap=plt.cm.rainbow,
    )
    plt.show()

    # contour plot
    ax = sns.kdeplot(kc_tax[0:20000].SqFtTotLiving, kc_tax[0:20000].TaxAssessedValue)
    plt.show()
