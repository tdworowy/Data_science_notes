from random import shuffle, sample
from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd


def chi_square(observed: list, expected: list) -> np.ndarray:
    pearson_residuals = []
    for row, expected in zip(observed, expected):
        pearson_residuals.append(
            [(observed - expected) ** 2 / expected for observed in row]
        )

    return np.sum(pearson_residuals)


def perm_fun(box: list, expected: list) -> np.ndarray:
    sample_clicks = [
        sum(sample(box, 1000)),
        sum(sample(box, 1000)),
        sum(sample(box, 1000)),
    ]
    sample_no_clicks = [1000 - n for n in sample_clicks]
    return chi_square([sample_clicks, sample_no_clicks], expected)


if __name__ == "__main__":
    file = "../../data/statistics/click_rates.csv"
    data = pd.read_csv(file)
    clicks = data.pivot(index="Click", columns="Headline", values="Rate")

    box = [1] * 34
    box.extend([0] * 2966)
    shuffle(box)

    expected_clicks = 34 / 3
    expected_no_clicks = 1000 - expected_clicks
    expected = [34 / 3, 1000 - 34 / 3]

    chi_sq_observed = chi_square(clicks.values, expected)
    perm_ch = [perm_fun(box, expected) for _ in range(2000)]

    resampled_p_value = sum(perm_ch > chi_sq_observed) / len(perm_ch)

    print(f"Observed chi square: {chi_sq_observed}")
    print(f"Resampled p-value: {resampled_p_value}")

    cho_sq1, p_value1, df1, expected1 = chi2_contingency(clicks)

    print(f"p-value: {p_value1}")  # p-value from chi-square distribution
