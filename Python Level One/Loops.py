# Loops, for and while
# for loops -> many objects are iterable
#  iterable -> can iterate through

my_it = [1, 2, 3]
for item_name in my_it:
	print(item_name)  # prints 1 2 3
	
seq = [1, 2, 3, 4]
for item in seq:
	print(item ** 2)
	
for num in seq:
	print('Hello')
	
my_str = 'Hello'
for char in my_str:
	print(char)
	
my_dict = {
	'John': 10,
	'Sally': 20,
	'Lisa': 30,
}

for key in my_dict:
	print(key)  # looping through a dictionary will print the key
	print(my_dict[key])  # this will print the key value
	
for key in my_dict:
	print(my_dict[key])  # this will print the key value
	
# while -> will execute a block of code while a condition is true
some_boolean_condition = True
while some_boolean_condition:
	print('do something')
	
	
# Tuple unpacking
# list of tuples
my_pairs = [('a', 1), ('b', 2), ('c', 3)]
print(len(my_pairs))  # prints 3

for (item1, item2) in my_pairs:
	print(item1)
	print(item2)
	# this will unpack the tuple
	
# while loop
i = 1
while i < 5:
	print(f'i is currently {i}')
	i += 1
	
# using range
# range(start, stop, step)
range(0, 5, 1)
for x in range(0, 5):
	print(x)  # 1-4, will print up to but not including 5


result = list(range(0, 11, 2))
print(result)  # this prints the raw list range itself

print('s' in 'askfiohenwnoifhosakskhfioej')  # prints True
print('z' in [1, 2, 3])  # prints False
print(1 in [1, 2, 3])  # prints True