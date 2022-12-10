import connector
import student as student_class

#connector.remove_student(500)

students = connector.getStudents()
newstudent = student_class.Student(10,"Ade","Le")

found_duplicate = False
for student in students:
    if student.studentId == newstudent.studentId:
        found_duplicate = True
        break

if not found_duplicate:
    connector.add_student(newstudent)
    students.append(newstudent)

for student in students:
    print("---------------")
    student.display_info()
    print("---------------\n")