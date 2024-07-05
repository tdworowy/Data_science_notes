from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

from Python.basic.data_preparation import get_data_classification
from Python.basic.utils import calculate_metrics

if __name__ == "__main__":
    x_train, x_test, y_train, y_test = get_data_classification()

    classifier = SVC(verbose=3, kernel="linear")
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    accuracy, recall, precision = calculate_metrics(cm)
    print(f"accuracy:{accuracy}, recall:{recall}, precision: {precision}")
