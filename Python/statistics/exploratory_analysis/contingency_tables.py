import pandas as pd

if __name__ == "__main__":

    """summarize the relationship between several categorical variables"""

    file = "../../data/statistics/lc_loans.csv"
    data = pd.read_csv(file)

    cross_tab = data.pivot_table(
        index="grade", columns="status", aggfunc=lambda x: len(x), margins=True
    )

    data_frame = cross_tab.loc["A":"G", :].copy()
    data_frame.loc[:, "Charged Off":"Late"] = data_frame.loc[
        :, "Charged Off":"Late"
    ].div(data_frame["All"], axis=0)
    data_frame["All"] = data_frame["All"] / sum(data_frame["All"])

    print(data_frame)
