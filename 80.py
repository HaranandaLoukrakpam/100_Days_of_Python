#multilevel inheritance in python
'''it is a type of  inheritance in python where a derived class inherits from another derived class.
    this type  of inheritance allows you to build a heirarchy of classes whereone class build upon another, leading to a more specialised class.

    in python multilevel inheritance is achieved using the class heirarchy
    '''

class animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")
class dog(animal):
    def __init__(self, name , breed):
        animal.__init__(self,name, species = "dog")
        self.breed = breed

    def show_details(self):
        animal.show_details(self)
        print(f"breed: {self.breed}")

class goldenretriever(dog):
    def __init__(self,name,color):
        dog.__init__(self, name,breed ="husky")
        self.color = color
    def show_details(self):
        dog.show_details(self)
        print(f"color: {self.color}")

d = goldenretriever("Max","white")
d.show_details()


