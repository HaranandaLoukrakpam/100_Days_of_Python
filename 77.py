#operator overloading in python
'''Operator overloading is a feature in python that allows developers to redfine the behavior of mathematical and comparision operators for custom data-types
    This means we can use the standard mathematicl operatorss and comparision operators in your own class, just as we would for build in data-types like int, float and atr
    '''
class vector:                                       #create a class vector
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, x):
        #return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"                  #this will print the sum but not in the vector data-types
        return vector(self.i + x.i, self.j + x.j, self.k + x.k)
        
v = vector(5,6,7)
print(v)

v1 = vector(90,83,76)
print(v1)

print(v+v1)                                         #this will print the str type not vector/if i use the current one in the return it will print in the vector data-types
print(type(v+v1))








