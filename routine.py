import numpy as np
def generate_timetable(Q, work_concentration,num_actions,num_time_slots):
    timetable = {}

    # Find peak concentration hour for each task
    peak_concentration_hours = {0: np.argmax(work_concentration)}
    print(f"Peak productivity times: {peak_concentration_hours}")
    for action in range(1, num_actions):
        # Find peak concentration hour for current action
        peak_concentration_hours[action] = np.argmax(Q[:, action])

    # Sort actions based on peak concentration hour
    sorted_actions = sorted(peak_concentration_hours.keys(), key=lambda x: peak_concentration_hours[x])

    for state in range(num_time_slots):
        # Determine action based on sorted peak concentration hours
        action = sorted_actions[state % num_actions]

        action_name = int_to_action(action)
        start_time = f"{state // 2:02d}:{(state % 2) * 30:02d}"
        end_state = (state + 1) % num_time_slots
        end_time = f"{end_state // 2:02d}:{(end_state % 2) * 30:02d}"
        timetable[f"{start_time}-{end_time}"] = action_name
   # print(timetable)
    return timetable
def int_to_action(enc_code):
  if enc_code == 0:
    return 'work'
  elif enc_code == 1:
    return 'break'
  else:
    return 'sleep'

