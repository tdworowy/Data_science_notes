import random
import math
import gym
import gym_bandits
import numpy as np

from upper_confidence_bound import upper_confidence_bound
from epsilon_greedy import epsilon_greedy_policy
from softmax import softmax
from thompson_sampling_algorithm import thompson_sampling


def run(algorithm, algorithm_name, env, algorithm_args_names, algorithm_args_outer):
    num_rounds = 20000
    count = np.zeros(10)
    sum_rewards = np.zeros(10)
    q = np.zeros(10)
    reward = 0
    arm = 0

    alg_args_dict = {
        "count": count,
        "q": q,
        "env": env,
        "reward": reward,
        "arm": arm
    }

    alg_args_dict.update(algorithm_args_outer)

    for i in range(num_rounds):
        alg_args_dict["iters"] = i

        args = (alg_args_dict[key] for key in algorithm_args_names)

        arm = algorithm(*args)
        observation, reward, done, info = env.step(arm)

        count[arm] += 1
        sum_rewards[arm] += reward

        q[arm] = sum_rewards[arm] / count[arm]

    print(f"Optimal arm for {algorithm_name} is {np.argmax(q)}")


if __name__ == "__main__":
    env = gym.make('BanditTenArmedGaussian-v0')

    run(algorithm=epsilon_greedy_policy, algorithm_name="epsilon greedy policy", env=env,
        algorithm_args_names=["env", "q", "epsilon"], algorithm_args_outer={"epsilon": 0.5})

    run(algorithm=upper_confidence_bound, algorithm_name="upper confidence bound", env=env,
        algorithm_args_names=["iters", "count", "q"], algorithm_args_outer={})

    run(algorithm=softmax, algorithm_name="softmax", env=env,
        algorithm_args_names=["tau", "q"], algorithm_args_outer={"tau": 0.5})

    run(algorithm=thompson_sampling, algorithm_name="thompson sampling", env=env,
        algorithm_args_names=["reward", "arm"], algorithm_args_outer={})
