from keras import layers, Input, Model

lstm = layers.LSTM(32)
left_input = Input(shape=(None, 18))
left_output = lstm(left_input)

right_input = Input(shape=(None, 128))
right_output = lstm(right_input)

merged = layers.concatenate([left_output, right_output], axis=-1)
predictions = layers.Dense(1, activation="sigmoid")(merged)

model = Model([left_input, right_input], predictions)
