import numpy as np
from keras import models, layers, regularizers
from keras.datasets import imdb

from vizualization import plt_loss, plt_accuracy

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)


def get_plain_text(review):
    word_index = imdb.get_word_index()
    revers_word_index = dict([(value, key) for (key, value) in word_index.items()])
    return " ".join([revers_word_index.get(i - 3, "?") for i in review])


def vectorized_sequences(sequence, dimension=10000):
    results = np.zeros((len(sequence), dimension))
    for i, sequence in enumerate(sequence):
        results[i, sequence] = 1
    return results


print(get_plain_text(train_data[0]))
x_train = vectorized_sequences(train_data)
x_test = vectorized_sequences(test_data)

y_train = np.asarray(train_labels)
y_test = np.asarray(test_labels)

"""regularizers.l2 and layers.Dropout are use to prevent overfitting """
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.001), input_shape=(10000,)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(16, activation='relu',kernel_regularizer=regularizers.l2(0.001)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(partial_x_train, partial_y_train, epochs=10, batch_size=512, validation_data=(x_val, y_val))
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()

test_loss, test_acc = model.evaluate(x_test, test_labels)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
