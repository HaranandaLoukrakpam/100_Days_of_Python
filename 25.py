# tuple methods in python 
# to make changes in a tuple we first have to make a copy list of the tuple and convert the list back into a tuple as tuple are not meant to be changed
countries = ("Spain", "Italy", "India", "England", "Germany")

temp = list(countries)

# add item
temp.append("Russia")

# remove item (removes item at index 3)
temp.pop(3)

# change item (replace index 2)
temp[2] = "Finland"

countries = tuple(temp)

print(countries)

# we can concatinate two tuples without changing them into list as the resultant is a tuple 
countries1 = ("Pakistan", "Afghanistan",
"Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# count method is use in tuple 
# index also work the same as in list 
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
print('Count of 3 in tuple1 is:', res)