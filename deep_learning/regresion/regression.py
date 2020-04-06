from keras import models, layers, regularizers
from keras.datasets import boston_housing
import numpy as np
import matplotlib.pyplot as plt

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std


def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001), input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model


"""Corss validation"""
k = 4
num_val_samples = len(train_data) // 4
num_epochs = 100
all_mean_histories = []

for i in range(k):
    print('processing flod #', i)
    val_data = train_data[i * num_val_samples:(i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples:(i + 1) * num_val_samples]

    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples],
         train_data[(i + 1) * num_val_samples:]],
        axis=0)

    partial_train_targets = np.concatenate(
        [train_targets[:i * num_val_samples],
         train_targets[(i + 1) * num_val_samples:]],
        axis=0)

    model = build_model()
    history = model.fit(partial_train_data, partial_train_targets, epochs=num_epochs, batch_size=16,
                        validation_data=(val_data, val_targets), verbose=0)

    mean_history = history.history['val_mae']
    print(f"mean_history: {mean_history}")
    all_mean_histories.append(mean_history)

average_mea_history = [
    np.mean([x[i] for x in all_mean_histories]) for i in range(num_epochs)
]
print(f"average_mea_history: {average_mea_history}")

# Chart 1
plt.plot(range(1, len(average_mea_history) + 1), average_mea_history)
plt.xlabel("Epochs")
plt.ylabel("mean absolute error")
plt.show()


# Chart 2 smooth (without first 10 observations)

def smooth_curve(points, factor=0.9):
    smooth_points = []
    for point in points:
        if smooth_points:
            previous = smooth_points[-1]
            smooth_points.append(previous * factor + point * (1 - factor))
        else:
            smooth_points.append(point)
    return smooth_points


smooth__mean_history = smooth_curve(average_mea_history[10:])

plt.plot(range(1, len(smooth__mean_history) + 1), smooth__mean_history)
plt.xlabel("Epochs")
plt.ylabel("mean absolute error")
plt.show()
