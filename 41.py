# short hand if else statement in python 
num1=float(input("Enter a number: "))
num2=float(input("Enter another number to compare to the first nummber: "))

print("The number is")
print("num1") if num1>num2 else print ("=") if num1==num2 else print("num2") 

a= "num1 is greater" if num1>num2 else "I don't kow check youself"
print(a)