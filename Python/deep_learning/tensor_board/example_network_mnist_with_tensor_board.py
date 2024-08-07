from keras.datasets import mnist
from keras import models, layers
from keras.utils import to_categorical
import keras

"""recognition of handwritten numbers"""

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
callbacks = [
    keras.callbacks.TensorBoard(log_dir="logs", histogram_freq=1, embeddings_freq=1)
]

network = models.Sequential()
network.add(layers.Dense(256, activation="relu", input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation="softmax"))

network.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype("float32") / 255

print(f"Train new shape: {train_images.shape}")
print(f"Test new shape: {test_images.shape}")

train_label = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_label, epochs=5, batch_size=128, callbacks=callbacks)

print("******Start Test******")
test_loss, test_acc = network.evaluate(test_images, test_labels)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
