#Magic/Dunder methods in python
'''These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.
They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

__init__ method
The init method is a special method that is automatically invoked when you create a new instance of a class.
This method is responsible for setting up the object's initial state, and it is where you would typically define any instance variables that you need. 

__str__ and __repr__ methods
The str and repr methods are both used to convert an object to a string representation.
The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.
'''
class MyNumber:
    def __init__(self, value):
        self.value = value

    # String / Representation
    def __str__(self):
        return f"MyNumber({self.value})"

    def __repr__(self):
        return f"MyNumber({self.value})"

    # Arithmetic operators
    def __add__(self, other):
        return MyNumber(self.value + other.value)

    def __sub__(self, other):
        return MyNumber(self.value - other.value)

    def __mul__(self, other):
        return MyNumber(self.value * other.value)

    def __truediv__(self, other):
        return MyNumber(self.value / other.value)

    def __floordiv__(self, other):
        return MyNumber(self.value // other.value)

    def __mod__(self, other):
        return MyNumber(self.value % other.value)

    def __pow__(self, other):
        return MyNumber(self.value ** other.value)

    # Reverse operators
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return MyNumber(other.value - self.value)

    # Comparison operators
    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    # Unary operators
    def __neg__(self):
        return MyNumber(-self.value)

    def __pos__(self):
        return MyNumber(+self.value)

    def __abs__(self):
        return MyNumber(abs(self.value))

    # Type conversion
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    # Container-like behavior
    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, key):
        return str(self.value)[key]

    def __setitem__(self, key, value):
        temp = list(str(self.value))
        temp[key] = str(value)
        self.value = int("".join(temp))

    # Callable object
    def __call__(self):
        return f"Called with value {self.value}"

    # Context manager
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

    # Iterator
    def __iter__(self):
        self._index = 0
        self._digits = str(self.value)
        return self

    def __next__(self):
        if self._index < len(self._digits):
            result = self._digits[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


# Example usage
a = MyNumber(123)
b = MyNumber(10)

print(a + b)          # Arithmetic
print(a - b)
print(a * b)

print(a == b)         # Comparison
print(a > b)

print(len(a))         # Container behavior
print(a[1])

a[1] = 9
print(a)

print(int(a), float(a))  # Conversion

print(a())           # Callable

# Iteration
for digit in a:
    print(digit)

# Context manager
with MyNumber(50) as x:
    print(x)
