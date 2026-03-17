#lambda function in python

# def double(x):
#     return x*2
# print(double(5))

# instead of writing the code like this we use the lambda function like 

double = lambda x: x*2                  #takes x as an input and return x*2 as the output
print(double(5))                        #incase there is a scenario where i have to make 3-4 small function we use the lambda function

cube = lambda x: x*x*x
print(cube(2))

average = lambda x,y,z: x+y+z/3         #we can also use mutliple variable with the lamda function
print(average(456,678,987))

def hara(fx,value):
    return 69 + fx(value)
print(hara(cube,2))                     # we can also pass a function as a function in python

print(lambda w:w*3)                     #lamda can also be use inside the print statement