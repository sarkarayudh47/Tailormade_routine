import pandas as pd
from connectorr import fetchOutput
def learningRate(subject_name,obtained_marks,cutoff_marks,total_marks,first_exam,exam_flag): 
    current_lr= fetchOutput(subject_name, 'LR', False)
    sub_avgTime=fetchOutput(subject_name, 'AvgTime', False)
    sub_elapsedTime=fetchOutput(subject_name,'abc', True)
    Total_learning_Time=0.0
    if not exam_flag:                                           #jodi student exam na diye thake, tokhon jodi ei function ta call hoye tahole 'if' block ta call hobe, karon exam neoa hoye ni mane holo oke porte bola hocche, tar manei okei time recommend kora hocche 
        Total_learning_Time=current_lr*sub_avgTime  
        print("this is the total learning time "+ str(Total_learning_Time))#ekhane ami oke ekta total learning time recommend korchi based on average time and learning rate jeta kina initially 1
    elif exam_flag:                                             #exam niye marks peye gele ei block ta execute hobe
        if obtained_marks>cutoff_marks:                         #jodi student kore
            if not first_exam:                                  #ei jayega ta dekhche j ei current exam ta student er ei SUBJECT a first exam noy kina
                lr=sub_elapsedTime/sub_avgTime                  #eisob sub_elapsed, sub_avg etc pore fetch korte db theke sub name take use kore
                current_lr=(current_lr+lr)/2
                print("after atleast one attempt, learning rate is "+ str(current_lr))#etake store korte hobe
            else:                                               #jodi first exam hoye r bhalo marks paye tahole porer bar learning rate kichu ta komate chai jate next time oke average time er 30 min kom porte chaye
                lr=(sub_avgTime-0.5)/sub_avgTime                #karon ami protibar bhalo number pele 1/2 hour kore komate chai
                current_lr=lr  
                print("after First attempt success, learning rate is "+ str(current_lr))#update korchi learning rate ta
        else:
        #forced_exam?
            Total_learning_Time=sub_avgTime-((obtained_marks/total_marks)*sub_avgTime)#jodi marks baaje paye oke aro porte bolbo subject ta based on the amount of marks
            print("this is the additional learning time "+str(Total_learning_Time))
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
   
testOutput=learningRate("Queue",80,70,100,True,True)

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
