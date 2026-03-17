# how to throw custom error in python 
a=int(input("Enter value between 11 and 20: "))
if (a<11 or a>20):
    raise ValueError("Value should be between 11 and 20")
