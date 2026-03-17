# 'is' vs '==' in python 
# 'is' compare the exact location of object in memory and '==' compare the values 

a = [1,2,34]
b = [1,2,34]

print(a is b)               #location of object in memory
print(a == b)               #compare the values

c= 56
d= 56                       #python will not allocate another memory location as the value are the same instead it will leverage the same memory location of the value so in this case a is b will be true


print(c is d)
print(c == d)