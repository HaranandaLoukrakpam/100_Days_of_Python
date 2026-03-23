#Class methods as alternative constructors in python

class employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	@classmethod
	def fromStr(cls, string):
		return cls(string.split("-")[0], string.split("-")[1])

e = employee("Harananda", 3000000)
print(e.name)
print(e.salary)

string = "Alexander-2900000"
e2 = employee.fromStr(string)
print(e2.name)
print(e2.salary)
