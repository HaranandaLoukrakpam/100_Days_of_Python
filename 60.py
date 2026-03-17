# Getters and setters in python 
# we use this to use the return value of a function as a object properties 
# In Python, a getter and setter are methods used to access and update the attributes of a class. These methods provide a way to define controlled access to the attributes of an object, thereby ensuring the integrity of the data. By default, attributes in Python can be accessed directly. However, this can pose problems when attributes need validation or transformation before being assigned or retrieved.

# Getter: The getter method is used to retrieve the value of a private attribute. It allows controlled access to the attribute.
# Setter: The setter method is used to set or modify the value of a private attribute. It allows you to control how the value is updated, enabling validation or modification of the data before it’s actually assigned.

class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# function to get value of _age 
	def get_age(self): 
		print("getter method called") 
		return self._age 
	
	# function to set value of _age 
	def set_age(self, a): 
		print("setter method called") 
		self._age = a 

	# function to delete _age attribute 
	def del_age(self): 
		del self._age 
	
	age = property(get_age, set_age, del_age) 

mark = Geeks() 

mark.age = 10

print(mark.age)

# class Geeks: 
# 	def __init__(self): 
# 		self._age = 0
	
# 	# using property decorator 
# 	# a getter function 
# 	@property
# 	def age(self): 
# 		print("getter method called") 
# 		return self._age 
	
# 	# a setter function 
# 	@age.setter 
# 	def age(self, a): 
# 		if(a < 18): 
# 			raise ValueError("Sorry you age is below eligibility criteria") 
# 		print("setter method called") 
# 		self._age = a 

# mark = Geeks() 

# mark.age = 19

# print(mark.age)