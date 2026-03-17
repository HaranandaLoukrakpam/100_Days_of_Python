# local vs globla variable in python 
# WHEN DO WE USE THE GLOBAL VARIABLE 

# x=69                                          #Global variable

# def lera():
#     x=5                                       #local variabe 
#     print(f"The local variable is {x}")
#     print("I am jobless")

# lera()
# print(f"The Global variable is {x}")

# now the question is how do we make the local variable inside the function into a global variable 

x=10            #global variable

def hara():     
    global y
    y=12        #local variable
    print(y)

hara()
print(x)
print(y)        #this will cause an error cause y is a local variable and is not accessible outside the function