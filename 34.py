#Dictionary method in python
ep1={101: 11,102: 12,103: 13,104: 14,105: 15}
ep2={201: 21,202: 22,203: 23,204: 24,205: 25}

ep1.update(ep2) # basically puts the value of ep2 and updates it into the dictionary ep1

# ep1.clear() used to clear a dictionary

print(ep1)

# to create an empty dictioonary 
empt={}
print(type(empt))

ep1.pop(105) #when we want to pop out a specific element
ep1.popitem() #pops out the last element of the dictionary
print(ep1)

# to delete the entire dictionary we use the del method
#del ep1

# to delete a specific element in the dictionary 
del ep1[103]
print(ep1)