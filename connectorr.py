import mysql.connector as myconn
mydb = myconn.connect(
    host="bzww6voywepttascpl44-mysql.services.clever-cloud.com",
    user="uf9srr9rwtttokwi",
    password="SLk5emfZrpnqSMwspuyU",
    database="bzww6voywepttascpl44")

db_cursor = mydb.cursor()
# db_cursor.execute("SELECT LR FROM subdata where Subjects='Array'")  # select Total Timing from subdata  (alter this while searchig for total time)

def fetchOutput(subjectName, columnName, multipleSubjects):
    elapsedTime=0
    if not multipleSubjects:
        db_cursor.execute("SELECT " + columnName+" FROM subdata where Subjects='"+subjectName+"'")
        fetchedOutput=db_cursor.fetchone()
        return fetchedOutput[0] 
    else:
        columnList=['MondayTimings','TuesdayTimings','WednesdayTimings','ThursdayTimings','FridayTimings','SaturdayTimings','SundayTimings']
        for i in range(0,6):
             db_cursor.execute("SELECT " + columnList[i]+" FROM subdata where Subjects='"+subjectName+"'")
             fetchedOutput=db_cursor.fetchone()
             elapsedTime+=fetchedOutput[0]