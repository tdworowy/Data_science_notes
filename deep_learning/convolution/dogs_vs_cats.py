import os, shutil
from keras import models, layers, optimizers
from keras_preprocessing.image import ImageDataGenerator

from vizualization import plt_accuracy, plt_loss

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

list(map(lambda x: os.mkdir(x) if not (os.path.isdir(x)) else print(f'{x} exists'),
         [small_set, train_dir, validation_dir, test_dir, train_cats, train_dogs, validation_cats, validation_dogs,
          tests_cats, tests_dogs]))


def copy_data(animal, range, dest_dir):
    fnames = [f'{animal}.{i}.jpg' for i in range]
    for fname in fnames:
        scr = os.path.join(original_set, fname)
        dst = os.path.join(dest_dir, fname)
        shutil.copy(scr, dst)


copy_data('cat', range(2000), train_cats)
copy_data('cat', range(2500, 3500), validation_cats)
copy_data('cat', range(3500, 4500), tests_cats)
copy_data('dog', range(2000), train_dogs)
copy_data('dog', range(2500, 3500), validation_dogs)
copy_data('dog', range(3500, 4500), tests_dogs)


model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(optimizer=optimizers.RMSprop(lr=1e-4), loss="binary_crossentropy", metrics=['acc'])

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
    steps_per_epoch=150,
    epochs=60,
    validation_data=validation_generator,
    validation_steps=100
)

model.save("cat_and_dogs_small_2.h5")

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()
