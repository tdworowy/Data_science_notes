from keras.datasets import mnist
from keras import models, layers
from keras.utils import to_categorical
import matplotlib.pyplot as plt

"""recognition of handwritten numbers"""

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(f"Train shape: {train_images.shape}")
print(f"Test shape: {test_images.shape}")

# Display example dig
plt.imshow(train_images[4], plt.cm.binary)
plt.show()


def get_model_sequential():
    network = models.Sequential()
    # network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
    network.add(layers.Dense(256, activation='relu', input_shape=(28 * 28,)))
    network.add(layers.Dense(10, activation='softmax'))
    return network


def get_model_api_interface():
    input_tensor = layers.Input(shape=(784,))
    x = layers.Dense(32, activation='relu')(input_tensor)
    output_tensor = layers.Dense(10, activation='softmax')(x)
    return models.Model(inputs=input_tensor, outputs=output_tensor)


#network = get_model_sequential()
network = get_model_api_interface()
network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print(f"Train new shape: {train_images.shape}")
print(f"Test new shape: {test_images.shape}")

train_label = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_label, epochs=5, batch_size=128)

network.save("network1.h5", overwrite=True)
print("******Start Test******")
test_loss, test_acc = network.evaluate(test_images, test_labels)
print(f"test_acc:{test_acc}, test_loss:{test_loss}")
