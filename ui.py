from repository import Repostudents
from service import Servicestudents


class UI:
    def __init__(self, serviceStudents: Servicestudents):
        self.__students = serviceStudents

    @staticmethod
    def menu():
        print("Press 1 to display all students:")
        print("Press 2 add a student:")
        print("Press 3 to display all students in decreasing order of their grades:")
        print("Press 4 to give a bonus:")
        print("Press 5 to display students with a given string:")
        print("Press 6 to exit:")

    def start(self):
        running = True
        try:
            while running:
                self.menu()
                option = str(input("->"))
                if option == "1":
                   for student in self.__students.get_students():
                       print(student)
                elif option == "2":
                    id = self.__students.next_id()
                    name = str(input("Name:"))
                    att = str(input("Attendance:"))
                    grade = str(input("Grade:"))
                    self.__students.add_student(str(id), name, att, grade)
                    print("Operation done successfully!")
                elif option == "3":
                    studentslist = self.__students.sort()
                    for student in studentslist:
                        print(student)
                elif option == "4":
                    p = int(input("p attendance:"))
                    b = int(input("bonus:"))
                    self.__students.give_bonus(p,b)
                elif option == "5":
                    name = str(input("name:"))
                    students = self.__students.search(name)
                    for student in students:
                        print(student)
                elif option == "6":
                    running = False
                else:
                    print("Invalid input! Please try again!")
        except Exception as ex:
            print(ex)


def main():
    studentsrepo = Repostudents()
    studentsrepo.read_file()
    servicestudents = Servicestudents(studentsrepo)
    ui = UI(servicestudents)
    ui.start()

main()

