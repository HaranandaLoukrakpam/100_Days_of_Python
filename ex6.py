#Library Management System in python
''' To write a library class with no_of_books and books as two instance variable.
		Write a program to create a library from this library class.
		And show hoe you can print all the books, add a book and get the number of books using diferent methods.
		Show that the program doesn't persist the books after the program is stopped
		'''
class Library:
	def __init__(self):
		self.no_of_books = 0
		self.books = []

	def addbooks(self, book):
		self.books.append(book)
		self.no_of_books = len(self.books)

	def showinfo(self):
		print(f"The library has {self.no_of_books} books")

l1 =  Library()
l1.addbooks("Kafka on the shore")
l1.addbooks("The Intelligent Investor")
l1.addbooks("Norwegian Woods")
l1.showinfo()
