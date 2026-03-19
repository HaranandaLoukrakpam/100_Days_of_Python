#Static methods in Python
#Static methods are used when the instance of the class isn't required

class Math:
	def __init__(self,num):
		self.num = num

	def addtonum(self,n):
		self.num = self.num + n
	
	@staticmethod
	def add(a,b):
		return a+b

result = Math.add(45,56)
print("The result of this should be 101:",result)

a = Math(5)
print("The result of this should be 5:", a.num)

a.addtonum(6)
print("The output of this should be 11:",a.num)
