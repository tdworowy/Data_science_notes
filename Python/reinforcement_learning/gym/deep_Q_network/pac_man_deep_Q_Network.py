import numpy as np
import gym
from collections import deque, Counter
import random
from datetime import datetime
from keras import models, layers


# alternatives, dueling q networks, recurrent q networks
# TODO use Keras
def pre_process_observation(obs):
    color = np.array([210, 164, 74]).mean()

    img = obs[1:176:2, ::2]
    img = img.mean(axis=2)
    img[img == color] = 0
    img = (img - 128) / 128 - 1

    return img.reshape(88, 80, 1)


def epsilon_greedy(
    eps_min: float, eps_max: float, eps_decay_steps: float, action, step
):
    epsilon = max(eps_min, eps_max - (eps_max - eps_min) * step / eps_decay_steps)
    if np.random.rand() < epsilon:
        return np.random.randint(n_outputs)
    else:
        return action


def sample_memories(batch_size):
    perm_batch = np.random.permutation(len(exp_buffer))[:batch_size]
    mem = np.array(exp_buffer)[perm_batch]
    return mem[:, 0], mem[:, 1], mem[:, 2], mem[:, 3], mem[:, 4]


def generate_model():
    model = models.Sequential()

    model.add(
        layers.Conv2D(
            32, kernel_size=(8, 8), stride=4, padding="SAME", input_shape=(150, 150, 3)
        )
    )
    model.add(layers.Conv2D(64, kernel_size=(4, 4), stride=2, padding="SAME"))
    model.add(layers.Conv2D(64, kernel_size=(3, 3), stride=1, padding="SAME"))
    model.add(layers.Dense(128))
    model.add(layers.Dense(128))
    return model


if __name__ == "__main__":
    env = gym.make("MsPacman-v0")
    n_outputs = env.action_space.n

    epsilon = 0.5
    eps_min = 0.05
    eps_max = 1.0
    eps_decay_steps = 500000

    buffer_len = 20000
    exp_buffer = deque(maxlen=buffer_len)

    num_episodes = 800
    batch_size = 48
    input_shape = (None, 88, 80, 1)
    learning_rate = 0.001
    X_shape = (None, 88, 80, 1)
    discount_factor = 0.97

    global_step = 0
    copy_steps = 100
    steps_train = 4
    start_steps = 2000

    for i in range(num_episodes):
        done = False
        obs = env.reset()
        epoch = 0
        episodic_reward = 0
        actions_counter = Counter()
        episodic_loss = []

        mainQ, mainQ_outputs = generate_model()
        targetQ, targetQ_outputs = generate_model()

        while not done:

            # env.render()

            obs = pre_process_observation(obs)
            actions = mainQ_outputs.eval(
                feed_dict={X: [obs], in_training_mode: False}
            )  # TODO change to Keras

            action = np.argmax(actions, axis=-1)
            actions_counter[str(action)] += 1

            action = epsilon_greedy(
                eps_min, eps_max, eps_decay_steps, action, global_step
            )

            next_obs, reward, done, _ = env.step(action)

            exp_buffer.append(
                [obs, action, pre_process_observation(next_obs), reward, done]
            )

            if global_step % steps_train == 0 and global_step > start_steps:
                o_obs, o_act, o_next_obs, o_rew, o_done = sample_memories(batch_size)

                o_obs = [x for x in o_obs]
                o_next_obs = [x for x in o_next_obs]

                # next actions
                next_act = mainQ_outputs.eval(
                    feed_dict={X: o_next_obs, in_training_mode: False}
                )  # TODO change to Keras

                # reward
                y_batch = o_rew + discount_factor * np.max(next_act, axis=-1) * (
                    1 - o_done
                )

                mrg_summary = merge_summary.eval(
                    feed_dict={
                        X: o_obs,
                        y: np.expand_dims(y_batch, axis=-1),
                        X_action: o_act,
                        in_training_mode: False,
                    }
                )
                file_writer.add_summary(
                    mrg_summary, global_step
                )  # TODO change to Keras

                train_loss, _ = sess.run(
                    [loss, training_op],
                    feed_dict={
                        X: o_obs,
                        y: np.expand_dims(y_batch, axis=-1),
                        X_action: o_act,
                        in_training_mode: True,
                    },
                )  # TODO change to Keras
                episodic_loss.append(train_loss)

            if (global_step + 1) % copy_steps == 0 and global_step > start_steps:
                copy_target_to_main.run()  # TODO change to Keras

            obs = next_obs
            epoch += 1
            global_step += 1
            episodic_reward += reward

        print(
            "Epoch",
            epoch,
            "Reward",
            episodic_reward,
        )
