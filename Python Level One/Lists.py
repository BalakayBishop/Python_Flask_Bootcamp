# Lists
# Ordered sequences that can hold a variety of object types
# They use [] and comma separated
# Support indexing and slicing

my_list = [1, 2, 3]

print(my_list)
print(len(my_list))

# lists can hold mixed data types
my_list = [100, 20.1, "Hello"]
print(my_list[2])

my_list = ['a', 'b', 'c', 'd']
print(my_list[1])

# Slicing
print(my_list[1:4])  # starting at index one up to but not 4

# Adding to the end = appending
my_list.append('z')

# insert method, 2 params
my_list.insert(0, 'z')

# removing
popped_item = my_list.pop(0)  # assigning and removing the item from the list

print(my_list)
print(popped_item)

# Nested List
my_list1 = [0, 1, 2]
my_list2 = [3, 4, 5]
my_list3 = [6, 7, 8]

mega_list = [my_list1, my_list2, my_list3]
print(len(mega_list))  # this will print 3

print(mega_list[2][1])  # [2] = my_list3 and [1] = 7