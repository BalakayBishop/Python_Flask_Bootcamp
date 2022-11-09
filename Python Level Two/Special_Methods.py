# special dunder = double underscore methods
# how does len() know what type and how to return the correct length for the type

class Book():
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
	
	def __repr__(self):  # or str, but Flask doc uses repr
		return f"Title: {self.title}, Author: {self.author}"  # this will override the print method
	
	def __len__(self):
		return f"Length of Book: {self.pages}"  # this will override the len() method
		
my_book = Book('Python 101', 'Blake', 250)

print(my_book)
print(my_book)

length_book = len(my_book)
print(length_book)
