import os
import numpy as np
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras import layers
from keras.optimizers import RMSprop

from vizualization import plt_loss

data_dir = "../data/jena_climate"
f_name = "jena_climate_2009_2016.csv"

with open(os.path.join(data_dir, f_name)) as file:
    data = file.read()

lines = data.split("\n")
header = lines[0].split(",")
lines = lines[1:]
print(header)

float_data = np.zeros((len(lines), len(header) - 1))
for i, line in enumerate(lines):
    values = [float(x) for x in line.split(",")[1:]]
    float_data[i, :] = values

"""Temperature visualization"""
temp = float_data[:, 1]
plt.plot(range(len(temp)), temp)
plt.show()
# first 10 days
plt.plot(range(1440), temp[:1440])
plt.show()

lookback = 2160  # observations
step = 3  # one observation per half of hour
delay = 144  # predict temperature in next 24 hours
batch_size = 128

# data normalization
mean = float_data[:200000].mean(axis=0)
float_data -= mean
std = float_data[:200000].std(axis=0)
float_data /= std


def generator(
    data, lookback, delay, min_index, max_index, shuffle=False, batch_size=128, step=6
):
    if max_index is None:
        max_index = len(data) - delay - 1
    i = min_index + lookback
    while 1:
        if shuffle:
            rows = np.random.randint(min_index + lookback, max_index, size=batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback
            rows = np.arange(i, min(i + batch_size, max_index))
            i += len(rows)
        samples = np.zeros((len(rows), lookback // step, data.shape[-1]))
        targets = np.zeros((len(rows),))
        for j, row in enumerate(rows):
            indices = range(rows[j] - lookback, rows[j], step)
            samples[j] = data[indices]
            targets[j] = data[rows[j] + delay][1]
            yield samples, targets


train_gen = generator(
    float_data,
    lookback=lookback,
    delay=delay,
    min_index=0,
    max_index=200000,
    shuffle=True,
    step=step,
)
val_gen = generator(
    float_data,
    lookback=lookback,
    delay=delay,
    min_index=200001,
    max_index=300000,
    shuffle=True,
    step=step,
)
test_gen = generator(
    float_data,
    lookback=lookback,
    delay=delay,
    min_index=300001,
    max_index=None,
    shuffle=True,
    step=step,
)

val_steps = (300000 - 200001 - lookback) // batch_size
test_steps = (len(float_data) - 300001 - lookback) // batch_size

"""Naive method"""


def evaluate_naive_method():
    batch_maes = []
    for step in range(val_steps):
        samples, targets = next(val_gen)
        preds = samples[:, -1, 1]
        mae = np.mean(np.abs(preds - targets))
        batch_maes.append(mae)
    print(np.mean(batch_maes))


evaluate_naive_method()

model = Sequential()
model.add(
    layers.Conv1D(32, 5, activation="relu", input_shape=(None, float_data.shape[-1]))
)
model.add(layers.MaxPooling1D(3))
model.add(layers.Conv1D(32, 5, activation="relu"))

model.add(layers.LSTM(32, dropout=0.1, recurrent_dropout=0.5))
model.add(layers.Dense(1))

model.compile(optimizer=RMSprop(), loss="mae")
history = model.fit_generator(
    train_gen,
    steps_per_epoch=500,
    epochs=40,
    validation_data=val_gen,
    validation_steps=val_steps,
)

loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(loss) + 1)

plt_loss(epochs, loss, val_loss).show()
