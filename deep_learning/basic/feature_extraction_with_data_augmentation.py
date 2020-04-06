import os

from keras import models, layers, optimizers
from keras.applications import VGG16
from keras_preprocessing.image import ImageDataGenerator
from vizualization import plt_loss, plt_accuracy

conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(150, 150, 3))


conv_base.summary()
#conv_base.trainable = False # Freeze layers, prevent them from learning
conv_base.trainable = True
set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'block5_conv1':  # Freeze only upper layers, prevent them from learning
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

model = models.Sequential()
model.load_weights(conv_base_file)
#model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


original_set = 'data/original/train/train'
small_set = 'data/small'

train_dir = os.path.join(small_set, 'train')
validation_dir = os.path.join(small_set, 'validation')
test_dir = os.path.join(small_set, 'test')

train_cats = os.path.join(train_dir, 'cats')
train_dogs = os.path.join(train_dir, 'dogs')

validation_cats = os.path.join(validation_dir, 'cats')
validation_dogs = os.path.join(validation_dir, 'dogs')

tests_cats = os.path.join(test_dir, 'cats')
tests_dogs = os.path.join(test_dir, 'dogs')


model.compile(optimizer=optimizers.RMSprop(lr=1e-5), loss="binary_crossentropy", metrics=['acc'])

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   fill_mode='nearest')  # with data augmentation

val_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    directory=train_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)
validation_generator = val_datagen.flow_from_directory(
    directory=validation_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)
history = model.fit_generator(
    generator=train_generator,
    steps_per_epoch=100,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=50,
    verbose=2
)

model.save("cat_and_dogs_small_2.h5")

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()