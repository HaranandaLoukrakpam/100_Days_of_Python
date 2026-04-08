#shutil module in python

import shutil
import os

# Create a test directory and files for demonstration
os.makedirs("demo/source", exist_ok=True)
with open("demo/source/file1.txt", "w") as f:
    f.write("Hello, this is file1")

with open("demo/source/file2.txt", "w") as f:
    f.write("Hello, this is file2")


# 1. copy() → copies file content + permissions (not metadata like timestamps)
shutil.copy("demo/source/file1.txt", "demo/file1_copy.txt")  
# Copies file1.txt into demo directory


# 2. copy2() → copies file + metadata (timestamps etc.)
shutil.copy2("demo/source/file2.txt", "demo/file2_copy.txt")  
# More complete copy than copy()


# 3. copytree() → copies an entire directory recursively
shutil.copytree("demo/source", "demo/source_backup")  
# Creates a full duplicate of 'source' folder


# 4. move() → moves file or directory (can also rename)
shutil.move("demo/file1_copy.txt", "demo/moved_file1.txt")  
# Moves and renames file1_copy.txt


# 5. disk_usage() → returns total, used, and free disk space
usage = shutil.disk_usage("/")  
print("Disk usage:", usage)  
# Shows storage stats of root directory


# 6. make_archive() → creates archive (zip, tar, etc.)
shutil.make_archive("demo_archive", "zip", "demo/source")  
# Creates demo_archive.zip from source folder


# 7. unpack_archive() → extracts archive
shutil.unpack_archive("demo_archive.zip", "demo/extracted")  
# Extracts zip into 'extracted' folder


# 8. rmtree() → deletes a directory and all its contents
shutil.rmtree("demo/source_backup")  
# Removes the backup directory completely


# 9. which() → finds path of an executable
python_path = shutil.which("python")  
print("Python executable path:", python_path)  
# Useful for locating system commands


# Cleanup (optional)
# shutil.rmtree("demo")  # Uncomment to delete all demo files
