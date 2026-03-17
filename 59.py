# Decorators in python
# decorators in python are used to modify a function

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():                                        #decorated function
    print("Hello world")

def add(a, b):
    print(a + b)

# Calling the decorated function
hello()
greet(add)(8,9)

# Note: If you want to use @greet with add(a, b), 
# you'll need to update mfx to accept *args and **kwargs!