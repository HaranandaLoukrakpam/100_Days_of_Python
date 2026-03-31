#Single inheritance in python
'''Single inheritance is a type of inheritance where a class inherites the properties and behaviour from a single parent class.
    This is the single and most common form of inheritance
    '''

class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by an animal")

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species = "Husky")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

class cat(animal):                                              #cat class as the quiz exercise
    def __init__(self, name, breed):
        animal. __init__(self, name, species = "Persian")
        self.breed = breed

    def make_sound(self):
        print("meow!")


d = dog("Max", "Husky")                     #calls the dog class
d.make_sound()

a = animal("Dog", "Alaskan")                #calls the animal class
a.make_sound()

c = cat("khalid kashmiri", "persian")       #calls the cat class
c.make_sound()


