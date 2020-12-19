from numpy.core.multiarray import ndarray


def calculate_metrics(confusion_matrix: ndarray) -> tuple:
    tn, fp, fn, tp = confusion_matrix.ravel()
    accuracy = (tp + tn) / sum([tn, fp, fn, tp])
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    return accuracy, recall, precision