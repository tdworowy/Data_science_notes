import math
import gym
import gym_bandits
import numpy as np


def upper_confidence_bound(iters, count:  np.ndarray, q:  np.ndarray) -> np.ndarray:
    ucb = np.zeros(10)
    if iters < 10:
        return iters
    else:
        for arm in range(10):
            upper_bound = math.sqrt((2 ** math.log(sum(count))) / count[arm])
            ucb[arm] = q[arm] + upper_bound

    return np.argmax(ucb)


if __name__ == "__main__":
    env = gym.make('BanditTenArmedGaussian-v0')

    num_rounds = 20000
    count = np.zeros(10)
    sum_rewards = np.zeros(10)
    q = np.zeros(10)

    for i in range(num_rounds):
        arm = upper_confidence_bound(iters=i, count=count, q=q)
        observation, reward, done, info = env.step(arm)

        count[arm] += 1
        sum_rewards[arm] += reward

        q[arm] = sum_rewards[arm] / count[arm]

    print(f"Optimal arm for is {np.argmax(q)}")
