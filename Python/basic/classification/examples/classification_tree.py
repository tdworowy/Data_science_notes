from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

from Python.basic.data_preparation import get_data_classification
from Python.basic.utils import calculate_metrics


def decision_tree(x_train, y_train, x_test, y_test) -> tuple:
    '''Decision tree'''
    print('Decision Tree Classifier')
    tree_classifier = DecisionTreeClassifier(
        criterion='entropy',
        random_state=100,
        max_depth=2
    )
    tree_classifier.fit(x_train, y_train)
    y_pred = tree_classifier.predict(x_test)

    fig = plt.figure(figsize=(15, 10))
    _ = tree.plot_tree(tree_classifier,
                       filled=True)

    return confusion_matrix(y_test, y_pred), fig


if __name__ == '__main__':
    x_train, x_test, y_train, y_test = get_data_classification()
    cm, fig = decision_tree(x_train=x_train,
                            y_train=y_train,
                            x_test=x_test,
                            y_test=y_test)

    plt.show(fig)
    print("Confusion matrix")
    print(cm)
    accuracy, recall, precision = calculate_metrics(cm)
    print(f'accuracy:{accuracy}, recall:{recall}, precision: {precision}')
