import matplotlib.pyplot as plt


def plt_loss(epochs, loss, val_loss):
    plt.plot(epochs, loss, 'bo', label="Training loss")
    plt.plot(epochs, val_loss, 'b', label="Validation loss")
    plt.title("Training and validation loss")
    plt.xlabel('Epochs')
    plt.ylabel("Loss")
    plt.legend()
    return plt


def plt_accuracy(epochs, acc, val_acc):
    plt.plot(epochs, acc, 'bo', label="Training accuracy")
    plt.plot(epochs, val_acc, 'b', label="Validation accuracy")
    plt.title("Training and validation accuracy")
    plt.xlabel('Epochs')
    plt.ylabel("accuracy")
    plt.legend()
    return plt


def plt_loss_html(epochs, loss, val_loss):
    fig, _plt = plt.subplots()
    _plt.plot(epochs, loss, 'bo', label="Training loss")
    _plt.plot(epochs, val_loss, 'b', label="Validation loss")
    _plt.set_title("Training and validation loss")
    _plt.set_xlabel('Epochs')
    _plt.set_ylabel("Loss")
    _plt.legend()
    return fig


def plt_accuracy_html(epochs, acc, val_acc):
    fig, _plt = plt.subplots()
    _plt.plot(epochs, acc, 'bo', label="Training accuracy")
    _plt.plot(epochs, val_acc, 'b', label="Validation accuracy")
    _plt.set_title("Training and validation accuracy")
    _plt.set_xlabel('Epochs')
    _plt.set_ylabel("accuracy")
    plt.legend()
    return fig


