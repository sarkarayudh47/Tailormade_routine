import numpy as np
from routine import generate_timetable
num_time_slots = 48
num_actions = 3
num_episodes = 10
lr = 0.1
df = 0.9
ep = 0.2

Q = np.zeros((num_time_slots, num_actions))
work_concentration = np.zeros(num_time_slots)

user_feedback = [(0, 'work', 1), (1, 'work', 1), (2, 'work', 2),
                  (3, 'break', 1), (4, 'sleep', 2), (5, 'work', 3),
                  (6, 'work', 1), (7, 'work', 1), (8, 'work', 2),
                  (9, 'sleep', 1), (10, 'work', 1), (11, 'work', 2),
                  (12, 'work', 1), (13, 'break', 3), (14, 'work', 2),
                  (15, 'sleep', 1), (16, 'sleep', 1), (17, 'work', 2),
                  (18, 'work', 1), (19, 'work', 1), (20, 'break', 2)]

def action_to_int(action):
  if action == 'work':
    return 0
  elif action == 'break':
    return 1
  else:
    return 2

def get_reward(state, action):
    if action == 0:  # 'work' corresponds to action integer 0
        return work_concentration[state]
    else:
        return 0

for time, action, rating in user_feedback:
    Q[time, action_to_int(action)] = rating

for episode in range(num_episodes):
    state = -1
    epsilon = ep

    while True:
        new_state = (state + 1) % num_time_slots

        # Choose a random action with probability epsilon
        if np.random.rand() < epsilon:
            action = np.random.choice(range(num_actions))
        # Choose the action with the highest Q-value with probability 1-epsilon
        else:
            action = np.argmax(Q[state])

        reward = get_reward(state, action)

        new_Q = Q[state, action] + lr * (reward + df * np.max(Q[new_state]) - Q[state, action])
        Q[state, action] = new_Q

        if action == 0:  # 'work' corresponds to action integer 0
            work_concentration[state] += new_Q

        state = new_state

        # Decrease epsilon over time to reduce exploration
        epsilon *= 0.99

        #print(f"Episode: {episode}, State: {state}, Action: {action}, Reward: {reward}, Q-Values:\n {Q}")

        if state == num_time_slots - 1:
            break

peak_time = np.argmax(work_concentration)
tt=generate_timetable(Q, work_concentration,num_actions,num_time_slots)
print("Daily Timetable:")
for slot, task in tt.items():
    print(f"{slot}: {task}")
print(f"Peak productivity time: {peak_time}")
#total elapsed time ber korte hobe