import keras
import numpy as np
from keras import models, layers, regularizers
from keras.datasets import mnist
from keras.utils import to_categorical


class ActivationLogger(keras.callbacks.Callback):
    def set_model(self, model):
        self.model = model
        layer_outputs = [layer.output for layer in model.layers]
        self.activation_model = keras.models.Model(model.input, layer_outputs)

    def on_epoch_end(self, epoch, logs=None):
        if self.validation_data is None:
            raise RuntimeError("Requires validation data")
        validation_samples = self.validation_data[0][0:1]
        activations = self.activation_model.predict(validation_samples)
        f = open(f"activation_at_epoch{str(epoch)}.npz", "wb")
        np.savez(f, activations)
        f.close()


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
    callbacks=[ActivationLogger()],
    validation_split=0.2,
)
