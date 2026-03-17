# File i/o in python 

# read mode only allows reading of the file only 

# f=open('test.txt', 'r')     #this read the file 
# print(f)                    #this prints the encoding and all the stuff

# text=f.read()               #read mode or 'r' mode is default in python
# print(text)                 #this prints the content of the file
# f.close()


# rd for binary mode

# write mode

f=open('test.txt','w')
f.write('hello,world')
f.close()

#used a in place of w to append to the text file
