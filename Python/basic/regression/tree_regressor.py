from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error
from math import sqrt
from Python.basic.data_preparation import get_data_regression
from matplotlib import pyplot as plt

if __name__ == '__main__':
    x_train, x_test, y_train, y_test = get_data_regression()

    regressor = DecisionTreeRegressor(max_depth=4)
    regressor.fit(x_train, y_train)
    y_pred = regressor.predict(x_test)

    error_standard_deviation = sqrt(mean_squared_error(y_test, y_pred))
    print(error_standard_deviation)

    fig = plt.figure(figsize=(15, 10))
    _ = plot_tree(regressor,
                  filled=True)
    plt.show(fig)