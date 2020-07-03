from keras import layers, Input

x = Input(shape=(64,))
branch_a = layers.Conv2D(128, 1, activation='relu', strides=2)(x)
branch_b = layers.Conv2D(128, 1, activation='relu')(x)
branch_b = layers.Conv2D(128, 3, activation='relu', strides=2)(branch_b)
branch_c = layers.AveragePooling2D(3, strides=2)(x)
branch_c = layers.Conv2D(128, 3, activation='relu')(branch_c)
branch_d = layers.Conv2D(128, 1, actication='relu')(x)
branch_d = layers.Conv2D(128, 3, actication='relu')(branch_d)
branch_d = layers.Conv2D(128, 3, actication='relu', strides=2)(branch_d)

output = layers.Concatenate([branch_a, branch_b, branch_c, branch_d], axis=-1)
# complete architecture of Inception V3 is implemented in keras.applications.inception_V3
