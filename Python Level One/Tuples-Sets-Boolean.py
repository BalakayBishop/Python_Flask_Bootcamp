# Tuples - similar to lists, but immutable
# They are an ordered sequence
# (1, 2, 3)
# for when objects are not to be changed

my_tuple = (1, 2, 3)
print(my_tuple[0])
t = (1, 2, 3, 'a', 2.3)
print(t)
# t[0] = 'NEW' this is not allowed


# Sets - an unordered collection of unique elements
# there can only be one representative of the same object

my_set = set()
my_set.add(1)
print(my_set)  # prints {1}

my_set.add(2)
my_set.add(3)
print(my_set)  # prints {1,2,3}

my_set.add(3)
my_set.add(3)
my_set.add(3)
print(my_set)  # prints {1,2,3}, this happens because they are unique

my_list = [1, 2, 1, 3, 12, 1, 1, 2, 3, 4, 6, 6]
print(set(my_list))  # this will print the unique values in the list

# Booleans - true or false
# must be a capital T or F
a = True
print(a)

b = False
print(b)

c = None  # special keyword placeholder
print(c)