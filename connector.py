import mysql.connector
import student

def connect():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="manhattan153",
        db="chula_schooldb"
    )
    return db

def getStudents():
    db = connect()
    students = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM student")
    for x in cursor:
        s = student.Student(x[0],x[1],x[2])
        students.append(s)
    db.disconnect()
    cursor.close()
    return students

def add_student(s):
    db = connect()
    cursor = db.cursor()
    student_data = (s.studentId,s.firstname,s.lastname)
    add = "INSERT INTO student (student_id,firstname,lastname) VALUES (%s,%s,%s)"
    cursor.execute(add,student_data)
    db.commit()
    db.disconnect()
    cursor.close()

def remove_student(ID):
    db = connect()
    cursor = db.cursor()
    remove = f"DELETE FROM student WHERE (student_id = {ID})"
    cursor.execute(remove)
    db.commit()
    db.disconnect()
    cursor.close()

if __name__ == '__main__':
    print("Hello")
