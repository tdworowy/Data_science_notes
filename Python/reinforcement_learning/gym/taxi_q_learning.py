import gym
import random


def get_q(env) -> dict:
    q = {}
    for state in range(env.observation_space.n):
        for action in range(env.action_space.n):
            q[(state, action)] = 0
    return q


def update_q_table(
    env,
    q: dict,
    prev_state,
    action,
    reward: int,
    next_state,
    alpha: float,
    gamma: float,
) -> dict:
    q = q.copy()
    qa = max([q[next_state, _action] for _action in range(env.action_space.n)])
    q[(prev_state, action)] += alpha * (reward + gamma * qa - q[prev_state, action])
    return q


def epsilon_greedy_policy(env, q: dict, state, epsilon: float):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return max(list(range(env.action_space.n)), key=lambda x: q[state, x])


if __name__ == "__main__":
    env = gym.make("Taxi-v3")

    alpha = 0.4
    gamma = 0.999
    epsilon = 0.017

    q = get_q(env)
    rewards = []
    for i in range(8000):
        total_reward = 0
        prev_state = env.reset()

        while True:
            # env.render()
            action = epsilon_greedy_policy(env, q, prev_state, epsilon)
            next_state, reward, done, _ = env.step(action)

            q = update_q_table(
                env=env,
                q=q,
                prev_state=prev_state,
                action=action,
                reward=reward,
                next_state=next_state,
                alpha=alpha,
                gamma=gamma,
            )

            prev_state = next_state
            total_reward += reward
            if done:
                break
        rewards.append(total_reward)
        print(f"Total reward: {total_reward}")
    print(f"Best reward: {max(rewards)}")
    env.close()
