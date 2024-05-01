import random
from datetime import date, timedelta
from connectorr import updateValue, fetchOutput
import numpy as np
def generatePopulation(days):
    day=[]
    hoursList=[]
    member={}
    for days in range (days):
        day.append(days)
        hour=random.randrange(5,100,5) 
        hoursList.append((hour/10))
    for key,value in zip(day,hoursList):
        member[key]=value
    return member
# def generate_dates(start_date, end_date):
#     dates=[]
#     current_date=start_date
#     while current_date<=end_date:
#         dates.append(current_date)
#         current_date+=timedelta(days=1)
#     print(dates)
# generate_dates(date(2024,3,12),date(2024,10,29))

def fitness_function(population,TimeSum,hday_list):
    score_multiplier = np.empty((len(population), 2), dtype=object)
    hday= list(hday_list.values())
    print(hday)
    # for member in population:
    #     memberTimeSum=0
    #     hour=[]
    #     for key in member.values():
    #         # hour=member.values()   
    #         hour.append(key)
    #     for items in hour:
    #         memberTimeSum+=items
    flag=0
    flag1=0
    score=0
    for index, member in enumerate(population):
        score=0
        member_values = list(member.values())
        memberTimeSum = sum(member.values())
        # print(f"this is the minimum amount of time required {TimeSum}")
        # print(f"this is the total amount of time of the population member: {memberTimeSum}")
        if memberTimeSum < TimeSum:
            multiplier = 0
        else:
            multiplier = 1
        for i in range(len(member_values)):
            current_value = member_values[i]
            
            current_hday = hday[i]
            print(current_hday)
            if i+1<=(len(member_values)-1):
                next_value = member_values[i + 1]
                # print(f"Current value: {current_value}, Next value: {next_value}")
                if current_value < 4 and next_value > 6:
                    score += 1
                    # print(f"since current value is {current_value} and next is {next_value} score gets incremented by 1 due to if condition")
                elif current_value > 6 and next_value < 4:
                    score += 1
                    # print(f"since current value is {current_value} and next is {next_value} score gets incremented by 1 due to elif condition")
                if current_hday==1 and current_value>6:
                    score +=1
                    # print(f"since current value is {current_value} and hday is {current_hday} score gets incremented by 1 due to 1st condition")
                elif current_hday==0 and current_value<=4:
                    score+=1
                    # print(f"since current value is {current_value} and hday is {current_hday} score gets incremented by 1 due to 2nd condition")
                if current_hday==0 and current_value>=6:
                    score-=1
                    # print(f"since current value is {current_value} and hday is {current_hday} score gets decremented by 1 due to 3rd condition")
        
        score=score*multiplier
        score_multiplier[index] = [member, score]
        print("abc")
    return score_multiplier

TimeSum=0
population=[]
population_number=8
days=6
# score_multiplier=np.empty((population_number,2),dtype=object)
for i in range(0,population_number):
    population.append(generatePopulation(days))
# print(population)
for i in range(1,5):
        lr=fetchOutput('notQvalue',i,'LR',False)
        TimeSum+=fetchOutput('notQvalue',i,'AvgTime',False)*lr

def driver_func(length):
    my_dict= dict([(i, random.randint(0,1)) for i in range(length)])
    return my_dict

hday_list=driver_func(days)
print(hday_list)
a=fitness_function(population,TimeSum,hday_list)
print(a)
    