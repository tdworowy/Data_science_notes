from keras.datasets import imdb
from keras.preprocessing import sequence
from keras import layers
from keras.models import Sequential

from vizualization import plt_loss, plt_accuracy

max_features = 10000
maxlen = 500
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

model = Sequential()
model.add(layers.Embedding(max_features, 128))
model.add(layers.Bidirectional(layers.LSTM(32, dropout=0.2, recurrent_dropout=0.2)))
model.add(layers.Dense(1, activation="sigmoid"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])
history = model.fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.2)

acc = history.history["acc"]
val_acc = history.history["val_acc"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(acc) + 1)

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
