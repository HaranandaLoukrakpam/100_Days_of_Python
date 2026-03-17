# function argument in python 
def average(a=6,b=9):
    print("the average of a and b is:", (a+b)/2)
average(10,20)

# keyword arguments 
# required arguments 

def average1(*numbers):
    sum=0
    # print(type(numbers))
    for i in numbers:
        sum=sum+i
    print("Average1 is:", sum/len(numbers))
average1(1,1,1,1,1,1,1,1,1,1)

def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])
name(mname="Marshall",fname="Harananda",lname="Loukrakpam")