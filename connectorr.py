import mysql.connector as myconn
import numpy as np


mydb = myconn.connect(
    host="bzww6voywepttascpl44-mysql.services.clever-cloud.com",
    user="uf9srr9rwtttokwi",
    password="SLk5emfZrpnqSMwspuyU",
    database="bzww6voywepttascpl44")

db_cursor = mydb.cursor()
mydb.autocommit=True
# val=0.78
# strval=str(val)
# val_one=f"update subdata set LR={strval} where id=3"
# db_cursor.execute(val_one)  # select Total Timing from subdata  (alter this while searchig for total time)

def updateValue(mode,value,column,id):
    if mode=='notQvalue':
        columnList=["MondayTimings","TuesdayTimings","WednesdayTimings","ThursdayTimings","FridayTimings","SaturdayTimings","SundayTimings"]
        if column not in columnList:
            db_cursor.execute(f"update subdata set {column} = {value} where id = {id}")
        else:
            currentVal=fetchOutput(id,column,False)
            updatedVal=currentVal+value
            db_cursor.execute(f"update subdata set {column} = {updatedVal} where id = {id}")
    elif mode=='Qvalue':
        for i in range (0,48):
            for j in range (0,3):
                element=value[i,j]
                print(element)
                columnList=["value1","value2","value3"]
                db_cursor.execute(f"UPDATE Qtable SET {columnList[j]} = {element} where id={i+1}")
    mydb.commit()

def fetchOutput(mode,idValue, columnName, multipleSubjects):
    if mode=='notQvalue': 
        elapsedTime=0
        if not multipleSubjects:
            db_cursor.execute(f"SELECT {columnName} FROM subdata where id={idValue}")
            fetchedOutput=db_cursor.fetchone()
            return fetchedOutput[0] 
        else:
            columnList=["MondayTimings","TuesdayTimings","WednesdayTimings","ThursdayTimings","FridayTimings","SaturdayTimings","SundayTimings"]
            for columnNameLoopVariable in columnList:
                db_cursor.execute(f"SELECT {columnNameLoopVariable} FROM subdata where id={idValue}")
                fetchedOutput=db_cursor.fetchone()
                elapsedTime+=fetchedOutput[0]
        return elapsedTime
    elif mode=='Qvalue':
        query = "SELECT value1, value2, value3 FROM Qtable"
        db_cursor.execute(query)
        rows = db_cursor.fetchall()
        # numeric_row = [float(value) for value in row]  # Convert each value to float
        numeric_rows = [[float(value) for value in row] for row in rows] 
        numpy_array = np.array(numeric_rows)
        print(numpy_array)

# Fetch the row

#fetchOutput('notQvalue',None,None,None)
# Close the cursor and connection

# Convert the row into a numpy array

