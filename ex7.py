#Write a python program to clear the clutter inside a folder in our computer
''' To use the OS module to rename all the png image from 1.png all the way to n.png.
	And do the same for all the other files other than png.
	'''
import os

folder = "file path"						#reads the file path and access it using the os module
file_list = os.listdir(folder)				#reads all the files types and store it in a list in file_list like file_list = [hara.png, kok.txt, project.py, bull.jpg]

png_count = 1								#initialises the name of the png to 1 to start from 1.png, 2.png .... n.png
other_file_count = 1						#does the same initialisation for other files

for file in file_list:						#loops through every filename one by one
	old_path = os.path.join(folder, file)	#build the full path of the full file by combining the folder path and the file name

	if file.endswith(".png"):				#checks if the file name ends with .png
		new_name = str(png_count) + ".png"	#creates the new name by combining the the counter + ".png"
		png_count += 1
	else:
		ext = os.path.splitext(file)[1]		#for other files other than the .png files split the file name into two parts, the ext hold the extension of the file
		new_name = str(other_count) + ext	#creates a new name using the counter and the ext files
		other_count += 1

	new_path = os.path.join(folder, new_name)#builds a full path for the new name
	os.rename(old_path, new_path)			#takes the old path and rename it to new path

print("done")								#prints done for confirmation
