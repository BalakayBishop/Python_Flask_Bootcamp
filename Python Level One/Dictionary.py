# Dictionaries
# Unordered mappings for storing options
# Using a key value pair system
# Allows for grabbing without needing to know the position
# Uses {} with "" : ""

# Dictionary vs List
# Dict = objects are retrieved by a key name, unordered and cannot be sorted
# List = objects are retrieved by an index location, ordered and index-able/slice-able

# easier to find without needing to know the key location
my_diction = {
	'key1': 'value1',
	'key2': 'value2'
}
print(my_diction['key1'])

dict_salary = {
	'John': 20,
	'Sally': 30,
	'Sammy': 15
}
print(dict_salary['Sally'])

dict_salary['Cindy'] = 100  # adding the key Cindy to a value of 100 in the dictionary
print(dict_salary['Cindy'])

dict_salary['John'] = dict_salary['John'] + 40  # this is assigning the old value + 40 to the new value key

# Uncommon to pass dict or list
people = {
	'John': [1, 2, 3],
	'Sally': [40, 10, 30]
}

print(people['John'])  # this will print the list for key John

print(people['Sally'][0])  # grabbing the key of Sally and getting the first item from the list

# Nested dictionary
people = {
	'John': {
		'salary': 30,
		'age': 35
	}
}
print(people['John']['salary'])

d = {
	'k1': '10',
	'k2': '20',
	'k3': '30'
}
print(d.keys())  # return just the keys
print(d.values())  # return the values
print(d.items())  # printing the items = ('k1', 10), ... 