# Map, Filter and Reduce function in python 

def cube(d):
    return d*d*d
print(cube(56))

l=[1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))                     #for every item in l list it takes the element and return the cube of it and append it in the new list newl
# print(newl)

# instead of writing all the code above we can simply use the map function 

newl=list(map(cube,l))                              #the map function maps every element and apply the function on every element 
print(newl)                                         #the list function convert it into list as the map function only apply the parameters and so we can change it into any datatypes

# filter function 
# the filter function is use to filter out element

def filter_function(x):
    return x<4
newl2=list(filter(filter_function,l))                # this filter out all the number greater than 4 and only gives the smaller one
print(newl2)                                          #basically it filter out the elements according to the function provided

#when a function takes another function as an argument we called it as a higher order function
# so all the function map, filter and reduced are all higher order function 

from functools import reduce                        #reduce function needs to be imported from the functools modules
number=[1,2,3,4,5]

sum = reduce(lambda x,y:x+y,number)                 #calculate all the sum of the numbers using the reduce function
print(sum)


