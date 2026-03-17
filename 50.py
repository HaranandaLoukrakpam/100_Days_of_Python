# read(),readlines() and other methods in python 

# f=open('test.txt','r')
# while True:
#     line=f.readline()               #reads the content of the file line by line
#     print(line)
#     if not line:                    #if the line or the content ends then it executes this program
#         print(line,type(line))
#         break

q=open('test1.txt','r')
i=0
while True:
    i=i+1
    line1=q.readline()
    if not line1:
        break
    m1=line1.split(",")[0]
    m2=line1.split(",")[1]
    m3=line1.split(",")[2]
    print(f"Marks of the student {i} in maths is {m1}")
    print(f"Marks of the student {i} in maths is {m2}")
    print(f"Marks of the student {i} in maths is {m3}")

    print(line1)