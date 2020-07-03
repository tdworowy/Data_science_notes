import gym
import random


def get_q(env) -> dict:
    q = {}
    for state in range(env.observation_space.n):
        for action in range(env.action_space.n):
            q[(state, action)] = 0.0
    return q


def calculate_q(q: dict, state, action, next_action, reward: int, next_state, alpha: float, gamma: float) -> dict:
    q = q.copy()
    q[(state, action)] += alpha * (reward + gamma * q[(next_state, next_action)] - q[(state, action)])
    return q


def epsilon_greedy_policy(env, q: dict, state, epsilon: float):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return max(list(range(env.action_space.n)), key=lambda x: q[state, x])


if __name__ == "__main__":
    env = gym.make("Taxi-v3")

    alpha = 0.85
    gamma = 0.90
    epsilon = 0.8

    q = get_q(env)
    rewards = []
    for i in range(4000):
        total_reward = 0
        state = env.reset()

        action = epsilon_greedy_policy(env, q, state, epsilon)
        while True:
           # env.render()
            next_state, reward, done, _ = env.step(action)
            next_action = epsilon_greedy_policy(env, q, state, epsilon)
            q = calculate_q(q=q,
                            state=state,
                            action=action,
                            next_action = next_action,
                            reward=reward,
                            next_state=next_state,
                            alpha=alpha,
                            gamma=gamma)

            action = next_action
            state = next_state
            total_reward += reward
            if done:
                break
        rewards.append(total_reward)
        print(f"Total reward: {total_reward}")
    print(f"Best reward: {max(rewards)}")
    env.close()
