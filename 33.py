# # Dictionaries in python 
# dict={
#     "Harananda": "Human Being",
#     "Guitar": "Instrument"
#     }
# print(dict)
# print(type(dict))
# print(dict["Harananda"])

# # mapping an integer to a string value in python 
# dict1={
#     1:"Harananda", #1,2,3 is the key and Harananda, Alexander, Marshall are the value of the key
#     2:"Alexander",
#     3:"Marshall"
# }
# print(dict1[1])
# print(dict.get("Harananda")) # used when we don't want the code to throw error anddisplay 'None' if the key or value i not present in the dictionary
# print(dict1.get(1))

# print(dict("Harananda")) #used when we want the code to throw error if the key or value isn't present in the dictionary

blah={31:"alex",
      32:"maya",
      33:"jiten"}
print(blah)
print(blah.keys())

for key in blah.keys():
    print(blah[key])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
