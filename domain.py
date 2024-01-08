class Student:
    def __init__(self, id: int, name: str, attendance: int, grade:int):
        self.__id = id
        self.__name = name
        self.__attendance = attendance
        self.__grade = grade

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_attendance(self):
        return self.__attendance

    def get_grade(self):
        return self.__grade

    def set_attendance(self, new):
        self.__attendance = new

    def set_grade(self, new):
        self.__grade = new

    def __str__(self):
        return str(self.__id) + "," + str(self.__name) + "," + str(self.__attendance) + "," + str(self.__grade) + "\n"