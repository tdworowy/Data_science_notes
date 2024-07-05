import random

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def epsilon_greedy(q: np.ndarray, num_banner: int, epsilon: float) -> np.ndarray:
    if random.uniform(0, 1) < epsilon:
        return np.random.choice(num_banner)
    else:
        return np.argmax(q)


if __name__ == "__main__":
    num_banner = 5

    df = pd.DataFrame()
    for i in range(num_banner):
        df[f"Banner_type_{i}"] = np.random.randint(0, 2, 100000)

    num_of_iterations = 100000
    banner_selected = []
    count = np.zeros(num_banner)

    q = np.zeros(num_banner)
    sum_reward = np.zeros(num_banner)

    for i in range(num_of_iterations):
        banner = epsilon_greedy(q, num_banner, epsilon=0.5)
        reward = df.values[i, banner]

        count[banner] += 1
        sum_reward[banner] += reward
        q[banner] = sum_reward[banner] / count[banner]

        banner_selected.append(banner)

    sns.distplot(banner_selected)
    plt.show()
