import numpy as np

# Constants
NUM_ACTIONS = 6  # Number of possible durations: 0.5, 1, 1.5, 2, 2.5, 3 hours
NUM_SLOTS_PER_HOUR = 2  # Each slot represents 30 minutes
NUM_STATES = 3  # Number of activities: work, sleep, break
NUM_EPISODES = 1000
LR = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 0.1  # Epsilon-greedy parameter

# Q-table initialization
Q = np.zeros((NUM_STATES, NUM_ACTIONS))

# User feedback (slot, activity, rating)
user_feedback = [
    (0, 'work', 1), (1, 'work', 1), (2, 'work', 2),
    (3, 'break', 1), (4, 'sleep', 2), (5, 'work', 3),
    # Add more user feedback data
]

# Action durations in hours
ACTION_DURATIONS = [0.5, 1, 1.5, 2, 2.5, 3]  # Each action duration in hours

# Function to choose action based on epsilon-greedy strategy
def choose_action(state):
    return np.random.choice(NUM_ACTIONS) if np.random.rand() < EPSILON else np.argmax(Q[state])

# Main training loop
for _ in range(NUM_EPISODES):
    total_reward = 0
    state = 0  # Start from the beginning of the day
    for slot, activity, rating in user_feedback:
        duration = ACTION_DURATIONS[choose_action(state)]  # Choose action and duration

        # Update state based on activity
        if activity == 'work':
            state = 0
        elif activity == 'sleep':
            state = 1
        elif activity == 'break':
            state = 2

        # Calculate reward based on rating (for simplicity)
        reward = rating

        # Update Q-value using Q-learning update rule
        next_state = state + 1 if state < NUM_STATES - 1 else 0  # Cycle through states
        Q[state][choose_action(state)] += LR * (reward + GAMMA * np.max(Q[next_state]) - Q[state][choose_action(state)])

        # Accumulate total reward
        total_reward += reward

    print(f"Total Reward: {total_reward}")

# After training, the Q-table contains the learned Q-values
