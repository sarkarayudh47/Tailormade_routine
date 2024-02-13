import mysql.connector as myconn
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

def updateValue(value,column,id):
    columnList=["MondayTimings","TuesdayTimings","WednesdayTimings","ThursdayTimings","FridayTimings","SaturdayTimings","SundayTimings"]
    if column not in columnList:
        db_cursor.execute(f"update subdata set {column} = {value} where id = {id}")
    else:
        currentVal=fetchOutput(id,column,False)
        updatedVal=currentVal+value
        db_cursor.execute(f"update subdata set {column} = {updatedVal} where id = {id}")
    mydb.commit()

def fetchOutput(idValue, columnName, multipleSubjects):
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
# updateValue(1,"LR",3)
# def storeOutput(subjectName, columnName, value):
#     columnList=["MondayTimings","TuesdayTimings","WednesdayTimings","ThursdayTimings","FridayTimings","SaturdayTimings","SundayTimings"]
#     if columnName not in columnList:
#         print("f")
