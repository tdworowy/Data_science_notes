import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    file = "../../data/statistics/loans_income.csv"
    income = pd.read_csv(file)
    income = income['x']

    sample_data = pd.DataFrame({
        'income': income.sample(1000),
        'type': 'Data',
    })
    sample_mean_05 = pd.DataFrame({
        'income': [income.sample(5).mean() for _ in range(1000)],
        'type': 'Mean on 5',
    })
    sample_mean_20 = pd.DataFrame({
        'income': [income.sample(20).mean() for _ in range(1000)],
        'type': 'Mean on 20',
    })

    income = pd.concat([sample_data, sample_mean_05, sample_mean_20])

    graph = sns.FacetGrid(income,
                          col='type',
                          col_wrap=1,
                          height=2,
                          aspect=2)
    graph.map(plt.hist, "income",
              range=[0, 200000],
              bins=40)

    plt.show()
