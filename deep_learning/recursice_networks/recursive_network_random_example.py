import numpy as np
"""Random example"""
time_steps = 100
input_features = 32
output_features = 64
inputs = np.random.random((time_steps, input_features))  # just random noise
state_t = np.zeros(output_features)
W = np.random.random((output_features, input_features))
U = np.random.random((output_features, output_features))
b = np.random.random((output_features,))

successive_outputs = []

for input_t in inputs:
    output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t)) + b
    successive_outputs.append(output_t)
    state_t = output_t
final_output_sequence = np.concatenate(successive_outputs, axis=0)

print(final_output_sequence)
