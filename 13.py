# string methods
# strings are immutable
a="Harananda is Harananda even if he wants to be harananda "
print(a)
print(a.upper()) #new string which gives the original string in upppercase
print(a.lower())

# rstrip function removes the trailing charracter in a string 
# doesn't skip leading ones only the trailing ones 
b="harananda !!!!!!!!"
print(b.rstrip("!"))

# repalce function allows you to replace a specific word in the string with the desired one
print(a.replace("Harananda","Alexander"))

# split function converts the string into a list 
print(a.split(" "))

# capitalise function convets the first letter of the string into a capital letter and turns all the other into lowercase 
print(b.capitalize())

# centre function is used to centre the strings
print(len(b.center(50)))
print(b.center(50))

# count function allow us to cound the number of a specific word in the string 
print(a.count("Harananda"))

# endswith() function can check if the string end with specific character and can even check in between 
print(b.endswith("ra",2,4))

# find function is used to search for the first occurence of a specific character and return the index of the character 
print(a.find("if"))

#index function, isalnum function,isalpha() function 