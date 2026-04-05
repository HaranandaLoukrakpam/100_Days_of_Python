#Time module in python

import time
print(time.time())          #returns the current time in seconds since the Epoch.Fractions present if the system clock provides them

a = int(input("enter a number: "))
b = int(input("enter a number: "))

init = time.time()
print("the sum of the two number is: ", a+b)
print(time.time()-init)     #prints the time require to perfron the above function

print(3)
time.sleep(1)               #will delay the function to a specified time
print(2)
time.sleep(1)
print(1)

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)                  #will allow us to format the time layout so as to say
print("The time now is: "formatted_time)
