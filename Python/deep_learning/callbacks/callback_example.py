from keras.datasets import mnist
from keras import models, layers, callbacks, regularizers
from keras.utils import to_categorical

from vizualization import plt_loss, plt_accuracy

callbacks_list = [
    callbacks.EarlyStopping(monitor="acc", patience=1),
    callbacks.ModelCheckpoint(
        filepath="model.h5", monitor="val_loss", save_best_only=True
    ),
    callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.1, pateince=10),
]

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
network = models.Sequential()
network.add(
    layers.Dense(
        256,
        activation="relu",
        input_shape=(28 * 28,),
        kernel_regularizer=regularizers.l2(0.001),
    )
)
network.add(
    layers.Dense(256, activation="relu", kernel_regularizer=regularizers.l2(0.001))
)
network.add(layers.Dense(10, activation="softmax"))

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype("float32") / 255

train_label = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["acc"])
history = network.fit(
    train_images,
    train_label,
    epochs=10,
    batch_size=128,
    callbacks=callbacks_list,
    validation_split=0.2,
)

acc = history.history["acc"]
val_acc = history.history["val_acc"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(acc) + 1)

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()

test_loss, test_acc = network.evaluate(test_images, test_labels)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
