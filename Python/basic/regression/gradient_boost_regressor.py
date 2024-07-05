from math import sqrt

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

from Python.basic.data_preparation import get_data_regression

if __name__ == "__main__":
    x_train, x_test, y_train, y_test = get_data_regression()

    params = {
        "n_estimators": 500,
        "max_depth": 4,
        "min_samples_split": 2,
        "learning_rate": 0.01,
        "loss": "ls",
    }
    regressor = GradientBoostingRegressor(**params)
    regressor.fit(x_train, y_train)
    y_pred = regressor.predict(x_test)

    error_standard_deviation = sqrt(mean_squared_error(y_test, y_pred))
    print(error_standard_deviation)
