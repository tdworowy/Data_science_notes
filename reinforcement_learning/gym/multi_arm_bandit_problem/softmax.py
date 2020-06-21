import random
import math
import gym
import gym_bandits
import numpy as np


def softmax(tau: float, q:  np.ndarray):
    total = sum([math.exp(val / tau) for val in q])
    probs = [math.exp(val / tau) / total for val in q]
    threshold = random.random()

    cumulative_probe = 0.0
    for i, probe in enumerate(probs):
        cumulative_probe += probe
        if cumulative_probe > threshold:
            return i
    return np.argmax(probs)


if __name__ == "__main__":
    env = gym.make('BanditTenArmedGaussian-v0')

    num_rounds = 20000
    count = np.zeros(10)
    sum_rewards = np.zeros(10)
    q = np.zeros(10)

    for i in range(num_rounds):
        arm = softmax(tau=0.5, q=q)

        observation, reward, done, info = env.step(arm)

        count[arm] += 1
        sum_rewards[arm] += reward

        q[arm] = sum_rewards[arm] / count[arm]
    print(f"Optimal arm is {np.argmax(q)}")
