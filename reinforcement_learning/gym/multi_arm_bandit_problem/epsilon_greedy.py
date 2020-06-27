import random

import gym
import gym_bandits
import numpy as np


def epsilon_greedy_policy(env, q: np.ndarray, epsilon: float) -> np.ndarray:
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(q)


if __name__ == "__main__":
    env = gym.make('BanditTenArmedGaussian-v0')
    num_rounds = 20000
    count = np.zeros(10)
    q = np.zeros(10)
    sum_rewards = np.zeros(10)

    for i in range(num_rounds):
        arm = epsilon_greedy_policy(env, q, 0.5)

        observation, reward, done, info = env.step(arm)

        count[arm] += 1
        sum_rewards[arm] += reward

        q[arm] = sum_rewards[arm] / count[arm]
    print(f"Optimal arm:{np.argmax(q)}")
