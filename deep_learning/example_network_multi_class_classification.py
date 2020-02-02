import numpy as np
from keras import models, layers
from keras.datasets import reuters
from keras.utils import to_categorical

from vizualization import plt_loos, plt_accuracy

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=20000)


def get_plain_text(article):
    word_index = reuters.get_word_index()
    revers_word_index = dict([(value, key) for (key, value) in word_index.items()])
    return " ".join([revers_word_index.get(i - 3, "?") for i in article])


def vectorized_sequences(sequence, dimension=20000):
    results = np.zeros((len(sequence), dimension))
    for i, sequence in enumerate(sequence):
        results[i, sequence] = 1
    return results


def to_one_hot(labels, dimensions=46):
    """Same thing as keras.utils.to_categorical"""
    results = np.zeros((len(labels), dimensions))
    for i, label in enumerate(labels):
        results[i, label] = 1
    return results


print(get_plain_text(train_data[0]))
x_train = vectorized_sequences(train_data)
x_test = vectorized_sequences(test_data)

y_train = to_one_hot(train_labels)
y_test = to_one_hot(test_labels)
# y_train = to_categorical(train_labels)
# y_test = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(20000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

x_val = x_train[:1000]
partial_x_train = x_train[1000:]
y_val = y_train[:1000]
partial_y_train = y_train[1000:]

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
history = model.fit(partial_x_train, partial_y_train, epochs=9, batch_size=512, validation_data=(x_val, y_val))

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

plt_loos(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
