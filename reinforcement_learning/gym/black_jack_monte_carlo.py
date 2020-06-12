from collections import defaultdict
import gym
import numpy as np
from matplotlib import pyplot as plt


def sample_policy(observation) -> int:
    score, dealer_score, usable_ace = observation
    return 0 if score >= 20 else 1


def generate_episode(policy, env):
    states, actions, rewards = [], [], []
    observation = env.reset()

    while True:
        states.append(observation)
        action = policy(observation)
        actions.append(action)

        observation, reward, done, info = env.step(action)
        rewards.append(reward)

        if done:
            break
    return states, actions, rewards


def first_visit_mc_prediction(policy, env, n_episodes):
    value_table = defaultdict(float)
    n = defaultdict(int)

    for _ in range(n_episodes):
        states, _, rewards = generate_episode(policy, env)
        returns = 0
        for t in range(len(states) - 1, -1, -1):
            r = rewards[t]
            s = states[t]
            returns += r
            if s not in states[:t]:
                n[s] += 1
                value_table[s] += (returns - value_table[s]) / n[s]

    return value_table


def plot_blackjack(v, ax1, ax2):
    player_sum = np.arange(12, 21 + 1)
    dealer_show = np.arange(1, 10 + 1)
    usable_ace = np.array([False, True])
    state_values = np.zeros((len(player_sum), len(dealer_show), len(usable_ace)))

    for i, player in enumerate(player_sum):
        for j, dealer in enumerate(dealer_show):
            for k, ace in enumerate(usable_ace):
                state_values[i, j, k] = v[player, dealer, ace]

    x, y = np.meshgrid(player_sum, dealer_show)
    ax1.plot_wireframe(x, y, state_values[:, :, 0])
    ax2.plot_wireframe(x, y, state_values[:, :, 1])

    for ax in ax1, ax2:
        ax.set_zlim(-1, 1)
        ax.set_ylabel('player sum')
        ax.set_xlabel('dealer showing')
        ax.set_zlabel('state-value')


if __name__ == "__main__":
    env = gym.make("Blackjack-v0")
    plt.style.use("ggplot")

    fix, axes = plt.subplots(nrows=2, figsize=(5, 8), subplot_kw={'projection': '3d'})
    axes[0].set_title("value function without usable ace")
    axes[1].set_title("value function with usable ace")

    value = first_visit_mc_prediction(sample_policy, env, n_episodes=500000)
    print(value)
    plot_blackjack(value, axes[0], axes[1])

    plt.show()
