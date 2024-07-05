from keras.preprocessing.text import Tokenizer

samples = ["The cat sat on the mat", "The dog ate my homework"]
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(samples)
sequence = tokenizer.texts_to_sequences(samples)

one_hot_results = tokenizer.texts_to_matrix(samples, mode="binary")

print(sequence)
print(one_hot_results)

word_index = tokenizer.word_index
print(word_index)
