import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    file = "../../data/statistics/hw1_data.csv"
    data = pd.read_csv(file)
    percentiles = data["Temp"].quantile([0.05, 0.25, 0.5, 0.75, 0.95])

    print(percentiles)

    ax = data["Temp"].plot.box()
    plt.show()

    binned_temp = pd.cut(data["Temp"], 5)
    print(binned_temp.value_counts())  # frequency table

    ax = data["Temp"].plot.hist(figsize=(8, 8))
    plt.show()

    # density plot
    ax = data["Temp"].plot.hist(density=True)
    data["Temp"].plot.density(ax=ax)
    plt.show()