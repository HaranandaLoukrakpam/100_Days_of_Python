# error handling in python using try except method 
try:
    a=int(input("Enter a number to print the multiplication table: "))
    print(f"The multiplication table for {a} is as follows: ")
    for i in range(1,11):
        print(f"{a}x{i}={a*i}")
except:
    print("Please enter a valid number")
print("End of code")

# now the above code will run fine as long as the input is an integer but if the user enter another datatype say a character then python would throw 
# an error in which case we would need an error handling.
