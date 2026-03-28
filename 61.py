# Inheritance in Python 
# the types of inheritance in  python 
# single inheritance
# multiple imheritance
# multilevel inheritance
# heirarchial inheritance
# hybrid inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Show_Details(self):
        print(f"The name of the employee is: {self.name} is {self.id}")

class Programmer(Employee):
    def Showlanguage(self):
        print("The default language is python")

e = Employee("Harananda Loukrakpam", 69)
e.Show_Details()
        
e2 = Employee("Marshall Loukrakpam", 78)
e2.Show_Details()

e3 = Programmer("Alexander",90)
e3.Showlanguage()
        