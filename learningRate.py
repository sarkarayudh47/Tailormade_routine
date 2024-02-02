import pandas as pd
from connectorr import fetchOutput
def learningRate(subject_name,obtained_marks,cutoff_marks,total_marks,first_exam,exam_flag): 
    current_lr= fetchOutput(subject_name, 'LR', False)
    sub_avgTime=fetchOutput(subject_name, 'AvgTime', False)
    sub_elapsedTime=fetchOutput[subject_name,'abc', True]
    if not exam_flag:                                           #jodi student exam na diye thake, tokhon jodi ei function ta call hoye tahole 'if' block ta call hobe, karon exam neoa hoye ni mane holo oke porte bola hocche, tar manei okei time recommend kora hocche 
        Total_learning_Time=current_lr*sub_avgTime              #ekhane ami oke ekta total learning time recommend korchi based on average time and learning rate jeta kina initially 1
    elif exam_flag:                                             #exam niye marks peye gele ei block ta execute hobe
        if obtained_marks>cutoff_marks:                         #jodi student kore
            if not first_exam:                                  #ei jayega ta dekhche j ei current exam ta student er ei SUBJECT a first exam noy kina
                lr=sub_elapsedTime/sub_avgTime                  #eisob sub_elapsed, sub_avg etc pore fetch korte db theke sub name take use kore
                current_lr=(current_lr+lr)/2                    #etake store korte hobe
            else:                                               #jodi first exam hoye r bhalo marks paye tahole porer bar learning rate kichu ta komate chai jate next time oke average time er 30 min kom porte chaye
                lr=(sub_avgTime-0.5)/sub_avgTime                #karon ami protibar bhalo number pele 1/2 hour kore komate chai
                current_lr=lr                                   #update korchi learning rate ta
        else:
        #forced_exam?
            Total_learning_Time=sub_avgTime-((obtained_marks/total_marks)*sub_avgTime)#jodi marks baaje paye oke aro porte bolbo subject ta based on the amount of marks
    return Total_learning_Time

import datetime
def dayName():
   current_date = datetime.datetime.now()

# Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
   day_of_week = current_date.weekday()

# Convert the numeric day of the week to a string
   days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   day_name = days_of_week[day_of_week]
   return day_name


   #sub_elapsedTime
   #current_lr
   #sub_avgTime
   #total_time
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
'''examFlag=False
    existingValue=0.0#eta 0 hobe naa, database theke fetch kora hobe, mane existingValues er value ta
    #avgTime=0#eta o database theke fetch kora hobe, ek ekta subject er average value
    requiredHours=0#etar value tao fetch korte hobe, initially 0 thakbe
    for i in feedback:
        for j in i:
            if j=="work":
                currentHours+=1
    currentHours=currentHours/2
    existingValue+=currentHours
    lr=currentHours/avgTime
    if requiredHours==0:
        requiredHours=avgTime
    else:
        requiredHours=requiredHours*lr#updated required hours store korte hobe database a'''
            
'''ekhane database er saathe integration er code thakbe, mane current hours database a store kora hobe existingValue er saathe
        add kore, so existing value neoa hobe, current values er saathe add kora hobe, database a existing value r column update kora
        hobe'''
        
'''import numpy as np

class QLearningAgent:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_prob=0.2):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob

        # Initialize Q-table with zeros
        self.q_table = np.zeros((num_states, num_actions))

    def select_action(self, state):
        # Exploration vs. Exploitation
        if np.random.rand() < self.exploration_prob:
            # Explore - choose a random action
            return np.random.randint(self.num_actions)
        else:
            # Exploit - choose the action with the highest Q-value for the current state
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state):
        # Q-value update using the Q-learning formula
        current_q = self.q_table[state, action]
        max_future_q = np.max(self.q_table[next_state, :])
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_future_q)
        self.q_table[state, action] = new_q

# Example usage:
num_states = 5  # Number of states representing different subjects
num_actions = 3  # Number of actions representing different study time adjustments

# Initialize Q-learning agent
q_learning_agent = QLearningAgent(num_states, num_actions)

# Simulate episodes of learning
num_episodes = 1000
for episode in range(num_episodes):
    # In a more realistic scenario, you would have the student study, take tests, and update the Q-table based on results.
    # For simplicity, I'm assuming a state-action space where states and actions are represented by integers.

    # Simulate the student choosing an action based on the current state
    current_state = np.random.randint(num_states)
    chosen_action = q_learning_agent.select_action(current_state)

    # Simulate receiving a reward and transitioning to the next state
    reward = simulate_test_performance(current_state, chosen_action)
    next_state = np.random.randint(num_states)

    # Update the Q-table based on the observed reward and transition
    q_learning_agent.update_q_table(current_state, chosen_action, reward, next_state)

# After training, the Q-table contains learned Q-values that can be used to make decisions.
'''