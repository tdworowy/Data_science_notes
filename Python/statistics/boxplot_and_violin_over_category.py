import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # box plot
    file = "../data/statistics/airline_stats.csv"
    airline_stats = pd.read_csv(file)

    ax = airline_stats.boxplot(by="airline", column="pct_carrier_delay")
    plt.show()

    #violin
    ax = sns.violinplot(airline_stats.airline,
                        airline_stats.pct_carrier_delay,
                        inner="quartile",
                        color="blue")
    plt.show()