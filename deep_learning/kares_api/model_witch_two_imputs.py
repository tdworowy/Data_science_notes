from keras import Input, layers, Model
import numpy as np

from vizualization import plt_loss, plt_accuracy

text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

text_input = Input(shape=(None,), dtype='int32', name='text')
embedded_text = layers.Embedding(64, text_vocabulary_size)(text_input)
encoded_text = layers.LSTM(32)(embedded_text)

question_input = Input(shape=(None,), dtype='int32', name='question')
embedded_question = layers.Embedding(32, question_vocabulary_size)(question_input)
encoded_question = layers.LSTM(16)(embedded_question)

concatenated = layers.concatenate([encoded_text, encoded_question], axis=-1)
answer = layers.Dense(answer_vocabulary_size, activation='softmax')(concatenated)

model = Model([text_input, question_input], answer)

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['acc'])

# generate random data
num_samples = 1000
max_length = 100
text = np.random.randint(1, text_vocabulary_size,
                         size=(num_samples, max_length))
question = np.random.randint(1, question_vocabulary_size,
                             size=(num_samples, max_length))

answers = np.random.randint(0, 1, size=(num_samples, answer_vocabulary_size))

# train
#model.fit([text, question], answers, epochs=10, batch_size=128) # will also work
print(text)
print(question)
print(answers)
history = model.fit({'text': text, 'question': question}, answers, epochs=10, batch_size=128, validation_split=0.2) # Don't work

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

plt_loss(epochs, loss, val_loss).show()
plt_accuracy(epochs, acc, val_acc).show()
