import pandas as pd
from sklearn.utils import resample
import matplotlib.pyplot as plt

if __name__ == "__main__":
    file = "../../data/statistics/loans_income.csv"
    income = pd.read_csv(file)

    results = []
    for n_repeat in range(1000):
        sample = resample(income)
        results.append(sample.median())
    results_S = pd.Series(results)

    print("Bootstrap statistics:")
    print(f"original median: {income.median()}")
    print(f"bias: {results_S.mean() - income.median()}")
    print(f"std error: {results_S.std()}")

    # density plot original
    ax = income["x"].plot.hist(density=True, figsize=(10, 10))
    income["x"].plot.density(ax=ax)
    plt.show()

    # density plot bootstrapped (looks little weird)
    results_df = pd.DataFrame(results)

    ax = results_df.plot.hist(density=True, figsize=(10, 10))
    results_df.plot.density(ax=ax)
    plt.show()
