import gym
import random
import retro  # TODO find list of games

env = gym.make("CarRacing-v0")  # TODO change game

# env.configure(remotes=1)
left = [
    ("KeyEvent", "ArrowUp", True),
    ("KeyEvent", "ArrowLeft", True),
    ("KeyEvent", "ArrowRight", False),
]
right = [
    ("KeyEvent", "ArrowUp", True),
    ("KeyEvent", "ArrowLeft", False),
    ("KeyEvent", "ArrowRight", True),
]
forward = [
    ("KeyEvent", "ArrowUp", True),
    ("KeyEvent", "ArrowLeft", False),
    ("KeyEvent", "ArrowRight", False),
]

turn = 0
rewards = []
buffer_size = 100

action = forward
observation_n = env.reset()
while True:
    turn -= 1
    if turn <= 0:
        action = forward
        turn = 0

    action_n = [action for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    if len(rewards) >= buffer_size:
        mean = sum(rewards) / len(rewards)

        if mean == 0:
            turn = 20
            if random.random() < 0.5:
                action = right
            else:
                action = left
        rewards = []
    env.render()
