# Recursion in python 

def factorial(n):
    if (n==0 or n==1):
        return 1;
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(6))
print(factorial(0))

#Fuction to print the fibonacci sequence term

def fibonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
p=int(input("Enter the term upto which you want the fibonacci sequence: "))
for i in range(p):
    print(fibonaci(i),end=" ")
print(f"\nThe {p}th term of the fibonacci sequence is: ",fibonaci(i))
