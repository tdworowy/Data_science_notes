import gym

env = gym.make("BipedalWalker-v3")

for episode in range(100):
    observation = env.reset()
    for i in range(10000):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(f"{i+1} timesteps taken for the episode")
            break
