# break and continue statement
# break statement allow us to skip a part of the code 
for i in range(11):
        if(i==10):
                break
        print("5x",i+1,"=",5*(i+1))

# continue statement means escape the iteration 
for p in range(12):
        if(p==10):
                print("This iteration will be skipped")
                continue
        print("5x",p+1,"=",5*(p+1))
