#Method overriding  in python
''' method overiding is a powerful feature in OOP that allow us to redefined a method in a derived class
    the method in the derived class is said to override the method in the base class.
    when we create an instance of the derived class and call the overridden method the version of the method in the derived class is executed rather than the version in the base class
    '''

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius*3.14*self.radius             #return 3.12 * super().area()  what this does is call the area function inside this class

rect = shape(23, 120)
print(rect.area())

circ = circle(10)
print(circ.area())
