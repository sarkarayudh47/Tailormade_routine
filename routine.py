import numpy as np
from connectorr import updateValue, fetchOutput, updateWork_conc, fetchWorkConcentration

# def refineOne(Q, timetable, selected_indices, continous_limit, work_limit):
#     slots_alloted=len(selected_indices)
#     slot_limit=work_limit*2
    #   keys_list = list(timetable.keys())
#     currentWork=0
#     flag=0
#     for slot in selected_indices:
#         for i in range (continous_limit):
#             # if currentWork<=work_limit*2:
#             #     timetable[keys_list[(slot+i)%48]]='work'
#             # else:
#             #     flag=1
#             #     break
#             if i%2==0:
#                 i_updated=i+1
#             else:
#                 i_updated=-1*(i+1)
#             if currentWork<=work_limit*2:
#                 timetable[keys_list[(slot+i_updated)%48]]='worrk'
#             else:
#                 flag=1
#         if flag==1:
#             break
#     return timetable
keyToSlot={
"00:00-00:30": "0",
"00:30-01:00": "1",
"01:00-01:30": "2",
"01:30-02:00": "3",
"02:00-02:30": "4",
"02:30-03:00": "5",
"03:00-03:30": "6",
"03:30-04:00": "7",
"04:00-04:30": "8",
"04:30-05:00": "9",
"05:00-05:30": "10",
"05:30-06:00": "11",
"06:00-06:30": "12",
"06:30-07:00": "13",
"07:00-07:30": "14",
"07:30-08:00": "15",
"08:00-08:30": "16",
"08:30-09:00": "17",
"09:00-09:30": "18",
"09:30-10:00": "19",
"10:00-10:30": "20",
"10:30-11:00": "21",
"11:00-11:30": "22",
"11:30-12:00": "23",
"12:00-12:30": "24",
"12:30-13:00": "25",
"13:00-13:30": "26",
"13:30-14:00": "27",
"14:00-14:30": "28",
"14:30-15:00": "29",
"15:00-15:30": "30",
"15:30-16:00": "31",
"16:00-16:30": "32",
"16:30-17:00": "33",
"17:00-17:30": "34",
"17:30-18:00": "35",
"18:00-18:30": "36",
"18:30-19:00": "37",
"19:00-19:30": "38",
"19:30-20:00": "39",
"20:00-20:30": "40",
"20:30-21:00": "41",
"21:00-21:30": "42",
"21:30-22:00": "43",
"22:00-22:30": "44",
"22:30-23:00": "45",
"23:00-23:30": "46",
"23:30-00:00": "47"}
slotToKey={
     0:"00:00-00:30",
 1:"00:30-01:00",
 2:"01:00-01:30",
 3:"01:30-02:00",
 4:"02:00-02:30",
 5:"02:30-03:00",
 6:"03:00-03:30",
 7:"03:30-04:00",
 8:"04:00-04:30",
 9:"04:30-05:00",
 10:"05:00-05:30",
 11:"05:30-06:00",
 12:"06:00-06:30",
 13:"06:30-07:00",
 14:"07:00-07:30",
 15:"07:30-08:00",
 16:"08:00-08:30",
 17:"08:30-09:00",
 18:"09:00-09:30",
 19:"09:30-10:00",
 20:"10:00-10:30",
 21:"10:30-11:00",
 22:"11:00-11:30",
 23:"11:30-12:00",
 24:"12:00-12:30",
 25:"12:30-13:00",
 26:"13:00-13:30",
 27:"13:30-14:00",
 28:"14:00-14:30",
 29:"14:30-15:00",
 30:"15:00-15:30",
 31:"15:30-16:00",
 32:"16:00-16:30",
 33:"16:30-17:00",
 34:"17:00-17:30",
 35:"17:30-18:00",
 36:"18:00-18:30",
 37:"18:30-19:00",
 38:"19:00-19:30",
 39:"19:30-20:00",
 40:"20:00-20:30",
 41:"20:30-21:00",
 42:"21:00-21:30",
 43:"21:30-22:00",
 44:"22:00-22:30",
 45:"22:30-23:00",
 46:"23:00-23:30",
 47:"23:30-00:00"
}
def generate_timetable(Q, continous_limit, work_limit):
    
    timetable = {}
    work_action_index=0
    work_column = Q[:, work_action_index]
    # print(f"work_column is: \n{work_column}")
    sorted_indices = np.argsort(work_column)[::-1]
    sorted_indices = [20, 34, 44, 8, 25, 23, 19, 14, 12, 3, 28, 7, 40, 47, 9, 18, 41, 6, 4, 13, 16, 38, 2, 32, 36, 26, 11, 0, 35, 1, 30, 5, 43, 10, 45, 21, 42, 27, 31, 15, 22, 37, 33, 46, 24, 39, 29, 17]
    # print(f"sorted_indices are \n{sorted_indices}")
    # sorted_indices=np.zeros()
    # sorted_indices[10]
    # print(f"sorted index is: \n{sorted_indices}")
    for state in sorted_indices:
        if slotToKey[state] in timetable.keys():
            continue
        continous_limit=continous_limit if continous_limit<work_limit else work_limit
        # start_time = f"{state // 2:02d}:{(state % 2) * 30:02d}"
        # end_state = (state + 1) % 48
        # end_time = f"{end_state // 2:02d}:{(end_state % 2) * 30:02d}"
        slot=0
        flag=0
        num_to_convert = (continous_limit - 1) // 2
        additional = (continous_limit - 1) % 2
        start = max(state - num_to_convert, 0)
        end = min(state + num_to_convert + additional, 48)
        # print(start," ",end)
        for i in range(start, end+1):
            if slotToKey[i] not in timetable.keys():
                if slotToKey[(i+1)%48] in timetable.keys() and timetable[slotToKey[(i+1)%48]] != 'work':
                    timetable[slotToKey[i]] = 'work' 
                    work_limit-=1     
                    flag=1
                elif slotToKey[(i+1)%48] not in timetable.keys():
                    timetable[slotToKey[i]] = 'work' 
                    work_limit-=1     
                    flag=1
                else:
                    timetable[slotToKey[i]] = 'break'
            else:
                print(timetable[slotToKey[i]])
        if flag==0:
            timetable[slotToKey[state]] = "break"
    # t=refineOne(Q, timetable, selected_indices, continous_limit, work_limit)
    t=timetable
    return t

    
Q = fetchOutput('Qvalue',None,None,None)
t=generate_timetable(Q,3,6)

# for slot, task in t.items():
#         print(f"{slot}: {task}{keyToSlot[slot]}")
for key in slotToKey:
    if key>14:
        print(f"{slotToKey[key]}: {t[slotToKey[key]]}")
    else:
        print(f"{slotToKey[key]}: sleep")
        