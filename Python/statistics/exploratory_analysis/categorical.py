import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from collections import Counter

if __name__ == "__main__":
    # bar plot

    iris = datasets.load_iris(as_frame=True)
    targets_names = iris["target_names"]
    targets = [target for target in iris["target"]]

    targets = Counter(targets)
    data_frame = pd.DataFrame(targets.values(), index=targets_names)
    data_frame.transpose().plot.bar()

    plt.show()
