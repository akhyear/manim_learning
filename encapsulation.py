class Student:
    def __init__(self, name, id):
        self.name=name
        self.__id = id
    def details(self):
        print(f"Name: {self.name} and ID: {self.__id}")

rafin = Student("Rafin", 1999)
rafin.details()