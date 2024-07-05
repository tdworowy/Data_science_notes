import os

from keras import regularizers
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# from keras.models import Sequential
# from keras.layers import Embedding, Flatten, Dense
from tensorflow.python.keras.layers import Embedding, Flatten, Dense
from tensorflow.python.keras.models import Sequential
import numpy as np

from vizualization import plt_loss, plt_accuracy

imdb_dir = "../data/aclImdb"
train_dir = os.path.join(imdb_dir, "train")
labels = []
texts = []
for label_type in ["neg", "pos"]:
    dir_name = os.path.join(train_dir, label_type)
    for fname in os.listdir(dir_name):
        if fname[-4] == ".txt":
            with open(os.path.join(dir_name, fname)) as f:
                texts.append(f.read())
            if label_type == "neg":
                labels.append(0)
            else:
                labels.append(1)
maxlen = 100  # 300
training_samples = 299  # 400
validation_samples = 10000
max_words = 10000

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index
print(f"Found {word_index} unique tokens")

data = pad_sequences(sequences, maxlen=maxlen)
labels = np.array(labels)
print(f"Data tensor shape{data.shape}")
print(f"Labels tensor shape{data.shape}")

indices = np.arange(data.shape[0])
np.random.shuffle(indices)  # data order was not random
data = data[indices]
labels = labels[indices]

x_train = data[:training_samples]
y_train = labels[:training_samples]
x_val = data[training_samples:validation_samples]
y_val = labels[training_samples:validation_samples]

glove_dir = "../data/glove"
embeddings_index = {}
embedding_dim = 100

with open(
    os.path.join(glove_dir, f"glove.6B.{str(embedding_dim)}d.txt"), encoding="mbcs"
) as f:
    for line in f.readlines():
        values = line.split()
        try:
            word = values[0]
            coefs = np.asarray(values[1:], dtype="float32")
            embeddings_index[word] = coefs
        except Exception as ex:
            word = values[0] + values[1]
            coefs = np.asarray(values[2:], dtype="float32")
            embeddings_index[word] = coefs
    print(f"Found {len(embeddings_index)} word vectors")

embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if i < max_words:
        if embedding_vector:
            embedding_matrix[i] = embedding_vector

model = Sequential()
model.add(Embedding(max_words, embedding_dim, input_length=maxlen))
model.add(Flatten())
model.add(Dense(32, activation="relu", kernel_regularizer=regularizers.l2(0.001)))
model.add(Dense(32, activation="relu", kernel_regularizer=regularizers.l2(0.001)))
model.add(Dense(1, activation="sigmoid"))

model.layers[0].set_weights([embedding_matrix])
model.layers[0].trainable = False

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])

history = model.fit(
    x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val)
)

model.save_weights("pre_trained_glove_model.h5")
acc = history.history["acc"]
val_acc = history.history["val_acc"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(1, len(acc) + 1)

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()

# test_loss, test_acc = model.evaluate(x_test, test_labels)
# print(f"test_acc:{test_acc}, test_loss:{test_loss}")
