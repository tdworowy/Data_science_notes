import os, sys, random
from keras.engine.saving import load_model
from keras import utils, layers, models, optimizers
import numpy as np

file = 'nietzsche.txt'
if not os.path.isfile(file):
    path = utils.get_file(
        file,
        origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt'
    )
    text = open(path).read().lower()
    with open(file, 'w') as f:
        f.write(text)
else:
    text = open(file).read()

maxlen = 60
step = 3  # new sequence is probe every 3 characters
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i:i + maxlen])
    next_chars.append(text[i + maxlen])

chars = sorted(list(set(text)))
char_indices = dict((char, chars.index(char)) for char in chars)

x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

model = models.Sequential()
model.add(layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(layers.Dense(len(chars), activation='softmax'))

optimizer = optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=["acc"])


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


max_epoch = 20
model.fit(x, y, batch_size=128, epochs=max_epoch)
model.save('nietzsche.h5')
# model = load_model('nietzsche.h5')

for i in range(10):
    start_index = random.randint(0, len(text) - maxlen - 1)
    generated_text = text[start_index: start_index + maxlen]
    for temperature in [0.6]:  # [0.2, 0.5, 1.0, 1.2]:
        print('------Temperature:', temperature)
        for i in range(400):
            sampled = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(generated_text):
                sampled[0, t, char_indices[char]] = 1.
            preds = model.predict(sampled, verbose=0)[0]
            next_index = sample(preds, temperature)
            next_char = chars[next_index]
            generated_text += next_char
            generated_text = generated_text[1:]

        with open("output_nietzsche.txt", 'a') as out:
            out.write(f"Text: {generated_text}\n")
