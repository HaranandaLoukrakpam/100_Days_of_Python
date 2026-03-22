#class methods in python

class Employee:                                                                 #creates a class name called Employee
    company = "Apple"                                                           #initialises a class variable with apple name
    def show(self):                                                             #A regular instance[object] method that prints the employee's name and company
        print(f"The name is {self.name} and the company is {self.company}")

    @classmethod                                                                #the classmethos decorator make it possible to change the value in the class instead of the object
    def changeCompany(cls, newCompany):
        cls.company = newCompany
e1=Employee()
e1.name= "Harananda"
e1.show()

e1.changeCompany("Anthropic")
e1.show()

print(Employee.company)