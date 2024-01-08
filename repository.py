from domain import *

class Repostudents:
    def __init__(self):
        self.__students = []
        self.__filename = "Students.txt"

    def save_file(self):
        with open(self.__filename, "w") as f:
            for student in self.__students:
                f.write(student.__str__())

    def read_file(self):
        with open(self.__filename, "r") as f:
            for l in f:
                l = l.strip()
                if l == "":
                    continue
                id, name, attendance, grade = l.split(",")
                self.__students.append(Student(id, name, attendance, grade))
    def get_students(self):
        return self.__students
    def get_grade(self, student: Student):
        return student.get_grade()
    def create_student(self, id:int , name:str, att: int, grade:int):
        student = Student(id, name, att, grade)
        return student

    def add_student(self, id , name, att, grade):
        student = self.create_student(id , name, att, grade)
        self.__students.append(student)
        self.save_file()

    def give_bonus(self, p: int, b: int):
        for student in self.__students:
            if int(student.get_attendance()) >= p:
                if b + int(student.get_grade()) >= 10:
                    student.set_grade(10)
                else:
                    student.set_grade(b + int(student.get_grade()))
        self.save_file()