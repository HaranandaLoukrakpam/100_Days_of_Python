# Constructors in python 
# Constructor helps in makinng an object by helping in initialization

# class Person:
#     name="Harananda Loukrakpam"
#     occupation = "AI Engineer"

#     def info(self):
#         print(f"Hi, my name is {self.name} and I'm an {self.occupation}")

# a=Person()
# print(a.name)
# a.name="Alexander"
# a.occupation="Data-Scientist"
# a.info()


class Person:
    def __init__(self, name, occupation):                                                     #this methos is called every time the function 'Person' is being called
        print("Hey I'm a Software Engineer")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"Hi, my name is {self.name} and I'm an {self.occupation}")

a=Person("Marshall", "Web-developer")
b = Person("Sundays","Full satck developer")
# print(a.name)
# a.name="Alexander"
# a.occupation="Data-Scientist"
# a.info()

a.info()
b.info()