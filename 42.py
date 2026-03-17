# enumerate function in python 
marks=[12,56,32,98,12,45,1,4]
# print(type(marks))
# print(marks.index(98))
# index=0
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("the index has reached three")
#     index +=1

# to use the enumerate function in python to make the above loops more easy 

for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("the index has reached three")
    index +=1