import gym
import numpy as np


# Dynamic programing, markov decision process and  Bellman equation

def value_iterations(env, gamma: float = 1.0) -> np.array:
    value_table = np.zeros(env.observation_space.n)
    threshold = 1e-20
    i = 1
    while True:
        updated_value_table = np.copy(value_table)

        for state in range(env.observation_space.n):
            q_value = []

            for action in range(env.action_space.n):
                next_states_rewards = []

                for next_sr in env.P[state][action]:
                    trans_prob, next_state, reward_prob, _ = next_sr
                    next_states_rewards.append((trans_prob * (reward_prob + gamma * updated_value_table[next_state])))

                q_value.append(np.sum(next_states_rewards))
            value_table[state] = max(q_value)
        if np.sum(np.fabs(updated_value_table - value_table)) <= threshold:
            print(f"value-iteration converge at iteration {i}")
            break
        else:
            i += 1
    return value_table


def compute_value_function(policy, gamma: float = 1.0):
    value_table = np.zeros(env.nS)
    threshold = 1e-10

    while True:
        updated_value_table = np.copy(value_table)

        for state in range(env.nS):
            action = policy[state]
            value_table[state] = sum([trans_prob * (reward_prob + gamma * updated_value_table[next_state])
                                      for trans_prob, next_state, reward_prob, _ in env.P[state][action]])

        if np.sum((np.fabs(updated_value_table - value_table))) <= threshold:
            break
    return value_table


def extract_policy(env, value_table, gamma: float = 1.0):
    policy = np.zeros(env.observation_space.n)

    for state in range(env.observation_space.n):
        q_table = np.zeros(env.action_space.n)

        for action in range(env.action_space.n):

            for next_sr in env.P[state][action]:
                trans_prob, next_state, reward_prob, _ = next_sr
                q_table[action] += (trans_prob * (reward_prob + gamma * value_table[next_state]))

        policy[state] = np.argmax(q_table)
    return policy


def policy_iteration(env, gamma: float = 1.0):
    old_policy = np.zeros(env.observation_space.n)
    i = 1
    while True:
        new_value_function = compute_value_function(old_policy, gamma)
        new_policy = extract_policy(env, new_value_function, gamma)

        if np.all(old_policy == new_policy):
            print(f'Policy-Iteration converged at step {i}')
            break
        else:
            i += 1
        old_policy = new_policy

    return new_policy


if __name__ == "__main__":
    env = gym.make("FrozenLake-v0")

    print(f"State count: {env.observation_space.n}")
    print(f"Actions count: {env.action_space.n}")

    optimal_value_function = value_iterations(env)
    optimal_policy = extract_policy(env, optimal_value_function)

    print(f"Optimal value function: {optimal_value_function}")
    print(f"Optimal policy {optimal_policy}")  # will find optimal policy

    optimal_policy2 = policy_iteration(env)
    print(f"Optimal policy {optimal_policy2}")  # will find optimal policy (another way)
