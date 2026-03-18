# Access modifiers in python 
# public,private and protected exist and doesn't exist in the same way in python
# by default all the class and methods and variable in python are public 

# for private
# we use __ before the name of the class or variable we want to make private 
# weak internal use variable 

class employee:
    def __init__(self):
        self.__name ="Harananda"

a = employee()
# print(a.__name)                               #this will show error as the variable is make private 
print(a._employee__name)                        #this will print the variable use this if we want to access a weak private access 
                                                #can be accessed indirectly so as to say
# Name mangling in python 

print(a.__dir__())