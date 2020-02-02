import matplotlib.pyplot as plt


def plt_loos(epochs, loss, val_loss):
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
