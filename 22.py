# List in python 
l=[3,5,6,"Harananda",True,8,9,10,22,34,56,78]
print(type(l))
print(l)
print(l[1])
print(l[3])
print(l[4])

# acessing elements in list 
# negative indexing 
print("Negative Indexing")
print(l[-3]) #negative indexing
print(l[len(l)-3]) #conversion of negative indexing into positive indexing

if 6 in l:
    print("Yes the specified element is in the list")
else:
    print("nope")

if "rananda" in "Harananda":
    print("Yes the specified element is in the list")
else:
    print("nope")

print(l)
print(l[1:])
print(l[1:-1])
print(l[1:4:2])

lst=[i*i for i in range(7)]
print(lst)