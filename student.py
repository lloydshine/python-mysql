class Student:
    def __init__(self,studentId,firstname,lastname):
        self.studentId = studentId
        self.firstname = firstname
        self.lastname = lastname

    def display_info(self):
        print(f"Student ID: {self.studentId}\nFirstName: {self.firstname}\nLastName: {self.lastname}")

if __name__ == '__main__':
    print("Hello")