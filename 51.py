# seek(), tell() and other function 
# the "seek" and "tell" function are used to work to work with file object 

with open('test.txt','r') as f:     #text i/o wrapper
    print(type(f))

    print(f.tell())                 #tells where the reading starts
    
    f.seek(10)                      #move to the 10th byte of the file
    data=f.read(5)                  #read the next 5 byte of the file
    print(data)
    
