#Use the pypdf library in python to merge multiple pdf files
'''
from pypdf import PdfWriter as pw

merger = pw()
for pdf in ["sample.pdf", "sample1.pdf", "sample2.pdf"]:
    merger.append(pdf)
merger.write("Merged_pdf.pdf")
'''
#the above is a draft written using the documentation 

from pypdf import PdfWriter as pw
writer = pw()                   #creates a new empty pdf container in the memory

pdf_files = ["sample1.pdf", "sample.pdf", "sample2.pdf"]
sorted_pdf = sorted(pdf_files)
print("Unsorted files: ", pdf_files)
print("sorted files: ", sorted_pdf)

for files in sorted_pdf:                    #loops through every filename in the sorted list i,e sorted_pdf
    writer.append(files)
writer.write("Merged1.pdf")                 #this takes all the pages and creates a merged pdf after contruction it from a binary base


