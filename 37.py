# finally cause in python 
def func1():
    try:
        l=[1,2,3,4,5]
        b=int(input("Enter the index of the number you want to  print: "))
        print(l[b])
        return 1
    except:
        print("Enter a valid index")
        return o
    finally:
        print(f"The index is of valid from {len(l)-1}")
x=func1()
print(x)