# Functions
# Functions allow us to write blocks of code that can be used over and over again

# Syntax: def function_name (args):
def function_name():
	print("function called")
	
function_name()

# OR

def function_name(name):
	print("one arg function")
	
function_name("Blake")

# Default Param
def function_name(name='Blank'):
	print(name)
	
function_name()  # this will use the default param

# Typical Functions will not print, they will return something
# def add(num1, num2):
# 	print(num1 + num2)
	
# This is to not do
# result = add(1, 2)
# print(result + 10)

# Instead, do this
def add(num1, num2):
	return num1 + num2

result = add(1, 2)
print(result)

# ---------- Function pt. 2 ---------------
# max and min -> return the max or min of args
print(max(1, 2))
print(max([1, 2, 4, 6, 100, 20]))
print(min([1, 2, 4, 6, 100, 20]))

# enumerate
my_list = ['a', 'b', 'c']
for letter in my_list:
	print(letter)  # this will only print a, b, c
	
for letter in enumerate(my_list):
	print(letter)  # this will print tuple pairs of index and item
# OR
for index, item in enumerate(my_list):
	print(item)
	print(f"is at {index}")
	
# .join method '' is the connector for the items
my_list = ['a', 'b', 'c', 'd']
result = ''.join(my_list)
print(result)

# This is okay
# def secret_check(my_string):
# 	if 'secret' in my_string:
# 		return True
# 	else:
# 		return False

# This is better
# def secret_check(my_string):
# 	return 'secret' in my_string

# This would be the best for edge cases
def secret_check(my_string):
	return 'secret' in my_string.lower()
	
result = secret_check("This is a SeCrEt")
print(result)


# Checking a string to replace vowels with letter X
def replace_vowel(my_string):
	output = list(my_string)
	
	for dex, char in enumerate(my_string):
		for vowel in 'aeiou':
			if char.lower() == vowel:
				output[dex] = 'x'
				
	output = ''.join(output)
	return output
		
print(replace_vowel('Sammy'))