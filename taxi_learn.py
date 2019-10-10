import gym
from IPython.display import clear_output
from time import sleep
import numpy as np
import random

env = gym.make("Taxi-v2").env
env.render()

print(f"Action Space {env.action_space}")
print(f"State Space {env.observation_space}")

state = env.encode(3, 1, 2, 0) #taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()

env.s = 328

alpha = 0.1
gamma = 0.6
epsilon = 0.1

q_table = np.zeros([env.observation_space.n, env.action_space.n])

all_epochs = []
all_penalties = []


def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'].getvalue())
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)

for j in range(1, 100001):
    epochs = 0
    penalties = 0
    reward = 0
    frames = [] #for animation
    done = False

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1

        if j % 100 == 0:
            clear_output(wait=True)
            print(f"Episode: {j}")

    print("Training finished.\n")

total_epochs, total_penalties = 0, 0
episodes = 100

for _ in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0

    done = False

    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")