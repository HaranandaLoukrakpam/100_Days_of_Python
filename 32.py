# set method in python 
s0={1,2,3,4,5,6,7,8,9}
s1={1,2,5,6}
s2={3,4,7,2,5,1}
print(s1.union(s2)) #union of two set

# s1.update(s2) #this updates the set s1 with the value of s2 and s1 is changed

print(s1,s2)

print(s1.intersection(s2))
print(s1.symmetric_difference(s2)) #prints the symmetric difference of the two set
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.isdisjoint(s2)) #checks if the two set is disjoint or not
print(s0.issuperset(s1))

# to add an element to a set we use the following function 
s1.add(9)
print(s1)

# to remove an element from the set we use the remove method 
s1.remove(1)
print(s1)

# we also sometimes want to use the discard function as it perfrm the same function as remove but doesn't throw error if the element isn't present 
s1.discard(45)
print(s1)

# the pop function remove a random element from the set 
print(s1.pop())

# del function is used to delete an entire set 
# del s2
# print (s2)

# to chech if an element is present in a set we use the same method as that we use in list 
if 5 in s1:
    print("Yes the element is present in s1")
else:
    print("The element is not present in the set")