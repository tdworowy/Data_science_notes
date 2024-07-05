from sklearn.metrics import confusion_matrix
from xgboost import XGBClassifier

from Python.basic.data_preparation import get_data_classification
from Python.basic.utils import calculate_metrics

if __name__ == "__main__":
    x_train, x_test, y_train, y_test = get_data_classification()

    xgb_classifier = XGBClassifier(verbosity=3, n_estimators=10, max_depth=3)
    xgb_classifier.fit(x_train, y_train)
    y_pred = xgb_classifier.predict(x_test)

    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    accuracy, recall, precision = calculate_metrics(cm)
    print(f"accuracy:{accuracy}, recall:{recall}, precision: {precision}")
