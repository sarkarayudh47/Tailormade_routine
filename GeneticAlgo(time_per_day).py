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

def fitness_function(population,TimeSum):
    score_multiplier = np.empty((len(population), 2), dtype=object)
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
        flag1=flag1%2
        member_values = list(member.values())
        memberTimeSum = sum(member.values())
        if memberTimeSum < TimeSum:
            multiplier = 0
        else:
            multiplier = 1
        if index < len(member_values) - 1:
            for value in member_values:
                if value > 6:
                    if member_values[index + 1] < 4:
                        score += 1
                    # elif member_values[index + 1] > 6:
                    #     score -= 1
                    else:
                        score = 0
        multiplier=score*multiplier
        score_multiplier[index] = [member, multiplier]  # Assign directly, no need for np.append()
    return score_multiplier

TimeSum=0
population=[]
population_number=8
days=4
# score_multiplier=np.empty((population_number,2),dtype=object)
for i in range(0,population_number):
    population.append(generatePopulation(days))
print(population)
for i in range(1,5):
        lr=fetchOutput('notQvalue',i,'LR',False)
        TimeSum+=fetchOutput('notQvalue',i,'AvgTime',False)*lr
        print(TimeSum)
a=fitness_function(population,TimeSum)
print(a)
