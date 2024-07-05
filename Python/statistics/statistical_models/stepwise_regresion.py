from typing import Optional

import pandas as pd
from sklearn.linear_model import LinearRegression
from dmba import stepwise_selection
from dmba import AIC_score

if __name__ == "__main__":
    file = "../../data/statistics/house_sales.csv"
    data = pd.read_csv(file, sep="\t")

    predictors = [
        "SqFtTotLiving",
        "SqFtLot",
        "Bathrooms",
        "Bedrooms",
        "BldgGrade",
        "PropertyType",
        "NbrLivingUnits",
        "SqFtFinBasement",
        "YrBuilt",
        "YrRenovated",
        "NewConstruction",
    ]
    outcome = "AdjSalePrice"

    y = data[outcome]

    x = pd.get_dummies(data[predictors], drop_first=True)
    x["NewConstruction"] = [1 if nc else 0 for nc in x["NewConstruction"]]

    def train_model(variables: list) -> Optional[LinearRegression]:
        if len(variables) == 0:
            return None
        model = LinearRegression()
        model.fit(x[variables], y)
        return model

    def score_model(model: LinearRegression, variables: list):
        if len(variables) == 0:
            return AIC_score(y, [y.mean()] * len(y), model, df=1)
        return AIC_score(y, model.predict(x[variables]), model)

    best_model, best_variables = stepwise_selection(
        x.columns, train_model, score_model, verbose=True
    )

    print(f"Intercept: {best_model.intercept_:.3f}")
    print("Coefficients:")
    for name, coef in zip(best_variables, best_model.coef_):
        print(f" {name}: {coef}")
