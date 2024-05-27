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

def updateValue(mode,tableName,value,column,id):
    if mode=='notQvalue':
        columnList=["MondayTimings","TuesdayTimings","WednesdayTimings","ThursdayTimings","FridayTimings","SaturdayTimings","SundayTimings"]
        if column not in columnList:
            db_cursor.execute(f"update {tableName} set {column} = {value} where id = {id}")
        else:
            currentVal=fetchOutput("notQvalue",tableName,id,column,False)
            updatedVal=currentVal+value  #add total timing of reading for a day
            db_cursor.execute(f"update {tableName} set {column} = {updatedVal} where id = {id}")
    elif mode=='Qvalue':
        for i in range (0,48):
            for j in range (0,3):
                element=value[i,j] # extraction of value of i,j th position
                print(element)
                columnList=["value1","value2","value3"]
                db_cursor.execute(f"UPDATE Qtable SET {columnList[j]} = {element} where id={i+1}")
    mydb.commit()


def updateWork_conc(work_conc):
    # Convert numpy array to a Python list
    for i in range(48):
        element = work_conc[i]
        query = "UPDATE work_concentration SET elements = %s WHERE id = %s"
        db_cursor.execute(query, (element, i))
    mydb.commit()

# for i in range(0,48):
#     n=0.0
#     db_cursor.execute(f"insert into work_concentration (elements,id) values({n},{i}) ")
# mydb.commit()

def fetchOutput(mode,tableName,idValue, columnName, multipleDays):
    if mode=='notQvalue': 
        elapsedTime=0
        if not multipleDays:
            db_cursor.execute(f"SELECT {columnName} FROM {tableName} where id={idValue}")
            fetchedOutput=db_cursor.fetchone()
            return fetchedOutput[0] 
        else:
            columnList=["MondayTimings","TuesdayTimings","WednesdayTimings","ThursdayTimings","FridayTimings","SaturdayTimings","SundayTimings"]
            for columnNameLoopVariable in columnList:
                db_cursor.execute(f"SELECT {columnNameLoopVariable} FROM {tableName} where id={idValue}")
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
        return (numpy_array)

def fetchWorkConcentration():
    query = "SELECT elements FROM work_concentration"
    db_cursor.execute(query)
    rows = db_cursor.fetchall()
    
    # Convert fetched rows into a list of floats
    work_conc_list = [float(row[0]) for row in rows]
    
    # Convert the list to a NumPy array
    work_conc_array = np.array(work_conc_list)
    
    return work_conc_array
    
    
# Fetch the row
# a=np.empty()
# a=np.array([ 10.  7. 18.  0.  0. 24.  7. 10. 20.  0. 10. 18.  8.  0. 16.  0.  0. 18. 10. 10.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.])
# a=[10.0, 7.0]
# updateWork_conc(a)
# print(a)
# Close the cursor and connection

# Convert the row into a numpy array

