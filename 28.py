# f string in python 
# string formatting in python 
letter= "Hi, my name is {} and I'm from {}"
country="Manipur"
name="Harananda"
print(letter.format(name,country))

# new method of string formatting in python can be done in the following way 
print(f"Hey mu name is {name} and I'm from {country}.")

# for txt 
price=56.677895
txt=f"For only {price:.2f} dollars." #prints only upto 2 decimal points
print(txt)

