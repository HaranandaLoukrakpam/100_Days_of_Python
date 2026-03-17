# Docstrings in python 
def square(n):
    '''Takes in a number n, and prints the square of the number n that is n^2'''
    print(n**2)
square(6)
print(square.__doc__)

# change in comments doesn't affect the output of the programme whereas change in docstring can affect the outcoome of the programme 
# docstrings are the ones written just below the def statement 
# otherwise the statement becomes a comment and doesn't print when we use the function __doc__ 
