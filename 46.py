# os module in python 
# import os 

# can be used to create multiple folder and files 
# used to rename a large number of files and folders
# basically can be used to configure a large number of files & folders

#search up google for the different methods and attributes included in os module

import os

# 1. Get current working directory
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# 2. Create a new directory
new_folder = "test_folder"

if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"Folder '{new_folder}' created.")
else:
    print(f"Folder '{new_folder}' already exists.")

# 3. List files in current directory
print("\nFiles and folders in current directory:")
items = os.listdir(current_dir)
for item in items:
    print("-", item)

# 4. Create a file inside the new folder
file_path = os.path.join(new_folder, "sample.txt")
with open(file_path, "w") as file:
    file.write("Hello, this is a sample file.")

print(f"\nFile created at: {file_path}")

# 5. Remove the file
if os.path.exists(file_path):
    os.remove(file_path)
    print("File removed successfully.")
else:
    print("File does not exist.")