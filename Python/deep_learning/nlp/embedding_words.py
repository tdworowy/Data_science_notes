from keras.datasets import imdb
from keras.layers import Embedding, Flatten, Dense
from keras import preprocessing
from keras.models import Sequential

from vizualization import plt_loss, plt_accuracy

max_features = 10000
maxlen = 40
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(
    num_words=max_features
)

x_train = preprocessing.sequence.pad_sequences(train_data, maxlen=maxlen)
x_test = preprocessing.sequence.pad_sequences(test_data, maxlen=maxlen)

model = Sequential()
model.add(Embedding(max_features, 8, input_length=maxlen))
model.add(Flatten())
model.add(Dense(1, activation="sigmoid"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])

history = model.fit(
    x_train, train_labels, epochs=10, batch_size=32, validation_split=0.2
)

acc = history.history["acc"]
val_acc = history.history["val_acc"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(acc) + 1)

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()

test_loss, test_acc = model.evaluate(x_test, test_labels)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
