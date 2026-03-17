# classes and object in python 
class person:                                           # defines a class name person
    name = "Harananda"
    occupation = "College-Student" 
    networth = 20

    def info(self):                                     #self parameter is a reference to the current instance of the class and is use to access to the variables inside the class
        print(f"{self.name} is a {self.occupation}")

a = person()
a.name = "Alexander"                                    #used the person class to create an object with the same argument using different parameter               
a.occupation= "Data-Scientist"  

b = person()
b.name = "Marshall"
b.occupation = "AI-Engineer"

print(a)                                                #prints the memory location
print(a.name, a.occupation)                             #prints the object name ans occupation
a.info()                                                #prints the function 'info' with the object name and occupation

print(b.name,b.occupation)                              # the self keyword calls the parameters of the object
b.info()