import numpy as np

"""Hot-one encode word"""

samples = ["The cat sat on the mat", "The dog ate my homework"]
token_index = {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1

max_length = 10
results = np.zeros((len(samples), max_length, max(token_index.values()) + 1))
for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1
print("WORDS")
print(results)
print("*" * 50)
"""Hot one encode character"""

import string

samples = ["The cat sat on the mat", "The dog ate my homework"]
characters = string.printable  # all printable ASCII characters

token_index = dict(zip(characters, range(1, len(characters) + 1)))
max_length = 50
results = np.zeros((len(samples), max_length, max(token_index.values()) + 1))

for i, sample in enumerate(samples):
    for j, character in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(character)
        results[i, j, index] = 1

print("Characters")
print(results)
