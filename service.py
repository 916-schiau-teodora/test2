from repository import Repostudents

class Validate:
    def __init__(self):
        pass
    def validate_name(self, name: str):
        errors = ""
        if " " not in name:
            errors += "invalid name!"
        else:
            first_name, last_name = name.split(" ")
            if len(first_name) < 3 or len(last_name) < 3:
                errors += "invalid name!"
        if len (errors)  >0:
            raise ValueError(errors)

    def validate_att(self, att:str):
        errors = ""
        if  not att.isnumeric():
            errors += "Attendance must me a number!"
        else:
            if int(att) < 0 :
                errors += "invalid attendance!"
        if len (errors)  >0:
            raise ValueError(errors)

    def validate_grade(self, grade: str):
        errors = ""
        if not grade.isnumeric():
            errors += "Grade must me a number!"
        else:
            if int(grade) < 0 or int(grade)> 10:
                errors += "invalid grade!"
        if len(errors) > 0:
            raise ValueError(errors)
class Servicestudents:
    def __init__(self, studentsRepo : Repostudents):
        self.__students = studentsRepo
        self.__validator = Validate()
    def get_students(self):
        return self.__students.get_students()
    def add_student(self, id:str , name:str, att:str, grade:str):
        self.__validator.validate_name(name)
        self.__validator.validate_att(att)
        self.__validator.validate_grade(grade)
        self.__students.add_student(int(id), name, int(att), int(grade))

    def next_id(self):
        new = int(self.__students.get_students()[len(self.__students.get_students())-1].get_id())+1
        return new

    def sort(self):
        students_list = sorted(self.__students.get_students(), key = lambda student: (-(int(student.get_grade())), student.get_name()))
        return students_list

    def give_bonus(self, p:int, b:int):
        self.__students.give_bonus(p, b)
    def search(self, name):
        studentlist = []
        for student in self.__students.get_students():
            if name.lower() in student.get_name().lower():
                studentlist.append(student)
        studentlist = sorted(studentlist, key=lambda student: student.get_name())
        return studentlist