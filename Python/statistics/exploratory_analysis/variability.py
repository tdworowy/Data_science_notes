import pandas as pd
from statsmodels import robust

if __name__ == "__main__":
    file = "../../data/statistics/hw1_data.csv"
    data = pd.read_csv(file)

    standard_deviation = data["Wind"].std()
    interquartile_range = data["Wind"].quantile(0.75) - data["Wind"].quantile(0.25)
    median_absolute_deviation = robust.scale.mad(data["Wind"])

    print(
        f"standard deviation: {standard_deviation}\ninterquartile range: {interquartile_range}\nmedian absolute deviation: {median_absolute_deviation}"
    )
