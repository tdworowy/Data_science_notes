import ssl

from keras.applications import VGG16

ssl._create_default_https_context = ssl._create_unverified_context
conv_base = VGG16(weights="imagenet", include_top=False, input_shape=(150, 150, 3))

conv_base.summary()
