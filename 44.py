# how import works in python 

# import pandas as pd
# d = pd.read_excel(r"D:\semester 4\html and css\ADTU_0_2024_28_BCSM_013.xlsx")
# print(d)

# import math as m  
# p=m.sqrt(3.14)
# print(p)

# the "as" keyword is used to shortened the module name as we call it again and agin instead of typing the long module name again and again 

# from math import sqrt,pi
# q=pi
# p=sqrt(q)
# print(p,"\n",q)

# from math import*  #this imports all the function and variable in the module
# result=sqrt(256)*pi
# print(result)

# print(dir(math))

# to know all the function and variable in a module we use the directory function 

import pandas as pd

pd.set_option('display.max_rows', None) #helps display all the series instead of shortening it

d = dir(pd)
s = pd.Series(d)

print(s)

from module1 import jugali, po
jugali()
print(po)