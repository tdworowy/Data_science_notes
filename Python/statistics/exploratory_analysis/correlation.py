import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.stats import pearsonr

if __name__ == "__main__":
    boston = datasets.load_boston()
    boston = pd.DataFrame(data=boston.data, columns=boston.feature_names)

    print(boston)
    correlation, _ = pearsonr(boston["TAX"], boston["B"])
    print(f"Correlation between TAX and B: {correlation}")

    # scatter plot
    boston.plot.scatter(
        x="TAX", y="B"
    )  # x and y are columns names from boston data frame
    plt.show()
