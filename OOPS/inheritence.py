class Person:
    def __init__(self,name=None,id=None):
        self.name = name
        self.id = id

    def details(self):
        print(f"Welcome {self.name}! Your ID is {self.id}")

class Student(Person):
    def print_det(self):
        print("This is Student class")
        print(f"Student name is : {self.name} and ID is : {self.id}")

class Employee(Person):
    def show(self):
        print("This is Employee class") 
        print(f"Employee name is : {self.name} and ID is : {self.id}")


stud = Student("Sandy","23BCS075")
emp = Employee("Santhiya B","22EMP303")
stud.print_det()
stud.details()
emp.show()
emp.details()