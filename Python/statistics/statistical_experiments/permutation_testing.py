from random import sample

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def permutation(x: pd, nA: int, nB: int):
    n = nA + nB
    idx_b = set(sample(range(n), nB))
    idx_a = set(range(n)) - idx_b
    return x.loc[idx_b].mean() - x.loc[idx_a].mean()


if __name__ == "__main__":
    file = "../../data/statistics/web_page_data.csv"
    data = pd.read_csv(file)

    data.boxplot(by="Page", column="Time")
    plt.show()

    # compare means
    mean_a = data[data.Page == "Page A"].Time.mean()
    mean_b = data[data.Page == "Page B"].Time.mean()

    print(f"mean diff: {mean_a - mean_b}")

    nA = data[data.Page == 'Page A'].shape[0]
    nB = data[data.Page == 'Page B'].shape[0]

    perm_diff = [permutation(data.Time, nA, nB) for _ in range(1000)]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.hist(perm_diff, bins=11, rwidth=0.9)
    ax.axvline(x=mean_b - mean_a, color="red", lw=3)
    ax.text(50,190, "Observed\ndifference",
            bbox={"facecolor":"blue"})
    ax.set_xlabel("Session time differences")
    ax.set_ylabel("Frequency")

    plt.show()

    # how often mean difference of random permutation exceeds observed difference
    print(np.mean(perm_diff > mean_b - mean_a))
    """observed differences in session time between page A and B is well within the range of chance variation
    thus in not statistically significant 
    """