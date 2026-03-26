#Super keyword in python
'''The super() keyword in python is used to referred to the parent class
    it is useful when a child inherits from multiple parents and we want to call a method from one of the class
    When a class inherit from a parent class it can override or extend the method in the parent class

'''

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class programmer:
    def __init__(self, name, id, lang):
        self.name = name
        self.id = id
        self.lang = lang

class ParentClass:
    def parent_method(self):
        print("This is the parent method")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harananda")
        super().parent_method()

    def child_method(self):
        print("This is the child method")

        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

Brajalen = Employee("Brajalen", "Broken Playboy 69")
Yoihenba = programmer("Yoihenba", "Anime Loverboi", "Japanese")

print(Brajalen.name)

print(Brajalen.name)
print(Brajalen.id)
print(Yoihenba.name)
print(Yoihenba.id)
print(Yoihenba.lang)

