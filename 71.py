#dir, __dict__ and help() methods in python
#they are used for object introspection meaning we use them to view what what are htere inside an unknown object

#x = [1, 2, 3]
#print(dir(x))

#print(x.__add__)

class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.version = 21

p = person("Harananda",77)
print(p.__dict__)						#this will print the attributes and parameter and its holders in the form of a dictionary

#print(help(str))						#this will print everything i need to know for the str method and we can do this for any method

print(help(person))						#this will print every information about the class 'person' so we can use this to ontrospec a class to know what is it we are using

