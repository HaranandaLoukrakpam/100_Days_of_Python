# list method in python 
l=[1,2,3,4,5,6,4,4,23,45,67]
print(l)

# append function 
p=l.append(6)
print(l)

# reverse function 
l.sort(reverse=True)
print(l)

# to know the index of the first occurence of an element 
print(l.index(4))

#to count the number of occurence of an element
print(l.count(4))

# copy function to copy a list 
m=l.copy()
print(m)

# to insert an element to a specific index in the list 
l.insert(4,677)
print(l)

# to insert elements at the end of the list we use the extend method
n=[900,456,332]
l.extend(n)
print(l)

# to concatinate 2 list into a new list we use '+' symbol 
o=l+m;
print(o)