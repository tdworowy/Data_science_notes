import math
import gym
import gym_bandits
import numpy as np

alpha = np.ones(10)
beta = np.ones(10)


def thompson_sampling(reward: int, arm: int) -> np.ndarray:
    samples = [np.random.beta(alpha[i] + 1, beta[i] + 1) for i in range(10)]
    if reward > 0:
        alpha[arm] += 1
    else:
        beta[arm] += 1
    return np.argmax(samples)


if __name__ == "__main__":
    env = gym.make("BanditTenArmedGaussian-v0")
    num_rounds = 20000
    count = np.zeros(10)
    sum_rewards = np.zeros(10)
    q = np.zeros(10)

    reward = 0
    arm = 0

    for i in range(num_rounds):
        arm = thompson_sampling(reward, arm)
        observation, reward, done, info = env.step(arm)

        count[arm] += 1
        sum_rewards[arm] += reward

        q[arm] = sum_rewards[arm] / count[arm]

    print(f"Optimal arm for is {np.argmax(q)}")
