# Key data types -> basic building blocks when constructing larger pieces
# Integers -> (int) whole numbers
# Floating Point -> (float) decimal point
# Strings -> (str) ordered sequence of characters
# 	double quotes or single quotes
# Lists -> (list) ordered sequence of objects
# Dictionary -> (dict) unordered with value pair
# Tuples -> (tup) ordered immutable sequence of objects
# Set -> (set) unordered collection of unique objects
# Boolean -> (bool) logical true and false

print("Hello, World!")

# Numbers and Variables
print(2+1)
print(1/2)
print(1-2)
print(3*3)

print(2**3)

# Order of Operation
print(2 + 10 * 10 + 3)

# Use Parenthesis to dictate order of operations
print((2 + 10) * (10 + 3))

# Assigning Variables
	# cannot start with a number, no spaces, and no special chars
	# PEP8 -> names should be lower case

a = 10
print(a)  # prints 10

a = a + a
print(a)  # print 20

puppies = 6
weight = 2

total = puppies * weight  # assigns 12 to total
print(total)  # prints 12

# Dynamic Python
my_dogs = 2
my_dogs = ["Sammy", "Frankie"]

# -------------------------------------------
# Strings
'hello'
"Hello"
"I don't do that"  # single quote is okay because it is wrapped in double quote

# Strings are ordered sequences meaning it can be indexed and sliced
# indexing 0 1 2 3 and reverse indexing 0 -4 -3 -2 -1
my_str = "Hello"
print(my_str[0])  # prints H
print(my_str[-1])  # prints o or last char
print(len(my_str))  # print the length of string

# Slicing = substr
# [start:stop:step] start = starting pos, stop = up to but not inc, step = the size of jump to next char
my_str = "abcdefg"
print(my_str[0:3])
print(my_str[4:7])
print(my_str[0:7:2])

print(my_str[:7])  # this will default start at 0
print(my_str[7:])  # this will default start at 7 and go to end
print(my_str[::])  # this will start at the beginning to the end
print(my_str[::2])  # this will start at the beginning to the end, stepping by 2
print(my_str[::-1])  # this will reverse the string

# String properties and methods
# Strings are immutable
my_str[0] = 'z'  # this is not possible

print(my_str + my_str)  # concat

# Upper case all
print(my_str.upper())

# Lower case all
print(my_str.lower())

# split
print(my_str.split())  # this will split on whitespace to create a list
print(my_str.split('W'))  # split on chars

# Print Formatting
username = "Sammy"
color = "Blue"

print("The {} is favorite is {}".format(username, color))  # this will format and insert these intp the curly

# F string literal
print(f"The {username} chose {color}")