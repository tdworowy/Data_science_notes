from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
from Python.basic.data_preparation import get_data_regression


if __name__ == "__main__":
    x_train, x_test, y_train, y_test = get_data_regression()

    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    y_pred = regressor.predict(x_test)

    error_standard_deviation = sqrt(mean_squared_error(y_test, y_pred))
    print(error_standard_deviation)
