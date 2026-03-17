# Virtual environment in python 
'''A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple 
projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have 
conflicting package versions or packages that are not compatible with each other.'''

# python -m venv % python3 -m venv myenv 
# to create a virtual envionment 'myenv' is the directory name

# # .\myenv\Scripts\Activate.ps1 
# to activate the virtual environment of pyhton in window, different for mac and linux user
 
import pandas as pd
l=[4,5,6,7,8,89]
lo=pd.Series(l)
print(lo)

# requirement.txt file in virtual environment
# to print out all the module and packages in the python virtual environment we used the following command line 
# pip3 freeze > requirements.txt 


